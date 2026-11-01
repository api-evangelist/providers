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
  href: https://artifacts.apis.io/dglgroupllc/hosts/dglgroupllc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dglgroupllc-hosts.yml
- group: other
  href: https://artifacts.apis.io/dglgroupllc/vendors/dglgroupllc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dglgroupllc-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dglgroupllc/security/dglgroupllc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dglgroupllc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dglgroupllc.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dglgroupllc.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dglgroupllc.com/terms
coverage:
  checked: '2026-10-23'
  detail: Homepage renders via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://dglgroupllc.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: DGL GROUP LLC is a software development and technology consulting firm based in Albuquerque, New Mexico. The company provides custom software solutions, enterprise applications, API development, cloud-native services, telecommunications infrastructure, and mobile app development for businesses worldwide. With over a decade of experience, DGL GROUP serves startups to large enterprises, delivering scalable, high‑quality technology solutions and 24/7 support.
image: https://dglgroupllc.com/og-image.png
layout: provider
modified: '2026-10-23'
name: Dglgroupllc
nav: Providers
network: true
overview: Dglgroupllc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Consulting, Development, and Technology.
random_paper: 7
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 8
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
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
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
  name: Dglgroupllc Domain Security
  slug: dglgroupllc-domain-security
  summary_line: TLSv1.3
slug: dglgroupllc
tags:
- Company
- Software
- Consulting
- Development
- Technology
website: https://dglgroupllc.com
---
