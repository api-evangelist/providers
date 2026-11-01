---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/sitime/hosts/sitime-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sitime-hosts.yml
- group: other
  href: https://artifacts.apis.io/sitime/vendors/sitime-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sitime-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sitime.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.sitime.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sitime.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.sitime.com/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.sitime.com/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.sitime.com/company/newsroom/blog
- group: auth
  href: https://artifacts.apis.io/sitime/security/sitime-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sitime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sitime.com/
created: '2026-10-22'
description: SiTime is a precision timing company that designs and manufactures MEMS-based timing solutions, including silicon oscillators, resonators, and timing modules for aerospace, defense, automotive, and communications applications. Their products provide high stability and low power consumption, enabling reliable clock timing across a wide range of industries.
layout: provider
modified: '2026-10-22'
name: SiTime
nav: Providers
network: true
overview: 'SiTime is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Timing, MEMS, Aerospace, and Automotive.


  SiTime''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.3
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
    developer_ergonomics: 7.1
    discoverability: 48.2
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
  name: Sitime Domain Security
  slug: sitime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sitime
tags:
- Company
- Timing
- MEMS
- Aerospace
- Automotive
website: https://www.sitime.com/
---
