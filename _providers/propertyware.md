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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 86
  human_in_the_loop: 0
  name: Propertyware Agentic Access
  operation_count: 162
  slug: propertyware-agentic-access
  summary_line: 162 operations · 86 acting
api_count: 1
apis:
- description: Resources providing access to accounting data such as general ledger accounts and financial transactions.
  name: Propertyware Accounting API
  slug: propertyware-accounting-api
- description: Resources providing access to bills and bill payments.
  name: Propertyware Bills API
  slug: propertyware-bills-api
- description: Resources providing access to buildings.
  name: Propertyware Buildings API
  slug: propertyware-buildings-api
- description: Resources providing access to contacts.
  name: Propertyware Contacts API
  slug: propertyware-contacts-api
- description: Resources providing access to custom fields definitions.
  name: Propertyware Custom field definitions API
  slug: propertyware-custom-field-definitions-api
- description: Resources providing access to documents.
  name: Propertyware Documents API
  slug: propertyware-documents-api
- description: API health check resources.
  name: Propertyware Health check API
  slug: propertyware-health-check-api
- description: Resources providing access to inspections.
  name: Propertyware Inspections API
  slug: propertyware-inspections-api
- description: Resources providing access to rental property leases.
  name: Propertyware Leases API
  slug: propertyware-leases-api
- description: Resources providing access to portfolios.
  name: Propertyware Portfolios API
  slug: propertyware-portfolios-api
- description: Resources providing access to prospects.
  name: Propertyware Prospects API
  slug: propertyware-prospects-api
- description: Resources providing access to units.
  name: Propertyware Units API
  slug: propertyware-units-api
- description: Resources providing access to vendors.
  name: Propertyware Vendors API
  slug: propertyware-vendors-api
- description: Resources providing access to work orders.
  name: Propertyware Work orders API
  slug: propertyware-work-orders-api
artifact_total: 284
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open API, powered by Propertyware Accounting API
  slug: open-propertyware-accounting-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Bills API
  slug: open-propertyware-bills-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Buildings API
  slug: open-propertyware-buildings-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Contacts API
  slug: open-propertyware-contacts-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Custom field definitions API
  slug: open-propertyware-custom-field-definitions-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Documents API
  slug: open-propertyware-documents-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Health check API
  slug: open-propertyware-health-check-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Inspections API
  slug: open-propertyware-inspections-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Leases API
  slug: open-propertyware-leases-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Portfolios API
  slug: open-propertyware-portfolios-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Prospects API
  slug: open-propertyware-prospects-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Units API
  slug: open-propertyware-units-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Vendors API
  slug: open-propertyware-vendors-api
- collection_type: open
  name: Open API, powered by Propertyware Accounting Work orders API
  slug: open-propertyware-work-orders-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/propertyware-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propertyware-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propertyware-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/propertyware-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.propertyware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.propertyware.com/apidocs/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.propertyware.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.propertyware.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propertyware.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propertyware
- group: other
  title: ''
  type: X
  url: https://twitter.com/propertyware
- group: commercial
  title: ''
  type: Plans
  url: plans/propertyware-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/propertyware-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/propertyware-finops.yml
created: '2026-06-13'
description: Propertyware is a cloud-based property management software platform offering a REST API for managing properties, units, leases, tenants, work orders, maintenance requests, financial transactions, and owner reports. The open API enables two-way data exchange with third-party systems and supports custom integrations for single-family and low-density rental portfolios.
examples:
- key_count: 36
  name: Account
  slug: account
- key_count: 6
  name: Address
  slug: address
- key_count: 12
  name: Adjustment
  slug: adjustment
- key_count: 4
  name: Amenity
  slug: amenity
- key_count: 2
  name: Auto Charge
  slug: auto-charge
- key_count: 15
  name: Auto Journal Entry
  slug: auto-journal-entry
- key_count: 14
  name: Auto Payment
  slug: auto-payment
- key_count: 9
  name: Bank Deposit
  slug: bank-deposit
- key_count: 18
  name: Bank
  slug: bank
- key_count: 12
  name: Basic Vendor
  slug: basic-vendor
- key_count: 4
  name: Bill Paid
  slug: bill-paid
- key_count: 2
  name: Bill Pay
  slug: bill-pay
- key_count: 16
  name: Bill Payment
  slug: bill-payment
- key_count: 13
  name: Bill Split
  slug: bill-split
