---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Multiplier provides technology services; the API is not publicly documented.
  name: Multiplier API
  slug: multiplier-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/multiplierholdings-com/mcp/multiplierholdings-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/multiplierholdings-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/multiplierholdings-com/well-known/multiplierholdings-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/multiplierholdings-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/multiplierholdings-com/hosts/multiplierholdings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/multiplierholdings-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/multiplierholdings-com/vendors/multiplierholdings-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/multiplierholdings-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.multiplierholdings.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/multiplierholdings-com/security/multiplierholdings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/multiplierholdings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.multiplierholdings.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.multiplierholdings.com/terms
coverage:
  checked: '2026-10-29'
  detail: API reference is gated behind a login on the MCP endpoint (app.multiplierholdings.com/mcp) returning 401.
  evidence:
  - status: 401
    url: https://app.multiplierholdings.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: 'Multiplier is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by lightspeed-venture-partners) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/69de9c3fa0cf445a157431f1/6a0b3a7d7375144247492f4e_Multiplier-fulllogo-horizontal-green.svg
layout: provider
mcp_servers:
- description: Remote MCP server at app.multiplierholdings.com.
  name: Multiplier MCP Server
  slug: multiplierholdings-com-mcp-yml
modified: '2026-10-29'
name: Multiplier
nav: Providers
network: true
overview: Multiplier is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Professional Services, Technology, and Acquisition.
random_paper: 11
scopes:
- name: Multiplierholdings Com Scopes
  scope_count: 0
  slug: multiplierholdings-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/multiplierholdings-com/multiplierholdings-com-2026-11-03T135919.png
security:
- kind: authentication
  name: Multiplierholdings Com Authentication
  slug: multiplierholdings-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Multiplierholdings Com Domain Security
  slug: multiplierholdings-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: multiplierholdings-com
tags:
- Company
- Artificial Intelligence
- Professional Services
- Technology
- Acquisition
website: https://www.multiplierholdings.com/
---
