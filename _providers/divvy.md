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
  - '{''url'': ''https://getdivvy.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.bill.com/product/spend-and-expense — a different registrable domain (getdivvy.com -> bill.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 208
  human_in_the_loop: 0
  name: Divvy Agentic Access
  operation_count: 326
  slug: divvy-agentic-access
  summary_line: 326 operations · 208 acting
api_count: 2
apis:
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The attachments API from Divvy — 4 operation(s) for attachments.
  name: Divvy Attachments API
  slug: divvy-attachments-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The authentication API from Divvy — 4 operation(s) for authentication.
  name: Divvy Authentication API
  slug: divvy-authentication-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The bill-approvals API from Divvy — 4 operation(s) for bill-approvals.
  name: Divvy Bill Approvals API
  slug: divvy-bill-approvals-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The bills API from Divvy — 6 operation(s) for bills.
  name: Divvy Bills API
  slug: divvy-bills-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The budgets API from Divvy — 5 operation(s) for budgets.
  name: Divvy Budgets API
  slug: divvy-budgets-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The cards API from Divvy — 5 operation(s) for cards.
  name: Divvy Cards API
  slug: divvy-cards-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The classifications API from Divvy — 49 operation(s) for classifications.
  name: Divvy Classifications API
  slug: divvy-classifications-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The credit-memos API from Divvy — 7 operation(s) for credit-memos.
  name: Divvy Credit Memos API
  slug: divvy-credit-memos-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The custom-fields API from Divvy — 4 operation(s) for custom-fields.
  name: Divvy Custom Fields API
  slug: divvy-custom-fields-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The customers API from Divvy — 12 operation(s) for customers.
  name: Divvy Customers API
  slug: divvy-customers-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The documents API from Divvy — 3 operation(s) for documents.
  name: Divvy Documents API
  slug: divvy-documents-api
- baseURL: https://gateway.stage.bill.com/connect-events
  baseurl_source: spec
  description: The events API from Divvy — 3 operation(s) for events.
  name: Divvy Events API
  slug: divvy-events-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The exports API from Divvy — 2 operation(s) for exports.
  name: Divvy Exports API
  slug: divvy-exports-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The funding-accounts API from Divvy — 13 operation(s) for funding-accounts.
  name: Divvy Funding Accounts API
  slug: divvy-funding-accounts-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The health API from Divvy — 1 operation(s) for health.
  name: Divvy Health API
  slug: divvy-health-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The invoices API from Divvy — 7 operation(s) for invoices.
  name: Divvy Invoices API
  slug: divvy-invoices-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The mfa API from Divvy — 6 operation(s) for mfa.
  name: Divvy Mfa API
  slug: divvy-mfa-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The network API from Divvy — 5 operation(s) for network.
  name: Divvy Network API
  slug: divvy-network-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The organization-users API from Divvy — 4 operation(s) for organization-users.
  name: Divvy Organization Users API
  slug: divvy-organization-users-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The organizations API from Divvy — 5 operation(s) for organizations.
  name: Divvy Organizations API
  slug: divvy-organizations-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The partner API from Divvy — 11 operation(s) for partner.
  name: Divvy Partner API
  slug: divvy-partner-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The payment-terms API from Divvy — 2 operation(s) for payment-terms.
  name: Divvy Payment Terms API
  slug: divvy-payment-terms-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The payments API from Divvy — 10 operation(s) for payments.
  name: Divvy Payments API
  slug: divvy-payments-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The receivable-payments API from Divvy — 2 operation(s) for receivable-payments.
  name: Divvy Receivable Payments API
  slug: divvy-receivable-payments-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The recurring-invoices API from Divvy — 4 operation(s) for recurring-invoices.
  name: Divvy Recurring Invoices API
  slug: divvy-recurring-invoices-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The recurringbills API from Divvy — 4 operation(s) for recurringbills.
  name: Divvy Recurringbills API
  slug: divvy-recurringbills-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The reimbursements API from Divvy — 6 operation(s) for reimbursements.
  name: Divvy Reimbursements API
  slug: divvy-reimbursements-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The reports API from Divvy — 1 operation(s) for reports.
  name: Divvy Reports API
  slug: divvy-reports-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The risk-verifications API from Divvy — 2 operation(s) for risk-verifications.
  name: Divvy Risk Verifications API
  slug: divvy-risk-verifications-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The roles API from Divvy — 2 operation(s) for roles.
  name: Divvy Roles API
  slug: divvy-roles-api
- baseURL: https://gateway.stage.bill.com/connect-events
  baseurl_source: spec
  description: The subscriptions API from Divvy — 4 operation(s) for subscriptions.
  name: Divvy Subscriptions API
  slug: divvy-subscriptions-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The transactions API from Divvy — 8 operation(s) for transactions.
  name: Divvy Transactions API
  slug: divvy-transactions-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The users API from Divvy — 3 operation(s) for users.
  name: Divvy Users API
  slug: divvy-users-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The vendor-credits API from Divvy — 5 operation(s) for vendor-credits.
  name: Divvy Vendor Credits API
  slug: divvy-vendor-credits-api
