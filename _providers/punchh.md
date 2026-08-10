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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Punchh Agentic Access
  operation_count: 17
  slug: punchh-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 7
apis:
- description: Loyalty check-ins for online orders.
  name: Punchh Check-In API
  slug: punchh-check-in-api
- description: Loyalty check-in transaction details.
  name: Punchh Check-Ins API
  slug: punchh-check-ins-api
- description: Location and program configuration/metadata.
  name: Punchh Configuration API
  slug: punchh-configuration-api
- description: Guest offer management.
  name: Punchh Offers API
  slug: punchh-offers-api
- description: Receipt detail storage.
  name: Punchh Receipts API
  slug: punchh-receipts-api
- description: Apply rewards and discounts against online order receipts.
  name: Punchh Redemptions API
  slug: punchh-redemptions-api
- description: Guest registration, authentication, and profile management.
  name: Punchh Users API
  slug: punchh-users-api
artifact_total: 94
collections:
- collection_type: postman
  name: PAR Punchh Mobile Check-In API
  slug: postman-punchh-check-in-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Check-Ins API
  slug: postman-punchh-check-ins-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Configuration API
  slug: postman-punchh-configuration-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Offers API
  slug: postman-punchh-offers-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Receipts API
  slug: postman-punchh-receipts-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Redemptions API
  slug: postman-punchh-redemptions-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Users API
  slug: postman-punchh-users-api
- collection_type: open
  name: PAR Punchh Mobile API
  slug: open-punchh-mobile
- collection_type: open
  name: PAR Punchh Online Ordering and SSO API
  slug: open-punchh-online-ordering
- collection_type: open
  name: PAR Punchh Platform Functions API
  slug: open-punchh-platform-functions
- collection_type: open
  name: PAR Punchh POS and Kiosk API
  slug: open-punchh-pos
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/punchh/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/punchh-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/punchh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/punchh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/punchh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://punchh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.partech.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.partech.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.partech.com/docs/dev-portal-developer-resources
- group: build
  title: ''
  type: Postman
  url: https://punchh.com/blog/2024/07/12/par-punchh-apis-now-available-on-postman-workspace/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/punchh
- group: company
  title: ''
  type: Blog
  url: https://punchh.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/partechnology
- group: design
  title: ''
  type: SpectralRules
  url: rules/punchh-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/punchh-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/punchh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/punchh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/punchh-finops.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.partech.com/docs/dev-portal-webhooks-manager/8c18e3660f73f-event-guest
created: '2026-06-02'
description: Punchh, now part of PAR Technology and offered under the PAR Engagement brand, is an enterprise loyalty, offers, and customer engagement platform for restaurants. It unifies guest data from online ordering, mobile apps, POS, and kiosks into a single view so brands can run personalized loyalty and marketing programs. PAR exposes well-documented Punchh APIs through its developer portal covering platform functions, mobile, online ordering, POS and kiosk integration, and a webhooks manager, with sample collections published to Postman. Most integration surfaces require partner certification. Over 275 restaurant brands rely on Punchh to grow customer lifetime value.
examples:
- key_count: 4
  name: Mobile Access Token Example
  slug: mobile-access-token-example
- key_count: 4
  name: Mobile Create User Request Example
  slug: mobile-create-user-request-example
- key_count: 2
  name: Mobile Login Request Example
  slug: mobile-login-request-example
- key_count: 4
  name: Mobile Mark Offers Read Request Example
  slug: mobile-mark-offers-read-request-example
- key_count: 2
  name: Mobile Transaction Details Example
  slug: mobile-transaction-details-example
- key_count: 2
  name: Mobile Transaction Details Request Example
  slug: mobile-transaction-details-request-example
- key_count: 2
  name: Mobile Update User Profile Request Example
  slug: mobile-update-user-profile-request-example
- key_count: 2
  name: Mobile User Session Example
  slug: mobile-user-session-example
