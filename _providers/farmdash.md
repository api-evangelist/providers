---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 2
  name: Farmdash Agentic Access
  operation_count: 73
  slug: farmdash-agentic-access
  summary_line: 73 operations · 29 acting · 2 human-in-the-loop
api_count: 6
apis:
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Hyperliquid account state and risk management
  name: FarmDash Agent Hub Account API
  slug: farmdash-account-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Policy-bounded loop configuration and execution
  name: FarmDash Agent Hub Autopilot API
  slug: farmdash-autopilot-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Hyperliquid wallet delegation
  name: FarmDash Agent Hub Delegation API
  slug: farmdash-delegation-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Futures order execution and cancellation
  name: FarmDash Agent Hub Execution API
  slug: farmdash-execution-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: The ExecutionAuthority API from FarmDash Agent Hub — 1 operation(s) for executionauthority.
  name: FarmDash Agent Hub Execution Authority API
  slug: farmdash-executionauthority-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Fee event history and revenue metrics
  name: FarmDash Agent Hub History API
  slug: farmdash-history-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Trail Heat protocol data and chain analytics
  name: FarmDash Agent Hub Intelligence API
  slug: farmdash-intelligence-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: The Planning API from FarmDash Agent Hub — 2 operation(s) for planning.
  name: FarmDash Agent Hub Planning API
  slug: farmdash-planning-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: The Proof API from FarmDash Agent Hub — 3 operation(s) for proof.
  name: FarmDash Agent Hub Proof API
  slug: farmdash-proof-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: The Reputation API from FarmDash Agent Hub — 1 operation(s) for reputation.
  name: FarmDash Agent Hub Reputation API
  slug: farmdash-reputation-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Futures market research — funding rates, technical indicators
  name: FarmDash Agent Hub Research API
  slug: farmdash-research-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Pre-trade risk analysis, alerts, and execution guardrails
  name: FarmDash Agent Hub Risk API
  slug: farmdash-risk-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Bounded session management
  name: FarmDash Agent Hub Session API
  slug: farmdash-session-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Strategy analysis and position sizing
  name: FarmDash Agent Hub Strategy API
  slug: farmdash-strategy-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Token swap quotes, execution, and confirmation
  name: FarmDash Agent Hub Swap API
  slug: farmdash-swap-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: The Wallet API from FarmDash Agent Hub — 1 operation(s) for wallet.
  name: FarmDash Agent Hub Wallet API
  slug: farmdash-wallet-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: The Agent API from FarmDash Agent Hub — 1 operation(s) for agent.
  name: FarmDash Agent Hub Agent API
  slug: farmdash-agent-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Payment kernel access rails — native-ETH payment intents, FarmDash prepaid credit, and the single-use execution-bootstrap grant. Describes settlement only; implies nothing about autonomous-execution r
  name: FarmDash Agent Hub Payments API
  slug: farmdash-payments-api
artifact_total: 50
common:
- group: commercial
  href: https://artifacts.apis.io/farmdash/finops/farmdash-finops.yml
  title: ''
  type: FinOps
  url: finops/farmdash-finops.yml
- group: other
  href: https://artifacts.apis.io/farmdash/a2a/farmdash-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/farmdash-a2a.yml
- group: build
  href: https://artifacts.apis.io/farmdash/integrations/farmdash-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/farmdash-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/farmdash/capabilities/farmdash-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/farmdash-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/farmdash/changelog/farmdash-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/farmdash-changelog.yml
- group: agent
  href: https://artifacts.apis.io/farmdash/agentic-access/farmdash-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/farmdash-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/farmdash/rules/farmdash-rules.yml
  title: ''
  type: Spectral
  url: rules/farmdash-rules.yml
- group: design
  href: https://artifacts.apis.io/farmdash/json-ld/farmdash-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/farmdash-context.jsonld
- group: design
  href: https://artifacts.apis.io/farmdash/vocabulary/farmdash-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/farmdash-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/farmdash/conventions/farmdash-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/farmdash-conventions.yml
