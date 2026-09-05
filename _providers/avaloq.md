---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Avaloq Agentic Access
  operation_count: 9
  slug: avaloq-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 2
apis:
- description: Community APIs for fintech integration providing simplified REST endpoints for connecting third-party applications with the Avaloq banking platform. Pre-vetted by Avaloq for secure, standards-based in
  name: Avaloq Community API
  slug: avaloq-community-api
- baseURL: https://api.avaloq.com
  baseurl_source: declared
  description: Bank account management
  name: Avaloq Accounts API
  slug: avaloq-accounts-api
- baseURL: https://api.avaloq.com
  baseurl_source: declared
  description: Customer data management
  name: Avaloq Customers API
  slug: avaloq-customers-api
- baseURL: https://api.avaloq.com
  baseurl_source: declared
  description: Payment tracking and status
  name: Avaloq Payment Status API
  slug: avaloq-payment-status-api
- baseURL: https://api.avaloq.com
  baseurl_source: declared
  description: Payment instructions and transfers
  name: Avaloq Payments API
  slug: avaloq-payments-api
- baseURL: https://api.avaloq.com
  baseurl_source: declared
  description: Transaction history and management
  name: Avaloq Transactions API
  slug: avaloq-transactions-api
artifact_total: 91
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Avaloq Banking Accounts API
  slug: open-avaloq-accounts-api
- collection_type: open
  name: Avaloq Banking API
  slug: open-avaloq-banking
- collection_type: open
  name: Avaloq Banking Accounts Customers API
  slug: open-avaloq-customers-api
- collection_type: open
  name: Avaloq Banking Accounts Payment Status API
  slug: open-avaloq-payment-status-api
- collection_type: open
  name: Avaloq Banking Accounts Payments API
  slug: open-avaloq-payments-api
- collection_type: open
  name: Avaloq Payments API
  slug: open-avaloq-payments
- collection_type: open
  name: Avaloq Banking Accounts Transactions API
  slug: open-avaloq-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/avaloq-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/avaloq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avaloq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/avaloq-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.avaloq.com/
- group: company
  title: ''
  type: Website
  url: https://www.avaloq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.avaloq.com/web/developer-portal/getting-started/developing
- group: other
  title: ''
  type: Ecosystem
  url: https://www.avaloq.com/platform/ecosystem
- group: learn
  title: ''
  type: Academy
  url: https://avaloq.academy/
- group: operate
  title: ''
  type: Support
  url: https://www.avaloq.com/en/for-developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avaloq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avaloq/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-banking-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/rules/avaloq-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/vocabulary/avaloq-vocabulary.yaml
created: '2024-01-20'
description: Avaloq is a leading provider of wealth management technology and digital banking solutions, offering over 7,500 REST API endpoints for financial services integration. The platform connects more than 170 financial institutions with 200+ fintech partners through Community APIs, Standard Adapters, and certified integrations for banking, wealth management, payments, and compliance.
examples:
- key_count: 6
  name: Avaloq Createpayment Example
  slug: avaloq-createpayment-example
- key_count: 6
  name: Avaloq Listaccounts Example
  slug: avaloq-listaccounts-example
- key_count: 7
  name: Banking Account Example
  slug: banking-account-example
- key_count: 4
  name: Banking Account List Example
  slug: banking-account-list-example
- key_count: 6
  name: Banking Create Customer Request Example
  slug: banking-create-customer-request-example
- key_count: 8
  name: Banking Customer Example
  slug: banking-customer-example
- key_count: 2
  name: Banking Customer List Example
  slug: banking-customer-list-example
- key_count: 9
  name: Banking Transaction Example
  slug: banking-transaction-example
- key_count: 4
  name: Banking Transaction List Example
  slug: banking-transaction-list-example
- key_count: 7
  name: Payments Payment Example
  slug: payments-payment-example
- key_count: 2
  name: Payments Payment List Example
  slug: payments-payment-list-example
- key_count: 9
  name: Payments Payment Request Example
  slug: payments-payment-request-example
features:
- description: Over 7,500 REST API endpoints for comprehensive banking and wealth management operations.
  name: 7500+ REST API Endpoints
- description: Pre-vetted REST APIs for seamless fintech integration with the Avaloq platform.
  name: Community APIs
- description: Three adapter types (Standard, Certified, Project) enabling ecosystem connectivity.
  name: Standard and Certified Adapters
- description: Sandbox access to Avaloq products in the cloud for integration testing.
  name: Cloud Sandbox
- description: Event-driven integration via Apache Kafka for real-time data streaming alongside REST APIs.
  name: Kafka Integration
- description: Dual protocol support for SOAP and REST through the AMI Web Services Framework.
  name: SOAP and REST Support
- description: Built-in integration with BlackRock Aladdin for institutional investment management.
  name: BlackRock Aladdin Integration
- description: Support for FINMA, MiFID II, GDPR, and other regulatory frameworks.
  name: Multi-Jurisdiction Regulatory Support
finops:
- name: Avaloq Finops
  service_category: Core Banking / Wealth Management
  slug: avaloq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avaloq.png
integrations:
- description: Native integration with Aladdin by BlackRock for institutional investment management.
  name: BlackRock Aladdin
- description: Market data integration with Bloomberg for pricing and analytics.
  name: Bloomberg