- key_count: 20
  name: Bill
  slug: bill
- key_count: 56
  name: Building
  slug: building
- key_count: 5
  name: Campaign Source
  slug: campaign-source
- key_count: 22
  name: Campaign
  slug: campaign
- key_count: 16
  name: Charge Tx
  slug: charge-tx
- key_count: 15
  name: Charge
  slug: charge
- key_count: 7
  name: Check Split
  slug: check-split
- key_count: 16
  name: Check
  slug: check
- key_count: 5
  name: Close Work Order
  slug: close-work-order
- key_count: 0
  name: 'Collection Long '
  slug: collection-long-
- key_count: 6
  name: Comment
  slug: comment
- key_count: 2
  name: Contact Category
  slug: contact-category
- key_count: 30
  name: Contact Extension
  slug: contact-extension
- key_count: 29
  name: Contact
  slug: contact
- key_count: 10
  name: Conversation
  slug: conversation
- key_count: 1
  name: Credit Card Account
  slug: credit-card-account
- key_count: 13
  name: Credit Memo
  slug: credit-memo
- key_count: 7
  name: Current Asset
  slug: current-asset
- key_count: 8
  name: Current Liability
  slug: current-liability
- key_count: 5
  name: Custom Field Definition
  slug: custom-field-definition
- key_count: 2
  name: Custom Field Set
  slug: custom-field-set
- key_count: 4
  name: Custom Field
  slug: custom-field
- key_count: 12
  name: Discount
  slug: discount
- key_count: 12
  name: Document
  slug: document
- key_count: 9
  name: Entry
  slug: entry
- key_count: 8
  name: Equity
  slug: equity
- key_count: 3
  name: Error Response
  slug: error-response
- key_count: 6
  name: Expense Recovery Charge
  slug: expense-recovery-charge
- key_count: 8
  name: Expense
  slug: expense
- key_count: 12
  name: G L Item
  slug: g-l-item
- key_count: 9
  name: Income
  slug: income
- key_count: 3
  name: Inspection Area
  slug: inspection-area
- key_count: 4
  name: Inspection Item
  slug: inspection-item
- key_count: 19
  name: Inspection
  slug: inspection
- key_count: 4
  name: Journal Entry Split Response
  slug: journal-entry-split-response
- key_count: 4
  name: Journal Entry Split
  slug: journal-entry-split
- key_count: 10
  name: Journal Entry
  slug: journal-entry
- key_count: 5
  name: Late Fee Rule
  slug: late-fee-rule
- key_count: 3
  name: Lease Clause
  slug: lease-clause
- key_count: 11
  name: Lease Contact
  slug: lease-contact
- key_count: 6
  name: Lease Status
  slug: lease-status
- key_count: 34
  name: Lease
  slug: lease
- key_count: 7
  name: Line Item
  slug: line-item
- key_count: 7
  name: Management Fee
  slug: management-fee
- key_count: 6
  name: Management Settings
  slug: management-settings
- key_count: 24
  name: Marketing
  slug: marketing
- key_count: 5
  name: Non Current Asset
  slug: non-current-asset
- key_count: 8
  name: Non Current Liability
  slug: non-current-liability
- key_count: 8
  name: Non Operating Expense
  slug: non-operating-expense
- key_count: 8
  name: Non Operating Inome
  slug: non-operating-inome
- key_count: 9
  name: Note
  slug: note
- key_count: 15
  name: Owner Contribution
  slug: owner-contribution
- key_count: 15
  name: Owner Draw
  slug: owner-draw
- key_count: 11
  name: Owner
  slug: owner
- key_count: 12
  name: Payment Charge
  slug: payment-charge
- key_count: 19
  name: Payment
  slug: payment
- key_count: 23
  name: Portfolio
  slug: portfolio
- key_count: 5
  name: Property Manager
  slug: property-manager
- key_count: 8
  name: Prospect Contact
  slug: prospect-contact
- key_count: 4
  name: Prospect Status
  slug: prospect-status
- key_count: 51
  name: Prospect
  slug: prospect
- key_count: 3
  name: R E S T A P I Bulk Error Response
  slug: r-e-s-t-a-p-i-bulk-error-response
- key_count: 1
  name: R E S T A P I Bulk Success Response
  slug: r-e-s-t-a-p-i-bulk-success-response
- key_count: 2
  name: R E S T A P I Error
  slug: r-e-s-t-a-p-i-error
