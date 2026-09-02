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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Fake Store Api Agentic Access
  operation_count: 22
  slug: fake-store-api-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 1
apis:
- description: Authentication operations.
  name: Fake Store API Auth API
  slug: fake-store-api-auth-api
- description: Shopping cart operations.
  name: Fake Store API Carts API
  slug: fake-store-api-carts-api
- description: Product catalog operations.
  name: Fake Store API Products API
  slug: fake-store-api-products-api
- description: User account operations.
  name: Fake Store API Users API
  slug: fake-store-api-users-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fake Store Auth API
  slug: open-fake-store-api-auth-api
- collection_type: open
  name: Fake Store Auth Carts API
  slug: open-fake-store-api-carts-api
- collection_type: open
  name: Fake Store Auth Products API
  slug: open-fake-store-api-products-api
- collection_type: open
  name: Fake Store Auth Users API
  slug: open-fake-store-api-users-api
- collection_type: open
  name: Fake Store API
  slug: open-fake-store-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/keikaavousi/fake-store-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/keikaavousi/fake-store-api/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fake-store-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fake-store-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fake-store-api
- group: company
  title: ''
  type: Website
  url: https://fakestoreapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fakestoreapi.com/docs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/keikaavousi/fake-store-api
created: '2025-02-24'
description: Fake Store API is a tool that allows users to access a database of fake products, customers, and orders. Users can use the API to generate test data for their e-commerce applications or to practice integrating with external APIs. The Fake Store API provides a simple and easy-to-use interface for retrieving information such as product details, customer information, and order history.
finops:
- name: Fake Store Api Finops
  service_category: API
  slug: fake-store-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fake-store-api.png
layout: provider
modified: '2026-05-19'
name: Fake Store API
nav: Providers
network: true
overview: 'Fake Store API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Carts API, Products API, and 1 more. Tagged areas include Customers, Fake Data, Order, Product, and Synthetic Data.


  Fake Store API''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Fake Store Api Plans Pricing
  plan_count: 3
  slug: fake-store-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Fake Store Api Rate Limits
  slug: fake-store-api-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.3
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 26.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fake-store-api/refs/heads/main/screenshots/fake-store-api-2026-06-20T181017.png
security:
- kind: domain-security
  name: Fake Store Api Domain Security
  slug: fake-store-api-domain-security
  summary_line: TLSv1.3
slug: fake-store-api
tags:
- Customers
- Fake Data
- Order
- Product
- Synthetic Data
website: https://fakestoreapi.com/
---
