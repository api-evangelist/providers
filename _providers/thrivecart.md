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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Account API from ThriveCart — 1 operation(s) for account.
  name: ThriveCart Account API
  phrasing_intents:
  - id: ping
    intent: Check my API key and account details
    question: Is my ThriveCart API token still valid?
  phrasing_ops: 1
  slug: thrivecart-account-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Affiliates API from ThriveCart — 9 operation(s) for affiliates.
  name: ThriveCart Affiliates API
  phrasing_intents:
  - id: searchAffiliates
    intent: Search affiliates by product, name or email
    question: How do I find affiliates approved to promote a particular product?
  - id: createNewAffiliate
    intent: Create a new affiliate
    question: How do I sign up a new affiliate and add them to my products?
  - id: readAffiliateInfo
    intent: Look up one affiliate's details
    question: How can I pull up the details of a single affiliate?
  - id: markAffiliateAsFavorite
    intent: Mark an affiliate as a favorite
    question: How do I flag one of my affiliates as a VIP?
  - id: unFavouriteAnAffiliate
    intent: Remove an affiliate's favorite marker
    question: How do I take an affiliate off my favorites?
  - id: registerAffiliateForAProduct
    intent: Register an existing affiliate for products
    question: How do I add an affiliate I already have to another product?
  - id: approveAnAffiliateForAProduct
    intent: Approve an affiliate's pending application
    question: How do I approve an affiliate who applied to promote my product?
  - id: rejectAnAffiliateForAProduct
    intent: Reject an affiliate's pending application
    question: How do I turn down an affiliate's application to promote a product?
  phrasing_ops: 10
  slug: thrivecart-affiliates-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Bumps API from ThriveCart — 3 operation(s) for bumps.
  name: ThriveCart Bumps API
  phrasing_intents:
  - id: listBumpOffers
    intent: List bump offers
    question: What order bump offers do I have set up?
  - id: getBump
    intent: Get a bump offer
    question: How do I view the settings of one specific bump offer?
  - id: getBumpPriceDetails
    intent: Get a bump offer's pricing options
    question: What pricing options are configured on a bump offer?
  phrasing_ops: 3
  slug: thrivecart-bumps-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Customers API from ThriveCart — 2 operation(s) for customers.
  name: ThriveCart Customers API
  phrasing_intents:
  - id: readCustomerInformation
    intent: Read a customer's purchase history
    question: How do I see everything a customer has bought and subscribed to?
  - id: updateCustomerEmailAddress
    intent: Change a customer's email address
    question: How do I change the email address on a customer's orders?
  phrasing_ops: 2
  slug: thrivecart-customers-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Downsells API from ThriveCart — 3 operation(s) for downsells.
  name: ThriveCart Downsells API
  phrasing_intents:
  - id: listDownsells
    intent: List downsells
    question: Which downsell offers exist in my account?
  - id: getDownsell
    intent: Get a downsell
    question: How do I view one downsell's details?
  - id: getDownsellPriceDetails
    intent: Get a downsell's pricing options
    question: What price options does a downsell offer?
  phrasing_ops: 3
  slug: thrivecart-downsells-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Event subscriptions API from ThriveCart — 2 operation(s) for event subscriptions.
  name: ThriveCart Event subscriptions API
  phrasing_intents:
  - id: createEventSubscription
    intent: Subscribe an endpoint to webhook events
    question: How do I get webhook notifications sent to my endpoint?
  - id: unsubscribeFromAnEvent
    intent: Unsubscribe an endpoint from webhooks
    question: How do I stop webhook notifications going to an endpoint?
  phrasing_ops: 2
  slug: thrivecart-event-subscriptions-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Learn API from ThriveCart — 1 operation(s) for learn.
  name: ThriveCart Learn API
  phrasing_intents:
  - id: createNewStudent
    intent: Enroll a new student in a course
    question: How do I give someone access to a course in my Learn area?
  phrasing_ops: 1
  slug: thrivecart-learn-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Products API from ThriveCart — 3 operation(s) for products.
  name: ThriveCart Products API
  phrasing_intents:
  - id: listProducts
    intent: List products
    question: What products do I have in my account?
  - id: getProduct
    intent: Get a product
    question: How do I look up one product's details?
  - id: getProductPriceDetails
    intent: Get a product's pricing options
    question: What pricing options are available for a product?
  phrasing_ops: 3
  slug: thrivecart-products-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Subscriptions API from ThriveCart — 4 operation(s) for subscriptions.
  name: ThriveCart Subscriptions API
  phrasing_intents:
  - id: cancelASubscription
    intent: Cancel a subscription
    question: How do I cancel a customer's recurring subscription?
  - id: refundATransaction
    intent: Refund a transaction
    question: How do I refund a customer's purchase?
  - id: pauseASubscription
    intent: Pause a subscription
    question: How do I put a customer's subscription on hold?
  - id: resumeASubscription
    intent: Resume a paused subscription
    question: How do I restart a subscription I paused?
  phrasing_ops: 4
  slug: thrivecart-subscriptions-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Transactions API from ThriveCart — 1 operation(s) for transactions.
  name: ThriveCart Transactions API
  phrasing_intents:
  - id: searchTransactions
    intent: Search transaction activity
    question: How do I find all the charges and refunds for a customer email?
  phrasing_ops: 1
  slug: thrivecart-transactions-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Upsells API from ThriveCart — 3 operation(s) for upsells.
  name: ThriveCart Upsells API
  phrasing_intents:
  - id: listUpsells
    intent: List upsells
    question: Which upsell offers have I created?
  - id: getUpsell
    intent: Get an upsell
    question: How do I view a single upsell's details?
  - id: getUpsellPriceDetails
    intent: Get an upsell's pricing options
    question: What price options does an upsell offer have?
  phrasing_ops: 3
  slug: thrivecart-upsells-api
