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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Augurn provides an API accessible via its MCP endpoint, but the contract is not publicly available.
  name: Augurn API
  slug: augurn-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/augurn-com/llms/augurn-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/augurn-com-llms.txt
- group: other
  href: https://artifacts.apis.io/augurn-com/hosts/augurn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augurn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/augurn-com/vendors/augurn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augurn-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/augurn-com/security/augurn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augurn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augurn.com/
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires POST and returns error, no OpenAPI spec is published.
  evidence:
  - status: 405
    url: https://augurn.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'augurn-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://augurn.com/models/knarb-makes__share-castle__v1.jpg
layout: provider
modified: '2026-11-02'
name: augurn-com
nav: Providers
network: true
overview: augurn-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 14
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  previous_composite: 2.6
  provenance:
    mcp: derived
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
  name: Augurn Com Domain Security
  slug: augurn-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: augurn-com
tags:
- Company
website: https://augurn.com/
---