- group: operate
  href: https://artifacts.apis.io/farmdash/lifecycle/farmdash-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/farmdash-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/farmdash/hosts/farmdash-hosts.yml
  title: ''
  type: Hosts
  url: hosts/farmdash-hosts.yml
- group: other
  href: https://artifacts.apis.io/farmdash/vendors/farmdash-vendors.yml
  title: ''
  type: Vendors
  url: vendors/farmdash-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.farmdash.one/status
- group: auth
  title: ''
  type: Security
  url: https://www.farmdash.one/security
- group: company
  title: ''
  type: Website
  url: https://www.farmdash.one/
- group: other
  title: ''
  type: APIsJSON
  url: https://www.farmdash.one/apis.json
- group: agent
  href: https://artifacts.apis.io/farmdash/mcp/farmdash-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/farmdash-mcp.yml
- group: other
  href: https://artifacts.apis.io/farmdash/overlays/farmdash-agent-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/farmdash-agent-api-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://www.farmdash.one/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.farmdash.one/agents
- group: docs
  title: ''
  type: APIReference
  url: https://www.farmdash.one/agents/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.farmdash.one/agents
- group: commercial
  title: ''
  type: Pricing
  url: https://www.farmdash.one/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.farmdash.one/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.farmdash.one/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/AR6hVaDj
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.farmdash.one/updates
- group: commercial
  href: https://artifacts.apis.io/farmdash/plans/farmdash-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/farmdash-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/farmdash/rate-limits/farmdash-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/farmdash-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/farmdash/well-known/farmdash-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/farmdash-well-known.yml
- group: design
  href: https://artifacts.apis.io/farmdash/conformance/farmdash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/farmdash-conformance.yml
- group: design
  href: https://artifacts.apis.io/farmdash/lifecycle/farmdash-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/farmdash-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/farmdash/conventions/farmdash-conventions.yml
  title: ''
  type: Conventions
  url: conventions/farmdash-conventions.yml
- group: design
  href: https://artifacts.apis.io/farmdash/errors/farmdash-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/farmdash-problem-types.yml
- group: design
  href: https://artifacts.apis.io/farmdash/data-model/farmdash-data-model.yml
  title: ''
  type: DataModel
  url: data-model/farmdash-data-model.yml
- group: start
  href: https://artifacts.apis.io/farmdash/sandbox/farmdash-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/farmdash-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/farmdash/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/farmdash/authentication/farmdash-authentication.yml
  title: ''
  type: Authentication
  url: authentication/farmdash-authentication.yml
- group: auth
  href: https://artifacts.apis.io/farmdash/security/farmdash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmdash-domain-security.yml
created: '2026-08-26'
description: 'FarmDash is a zero-custody intelligence and control layer for DeFi agents and airdrop farmers, combining Trail Heat opportunity scoring, Signal Architect swap routing, wallet and Sybil-risk intelligence, and Hyperliquid futures research across EVM, Solana, HyperEVM and StarkNet. It is one of the most thoroughly agent-instrumented providers in the catalog: a live OpenAPI 3.1.0 with 54 operations (75 across four published OpenAPI documents, the swap and futures specialist contracts restating operations of the primary one), a 94-tool MCP manifest carrying full input schemas, ten MIT-licensed OpenClaw skill contracts, a legacy agent capability manifest at the former A2A path (FarmDash exposes no A2A message transport), an ai-plugin manifest, llms.txt, ai.txt, a machine-readable agent report, and a runtime capability contract that the provider declares authoritative over tool discovery. Auth is tiered API keys (Scout free / Pioneer $39.99 / Syndicate $199, all USDC) with a verified
  live x402 machine-payment fallback settling on Base. Writes are gated by mandatory pre-execution simulation and user-held EIP-191/EIP-712 signatures — FarmDash never broadcasts and never holds keys.'
finops:
- has_sources: true
  method: derived
  name: Farmdash Finops
  primary_unit: requests
  service_category: ''
  slug: farmdash-finops
  template: false
image: https://www.farmdash.one/og-wagon-preview.png?v=20260425
json_schemas:
- name: CancelOrderResponse
  property_count: 10
  slug: farmdash-cancel-order-response