- key_count: 12
  name: Online Ordering Online Order Checkin Request Example
  slug: online-ordering-online-order-checkin-request-example
- key_count: 5
  name: Online Ordering Online Order Checkin Response Example
  slug: online-ordering-online-order-checkin-response-example
- key_count: 7
  name: Online Ordering Online Order Redemption Request Example
  slug: online-ordering-online-order-redemption-request-example
- key_count: 7
  name: Online Ordering Online Order Redemption Response Example
  slug: online-ordering-online-order-redemption-response-example
- key_count: 5
  name: Platform Functions Redeemable Example
  slug: platform-functions-redeemable-example
- key_count: 4
  name: Pos Pos Checkin Request Example
  slug: pos-pos-checkin-request-example
- key_count: 6
  name: Pos Pos User Example
  slug: pos-pos-user-example
features:
- description: Configurable points, rewards, tiers, and membership levels across channels.
  name: Loyalty Programs
- description: Targeted offers, coupons, and personalized marketing campaigns driven by unified guest data.
  name: Offers and Campaigns
- description: Earn loyalty across mobile, online ordering, POS, and kiosk channels.
  name: Omnichannel Check-Ins
- description: Apply rewards, redeemables, and discounts against receipts with possible/create/void flows.
  name: Redemptions
- description: Real-time event notifications for coupons, points, rewards, and guest lifecycle events.
  name: Webhooks Manager
- description: Surface Punchh-defined offers natively in external platforms via Platform Functions.
  name: Headless Offers
finops:
- name: Punchh Finops
  service_category: Loyalty + Guest Engagement
  slug: punchh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/punchh.png
integrations:
- description: Integrations with restaurant POS platforms for in-store loyalty.
  name: Point of Sale Systems
- description: Digital and online ordering platforms connect via the Online Ordering and SSO API.
  name: Online Ordering Platforms
- description: Unify guest data with CDPs and CRMs.
  name: Customer Data Platforms
- description: Punchh Loyalty connector for Salesforce Marketing Cloud on AppExchange.
  name: Salesforce Marketing Cloud
- description: Connects to messaging platforms, surveys, and payment gateways across dozens of categories.
  name: Messaging and Payment Gateways
json_schemas:
- name: AccessToken
  property_count: 4
  slug: mobile-access-token
- name: CreateUserRequest
  property_count: 4
  slug: mobile-create-user-request
- name: LoginRequest
  property_count: 2
  slug: mobile-login-request
- name: MarkOffersReadRequest
  property_count: 4
  slug: mobile-mark-offers-read-request
- name: TransactionDetailsRequest
  property_count: 2
  slug: mobile-transaction-details-request
- name: TransactionDetails
  property_count: 2
  slug: mobile-transaction-details
- name: UpdateUserProfileRequest
  property_count: 2
  slug: mobile-update-user-profile-request
- name: UserSession
  property_count: 2
  slug: mobile-user-session
- name: OnlineOrderCheckinRequest
  property_count: 12
  slug: online-ordering-online-order-checkin-request
- name: OnlineOrderCheckinResponse
  property_count: 5
  slug: online-ordering-online-order-checkin-response
- name: OnlineOrderRedemptionRequest
  property_count: 7
  slug: online-ordering-online-order-redemption-request
- name: OnlineOrderRedemptionResponse
  property_count: 7
  slug: online-ordering-online-order-redemption-response
- name: Redeemable
  property_count: 5
  slug: platform-functions-redeemable
- name: PosCheckinRequest
  property_count: 4
  slug: pos-pos-checkin-request
- name: PosUser
  property_count: 6
  slug: pos-pos-user
json_structures:
- name: Mobile Access Token Structure
  property_count: 4
  slug: mobile-access-token-structure
- name: Mobile Create User Request Structure
  property_count: 4
  slug: mobile-create-user-request-structure
- name: Mobile Login Request Structure
  property_count: 2
  slug: mobile-login-request-structure
- name: Mobile Mark Offers Read Request Structure
  property_count: 4
  slug: mobile-mark-offers-read-request-structure
