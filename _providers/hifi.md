---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Hifi Agentic Access
  operation_count: 87
  slug: hifi-agentic-access
  summary_line: 87 operations · 42 acting
api_count: 15
apis:
- description: Account endpoints
  name: Hifi Account API
  slug: hifi-account-api
- description: Common endpoints
  name: Hifi Common API
  slug: hifi-common-api
- description: Cross-Chain Bridge endpoints
  name: Hifi Cross-Chain Bridge API
  slug: hifi-cross-chain-bridge-api
- description: Crypto Transfer endpoints
  name: Hifi Crypto Transfer API
  slug: hifi-crypto-transfer-api
- description: File endpoints
  name: Hifi File API
  slug: hifi-file-api
- description: Kyc endpoints
  name: Hifi Kyc API
  slug: hifi-kyc-api
- description: Offramp endpoints
  name: Hifi Offramp API
  slug: hifi-offramp-api
- description: Onramp endpoints
  name: Hifi Onramp API
  slug: hifi-onramp-api
- description: Reporting and metrics endpoints
  name: Hifi Reporting API
  slug: hifi-reporting-api
- description: The Settlement Rules API from Hifi — 5 operation(s) for settlement rules.
  name: Hifi Settlement Rules API
  slug: hifi-settlement-rules-api
- description: Token Swap endpoints
  name: Hifi Token Swap API
  slug: hifi-token-swap-api
- description: Transfer approval workflow and admin actions
  name: Hifi Transfer Approvals API
  slug: hifi-transfer-approvals-api
- description: User endpoints
  name: Hifi User API
  slug: hifi-user-api
- description: Virtual Account endpoints
  name: Hifi Virtual Account API
  slug: hifi-virtual-account-api
- description: Wallet endpoints
  name: Hifi Wallet API
  slug: hifi-wallet-api
artifact_total: 20
asyncapis:
- description: ''
  name: Hifi Webhooks
  slug: hifi-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hifi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hifi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hifi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hifi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hifi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hifi.com/guides/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hifi.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hifi.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://hifi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://hifi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hifi.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hifi.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.hifi.com/request-access
- group: start
  title: ''
  type: Login
  url: https://app.hifi.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hifi-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hifi-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hifi-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hifi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hifi-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hifi-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hifi-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hifi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hifi-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hifi-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hifi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hifi-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hifi-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hifi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Hifi is a stablecoin and money-movement infrastructure company that provides composable financial APIs for moving, converting, routing, and settling value across bank rails and stablecoins. The platform covers fiat on-ramps and off-ramps, crypto transfers, token swaps, cross-chain bridging, virtual accounts, wallets and custody, KYC and compliance onboarding, settlement rules and orchestration addresses, transfer approvals, and reporting. Hifi is registered as a Money Services Business and partners with Cross River Bank for regulated banking, letting developers build global payouts, treasury automation, escrow flows, and multi-chain settlement programmatically over a single REST API secured with bearer API keys.
image: https://www.hifi.com/seo/hifi-opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: hifi-mcp.yml
  slug: hifi-mcpyml
modified: '2026-07-19'
name: Hifi
nav: Providers
network: true
overview: 'Hifi publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, Common API, Cross-Chain Bridge API, and 12 more. Tagged areas include Company, Stablecoins, Payments, Money Movement, and On-Ramp.


  The Hifi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hifi''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 56
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hifi/refs/heads/main/screenshots/hifi-2026-07-25T221141.png
security:
- kind: authentication
  name: Hifi Authentication
  slug: hifi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hifi Domain Security
  slug: hifi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hifi
tags:
- Company
- Stablecoins
- Payments
- Money Movement
- On-Ramp
- Off-Ramp
- Crypto
- Fintech
- KYC
- Virtual Accounts
- Cross-Chain
- Financial Infrastructure
website: https://hifi.com
---
