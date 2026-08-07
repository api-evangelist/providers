---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The Drip REST API provides programmatic access to accounts, subscribers, events, email series campaigns, single-email campaigns (broadcasts), workflows, workflow triggers, tags, custom fields, convers
  name: Drip REST API
  slug: drip-rest-api
- description: The Drip OAuth 2.0 API authorizes public integrations to act on behalf of Drip users. It exposes the authorize and token endpoints needed to obtain access tokens for the Drip REST API.
  name: Drip OAuth 2.0 API
  slug: drip-oauth-api
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drip.com
- group: start
  title: ''
  type: Portal
  url: https://developer.drip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.drip.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.drip.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.drip.com/#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.drip.com/#rate-limiting
- group: start
  title: ''
  type: Signup
  url: https://www.getdrip.com/signup
- group: start
  title: ''
  type: Console
  url: https://www.getdrip.com/user/applications
- group: operate
  title: ''
  type: StatusPage
  url: https://status.drip.com
- group: operate
  title: ''
  type: Support
  url: https://help.drip.com/
- group: company
  title: ''
  type: Blog
  url: https://www.drip.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.drip.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drip.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drip.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DripEmail
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drip-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getdrip
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DripEmail/drip-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DripEmail/drip-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DripEmail/drip-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DripEmail/drip-dot-net
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DripEmail/omniauth-drip
created: '2026-05-25'
description: Drip is a Minneapolis-based ecommerce marketing automation platform that combines email, SMS, popups, and workflow-driven customer journeys for direct-to-consumer brands. The Drip REST API v2 and v3 exposes accounts, subscribers, events, campaigns, broadcasts, workflows, tags, custom fields, conversions, orders, cart activity, product activity, forms, webhooks, and shopper activity endpoints for building deep ecommerce integrations and data pipelines.
features:
- description: Drag-and-drop visual email builder with branded templates, conditional content, and dynamic ecommerce blocks.
  name: Email Marketing
- description: Two-way SMS campaigns and automations alongside email in a single workflow.
  name: SMS Marketing
- description: Visual multi-step automation builder with branching logic, delays, and ecommerce-aware triggers.
  name: Workflows
- description: Behavioral and ecommerce segmentation across subscriber events, tags, custom fields, and shopper activity.
  name: Segmentation
- description: Onsite forms, popups, and embedded forms for list growth and lead capture.
  name: Forms and Popups
- description: Public REST API at api.getdrip.com covering subscribers, events, campaigns, workflows, orders, and shopper activity.
  name: REST API v2 and v3
- description: Outbound webhooks for subscriber lifecycle, email engagement, conversions, and ecommerce activity.
  name: Webhooks
- description: OAuth 2.0 authorization for public integrations alongside API key authentication for private integrations.
  name: OAuth 2.0
- description: 3,600 individual requests per hour and up to 50 batch requests per hour, with up to 1,000 records per batch call.
  name: Rate Limits
- description: Cart, order, and product activity endpoints purpose-built for direct-to-consumer brands.
  name: Ecommerce Activity Tracking
- description: First-party integrations with Shopify, WooCommerce, BigCommerce, Magento, and other ecommerce platforms.
  name: Native Ecommerce Integrations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drip-com.png
integrations:
- description: First-party Shopify integration syncs customers, orders, products, and cart activity into Drip.
  name: Shopify
- description: Official WordPress/WooCommerce plugin connects stores to Drip for ecommerce automation.
  name: WooCommerce
- description: Native BigCommerce integration syncs ecommerce events and customer data into Drip.
  name: BigCommerce
- description: Official Magento 1 and Magento 2 extensions connect stores to Drip.
  name: Magento
- description: Official WordPress plugin for embedding forms and tracking visitor activity.
  name: WordPress
- description: Sync Drip segments to Facebook for targeted advertising.
  name: Facebook Custom Audiences
- description: Connect Drip to thousands of apps via Zapier triggers and actions.
  name: Zapier
layout: provider
modified: '2026-05-25'
name: Drip
nav: Providers
network: true
overview: 'Drip publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Email, SMS, Ecommerce, and Automation.


  Drip''s developer surface includes developer portal, documentation, API reference, authentication, signup flow, developer console, support, and 16 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drip-com/refs/heads/main/screenshots/drip-com-2026-06-20T180236.png
security:
- kind: domain-security
  name: Drip Com Domain Security
  slug: drip-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drip-com
solutions:
- description: Marketing automation tailored for direct-to-consumer ecommerce brands and online stores.
  name: Ecommerce Brands
- description: Email marketing and audience engagement workflows for bloggers, creators, and content businesses.
  name: Bloggers and Creators
tags:
- Marketing
- Email
- SMS
- Ecommerce
- Automation
- Customer Data
- Workflows
use_cases:
- description: Drive repeat purchases, abandoned cart recovery, and post-purchase journeys for direct-to-consumer brands.
  name: Ecommerce Marketing Automation
- description: Coordinate multi-channel customer journeys across email and SMS from a single workflow.
  name: Email and SMS Customer Journeys
- description: Stream subscriber profile updates and behavioral events from custom applications into Drip via the REST API.
  name: Subscriber and Event Data Pipelines
- description: Integrate proprietary storefronts with Drip using the cart, order, and product activity endpoints.
  name: Custom Ecommerce Integrations
- description: Capture leads from onsite forms and popups and route them into segmented nurture workflows.
  name: Lead Capture and List Growth
website: https://www.drip.com
---
