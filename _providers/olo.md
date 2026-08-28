---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Olo Agentic Access
  operation_count: 12
  slug: olo-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 15
apis:
- description: The Olo Dispatch API orchestrates direct delivery for restaurants by routing orders to a network of delivery service providers (DSPs) such as DoorDash Drive, Uber Direct, Postmates, and Relay. Dispatc
  name: Olo Dispatch API
  slug: olo-dispatch
- description: The Olo POS Interface Specification (commonly OloCloud) is the contract POS vendors implement to make their point-of-sale system natively integrable with Olo's ordering platform. The interface defines
  name: Olo POS Interface (OloCloud)
  slug: olo-pos-interface
- description: Omnivore (acquired by Olo in 2019) is a universal POS API that abstracts 12+ point-of-sale systems behind a single REST surface, handling 5.6M API calls per day across 23,000+ restaurant locations. En
  name: Omnivore POS API
  slug: olo-omnivore
- description: 'Olo Pay is the platform''s embedded payments solution, providing PCI-compliant card capture, tokenization, Apple Pay / Google Pay digital wallet acceptance, network tokenization, fraud prevention, and '
  name: Olo Pay API
  slug: olo-pay
- description: The Olo Network is a second-party ordering ecosystem that exposes participating restaurant brands' menus and ordering surfaces to high-intent guest channels (super-apps, wallets, voice agents, AI assi
  name: Olo Network API
  slug: olo-network
- description: Olo Marketing and the Guest Data Platform (GDP) unify first-party guest data captured across ordering, payments, loyalty, host, and sentiment signals into a single guest profile that powers segmentati
  name: Olo Marketing & Guest Data Platform API
  slug: olo-marketing
- description: Olo Host (acquired from Wisely) provides reservations, waitlist, table management, and host-stand workflows for restaurants. The Host API exposes reservation creation, waitlist updates, table state, a
  name: Olo Host API
  slug: olo-host
- description: Olo Sentiment aggregates guest feedback signals - post-order surveys, public reviews (Google, Yelp), and social mentions - and exposes them through a sentiment API used for reputation management dashb
  name: Olo Sentiment API
  slug: olo-sentiment
- description: Olo exposes outbound webhooks that fire on order lifecycle events (placed, confirmed, ready, completed, refunded), gift-card activity, loyalty accrual / redemption, tender events, and marketplace stat
  name: Olo Webhooks
  slug: olo-webhooks
- description: Loyalty account creation and lookup
  name: Olo Accounts API
  slug: olo-accounts-api
- description: Loyalty point accrual and void
  name: Olo Accruals API
  slug: olo-accruals-api
- description: Brand-level configuration and metadata
  name: Olo Brand API
  slug: olo-brand-api
- description: Validation and redemption of coupons and loyalty rewards
  name: Olo Promotions API
  slug: olo-promotions-api
- description: Marketplace Rails partner export and order injection operations
  name: Olo Rails API
  slug: olo-rails-api
- description: Guest account lookups
  name: Olo Users API
  slug: olo-users-api
