---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Payjp Agentic Access
  operation_count: 59
  slug: payjp-agentic-access
  summary_line: 59 operations · 30 acting
api_count: 1
apis:
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The 3D Secure API from PAY.JP — 4 operation(s) for 3d secure.
  name: PAY.JP 3D Secure API
  phrasing_intents:
  - id: finishChargeThreeDSecure
    intent: Finish 3D Secure authentication for a charge
    question: After the cardholder passes 3D Secure, how do I complete the charge that was waiting on it?
  - id: finishTokenThreeDSecure
    intent: Finish 3D Secure authentication for a card token
    question: Once a cardholder completes 3D Secure on a token, how do I mark the token as authenticated?
  - id: listThreeDSecureRequests
    intent: List 3D Secure requests
    question: Which standalone 3D Secure requests have I started for stored cards?
  - id: createThreeDSecureRequest
    intent: Start 3D Secure authentication for a stored card
    question: How do I run 3D Secure on a card that is already saved to a customer?
  - id: retrieveThreeDSecureRequest
    intent: Get a 3D Secure request
    question: How can I check the status of one particular 3D Secure request?
  phrasing_ops: 5
  slug: payjp-3d-secure-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Account API from PAY.JP — 1 operation(s) for account.
  name: PAY.JP Account API
  phrasing_intents:
  - id: retrieveAccount
    intent: Get my merchant account details
    question: How do I look up the PAY.JP merchant account my API key belongs to?
  phrasing_ops: 1
  slug: payjp-account-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Balances API from PAY.JP — 2 operation(s) for balances.
  name: PAY.JP Balances API
  phrasing_intents:
  - id: listBalances
    intent: List account balances
    question: What balances do I have accumulating on my account?
  - id: retrieveBalance
    intent: Get a single balance
    question: How do I look up the details of one specific balance?
  phrasing_ops: 2
  slug: payjp-balances-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Cards API from PAY.JP — 2 operation(s) for cards.
  name: PAY.JP Cards API
  phrasing_intents:
  - id: listCustomerCards
    intent: List a customer's saved cards
    question: Which cards does this customer have on file?
  - id: createCustomerCard
    intent: Add a card to a customer
    question: How do I save a new card to an existing customer using a token?
  - id: retrieveCustomerCard
    intent: Get one of a customer's cards
    question: How do I look up a specific saved card for a customer?
  - id: updateCustomerCard
    intent: Update a customer's saved card
    question: How do I change the details of a card already saved on a customer?
  - id: deleteCustomerCard
    intent: Remove a card from a customer
    question: How do I remove a saved card from a customer?
  phrasing_ops: 5
  slug: payjp-cards-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Charges API from PAY.JP — 6 operation(s) for charges.
  name: PAY.JP Charges API
  phrasing_intents:
  - id: listCharges
    intent: List charges
    question: How do I see all the payments I've charged?
  - id: createCharge
    intent: Charge a card or customer
    question: How do I charge a customer's card in yen with PAY.JP?
  - id: retrieveCharge
    intent: Get a charge
    question: How do I check the details of one charge?
  - id: updateCharge
    intent: Edit a charge's description or metadata
    question: Can I change the description on a charge after it was created?
  - id: refundCharge
    intent: Refund a charge
    question: How do I refund a payment?
  - id: captureCharge
    intent: Capture an authorized charge
    question: How do I collect the money on a charge I only authorized?
  - id: reauthCharge
    intent: Re-authorize an expiring charge
    question: My authorization hold is about to expire — can I extend it?
  - id: finishChargeThreeDSecure
    intent: Finish 3D Secure authentication for a charge
    question: After the cardholder passes 3D Secure, how do I complete the charge that was waiting on it?
  phrasing_ops: 8
  slug: payjp-charges-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Customers API from PAY.JP — 2 operation(s) for customers.
  name: PAY.JP Customers API
  phrasing_intents:
  - id: listCustomers
    intent: List customers
    question: How do I get a list of all my customers?
  - id: createCustomer
    intent: Create a customer
    question: How do I create a customer so I can charge them again later?
  - id: retrieveCustomer
    intent: Get a customer
    question: How do I look up one customer's details?
  - id: updateCustomer
    intent: Update a customer
    question: How do I change an existing customer's details?
  - id: deleteCustomer
    intent: Delete a customer
    question: How do I permanently remove a customer?
  phrasing_ops: 5
  slug: payjp-customers-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Events API from PAY.JP — 2 operation(s) for events.
  name: PAY.JP Events API
  phrasing_intents:
  - id: listEvents
    intent: List webhook events
    question: How do I see the events that were sent to my webhooks?
  - id: retrieveEvent
    intent: Get an event
    question: How do I look up one event by its id?
  phrasing_ops: 2
  slug: payjp-events-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Plans API from PAY.JP — 2 operation(s) for plans.
  name: PAY.JP Plans API
  phrasing_intents:
  - id: listPlans
    intent: List recurring plans
    question: What recurring billing plans have I set up?
  - id: createPlan
    intent: Create a recurring billing plan
    question: How do I set up a monthly plan for subscriptions?
  - id: retrievePlan
    intent: Get a plan
    question: How do I check the price and interval of one plan?
  - id: updatePlan
    intent: Update a plan
    question: Can I edit a plan after I've created it?
  - id: deletePlan
    intent: Delete a plan
    question: How do I remove a plan I no longer offer?
  phrasing_ops: 5
  slug: payjp-plans-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Platform API from PAY.JP — 4 operation(s) for platform.
  name: PAY.JP Platform API
  phrasing_intents:
  - id: listTenants
    intent: List platform tenants
    question: Which sub-merchants are registered under my platform?
  - id: createTenant
    intent: Add a sub-merchant tenant
    question: How do I onboard a new sub-merchant onto my platform?
  - id: retrieveTenant
    intent: Get a platform tenant
    question: How do I look up one sub-merchant's tenant record?
  - id: updateTenant
    intent: Update a platform tenant
    question: How do I change a sub-merchant's tenant details?
  - id: deleteTenant
    intent: Remove a platform tenant
    question: How do I remove a sub-merchant from my platform?
  - id: listTenantTransfers
    intent: List payouts to tenants
    question: How do I see the payouts made to my sub-merchants?
  - id: retrieveTenantTransfer
    intent: Get a tenant transfer
    question: How do I check the details of one payout to a sub-merchant?
  phrasing_ops: 7
  slug: payjp-platform-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Statements API from PAY.JP — 3 operation(s) for statements.
  name: PAY.JP Statements API
  phrasing_intents:
  - id: listStatements
    intent: List transaction statements
    question: How do I see my transaction statements?
  - id: retrieveStatement
    intent: Get a transaction statement
    question: How do I view the line items in one statement?
  - id: createStatementDownloadUrl
    intent: Get a CSV download link for a statement
    question: Can I download a statement as a CSV file?
  phrasing_ops: 3
  slug: payjp-statements-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Subscriptions API from PAY.JP — 5 operation(s) for subscriptions.
  name: PAY.JP Subscriptions API
  phrasing_intents:
  - id: listSubscriptions
    intent: List subscriptions
    question: How do I see all my active and past subscriptions?
  - id: createSubscription
    intent: Subscribe a customer to a plan
    question: How do I put a customer on a recurring plan?
  - id: retrieveSubscription
    intent: Get a subscription
    question: How do I check the status of one subscription?
  - id: updateSubscription
    intent: Update a subscription
    question: How do I change the settings on an existing subscription?
  - id: deleteSubscription
    intent: Delete a subscription
    question: How do I delete a subscription record entirely?
  - id: pauseSubscription
    intent: Pause a subscription
    question: Can I temporarily stop billing a subscriber?
  - id: resumeSubscription
    intent: Resume a paused subscription
    question: How do I restart billing on a paused subscription?
  - id: cancelSubscription
    intent: Cancel a subscription
    question: How do I cancel a customer's subscription?
  phrasing_ops: 8
  slug: payjp-subscriptions-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Terms API from PAY.JP — 2 operation(s) for terms.
  name: PAY.JP Terms API
  phrasing_intents:
  - id: listTerms
    intent: List aggregation terms
    question: How do I see the aggregation periods my sales are grouped into?
  - id: retrieveTerm
    intent: Get an aggregation term
    question: How do I look up one aggregation period?
  phrasing_ops: 2
  slug: payjp-terms-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Tokens API from PAY.JP — 3 operation(s) for tokens.
  name: PAY.JP Tokens API
  phrasing_intents:
  - id: createToken
    intent: Tokenize a card
    question: How do I turn card details into a single-use token?
  - id: retrieveToken
    intent: Get a card token
    question: How do I check whether a card token has been used?
  - id: finishTokenThreeDSecure
    intent: Finish 3D Secure authentication for a card token
    question: Once a cardholder completes 3D Secure on a token, how do I mark the token as authenticated?
  phrasing_ops: 3
  slug: payjp-tokens-api
