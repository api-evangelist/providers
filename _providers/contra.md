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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Public Api API from Contra — 3 operation(s) for public api.
  name: Contra Public Api API
  slug: contra-public-api-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://contra.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/contra/contra-sdk
- group: company
  title: ''
  type: Blog
  url: https://contra.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://contra.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://contra.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contra.com/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contra.com/policies/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contra
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contra.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/contra-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contra-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/contra-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/contra-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/contra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/contra-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/contra-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contra-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contra-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/contra-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contra-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contra-llms.txt
created: '2026-07-17'
description: Contra is an independent-first, commission-free freelance marketplace and professional network for the jobs and skills of the future, founded in 2019 by Ben Huffman and Gajus Kuizinas and backed by Cowboy Ventures, Unusual Ventures, and NEA. Independents build a portfolio, get discovered, and manage work from inquiry to contract to payment without platform commissions. For developers, Contra exposes a read-only Public API (programs, filters, and expert profiles under https://contra.com/public-api/, authenticated with an X-API-Key header), an attribute-driven Webflow SDK, a React UI-kit, and a hosted, OAuth 2.1-protected Model Context Protocol (MCP) server at https://contra.com/mcp (scope mcp:tools).
image: https://contra.com/static/opengraph-assets/v2/fallbacks/contra-fallback-open-graph-image.png
layout: provider
mcp_servers:
- description: ''
  name: contra-mcp.yml
  slug: contra-mcpyml
modified: '2026-07-18'
name: Contra
nav: Providers
network: true
overview: 'Contra publishes 1 API on the [APIs.io](https://apis.io/) network: Public Api API. Tagged areas include Company, Future Of Work, Freelance Marketplace, Talent, and Hiring.


  Contra''s developer surface includes documentation, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 73
scopes:
- name: Contra Scopes
  scope_count: 1
  slug: contra-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 38.2
  delta: 0.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 30.5
    developer_ergonomics: 38.6
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 37.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contra/refs/heads/main/screenshots/contra-2026-07-25T210337.png
security:
- kind: authentication
  name: Contra Authentication
  slug: contra-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Contra Domain Security
  slug: contra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contra
tags:
- Company
- Future Of Work
- Freelance Marketplace
- Talent
- Hiring
- Professional Network
- Model Context Protocol
- Developer API
website: https://contra.com
---
