---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gonna Bond Agentic Access
  operation_count: 24
  slug: gonna-bond-agentic-access
  summary_line: 24 operations · 3 acting
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://legit.gonna.bond/mcp (stateless JSON-RPC 2.0 over HTTP POST; initialize reports protocolVersion 2024-11-05, serverInfo legit 1.0.0, capabilities tools o
  name: LEGIT MCP Server
  slug: legit-mcp-server
- description: 'Agent card served from https://legit.gonna.bond/.well-known/agent.json and, byte-identical, from the canonical /.well-known/agent-card.json: name LEGIT, version 0.1.0, provider organization GONNA, cap'
  name: LEGIT A2A Agent Card
  slug: legit-a2a-agent
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Arena API from GONNA — 2 operation(s) for arena.
  name: GONNA Arena API
  slug: gonna-bond-arena-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Batch Check API from GONNA — 1 operation(s) for batch check.
  name: GONNA Batch Check API
  slug: gonna-bond-batch-check-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Chain Logos API from GONNA — 1 operation(s) for chain logos.
  name: GONNA Chain Logos API
  slug: gonna-bond-chain-logos-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Check API from GONNA — 1 operation(s) for check.
  name: GONNA Check API
  slug: gonna-bond-check-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Compare API from GONNA — 1 operation(s) for compare.
  name: GONNA Compare API
  slug: gonna-bond-compare-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Deep Check API from GONNA — 1 operation(s) for deep check.
  name: GONNA Deep Check API
  slug: gonna-bond-deep-check-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Health API from GONNA — 1 operation(s) for health.
  name: GONNA Health API
  slug: gonna-bond-health-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The History API from GONNA — 1 operation(s) for history.
  name: GONNA History API
  slug: gonna-bond-history-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Leaderboard API from GONNA — 1 operation(s) for leaderboard.
  name: GONNA Leaderboard API
  slug: gonna-bond-leaderboard-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Merchant API from GONNA — 1 operation(s) for merchant.
  name: GONNA Merchant API
  slug: gonna-bond-merchant-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Networks API from GONNA — 1 operation(s) for networks.
  name: GONNA Networks API
  slug: gonna-bond-networks-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Pulse API from GONNA — 1 operation(s) for pulse.
  name: GONNA Pulse API
  slug: gonna-bond-pulse-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Receipts API from GONNA — 1 operation(s) for receipts.
  name: GONNA Receipts API
  slug: gonna-bond-receipts-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Referee API from GONNA — 2 operation(s) for referee.
  name: GONNA Referee API
  slug: gonna-bond-referee-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Report API from GONNA — 1 operation(s) for report.
  name: GONNA Report API
  slug: gonna-bond-report-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Route API from GONNA — 1 operation(s) for route.
  name: GONNA Route API
  slug: gonna-bond-route-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Stats API from GONNA — 1 operation(s) for stats.
  name: GONNA Stats API
  slug: gonna-bond-stats-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Trending API from GONNA — 1 operation(s) for trending.
  name: GONNA Trending API
  slug: gonna-bond-trending-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Watch API from GONNA — 1 operation(s) for watch.
  name: GONNA Watch API
  slug: gonna-bond-watch-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The Watches API from GONNA — 2 operation(s) for watches.
  name: GONNA Watches API
  slug: gonna-bond-watches-api
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: The .well Known API from GONNA — 1 operation(s) for .well known.
  name: GONNA .well Known API
  slug: gonna-bond-well-known-api
artifact_total: 36
asyncapis:
- description: ''
  name: Gonna Bond Watch Webhooks
  slug: gonna-bond-watch-webhooks
common:
- group: other
  href: https://artifacts.apis.io/gonna-bond/capabilities/gonna-bond-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gonna-bond-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/gonna-bond/overlays/gonna-bond-legit-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gonna-bond-legit-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/gonna-bond/agentic-access/gonna-bond-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gonna-bond-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gonna-bond/security/gonna-bond-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gonna-bond-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gonna-bond/well-known/gonna-bond-security.txt
  title: ''
  type: Security
  url: well-known/gonna-bond-security.txt
- group: start
  href: https://artifacts.apis.io/gonna-bond/sandbox/gonna-bond-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gonna-bond-sandbox.yml
- group: company
  title: ''
  type: Website
  url: https://gonna.bond/
- group: docs
  title: ''
  type: Documentation
  url: https://legit.gonna.bond/docs
- group: docs
  title: ''
  type: APIReference
  url: https://legit.gonna.bond/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://legit.gonna.bond/.well-known/legit
- group: operate
  title: ''
  type: Community
  url: https://t.me/GONNAFI
- group: company
  title: ''
  type: Twitter
  url: https://x.com/gonnalgo
- group: other
  href: https://artifacts.apis.io/gonna-bond/a2a/gonna-bond-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gonna-bond-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gonna-bond/mcp/gonna-bond-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gonna-bond-mcp.yml
- group: build
  href: https://artifacts.apis.io/gonna-bond/mcp/gonna-bond-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gonna-bond-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gonna-bond/llms/gonna-bond-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gonna-bond-llms.txt