- key_count: 14
  name: Refund
  slug: refund
- key_count: 2
  name: Response Entity
  slug: response-entity
- key_count: 18
  name: Save Account
  slug: save-account
- key_count: 6
  name: Save Address
  slug: save-address
- key_count: 5
  name: Save Adjustment
  slug: save-adjustment
- key_count: 8
  name: Save Auto Charge
  slug: save-auto-charge
- key_count: 4
  name: Save Bank Deposit
  slug: save-bank-deposit
- key_count: 7
  name: Save Bill Payment
  slug: save-bill-payment
- key_count: 10
  name: Save Bill Split
  slug: save-bill-split
- key_count: 12
  name: Save Bill
  slug: save-bill
- key_count: 47
  name: Save Building
  slug: save-building
- key_count: 6
  name: Save Charge
  slug: save-charge
- key_count: 7
  name: Save Check Split
  slug: save-check-split
- key_count: 7
  name: Save Check
  slug: save-check
- key_count: 1
  name: Save Comment
  slug: save-comment
- key_count: 23
  name: Save Contact
  slug: save-contact
- key_count: 2
  name: Save Conversation
  slug: save-conversation
- key_count: 6
  name: Save Credit
  slug: save-credit
- key_count: 2
  name: Save Custom Field
  slug: save-custom-field
- key_count: 6
  name: Save Discount
  slug: save-discount
- key_count: 3
  name: Save Journal Entry Split
  slug: save-journal-entry-split
- key_count: 5
  name: Save Lease Journal Entry
  slug: save-lease-journal-entry
- key_count: 25
  name: Save Lease
  slug: save-lease
- key_count: 9
  name: Save Owner Contribution
  slug: save-owner-contribution
- key_count: 9
  name: Save Owner Draw
  slug: save-owner-draw
- key_count: 10
  name: Save Owner
  slug: save-owner
- key_count: 9
  name: Save Payment
  slug: save-payment
- key_count: 14
  name: Save Portfolio
  slug: save-portfolio
- key_count: 10
  name: Save Prospect Contact
  slug: save-prospect-contact
- key_count: 30
  name: Save Prospect
  slug: save-prospect
- key_count: 9
  name: Save Refund
  slug: save-refund
- key_count: 22
  name: Save Unit
  slug: save-unit
- key_count: 30
  name: Save Vendor
  slug: save-vendor
- key_count: 7
  name: Save Work Order Task
  slug: save-work-order-task
- key_count: 21
  name: Save Work Order
  slug: save-work-order
- key_count: 9
  name: Split Paid
  slug: split-paid
- key_count: 2
  name: Split Pay
  slug: split-pay
- key_count: 13
  name: Task
  slug: task
- key_count: 8
  name: Time Card Entry
  slug: time-card-entry
- key_count: 40
  name: Unit
  slug: unit
- key_count: 45
  name: Update Building
  slug: update-building
- key_count: 4
  name: Update Document
  slug: update-document
- key_count: 5
  name: Update Lease Journal Entry
  slug: update-lease-journal-entry
- key_count: 39
  name: Vendor
  slug: vendor
- key_count: 39
  name: Work Order
  slug: work-order
finops:
- name: Propertyware Finops
  service_category: ''
  slug: propertyware-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/propertyware.png
json_schemas:
- name: Account
  property_count: 36
  slug: account
- name: Address
  property_count: 6
  slug: address
- name: Adjustment
  property_count: 12
  slug: adjustment
- name: Amenity
  property_count: 4
  slug: amenity
- name: AutoCharge
  property_count: 2
  slug: auto-charge
- name: AutoJournalEntry
  property_count: 15
  slug: auto-journal-entry
- name: AutoPayment
  property_count: 14
  slug: auto-payment
- name: BankDeposit
  property_count: 9
  slug: bank-deposit
- name: Bank
  property_count: 18
  slug: bank
- name: BasicVendor
  property_count: 12
  slug: basic-vendor
- name: BillPaid
  property_count: 4
  slug: bill-paid
- name: BillPay
  property_count: 2
  slug: bill-pay
- name: BillPayment
  property_count: 16
  slug: bill-payment
- name: BillSplit
  property_count: 13
  slug: bill-split
- name: Bill
  property_count: 20
  slug: bill
- name: Building
  property_count: 56
  slug: building
- name: CampaignSource
  property_count: 5
  slug: campaign-source
