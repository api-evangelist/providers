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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/alpineai/llms/alpineai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpineai-llms.txt
- group: agent
  href: https://artifacts.apis.io/alpineai/well-known/alpineai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpineai-well-known.yml
- group: other
  href: https://artifacts.apis.io/alpineai/hosts/alpineai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpineai-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://alpineai.swiss/blog/
- group: auth
  href: https://artifacts.apis.io/alpineai/security/alpineai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpineai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alpineai.swiss
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://alpineai.swiss
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'AlpineAI is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by true-ventures) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-24'
name: AlpineAI
nav: Providers
network: true
overview: 'AlpineAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  AlpineAI''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 2.7
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
    developer_ergonomics: 2.4
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Alpineai Domain Security
  slug: alpineai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alpineai
tags:
- Company
website: https://alpineai.swiss
---
