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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Qogita's REST API for retailers and integration partners on api.qogita.com, covering catalog, ordering, and fulfilment workflows. Documented via the developer portal (hosted on Notion).
  name: Qogita API
  slug: qogita-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.qogita.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.qogita.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.qogita.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qogita.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.qogita.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.qogita.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qogita.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qogita.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.qogita.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qogita
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qogita-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qogita-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qogita-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qogita-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qogita-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qogita-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qogita-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qogita-domain-security.yml
created: '2026-07-17'
description: Qogita is Europe's B2B wholesale marketplace for the health and beauty sector, connecting retailers to a combined catalog of more than 500 suppliers and distributors and over 10,000 brands with guaranteed authenticity for EU and UK retail. Qogita handles sourcing, ordering, payment, and logistics across borders, and exposes a REST API at api.qogita.com (documented at developers.qogita.com) alongside a hosted, OAuth-protected Model Context Protocol (MCP) server for agent access. The company is backed by Accel and Bessemer Venture Partners.
image: https://www.qogita.com/
layout: provider
mcp_servers:
- description: ''
  name: qogita-mcp.yml
  slug: qogita-mcpyml
modified: '2026-07-20'
name: Qogita
nav: Providers
network: true
overview: 'Qogita publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Wholesale, Marketplace, and Health and Beauty.


  Qogita''s developer surface includes documentation, engineering blog, support, authentication, and 14 more developer resources.'
random_paper: 15
scopes:
- name: Qogita Scopes
  scope_count: 1
  slug: qogita-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 24.8
  delta: -4.8
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Qogita Authentication
  slug: qogita-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Qogita Domain Security
  slug: qogita-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qogita
tags:
- Company
- Ecommerce
- Wholesale
- Marketplace
- Health and Beauty
- B2B
- Retail
- Distribution
website: https://www.qogita.com/
---