- name: Campaign
  property_count: 22
  slug: campaign
- name: ChargeTx
  property_count: 16
  slug: charge-tx
- name: Charge
  property_count: 15
  slug: charge
- name: CheckSplit
  property_count: 7
  slug: check-split
- name: Check
  property_count: 16
  slug: check
- name: CloseWorkOrder
  property_count: 5
  slug: close-work-order
- name: Collection_long_
  property_count: 0
  slug: collection-long-
- name: Comment
  property_count: 6
  slug: comment
- name: ContactCategory
  property_count: 2
  slug: contact-category
- name: ContactExtension
  property_count: 30
  slug: contact-extension
- name: Contact
  property_count: 29
  slug: contact
- name: Conversation
  property_count: 10
  slug: conversation
- name: CreditCardAccount
  property_count: 1
  slug: credit-card-account
- name: CreditMemo
  property_count: 13
  slug: credit-memo
- name: CurrentAsset
  property_count: 7
  slug: current-asset
- name: CurrentLiability
  property_count: 8
  slug: current-liability
- name: CustomFieldDefinition
  property_count: 5
  slug: custom-field-definition
- name: CustomFieldSet
  property_count: 2
  slug: custom-field-set
- name: CustomField
  property_count: 4
  slug: custom-field
- name: Discount
  property_count: 12
  slug: discount
- name: Document
  property_count: 12
  slug: document
- name: Entry
  property_count: 9
  slug: entry
- name: Equity
  property_count: 8
  slug: equity
- name: ErrorResponse
  property_count: 3
  slug: error-response
- name: ExpenseRecoveryCharge
  property_count: 6
  slug: expense-recovery-charge
- name: Expense
  property_count: 8
  slug: expense
- name: GLItem
  property_count: 12
  slug: g-l-item
- name: Income
  property_count: 9
  slug: income
- name: InspectionArea
  property_count: 3
  slug: inspection-area
- name: InspectionItem
  property_count: 4
  slug: inspection-item
- name: Inspection
  property_count: 19
  slug: inspection
- name: JournalEntrySplitResponse
  property_count: 4
  slug: journal-entry-split-response
- name: JournalEntrySplit
  property_count: 4
  slug: journal-entry-split
- name: JournalEntry
  property_count: 10
  slug: journal-entry
- name: LateFeeRule
  property_count: 5
  slug: late-fee-rule
- name: LeaseClause
  property_count: 3
  slug: lease-clause
- name: LeaseContact
  property_count: 11
  slug: lease-contact
- name: LeaseStatus
  property_count: 6
  slug: lease-status
- name: Lease
  property_count: 34
  slug: lease
- name: LineItem
  property_count: 7
  slug: line-item
- name: ManagementFee
  property_count: 7
  slug: management-fee
- name: ManagementSettings
  property_count: 6
  slug: management-settings
- name: Marketing
  property_count: 24
  slug: marketing
- name: NonCurrentAsset
  property_count: 5
  slug: non-current-asset
- name: NonCurrentLiability
  property_count: 8
  slug: non-current-liability
- name: NonOperatingExpense
  property_count: 8
  slug: non-operating-expense
- name: NonOperatingInome
  property_count: 8
  slug: non-operating-inome
- name: Note
  property_count: 9
  slug: note
- name: OwnerContribution
  property_count: 15
  slug: owner-contribution
- name: OwnerDraw
  property_count: 15
  slug: owner-draw
- name: Owner
  property_count: 11
  slug: owner
- name: PaymentCharge
  property_count: 12
  slug: payment-charge
- name: Payment
  property_count: 19
  slug: payment
- name: Portfolio
  property_count: 23
  slug: portfolio
- name: PropertyManager
  property_count: 5
  slug: property-manager
- name: ProspectContact
  property_count: 8
  slug: prospect-contact
- name: ProspectStatus
  property_count: 4
  slug: prospect-status
- name: Prospect
  property_count: 51
  slug: prospect
- name: RESTAPIBulkErrorResponse
  property_count: 3
  slug: r-e-s-t-a-p-i-bulk-error-response
- name: RESTAPIBulkSuccessResponse
  property_count: 1
  slug: r-e-s-t-a-p-i-bulk-success-response
- name: RESTAPIError
  property_count: 2
  slug: r-e-s-t-a-p-i-error
- name: Refund
  property_count: 14
  slug: refund
