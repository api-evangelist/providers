---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Bbandt Corp Agentic Access
  operation_count: 31
  slug: bbandt-corp-agentic-access
  summary_line: 31 operations · 12 acting · 1 human-in-the-loop
api_count: 15
apis:
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Search and view customer accounts
  name: BB&T Corp (Truist) Account Information API
  slug: bbandt-corp-account-information-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Search and view account transactions
  name: BB&T Corp (Truist) Account Transactions API
  slug: bbandt-corp-account-transactions-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Returns account balances for a specific account
  name: BB&T Corp (Truist) Commercial Account Balance API
  slug: bbandt-corp-commercial-account-balance-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Returns account transactions for a specific account
  name: BB&T Corp (Truist) Commercial Account Transactions API
  slug: bbandt-corp-commercial-account-transactions-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Retrieves the list of accounts
  name: BB&T Corp (Truist) Commercial Accounts API
  slug: bbandt-corp-commercial-accounts-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Eligible accounts for Real Time Payment Credit Transfer
  name: BB&T Corp (Truist) Credit Transfers Account List API
  slug: bbandt-corp-credit-transfers-account-list-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Credit Transfer Acknowledge for an inbound credit transfer
  name: BB&T Corp (Truist) Credit Transfers Acknowledge API
  slug: bbandt-corp-credit-transfers-acknowledge-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Credit Transfers for a Real Time Payment
  name: BB&T Corp (Truist) Credit Transfers API
  slug: bbandt-corp-credit-transfers-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Approvals for Real Time Payment Credit Transfer
  name: BB&T Corp (Truist) Credit Transfers Approval/Reject API
  slug: bbandt-corp-credit-transfers-approval-reject-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Manage Event Notification Subscriptions
  name: BB&T Corp (Truist) Event Notification Subscriptions API
  slug: bbandt-corp-event-notification-subscriptions-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Manage Event Notifications
  name: BB&T Corp (Truist) Event Notifications API
  slug: bbandt-corp-event-notifications-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Get ATM and branch location info - latitude, longitude, address, phone and fax
  name: BB&T Corp (Truist) Location Information API
  slug: bbandt-corp-location-information-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: View account money movement details
  name: BB&T Corp (Truist) Money Movement API
  slug: bbandt-corp-money-movement-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: OAuth 2.0 authorize and token services
  name: BB&T Corp (Truist) OAuth 2.0 API
  slug: bbandt-corp-oauth-2-0-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Search and view customer or customers
  name: BB&T Corp (Truist) Personal Information API
  slug: bbandt-corp-personal-information-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Manage recipients
  name: BB&T Corp (Truist) Recipients API
  slug: bbandt-corp-recipients-api
- baseURL: https://api.truist.com/commercial
  baseurl_source: declared
  description: Request a customer consent grant
  name: BB&T Corp (Truist) User Consent API
  slug: bbandt-corp-user-consent-api
artifact_total: 72
asyncapis:
- description: ''
  name: Bbandt Corp Event Notifications Webhooks
  slug: bbandt-corp-event-notifications-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/bbandt-corp/agentic-access/bbandt-corp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bbandt-corp-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/rules/bbandt-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/bbandt-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/rules/bbandt-corp-rules.yml
  title: ''
  type: Spectral
  url: rules/bbandt-corp-rules.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/json-ld/bbandt-corp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bbandt-corp-context.jsonld
- group: design
  href: https://artifacts.apis.io/bbandt-corp/vocabulary/bbandt-corp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bbandt-corp-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/hosts/bbandt-corp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bbandt-corp-hosts.yml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/vendors/bbandt-corp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bbandt-corp-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.truist.com/wealth/work-with-us/leadership
- group: commercial
  href: https://artifacts.apis.io/bbandt-corp/finops/bbandt-corp-finops.yml
  title: ''
  type: FinOps
  url: finops/bbandt-corp-finops.yml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-commercial-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-commercial-accounts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-commercial-account-balance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-commercial-account-balance-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-commercial-account-transactions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-commercial-account-transactions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-accounts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-locator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-locator-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-accounts-transaction-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-accounts-transaction-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-customers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-customers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-auth-oauth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-auth-oauth-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-consents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-consents-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-register-recipient-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-register-recipient-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-payment-networks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-payment-networks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-accounts-contact-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-accounts-contact-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-commercial-credit-transfers-oas-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-commercial-credit-transfers-oas-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-event-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-event-notifications-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bbandt-corp/overlays/bbandt-corp-retail-event-subscriptions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bbandt-corp-retail-event-subscriptions-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/bbandt-corp/scopes/bbandt-corp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bbandt-corp-scopes.yml
- group: auth
  href: https://artifacts.apis.io/bbandt-corp/authentication/bbandt-corp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bbandt-corp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bbandt-corp/security/bbandt-corp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bbandt-corp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truistfinancialcorporation
- group: start
  title: ''
  type: Portal
  url: https://developer.truist.com/
