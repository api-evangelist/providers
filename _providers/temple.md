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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 10.8
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/temple-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.temple.capital/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/temple-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/temple-mcp.yml
created: '2026-07-17'
description: Temple Capital is a cryptocurrency trading firm founded in 2018 that specializes in the algorithmic trading of liquid digital assets using machine learning technology. The firm has a seven-year live fund track record and manages over $75 million in assets on behalf of a diversified investor base, supported by a team of roughly 25 investment professionals across quantitative research, engineering, and operations. Backed by investors including Pantera Capital and Bain Capital, Temple Capital operates as a quantitative crypto hedge fund and does not currently publish a first-party developer API; its temple.capital marketing site is Wix-hosted and exposes a generic Wix Site MCP endpoint for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/temple.png
layout: provider
mcp_servers:
- description: ''
  name: temple-mcp.yml
  slug: temple-mcpyml
modified: '2026-07-21'
name: Temple
nav: Providers
network: true
overview: Temple is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Cryptocurrency, Digital Assets, and Hedge Fund.
random_paper: 31
score:
  band: minimal
  composite: 7.5
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Temple Domain Security
  slug: temple-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: temple
tags:
- Company
- Crypto
- Cryptocurrency
- Digital Assets
- Hedge Fund
- Algorithmic Trading
- Quantitative Trading
- Machine Learning
- Asset Management
- Investment
website: https://www.temple.capital/
---
