---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: Official read-only MCP agent surface for the Shelter budgeting product — ten tools covering status, runway, forecast, alerts, opportunities, context, affordability, coaching, and Guardian Q&A, shipped
  name: Shelter MCP
  slug: shelter-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://shelter.money
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shelter.money/developers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shelter-money-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/shelter-money-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shelter-money-llms.txt
- group: auth
  title: ''
  type: Security
  url: security/shelter-money-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shelter-money-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shelter-money-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shelter-money-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/shelter-money-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shelter-money-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shelter-money-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://shelter.money/pricing
- group: operate
  title: ''
  type: Support
  url: https://shelter.money/support
- group: company
  title: ''
  type: Blog
  url: https://shelter.money/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shelter.money/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shelter.money/terms
- group: start
  title: ''
  type: SignUp
  url: https://shelter.money/sign-up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextauralabs
created: '2026-09-07'
description: Shelter is a read-only AI money guardian from Nextaura Labs that connects to a user's financial accounts through Plaid and publishes a 30-day cash-flow forecast, safe-to-spend and affordability checks, bill and subscription detection, and low-balance alerts. Its agent surface is an official open-source MCP server (npm @shelter.money/mcp, ten read-only tools with an MCP-registry server.json) backed by a scoped-API-key Agent API; the documented API host api.shelter.money was NXDOMAIN at probe time (2026-09-07), so the live API could not be reached.
layout: provider
mcp_servers:
- description: Official, open-source (MIT) read-only MCP server connecting Claude, Codex, Cursor and other MCP-compatible agents to scoped financial context from a user's own Shelter account — forecasts, runway, ale
  name: Shelter MCP Server
  slug: shelter-mcp-server
modified: '2026-09-07'
name: Shelter
nav: Providers
network: true
overview: 'Shelter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Finance, Budgeting, Fintech, MCP, and AI Agents.


  Shelter''s developer surface includes pricing, support, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Shelter Money Plans Pricing
  plan_count: 2
  slug: shelter-money-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Shelter Money Rate Limits
  slug: shelter-money-rate-limits
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 37.4
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Shelter Money Authentication
  slug: shelter-money-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shelter Money Domain Security
  slug: shelter-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shelter Money Vulnerability Disclosure
  slug: shelter-money-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Shelter Money Trust Center
  slug: shelter-money-trust-center
  summary_line: trust center published
slug: shelter-money
tags:
- Personal Finance
- Budgeting
- Fintech
- MCP
- AI Agents
- Cash Flow Forecasting
website: https://shelter.money
---
