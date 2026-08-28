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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 118
  human_in_the_loop: 77
  name: Emburse Agentic Access
  operation_count: 213
  slug: emburse-agentic-access
  summary_line: 213 operations · 118 acting · 77 human-in-the-loop
api_count: 48
apis:
- description: REST API for Emburse Professional (formerly Certify) supporting push/pull of users, departments, categories, expense reports, expense lines, receipt data, and invoices. Base URL is https://api.certify
  name: Emburse Professional API
  slug: emburse-professional-api
- description: Modern REST API for Emburse Spend (formerly Abacus) using OAuth 2.0 authentication and JSON for expense and card management. Available to Partners and customers on the Plus plan or higher.
  name: Emburse Spend API
  slug: emburse-spend-api
- description: The Accounts API from Emburse — 4 operation(s) for accounts.
  name: Emburse Accounts API
  slug: emburse-accounts-api
- description: The allocation-api-controller-v-1 API from Emburse — 1 operation(s) for allocation-api-controller-v-1.
  name: Emburse allocation-api-controller-v-1 API
  slug: emburse-allocation-api-controller-v-1-api
- description: The allocation-api-controller-v-2 API from Emburse — 1 operation(s) for allocation-api-controller-v-2.
  name: Emburse allocation-api-controller-v-2 API
  slug: emburse-allocation-api-controller-v-2-api
- description: V3 endpoints include better support and error handling for allocation user defined attributes (UDA).
  name: Emburse allocation-api-controller-v-3 API
  slug: emburse-allocation-api-controller-v-3-api
- description: The Allowances API from Emburse — 1 operation(s) for allowances.
  name: Emburse Allowances API
  slug: emburse-allowances-api
- description: The Cards API from Emburse — 3 operation(s) for cards.
  name: Emburse Cards API
  slug: emburse-cards-api
- description: The Categories API from Emburse — 2 operation(s) for categories.
  name: Emburse Categories API
  slug: emburse-categories-api
- description: The Company API from Emburse — 2 operation(s) for company.
  name: Emburse Company API
  slug: emburse-company-api
- description: The Departments API from Emburse — 2 operation(s) for departments.
  name: Emburse Departments API
  slug: emburse-departments-api
- description: Entity Type Controller
  name: Emburse Entity Type API
  slug: emburse-entity-type-api
- description: V1 Entity Controller
  name: Emburse Entity (V1) API
  slug: emburse-entity-v1-api
- description: V2 Entity Controller
  name: Emburse Entity (V2) API
  slug: emburse-entity-v2-api
- description: Approve, return and reassign expense reports.
  name: Emburse expense-approval-controller-v1 API
  slug: emburse-expense-approval-controller-v1-api
- description: Approve, return and reassign expense reports using username or email of approver.
  name: Emburse expense-approval-controller-v2 API
  slug: emburse-expense-approval-controller-v2-api
- description: Retrieve expense report information and create draft expense reports
  name: Emburse expense-controller-v1 API
  slug: emburse-expense-controller-v1-api
- description: Retrieve expense reports by filter(s)
  name: Emburse expense-controller-v3 API
  slug: emburse-expense-controller-v3-api
- description: Get and post expense export information.
  name: Emburse expense-export-controller-v1 API
  slug: emburse-expense-export-controller-v1-api
- description: Get and post expense or invoice export information.
  name: Emburse expense-export-controller-v2 API
  slug: emburse-expense-export-controller-v2-api
- description: Retrieve Expense Report Receipts / Images
  name: Emburse expense-image-api API
  slug: emburse-expense-image-api-api
- description: Retrieve expense receipt PDF
  name: Emburse expense-receipts-controller API
  slug: emburse-expense-receipts-controller-api
- description: Retrieve expense report line items
  name: Emburse expense-report-line-item-controller API
  slug: emburse-expense-report-line-item-controller-api
- description: Retrieve expense type information
  name: Emburse expense-types-controller API
  slug: emburse-expense-types-controller-api
- description: Operations in Invoice Api
  name: Emburse invoice-api-external-controller API
  slug: emburse-invoice-api-external-controller-api
- description: The Labels API from Emburse — 2 operation(s) for labels.
  name: Emburse Labels API
  slug: emburse-labels-api
