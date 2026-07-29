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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Sumup Agentic Access
  operation_count: 39
  slug: sumup-agentic-access
  summary_line: 39 operations · 19 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Checkouts represent online payment sessions that you create before attempting to charge a payer. A checkout captures the payment intent, such as the amount, currency, merchant, and optional customer o
  name: SumUp Checkouts API
  slug: sumup-checkouts-api
- description: 'Allow your regular customers to save their information with the Customers model. This will prevent re-entering payment instrument information for recurring payments on your platform. Depending on the '
  name: SumUp Customers API
  slug: sumup-customers-api
- description: Endpoints to manage account members. Members are users that have membership within merchant accounts.
  name: SumUp Members API
  slug: sumup-members-api
- description: Endpoints to manage user's memberships. Memberships are used to connect the user to merchant accounts and to grant them access to the merchant's resources via roles.
  name: SumUp Memberships API
  slug: sumup-memberships-api
- description: Merchant account represents a single business entity at SumUp.
  name: SumUp Merchants API
  slug: sumup-merchants-api
- description: The Payouts model will allow you to track funds you’ve received from SumUp. You can receive a detailed payouts list with information like dates, fees, references and statuses, using the `List payouts`
  name: SumUp Payouts API
  slug: sumup-payouts-api
- description: A reader represents a device that accepts payments. You can use the SumUp Solo to accept in-person payments.
  name: SumUp Readers API
  slug: sumup-readers-api
- description: The Receipts model obtains receipt-like details for specific transactions.
  name: SumUp Receipts API
  slug: sumup-receipts-api
- description: Endpoints to manage custom roles. Custom roles allow you to tailor roles from individual permissions to match your needs. Once created, you can assign your custom roles to your merchant account member
  name: SumUp Roles API
  slug: sumup-roles-api
- description: Transactions represent completed or attempted payment operations processed for a merchant account. A transaction contains the core payment result, such as the amount, currency, payment method, creatio
  name: SumUp Transactions API
  slug: sumup-transactions-api
artifact_total: 131
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sumup-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sumup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sumup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sumup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sumup-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://sumup.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sumup.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sumup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sumup
- group: company
  title: ''
  type: Blog
  url: https://medium.com/sumup-engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://sumup.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sumup.com/
- group: other
  title: ''
  type: X
  url: https://x.com/SumUp
- group: commercial
  title: ''
  type: Plans
  url: plans/sumup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sumup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sumup-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.sumup.com/changelog
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sumup/sumup-openapi
created: '2026-06-13'
description: European mobile payment and POS platform with REST APIs for creating checkout links, managing card readers, processing payments, tracking transactions, and accessing payout data. SumUp serves over 4 million merchants in 37 markets with built-in fraud protection, sandbox environments for testing, and SDKs for multiple programming languages.
examples:
- key_count: 11
  name: Createapplepaysession Response 200
  slug: createapplepaysession-response-200
- key_count: 7
  name: Createcheckout Request
  slug: createcheckout-request
- key_count: 14
  name: Createcheckout Response 201
  slug: createcheckout-response-201
- key_count: 6
  name: Createreader Response 201
  slug: createreader-response-201
- key_count: 12
  name: Deactivatecheckout Response 200
  slug: deactivatecheckout-response-200
- key_count: 10
  name: Getcheckout Response 200
  slug: getcheckout-response-200
- key_count: 1
  name: Getpaymentmethods Response 200
  slug: getpaymentmethods-response-200
- key_count: 3
  name: Getreceipt Response 200
  slug: getreceipt-response-200
- key_count: 13
  name: Gettransactionv2.1 Response 200
  slug: gettransactionv2.1-response-200
- key_count: 2
  name: Listtransactionsv2.1 Response 200
  slug: listtransactionsv2.1-response-200
- key_count: 4
  name: Processcheckout Request
  slug: processcheckout-request
- key_count: 15
  name: Processcheckout Response 200
  slug: processcheckout-response-200
- key_count: 1
  name: Refundtransaction Request
  slug: refundtransaction-request
finops:
- name: Sumup Finops
  service_category: ''
  slug: sumup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sumup.png
