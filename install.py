#!/usr/bin/env python3
"""Install reviewed configuration files; never installs packages or handles secrets."""
import argparse
import json
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parent


def plan(home, include_home_rules=False, mcp=False):
    pairs = []
    for source_dir, destination in (
        (ROOT / 'config/agent', home / '.pi/agent'),
        (ROOT / 'skills', home / '.agents/skills'),
        (ROOT / 'docs', home / '.pi/docs'),
        (ROOT / 'bin', home / '.local/bin'),
        (ROOT / 'third-party', home / '.pi/third-party'),
    ):
        for source in sorted(source_dir.rglob('*')):
            if source.is_symlink():
                raise ValueError(f'Source symlink not allowed: {source}')
            if source.is_file():
                pairs.append((source, destination / source.relative_to(source_dir)))
    pairs.append((ROOT / 'SKILLS.md', home / '.pi/SKILLS.md'))
    if include_home_rules:
        pairs.append((ROOT / 'global/AGENTS.md', home / 'AGENTS.md'))
    if mcp:
        pairs.append((ROOT / 'config/mcp.example.json', home / '.pi/agent/mcp.json'))
    return pairs


def install(home, dry_run=False, force=False, include_home_rules=False, mcp=False):
    home = home.expanduser().absolute()
    pairs = plan(home, include_home_rules, mcp)
    if not (ROOT / 'config/agent/settings.json').is_file():
        raise ValueError('Incomplete checkout: config/agent/settings.json missing')
    conflicts = []
    for source, dest in pairs:
        if not source.is_file():
            raise ValueError(f'Missing source: {source}')
        # Never follow a link into some other user configuration tree.
        if any(p.is_symlink() for p in (dest, *dest.parents) if p == home or home in p.parents):
            raise ValueError(f'Destination symlink not allowed: {dest}')
        if dest.exists():
            if not dest.is_file():
                raise ValueError(f'Destination is not a file: {dest}')
            conflicts.append(dest)
    if conflicts and not force:
        raise ValueError(f'{len(conflicts)} existing files; no changes made. Review then use --force (backs up overwritten files).')
    if dry_run:
        return f'dry-run: {len(pairs)} files, {len(conflicts)} replacements; target={home}'
    backup = None
    if conflicts:
        backup_root = home / '.pi/config-backups'
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = Path(tempfile.mkdtemp(prefix='pi-agent-config-', dir=backup_root))
        for dest in conflicts:
            target = backup / dest.relative_to(home)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dest, target)
    for source, dest in pairs:
        dest.parent.mkdir(parents=True, exist_ok=True)
        data = source.read_bytes()
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            pass
        else:
            if source.suffix == '.json':
                # Escape unusual home-directory characters correctly in JSON strings.
                text = text.replace('__HOME__', json.dumps(str(home))[1:-1])
                json.loads(text)
            else:
                text = text.replace('__HOME__', str(home))
            data = text.encode('utf-8')
        fd, temp = tempfile.mkstemp(prefix='.pi-install-', dir=dest.parent)
        try:
            with os.fdopen(fd, 'wb') as stream:
                stream.write(data)
            os.chmod(temp, source.stat().st_mode & 0o777)
            os.replace(temp, dest)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
    return f'installed: {len(pairs)} files; target={home}; backup={backup or "none"}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='Target home (use a temporary directory for testing)')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--force', action='store_true', help='Back up and replace colliding files; unrelated files are retained')
    parser.add_argument('--include-home-rules', action='store_true', help='Also install ~/AGENTS.md; affects other agents and projects under home')
    parser.add_argument('--mcp', action='store_true', help='Install optional desktop/browser MCP configuration; requires external tools')
    args = parser.parse_args()
    try:
        print(install(args.home, args.dry_run, args.force, args.include_home_rules, args.mcp))
    except (OSError, ValueError) as error:
        parser.exit(1, f'install failed: {error}\n')


if __name__ == '__main__':
    main()
