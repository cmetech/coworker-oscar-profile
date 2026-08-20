from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "oscar-admin-qa",
    "oscar-install-upgrade",
    "oscar-platform-operations",
    "oscar-alert-mappings",
    "oscar-alert-rules",
    "oscar-correlation-rules",
    "oscar-vmalert-rules",
    "oscar-troubleshooting",
}
FORBIDDEN_NAMES = {
    ".env",
    "auth.json",
    "state.db",
    "hermes_state.db",
    "response_store.db",
}


def read(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


class DistributionContractTests(unittest.TestCase):
    def test_manifest_is_rooted_named_and_explicitly_owned(self) -> None:
        manifest = read("distribution.yaml")
        parsed = yaml.safe_load(manifest)
        self.assertIsInstance(parsed, dict)
        self.assertEqual("oscar", parsed["name"])
        self.assertEqual("0.2.0", parsed["version"])
        self.assertRegex(manifest, r"(?m)^name:\s*oscar\s*$")
        self.assertRegex(manifest, r"(?m)^version:\s*0\.2\.0\s*$")
        self.assertIn("distribution_owned:", manifest)
        for owned in ("SOUL.md", "config.yaml", "skills/", "README.md"):
            self.assertIn(f"  - {owned}", manifest)

    def test_profile_assets_exist(self) -> None:
        for relative in ("SOUL.md", "config.yaml", "README.md", "LICENSE"):
            self.assertTrue((REPO / relative).is_file(), relative)

    def test_profile_contract_is_evidence_and_confirmation_driven(self) -> None:
        soul = read("SOUL.md").lower()
        for phrase in (
            "glean",
            "confluence",
            "canonical oscar documentation",
            "code-present",
            "service-running",
            "operator-enabled",
            "explicit confirmation",
            "cite",
        ):
            self.assertIn(phrase, soul)

    def test_no_secret_or_runtime_files_are_tracked(self) -> None:
        found = {
            path.name
            for path in REPO.rglob("*")
            if path.is_file() and ".git" not in path.parts
        }
        self.assertTrue(FORBIDDEN_NAMES.isdisjoint(found), found & FORBIDDEN_NAMES)


class SkillContractTests(unittest.TestCase):
    def test_required_skill_set_exists(self) -> None:
        skills_dir = REPO / "skills" / "oscar"
        actual = {path.name for path in skills_dir.iterdir() if path.is_dir()}
        self.assertEqual(EXPECTED_SKILLS, actual)

    def test_each_skill_has_discoverable_frontmatter_and_safety_contract(self) -> None:
        for name in sorted(EXPECTED_SKILLS):
            with self.subTest(skill=name):
                text = read(f"skills/oscar/{name}/SKILL.md")
                metadata = frontmatter(text)
                self.assertEqual(name, metadata.get("name"))
                self.assertTrue(metadata.get("description", "").startswith("Use when"))
                self.assertIn("## Workflow", text)
                self.assertIn("## Safety", text)

    def test_scaffold_contains_no_unfinished_markers(self) -> None:
        marker = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)
        for skill_file in (REPO / "skills" / "oscar").glob("*/SKILL.md"):
            with self.subTest(skill=skill_file.parent.name):
                self.assertIsNone(marker.search(skill_file.read_text(encoding="utf-8")))


class OperatorExperienceTests(unittest.TestCase):
    def test_readme_documents_remote_windows_lifecycle(self) -> None:
        readme = read("README.md")
        self.assertIn("loop24 profile install github.com/cmetech/coworker-oscar-profile", readme)
        self.assertIn("loop24 profile info oscar", readme)
        self.assertIn("loop24 profile update oscar", readme)
        self.assertIn("loop24 profile delete oscar", readme)
        self.assertIn(r"%LOCALAPPDATA%\loop24\profiles\oscar", readme)
        self.assertIn("Test-ProfileInstall.ps1", readme)
        self.assertIn(
            "cmetech/coworker-oscar-profile/skills/oscar/oscar-vmalert-rules",
            readme,
        )

    def test_windows_smoke_test_uses_only_disposable_profile(self) -> None:
        script = read("scripts/Test-ProfileInstall.ps1")
        self.assertIn("Get-Command loop24", script)
        self.assertIn("oscar-install-smoke", script)
        self.assertIn("--name", script)
        self.assertIn("profile info", script)
        self.assertRegex(script, r'"profile",\s*"delete",\s*\$profileName')
        self.assertIn("finally", script)
        self.assertNotRegex(script, r"profile delete\s+oscar(?:\s|$)")


if __name__ == "__main__":
    unittest.main()