artifact_total: 21
asyncapis:
- description: ThriveCart delivers account events to subscriber endpoints over HTTP POST. Two surfaces exist and they do not share event names. **Event Subscription API (this document).** Created programmatically wi
  name: ThriveCart Event Subscriptions
  slug: thrivecart-events-asyncapi
collections:
- collection_type: postman
  name: ThriveCart API
  slug: postman-thrivecart-api
- collection_type: open
  name: ThriveCart API
  slug: open-thrivecart-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/capabilities/thrivecart-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thrivecart-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/overlays/thrivecart-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thrivecart-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/mcp/thrivecart-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thrivecart-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/scopes/thrivecart-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/thrivecart-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://thrivecart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.thrivecart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thrivecart.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.thrivecart.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.thrivecart.com/documentation/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.thrivecart.com/
- group: operate
  title: ''
  type: Support
  url: https://support.thrivecart.com/
- group: company
  title: ''
  type: Blog
  url: https://thrivecart.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://thrivecart.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thrivecart
- group: operate
  title: ''
  type: Roadmap
  url: https://thrivecart.com/resources/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://thrivecart.com/products/proplus/
- group: start
  title: ''
  type: SignUp
  url: https://checkout.thrivecart.com/thrivecart-standard-monthly-plan/
- group: start
  title: ''
  type: Login
  url: https://thrivecart.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thrivecart.com/legal/thrivecart/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thrivecart.com/legal/thrivecart/?tab=privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://thrivecart.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://thrivecart.com/blog/category/product-updates/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/packages/thrivecart-packages.yml
  title: ''
  type: Packages
  url: packages/thrivecart-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/packages/thrivecart-packages.yml
  title: ''
  type: SDKs
  url: packages/thrivecart-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/well-known/thrivecart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thrivecart-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/well-known/thrivecart-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thrivecart-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/security/thrivecart-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thrivecart-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/security/thrivecart-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thrivecart-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/security/thrivecart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thrivecart-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/lifecycle/thrivecart-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thrivecart-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/conformance/thrivecart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thrivecart-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/conformance/thrivecart-conformance.yml
  title: ''
  type: Compliance
  url: conformance/thrivecart-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/components/thrivecart-components.yml
  title: ''
  type: Components
  url: components/thrivecart-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/sandbox/thrivecart-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thrivecart-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/changelog/thrivecart-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thrivecart-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/plans/thrivecart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thrivecart-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/rate-limits/thrivecart-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thrivecart-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/llms/thrivecart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thrivecart-llms.txt
created: '2026-08-12'
description: ThriveCart is a hosted shopping cart, checkout and course platform for creators, coaches and digital-product sellers, operated by ThriveCart LLC. It sells one-time and recurring digital and physical products through customisable checkout pages with order bumps, one-click upsells and downsells, A/B testing, abandoned-cart recovery, sales-tax automation and a built-in affiliate centre, and bundles a learning-management product (ThriveCart Learn / ThriveCart Academy). Payments are processed through Stripe, PayPal, Authorize.net and ThrivePay Installments rather than by ThriveCart itself. The public ThriveCart API is a bearer-token REST surface at https://thrivecart.com/api/external covering products, bump offers, upsells, downsells, pricing options, transactions, customers, subscriptions, affiliates, Learn students and event subscriptions, with an account-wide webhook surface and a targeted Event Subscription API alongside it.
image: https://thrivecart.com/wp-content/uploads/2025/07/TC-logo-on-White.png
layout: provider
modified: '2026-08-12'
name: ThriveCart
nav: Providers
network: true
overview: 'ThriveCart publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Affiliates API, Bumps API, and 8 more. Tagged areas include Company, Checkout, Shopping Cart, Payments, and E-Commerce.


  The ThriveCart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThriveCart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Thrivecart Plans Pricing
  plan_count: 3
  slug: thrivecart-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Thrivecart Rate Limits
  slug: thrivecart-rate-limits
scopes:
- name: Thrivecart Scopes
  scope_count: 0
  slug: thrivecart-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 72.0
    discoverability: 73.2
    operational_transparency: 78.9
  previous_composite: 67.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 41.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/screenshots/thrivecart-2026-08-17T082349.png
security:
- kind: authentication
  name: Thrivecart Authentication
  slug: thrivecart-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Thrivecart Domain Security
  slug: thrivecart-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Thrivecart Vulnerability Disclosure
  slug: thrivecart-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Thrivecart Trust Center
  slug: thrivecart-trust-center
  summary_line: PCI DSS, GDPR, CCPA
slug: thrivecart
tags:
- Company
- Checkout
- Shopping Cart
- Payments
- E-Commerce
- Subscription
- Affiliate Marketing
- Learning Management
- Creator Economy
- Webhook
website: https://thrivecart.com/
---
