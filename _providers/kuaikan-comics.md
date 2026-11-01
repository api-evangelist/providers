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
  href: https://artifacts.apis.io/kuaikan-comics/hosts/kuaikan-comics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kuaikan-comics-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.kuaikanmanhua.com/webs/help
- group: auth
  href: https://artifacts.apis.io/kuaikan-comics/security/kuaikan-comics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kuaikan-comics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuaikanmanhua.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.kuaikanmanhua.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: 'Kuaikan Comics is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by coatue) and added to the network as a stub for full-pipeline profiling.'
image: https://festatic.v3mh.com/static-resource/img/20210706/tiny/logo_128x128.png
layout: provider
modified: '2026-10-25'
name: Kuaikan Comics
nav: Providers
network: true
overview: 'Kuaikan Comics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Kuaikan Comics'' developer surface includes support and 3 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 30.4
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
  name: Kuaikan Comics Domain Security
  slug: kuaikan-comics-domain-security
  summary_line: TLSv1.2
slug: kuaikan-comics
tags:
- Company
website: https://www.kuaikanmanhua.com/
---