- group: agent
  href: https://artifacts.apis.io/gonna-bond/well-known/gonna-bond-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gonna-bond-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gonna-bond/well-known/gonna-bond-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gonna-bond-security.txt
- group: other
  href: https://artifacts.apis.io/gonna-bond/well-known/gonna-bond-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/gonna-bond-x402.json
- group: design
  href: https://artifacts.apis.io/gonna-bond/asyncapi/gonna-bond-watch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gonna-bond-watch-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/gonna-bond/authentication/gonna-bond-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gonna-bond-authentication.yml
- group: design
  href: https://artifacts.apis.io/gonna-bond/conventions/gonna-bond-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gonna-bond-conventions.yml
- group: design
  href: https://artifacts.apis.io/gonna-bond/errors/gonna-bond-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gonna-bond-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gonna-bond/data-model/gonna-bond-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gonna-bond-data-model.yml
- group: design
  href: https://artifacts.apis.io/gonna-bond/components/gonna-bond-components.yml
  title: ''
  type: Components
  url: components/gonna-bond-components.yml
- group: operate
  href: https://artifacts.apis.io/gonna-bond/rate-limits/gonna-bond-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gonna-bond-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gonna-bond/plans/gonna-bond-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gonna-bond-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gonna-bond/conformance/gonna-bond-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gonna-bond-conformance.yml
- group: design
  href: https://artifacts.apis.io/gonna-bond/lifecycle/gonna-bond-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gonna-bond-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/gonna-bond/packages/gonna-bond-packages.yml
  title: ''
  type: Packages
  url: packages/gonna-bond-packages.yml
- group: agent
  href: https://artifacts.apis.io/gonna-bond/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/gonna-bond/security/gonna-bond-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gonna-bond-domain-security.yml
- group: other
  href: https://artifacts.apis.io/gonna-bond/regulatory/gonna-bond-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/gonna-bond-regulatory-posture.yml
created: '2026-09-19'
description: 'GONNA is an Algorand-native meme-coin and games community ($GONNA, Algorand ASA 2582294183; the "GONNAVERSE" at gonna.bond) that builds and operates LEGIT, a trust oracle for the x402 agentic economy at legit.gonna.bond. LEGIT trust-checks any x402 merchant or agent address across Algorand, Base, Solana and 17 other chains before a payment is routed: grades (A+ to F) and scores (0-100) are built from live uptime, latency and payment-coherence probes rather than self-reported data. The surface is exposed three ways from one host: a 24-operation OpenAPI 3.1.0 REST contract at https://legit.gonna.bond/openapi.json (free reads; five verdict endpoints paid per call in USDC over x402, $0.004 on Algorand / $0.005 on Base, no accounts or API keys), a remote MCP server at https://legit.gonna.bond/mcp answering an anonymous tools/list with four tools, and an A2A-style agent card at /.well-known/agent.json and /.well-known/agent-card.json. The apex site gonna.bond is a JavaScript-rendered
  community page with no API surface of its own.'
finops:
- has_sources: true
  method: derived
  name: Gonna Bond Finops
  primary_unit: ''
  service_category: ''
  slug: gonna-bond-finops
  template: true
image: https://legit.gonna.bond/favicon.png
layout: provider
mcp_servers:
- description: 'LEGIT operates ONE remote MCP server at https://legit.gonna.bond/mcp: stateless JSON-RPC 2.0 over HTTP POST, no session, no authentication. An anonymous initialize answered protocolVersion 2024-11-05 '
  name: GONNA MCP Server
  slug: gonna-bond-mcp-yml
modified: '2026-09-19'
name: GONNA
nav: Providers
network: true
overview: 'GONNA publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Arena API, Batch Check API, Chain Logos API, and 20 more. Tagged areas include Company, Agents, Agentic Commerce, x402, and Trust.


  The GONNA catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  GONNA''s developer surface includes sandbox, documentation, API reference, pricing, authentication, and 28 more developer resources.'
plans:
- name: Gonna Bond Plans Pricing
  plan_count: 2
  slug: gonna-bond-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Gonna Bond Rate Limits
  slug: gonna-bond-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: GONNA API Rules
  rule_count: 52
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 4
  slug: gonna-bond-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 26.3
    contract_governance: 31.8
    contract_quality: 54.4
    developer_ergonomics: 31.5
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gonna-bond/gonna-bond-2026-10-11T104949.png
security:
- kind: authentication
  name: Gonna Bond Authentication
  slug: gonna-bond-authentication
  summary_line: none/x402 · 3 schemes
- kind: domain-security
  name: Gonna Bond Domain Security
  slug: gonna-bond-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gonna Bond Vulnerability Disclosure
  slug: gonna-bond-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Pay for a LEGIT verdict over x402
  slug: gonna-bond-pay-per-call-x402
- name: Pre-payment trust check
  slug: gonna-bond-pre-payment-trust-check
- name: Watch a merchant with a webhook-armed sentinel
  slug: gonna-bond-watch-sentinel
slug: gonna-bond
tags:
- Company
- Agents
- Agentic Commerce
- x402
- Trust
- Merchant Trust
- MCP
- A2A
- Algorand
- Blockchain
- Payments
- Agent-Native
website: https://gonna.bond/
---
