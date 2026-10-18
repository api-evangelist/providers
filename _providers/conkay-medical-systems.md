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
api_count: 1
apis:
- description: ConKay Medical Systems API (no public documentation found)
  name: ConKay API
  slug: conkay-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conkay-medical-systems/refs/heads/main/hosts/conkay-medical-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conkay-medical-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conkay-medical-systems/refs/heads/main/vendors/conkay-medical-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conkay-medical-systems-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.conkaymedical.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conkay-medical-systems/refs/heads/main/security/conkay-medical-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conkay-medical-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.conkaymedical.com/
coverage:
  checked: '2026-10-10'
  detail: No public API documentation or developer program is available on the company's website or API host.
  evidence:
  - status: 0
    url: https://api.conkaymedical.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: ConKay Medical Systems is an early‑stage medical device company focused on developing minimally invasive solutions to treat valvular regurgitation in patients with progressive heart failure. Founded in 2020 and based in Pleasanton, CA, the company advances annular repair catheter systems for the tricuspid valve, aiming to reduce the need for open‑heart surgery.
image: http://static1.squarespace.com/static/60e6a47b16b333003b415d52/t/610b080502dd814d8502056a/1628112901038/conkay-color-onblack.png?format=1500w
layout: provider
modified: '2026-10-10'
name: ConKay Medical Systems
nav: Providers
network: true
overview: ConKay Medical Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Cardiovascular, Valvular Regurgitation, Early Stage, and Pleasanton.
random_paper: 2
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Conkay Medical Systems Domain Security
  slug: conkay-medical-systems-domain-security
  summary_line: TLSv1.3 · HSTS
slug: conkay-medical-systems
tags:
- Medical Devices
- Cardiovascular
- Valvular Regurgitation
- Early Stage
- Pleasanton
website: https://www.conkaymedical.com/
---