- name: Mobile Transaction Details Request Structure
  property_count: 2
  slug: mobile-transaction-details-request-structure
- name: Mobile Transaction Details Structure
  property_count: 2
  slug: mobile-transaction-details-structure
- name: Mobile Update User Profile Request Structure
  property_count: 2
  slug: mobile-update-user-profile-request-structure
- name: Mobile User Session Structure
  property_count: 2
  slug: mobile-user-session-structure
- name: Online Ordering Online Order Checkin Request Structure
  property_count: 12
  slug: online-ordering-online-order-checkin-request-structure
- name: Online Ordering Online Order Checkin Response Structure
  property_count: 5
  slug: online-ordering-online-order-checkin-response-structure
- name: Online Ordering Online Order Redemption Request Structure
  property_count: 7
  slug: online-ordering-online-order-redemption-request-structure
- name: Online Ordering Online Order Redemption Response Structure
  property_count: 7
  slug: online-ordering-online-order-redemption-response-structure
- name: Platform Functions Redeemable Structure
  property_count: 5
  slug: platform-functions-redeemable-structure
- name: Pos Pos Checkin Request Structure
  property_count: 4
  slug: pos-pos-checkin-request-structure
- name: Pos Pos User Structure
  property_count: 6
  slug: pos-pos-user-structure
jsonld:
- class_count: 8
  name: Punchh Mobile Context
  property_count: 52
  slug: punchh-mobile-context
- class_count: 4
  name: Punchh Online Ordering Context
  property_count: 27
  slug: punchh-online-ordering-context
- class_count: 1
  name: Punchh Platform Functions Context
  property_count: 5
  slug: punchh-platform-functions-context
- class_count: 2
  name: Punchh Pos Context
  property_count: 10
  slug: punchh-pos-context
layout: provider
modified: '2026-06-03'
name: Punchh
nav: Providers
network: true
overview: 'Punchh publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Check-In API, Check-Ins API, Configuration API, and 4 more. Tagged areas include Restaurant, Loyalty, Marketing, Guest Engagement, and Online Ordering.


  The Punchh catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Punchh''s developer surface includes authentication, documentation, developer portal, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Punchh Plans Pricing
  plan_count: 1
  slug: punchh-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 4
  name: Punchh Rate Limits
  slug: punchh-rate-limits
rules:
- name: Punchh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: punchh-jsonschema-spectral-rules
- name: Punchh API Rules
  rule_count: 37
  severity_counts:
    error: 3
    hint: 0
    info: 11
    warn: 23
  slug: punchh-spectral-rules
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.8
    developer_ergonomics: 45.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 44.7
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/screenshots/punchh-2026-06-20T192311.png
security:
- kind: authentication
  name: Punchh Authentication
  slug: punchh-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Punchh Domain Security
  slug: punchh-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Punchh Vulnerability Disclosure
  slug: punchh-vulnerability-disclosure
  summary_line: Hackerone
slug: punchh
solutions:
- description: Enterprise loyalty program management for restaurant brands.
  name: Loyalty
- description: Personalized offers and promotions engine.
  name: Offers
- description: Unified marketing and engagement across the guest lifecycle.
  name: Guest Engagement
tags:
- Restaurant
- Loyalty
- Marketing
- Guest Engagement
- Online Ordering
- Mobile
- Point Of Sale
- Webhooks
use_cases:
- description: Power a restaurant brand's mobile app with sign-in, profile, check-ins, and offers.
  name: Branded Mobile Loyalty App
- description: Let guests earn and redeem loyalty on a digital ordering platform via SSO and check-in APIs.
  name: Online Ordering Rewards
- description: Look up guests, accrue points, and redeem rewards at the point of sale or kiosk.
  name: POS Loyalty at the Counter
- description: Pull Punchh redeemables into a CDP, messaging platform, or partner channel.
  name: External Offer Distribution
website: https://punchh.com/
---
