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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Bakkt Agentic Access
  operation_count: 54
  slug: bakkt-agentic-access
  summary_line: 54 operations · 30 acting
api_count: 17
apis:
- description: Accounts are used to represent users that use the platform's services.
  name: Bakkt Accounts API
  slug: bakkt-accounts-api
- description: Authorization allows Client systems to authenticate and access services on behalf of their investors.
  name: Bakkt Authorization API
  slug: bakkt-authorization-api
- description: The Block Trade & Allocate API from Bakkt — 5 operation(s) for block trade & allocate.
  name: Bakkt Block Trade & Allocate API
  slug: bakkt-block-trade-allocate-api
- description: Client systems can use these resources to provide a connection to the platform's services and check API status.
  name: Bakkt Configuration and Status API
  slug: bakkt-configuration-and-status-api
- description: The Currency Onboarding API from Bakkt — 5 operation(s) for currency onboarding.
  name: Bakkt Currency Onboarding API
  slug: bakkt-currency-onboarding-api
- description: Documents allows users to upload and retrieve documents along with their relevant metadata.
  name: Bakkt Documents API
  slug: bakkt-documents-api
- description: The Fiat Onboarding API from Bakkt — 5 operation(s) for fiat onboarding.
  name: Bakkt Fiat Onboarding API
  slug: bakkt-fiat-onboarding-api
- description: The Gift API from Bakkt — 2 operation(s) for gift.
  name: Bakkt Gift API
  slug: bakkt-gift-api
- description: Instruments provides information about assets offered on the platform.
  name: Bakkt Instruments API
  slug: bakkt-instruments-api
- description: Jurisdictions provides information about trading restrictions in different jurisdictions
  name: Bakkt Jurisdictions API
  slug: bakkt-jurisdictions-api
- description: Orders enables customers to buy or sell crypto.
  name: Bakkt Orders API
  slug: bakkt-orders-api
- description: The Partner Connectivity API from Bakkt — 2 operation(s) for partner connectivity.
  name: Bakkt Partner Connectivity API
  slug: bakkt-partner-connectivity-api
- description: The Partner Party Funding API from Bakkt — 5 operation(s) for partner party funding.
  name: Bakkt Partner Party Funding API
  slug: bakkt-partner-party-funding-api
- description: The Partner Party Kyc API from Bakkt — 1 operation(s) for partner party kyc.
  name: Bakkt Partner Party Kyc API
  slug: bakkt-partner-party-kyc-api
- description: The Partner Party Linking API from Bakkt — 3 operation(s) for partner party linking.
  name: Bakkt Partner Party Linking API
  slug: bakkt-partner-party-linking-api
- description: Positions provide up-to-date information about crypto balances and transactions.
  name: Bakkt Positions API
  slug: bakkt-positions-api
- description: Transfers allow users to access deposit and withdrawal functionality both within the Bakkt network and across the blockchain.
  name: Bakkt Transfers API
  slug: bakkt-transfers-api
artifact_total: 22
asyncapis:
- description: ''
  name: Bakkt Webhooks
  slug: bakkt-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bakkt.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://bakkt.readme.io/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://bakkt.readme.io/reference/login
- group: start
  title: ''
  type: GettingStarted
  url: https://bakkt.readme.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://bakkt.readme.io/docs/support-feedback
- group: company
  title: ''
  type: Blog
  url: https://bakkt.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bakkt.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bakkt.com/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bakkt.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://bakkt.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/bakkt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bakkt-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bakkt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bakkt-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/bakkt-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/bakkt-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bakkt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bakkt-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bakkt-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bakkt-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bakkt-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bakkt-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bakkt-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bakkt-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bakkt-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bakkt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bakkt-domain-security.yml
created: '2026-07-17'
description: Bakkt is a digital asset platform that provides crypto trading, custody, and fiat funding infrastructure to financial institutions and fintech apps. Its Crypto Solutions API is a REST/FIX platform (with WebSocket market data and webhook/SQS events) that lets a client's investors buy, sell, hold, and transfer bitcoin, ether, and other digital assets in a branded environment, plus a Fiat/Partner API for account opening, KYC/KYB, Plaid bank linking, and ACH/Wire on-ramping. Surfaced as a portfolio company of Multicoin Capital and Pantera Capital and enriched from Bakkt's public developer hub (bakkt.readme.io / developer.bakkt.com).
image: https://bakkt.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: bakkt-mcp.yml
  slug: bakkt-mcpyml
modified: '2026-07-18'
name: Bakkt
nav: Providers
network: true
overview: 'Bakkt publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authorization API, Block Trade & Allocate API, and 14 more. Tagged areas include Company, Crypto Web3, Cryptocurrency, Digital Assets, and Trading.


  The Bakkt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bakkt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 21 more developer resources.'
random_paper: 45
score:
  band: developing
  composite: 47.4
  delta: -3.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bakkt/refs/heads/main/screenshots/bakkt-2026-07-25T202255.png
security:
- kind: authentication
  name: Bakkt Authentication
  slug: bakkt-authentication
  summary_line: http-token · 1 scheme
- kind: domain-security
  name: Bakkt Domain Security
  slug: bakkt-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bakkt
tags:
- Company
- Crypto Web3
- Cryptocurrency
- Digital Assets
- Trading
- Payments
- Fiat On-Ramp
- Custody
- Webhooks
- FIX Protocol
website: https://bakkt.com
---
