---
aid: codex-md
url: https://raw.githubusercontent.com/api-evangelist/codex-md/refs/heads/main/apis.yml
name: CODEX.md
tags:
  - AI Agents
  - AI Copilot
  - Coding Standards
  - Configuration
  - Developer Workflow
  - Memory
  - OpenAI Codex
type: Standard
x-type: standard
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-26'
position: Consumer
description: CODEX.md is a project-level Markdown memory file that the OpenAI Codex CLI loads to bootstrap an AI coding agent with persistent project instructions, coding conventions, build and test commands, and team conventions. The OpenAI Codex CLI now standardizes on AGENTS.md as the canonical filename, with CODEX.md and codex.md historically used and still recognized as fallback configuration filenames. Files are discovered through a three-tier hierarchy spanning the user's home directory, the Git repository root, and the current working directory, with closer files overriding earlier guidance when concatenated into the model prompt.
apis: []
common:
  - type: Specification
    url: https://developers.openai.com/codex/guides/agents-md
  - type: Documentation
    url: https://developers.openai.com/codex/cli
  - type: GitHub
    url: https://github.com/openai/codex
  - type: Landing Page
    url: https://developers.openai.com/codex
x-features:
  - Markdown-based freeform instruction format with no mandated schema
  - Loaded automatically by Codex CLI before any task execution
  - Three-tier discovery (home directory, Git repo root, current directory)
  - Override file convention (AGENTS.override.md / CODEX.override.md)
  - Concatenated merge order with closer files taking precedence
  - Equivalent role to CLAUDE.md (Claude Code) and .cursorrules (Cursor)
  - Designed to encode build commands, test commands, lint rules, and conventions
  - Agentic memory primitive for persistent project context across CLI sessions
x-use-cases:
  - Pin a repository to specific package managers, formatters, and linters
  - Document non-obvious build, test, or migration commands for the agent
  - Establish project-wide coding standards (naming, error handling, imports)
  - Capture team norms (PR descriptions, commit style, branch naming)
  - Restrict the agent from touching protected files or directories
  - Bridge organizational knowledge into AI-assisted development sessions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
