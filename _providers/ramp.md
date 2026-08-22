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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ramp Agentic Access
  operation_count: 12
  slug: ramp-agentic-access
  summary_line: 12 operations
api_count: 11
apis:
- description: General ledger account resources used to map Ramp activity to accounting systems.
  name: Ramp Accounts API
  slug: ramp-accounts-api
- description: Audit events recording activity within a Ramp organization.
  name: Ramp Audit Logs API
  slug: ramp-audit-logs-api
- description: Bill pay records and approval workflows.
  name: Ramp Bills API
  slug: ramp-bills-api
- description: Physical and virtual cards issued to users and departments.
  name: Ramp Cards API
  slug: ramp-cards-api
- description: Department records used to organize spend.
  name: Ramp Departments API
  slug: ramp-departments-api
- description: Location records used to organize spend.
  name: Ramp Locations API
  slug: ramp-locations-api
- description: Out-of-pocket reimbursement requests.
  name: Ramp Reimbursements API
  slug: ramp-reimbursements-api
- description: Card statement records.
  name: Ramp Statements API
  slug: ramp-statements-api
- description: Card and bill transactions across the organization.
  name: Ramp Transactions API
  slug: ramp-transactions-api
- description: User accounts within a Ramp organization.
  name: Ramp Users API
  slug: ramp-users-api
- description: Vendor records used by accounting integrations and bill pay workflows.
  name: Ramp Vendors API
  slug: ramp-vendors-api
arazzos:
- description: Resolve a transaction's card and user, then pull the user and card directories for attribution.
  name: Ramp Attribute Transaction To Cardholder
  slug: ramp-attribute-transaction-to-cardholder-workflow
- description: List audit events and the user directory to resolve the actor behind each event.
  name: Ramp Audit Event Target Lookup
  slug: ramp-audit-event-target-lookup-workflow
- description: Pull the card and user directories to build a per-cardholder card inventory.
  name: Ramp Card Inventory By Cardholder
  slug: ramp-card-inventory-by-cardholder-workflow
- description: Retrieve a transaction and pull the GL account list to support categorization.
  name: Ramp Categorize Transaction To Account
  slug: ramp-categorize-transaction-to-account-workflow
- description: Pull transactions, cards, and users together to assemble a single spend snapshot.
  name: Ramp Export Spend Snapshot
  slug: ramp-export-spend-snapshot-workflow
- description: List users, then list a date window of transactions to slice spend by cardholder.
  name: Ramp Find Cardholder Recent Spend
  slug: ramp-find-cardholder-recent-spend-workflow
- description: List transactions in a window and branch on whether the first one exceeds a threshold.
  name: Ramp Flag Large Transaction
  slug: ramp-flag-large-transaction-workflow
- description: List bills and branch into a vendor lookup only when the first bill is still open.
  name: Ramp Flag Open Bill Vendor
  slug: ramp-flag-open-bill-vendor-workflow
- description: List transactions in a date range, pick the first, and retrieve its full record.
  name: Ramp Inspect Transaction Detail
  slug: ramp-inspect-transaction-detail-workflow
- description: Pull departments, users, and transactions to roll spend up by department.
  name: Ramp Locate Department Spend
  slug: ramp-locate-department-spend-workflow
- description: Pull locations, users, and transactions to roll spend up by location.
  name: Ramp Locate Location Spend
  slug: ramp-locate-location-spend-workflow
- description: Pull the user, department, and location directories to build an org spend map.
  name: Ramp Map Users To Departments
  slug: ramp-map-users-to-departments-workflow
- description: Page through the general ledger account list by following the start cursor.
  name: Ramp Paginate Accounting Accounts
  slug: ramp-paginate-accounting-accounts-workflow
- description: Pull bills and the accounting vendor directory to resolve each bill's vendor.
  name: Ramp Reconcile Bills With Vendors
  slug: ramp-reconcile-bills-with-vendors-workflow
- description: Pull reimbursements and the user directory to attribute each request to a person.
  name: Ramp Reconcile Reimbursements To Users
  slug: ramp-reconcile-reimbursements-to-users-workflow
- description: List reimbursements and branch into a user lookup only when one is still pending.
  name: Ramp Review Pending Reimbursement Detail
  slug: ramp-review-pending-reimbursement-detail-workflow
- description: List statements, then pull the transactions for the statement period to reconcile a close.
  name: Ramp Statement Close Detail
  slug: ramp-statement-close-detail-workflow
- description: List transactions, retrieve the first in full, then pull GL accounts for coding.
  name: Ramp Trace Transaction To Account Detail
  slug: ramp-trace-transaction-to-account-detail-workflow
artifact_total: 67
asyncapis:
- description: Event-driven surface for the Ramp Developer API. Ramp delivers webhook events to subscriber-provided HTTPS endpoints whenever state changes occur on resources such as transactions, bills, reimbursemen
  name: Ramp Developer API Webhooks
  slug: ramp-developer-api-webhooks-asyncapi
collections:
- collection_type: postman
  name: Ramp Developer API
  slug: postman-ramp-developer-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ramp Developer Accounts API
  slug: open-ramp-accounts-api
- collection_type: open
  name: Ramp Developer Accounts Audit Logs API
  slug: open-ramp-audit-logs-api
