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
  href: https://artifacts.apis.io/thesis-co/hosts/thesis-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thesis-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/thesis-co/vendors/thesis-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thesis-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thesis.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thesis.co/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://thesis.co/press
- group: other
  title: ''
  type: Leadership
  url: https://thesis.co/company/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thesis
- group: company
  title: ''
  type: Blog
  url: https://thesis.co/blog
- group: auth
  href: https://artifacts.apis.io/thesis-co/security/thesis-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thesis-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thesis.co
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://thesis.co
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: 'Thesis is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by polychain) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.sanity.io/images/igpikldw/production/a64701134e71010c7546c6c03e39e7976f8a30c6-1920x1080.svg?w=1200&h=630&dpr=2&fit=max
layout: provider
modified: '2026-10-28'
name: Thesis
nav: Providers
network: true
overview: 'Thesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include venture studio, Bitcoin, decentralized products, crypto, and blockchain.


  Thesis'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 42.9
    operational_transparency: 5.3
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
  name: Thesis Co Domain Security
  slug: thesis-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thesis-co
tags:
- venture studio
- Bitcoin
- decentralized products
- crypto
- blockchain
website: https://thesis.co
---
