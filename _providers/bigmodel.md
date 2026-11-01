---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bigmodel/llms/bigmodel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigmodel-llms.txt
- group: other
  href: https://artifacts.apis.io/bigmodel/a2a/bigmodel-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bigmodel-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bigmodel/well-known/bigmodel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bigmodel-well-known.yml
- group: other
  href: https://artifacts.apis.io/bigmodel/hosts/bigmodel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigmodel-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bigmodel.cn/cn/guide/start/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bigmodel.cn/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bigmodel.cn/llms.txt
- group: auth
  href: https://artifacts.apis.io/bigmodel/security/bigmodel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigmodel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigmodel.cn/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://bigmodel.cn/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: 'Zhipu AI is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-20'
name: Zhipu AI
nav: Providers
network: true
overview: 'Zhipu AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Zhipu AI''s developer surface includes getting-started guide, documentation, API reference, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
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
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bigmodel Domain Security
  slug: bigmodel-domain-security
  summary_line: TLSv1.3
slug: bigmodel
tags:
- Company
website: https://bigmodel.cn/
---
