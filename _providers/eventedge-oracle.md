---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: Unsigned calldata for the customer's own wallet to send.
  name: EventEdge Oracle Cancellation API
  slug: eventedge-oracle-cancellation-api
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: A single payment to a single recipient.
  name: EventEdge Oracle One-time payments API
  slug: eventedge-oracle-one-time-payments-api
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: Signed once by the customer, charged by your renewal job.
  name: EventEdge Oracle Recurring payments API
  slug: eventedge-oracle-recurring-payments-api
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: A transfer from the merchant's own wallet back to the wallet that paid.
  name: EventEdge Oracle Refunds API
  slug: eventedge-oracle-refunds-api
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: Liveness.
  name: EventEdge Oracle Service API
  slug: eventedge-oracle-service-api
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: The Subscriptions API from EventEdge Oracle — 1 operation(s) for subscriptions.
  name: EventEdge Oracle Subscriptions API
  slug: eventedge-oracle-subscriptions-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://edge.arakelproof.space/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eventedge-oracle/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eventedge-oracle/refs/heads/main/overlays/eventedge-oracle-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eventedge-oracle-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://edge.arakelproof.space
created: '2026-09-15'
description: Read-only, machine-readable prediction-market context (Polymarket + Kalshi) built for autonomous AI agents. Provides decision-support data only (no trade execution), accessed via the x402 pay-per-request payment protocol (USDC on Base). Exposes a REST API (OpenAPI 3.1), a live remote MCP server, an A2A agent card backed by a live /a2a JSON-RPC endpoint, and llms.txt / ai-plugin / x402 discovery surfaces.
layout: provider
mcp_servers:
- description: ''
  name: EventEdge Oracle MCP Server
  slug: eventedge-oracle-mcp-server
modified: '2026-09-15'
name: EventEdge Oracle
nav: Providers
network: true
overview: EventEdge Oracle publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cancellation API, One-time payments API, Recurring payments API, and 3 more. Tagged areas include Prediction Markets, x402, AI Agents, Polymarket, and Kalshi.
plans:
- name: Eventedge Oracle Plans Pricing
  plan_count: 0
  slug: eventedge-oracle-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Eventedge Oracle Rate Limits
  slug: eventedge-oracle-rate-limits
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 51.6
    developer_ergonomics: 25.6
    discoverability: 72.2
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Eventedge Oracle Authentication
  slug: eventedge-oracle-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Eventedge Oracle Domain Security
  slug: eventedge-oracle-domain-security
  summary_line: TLSv1.3
slug: eventedge-oracle
tags:
- Prediction Markets
- x402
- AI Agents
- Polymarket
- Kalshi
- market-context
- Decision Support
- Finance
website: https://edge.arakelproof.space
---
