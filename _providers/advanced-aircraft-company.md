---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
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
  score: 21.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Advanced Aircraft Company website at advancedaircraftcompany.com: the route index of the site''s content management system, catalogued as one site surface'
  name: Advanced Aircraft Company Website (WordPress REST)
  slug: advancedaircraftcompany-com-website-wordpress-rest
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://advancedaircraftcompany.com/
- group: company
  title: ''
  type: Blog
  url: https://advancedaircraftcompany.com/news/
- group: operate
  title: ''
  type: Support
  url: https://advancedaircraftcompany.com/contact/
- group: agent
  href: https://artifacts.apis.io/advanced-aircraft-company/llms/advanced-aircraft-company-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/advanced-aircraft-company-llms.txt
- group: agent
  href: https://artifacts.apis.io/advanced-aircraft-company/mcp/advanced-aircraft-company-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/advanced-aircraft-company-mcp.yml
- group: agent
  href: https://artifacts.apis.io/advanced-aircraft-company/well-known/advanced-aircraft-company-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/advanced-aircraft-company-well-known.yml
- group: auth
  href: https://artifacts.apis.io/advanced-aircraft-company/authentication/advanced-aircraft-company-authentication.yml
  title: ''
  type: Authentication
  url: authentication/advanced-aircraft-company-authentication.yml
- group: auth
  href: https://artifacts.apis.io/advanced-aircraft-company/scopes/advanced-aircraft-company-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/advanced-aircraft-company-scopes.yml
- group: design
  href: https://artifacts.apis.io/advanced-aircraft-company/conformance/advanced-aircraft-company-conformance.yml
  title: ''
  type: Conformance
  url: conformance/advanced-aircraft-company-conformance.yml
- group: design
  href: https://artifacts.apis.io/advanced-aircraft-company/errors/advanced-aircraft-company-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/advanced-aircraft-company-problem-types.yml
- group: design
  href: https://artifacts.apis.io/advanced-aircraft-company/conventions/advanced-aircraft-company-conventions.yml
  title: ''
  type: Conventions
  url: conventions/advanced-aircraft-company-conventions.yml
- group: design
  href: https://artifacts.apis.io/advanced-aircraft-company/lifecycle/advanced-aircraft-company-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/advanced-aircraft-company-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/advanced-aircraft-company/rate-limits/advanced-aircraft-company-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/advanced-aircraft-company-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/advanced-aircraft-company/plans/advanced-aircraft-company-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/advanced-aircraft-company-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/advanced-aircraft-company/packages/advanced-aircraft-company-packages.yml
  title: ''
  type: Packages
  url: packages/advanced-aircraft-company-packages.yml
- group: auth
  href: https://artifacts.apis.io/advanced-aircraft-company/security/advanced-aircraft-company-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advanced-aircraft-company-domain-security.yml
created: '2026-09-07'
description: Advanced Aircraft Company (AAC) is a veteran-owned aerospace manufacturer in Hampton, Virginia, founded in 2017 to build long-endurance hybrid fuel-electric VTOL unmanned aircraft systems for commercial, public-safety and defense missions. Its flagship HAMR (Hybrid Advanced Multi-Rotor) UAS flies 3.5+ hours on gas-electric propulsion, and its Greased Lightning tilt-wing is built on technology licensed from NASA Langley Research Center. AAC is a hardware company with no developer program and no product API; its only public machine-readable surface is the WordPress REST API and an OAuth-gated WordPress MCP Adapter server exposed by its own marketing site.
layout: provider
mcp_servers:
- description: 'A live, OAuth-gated Model Context Protocol server is served from the Advanced Aircraft Company corporate site. It is the WordPress MCP Adapter, surfaced through the WordPress REST API under the `mcp` '
  name: Advanced Aircraft Company MCP Server
  slug: advanced-aircraft-company-mcp-server
modified: '2026-09-07'
name: Advanced Aircraft Company
nav: Providers
network: true
overview: 'Advanced Aircraft Company is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Defense, Drones, and Unmanned Aircraft Systems.


  Advanced Aircraft Company''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Advanced Aircraft Company Plans Pricing
  plan_count: 0
  slug: advanced-aircraft-company-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Advanced Aircraft Company Rate Limits
  slug: advanced-aircraft-company-rate-limits
scopes:
- name: Advanced Aircraft Company Scopes
  scope_count: 1
  slug: advanced-aircraft-company-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 63.3
    operational_transparency: 0.0
  previous_composite: 15.9
  provenance:
    conformance: first-party
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/advanced-aircraft-company/advanced-aircraft-company-2026-10-11T092847.png
security:
- kind: authentication
  name: Advanced Aircraft Company Authentication
  slug: advanced-aircraft-company-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Advanced Aircraft Company Domain Security
  slug: advanced-aircraft-company-domain-security
  summary_line: TLSv1.3
slug: advanced-aircraft-company
tags:
- Company
- Aerospace
- Defense
- Drones
- Unmanned Aircraft Systems
- UAV
- VTOL
- Manufacturing
- Public Safety
website: https://advancedaircraftcompany.com/
---