- name: ResponseEntity
  property_count: 2
  slug: response-entity
- name: SaveAccount
  property_count: 18
  slug: save-account
- name: SaveAddress
  property_count: 6
  slug: save-address
- name: SaveAdjustment
  property_count: 5
  slug: save-adjustment
- name: SaveAutoCharge
  property_count: 8
  slug: save-auto-charge
- name: SaveBankDeposit
  property_count: 4
  slug: save-bank-deposit
- name: SaveBillPayment
  property_count: 7
  slug: save-bill-payment
- name: SaveBillSplit
  property_count: 10
  slug: save-bill-split
- name: SaveBill
  property_count: 12
  slug: save-bill
- name: SaveBuilding
  property_count: 47
  slug: save-building
- name: SaveCharge
  property_count: 6
  slug: save-charge
- name: SaveCheckSplit
  property_count: 7
  slug: save-check-split
- name: SaveCheck
  property_count: 7
  slug: save-check
- name: SaveComment
  property_count: 1
  slug: save-comment
- name: SaveContact
  property_count: 23
  slug: save-contact
- name: SaveConversation
  property_count: 2
  slug: save-conversation
- name: SaveCredit
  property_count: 6
  slug: save-credit
- name: SaveCustomField
  property_count: 2
  slug: save-custom-field
- name: SaveDiscount
  property_count: 6
  slug: save-discount
- name: SaveJournalEntrySplit
  property_count: 3
  slug: save-journal-entry-split
- name: SaveLeaseJournalEntry
  property_count: 5
  slug: save-lease-journal-entry
- name: SaveLease
  property_count: 25
  slug: save-lease
- name: SaveOwnerContribution
  property_count: 9
  slug: save-owner-contribution
- name: SaveOwnerDraw
  property_count: 9
  slug: save-owner-draw
- name: SaveOwner
  property_count: 10
  slug: save-owner
- name: SavePayment
  property_count: 9
  slug: save-payment
- name: SavePortfolio
  property_count: 14
  slug: save-portfolio
- name: SaveProspectContact
  property_count: 10
  slug: save-prospect-contact
- name: SaveProspect
  property_count: 30
  slug: save-prospect
- name: SaveRefund
  property_count: 9
  slug: save-refund
- name: SaveUnit
  property_count: 22
  slug: save-unit
- name: SaveVendor
  property_count: 30
  slug: save-vendor
- name: SaveWorkOrderTask
  property_count: 7
  slug: save-work-order-task
- name: SaveWorkOrder
  property_count: 21
  slug: save-work-order
- name: SplitPaid
  property_count: 9
  slug: split-paid
- name: SplitPay
  property_count: 2
  slug: split-pay
- name: Task
  property_count: 13
  slug: task
- name: TimeCardEntry
  property_count: 8
  slug: time-card-entry
- name: Unit
  property_count: 40
  slug: unit
- name: UpdateBuilding
  property_count: 45
  slug: update-building
- name: UpdateDocument
  property_count: 4
  slug: update-document
- name: UpdateLeaseJournalEntry
  property_count: 5
  slug: update-lease-journal-entry
- name: Vendor
  property_count: 39
  slug: vendor
- name: WorkOrder
  property_count: 39
  slug: work-order
jsonld:
- class_count: 0
  name: Propertyware Context
  property_count: 124
  slug: propertyware-context
- class_count: 0
  name: Propertyware Graph Context
  property_count: 0
  slug: propertyware-graph
layout: provider
modified: '2026-06-13'
name: Propertyware
nav: Providers
network: true
overview: 'Propertyware publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Bills API, Buildings API, and 11 more. Tagged areas include Property Management, Real-Estate, Rental Properties, Single-Family Rentals, and Leases.


  The Propertyware catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Propertyware''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Propertyware Plans Pricing
  plan_count: 3
  slug: propertyware-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Propertyware Rate Limits
  slug: propertyware-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Propertyware API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: propertyware-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 65.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propertyware/refs/heads/main/screenshots/propertyware-2026-06-20T192210.png
security:
- kind: authentication
  name: Propertyware Authentication
  slug: propertyware-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Propertyware Domain Security
  slug: propertyware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: propertyware
tags:
- Property Management
- Real-Estate
- Rental Properties
- Single-Family Rentals
- Leases
- Tenants
- Maintenance
- Work Orders
- Financial Transactions
- Owner Reports
website: https://www.propertyware.com/
---
