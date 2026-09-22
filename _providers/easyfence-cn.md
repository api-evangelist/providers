---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://www.easyfence.cn
  baseurl_source: declared
  description: 'The store''s public JSON surface: the service catalog with USD prices and the x402 payment block (GET /api/catalog), the payment-gated delivery endpoint (POST /api/deliver, 402 until a USDC authorizati'
  name: X402 AI 自助门店 Store API
  slug: easyfence-cn-store-api
- description: 'The store''s agent-to-agent surface: an anonymous A2A 0.3 JSON-RPC endpoint the agent card points at, where a buyer agent negotiates with the store clerk before ordering. The provider''s documented meth'
  name: X402 AI 自助门店 A2A Agent
  slug: easyfence-cn-a2a-agent
- baseURL: https://www.easyfence.cn/facilitator
  baseurl_source: declared
  description: 'A self-hosted x402 facilitator role on the same host - POST /facilitator/verify and POST /facilitator/settle with free-form JSON bodies, plus /facilitator/healthz reporting the networks it settles on '
  name: X402 AI 自助门店 x402 Facilitator API
  slug: easyfence-cn-x402-facilitator-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.easyfence.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://www.easyfence.cn/a2a
- group: docs
  title: ''
  type: APIReference
  url: https://www.easyfence.cn/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easyfence.cn/#services
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/a2a/easyfence-cn-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/easyfence-cn-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/llms/easyfence-cn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyfence-cn-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/authentication/easyfence-cn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easyfence-cn-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/conventions/easyfence-cn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/easyfence-cn-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/errors/easyfence-cn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/easyfence-cn-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/data-model/easyfence-cn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/easyfence-cn-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/plans/easyfence-cn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easyfence-cn-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/rate-limits/easyfence-cn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/easyfence-cn-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/conformance/easyfence-cn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easyfence-cn-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/lifecycle/easyfence-cn-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/easyfence-cn-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/overlays/easyfence-cn-store-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/easyfence-cn-store-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/mcp/easyfence-cn-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/easyfence-cn-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/well-known/easyfence-cn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easyfence-cn-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/security/easyfence-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyfence-cn-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/easyfence-cn/refs/heads/main/regulatory/easyfence-cn-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/easyfence-cn-regulatory-posture.yml
created: '2026-09-19'
description: 'X402 AI 自助门店 ("X402 AI self-service store") is a single-operator agent-commerce storefront at easyfence.cn that sells only to other AI agents: a buyer agent reads the A2A agent card, lists seven generated services priced 0.30-2.00 USD per call in /api/catalog, optionally negotiates with the store clerk over A2A JSON-RPC at /a2a, and orders at /api/deliver, which answers HTTP 402 with an x402 payment requirement (USDC on Base or BSC, mainnet) until an EIP-3009 authorization is presented, then returns the deliverable. The store also acts as an ERC-8004 style identity issuer with a public trust registry and runs its own x402 facilitator for the BSC route. A FastAPI-generated OpenAPI 3.1.0 is served at /openapi.json; no SDKs, terms, support channel or operator identity are published, and payments are irreversible.'
layout: provider
mcp_servers:
- description: 'X402 AI 自助门店 publishes NO MCP server. /.well-known/mcp.json 404s on both hosts, POST tools/list to the only JSON-RPC endpoint (/a2a) returns -32601 "method does not exist", and no npm/PyPI package or '
  name: X402 AI 自助门店 MCP Server
  slug: x402-ai-自助门店-mcp-server
modified: '2026-09-19'
name: X402 AI 自助门店
nav: Providers
network: true
overview: 'X402 AI 自助门店 publishes 2 APIs on the [APIs.io](https://apis.io/) network: Store API and x402 Facilitator API. Tagged areas include Agentic Commerce, AI Agents, A2A, x402, and Payments.


  X402 AI 自助门店''s developer surface includes documentation, API reference, pricing, authentication, and 16 more developer resources.'
plans:
- name: Easyfence Cn Plans Pricing
  plan_count: 7
  slug: easyfence-cn-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Easyfence Cn Rate Limits
  slug: easyfence-cn-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 30.4
    discoverability: 64.8
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
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
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Easyfence Cn Authentication
  slug: easyfence-cn-authentication
  summary_line: none/x402-payment/erc8004-identity/query-token · 4 schemes
- kind: domain-security
  name: Easyfence Cn Domain Security
  slug: easyfence-cn-domain-security
  summary_line: TLSv1.3
slug: easyfence-cn
tags:
- Agentic Commerce
- AI Agents
- A2A
- x402
- Payments
- Stablecoins
- Agent Identity
- Content Generation
- Web3
website: https://www.easyfence.cn/
---
