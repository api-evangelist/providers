---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Fyndiq Agentic Access
  operation_count: 16
  slug: fyndiq-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 1
apis:
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: Create, update, retrieve and delete product articles.
  name: Fyndiq Articles API
  slug: fyndiq-articles-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: Retrieve, fulfil and cancel marketplace orders.
  name: Fyndiq Orders API
  slug: fyndiq-orders-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Carrier Codes API from Fyndiq — 1 operation(s) for carrier codes.
  name: Fyndiq Carrier Codes API
  slug: fyndiq-carrier-codes-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Categories API from Fyndiq — 1 operation(s) for categories.
  name: Fyndiq Categories API
  slug: fyndiq-categories-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Financial Reports API from Fyndiq — 1 operation(s) for financial reports.
  name: Fyndiq Financial Reports API
  slug: fyndiq-financial-reports-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Health API from Fyndiq — 1 operation(s) for health.
  name: Fyndiq Health API
  slug: fyndiq-health-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Jobs API from Fyndiq — 2 operation(s) for jobs.
  name: Fyndiq Jobs API
  slug: fyndiq-jobs-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Merchant API from Fyndiq — 4 operation(s) for merchant.
  name: Fyndiq Merchant API
  slug: fyndiq-merchant-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Sales Funnels API from Fyndiq — 1 operation(s) for sales funnels.
  name: Fyndiq Sales Funnels API
  slug: fyndiq-sales-funnels-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Shipping Configurations API from Fyndiq — 2 operation(s) for shipping configurations.
  name: Fyndiq Shipping Configurations API
  slug: fyndiq-shipping-configurations-api
- baseURL: https://merchants-api.fyndiq.se/api/v1
  baseurl_source: declared
  description: The Statuses API from Fyndiq — 2 operation(s) for statuses.
  name: Fyndiq Statuses API
  slug: fyndiq-statuses-api
artifact_total: 20
collections:
- collection_type: postman
  name: NEW FYNDIQ API
  slug: postman-fyndiq-merchant-api
- collection_type: open
  name: Fyndiq Merchant Articles API
  slug: open-fyndiq-articles-api
- collection_type: open
  name: Fyndiq Merchant Articles Orders API
  slug: open-fyndiq-orders-api
common:
- group: other
  href: https://artifacts.apis.io/fyndiq/capabilities/fyndiq-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fyndiq-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/fyndiq/overlays/fyndiq-merchant-api-overlay.yaml
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
  href: https://artifacts.apis.io/fyndiq/authentication/fyndiq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fyndiq-authentication.yml
- group: design
  href: https://artifacts.apis.io/fyndiq/conventions/fyndiq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fyndiq-conventions.yml
- group: design
  href: https://artifacts.apis.io/fyndiq/errors/fyndiq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fyndiq-problem-types.yml
- group: start
  href: https://artifacts.apis.io/fyndiq/sandbox/fyndiq-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fyndiq-sandbox.yml
- group: design
  href: https://artifacts.apis.io/fyndiq/lifecycle/fyndiq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fyndiq-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fyndiq/data-model/fyndiq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fyndiq-data-model.yml
- group: design
  href: https://artifacts.apis.io/fyndiq/conformance/fyndiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fyndiq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fyndiq/mcp/fyndiq-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fyndiq-mcp.yml
- group: build
  href: https://artifacts.apis.io/fyndiq/packages/fyndiq-packages.yml
  title: ''
  type: Packages
  url: packages/fyndiq-packages.yml
- group: build
  href: https://artifacts.apis.io/fyndiq/packages/fyndiq-packages.yml
  title: ''
  type: SDKs
  url: packages/fyndiq-packages.yml
- group: agent
  href: https://artifacts.apis.io/fyndiq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fyndiq/llms/fyndiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fyndiq-llms.txt
- group: agent
  href: https://artifacts.apis.io/fyndiq/agentic-access/fyndiq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fyndiq-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fyndiq/security/fyndiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fyndiq-domain-security.yml
created: '2026-07-17'
description: Fyndiq is Sweden's largest online marketplace for bargains and deals, connecting merchants with millions of deal-seeking consumers across categories from electronics and mobile accessories to home, fashion, beauty and children's goods. Merchants list products while Fyndiq handles the storefront, customer relations and payments. Fyndiq exposes a REST Merchant API that lets sellers upload and manage product articles (create, bulk, price, quantity, delete) and retrieve, fulfil and cancel orders. The API is JSON over HTTPS, secured with HTTP Basic Authentication (Base64 merchantID:token), with a self-contained sandbox environment for integration testing and official Magento, PrestaShop and WooCommerce integration modules. Fyndiq is part of the CDON marketplace group and was originally backed by Northzone.
image: https://fyndiq.se/fyndiq/fyndiq_share.png
layout: provider
modified: '2026-07-19'
name: Fyndiq
nav: Providers
network: true
overview: 'Fyndiq publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Orders API, Carrier Codes API, and 8 more. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Retail.


  The Fyndiq catalog on APIs.io includes 1 Spectral governance ruleset.


  Fyndiq''s developer surface includes documentation, API reference, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Fyndiq API Rules
  rule_count: 36
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 3
  slug: fyndiq-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 33.5
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 21.4
      derived: 0
      marker_coverage: 78.6
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fyndiq/fyndiq-2026-07-25T215343.png
security:
- kind: authentication
  name: Fyndiq Authentication
  slug: fyndiq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fyndiq Domain Security
  slug: fyndiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Fulfil Fyndiq orders
  slug: fyndiq-fulfill-orders
- name: Manage the Fyndiq product catalog
  slug: fyndiq-manage-product-catalog
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
