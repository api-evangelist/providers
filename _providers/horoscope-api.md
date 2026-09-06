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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Horoscope Api Agentic Access
  operation_count: 3
  slug: horoscope-api-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://freehoroscopeapi.com/api/v1
  baseurl_source: declared
  description: Horoscope predictions by zodiac sign
  name: Horoscope API Horoscope API
  slug: horoscope-api-horoscope-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Horoscope API
  slug: open-horoscope-api-horoscope-api
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
random_paper: 14
rate_limits:
- limit_count: 5
  name: Horoscope Api Rate Limits
  slug: horoscope-api-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Horoscope API API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: horoscope-api-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