- baseURL: https://api.pay.jp/v1
  baseurl_source: declared
  description: The Transfers API from PAY.JP — 3 operation(s) for transfers.
  name: PAY.JP Transfers API
  phrasing_intents:
  - id: listTransfers
    intent: List payouts
    question: When have I been paid out to my bank account?
  - id: retrieveTransfer
    intent: Get a payout
    question: How do I look up one payout's amount and date?
  - id: listTransferDetails
    intent: List the charges in a payout
    question: Which charges were settled in a specific payout?
  phrasing_ops: 3
  slug: payjp-transfers-api
artifact_total: 56
asyncapis:
- description: ''
  name: Payjp Webhooks
  slug: payjp-webhooks
collections:
- collection_type: postman
  name: PAY.JP 3D Secure API
  slug: postman-payjp-3d-secure-api
- collection_type: postman
  name: PAY.JP 3D Secure Account API
  slug: postman-payjp-account-api
- collection_type: postman
  name: PAY.JP 3D Secure Balances API
  slug: postman-payjp-balances-api
- collection_type: postman
  name: PAY.JP 3D Secure Cards API
  slug: postman-payjp-cards-api
- collection_type: postman
  name: PAY.JP 3D Secure Charges API
  slug: postman-payjp-charges-api
- collection_type: postman
  name: PAY.JP 3D Secure Customers API
  slug: postman-payjp-customers-api
