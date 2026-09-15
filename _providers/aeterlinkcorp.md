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
  scored_at: '2026-09-14'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://aeterlink.com/en/
- group: other
  title: ''
  type: Company
  url: https://aeterlink.com/en/company/
- group: other
  title: ''
  type: Technology
  url: https://aeterlink.com/en/technology/
- group: company
  title: ''
  type: News
  url: https://aeterlink.com/en/news/
- group: operate
  title: ''
  type: Contact
  url: https://aeterlink.com/en/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeterlink.com/en/privacy_policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeterlink.com/wp-content/uploads/airplug_term_of_service.pdf
- group: company
  title: ''
  type: Careers
  url: https://aeterlink.com/recruit/
- group: company
  title: ''
  type: Blog
  url: https://note.com/aeterlink
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeterlinkcorp/refs/heads/main/llms/aeterlinkcorp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeterlinkcorp-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aeterlinkcorp/refs/heads/main/security/aeterlinkcorp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeterlinkcorp-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aeterlinkcorp/refs/heads/main/plans/aeterlinkcorp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeterlinkcorp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aeterlinkcorp/refs/heads/main/rate-limits/aeterlinkcorp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aeterlinkcorp-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: Aeterlink's own engineering article names two AirPlug integration surfaces — a "Cloud API" on AirPlug Cloud and a "Direct API" on the Sumit edge computer — but neither has any public reference, base URL or spec, and the only route to technical material is the document-request form at /en/documents/, which emails brochures after a company name and email are submitted.
  evidence:
  - status: 200
    url: https://aeterlink.com/en/documents/
  - status: 200
    url: https://note.com/aeterlink/n/nfe9fd1486ef2
  - status: 404
    url: https://aeterlink.com/openapi.json
  - status: 404
    url: https://airplug-wpt.com/openapi.json
  - status: 404
    url: https://aeterlink.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-12'
description: Aeterlink Corp. is a Tokyo-headquartered deep-tech company, originating from Stanford University research, that develops, manufactures and sells spatial (microwave) wireless power transfer systems under the AirPlug brand. AirPlug delivers power to battery-free IoT sensors and devices at distances of roughly 15-20 meters with bidirectional data communication, and is sold into factory automation, building management and medical implant applications. Founded in August 2020, the company operates offices in Tokyo, Indianapolis and Bangkok, and is active in the international standardization of spatial wireless power transfer. Aeterlink publishes no public developer program, API reference or machine-readable API contract; its product materials are distributed by request form.
image: https://aeterlink.com/wp-content/uploads/ogp/ogp_new_en.png
layout: provider
modified: '2026-09-12'
name: Aeterlink Corp.
nav: Providers
network: true
overview: 'Aeterlink Corp. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wireless Power, Internet of Things, Hardware, and Industrial Automation.


  Aeterlink Corp.''s developer surface includes product news, engineering blog, and 11 more developer resources.'
plans:
- name: Aeterlinkcorp Plans Pricing
  plan_count: 0
  slug: aeterlinkcorp-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aeterlinkcorp Rate Limits
  slug: aeterlinkcorp-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
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
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeterlinkcorp Domain Security
  slug: aeterlinkcorp-domain-security
  summary_line: TLSv1.3
slug: aeterlinkcorp
tags:
- Company
- Wireless Power
- Internet of Things
- Hardware
- Industrial Automation
- Building Management
- Medical Devices
- Deep Tech
- Japan
website: https://aeterlink.com/en/
---
