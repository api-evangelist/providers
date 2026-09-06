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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4dbios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.4d-bios.com/
- group: operate
  title: ''
  type: Support
  url: https://www.4d-bios.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.4d-bios.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.4d-bios.com/legal-notices
- group: start
  title: ''
  type: Login
  url: https://openapi.4d-bios.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/4dbios-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4dbios-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4dbios-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 4D Bios names a "4D Bios Open Platform API" on its own solutions page but conditions it on already having bought the hardware — "If you've purchased products from 4D Bios ... you can customize functions and integrate them using the 4D Bios Open Platform API" — and publishes no reference, spec or developer portal anywhere; the Open Platform console at openapi.4d-bios.com answers 200 with the same 14,728-byte Ant Design Vue login shell on every path including /openapi.json and /v3/api-docs.
  evidence:
  - status: 200
    url: https://www.4d-bios.com/solutions
  - status: 200
    url: https://openapi.4d-bios.com/openapi.json
  - status: 404
    url: https://www.4d-bios.com/llms.txt
  - status: 404
    url: https://www.4d-bios.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2026-09-05'
description: '4D Bios Co., Ltd. (四维生态, Hangzhou, China) is an ag-tech manufacturer of smart vertical-farming systems, founded in 2018 by Dr. Gary Hua. It designs and builds fully enclosed, digitally controlled plant factories — 3D, nursery, strawberry, leafy-greens and specialty lines — alongside containerized grow systems, indoor grow boxes, full-control planting equipment and LED horticultural lighting. The hardware is operated from the company''s own software layer: the 4D Cloud Platform, the 4D CUBE MS management console and 4D BOX, which combine IoT telemetry, environmental and HVAC control, nutrient-solution circulation and big-data analytics for year-round continuous production. 4D Bios markets a "4D Bios Open Platform API" for customers who have already purchased its products and want to build their own software or hardware against the platform, and invites third-party platform service providers to develop applications on the Open Platform. That API has no public developer portal,
  reference, or machine-readable contract; the Open Platform and IoT consoles are login-gated single-page applications.'
image: https://www.4d-bios.com/templates/assets/image/logo_en.svg
layout: provider
modified: '2026-09-05'
name: 4D Bios
nav: Providers
network: true
overview: '4D Bios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Smart Agriculture, Vertical Farming, and Plant Factory.


  4D Bios'' developer surface includes support and 8 more developer resources.'
plans:
- name: 4Dbios Plans Pricing
  plan_count: 0
  slug: 4dbios-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: 4Dbios Rate Limits
  slug: 4dbios-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Dbios Domain Security
  slug: 4dbios-domain-security
  summary_line: HSTS
slug: 4dbios
tags:
- Company
- Agriculture
- Smart Agriculture
- Vertical Farming
- Plant Factory
- Controlled Environment Agriculture
- Internet of Things
- LED Lighting
- Hardware
- Manufacturing
website: https://www.4d-bios.com/
---
