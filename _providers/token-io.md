---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Token Io Agentic Access
  operation_count: 71
  slug: token-io-agentic-access
  summary_line: 71 operations · 24 acting · 1 human-in-the-loop
api_count: 29
apis:
- description: Official Token.io JavaScript SDK for Node.js and browser environments interacting with the Token System and Open Banking API.
  name: Token.io JavaScript SDK
  slug: javascript-sdk
- description: Official Token.io PHP SDK for interacting with the Token System and Open Banking API.
  name: Token.io PHP SDK
  slug: php-sdk
- description: Official Token.io C# / .NET SDK for the Open Banking API.
  name: Token.io C# SDK
  slug: csharp-sdk
- description: Official Token.io Objective-C SDK for iOS.
  name: Token.io Objective-C SDK
  slug: objc-sdk
- description: iOS webview SDK for embedding Token.io Hosted Payments pages in native iOS apps.
  name: Token.io iOS Webview SDK
  slug: ios-webview-sdk
- description: Android webview SDK for embedding Token.io Hosted Payments pages in native Android apps.
  name: Token.io Android Webview SDK
  slug: android-webview-sdk
- description: Java merchant checkout sample illustrating Token.io payment initiation flows.
  name: Merchant Sample (Java)
  slug: merchant-sample-java
- description: Simple JavaScript merchant checkout example for Token.io.
  name: Merchant Sample (JavaScript)
  slug: merchant-sample-js
- description: Sample implementation of the Token Bank Integration API in Java.
  name: Bank Sample (Java)
  slug: bank-sample-java
- description: Simple personal finance app illustrating Token.io's Access Tokens for AIS use cases.
  name: Personal Finance Management Sample (Java)
  slug: pfm-sample-java
- description: Hands-on workshop for integrating a merchant with Token Checkout.
  name: Merchant Integration Workshop
  slug: merchant-integration-workshop
- description: These endpoints allow you to create and manage an Account on File from bank account details. The Account on File can then be used in other API requests instead of sending the full account details.
  name: token-io Account on File API
  slug: token-io-account-on-file-api
- description: These endpoints provide authorized access to an authenticated user's account information.
  name: token-io Accounts API
  slug: token-io-accounts-api
- description: These endpoints are for managing the public keys that are used for JWT authentication.
  name: token-io Authentication keys API
  slug: token-io-authentication-keys-api
- description: These endpoints filter and fetch the list of connected banks, get information on specific banks, and initiate authorization with user-selected banks using Payments v1.
  name: token-io Banks v1 API
  slug: token-io-banks-v1-api
- description: This endpoint filters and fetches the list of connected banks, gets information on specific banks, and initiates authorization with user-selected banks using Payments v2.
  name: token-io Banks v2 API
  slug: token-io-banks-v2-api
- description: These endpoints allow you to create and manage payment links. Payment links are reusable or single-use payment URLs that can be shared with customers, supporting fixed or variable amounts, usage limit
  name: token-io Pay by Link API
  slug: token-io-pay-by-link-api
- description: Creates and initiates a single immediate payment or a future-dated payment. Also supports initiating a Variable Recurring Payment (VRP) using an existing VRP mandate that has been created and authoris
  name: token-io Payments v2 API
  slug: token-io-payments-v2-api
- description: These endpoints allow you to make payouts.
  name: token-io Payouts API
  slug: token-io-payouts-api
- description: These endpoints allow you to handle registration, posting, and retrieval of refunds associated with original transaction account information.
  name: token-io Refunds API
  slug: token-io-refunds-api
- description: These endpoints retrieve the current AIS and PIS status of connected banks.
  name: token-io Reports API
  slug: token-io-reports-api
- description: These endpoints allow you to initiate a Payments v1 request or an AIS request, and retrieve the status of the request.
  name: token-io Requests - for Payments v1 or AIS API
  slug: token-io-requests-for-payments-v1-or-ais-api
- description: These endpoints provide authorized access to an authenticated user's settlement account information, enabling you to create settlement accounts, retrieve settlement account details, transactions and p
  name: token-io Settlement Accounts API
  slug: token-io-settlement-accounts-api
