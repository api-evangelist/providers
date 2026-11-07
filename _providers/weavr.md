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
  band: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.7
  scored_at: '2026-11-06'
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
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Ibans API from Weavr — 0 operation(s) for ibans.
  name: Weavr Ibans API
  slug: weavr-ibans-api
- baseURL: https://api.weavr.io/multi
  baseurl_source: declared
  description: The Wire Transfers API from Weavr — 2 operation(s) for wire transfers.
  name: Weavr Wire Transfers API
  slug: weavr-wire-transfers-api
arazzos:
- description: Simulate a deposit into a managed account, then move funds with an internal transfer and an external send. Uses the Simulator API for the deposit so a fork runs end-to-end in the Weavr sandbox.
  name: Fund a managed account and move money
  slug: weavr-fund-account-and-transfer
- description: Create a corporate identity, authenticate, open a managed account and issue a virtual card on the Weavr Multi API. Fork and run against the sandbox (https://sandbox.weavr.io).
  name: Onboard a corporate and issue a virtual card
  slug: weavr-onboard-corporate-and-issue-card
artifact_total: 142
asyncapis:
- description: ''
  name: Weavr Webhooks
  slug: weavr-webhooks
collections:
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
- group: build
  href: https://artifacts.apis.io/weavr/mcp/weavr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/weavr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/weavr/mcp/weavr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/weavr-mcp.yml
- group: operate
  href: https://artifacts.apis.io/weavr/rate-limits/weavr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/weavr-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/weavr/rules/weavr-rules.yml
  title: ''
  type: Spectral
  url: rules/weavr-rules.yml
- group: design
  href: https://artifacts.apis.io/weavr/json-ld/weavr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/weavr-context.jsonld
- group: design
  href: https://artifacts.apis.io/weavr/vocabulary/weavr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weavr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/weavr/asyncapi/weavr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/weavr-webhooks.yml
- group: design
  href: https://artifacts.apis.io/weavr/errors/weavr-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/weavr-error-codes.yml
- group: other
  href: https://artifacts.apis.io/weavr/a2a/weavr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/weavr-a2a.yml
- group: other
  href: https://artifacts.apis.io/weavr/hosts/weavr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weavr-hosts.yml
- group: other
  href: https://artifacts.apis.io/weavr/vendors/weavr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weavr-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.weavr.io/category/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.weavr.io/blog/feed/
- group: commercial
  href: https://artifacts.apis.io/weavr/plans/weavr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weavr-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/weavr/capabilities/weavr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/weavr-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/weavr/overlays/weavr-multi-backoffice-overlay.yaml
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
  href: https://artifacts.apis.io/weavr/authentication/weavr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weavr-authentication.yml
- group: design
  href: https://artifacts.apis.io/weavr/conventions/weavr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/weavr-conventions.yml
- group: design
  href: https://artifacts.apis.io/weavr/conventions/weavr-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/weavr-conventions.yml
- group: design
  href: https://artifacts.apis.io/weavr/errors/weavr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/weavr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/weavr/lifecycle/weavr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/weavr-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/weavr/changelog/weavr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/weavr-changelog.yml
- group: start
  href: https://artifacts.apis.io/weavr/sandbox/weavr-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/weavr-sandbox.yml
- group: design
  href: https://artifacts.apis.io/weavr/components/weavr-components.yml
  title: ''
  type: Components
  url: components/weavr-components.yml
- group: design
  href: https://artifacts.apis.io/weavr/data-model/weavr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/weavr-data-model.yml
- group: build
  href: https://artifacts.apis.io/weavr/packages/weavr-packages.yml
  title: ''
  type: Packages
  url: packages/weavr-packages.yml
- group: build
  href: https://artifacts.apis.io/weavr/packages/weavr-packages.yml
  title: ''
  type: SDKs
  url: packages/weavr-packages.yml
- group: design
  href: https://artifacts.apis.io/weavr/openapi/_original/weavr-webhooks-openapi-original.yml
  title: ''
  type: Webhooks
  url: openapi/_original/weavr-webhooks-openapi-original.yml
- group: agent
  href: https://artifacts.apis.io/weavr/well-known/weavr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/weavr-well-known.yml
- group: agent
  href: https://artifacts.apis.io/weavr/mcp/weavr-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/weavr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/weavr/llms/weavr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weavr-llms.txt
- group: agent
  href: https://artifacts.apis.io/weavr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/weavr/conformance/weavr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weavr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.weavr.io/
- group: auth
  href: https://artifacts.apis.io/weavr/security/weavr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/weavr-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/weavr/security/weavr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weavr-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/weavr/agentic-access/weavr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/weavr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/weavr/arazzo/weavr-onboard-corporate-and-issue-card.yml
  title: ''
  type: Arazzo
  url: arazzo/weavr-onboard-corporate-and-issue-card.yml
- group: design
  href: https://artifacts.apis.io/weavr/arazzo/weavr-fund-account-and-transfer.yml
  title: ''
  type: Arazzo
  url: arazzo/weavr-fund-account-and-transfer.yml
created: '2026-07-17'
description: Weavr is an embedded-finance ("banking-as-a-service") platform that lets software companies embed regulated financial products — managed accounts, IBANs, virtual and physical cards, transfers, sends and wire payments — directly inside their applications. Its Multi API issues accounts and cards to corporate and consumer end-users with full KYB/KYC onboarding, Strong Customer Authentication (SCA) step-up challenges, and client-side "Secure Components" that tokenize sensitive data so the embedder stays out of PCI scope. Weavr operates through regulated EMI partners (Paynetics AD in the EU, Paynetics UK in the UK) and exposes a Multi API, a BackOffice programme-operations API, an Embedded Payment Run API, a Webhooks event surface and a sandbox Simulator API, backed by SDKs for Web, iOS, Android and React Native and an official agent-skills pack.
finops:
- has_sources: true
  method: derived
  name: Weavr Finops
  primary_unit: platform licence subscription
  service_category: ''
  slug: weavr-finops
  template: false
image: https://www.weavr.io/wp-content/uploads/2025/12/Image-8-1.png
json_schemas:
- name: BulkProcessesPaged
  property_count: 3
  slug: weavr-bulk-processes-paged
- name: CurrencyAmount
  property_count: 2
  slug: weavr-currency-amount
- name: Date
  property_count: 3
  slug: weavr-date
- name: DepositRequestByAccountId
  property_count: 10
  slug: weavr-deposit-request-by-account-id
- name: DepositRequest
  property_count: 13
  slug: weavr-deposit-request
- name: DepositResponse0
  property_count: 1
  slug: weavr-deposit-response0
- name: DepositResponse1
  property_count: 1
  slug: weavr-deposit-response1
- name: Email
  property_count: 0
  slug: weavr-email
- name: ImpersonateIdentityLoginRequest
  property_count: 2
  slug: weavr-impersonate-identity-login-request
- name: LinkedAccountRunRequest
  property_count: 1
  slug: weavr-linked-account-run-request
- name: Mobile
  property_count: 2
  slug: weavr-mobile
- name: OutgoingWireTransferCreateRequest
  property_count: 8
  slug: weavr-outgoing-wire-transfer-create-request
- name: OutgoingWireTransferUpdateBeneficiaryNameRequest
  property_count: 2
  slug: weavr-outgoing-wire-transfer-update-beneficiary-name-request
- name: ProfileId
  property_count: 0
  slug: weavr-profile-id
- name: PurchaseRequestByCardId
  property_count: 13
  slug: weavr-purchase-request-by-card-id
- name: PurchaseRequest
  property_count: 15
  slug: weavr-purchase-request
- name: PurchaseResponse
  property_count: 2
  slug: weavr-purchase-response
- name: RbacRole
  property_count: 3
  slug: weavr-rbac-role
- name: Response
  property_count: 1
  slug: weavr-response
- name: SendCreateRequest
  property_count: 7
  slug: weavr-send-create-request
- name: SimulateVerifyChallengeResponse
  property_count: 1
  slug: weavr-simulate-verify-challenge-response
- name: VerificationCode
  property_count: 0
  slug: weavr-verification-code
- name: VerifyRequestByAccountId
  property_count: 2
  slug: weavr-verify-request-by-account-id
jsonld:
- class_count: 120
  name: Weavr Context
  property_count: 194
  slug: weavr-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.weavr.io over HTTP; 11 tools listed.
  name: Weavr MCP Server
  slug: weavr
modified: '2026-10-06'
name: Weavr
nav: Providers
network: true
overview: 'Weavr publishes 54 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Token API, Access Tokens API, Accounts API, and 51 more. Tagged areas include Embedded Finance, Banking as a Service, Payments, Cards, and Fintech.


  The Weavr catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Weavr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 45 more developer resources.'
plans:
- name: Weavr Plans Pricing
  plan_count: 2
  slug: weavr-plans-pricing
- name: Weavr Price Estimates
  plan_count: 0
  slug: weavr-price-estimates
random_paper: 21
rate_limits:
- limit_count: 3
  name: Weavr Rate Limits
  slug: weavr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Weavr API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: weavr-rules
score:
  band: exemplar
  composite: 74.3
  coverage:
    artifact_dirs: 39
    catalog_earned: 88.8
    catalog_earned_first_party: 20.0
    catalog_gap: 26.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 78.6
    developer_ergonomics: 76.2
    discoverability: 80.8
    operational_transparency: 73.7
  previous_composite: 73.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 42.6
      total: 54
    mcp: first-party
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
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/weavr/weavr-2026-08-17T082854.png
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
skill_count: 8
skills:
- name: weavr-api
  slug: weavr-api
- name: weavr-components
  slug: weavr-components
- name: weavr-glossary
  slug: weavr-glossary
- name: weavr-sdk-android
  slug: weavr-sdk-android
- name: weavr-sdk-ios
  slug: weavr-sdk-ios
- name: weavr-sdk-react-native
  slug: weavr-sdk-react-native
- name: weavr-sdk-web
  slug: weavr-sdk-web
- name: weavr-simulator
  slug: weavr-simulator
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
