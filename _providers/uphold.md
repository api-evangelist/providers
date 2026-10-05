---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-04'
api_count: 5
apis:
- description: The long-standing public Uphold API at api.uphold.com/v0 — tickers and exchange rates, supported currencies and assets, plus OAuth 2.0 authenticated access to a member's cards, transactions and accoun
  name: Uphold Public API (v0)
  slug: uphold-public-api-v0
- description: Anonymous, read-only Model Context Protocol server published by Uphold at developer.uphold.com/mcp over streamable HTTP. Exposes three tools (documentation search, a virtualized read-only docs filesys
  name: Uphold Documentation MCP Server
  slug: uphold-documentation-mcp-server
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Accounts.
  name: Uphold Accounts API
  phrasing_intents:
  - id: core.list-accounts
    intent: List a user's accounts
    question: Which accounts does this user hold on Uphold?
  - id: core.create-account
    intent: Open a new account in an asset
    question: How do I open a new account for holding a specific asset?
  - id: core.list-default-accounts
    intent: List the default account per asset
    question: Which account is the default one for each asset I own?
  - id: core.get-account
    intent: Look up one account by id
    question: How do I fetch the details and balance of a single account?
  - id: core.update-account
    intent: Rename an account
    question: How do I change the label on an existing account?
  - id: core.archive-account
    intent: Archive an account
    question: How do I archive an account I no longer use?
  - id: core.get-account-deposit-method
    intent: Get deposit details for funding an account
    question: Where do I send funds to deposit into an account from outside?
  - id: core.setup-account-deposit-method
    intent: Set up a deposit method for an account
    question: How do I enable external deposits into an account for a new asset and network?
  phrasing_ops: 10
  slug: uphold-accounts-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Assets, networks and rails.
  name: Uphold Assets API
  phrasing_intents:
  - id: core.list-assets
    intent: List supported assets
    question: Which assets and currencies does Uphold support?
  - id: core.get-many-assets
    intent: Look up several assets by code at once
    question: Can I fetch details for several asset codes in a single request?
  - id: core.get-asset
    intent: Get details of one asset
    question: What details are available for a single asset code?
  - id: core.get-asset-rates
    intent: Get current exchange rates for an asset
    question: What is the current exchange rate of an asset against other assets?
  - id: core.get-asset-historical-rates
    intent: Get historical price history for an asset
    question: How has an asset's price moved over time?
  - id: core.list-networks
    intent: List supported networks
    question: Which blockchain and payment networks are supported?
  - id: core.get-network
    intent: Get details of one network
    question: What information is available about a specific network like Ethereum?
  - id: core.validate-network-address
    intent: Check if an address is valid on a network
    question: How do I check whether a wallet address is valid before sending funds?
  phrasing_ops: 13
  slug: uphold-assets-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Authentication.
  name: Uphold Authentication API
  phrasing_intents:
  - id: core.create-oauth2-token
    intent: Get an OAuth2 access token
    question: How do I get an access token to call the Uphold API?
  phrasing_ops: 1
  slug: uphold-authentication-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: User capabilities.
  name: Uphold Capabilities API
  phrasing_intents:
  - id: core.list-capabilities
    intent: List what a user is allowed to do
    question: Which capabilities does this user currently have, like trading or withdrawing?
  - id: core.get-capability
    intent: Check one user capability
    question: Can this user withdraw right now, and if not, why?
  phrasing_ops: 2
  slug: uphold-capabilities-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Countries.
  name: Uphold Countries API
  phrasing_intents:
  - id: core.list-countries
    intent: List supported countries
    question: Which countries are supported on the platform?
  - id: core.get-country
    intent: Get details for one country
    question: What are the details and support status for a specific country?
  phrasing_ops: 2
  slug: uphold-countries-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: External accounts.
  name: Uphold External accounts API
  phrasing_intents:
  - id: core.create-external-account
    intent: Link an external account
    question: How do I link a bank account or card as an external account?
  - id: core.list-external-accounts
    intent: List linked external accounts
    question: Which external bank accounts or cards has this user linked?
  - id: core.get-external-account
    intent: Get one external account
    question: How do I look up a single linked external account?
  - id: core.update-external-account
    intent: Rename a linked external account
    question: How do I change the label on a linked external account?
  - id: core.delete-external-account
    intent: Remove a linked external account
    question: How do I unlink an external account?
  phrasing_ops: 5
  slug: uphold-external-accounts-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Files.
  name: Uphold Files API
  phrasing_intents:
  - id: core.create-file
    intent: Create a file for upload
    question: How do I upload a document such as an ID image?
  - id: core.get-file
    intent: Get an uploaded file
    question: How do I check the status of a file I uploaded?
  - id: core.list-files-settings
    intent: List file upload settings
    question: What file sizes and formats are accepted for uploads?
  phrasing_ops: 3
  slug: uphold-files-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: General.
  name: Uphold General API
  phrasing_intents:
  - id: market-pulse.list-general-news
    intent: Get the latest general market news
    question: What is the latest overall crypto and market news?
  phrasing_ops: 1
  slug: uphold-general-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: The Ingestions API from Uphold — 0 operation(s) for ingestions.
  name: Uphold Ingestions API
  slug: uphold-ingestions-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Business User's KYB.
  name: Uphold KYB API
  slug: uphold-kyb-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Individual User's KYC.
  name: Uphold KYC API
  phrasing_intents:
  - id: core.get-kyc-overview
    intent: Get a user's KYC status overview
    question: Where does this user stand in identity verification?
  - id: core.update-kyc-profile
    intent: Submit a user's KYC profile details
    question: How do I submit a user's name and birth date for KYC?
  - id: core.update-kyc-address
    intent: Submit a user's residential address for KYC
    question: How do I provide a user's home address for verification?
  - id: core.update-kyc-email
    intent: Submit a user's email for KYC
    question: How do I verify a user's email address as part of onboarding?
  - id: core.update-kyc-phone
    intent: Submit a user's phone number for KYC
    question: How do I add a phone number to a user's verification?
  - id: core.update-kyc-identity
    intent: Update the identity verification step
    question: How do I move a user's identity document check forward?
  - id: core.update-kyc-proof-of-address
    intent: Update the proof-of-address step
    question: How do I progress a user's proof-of-address check?
  - id: core.update-kyc-customer-due-diligence
    intent: Submit customer due diligence answers
    question: How do I submit customer due diligence answers like source of funds?
  phrasing_ops: 13
  slug: uphold-kyc-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: KYC sharing.
  name: Uphold KYC sharing API
  phrasing_intents:
  - id: topper.identify-kyc-sharing-user
    intent: Identify a user for KYC sharing
    question: How do I check whether a user can reuse existing KYC via sharing?
  - id: topper.create-kyc-sharing-session
    intent: Start a KYC sharing session
    question: How do I start a session so a user can share their KYC data?
  phrasing_ops: 2
  slug: uphold-kyc-sharing-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Metadata.
  name: Uphold Metadata API
  phrasing_intents:
  - id: core.get-metadata
    intent: Get custom metadata on a record
    question: How do I read the custom metadata attached to an account or transaction?
  - id: core.set-metadata
    intent: Create or replace metadata on a record
    question: How do I attach my own metadata to an account or transaction?
  - id: core.update-metadata
    intent: Partially update metadata on a record
    question: How do I change a few metadata keys without replacing the rest?
  - id: core.delete-metadata
    intent: Delete metadata from a record
    question: How do I remove all custom metadata from an entity?
  phrasing_ops: 4
  slug: uphold-metadata-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Payment.
  name: Uphold Payment API
  phrasing_intents:
  - id: widgets.create-payment-widget-session
    intent: Start a Payment Widget session
    question: How do I launch the embedded Payment Widget for a user?
  phrasing_ops: 1
  slug: uphold-payment-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Portfolio.
  name: Uphold Portfolio API
  phrasing_intents:
  - id: core.get-portfolio-overview
    intent: Get the total portfolio value and holdings
    question: What is my whole portfolio worth right now and what is in it?
  - id: core.get-portfolio-performance
    intent: Get overall portfolio performance
    question: How much have I gained or lost across my whole portfolio?
  - id: core.get-portfolio-historical-balance
    intent: Get portfolio balance history
    question: How has my total portfolio balance changed over time?
  - id: core.get-portfolio-asset-performance
    intent: Get performance of one asset I hold
    question: How is my Bitcoin position performing?
  - id: core.get-portfolio-many-assets-performance
    intent: Compare performance of several assets I hold
    question: Can I get gains and losses for several of my assets in one call?
  - id: core.get-portfolio-asset-historical-balance
    intent: Get balance history for one asset I hold
    question: How has my balance in a specific asset changed over time?
  - id: core.get-portfolio-account-performance
    intent: Get performance of one account
    question: How is one particular account performing?
  - id: core.get-portfolio-many-accounts-performance
    intent: Compare performance of several accounts
    question: Can I get performance for several accounts in one request?
  phrasing_ops: 9
  slug: uphold-portfolio-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Statements.
  name: Uphold Statements API
  phrasing_intents:
  - id: core.get-portfolio-statement
    intent: Get a portfolio statement for a period
    question: How do I get my monthly portfolio statement?
  - id: core.get-transactions-statement
    intent: Get a transactions statement for a period
    question: Where can I get a statement of all my transactions for a month?
  phrasing_ops: 2
  slug: uphold-statements-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Sumsub KYC Connector.
  name: Uphold Sumsub API
  phrasing_intents:
  - id: kyc-connector.create-sumsub-ingestion
    intent: Import KYC data from Sumsub
    question: How do I import a user's existing Sumsub verification?
  - id: kyc-connector.list-sumsub-ingestions
    intent: List Sumsub KYC imports
    question: Which Sumsub verifications have been imported for this user?
  - id: kyc-connector.get-sumsub-ingestion
    intent: Check a Sumsub KYC import
    question: How do I check whether a Sumsub import finished?
  phrasing_ops: 3
  slug: uphold-sumsub-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: User terms of service.
  name: Uphold Terms of service API
  phrasing_intents:
  - id: core.list-terms-of-service
    intent: List applicable terms of service
    question: Which terms of service apply to users in a given country?
  - id: core.get-terms-of-service
    intent: Get one terms of service document
    question: How do I read a specific terms of service document?
  - id: core.accept-terms-of-service
    intent: Accept terms of service
    question: How do I record that a user accepted the terms of service?
  phrasing_ops: 3
  slug: uphold-terms-of-service-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Transactions.
  name: Uphold Transactions API
  phrasing_intents:
  - id: core.create-quote
    intent: Get a quote for a transfer or trade
    question: How do I get a price quote before converting or sending funds?
  - id: core.list-account-transactions
    intent: List transactions on one account
    question: How do I see the transaction history of one specific account?
  - id: core.list-transactions
    intent: List all of a user's transactions
    question: Where do I see every transaction across all my accounts?
  - id: core.create-transaction
    intent: Execute a transaction from a quote
    question: How do I commit a quote to actually execute the trade or transfer?
  - id: core.get-transaction
    intent: Get one transaction
    question: How do I check the status of a single transaction?
  - id: core.list-transaction-requests-for-information
    intent: List compliance questions on a transaction
    question: Why is my transaction on hold waiting for more information?
  - id: core.get-transaction-request-for-information
    intent: Get one request for information
    question: What exactly does a specific request for information ask for?
  - id: core.update-transaction-request-for-information
    intent: Answer a request for information
    question: How do I respond to a compliance request for information on a transaction?
  phrasing_ops: 8
  slug: uphold-transactions-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Travel rule.
  name: Uphold Travel rule API
  phrasing_intents:
  - id: widgets.create-travel-rule-widget-session
    intent: Start a Travel Rule widget session
    question: How do I collect Travel Rule originator and beneficiary info with the widget?
  phrasing_ops: 1
  slug: uphold-travel-rule-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Users.
  name: Uphold Users API
  phrasing_intents:
  - id: core.create-user
    intent: Create a new user
    question: How do I create a new end user on the platform?
  - id: core.get-user
    intent: Get the current user's profile
    question: How do I fetch the profile of the signed-in user?
  - id: core.delete-user
    intent: Delete the current user
    question: How do I delete a user's account entirely?
  phrasing_ops: 3
  slug: uphold-users-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Veriff KYC Connector.
  name: Uphold Veriff API
  phrasing_intents:
  - id: kyc-connector.create-veriff-ingestion
    intent: Import KYC data from Veriff sessions
    question: How do I import a user's completed Veriff sessions as KYC?
  - id: kyc-connector.list-veriff-ingestions
    intent: List Veriff KYC imports
    question: Which Veriff verifications have been imported for this user?
  - id: kyc-connector.get-veriff-ingestion
    intent: Check a Veriff KYC import
    question: How do I check whether a Veriff import finished?
  - id: kyc-connector.set-veriff-config
    intent: Configure Veriff for the organization
    question: How do I connect my Veriff integrations to the KYC connector?
  - id: kyc-connector.get-veriff-config
    intent: Get the organization's Veriff configuration
    question: How is Veriff configured for my organization?
  phrasing_ops: 5
  slug: uphold-veriff-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Webhooks.
  name: Uphold Webhooks API
  phrasing_intents:
  - id: core.create-webhook-management-link
    intent: Get a link to manage webhooks
    question: How do I configure webhooks for event notifications?
  phrasing_ops: 1
  slug: uphold-webhooks-api
artifact_total: 57
asyncapis:
- description: ''
  name: Uphold Core Webhooks
  slug: uphold-core-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Core Accounts API
  slug: open-uphold-accounts-api
- collection_type: open
  name: Uphold Assets API
  slug: open-uphold-assets-api
- collection_type: open
  name: Core Authentication API
  slug: open-uphold-authentication-api
- collection_type: open
  name: Core Capabilities API
  slug: open-uphold-capabilities-api
- collection_type: open
  name: Core Countries API
  slug: open-uphold-countries-api
- collection_type: open
  name: Core External accounts API
  slug: open-uphold-external-accounts-api
- collection_type: open
  name: Core Files API
  slug: open-uphold-files-api
- collection_type: open
  name: Market Pulse General API
  slug: open-uphold-general-api
- collection_type: open
  name: KYC Connectors Ingestions API
  slug: open-uphold-ingestions-api
- collection_type: open
  name: Core KYB API
  slug: open-uphold-kyb-api
- collection_type: open
  name: Uphold KYC API
  slug: open-uphold-kyc-api
- collection_type: open
  name: Topper KYC sharing API
  slug: open-uphold-kyc-sharing-api
- collection_type: open
  name: Core Metadata API
  slug: open-uphold-metadata-api
- collection_type: open
  name: Widget Payment API
  slug: open-uphold-payment-api
- collection_type: open
  name: Core Portfolio API
  slug: open-uphold-portfolio-api
- collection_type: open
  name: Core Statements API
  slug: open-uphold-statements-api
- collection_type: open
  name: KYC Connectors Sumsub API
  slug: open-uphold-sumsub-api
- collection_type: open
  name: Core Terms of service API
  slug: open-uphold-terms-of-service-api
- collection_type: open
  name: Core Transactions API
  slug: open-uphold-transactions-api
- collection_type: open
  name: Widget Travel rule API
  slug: open-uphold-travel-rule-api
- collection_type: open
  name: Core Users API
  slug: open-uphold-users-api
- collection_type: open
  name: KYC Connectors Veriff API
  slug: open-uphold-veriff-api
- collection_type: open
  name: Core Webhooks API
  slug: open-uphold-webhooks-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/plans/uphold-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uphold-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/capabilities/uphold-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/uphold-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/uphold/docs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/uphold/docs/releases
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/overlays/uphold-core-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uphold-core-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://uphold.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uphold.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uphold.com/rest-apis/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uphold.com/rest-apis/core-api/concepts
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uphold.com/get-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://developer.uphold.com/get-started/make-your-first-api-call
- group: operate
  title: ''
  type: Support
  url: https://support.uphold.com/
- group: company
  title: ''
  type: Blog
  url: https://uphold.com/en-us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uphold
- group: commercial
  title: ''
  type: Pricing
  url: https://uphold.com/en-us/get-started/service-fees
- group: start
  title: ''
  type: SignUp
  url: https://portal.enterprise.uphold.com/
- group: start
  title: ''
  type: Login
  url: https://portal.enterprise.uphold.com/
- group: commercial
  title: ''
  type: DeveloperAgreement
  url: https://uphold.com/en-us/legal/developer-agreement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uphold.com/en-us/legal/membership-agreement/usa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uphold.com/en-us/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/uphold/workspace/enterprise-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uphold.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.uphold.com/rest-apis/versioning
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/changelog/uphold-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uphold-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/lifecycle/uphold-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uphold-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://uphold.com/en-us/get-started/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/security/uphold-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/uphold-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/security/uphold-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/uphold-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://uphold.com/en-us/get-started/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/security/uphold-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uphold-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/well-known/uphold-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uphold-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/well-known/uphold-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uphold-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/llms/uphold-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uphold-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/a2a/uphold-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/uphold-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/mcp/uphold-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/uphold-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/authentication/uphold-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uphold-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/scopes/uphold-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/uphold-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/conventions/uphold-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uphold-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/conformance/uphold-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uphold-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/errors/uphold-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uphold-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/errors/uphold-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/uphold-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/data-model/uphold-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uphold-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/packages/uphold-packages.yml
  title: ''
  type: Packages
  url: packages/uphold-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/packages/uphold-packages.yml
  title: ''
  type: SDKs
  url: packages/uphold-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/components/uphold-components.yml
  title: ''
  type: Components
  url: components/uphold-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/sandbox/uphold-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/uphold-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/asyncapi/uphold-core-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uphold-core-webhooks.yml
created: '2026-08-05'
description: Uphold is a multi-asset digital money platform and regulated crypto exchange that lets consumers and businesses hold, trade, send and spend more than 300 cryptocurrencies, national currencies and precious metals from a single account. Its Enterprise API Suite ("Move on chain") is a modular set of OpenAPI 3.1 REST APIs — Core, Widgets, Topper, Market Pulse and KYC Connector — that partners embed to onboard and KYC/KYB-verify users, move value across bank rails (ACH, FedNow/RTP, Wire, FPS, SEPA), debit and credit cards, alternative payment methods (Apple Pay, PayPal) and 50+ blockchain networks, and to run buy/sell, trade, send, portfolio, statements and FATF Travel Rule flows. Uphold also runs a public legacy market-data and wallet API at api.uphold.com/v0, publishes embeddable Payment, KYC and Travel Rule widgets, a Svix-backed webhook event surface, a full Sandbox with test helpers, a public Postman workspace, an llms.txt, an A2A agent card and a documentation MCP server.
image: https://cdn.prod.website-files.com/65116a8935747aeda81c6865/65a8ffa13ea101b31a905d2f_UPHOLD%20LOGO-2.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.uphold.com over HTTP; 3 tools listed.
  name: Uphold
  slug: uphold
modified: '2026-08-05'
name: Uphold
nav: Providers
network: true
overview: 'Uphold publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Assets API, Authentication API, and 22 more. Tagged areas include Company, Cryptocurrency, Digital Assets, Payments, and Banking.


  The Uphold catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uphold''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 41 more developer resources.'
plans:
- name: Uphold Plans Pricing
  plan_count: 15
  slug: uphold-plans-pricing
random_paper: 14
scopes:
- name: Uphold Scopes
  scope_count: 64
  slug: uphold-scopes
  summary_line: 64 scopes · clientCredentials
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 60.3
    developer_ergonomics: 81.0
    discoverability: 80.0
    operational_transparency: 60.5
  previous_composite: 70.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/screenshots/uphold-2026-08-17T081941.png
security:
- kind: authentication
  name: Uphold Authentication
  slug: uphold-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Uphold Domain Security
  slug: uphold-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Uphold Vulnerability Disclosure
  slug: uphold-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Uphold Trust Center
  slug: uphold-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS
slug: uphold
tags:
- Company
- Cryptocurrency
- Digital Assets
- Payments
- Banking
- Fintech
- KYC
- Compliance
- Crypto Exchange
- Market Data
- Embedded Finance
- Travel Rule
- Webhook
- Agent-Native
- A2A
website: https://uphold.com/
---
