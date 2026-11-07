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
    dynamic_client_registration: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Sunshine provides AI-powered personal assistant services.
  name: Sunshine API
  slug: sunshine-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/sunshine/mcp/sunshine-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sunshine-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sunshine/well-known/sunshine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sunshine-well-known.yml
- group: other
  href: https://artifacts.apis.io/sunshine/hosts/sunshine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sunshine-hosts.yml
- group: other
  href: https://artifacts.apis.io/sunshine/vendors/sunshine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sunshine-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sunshine/security/sunshine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sunshine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sunshine.com/
coverage:
  checked: '2026-10-29'
  detail: The provider's developer page does not expose any machine-readable API specification.
  evidence:
  - status: 200
    url: https://dazzle.ai/dazzle-for-developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'Sunshine is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by unusual-ventures) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at api.dazzle.ai.
  name: Sunshine MCP Server
  slug: sunshine-mcp-yml
modified: '2026-10-29'
name: Sunshine
nav: Providers
network: true
overview: Sunshine is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 13
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.5
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
screenshot: https://apis.io/screenshots/sunshine/sunshine-2026-11-03T144021.png
security:
- kind: domain-security
  name: Sunshine Domain Security
  slug: sunshine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sunshine
tags:
- Company
website: https://sunshine.com/
---
