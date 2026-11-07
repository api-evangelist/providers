---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Departi's Model Context Protocol server (JSON-RPC 2.0 over HTTP, server version 3.2.0) for AI agents, chatbots and travel automation. It exposes seven tools - visa requirements, Schengen 90/180 tracki
  name: Departi MCP API
  slug: departi-mcp-api
artifact_total: 8
common:
- group: build
  href: https://artifacts.apis.io/departi-eu/integrations/departi-eu-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/departi-eu-integration-edges.yml
- group: operate
  href: https://artifacts.apis.io/departi-eu/rate-limits/departi-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/departi-eu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/departi-eu/plans/departi-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/departi-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/departi-eu/conventions/departi-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/departi-eu-conventions.yml
- group: auth
  href: https://artifacts.apis.io/departi-eu/authentication/departi-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/departi-eu-authentication.yml
- group: auth
  href: https://artifacts.apis.io/departi-eu/scopes/departi-eu-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/departi-eu-scopes.yml
- group: design
  href: https://artifacts.apis.io/departi-eu/lifecycle/departi-eu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/departi-eu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/departi-eu/conformance/departi-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/departi-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/departi-eu/llms/departi-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/departi-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/departi-eu/mcp/departi-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/departi-eu-mcp.yml
- group: agent
  href: https://artifacts.apis.io/departi-eu/well-known/departi-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/departi-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/departi-eu/hosts/departi-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/departi-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/departi-eu/vendors/departi-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/departi-eu-vendors.yml
- group: auth
  href: https://artifacts.apis.io/departi-eu/security/departi-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/departi-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://departi.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://departi.eu/developers
- group: docs
  title: ''
  type: Documentation
  url: https://departi.eu/developers/mcp
- group: company
  title: ''
  type: Blog
  url: https://departi.eu/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://departi.eu/pricing
- group: start
  title: ''
  type: Login
  url: https://departi.eu/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://departi.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://departi.eu/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://departi.eu/llms.txt
- group: company
  title: ''
  type: About
  url: https://departi.eu/about
- group: other
  title: ''
  type: Email
  url: mailto:hello@departi.eu
- group: other
  title: ''
  type: X
  url: https://x.com/departinow
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/departinow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/departi-travel
created: '2026-11-05'
description: 'Departi (departi.eu) is a European travel platform built by Crint Consulting BV, based in Belgium, covering 189 destinations across 46 countries with curated accommodation, local experiences and practical guidance. It offers two memberships: Departi Explorer (EUR 4.90/mo) with member accommodation rates, experience booking, an AI travel concierge and group trip coordination, and Departi Nomad (EUR 9.90/mo) adding visa guidance, tax and fiscal analysis, Schengen tracking and a compliance concierge for digital nomads, remote workers and relocators. Developers integrate via a Model Context Protocol (MCP) server to search workation stays, query destination intelligence and book flights programmatically.'
examples:
- key_count: 3
  name: Departi Eu Mcp Tools List
  slug: departi-eu-mcp-tools-list
image: https://departi.eu/favicon.svg
layout: provider
mcp_servers:
- description: Departi official remote MCP server (serverInfo name Departi, version 3.2.0, protocolVersion 2025-11-25). Public tools at https://mcp.departi.eu/v3 need no authentication; the authenticated departi_get
  name: Departi MCP Server
  slug: departi-mcp-server
modified: '2026-11-05'
name: Departi
nav: Providers
network: true
overview: 'Departi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Digital Nomads, Accommodation, and Visa.


  Departi''s developer surface includes authentication, documentation, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Departi Eu Plans Pricing
  plan_count: 3
  slug: departi-eu-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Departi Eu Rate Limits
  slug: departi-eu-rate-limits
scopes:
- name: Departi Eu Scopes
  scope_count: 1
  slug: departi-eu-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 33.3
    discoverability: 71.7
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Departi Eu Authentication
  slug: departi-eu-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Departi Eu Domain Security
  slug: departi-eu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: departi-eu
tags:
- Company
- Travel
- Digital Nomads
- Accommodation
- Visa
- MCP
- AI Concierge
- Europe
website: https://departi.eu/
---
