---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Saleor Agentic Access
  operation_count: 2
  slug: saleor-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 9
apis:
- description: Single GraphQL endpoint exposing the entire Saleor commerce model - products, variants, categories, collections, channels, checkout, orders, payments, promotions, taxes, attributes, warehouses, and us
  name: Saleor GraphQL API
  slug: graphql-api
- description: TypeScript SDK for building Saleor Apps - background services that extend Saleor over the GraphQL API and react to webhooks. Handles app installation, auth, async webhooks, and metadata.
  name: Saleor App SDK
  slug: app-sdk
- description: Reference Next.js project for bootstrapping a Saleor App - install flow, webhook handlers, GraphQL clients, and a config UI mounted inside the Saleor Dashboard via the App Bridge.
  name: Saleor App Template
  slug: app-template
- description: Official TypeScript / JavaScript SDK wrapping the Saleor GraphQL API for storefronts and Apps - typed operations, auth, cart, and checkout helpers.
  name: saleor-sdk (TypeScript / JavaScript)
  slug: sdk-js
- description: Reference Next.js storefront talking to the Saleor GraphQL API - product browse, cart, checkout, account, and payments. Used as the canonical starting point for headless storefronts on Saleor.
  name: Saleor Storefront (Next.js Starter)
  slug: storefront
- description: Official React / TypeScript admin dashboard for Saleor - a thick client built entirely against the Saleor GraphQL API.
  name: Saleor Dashboard
  slug: dashboard
- description: Hosted, managed Saleor service - provisions Saleor cores per store with the same GraphQL API surface, plus environment management, deploys, and Apps marketplace.
  name: Saleor Cloud
  slug: cloud
- description: Source repository for the Saleor server - the Django / Python backend that implements the GraphQL API, business logic, persistence, and webhooks.
  name: Saleor Core (Server) Repository
  slug: core-repo
- description: The Saleor GraphQL API API from Saleor — 1 operation(s) for saleor graphql api.
  name: Saleor Saleor GraphQL API API
  slug: saleor-saleor-graphql-api-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Saleor GraphQL Saleor GraphQL API API
  slug: open-saleor-saleor-graphql-api-api
- collection_type: open
  name: Saleor GraphQL API
  slug: open-saleor
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/saleor/saleor-app-sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saleor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saleor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saleor-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://saleor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.saleor.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.saleor.io/api-reference/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/saleor
- group: other
  title: ''
  type: Cloud
  url: https://cloud.saleor.io/
- group: operate
  title: ''
  type: Discord
  url: https://saleor.io/discord
- group: operate
  title: ''
  type: Status
  url: https://status.saleor.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saleor-commerce/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.saleor.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://saleor.io/blog
created: '2026-05-23'
description: Saleor is an open-source, GraphQL-first commerce platform built in Python (Django) with a TypeScript dashboard. The entire commerce surface is exposed through a single GraphQL API used by storefronts, the Saleor Dashboard, and third-party Saleor Apps; mutations and queries cover products, channels, carts (checkout), orders, payments, promotions, taxes, attributes, and warehouses. Developer surface includes Saleor Cloud, the Saleor App SDK and App Template, a starter storefront, language SDKs (saleor-sdk for TS/JS), and an App Store of first-party and partner integrations.
finops:
- name: Saleor Finops
  service_category: API
  slug: saleor-finops
graphqls:
- description: Single GraphQL endpoint exposing the entire Saleor commerce model - products, variants, categories, collections, channels, checkout, orders, payments, promotions, taxes, attributes, warehouses, and us
  name: Saleor GraphQL API
  slug: saleor-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saleor.png
layout: provider
modified: '2026-05-25'
name: Saleor
nav: Providers
network: true
overview: 'Saleor publishes 1 API on the [APIs.io](https://apis.io/) network: Saleor GraphQL API API. Tagged areas include Commerce, Headless, E-Commerce, GraphQL, and Open-Source.


  Saleor''s developer surface includes authentication, documentation, API reference, GitHub presence, status page, engineering blog, and 8 more developer resources.'
plans:
- name: Saleor Plans Pricing
  plan_count: 1
  slug: saleor-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Saleor Rate Limits
  slug: saleor-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saleor/refs/heads/main/screenshots/saleor-2026-06-20T193340.png
security:
- kind: authentication
  name: Saleor Authentication
  slug: saleor-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Saleor Domain Security
  slug: saleor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saleor
tags:
- Commerce
- Headless
- E-Commerce
- GraphQL
- Open-Source
- Python
- TypeScript
website: https://saleor.io/
---
