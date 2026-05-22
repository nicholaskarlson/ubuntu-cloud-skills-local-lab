from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TestLocalLabContract(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "LICENSE",
            "Makefile",
            "compose.yaml",
            "public/index.html",
            "docs/learning-contract.md",
            "docs/book-series-plan.md",
            "docs/quickstart.md",
            "scripts/check_env.sh",
            ".github/workflows/verify.yml",
            "receipts/samples/docker-version-example.txt",
            "receipts/samples/local-web-smoke-example.txt",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_readme_states_no_paid_cloud_required(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("paid cloud account", text)
        self.assertIn("local-first", text)

    def test_readme_links_quickstart(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[Quickstart](docs/quickstart.md)", text)

    def test_compose_uses_local_web_port(self):
        text = (ROOT / "compose.yaml").read_text(encoding="utf-8")
        self.assertIn('"8080:80"', text)
        self.assertIn("nginx:", text)

    def test_makefile_has_non_docker_verify_and_docker_smoke(self):
        text = (ROOT / "Makefile").read_text(encoding="utf-8")
        self.assertIn("verify:", text)
        self.assertIn("lab-smoke:", text)
        self.assertIn("check-env:", text)

    def test_learning_contract_says_no_paid_docker_features(self):
        text = (ROOT / "docs/learning-contract.md").read_text(encoding="utf-8").lower()
        self.assertIn("docker pro", text)
        self.assertIn("not be required", text)

    def test_quickstart_is_not_truncated(self):
        text = (ROOT / "docs/quickstart.md").read_text(encoding="utf-8")
        self.assertIn("## 8. Stop the lab", text)
        self.assertIn("## Troubleshooting", text)
        self.assertIn("### You want to reset the lab", text)

    def test_github_actions_runs_make_verify(self):
        text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("make verify", text)


if __name__ == "__main__":
    unittest.main()
