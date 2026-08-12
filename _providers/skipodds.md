---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: API-key-authenticated REST API returning de-vigged consensus sports probabilities, fixtures, outrights, line movement, and webhook alerts across 13 sports. Public OpenAPI 3.0.3 contract with 11 operat
  name: SkipOdds REST API
  slug: skipodds-rest-api
- description: Hosted Model Context Protocol server exposing the SkipOdds Index to AI assistants — stateless streamable-http at https://skipodds.com/mcp, protocol version 2025-06-18, five read-only tools (list_fixtu
  name: SkipOdds MCP Server
  slug: skipodds-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Skipodds Webhooks
  slug: skipodds-webhooks
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
  name: mcp
  slug: mcp
- description: ''
  name: skipodds-mcp.yml
  slug: skipodds-mcpyml
modified: '2026-08-11'
name: SkipOdds
nav: Providers
network: true
overview: 'SkipOdds publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include sports, odds, probabilities, betting-data, and de-vig.


  The SkipOdds catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SkipOdds'' developer surface includes documentation, API reference, pricing, signup flow, support, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Skipodds Plans Pricing
  plan_count: 6
  slug: skipodds-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Skipodds Rate Limits
  slug: skipodds-rate-limits
score:
  band: strong
  composite: 57.2
  delta: 43.2
  facets:
    commercial_clarity: 76.3
    contract_quality: 61.9
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 14.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: rising
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
- sports
- odds
- probabilities
- betting-data
- de-vig
- sports-data
- real-time
- webhooks
- sports-betting
- mcp
- agent-ready
- market-data
website: https://skipodds.com/docs
---
