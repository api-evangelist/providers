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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Thanx Agentic Access
  operation_count: 30
  slug: thanx-agentic-access
  summary_line: 30 operations · 13 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: Retrieve a user's loyalty account, rewards, and points balances.
  name: Thanx Account API
  slug: thanx-account-api
- description: Acquire privileged end-user access tokens.
  name: Thanx Auth API
  slug: thanx-auth-api
- description: Create and update ordering baskets and redeem rewards or points products.
  name: Thanx Baskets API
  slug: thanx-baskets-api
- description: Create, retrieve, list campaigns and issue rewards.
  name: Thanx Campaigns API
  slug: thanx-campaigns-api
- description: Register and manage payment cards for card-linked loyalty.
  name: Thanx Cards API
  slug: thanx-cards-api
- description: Create, retrieve, and delete digital gift cards.
  name: Thanx Gift Cards API
  slug: thanx-gift-cards-api
- description: Track and revoke asynchronous reward issuance jobs.
  name: Thanx Issuance Jobs API
  slug: thanx-issuance-jobs-api
- description: Retrieve merchant locations.
  name: Thanx Locations API
  slug: thanx-locations-api
- description: Look up merchants, locations, and scopes.
  name: Thanx Metadata API
  slug: thanx-metadata-api
- description: Points balances, products, experiences, and multipliers.
  name: Thanx Points API
  slug: thanx-points-api
- description: Retrieve and report consumer purchases.
  name: Thanx Purchases API
  slug: thanx-purchases-api
- description: Retrieve, activate, finalize, and grant loyalty rewards.
  name: Thanx Rewards API
  slug: thanx-rewards-api
- description: Ingest marketing subscribers.
  name: Thanx Subscribers API
  slug: thanx-subscribers-api
- description: Create, retrieve, update, and delete Thanx users.
  name: Thanx Users API
  slug: thanx-users-api
artifact_total: 134
collections:
- collection_type: postman
  name: Thanx Consumer Account API
  slug: postman-thanx-account-api
- collection_type: postman
  name: Thanx Consumer Account Auth API
  slug: postman-thanx-auth-api
- collection_type: postman
  name: Thanx Consumer Account Baskets API
  slug: postman-thanx-baskets-api
- collection_type: postman
  name: Thanx Consumer Account Campaigns API
  slug: postman-thanx-campaigns-api
- collection_type: postman
  name: Thanx Consumer Account Cards API
  slug: postman-thanx-cards-api
- collection_type: postman
  name: Thanx Consumer Account Gift Cards API
  slug: postman-thanx-gift-cards-api
- collection_type: postman
  name: Thanx Consumer Account Issuance Jobs API
  slug: postman-thanx-issuance-jobs-api
- collection_type: postman
  name: Thanx Consumer Account Locations API
  slug: postman-thanx-locations-api
- collection_type: postman
  name: Thanx Consumer Account Metadata API
  slug: postman-thanx-metadata-api
- collection_type: postman
  name: Thanx Consumer Account Points API
  slug: postman-thanx-points-api
- collection_type: postman
  name: Thanx Consumer Account Purchases API
  slug: postman-thanx-purchases-api
- collection_type: postman
  name: Thanx Consumer Account Rewards API
  slug: postman-thanx-rewards-api
- collection_type: postman
  name: Thanx Consumer Account Subscribers API
  slug: postman-thanx-subscribers-api
- collection_type: postman
  name: Thanx Consumer Account Users API
  slug: postman-thanx-users-api
- collection_type: open
  name: Thanx Consumer API
  slug: open-thanx-consumer-api
- collection_type: open
  name: Thanx Loyalty API
  slug: open-thanx-loyalty-api
- collection_type: open
  name: Thanx Partner API
  slug: open-thanx-partner-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thanx/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thanx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thanx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thanx-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.thanx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thanx.com/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thanx.com/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thanx.com/overview/integrating
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thanx.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thanx
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.thanx.com/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.thanx.com/data/changelog
- group: other
  title: ''
  type: BestPractices
  url: https://docs.thanx.com/consumer/best-practices/design
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.thanx.com/consumer/usage/errors
- group: docs
  title: Webhooks Overview
  type: Documentation
  url: https://docs.thanx.com/webhooks/overview