- collection_type: open
  name: Ramp Developer Accounts Bills API
  slug: open-ramp-bills-api
- collection_type: open
  name: Ramp Developer Accounts Cards API
  slug: open-ramp-cards-api
- collection_type: open
  name: Ramp Developer Accounts Departments API
  slug: open-ramp-departments-api
- collection_type: open
  name: Ramp Developer API
  slug: open-ramp-developer-api
- collection_type: open
  name: Ramp Developer Accounts Locations API
  slug: open-ramp-locations-api
- collection_type: open
  name: Ramp Developer Accounts Reimbursements API
  slug: open-ramp-reimbursements-api
- collection_type: open
  name: Ramp Developer Accounts Statements API
  slug: open-ramp-statements-api
- collection_type: open
  name: Ramp Developer Accounts Transactions API
  slug: open-ramp-transactions-api
- collection_type: open
  name: Ramp Developer Accounts Users API
  slug: open-ramp-users-api
- collection_type: open
  name: Ramp Developer Accounts Vendors API
  slug: open-ramp-vendors-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ramp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ramp-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ramp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ramp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ramp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ramp-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ramp/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-attribute-transaction-to-cardholder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-audit-event-target-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-card-inventory-by-cardholder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-categorize-transaction-to-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-export-spend-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-find-cardholder-recent-spend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-flag-large-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-flag-open-bill-vendor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-inspect-transaction-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-locate-department-spend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-locate-location-spend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-map-users-to-departments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-paginate-accounting-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-reconcile-bills-with-vendors-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-reconcile-reimbursements-to-users-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-review-pending-reimbursement-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-statement-close-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ramp-trace-transaction-to-account-detail-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ramp-public
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ramp
- group: company
  title: ''
  type: Website
  url: https://ramp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ramp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ramp.com/developer-api/v1/overview/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://docs.ramp.com/developer-api/v1/guides/authorization
- group: start
  title: ''
  type: Signup
  url: https://app.ramp.com/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://ramp.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://ramp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.ramp.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ramp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ramp.com/legal/platform-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ramp.com/legal/privacy-policy
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ramp-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ramp.com/llms.txt
created: '2025-02-17'
description: Ramp is a finance automation platform that combines corporate cards, expense management, accounts payable, vendor management, and accounting integrations into a single product. The Ramp Developer API enables developers to access and manage Ramp account data, build applications for the Ramp App Center reaching over 25,000 Ramp customers, and automate financial workflows by integrating Ramp into existing systems.
examples:
- key_count: 2
  name: Ramp List Cards Example
  slug: ramp-list-cards-example
- key_count: 2
  name: Ramp List Transactions Example
  slug: ramp-list-transactions-example
- key_count: 2
  name: Ramp List Users Example
  slug: ramp-list-users-example
finops:
- name: Ramp Finops
  service_category: API
  slug: ramp-finops
graphqls:
- description: Ramp is a corporate card and spend management platform for finance teams. The API covers cards, transactions, reimbursements, departments, locations, accounting integrations, receipts, memos, and spen
  name: Ramp GraphQL API
  slug: ramp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ramp.png
json_schemas:
- name: Ramp Card
  property_count: 7
  slug: ramp-card
- name: Ramp Transaction
  property_count: 11
  slug: ramp-transaction
- name: Ramp User
  property_count: 10
  slug: ramp-user
json_structures:
- name: Ramp Card Structure
  property_count: 0
  slug: ramp-card-structure
- name: Ramp Transaction Structure
  property_count: 0
  slug: ramp-transaction-structure
- name: Ramp User Structure
  property_count: 0
  slug: ramp-user-structure
jsonld:
- class_count: 20
  name: Ramp Context
  property_count: 4
  slug: ramp-context
layout: provider
modified: '2026-05-30'
name: Ramp
nav: Providers
network: true
overview: 'Ramp publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Audit Logs API, Bills API, and 8 more. Tagged areas include Finance, Spend Management, Corporate Cards, Expense Management, and Accounts Payable.


  The Ramp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Ramp''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 34 more developer resources.'
plans:
- name: Ramp Plans Pricing
  plan_count: 3
  slug: ramp-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Ramp Rate Limits
  slug: ramp-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Ramp API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: ramp-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Ramp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ramp-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Ramp API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 4
  slug: ramp-rules
scopes:
- name: Ramp Scopes
  scope_count: 12
  slug: ramp-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: developing
  composite: 53.2
  delta: -7.9
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 26.5
    contract_quality: 73.8
    developer_ergonomics: 7.1
    discoverability: 81.5
    governance: 26.5
    operational_transparency: 18.4
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ramp/refs/heads/main/screenshots/ramp-2026-06-20T192620.png
security:
- kind: authentication
  name: Ramp Authentication
  slug: ramp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ramp Domain Security
  slug: ramp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ramp Vulnerability Disclosure
  slug: ramp-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ramp Trust Center
  slug: ramp-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP
slug: ramp
tags:
- Finance
- Spend Management
- Corporate Cards
- Expense Management
- Accounts Payable
- Bill Pay
- Accounting
- Reimbursements
website: https://ramp.com/
---
