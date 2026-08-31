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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Fyndiq Agentic Access
  operation_count: 16
  slug: fyndiq-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 1
apis:
- description: Create, update, retrieve and delete product articles.
  name: Fyndiq Articles API
  slug: fyndiq-articles-api
- description: Retrieve, fulfil and cancel marketplace orders.
  name: Fyndiq Orders API
  slug: fyndiq-orders-api
artifact_total: 10
collections:
- collection_type: postman
  name: NEW FYNDIQ API
  slug: postman-fyndiq-merchant-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fyndiq Merchant Articles API
  slug: open-fyndiq-articles-api
- collection_type: open
  name: Fyndiq Merchant Articles Orders API
  slug: open-fyndiq-orders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fyndiq-merchant-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.fyndiq.se
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fyndiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fyndiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://merchantapi.fyndiq.com/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/2328684/7185ENK
- group: operate
  title: ''
  type: Support
  url: https://support.fyndiq.se/hc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fyndiq
- group: start
  title: ''
  type: Login
  url: https://merchantcenter.fyndiq.se/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fyndiq.se/fyndiq/policy-och-villkor/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fyndiq.se/fyndiq/policy-och-villkor/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fyndiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fyndiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fyndiq-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fyndiq-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fyndiq-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fyndiq-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fyndiq-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fyndiq-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/fyndiq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fyndiq-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fyndiq-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fyndiq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fyndiq-domain-security.yml
created: '2026-07-17'
description: Fyndiq is Sweden's largest online marketplace for bargains and deals, connecting merchants with millions of deal-seeking consumers across categories from electronics and mobile accessories to home, fashion, beauty and children's goods. Merchants list products while Fyndiq handles the storefront, customer relations and payments. Fyndiq exposes a REST Merchant API that lets sellers upload and manage product articles (create, bulk, price, quantity, delete) and retrieve, fulfil and cancel orders. The API is JSON over HTTPS, secured with HTTP Basic Authentication (Base64 merchantID:token), with a self-contained sandbox environment for integration testing and official Magento, PrestaShop and WooCommerce integration modules. Fyndiq is part of the CDON marketplace group and was originally backed by Northzone.
image: https://fyndiq.se/fyndiq/fyndiq_share.png
layout: provider
mcp_servers:
- description: ''
  name: Fyndiq MCP Server
  slug: fyndiq-mcp-server
modified: '2026-07-19'
name: Fyndiq
nav: Providers
network: true
overview: 'Fyndiq publishes 2 APIs on the [APIs.io](https://apis.io/) network: Articles API and Orders API. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Retail.


  Fyndiq''s developer surface includes documentation, API reference, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 17.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fyndiq/refs/heads/main/screenshots/fyndiq-2026-07-25T215343.png
security:
- kind: authentication
  name: Fyndiq Authentication
  slug: fyndiq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fyndiq Domain Security
  slug: fyndiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fyndiq
tags:
- Company
- Consumer
- Marketplace
- E-Commerce
- Retail
- Product
- Order
- Sweden
website: https://www.fyndiq.se
---
