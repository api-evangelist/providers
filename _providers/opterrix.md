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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Opterrix Data API provides real-time and historical weather and hazard data through high-performance endpoints designed for the insurance industry. It supports storm event history with location-ba
  name: Opterrix Data API
  slug: data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opterrix-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opterrix
- group: company
  title: ''
  type: Website
  url: https://www.opterrix.com/
- group: other
  title: ''
  type: Data API
  url: https://www.opterrix.com/data-api
- group: operate
  title: ''
  type: Contact
  url: https://www.opterrix.com/contact
- group: company
  title: ''
  type: About
  url: https://www.opterrix.com/about
created: '2025-02-17'
description: Opterrix delivers real-time and historical weather and natural hazard intelligence to inform and automate key decision-making throughout the insurance value chain. Their high-performance APIs provide property-level data on perils such as wind, hail, precipitation, wildfire, and convective storms, supporting underwriting, claims, portfolio risk management, and moratorium verification workflows.
finops:
- name: Opterrix Finops
  service_category: API
  slug: opterrix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opterrix.png
layout: provider
modified: '2026-04-28'
name: Opterrix
nav: Providers
network: true
overview: Opterrix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hazard Data, Insurance, Insurtech, Risk Intelligence, and Underwriting.
plans:
- name: Opterrix Plans Pricing
  plan_count: 3
  slug: opterrix-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Opterrix Rate Limits
  slug: opterrix-rate-limits
score:
  band: emerging
  composite: 16.6
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opterrix/refs/heads/main/screenshots/opterrix-2026-06-20T191110.png
security:
- kind: domain-security
  name: Opterrix Domain Security
  slug: opterrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opterrix
tags:
- Hazard Data
- Insurance
- Insurtech
- Risk Intelligence
- Underwriting
- Weather Data
website: https://www.opterrix.com/
---