- description: The Locations API from Emburse — 2 operation(s) for locations.
  name: Emburse Locations API
  slug: emburse-locations-api
- description: The Members API from Emburse — 3 operation(s) for members.
  name: Emburse Members API
  slug: emburse-members-api
- description: The Merchant Categories API from Emburse — 1 operation(s) for merchant categories.
  name: Emburse Merchant Categories API
  slug: emburse-merchant-categories-api
- description: The Oauth API from Emburse — 3 operation(s) for oauth.
  name: Emburse Oauth API
  slug: emburse-oauth-api
- description: Post payments
  name: Emburse paid-expense-controller API
  slug: emburse-paid-expense-controller-api
- description: Person Controller v2
  name: Emburse person-controller-v2 API
  slug: emburse-person-controller-v2-api
- description: Person Controller v3
  name: Emburse person-controller-v3 API
  slug: emburse-person-controller-v3-api
- description: Person Web Services
  name: Emburse person-controller-v4 API
  slug: emburse-person-controller-v4-api
- description: Operations in PO APIs
  name: Emburse po-api-controller API
  slug: emburse-po-api-controller-api
- description: Operations in PO Receipts APIs
  name: Emburse po-api-receipt-controller API
  slug: emburse-po-api-receipt-controller-api
- description: The pre-approval-api-controller API from Emburse — 9 operation(s) for pre-approval-api-controller.
  name: Emburse pre-approval-api-controller API
  slug: emburse-pre-approval-api-controller-api
- description: The pre-approval-api-controller-v-2 API from Emburse — 3 operation(s) for pre-approval-api-controller-v-2.
  name: Emburse pre-approval-api-controller-v-2 API
  slug: emburse-pre-approval-api-controller-v-2-api
- description: The pre-approval-api-export-controller API from Emburse — 4 operation(s) for pre-approval-api-export-controller.
  name: Emburse pre-approval-api-export-controller API
  slug: emburse-pre-approval-api-export-controller-api
- description: The pre-approval-import-controller API from Emburse — 1 operation(s) for pre-approval-import-controller.
  name: Emburse pre-approval-import-controller API
  slug: emburse-pre-approval-import-controller-api
- description: The Requisitions API from Emburse — 2 operation(s) for requisitions.
  name: Emburse Requisitions API
  slug: emburse-requisitions-api
- description: Retrieve information concerning returned payments
  name: Emburse returned-payments-controller API
  slug: emburse-returned-payments-controller-api
- description: Sap Person Controller
  name: Emburse sap-person-controller API
  slug: emburse-sap-person-controller-api
- description: The Shared Links API from Emburse — 2 operation(s) for shared links.
  name: Emburse Shared Links API
  slug: emburse-shared-links-api
- description: The Shipping Addresses API from Emburse — 2 operation(s) for shipping addresses.
  name: Emburse Shipping Addresses API
  slug: emburse-shipping-addresses-api
- description: The Transactions API from Emburse — 2 operation(s) for transactions.
  name: Emburse Transactions API
  slug: emburse-transactions-api
- description: The /v1/contacts API from Emburse — 1 operation(s) for /v1/contacts.
  name: Emburse /v1/contacts API
  slug: emburse-v1-contacts-api
- description: Operations in Vendor API application service
  name: Emburse vendor-api-controller API
  slug: emburse-vendor-api-controller-api
artifact_total: 114
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Api Documentation Accounts API
  slug: open-emburse-accounts-api
- collection_type: open
  name: Api Documentation Accounts allocation-api-controller-v-1 API
  slug: open-emburse-allocation-api-controller-v-1-api
- collection_type: open
  name: Api Documentation Accounts allocation-api-controller-v-2 API
  slug: open-emburse-allocation-api-controller-v-2-api
- collection_type: open
  name: Api Documentation Accounts allocation-api-controller-v-3 API
  slug: open-emburse-allocation-api-controller-v-3-api
- collection_type: open
  name: Api Documentation Accounts Allowances API
  slug: open-emburse-allowances-api
- collection_type: open
  name: Api Documentation Accounts Cards API
  slug: open-emburse-cards-api
