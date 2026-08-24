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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: White-labeled embedded finance REST API for offering business financing — creating businesses, persons, and bank accounts; generating capital offers; creating capital, line-of-credit, and pay-over-tim
  name: Parafin API
  slug: parafin-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parafin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parafin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.parafin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parafin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parafin.com/
- group: company
  title: ''
  type: Blog
  url: https://www.parafin.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parafin.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildparafin
- group: operate
  title: ''
  type: Support
  url: https://www.parafin.com/contact
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parafin-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/parafin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parafin-packages.yml
- group: design
  title: ''
  type: Components
  url: components/parafin-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parafin-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parafin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parafin-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/parafin-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parafin-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parafin-lifecycle.yml
created: '2026-07-17'
description: Parafin is an embedded finance infrastructure company (founded 2020) that lets software platforms, marketplaces, and payment service providers offer capital, spend, and pay-over-time products to the small businesses on their platform. Parafin abstracts the hardest parts of launching a business-financing product — capital sourcing, regulatory and compliance know-how, underwriting and risk modeling, servicing, and collections — behind white-labeled REST APIs and embeddable UI widgets (Parafin Elements) shipped for React, Vue, and Angular. Products include Capital (revenue-based cash advances and flex term loans), Line of Credit, Spend (card and cash account), and Pay Over Time. Platforms integrate via a no-code option (Parafin Lite), low-code embedded Elements, or a custom API build. Notable customers include DoorDash and Mindbody. Backed by GGV Capital, Redpoint Ventures, and Ribbit Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parafin.png
layout: provider
mcp_servers:
- description: Parafin operates a hosted, remote MCP server over Streamable HTTP at https://docs.parafin.com/mcp that exposes documentation search to agents. It is protected by OAuth 2.1 (RFC 8414 authorization-serv
  name: Parafin MCP Server
  slug: parafin-mcp-server
modified: '2026-07-20'
name: Parafin
nav: Providers
network: true
overview: 'Parafin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Embedded Finance, Lending, and Capital.


  Parafin''s developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 13 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.7
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parafin/refs/heads/main/screenshots/parafin-2026-08-07T191409.png
security:
- kind: authentication
  name: Parafin Authentication
  slug: parafin-authentication
  summary_line: oauth2/http-bearer · 2 schemes
- kind: domain-security
  name: Parafin Domain Security
  slug: parafin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parafin
tags:
- Company
- Fintech
- Embedded Finance
- Lending
- Capital
- Payments
- Small Business
- Working Capital
website: https://www.parafin.com/
---
