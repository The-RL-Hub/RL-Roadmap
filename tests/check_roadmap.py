"""Check the local structure of the curriculum roadmap."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
RELEASE_MAPS = tuple(f"CHAPTER{chapter:02d}.md" for chapter in range(1, 9))
CHAPTER05_DIAGNOSTICS = (
    "model_metrics.py",
    "trajectory_probability.py",
    "discounting.py",
    "steady_state.py",
    "policy_classes.py",
    "model_comparison.py",
    "coverage.py",
    "policy_comparison.py",
)
EXECUTABLE_EVIDENCE = {
    "CHAPTER02.md": ("standard_bandits.py", "test_standard_bandits.py"),
    "CHAPTER06.md": ("notebook_adapter.py", "reference solver"),
    "CHAPTER07.md": ("Monte_Carlo_Control.ipynb", "test_monte_carlo_control.py"),
    "CHAPTER08.md": ("shared target and update helpers", "TD0_Prediction.ipynb"),
}
CLOSED_GATE_TEXT = {
    "CHAPTER02.md": "add deterministic tests for the core action-selection updates",
    "CHAPTER06.md": "connect the notebook examples to the tested module",
    "CHAPTER07.md": "add an executable on-policy Monte Carlo control lab",
    "CHAPTER08.md": "connect the notebook example to the shared end-signal update helper",
}


def main() -> None:
    missing: list[str] = []
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    for markdown in ROOT.glob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for reference in link_pattern.findall(text):
            parsed = urlsplit(reference)
            if parsed.scheme or parsed.netloc or reference.startswith("#"):
                continue
            target = (markdown.parent / parsed.path).resolve()
            if not target.exists():
                missing.append(f"{markdown.name} -> {reference}")

    assert not missing, "Missing local links:\n" + "\n".join(missing)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    learning_path = readme.split("## Current learning path", 1)[1].split(
        "## Dependency logic", 1
    )[0]
    rows = re.findall(
        r"^\|\s*(\d+)\s*\|",
        learning_path,
        flags=re.MULTILINE,
    )
    assert rows == [str(chapter) for chapter in range(1, 9)], (
        f"Expected ordered chapter rows 1-8, found {rows}"
    )
    assert "Definition of done for a chapter" in readme

    completion_path = ROOT / "COMPLETION.md"
    assert completion_path.exists(), "Missing completion registry"
    assert "](COMPLETION.md)" in readme
    completion = completion_path.read_text(encoding="utf-8")
    completion_rows = dict(
        re.findall(
            r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|",
            completion,
            flags=re.MULTILINE,
        )
    )
    assert list(completion_rows) == [str(chapter) for chapter in range(1, 9)]
    assert set(value.strip() for value in completion_rows.values()) == {"Complete"}
    assert not tuple(ROOT.glob("reviews/*.md")), "Obsolete records exist"

    for release_map in RELEASE_MAPS:
        path = ROOT / release_map
        assert path.exists(), f"Missing release map: {release_map}"
        assert f"]({release_map})" in readme, (
            f"README does not link release map: {release_map}"
        )
        map_text = path.read_text(encoding="utf-8")
        assert "## Learning contract" in map_text
        assert "## Artifact map" in map_text
        assert "## Required invariant checks" in map_text
        assert "## Assessment plan" in map_text
        assert "## Verification questions" in map_text
        assert "## Completion status" in map_text
        chapter = str(int(release_map[7:9]))
        status_match = re.search(
            r"^Status: \*\*(.+)\*\*$",
            map_text,
            flags=re.MULTILINE,
        )
        assert status_match, f"Missing status label in {release_map}"
        assert status_match.group(1) == "Complete"
        assert completion_rows[chapter].strip() == status_match.group(1)
        assert f"]({release_map})" in completion

        expected_evidence = EXECUTABLE_EVIDENCE.get(release_map)
        if expected_evidence:
            missing_evidence = [
                item for item in expected_evidence if item not in map_text
            ]
            assert not missing_evidence, (
                f"{release_map} omits closed evidence: {missing_evidence}"
            )
            assert CLOSED_GATE_TEXT[release_map] not in map_text

        if release_map == "CHAPTER05.md":
            assert "## Diagnostic utility map" in map_text
            missing_diagnostics = [
                name for name in CHAPTER05_DIAGNOSTICS if name not in map_text
            ]
            assert not missing_diagnostics, (
                f"Chapter 5 map omits diagnostics: {missing_diagnostics}"
            )

    print("PASS roadmap integrity checks")


if __name__ == "__main__":
    main()
