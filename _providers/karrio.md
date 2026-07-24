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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Karrio Agentic Access
  operation_count: 7
  slug: karrio-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 2
apis:
- description: Karrio's headless shipping API for live rating, label generation, package tracking, and carrier integrations.
  name: Karrio Shipping API
  slug: shipping-api
- description: Create, manage, rate, purchase, and void shipments.
  name: Karrio Shipments API
  slug: karrio-shipments-api
artifact_total: 9
collections:
- collection_type: open
  name: Karrio Shipments API
  slug: open-karrio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/karrio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karrio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/karrio-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/karrioapi
- group: company
  title: ''
  type: Website
  url: https://www.karrio.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.karrio.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karrioapi/karrio
- group: company
  title: ''
  type: Blog
  url: https://www.karrio.io/blog
created: '2024-03-30'
description: Karrio is the most flexible way to integrate shipping into your platform. The headless shipping platform enables you to build shipping experiences from live rating, label generation, package tracking, and more.
finops:
- name: Karrio Finops
  service_category: API
  slug: karrio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karrio.png
layout: provider
modified: '2026-03-16'
name: Karrio
nav: Providers
network: true
overview: 'Karrio publishes 1 API on the [APIs.io](https://apis.io/) network: Shipments API. Tagged areas include Label Generation, Logistics, Package Tracking, and Shipping.


  Karrio''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Karrio Plans Pricing
  plan_count: 3
  slug: karrio-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Karrio Rate Limits
  slug: karrio-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.0
    developer_ergonomics: 21.7
    discoverability: 47.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karrio/refs/heads/main/screenshots/karrio-2026-06-20T183922.png
security:
- kind: authentication
  name: Karrio Authentication
  slug: karrio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Karrio Domain Security
  slug: karrio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: karrio
tags:
- Label Generation
- Logistics
- Package Tracking
- Shipping
website: https://www.karrio.io/
---