- group: company
  title: ''
  type: Website
  url: https://www.truist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.truist.com/api/view-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.truist.com/api/working-with-truist
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truist.com/terms-and-conditions
- group: design
  href: https://artifacts.apis.io/bbandt-corp/rules/bbandt-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/bbandt-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/vocabulary/bbandt-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/bbandt-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/json-ld/bbandt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bbandt-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://media.truist.com/news-releases?pagetemplate=rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truist.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://developer.truist.com/api/personal-and-small-business-accounts/documentation
- group: operate
  title: ''
  type: Support
  url: https://developer.truist.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.truist.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://developer.truist.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.truist.com/ui/login
- group: design
  href: https://artifacts.apis.io/bbandt-corp/errors/bbandt-corp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bbandt-corp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/conformance/bbandt-corp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bbandt-corp-conformance.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/lifecycle/bbandt-corp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bbandt-corp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/conventions/bbandt-corp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bbandt-corp-conventions.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/data-model/bbandt-corp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bbandt-corp-data-model.yml
- group: start
  href: https://artifacts.apis.io/bbandt-corp/sandbox/bbandt-corp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bbandt-corp-sandbox.yml
- group: design
  href: https://artifacts.apis.io/bbandt-corp/asyncapi/bbandt-corp-event-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bbandt-corp-event-notifications-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/bbandt-corp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bbandt-corp/mcp/bbandt-corp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bbandt-corp-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/bbandt-corp/plans/bbandt-corp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bbandt-corp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bbandt-corp/rate-limits/bbandt-corp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bbandt-corp-rate-limits.yml
created: '2026-03-23'
description: BB&T Corporation merged with SunTrust Banks in December 2019 to form Truist Financial Corporation, the sixth-largest US commercial bank. Truist runs an open-banking API program at developer.truist.com and publishes fifteen first-party OpenAPI contracts covering 31 operations — personal and small-business accounts, transactions, client contact, account address and payment networks; commercial accounts, balances and transactions; RTP real-time credit transfers; OAuth 2.0 authentication, customer consent, RFC 7591 dynamic client registration, event subscriptions and notifications, and a branch/ATM locator. The retail surface is built to the Financial Data Exchange (FDX) API (V5.4.1, V6.4.1 and v6.5) and every API carries the FAPI x-fapi-interaction-id correlation header. Access is OAuth 2.0 authorization_code with per-customer consent; sandbox is self-serve after registration, production requires manual approval by a Truist engagement team.
examples:
- key_count: 4
  name: Account List Example
  slug: account-list-example
features:
- description: REST APIs enabling fintech applications to access account and transaction data with customer consent.
  name: Open Banking APIs
- description: APIs for personal and small business banking account access including balances and transaction history.
  name: Personal Banking APIs
- description: APIs for commercial account management, treasury operations, and enterprise banking integrations.
  name: Commercial Banking APIs
- description: Specialized APIs for association management companies to handle dues, payments, and financial reporting.
  name: Association Services
- description: Secure OAuth 2.0 based authentication for customer data access with proper consent flows.
  name: OAuth 2.0 Authentication
finops:
- has_sources: true
  method: derived
  name: Bbandt Corp Finops
  primary_unit: ''
  service_category: ''
  slug: bbandt-corp-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bbandt-corp.png
integrations:
- description: Third-party data aggregator providing alternative connectivity to Truist account data.
  name: Plaid
- description: Open banking platform providing access to Truist banking data via aggregation.
  name: Tink
- description: Accounting software integration for Truist commercial banking customers.
  name: QuickBooks
json_schemas:
- name: Commercial account eligible account list
  property_count: 4
  slug: bbandt-corp-account-detail
- name: Commercial Account List
  property_count: 1
  slug: bbandt-corp-account-list
- name: Account With Details entity
  property_count: 0
  slug: bbandt-corp-account-with-details
- name: Accounts entity
  property_count: 1
  slug: bbandt-corp-accounts
- name: Payment acknowledgement request
  property_count: 1
  slug: bbandt-corp-acknowledge-payment-request
- name: Payment acknowledgement response
  property_count: 1
  slug: bbandt-corp-acknowledge-payment-response
- name: ATMs Entity
  property_count: 1
  slug: bbandt-corp-atms
- name: Branches Entity
  property_count: 1
  slug: bbandt-corp-branches
- name: Request definition for status update
  property_count: 2
  slug: bbandt-corp-cancel-payment-request
- name: Consent Grant entity
  property_count: 11
  slug: bbandt-corp-consent-grant
- name: Consent revocation request entity
  property_count: 2
  slug: bbandt-corp-consent-revocation-request
- name: Customer entity
  property_count: 5
  slug: bbandt-corp-customer
- name: All reported transactions
  property_count: 1
  slug: bbandt-corp-get-approvals-payment-response
- name: All or ATM Locations
  property_count: 1
  slug: bbandt-corp-locations
