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
  href: https://artifacts.apis.io/bere-al/vendors/bere-al-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bere-al-vendors.yml
- group: other
  href: https://artifacts.apis.io/bere-al/hosts/bere-al-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bere-al-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bereal.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.bereal.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bereal.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bereal.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://help.bereal.com/
- group: auth
  href: https://artifacts.apis.io/bere-al/security/bere-al-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bere-al-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bere.al/en
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.bereal.com/mcp
  - status: 200
    url: https://bere.al/en
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: 'BeReal is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by accel, coatue) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/images/xP59bejPGkz1FlgVZnefYlWr4.png
layout: provider
modified: '2026-10-21'
name: BeReal
nav: Providers
network: true
overview: 'BeReal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  BeReal''s developer surface includes support, documentation, and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 32.1
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
  name: Bere Al Domain Security
  slug: bere-al-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bere-al
tags:
- Company
website: https://bere.al/en
---