- collection_type: postman
  name: PAY.JP 3D Secure Events API
  slug: postman-payjp-events-api
- collection_type: postman
  name: PAY.JP 3D Secure Plans API
  slug: postman-payjp-plans-api
- collection_type: postman
  name: PAY.JP 3D Secure Platform API
  slug: postman-payjp-platform-api
- collection_type: postman
  name: PAY.JP 3D Secure Statements API
  slug: postman-payjp-statements-api
- collection_type: postman
  name: PAY.JP 3D Secure Subscriptions API
  slug: postman-payjp-subscriptions-api
- collection_type: postman
  name: PAY.JP 3D Secure Terms API
  slug: postman-payjp-terms-api
- collection_type: postman
  name: PAY.JP 3D Secure Tokens API
  slug: postman-payjp-tokens-api
- collection_type: postman
  name: PAY.JP 3D Secure Transfers API
  slug: postman-payjp-transfers-api
- collection_type: open
  name: PAY.JP 3D Secure API
  slug: open-payjp-3d-secure-api
- collection_type: open
  name: PAY.JP 3D Secure Account API
  slug: open-payjp-account-api
- collection_type: open
  name: PAY.JP 3D Secure Balances API
  slug: open-payjp-balances-api
- collection_type: open
  name: PAY.JP 3D Secure Cards API
  slug: open-payjp-cards-api
- collection_type: open
  name: PAY.JP 3D Secure Charges API
  slug: open-payjp-charges-api
- collection_type: open
  name: PAY.JP 3D Secure Customers API
  slug: open-payjp-customers-api
- collection_type: open
  name: PAY.JP 3D Secure Events API
  slug: open-payjp-events-api
- collection_type: open
  name: PAY.JP 3D Secure Plans API
  slug: open-payjp-plans-api
- collection_type: open
  name: PAY.JP 3D Secure Platform API
  slug: open-payjp-platform-api
- collection_type: open
  name: PAY.JP 3D Secure Statements API
  slug: open-payjp-statements-api
- collection_type: open
  name: PAY.JP 3D Secure Subscriptions API
  slug: open-payjp-subscriptions-api
- collection_type: open
  name: PAY.JP 3D Secure Terms API
  slug: open-payjp-terms-api
- collection_type: open
  name: PAY.JP 3D Secure Tokens API
  slug: open-payjp-tokens-api
- collection_type: open
  name: PAY.JP 3D Secure Transfers API
  slug: open-payjp-transfers-api
common:
- group: other
  href: https://artifacts.apis.io/payjp/capabilities/payjp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/payjp-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/payjp/overview
- group: agent
  href: https://artifacts.apis.io/payjp/agentic-access/payjp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/payjp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/payjp/security/payjp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/payjp-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://pay.jp/security
- group: auth
  href: https://artifacts.apis.io/payjp/security/payjp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/payjp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/payjp/security/payjp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payjp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/payjp/authentication/payjp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/payjp-authentication.yml
- group: design
  href: https://artifacts.apis.io/payjp/conventions/payjp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/payjp-conventions.yml
- group: build
  href: https://artifacts.apis.io/payjp/packages/payjp-packages.yml
  title: ''
  type: Packages
  url: packages/payjp-packages.yml
- group: build
  href: https://artifacts.apis.io/payjp/packages/payjp-packages.yml
  title: ''
  type: SDKs
  url: packages/payjp-packages.yml
