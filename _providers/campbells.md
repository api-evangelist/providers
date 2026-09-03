---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Campbell's Kitchen API exposes recipe and product data from Campbell's consumer brands — including Campbell's, Swanson, Pace, Prego, and Pepperidge Farm — for use in search-based recipe and produc
  name: Campbell's Kitchen API
  slug: campbells-kitchen-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campbells-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-campbells-company
- group: company
  title: ''
  type: Website
  url: https://www.campbells.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.thecampbellscompany.com/
- group: learn
  title: ''
  type: Recipes
  url: https://www.campbells.com/recipes/
- group: other
  title: ''
  type: Products
  url: https://www.campbells.com/products/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.campbellskitchen.com/
created: '2026-03-21'
description: Campbell's (Campbell Soup Company, now The Campbell's Company) is the consumer brand trusted for generations to provide authentic, flavourful, and readily available soups, meals, and recipes. Alongside its consumer website, Campbell's has historically operated a Campbell's Kitchen Developer API that let developers embed Campbell's, Swanson, Pace, Prego, and Pepperidge Farm recipes, products, and nutrition data into their own web and mobile experiences.
finops:
- name: Campbells Finops
  service_category: Consumer Packaged Goods / Food
  slug: campbells-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campbells.png
layout: provider
modified: '2026-04-23'
name: Campbell's
nav: Providers
network: true
overview: Campbell's publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Food, Consumer Packaged Goods, Recipes, and Brands.
plans:
- name: Campbells Plans Pricing
  plan_count: 0
  slug: campbells-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Campbells Rate Limits
  slug: campbells-rate-limits
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campbells/refs/heads/main/screenshots/campbells-2026-06-20T173911.png
security:
- kind: domain-security
  name: Campbells Domain Security
  slug: campbells-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: campbells
tags:
- Food
- Consumer Packaged Goods
- Recipes
- Brands
website: https://www.campbells.com/
---
