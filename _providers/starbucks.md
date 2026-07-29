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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Starbucks Agentic Access
  operation_count: 10
  slug: starbucks-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 5
apis:
- description: Starbucks Rewards loyalty program operations
  name: Starbucks Loyalty API
  slug: starbucks-loyalty-api
- description: Menu categories and items operations
  name: Starbucks Menu API
  slug: starbucks-menu-api
- description: Ordering and cart management operations
  name: Starbucks Orders API
  slug: starbucks-orders-api
- description: API health and status operations
  name: Starbucks Status API
  slug: starbucks-status-api
- description: Store location and search operations
  name: Starbucks Stores API
  slug: starbucks-stores-api
artifact_total: 25
collections:
- collection_type: open
  name: Starbucks API
  slug: open-starbucks-starbucks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/starbucks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starbucks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/starbucks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starbucks
- group: company
  title: ''
  type: Website
  url: https://www.starbucks.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.starbucks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.starbucks.com/
- group: company
  title: ''
  type: About
  url: https://www.starbucks.com/about-us/company-information/starbucks-company-timeline
- group: company
  title: ''
  type: Careers
  url: https://www.starbucks.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starbucks.com/responsibility/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starbucks.com/about-us/company-information/online-policies/terms-of-use
- group: other
  title: ''
  type: X
  url: https://x.com/Starbucks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/starbucks
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Starbucks
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/starbucks
created: '2024-01-01'
description: Starbucks provides partner APIs for ordering, loyalty program integration, store locations, and menu data through their developer portal. These APIs enable authorized partners to integrate Starbucks ordering, rewards, and store discovery into their applications.
examples:
- key_count: 2
  name: Starbucks Create Order Example
  slug: starbucks-create-order-example
- key_count: 2
  name: Starbucks Get Loyalty Account Example
  slug: starbucks-get-loyalty-account-example
- key_count: 2
  name: Starbucks List Menu Categories Example
  slug: starbucks-list-menu-categories-example
- key_count: 2
  name: Starbucks List Stores Example
  slug: starbucks-list-stores-example
finops:
- name: Starbucks Finops
  service_category: Food & Beverage / Retail
  slug: starbucks-finops
graphqls:
- description: This conceptual GraphQL schema models the Starbucks platform — covering store locations, menu items, ordering, loyalty rewards, payments, and customer profiles. It is derived from publicly available i
  name: Starbucks GraphQL Schema
  slug: starbucks-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/starbucks.png
json_schemas:
- name: Starbucks Loyalty Account
  property_count: 7
  slug: starbucks-loyalty-account
- name: Menu Item
  property_count: 11
  slug: starbucks-menu-item
- name: Starbucks Store
  property_count: 11
  slug: starbucks-store
json_structures:
- name: Starbucks Menu Item Structure
  property_count: 0
  slug: starbucks-menu-item-structure
- name: Starbucks Store Structure
  property_count: 0
  slug: starbucks-store-structure
jsonld:
- class_count: 32
  name: Starbucks Context
  property_count: 5
  slug: starbucks-context
layout: provider
modified: '2026-05-19'
name: Starbucks
nav: Providers
network: true
overview: 'Starbucks publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Loyalty API, Menu API, Orders API, and 2 more. Tagged areas include Coffee, Food Service, Loyalty, Ordering, and Retail.


  The Starbucks catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Starbucks'' developer surface includes authentication, developer portal, documentation, and 12 more developer resources.'
plans:
- name: Starbucks Plans Pricing
  plan_count: 1
  slug: starbucks-plans-pricing
press:
- date: '2026-05-25'
  title: Starbucks is sunsetting its AI inventory program after it ...
  url: https://www.facebook.com/KIRO7Seattle/posts/starbucks-is-sunsetting-its-ai-inventory-program-after-it-reportedly-miscounted-/1404923738337353/
- date: '2026-05-25'
  title: Starbucks ditches AI inventory system after just 9 months
  url: https://www.restaurantdive.com/news/Starbucks-eliminates-computer-vision-ai-inventory-system/820934/
- date: '2026-05-25'
  title: Supporting the moments that matter with artificial intelligence
  url: https://about.starbucks.com/press/2026/supporting-the-moments-that-matter-with-artificial-intelligence/
- date: '2026-05-25'
  title: 'Meet Green Dot Assist: Starbucks Generative AI-Powered ...'
  url: https://about.starbucks.com/press/2025/meet-green-dot-assist-starbucks-generative-ai-powered-coffeehouse-companion/
- date: '2026-05-25'
  title: News Blog
  url: https://about.starbucks.com/press/news-blog/
random_paper: 18
rate_limits:
- limit_count: 1
  name: Starbucks Rate Limits
  slug: starbucks-rate-limits
rules:
- name: Starbucks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: starbucks-jsonschema-spectral-rules
- name: Starbucks API Rules
  rule_count: 18
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 12
  slug: starbucks-rules
score:
  band: developing
  composite: 48.6
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.1
    developer_ergonomics: 28.3
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starbucks/refs/heads/main/screenshots/starbucks-2026-06-20T194508.png
security:
- kind: authentication
  name: Starbucks Authentication
  slug: starbucks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Starbucks Domain Security
  slug: starbucks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starbucks
tags:
- Coffee
- Food Service
- Loyalty
- Ordering
- Retail
- Fortune 500
website: https://www.starbucks.com/
---
