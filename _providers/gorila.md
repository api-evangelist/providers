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
    auth_clarity: true
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
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'B2B REST API for investment-portfolio consolidation and analytics: create portfolios, ingest transactions, and retrieve NAV, P&L, TWR, and IRR time series. Authenticated with a static API key in the A'
  name: GorilaCORE
  slug: gorilacore
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://gorila.com.br
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gorila.com.br/core/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://core.gorila.com.br/docs
- group: docs
  title: ''
  type: APIReference
  url: https://gorila.com.br/core/en/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://gorila.com.br/core/en/docs/quickstart/
- group: operate
  title: ''
  type: ChangeLog
  url: https://gorila.com.br/core/changelog/
- group: company
  title: ''
  type: Blog
  url: https://gorila.com.br/blog/
- group: operate
  title: ''
  type: Support
  url: https://gorila.com.br/contato/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gorilainvest
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gorila.com.br/
- group: start
  title: ''
  type: SignUp
  url: https://view.gorila.com.br/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gorila.com.br/termos-de-uso/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gorila.com.br/politica-de-privacidade/
- group: auth
  title: ''
  type: Authentication
  url: authentication/gorila-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gorila-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gorila-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gorila-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gorila-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gorila-domain-security.yml
created: '2026-07-17'
description: 'Gorila is a Brazilian investment-technology company that consolidates, calculates, and reconciles investment portfolios across every custodian. Its developer product, GorilaCORE, is a B2B REST API that lets financial institutions, fintechs, brokerages, multi-family offices, and advisors build their own investment-consolidation and portfolio-analytics experiences: create portfolios, ingest transactions, and retrieve NAV, P&L, time-weighted return (TWR), and internal-rate-of-return (IRR) time series computed from millions of transactions across hundreds of thousands of products. Gorila is backed by Ribbit Capital.'
image: https://gorila.com.br/img/preview-site.webp
layout: provider
mcp_servers:
- description: ''
  name: gorila-mcp.yml
  slug: gorila-mcpyml
modified: '2026-07-19'
name: Gorila
nav: Providers
network: true
overview: 'Gorila publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investments, Portfolio Management, and Wealth Management.


  Gorila''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, signup flow, and 12 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 30.3
  delta: 0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 30.1
  provenance:
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gorila/refs/heads/main/screenshots/gorila-2026-07-25T220111.png
security:
- kind: authentication
  name: Gorila Authentication
  slug: gorila-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gorila Domain Security
  slug: gorila-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gorila
tags:
- Company
- Fintech
- Investments
- Portfolio Management
- Wealth Management
- Financial Data
- Investment Consolidation
- Brazil
- API
website: https://gorila.com.br
---
