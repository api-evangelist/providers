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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://tonk.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tonk.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://tonk-labs.github.io/tonk
- group: start
  title: ''
  type: GettingStarted
  url: https://tonk-labs.github.io/tonk/quickstart.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tonk-labs
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/cHqkYpRE
- group: build
  title: ''
  type: Packages
  url: packages/tonk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tonk-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tonk-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tonk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tonk-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tonk-domain-security.yml
created: '2026-07-17'
description: Tonk, built by Tonk Labs, is an open-source containerized format, host environment, and protocol for multiplayer, local-first software you keep and share like files. A .tonk bundle packages an application together with its data into a single self-contained file that runs anywhere, works offline, and stays under user control. It is built on a document-based virtual file system using Automerge CRDTs, a browser/WebAssembly runtime compiled from Rust, and peer-to-peer synchronization through WebSocket relays. Tonk ships first-party npm client libraries, a CLI, a sync relay, an authentication library, and an MCP worker rather than a hosted REST API. Backed by Electric Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tonk.png
layout: provider
mcp_servers:
- description: First-party Model Context Protocol (MCP) worker service published by Tonk Labs under the @tonk npm scope. It provides MCP support for the Tonk + Obsidian integration (exposing Tonk-managed knowledge/d
  name: Tonk MCP Server
  slug: tonk-mcp-server
modified: '2026-07-21'
name: Tonk
nav: Providers
network: true
overview: 'Tonk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Local-First, CRDT, and Collaboration.


  Tonk''s developer surface includes documentation, getting-started guide, support, CLI, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.1
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tonk Domain Security
  slug: tonk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tonk
tags:
- Company
- Developer Tools
- Local-First
- CRDT
- Collaboration
- Open-Source
- Data Sync
- WebAssembly
website: https://tonk.xyz/
---
