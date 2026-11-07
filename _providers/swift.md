---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Swift Agentic Access
  operation_count: 22
  slug: swift-agentic-access
  summary_line: 22 operations
api_count: 7
apis:
- baseURL: https://api.swift.com/swift-preval/v2
  baseurl_source: declared
  description: The SWIFT Payment Pre-validation API allows financial institutions and PSPs to verify payment instruction data against reference data and counterparty information before executing a payment. Checks ac
  name: Payment Pre-validation API
  slug: payment-pre-validation-api
- description: The SWIFT Transaction Screening API enables financial institutions to submit transactions to the SWIFT Transaction Screening Service (TSS) for sanctions and compliance screening before processing. Ret
  name: Transaction Screening API
  slug: transaction-screening-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: Account number format validation
  name: SWIFT Account Numbers API
  slug: swift-account-numbers-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: BBAN to IBAN conversion
  name: SWIFT BBANs API
  slug: swift-bbans-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: BIC (Bank Identifier Code) lookup and validation
  name: SWIFT BICs API
  slug: swift-bics-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: Country code lookup and validation
  name: SWIFT Country Codes API
  slug: swift-country-codes-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: Currency code lookup and validation
  name: SWIFT Currency Codes API
  slug: swift-currency-codes-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: LEI (Legal Entity Identifier) lookup and validation
  name: SWIFT LEIs API
  slug: swift-leis-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: National ID lookup and BIC resolution
  name: SWIFT National IDs API
  slug: swift-national-ids-api
- baseURL: https://api.swift.com/swiftrefdata
  baseurl_source: declared
  description: IBAN (International Bank Account Number) lookup and validation
  name: SWIFT IBANs API
  slug: swift-ibans-api
- baseURL: https://virtserver.swaggerhub.com/SWIFT-API/corporate-to_bank_account_balance_information/1.0.9
  baseurl_source: declared
  description: The Account Information API from SWIFT — 3 operation(s) for account information.
  name: SWIFT Account Information API
  slug: swift-account-information-api
- baseURL: https://virtserver.swaggerhub.com/SWIFT-API/Swift-Messaging/2.0.0
  baseurl_source: declared
  description: The distributions API from SWIFT — 4 operation(s) for distributions.
  name: SWIFT Distributions API
  slug: swift-distributions-api
- baseURL: https://virtserver.swaggerhub.com/SWIFT-API/Swift-Messaging/2.0.0
  baseurl_source: declared
  description: The fileact API from SWIFT — 10 operation(s) for fileact.
  name: SWIFT Fileact API
  slug: swift-fileact-api
- baseURL: https://virtserver.swaggerhub.com/SWIFT-API/Swift-Messaging/2.0.0
  baseurl_source: declared
  description: The fin API from SWIFT — 13 operation(s) for fin.
  name: SWIFT Fin API
  slug: swift-fin-api
- baseURL: https://api-test.swiftnet.sipn.swift.com/swift-apitracker-pilot/v6
  baseurl_source: declared
  description: 'Payment Transactions - Getting the Last Changed Payment Transactions Purpose of the API * This API is a delta query to get all payment update information starting from a given date and time. This API '
  name: SWIFT Get Changed Payment Transactions API
  slug: swift-get-changed-payment-transactions-api
- baseURL: https://api-test.swiftnet.sipn.swift.com/swift-apitracker-pilot/v6
  baseurl_source: declared
  description: 'Payment Transactions - Getting a Payment Transaction Purpose of the API * This API is a payment query to get detailed information regarding a given payment. It requires the UETR to be known. Examples '
  name: SWIFT Get Payment Transaction Details API
  slug: swift-get-payment-transaction-details-api
- baseURL: https://api.swift.com/swiftrefdata/v4
  baseurl_source: declared
  description: The iban_national_ids API from SWIFT — 1 operation(s) for iban_national_ids.
  name: SWIFT Iban National IDs API
  slug: swift-iban-national-ids-api
