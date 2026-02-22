#!/usr/bin/env python3
"""
TMT Law Research Pipeline - CLI Entry Point

This script invokes Claude Code CLI to run the multi-agent research pipeline.
Uses your Claude Max subscription (no API key needed).

Usage:
    python -m tmt_researcher "data protection compliance challenges"
    python -m tmt_researcher --topic "AI regulation in India"
    python -m tmt_researcher --setup-notion --parent-page-id <PAGE_ID>
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent


def get_claude_md_path() -> Path:
    """Get path to CLAUDE.md file."""
    return get_project_root() / "CLAUDE.md"


def run_notion_setup(parent_page_id: str) -> int:
    """Run the Notion database setup script."""
    setup_script = get_project_root() / "scripts" / "setup_notion.py"

    cmd = [sys.executable, str(setup_script)]
    if parent_page_id:
        cmd.extend(["--parent-page-id", parent_page_id])

    result = subprocess.run(cmd)
    return result.returncode


def build_research_prompt(topic: str, focus_areas: list[str] | None = None) -> str:
    """Build the research prompt for Claude Code."""

    prompt_parts = [
        f"Research novel TMT law article ideas on the topic: {topic}",
        "",
        "Follow the pipeline defined in CLAUDE.md:",
        "1. Brainstorm 5-7 initial topic hypotheses",
        "2. Run novelty check on each - REJECT any that have been covered before",
        "3. Deep research on ideas that pass novelty check",
        "4. Validate all citations and legal accuracy",
        "5. Final review - apply the Bhatia bar",
        "",
        "Quality requirements:",
        "- Depth >>> surface-level insight",
        "- Novelty >>> quantity",
        "- Every claim must be cited",
        "- REJECT most ideas - only truly original ones should pass",
        "",
        "Output each approved idea in the structured format from CLAUDE.md.",
    ]

    if focus_areas:
        prompt_parts.insert(1, f"Focus areas: {', '.join(focus_areas)}")

    return "\n".join(prompt_parts)


def run_pipeline(topic: str, focus_areas: list[str] | None = None) -> int:
    """Run the research pipeline via Claude Code CLI."""

    prompt = build_research_prompt(topic, focus_areas)
    project_root = get_project_root()

    # Build Claude Code command
    cmd = [
        "claude",
        "--print",  # Print conversation to stdout
        "--dangerously-skip-permissions",  # Allow all tools (you're already authenticated)
        "-p", prompt,
    ]

    print(f"Starting TMT research pipeline for: {topic}")
    print("=" * 60)
    print()

    # Run from project root so CLAUDE.md is picked up
    result = subprocess.run(
        cmd,
        cwd=str(project_root),
    )

    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="TMT Law Research Pipeline - Generate novel article ideas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python -m tmt_researcher "data protection challenges"
    python -m tmt_researcher --topic "AI regulation" --focus technology
    python -m tmt_researcher --setup-notion --parent-page-id abc123

This tool uses your Claude Max subscription via Claude Code CLI.
No API key needed - just be logged into Claude Code.
        """,
    )

    parser.add_argument(
        "topic",
        nargs="?",
        help="Research topic (e.g., 'data protection compliance')",
    )

    parser.add_argument(
        "-t", "--topic",
        dest="topic_flag",
        help="Research topic (alternative to positional argument)",
    )

    parser.add_argument(
        "-f", "--focus",
        action="append",
        dest="focus_areas",
        choices=["technology", "media", "telecommunications"],
        help="Focus on specific TMT area(s)",
    )

    parser.add_argument(
        "--setup-notion",
        action="store_true",
        help="Set up Notion database instead of running research",
    )

    parser.add_argument(
        "--parent-page-id",
        help="Notion page ID for database creation (use with --setup-notion)",
    )

    args = parser.parse_args()

    # Handle Notion setup
    if args.setup_notion:
        return run_notion_setup(args.parent_page_id)

    # Get topic from either positional or flag argument
    topic = args.topic or args.topic_flag

    if not topic:
        parser.print_help()
        print("\nError: Please provide a research topic")
        return 1

    # Check if Claude Code is available
    try:
        subprocess.run(
            ["claude", "--version"],
            capture_output=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Claude Code CLI not found or not working")
        print("Please ensure you have Claude Code installed and are logged in:")
        print("  https://claude.ai/code")
        return 1

    # Run the pipeline
    return run_pipeline(topic, args.focus_areas)


if __name__ == "__main__":
    sys.exit(main())
