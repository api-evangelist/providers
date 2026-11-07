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
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ASA Condor provides tools to compute break-even CPA for Apple Search Ads and manage campaigns.
  name: ASA Condor API
  slug: asa-condor-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/asacondor-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/asacondor-com/mcp/asacondor-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asacondor-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asacondor-com/well-known/asacondor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asacondor-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asacondor-com/hosts/asacondor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asacondor-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asacondor-com/vendors/asacondor-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asacondor-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asacondor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asacondor.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://asacondor.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://asacondor.com/media/country-test.mp4
- group: company
  title: ''
  type: Blog
  url: https://asacondor.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.asacondor.com/
- group: auth
  href: https://artifacts.apis.io/asacondor-com/security/asacondor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asacondor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asacondor.com/
coverage:
  checked: '2026-11-01'
  detail: API endpoints require authentication and return 401, preventing access to contract.
  evidence:
  - status: 401
    url: https://app.asacondor.com/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: 'asacondor-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://asacondor.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.asacondor.com.
  name: asacondor-com MCP Server
  slug: asacondor-com-mcp-yml
modified: '2026-11-01'
name: asacondor-com
nav: Providers
network: true
overview: 'asacondor-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  asacondor-com''s developer surface includes pricing, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Asacondor Com Plans Pricing
  plan_count: 0
  slug: asacondor-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Asacondor Com Rate Limits
  slug: asacondor-com-rate-limits
scopes:
- name: Asacondor Com Scopes
  scope_count: 0
  slug: asacondor-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 40.8
    operational_transparency: 0.0
  previous_composite: 16.3
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asacondor Com Authentication
  slug: asacondor-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Asacondor Com Domain Security
  slug: asacondor-com-domain-security
  summary_line: TLSv1.3
slug: asacondor-com
tags:
- Company
website: https://asacondor.com/
---
