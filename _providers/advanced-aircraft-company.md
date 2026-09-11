---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: The public WordPress REST API served from the Advanced Aircraft Company corporate site at https://advancedaircraftcompany.com/wp-json. The self-describing route index advertises 647 routes across 46 n
  name: Advanced Aircraft Company Site Content API
  slug: advanced-aircraft-company-site-content-api
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
  title: ''
  type: LLMsTxt
  url: llms/advanced-aircraft-company-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/advanced-aircraft-company-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/advanced-aircraft-company-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advanced-aircraft-company-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/advanced-aircraft-company-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advanced-aircraft-company-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advanced-aircraft-company-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advanced-aircraft-company-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advanced-aircraft-company-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advanced-aircraft-company-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advanced-aircraft-company-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/advanced-aircraft-company-packages.yml
- group: auth
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
overview: 'Advanced Aircraft Company publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Defense, Drones, and Unmanned Aircraft Systems.


  Advanced Aircraft Company''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Advanced Aircraft Company Plans Pricing
  plan_count: 0
  slug: advanced-aircraft-company-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Advanced Aircraft Company Rate Limits
  slug: advanced-aircraft-company-rate-limits
scopes:
- name: Advanced Aircraft Company Scopes
  scope_count: 0
  slug: advanced-aircraft-company-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- Content
website: https://advancedaircraftcompany.com/
---
