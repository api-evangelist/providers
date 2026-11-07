---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dualregistry Dev Agentic Access
  operation_count: 7
  slug: dualregistry-dev-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: An A2A 0.3.0 agent card served at https://dualregistry.dev/.well-known/agent-card.json (and byte-identical at /agent-card.json, on www. and on the legacy Vercel host) that doubles as an ERC-8004 off-c
  name: Scro Orphan Desk A2A agent card
  slug: a2a-agent
- baseURL: https://dualregistry.dev
  baseurl_source: spec
  description: The Echo API from Scro Orphan Desk — 1 operation(s) for echo.
  name: Scro Orphan Desk Echo API
  slug: dualregistry-dev-echo-api
- baseURL: https://dualregistry.dev
  baseurl_source: spec
  description: The Index.json API from Scro Orphan Desk — 1 operation(s) for index.json.
  name: Scro Orphan Desk Index.json API
  slug: dualregistry-dev-index-json-api
- baseURL: https://dualregistry.dev
  baseurl_source: spec
  description: The Orphandust API from Scro Orphan Desk — 1 operation(s) for orphandust.
  name: Scro Orphan Desk Orphandust API
  slug: dualregistry-dev-orphandust-api
- baseURL: https://dualregistry.dev
  baseurl_source: spec
  description: The Quote Fee API from Scro Orphan Desk — 1 operation(s) for quote fee.
  name: Scro Orphan Desk Quote Fee API
  slug: dualregistry-dev-quote-fee-api
- baseURL: https://dualregistry.dev
  baseurl_source: spec
  description: The Settle Fee API from Scro Orphan Desk — 1 operation(s) for settle fee.
  name: Scro Orphan Desk Settle Fee API
  slug: dualregistry-dev-settle-fee-api
- baseURL: https://dualregistry.dev
  baseurl_source: spec
  description: The Stats.json API from Scro Orphan Desk — 1 operation(s) for stats.json.
  name: Scro Orphan Desk Stats.json API
  slug: dualregistry-dev-stats-json-api
artifact_total: 17
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
  href: https://artifacts.apis.io/dualregistry-dev/llms/dualregistry-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dualregistry-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/dualregistry-dev/well-known/dualregistry-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dualregistry-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/dualregistry-dev/a2a/dualregistry-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dualregistry-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dualregistry-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/dualregistry-dev/authentication/dualregistry-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dualregistry-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/dualregistry-dev/conventions/dualregistry-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dualregistry-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/dualregistry-dev/conformance/dualregistry-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dualregistry-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/dualregistry-dev/errors/dualregistry-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dualregistry-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dualregistry-dev/lifecycle/dualregistry-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dualregistry-dev-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/dualregistry-dev/plans/dualregistry-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dualregistry-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dualregistry-dev/rate-limits/dualregistry-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dualregistry-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/dualregistry-dev/data-model/dualregistry-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dualregistry-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/dualregistry-dev/examples/dualregistry-dev-examples.yml
  title: ''
  type: Examples
  url: examples/dualregistry-dev-examples.yml
- group: other
  href: https://artifacts.apis.io/dualregistry-dev/overlays/dualregistry-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dualregistry-dev-openapi-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/dualregistry-dev/json-schema/dualregistry-dev-fee-quote.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/dualregistry-dev-fee-quote.schema.json
- group: other
  href: https://artifacts.apis.io/dualregistry-dev/regulatory/dualregistry-dev-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/dualregistry-dev-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/dualregistry-dev/security/dualregistry-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dualregistry-dev-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/dualregistry-dev/agentic-access/dualregistry-dev-agentic-access.yml
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
overview: 'Scro Orphan Desk publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Echo API, Index.json API, Orphandust API, and 4 more. Tagged areas include AI Agents, x402, A2A, DeFi, and Cryptocurrency.


  The Scro Orphan Desk catalog on APIs.io includes 1 Spectral governance ruleset.


  Scro Orphan Desk''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, code examples, and 19 more developer resources.'
plans:
- name: Dualregistry Dev Plans Pricing
  plan_count: 1
  slug: dualregistry-dev-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Dualregistry Dev Rate Limits
  slug: dualregistry-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Scro Orphan Desk API Rules
  rule_count: 27
  severity_counts:
    error: 24
    hint: 0
    info: 2
    warn: 1
  slug: dualregistry-dev-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 47.9
    catalog_earned_first_party: 8.0
    catalog_gap: 67.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 47.2
    developer_ergonomics: 31.5
    discoverability: 60.7
    operational_transparency: 5.3
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dualregistry-dev/dualregistry-dev-2026-10-11T103936.png
security:
- kind: authentication
  name: Dualregistry Dev Authentication
  slug: dualregistry-dev-authentication
  summary_line: none/x402-payment-proof · 3 schemes
- kind: domain-security
  name: Dualregistry Dev Domain Security
  slug: dualregistry-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: dualregistry-dev-buy-an-orphandust-unlock
  slug: dualregistry-dev-buy-an-orphandust-unlock
- name: dualregistry-dev-discover-and-preview-echoes
  slug: dualregistry-dev-discover-and-preview-echoes
- name: dualregistry-dev-redeem-an-echo-with-x402
  slug: dualregistry-dev-redeem-an-echo-with-x402
slug: dualregistry-dev
tags:
- AI Agents
- x402
- A2A
- DeFi
- Cryptocurrency
- Stablecoins
- Payments
- Intent Trading
- Machine Economy
- Agent-Native
website: https://dualregistry.dev/
---
