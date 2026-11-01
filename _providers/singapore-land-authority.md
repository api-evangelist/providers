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
  href: https://artifacts.apis.io/singapore-land-authority/hosts/singapore-land-authority-hosts.yml
  title: ''
  type: Hosts
  url: hosts/singapore-land-authority-hosts.yml
- group: other
  href: https://artifacts.apis.io/singapore-land-authority/vendors/singapore-land-authority-vendors.yml
  title: ''
  type: Vendors
  url: vendors/singapore-land-authority-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sla.gov.sg/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sla.gov.sg/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sla.gov.sg/news/
- group: auth
  href: https://artifacts.apis.io/singapore-land-authority/security/singapore-land-authority-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/singapore-land-authority-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.sla.gov.sg
created: '2026-10-26'
description: The Singapore Land Authority (SLA) is a Singapore government agency that manages about 11,000 hectares of state land and 2,600 properties, provides geospatial technology and data services, and acts as the national land registration and survey authority. It delivers land‑resource optimisation, geospatial ecosystem development and regulatory frameworks for owners, developers, businesses and the public.
image: https://isomer-user-content.by.gov.sg/73/8611e39c-ecfa-4529-9299-0fa073f6af32/Lvl02-Oblique-Forward-063-16940_ss1.jpg
layout: provider
modified: '2026-10-26'
name: Singapore Land Authority
nav: Providers
network: true
overview: Singapore Land Authority is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial Data, Regulatory, and State Assets.
random_paper: 2
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Singapore Land Authority Domain Security
  slug: singapore-land-authority-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: singapore-land-authority
tags:
- Geospatial Data
- Regulatory
- State Assets
website: http://www.sla.gov.sg
---
