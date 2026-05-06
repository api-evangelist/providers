---
aid: conventions-md
url: https://raw.githubusercontent.com/api-evangelist/conventions-md/refs/heads/main/apis.yml
name: CONVENTIONS.md
x-type: standard
description: CONVENTIONS.md is a Markdown convention popularized by AI pair programming tools such as aider and adopted by AI coding agents like Cursor, Cline, and Claude Code. It documents project-specific coding standards, library preferences, naming conventions, architecture decisions, and development practices in plain natural language so both human developers and AI assistants share the same expectations. The file is loaded into the model context to steer code generation toward project conventions.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Coding
  - Aider
  - Best Practices
  - Coding Standards
  - Conventions
  - Developer Workflow
  - Documentation
  - Markdown
  - Project Configuration
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: conventions-md:format
    name: CONVENTIONS.md Format
    tags:
      - AI Coding
      - Convention
      - Markdown
      - Project Configuration
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aider.chat/docs/usage/conventions.html
    properties:
      - url: https://aider.chat/docs/usage/conventions.html
        type: Documentation
      - url: https://aider.chat/docs/config/aider_conf.html
        type: Documentation
      - url: https://github.com/Aider-AI/aider
        type: Repository
    description: The CONVENTIONS.md format is a free-form Markdown file describing the coding rules an AI coding agent should follow inside a repository. The file is loaded into the chat context, typically in read-only mode, and may be referenced via /read CONVENTIONS.md, the --read CLI flag, or a persistent read entry in .aider.conf.yml. Common content includes preferred libraries, language and version targets, type system rules, lint and format expectations, error handling style, and architectural patterns the project favors.
    x-features:
      - Plain Markdown bullet list of project rules
      - Loaded into AI agent context per session or via config
      - Supports prompt caching when marked read-only
      - Composable alongside CLAUDE.md, .cursor/rules, and copilot-instructions
      - No required schema, allowing each project to define what matters
    x-useCases:
      - Steering AI agents toward preferred libraries and frameworks
      - Documenting type hint, naming, and lint requirements
      - Capturing architecture decisions for AI assisted refactors
      - Aligning human and AI contributors on a single source of conventions
      - Reducing rework caused by AI generated code that misses team norms
  - aid: conventions-md:related-conventions
    name: AI Coding Conventions Ecosystem
    tags:
      - AI Coding
      - Comparison
      - Conventions
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.anthropic.com/en/docs/claude-code/memory
    properties:
      - url: https://docs.anthropic.com/en/docs/claude-code/memory
        type: Documentation
      - url: https://docs.cursor.com/context/rules-for-ai
        type: Documentation
      - url: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
        type: Documentation
      - url: https://aider.chat/docs/usage/conventions.html
        type: Documentation
    description: 'CONVENTIONS.md sits alongside several closely related AI coding conventions. CLAUDE.md is used by Claude Code for repository memory. .cursor/rules and .cursorrules are used by Cursor. .github/copilot- instructions.md is used by GitHub Copilot. Each follows a similar pattern: a Markdown or text file describing repository-specific rules that gets injected into the AI assistant prompt context. CONVENTIONS.md is the most tool-agnostic option and is widely adopted across multiple AI coding agents.'
    x-features:
      - Tool-agnostic file naming compared to CLAUDE.md or .cursorrules
      - Often committed to repo root for visibility to humans and AI
      - Frequently referenced by other agent files such as CLAUDE.md
      - Composable with .editorconfig, .prettierrc, and lint configurations
    x-useCases:
      - Sharing one set of rules across aider, Cursor, Cline, and Claude Code
      - Consolidating coding standards for human and AI contributors
      - Documenting cross-cutting concerns separate from tool-specific config
common:
  - type: Documentation
    url: https://aider.chat/docs/usage/conventions.html
  - type: Documentation
    url: https://docs.anthropic.com/en/docs/claude-code/memory
  - type: Documentation
    url: https://docs.cursor.com/context/rules-for-ai
  - type: Documentation
    url: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
