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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Remote MCP server on the primary domain: POST https://coinrailz.com/mcp (JSON-RPC 2.0). tools/list is open and returns 80 tools with input and output schemas; tool calls are metered (X-API-KEY prepaid'
  name: Coin Railz MCP Server
  slug: mcp
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Pay-per-call AI inference
  name: Coin Railz AI Services API
  slug: coinrailz-com-ai-services-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: The Base Native API from Coin Railz — 3 operation(s) for base native.
  name: Coin Railz Base Native API
  slug: coinrailz-com-base-native-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: The DeFi & Yield API from Coin Railz — 4 operation(s) for defi & yield.
  name: Coin Railz DeFi & Yield API
  slug: coinrailz-com-defi-yield-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: The Developer Tools API from Coin Railz — 1 operation(s) for developer tools.
  name: Coin Railz Developer Tools API
  slug: coinrailz-com-developer-tools-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Test and discovery endpoints
  name: Coin Railz Discovery API
  slug: coinrailz-com-discovery-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Transaction building and wallet services
  name: Coin Railz Execution API
  slug: coinrailz-com-execution-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Trading signals and portfolio optimization
  name: Coin Railz Investment API
  slug: coinrailz-com-investment-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: IoT device data and fleet telematics
  name: Coin Railz IoT & DePIN API
  slug: coinrailz-com-iot-depin-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Arbitrage and risk analysis
  name: Coin Railz Market Intelligence API
  slug: coinrailz-com-market-intelligence-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: MPP (Machine Payments Protocol) endpoints — pathUSD via Tempo. See /.well-known/mpp.json
  name: Coin Railz MPP API
  slug: coinrailz-com-mpp-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Get an API key or checkout session — no wallet required
  name: Coin Railz Onboarding API
  slug: coinrailz-com-onboarding-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Polymarket, Kalshi, and prediction data
  name: Coin Railz Prediction Markets API
  slug: coinrailz-com-prediction-markets-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: High-value professional services
  name: Coin Railz Premium API
  slug: coinrailz-com-premium-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Property and construction analytics
  name: Coin Railz Real Estate API
  slug: coinrailz-com-real-estate-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Informational technical risk and compliance-analysis outputs; not banking, legal, or regulated advice
  name: Coin Railz Risk & Compliance APIs API
  slug: coinrailz-com-risk-compliance-apis-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: The Robinhood Chain API from Coin Railz — 5 operation(s) for robinhood chain.
  name: Coin Railz Robinhood Chain API
  slug: coinrailz-com-robinhood-chain-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: The RWA & Tokenization API from Coin Railz — 2 operation(s) for rwa & tokenization.
  name: Coin Railz RWA & Tokenization API
  slug: coinrailz-com-rwa-tokenization-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: NASA/ESA satellite data APIs
  name: Coin Railz Satellite Intelligence API
  slug: coinrailz-com-satellite-intelligence-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Non-custodial USDC yield portal on Solana — deposits into Kamino Lending. Agent signs and submits transactions; Coin Railz never holds funds.
  name: Coin Railz Solana Yield API
  slug: coinrailz-com-solana-yield-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Real-time market data and analysis
  name: Coin Railz Trading Intelligence API
  slug: coinrailz-com-trading-intelligence-api
- baseURL: https://coinrailz.com/mcp
  baseurl_source: declared
  description: Non-custodial USDC yield vault — ERC-4626 auto-routing across Aave v3, Compound v3, and Morpho Blue on Base. No lockup, 0% exit fee.
  name: Coin Railz Yield API
  slug: coinrailz-com-yield-api
artifact_total: 34
common:
- group: company
  title: ''
  type: Blog
  url: https://coinrailz.com/blog/
- group: other
  href: https://artifacts.apis.io/coinrailz-com/capabilities/coinrailz-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coinrailz-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/coinrailz-com/overlays/coinrailz-com-agent-payment-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coinrailz-com-agent-payment-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/coinrailz-com/overlays/coinrailz-com-x402-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coinrailz-com-x402-services-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/coinrailz-com/security/coinrailz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinrailz-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/coinrailz-com/authentication/coinrailz-com-authentication.yml
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
  href: https://artifacts.apis.io/coinrailz-com/llms/coinrailz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinrailz-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://coinrailz.com/llms.txt
- group: other
  href: https://artifacts.apis.io/coinrailz-com/a2a/coinrailz-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coinrailz-com-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://coinrailz.com/.well-known/agent-card.json
- group: agent
  href: https://artifacts.apis.io/coinrailz-com/mcp/coinrailz-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinrailz-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/coinrailz-com/mcp/coinrailz-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/coinrailz-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/coinrailz-com/well-known/coinrailz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinrailz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinrailz-com/well-known/coinrailz-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/coinrailz-com-api-catalog.json
