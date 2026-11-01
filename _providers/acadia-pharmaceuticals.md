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
  href: https://artifacts.apis.io/acadia-pharmaceuticals/hosts/acadia-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acadia-pharmaceuticals-hosts.yml
- group: other
  href: https://artifacts.apis.io/acadia-pharmaceuticals/vendors/acadia-pharmaceuticals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acadia-pharmaceuticals-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acadia.com/en-us/legal-policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acadia.com/en-us/legal-policies/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://acadia.com/en-us/media
- group: other
  title: ''
  type: Leadership
  url: https://acadia.com/en-us/about/leadership
- group: auth
  href: https://artifacts.apis.io/acadia-pharmaceuticals/security/acadia-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acadia-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acadia.com/en-us
- group: other
  title: ''
  type: Image
  url: https://acadia.com/s/homepage-og-image_Z16Vw7s.jpg
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://acadia.com/en-us
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Acadia Pharmaceuticals advances care for underserved neurological disorders and rare diseases. Since its founding, Acadia has been at the forefront of healthcare, developing innovative medicines to bring vital solutions to patients in need. The company focuses on scientific discovery and translating breakthroughs into meaningful treatments for conditions such as Parkinson’s disease, Alzheimer’s disease, and other neurodegenerative disorders.
image: https://acadia.com/s/homepage-og-image_Z16Vw7s.jpg
layout: provider
modified: '2026-10-22'
name: Acadia Pharmaceuticals
nav: Providers
network: true
overview: Acadia Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Neurology, and Healthcare.
random_paper: 22
score:
  band: minimal
  composite: 9.2
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
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Acadia Pharmaceuticals Domain Security
  slug: acadia-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acadia-pharmaceuticals
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Neurology
- Healthcare
website: https://acadia.com/en-us
---
