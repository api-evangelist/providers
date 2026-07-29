---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 8
  human_in_the_loop: 0
  name: Tiktok Agentic Access
  operation_count: 19
  slug: tiktok-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 10
apis:
- description: Ad group (ad set) management
  name: TikTok Ad Groups API
  slug: tiktok-ad-groups-api
- description: Individual ad management
  name: TikTok Ads API
  slug: tiktok-ads-api
- description: Custom audience management
  name: TikTok Audiences API
  slug: tiktok-audiences-api
- description: Advertising campaign management
  name: TikTok Campaigns API
  slug: tiktok-campaigns-api
- description: User data export operations
  name: TikTok Data Portability API
  slug: tiktok-data-portability-api
- description: Settlement and financial reporting
  name: TikTok Finance API
  slug: tiktok-finance-api
- description: Shipping and logistics operations
  name: TikTok Logistics API
  slug: tiktok-logistics-api
- description: Order management and fulfillment
  name: TikTok Orders API
  slug: tiktok-orders-api
- description: Product catalog management
  name: TikTok Products API
  slug: tiktok-products-api
- description: Campaign performance reporting
  name: TikTok Reporting API
  slug: tiktok-reporting-api
artifact_total: 38
collections:
- collection_type: postman
  name: TikTok API for Business Ad Groups API
  slug: postman-tiktok-ad-groups-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Ads API
  slug: postman-tiktok-ads-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Audiences API
  slug: postman-tiktok-audiences-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Campaigns API
  slug: postman-tiktok-campaigns-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Data Portability API
  slug: postman-tiktok-data-portability-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Finance API
  slug: postman-tiktok-finance-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Logistics API
  slug: postman-tiktok-logistics-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Orders API
  slug: postman-tiktok-orders-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Products API
  slug: postman-tiktok-products-api
- collection_type: postman
  name: TikTok API for Business Ad Groups Reporting API
  slug: postman-tiktok-reporting-api
- collection_type: open
  name: TikTok API for Business
  slug: open-tiktok-business
- collection_type: open
  name: TikTok Data Portability API
  slug: open-tiktok-data-portability
- collection_type: open
  name: TikTok Shop API
  slug: open-tiktok-shop
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tiktok/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiktok-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiktok-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiktok-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiktok
- group: company
  title: ''
  type: Website
  url: https://www.tiktok.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.tiktok.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tiktok.com/doc/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tiktok.com/doc/overview
- group: start
  title: ''
  type: Business API Portal
  url: https://business-api.tiktok.com/portal
- group: start
  title: ''
  type: Shop Partner Portal
  url: https://partner.tiktokshop.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiktok
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tiktok/tiktok-business-api-sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.tiktok.com/doc/changelog
- group: company
  title: ''
  type: Blog
  url: https://developers.tiktok.com/blog
- group: operate
  title: ''
  type: Forums
  url: https://developers.tiktok.com/community
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tiktok.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.tiktok.com/doc/tiktok-api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.tiktok.com/doc/tiktok-api-data-privacy
- group: start
  title: ''
  type: Signup
  url: https://developers.tiktok.com/
- group: start
  title: ''
  type: Login
  url: https://developers.tiktok.com/login
created: '2025-08-14'
description: TikTok is a short-form social video platform offering developers REST APIs for advertising, e-commerce, content discovery, and platform integrations. Key products include the TikTok API for Business (advertising and campaign management), TikTok Shop API (seller product and order management), and the Data Portability API.
examples:
- key_count: 2
  name: Tiktok Business Getcampaigns Example
  slug: tiktok-business-getCampaigns-example
- key_count: 2
  name: Tiktok Shop Listorders Example
  slug: tiktok-shop-listOrders-example
finops:
- name: Tiktok Finops
  service_category: Social Platform APIs
  slug: tiktok-finops
graphqls:
- description: 'This conceptual GraphQL schema models the TikTok platform''s APIs as a unified graph. It is derived from three primary REST API surfaces offered by TikTok for Developers:'
  name: TikTok GraphQL Schema
  slug: tiktok-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiktok.png
json_schemas:
- name: TikTok Campaign
  property_count: 9
  slug: tiktok-campaign
- name: TikTok Shop Order
  property_count: 7
  slug: tiktok-order
json_structures:
- name: Tiktok Campaign Structure
  property_count: 0
  slug: tiktok-campaign-structure
jsonld:
- class_count: 14
  name: Tiktok Context
  property_count: 0
  slug: tiktok-context
layout: provider
modified: '2026-05-19'
name: TikTok
nav: Providers
network: true
overview: 'TikTok publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Ad Groups API, Ads API, Audiences API, and 7 more. Tagged areas include Advertising, Commerce, Content, E-Commerce, and Social Media.


  The TikTok catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TikTok''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Tiktok Plans Pricing
  plan_count: 4
  slug: tiktok-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Tiktok Rate Limits
  slug: tiktok-rate-limits
rules:
- name: TikTok API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tiktok-jsonschema-spectral-rules
- name: TikTok API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: tiktok-rules
score:
  band: exemplar
  composite: 66.2
  delta: -1.9
  facets:
    commercial_clarity: 73.7
    contract_quality: 70.7
    developer_ergonomics: 52.2
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiktok/refs/heads/main/screenshots/tiktok-2026-06-20T195349.png
security:
- kind: authentication
  name: Tiktok Authentication
  slug: tiktok-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Tiktok Domain Security
  slug: tiktok-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiktok
tags:
- Advertising
- Commerce
- Content
- E-Commerce
- Social Media
- Video
website: https://www.tiktok.com/
---
