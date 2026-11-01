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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dimatrix/hosts/dimatrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dimatrix-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diamatrix.com/about/privacy-terms-and-conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://diamatrix.com/news/
- group: auth
  href: https://artifacts.apis.io/dimatrix/security/dimatrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimatrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diamatrix.com
coverage:
  checked: '2026-10-23'
  detail: No API documentation or machine-readable contracts were found on the company's website.
  evidence:
  - status: 200
    url: https://diamatrix.com
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Dimatrix Ltd is a provider of ophthalmic surgical instruments, knives, sutures and related medical devices. Founded in 1993, the company offers a range of high‑quality products for eye surgeons, including diamond‑coated knives, stainless‑steel instruments, iris speculum devices, and suture solutions. Their portfolio emphasizes innovation, precision, and patient outcomes, serving hospitals and eye‑care facilities worldwide.
layout: provider
modified: '2026-10-23'
name: Dimatrix
nav: Providers
network: true
overview: Dimatrix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical, Ophthalmology, Surgical Instruments, Healthcare, and Devices.
random_paper: 2
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dimatrix Domain Security
  slug: dimatrix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dimatrix
tags:
- Medical
- Ophthalmology
- Surgical Instruments
- Healthcare
- Devices
website: https://diamatrix.com
---
