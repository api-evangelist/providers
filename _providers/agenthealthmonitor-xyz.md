---
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Agenthealthmonitor Xyz Agentic Access
  operation_count: 80
  slug: agenthealthmonitor-xyz-agentic-access
  summary_line: 80 operations · 14 acting
api_count: 4
apis:
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Internal admin endpoints protected by X-Internal-Key header. Security activity logs, trust registry, and registry scan triggers.
  name: Agent Health Monitor Admin API
  slug: agenthealthmonitor-xyz-admin-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Subscribe wallets to automated health monitoring with webhook alerts. Health checks run every 6 hours; alerts fire when configurable thresholds are breached.
  name: Agent Health Monitor Alerts API
  slug: agenthealthmonitor-xyz-alerts-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Stripe checkout webhooks and API key management for fiat-paid access.
  name: Agent Health Monitor Billing API
  slug: agenthealthmonitor-xyz-billing-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Partner coupon routes — access any paid endpoint for free with a valid coupon code. Rate-limited to 5 requests per IP per minute.
  name: Agent Health Monitor Coupon Access API
  slug: agenthealthmonitor-xyz-coupon-access-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Service discovery, pricing info, ecosystem statistics, and x402/ERC-8004 well-known documents for automated agent registration.
  name: Agent Health Monitor Discovery & Info API
  slug: agenthealthmonitor-xyz-discovery-info-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: The Health API from Agent Health Monitor — 1 operation(s) for health.
  name: Agent Health Monitor Health API
  slug: agenthealthmonitor-xyz-health-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Wallet health diagnosis, hygiene scans, composite Agent Health Score (AHS), and visual report cards. Core analysis endpoints from $0.50 to $2.00.
  name: Agent Health Monitor Health & Hygiene API
  slug: agenthealthmonitor-xyz-health-hygiene-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Gas optimization reports and failed-transaction retry bot. Returns per-transaction-type savings and ready-to-sign EIP-1559 retry payloads.
  name: Agent Health Monitor Optimization API
  slug: agenthealthmonitor-xyz-optimization-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: The Outputs API from Agent Health Monitor — 1 operation(s) for outputs.
  name: Agent Health Monitor Outputs API
  slug: agenthealthmonitor-xyz-outputs-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Autonomous protection agent that triages risk and runs the appropriate combination of health, optimization, and retry services automatically.
  name: Agent Health Monitor Protection API
  slug: agenthealthmonitor-xyz-protection-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Risk scoring, counterparty analysis, and wallet network mapping. Fast pre-flight checks from $0.001 to deep Nansen-enriched analysis at $0.10.
  name: Agent Health Monitor Scoring & Risk API
  slug: agenthealthmonitor-xyz-scoring-risk-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: The Specs API from Agent Health Monitor — 1 operation(s) for specs.
  name: Agent Health Monitor Specs API
  slug: agenthealthmonitor-xyz-specs-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: Health checks and AI chat assistant.
  name: Agent Health Monitor Utility API
  slug: agenthealthmonitor-xyz-utility-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: The Verdicts API from Agent Health Monitor — 1 operation(s) for verdicts.
  name: Agent Health Monitor Verdicts API
  slug: agenthealthmonitor-xyz-verdicts-api
artifact_total: 21
asyncapis:
- description: ''
  name: Agenthealthmonitor Xyz Alerts Webhooks
  slug: agenthealthmonitor-xyz-alerts-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/overlays/agenthealthmonitor-xyz-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agenthealthmonitor-xyz-openapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/overlays/agenthealthmonitor-xyz-verify-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agenthealthmonitor-xyz-verify-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/agentic-access/agenthealthmonitor-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenthealthmonitor-xyz-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://agenthealthmonitor.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agenthealthmonitor.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agenthealthmonitor.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://agenthealthmonitor.xyz/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agenthealthmonitor.xyz/#getting-started
- group: start
  title: ''
  type: Console
  url: https://agenthealthmonitor.xyz/app
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.agenthealthmonitor.xyz/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://agenthealthmonitor.xyz/pay-by-card
- group: operate
  title: ''
  type: Roadmap
  url: https://agenthealthmonitor.xyz/roadmap
- group: company
  title: ''
  type: Blog
  url: https://blog.agenthealthmonitor.xyz/
