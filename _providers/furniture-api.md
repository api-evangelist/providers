---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Furniture Api Agentic Access
  operation_count: 5
  slug: furniture-api-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://furniture-api.fly.dev
  baseurl_source: declared
  description: Product catalog, inventory, and merchandising operations
  name: Furniture API Products API
  slug: furniture-api-products-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Furniture Products API
  slug: open-furniture-api-products-api
- collection_type: open
  name: Furniture API
  slug: open-furniture-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/furniture-api-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://furniture-api.fly.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://furniture-api.fly.dev/
created: '2025-02-24'
description: Furniture API is a service that provides developers with access to a wide range of furniture data and resources through a simple and easy-to-use interface. This API allows users to retrieve information on various types of furniture, including furniture models, prices, availability, and more. Developers can use this data to enhance their applications, websites, and online platforms by incorporating detailed furniture listings, product images, and other relevant information.
finops:
- name: Furniture Api Finops
  service_category: API
  slug: furniture-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/furniture-api.png
layout: provider
modified: '2026-05-19'
name: Furniture API
nav: Providers
network: true
overview: 'Furniture API publishes 1 API on the [APIs.io](https://apis.io/) network: Products API. Tagged areas include Furniture, Product, and E-Commerce.


  Furniture API''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Furniture Api Plans Pricing
  plan_count: 3
  slug: furniture-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Furniture Api Rate Limits
  slug: furniture-api-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/furniture-api/refs/heads/main/screenshots/furniture-api-2026-06-20T181622.png
slug: furniture-api
tags:
- Furniture
- Product
- E-Commerce
website: https://furniture-api.fly.dev/
---
