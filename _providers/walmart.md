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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 82
  human_in_the_loop: 2
  name: Walmart Agentic Access
  operation_count: 171
  slug: walmart-agentic-access
  summary_line: 171 operations · 82 acting · 2 human-in-the-loop
api_count: 25
apis:
- description: The Assortment Recommendations API from Walmart — 3 operation(s) for assortment recommendations.
  name: Walmart Assortment Recommendations API
  slug: walmart-assortment-recommendations-api
- description: The Authorization API from Walmart — 2 operation(s) for authorization.
  name: Walmart Authorization API
  slug: walmart-authorization-api
- description: The DSV Cost API from Walmart — 1 operation(s) for dsv cost.
  name: Walmart DSV Cost API
  slug: walmart-dsv-cost-api
- description: The DSV Orders API from Walmart — 6 operation(s) for dsv orders.
  name: Walmart DSV Orders API
  slug: walmart-dsv-orders-api
- description: The Feeds API from Walmart — 3 operation(s) for feeds.
  name: Walmart Feeds API
  slug: walmart-feeds-api
- description: The Fulfillment API from Walmart — 21 operation(s) for fulfillment.
  name: Walmart Fulfillment API
  slug: walmart-fulfillment-api
- description: The Insight API from Walmart — 7 operation(s) for insight.
  name: Walmart Insight API
  slug: walmart-insight-api
- description: The Inventory API from Walmart — 6 operation(s) for inventory.
  name: Walmart Inventory API
  slug: walmart-inventory-api
- description: The Items API from Walmart — 13 operation(s) for items.
  name: Walmart Items API
  slug: walmart-items-api
- description: The Lag Time API from Walmart — 2 operation(s) for lag time.
  name: Walmart Lag Time API
  slug: walmart-lag-time-api
- description: The Listing Quality API from Walmart — 3 operation(s) for listing quality.
  name: Walmart Listing Quality API
  slug: walmart-listing-quality-api
- description: The Notifications API from Walmart — 4 operation(s) for notifications.
  name: Walmart Notifications API
  slug: walmart-notifications-api
- description: The On-Request Report API from Walmart — 3 operation(s) for on-request report.
  name: Walmart On-Request Report API
  slug: walmart-on-request-report-api
- description: The On Request Reports API from Walmart — 3 operation(s) for on request reports.
  name: Walmart On Request Reports API
  slug: walmart-on-request-reports-api
- description: The Orders API from Walmart — 7 operation(s) for orders.
  name: Walmart Orders API
  slug: walmart-orders-api
- description: The Pre-Generated Reports API from Walmart — 1 operation(s) for pre-generated reports.
  name: Walmart Pre-Generated Reports API
  slug: walmart-pre-generated-reports-api
- description: The Prices API from Walmart — 8 operation(s) for prices.
  name: Walmart Prices API
  slug: walmart-prices-api
- description: The Promotions API from Walmart — 3 operation(s) for promotions.
  name: Walmart Promotions API
  slug: walmart-promotions-api
- description: The Reports API from Walmart — 7 operation(s) for reports.
  name: Walmart Reports API
  slug: walmart-reports-api
- description: The Returns/Refunds API from Walmart — 3 operation(s) for returns/refunds.
  name: Walmart Returns/Refunds API
  slug: walmart-returns-refunds-api
- description: The Reviews API from Walmart — 3 operation(s) for reviews.
  name: Walmart Reviews API
  slug: walmart-reviews-api
- description: The Rules API from Walmart — 14 operation(s) for rules.
  name: Walmart Rules API
  slug: walmart-rules-api
- description: The Settings API from Walmart — 11 operation(s) for settings.
  name: Walmart Settings API
  slug: walmart-settings-api
- description: The Ship with Walmart API from Walmart — 7 operation(s) for ship with walmart.
  name: Walmart Ship with Walmart API
  slug: walmart-ship-with-walmart-api
- description: The Utilities API from Walmart — 4 operation(s) for utilities.
  name: Walmart Utilities API
  slug: walmart-utilities-api
artifact_total: 44
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/walmart-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/walmart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walmart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/walmart-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/walmartlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/walmart
- group: start
  title: ''
  type: Portal
  url: https://developer.walmart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.walmart.com/home/us-mp/
- group: start
  title: ''
  type: Sandbox
  url: https://developer.walmart.com/doc/sandbox/
- group: other
  title: ''
  type: Whats New
  url: https://developer.walmart.com/category/us/whats-new/