json_schemas:
- name: Address
  property_count: 17
  slug: address
- name: Address Legacy
  property_count: 6
  slug: addresslegacy
- name: Attributes
  property_count: 0
  slug: attributes
- name: BadRequest
  property_count: 1
  slug: badrequest
- name: BasePerson
  property_count: 16
  slug: baseperson
- name: Branding
  property_count: 8
  slug: branding
- name: BusinessProfile
  property_count: 7
  slug: businessprofile
- name: Card
  property_count: 7
  slug: card
- name: Card Response
  property_count: 2
  slug: cardresponse
- name: Card Type
  property_count: 0
  slug: cardtype
- name: ChangeStatus
  property_count: 0
  slug: changestatus
- name: Checkout
  property_count: 14
  slug: checkout
- name: Checkout Accepted
  property_count: 1
  slug: checkoutaccepted
- name: Checkout Create Request
  property_count: 11
  slug: checkoutcreaterequest
- name: Checkout Success
  property_count: 0
  slug: checkoutsuccess
- name: ClassicMerchantIdentifiers
  property_count: 1
  slug: classicmerchantidentifiers
- name: Company
  property_count: 9
  slug: company
- name: CompanyIdentifier
  property_count: 2
  slug: companyidentifier
- name: CompanyIdentifiers
  property_count: 0
  slug: companyidentifiers
- name: CountryCode
  property_count: 0
  slug: countrycode
- name: CreateReaderCheckoutError
  property_count: 1
  slug: createreadercheckouterror
- name: CreateReaderCheckoutRequest
  property_count: 9
  slug: createreadercheckoutrequest
- name: CreateReaderCheckoutResponse
  property_count: 1
  slug: createreadercheckoutresponse
- name: CreateReaderCheckoutUnprocessableEntity
  property_count: 1
  slug: createreadercheckoutunprocessableentity
- name: CreateReaderTerminateError
  property_count: 1
  slug: createreaderterminateerror
- name: CreateReaderTerminateUnprocessableEntity
  property_count: 1
  slug: createreaderterminateunprocessableentity
- name: Currency
  property_count: 0
  slug: currency
- name: Customer
  property_count: 2
  slug: customer
- name: Details Error
  property_count: 4
  slug: detailserror
- name: Device
  property_count: 5
  slug: device
- name: ELV Card Account
  property_count: 4
  slug: elvcardaccount
- name: Entry Mode
  property_count: 0
  slug: entrymode
- name: Error
  property_count: 2
  slug: error
- name: Error Extended
  property_count: 0
  slug: errorextended
- name: Error Forbidden
  property_count: 3
  slug: errorforbidden
- name: Event
  property_count: 10
  slug: event
- name: Event ID
  property_count: 0
  slug: eventid
- name: Event Status
  property_count: 0
  slug: eventstatus
- name: Event Type
  property_count: 0
  slug: eventtype
- name: Financial Payout
  property_count: 9
  slug: financialpayout
- name: Financial Payouts
  property_count: 0
  slug: financialpayouts
- name: Horizontal Accuracy
  property_count: 0
  slug: horizontalaccuracy
- name: Hosted Checkout
  property_count: 1
  slug: hostedcheckout
- name: Invite
  property_count: 2
  slug: invite
- name: Latitude
  property_count: 0
  slug: lat
- name: LegalType
  property_count: 0
  slug: legaltype
- name: Link
  property_count: 5
  slug: link
- name: ListPersonsResponseBody
  property_count: 1
  slug: listpersonsresponsebody
- name: Longitude
  property_count: 0
  slug: lon
- name: Mandate Payload
  property_count: 3
  slug: mandatepayload
- name: Mandate Response
  property_count: 3
  slug: mandateresponse
- name: Member
  property_count: 10
  slug: member
- name: Membership
  property_count: 12
  slug: membership
- name: Resource
  property_count: 7
  slug: membershipresource
- name: MembershipStatus
  property_count: 0
  slug: membershipstatus
- name: MembershipUser
  property_count: 9
  slug: membershipuser
- name: MembershipUserClassic
  property_count: 1
  slug: membershipuserclassic
