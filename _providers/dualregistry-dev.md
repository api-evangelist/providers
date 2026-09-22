---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dualregistry Dev Agentic Access
  operation_count: 7
  slug: dualregistry-dev-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://dualregistry.dev
  baseurl_source: declared
  description: 'The desk''s HTTP/JSON surface on https://dualregistry.dev, described by a served OpenAPI 3.0.3 stub of 7 operations (the provider''s own ai-plugin calls it "minimal") and more fully by llms.txt: a free '
  name: Scro Orphan Desk Intent Echo API
  slug: intent-echo-api
- description: An A2A 0.3.0 agent card served at https://dualregistry.dev/.well-known/agent-card.json (and byte-identical at /agent-card.json, on www. and on the legacy Vercel host) that doubles as an ERC-8004 off-c
  name: Scro Orphan Desk A2A agent card
  slug: a2a-agent
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://dualregistry.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://dualregistry.dev/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://dualregistry.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://dualregistry.dev/AGENT.md
- group: commercial
  title: ''
  type: Pricing
  url: https://dualregistry.dev/PROMO.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manhatton31-svg
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/manhatton31-svg/orphan-desk-source
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/llms/dualregistry-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dualregistry-dev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/well-known/dualregistry-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dualregistry-dev-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/a2a/dualregistry-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dualregistry-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/authentication/dualregistry-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dualregistry-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/conventions/dualregistry-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dualregistry-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/conformance/dualregistry-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dualregistry-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/errors/dualregistry-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dualregistry-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/lifecycle/dualregistry-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dualregistry-dev-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/plans/dualregistry-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dualregistry-dev-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/rate-limits/dualregistry-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dualregistry-dev-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/data-model/dualregistry-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dualregistry-dev-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/examples/dualregistry-dev-examples.yml
  title: ''
  type: Examples
  url: examples/dualregistry-dev-examples.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/overlays/dualregistry-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dualregistry-dev-openapi-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/json-schema/dualregistry-dev-fee-quote.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/dualregistry-dev-fee-quote.schema.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/regulatory/dualregistry-dev-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/dualregistry-dev-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/security/dualregistry-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dualregistry-dev-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dualregistry-dev/refs/heads/main/agentic-access/dualregistry-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dualregistry-dev-agentic-access.yml
created: '2026-09-19'
description: 'Scro Orphan Desk is a machine-only "Intent Echo resurrection desk" served from dualregistry.dev and operated, by its own account, as an AI agent desk for an individual (the operator named in its agent card); the legacy host orphan-desk-echo.vercel.app serves the same bytes. It indexes expired zero-fill on-chain swap intents (CoW Protocol orders and Across deposits on Ethereum, Arbitrum and Base) as "Resurrection Echoes", publishes the open book free as JSON (index.json, stats.json, fill_hint.json, PROMO.json, ORPHANDUST.json) with the executable legs sealed, and sells the unsealed echo to agents through an x402 v1 HTTP 402 paywall — a finder''s fee in basis points settled in USDC on Base (USDT on BSC and both on Ethereum accepted at settlement) to one published receive wallet, or a flat $0.50 "OrphanDust" unlock credit. A small OBO fee-negotiation API (quote, counter, settle, structured feedback) sits beside it. Every surface is machine-first: a served OpenAPI 3.0.3 stub (7
  operations), an A2A 0.3.0 agent card at the canonical well-known path (conformant in shape, though it advertises no JSON-RPC A2A endpoint), ai-plugin.json, llms.txt, an x402 discovery document, a JSON Schema for fee quotes, and an "mcp.json" that is a tool manifest rather than an MCP server. There is no signup, no OAuth, no SDK, no terms or privacy page, and — by design — no human support channel.'
json_schemas:
- name: Orphan Desk OBO fee quote / counter
  property_count: 0
  slug: dualregistry-dev-fee-quote.schema
layout: provider
modified: '2026-09-19'
name: Scro Orphan Desk
nav: Providers
network: true
overview: 'Scro Orphan Desk publishes 1 API on the [APIs.io](https://apis.io/) network: Intent Echo API. Tagged areas include AI Agents, x402, A2A, DeFi, and Crypto.


  Scro Orphan Desk''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, code examples, and 19 more developer resources.'
plans:
- name: Dualregistry Dev Plans Pricing
  plan_count: 1
  slug: dualregistry-dev-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Dualregistry Dev Rate Limits
  slug: dualregistry-dev-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 8.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 42.3
    discoverability: 72.2
    operational_transparency: 5.3
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dualregistry Dev Authentication
  slug: dualregistry-dev-authentication
  summary_line: none/x402-payment-proof · 3 schemes
- kind: domain-security
  name: Dualregistry Dev Domain Security
  slug: dualregistry-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dualregistry-dev
tags:
- AI Agents
- x402
- A2A
- DeFi
- Crypto
- Stablecoins
- Payments
- Intent Trading
- Machine Economy
- agent-native
website: https://dualregistry.dev/
---
