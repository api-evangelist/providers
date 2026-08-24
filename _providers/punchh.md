---
access_model:
  confidence: high
  label: Enterprise · Partner certification required
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://developers.partech.com/engagement-tools/par-punchh/
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Punchh Agentic Access
  operation_count: 17
  slug: punchh-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 15
apis:
- description: Punchh provides a robust platform for offering loyalty programs to customers. When a business integrates its back-end with the Punchh server, the Punchh APIs become instrumental in executing loyalty p
  name: Punchh Mobile API
  slug: punchh-mobile-api
- description: For more information, see Online Ordering Module 5 - Redemptions. Published by PAR on the mobile section of the PAR developer portal; 6 operations. Certification required.
  name: Punchh Redemptions 1.0 (Legacy) API - Mobile
  slug: punchh-mobile-redemptions-legacy
- description: 'The Redemptions 2.0 protocol has been designed to replace the legacy Redemptions 1.0 endpoints. The new protocol allows for the following features: - Single-scan flow support - Batching of redemptions'
  name: Punchh Redemptions 2.0 (New) API - Mobile
  slug: punchh-mobile-redemptions-v2
- description: Subscriptions is an add-on Punchh loyalty product that allows businesses to create subscription plans to generate up-front revenue and offers benefits in addition to the standard benefits that unsubsc
  name: Punchh Subscription API - Mobile
  slug: punchh-mobile-subscription
- description: 'For more information, see Online Ordering Module 5: Redemptions. Published by PAR on the online ordering section of the PAR developer portal; 4 operations. Certification required.'
  name: Punchh Redemptions 1.0 (Legacy) API - Online Ordering
  slug: punchh-online-ordering-redemptions-legacy
- description: 'The Redemptions 2.0 protocol has been designed to replace the legacy Redemptions 1.0 endpoints. The new protocol allows for the following features: - Single-scan flow support - Batching of redemptions'
  name: Punchh Redemptions 2.0 (New) API - Online Ordering
  slug: punchh-online-ordering-redemptions-v2
- description: The Punchh SSO API endpoints provide user-management functions such as login, registration, forgot password, and connect with Facebook for users on the Punchh loyalty platform. You can also fetch user
  name: Punchh Online Ordering and SSO API
  slug: punchh-online-ordering-sso-api
- description: Subscriptions is an add-on Punchh loyalty product that allows businesses to create subscription plans to generate up-front revenue and offers benefits in addition to the standard benefits that unsubsc
  name: Punchh Subscription API - Online Ordering
  slug: punchh-online-ordering-subscription
- description: This API documentation is intended to provide comprehensive information for admin users of the Punchh platform. Many of the settings and available actions depend on an appropriate level of access to P
  name: Punchh Platform Functions API
  slug: punchh-platform-functions-api
- description: Distribute Punchh offers through an external system of choice by configuring and scheduling the mass offer campaign functionality through API calls. For more information, see Headless Offers Managemen
  name: Punchh Headless Offers API - Platform Functions
  slug: punchh-platform-functions-headless-offers
- description: Create and update in bulk and list Line Item Selectors (LIS), Qualification Criteria (QC), and Reedemables through Offers Ingestion API calls. For more information, see Offers Ingestion Management Pub
  name: Punchh Offers Ingestion API - Platform Functions
  slug: punchh-platform-functions-offers-ingestion
- description: Subscriptions is an add-on Punchh loyalty product that allows businesses to create subscription plans to generate up-front revenue and offers benefits in addition to the standard benefits that unsubsc
  name: Punchh Subscription API - Platform Functions
  slug: punchh-platform-functions-subscription
- description: Punchh provides robust APIs for integrating POS (Point-of-Sale) terminals with its back end. The integration helps businesses to offer their customers loyalty programs directly from their POS systems.
  name: Punchh POS API
  slug: punchh-pos-api
- description: For more information, see POS Module 6 - Redemptions. Published by PAR on the pos section of the PAR developer portal; 6 operations. Certification required.
  name: Punchh Redemptions 1.0 (Legacy) API - POS
  slug: punchh-pos-redemptions-legacy
- description: 'The Redemptions 2.0 protocol has been designed to replace the legacy Redemptions 1.0 endpoints. The new protocol allows for the following features: - Single-scan flow support - Batching of redemptions'
  name: Punchh Redemptions 2.0 (New) API - POS
  slug: punchh-pos-redemptions-v2
artifact_total: 102
asyncapis:
- description: ''
  name: Punchh Webhooks
  slug: punchh-webhooks
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mobile API
  slug: open-punchh-mobile-api