- name: MultipleRtpPaymentRequest.
  property_count: 1
  slug: bbandt-corp-multiple-rtp-payment-request
- name: Notification entity
  property_count: 8
  slug: bbandt-corp-notification
- name: Notification Subscription entity
  property_count: 6
  slug: bbandt-corp-notification-subscription
- name: PostedOrPending
  property_count: 1
  slug: bbandt-corp-posted-or-pending
- name: Recipient Request
  property_count: 12
  slug: bbandt-corp-recipient-request
- name: Response definition for the RTP Transfer
  property_count: 1
  slug: bbandt-corp-rtp-response
- name: TokenRequest
  property_count: 6
  slug: bbandt-corp-token-request
- name: TokenResponse
  property_count: 8
  slug: bbandt-corp-token-response
- name: Transactions entity
  property_count: 2
  slug: bbandt-corp-transactions
- name: Request definition for status update
  property_count: 2
  slug: bbandt-corp-update-payment-request
- name: Succcessful response for payment update
  property_count: 2
  slug: bbandt-corp-update-payment-response
jsonld:
- class_count: 0
  name: Bbandt Context
  property_count: 11
  slug: bbandt-context
- class_count: 113
  name: Bbandt Corp Context
  property_count: 180
  slug: bbandt-corp-context
layout: provider
modified: '2026-09-04'
name: BB&T Corp (Truist)
nav: Providers
network: true
overview: 'BB&T Corp (Truist) publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Information API, Account Transactions API, Commercial Account Balance API, and 14 more. Tagged areas include Banking, Financial Services, Open Banking, Truist, and BB&T.


  The BB&T Corp (Truist) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  BB&T Corp (Truist)''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, API reference, support, and 47 more developer resources.'
plans:
- name: Bbandt Corp Plans Pricing
  plan_count: 0
  slug: bbandt-corp-plans-pricing
press:
- date: ''
  title: BB&T and SunTrust receive final approvals for merger to ...
  url: https://www.delcotimes.com/2019/11/22/bbt-and-suntrust-receive-final-approvals-for-merger-to-form-truist/
- date: ''
  title: BB&T-SunTrust merger spurs deal talk
  url: https://www.taipeitimes.com/News/biz/archives/2019/02/09/2003709442
- date: ''
  title: BB&T, SunTrust to combine in $28B merger
  url: https://www.americanbanker.com/news/bb-t-suntrust-to-combine-in-28b-merger
- date: ''
  title: BB&T to buy SunTrust in biggest U.S. bank deal in a decade
  url: https://www.reuters.com/article/business/bbt-to-buy-suntrust-in-biggest-us-bank-deal-in-a-decade-idUSKCN1PW17G/
- date: ''
  title: Truist CIO Focuses on Positioning Bank for Digital Innovation
  url: https://www.wsj.com/articles/truist-cio-focuses-on-positioning-bank-for-digital-innovation-11625563800?eafs_enabled=false
random_paper: 20
rate_limits:
- limit_count: 0
  name: Bbandt Corp Rate Limits
  slug: bbandt-corp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: BB&T Corp (Truist) API Rules
  rule_count: 20
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 5
  slug: bbandt-corp-rules
- authorship: unmarked
  effective_rule_count: 5
  extends: []
  name: BB&T Corp (Truist) — bbandt rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 1
  slug: bbandt-spectral-rules
scopes:
- name: Bbandt Corp Scopes
  scope_count: 12
  slug: bbandt-corp-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 35
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 78.3
    developer_ergonomics: 42.3
    discoverability: 72.3
    operational_transparency: 7.9
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 94.1
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fdx
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 50.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/bbandt-corp/bbandt-corp-2026-06-20T173059.png
security:
- kind: authentication
  name: Bbandt Corp Authentication
  slug: bbandt-corp-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bbandt Corp Domain Security
  slug: bbandt-corp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: truist-find-branches-and-atms
  slug: bbandt-corp-find-branches-and-atms
- name: truist-manage-consent-and-events
  slug: bbandt-corp-manage-consent-and-events
- name: truist-register-data-recipient
  slug: bbandt-corp-register-data-recipient
- name: truist-retrieve-accounts-and-transactions
  slug: bbandt-corp-retrieve-accounts-and-transactions
- name: truist-send-rtp-credit-transfer
  slug: bbandt-corp-send-rtp-credit-transfer
slug: bbandt-corp
tags:
- Banking
- Financial Services
- Open Banking
- Truist
- BB&T
- Fortune 500
use_cases:
- description: Build personal finance management apps that aggregate account and transaction data for Truist customers.
  name: Personal Finance Apps
- description: Integrate Truist commercial accounts with accounting software like QuickBooks or Xero.
  name: Accounting Software Integration
- description: Enable enterprise treasury teams to access real-time commercial account balances and transaction data.
  name: Treasury Management
- description: Automate dues collection and financial reporting for homeowners associations and membership organizations.
  name: Association Management
website: https://www.truist.com/
---
