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
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for A-du marketplace providing ADU rentals, listings, plans, and services.
  name: A-du API
  slug: a-du-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/a-du-homes/conformance/a-du-homes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a-du-homes-conformance.yml
- group: agent
  href: https://artifacts.apis.io/a-du-homes/llms/a-du-homes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a-du-homes-llms.txt
- group: other
  href: https://artifacts.apis.io/a-du-homes/a2a/a-du-homes-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/a-du-homes-a2a.yml
- group: build
  href: https://artifacts.apis.io/a-du-homes/mcp/a-du-homes-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/a-du-homes-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/a-du-homes/mcp/a-du-homes-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/a-du-homes-mcp.yml
- group: agent
  href: https://artifacts.apis.io/a-du-homes/well-known/a-du-homes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/a-du-homes-well-known.yml
- group: other
  href: https://artifacts.apis.io/a-du-homes/hosts/a-du-homes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a-du-homes-hosts.yml
- group: other
  href: https://artifacts.apis.io/a-du-homes/vendors/a-du-homes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a-du-homes-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://a-du.homes/press
- group: auth
  href: https://artifacts.apis.io/a-du-homes/security/a-du-homes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a-du-homes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a-du.homes/
- group: docs
  title: ''
  type: APIReference
  url: https://a-du.homes/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://a-du.homes/pricing
- group: company
  title: ''
  type: Blog
  url: https://a-du.homes/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a-du.homes/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a-du.homes/privacy
created: '2026-10-31'
description: A-du is a marketplace built around Accessory Dwelling Units (ADUs), operating in Los Angeles County, San Francisco, San Diego County and New York City. Rent or list a permit-verified ADU, a house or a room; manage the tenancy; or choose a pre-approved ADU plan, test it on your lot, estimate permit fees and hire licensed professionals directly. A-du does not design, permit or build ADUs.
image: https://a-du.homes/og-horton-house.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at a-du.homes.
  name: A-du, LLC MCP Server
  slug: a-du-homes-mcp-yml
modified: '2026-10-31'
name: A-du, LLC
nav: Providers
network: true
overview: 'A-du, LLC is listed with 1 API on the [APIs.io](https://apis.io/) network: A-du API. Tagged areas include Real Estate, Property Management, ADU, Rentals, and Construction.


  A-du, LLC''s developer surface includes API reference, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: A Du Homes Plans Pricing
  plan_count: 0
  slug: a-du-homes-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: A Du Homes Rate Limits
  slug: a-du-homes-rate-limits
scopes:
- name: A Du Homes Scopes
  scope_count: 0
  slug: a-du-homes-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 24.0
    developer_ergonomics: 4.8
    discoverability: 65.8
    operational_transparency: 0.0
  previous_composite: 23.4
  provenance:
    conformance: derived
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
  name: A Du Homes Authentication
  slug: a-du-homes-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A Du Homes Domain Security
  slug: a-du-homes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a-du-homes
tags:
- Real Estate
- Property Management
- ADU
- Rentals
- Construction
website: https://a-du.homes/
---
