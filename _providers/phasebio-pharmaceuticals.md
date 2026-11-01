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
  href: https://artifacts.apis.io/phasebio-pharmaceuticals/hosts/phasebio-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phasebio-pharmaceuticals-hosts.yml
- group: other
  href: https://artifacts.apis.io/phasebio-pharmaceuticals/vendors/phasebio-pharmaceuticals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phasebio-pharmaceuticals-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phasebio.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/phasebio-pharmaceuticals/security/phasebio-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phasebio-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phasebio.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://phasebio.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: PhaseBio Pharmaceuticals develops innovative therapies focused on cardiovascular and metabolic diseases, aiming to improve patient outcomes. The company’s mission, reflected in its tagline “Take It To Heart,” emphasizes commitment to advancing science and delivering impactful treatments.
layout: provider
modified: '2026-10-22'
name: PhaseBio Pharmaceuticals
nav: Providers
network: true
overview: PhaseBio Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cardiovascular, Therapeutics, and ClinicalTrials.
random_paper: 6
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 6
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
    discoverability: 44.6
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
  name: Phasebio Pharmaceuticals Domain Security
  slug: phasebio-pharmaceuticals-domain-security
  summary_line: TLSv1.3
slug: phasebio-pharmaceuticals
tags:
- Company
- Biotechnology
- Cardiovascular
- Therapeutics
- ClinicalTrials
website: https://phasebio.com
---