- baseURL: https://virtserver.swaggerhub.com/SWIFT-API/Swift-Messaging/2.0.0
  baseurl_source: declared
  description: The interact API from SWIFT — 13 operation(s) for interact.
  name: SWIFT Interact API
  slug: swift-interact-api
- baseURL: https://api.swift.com/swiftrefdata/v4
  baseurl_source: declared
  description: The pmis API from SWIFT — 5 operation(s) for pmis.
  name: SWIFT Pmis API
  slug: swift-pmis-api
- baseURL: https://virtserver.swaggerhub.com/SWIFT-API/corporate-to_bank_account_balance_information/1.0.9
  baseurl_source: declared
  description: The Reporting API from SWIFT — 2 operation(s) for reporting.
  name: SWIFT Reporting API
  slug: swift-reporting-api
- baseURL: https://api-test.swiftnet.sipn.swift.com/swift-apitracker-gcct-pilot/v6
  baseurl_source: declared
  description: Payment Transactions - Updating the Status of a gCCT Payment Transaction
  name: SWIFT Status Confirmations API
  slug: swift-status-confirmations-api
artifact_total: 93
collections:
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers API
  slug: postman-swift-account-numbers-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers BBANs API
  slug: postman-swift-bbans-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers BICs API
  slug: postman-swift-bics-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers Country Codes API
  slug: postman-swift-country-codes-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers Currency Codes API
  slug: postman-swift-currency-codes-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers IBANs API
  slug: postman-swift-ibans-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers LEIs API
  slug: postman-swift-leis-api
- collection_type: postman
  name: SWIFT SwiftRef Account Numbers National IDs API
  slug: postman-swift-national-ids-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers API
  slug: open-swift-account-numbers-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers BBANs API
  slug: open-swift-bbans-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers BICs API
  slug: open-swift-bics-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers Country Codes API
  slug: open-swift-country-codes-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers Currency Codes API
  slug: open-swift-currency-codes-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers IBANs API
  slug: open-swift-ibans-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers LEIs API
  slug: open-swift-leis-api
- collection_type: open
  name: SWIFT SwiftRef Account Numbers National IDs API
  slug: open-swift-national-ids-api
- collection_type: open
  name: SWIFT SwiftRef API
  slug: open-swift-swiftref-api
common:
- group: design
  href: https://artifacts.apis.io/swift/rules/swift-rules.yml
  title: ''
  type: Spectral
  url: rules/swift-rules.yml
- group: design
  href: https://artifacts.apis.io/swift/rules/swift-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/swift-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/swift/json-ld/swift-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/swift-context.jsonld
- group: design
  href: https://artifacts.apis.io/swift/vocabulary/swift-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swift-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/swift/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/swift/data-model/swift-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swift-data-model.yml
- group: operate
  href: https://artifacts.apis.io/swift/changelog/swift-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/swift-changelog.yml
- group: design
  href: https://artifacts.apis.io/swift/conventions/swift-conventions.yml
  title: ''
  type: Conventions
  url: conventions/swift-conventions.yml
- group: start
  href: https://artifacts.apis.io/swift/sandbox/swift-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/swift-sandbox.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/swiftinc/SWIFT-API-Guide/blob/master/docs/versions.md
- group: operate
  title: ''
  type: StatusPage
  url: https://www.swift.com/myswift#status
- group: design
  href: https://artifacts.apis.io/swift/lifecycle/swift-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/swift-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/swift/errors/swift-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/swift-error-codes.yml
- group: design
  href: https://artifacts.apis.io/swift/errors/swift-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/swift-problem-types.yml
- group: design
  href: https://artifacts.apis.io/swift/conformance/swift-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swift-conformance.yml
- group: agent
  href: https://artifacts.apis.io/swift/llms/swift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swift-llms.txt
- group: other
  href: https://artifacts.apis.io/swift/hosts/swift-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swift-hosts.yml
