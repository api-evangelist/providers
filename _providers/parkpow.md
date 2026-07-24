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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: ParkPow API for managing parking lots, tracking vehicles, alerts, and enforcement of parking rules.
  name: ParkPow
  slug: parkpow
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parkpow-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://parkpow.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parkpow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parkpow
- group: company
  title: ''
  type: Website
  url: https://parkpow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.parkpow.com/documentation/
created: '2025-02-08'
description: ParkPow is software to manage and enforce parking lots. It lets you track vehicles, get custom alerts, and enforce your parking rules. The ParkPow API documentation requires application access and is not publicly available.
finops:
- name: Parkpow Finops
  service_category: API
  slug: parkpow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parkpow.png
layout: provider
modified: '2026-04-28'
name: ParkPow
nav: Providers
network: true
overview: 'ParkPow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, License Plate Recognition, and Enforcement.


  ParkPow''s developer surface includes engineering blog, documentation, and 4 more developer resources.'
plans:
- name: Parkpow Plans Pricing
  plan_count: 3
  slug: parkpow-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Parkpow Rate Limits
  slug: parkpow-rate-limits
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parkpow/refs/heads/main/screenshots/parkpow-2026-06-20T191414.png
security:
- kind: domain-security
  name: Parkpow Domain Security
  slug: parkpow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parkpow
tags:
- Parking
- License Plate Recognition
- Enforcement
website: https://parkpow.com/
---
