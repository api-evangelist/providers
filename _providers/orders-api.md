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
  scored_at: '2026-08-10'
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
artifact_total: 7
collections:
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
random_paper: 86
rate_limits:
- limit_count: 5
  name: Orders Api Rate Limits
  slug: orders-api-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.8
    developer_ergonomics: 10.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
