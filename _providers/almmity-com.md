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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/almmity-com/llms/almmity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/almmity-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/almmity-com/well-known/almmity-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/almmity-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/almmity-com/hosts/almmity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/almmity-com-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://api.almmity.com/blog/
- group: auth
  href: https://artifacts.apis.io/almmity-com/security/almmity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/almmity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://almmity.com/
coverage:
  checked: '2026-11-01'
  detail: OpenAPI spec not found at known hosts (api.almmity.com, almmity.com, ksef.almmity.com)
  evidence:
  - status: 404
    url: https://api.almmity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'almmity-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://almmity.com/og.png
layout: provider
modified: '2026-11-01'
name: almmity-com
nav: Providers
network: true
overview: 'almmity-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  almmity-com''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 30.4
    operational_transparency: 0.0
  previous_composite: 3.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Almmity Com Domain Security
  slug: almmity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: almmity-com
tags:
- Company
website: https://almmity.com/
---
