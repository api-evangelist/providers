---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: docs
  title: ''
  type: Specification
  url: https://code.claude.com/docs/en/memory
- group: docs
  title: ''
  type: Documentation
  url: https://code.claude.com/docs/en/memory#claude-md-files
- group: other
  title: ''
  type: Vendor
  url: https://www.anthropic.com/
- group: build
  title: ''
  type: Tools
  url: https://code.claude.com/
- group: docs
  title: ''
  type: Settings Reference
  url: https://code.claude.com/docs/en/settings
- group: docs
  title: ''
  type: Hooks Reference
  url: https://code.claude.com/docs/en/hooks
- group: design
  title: ''
  type: JSONLD
  url: json-ld/claude-md-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://claude.com/llms.txt
created: '2025-01-01'
description: CLAUDE.md is the markdown-based project memory format used by Anthropic's Claude Code CLI to give the model persistent, session-spanning instructions about a codebase. CLAUDE.md files are plain markdown that Claude Code loads at the start of every session by walking up the directory tree from the working directory, picking up files at organization-managed, user (~/.claude/CLAUDE.md), project (./CLAUDE.md or ./.claude/CLAUDE.md), and local (./CLAUDE.local.md) scopes. The format supports an @path import syntax for composing files together (up to five hops, relative or absolute), HTML block comments that are stripped before injection, an AGENTS.md import pattern for compatibility with other agents, and a complementary .claude/rules/ directory of path-scoped markdown rules with YAML frontmatter. CLAUDE.md is the human-authored counterpart to Claude Code's auto memory at ~/.claude/projects/<project>/memory/MEMORY.md, which Claude writes itself.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/claude-md.png
jsonld:
- class_count: 14
  name: Claude Md Context
  property_count: 0
  slug: claude-md-context
layout: provider
modified: '2026-04-23'
name: CLAUDE.md
nav: Providers
network: true
overview: 'CLAUDE.md is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Claude Code, Coding Standards, Configuration, and Developer Workflow.


  The CLAUDE.md catalog on APIs.io includes 1 JSON-LD context.


  CLAUDE.md''s developer surface includes documentation, tooling, and 6 more developer resources.'
random_paper: 76
score:
  band: minimal
  composite: 10.0
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/claude-md/refs/heads/main/screenshots/claude-md-2026-06-20T174448.png
slug: claude-md
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
---
