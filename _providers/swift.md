---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Swift Agentic Access
  operation_count: 22
  slug: swift-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: The SWIFT GPI (Global Payments Innovation) API enables financial institutions to track cross-border payment transactions in real time, update payment statuses, and manage stop-and-recall requests. Use
  name: SWIFT GPI API
  slug: swift-gpi-api
- description: The SWIFT Payment Pre-validation API allows financial institutions and PSPs to verify payment instruction data against reference data and counterparty information before executing a payment. Checks ac
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
  description: IBAN (International Bank Account Number) lookup and validation
  name: SWIFT IBANs API
  slug: swift-ibans-api
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
artifact_total: 44
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
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/swift-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/swift/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swift-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swift-authentication.yml
- group: auth
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
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.swift.com
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
- name: Swift Finops
  service_category: Financial Messaging & Cross-Border Payments
  slug: swift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swift.png
json_schemas:
- name: SWIFT BIC
  property_count: 7
  slug: swift-bic
- name: SWIFT IBAN
  property_count: 6
  slug: swift-iban
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
modified: '2026-05-19'
name: SWIFT
nav: Providers
network: true
overview: 'SWIFT publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account Numbers API, BBANs API, BICs API, and 5 more. Tagged areas include Banking, Cross-Border Payments, Financial Messaging, Financial-Services, and GPI.


  The SWIFT catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SWIFT''s developer surface includes authentication, API reference, sandbox, support, and 17 more developer resources.'
plans:
- name: Swift Plans Pricing
  plan_count: 1
  slug: swift-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Swift Rate Limits
  slug: swift-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SWIFT API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swift-jsonschema-spectral-rules
- effective_rule_count: 49
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
  summary_line: 2 scopes · password
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 13.6
    contract_quality: 59.2
    developer_ergonomics: 32.1
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swift/refs/heads/main/screenshots/swift-2026-06-20T194804.png
security:
- kind: authentication
  name: Swift Authentication
  slug: swift-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Swift Domain Security
  slug: swift-domain-security
  summary_line: TLSv1.3 · DMARC
slug: swift
tags:
- Banking
- Cross-Border Payments
- Financial Messaging
- Financial-Services
- GPI
- ISO 20022
- Payments
website: https://www.swift.com
---
