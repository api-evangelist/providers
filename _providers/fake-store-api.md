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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Fake Store Api Agentic Access
  operation_count: 22
  slug: fake-store-api-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 4
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
artifact_total: 10
collections:
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
overview: 'Fake Store API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Carts API, Products API, and 1 more. Tagged areas include Customers, Fake Data, Orders, Products, and Synthetic Data.


  Fake Store API''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Fake Store Api Plans Pricing
  plan_count: 3
  slug: fake-store-api-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Fake Store Api Rate Limits
  slug: fake-store-api-rate-limits
score:
  band: emerging
  composite: 25.9
  delta: -8.3
  facets:
    commercial_clarity: 15.8
    contract_quality: 50.4
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
- Orders
- Products
- Synthetic Data
website: https://fakestoreapi.com/
---
