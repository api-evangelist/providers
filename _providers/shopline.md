---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Versioned REST access to store data (products, orders, customers, inventory, fulfillment, discounts, and more) for SHOPLINE apps.
  name: SHOPLINE Admin REST API
  slug: shopline-admin-rest-api
- description: GraphQL access to SHOPLINE store data, with schema documentation and an explorer.
  name: SHOPLINE Admin GraphQL API
  slug: shopline-admin-graphql-api
- description: GraphQL storefront API for building custom storefront experiences.
  name: SHOPLINE Storefront API
  slug: shopline-storefront-api
artifact_total: 7
asyncapis:
- description: ''
  name: Shopline Webhooks
  slug: shopline-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shoplineapp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.shopline.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shopline.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.shopline.com/docs/apps/api-instructions-for-use/rest-admin-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.shopline.com/docs/apps/overview
- group: company
  title: ''
  type: Blog
  url: https://developer.shopline.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:openapi_v2@shopline.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shoplineapp
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shopline.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.shopline.com/docs/apps/api-instructions-for-use/api-versioning-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shopline.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developer.shopline.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.shopline.com/docs/apps/get-started/shopline-developer-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopline.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopline-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shopline-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopline-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopline-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shopline-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopline-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shopline-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/shopline-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shopline-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/shopline-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shopline-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/shopline-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopline-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopline-domain-security.yml
created: '2026-07-17'
description: SHOPLINE is an all-in-one commerce platform that lets merchants sell across online stores, social channels, and offline point-of-sale, serving businesses from budding entrepreneurs to global brands across Australia, China, Hong Kong, Japan, Malaysia, Singapore, Taiwan, the United Kingdom, and the United States. The SHOPLINE Open Platform gives developers a versioned Admin REST API, an Admin GraphQL API, and a Storefront API for building apps, themes, and integrations. Apps authenticate with OAuth 2.0 (Custom and Public apps) or private-app tokens, request granular read_*/write_* access scopes, receive HMAC-signed webhooks, and are built with the SHOPLINE CLI against free development stores.
image: https://s2cdn.myshopline.com/slfs/op-new/170236799353875/SEO_banner.png
layout: provider
modified: '2026-07-21'
name: SHOPLINE
nav: Providers
network: true
overview: 'SHOPLINE publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Commerce, Retail, and Point of Sale.


  The SHOPLINE catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SHOPLINE''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 121
scopes:
- name: Shopline Scopes
  scope_count: 63
  slug: shopline-scopes
  summary_line: 63 scopes · authorizationCode
score:
  band: developing
  composite: 52.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 71.7
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 52.6
  previous_composite: 52.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Shopline Authentication
  slug: shopline-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Shopline Domain Security
  slug: shopline-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shopline
tags:
- Company
- E-Commerce
- Commerce
- Retail
- Point of Sale
- Storefront
- Payments
- Webhooks
- GraphQL
- Developer Platform
- Apps
website: https://shoplineapp.com
---