- group: docs
  title: Data Exports (Connex)
  type: Documentation
  url: https://docs.thanx.com/data/overview
- group: build
  title: MCP Server
  type: Tools
  url: https://docs.thanx.com/mcp
- group: docs
  title: AI Integration
  type: Documentation
  url: https://docs.thanx.com/ai/overview
- group: build
  title: Claude Code Skills (Agent Starter)
  type: Tools
  url: https://github.com/thanx/thanx-agent-starter
- group: build
  title: Postman API Collections
  type: CodeExamples
  url: https://docs.thanx.com/overview/api_collections
- group: design
  title: ''
  type: SpectralRules
  url: rules/thanx-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/thanx-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/thanx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thanx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thanx-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.thanx.com/blog
created: '2026-06-02'
description: Thanx is a customer engagement, loyalty, and marketing automation platform for restaurants and other offline businesses, built to acquire, engage, and retain best customers and grow customer lifetime value. The platform combines data infrastructure, lifecycle marketing, loyalty and CRM, and digital ordering experiences. Thanx is API-first and publishes a public developer portal documenting a Consumer API for custom consumer experiences, a Partner API for privileged integration use cases, and a Loyalty API for digital ordering and kiosk providers, along with webhooks and Connex data-export integrations to warehouses like Snowflake and BigQuery. Thanx serves roughly 500 brands and processes over a billion transactions annually. It also publishes a hosted Docs MCP server for natural-language API search and an open agent-skills starter kit.
examples:
- key_count: 5
  name: Consumer Api Authorization Example
  slug: consumer-api-authorization-example
- key_count: 3
  name: Consumer Api Birth Date Example
  slug: consumer-api-birth-date-example
- key_count: 1
  name: Consumer Api Card Envelope Example
  slug: consumer-api-card-envelope-example
- key_count: 5
  name: Consumer Api Card Example
  slug: consumer-api-card-example
- key_count: 4
  name: Consumer Api Gift Card Example
  slug: consumer-api-gift-card-example
- key_count: 9
  name: Consumer Api Location Example
  slug: consumer-api-location-example
- key_count: 3
  name: Consumer Api Pagination Example
  slug: consumer-api-pagination-example
- key_count: 7
  name: Consumer Api Purchase Example
  slug: consumer-api-purchase-example
- key_count: 1
  name: Consumer Api Reward Envelope Example
  slug: consumer-api-reward-envelope-example
- key_count: 16
  name: Consumer Api Reward Example
  slug: consumer-api-reward-example
- key_count: 1
  name: Consumer Api User Envelope Example
  slug: consumer-api-user-envelope-example
- key_count: 7
  name: Consumer Api User Example
  slug: consumer-api-user-example
- key_count: 7
  name: Consumer Api User Input Example
  slug: consumer-api-user-input-example
- key_count: 5
  name: Loyalty Api Account Example
  slug: loyalty-api-account-example
- key_count: 3
  name: Loyalty Api Basket Example
  slug: loyalty-api-basket-example
- key_count: 9
  name: Loyalty Api Basket Input Example
  slug: loyalty-api-basket-input-example
- key_count: 5
  name: Loyalty Api Basket Item Example
  slug: loyalty-api-basket-item-example
- key_count: 5
  name: Loyalty Api Loyalty Reward Example
  slug: loyalty-api-loyalty-reward-example
- key_count: 4
  name: Loyalty Api Payment Example
  slug: loyalty-api-payment-example
- key_count: 3
  name: Loyalty Api Points Product Example
  slug: loyalty-api-points-product-example
- key_count: 10
  name: Partner Api Campaign Example
  slug: partner-api-campaign-example
- key_count: 9
  name: Partner Api Campaign Input Example
  slug: partner-api-campaign-input-example
- key_count: 2
  name: Partner Api Campaign Variant Input Example
  slug: partner-api-campaign-variant-input-example
- key_count: 7
  name: Partner Api Issuance Job Example
  slug: partner-api-issuance-job-example
- key_count: 5
  name: Partner Api Partner User Example
  slug: partner-api-partner-user-example
