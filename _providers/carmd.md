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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
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
random_paper: 72
rate_limits:
- limit_count: 5
  name: Carmd Rate Limits
  slug: carmd-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: -3.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
