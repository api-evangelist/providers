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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Storefront GraphQL API is Nacelle's primary query interface for syndicating normalized commerce data — products, variants, content, pricing, price rules, media, metafields, SEO, and product option
  name: Nacelle Storefront GraphQL API
  slug: nacelle-storefront-graphql-api
- description: The Ingest REST API moves commerce data into Nacelle from any source — products, content, pricing, inventory, orders, and customer data — and backs Nacelle's prebuilt Shopify, Contentful, and Sanity c
  name: Nacelle Ingest REST API
  slug: nacelle-ingest-rest-api
- description: The Admin API exposes administrative operations for managing Nacelle spaces, configuration, connectors, and platform-level resources outside of the storefront query and ingest paths. Used by the Nacel
  name: Nacelle Admin API
  slug: nacelle-admin-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/nacelle-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nacelle-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nacelle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nacelle.com
- group: start
  title: ''
  type: Portal
  url: https://docs.nacelle.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/docs/build-with-nacelle
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nacelle.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/graphql
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/recipes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/llms.txt
- group: start
  title: ''
  type: Sandbox
  url: https://docs.nacelle.com/docs/graphql-explorer
- group: start
  title: ''
  type: Signup
  url: https://dashboard.nacelle.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.nacelle.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nacelle.com
- group: company
  title: ''
  type: Blog
  url: https://nacelle.com/blog
- group: other
  title: ''
  type: CaseStudies
  url: https://nacelle.com/resources/customer-stories
- group: company
  title: ''
  type: Careers
  url: https://nacelle.com/careers
- group: company
  title: ''
  type: Partners
  url: https://nacelle.com/partners/partner-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://nacelle.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getnacelle
- group: build
  title: ''
  type: SDKs
  url: https://github.com/getnacelle/nacelle-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/getnacelle/storefront-sdk-2.x-testing
- group: build
  title: ''
  type: Tools
  url: https://github.com/getnacelle/contentful-app-nacelle
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/getnacelle/nuxt-2-reference-store
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getnacelle
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getnacelle
created: '2026-05-25'
description: Nacelle is a headless commerce and AI personalization platform founded in 2019 that provides a composable data orchestration layer for premium ecommerce brands. The platform sits between commerce systems of record (Shopify, BigCommerce, Salesforce Commerce Cloud) and CMS/content systems (Contentful, Sanity), ingesting product, content, pricing, inventory, order, and customer data, then exposing a normalized Storefront GraphQL API and Storefront SDK to power custom frontends, personalized merchandising, and AI-driven product discovery. Nacelle's Ingest REST API and prebuilt connectors (Shopify, Contentful, Sanity) move data into the platform, the Storefront GraphQL API and JavaScript SDK syndicate it to storefronts, and the Admin API manages spaces and configuration. The company's product line includes the AI Personalization Suite featuring "Paige" (an AI shopping assistant), behavioral targeting, recommendations, cross-sell/upsell, and composable data orchestration. Pricing
  is plan-based — Standard at $399/mo and Enterprise custom — with the Headless Commerce platform sold as an enterprise tier. Customers include Boll & Branch, FTD, ProFlowers, Ancient Nutrition, Rhone, Barefoot Dreams, Peach & Lily, and Healthy Baby.
graphqls:
- description: The Storefront GraphQL API is Nacelle's primary query interface for syndicating normalized commerce data — products, variants, content, pricing, price rules, media, metafields, SEO, and product option
  name: Nacelle GraphQL API
  slug: nacelle-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nacelle-com.png
layout: provider
modified: '2026-05-25'
name: Nacelle
nav: Providers
network: true
overview: 'Nacelle publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce, Ecommerce, Headless Commerce, Composable Commerce, and Storefront.


  Nacelle''s developer surface includes developer portal, documentation, getting-started guide, sandbox, signup flow, support, engineering blog, and 20 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 22.5
  delta: -2.2
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nacelle-com/refs/heads/main/screenshots/nacelle-com-2026-06-20T185924.png
security:
- kind: domain-security
  name: Nacelle Com Domain Security
  slug: nacelle-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Nacelle Com Vulnerability Disclosure
  slug: nacelle-com-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nacelle Com Trust Center
  slug: nacelle-com-trust-center
  summary_line: SOC 2, GDPR
slug: nacelle-com
tags:
- Commerce
- Ecommerce
- Headless Commerce
- Composable Commerce
- Storefront
- Personalization
- AI Personalization
- Product Recommendations
- Data Orchestration
- GraphQL
- Shopify
- Contentful
- Sanity
website: https://nacelle.com
---
