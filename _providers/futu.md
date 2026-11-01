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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Programmatic trading and market-data API for global markets, options, futures, crypto and event contracts. Proprietary Protocol Buffers protocol spoken over TCP to a locally run OpenD gateway (default
  name: Futu OpenAPI
  slug: futu-openapi
artifact_total: 5
common:
- group: company
  title: ''
  type: Blog
  url: https://futuholdings.com/en-us/news
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
  href: https://artifacts.apis.io/futu/packages/futu-packages.yml
  title: ''
  type: Packages
  url: packages/futu-packages.yml
- group: build
  href: https://artifacts.apis.io/futu/packages/futu-packages.yml
  title: ''
  type: SDKs
  url: packages/futu-packages.yml
- group: other
  href: https://artifacts.apis.io/futu/grpc/futu-protobuf-index.yml
  title: ''
  type: Protobuf
  url: grpc/futu-protobuf-index.yml
- group: agent
  href: https://artifacts.apis.io/futu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/futu/mcp/futu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/futu-mcp.yml
- group: design
  href: https://artifacts.apis.io/futu/conventions/futu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/futu-conventions.yml
- group: design
  href: https://artifacts.apis.io/futu/conventions/futu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/futu-conventions.yml
- group: auth
  href: https://artifacts.apis.io/futu/security/futu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/futu-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/futu/llms/futu-llms.txt
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
  slug: futu-agent-hub
modified: '2026-10-06'
name: Futu
nav: Providers
network: true
overview: 'Futu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Fintech, Brokerage, and Trading.


  Futu''s developer surface includes engineering blog, documentation, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 15.9
  provenance:
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/futu/futu-2026-07-25T215329.png
security:
- kind: domain-security
  name: Futu Domain Security
  slug: futu-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: futuapi
  slug: futu-futuapi
- name: install-futu-opend
  slug: futu-install-opend
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
- Financial Services
website: https://futuholdings.com
---