- collection_type: open
  name: Api Documentation Accounts Categories API
  slug: open-emburse-categories-api
- collection_type: open
  name: Api Documentation Accounts Company API
  slug: open-emburse-company-api
- collection_type: open
  name: Api Documentation Accounts Departments API
  slug: open-emburse-departments-api
- collection_type: open
  name: Api Documentation Accounts Entity Type API
  slug: open-emburse-entity-type-api
- collection_type: open
  name: Api Documentation Accounts Entity (V1) API
  slug: open-emburse-entity-v1-api
- collection_type: open
  name: Api Documentation Accounts Entity (V2) API
  slug: open-emburse-entity-v2-api
- collection_type: open
  name: Api Documentation Accounts expense-approval-controller-v1 API
  slug: open-emburse-expense-approval-controller-v1-api
- collection_type: open
  name: Api Documentation Accounts expense-approval-controller-v2 API
  slug: open-emburse-expense-approval-controller-v2-api
- collection_type: open
  name: Api Documentation Accounts expense-controller-v1 API
  slug: open-emburse-expense-controller-v1-api
- collection_type: open
  name: Api Documentation Accounts expense-controller-v3 API
  slug: open-emburse-expense-controller-v3-api
- collection_type: open
  name: Api Documentation Accounts expense-export-controller-v1 API
  slug: open-emburse-expense-export-controller-v1-api
- collection_type: open
  name: Api Documentation Accounts expense-export-controller-v2 API
  slug: open-emburse-expense-export-controller-v2-api
- collection_type: open
  name: Api Documentation Accounts expense-image-api API
  slug: open-emburse-expense-image-api-api
- collection_type: open
  name: Api Documentation Accounts expense-receipts-controller API
  slug: open-emburse-expense-receipts-controller-api
- collection_type: open
  name: Api Documentation Accounts expense-report-line-item-controller API
  slug: open-emburse-expense-report-line-item-controller-api
- collection_type: open
  name: Api Documentation Accounts expense-types-controller API
  slug: open-emburse-expense-types-controller-api
- collection_type: open
  name: Api Documentation Accounts invoice-api-external-controller API
  slug: open-emburse-invoice-api-external-controller-api
- collection_type: open
  name: Api Documentation Accounts Labels API
  slug: open-emburse-labels-api
- collection_type: open
  name: Api Documentation Accounts Locations API
  slug: open-emburse-locations-api
- collection_type: open
  name: Api Documentation Accounts Members API
  slug: open-emburse-members-api
- collection_type: open
  name: Api Documentation Accounts Merchant Categories API
  slug: open-emburse-merchant-categories-api
- collection_type: open
  name: Api Documentation Accounts Oauth API
  slug: open-emburse-oauth-api
- collection_type: open
  name: Api Documentation Accounts paid-expense-controller API
  slug: open-emburse-paid-expense-controller-api
- collection_type: open
  name: Api Documentation Accounts person-controller-v2 API
  slug: open-emburse-person-controller-v2-api
- collection_type: open
  name: Api Documentation Accounts person-controller-v3 API
  slug: open-emburse-person-controller-v3-api
- collection_type: open
  name: Api Documentation Accounts person-controller-v4 API
  slug: open-emburse-person-controller-v4-api
- collection_type: open
  name: Api Documentation Accounts po-api-controller API
  slug: open-emburse-po-api-controller-api
- collection_type: open
  name: Api Documentation Accounts po-api-receipt-controller API
  slug: open-emburse-po-api-receipt-controller-api
- collection_type: open
  name: Api Documentation Accounts pre-approval-api-controller API
  slug: open-emburse-pre-approval-api-controller-api
- collection_type: open
  name: Api Documentation Accounts pre-approval-api-controller-v-2 API
  slug: open-emburse-pre-approval-api-controller-v-2-api
- collection_type: open
  name: Api Documentation Accounts pre-approval-api-export-controller API
  slug: open-emburse-pre-approval-api-export-controller-api
- collection_type: open
  name: Api Documentation Accounts pre-approval-import-controller API
  slug: open-emburse-pre-approval-import-controller-api
- collection_type: open
  name: Api Documentation Accounts Requisitions API
  slug: open-emburse-requisitions-api
