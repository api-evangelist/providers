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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Supplier product catalog retrieval, filtering and upload.
  name: Recurrency E-Procurement API
  slug: recurrency-e-procurement-api
- description: Create, list and retrieve sales orders and quotes.
  name: Recurrency Orders API
  slug: recurrency-orders-api
arazzos:
- description: Discover a supplier, find an item, confirm price, create an order, and read it back.
  name: Recurrency procure-to-pay
  slug: recurrency-procure-to-pay
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Recurrency E-Procurement API
  slug: open-recurrency-e-procurement-api
- collection_type: open
  name: Recurrency E-Procurement Orders API
  slug: open-recurrency-orders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/recurrency-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://recurrency.gitbook.io/recurrency/
- group: docs
  title: ''
  type: Documentation
  url: https://recurrency.gitbook.io/recurrency/
- group: auth
  title: ''
  type: Authentication
  url: authentication/recurrency-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/recurrency-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recurrency-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recurrency-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/recurrency-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/recurrency-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/recurrency-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/recurrency-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/recurrency-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recurrency-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/recurrency-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/recurrency-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/recurrency-procure-to-pay.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recurrency-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recurrency-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/recurrency-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Blog
  url: https://www.recurrency.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recurrency
- group: operate
  title: ''
  type: Support
  url: https://recurrency.gitbook.io/recurrency/support/need-help
- group: start
  title: ''
  type: SignUp
  url: https://www.recurrency.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.recurrency.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.recurrency.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.recurrency.com/
created: '2026-07-17'
description: Recurrency is an AI-powered ERP automation platform for wholesale distributors and B2B suppliers, sitting on top of distribution ERPs to automate and optimize purchasing and sales — forecasting, pricing, reorders and product recommendations across sales, purchasing and operations workflows. Recurrency exposes a public e-procurement REST API (documented on GitBook) for authenticating, retrieving and filtering a supplier's product catalog (items, availability, pricing, locations, groups), uploading catalog data, and creating and managing sales orders and quotes. It also operates a hosted, OAuth-secured MCP server for agent access. Backed by Bessemer Venture Partners.
image: https://storage.googleapis.com/s.mkswft.com/RmlsZTpiNjE4NGRjYy01OGVjLTQ2YWQtOWMyMS0zNjJiZWZiNmYxOTM=/recurrency-dashboard.webp
layout: provider
mcp_servers:
- description: ''
  name: Recurrency MCP Server
  slug: recurrency-mcp-server
modified: '2026-07-21'
name: Recurrency
nav: Providers
network: true
overview: 'Recurrency publishes 2 APIs on the [APIs.io](https://apis.io/) network: E-Procurement API and Orders API. Tagged areas include Company, Ai Ml, ERP, Distribution, and Wholesale.


  Recurrency''s developer surface includes documentation, authentication, sandbox, engineering blog, support, signup flow, and 21 more developer resources.'
random_paper: 19
scopes:
- name: Recurrency Scopes
  scope_count: 4
  slug: recurrency-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 33.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recurrency/refs/heads/main/screenshots/recurrency-2026-08-17T081457.png
security:
- kind: authentication
  name: Recurrency Authentication
  slug: recurrency-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Recurrency Domain Security
  slug: recurrency-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Recurrency Vulnerability Disclosure
  slug: recurrency-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: recurrency
tags:
- Company
- Ai Ml
- ERP
- Distribution
- Wholesale
- eProcurement
- Supply Chain
- Order
website: https://www.recurrency.com/
---
