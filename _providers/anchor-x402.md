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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-09-12'
api_count: 1
apis:
- baseURL: https://api.anchor-x402.com
  baseurl_source: declared
  description: Eighteen stateless pay-per-call services on one FastAPI/AWS Lambda host. Every paid route answers an unpaid request with an x402 v2 402 PaymentRequired challenge carrying an accepts[] array of Base US
  name: anchor-x402 API
  slug: anchor-x402-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://anchor-x402.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anchor-x402.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.anchor-x402.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.anchor-x402.com/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://anchor-x402.com/guides/pay-x402-api-node/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hypeprinter007-stack
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/hypeprinter007-stack/anchor-x402
- group: commercial
  title: ''
  type: Pricing
  url: https://anchor-x402.com/.well-known/x402.json
- group: operate
  title: ''
  type: StatusPage
  url: https://anchor-x402.betteruptime.com
- group: auth
  title: ''
  type: Security
  url: security/anchor-x402-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anchor-x402-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/anchor-x402-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anchor-x402-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/anchor-x402-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anchor-x402-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/anchor-x402-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anchor-x402-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/anchor-x402-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anchor-x402-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anchor-x402-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anchor-x402-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anchor-x402-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anchor-x402-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anchor-x402-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anchor-x402-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anchor-x402-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anchor-x402-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/anchor-x402-examples.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anchor-x402-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anchor-x402-rate-limits.yml
created: '2026-09-11'
description: anchor-x402 operates a pay-per-call API surface for AI agents, billed with the x402 HTTP payment protocol instead of API keys or accounts. Eighteen stateless services run on AWS Lambda and FastAPI behind https://api.anchor-x402.com, each returning an x402 v2 402 PaymentRequired challenge that a caller settles per request in USDC on Base or Solana (select routes also settle JPYC on Polygon) via EIP-3009 transferWithAuthorization. The catalog spans on-chain anchoring and attestation, wallet sanctions and risk screening, Web3 data decoding, ENS/SNS name resolution, token pricing, x402 spend accounting, verifiable signed randomness, and LLM-backed content analysis, priced from $0.001 to $1.77 per call. The same 18 services are exposed over MCP (a hosted Streamable HTTP endpoint at https://api.anchor-x402.com/mcp whose tools/list is free and anonymous, plus an npm stdio package) and over a signed A2A JSON-RPC door at /v1/a2a, with a conformant A2A 0.3.0 agent card and a hosted Claude
  chatbot at chat.anchor-x402.com for non-developers. Source is MIT licensed and the operator publishes a trust portal that states plainly it holds no SOC 2, ISO 27001, PCI or HIPAA certification.
image: https://anchor-x402.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: anchor-x402 MCP Server
  slug: anchor-x402-mcp-server
modified: '2026-09-11'
name: anchor-x402
nav: Providers
network: true
overview: 'anchor-x402 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, x402, Agents, Payments, and Blockchain.


  anchor-x402''s developer surface includes documentation, API reference, getting-started guide, pricing, sandbox, authentication, code examples, and 24 more developer resources.'
plans:
- name: Anchor X402 Plans Pricing
  plan_count: 3
  slug: anchor-x402-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Anchor X402 Rate Limits
  slug: anchor-x402-rate-limits
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 71.4
    discoverability: 75.9
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Anchor X402 Authentication
  slug: anchor-x402-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Anchor X402 Domain Security
  slug: anchor-x402-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Anchor X402 Vulnerability Disclosure
  slug: anchor-x402-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Anchor X402 Trust Center
  slug: anchor-x402-trust-center
  summary_line: trust center published
slug: anchor-x402
tags:
- Company
- x402
- Agents
- Payments
- Blockchain
- MCP
- Web3
- Pay Per Call
- Agent Payments
- Stablecoins
- Compliance
- Attestation
website: https://anchor-x402.com
---
