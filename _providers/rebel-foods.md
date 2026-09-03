---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rebel-foods-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rebelfoods.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rebelfoods.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.rebelfoods.com/reach-out
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rebelfoods.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rebelfoods.com/policy
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/rebel-foods-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rebel-foods-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Rebel Foods builds and runs its own Rebel Operating System for cloud-kitchen workflow and offers it to restaurant chains only through the Rebel Launcher partnership — there is no developer portal, no API reference and no api./developer./docs. subdomain that even resolves, and every /openapi.json, /swagger.json and /.well-known/ path on both www.rebelfoods.com and the EatSure consumer host returns 404.
  evidence:
  - status: 404
    url: https://www.rebelfoods.com/openapi.json
  - status: 404
    url: https://www.rebelfoods.com/.well-known/api-catalog
  - status: 404
    url: https://www.eatsure.com/.well-known/agent-card.json
  - status: <no dns>
    url: https://api.rebelfoods.com/
  - status: <no dns>
    url: https://developer.rebelfoods.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Rebel Foods is an Indian cloud-kitchen operator, headquartered in Mumbai, that describes itself as the world''s largest chain of internet restaurants. It runs a portfolio of delivery-first food brands — Faasos, Behrouz Biryani, Oven Story, Firangi Bake, The Good Bowl, Sweet Truth, Mandarin Oak, The Biryani Life and Lunch Box — out of a shared network of cloud kitchens, and consolidates them for consumers in the EatSure ordering app. Its internal technology platform, the Rebel Operating System, handles kitchen workflow, inventory, demand forecasting, order routing and logistics, and is offered to third-party restaurant chains through the Rebel Launcher partner programme. That platform is a commercial partnership, not a self-serve developer product: as of this profile Rebel Foods publishes no developer portal, no public API documentation, and no machine-readable API contract.'
image: https://www.rebelfoods.com/images/rebelicons/favicon.png
layout: provider
modified: '2026-08-26'
name: Rebel Foods
nav: Providers
network: true
overview: 'Rebel Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Restaurant, Cloud Kitchens, and Food Delivery.


  Rebel Foods'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rebel-foods/refs/heads/main/screenshots/rebel-foods-2026-09-02T153026.png
security:
- kind: domain-security
  name: Rebel Foods Domain Security
  slug: rebel-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rebel-foods
tags:
- Company
- Food and Beverage
- Restaurant
- Cloud Kitchens
- Food Delivery
- Consumer
- Logistics
- India
website: https://www.rebelfoods.com/
---