- baseURL: https://gateway.stage.bill.com/connect
  baseurl_source: spec
  description: The vendors API from Divvy — 8 operation(s) for vendors.
  name: Divvy Vendors API
  slug: divvy-vendors-api
artifact_total: 54
asyncapis:
- description: ''
  name: Divvy Spend Expense Webhooks
  slug: divvy-spend-expense-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/agentic-access/divvy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/divvy-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/rules/divvy-rules.yml
  title: ''
  type: Spectral
  url: rules/divvy-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/json-ld/divvy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/divvy-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/vocabulary/divvy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/divvy-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/conventions/divvy-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/divvy-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/errors/divvy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/divvy-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/conformance/divvy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/divvy-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/a2a/divvy-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/divvy-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/well-known/divvy-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/divvy-apis-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/well-known/divvy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/divvy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/hosts/divvy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/divvy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/vendors/divvy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/divvy-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bill.com/product/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.bill.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.bill.com/leadership
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bill/
- group: company
  title: ''
  type: Website
  url: https://getdivvy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bill.com/docs/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bill.com/docs/spend-expense-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bill.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bill.com/docs/bill-v3-api-get-started
- group: operate
  title: ''
  type: Support
  url: https://help.bill.com/direct/s/
- group: company
  title: ''
  type: Blog
  url: https://www.bill.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bill.com/product/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bill.com/signup
- group: start
  title: ''
  type: Login
  url: https://login.us.bill.com/neo/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bill.com/legal/spend-expense-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bill.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://developer.bill.com/docs/bill-v3-api-postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.bill.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/changelog/divvy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/divvy-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/authentication/divvy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/divvy-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/rate-limits/divvy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/divvy-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/asyncapi/divvy-spend-expense-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/divvy-spend-expense-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/conventions/divvy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/divvy-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/errors/divvy-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/divvy-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/lifecycle/divvy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/divvy-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/lifecycle/divvy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/divvy-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/sandbox/divvy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/divvy-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/data-model/divvy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/divvy-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/security/divvy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divvy-domain-security.yml
created: '2026-07-17'
description: Divvy is a corporate card and spend-management platform (free software plus business credit cards) that was acquired by BILL and now operates as BILL Spend & Expense; getdivvy.com redirects to bill.com. Its API for budgets, users, virtual cards, transactions, and reimbursements is delivered through the BILL developer platform (developer.bill.com) as part of the BILL v3 API, authenticated with a Spend & Expense API token, with a documented webhook event surface, dated changelog, sandbox environment, and per-token rate limits. This profile was surfaced as an Insight Partners portfolio company and has been enriched from BILL's public developer surface.
image: https://www.bill.com/product/spend-and-expense
json_schemas:
- name: BudgetCreateDto
  property_count: 21
  slug: divvy-budget-create-dto
- name: EventDto
  property_count: 7
  slug: divvy-event-dto
- name: InvoiceReplaceRequestDto
  property_count: 14
  slug: divvy-invoice-replace-request-dto
- name: InvoiceResponseDto
  property_count: 28
  slug: divvy-invoice-response-dto
- name: PaymentRequestDto
  property_count: 12
  slug: divvy-payment-request-dto
- name: PaymentResponseDto
  property_count: 28
  slug: divvy-payment-response-dto
- name: SendTestEventRequestDto
  property_count: 12
  slug: divvy-send-test-event-request-dto
- name: SubscriptionRequestDto
  property_count: 4
  slug: divvy-subscription-request-dto
- name: SubscriptionResponseDto
  property_count: 8
  slug: divvy-subscription-response-dto
- name: SubscriptionUpdateRequestDto
  property_count: 4
  slug: divvy-subscription-update-request-dto
- name: SubscriptionWithSecurityKeyResponseDto
  property_count: 9
  slug: divvy-subscription-with-security-key-response-dto
- name: TransactionResponseDto
  property_count: 54
  slug: divvy-transaction-response-dto
jsonld:
- class_count: 120
  name: Divvy Context
  property_count: 149
  slug: divvy-context
layout: provider
modified: '2026-07-18'
name: Divvy
nav: Providers
network: true
overview: 'Divvy publishes 35 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachments API, Authentication API, Bill Approvals API, and 32 more. Tagged areas include Company, Payments, Spend Management, Corporate Cards, and Expense Management.


  The Divvy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Divvy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 5
  name: Divvy Rate Limits
  slug: divvy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Divvy API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: divvy-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.8
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 45.2
    discoverability: 51.8
    operational_transparency: 65.8
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 35
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/divvy/refs/heads/main/screenshots/divvy-2026-07-25T212135.png
security:
- kind: authentication
  name: Divvy Authentication
  slug: divvy-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Divvy Domain Security
  slug: divvy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: divvy
tags:
- Company
- Payments
- Spend Management
- Corporate Cards
- Expense Management
- Fintech
- Bills
website: https://getdivvy.com/
---
