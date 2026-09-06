---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/superset-create-workspace-and-run-agent.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superset-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/superset-a2a.yml
created: '2026-07-17'
description: Superset is a company surfaced as a portfolio company of y-combinator and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: Superset MCP Server
  slug: superset-mcp-server
modified: '2026-07-17'
name: Superset
nav: Providers
network: true
overview: Superset is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 9
scopes:
- name: Superset Scopes
  scope_count: 4
  slug: superset-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 35.2
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 6.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Superset Authentication
  slug: superset-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Superset Domain Security
  slug: superset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: superset
tags:
- Company
---
