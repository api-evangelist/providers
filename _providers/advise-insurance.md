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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advise-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bloomthrives.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomthrives.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomthrives.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomthrives.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.bloomthrives.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bloomthrives.com/enroll/pricing/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advise-insurance-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/advise-insurance-plans-pricing.yml
coverage:
  checked: '2026-09-09'
  detail: 'Advise Insurance ships real software — the Ascend white-label Medicare quoting, enrollment and health-activation platform, sold to health plans through its operating brand Bloom — but ships it only as an end-user/white-label product: the Ascend page promises to "integrate with the technology and operating platforms you already use through an open system design" while the site carries no developer portal, no API reference and no spec, /developers, /api and /partners all 404, and api., docs., developer. and ascend.bloomthrives.com do not resolve in DNS at all; the company''s own domain adviseinsurance.com no longer serves a site and rewrites every path — including ones that cannot exist — to the bloomthrives.com WordPress multisite signup shell, which is why it answers 200 to everything.'
  evidence:
  - status: 404
    url: https://www.bloomthrives.com/developers
  - status: 404
    url: https://www.bloomthrives.com/openapi.json
  - status: 404
    url: https://www.bloomthrives.com/.well-known/api-catalog
  - status: 200
    url: https://www.bloomthrives.com/ascend-platform/
  - status: 200
    url: https://adviseinsurance.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-09'
description: Advise Insurance is the Medicare distribution business of Advise Health Holdings, a Bloomington, Indiana company founded in 2018 by Sherman Rogers that raised a $100M growth round led by Oak HC/FT in March 2021. It operates as a Medicare concierge agency — unbiased plan comparison and enrollment help for seniors, plus managed-care growth support for physician practices — and its operating brand today is Bloom (bloomthrives.com), the Medicare telesales, quoting, enrollment and health-activation business Rogers launched in 2007. Bloom sells the Ascend platform (Ascend Quote & Enroll, Ascend Broker, Health Activations) to national and regional health plans on a white-label basis. As of 2026-09-09 the company publishes no developer portal, no API documentation and no machine-readable API contract; adviseinsurance.com no longer serves a site of its own and resolves into the bloomthrives.com WordPress multisite.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-09-09'
name: Advise Insurance
nav: Providers
network: true
overview: 'Advise Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Health Insurance, Medicare, and Health Care.


  Advise Insurance''s developer surface includes support, engineering blog, pricing, and 6 more developer resources.'
plans:
- name: Advise Insurance Plans Pricing
  plan_count: 1
  slug: advise-insurance-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Advise Insurance Rate Limits
  slug: advise-insurance-rate-limits
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advise Insurance Domain Security
  slug: advise-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advise-insurance
tags:
- Company
- Insurance
- Health Insurance
- Medicare
- Health Care
- Insurtech
- Enrollment
- Telesales
website: https://www.bloomthrives.com/
---
