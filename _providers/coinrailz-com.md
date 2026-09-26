---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-09-25'
api_count: 2
apis:
- baseURL: https://coinrailz.com
  baseurl_source: spec
  description: 'The full Coin Railz surface: onboarding and prepaid-credit operations (free $5 trial key, Stripe hosted checkout), the 80 metered /x402/<service> endpoints, MPP (Machine Payments Protocol) twins of th'
  name: Coin Railz Agent Payment API
  slug: agent-payment-api
- baseURL: https://coinrailz.com
  baseurl_source: spec
  description: 'The 80 pay-per-request services as a standalone OpenAPI 3.0.3 contract (one POST /x402/<service> per service, price in the description): gas and token oracles, DEX liquidity, whale alerts, wallet risk'
  name: Coin Railz x402 Micropayment Services
  slug: x402-services
- description: 'Remote MCP server on the primary domain: POST https://coinrailz.com/mcp (JSON-RPC 2.0). tools/list is open and returns 80 tools with input and output schemas; tool calls are metered (X-API-KEY prepaid'
  name: Coin Railz MCP Server
  slug: mcp
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/security/coinrailz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinrailz-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/authentication/coinrailz-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coinrailz-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coinrailz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coinrailz.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://coinrailz.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://coinrailz.com/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://coinrailz.com/x402/catalog
- group: commercial
  title: ''
  type: Pricing
  url: https://coinrailz.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coinrailz.com/free-agent-registration
- group: start
  title: ''
  type: Login
  url: https://coinrailz.com/api-keys
- group: operate
  title: ''
  type: Support
  url: https://coinrailz.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinrailz.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinrailz.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tdnupe3
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/llms/coinrailz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinrailz-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://coinrailz.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/a2a/coinrailz-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coinrailz-com-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://coinrailz.com/.well-known/agent-card.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/mcp/coinrailz-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinrailz-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/mcp/coinrailz-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/coinrailz-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/well-known/coinrailz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinrailz-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/well-known/coinrailz-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/coinrailz-com-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/well-known/coinrailz-com-ai-plugin.json
  title: ''
  type: OpenAIPluginManifest
  url: well-known/coinrailz-com-ai-plugin.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/packages/coinrailz-com-packages.yml
  title: ''
  type: Packages
  url: packages/coinrailz-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/packages/coinrailz-com-packages.yml
  title: ''
  type: SDKs
  url: packages/coinrailz-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/conformance/coinrailz-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinrailz-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/errors/coinrailz-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinrailz-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/lifecycle/coinrailz-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coinrailz-com-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/sandbox/coinrailz-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/coinrailz-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/conventions/coinrailz-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinrailz-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/conventions/coinrailz-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coinrailz-com-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/regulatory/coinrailz-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/coinrailz-com-regulatory-posture.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/plans/coinrailz-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinrailz-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/rate-limits/coinrailz-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coinrailz-com-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/security/coinrailz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinrailz-com-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/well-known/coinrailz-com-agent-instructions.json
  title: ''
  type: AgentInstructions
  url: well-known/coinrailz-com-agent-instructions.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinrailz-com/refs/heads/main/well-known/coinrailz-com-x402.json
  title: ''
  type: X402
  url: well-known/coinrailz-com-x402.json
created: '2026-09-19'
description: 'Coin Railz (Kellogg Holdings LLC) is pay-per-call financial and data infrastructure built for autonomous AI agents: 80 metered services - crypto and DeFi intelligence, trading signals, wallet and contract risk, prediction-market odds (Kalshi, Polymarket), NASA/ESA satellite data, IoT/DePIN feeds, AI inference, real estate and compliance checks - paid per request with x402 USDC micropayments on Base, Arc and Solana, or with card-funded prepaid credits. It publishes two OpenAPIs, a conformant A2A agent card, an open remote MCP server with 80 tools, an llms.txt, MPP and AP2 payment manifests, and an ERC-4626 USDC yield vault.'
image: https://coinrailz.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: 'Coin Railz operates a remote MCP server on its primary domain: POST https://coinrailz.com/mcp with {jsonrpc:2.0, method:tools/list} returned 80 tools with inputSchema and outputSchema, anonymously (GE'
  name: Coin Railz MCP Server
  slug: coin-railz-mcp-server
modified: '2026-09-19'
name: Coin Railz
nav: Providers
network: true
overview: 'Coin Railz publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Agent Payment API, x402 Micropayment Services, and 1 more. Tagged areas include Company, Payments, Agents, x402, and Micropayments.


  Coin Railz''s developer surface includes authentication, documentation, getting-started guide, API reference, pricing, signup flow, support, and 31 more developer resources.'
plans:
- name: Coinrailz Com Plans Pricing
  plan_count: 5
  slug: coinrailz-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Coinrailz Com Rate Limits
  slug: coinrailz-com-rate-limits
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 51.1
    developer_ergonomics: 44.6
    discoverability: 66.7
    operational_transparency: 34.2
  previous_composite: 49.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Coinrailz Com Authentication
  slug: coinrailz-com-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Coinrailz Com Domain Security
  slug: coinrailz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinrailz Com Vulnerability Disclosure
  slug: coinrailz-com-vulnerability-disclosure
  summary_line: contact published
slug: coinrailz-com
tags:
- Company
- Payments
- Agents
- x402
- Micropayments
- Cryptocurrency
- DeFi
- Blockchain
- Stablecoins
- USDC
- Prediction Markets
- Satellite Data
- IoT
- Trading
- Compliance
- MCP
- A2A
website: https://coinrailz.com/
---
