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
    well_known_catalog: true
  schema_version: 0.2
  score: 8.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Signed, service-based JSON API for vendors, developers, and ISVs to integrate with VIPShop's e-commerce systems — orders, commodities/products, inventory, warehouse & logistics, marketplace, multi-cha
  name: VIPShop Open Platform (VOP)
  slug: vipshop-open-platform-vop
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.vip.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vop.vip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vop.vip.com/doccenter/index
- group: docs
  title: ''
  type: APIReference
  url: https://vop.vip.com/apicenter/index
- group: start
  title: ''
  type: GettingStarted
  url: https://vop.vip.com/doccenter/viewdoc/42
- group: operate
  title: ''
  type: Support
  url: https://vop.vip.com/support/index
- group: start
  title: ''
  type: SignUp
  url: https://vop.vip.com/member/console/index
- group: start
  title: ''
  type: Login
  url: https://vop.vip.com/login/loginSystem
- group: operate
  title: ''
  type: ChangeLog
  url: https://vop.vip.com/home#/announcement
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vipshop-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/vipshop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vipshop-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vipshop-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vipshop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vipshop-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vipshop-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vipshop-domain-security.yml
created: '2026-07-17'
description: VIPShop (唯品会, vip.com) is a Chinese e-commerce company specializing in branded flash sales and discount retail, connecting brands with consumers through time-limited special-offer events. For partners it runs VOP (VIPShop Open Platform, vop.vip.com), a developer/open platform that lets vendors, individual developers, and ISVs integrate with VIPShop's e-commerce systems — covering orders, products/commodities, inventory, warehouse and logistics, marketplace, multi-channel and new-retail services. VOP exposes a signed, service-based JSON API through the gw.vipapis.com gateway (with a sandbox.vipapis.com test environment), ships official Java, PHP, and C# SDKs, and authenticates callers with an app-key + secret credential and per-request signature.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vipshop.png
layout: provider
modified: '2026-07-21'
name: VIPShop
nav: Providers
network: true
overview: 'VIPShop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Retail, and Flash Sales.


  VIPShop''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, sandbox, and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 25.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vipshop/refs/heads/main/screenshots/vipshop-2026-09-02T165948.png
security:
- kind: authentication
  name: Vipshop Authentication
  slug: vipshop-authentication
  summary_line: apiKey/signature · 2 schemes
- kind: domain-security
  name: Vipshop Domain Security
  slug: vipshop-domain-security
  summary_line: TLSv1.2
slug: vipshop
tags:
- Company
- Consumer
- E-Commerce
- Retail
- Flash Sales
- Open Platform
- China
- Order
- Inventory
- Logistics
website: http://www.vip.com/
---
