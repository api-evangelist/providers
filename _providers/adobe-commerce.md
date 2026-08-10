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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: REST API for Adobe Commerce providing access to products, catalogs, categories, customers, carts, checkout, orders, inventory, sales rules, CMS content, and store configuration. Endpoints follow the p
  name: Adobe Commerce REST API
  slug: adobe-commerce-rest-api
- description: GraphQL API for Adobe Commerce optimized for headless storefronts, progressive web apps, and mobile experiences. Provides queries and mutations for products, categories, carts, checkout, customers, an
  name: Adobe Commerce GraphQL API
  slug: adobe-commerce-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-commerce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-commerce-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobe-commerce
- group: company
  title: ''
  type: Website
  url: https://business.adobe.com/products/magento/magento-commerce.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/commerce/webapi/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/commerce/
- group: start
  title: ''
  type: Signup
  url: https://business.adobe.com/products/magento/get-started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/magento/magento-commerce.html
- group: operate
  title: ''
  type: Support
  url: https://experienceleague.adobe.com/en/docs/commerce
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magento
created: '2026-05-11'
description: Adobe Commerce (formerly Magento Commerce) is an enterprise e-commerce platform for building and operating online storefronts, marketplaces, and B2B/B2C catalogs across web, mobile, and headless experiences. The Adobe Commerce Web APIs expose REST and GraphQL access to products, categories, customers, carts, orders, inventory, and configuration with OAuth 1.0a and token-based (Bearer) authentication against a merchant-hosted base URL.
graphqls:
- description: GraphQL API for Adobe Commerce optimized for headless storefronts, progressive web apps, and mobile experiences. Provides queries and mutations for products, categories, carts, checkout, customers, an
  name: Adobe Commerce GraphQL API
  slug: adobe-commerce-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adobe-commerce.png
layout: provider
modified: '2026-05-11'
name: Adobe Commerce
nav: Providers
network: true
overview: 'Adobe Commerce publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-commerce, Commerce, Magento, Adobe, and Online Store.


  Adobe Commerce''s developer surface includes documentation, signup flow, pricing, support, and 6 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-commerce/refs/heads/main/screenshots/adobe-commerce-2026-06-20T164845.png
security:
- kind: domain-security
  name: Adobe Commerce Domain Security
  slug: adobe-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Commerce Vulnerability Disclosure
  slug: adobe-commerce-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-commerce
tags:
- E-commerce
- Commerce
- Magento
- Adobe
- Online Store
- Marketplace
website: https://business.adobe.com/products/magento/magento-commerce.html
---
