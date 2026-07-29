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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Teya Agentic Access
  operation_count: 42
  slug: teya-agentic-access
  summary_line: 42 operations · 29 acting
api_count: 16
apis:
- description: Operations related to capturing pre-authorised transactions.
  name: Teya Captures API
  slug: teya-captures-api
- description: Operations related to dynamic currency conversion
  name: Teya DCC API
  slug: teya-dcc-api
- description: The ePOS Registration API from Teya — 1 operation(s) for epos registration.
  name: Teya ePOS Registration API
  slug: teya-epos-registration-api
- description: APIs exposed for session management
  name: Teya Hosted Checkout API
  slug: teya-hosted-checkout-api
- description: The '@internal' API from Teya — 2 operation(s) for '@internal'.
  name: Teya '@internal' API
  slug: teya-internal-api
- description: The Pay at Table API from Teya — 9 operation(s) for pay at table.
  name: Teya Pay at Table API
  slug: teya-pay-at-table-api
- description: APIs exposed for pay by link customers
  name: Teya PayByLink API
  slug: teya-paybylink-api
- description: The Payment Requests API from Teya — 4 operation(s) for payment requests.
  name: Teya Payment Requests API
  slug: teya-payment-requests-api
- description: Create a receipt print job and fetch its status/events
  name: Teya Print Receipts (ePOS) API
  slug: teya-print-receipts-epos-api
- description: The '@public' API from Teya — 4 operation(s) for '@public'.
  name: Teya '@public' API
  slug: teya-public-api
- description: The Refunds API from Teya — 2 operation(s) for refunds.
  name: Teya Refunds API
  slug: teya-refunds-api
- description: The Reversals API from Teya — 1 operation(s) for reversals.
  name: Teya Reversals API
  slug: teya-reversals-api
- description: The Stores API from Teya — 3 operation(s) for stores.
  name: Teya Stores API
  slug: teya-stores-api
- description: The Terminals API from Teya — 1 operation(s) for terminals.
  name: Teya Terminals API
  slug: teya-terminals-api
- description: Token management for saved payment methods
  name: Teya Tokens API
  slug: teya-tokens-api
- description: Transactions
  name: Teya Transactions API
  slug: teya-transactions-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.teya.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.teya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teya.com/apis/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.teya.com/apis/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.teya.com/apis/developer-portal/configure-application
- group: operate
  title: ''
  type: Support
  url: https://help.teya.com/
- group: company
  title: ''
  type: Blog
  url: https://www.teya.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saltpay
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teya.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.teya.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teya.com/legal/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teya.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/teya-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/teya-scopes.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/teya-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teya-conventions.yml
- group: build
  title: ''
  type: SDKs
  url: packages/teya-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/teya-packages.yml
- group: design
  title: ''
  type: Components
  url: components/teya-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/teya-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teya-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teya-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teya-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teya-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teya-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/teya-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teya-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teya-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teya-domain-security.yml
created: '2026-07-17'
description: 'Teya (formerly SaltPay) is a European payments and business-services provider serving local businesses with card machines, online and in-person card acquiring, a business account, and flexible business funding. Its developer platform exposes REST APIs for the full card-payment lifecycle: Online Payments (Hosted Checkout, PayByLink, e-commerce transactions, captures, refunds, digital receipts, tokens), a Payments Gateway (card-present, MOTO, refunds, captures, reversals), POSLink for cloud terminal control (payment requests, tabs, stores, terminals, ePOS registration, receipt printing), and a Teya FX API for Dynamic Currency Conversion, plus a SOAP-based Settlement API for payout reporting. Authentication is OAuth 2.0 (authorization code and client credentials) against id.teya.com, write operations support Idempotency-Key, and first-party SDKs cover web (Teya Blocks) and Android/iOS point-of-sale.'
image: https://www.teya.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: teya-mcp.yml
  slug: teya-mcpyml
modified: '2026-07-21'
name: Teya
nav: Providers
network: true
overview: 'Teya publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Captures API, DCC API, ePOS Registration API, and 13 more. Tagged areas include Company, Payments, Payment Processing, Card Acquiring, and Online Payments.


  Teya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 35
scopes:
- name: Teya Scopes
  scope_count: 2
  slug: teya-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.6
  delta: -2.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.6
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 67.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Teya Authentication
  slug: teya-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Teya Domain Security
  slug: teya-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teya
tags:
- Company
- Payments
- Payment Processing
- Card Acquiring
- Online Payments
- Point of Sale
- E-commerce
- Fintech
- Merchant Services
- Europe
website: https://www.teya.com/
---
