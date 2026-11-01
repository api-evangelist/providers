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
  href: https://artifacts.apis.io/channeladvisor/vendors/channeladvisor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/channeladvisor-vendors.yml
- group: agent
  href: https://artifacts.apis.io/channeladvisor/llms/channeladvisor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/channeladvisor-llms.txt
- group: other
  href: https://artifacts.apis.io/channeladvisor/hosts/channeladvisor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/channeladvisor-hosts.yml
- group: build
  href: https://artifacts.apis.io/channeladvisor/packages/channeladvisor-packages.yml
  title: ''
  type: SDKs
  url: packages/channeladvisor-packages.yml
- group: build
  href: https://artifacts.apis.io/channeladvisor/packages/channeladvisor-packages.yml
  title: ''
  type: Packages
  url: packages/channeladvisor-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://pcat.readme.io/docs/getting-started-1
- group: docs
  title: ''
  type: Documentation
  url: https://developer.channeladvisor.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/channeladvisor
- group: auth
  href: https://artifacts.apis.io/channeladvisor/security/channeladvisor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channeladvisor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.channeladvisor.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.channeladvisor.com/openapi
  - status: 401
    url: https://docs.productcatalog.channeladvisor.com/mcp
  - status: 403
    url: https://developer.channeladvisor.com/mcp
  - status: 401
    url: https://knowledge.channeladvisor.com/api/mcp
  - status: 301
    url: https://www.channeladvisor.com
  reason: partner-login
  state: gated
created: '2026-10-22'
description: 'ChannelAdvisor is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by nea) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-22'
name: ChannelAdvisor
nav: Providers
network: true
overview: 'ChannelAdvisor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  ChannelAdvisor''s developer surface includes getting-started guide, documentation, and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 26.8
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Channeladvisor Domain Security
  slug: channeladvisor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: channeladvisor
tags:
- Company
website: https://www.channeladvisor.com
---
