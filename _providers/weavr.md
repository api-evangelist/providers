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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 187
  human_in_the_loop: 5
  name: Weavr Agentic Access
  operation_count: 257
  slug: weavr-agentic-access
  summary_line: 257 operations · 187 acting · 5 human-in-the-loop
api_count: 43
apis:
- description: Acquire a token granting you access to perform sensitive operations on behalf of an identity.
  name: Weavr Access Token API
  slug: weavr-access-token-api
- description: Acquire and revoke access tokens.
  name: Weavr Access Tokens API
  slug: weavr-access-tokens-api
- description: The Accounts API from Weavr — 2 operation(s) for accounts.
  name: Weavr Accounts API
  slug: weavr-accounts-api
- description: The Additional Factors API from Weavr — 2 operation(s) for additional factors.
  name: Weavr Additional Factors API
  slug: weavr-additional-factors-api
- description: Manage user authentication factors, including passwords and device-based factors (OTP and push).
  name: Weavr Authentication Factors API
  slug: weavr-authentication-factors-api
- description: Verify the email of root users who act as authorised signatories of a Corporate or Consumer identity.
  name: Weavr Authorised Signatories API
  slug: weavr-authorised-signatories-api
- description: Corporate and Consumer identities can invite authorised users to access their account. Once on-boarded, authorised users can create and manage instruments and transactions on behalf of the identity th
  name: Weavr Authorised Users API
  slug: weavr-authorised-users-api
- description: 'Buyers can invite authorised users to access their account. Once on-boarded, authorised users can transact on behalf of the identity they are on-boarded with. Authorised users are typically employees '
  name: Weavr Buyer Authorised Users API
  slug: weavr-buyer-authorised-users-api
- description: Buyers are identities representing a business Once on-boarded, Buyers can create payment runs and pay their suppliers in your application.
  name: Weavr Buyers API
  slug: weavr-buyers-api
- description: Retrieve card payment activity, including authorisations, settlements, and related events.
  name: Weavr Card Payments API
  slug: weavr-card-payments-api
- description: The Cards API from Weavr — 7 operation(s) for cards.
  name: Weavr Cards API
  slug: weavr-cards-api
- description: Issue and verify confirmation challenges used to authorise lists of resources.
  name: Weavr Confirmation Challenges API
  slug: weavr-confirmation-challenges-api
- description: The Consumers API from Weavr — 3 operation(s) for consumers.
  name: Weavr Consumers API
  slug: weavr-consumers-api
- description: The Corporates API from Weavr — 3 operation(s) for corporates.
  name: Weavr Corporates API
  slug: weavr-corporates-api
- description: Correspondent bank transfers allow financial institutions to initiate wire transfers on behalf of originators (third parties). These transfers comply with travel rule requirements by capturing and tra
  name: Weavr Correspondent Bank Transfers API
  slug: weavr-correspondent-bank-transfers-api
- description: Manage customer profile data and KYC/KYB due diligence flows for corporates and consumers.
  name: Weavr Customer Data & Due Diligence API
  slug: weavr-customer-data-due-diligence-api
- description: The Factors API from Weavr — 3 operation(s) for factors.
  name: Weavr Factors API
  slug: weavr-factors-api
- description: The Fees API from Weavr — 4 operation(s) for fees.
  name: Weavr Fees API
  slug: weavr-fees-api
- description: Incoming wire transfers received from external bank accounts to managed accounts with IBANs.
  name: Weavr Incoming Wire Transfers API
  slug: weavr-incoming-wire-transfers-api
- description: Institutions supported by Embedded Payment Run.
  name: Weavr Institutions API
  slug: weavr-institutions-api
- description: The Linked Accounts API from Weavr — 11 operation(s) for linked accounts.
  name: Weavr Linked Accounts API
  slug: weavr-linked-accounts-api
- description: The Manage API from Weavr — 7 operation(s) for manage.
  name: Weavr Manage API
  slug: weavr-manage-api
- description: 'Managed Accounts are a type of financial instrument offered by Weavr. They hold funds for their owner, and can be upgraded to IBANs so as to receive and send funds to instruments outside of the Weavr '
  name: Weavr Managed Accounts API
  slug: weavr-managed-accounts-api
- description: Managed Cards are a type of financial instrument offered by Weavr. Cards created in prepaid mode have their own balance, whereas those created in debit mode tap into the balance of their parent Manage
  name: Weavr Managed Cards API
  slug: weavr-managed-cards-api
- description: The Operations API from Weavr — 9 operation(s) for operations.
  name: Weavr Operations API
  slug: weavr-operations-api
- description: The Outgoing Wire Transfer transaction is used to transfer funds from managed accounts to an external bank account.
  name: Weavr Outgoing Wire Transfers API
  slug: weavr-outgoing-wire-transfers-api
- description: The Passwords API from Weavr — 5 operation(s) for passwords.
  name: Weavr Passwords API
  slug: weavr-passwords-api
- description: A Payment run contains a list of supplier payments. A Payment run can be - created by a user with a `CREATOR` role - confirmed by a user with a `CONTROLLER` role - funded by a user with a `CONTROLLER`
  name: Weavr Payment runs API
  slug: weavr-payment-runs-api
- description: The Roles API from Weavr — 1 operation(s) for roles.
  name: Weavr Roles API
  slug: weavr-roles-api
- description: The Send transaction is used to send funds between managed accounts and managed cards belonging to different identities.
  name: Weavr Sends API
  slug: weavr-sends-api
