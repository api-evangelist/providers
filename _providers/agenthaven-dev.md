---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Agenthaven Dev Agentic Access
  operation_count: 2
  slug: agenthaven-dev-agentic-access
  summary_line: 2 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Seller agent for flight search and travel checkout, exposed on one host through two protocol doors: A2A JSON-RPC 0.3 at https://travel.agenthaven.dev/a2a (message/send with a DataPart {action, input} '
  name: Agent Bench Travel Merchant
  slug: agent-bench-travel-merchant
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://agenthaven.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://travel.agenthaven.dev/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/a2a/agenthaven-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenthaven-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/mcp/agenthaven-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenthaven-dev-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/agentic-access/agenthaven-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenthaven-dev-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/well-known/agenthaven-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenthaven-dev-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/llms/agenthaven-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenthaven-dev-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/authentication/agenthaven-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenthaven-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/conventions/agenthaven-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agenthaven-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/conventions/agenthaven-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agenthaven-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/errors/agenthaven-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenthaven-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/data-model/agenthaven-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenthaven-dev-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/rate-limits/agenthaven-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agenthaven-dev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/plans/agenthaven-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenthaven-dev-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/sandbox/agenthaven-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agenthaven-dev-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/conformance/agenthaven-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenthaven-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/lifecycle/agenthaven-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agenthaven-dev-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agenthaven-dev/refs/heads/main/security/agenthaven-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenthaven-dev-domain-security.yml
created: '2026-09-19'
description: 'Agent Bench operates agenthaven.dev, a DNSSEC-signed zone that publishes AI agents through DNS-AID, and runs one live agent in it: the Agent Bench Travel Merchant at travel.agenthaven.dev — a proof-of-concept seller agent that quotes real flight fares (Google Flights via SerpApi) and turns a chosen quote into a Stripe test-mode payment intent under a buyer-supplied spending mandate. It is reachable over A2A (JSON-RPC 0.3, agent card at the canonical well-known path, pinned by SHA-256 digest and ES256 signature in the DNS SVCB record) and MCP (2025-06-18, two tools with full input and output schemas, anonymous tools/list). It publishes a SPIFFE JWT-SVID for the running instance, DANE TLSA pins, an ARD trust catalog, a GoDaddy ANS registration and a public hash-chained ledger of every quote, refusal and checkout. No OpenAPI, no SDKs, no pricing; no real money moves and no ticket is issued.'
layout: provider
mcp_servers:
- description: ''
  name: Agent Bench MCP Server
  slug: agent-bench-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP, POST only)
  slug: mcp-endpoint-streamable-http-post-only
modified: '2026-09-19'
name: Agent Bench
nav: Providers
network: true
overview: 'Agent Bench publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, A2A, MCP, Agentic Commerce, and DNS-AID.


  Agent Bench''s developer surface includes documentation, authentication, sandbox, and 16 more developer resources.'
plans:
- name: Agenthaven Dev Plans Pricing
  plan_count: 0
  slug: agenthaven-dev-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Agenthaven Dev Rate Limits
  slug: agenthaven-dev-rate-limits
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    operational_transparency: 31.6
  previous_composite: 2.8
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenthaven Dev Authentication
  slug: agenthaven-dev-authentication
  summary_line: none/http-bearer-jwt · 2 schemes
- kind: domain-security
  name: Agenthaven Dev Domain Security
  slug: agenthaven-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: agenthaven-dev
tags:
- Agents
- A2A
- MCP
- Agentic Commerce
- DNS-AID
- Travel
- Flights
- Payments
- Agent Identity
- Proof of Concept
- agent-native
website: https://agenthaven.dev/
---