- group: operate
  title: ''
  type: Support
  url: https://developer.walmart.com/home/help/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.walmart.com/faq/us/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.walmart.com/apiStatus
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.walmart.com/faq/terms-and-conditions
- group: other
  title: ''
  type: Summary
  url: ''
created: 2023/11/15
description: Walmart is a multinational retail corporation that operates a chain of hypermarkets, discount department stores, and grocery stores. The company is known for offering a wide range of products at competitive prices, attracting customers from all walks of life. Walmart also provides various convenience services, such as pharmacy, optical, and financial services, making it a one-stop shop for many consumers. The Walmart Marketplace APIs enable third-party sellers to list and sell products, manage orders, inventory, pricing, fulfillment, and reporting on Walmart.com.
examples:
- key_count: 2
  name: Walmart Marketplace Inventory Updateinventory Example
  slug: walmart-marketplace-inventory-updateInventory-example
- key_count: 2
  name: Walmart Marketplace Orders Listorders Example
  slug: walmart-marketplace-orders-listOrders-example
features:
- 'Walmart: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Walmart Marketplace APIs require Marketplace seller approval; commission rates 6-15% by category.
finops:
- name: Walmart Finops
  service_category: Retail / Marketplace
  slug: walmart-finops
graphqls:
- description: This conceptual GraphQL schema represents the Walmart Marketplace API surface, covering the full lifecycle of retail commerce operations available through the [Walmart Developer Portal](https://develo
  name: Walmart GraphQL Schema
  slug: walmart-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walmart.png
json_schemas:
- name: Walmart Marketplace Inventory
  property_count: 3
  slug: walmart-inventory
- name: Walmart Marketplace Order
  property_count: 6
  slug: walmart-order
json_structures:
- name: Walmart Order Structure
  property_count: 0
  slug: walmart-order-structure
jsonld:
- class_count: 6
  name: Walmart Context
  property_count: 17
  slug: walmart-context
layout: provider
modified: '2026-05-30'
name: Walmart
nav: Providers
network: true
overview: 'Walmart publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Assortment Recommendations API, Authorization API, DSV Cost API, and 22 more. Tagged areas include Commerce, Retail, and Fortune 100.


  The Walmart catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Walmart''s developer surface includes authentication, developer portal, documentation, sandbox, support, FAQ, and 8 more developer resources.'
plans:
- name: Walmart Plans Pricing
  plan_count: 1
  slug: walmart-plans-pricing
press:
- date: '2026-05-25'
  title: Walmart is restructuring its staff to focus on expansion of AI ...
  url: https://www.facebook.com/fox6news/posts/walmart-is-restructuring-its-staff-to-focus-on-expansion-of-ai-and-tech-initiati/1558661845847300/
- date: '2026-05-25'
  title: Walmart Unveils New AI-Powered Tools To Empower 1.5 ...
  url: https://corporate.walmart.com/news/2025/06/24/walmart-unveils-new-ai-powered-tools-to-empower-1-5-million-associates
- date: '2026-05-25'
  title: Walmart Reveals Plan for Scaling Artificial Intelligence ...
  url: https://corporate.walmart.com/news/2024/10/09/walmart-reveals-plan-for-scaling-artificial-intelligence-generative-ai-augmented-reality-and-immersive-commerce-experiences
- date: '2026-05-25'
  title: Walmart and Google Turn AI Discovery Into Effortless ...
  url: https://corporate.walmart.com/news/2026/01/11/walmart-and-google-turn-ai-discovery-into-effortless-shopping-experiences
- date: '2026-05-25'
  title: Walmart Partners with OpenAI to Create AI-First Shopping ...
  url: https://corporate.walmart.com/news/2025/10/14/walmart-partners-with-openai-to-create-ai-first-shopping-experiences
random_paper: 12
rate_limits:
- limit_count: 1
  name: Walmart Rate Limits
  slug: walmart-rate-limits
rules:
- name: Walmart API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: walmart-jsonschema-spectral-rules
- name: Walmart API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: walmart-rules
score:
  band: developing
  composite: 52.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.3
    developer_ergonomics: 39.1
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 52.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walmart/refs/heads/main/screenshots/walmart-2026-06-20T201220.png
security:
- kind: authentication
  name: Walmart Authentication
  slug: walmart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Walmart Domain Security
  slug: walmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Walmart Vulnerability Disclosure
  slug: walmart-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: walmart
tags:
- Commerce
- Retail
- Fortune 100
website: https://developer.walmart.com/
---