- group: agent
  href: https://artifacts.apis.io/payjp/mcp/payjp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/payjp-mcp.yml
- group: agent
  href: https://artifacts.apis.io/payjp/llms/payjp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/payjp-llms.txt
- group: other
  href: https://artifacts.apis.io/payjp/overlays/payjp-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/payjp-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/payjp/conformance/payjp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payjp-conformance.yml
- group: design
  href: https://artifacts.apis.io/payjp/errors/payjp-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/payjp-error-codes.yml
- group: build
  href: https://artifacts.apis.io/payjp/errors/payjp-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/payjp-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/payjp/asyncapi/payjp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/payjp-webhooks.yml
- group: start
  href: https://artifacts.apis.io/payjp/sandbox/payjp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/payjp-sandbox.yml
- group: design
  href: https://artifacts.apis.io/payjp/data-model/payjp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/payjp-data-model.yml
- group: design
  href: https://artifacts.apis.io/payjp/components/payjp-components.yml
  title: ''
  type: Components
  url: components/payjp-components.yml
- group: design
  href: https://artifacts.apis.io/payjp/lifecycle/payjp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/payjp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pay.jp
- group: operate
  title: ''
  type: Deprecation
  url: https://pay.jp/info
- group: operate
  href: https://artifacts.apis.io/payjp/changelog/payjp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/payjp-changelog.yml
- group: agent
  href: https://artifacts.apis.io/payjp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/payjp/collections/payjp.postman_collection.json
  title: ''
  type: Postman
  url: collections/payjp.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payjp
- group: company
  title: ''
  type: Website
  url: https://pay.jp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pay.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pay.jp/v1/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pay.jp/v1/started
- group: operate
  title: ''
  type: Support
  url: https://help.pay.jp/ja
- group: commercial
  title: ''
  type: Pricing
  url: https://pay.jp/plan
- group: start
  title: ''
  type: SignUp
  url: https://console.pay.jp/d/signup
- group: start
  title: ''
  type: Login
  url: https://console.pay.jp/d/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pay.jp/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pay.co.jp/privacy
- group: commercial
  href: https://artifacts.apis.io/payjp/plans/payjp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/payjp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/payjp/rate-limits/payjp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/payjp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/payjp/finops/payjp-finops.yml
  title: ''
  type: FinOps
  url: finops/payjp-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pay.jp/info
created: '2026-07-17'
description: PAY.JP is an online payment service operated by PAY, Inc. (PAY株式会社) in Japan. Its Stripe-style REST API lets merchants create charges, tokenize cards, manage customers, run subscriptions (定期課金), and settle transfers (入金) in Japanese yen, with a Platform API (beta) for marketplace/multi-tenant payouts.
finops:
- has_sources: true
  method: derived
  name: Payjp Finops
  primary_unit: カード決済手数料
  service_category: ''
  slug: payjp-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payjp.png
layout: provider
modified: '2026-07-18'
name: PAY.JP
nav: Providers
network: true
overview: 'PAY.JP publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including 3D Secure API, Account API, Balances API, and 11 more. Tagged areas include Payments, Fintech, Japan, Credit Cards, and Subscription.


  The PAY.JP catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PAY.JP''s developer surface includes authentication, sandbox, changelog, documentation, getting-started guide, support, pricing, and 35 more developer resources.'
plans:
- name: Payjp Plans Pricing
  plan_count: 9
  slug: payjp-plans-pricing
- name: Payjp Price Estimates
  plan_count: 0
  slug: payjp-price-estimates
random_paper: 20
rate_limits:
- limit_count: 3
  name: Payjp Rate Limits
  slug: payjp-rate-limits
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 51.8
    developer_ergonomics: 74.4
    discoverability: 66.1
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 44.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/payjp/payjp-2026-08-07T191639.png
security:
- kind: authentication
  name: Payjp Authentication
  slug: payjp-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Payjp Domain Security
  slug: payjp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payjp Vulnerability Disclosure
  slug: payjp-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Payjp Trust Center
  slug: payjp-trust-center
  summary_line: PCI DSS
skill_count: 4
skills:
- name: Authorize, capture, and refund a charge
  slug: payjp-authorize-capture-refund
- name: Create a customer, plan, and subscription
  slug: payjp-customer-subscription
- name: Receive and verify PAY.JP webhooks
  slug: payjp-handle-webhooks
- name: Tokenize a card and create a charge
  slug: payjp-tokenize-and-charge
slug: payjp
tags:
- Payments
- Fintech
- Japan
- Credit Cards
- Subscription
- Tokenization
website: https://pay.jp/
---
