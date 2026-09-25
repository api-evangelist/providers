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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arianespace/refs/heads/main/hosts/arianespace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arianespace-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.arianespace.com/news/ariane-6-post-launch-update/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arianespace/refs/heads/main/security/arianespace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arianespace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arianespace.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arianespace.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arianespace.com/privacy-and-data-protection-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.arianespace.com/contact/
created: '2026-09-23'
description: Arianespace is a leading European launch service provider, delivering satellites and payloads to a wide range of orbits using its Ariane family of rockets. Founded in 1980, it operates from the Guiana Space Centre and serves commercial, institutional and governmental customers worldwide, offering flexible launch solutions, ground services and mission support.
layout: provider
modified: '2026-09-23'
name: Arianespace
nav: Providers
network: true
overview: 'Arianespace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Launch Services, Satellite, and Europe.


  Arianespace''s developer surface includes support and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arianespace Domain Security
  slug: arianespace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arianespace
tags:
- Company
- Space
- Launch Services
- Satellite
- Europe
website: https://arianespace.com/
---