- group: operate
  title: ''
  type: Support
  url: https://docs.agenthealthmonitor.xyz/#design-partner
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moonshot-cyber
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/moonshot-cyber/agent-health-monitor
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/openapi/agenthealthmonitor-xyz-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/agenthealthmonitor-xyz-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/a2a/agenthealthmonitor-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenthealthmonitor-xyz-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://agenthealthmonitor.xyz/.well-known/agent.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/mcp/agenthealthmonitor-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenthealthmonitor-xyz-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/well-known/agenthealthmonitor-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenthealthmonitor-xyz-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/llms/agenthealthmonitor-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenthealthmonitor-xyz-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/packages/agenthealthmonitor-xyz-packages.yml
  title: ''
  type: Packages
  url: packages/agenthealthmonitor-xyz-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/packages/agenthealthmonitor-xyz-packages.yml
  title: ''
  type: SDKs
  url: packages/agenthealthmonitor-xyz-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/authentication/agenthealthmonitor-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenthealthmonitor-xyz-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/conventions/agenthealthmonitor-xyz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agenthealthmonitor-xyz-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/errors/agenthealthmonitor-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenthealthmonitor-xyz-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/data-model/agenthealthmonitor-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenthealthmonitor-xyz-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/rate-limits/agenthealthmonitor-xyz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agenthealthmonitor-xyz-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/plans/agenthealthmonitor-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenthealthmonitor-xyz-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/conformance/agenthealthmonitor-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenthealthmonitor-xyz-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/lifecycle/agenthealthmonitor-xyz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agenthealthmonitor-xyz-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/asyncapi/agenthealthmonitor-xyz-alerts-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agenthealthmonitor-xyz-alerts-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/security/agenthealthmonitor-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenthealthmonitor-xyz-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agenthealthmonitor-xyz/refs/heads/main/regulatory/agenthealthmonitor-xyz-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/agenthealthmonitor-xyz-regulatory-posture.yml
created: '2026-09-19'
description: 'Digital Intensity Ltd operates Agent Health Monitor (AHM, agenthealthmonitor.xyz), trust and health verification for autonomous agents on Base L2. Fourteen pay-per-call REST endpoints score any agent wallet: quick and premium risk scores (Nansen labels), health and wash diagnostics, the 0-100 Agent Health Score with A-F grades, tiered trust routing (instant_settle / escrow / reject) for payment middleware, gas optimisation, ready-to-sign retry transactions, 30-day webhook alerts and an all-in-one protection run, priced $0.001 to $25.00 per call. Agents pay per call in USDC over x402 (HTTP 402 + PAYMENT-REQUIRED, discovery at /.well-known/x402); humans buy an X-API-Key credit pack via Stripe ($9 / $39 one-time, $99/month). Published as OpenAPI 3.1.0, open source (MIT) on GitHub, with the ahm-shield Python SDK. AHM Verify scores delivered agent output at $0.50 per verdict. AHM also serves an ERC-8004 registration file, a legacy-path A2A agent card and a public roadmap.'
image: https://agenthealthmonitor.xyz/static/ahm-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Agent Health Monitor MCP Server
  slug: agent-health-monitor-mcp-server
modified: '2026-09-19'
name: Agent Health Monitor
nav: Providers
network: true
overview: 'Agent Health Monitor publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Alerts API, Billing API, and 11 more. Tagged areas include Agents, Agent Trust, Risk Scoring, Wallet Intelligence, and Blockchain.


  The Agent Health Monitor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agent Health Monitor''s developer surface includes documentation, API reference, getting-started guide, developer console, pricing, signup flow, engineering blog, and 29 more developer resources.'
plans:
- name: Agenthealthmonitor Xyz Plans Pricing
  plan_count: 10
  slug: agenthealthmonitor-xyz-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Agenthealthmonitor Xyz Rate Limits
  slug: agenthealthmonitor-xyz-rate-limits
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.6
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 73.2
    discoverability: 71.4
    operational_transparency: 18.4
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agenthealthmonitor Xyz Authentication
  slug: agenthealthmonitor-xyz-authentication
  summary_line: apiKey/x402-payment/internal-key/coupon · 4 schemes
- kind: domain-security
  name: Agenthealthmonitor Xyz Domain Security
  slug: agenthealthmonitor-xyz-domain-security
  summary_line: TLSv1.2 · DMARC
slug: agenthealthmonitor-xyz
tags:
- Agents
- Agent Trust
- Risk Scoring
- Wallet Intelligence
- Blockchain
- Base
- x402
- Agentic Commerce
- Monitoring
- Webhook
- Web3
- Verifiable Credentials
- Developer Tools
- Agent-Native
- A2A
website: https://agenthealthmonitor.xyz/
---
