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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Swift Agentic Access
  operation_count: 22
  slug: swift-agentic-access
  summary_line: 22 operations
api_count: 11
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
- description: Account number format validation
  name: SWIFT Account Numbers API
  slug: swift-account-numbers-api
- description: BBAN to IBAN conversion
  name: SWIFT BBANs API
  slug: swift-bbans-api
- description: BIC (Bank Identifier Code) lookup and validation
  name: SWIFT BICs API
  slug: swift-bics-api
- description: Country code lookup and validation
  name: SWIFT Country Codes API
  slug: swift-country-codes-api
- description: Currency code lookup and validation
  name: SWIFT Currency Codes API
  slug: swift-currency-codes-api
- description: IBAN (International Bank Account Number) lookup and validation
  name: SWIFT IBANs API
  slug: swift-ibans-api
- description: LEI (Legal Entity Identifier) lookup and validation
  name: SWIFT LEIs API
  slug: swift-leis-api
- description: National ID lookup and BIC resolution
  name: SWIFT National IDs API
  slug: swift-national-ids-api
artifact_total: 35
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
  name: SWIFT SwiftRef API
  slug: open-swift-swiftref-api
common:
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
overview: 'SWIFT publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account Numbers API, BBANs API, BICs API, and 5 more. Tagged areas include Banking, Cross-Border Payments, Financial Messaging, Financial Services, and GPI.


  The SWIFT catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SWIFT''s developer surface includes authentication, API reference, sandbox, support, and 16 more developer resources.'
plans:
- name: Swift Plans Pricing
  plan_count: 1
  slug: swift-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 1
  name: Swift Rate Limits
  slug: swift-rate-limits
rules:
- name: SWIFT API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swift-jsonschema-spectral-rules
- name: SWIFT API Rules
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
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 67.4
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 54.4
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
    score: 53.2
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Financial Services
- GPI
- ISO 20022
- Payments
website: https://www.swift.com
---
