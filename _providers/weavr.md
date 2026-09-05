---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 187
  human_in_the_loop: 5
  name: Weavr Agentic Access
  operation_count: 257
  slug: weavr-agentic-access
  summary_line: 257 operations · 187 acting · 5 human-in-the-loop
api_count: 5
apis:
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Acquire a token granting you access to perform sensitive operations on behalf of an identity.
  name: Weavr Access Token API
  slug: weavr-access-token-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Acquire and revoke access tokens.
  name: Weavr Access Tokens API
  slug: weavr-access-tokens-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Accounts API from Weavr — 2 operation(s) for accounts.
  name: Weavr Accounts API
  slug: weavr-accounts-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Additional Factors API from Weavr — 2 operation(s) for additional factors.
  name: Weavr Additional Factors API
  slug: weavr-additional-factors-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Manage user authentication factors, including passwords and device-based factors (OTP and push).
  name: Weavr Authentication Factors API
  slug: weavr-authentication-factors-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Verify the email of root users who act as authorised signatories of a Corporate or Consumer identity.
  name: Weavr Authorised Signatories API
  slug: weavr-authorised-signatories-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Corporate and Consumer identities can invite authorised users to access their account. Once on-boarded, authorised users can create and manage instruments and transactions on behalf of the identity th
  name: Weavr Authorised Users API
  slug: weavr-authorised-users-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: 'Buyers can invite authorised users to access their account. Once on-boarded, authorised users can transact on behalf of the identity they are on-boarded with. Authorised users are typically employees '
  name: Weavr Buyer Authorised Users API
  slug: weavr-buyer-authorised-users-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Buyers are identities representing a business Once on-boarded, Buyers can create payment runs and pay their suppliers in your application.
  name: Weavr Buyers API
  slug: weavr-buyers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Retrieve card payment activity, including authorisations, settlements, and related events.
  name: Weavr Card Payments API
  slug: weavr-card-payments-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Cards API from Weavr — 7 operation(s) for cards.
  name: Weavr Cards API
  slug: weavr-cards-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Issue and verify confirmation challenges used to authorise lists of resources.
  name: Weavr Confirmation Challenges API
  slug: weavr-confirmation-challenges-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Consumers API from Weavr — 3 operation(s) for consumers.
  name: Weavr Consumers API
  slug: weavr-consumers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Corporates API from Weavr — 3 operation(s) for corporates.
  name: Weavr Corporates API
  slug: weavr-corporates-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Correspondent bank transfers allow financial institutions to initiate wire transfers on behalf of originators (third parties). These transfers comply with travel rule requirements by capturing and tra
  name: Weavr Correspondent Bank Transfers API
  slug: weavr-correspondent-bank-transfers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Manage customer profile data and KYC/KYB due diligence flows for corporates and consumers.
  name: Weavr Customer Data & Due Diligence API
  slug: weavr-customer-data-due-diligence-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Factors API from Weavr — 3 operation(s) for factors.
  name: Weavr Factors API
  slug: weavr-factors-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Fees API from Weavr — 4 operation(s) for fees.
  name: Weavr Fees API
  slug: weavr-fees-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Incoming wire transfers received from external bank accounts to managed accounts with IBANs.
  name: Weavr Incoming Wire Transfers API
  slug: weavr-incoming-wire-transfers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Institutions supported by Embedded Payment Run.
  name: Weavr Institutions API
  slug: weavr-institutions-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Linked Accounts API from Weavr — 11 operation(s) for linked accounts.
  name: Weavr Linked Accounts API
  slug: weavr-linked-accounts-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Manage API from Weavr — 7 operation(s) for manage.
  name: Weavr Manage API
  slug: weavr-manage-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: 'Managed Accounts are a type of financial instrument offered by Weavr. They hold funds for their owner, and can be upgraded to IBANs so as to receive and send funds to instruments outside of the Weavr '
  name: Weavr Managed Accounts API
  slug: weavr-managed-accounts-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Managed Cards are a type of financial instrument offered by Weavr. Cards created in prepaid mode have their own balance, whereas those created in debit mode tap into the balance of their parent Manage
  name: Weavr Managed Cards API
  slug: weavr-managed-cards-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Operations API from Weavr — 9 operation(s) for operations.
  name: Weavr Operations API
  slug: weavr-operations-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Outgoing Wire Transfer transaction is used to transfer funds from managed accounts to an external bank account.
  name: Weavr Outgoing Wire Transfers API
  slug: weavr-outgoing-wire-transfers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Passwords API from Weavr — 5 operation(s) for passwords.
  name: Weavr Passwords API
  slug: weavr-passwords-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: A Payment run contains a list of supplier payments. A Payment run can be - created by a user with a `CREATOR` role - confirmed by a user with a `CONTROLLER` role - funded by a user with a `CONTROLLER`
  name: Weavr Payment runs API
  slug: weavr-payment-runs-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Roles API from Weavr — 1 operation(s) for roles.
  name: Weavr Roles API
  slug: weavr-roles-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Send transaction is used to send funds between managed accounts and managed cards belonging to different identities.
  name: Weavr Sends API
  slug: weavr-sends-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Register and manage the lifecycle of users that can access an identity, including authorised users invited by a Corporate or Consumer root user.
  name: Weavr Setup API
  slug: weavr-setup-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Sign users in using passwords, biometrics, or third-party auth providers.
  name: Weavr Sign-in API
  slug: weavr-sign-in-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Simulators enable you to trigger processes in Sandbox that in Production are triggered from an external action rather than from your application. this way you can test scenarios that otherwise you wou
  name: Weavr Simulator API
  slug: weavr-simulator-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Simulator Linked accounts API from Weavr — 2 operation(s) for simulator linked accounts.
  name: Weavr Simulator Linked accounts API
  slug: weavr-simulator-linked-accounts-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Manage spend rules and authorisation forwarding to approve or reject card payments in real time.
  name: Weavr Spend Controls API
  slug: weavr-spend-controls-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Step up API from Weavr — 2 operation(s) for step up.
  name: Weavr Step up API
  slug: weavr-step-up-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Issue and verify step-up challenges that elevate an existing user token.
  name: Weavr Step-up Challenges API
  slug: weavr-step-up-challenges-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Tokens API from Weavr — 2 operation(s) for tokens.
  name: Weavr Tokens API
  slug: weavr-tokens-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Retrieve the consolidated transaction activity across instruments.
  name: Weavr Transaction Activity API
  slug: weavr-transaction-activity-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Transfers API from Weavr — 3 operation(s) for transfers.
  name: Weavr Transfers API
  slug: weavr-transfers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Manage a list of trusted payees for Outgoing wire transfers and Sends. Aside from convenience and a reduced chance of making errors when making transactions, this allows for the introduction an SCA ex
  name: Weavr Trusted Payees API
  slug: weavr-trusted-payees-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The User Impersonation API from Weavr — 1 operation(s) for user impersonation.
  name: Weavr User Impersonation API
  slug: weavr-user-impersonation-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Wiretransfers API from Weavr — 2 operation(s) for wiretransfers.
  name: Weavr Wiretransfers API
  slug: weavr-wiretransfers-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Notification of the Authentication Factors that are used for the `Identity`.
  name: Weavr Authentication Factors Webhooks API
  slug: weavr-authentication-factors-webhooks-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Bulk Operations API from Weavr — 0 operation(s) for bulk operations.
  name: Weavr Bulk Operations API
  slug: weavr-bulk-operations-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Buyers are identities representing companies. Once on-boarded, Buyers can create and manage their own instruments via your application.
  name: Weavr Buyers Webhooks API
  slug: weavr-buyers-webhooks-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Ibans API from Weavr — 0 operation(s) for ibans.
  name: Weavr Ibans API
  slug: weavr-ibans-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Notification that the status of a Linked Account has been updated.
  name: Weavr Linked Accounts Webhooks API
  slug: weavr-linked-accounts-webhooks-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Login API from Weavr — 0 operation(s) for login.
  name: Weavr Login API
  slug: weavr-login-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Manual Transactions API from Weavr — 0 operation(s) for manual transactions.
  name: Weavr Manual Transactions API
  slug: weavr-manual-transactions-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Notification that the Payment Run and payment statuses have been updated.
  name: Weavr Payment runs Webhooks API
  slug: weavr-payment-runs-webhooks-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Stepup API from Weavr — 0 operation(s) for stepup.
  name: Weavr Stepup API
  slug: weavr-stepup-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Notification that a step-up has been completed or declined.
  name: Weavr Stepup Webhooks API
  slug: weavr-stepup-webhooks-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Tokens webhooks
  name: Weavr Tokens Webhooks API
  slug: weavr-tokens-webhooks-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: Notification that the status of a transaction has been updated.
  name: Weavr Transactions Webhooks API
  slug: weavr-transactions-webhooks-api
