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
  href: https://artifacts.apis.io/bustle-com/hosts/bustle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bustle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bustle-com/vendors/bustle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bustle-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.bustle.com/
- group: auth
  href: https://artifacts.apis.io/bustle-com/security/bustle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bustle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bustle.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.bustle.com/mcp
  - status: 403
    url: https://support.bustle.com/mcp
  - status: 200
    url: https://www.bustle.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: 'Bustle is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by general-catalyst) and added to the network as a stub for full-pipeline profiling.'
image: https://imgix.bustle.com/uploads/image/2020/6/30/6d22de04-dedd-4236-9c06-71902dec41f0-socialshare_bustle.png?w=1200&h=630&fit=crop&crop=faces&fm=jpg
layout: provider
modified: '2026-10-22'
name: Bustle
nav: Providers
network: true
overview: 'Bustle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Entertainment, News, Politics, Fashion, and Beauty.


  Bustle''s developer surface includes support and 4 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Bustle Com Domain Security
  slug: bustle-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bustle-com
tags:
- Entertainment
- News
- Politics
- Fashion
- Beauty
website: https://www.bustle.com
---
