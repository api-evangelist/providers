---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: The `allProducts` query on Nacelle's Storefront GraphQL API returns normalized product entries (variants, pricing, media, metafields) drawn from ingested Shopify or other commerce sources, with Relay-
  name: Nacelle Storefront Products API
  slug: nacelle-storefront-products-api
- description: The `allProductCollections` query returns merchandised collections of products (the normalized equivalent of Shopify collections) with their member product references, for building category and listin
  name: Nacelle Storefront Product Collections API
  slug: nacelle-storefront-product-collections-api
- description: The `allContent` query returns CMS content entries (pages, articles, marketing blocks, media) ingested from sources such as Contentful, with a configurable entryDepth for resolving nested content refe
  name: Nacelle Storefront Content API
  slug: nacelle-storefront-content-api
- description: 'The `navigation` and `spaceProperties` queries return a space''s navigation groups (menus) and space-level configuration (locales, currency, metadata) used to render a headless storefront''s chrome and '
  name: Nacelle Storefront Navigation and Spaces API
  slug: nacelle-storefront-navigation-spaces-api
- description: The Admin GraphQL API triggers and monitors the indexing / ingestion pipeline that pulls data from connected sources (Shopify, CMS) into a space - starting or resetting index jobs for a data source, e
  name: Nacelle Admin Indexing and Ingestion API
  slug: nacelle-admin-indexing-api
artifact_total: 13
collections:
- collection_type: open
  name: Nacelle GraphQL API
  slug: open-nacelle
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/nacelle-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nacelle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nacelle-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getnacelle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nacelle
- group: company
  title: ''
  type: Website
  url: https://nacelle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/nacelle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nacelle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nacelle-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://nacelle.com/blog
created: '2026-07-01'
description: Nacelle is a headless / composable commerce data platform that ingests, normalizes, and indexes commerce and content data (Shopify, Contentful and other CMS sources) and serves it back to headless storefronts through a single, fast GraphQL Storefront API. The company has since pivoted toward an AI personalization engine, and the headless commerce Storefront API is now a legacy / maintenance-mode product rather than an actively expanding platform.
finops:
- name: Nacelle Finops
  service_category: Commerce and Content Infrastructure
  slug: nacelle-finops
graphqls:
- description: Nacelle is a headless / composable commerce data platform. It ingests and normalizes
  name: Nacelle GraphQL APIs
  slug: nacelle-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nacelle.png
layout: provider
modified: '2026-07-01'
name: Nacelle
nav: Providers
network: true
overview: 'Nacelle publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Storefront Products API, Storefront Product Collections API, Storefront Content API, and 2 more. Tagged areas include Commerce, Headless Commerce, Composable Commerce, GraphQL, and Content.


  Nacelle''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Nacelle Plans Pricing
  plan_count: 1
  slug: nacelle-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Nacelle Rate Limits
  slug: nacelle-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Nacelle Domain Security
  slug: nacelle-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Nacelle Vulnerability Disclosure
  slug: nacelle-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nacelle Trust Center
  slug: nacelle-trust-center
  summary_line: SOC 2, GDPR
slug: nacelle
tags:
- Commerce
- Headless Commerce
- Composable Commerce
- GraphQL
- Content
- Data Indexing
website: https://nacelle.com/
---
