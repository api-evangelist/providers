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
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Programmatic trading and market-data API for global markets, options, futures, crypto and event contracts. Proprietary Protocol Buffers protocol spoken over TCP to a locally run OpenD gateway (default
  name: Futu OpenAPI
  slug: futu-openapi
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://futuholdings.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.futunn.com/futu-api-doc/en/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.futunn.com/futu-api-doc/en/
- group: docs
  title: ''
  type: APIReference
  url: https://static.futunn.com/upload/futu-api/Futu-API-Doc-en-Python.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://openapi.futunn.com/futu-api-doc/en/quick/opend-base.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FutunnOpen
- group: build
  title: ''
  type: Packages
  url: packages/futu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/futu-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/futu-protobuf-index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/futu-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/futu-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/futu-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/futu-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/futu-llms.txt
created: '2026-07-17'
description: 'Futu Holdings Limited (NASDAQ: FUTU), operator of the Futubull and moomoo platforms, is a digital brokerage and wealth-management technology company. Its Futu OpenAPI gives developers programmatic access to real-time and historical market data and to trading across Hong Kong, US, China A-share, Singapore, Malaysia and Japan markets, plus options, futures, cryptocurrency and event (prediction) contracts. Rather than an HTTP/REST API, Futu exposes a proprietary Protocol Buffers (proto2) protocol over TCP through a locally run OpenD gateway, with official Python, Java, C#, C++ and JavaScript SDKs and an official MCP-compatible Agent Skill hub. Backed by Hongshan and Ribbit Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/futu.png
layout: provider
mcp_servers:
- description: Futu does not publish a hosted/remote MCP server. Instead it ships the official "Futu Agent Hub", an MCP-compatible Agent Skill center that connects AI tools (Claude Code, Cursor, Claude Desktop, VS C
  name: Futu MCP Server
  slug: futu-mcp-server
modified: '2026-07-19'
name: Futu
nav: Providers
network: true
overview: 'Futu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Fintech, Brokerage, and Trading.


  Futu''s developer surface includes documentation, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 21.3
  provenance:
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/futu/refs/heads/main/screenshots/futu-2026-07-25T215329.png
security:
- kind: domain-security
  name: Futu Domain Security
  slug: futu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: futu
tags:
- Company
- Technology
- Fintech
- Brokerage
- Trading
- Market Data
- Stocks
- Options
- Investing
- Financial-Services
website: https://futuholdings.com
---
