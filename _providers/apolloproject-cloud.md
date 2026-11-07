---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/apolloproject-cloud/a2a/apolloproject-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apolloproject-cloud-a2a.yml
- group: other
  href: https://artifacts.apis.io/apolloproject-cloud/hosts/apolloproject-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apolloproject-cloud-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apolloproject-cloud/security/apolloproject-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apolloproject-cloud-domain-security.yml
coverage:
  checked: '2026-11-01'
  detail: OpenAPI spec at https://geo360.apolloproject.cloud/openapi.json does not appear to belong to apolloproject-cloud based on title and info fields.
  evidence:
  - status: 200
    url: https://geo360.apolloproject.cloud/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'apolloproject-cloud is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-01'
name: apolloproject-cloud
nav: Providers
network: true
overview: apolloproject-cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Apolloproject Cloud Plans Pricing
  plan_count: 0
  slug: apolloproject-cloud-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Apolloproject Cloud Rate Limits
  slug: apolloproject-cloud-rate-limits
scopes:
- name: Apolloproject Cloud Scopes
  scope_count: 0
  slug: apolloproject-cloud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  previous_composite: 2.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apolloproject Cloud Authentication
  slug: apolloproject-cloud-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apolloproject Cloud Domain Security
  slug: apolloproject-cloud-domain-security
  summary_line: TLSv1.3
slug: apolloproject-cloud
tags:
- Company
---