- group: build
  href: https://artifacts.apis.io/swift/integrations/swift-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/swift-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/swift/vendors/swift-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swift-vendors.yml
- group: build
  href: https://artifacts.apis.io/swift/packages/swift-packages.yml
  title: ''
  type: SDKs
  url: packages/swift-packages.yml
- group: build
  href: https://artifacts.apis.io/swift/packages/swift-packages.yml
  title: ''
  type: Packages
  url: packages/swift-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.swift.com/
- group: commercial
  href: https://artifacts.apis.io/swift/finops/swift-finops.yml
  title: ''
  type: FinOps
  url: finops/swift-finops.yml
- group: other
  href: https://artifacts.apis.io/swift/capabilities/swift-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/swift-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/swift/agentic-access/swift-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/swift-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/swift/security/swift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swift-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/swift/authentication/swift-authentication.yml
  title: ''
  type: Authentication
  url: authentication/swift-authentication.yml
- group: auth
  href: https://artifacts.apis.io/swift/scopes/swift-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/swift-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.swift.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.swift.com
- group: docs
  title: ''
  type: APIDocumentation
  url: https://developer.swift.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.swift.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swiftinc
- group: other
  title: ''
  type: ProductPage
  url: https://www.swift.com/products/swift-apis
- group: operate
  title: ''
  type: Support
  url: https://www.swift.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.swift.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swift.com/privacy-legal
- group: other
  title: ''
  type: ISO20022
  url: https://www.swift.com/standards/iso-20022
- group: other
  title: ''
  type: SwiftRef
  url: https://www.swift.com/products/swiftref
- group: other
  title: ''
  type: GPI
  url: https://www.swift.com/products/swift-gpi
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/swift-developer-support/swift-api-sandbox-collections
- group: start
  title: ''
  type: Login
  url: https://developer.swift.com/login
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/swiftinc/api-sample-code
created: '2025-02-06'
description: SWIFT (Society for Worldwide Interbank Financial Telecommunication) is a global member-owned cooperative providing secure financial messaging services and reference data to financial institutions worldwide. SWIFT offers REST APIs for cross-border payment tracking (GPI), payment pre-validation, reference data lookup (SwiftRef), transaction screening, instant payments, and more. APIs use OAuth 2.0 authentication and are documented using OpenAPI 3.0.
examples:
- key_count: 4
  name: Swift Get Bic Details Example
  slug: swift-get-bic-details-example
- key_count: 4
  name: Swift Validate Iban Example
  slug: swift-validate-iban-example
finops:
- has_sources: true
  method: generated
  name: Swift Finops
  primary_unit: ''
  service_category: Financial Messaging & Cross-Border Payments
  slug: swift-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swift.png
json_schemas:
- name: AccountFormatValidationStatus1
  property_count: 6
  slug: swift-account-format-validation-status1
- name: AccountVerificationRequest
  property_count: 9
  slug: swift-account-verification-request
- name: BicDetails
  property_count: 7
  slug: swift-bic-details
- name: BicIsoDetails
  property_count: 11
  slug: swift-bic-iso-details
- name: SWIFT BIC
  property_count: 7
  slug: swift-bic
- name: CashAccount41
  property_count: 11
  slug: swift-cash-account41
- name: CountryCodeDetails
  property_count: 4
  slug: swift-country-code-details
- name: CurrencyCodeDetails
  property_count: 3
  slug: swift-currency-code-details
- name: Currency
  property_count: 5
  slug: swift-currency
- name: Distribution
  property_count: 10
  slug: swift-distribution
- name: EligibilityCheckStatus1
  property_count: 3
  slug: swift-eligibility-check-status1
- name: FileActArchiveDownloadResponse
  property_count: 3
  slug: swift-file-act-archive-download-response
- name: FileActMessageDownloadResponse
  property_count: 3
  slug: swift-file-act-message-download-response
- name: FinEmission
  property_count: 7
  slug: swift-fin-message-emission
- name: IbanDetails
  property_count: 5
  slug: swift-iban-details
