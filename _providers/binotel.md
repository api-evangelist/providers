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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/binotel/hosts/binotel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/binotel-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.binotel.ua/ua/terms
- group: auth
  href: https://artifacts.apis.io/binotel/security/binotel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/binotel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.binotel.ua/
- group: company
  title: ''
  type: About
  url: https://www.binotel.ua/ua/about
- group: operate
  title: ''
  type: Contact
  url: https://www.binotel.ua/ua/contacts
- group: other
  title: ''
  type: Info
  url: https://www.binotel.ua/ua/info
- group: company
  title: ''
  type: Partners
  url: https://www.binotel.ua/ua/binotelpartners
coverage:
  checked: '2026-10-26'
  detail: Binotel does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.binotel.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Binotel provides a virtual PBX (private branch exchange) telephone system for businesses, offering cloud‑based call handling, IVR, call routing, and analytics. The platform aims to improve sales, manager efficiency, and customer service quality through smart telephony solutions.
image: https://www.binotel.ua/favicon/apple-touch-icon.png
layout: provider
modified: '2026-10-26'
name: Binotel
nav: Providers
network: true
overview: Binotel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telephony, Cloud, Business, and Communications.
random_paper: 5
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Binotel Domain Security
  slug: binotel-domain-security
  summary_line: TLSv1.2 · DMARC
slug: binotel
tags:
- Company
- Telephony
- Cloud
- Business
- Communications
website: https://www.binotel.ua/
---
