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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Idrx Agentic Access
  operation_count: 13
  slug: idrx-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- description: Onboard users and manage their bank accounts.
  name: IDRX Onboarding API
  slug: idrx-onboarding-api
- description: Mint, redeem, and bridge IDRX, and query rates/fees/history.
  name: IDRX Transaction API
  slug: idrx-transaction-api
- description: The IDRX API API from IDRX — 0 operation(s) for idrx api.
  name: IDRX IDRX API
  slug: idrx-idrx-api-api
artifact_total: 11
asyncapis:
- description: ''
  name: Idrx Callback Webhooks
  slug: idrx-callback-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IDRX Onboarding API
  slug: open-idrx-onboarding-api
- collection_type: open
  name: IDRX Onboarding Transaction API
  slug: open-idrx-transaction-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/idrx-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.idrx.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.idrx.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.idrx.co/api/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.idrx.co/api/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://app.idrx.co
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.idrx.co/services/fees
- group: operate
  title: ''
  type: Support
  url: mailto:support@idrx.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/idrx-co
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.idrx.co/introduction/idrx-whitepaper
- group: auth
  title: ''
  type: Authentication
  url: authentication/idrx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/idrx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/idrx-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/idrx-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/idrx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/idrx-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/idrx-callback-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/idrx-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/idrx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idrx-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/idrx-llms.txt
created: '2026-07-17'
description: IDRX is a stablecoin pegged 1:1 to the Indonesian Rupiah (IDR), issued by a regulated Indonesian entity and available across multiple EVM chains and Solana. Its REST API lets business (organization) accounts onboard KYC-verified users, register bank accounts, and process mint (fiat IDR -> IDRX / USDT on-chain), redeem (IDRX -> fiat IDR to a bank account), and bridge (cross-chain) transactions, plus query swap rates, fees, supported bank methods, and transaction history. Requests are authenticated with an API key and an HMAC-SHA256 request signature, and settlement is confirmed via single-delivery webhooks or transaction-history polling. IDRX is a portfolio company of a16z (crypto).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idrx.png
layout: provider
mcp_servers:
- description: ''
  name: IDRX MCP Server
  slug: idrx-mcp-server
modified: '2026-07-19'
name: IDRX
nav: Providers
network: true
overview: 'IDRX publishes 3 APIs on the [APIs.io](https://apis.io/) network: Onboarding API, Transaction API, and IDRX API. Tagged areas include Stablecoins, Cryptocurrency, Payments, Blockchain, and Fintech.


  The IDRX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IDRX''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, authentication, and 15 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 58.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idrx/refs/heads/main/screenshots/idrx-2026-07-25T222044.png
security:
- kind: authentication
  name: Idrx Authentication
  slug: idrx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Idrx Domain Security
  slug: idrx-domain-security
  summary_line: TLSv1.3
slug: idrx
tags:
- Stablecoins
- Cryptocurrency
- Payments
- Blockchain
- Fintech
- Indonesia
- Rupiah
- Web3
- On-Ramp
- Digital Currency
website: https://docs.idrx.co
---