- description: These endpoints are for resellers using Token.io's licence to create, retrieve and delete sub-TPPs.
  name: token-io Sub-TPPs API
  slug: token-io-sub-tpps-api
- description: These endpoints retrieve all tokens, a filtered list of tokens, or a specific token, as well as allowing you to cancel an existing token.
  name: token-io Tokens API
  slug: token-io-tokens-api
- description: These endpoints relate to transfers, which are requests to move money between accounts.
  name: token-io Transfers - for Payments v1 API
  slug: token-io-transfers-for-payments-v1-api
- description: These endpoints enable you to initiate Variable Recurring Payments (VRP). Note, that VRP is also available in Payments v2 API.
  name: token-io Variable Recurring Payments API
  slug: token-io-variable-recurring-payments-api
- description: The Verification API from token-io — 1 operation(s) for verification.
  name: token-io Verification API
  slug: token-io-verification-api
- description: These endpoints configure, retrieve and remove webhooks. See <a href="https://developer.token.io/token_rest_api_doc/content/e-rest/api-basics.htm#Webhook" target="_blank">Webhooks</a> for more details
  name: token-io Webhooks API
  slug: token-io-webhooks-api
artifact_total: 113
collections:
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File API
  slug: postman-token-io-account-on-file-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Accounts API
  slug: postman-token-io-accounts-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Authentication keys API
  slug: postman-token-io-authentication-keys-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Banks v1 API
  slug: postman-token-io-banks-v1-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Banks v2 API
  slug: postman-token-io-banks-v2-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Pay by Link API
  slug: postman-token-io-pay-by-link-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Payments v2 API
  slug: postman-token-io-payments-v2-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Payouts API
  slug: postman-token-io-payouts-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Refunds API
  slug: postman-token-io-refunds-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Reports API
  slug: postman-token-io-reports-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Requests - for Payments v1 or AIS API
  slug: postman-token-io-requests-for-payments-v1-or-ais-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Settlement Accounts API
  slug: postman-token-io-settlement-accounts-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Sub-TPPs API
  slug: postman-token-io-sub-tpps-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Tokens API
  slug: postman-token-io-tokens-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Transfers - for Payments v1 API
  slug: postman-token-io-transfers-for-payments-v1-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Variable Recurring Payments API
  slug: postman-token-io-variable-recurring-payments-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Verification API
  slug: postman-token-io-verification-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Webhooks API
  slug: postman-token-io-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File API
  slug: open-token-io-account-on-file-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Accounts API
  slug: open-token-io-accounts-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Authentication keys API
  slug: open-token-io-authentication-keys-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Banks v1 API
  slug: open-token-io-banks-v1-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Banks v2 API
  slug: open-token-io-banks-v2-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Pay by Link API
  slug: open-token-io-pay-by-link-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Payments v2 API
  slug: open-token-io-payments-v2-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Payouts API
  slug: open-token-io-payouts-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Refunds API
  slug: open-token-io-refunds-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Reports API
  slug: open-token-io-reports-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Requests - for Payments v1 or AIS API
  slug: open-token-io-requests-for-payments-v1-or-ais-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Settlement Accounts API
  slug: open-token-io-settlement-accounts-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Sub-TPPs API
  slug: open-token-io-sub-tpps-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Tokens API
  slug: open-token-io-tokens-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Transfers - for Payments v1 API
  slug: open-token-io-transfers-for-payments-v1-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Variable Recurring Payments API
  slug: open-token-io-variable-recurring-payments-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Verification API
  slug: open-token-io-verification-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Webhooks API
  slug: open-token-io-webhooks-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs
  slug: open-token-io
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/token-io/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/token-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/token-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/token-io-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://token.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.token.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.token.io/products/tpp
- group: docs
  title: ''
  type: Reference
  url: https://reference.token.io/
- group: operate
  title: ''
  type: Support
  url: https://support.token.io
- group: start
  title: ''
  type: Sandbox
  url: https://dashboard.sandbox.token.io/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokenio
- group: commercial
  title: ''
  type: Pricing
  url: https://token.io/contact/pricing
- group: company
  title: ''
  type: News
  url: https://token.io/news
- group: company
  title: ''
  type: Blog
  url: https://token.io/blog