arazzos:
- description: Simulate a deposit into a managed account, then move funds with an internal transfer and an external send. Uses the Simulator API for the deposit so a fork runs end-to-end in the Weavr sandbox.
  name: Fund a managed account and move money
  slug: weavr-fund-account-and-transfer
- description: Create a corporate identity, authenticate, open a managed account and issue a virtual card on the Weavr Multi API. Fork and run against the sandbox (https://sandbox.weavr.io).
  name: Onboard a corporate and issue a virtual card
  slug: weavr-onboard-corporate-and-issue-card
artifact_total: 105
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token API
  slug: open-weavr-access-token-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Access Tokens API
  slug: open-weavr-access-tokens-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Accounts API
  slug: open-weavr-accounts-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Additional Factors API
  slug: open-weavr-additional-factors-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Authentication Factors API
  slug: open-weavr-authentication-factors-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Authorised Signatories API
  slug: open-weavr-authorised-signatories-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Authorised Users API
  slug: open-weavr-authorised-users-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Buyer Authorised Users API
  slug: open-weavr-buyer-authorised-users-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Buyers API
  slug: open-weavr-buyers-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Card Payments API
  slug: open-weavr-card-payments-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Cards API
  slug: open-weavr-cards-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Confirmation Challenges API
  slug: open-weavr-confirmation-challenges-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Consumers API
  slug: open-weavr-consumers-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Corporates API
  slug: open-weavr-corporates-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Correspondent Bank Transfers API
  slug: open-weavr-correspondent-bank-transfers-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Customer Data & Due Diligence API
  slug: open-weavr-customer-data-due-diligence-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Factors API
  slug: open-weavr-factors-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Fees API
  slug: open-weavr-fees-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Incoming Wire Transfers API
  slug: open-weavr-incoming-wire-transfers-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Institutions API
  slug: open-weavr-institutions-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Linked Accounts API
  slug: open-weavr-linked-accounts-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Manage API
  slug: open-weavr-manage-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Managed Accounts API
  slug: open-weavr-managed-accounts-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Managed Cards API
  slug: open-weavr-managed-cards-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Operations API
  slug: open-weavr-operations-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Outgoing Wire Transfers API
  slug: open-weavr-outgoing-wire-transfers-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Passwords API
  slug: open-weavr-passwords-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Payment runs API
  slug: open-weavr-payment-runs-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Roles API
  slug: open-weavr-roles-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Sends API
  slug: open-weavr-sends-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Setup API
  slug: open-weavr-setup-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Sign-in API
  slug: open-weavr-sign-in-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Simulator API
  slug: open-weavr-simulator-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Simulator Linked accounts API
  slug: open-weavr-simulator-linked-accounts-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Spend Controls API
  slug: open-weavr-spend-controls-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Step up API
  slug: open-weavr-step-up-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Step-up Challenges API
  slug: open-weavr-step-up-challenges-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Tokens API
  slug: open-weavr-tokens-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Transaction Activity API
  slug: open-weavr-transaction-activity-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Transfers API
  slug: open-weavr-transfers-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Trusted Payees API
  slug: open-weavr-trusted-payees-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token User Impersonation API
  slug: open-weavr-user-impersonation-api
- collection_type: open
  name: Weavr Multi Product BackOffice Access Token Wiretransfers API
  slug: open-weavr-wiretransfers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/weavr-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/weavr-multi-backoffice-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Weavr
nav: Providers
network: true
overview: 'Weavr publishes 55 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Access Tokens API, Accounts API, and 52 more. Tagged areas include Embedded Finance, Banking as a Service, Payments, Cards, and Fintech.


  Weavr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 31 more developer resources.'
random_paper: 3
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 76.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 55
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weavr/refs/heads/main/screenshots/weavr-2026-08-17T082854.png
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
- Account
- KYC
- Company
website: https://www.weavr.io/
---
