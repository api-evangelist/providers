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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
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
- description: ''
  name: futu-mcp.yml
  slug: futu-mcpyml
modified: '2026-07-19'
name: Futu
nav: Providers
network: true
overview: 'Futu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, FinTech, Brokerage, and Trading.


  Futu''s developer surface includes documentation, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 20.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.0
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- FinTech
- Brokerage
- Trading
- Market Data
- Stocks
- Options
- Investing
- Financial Services
website: https://futuholdings.com
---