- description: Register and manage the lifecycle of users that can access an identity, including authorised users invited by a Corporate or Consumer root user.
  name: Weavr Setup API
  slug: weavr-setup-api
- description: Sign users in using passwords, biometrics, or third-party auth providers.
  name: Weavr Sign-in API
  slug: weavr-sign-in-api
- description: Simulators enable you to trigger processes in Sandbox that in Production are triggered from an external action rather than from your application. this way you can test scenarios that otherwise you wou
  name: Weavr Simulator API
  slug: weavr-simulator-api
- description: The Simulator Linked accounts API from Weavr — 2 operation(s) for simulator linked accounts.
  name: Weavr Simulator Linked accounts API
  slug: weavr-simulator-linked-accounts-api
- description: Manage spend rules and authorisation forwarding to approve or reject card payments in real time.
  name: Weavr Spend Controls API
  slug: weavr-spend-controls-api
- description: The Step up API from Weavr — 2 operation(s) for step up.
  name: Weavr Step up API
  slug: weavr-step-up-api
- description: Issue and verify step-up challenges that elevate an existing user token.
  name: Weavr Step-up Challenges API
  slug: weavr-step-up-challenges-api
- description: The Tokens API from Weavr — 2 operation(s) for tokens.
  name: Weavr Tokens API
  slug: weavr-tokens-api
- description: Retrieve the consolidated transaction activity across instruments.
  name: Weavr Transaction Activity API
  slug: weavr-transaction-activity-api
- description: The Transfers API from Weavr — 3 operation(s) for transfers.
  name: Weavr Transfers API
  slug: weavr-transfers-api
- description: Manage a list of trusted payees for Outgoing wire transfers and Sends. Aside from convenience and a reduced chance of making errors when making transactions, this allows for the introduction an SCA ex
  name: Weavr Trusted Payees API
  slug: weavr-trusted-payees-api
- description: The User Impersonation API from Weavr — 1 operation(s) for user impersonation.
  name: Weavr User Impersonation API
  slug: weavr-user-impersonation-api
- description: The Wiretransfers API from Weavr — 2 operation(s) for wiretransfers.
  name: Weavr Wiretransfers API
  slug: weavr-wiretransfers-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Simulate a deposit into a managed account, then move funds with an internal transfer and an external send. Uses the Simulator API for the deposit so a fork runs end-to-end in the Weavr sandbox.
  name: Fund a managed account and move money
  slug: weavr-fund-account-and-transfer
- description: Create a corporate identity, authenticate, open a managed account and issue a virtual card on the Weavr Multi API. Fork and run against the sandbox (https://sandbox.weavr.io).
  name: Onboard a corporate and issue a virtual card
  slug: weavr-onboard-corporate-and-issue-card
artifact_total: 51
common:
- group: company
  title: ''
  type: Website
  url: https://www.weavr.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.weavr.io/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.weavr.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.weavr.io/products/multi/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.weavr.io/start/multi-welcome/
- group: operate
  title: ''
  type: Support
  url: https://support.weavr.io/
- group: company
  title: ''
  type: Blog
  url: https://www.weavr.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weavr-io
- group: start
  title: ''
  type: SignUp
  url: https://portal.weavr.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.weavr.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weavr.io/terms-policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weavr.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://weavr.statuspage.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/weavr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/weavr-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/weavr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/weavr-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weavr-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/weavr-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/weavr-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/weavr-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/weavr-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/weavr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/weavr-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: openapi/_original/weavr-webhooks-openapi-original.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weavr-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/weavr-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weavr-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/weavr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.weavr.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/weavr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weavr-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weavr-agentic-access.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weavr-onboard-corporate-and-issue-card.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weavr-fund-account-and-transfer.yml
created: '2026-07-17'
description: Weavr is an embedded-finance ("banking-as-a-service") platform that lets software companies embed regulated financial products — managed accounts, IBANs, virtual and physical cards, transfers, sends and wire payments — directly inside their applications. Its Multi API issues accounts and cards to corporate and consumer end-users with full KYB/KYC onboarding, Strong Customer Authentication (SCA) step-up challenges, and client-side "Secure Components" that tokenize sensitive data so the embedder stays out of PCI scope. Weavr operates through regulated EMI partners (Paynetics AD in the EU, Paynetics UK in the UK) and exposes a Multi API, a BackOffice programme-operations API, an Embedded Payment Run API, a Webhooks event surface and a sandbox Simulator API, backed by SDKs for Web, iOS, Android and React Native and an official agent-skills pack.
image: https://www.weavr.io/wp-content/uploads/2025/12/Image-8-1.png
layout: provider
mcp_servers:
- description: ''
  name: weavr-mcp.yml
  slug: weavr-mcpyml
modified: '2026-07-21'
name: Weavr
nav: Providers
network: true
overview: 'Weavr publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Access Tokens API, Accounts API, and 40 more. Tagged areas include Embedded Finance, Banking as a Service, Payments, Cards, and Fintech.


  Weavr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 29 more developer resources.'
random_paper: 85
score:
  band: strong
  composite: 62.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.5
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 62.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Weavr Authentication
  slug: weavr-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Weavr Domain Security
  slug: weavr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Weavr Trust Center
  slug: weavr-trust-center
  summary_line: ISO 27001, PCI DSS, CSA STAR
slug: weavr
tags:
- Embedded Finance
- Banking as a Service
- Payments
- Cards
- Fintech
- Accounts
- KYC
- Company
website: https://www.weavr.io/
---
