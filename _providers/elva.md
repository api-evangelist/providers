---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: Public, no-auth REST API for scoring OpenAPI documents. GET /api/review/checks returns the full set of checks; POST /api/review scores a submitted OpenAPI document with category scores, per-check brea
  name: Spec Scoring API
  slug: spec-scoring-api
artifact_total: 9
asyncapis:
- description: ''
  name: Elva Webhooks
  slug: elva-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://getelva.ai
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/elva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elva-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elva-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/elva-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elva-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elva-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elva-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elva-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/elva-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elva-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elva-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/elva-webhooks.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://getelva.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://getelva.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getelva.ai/get-started/quickstart-repo-to-mcp
- group: start
  title: ''
  type: SignUp
  url: https://getelva.ai/waitlist
- group: start
  title: ''
  type: Login
  url: https://app.getelva.ai
created: '2026-09-06'
description: 'API management platform for the agentic era: reads repos to build an API catalog, enforces per-audience contracts, generates tests, and turns APIs into governed, hosted MCP servers for AI agents. Built by Theneo. Exposes a public no-auth OpenAPI scoring REST API and an llms.txt.'
image: https://getelva.ai/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: Elva MCP
  slug: elva-mcp
modified: '2026-09-07'
name: Elva
nav: Providers
network: true
overview: 'Elva publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Management, MCP Server, MCP Logs, MCP Insights, and API Client.


  The Elva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elva''s developer surface includes authentication, pricing, engineering blog, getting-started guide, signup flow, and 15 more developer resources.'
plans:
- name: Elva Plans Pricing
  plan_count: 4
  slug: elva-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Elva Rate Limits
  slug: elva-rate-limits
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 49.5
  provenance:
    conformance: first-party
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
  name: Elva Authentication
  slug: elva-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Elva Domain Security
  slug: elva-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Elva Vulnerability Disclosure
  slug: elva-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Elva Trust Center
  slug: elva-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701
slug: elva
tags:
- API Management
- MCP Server
- MCP Logs
- MCP Insights
- API Client
- API Contract
- API Governance
- API Discovery
- OpenAPI
- API Testing
- Developer Tools
- AI Agent Infrastructure
website: https://getelva.ai
---
