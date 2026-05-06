---
aid: claude-md
name: CLAUDE.md
url: https://raw.githubusercontent.com/api-evangelist/claude-md/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-23'
type: Standard
access: Open
position: Standard
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - Claude Code
  - Coding Standards
  - Configuration
  - Developer Workflow
  - Markdown
  - Memory
  - Project Configuration
  - Standard
description: CLAUDE.md is the markdown-based project memory format used by Anthropic's Claude Code CLI to give the model persistent, session-spanning instructions about a codebase. CLAUDE.md files are plain markdown that Claude Code loads at the start of every session by walking up the directory tree from the working directory, picking up files at organization-managed, user (~/.claude/CLAUDE.md), project (./CLAUDE.md or ./.claude/CLAUDE.md), and local (./CLAUDE.local.md) scopes. The format supports an @path import syntax for composing files together (up to five hops, relative or absolute), HTML block comments that are stripped before injection, an AGENTS.md import pattern for compatibility with other agents, and a complementary .claude/rules/ directory of path-scoped markdown rules with YAML frontmatter. CLAUDE.md is the human-authored counterpart to Claude Code's auto memory at ~/.claude/projects/<project>/memory/MEMORY.md, which Claude writes itself.
apis: []
artifacts:
  - aid: claude-md:format
    name: CLAUDE.md File Format
    tags:
      - Format
      - Markdown
      - Memory
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://code.claude.com/docs/en/memory
    properties:
      - url: https://code.claude.com/docs/en/memory
        type: Specification
      - url: https://code.claude.com/docs/en/memory#claude-md-files
        type: Documentation
    description: Plain-markdown file containing project, user, or organization-wide instructions that Claude Code loads as a user message at session start. Recommended size is under 200 lines per file with concrete, verifiable instructions and markdown headers and bullets for structure.
  - aid: claude-md:imports
    name: CLAUDE.md @path Imports
    tags:
      - Composition
      - Imports
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://code.claude.com/docs/en/memory#import-additional-files
    properties:
      - url: https://code.claude.com/docs/en/memory#import-additional-files
        type: Documentation
    description: The @path/to/file syntax expands and inlines another file into a CLAUDE.md at load time. Imports support relative and absolute paths, recursive imports up to five hops, and are commonly used to pull in README, AGENTS.md, package.json, or shared instruction files from a user's home directory.
  - aid: claude-md:scopes
    name: CLAUDE.md Scope Hierarchy
    tags:
      - Hierarchy
      - Scope
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files
    properties:
      - url: https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files
        type: Documentation
    description: 'CLAUDE.md resolves through four scopes: managed policy (organization-wide, distributed via MDM/Group Policy), user (~/.claude/CLAUDE.md), project (./CLAUDE.md or ./.claude/CLAUDE.md checked into source control), and local (./CLAUDE.local.md, gitignored). All discovered files are concatenated into context rather than overriding each other.'
  - aid: claude-md:rules
    name: .claude/rules/ Directory
    tags:
      - Path-Scoped
      - Rules
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/
    properties:
      - url: https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/
        type: Documentation
    description: The .claude/rules/ directory holds modular markdown rule files with optional YAML frontmatter declaring a paths list of glob patterns. Rules without paths load at launch alongside CLAUDE.md; path-scoped rules load only when Claude reads matching files.
  - aid: claude-md:auto-memory
    name: Claude Code Auto Memory
    tags:
      - Auto Memory
      - MEMORY.md
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://code.claude.com/docs/en/memory#auto-memory
    properties:
      - url: https://code.claude.com/docs/en/memory#auto-memory
        type: Documentation
    description: Auto memory is the machine-managed companion to CLAUDE.md. Claude Code maintains ~/.claude/projects/<project>/memory/MEMORY.md as a concise index plus topic files written and read by the agent across sessions. The first 200 lines or 25 KB of MEMORY.md load at session start.
common:
  - type: Specification
    url: https://code.claude.com/docs/en/memory
  - type: Documentation
    url: https://code.claude.com/docs/en/memory#claude-md-files
  - type: Vendor
    url: https://www.anthropic.com/
  - type: Tool
    url: https://code.claude.com/
  - type: Settings Reference
    url: https://code.claude.com/docs/en/settings
  - type: Hooks Reference
    url: https://code.claude.com/docs/en/hooks
  - type: JSON-LD
    url: json-ld/claude-md-context.jsonld
  - type: Naftiko Capabilities
    url: capabilities/claude-md-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
