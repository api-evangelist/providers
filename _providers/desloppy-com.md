---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/desloppy-com/llms/desloppy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/desloppy-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/desloppy-com/well-known/desloppy-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/desloppy-com-security.txt
- group: agent
  href: https://artifacts.apis.io/desloppy-com/well-known/desloppy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/desloppy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/desloppy-com/hosts/desloppy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/desloppy-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/desloppy
- group: auth
  href: https://artifacts.apis.io/desloppy-com/security/desloppy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desloppy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://desloppy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://desloppy.com/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: 'desloppy-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-05'
name: desloppy-com
nav: Providers
network: true
overview: desloppy-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 20
score:
  band: minimal
  composite: 4.2
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
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Desloppy Com Domain Security
  slug: desloppy-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: desloppy-com
tags:
- Company
website: https://desloppy.com/
---
