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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SolarScope has an MCP server and a REST API that screen sites with the same data and the same verdict as Site Studio.
  name: SolarScope API
  slug: solarscope-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/solarscope-io/plans/solarscope-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/solarscope-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/solarscope-io/authentication/solarscope-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/solarscope-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/solarscope-io/conformance/solarscope-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/solarscope-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/solarscope-io/llms/solarscope-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/solarscope-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/solarscope-io/mcp/solarscope-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/solarscope-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/solarscope-io/well-known/solarscope-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/solarscope-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/solarscope-io/hosts/solarscope-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/solarscope-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/solarscope-io/vendors/solarscope-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/solarscope-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://solarscope.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://solarscope.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://solarscope.io/docs/getting-started/quick-start
- group: auth
  href: https://artifacts.apis.io/solarscope-io/security/solarscope-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solarscope-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://solarscope.io/
- group: docs
  title: ''
  type: Documentation
  url: https://solarscope.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://solarscope.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.solarscope.io
- group: operate
  title: ''
  type: Support
  url: https://solarscope.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solarscope.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solarscope.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solarscope
coverage:
  checked: '2026-10-31'
  detail: API endpoint https://solarscope.io/mcp requires authentication (401 Unauthorized).
  evidence:
  - status: 401
    url: https://solarscope.io/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: SolarScope provides an AI‑powered platform for screening and analyzing US solar development sites. It aggregates solar irradiance data from NREL and NASA POWER, transmission line distances, FEMA flood zones, and grid information onto an interactive map. Users can input an address or coordinates and receive a site verdict within minutes, with AI‑generated insights that flag potential deal‑breakers. The service offers a free 14‑day trial, tiered pricing plans, PDF report generation, and integration with AI agents such as ChatGPT, Claude, and Cursor via a REST‑based MCP server and API. SolarScope aims to accelerate renewable‑energy project planning for developers, engineers, and investors.
image: https://solarscope.io/static/images/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at solarscope.io.
  name: solarscope-io MCP Server
  slug: solarscope-io-mcp-yml
modified: '2026-10-31'
name: solarscope-io
nav: Providers
network: true
overview: 'solarscope-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Solar, AI, Renewable-Energy, Site-Screening, and Mapping.


  solarscope-io''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Solarscope Io Plans Pricing
  plan_count: 4
  slug: solarscope-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Solarscope Io Rate Limits
  slug: solarscope-io-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 19.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Solarscope Io Authentication
  slug: solarscope-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Solarscope Io Domain Security
  slug: solarscope-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: solarscope-io
tags:
- Solar
- AI
- Renewable-Energy
- Site-Screening
- Mapping
website: https://solarscope.io/
---
