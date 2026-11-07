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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP integration for vehicle data, diagnostics and fleet management.
  name: AUTO411 MCP
  slug: auto411-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/411specs-com/mcp/411specs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/411specs-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/411specs-com/well-known/411specs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/411specs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/411specs-com/hosts/411specs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/411specs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/411specs-com/vendors/411specs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/411specs-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://411specs.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://411specs.com/privacy
- group: auth
  href: https://artifacts.apis.io/411specs-com/security/411specs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/411specs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://411specs.com/
coverage:
  checked: '2026-10-31'
  detail: Documentation is not machine‑readable; only HTML pages are available without a spec.
  evidence:
  - status: 200
    url: https://411specs.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AUTO411 delivers configuration‑aware vehicle intelligence for automotive businesses, offering MCP integrations that enable real‑time data, diagnostics, and fleet management. The platform provides APIs for vehicle data access, analytics, and integration with third‑party services, supporting developers to build automotive solutions.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.411specs.com.
  name: AUTO411 MCP Server
  slug: 411specs-com-mcp-yml
modified: '2026-10-31'
name: AUTO411
nav: Providers
network: true
overview: 'AUTO411 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Vehicle Intelligence, MCP Integration, API Platform, and AUTO411.


  AUTO411''s developer surface includes support and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 7.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 411Specs Com Domain Security
  slug: 411specs-com-domain-security
  summary_line: TLSv1.3
slug: 411specs-com
tags:
- Automotive
- Vehicle Intelligence
- MCP Integration
- API Platform
- AUTO411
website: https://411specs.com/
---