- group: operate
  title: ''
  type: FAQ
  url: https://token.io/faq
- group: commercial
  title: ''
  type: License
  url: https://www.openbanking.org.uk/regulated-providers/token/
- group: commercial
  title: ''
  type: Plans
  url: plans/token-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/token-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/token-io-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Token.io is an Open Banking infrastructure provider offering A2A (Account-to-Account) payments and account information services across Europe. Founded in 2016 and FCA-authorised since 2018, Token.io was the first payment initiation service provider to conduct an end-to-end PSD2-compliant Open Banking transaction. The Token.io platform connects developers and TPPs to over 4,000 banks via a single standardised API supporting Payment Initiation Services (PIS), Account Information Services (AIS), Variable Recurring Payments (VRP), refunds, payouts, settlement accounts, account verification, and Pay-by-Link checkout. Used by merchants, PSPs, fintechs, PFM apps, and platform businesses to replace card-rail payments and aggregate multibank data.
features:
- Single Immediate Payments (SIP) via Payments v2
- Future-Dated Payments
- Variable Recurring Payments (VRP) — sweeping and commercial / non-sweeping
- VRP Consents with fund availability checks
- Account Information Services (AIS) — balances, transactions, standing orders, account details
- Pay by Link — reusable payment URLs with usage and amount limits
- Account on File — tokenized bank account references for repeat payments
- Refunds tied to original payment transactions
- Payouts — outbound transfer execution and monitoring
- Settlement Accounts — virtual accounts, transaction lists, and settlement rules
- Account Verification — name and account-holder confirmation checks
- Banks v1 and Banks v2 — discovery of 4,000+ connected banks across Europe
- Sub-TPP management for reseller and platform models
- Authentication Keys API for managing JWT public keys
- Webhooks for event notifications across payments and AIS lifecycle
- Reports API for monitoring AIS/PIS bank status
- JWT Bearer Token authentication (production and sandbox)
- Basic Auth for sandbox testing
- Hosted Payment Pages via iOS and Android webview SDKs
- PSD2-compliant Payment Initiation Service (PIS) and Account Information Service (AIS)
- FCA-authorised UK PISP / AISP since 2018
- Coverage across UK and EU SEPA payment rails
- Official SDKs for JavaScript, PHP, C#, and Objective-C
- Sandbox environment at dashboard.sandbox.token.io
finops:
- name: Token Io Finops
  service_category: Financial Services - Open Banking Infrastructure
  slug: token-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/token-io.png
json_schemas:
- name: Token.io Account
  property_count: 0
  slug: token-io-account
- name: Token.io Payment
  property_count: 0
  slug: token-io-payment
- name: Token.io VRP Consent
  property_count: 11
  slug: token-io-vrp-consent
jsonld:
- class_count: 0
  name: Token Io Context
  property_count: 6
  slug: token-io-context
layout: provider
modified: '2026-05-25'
name: token-io
nav: Providers
network: true
overview: 'token-io publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account on File API, Accounts API, Authentication keys API, and 15 more.


  The token-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  token-io''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, sandbox, pricing, and 12 more developer resources.'
plans:
- name: Token Io Plans Pricing
  plan_count: 4
  slug: token-io-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Token Io Rate Limits
  slug: token-io-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: token-io API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: token-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.4
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 68.5
    developer_ergonomics: 69.0
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/token-io/refs/heads/main/screenshots/token-io-2026-06-20T195438.png
security:
- kind: authentication
  name: Token Io Authentication
  slug: token-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Token Io Domain Security
  slug: token-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: token-io
use_cases:
- E-commerce Pay-by-Bank checkout (Account-to-Account payments)
- Subscription billing via VRP commercial mandates
- Utility bill recurring payments via VRP
- Account top-ups (investment, gaming, mobile, savings)
- Charity donations (zero-fee for charitable organisations)
- Personal Finance Management (PFM) multibanking via AIS
- Peer-to-peer (P2P) and Business-to-Business (B2B) payments
- Lending and credit risk assessment via account data
- Account verification for KYC and anti-fraud workflows
- Payouts and settlements for marketplaces and platforms
- Reseller / Sub-TPP platform integrations
website: https://token.io
---
