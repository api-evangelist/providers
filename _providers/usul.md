---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 13.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/usul/vendors/usul-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usul-vendors.yml
- group: agent
  href: https://artifacts.apis.io/usul/well-known/usul-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usul-well-known.yml
- group: other
  href: https://artifacts.apis.io/usul/hosts/usul-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usul-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://usul.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usul.com/
- group: auth
  href: https://artifacts.apis.io/usul/security/usul-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usul-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usul.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://app.usul.com/api/mcp
  - status: 200
    url: https://usul.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'Usul is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by true-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/images/UvPrnUwICNZWXZjnZnaulxMOHU.png
layout: provider
modified: '2026-10-24'
name: Usul
nav: Providers
network: true
overview: 'Usul is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government Contracts, AI Platform, Competitive Intelligence, Stakeholder Mapping, and Budget Analysis.


  Usul''s developer surface includes documentation and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 41.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usul Domain Security
  slug: usul-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usul
tags:
- Government Contracts
- AI Platform
- Competitive Intelligence
- Stakeholder Mapping
- Budget Analysis
- Supplier Management
- Business Development
website: https://usul.com
---