- description: SWIFT messaging network integration for international payment processing.
  name: SWIFT
- description: SEPA credit transfer and direct debit support for European payments.
  name: SEPA
- description: Avaloq Model Bank available on AWS for simplified cloud deployment and testing.
  name: AWS
- description: CRM integration with Salesforce for client relationship management.
  name: Salesforce
- description: FIX protocol support for electronic trading and order routing.
  name: FIX Protocol
json_schemas:
- name: Account
  property_count: 10
  slug: avaloq-account
- name: AccountList
  property_count: 3
  slug: avaloq-accountlist
- name: CreateCustomerRequest
  property_count: 6
  slug: avaloq-createcustomerrequest
- name: Customer
  property_count: 10
  slug: avaloq-customer
- name: CustomerList
  property_count: 3
  slug: avaloq-customerlist
- name: Error
  property_count: 3
  slug: avaloq-error
- name: Payment
  property_count: 7
  slug: avaloq-payment
- name: PaymentList
  property_count: 3
  slug: avaloq-paymentlist
- name: PaymentRequest
  property_count: 8
  slug: avaloq-paymentrequest
- name: Transaction
  property_count: 11
  slug: avaloq-transaction
- name: TransactionList
  property_count: 3
  slug: avaloq-transactionlist
- name: AccountList
  property_count: 3
  slug: banking-account-list
- name: Account
  property_count: 10
  slug: banking-account
- name: CreateCustomerRequest
  property_count: 6
  slug: banking-create-customer-request
- name: CustomerList
  property_count: 3
  slug: banking-customer-list
- name: Customer
  property_count: 10
  slug: banking-customer
- name: TransactionList
  property_count: 3
  slug: banking-transaction-list
- name: Transaction
  property_count: 11
  slug: banking-transaction
- name: PaymentList
  property_count: 3
  slug: payments-payment-list
- name: PaymentRequest
  property_count: 8
  slug: payments-payment-request
- name: Payment
  property_count: 7
  slug: payments-payment
json_structures:
- name: Avaloq Structure
  property_count: 0
  slug: avaloq-structure
- name: Banking Account List Structure
  property_count: 3
  slug: banking-account-list-structure
- name: Banking Account Structure
  property_count: 10
  slug: banking-account-structure
- name: Banking Create Customer Request Structure
  property_count: 6
  slug: banking-create-customer-request-structure
- name: Banking Customer List Structure
  property_count: 3
  slug: banking-customer-list-structure
- name: Banking Customer Structure
  property_count: 10
  slug: banking-customer-structure
- name: Banking Transaction List Structure
  property_count: 3
  slug: banking-transaction-list-structure
- name: Banking Transaction Structure
  property_count: 11
  slug: banking-transaction-structure
- name: Payments Payment List Structure
  property_count: 3
  slug: payments-payment-list-structure
- name: Payments Payment Request Structure
  property_count: 8
  slug: payments-payment-request-structure
- name: Payments Payment Structure
  property_count: 7
  slug: payments-payment-structure
jsonld:
- class_count: 0
  name: Avaloq Banking Context
  property_count: 17
  slug: avaloq-banking-context
- class_count: 0
  name: Avaloq Payments Context
  property_count: 8
  slug: avaloq-payments-context
layout: provider
modified: '2026-05-19'
name: Avaloq
nav: Providers
network: true
overview: 'Avaloq publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Customers API, Payment Status API, and 2 more. Tagged areas include Banking, Digital Banking, Financial-Services, Fintech, and Payments.


  The Avaloq catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Avaloq''s developer surface includes authentication, developer portal, getting-started guide, academy / training, support, and 10 more developer resources.'
plans:
- name: Avaloq Plans Pricing
  plan_count: 2
  slug: avaloq-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Avaloq Rate Limits
  slug: avaloq-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Avaloq API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: avaloq-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Avaloq API Rules
  rule_count: 33
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 22
  slug: avaloq-spectral-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 60.7
    developer_ergonomics: 36.9
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/screenshots/avaloq-2026-06-20T172720.png
security:
- kind: authentication
  name: Avaloq Authentication
  slug: avaloq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Avaloq Domain Security
  slug: avaloq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: avaloq
tags:
- Banking
- Digital Banking
- Financial-Services
- Fintech
- Payments
- Wealth Management
use_cases:
- description: Connect advisory tools and portfolio management applications with core banking data.
  name: Wealth Management Platform Integration
- description: Build mobile and web banking experiences on top of Avaloq account and transaction APIs.
  name: Digital Banking Channels
- description: Onboard fintech partners into the banking ecosystem through Community APIs.
  name: Fintech Partner Integration
- description: Automate MiFID II, FINMA, and other regulatory report generation and submission.
  name: Regulatory Reporting Automation
- description: Integrate domestic SEPA and international SWIFT payment processing.
  name: Payment Processing
- description: Digitize client onboarding with KYC checks, document collection, and compliance screening.
  name: KYC and Client Onboarding
- description: Build robo-advisory and portfolio management tools using investment APIs.
  name: Investment Portfolio Management
- description: Execute and manage multi-asset trade orders through the Avaloq OMS.
  name: Trade Order Management
website: https://www.avaloq.com/
---