- name: ConfirmRequest
  property_count: 5
  slug: farmdash-confirm-request
- name: ExecuteOrderResponse
  property_count: 9
  slug: farmdash-execute-order-response
- name: FirmQuoteResponse
  property_count: 18
  slug: farmdash-firm-quote-response
- name: MarketEstimateResponse
  property_count: 27
  slug: farmdash-market-estimate-response
- name: ReconcileOrderRequest
  property_count: 6
  slug: farmdash-reconcile-order-request
- name: ReconcileOrderResponse
  property_count: 7
  slug: farmdash-reconcile-order-response
- name: SwapRequest
  property_count: 20
  slug: farmdash-swap-request
jsonld:
- class_count: 77
  name: Farmdash Context
  property_count: 390
  slug: farmdash-context
layout: provider
mcp_servers:
- description: 'FarmDash MCP server for zero-custody DeFi agent intelligence and control: Trail Heat discovery, wallet intelligence, typed adapter validation, policy checks, simulations, EIP-712 approval queues and x'
  name: FarmDash Agent Hub MCP Server
  slug: farmdash-mcp-yml
modified: '2026-10-19'
name: FarmDash Agent Hub
nav: Providers
network: true
overview: 'FarmDash Agent Hub publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Autopilot API, Delegation API, and 15 more. Tagged areas include DeFi, DeFAI, AI Agents, MCP, and OpenAPI.


  The FarmDash Agent Hub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FarmDash Agent Hub''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, support, sandbox, and 33 more developer resources.'
plans:
- name: Farmdash Plans Pricing
  plan_count: 3
  slug: farmdash-plans-pricing
- name: Farmdash Price Estimates
  plan_count: 2
  slug: farmdash-price-estimates
random_paper: 22
rate_limits:
- limit_count: 3
  name: Farmdash Rate Limits
  slug: farmdash-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: FarmDash Agent Hub API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 3
  slug: farmdash-rules
score:
  band: strong
  composite: 64.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 92.8
    catalog_earned_first_party: 24.0
    catalog_gap: 22.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 69.6
    developer_ergonomics: 64.3
    discoverability: 76.7
    operational_transparency: 68.4
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 45.0
      total: 40
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/farmdash/farmdash-2026-09-02T145504.png
security:
- kind: authentication
  name: Farmdash Authentication
  slug: farmdash-authentication
  summary_line: http/apiKey-literal/wallet-signature/http-payment · 7 schemes
- kind: domain-security
  name: Farmdash Domain Security
  slug: farmdash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 14
skills:
- name: farmdash-autonomous-operator
  slug: farmdash-autonomous-operator
- name: farmdash-camp-guard
  slug: farmdash-camp-guard
- name: farmdash-futures-strategist
  slug: farmdash-futures-strategist
- name: farmdash-guarded-futures
  slug: farmdash-guarded-futures
- name: farmdash-hedge-warden
  slug: farmdash-hedge-warden
- name: farmdash-ledger-keeper
  slug: farmdash-ledger-keeper
- name: farmdash-signal-architect
  slug: farmdash-signal-architect
- name: farmdash-supply-master
  slug: farmdash-supply-master
- name: farmdash-trail-heat-research
  slug: farmdash-trail-heat-research
- name: farmdash-trail-intelligence
  slug: farmdash-trail-intelligence
- name: farmdash-trail-marshal
  slug: farmdash-trail-marshal
- name: farmdash-wagon-steward
  slug: farmdash-wagon-steward
- name: farmdash-x402-payment
  slug: farmdash-x402-payment
- name: farmdash-zero-custody-swap
  slug: farmdash-zero-custody-swap
slug: farmdash
tags:
- DeFi
- DeFAI
- AI Agents
- MCP
- OpenAPI
- x402
- Blockchain
- Cryptocurrency
- airdrop tracking
- Developer Tools
- Agent Readiness
- Machine Payments
- Hyperliquid
- Wallet Intelligence
- zero custody
website: https://www.farmdash.one/
---