- collection_type: open
  name: Redemptions 1.0 (Legacy) API - Mobile
  slug: open-punchh-mobile-redemptions-legacy
- collection_type: open
  name: Redemptions 2.0 (New) API - Mobile
  slug: open-punchh-mobile-redemptions-v2
- collection_type: open
  name: Subscription API - Mobile
  slug: open-punchh-mobile-subscription
- collection_type: open
  name: PAR Punchh Mobile API
  slug: open-punchh-mobile
- collection_type: open
  name: Redemptions 1.0 (Legacy) API - Online Ordering
  slug: open-punchh-online-ordering-redemptions-legacy
- collection_type: open
  name: Redemptions 2.0 (New) API - Online Ordering
  slug: open-punchh-online-ordering-redemptions-v2
- collection_type: open
  name: Online Ordering and SSO API
  slug: open-punchh-online-ordering-sso-api
- collection_type: open
  name: Subscription API - Online Ordering
  slug: open-punchh-online-ordering-subscription
- collection_type: open
  name: PAR Punchh Online Ordering and SSO API
  slug: open-punchh-online-ordering
- collection_type: open
  name: Platform Functions API
  slug: open-punchh-platform-functions-api
- collection_type: open
  name: Headless Offers API - Platform Functions
  slug: open-punchh-platform-functions-headless-offers
- collection_type: open
  name: Offers Ingestion API - Platform Functions
  slug: open-punchh-platform-functions-offers-ingestion
- collection_type: open
  name: Subscription API - Platform Functions
  slug: open-punchh-platform-functions-subscription
- collection_type: open
  name: PAR Punchh Platform Functions API
  slug: open-punchh-platform-functions
- collection_type: open
  name: POS API
  slug: open-punchh-pos-api
- collection_type: open
  name: Redemptions 1.0 (Legacy) API - POS
  slug: open-punchh-pos-redemptions-legacy
- collection_type: open
  name: Redemptions 2.0 (New) API - POS
  slug: open-punchh-pos-redemptions-v2
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
- group: design
  title: ''
  type: Conventions
  url: conventions/punchh-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/punchh-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/punchh-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/punchh-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.punchh.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/punchh-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/punchh-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/punchh-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/punchh-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/punchh-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/punchh-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/punchh-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/punchh-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/punchh-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/punchh-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partech.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://punchh.com/contact/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.partech.com/docs/dev-portal-developer-resources
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://punchh.com/security/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/par-tech/workspace/par-tech-apis-official
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
finops:
- name: Punchh Finops
  service_category: Loyalty + Guest Engagement
  slug: punchh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/punchh.png
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
mcp_servers:
- description: ''
  name: Punchh MCP Server
  slug: punchh-mcp-server
modified: '2026-08-13'
name: Punchh
nav: Providers
network: true
overview: 'Punchh publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Mobile API, Redemptions 1.0 (Legacy) API - Mobile, Redemptions 2.0 (New) API - Mobile, and 12 more. Tagged areas include Gift Cards, Guest Engagement, Loyalty, Marketing, and Mobile.


  The Punchh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 4 JSON-LD contexts, and 2 Spectral governance rulesets.


  Punchh''s developer surface includes authentication, documentation, developer portal, getting-started guide, engineering blog, sandbox, changelog, and 33 more developer resources.'
plans:
- name: Punchh Plans Pricing
  plan_count: 1
  slug: punchh-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Punchh Rate Limits
  slug: punchh-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Punchh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: punchh-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  name: Punchh API Rules
  rule_count: 37
  severity_counts:
    error: 3
    hint: 0
    info: 11
    warn: 23
  slug: punchh-spectral-rules
score:
  band: exemplar
  composite: 67.6
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 59.1
    contract_quality: 59.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 59.1
    operational_transparency: 92.1
  previous_composite: 67.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 42.3
      derived: 11
      marker_coverage: 42.3
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/screenshots/punchh-2026-06-20T192311.png
security:
- kind: authentication
  name: Punchh Authentication
  slug: punchh-authentication
  summary_line: http/apiKey/oauth2-flavoured · 7 schemes
- kind: domain-security
  name: Punchh Domain Security
  slug: punchh-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Punchh Vulnerability Disclosure
  slug: punchh-vulnerability-disclosure
  summary_line: Hackerone
slug: punchh
tags:
- Gift Cards
- Guest Engagement
- Loyalty
- Marketing
- Mobile
- Offers
- Online Ordering
- PAR Technology
- Point-of-Sale
- Restaurant
- Restaurant Technology
- Webhook
website: https://punchh.com/
---
