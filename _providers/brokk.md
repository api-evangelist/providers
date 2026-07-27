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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 15.4
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brokk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brokk.ai
- group: docs
  title: ''
  type: Documentation
  url: https://brokkai.github.io/bifrost/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BrokkAi
- group: company
  title: ''
  type: Blog
  url: https://brokk.ai/blog/
- group: build
  title: ''
  type: Packages
  url: packages/brokk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brokk-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brokk-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/brokk-cli.yml
- group: design
  title: ''
  type: Components
  url: components/brokk-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brokk-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brokk-well-known.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brokk-changelog.yml
created: '2026-07-17'
description: Brokk (Brokk, Inc.) builds AI tooling for large codebases. Rather than a hosted REST API, Brokk ships open-source developer tools centered on "bifrost" — a Tree-sitter-backed multi-language static-analysis engine that gives coding agents structured code intelligence (symbols, definitions, references, call graphs, usage analysis) across 12 languages. Bifrost runs as a CLI, a workspace-aware language server (LSP), and a stdio MCP server, and is published to crates.io (brokk-bifrost) and PyPI (brokk-bifrost-searchtools). The company, founded by Jonathan Ellis (Apache Cassandra / DataStax) and backed by Mayfield, also ships the core Brokk application, the brokk-cli launcher, and Agent Client Protocol (ACP) tooling (anvil, mjolnir).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brokk.png
layout: provider
mcp_servers:
- description: ''
  name: brokk-mcp.yml
  slug: brokk-mcpyml
modified: '2026-07-18'
name: Brokk
nav: Providers
network: true
overview: 'Brokk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Developer Tools, Code Analysis, and Static Analysis.


  Brokk''s developer surface includes documentation, engineering blog, CLI, changelog, and 9 more developer resources.'
random_paper: 61
score:
  band: emerging
  composite: 16.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brokk/refs/heads/main/screenshots/brokk-2026-07-25T203947.png
security:
- kind: domain-security
  name: Brokk Domain Security
  slug: brokk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brokk
tags:
- Company
- AI
- Developer Tools
- Code Analysis
- Static Analysis
- MCP
- Coding Agents
- LSP
- Rust
website: https://brokk.ai
---
