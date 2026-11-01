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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/ams-com/well-known/ams-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ams-com-security.txt
- group: agent
  href: https://artifacts.apis.io/ams-com/well-known/ams-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ams-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ams-com/hosts/ams-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ams-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ams-osram.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://ams-osram.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ams-osram.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://ams-osram.com/news
- group: auth
  href: https://artifacts.apis.io/ams-com/security/ams-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ams-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ams-osram.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.ams.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: ams OSRAM is a global provider of light and sensor solutions. It designs and manufactures LEDs, lasers, photodetectors, time‑of‑flight sensors, drivers and related optical modules for customers in automotive and mobility, industrial automation, medical and health devices, mobile and wearable products, lighting and computing applications.
image: https://look.ams-osram.com/transform/82cabd10-d50e-4ab0-9f20-3ce562ad4c6c/ams-OSRAM-visual-CI-grey-cicrle
layout: provider
modified: '2026-10-22'
name: ams OSRAM
nav: Providers
network: true
overview: 'ams OSRAM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include LEDs, Sensors, Automotive, Industrial, and Medical.


  ams OSRAM''s developer surface includes support and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ams Com Domain Security
  slug: ams-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ams-com
tags:
- LEDs
- Sensors
- Automotive
- Industrial
- Medical
- Wearables
- Lighting
- Computing
website: https://ams-osram.com/
---
