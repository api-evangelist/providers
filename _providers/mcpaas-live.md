---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: MCPaaS documentation — claim a namepoint, voice memory, Slash pre-flight checks, FAFHub, the hosted MCP endpoint, and the .faf format specs.
  name: MCPaaS API
  slug: mcpaas-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: https://mcpaas.live/security-policy
- group: commercial
  href: https://artifacts.apis.io/mcpaas-live/plans/mcpaas-live-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mcpaas-live-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/mcpaas-live/mcp/mcpaas-live-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mcpaas-live-mcp.yml
- group: auth
  href: https://artifacts.apis.io/mcpaas-live/well-known/mcpaas-live-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mcpaas-live-security.txt
- group: agent
  href: https://artifacts.apis.io/mcpaas-live/well-known/mcpaas-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mcpaas-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/mcpaas-live/hosts/mcpaas-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpaas-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcpaas-live/vendors/mcpaas-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcpaas-live-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wolfe-Jam
- group: operate
  title: ''
  type: ChangeLog
  url: https://mcpaas.live/changelog
- group: auth
  href: https://artifacts.apis.io/mcpaas-live/security/mcpaas-live-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mcpaas-live-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mcpaas-live/security/mcpaas-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpaas-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpaas.live/
- group: docs
  title: ''
  type: Documentation
  url: https://mcpaas.live/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcpaas.live/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mcpaas.live/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://mcpaas.live/claim
- group: commercial
  title: ''
  type: Pricing
  url: https://mcpaas.live/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcpaas.live/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcpaas.live/privacy
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine-readable OpenAPI, AsyncAPI, GraphQL, or other spec was found.
  evidence:
  - status: 200
    url: https://mcpaas.live/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: mcpaas-live provides MCPaaS, a Zig-WASM powered “MCP as a Service” platform delivering sub-millisecond AI context endpoints at the edge. It operates across 300+ edge locations, offering developers namepoint leasing, context storage, and integration with FAF and other AI tools. The service emphasizes low latency, transparent pricing, and open specifications, targeting developers building AI-enhanced applications.
image: https://mcpaas.live/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcpaas.live.
  name: mcpaas-live MCP Server
  slug: mcpaas-live-mcp-yml
modified: '2026-10-29'
name: mcpaas-live
nav: Providers
network: true
overview: 'mcpaas-live is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCPaaS, Edge Computing, AI, and Zig.


  mcpaas-live''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Mcpaas Live Plans Pricing
  plan_count: 4
  slug: mcpaas-live-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 31.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mcpaas Live Domain Security
  slug: mcpaas-live-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Mcpaas Live Vulnerability Disclosure
  slug: mcpaas-live-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mcpaas-live
tags:
- Company
- MCPaaS
- Edge Computing
- AI
- Zig
- WASM
website: https://mcpaas.live/
---
