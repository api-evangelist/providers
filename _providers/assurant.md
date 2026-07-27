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
- acting_count: 2
  human_in_the_loop: 0
  name: Assurant Agentic Access
  operation_count: 5
  slug: assurant-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 5
apis:
- description: The Assurant Global Housing API provides property management companies and housing partners with programmatic access to insurance products including renter's insurance, lender-placed insurance, and pr
  name: Assurant Global Housing API
  slug: global-housing-api
- description: Claims filing and management
  name: Assurant Claims API
  slug: assurant-claims-api
- description: Customer enrollment operations
  name: Assurant Enrollments API
  slug: assurant-enrollments-api
- description: Insurance policy management
  name: Assurant Policies API
  slug: assurant-policies-api
- description: Insurance product catalog
  name: Assurant Products API
  slug: assurant-products-api
artifact_total: 24
collections:
- collection_type: open
  name: Assurant APEX Embedded Insurance API
  slug: open-assurant-apex-insurance-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/assurant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assurant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/assurant-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assurantlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/assurant
- group: start
  title: Assurant Website
  type: Portal
  url: https://www.assurant.com/
- group: start
  title: APEX Partner Platform
  type: Portal
  url: https://www.assurant.com/partner-with-us/apex
- group: start
  title: Partner with Assurant
  type: Signup
  url: https://www.assurant.com/partner-with-us/apex
created: '2024-01-15'
description: Assurant is a global provider of lifestyle and housing solutions that help people thrive in a connected world. The company provides protection products and services including device protection, renter's insurance, auto F&I products, and connected living services. Assurant's APEX (Assurant Product Experience Exchange) platform provides embedded insurance APIs that enable partners to integrate protection products, claims management, and diagnostics directly into their workflows and customer experiences. The APEX platform supports 99.95% uptime and covers multiple product lines across technology, real estate, auto, and retail industries.
features:
- description: APIs for embedding smartphone, tablet, and consumer electronics protection programs directly into carrier, retailer, and OEM customer experiences.
  name: Embedded Device Protection
- description: End-to-end claims management APIs supporting claim filing, status tracking, device diagnostics, and repair/replacement fulfillment.
  name: Claims Management
- description: API integration for embedding renter's insurance enrollment, policy management, and claims into property management platforms.
  name: Renter's Insurance
- description: Finance and insurance product APIs for automotive dealers including vehicle service contracts, GAP insurance, and protection products.
  name: Auto F&I Products
- description: Smart home device protection and tech support service APIs for connected device ecosystems.
  name: Connected Living Services
finops:
- name: Assurant Finops
  service_category: API
  slug: assurant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/assurant.png
integrations:
- description: Integration with mobile carrier billing and CRM systems for device protection plan enrollment and premium collection.
  name: Carrier Billing Systems
- description: Integration with property management software including Yardi, RealPage, and AppFolio for renter's insurance programs.
  name: Property Management Platforms
- description: Integration with automotive DMS platforms for F&I product enrollment and vehicle protection program management.
  name: Dealer Management Systems
layout: provider
modified: '2026-05-19'
name: Assurant
nav: Providers
network: true
overview: 'Assurant publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Enrollments API, Policies API, and 1 more. Tagged areas include Insurance, Device Protection, Embedded Insurance, Housing, and Claims.


  Assurant''s developer surface includes authentication, developer portal, signup flow, and 5 more developer resources.'
plans:
- name: Assurant Plans Pricing
  plan_count: 3
  slug: assurant-plans-pricing
press:
- date: '2026-05-25'
  title: 'Consumers Trade Up for AI: Assurant Reports Record ...'
  url: https://www.businesswire.com/news/home/20251204879367/en/Consumers-Trade-Up-for-AI-Assurant-Reports-Record-%241.59-Billion-Returned-in-Third-Quarter-Through-Mobile-Trade-In-Programs
- date: '2026-05-25'
  title: News & Insights
  url: https://www.assurant.ca/news-insights
- date: '2026-05-25'
  title: Hello, Las Vegas! The Assurant team has arrived at CES ...
  url: https://www.facebook.com/AssurantInc/posts/hello-las-vegas-the-assurant-team-has-arrived-at-ces-2026-and-is-ready-to-share-/1321253986709533/
- date: '2026-05-25'
  title: Insurance & Tech Industry Insights | Assurant Research Hub
  url: https://www.assurant.com/industry-insights
- date: '2026-05-25'
  title: 'Building Trust in Enterprise AI: a Human-Centric Approach'
  url: https://www.assurant.com/news-insights/articles/human-approach-to-enterprise-ai
random_paper: 65
rate_limits:
- limit_count: 5
  name: Assurant Rate Limits
  slug: assurant-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.4
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/assurant/refs/heads/main/screenshots/assurant-2026-06-20T172509.png
security:
- kind: authentication
  name: Assurant Authentication
  slug: assurant-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Assurant Domain Security
  slug: assurant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: assurant
tags:
- Insurance
- Device Protection
- Embedded Insurance
- Housing
- Claims
- Fortune 500
use_cases:
- description: Mobile carriers integrate APEX APIs to offer device protection plans at point of sale and manage claims for damaged or lost devices.
  name: Mobile Carrier Device Protection
- description: Property management companies integrate the Global Housing API to offer and track renter's insurance compliance among tenants.
  name: Property Management Renters Insurance
- description: Auto dealers and F&I providers integrate Assurant's vehicle protection APIs into dealer management systems for protection product sales.
  name: Auto Dealer F&I Integration
- description: Retailers integrate APEX APIs to offer product protection programs at checkout for electronics, appliances, and other products.
  name: E-Commerce Protection Programs
website: https://www.assurant.com/
---