- name: SWIFT IBAN
  property_count: 6
  slug: swift-iban
- name: InterActMessageEmission
  property_count: 10
  slug: swift-inter-act-message-emission
- name: LeiDetails
  property_count: 4
  slug: swift-lei-details
- name: Links
  property_count: 0
  slug: swift-links
- name: NationalIdDetails
  property_count: 5
  slug: swift-national-id-details
- name: NationalId
  property_count: 3
  slug: swift-national-id
- name: PaymentInstruction
  property_count: 12
  slug: swift-payment-instruction
- name: PaymentInstructionValidation
  property_count: 4
  slug: swift-payment-instruction-validation
- name: PaymentPurposeValidationStatus1
  property_count: 9
  slug: swift-payment-purpose-validation-status1
- name: PaymentStatusRequest9
  property_count: 22
  slug: swift-payment-status-request9
- name: PaymentTransaction149
  property_count: 13
  slug: swift-payment-transaction149
- name: PmiDetails
  property_count: 17
  slug: swift-pmi-details
- name: PmiParticipantDetails
  property_count: 25
  slug: swift-pmi-participant-details
- name: PmiParticipants
  property_count: 2
  slug: swift-pmi-participants
- name: ReachabilityResult
  property_count: 3
  slug: swift-reachability-result
- name: ReadChangedPaymentTransactionsResponse2
  property_count: 2
  slug: swift-read-changed-payment-transactions-response2
- name: SendBatchMessagesResponse
  property_count: 0
  slug: swift-send-batch-messages-response
- name: StatementLineSummary
  property_count: 7
  slug: swift-statement-line-summary
- name: Statement
  property_count: 11
  slug: swift-statement
- name: TransactionSummary1
  property_count: 6
  slug: swift-transaction-summary1
- name: ValidityResult
  property_count: 3
  slug: swift-validity-result
json_structures:
- name: Swift Bic Structure
  property_count: 0
  slug: swift-bic-structure
jsonld:
- class_count: 19
  name: Swift Context
  property_count: 1
  slug: swift-context
layout: provider
modified: '2026-11-05'
name: SWIFT
nav: Providers
network: true
overview: 'SWIFT publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Payment Pre-validation API, Account Numbers API, BBANs API, and 18 more. Tagged areas include Banking, Cross-Border Payments, Financial Messaging, Financial Services, and GPI.


  The SWIFT catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SWIFT''s developer surface includes changelog, sandbox, documentation, authentication, API reference, support, and 37 more developer resources.'
plans:
- name: Swift Plans Pricing
  plan_count: 0
  slug: swift-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Swift Rate Limits
  slug: swift-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SWIFT — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swift-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: SWIFT API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 1
    info: 0
    warn: 7
  slug: swift-rules
scopes:
- name: Swift Scopes
  scope_count: 2
  slug: swift-scopes
  summary_line: 2 scopes · password/clientCredentials
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 38
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.9
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 66.3
    developer_ergonomics: 41.1
    discoverability: 62.5
    operational_transparency: 42.1
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/swift/swift-2026-06-20T194804.png
security:
- kind: authentication
  name: Swift Authentication
  slug: swift-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Swift Domain Security
  slug: swift-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 6
skills:
- name: swift-confirm-gpi-payment-status
  slug: swift-confirm-gpi-payment-status
- name: swift-fetch-account-balances-and-statements
  slug: swift-fetch-account-balances-and-statements
- name: swift-resolve-bic-and-iban
  slug: swift-resolve-bic-and-iban
- name: swift-send-fin-message
  slug: swift-send-fin-message
- name: swift-track-gpi-payment
  slug: swift-track-gpi-payment
- name: swift-verify-beneficiary-account
  slug: swift-verify-beneficiary-account
slug: swift
tags:
- Banking
- Cross-Border Payments
- Financial Messaging
- Financial Services
- GPI
- ISO 20022
- Payments
- SWIFT
website: https://www.swift.com
---
