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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/auto1-com/hosts/auto1-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auto1-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/auto1-com/vendors/auto1-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auto1-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auto1-com/security/auto1-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auto1-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auto1.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auto1.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auto1.com/en/privacy-notice
- group: operate
  title: ''
  type: Support
  url: https://www.auto1.com/en/home/contact
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.auto1.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Auto1 operates Europe’s leading used‑car marketplace, connecting dealers and private sellers through a digital platform that streamlines buying, selling, and logistics. The company offers services such as vehicle inspection, financing, and cross‑border transport, leveraging a large dealer network and technology‑driven solutions to simplify the used‑car market across multiple European countries.
layout: provider
modified: '2026-10-24'
name: Auto1
nav: Providers
network: true
overview: 'Auto1 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Automotive, Europe, and UsedCars.


  Auto1''s developer surface includes support and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 6
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
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Auto1 Com Domain Security
  slug: auto1-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: auto1-com
tags:
- Company
- Marketplace
- Automotive
- Europe
- UsedCars
website: https://www.auto1.com/
---
