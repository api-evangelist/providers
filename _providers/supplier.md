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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://supplier.io
- group: company
  title: ''
  type: About
  url: https://supplier.io/about
- group: company
  title: ''
  type: Blog
  url: https://supplier.io/blog-index
- group: commercial
  title: ''
  type: Pricing
  url: https://supplier.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://supplierio.zendesk.com/
- group: start
  title: ''
  type: Login
  url: https://explorer.supplier.io/Login/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supplier.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supplier.io/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/supplier-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supplier-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supplier-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/supplier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/supplier-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supplier-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supplier-domain-security.yml
created: '2026-07-17'
description: Supplier.io is a supplier intelligence and supplier diversity platform for enterprise procurement teams. It pairs a database of 20M+ suppliers enriched from 450+ sources with spend analytics, diverse- and small-business spend reporting, Tier 2 reporting, supplier discovery and sourcing (Supplier Explorer), economic impact analysis, and Scope 3 carbon/ESG analytics. Backed by Norwest Venture Partners, it serves Fortune 100 procurement organizations. Its only public machine-accessible surface is a published Model Context Protocol (MCP) server (the Royal MCP WordPress plugin) at supplier.io; there is no documented public developer REST API.
image: https://supplier.io/wp-content/uploads/2025/07/SupplierIO-OG.jpg
layout: provider
mcp_servers:
- description: ''
  name: supplier-mcp.yml
  slug: supplier-mcpyml
modified: '2026-07-21'
name: Supplier
nav: Providers
network: true
overview: 'Supplier is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Supply Chain, Supplier Diversity, and Spend Analytics.


  Supplier''s developer surface includes engineering blog, pricing, support, authentication, and 11 more developer resources.'
random_paper: 64
scopes:
- name: Supplier Scopes
  scope_count: 1
  slug: supplier-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 22.5
  delta: 1.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Supplier Authentication
  slug: supplier-authentication
  summary_line: oauth2/apiKey/http · 3 schemes
- kind: domain-security
  name: Supplier Domain Security
  slug: supplier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: supplier
tags:
- Company
- Procurement
- Supply Chain
- Supplier Diversity
- Spend Analytics
- Sourcing
- ESG
- Sustainability
- MCP
website: https://supplier.io
---
