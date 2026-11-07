---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Astryke API provides programmatic access to its tools and data.
  name: Astryke API
  slug: astryke-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/astryke-com/plans/astryke-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astryke-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/astryke-com/cli/astryke-com-cli.yml
  title: ''
  type: CLI
  url: cli/astryke-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/astryke-com/authentication/astryke-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/astryke-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/astryke-com/conformance/astryke-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astryke-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astryke-com/mcp/astryke-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/astryke-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/astryke-com/well-known/astryke-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astryke-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/astryke-com/hosts/astryke-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astryke-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/astryke-com/vendors/astryke-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astryke-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/astryke-com/security/astryke-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astryke-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astryke.com/
- group: docs
  title: ''
  type: Documentation
  url: https://astryke.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://astryke.com/pro/
- group: start
  title: ''
  type: GettingStarted
  url: https://astryke.com/guides/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astryke.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astryke.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.astryke.com/register.php
coverage:
  checked: '2026-11-02'
  detail: OpenAPI spec URLs on api.astryke.com and app.astryke.com redirect to a login page, requiring authentication.
  evidence:
  - status: 302
    url: https://app.astryke.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Astryke provides forge‑built tools for indie game developers, including pixel art editors, sprite sheet packers, SFX generators, slot machine and dice widgets, all free and embeddable. Its Hub remembers project state so connected AI sessions can continue where they left off, preventing AI forgetting. The platform offers a web‑based dashboard, API, and free tools, with pricing for advanced features.
image: https://astryke.com/opengraph-image?93b1e0d90599500a
layout: provider
mcp_servers:
- description: Remote MCP server at app.astryke.com.
  name: Astryke MCP Server
  slug: astryke-com-mcp-yml
modified: '2026-11-01'
name: Astryke
nav: Providers
network: true
overview: 'Astryke is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Game Development, Indie Tools, Pixel Art, Audio Generation, and Free Widgets.


  Astryke''s developer surface includes CLI, authentication, documentation, pricing, getting-started guide, signup flow, and 10 more developer resources.'
plans:
- name: Astryke Com Plans Pricing
  plan_count: 2
  slug: astryke-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Astryke Com Rate Limits
  slug: astryke-com-rate-limits
scopes:
- name: Astryke Com Scopes
  scope_count: 0
  slug: astryke-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astryke Com Authentication
  slug: astryke-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Astryke Com Domain Security
  slug: astryke-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: astryke-com
tags:
- Game Development
- Indie Tools
- Pixel Art
- Audio Generation
- Free Widgets
website: https://astryke.com/
---
