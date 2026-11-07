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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The priced projection of the same trust surface: 77 endpoints under /api/x402/* (29 priced GET reads, 46 priced POST transaction-preparation actions, 2 free) paid per call in USDC on Base mainnet with'
  name: Vaultfire Trust Service (x402)
  slug: vaultfire-trust-service-x402
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Agent identity and trust profiles
  name: Vaultfire Protocol Agent API
  slug: theloopbreaker-com-agent-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Agent performance analytics
  name: Vaultfire Protocol Analytics API
  slug: theloopbreaker-com-analytics-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Partnership and accountability bonds
  name: Vaultfire Protocol Bonds API
  slug: theloopbreaker-com-bonds-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Cross-chain trust sync
  name: Vaultfire Protocol Bridge API
  slug: theloopbreaker-com-bridge-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Mission enforcement, privacy, validation
  name: Vaultfire Protocol Compliance API
  slug: theloopbreaker-com-compliance-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Agent directory and search
  name: Vaultfire Protocol Discovery API
  slug: theloopbreaker-com-discovery-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Dispute resolution
  name: Vaultfire Protocol Disputes API
  slug: theloopbreaker-com-disputes-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Multisig governance
  name: Vaultfire Protocol Governance API
  slug: theloopbreaker-com-governance-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: VNS naming service
  name: Vaultfire Protocol Identity API
  slug: theloopbreaker-com-identity-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Bond insurance pool
  name: Vaultfire Protocol Insurance API
  slug: theloopbreaker-com-insurance-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Vaultfire Key Protocol — session keys, delegation, wallets
  name: Vaultfire Protocol Keys API
  slug: theloopbreaker-com-keys-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Protocol-wide stats and contracts
  name: Vaultfire Protocol Protocol API
  slug: theloopbreaker-com-protocol-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Task routing and matching
  name: Vaultfire Protocol Routing API
  slug: theloopbreaker-com-routing-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Health and system status
  name: Vaultfire Protocol System API
  slug: theloopbreaker-com-system-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Task marketplace with USDC escrow
  name: Vaultfire Protocol Tasks API
  slug: theloopbreaker-com-tasks-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Reputation, vouching, credentials, oracles
  name: Vaultfire Protocol Trust API
  slug: theloopbreaker-com-trust-api
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: Event subscriptions
  name: Vaultfire Protocol Webhooks API
  slug: theloopbreaker-com-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Theloopbreaker Com Webhooks
  slug: theloopbreaker-com-webhooks
common:
- group: other
  href: https://artifacts.apis.io/theloopbreaker-com/capabilities/theloopbreaker-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/theloopbreaker-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/theloopbreaker-com/overlays/theloopbreaker-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/theloopbreaker-com-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/theloopbreaker-com/security/theloopbreaker-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/theloopbreaker-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://theloopbreaker.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://theloopbreaker.com/start
- group: docs
  title: ''
  type: Documentation
  url: https://theloopbreaker.com/architecture
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theloopbreaker.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theloopbreaker.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://theloopbreaker.com/security
- group: operate
  title: ''
  type: Support
  url: https://theloopbreaker.com/partners
- group: build
  title: ''
  type: SourceCode
  url: https://explorer.gitlawb.com/repos/z6MkryiNsYdFEMHv95wxzSQ1vtFXPyVQQrxXdPw3tE5HpfxV/vaultfire
- group: commercial
  title: ''
  type: Pricing
  url: https://theloopbreaker.com/.well-known/x402.json
- group: agent
  href: https://artifacts.apis.io/theloopbreaker-com/llms/theloopbreaker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/theloopbreaker-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://theloopbreaker.com/llms.txt
- group: other
  href: https://artifacts.apis.io/theloopbreaker-com/a2a/theloopbreaker-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/theloopbreaker-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/theloopbreaker-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/theloopbreaker-com/mcp/theloopbreaker-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/theloopbreaker-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/theloopbreaker-com/mcp/theloopbreaker-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/theloopbreaker-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/theloopbreaker-com/well-known/theloopbreaker-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/theloopbreaker-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/theloopbreaker-com/well-known/theloopbreaker-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/theloopbreaker-com-security.txt
- group: build
  href: https://artifacts.apis.io/theloopbreaker-com/packages/theloopbreaker-com-packages.yml
  title: ''
  type: Packages
  url: packages/theloopbreaker-com-packages.yml
- group: build
  href: https://artifacts.apis.io/theloopbreaker-com/packages/theloopbreaker-com-packages.yml
  title: ''
  type: SDKs
  url: packages/theloopbreaker-com-packages.yml
- group: design
  href: https://artifacts.apis.io/theloopbreaker-com/conformance/theloopbreaker-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theloopbreaker-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/theloopbreaker-com/conventions/theloopbreaker-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/theloopbreaker-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/theloopbreaker-com/authentication/theloopbreaker-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theloopbreaker-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/theloopbreaker-com/errors/theloopbreaker-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/theloopbreaker-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/theloopbreaker-com/lifecycle/theloopbreaker-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/theloopbreaker-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/theloopbreaker-com/changelog/theloopbreaker-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/theloopbreaker-com-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/theloopbreaker-com/plans/theloopbreaker-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/theloopbreaker-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/theloopbreaker-com/rate-limits/theloopbreaker-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theloopbreaker-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/theloopbreaker-com/asyncapi/theloopbreaker-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/theloopbreaker-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/theloopbreaker-com/data-model/theloopbreaker-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/theloopbreaker-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/theloopbreaker-com/security/theloopbreaker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theloopbreaker-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://theloopbreaker.com/privacy
created: '2026-09-19'
description: Vaultfire Protocol (theloopbreaker.com) is on-chain trust infrastructure for AI agents — "KYA, Know Your Agent". It runs 134 smart contracts across Base, Avalanche, Arbitrum and Polygon for ERC-8004 agent identity, verifiable reputation (Street Cred), partnership and accountability bonds, a USDC task-escrow marketplace, VNS agent names, key delegation (VKP), ZK trust attestations and a cross-chain trust bridge. Its public Agent Hub API exposes 34 free REST operations (OpenAPI 3.1) that read those contracts and return unsigned transactions for the caller to sign, plus 77 x402-priced endpoints paid per call in USDC, an 18-skill A2A agent card, llms.txt, agents.txt, a published Agent Skill and a stdio MCP server on npm.
finops:
- has_sources: true
  method: derived
  name: Theloopbreaker Com Finops
  primary_unit: api call (usdc on base)
  service_category: ''
  slug: theloopbreaker-com-finops
  template: false
image: https://theloopbreaker.com/og-image.png
layout: provider
mcp_servers:
- description: Vaultfire ships an official MCP server as the npm package @vaultfire/mcp-server (bin vaultfire-mcp-server), a local stdio server that reads the four chains over JSON-RPC with ethers and exposes 9 tool
  name: Vaultfire Protocol MCP Server
  slug: vaultfire
modified: '2026-09-19'
name: Vaultfire Protocol
nav: Providers
network: true
overview: 'Vaultfire Protocol publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Analytics API, Bonds API, and 15 more. Tagged areas include AI Agents, Agent Identity, Trust, Reputation, and Blockchain.


  The Vaultfire Protocol catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Vaultfire Protocol''s developer surface includes getting-started guide, documentation, support, pricing, authentication, changelog, and 28 more developer resources.'
plans:
- name: Theloopbreaker Com Plans Pricing
  plan_count: 5
  slug: theloopbreaker-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Theloopbreaker Com Rate Limits
  slug: theloopbreaker-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Vaultfire Protocol API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: theloopbreaker-com-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 53.7
    developer_ergonomics: 42.9
    discoverability: 71.7
    operational_transparency: 55.3
  previous_composite: 58.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/theloopbreaker-com/theloopbreaker-com-2026-10-11T130849.png
security:
- kind: authentication
  name: Theloopbreaker Com Authentication
  slug: theloopbreaker-com-authentication
  summary_line: none/erc-8128-http-signature/x402-payment/wallet-signature · 5 schemes
- kind: domain-security
  name: Theloopbreaker Com Domain Security
  slug: theloopbreaker-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Theloopbreaker Com Vulnerability Disclosure
  slug: theloopbreaker-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: Check an agent's trust profile before you rely on it
  slug: theloopbreaker-com-check-agent-trust
- name: Register an agent and pledge a partnership bond
  slug: theloopbreaker-com-register-and-bond
- name: Find and route a task to a trusted agent
  slug: theloopbreaker-com-route-task
- name: Subscribe to Vaultfire events with a webhook
  slug: theloopbreaker-com-subscribe-webhooks
- name: vaultfire
  slug: theloopbreaker-com-vaultfire-skill
slug: theloopbreaker-com
tags:
- AI Agents
- Agent Identity
- Trust
- Reputation
- Blockchain
- Web3
- Payments
- x402
- MCP
- A2A
- Company
website: https://theloopbreaker.com/
---
