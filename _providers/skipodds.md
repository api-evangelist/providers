---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Hosted Model Context Protocol server exposing the SkipOdds Index to AI assistants — stateless streamable-http at https://skipodds.com/mcp, protocol version 2025-06-18, five read-only tools (list_fixtu
  name: SkipOdds MCP Server
  slug: skipodds-mcp-server
- description: The Alerts API from SkipOdds — 1 operation(s) for alerts.
  name: SkipOdds Alerts API
  slug: skipodds-alerts-api
- description: The Fixtures API from SkipOdds — 6 operation(s) for fixtures.
  name: SkipOdds Fixtures API
  slug: skipodds-fixtures-api
- description: The Golf API from SkipOdds — 2 operation(s) for golf.
  name: SkipOdds Golf API
  slug: skipodds-golf-api
- description: The Outrights API from SkipOdds — 1 operation(s) for outrights.
  name: SkipOdds Outrights API
  slug: skipodds-outrights-api
artifact_total: 13
asyncapis:
- description: ''
  name: Skipodds Webhooks
  slug: skipodds-webhooks
collections:
- collection_type: open
  name: SkipOdds
  slug: open-skipodds
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skipodds.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://skipodds.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://skipodds.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://skipodds.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://skipodds.com/#free
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skipodds.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skipodds.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@skipodds.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skipodds-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/skipodds-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skipodds-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skipodds-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skipodds-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skipodds-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skipodds-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skipodds-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skipodds-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/skipodds-packages.yml
- group: design
  title: ''
  type: Components
  url: components/skipodds-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/skipodds-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skipodds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skipodds-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/skipodds-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/skipodds-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skipodds-domain-security.yml
created: '2026-07-17'
description: 'SkipOdds is a sports-odds data API from SkipSeek Inc. that publishes de-vigged consensus win probabilities — the SkipOdds Index — across 13 sports: soccer, American football, basketball, baseball, hockey, college football, college basketball, tennis, golf, cricket, rugby, MMA and boxing. Every surveyed bookmaker price for a market is averaged and stripped of its margin so the returned probabilities sum to exactly 100%, with fair decimal odds, the number of books surveyed, and the margin removed carried alongside. The surface covers fixtures, tournament outrights, line movement over a configurable window, and threshold-triggered webhook alerts, and is offered three ways: a public OpenAPI 3.0.3 REST contract, an anonymous streamable-http MCP server, and a keyless embeddable widget. Data is informational only — no bets are taken, no funds held, and no bookmaker names exposed.'
image: https://skipodds.com/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: SkipOdds MCP Server
  slug: skipodds-mcp-server
- description: ''
  name: SkipOdds MCP Server
  slug: skipodds-mcp-server-2
modified: '2026-08-11'
name: SkipOdds
nav: Providers
network: true
overview: 'SkipOdds publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Fixtures API, Golf API, and 1 more. Tagged areas include Sports, Odds, probabilities, betting-data, and de-vig.


  The SkipOdds catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SkipOdds'' developer surface includes documentation, API reference, pricing, signup flow, support, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Skipodds Plans Pricing
  plan_count: 6
  slug: skipodds-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Skipodds Rate Limits
  slug: skipodds-rate-limits
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.9
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 4.5
    contract_quality: 62.6
    developer_ergonomics: 51.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 56.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skipodds/refs/heads/main/screenshots/skipodds-2026-08-17T081914.png
security:
- kind: authentication
  name: Skipodds Authentication
  slug: skipodds-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Skipodds Domain Security
  slug: skipodds-domain-security
  summary_line: TLSv1.3
slug: skipodds
tags:
- Sports
- Odds
- probabilities
- betting-data
- de-vig
- sports-data
- Real-Time
- Webhook
- sports-betting
- MCP
- Agent Ready
- Market Data
website: https://skipodds.com/docs
---
