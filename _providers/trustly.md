---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trustly Agentic Access
  operation_count: 31
  slug: trustly-agentic-access
  summary_line: 31 operations · 15 acting
api_count: 2
apis:
- description: JSON-RPC 1.1 API for Trustly Pay by Bank in Europe and the UK. Methods cover Deposit, Withdraw/AccountPayout, Refund, SelectAccount, RegisterAccount, VerifyAccount, Charge and recurring direct debit (
  name: Trustly Europe API
  slug: trustly-europe-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The accounts API from Trustly Group — 3 operation(s) for accounts.
  name: Trustly Group Accounts API
  slug: trustly-accounts-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The API API from Trustly Group — 0 operation(s) for api.
  name: Trustly Group API
  slug: trustly-api-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The countries API from Trustly Group — 1 operation(s) for countries.
  name: Trustly Group Countries API
  slug: trustly-countries-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The customers API from Trustly Group — 2 operation(s) for customers.
  name: Trustly Group Customers API
  slug: trustly-customers-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The identity API from Trustly Group — 3 operation(s) for identity.
  name: Trustly Group Identity API
  slug: trustly-identity-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The networkCheckApi API from Trustly Group — 1 operation(s) for networkcheckapi.
  name: Trustly Group Network Check API
  slug: trustly-networkcheckapi-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The payments API from Trustly Group — 2 operation(s) for payments.
  name: Trustly Group Payments API
  slug: trustly-payments-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The transactions API from Trustly Group — 10 operation(s) for transactions.
  name: Trustly Group Transactions API
  slug: trustly-transactions-api
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: The verifyCustomer API from Trustly Group — 1 operation(s) for verifycustomer.
  name: Trustly Group Verify Customer API
  slug: trustly-verifycustomer-api
- baseURL: https://api.trustly.com/1
  baseurl_source: declared
  description: The Account Data API from Trustly Group — 4 operation(s) for account data.
  name: Trustly Group Account Data API
  slug: trustly-account-data-api
- baseURL: https://api.trustly.com/1
  baseurl_source: declared
  description: The Dispute Management API from Trustly Group — 1 operation(s) for dispute management.
  name: Trustly Group Dispute Management API
  slug: trustly-dispute-management-api
- baseURL: https://api.trustly.com/1
  baseurl_source: declared
  description: The Payment Providers API from Trustly Group — 1 operation(s) for payment providers.
  name: Trustly Group Payment Providers API
  slug: trustly-payment-providers-api
artifact_total: 56
asyncapis:
- description: ''
  name: Trustly North America Webhooks
  slug: trustly-north-america-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/trustly/agentic-access/trustly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trustly-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/trustly/rules/trustly-rules.yml
  title: ''
  type: Spectral
  url: rules/trustly-rules.yml
- group: design
  href: https://artifacts.apis.io/trustly/json-ld/trustly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trustly-context.jsonld
- group: design
  href: https://artifacts.apis.io/trustly/vocabulary/trustly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trustly-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/trustly/hosts/trustly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trustly-hosts.yml
- group: other
  href: https://artifacts.apis.io/trustly/vendors/trustly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trustly-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.trustly.com/br/press
- group: other
  href: https://artifacts.apis.io/trustly/capabilities/trustly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trustly-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://amer.developers.trustly.com/_mcp/server
- group: auth
  href: https://artifacts.apis.io/trustly/security/trustly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/trustly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/trustly/security/trustly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trustly-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trustly/security/trustly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trustly-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/trustly/authentication/trustly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trustly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://amer.developers.trustly.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trustly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://amer.developers.trustly.com/api-reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://amer.developers.trustly.com/integrate/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.trustly.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://amer.developers.trustly.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.trustly.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trustly
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrustlyInc
- group: start
  title: ''
  type: Login
  url: https://backoffice.trustly.com/
- group: start
  title: ''
  type: Login
  url: https://paywithmybank.com/merchant-portal/
- group: start
  title: ''
  type: SignUp
  url: https://www.trustly.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustly.com/about-us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustly.com/about-us/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trustly.net/
- group: auth
  title: ''
  type: Security
  url: https://www.trustly.com/security/disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://www.trustly.com/security
- group: company
  title: ''
  type: Careers
  url: https://www.trustly.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustly/
- group: other
  title: ''
  type: X
  url: https://x.com/Trustly
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/TrustlySE
- group: build
  href: https://artifacts.apis.io/trustly/packages/trustly-packages.yml
  title: ''
  type: Packages
  url: packages/trustly-packages.yml
- group: build
  href: https://artifacts.apis.io/trustly/packages/trustly-packages.yml
  title: ''
  type: SDKs
  url: packages/trustly-packages.yml
- group: agent
  href: https://artifacts.apis.io/trustly/well-known/trustly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trustly-well-known.yml
- group: other
  href: https://artifacts.apis.io/trustly/well-known/trustly-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/trustly-api-catalog.json
- group: design
  href: https://artifacts.apis.io/trustly/conformance/trustly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trustly-conformance.yml
- group: auth
  href: https://artifacts.apis.io/trustly/conformance/trustly-conformance.yml
  title: ''
  type: Compliance
  url: conformance/trustly-conformance.yml
- group: design
  href: https://artifacts.apis.io/trustly/lifecycle/trustly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trustly-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/trustly/lifecycle/trustly-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/trustly-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/trustly/rate-limits/trustly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trustly-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trustly/plans/trustly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trustly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trustly/components/trustly-components.yml
  title: ''
  type: Components
  url: components/trustly-components.yml
- group: design
  href: https://artifacts.apis.io/trustly/conventions/trustly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trustly-conventions.yml
- group: design
  href: https://artifacts.apis.io/trustly/conventions/trustly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trustly-conventions.yml
- group: design
  href: https://artifacts.apis.io/trustly/errors/trustly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trustly-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/trustly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/trustly/llms/trustly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trustly-llms.txt
- group: agent
  href: https://artifacts.apis.io/trustly/mcp/trustly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trustly-mcp.yml
- group: design
  href: https://artifacts.apis.io/trustly/asyncapi/trustly-north-america-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trustly-north-america-webhooks.yml
- group: start
  href: https://artifacts.apis.io/trustly/sandbox/trustly-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/trustly-sandbox.yml
- group: design
  href: https://artifacts.apis.io/trustly/data-model/trustly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trustly-data-model.yml
- group: auth
  href: https://artifacts.apis.io/trustly/security/trustly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/trustly-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/trustly/overlays/trustly-north-america-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trustly-north-america-overlay.yaml
created: '2026-09-18'
description: Trustly is a Pay by Bank payments company operating two developer surfaces. Trustly Europe (Trustly Group AB, Stockholm, a licensed Swedish payment institution) exposes a JSON-RPC 1.1 API at api.trustly.com for deposits, withdrawals/payouts, refunds, account tokenisation (SelectAccount/RegisterAccount), recurring direct debit (Autogiro, BACS, SEPA), local methods (Swish, iDEAL, MB Way, Bancontact) and settlement/ledger reporting, with RSA-signed requests and notifications. Trustly North America (Trustly Inc., formerly PayWithMyBank) exposes a REST API at trustly.one/api/v1 for establishing and authorizing bank transactions, capture, deposit, payout, refund, account verification and tokenization, Trustly ID identity data and event-notification webhooks, documented with a public OpenAPI 3.1, an llms.txt and a hosted MCP docs server.
finops:
- has_sources: true
  method: derived
  name: Trustly Finops
  primary_unit: ''
  service_category: ''
  slug: trustly-finops
  template: true
image: https://cdn.prod.website-files.com/6798a4db9ed2b5ffc8c81f32/67efd2d42cacfccbc8be80ed_OG%20Image.jpg
json_schemas:
- name: Account Data_get-transaction-account-summary_Response_200
  property_count: 3
  slug: trustly-account-data-get-transaction-account-summary-response-200
- name: Account Data_get-transactions-account-balance_Response_200
  property_count: 1
  slug: trustly-account-data-get-transactions-account-balance-response-200
- name: Account Data_list-selected-accounts_Response_200
  property_count: 1
  slug: trustly-account-data-list-selected-accounts-response-200
- name: Accounts_post-accounts-tokenize?-verifyAccount_Response_200
  property_count: 14
  slug: trustly-accounts-post-accounts-tokenize-verify-account-response-200
- name: AccountsTokenizePostRequestBodyContentApplicationJsonSchemaAccount
  property_count: 4
  slug: trustly-accounts-tokenize-post-request-body-content-application-json-schema-account
- name: AccountsVerifyPostRequestBodyContentApplicationJsonSchemaAccount
  property_count: 4
  slug: trustly-accounts-verify-post-request-body-content-application-json-schema-account
- name: Countries_get-countries_Response_200
  property_count: 1
  slug: trustly-countries-get-countries-response-200
- name: CustomerLookupResponse
  property_count: 2
  slug: trustly-customer-lookup-response
- name: Customer
  property_count: 21
  slug: trustly-customer
- name: Customers_get-customers-customerId_Response_200
  property_count: 1
  slug: trustly-customers-get-customers-customer-id-response-200
- name: Customers_get-customers_Response_200
  property_count: 1
  slug: trustly-customers-get-customers-response-200
- name: Customers_post-customers-customerId_Response_200
  property_count: 1
  slug: trustly-customers-post-customers-customer-id-response-200
- name: Customers_post-customers_Response_200
  property_count: 1
  slug: trustly-customers-post-customers-response-200
- name: EstablishData
  property_count: 20
  slug: trustly-establish-data
- name: EstablishPostRequestBodyContentApplicationJsonSchemaBeneficiary
  property_count: 8
  slug: trustly-establish-post-request-body-content-application-json-schema-beneficiary
- name: EstablishPostRequestBodyContentApplicationJsonSchemaMetadata
  property_count: 5
  slug: trustly-establish-post-request-body-content-application-json-schema-metadata
- name: EstablishPostRequestBodyContentApplicationJsonSchemaPaymentType
  property_count: 0
  slug: trustly-establish-post-request-body-content-application-json-schema-payment-type
- name: FeedbackPostRequestBodyContentApplicationJsonSchemaAccount
  property_count: 3
  slug: trustly-feedback-post-request-body-content-application-json-schema-account
- name: Feedback
  property_count: 8
  slug: trustly-feedback
- name: FinancialInstitutionAccount
  property_count: 14
  slug: trustly-financial-institution-account
- name: FIUser
  property_count: 9
  slug: trustly-fiuser
- name: Payment Providers_get-paymentProviders_Response_200
  property_count: 3
  slug: trustly-payment-providers-get-payment-providers-response-200
- name: Payment
  property_count: 34
  slug: trustly-payment
- name: Payments_list-payments_Response_200
  property_count: 3
  slug: trustly-payments-list-payments-response-200
- name: Transaction
  property_count: 29
  slug: trustly-transaction
- name: User
  property_count: 12
  slug: trustly-user
- name: UserVerificationDetail
  property_count: 1
  slug: trustly-user-verification-detail
- name: Verify Customer_get-verify-customer_Response_200
  property_count: 1
  slug: trustly-verify-customer-get-verify-customer-response-200
jsonld:
- class_count: 120
  name: Trustly Context
  property_count: 195
  slug: trustly-context
layout: provider
mcp_servers:
- description: ''
  name: Trustly Group MCP Server
  slug: server
modified: '2026-10-12'
name: Trustly Group
nav: Providers
network: true
overview: 'Trustly Group publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Countries API, and 11 more. Tagged areas include Company, Payments, Pay by Bank, Open Banking, and Account-to-Account.


  The Trustly Group catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Trustly Group''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 50 more developer resources.'
plans:
- name: Trustly Plans Pricing
  plan_count: 0
  slug: trustly-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Trustly Rate Limits
  slug: trustly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Trustly Group API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: trustly-rules
score:
  band: exemplar
  composite: 72.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 76.2
    developer_ergonomics: 82.7
    discoverability: 85.8
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 71.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 91.7
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/trustly/trustly-2026-10-11T131230.png
security:
- kind: authentication
  name: Trustly Authentication
  slug: trustly-authentication
  summary_line: http/signature · 5 schemes
- kind: domain-security
  name: Trustly Domain Security
  slug: trustly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trustly Vulnerability Disclosure
  slug: trustly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Trustly Trust Center
  slug: trustly-trust-center
  summary_line: ISO 27001, GDPR
skill_count: 3
skills:
- name: trustly-pay-authorize-and-capture
  slug: trustly-pay-authorize-and-capture
- name: trustly-payout
  slug: trustly-payout
- name: trustly-verify-account-and-identity
  slug: trustly-verify-account-and-identity
slug: trustly
tags:
- Company
- Payments
- Pay by Bank
- Open Banking
- Account-to-Account
- Payouts
- Direct Debit
- Bank Account Verification
- Identity Verification
- Fintech
- Webhook
- MCP
website: https://www.trustly.com/
---