features:
- description: Configurable loyalty programs with points, tiers, rewards, multipliers, and reward templates across in-store and online venues.
  name: Loyalty & Rewards
- description: Campaign creation with treatment/control variants and batched reward issuance to targeted audiences.
  name: Lifecycle Marketing
- description: Unified customer profiles, communication settings, tags, and NPS feedback backed by warehouse data exports.
  name: CRM & Data Infrastructure
- description: Basket lifecycle and account APIs for digital ordering, kiosk, and pay-at-table integrations.
  name: Digital Ordering & Pay
- description: Register payment cards to attribute purchases automatically for card-linked loyalty earning.
  name: Card-Linked Loyalty
- description: Real-time events for purchases, reward issuance, reward batch completion, SMS subscriptions, and communication settings.
  name: Webhooks
finops:
- name: Thanx Finops
  service_category: Customer Engagement + Loyalty
  slug: thanx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thanx.png
integrations:
- description: Online ordering provider referenced in purchase order providers.
  name: Olo
- description: POS / ordering provider referenced in purchase order providers.
  name: Toast
- description: Connex data-export destination.
  name: Snowflake
- description: Connex data-export destination.
  name: Google BigQuery
- description: Connex data-export destination.
  name: Amazon Redshift
- description: Connex data-export destination.
  name: Databricks
- description: Private connectivity option for the Loyalty API.
  name: AWS PrivateLink
json_schemas:
- name: Authorization
  property_count: 5
  slug: consumer-api-authorization
- name: BirthDate
  property_count: 3
  slug: consumer-api-birth-date
- name: CardEnvelope
  property_count: 1
  slug: consumer-api-card-envelope
- name: Card
  property_count: 5
  slug: consumer-api-card
- name: GiftCard
  property_count: 4
  slug: consumer-api-gift-card
- name: Location
  property_count: 9
  slug: consumer-api-location
- name: Pagination
  property_count: 3
  slug: consumer-api-pagination
- name: Purchase
  property_count: 7
  slug: consumer-api-purchase
- name: RewardEnvelope
  property_count: 1
  slug: consumer-api-reward-envelope
- name: Reward
  property_count: 16
  slug: consumer-api-reward
- name: UserEnvelope
  property_count: 1
  slug: consumer-api-user-envelope
- name: UserInput
  property_count: 7
  slug: consumer-api-user-input
- name: User
  property_count: 7
  slug: consumer-api-user
- name: Account
  property_count: 5
  slug: loyalty-api-account
- name: BasketInput
  property_count: 9
  slug: loyalty-api-basket-input
- name: BasketItem
  property_count: 5
  slug: loyalty-api-basket-item
- name: Basket
  property_count: 3
  slug: loyalty-api-basket
- name: LoyaltyReward
  property_count: 5
  slug: loyalty-api-loyalty-reward
- name: Payment
  property_count: 4
  slug: loyalty-api-payment
- name: PointsProduct
  property_count: 3
  slug: loyalty-api-points-product
- name: CampaignInput
  property_count: 9
  slug: partner-api-campaign-input
- name: Campaign
  property_count: 10
  slug: partner-api-campaign
- name: CampaignVariantInput
  property_count: 2
  slug: partner-api-campaign-variant-input
- name: IssuanceJob
  property_count: 7
  slug: partner-api-issuance-job
- name: PartnerUser
  property_count: 5
  slug: partner-api-partner-user
json_structures:
- name: Consumer Api Authorization Structure
  property_count: 5
  slug: consumer-api-authorization-structure
- name: Consumer Api Birth Date Structure
  property_count: 3
  slug: consumer-api-birth-date-structure
- name: Consumer Api Card Envelope Structure
  property_count: 1
  slug: consumer-api-card-envelope-structure
- name: Consumer Api Card Structure
  property_count: 5
  slug: consumer-api-card-structure
- name: Consumer Api Gift Card Structure
  property_count: 4
  slug: consumer-api-gift-card-structure
- name: Consumer Api Location Structure
  property_count: 9
  slug: consumer-api-location-structure
- name: Consumer Api Pagination Structure
  property_count: 3
  slug: consumer-api-pagination-structure
