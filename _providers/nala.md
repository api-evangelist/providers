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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 79.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nala Agentic Access
  operation_count: 8
  slug: nala-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 5
apis:
- description: The Bank API from NALA — 1 operation(s) for bank.
  name: NALA Bank API
  slug: nala-bank-api
- description: The Lookup API from NALA — 1 operation(s) for lookup.
  name: NALA Lookup API
  slug: nala-lookup-api
- description: The Payment Account API from NALA — 1 operation(s) for payment account.
  name: NALA Payment Account API
  slug: nala-payment-account-api
- description: The Payout API from NALA — 2 operation(s) for payout.
  name: NALA Payout API
  slug: nala-payout-api
- description: The Wallet API from NALA — 1 operation(s) for wallet.
  name: NALA Wallet API
  slug: nala-wallet-api
artifact_total: 11
asyncapis:
- description: ''
  name: Nala Rafiki Webhooks
  slug: nala-rafiki-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nala-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nala.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rafiki.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rafiki.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rafiki.com/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rafiki.com/recipes/create-account-and-send-money
- group: operate
  title: ''
  type: Support
  url: https://help.nala.money/en/
- group: company
  title: ''
  type: Blog
  url: https://www.nala.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NalaMoney
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rafiki.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nala.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nala.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nala-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nala-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nala-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nala-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nala-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nala-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nala-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/nala-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nala-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nala-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nala-rafiki-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nala-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nala-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/nala-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nala-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nala-rafiki-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nala-create-account-and-send-payout.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nala-lookup-recipient-account.md
- group: start
  title: ''
  type: SignUp
  url: https://rafiki.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.rafiki.com
created: '2026-07-17'
description: 'NALA is a fintech building cross-border payments infrastructure for emerging markets. Its consumer app is an international money-transfer and multi-currency account used to send money from the UK, US and EU to 35+ countries across Africa and Asia, with 98% of transfers arriving within minutes. NALA''s B2B product, Rafiki, is a single API for global payouts and collections: move, collect and settle funds in local currency or stablecoins (USDC/USDT) across the US, UK, Europe, Asia and Africa, reaching 300+ banks and 40+ mobile-money operators with real-time FX, lookups, wallet statements, webhooks and built-in compliance and sanctions screening. Backed by Bessemer Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nala.png
layout: provider
mcp_servers:
- description: ''
  name: nala-mcp.yml
  slug: nala-mcpyml
modified: '2026-07-20'
name: NALA
nav: Providers
network: true
overview: 'NALA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bank API, Lookup API, Payment Account API, and 2 more. Tagged areas include Company, Fintech, Payments, Remittances, and Money Transfer.


  The NALA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NALA''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 26 more developer resources.'
random_paper: 4
scopes:
- name: Nala Scopes
  scope_count: 9
  slug: nala-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 56.1
  delta: 3.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.7
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 52.6
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Nala Authentication
  slug: nala-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nala Domain Security
  slug: nala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nala
tags:
- Company
- Fintech
- Payments
- Remittances
- Money Transfer
- Payouts
- Cross-Border Payments
- Mobile Money
- Stablecoins
- Africa
website: https://www.nala.com/
---