- name: Merchant
  property_count: 0
  slug: merchant
- name: Meta
  property_count: 0
  slug: meta
- name: Metadata
  property_count: 0
  slug: metadata
- name: NotFound
  property_count: 1
  slug: notfound
- name: Ownership
  property_count: 1
  slug: ownership
- name: Payment Instrument Response
  property_count: 6
  slug: paymentinstrumentresponse
- name: Payment Type
  property_count: 0
  slug: paymenttype
- name: Person
  property_count: 0
  slug: person
- name: Personal Details
  property_count: 7
  slug: personaldetails
- name: PersonalIdentifier
  property_count: 2
  slug: personalidentifier
- name: PhoneNumber
  property_count: 0
  slug: phonenumber
- name: Problem
  property_count: 5
  slug: problem
- name: Process Checkout
  property_count: 9
  slug: processcheckout
- name: Product
  property_count: 10
  slug: product
- name: Reader
  property_count: 8
  slug: reader
- name: ReaderCheckoutStatusChange
  property_count: 4
  slug: readercheckoutstatuschange
- name: ReaderDevice
  property_count: 2
  slug: readerdevice
- name: ReaderID
  property_count: 0
  slug: readerid
- name: ReaderName
  property_count: 0
  slug: readername
- name: ReaderPairingCode
  property_count: 0
  slug: readerpairingcode
- name: ReaderStatus
  property_count: 0
  slug: readerstatus
- name: Receipt
  property_count: 4
  slug: receipt
- name: Receipt Card
  property_count: 2
  slug: receiptcard
- name: Receipt Event
  property_count: 7
  slug: receiptevent
- name: Receipt Merchant Data
  property_count: 2
  slug: receiptmerchantdata
- name: Receipt Reader
  property_count: 2
  slug: receiptreader
- name: Receipt Transaction
  property_count: 20
  slug: receipttransaction
- name: ResourceType
  property_count: 0
  slug: resourcetype
- name: Role
  property_count: 8
  slug: role
- name: StatusResponse
  property_count: 1
  slug: statusresponse
- name: Timestamps
  property_count: 2
  slug: timestamps
- name: Transaction Base
  property_count: 8
  slug: transactionbase
- name: Transaction Checkout Info
  property_count: 5
  slug: transactioncheckoutinfo
- name: Transaction Event
  property_count: 8
  slug: transactionevent
- name: Transaction Full
  property_count: 0
  slug: transactionfull
- name: Transaction History
  property_count: 0
  slug: transactionhistory
- name: Transaction ID
  property_count: 0
  slug: transactionid
- name: Transaction Mixin History
  property_count: 4
  slug: transactionmixinhistory
- name: Transactions History Link
  property_count: 2
  slug: transactionshistorylink
- name: Transaction Status
  property_count: 0
  slug: transactionstatus
- name: Unauthorized
  property_count: 1
  slug: unauthorized
- name: Version
  property_count: 0
  slug: version
layout: provider
modified: '2026-06-13'
name: SumUp
nav: Providers
network: true
overview: 'SumUp publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Checkouts API, Customers API, Members API, and 7 more. Tagged areas include Payments, POS, Point of Sale, Card Readers, and Checkout.


  The SumUp catalog on APIs.io includes 1 Spectral governance ruleset.


  SumUp''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 13 more developer resources.'
plans:
- name: Sumup Plans Pricing
  plan_count: 5
  slug: sumup-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Sumup Rate Limits
  slug: sumup-rate-limits
rules:
- name: SumUp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sumup-jsonschema-spectral-rules
scopes:
- name: Sumup Scopes
  scope_count: 10
  slug: sumup-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 49.9
  delta: -6.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sumup/refs/heads/main/screenshots/sumup-2026-06-20T194647.png
security:
- kind: authentication
  name: Sumup Authentication
  slug: sumup-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sumup Domain Security
  slug: sumup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sumup Vulnerability Disclosure
  slug: sumup-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sumup
tags:
- Payments
- POS
- Point of Sale
- Card Readers
- Checkout
- Fintech
- Mobile Payments
- Online Payments
website: https://sumup.com
---