- name: Consumer Api Purchase Structure
  property_count: 7
  slug: consumer-api-purchase-structure
- name: Consumer Api Reward Envelope Structure
  property_count: 1
  slug: consumer-api-reward-envelope-structure
- name: Consumer Api Reward Structure
  property_count: 16
  slug: consumer-api-reward-structure
- name: Consumer Api User Envelope Structure
  property_count: 1
  slug: consumer-api-user-envelope-structure
- name: Consumer Api User Input Structure
  property_count: 7
  slug: consumer-api-user-input-structure
- name: Consumer Api User Structure
  property_count: 7
  slug: consumer-api-user-structure
- name: Loyalty Api Account Structure
  property_count: 5
  slug: loyalty-api-account-structure
- name: Loyalty Api Basket Input Structure
  property_count: 9
  slug: loyalty-api-basket-input-structure
- name: Loyalty Api Basket Item Structure
  property_count: 5
  slug: loyalty-api-basket-item-structure
- name: Loyalty Api Basket Structure
  property_count: 3
  slug: loyalty-api-basket-structure
- name: Loyalty Api Loyalty Reward Structure
  property_count: 5
  slug: loyalty-api-loyalty-reward-structure
- name: Loyalty Api Payment Structure
  property_count: 4
  slug: loyalty-api-payment-structure
- name: Loyalty Api Points Product Structure
  property_count: 3
  slug: loyalty-api-points-product-structure
- name: Partner Api Campaign Input Structure
  property_count: 9
  slug: partner-api-campaign-input-structure
- name: Partner Api Campaign Structure
  property_count: 10
  slug: partner-api-campaign-structure
- name: Partner Api Campaign Variant Input Structure
  property_count: 2
  slug: partner-api-campaign-variant-input-structure
- name: Partner Api Issuance Job Structure
  property_count: 7
  slug: partner-api-issuance-job-structure
- name: Partner Api Partner User Structure
  property_count: 5
  slug: partner-api-partner-user-structure
jsonld:
- class_count: 13
  name: Thanx Consumer Api Context
  property_count: 56
  slug: thanx-consumer-api-context
- class_count: 7
  name: Thanx Loyalty Api Context
  property_count: 27
  slug: thanx-loyalty-api-context
- class_count: 5
  name: Thanx Partner Api Context
  property_count: 22
  slug: thanx-partner-api-context
layout: provider
modified: '2026-06-03'
name: Thanx
nav: Providers
network: true
overview: 'Thanx publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Baskets API, and 11 more. Tagged areas include Restaurant, Loyalty, Guest Engagement, Marketing, and CRM.


  The Thanx catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Thanx''s developer surface includes authentication, documentation, getting-started guide, pricing, changelog, tooling, code examples, and 19 more developer resources.'
plans:
- name: Thanx Plans Pricing
  plan_count: 1
  slug: thanx-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 3
  name: Thanx Rate Limits
  slug: thanx-rate-limits
rules:
- name: Thanx API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thanx-jsonschema-spectral-rules
- name: Thanx API Rules
  rule_count: 40
  severity_counts:
    error: 6
    hint: 0
    info: 10
    warn: 24
  slug: thanx-spectral-rules
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 82.2
    developer_ergonomics: 45.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thanx/refs/heads/main/screenshots/thanx-2026-06-20T195212.png
security:
- kind: authentication
  name: Thanx Authentication
  slug: thanx-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Thanx Domain Security
  slug: thanx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thanx
tags:
- Restaurant
- Loyalty
- Guest Engagement
- Marketing
- CRM
- Online Ordering
- Webhooks
- Points
- Rewards
- Campaigns
use_cases:
- description: Build a custom branded app on the Consumer API with SSO, rewards, points, and purchase history.
  name: Branded Loyalty App
- description: Partners create campaigns and issue rewards to large audiences via batched issuance jobs.
  name: Targeted Reward Campaigns
- description: Ordering and kiosk providers connect baskets to a brand loyalty program to apply rewards and points.
  name: Kiosk & Online Ordering Loyalty
- description: Export Thanx data models to Snowflake, BigQuery, Redshift, or Databricks for analytics.
  name: Warehouse Analytics
website: https://www.thanx.com/
---
