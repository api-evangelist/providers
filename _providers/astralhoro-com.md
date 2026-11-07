---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AstralHoro provides horoscope, birth chart, and tarot functionalities via its web platform.
  name: AstralHoro API
  slug: astralhoro-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/astralhoro-com/plans/astralhoro-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astralhoro-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/astralhoro-com/llms/astralhoro-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astralhoro-com-llms.txt
- group: other
  href: https://artifacts.apis.io/astralhoro-com/hosts/astralhoro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astralhoro-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/astralhoro-com/vendors/astralhoro-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astralhoro-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astralhoro.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astralhoro.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://astralhoro.com/guides
- group: auth
  href: https://artifacts.apis.io/astralhoro-com/security/astralhoro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astralhoro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astralhoro.com/
coverage:
  checked: '2026-11-02'
  detail: All attempted OpenAPI discovery URLs on astralhoro.com returned HTTP 403, and no API documentation provides a machine‑readable spec.
  evidence:
  - status: 403
    url: https://astralhoro.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'AstralHoro is an online astrology service that delivers three core tools: a daily horoscope for the Sun sign, a personalized birth chart calculated from the exact birth moment, and a tarot reading for specific questions. The website explains how horoscopes differ from birth charts, offers detailed zodiac sign pages, daily forecasts for all twelve signs, and a variety of tarot draws including three‑card readings and yes/no answers. Users can also generate written reports that combine horoscope and chart data. The platform emphasizes tropical zodiac positions and whole‑sign houses, providing clear guidance on how to interpret the celestial influences.'
image: https://astralhoro.com/favicon.ico
layout: provider
modified: '2026-11-01'
name: AstralHoro
nav: Providers
network: true
overview: 'AstralHoro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Astrology, Horoscope, BirthChart, Tarot, and Web Service.


  AstralHoro''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Astralhoro Com Plans Pricing
  plan_count: 3
  slug: astralhoro-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astralhoro Com Domain Security
  slug: astralhoro-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astralhoro-com
tags:
- Astrology
- Horoscope
- BirthChart
- Tarot
- Web Service
website: https://astralhoro.com/
---