- collection_type: open
  name: Api Documentation Accounts returned-payments-controller API
  slug: open-emburse-returned-payments-controller-api
- collection_type: open
  name: Api Documentation Accounts sap-person-controller API
  slug: open-emburse-sap-person-controller-api
- collection_type: open
  name: Api Documentation Accounts Shared Links API
  slug: open-emburse-shared-links-api
- collection_type: open
  name: Api Documentation Accounts Shipping Addresses API
  slug: open-emburse-shipping-addresses-api
- collection_type: open
  name: Api Documentation Accounts Transactions API
  slug: open-emburse-transactions-api
- collection_type: open
  name: Api Documentation Accounts /v1/contacts API
  slug: open-emburse-v1-contacts-api
- collection_type: open
  name: Api Documentation Accounts vendor-api-controller API
  slug: open-emburse-vendor-api-controller-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emburse-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/emburse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emburse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emburse-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.emburse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.emburse.com/api-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emburse
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emburse
- group: other
  title: ''
  type: X
  url: https://twitter.com/emburse
- group: company
  title: ''
  type: Blog
  url: https://www.emburse.com/blog
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/emburse/refs/heads/main/plans/emburse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/emburse/refs/heads/main/rate-limits/emburse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/emburse/refs/heads/main/finops/emburse-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/emburse/refs/heads/main/vocabulary/emburse-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/emburse/refs/heads/main/json-ld/emburse-context.jsonld
created: 2026-06-12
description: Emburse is an expense management and accounts payable automation platform serving over 4 million finance leaders and business travelers worldwide. The company offers REST APIs across its product lines including Emburse Professional (formerly Certify), Emburse Spend (formerly Abacus), and Emburse Enterprise (Chrome River), enabling integrations for expense reports, corporate card management, invoice processing, receipt capture, and reimbursement workflows. The Virtual Cards API provides OAuth2-secured endpoints for creating and managing virtual and physical cards, transactions, members, and accounting data. Emburse Enterprise exposes Swagger-documented APIs for Expense, Invoice, Person, PreApproval, Purchase Order, Vendor, and Allocation resources. API access for the Spend product is available to Partners and customers on the Plus plan or higher.
examples:
- key_count: 13
  name: Emburse Account Example
  slug: emburse-account-example
- key_count: 22
  name: Emburse Card Example
  slug: emburse-card-example
- key_count: 11
  name: Emburse Member Example
  slug: emburse-member-example
- key_count: 28
  name: Emburse Transaction Example
  slug: emburse-transaction-example
finops:
- name: Emburse Finops
  service_category: ''
  slug: emburse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emburse.png
json_schemas:
- name: APIAccount
  property_count: 13
  slug: emburse-account
- name: APIAllowance
  property_count: 14
  slug: emburse-allowance
- name: APICard
  property_count: 22
  slug: emburse-card
- name: APIMember
  property_count: 11
  slug: emburse-member
- name: APIShippingAddress
  property_count: 10
  slug: emburse-shippingaddress
- name: APITransaction
  property_count: 28
  slug: emburse-transaction
jsonld:
- class_count: 21
  name: Emburse Context
  property_count: 15
  slug: emburse-context
layout: provider
modified: 2026-06-12
name: Emburse
nav: Providers
network: true
overview: 'Emburse publishes 46 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, allocation-api-controller-v-1 API, allocation-api-controller-v-2 API, and 43 more. Tagged areas include Expense Management, AP Automation, Corporate Cards, Virtual Cards, and Receipt Capture.


  The Emburse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Emburse''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Emburse Plans Pricing
  plan_count: 7
  slug: emburse-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Emburse Rate Limits
  slug: emburse-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Emburse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: emburse-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 59.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 34.2
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emburse/refs/heads/main/screenshots/emburse-2026-06-20T180630.png
security:
- kind: authentication
  name: Emburse Authentication
  slug: emburse-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Emburse Domain Security
  slug: emburse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Emburse Vulnerability Disclosure
  slug: emburse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: emburse
tags:
- Expense Management
- AP Automation
- Corporate Cards
- Virtual Cards
- Receipt Capture
- Reimbursement
- Invoice Processing
- Finance
- Fintech
website: https://www.emburse.com/
---
