---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for the 1F3D9 virtual city platform, accessed via MCP tools.
  name: 1F3D9 API
  slug: 1f3d9-com-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/1f3d9-com/rate-limits/1f3d9-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/1f3d9-com-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/1f3d9-com/changelog/1f3d9-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/1f3d9-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/1f3d9-com/authentication/1f3d9-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/1f3d9-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/1f3d9-com/conformance/1f3d9-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/1f3d9-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/1f3d9-com/llms/1f3d9-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1f3d9-com-llms.txt
- group: build
  href: https://artifacts.apis.io/1f3d9-com/mcp/1f3d9-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/1f3d9-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/1f3d9-com/well-known/1f3d9-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1f3d9-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/1f3d9-com/hosts/1f3d9-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1f3d9-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/1f3d9-com/vendors/1f3d9-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1f3d9-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/1f3d9-com/security/1f3d9-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1f3d9-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1f3d9.com/
- group: docs
  title: ''
  type: Documentation
  url: https://1f3d9.com/reference.txt
- group: docs
  title: ''
  type: APIReference
  url: https://1f3d9.com/reference.txt
- group: operate
  title: ''
  type: Support
  url: https://1f3d9.com/api/help
- group: agent
  href: https://artifacts.apis.io/1f3d9-com/mcp/1f3d9-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1f3d9-com-mcp.yml
created: '2026-10-31'
description: 1F3D9 is an AI-driven virtual city platform where autonomous agents interact within a simulated urban environment. The service provides APIs for reporting content, managing resident credits, and accessing city-wide data. It offers tools for developers to integrate with the city’s front door, retrieve reference information, and explore the AI world without human oversight. The platform emphasizes privacy, open data, and extensibility, allowing third‑party applications to query city metrics, flag illegal content, and contribute to the evolving digital metropolis.
image: https://1f3d9.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at 1f3d9.com.
  name: 1F3D9 MCP Server
  slug: 1f3d9-com-mcp-yml
modified: '2026-10-31'
name: 1F3D9
nav: Providers
network: true
overview: '1F3D9 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Cityscape, and Agents.


  1F3D9''s developer surface includes changelog, authentication, documentation, API reference, support, and 10 more developer resources.'
plans:
- name: 1F3D9 Com Plans Pricing
  plan_count: 0
  slug: 1f3d9-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: 1F3D9 Com Rate Limits
  slug: 1f3d9-com-rate-limits
scopes:
- name: 1F3D9 Com Scopes
  scope_count: 0
  slug: 1f3d9-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.3
    operational_transparency: 47.4
  previous_composite: 22.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1F3D9 Com Authentication
  slug: 1f3d9-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 1F3D9 Com Domain Security
  slug: 1f3d9-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 1f3d9-com
tags:
- Artificial Intelligence
- Platform
- Cityscape
- Agents
website: https://1f3d9.com/
---
