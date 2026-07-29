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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: CarMD's vehicle API provides access to code definitions, vehicle images, and diagnostics for predicting upcoming vehicle issues.
  name: CarMD Vehicle API
  slug: carmd
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-carmd
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carmd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carmd.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carmd.com/privacy-policy
created: '2024-03-30'
description: CarMD specializes in automotive diagnostics and insights. The CarMD vehicle API is a user-centric and affordable way to access API services for your vehicle. The vehicle data API provides a wide range of services, from displaying code definitions and vehicle images to predicting upcoming issues.
finops:
- name: Carmd Finops
  service_category: API
  slug: carmd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carmd.png
layout: provider
modified: '2026-03-16'
name: CarMD
nav: Providers
network: true
overview: 'CarMD publishes 1 API on the [APIs.io](https://apis.io/) network: Vehicle API. Tagged areas include Automobiles, Cars, Diagnostics, and Vehicles.'
plans:
- name: Carmd Plans Pricing
  plan_count: 3
  slug: carmd-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Carmd Rate Limits
  slug: carmd-rate-limits
score:
  band: emerging
  composite: 27.2
  delta: -3.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 30.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carmd/refs/heads/main/screenshots/carmd-2026-06-20T174011.png
security:
- kind: domain-security
  name: Carmd Domain Security
  slug: carmd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carmd
tags:
- Automobiles
- Cars
- Diagnostics
- Vehicles
website: https://www.carmd.com/
---
