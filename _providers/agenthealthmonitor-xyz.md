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
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Agenthealthmonitor Xyz Agentic Access
  operation_count: 80
  slug: agenthealthmonitor-xyz-agentic-access
  summary_line: 80 operations · 14 acting
api_count: 2
apis:
- baseURL: https://agenthealthmonitor.xyz
  baseurl_source: declared
  description: REST API for agent-wallet trust and health on Base L2, published as OpenAPI 3.1.0 (v1.8.0) at https://agenthealthmonitor.xyz/openapi.json — 74 paths / 76 operations across Scoring & Risk (/risk, /risk
  name: Agent Health Monitor API
  slug: agent-health-monitor-api
- baseURL: https://verify.agenthealthmonitor.xyz
  baseurl_source: declared
  description: 'Post-transaction output-quality scoring: register a job specification (POST /v1/specs, free), submit an agent''s delivered output for evaluation by a six-role adversarial Claude panel (POST /v1/outputs'
  name: AHM Verify API
  slug: ahm-verify-api
artifact_total: 9
asyncapis:
- description: ''
  name: Agenthealthmonitor Xyz Alerts Webhooks
  slug: agenthealthmonitor-xyz-alerts-webhooks
common:
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
  name: Digital Intensity Ltd MCP Server
  slug: digital-intensity-ltd-mcp-server
modified: '2026-09-19'
name: Digital Intensity Ltd
nav: Providers
network: true
overview: 'Digital Intensity Ltd publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agent Health Monitor API and AHM Verify API. Tagged areas include Agents, Agent Trust, Risk Scoring, Wallet Intelligence, and Blockchain.


  The Digital Intensity Ltd catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Digital Intensity Ltd''s developer surface includes documentation, API reference, getting-started guide, developer console, pricing, signup flow, engineering blog, and 27 more developer resources.'
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
  composite: 40.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 20.0
    developer_ergonomics: 73.2
    discoverability: 68.5
    operational_transparency: 18.4
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
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
