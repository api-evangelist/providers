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
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pipefork provides an AI‑powered API builder via the Model Context Protocol (MCP). No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts are published.
  name: Pipefork API
  slug: pipefork-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/pipefork-com/mcp/pipefork-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pipefork-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pipefork-com/well-known/pipefork-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pipefork-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pipefork-com/hosts/pipefork-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pipefork-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pipefork-com/vendors/pipefork-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pipefork-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pipefork.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pipefork.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/pipefork-com/security/pipefork-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pipefork-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pipefork.com/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found at standard locations.
  evidence:
  - status: 404
    url: https://api.pipefork.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Pipefork is an AI‑powered API builder that lets developers compose, transform, and secure multiple APIs through the Model Context Protocol (MCP). With a browser‑based interface, users can create endpoints, integrate AI agents, apply API key protection, and deploy instantly. Features include AI‑driven endpoint creation, multi‑API composition, response transformation, and built‑in security, enabling rapid development of integrated services without writing code.
image: https://www.pipefork.com/pipefork-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.pipefork.com.
  name: pipefork-com MCP Server
  slug: pipefork-com-mcp-yml
modified: '2026-10-30'
name: pipefork-com
nav: Providers
network: true
overview: pipefork-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Builder, Artificial Intelligence, MCP, and Low-Code.
plans:
- name: Pipefork Com Plans Pricing
  plan_count: 0
  slug: pipefork-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Pipefork Com Rate Limits
  slug: pipefork-com-rate-limits
scopes:
- name: Pipefork Com Scopes
  scope_count: 0
  slug: pipefork-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 11.7
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
screenshot: https://apis.io/screenshots/pipefork-com/pipefork-com-2026-11-03T141244.png
security:
- kind: authentication
  name: Pipefork Com Authentication
  slug: pipefork-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pipefork Com Domain Security
  slug: pipefork-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pipefork-com
tags:
- Company
- API Builder
- Artificial Intelligence
- MCP
- Low-Code
- Integration
website: https://pipefork.com/
---