- group: build
  href: https://artifacts.apis.io/coinrailz-com/well-known/coinrailz-com-ai-plugin.json
  title: ''
  type: OpenAIPluginManifest
  url: well-known/coinrailz-com-ai-plugin.json
- group: build
  href: https://artifacts.apis.io/coinrailz-com/packages/coinrailz-com-packages.yml
  title: ''
  type: Packages
  url: packages/coinrailz-com-packages.yml
- group: build
  href: https://artifacts.apis.io/coinrailz-com/packages/coinrailz-com-packages.yml
  title: ''
  type: SDKs
  url: packages/coinrailz-com-packages.yml
- group: design
  href: https://artifacts.apis.io/coinrailz-com/conformance/coinrailz-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinrailz-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/coinrailz-com/errors/coinrailz-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinrailz-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coinrailz-com/lifecycle/coinrailz-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coinrailz-com-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/coinrailz-com/sandbox/coinrailz-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/coinrailz-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/coinrailz-com/conventions/coinrailz-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinrailz-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/coinrailz-com/conventions/coinrailz-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coinrailz-com-conventions.yml
- group: other
  href: https://artifacts.apis.io/coinrailz-com/regulatory/coinrailz-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/coinrailz-com-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/coinrailz-com/plans/coinrailz-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinrailz-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coinrailz-com/rate-limits/coinrailz-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coinrailz-com-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/coinrailz-com/security/coinrailz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinrailz-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/coinrailz-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/coinrailz-com/well-known/coinrailz-com-agent-instructions.json
  title: ''
  type: AgentInstructions
  url: well-known/coinrailz-com-agent-instructions.json
- group: other
  href: https://artifacts.apis.io/coinrailz-com/well-known/coinrailz-com-x402.json
  title: ''
  type: X402
  url: well-known/coinrailz-com-x402.json
created: '2026-09-19'
description: 'Coin Railz (Kellogg Holdings LLC) is pay-per-call financial and data infrastructure built for autonomous AI agents: 80 metered services - crypto and DeFi intelligence, trading signals, wallet and contract risk, prediction-market odds (Kalshi, Polymarket), NASA/ESA satellite data, IoT/DePIN feeds, AI inference, real estate and compliance checks - paid per request with x402 USDC micropayments on Base, Arc and Solana, or with card-funded prepaid credits. It publishes two OpenAPIs, a conformant A2A agent card, an open remote MCP server with 80 tools, an llms.txt, MPP and AP2 payment manifests, and an ERC-4626 USDC yield vault.'
finops:
- has_sources: true
  method: derived
  name: Coinrailz Com Finops
  primary_unit: call (usdc)
  service_category: ''
  slug: coinrailz-com-finops
  template: false
image: https://coinrailz.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: 'Coin Railz operates a remote MCP server on its primary domain: POST https://coinrailz.com/mcp with {jsonrpc:2.0, method:tools/list} returned 80 tools with inputSchema and outputSchema, anonymously (GE'
  name: Coin Railz MCP Server
  slug: coin-railz-mcp-server
modified: '2026-10-06'
name: Coin Railz
nav: Providers
network: true
overview: 'Coin Railz publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Services API, Base Native API, DeFi & Yield API, and 19 more. Tagged areas include Company, Payments, Agents, x402, and Micropayments.


  The Coin Railz catalog on APIs.io includes 1 Spectral governance ruleset.


  Coin Railz''s developer surface includes engineering blog, authentication, documentation, getting-started guide, API reference, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Coinrailz Com Plans Pricing
  plan_count: 11
  slug: coinrailz-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Coinrailz Com Rate Limits
  slug: coinrailz-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Coin Railz API Rules
  rule_count: 56
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 10
  slug: coinrailz-com-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 56.6
    contract_governance: 31.8
    contract_quality: 58.4
    developer_ergonomics: 47.0
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 53.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
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
    score: 27.8
screenshot: https://apis.io/screenshots/coinrailz-com/coinrailz-com-2026-10-11T103128.png
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
skill_count: 4
skills:
- name: Buy prepaid credits by card (hosted checkout)
  slug: coinrailz-com-buy-credits-by-card
- name: Onboard an agent with the free trial key
  slug: coinrailz-com-onboard-with-trial-key
- name: Park idle USDC in the yield vault
  slug: coinrailz-com-park-usdc-in-yield-vault
- name: Pay for a single call with x402 USDC
  slug: coinrailz-com-pay-per-call-with-x402
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
