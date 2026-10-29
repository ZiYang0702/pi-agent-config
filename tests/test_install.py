import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.home = Path(self.temp.name) / 'home'

    def tearDown(self):
        self.temp.cleanup()

    def test_dry_run_does_not_write(self):
        self.assertIn('dry-run:', installer.install(self.home, dry_run=True))
        self.assertFalse(self.home.exists())

    def test_fresh_install_and_json(self):
        installer.install(self.home, include_home_rules=True, mcp=True)
        self.assertTrue((self.home / 'AGENTS.md').is_file())
        self.assertTrue((self.home / '.local/bin/quiet-test').is_file())
        for path in (self.home / '.pi/agent').rglob('*.json'):
            json.loads(path.read_text())
            self.assertNotIn('__HOME__', path.read_text())
        self.assertTrue(list((self.home / '.agents/skills').glob('*/SKILL.md')))
        self.assertFalse((self.home / '.pi/agent/auth.json').exists())

    def test_conflicts_fail_before_writes_and_force_backups(self):
        settings = self.home / '.pi/agent/settings.json'
        settings.parent.mkdir(parents=True)
        settings.write_text('{"existing": true}')
        with self.assertRaises(ValueError):
            installer.install(self.home)
        self.assertEqual(settings.read_text(), '{"existing": true}')
        self.assertFalse((self.home / '.agents').exists())
        installer.install(self.home, force=True)
        backups = list((self.home / '.pi/config-backups').glob('*/.pi/agent/settings.json'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), '{"existing": true}')

    def test_optional_files_not_installed_by_default(self):
        installer.install(self.home)
        self.assertFalse((self.home / 'AGENTS.md').exists())
        self.assertFalse((self.home / '.pi/agent/mcp.json').exists())

    def test_symlink_destination_refused(self):
        self.home.mkdir()
        other = Path(self.temp.name) / 'other'
        other.mkdir()
        (self.home / '.pi').symlink_to(other, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.install(self.home, force=True)
        self.assertFalse(list(other.iterdir()))

    def test_restricted_skills_absent(self):
        forbidden = {'docx', 'pdf', 'pptx', 'xlsx', 'chrome-browser', 'built-in-browser', 'computer-use'}
        for path in (ROOT / 'skills').rglob('SKILL.md'):
            self.assertNotIn(path.parent.name, forbidden)


if __name__ == '__main__':
    unittest.main()
