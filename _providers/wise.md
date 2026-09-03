---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 147
  human_in_the_loop: 6
  name: Wise Agentic Access
  operation_count: 238
  slug: wise-agentic-access
  summary_line: 238 operations · 147 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: To manage certain aspects of the 3D Secure (3DS) authentication, you will need to integrate with the following APIs.
  name: Wise 3ds API
  slug: wise-3ds-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Activity represents a snapshot of a performed action for a profile.
  name: Wise activity API
  slug: wise-activity-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Manage physical addresses associated with user profiles. Address requirements vary by country — use the address requirements endpoints to dynamically discover which fields are needed before creating a
  name: Wise address API
  slug: wise-address-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'Create and manage balance accounts within a multi-currency account. Each profile can hold multiple balance accounts in different currencies. A `STANDARD` balance is limited to one per currency, while '
  name: Wise balance API
  slug: wise-balance-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Balance statements contain transactional activities on a Wise Multi-Currency Account, including deposits, withdrawals, conversions, card transactions, and fees. Statements can be retrieved in multiple
  name: Wise balance-statement API
  slug: wise-balance-statement-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'Bank account details allow users to receive money into their Wise Multi-Currency Account. Each currency balance can have local bank details (for domestic payments) and international bank details (for '
  name: Wise bank-account-details API
  slug: wise-bank-account-details-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: A batch group is a named collection of up to 1000 transfers that can be managed as a single unit. Batch groups are primarily used for funding multiple transfers with a single payment. **Workflow:** 1.
  name: Wise batch-group API
  slug: wise-batch-group-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Bulk settlement allows partners to settle multiple transfers in a single bank transfer at the end of a settlement period. This model splits transfer creation/funding from final settlement, allowing Wi
  name: Wise bulk-settlement API
  slug: wise-bulk-settlement-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Manage your customers' cards programmatically. These APIs allow you to list cards, retrieve card details, control card status, and manage spending permissions. **Key capabilities:** - List and retriev
  name: Wise card API
  slug: wise-card-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: These APIs are designed to allow you to print and encrypt your card directly from a kiosk machine. The card information will be sent to our card manufacturer to configure and print the card on-site on
  name: Wise card-kiosk-collection API
  slug: wise-card-kiosk-collection-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: With this set of APIs, you will be able to create cards for your customers. You can also retrieve and view the status of your current card orders, as well as the list of available card programs for th
  name: Wise card-order API
  slug: wise-card-order-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Wise is a PCI DSS compliant provider and stores all card data securely. The scope for PCI compliance depends on your use case and will impact how you integrate. For all sensitive card details endpoint
  name: Wise card-sensitive-details API
  slug: wise-card-sensitive-details-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'Retrieve information on transactions made on your users'' cards. Transaction types {% #card-transaction-type .title-3 .m-t-5 %} The possible `type` values are: - `ACCOUNT_CREDIT` - Receiving money on t'
  name: Wise card-transaction API
  slug: wise-card-transaction-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'Partner Cases are part of the Partner Support API, allowing partners to open, retrieve and respond to support and operations queries. The endpoints described here allow partners to directly integrate '
  name: Wise case API
  slug: wise-case-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Allow a customer to take ownership of an account [created on their behalf](/api-reference/user/usercreate). Generate a short-lived `claim_account_code` and use it when [redirecting the customer to Wis
  name: Wise claim-account API
  slug: wise-claim-account-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'The comparison API can be used to request price and speed information about various money transfer providers. This includes not only Wise but other providers in the market. Price Estimation {% #compar'
  name: Wise comparison API
  slug: wise-comparison-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Find discoverable Wise profiles and add them to your recipient list using an identifier — such as a Wisetag, email, or phone number — without needing bank details. Creating a transfer with a contact {
  name: Wise contact API
  slug: wise-contact-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Retrieve the list of currencies supported for transfers, including currency codes and display names.
  name: Wise currencies API
  slug: wise-currencies-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Get the estimated delivery time for a transfer, showing when funds are expected to arrive in the recipient's bank account.
  name: Wise delivery-estimate API
  slug: wise-delivery-estimate-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: These APIs provide encrypted cardholder information needed to implement push provisioning (Apple Pay, Google Pay) in your own mobile app.
  name: Wise digital-wallet API
  slug: wise-digital-wallet-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Register and retrieve external bank accounts used to fund batch transfers via ACH (USD) or EFT (CAD) direct debit.
  name: Wise direct-debit-account API
  slug: wise-direct-debit-account-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'Raise and manage card transaction disputes, including submission via Dynamic Flow or direct API, file uploads, and dispute lifecycle tracking. For implementation details, see: - [Disputes via Dynamic '
  name: Wise disputes API
  slug: wise-disputes-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Wise leverages [FaceTec's](https://www.facetec.com/) facial biometric technology for authentication. Use this endpoint to retrieve the public key needed for exporting 3D FaceMaps.
  name: Wise facetec API
  slug: wise-facetec-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Wise uses the [JOSE framework](https://jose.readthedocs.io/en/latest/) to accept and respond with signed and encrypted payloads. These endpoints allow you to manage keys and test your signing and encr
  name: Wise jose API
  slug: wise-jose-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'KYC Review API provides endpoints to view, update and submit information related to the KYC flow. There are two ways to collect KYC requirements from your customers: - **Hosted KYC** — redirect your c'
  name: Wise kyc-review API
  slug: wise-kyc-review-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: The Wise multi-currency account (MCA) enables users to hold, convert, and fund transfers (single or batches) with balances in up to 56 currencies. Of the 50+ currency balances supported, 10+ come with
  name: Wise multi-currency-account API
  slug: wise-multi-currency-account-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: 'Exchange client credentials or authorisation grants for OAuth 2.0 access tokens. All grant types use `POST /oauth/token` with basic authentication (your `client_id` and `client_secret`). Depending on '
  name: Wise oauth-token API
  slug: wise-oauth-token-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: The payin deposit details API allows you to get the bank details for the account that the customer should send funds to when paying for a Wise transfer via a bank transfer. These details will be provi
  name: Wise payin-deposit-detail API
  slug: wise-payin-deposit-detail-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: The payin APIs allow you to fund the MCA or transfers with local payment rails, by retrieving or creating the relevant details to send to for funding a payment. These details will be provided in the l
  name: Wise payins API
  slug: wise-payins-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: A profile represents an identity that can send and receive money through Wise — either a personal profile (an individual) or a business profile (a company). Most API endpoints require a `profileId` pa
  name: Wise profile API
  slug: wise-profile-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: The quote resource defines the basic information required for a Wise transfer - the currencies to send between, the amount to send and the profile who is sending the money. The profile _must_ be inclu
  name: Wise quote API
  slug: wise-quote-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Current and historical exchange rates by currency routes.
  name: Wise rate API
  slug: wise-rate-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Recipient or beneficiary is the one who will receive the funds. Recipient account endpoints use a mixture of our v1 and v2 APIs. Please ensure you address the right version to get the expected results
  name: Wise recipient API
  slug: wise-recipient-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Device fingerprints are possession-based SCA challenge factors. They allow you to verify that a user is accessing the API from a recognized device. A profile can have up to 3 device fingerprints regis
  name: Wise sca-device-fingerprints API
  slug: wise-sca-device-fingerprints-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Facemaps are inherence-based (biometric) SCA challenge factors that use FaceTec's 3D face recognition technology. Facemaps should be exported from your FaceTec server using their SDK's export API. Use
  name: Wise sca-facemaps API
  slug: wise-sca-facemaps-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: For phone-based OTP (one-time password) authentication — where an OTP is a single-use 6-digit code sent to verify the identity of a user — Wise supports multiple delivery methods, including SMS, Whats
  name: Wise sca-otp API
  slug: wise-sca-otp-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: One-time tokens are temporary authentication sessions used to track SCA challenges. When an SCA-protected endpoint is called, a one-time token is returned containing the challenges that must be comple
  name: Wise sca-ott API
  slug: wise-sca-ott-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: PIN (Personal Identification Number) is a knowledge-based SCA challenge factor. Users create a 4-digit PIN that can be used to verify their identity when accessing SCA-protected endpoints. All PIN cre
  name: Wise sca-pin API
  slug: wise-sca-pin-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: SCA sessions allow you to manually trigger Strong Customer Authentication, returning a one-time token along with a list of associated challenges. These challenges can be cleared using the verify endpo
  name: Wise sca-sessions API
  slug: wise-sca-sessions-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Use these endpoints to simulate key actions in the sandbox environment, including transfer state changes, balance top-ups, card transactions, KYC reviews, and incoming payments. {% admonition type="in
  name: Wise simulation API
  slug: wise-simulation-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Control which card transactions are permitted by creating rules based on merchant category code (MCC) or transaction currency. An authorisation rule dictates whether transactions should be declined or
  name: Wise spend-controls API
  slug: wise-spend-controls-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Manage spending limits applied to profiles and cards. Profile limits are shared across all cards under the same profile, while card limits apply to individual cards. For more details on how profile an
  name: Wise spend-limits API
  slug: wise-spend-limits-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: A transfer is a payment order to a [recipient account](/api-reference/recipient) based on a [quote](/api-reference/quote). Once created, a transfer usually needs to be funded within fourteen days. Oth
  name: Wise transfer API
  slug: wise-transfer-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: A User serves as the primary entity and can possess multiple Profiles to represent different contexts or settings. A User can have one personal Profile and multiple business Profiles. Each [Profile](/
  name: Wise user API
  slug: wise-user-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: '{% admonition type="warning" %} These endpoints are deprecated. Please refer to [PIN](/api-reference/sca-pin), [Facemaps](/api-reference/sca-facemaps), and [Device Fingerprints](/api-reference/sca-dev'
  name: Wise user-security API
  slug: wise-user-security-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: In certain situations, additional evidence is required to verify customers and ensure we’re compliant with the KYC regulations. Additional Verification APIs support a list of evidences that can be fou
  name: Wise verification API
  slug: wise-verification-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Manage webhook subscriptions at both the application and profile level. Create, list, retrieve, and delete subscriptions, as well as test your webhook endpoints. For more information on creating and m
  name: Wise webhook API
  slug: wise-webhook-api
- baseURL: https://api.wise.com/v2
  baseurl_source: declared
  description: Webhook events are notifications sent by Wise to your server when specific actions occur. Subscribe to events using the [Webhook](/api-reference/webhook) endpoints at the application or profile level.
  name: Wise Webhook Event API
  slug: wise-webhook-event-api
artifact_total: 107
asyncapis:
- description: AsyncAPI 2.6 description of the Wise Platform webhook surface. Wise pushes HTTP `POST` notifications to subscriber-defined HTTPS endpoints when events occur against profiles, transfers, balances, card
  name: Wise Platform Webhooks
  slug: wise-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wise Platform 3ds API
  slug: open-wise-3ds-api
- collection_type: open
  name: Wise Platform 3ds activity API
  slug: open-wise-activity-api
- collection_type: open
  name: Wise Platform 3ds address API
  slug: open-wise-address-api
- collection_type: open
  name: Wise Platform 3ds balance API
  slug: open-wise-balance-api
- collection_type: open
  name: Wise Platform 3ds balance-statement API
  slug: open-wise-balance-statement-api
- collection_type: open
  name: Wise Platform 3ds bank-account-details API
  slug: open-wise-bank-account-details-api
- collection_type: open
  name: Wise Platform 3ds batch-group API
  slug: open-wise-batch-group-api
- collection_type: open
  name: Wise Platform 3ds bulk-settlement API
  slug: open-wise-bulk-settlement-api
- collection_type: open
  name: Wise Platform 3ds card API
  slug: open-wise-card-api
- collection_type: open
  name: Wise Platform 3ds card-kiosk-collection API
  slug: open-wise-card-kiosk-collection-api
- collection_type: open
  name: Wise Platform 3ds card-order API
  slug: open-wise-card-order-api
- collection_type: open
  name: Wise Platform 3ds card-sensitive-details API
  slug: open-wise-card-sensitive-details-api
- collection_type: open
  name: Wise Platform 3ds card-transaction API
  slug: open-wise-card-transaction-api
- collection_type: open
  name: Wise Platform 3ds case API
  slug: open-wise-case-api
- collection_type: open
  name: Wise Platform 3ds claim-account API
  slug: open-wise-claim-account-api
- collection_type: open
  name: Wise Platform 3ds comparison API
  slug: open-wise-comparison-api
- collection_type: open
  name: Wise Platform 3ds contact API
  slug: open-wise-contact-api
- collection_type: open
  name: Wise Platform 3ds currencies API
  slug: open-wise-currencies-api
- collection_type: open
  name: Wise Platform 3ds delivery-estimate API
  slug: open-wise-delivery-estimate-api
- collection_type: open
  name: Wise Platform 3ds digital-wallet API
  slug: open-wise-digital-wallet-api
- collection_type: open
  name: Wise Platform 3ds direct-debit-account API
  slug: open-wise-direct-debit-account-api
- collection_type: open
  name: Wise Platform 3ds disputes API
  slug: open-wise-disputes-api
- collection_type: open
  name: Wise Platform 3ds facetec API
  slug: open-wise-facetec-api
- collection_type: open
  name: Wise Platform 3ds jose API
  slug: open-wise-jose-api
- collection_type: open
  name: Wise Platform 3ds multi-currency-account API
  slug: open-wise-multi-currency-account-api
- collection_type: open
  name: Wise Platform 3ds oauth-token API
  slug: open-wise-oauth-token-api
- collection_type: open
  name: Wise Platform 3ds payin-deposit-detail API
  slug: open-wise-payin-deposit-detail-api
- collection_type: open
  name: Wise Platform 3ds payins API
  slug: open-wise-payins-api
- collection_type: open
  name: Wise Platform API
  slug: open-wise-platform
- collection_type: open
  name: Wise Platform 3ds profile API
  slug: open-wise-profile-api
- collection_type: open
  name: Wise Platform 3ds quote API
  slug: open-wise-quote-api
- collection_type: open
  name: Wise Platform 3ds rate API
  slug: open-wise-rate-api
- collection_type: open
  name: Wise Platform 3ds recipient API
  slug: open-wise-recipient-api
- collection_type: open
  name: Wise Platform 3ds sca-device-fingerprints API
  slug: open-wise-sca-device-fingerprints-api
- collection_type: open
  name: Wise Platform 3ds sca-facemaps API
  slug: open-wise-sca-facemaps-api
- collection_type: open
  name: Wise Platform 3ds sca-otp API
  slug: open-wise-sca-otp-api
- collection_type: open
  name: Wise Platform 3ds sca-ott API
  slug: open-wise-sca-ott-api
- collection_type: open
  name: Wise Platform 3ds sca-pin API
  slug: open-wise-sca-pin-api
- collection_type: open
  name: Wise Platform 3ds sca-sessions API
  slug: open-wise-sca-sessions-api
- collection_type: open
  name: Wise Platform 3ds simulation API
  slug: open-wise-simulation-api
- collection_type: open
  name: Wise Platform 3ds spend-controls API
  slug: open-wise-spend-controls-api
- collection_type: open
  name: Wise Platform 3ds spend-limits API
  slug: open-wise-spend-limits-api
- collection_type: open
  name: Wise Platform 3ds transfer API
  slug: open-wise-transfer-api
- collection_type: open
  name: Wise Platform 3ds user API
  slug: open-wise-user-api
- collection_type: open
  name: Wise Platform 3ds user-security API
  slug: open-wise-user-security-api
- collection_type: open
  name: Wise Platform 3ds verification API
  slug: open-wise-verification-api
- collection_type: open
  name: Wise Platform 3ds webhook API
  slug: open-wise-webhook-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wise-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wise-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wise-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wise-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wise-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wise-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wise-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wise-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transferwise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wiseaccount
- group: company
  title: ''
  type: Website
  url: https://wise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wise.com/
- group: start
  title: ''
  type: Sandbox
  url: https://api.sandbox.transferwise.tech
- group: commercial
  title: ''
  type: Plans
  url: plans/wise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wise-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.wise.com/llms.txt
created: '2026-05-08'
description: Wise (formerly TransferWise) provides cross-border payments and multi-currency accounts for personal and business customers. The Wise Platform API exposes profiles, balances, transfers, recipients, quotes, multi-currency accounts, cards, statements, and webhooks.
finops:
- name: Wise Finops
  service_category: Payments
  slug: wise-finops
graphqls:
- description: This conceptual GraphQL schema models the Wise (formerly TransferWise) Platform API surface, covering cross-border money transfers, multi-currency accounts, balances, recipients, quotes, payments, and
  name: Wise GraphQL Schema
  slug: wise-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wise.png
layout: provider
modified: '2026-05-30'
name: Wise
nav: Providers
network: true
overview: 'Wise publishes 48 APIs on the [APIs.io](https://apis.io/) network, including 3ds API, activity API, address API, and 45 more. Tagged areas include Payments, FX, Cross-Border, Banking, and Multi-Currency.


  The Wise catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Wise''s developer surface includes authentication, sandbox, changelog, documentation, and 15 more developer resources.'
plans:
- name: Wise Plans Pricing
  plan_count: 3
  slug: wise-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Wise Rate Limits
  slug: wise-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Wise API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: wise-asyncapi-spectral-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 11.4
    contract_quality: 65.5
    developer_ergonomics: 21.4
    discoverability: 51.9
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wise/refs/heads/main/screenshots/wise-2026-06-20T201536.png
security:
- kind: authentication
  name: Wise Authentication
  slug: wise-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Wise Domain Security
  slug: wise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wise Vulnerability Disclosure
  slug: wise-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Wise Trust Center
  slug: wise-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, PCI DSS, ISO 27001, GDPR
slug: wise
tags:
- Payments
- FX
- Cross-Border
- Banking
- Multi-Currency
website: https://wise.com/
---
