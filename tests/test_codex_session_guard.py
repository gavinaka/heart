from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CodexSessionGuardTests(unittest.TestCase):
    def test_codex_hook_exists_and_runs_status_guard(self):
        payload = json.loads((ROOT / ".codex" / "hooks.json").read_text(encoding="utf-8"))
        hooks = payload["hooks"]["SessionStart"][0]["hooks"]
        self.assertIn("scripts\\开场同步.py", hooks[0]["command"])

    def test_guard_is_read_only_and_reports_status(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "开场同步.py")],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("[Heart 状态]", result.stdout)
        source = (ROOT / "scripts" / "开场同步.py").read_text(encoding="utf-8")
        self.assertNotIn("subprocess", source)
        self.assertNotIn("write_text", source)

    def test_charter_does_not_claim_clinical_identity_or_cross_workflow_refresh(self):
        text = (ROOT / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn("全球顶尖精神治疗", text)
        self.assertNotIn("唯一例外", text)
        self.assertIn("七 Agent", text)

    def test_startup_context_is_phase_loaded_and_bounded(self):
        entry = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        contract = (ROOT / "governance" / "runtime_contract.md").read_text(encoding="utf-8")
        self.assertIn("@governance/runtime_contract.md", entry)
        self.assertNotIn("@AGENT.md", entry)
        self.assertNotIn("@domains/危机干预协议.md", entry)
        self.assertIn("安全分流", contract)
        self.assertIn("会话分级加载", contract)
        self.assertLessEqual(len((entry + contract).encode("utf-8")), 10_000)


if __name__ == "__main__":
    unittest.main()
