---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lowes Agentic Access
  operation_count: 3
  slug: lowes-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Check product availability and stock levels.
  name: Lowe's Inventory API
  slug: lowes-inventory-api
- description: Search and retrieve product information.
  name: Lowe's Products API
  slug: lowes-products-api
- description: Access store location and information data.
  name: Lowe's Stores API
  slug: lowes-stores-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lowe's Product Inventory API
  slug: open-lowes-inventory-api
- collection_type: open
  name: Lowe's Product API
  slug: open-lowes-product-api
- collection_type: open
  name: Lowe's Product Inventory Products API
  slug: open-lowes-products-api
- collection_type: open
  name: Lowe's Product Inventory Stores API
  slug: open-lowes-stores-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lowes-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lowes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lowes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lowes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lowes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lowes
- group: start
  title: ''
  type: Portal
  url: https://portal.apim.lowes.com/
- group: company
  title: ''
  type: Website
  url: https://www.lowes.com/
- group: start
  title: ''
  type: Signup
  url: https://portal.apim.lowes.com/signup
- group: start
  title: ''
  type: Login
  url: https://portal.apim.lowes.com/signin
created: '2026-03-21'
description: Lowe's Companies, Inc. is an American retail company specializing in home improvement. Lowe's operates a developer portal built on Microsoft Azure API Management that provides partners and developers access to product, inventory, pricing, and store APIs for integration with Lowe's retail operations. Discover APIs, learn how to use them, try them out interactively, and sign up to acquire keys.
finops:
- name: Lowes Finops
  service_category: Retail
  slug: lowes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lowes.png
layout: provider
modified: '2026-05-19'
name: Lowe's
nav: Providers
network: true
overview: 'Lowe''s publishes 3 APIs on the [APIs.io](https://apis.io/) network: Inventory API, Products API, and Stores API. Tagged areas include E-Commerce, Home Improvement, Product, Retail, and Fortune 100.


  Lowe''s'' developer surface includes authentication, developer portal, signup flow, and 7 more developer resources.'
plans:
- name: Lowes Plans Pricing
  plan_count: 1
  slug: lowes-plans-pricing
press:
- date: '2026-05-25'
  title: Lowe's puts project expertise into every hand
  url: https://openai.com/index/lowes/
- date: '2026-05-25'
  title: Lowe's Boosts Pro Efficiency with AI-Driven Material Lists ...
  url: https://www.prnewswire.com/news-releases/lowes-boosts-pro-efficiency-with-ai-driven-material-lists-a-new-tool-that-delivers-product-quotes-in-minutes-302778296.html
- date: '2026-05-25'
  title: Chandhu Nair
  url: https://corporate.lowes.com/who-we-are/lowes-leadership/senior-leadership/chandhu-nair
- date: '2026-05-25'
  title: Lowe's Launches First Ai-Powered Home Improvement ...
  url: https://corporate.lowes.com/newsroom/press-releases/lowes-launches-first-ai-powered-home-improvement-virtual-advisor-03-05-25
- date: '2026-05-25'
  title: Lowe's deploys First at-scale AI assistant for Retail ...
  url: https://corporate.lowes.com/newsroom/press-releases/lowes-deploys-first-scale-ai-assistant-retail-associates-05-05-25
random_paper: 8
rate_limits:
- limit_count: 1
  name: Lowes Rate Limits
  slug: lowes-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 19.7
    commercial_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lowes/refs/heads/main/screenshots/lowes-2026-06-20T184736.png
security:
- kind: authentication
  name: Lowes Authentication
  slug: lowes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lowes Domain Security
  slug: lowes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lowes
tags:
- E-Commerce
- Home Improvement
- Product
- Retail
- Fortune 100
website: https://www.lowes.com/
---
