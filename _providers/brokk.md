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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
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
- description: Brokk ships an official MCP (Model Context Protocol) server as part of "bifrost", its multi-language static-analysis engine. It runs as a local stdio server that exposes structured code-analysis tools
  name: Brokk MCP Server
  slug: brokk-mcp-server
modified: '2026-07-18'
name: Brokk
nav: Providers
network: true
overview: 'Brokk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Developer Tools, Code Analysis, and Static Analysis.


  Brokk''s developer surface includes documentation, engineering blog, CLI, changelog, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 13.4
  provenance:
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
- Artificial Intelligence
- Developer Tools
- Code Analysis
- Static Analysis
- MCP
- Coding Agents
- LSP
- Rust
website: https://brokk.ai
---
