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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API reference not found; provider website offers no machine-readable contract.
  name: Apricot Tools API
  slug: apricot-tools-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/apricot-tools/llms/apricot-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apricot-tools-llms.txt
- group: other
  href: https://artifacts.apis.io/apricot-tools/hosts/apricot-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apricot-tools-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.apricot.tools/
- group: auth
  href: https://artifacts.apis.io/apricot-tools/security/apricot-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apricot-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apricot.tools/
coverage:
  checked: '2026-11-01'
  detail: Website provides no public OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://apricot.tools/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'apricot-tools is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-01'
name: apricot-tools
nav: Providers
network: true
overview: 'apricot-tools is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  apricot-tools'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 2.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apricot Tools Domain Security
  slug: apricot-tools-domain-security
  summary_line: TLSv1.3
slug: apricot-tools
tags:
- Company
website: https://apricot.tools/
---
