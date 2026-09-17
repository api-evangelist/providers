---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiden-auto/refs/heads/main/security/aiden-auto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiden-auto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidenauto.com/
- group: company
  title: ''
  type: About
  url: https://aidenauto.com/about
- group: operate
  title: ''
  type: Contact
  url: https://aidenauto.com/contact
- group: company
  title: ''
  type: Blog
  url: https://aidenauto.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidenauto.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidenauto.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aidenauto/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiden-auto/refs/heads/main/llms/aiden-auto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiden-auto-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiden-auto/refs/heads/main/plans/aiden-auto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiden-auto-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiden-auto/refs/heads/main/rate-limits/aiden-auto-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiden-auto-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: 'AiDEN Auto markets "AiDEN APIs" and the AiDEN Portal as steps inside its partner onboarding flow on https://aidenauto.com/partners, but publishes no reference for them: docs.aidenauto.com, developer.aidenauto.com and api.aidenauto.com do not resolve, /developers, /docs and /api on the marketing site 404, and every route to the platform is a "Request A Demo" form.'
  evidence:
  - status: 200
    url: https://aidenauto.com/partners
  - status: 404
    url: https://aidenauto.com/developers
  - status: 404
    url: https://aidenauto.com/openapi.json
  - status: 404
    url: https://aidenauto.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-14'
description: AiDEN Auto (Aiden Automotive Inc.) is a connected-vehicle software company founded in 2021 by former Volvo Cars connected-services and infotainment engineers, with offices in San Ramon, California and Gothenburg, Sweden. Its software-only platform runs natively on Android Automotive OS (AAOS) infotainment head units and lets automakers, fleets and third-party service providers deliver in-cab mobility services — tolling, parking, fueling and charging, payments, insurance, roadside assistance, maintenance and regulatory compliance such as Poland's SENT cross-border freight reporting — without a phone, a downloaded app, or a bespoke per-OEM integration. AiDEN brokers real-time vehicle signals (fuel level, tire pressure, battery state, engine data, location) to partner backends under an application-level, GDPR/CCPA-aligned consent model, and partners configure signal access and triggers through the AiDEN Portal rather than proprietary OEM APIs. The company is a COVESA member, has
  raised roughly $11M (a $6.1M oversubscribed seed announced February 2025), holds three patents covering in-vehicle consent, payments and data sharing, and works with Volvo Trucks, HERE Technologies and IF Insurance among others.
image: https://cdn.prod.website-files.com/693738baf4658f638a869c9c/695d901b3736d6cb2099ca6e_aiden-p.png
layout: provider
modified: '2026-09-14'
name: Aiden Auto
nav: Providers
network: true
overview: 'Aiden Auto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Connected Vehicles, Mobility, and Telematics.


  Aiden Auto''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Aiden Auto Plans Pricing
  plan_count: 0
  slug: aiden-auto-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aiden Auto Rate Limits
  slug: aiden-auto-rate-limits
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiden Auto Domain Security
  slug: aiden-auto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aiden-auto
tags:
- Company
- Automotive
- Connected Vehicles
- Mobility
- Telematics
- Android Automotive
- Fleet Management
- Vehicle Data
- In-Vehicle Payments
- Consent Management
website: https://aidenauto.com/
---
