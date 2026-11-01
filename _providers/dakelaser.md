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
  href: https://artifacts.apis.io/dakelaser/hosts/dakelaser-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dakelaser-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dekalaser.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dekalaser.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/dakelaser/security/dakelaser-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dakelaser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dekalaser.com
created: '2026-10-22'
description: Dakelaser is an Italian medical laser technology company specializing in aesthetic and dermatological laser systems. Founded in 1981, it develops, manufactures, and sells a broad portfolio of laser devices for skin treatments, surgical procedures, and research. The company operates globally, offering products such as Exolight, HELIX, and SmartXide, and provides training and support through its DEKA Academy and DEKA Club.
layout: provider
modified: '2026-10-22'
name: Dakelaser
nav: Providers
network: true
overview: Dakelaser is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aesthetic Medicine, Medical Devices, Surgical Technology, and Women Health.
random_paper: 4
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
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
  name: Dakelaser Domain Security
  slug: dakelaser-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dakelaser
tags:
- Aesthetic Medicine
- Medical Devices
- Surgical Technology
- Women Health
website: https://dekalaser.com
---
