---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Products Api Agentic Access
  operation_count: 6
  slug: products-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Placing and managing of products placed for products.
  name: Products Products API
  slug: products-api-products-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Products API
  slug: open-products-api-products-api
- collection_type: open
  name: Products API
  slug: open-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/products-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/products-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: http://apievangelist.com
created: '2024-12-29'
description: This is a template APIs.json for a products API, to be used in storytelling, training, and knowledge bases.
finops:
- name: Products Api Finops
  service_category: API
  slug: products-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/products-api.png
layout: provider
modified: '2026-06-23'
name: Products
nav: Providers
network: true
overview: 'Products publishes 1 API on the [APIs.io](https://apis.io/) network: Products API. Tagged areas include Application Programming Interface and Products.


  Products'' developer surface includes authentication and 2 more developer resources.'
plans:
- name: Products Api Plans
  plan_count: 3
  slug: products-api-plans
random_paper: 51
rate_limits:
- limit_count: 5
  name: Products Api Rate Limits
  slug: products-api-rate-limits
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 68.9
    developer_ergonomics: 10.9
    discoverability: 57.4
    governance: 8.3
    operational_transparency: 7.9
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/products-api/refs/heads/main/screenshots/products-api-2026-06-20T192140.png
security:
- kind: authentication
  name: Products Api Authentication
  slug: products-api-authentication
  summary_line: apiKey · 1 scheme
slug: products-api
tags:
- Application Programming Interface
- Products
website: http://apievangelist.com
---
