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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Prediko''s public REST API for inventory operations: manage orders and deliveries, read SKUs and procurement suggestions, manage bill-of-materials and production consumption, and sync suppliers and war'
  name: Prediko API
  slug: prediko-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://prediko.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.prediko.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.prediko.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.prediko.io/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.prediko.io/docs/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prediko.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.prediko.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.prediko.io/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prediko.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.prediko.io/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prediko-changelog.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prediko.io/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/prediko-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prediko-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prediko-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prediko-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prediko-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prediko-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prediko-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prediko-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prediko-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/prediko-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.prediko.io/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prediko-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prediko-domain-security.yml
created: '2026-07-17'
description: Prediko is an AI-powered inventory management and planning platform for Shopify D2C and B2B brands, covering demand forecasting, supply and replenishment planning, purchase-order management, raw-materials and bill-of-materials tracking, and multi-location inventory. Prediko exposes a public REST API (https://api.prediko.io/api/v1) authenticated with pk_live_ bearer API keys, letting merchants and integrators manage orders, read SKU stock levels and procurement suggestions, sync suppliers and warehouses, and automate inventory workflows. "Pia" is Prediko's AI inventory agent. The company is backed by Techstars.
image: https://cdn.prod.website-files.com/68ceeb4f2c25c399d42f4726/696653966c56edb6b763849e_predikoinventorymanagement.png
layout: provider
mcp_servers:
- description: ''
  name: Prediko MCP Server
  slug: prediko-mcp-server
modified: '2026-07-20'
name: Prediko
nav: Providers
network: true
overview: 'Prediko publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Inventory Management, Demand Forecasting, Supply Chain, and E-Commerce.


  Prediko''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, changelog, and 18 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 29.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Prediko Authentication
  slug: prediko-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Prediko Domain Security
  slug: prediko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prediko Vulnerability Disclosure
  slug: prediko-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: prediko
tags:
- Company
- Inventory Management
- Demand Forecasting
- Supply Chain
- E-Commerce
- Shopify
- Purchase Orders
- Retail
- Artificial Intelligence
website: https://prediko.io/
---
