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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/byonyks-medical-devices/refs/heads/main/hosts/byonyks-medical-devices-hosts.yml
  title: ''
  type: Hosts
  url: hosts/byonyks-medical-devices-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/byonyks-medical-devices/refs/heads/main/vendors/byonyks-medical-devices-vendors.yml
  title: ''
  type: Vendors
  url: vendors/byonyks-medical-devices-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://byonyks.com/media/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byonyks-medical-devices/refs/heads/main/security/byonyks-medical-devices-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/byonyks-medical-devices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://byonyks.com/
- group: company
  title: ''
  type: AboutUs
  url: https://byonyks.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://byonyks.com/contact/
- group: company
  title: ''
  type: NewsAndMedia
  url: https://byonyks.com/news-and-media/
- group: other
  title: ''
  type: FDA Clearance
  url: https://byonyks.com/fda-510k-clearance/
coverage:
  checked: '2026-10-06'
  detail: No machine‑readable API specification was found on the company’s website or API host.
  evidence:
  - status: 200
    url: https://byonyks.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Byonyks Medical Devices is a medical device company focused on home peritoneal dialysis solutions. It develops innovative automated dialysis cyclers, having received FDA 510(k) clearance for its X-1 APD Cycler. The company aims to improve patient outcomes, reduce treatment costs, and extend kidney failure patients’ quality of life through advanced, biocompatible technology.
layout: provider
modified: '2026-10-06'
name: Byonyks Medical Devices
nav: Providers
network: true
overview: Byonyks Medical Devices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Dialysis, Healthcare, Innovation, and FDA-cleared.
random_paper: 21
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Byonyks Medical Devices Domain Security
  slug: byonyks-medical-devices-domain-security
  summary_line: TLSv1.3
slug: byonyks-medical-devices
tags:
- Medical Devices
- Dialysis
- Healthcare
- Innovation
- FDA-cleared
website: https://byonyks.com/
---