artifact_total: 98
asyncapis:
- description: Olo emits outbound HTTP webhooks to partner-registered endpoints for order lifecycle, loyalty, gift-card, tender, and marketplace status events. Each delivery includes an X-Olo-Message-Id header (a un
  name: Olo Webhooks
  slug: olo-webhooks-asyncapi
collections:
- collection_type: postman
  name: Olo Ordering Accounts API
  slug: postman-olo-accounts-api
- collection_type: postman
  name: Olo Ordering Accounts Accruals API
  slug: postman-olo-accruals-api
- collection_type: postman
  name: Olo Ordering Accounts Brand API
  slug: postman-olo-brand-api
- collection_type: postman
  name: Olo Ordering Accounts Promotions API
  slug: postman-olo-promotions-api
- collection_type: postman
  name: Olo Ordering Accounts Rails API
  slug: postman-olo-rails-api
- collection_type: postman
  name: Olo Ordering Accounts Users API
  slug: postman-olo-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Olo Ordering Accounts API
  slug: open-olo-accounts-api
- collection_type: open
  name: Olo Ordering Accounts Accruals API
  slug: open-olo-accruals-api
- collection_type: open
  name: Olo Ordering Accounts Brand API
  slug: open-olo-brand-api
- collection_type: open
  name: Olo Ordering API
  slug: open-olo-ordering
- collection_type: open
  name: Olo Ordering Accounts Promotions API
  slug: open-olo-promotions-api
- collection_type: open
  name: Olo Promotions API
  slug: open-olo-promotions
- collection_type: open
  name: Olo Ordering Accounts Rails API
  slug: open-olo-rails-api
- collection_type: open
  name: Olo Ordering Accounts Users API
  slug: open-olo-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/olo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/olo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/olo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/olo-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.olo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.olo.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.olo.com/Account/Register
- group: start
  title: ''
  type: Login
  url: https://developer.olo.com/Account/Login
- group: docs
  title: ''
  type: Documentation
  url: https://developer.olo.com/
- group: company
  title: ''
  type: Partners
  url: https://partners.olo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.olo.com/api-usage-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.olo.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.olo.com/
- group: operate
  title: ''
  type: Support
  url: https://olosupport.zendesk.com/hc/en-us
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://olosupport.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.olo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ololabs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ololabs/dev-support-code-samples
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ololabs/promotions-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ololabs/olo-serve-gtm-templates
- group: design
  title: ''
  type: SpectralRules
  url: rules/olo-spectral-rules.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/olo
- group: other
  title: ''
  type: X
  url: https://twitter.com/olo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OloRestaurantTech
- group: auth
  title: ''
  type: Security
  url: https://www.olo.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.olo.com/
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/ololabs/dev-support-code-samples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ololabs/olo-pay-ios-sdk-releases
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ololabs/olo-pay-android-sdk-releases
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ololabs/olo-pay-flutter-sdk-releases
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ololabs/pay-digitalwallets-ios-sdk-releases
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ololabs/pay-digitalwallets-android-sdk-releases
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ololabs/pay-digitalwallets-flutter-sdk-releases
- group: docs
  title: ''
  type: GraphQL
  url: graphql/olo-graphql.md
- group: commercial
  title: ''
  type: Plans
  url: plans/olo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/olo-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/olo-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/olo-context.jsonld
created: '2026-05-25'
description: Olo is a leading on-demand commerce platform powering the digital experience for restaurant brands, serving approximately 750+ enterprise and emerging chains across 90,000+ restaurant locations. The Olo platform combines online ordering, delivery dispatch, marketplace integration (Rails), payments (Olo Pay), guest data (GDP / Marketing), loyalty, and POS connectivity (Omnivore) into a single restaurant commerce stack. Developers and certified Olo Connect partners build against the Ordering API (custom order injection), Rails API (third-party marketplace order delivery), Dispatch API (delivery orchestration), the POS Interface (OloCloud) for direct POS integrations, the Omnivore API (multi-POS abstraction), the Olo Pay SDKs (iOS, Android, Flutter, Digital Wallets), and a webhook surface that fires order, loyalty, gift-card, and tender events. APIs use signature-based request authorization (HMAC) for ordering/rails plus webhook signature validation; sample code is published for
  C#, Java, PHP, Ruby, JavaScript, and Python. Olo (NYSE - OLO) is headquartered in New York City and went public in March 2021.
examples:
- key_count: 1
  name: Olo Ordering Check User Exists Example
  slug: olo-ordering-check-user-exists-example
- key_count: 1
  name: Olo Ordering Create Basket Example
  slug: olo-ordering-create-basket-example
- key_count: 4
  name: Olo Promotions Account Example
  slug: olo-promotions-account-example
- key_count: 20
  name: Olo Promotions Validate Example
  slug: olo-promotions-validate-example
features:
- description: White-label web, mobile, and kiosk ordering surfaces backed by the Olo Ordering API for 800+ enterprise restaurant brands.
  name: Direct Online Ordering
- description: Bidirectional integration with DoorDash, Uber Eats, Grubhub, Google, and 25+ marketplaces for menu sync and order injection.
  name: Rails Marketplace Integration
- description: Multi-DSP delivery orchestration across DoorDash Drive, Uber Direct, Postmates, and Relay with quote-and-tender routing.
  name: Dispatch Direct Delivery
- description: Curated ordering distribution to super-apps, voice agents, and AI assistants while restaurants retain the guest relationship.
  name: Olo Network (Second-Party Distribution)
- description: Single REST interface abstracting 12+ POS systems (Aloha, PAR Brink, Micros, POSitouch, etc.) for partner integrations.
  name: Omnivore Universal POS API
- description: PCI-compliant card capture, network tokenization, Apple Pay / Google Pay, and fraud prevention via native iOS, Android, and Flutter SDKs.
  name: Olo Pay Embedded Payments
- description: Unified first-party guest profile combining ordering, payments, loyalty, host, and sentiment signals for segmentation and personalization.
  name: Guest Data Platform (GDP)
- description: Lifecycle campaigns and personalization driven by GDP audiences and integrations with Attentive, Infobip, and email providers.
  name: Olo Marketing
- description: Native loyalty plus integrations with Punchh, Paytronix, and Thanx with loyalty SSO bound to ordering and POS.
  name: Olo Loyalty
- description: Reservations, waitlist, and table management (formerly Wisely) feeding GDP for unified guest profiles.
  name: Olo Host
- description: Aggregated post-order surveys, public review monitoring, and automated guest recovery workflows.
  name: Sentiment and Reputation
- description: Catering order management with capacity controls, lead times, and large-order workflows on top of the Ordering API.
  name: Catering+
- description: Digitized phone-order capture that routes voice orders into Olo Ordering and the POS Interface.
  name: Switchboard
- description: Front-end ordering kit and passwordless guest checkout that reduce friction across guest channels.
  name: Serve and Olo Accounts
- description: Local listing management across Google, Yelp, and search surfaces tied to restaurant store data.
  name: Sync (Local Listings)
- description: Outbound HMAC-signed webhooks for order lifecycle, loyalty, gift-card, and tender events.
  name: Webhooks for Order and Loyalty Events
- description: Dedicated sandbox issued through the Olo Developer Portal for partner certification and integration testing.
  name: Sandbox Environment
- description: Tiered (Standard, Gold, Platinum) partner program governing certification, co-marketing, and integration distribution.
  name: Olo Connect Partner Program
finops:
- name: Olo Finops
  service_category: Restaurant Commerce Platform
  slug: olo-finops
graphqls:
- description: Olo is a digital ordering and delivery platform for restaurant brands. The API covers orders, menus, baskets, restaurant locations, delivery dispatching, guest management, and webhook integrations for
  name: Olo GraphQL API
  slug: olo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/olo.png
integrations:
- description: Marketplace ordering via Rails and direct delivery via Dispatch.
  name: DoorDash
- description: Marketplace integration via Rails and Uber Direct via Dispatch.
  name: Uber Eats
- description: Marketplace order injection via Rails.
  name: Grubhub
- description: Order with Google integration and Sync local listings.
  name: Google
- description: POS interoperability for shared restaurant brands.
  name: Toast
- description: POS Interface and Omnivore-supported point-of-sale.
  name: NCR Aloha
- description: POS Interface and Omnivore-supported point-of-sale.
  name: PAR Brink
- description: POS Interface support for Simphony and SimphonyCloud.
  name: Oracle Micros Simphony
- description: POS Interface and Omnivore-supported point-of-sale.
  name: POSitouch
- description: Labor scheduling integration consuming Olo restaurant and order data.
  name: 7shifts
- description: SMS marketing activation driven by GDP audiences.
  name: Attentive
- description: Conversational messaging integration for marketing and order updates.
  name: Infobip
- description: Third-party loyalty engine integrated via Olo Loyalty.
  name: Punchh
- description: Loyalty and gift-card integration via Olo Loyalty.
  name: Paytronix
- description: Loyalty engine integration.
  name: Thanx
- description: Digital wallet acceptance via Olo Pay SDKs.
  name: Apple Pay
- description: Digital wallet acceptance via Olo Pay SDKs.
  name: Google Pay
json_schemas:
- name: Olo Promotions Account
  property_count: 4
  slug: olo-promotions-account
- name: Olo Promotions Request
  property_count: 20
  slug: olo-promotions-request
json_structures:
- name: Olo Promotions Structure
  property_count: 3
  slug: olo-promotions-structure
jsonld:
- class_count: 56
  name: Olo Context
  property_count: 0
  slug: olo-context
layout: provider
modified: '2026-06-03'
name: Olo
nav: Providers
network: true
overview: 'Olo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Accounts API, Accruals API, and 4 more. Tagged areas include Food Service, Restaurant, Online Ordering, Delivery, and Point-of-Sale.


  The Olo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Olo''s developer surface includes authentication, developer portal, signup flow, documentation, support, engineering blog, YouTube channel, and 32 more developer resources.'
plans:
- name: Olo Plans Pricing
  plan_count: 4
  slug: olo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Olo Rate Limits
  slug: olo-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Olo API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: olo-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Olo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: olo-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Olo API Rules
  rule_count: 36
  severity_counts:
    error: 8
    hint: 0
    info: 10
    warn: 18
  slug: olo-spectral-rules
score:
  band: strong
  composite: 64.9
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 28.8
    contract_quality: 77.6
    developer_ergonomics: 59.5
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 50.0
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olo/refs/heads/main/screenshots/olo-2026-06-20T190700.png
security:
- kind: authentication
  name: Olo Authentication
  slug: olo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Olo Domain Security
  slug: olo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Olo Trust Center
  slug: olo-trust-center
  summary_line: SOC 2, PCI DSS
slug: olo
solutions:
- description: Ordering, Serve, Dispatch, Rails, Catering+, Loyalty, Order with Google, Switchboard, and Olo Network.
  name: Increase Orders
- description: Olo Pay, Host, and Sync to streamline payments, reservations, and local listings.
  name: Streamline Operations
- description: Marketing, GDP, Sentiment, and Olo Accounts for unified, personalized guest journeys.
  name: Improve Guest Experiences
tags:
- Food Service
- Restaurant
- Online Ordering
- Delivery
- Point-of-Sale
- Hospitality
- Payments
- Loyalty
- Marketing
use_cases:
- description: Power web, app, kiosk, and voice ordering for chains like Five Guys, P.F. Chang's, Portillo's, and First Watch.
  name: Branded Direct Ordering for Enterprise Restaurant Chains
- description: Inject DoorDash, Uber Eats, and Grubhub orders into the restaurant POS via Rails without manual tablet workflows.
  name: Marketplace Order Injection
- description: Dispatch routes direct-delivery orders to DSPs without operators running their own fleet.
  name: Restaurant-Operated Direct Delivery
- description: Loyalty, payroll, KDS, and analytics vendors integrate against Omnivore once and reach 12+ POS systems.
  name: POS Partner Integrations via Omnivore
- description: Tie accrual / redemption directly to checkout via Olo Loyalty and webhooks.
  name: Loyalty and Gift Card Programs
- description: Build first-party audiences in GDP and activate them through Olo Marketing, Attentive SMS, and email ESPs.
  name: Guest Data Activation
- description: Manage catering capacity, lead times, and corporate accounts with Catering+ on top of Ordering API.
  name: Catering and Large-Order Channels
- description: Olo Network distributes ordering capabilities into voice, super-app, and AI assistant surfaces.
  name: Voice and AI Assistant Order Channels
- description: Run host stand, waitlist, and reservation flows via Olo Host while feeding the same guest profile.
  name: Reservations and Hospitality
- description: Aggregate sentiment signals and trigger automated recovery workflows after negative experiences.
  name: Reputation and Guest Recovery
website: https://developer.olo.com/
---
