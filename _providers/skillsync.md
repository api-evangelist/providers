---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skillsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skillsync.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skillsync.com/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://skillsync.com/docs/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://skillsync.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://skillsync.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skillsynchq
- group: start
  title: ''
  type: Login
  url: https://skillsync.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skillsync.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skillsync-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/skillsync-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/skillsync-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skillsync-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/skillsync-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skillsync-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/skillsync-conformance.yml
created: '2026-07-17'
description: Skillsync gives AI coding sessions a permanent home — "GitHub for your agent sessions." Developers install the `skl` CLI, sign in once through the browser, and publish a coding session; they can then revisit past work, share the full context behind a change, and turn workflows that worked into reusable skills. The CLI discovers sessions from Claude Code (full support), Codex and OpenCode (beta), and also pi, Campfire, Cursor, Grok, Amp, and Antigravity, and ships a Model Context Protocol server (`skl mcp`) that gives an assistant a long memory over past and published sessions. Skillsync is a Y Combinator (W2026) company; it exposes no public REST API — the CLI and its bundled MCP server are the integration surface.
image: https://skillsync.com/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Skillsync MCP server
  slug: skillsync-mcp-server
modified: '2026-07-21'
name: Skillsync
nav: Providers
network: true
overview: 'Skillsync is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, AI, Agents, and Coding Assistants.


  Skillsync''s developer surface includes documentation, getting-started guide, engineering blog, CLI, authentication, changelog, and 10 more developer resources.'
random_paper: 64
score:
  band: emerging
  composite: 26.0
  delta: 0.5
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 25.5
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Skillsync Authentication
  slug: skillsync-authentication
  summary_line: oauth2-browser · 1 scheme
- kind: domain-security
  name: Skillsync Domain Security
  slug: skillsync-domain-security
  summary_line: TLSv1.3 · HSTS
slug: skillsync
tags:
- Company
- Developer Tools
- AI
- Agents
- Coding Assistants
- Model Context Protocol
- CLI
- Knowledge Management
- Y Combinator
website: https://skillsync.com
---
