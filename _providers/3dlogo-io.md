---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- description: API for 3DLogo.io providing tools to generate 3D logos.
  name: 3DLogo.io API
  slug: 3dlogo-io-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/3dlogo-io/plans/3dlogo-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3dlogo-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/3dlogo-io/llms/3dlogo-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dlogo-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/3dlogo-io/mcp/3dlogo-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/3dlogo-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/3dlogo-io/well-known/3dlogo-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dlogo-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dlogo-io/hosts/3dlogo-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dlogo-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dlogo-io/vendors/3dlogo-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dlogo-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://3dlogo.io/signup?next=%2Feditor
- group: company
  title: ''
  type: Newsroom
  url: https://3dlogo.io/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://3dlogo.io/changelog
- group: auth
  href: https://artifacts.apis.io/3dlogo-io/security/3dlogo-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dlogo-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dlogo.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://3dlogo.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dlogo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dlogo.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://3dlogo.io/contact
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint requires authentication, preventing contract discovery.
  evidence:
  - status: 405
    url: https://3dlogo.io/api/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: 3DLogo.io provides a free browser-based 3D logo maker that lets users extrude a logo mark or typed name into a 3D render with chrome, gold, or glass finishes. Users can export their creations as PNG, GLB, or MP4 files without signing up, making it an easy tool for quick branding and graphic design.
image: https://3dlogo.io/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at 3dlogo.io.
  name: 3DLogo.io MCP Server
  slug: 3dlogo-io-mcp-yml
modified: '2026-10-31'
name: 3DLogo.io
nav: Providers
network: true
overview: '3DLogo.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Logo, Design, Graphics, and Company.


  3DLogo.io''s developer surface includes signup flow, changelog, pricing, support, and 11 more developer resources.'
plans:
- name: 3Dlogo Io Plans Pricing
  plan_count: 3
  slug: 3dlogo-io-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: 3Dlogo Io Rate Limits
  slug: 3dlogo-io-rate-limits
scopes:
- name: 3Dlogo Io Scopes
  scope_count: 0
  slug: 3dlogo-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 65.8
    operational_transparency: 7.9
  previous_composite: 27.1
  provenance:
    conformance: unknown
    mcp: first-party
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
  name: 3Dlogo Io Authentication
  slug: 3dlogo-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 3Dlogo Io Domain Security
  slug: 3dlogo-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3dlogo-io
tags:
- 3D
- Logo
- Design
- Graphics
- Company
website: https://3dlogo.io/
---
