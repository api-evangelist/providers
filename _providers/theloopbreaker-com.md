---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://theloopbreaker.com/api
  baseurl_source: declared
  description: 'Public REST API over the Vaultfire trust contracts on Base, Avalanche, Arbitrum and Polygon: agent trust profiles and Street Cred scores, ERC-8004 registration and partnership-bond transaction builder'
  name: Vaultfire Agent Hub API
  slug: vaultfire-agent-hub-api
- description: 'The priced projection of the same trust surface: 77 endpoints under /api/x402/* (29 priced GET reads, 46 priced POST transaction-preparation actions, 2 free) paid per call in USDC on Base mainnet with'
  name: Vaultfire Trust Service (x402)
  slug: vaultfire-trust-service-x402
artifact_total: 9
asyncapis:
- description: ''
  name: Theloopbreaker Com Webhooks
  slug: theloopbreaker-com-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/security/theloopbreaker-com-vulnerability-disclosure.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/llms/theloopbreaker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/theloopbreaker-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://theloopbreaker.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/a2a/theloopbreaker-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/theloopbreaker-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/mcp/theloopbreaker-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/theloopbreaker-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/mcp/theloopbreaker-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/theloopbreaker-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/well-known/theloopbreaker-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/theloopbreaker-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/well-known/theloopbreaker-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/theloopbreaker-com-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/packages/theloopbreaker-com-packages.yml
  title: ''
  type: Packages
  url: packages/theloopbreaker-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/packages/theloopbreaker-com-packages.yml
  title: ''
  type: SDKs
  url: packages/theloopbreaker-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/conformance/theloopbreaker-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theloopbreaker-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/conventions/theloopbreaker-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/theloopbreaker-com-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/authentication/theloopbreaker-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theloopbreaker-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/errors/theloopbreaker-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/theloopbreaker-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/lifecycle/theloopbreaker-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/theloopbreaker-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/changelog/theloopbreaker-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/theloopbreaker-com-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/plans/theloopbreaker-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/theloopbreaker-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/rate-limits/theloopbreaker-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theloopbreaker-com-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/asyncapi/theloopbreaker-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/theloopbreaker-com-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/data-model/theloopbreaker-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/theloopbreaker-com-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theloopbreaker-com/refs/heads/main/security/theloopbreaker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theloopbreaker-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://theloopbreaker.com/privacy
created: '2026-09-19'
description: Vaultfire Protocol (theloopbreaker.com) is on-chain trust infrastructure for AI agents — "KYA, Know Your Agent". It runs 134 smart contracts across Base, Avalanche, Arbitrum and Polygon for ERC-8004 agent identity, verifiable reputation (Street Cred), partnership and accountability bonds, a USDC task-escrow marketplace, VNS agent names, key delegation (VKP), ZK trust attestations and a cross-chain trust bridge. Its public Agent Hub API exposes 34 free REST operations (OpenAPI 3.1) that read those contracts and return unsigned transactions for the caller to sign, plus 77 x402-priced endpoints paid per call in USDC, an 18-skill A2A agent card, llms.txt, agents.txt, a published Agent Skill and a stdio MCP server on npm.
image: https://theloopbreaker.com/og-image.png
layout: provider
mcp_servers:
- description: Vaultfire ships an official MCP server as the npm package @vaultfire/mcp-server (bin vaultfire-mcp-server), a local stdio server that reads the four chains over JSON-RPC with ethers and exposes 9 tool
  name: Vaultfire Protocol MCP Server
  slug: vaultfire-protocol-mcp-server
modified: '2026-09-19'
name: Vaultfire Protocol
nav: Providers
network: true
overview: 'Vaultfire Protocol publishes 1 API on the [APIs.io](https://apis.io/) network: Vaultfire Agent Hub API. Tagged areas include AI Agents, Agent Identity, Trust, Reputation, and Blockchain.


  The Vaultfire Protocol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vaultfire Protocol''s developer surface includes getting-started guide, documentation, support, pricing, authentication, changelog, and 26 more developer resources.'
plans:
- name: Theloopbreaker Com Plans Pricing
  plan_count: 2
  slug: theloopbreaker-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Theloopbreaker Com Rate Limits
  slug: theloopbreaker-com-rate-limits
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 53.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    operational_transparency: 60.5
  previous_composite: 55.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
