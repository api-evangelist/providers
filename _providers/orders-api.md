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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Orders Api Agentic Access
  operation_count: 6
  slug: orders-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Placing and managing of orders placed for products.
  name: Orders Orders API
  slug: orders-api-orders-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orders API
  slug: open-orders-api-orders-api
- collection_type: open
  name: Orders API
  slug: open-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orders-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orders-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: http://apievangelist.com
created: '2024-12-29'
description: This is a template APIs.json for a orders API, to be used in storytelling, training, and knowledge bases.
finops:
- name: Orders Api Finops
  service_category: API
  slug: orders-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orders-api.png
layout: provider
modified: '2026-05-19'
name: Orders
nav: Providers
network: true
overview: 'Orders publishes 1 API on the [APIs.io](https://apis.io/) network: Orders API. Tagged areas include Application Programming Interface and Orders.


  Orders'' developer surface includes authentication and 2 more developer resources.'
plans:
- name: Orders Api Plans Pricing
  plan_count: 3
  slug: orders-api-plans-pricing
random_paper: 120
rate_limits:
- limit_count: 5
  name: Orders Api Rate Limits
  slug: orders-api-rate-limits
score:
  band: emerging
  composite: 25.7
  delta: -1.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 63.2
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orders-api/refs/heads/main/screenshots/orders-api-2026-06-20T191202.png
security:
- kind: authentication
  name: Orders Api Authentication
  slug: orders-api-authentication
  summary_line: apiKey · 1 scheme
slug: orders-api
tags:
- Application Programming Interface
- Orders
website: http://apievangelist.com
---
