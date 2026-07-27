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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Horoscope Api Agentic Access
  operation_count: 3
  slug: horoscope-api-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Horoscope predictions by zodiac sign
  name: Horoscope API Horoscope API
  slug: horoscope-api-horoscope-api
artifact_total: 8
collections:
- collection_type: open
  name: Horoscope API
  slug: open-horoscope-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/horoscope-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/horoscope-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://freehoroscopeapi.com
created: '2025-01-07'
description: The Horoscope API offers a versatile solution for accessing daily, weekly, and monthly horoscope predictions tailored to each zodiac sign. With intuitive endpoints, developers can seamlessly integrate astrological insights into their applications, delivering accurate and personalized horoscope data in JSON format.
finops:
- name: Horoscope Api Finops
  service_category: API
  slug: horoscope-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/horoscope-api.png
layout: provider
modified: '2026-05-19'
name: Horoscope API
nav: Providers
network: true
overview: 'Horoscope API publishes 1 API on the [APIs.io](https://apis.io/) network: Horoscope API. Tagged areas include Astrology, Content, Horoscope, and Zodiac.


  The Horoscope API catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Horoscope Api Plans Pricing
  plan_count: 3
  slug: horoscope-api-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Horoscope Api Rate Limits
  slug: horoscope-api-rate-limits
rules:
- name: Horoscope API API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: horoscope-api-rules
score:
  band: thin
  composite: 35.5
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 13.2
    operational_transparency: 31.6
  previous_composite: 32.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/horoscope-api/refs/heads/main/screenshots/horoscope-api-2026-06-20T182833.png
security:
- kind: domain-security
  name: Horoscope Api Domain Security
  slug: horoscope-api-domain-security
  summary_line: TLSv1.3
slug: horoscope-api
tags:
- Astrology
- Content
- Horoscope
- Zodiac
website: https://freehoroscopeapi.com
---
