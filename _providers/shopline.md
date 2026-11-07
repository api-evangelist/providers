---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
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
artifact_total: 10
asyncapis:
- description: ''
  name: Shopline Webhooks
  slug: shopline-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/shopline/plans/shopline-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shopline-plans-pricing.yml
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
  href: https://artifacts.apis.io/shopline/authentication/shopline-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shopline-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shopline/scopes/shopline-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/shopline-scopes.yml
- group: design
  href: https://artifacts.apis.io/shopline/conventions/shopline-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shopline-conventions.yml
- group: design
  href: https://artifacts.apis.io/shopline/lifecycle/shopline-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shopline-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/shopline/changelog/shopline-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shopline-changelog.yml
- group: design
  href: https://artifacts.apis.io/shopline/conformance/shopline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shopline-conformance.yml
- group: design
  href: https://artifacts.apis.io/shopline/asyncapi/shopline-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shopline-webhooks.yml
- group: build
  href: https://artifacts.apis.io/shopline/packages/shopline-packages.yml
  title: ''
  type: Packages
  url: packages/shopline-packages.yml
- group: build
  href: https://artifacts.apis.io/shopline/packages/shopline-packages.yml
  title: ''
  type: SDKs
  url: packages/shopline-packages.yml
- group: build
  href: https://artifacts.apis.io/shopline/cli/shopline-cli.yml
  title: ''
  type: CLI
  url: cli/shopline-cli.yml
- group: start
  href: https://artifacts.apis.io/shopline/sandbox/shopline-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/shopline-sandbox.yml
- group: design
  href: https://artifacts.apis.io/shopline/components/shopline-components.yml
  title: ''
  type: Components
  url: components/shopline-components.yml
- group: agent
  href: https://artifacts.apis.io/shopline/llms/shopline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shopline-llms.txt
- group: auth
  href: https://artifacts.apis.io/shopline/security/shopline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shopline-domain-security.yml
created: '2026-07-17'
description: SHOPLINE is an all-in-one commerce platform that lets merchants sell across online stores, social channels, and offline point-of-sale, serving businesses from budding entrepreneurs to global brands across Australia, China, Hong Kong, Japan, Malaysia, Singapore, Taiwan, the United Kingdom, and the United States. The SHOPLINE Open Platform gives developers a versioned Admin REST API, an Admin GraphQL API, and a Storefront API for building apps, themes, and integrations. Apps authenticate with OAuth 2.0 (Custom and Public apps) or private-app tokens, request granular read_*/write_* access scopes, receive HMAC-signed webhooks, and are built with the SHOPLINE CLI against free development stores.
finops:
- has_sources: true
  method: derived
  name: Shopline Finops
  primary_unit: store
  service_category: ''
  slug: shopline-finops
  template: false
image: https://s2cdn.myshopline.com/slfs/op-new/170236799353875/SEO_banner.png
layout: provider
modified: '2026-07-21'
name: SHOPLINE
nav: Providers
network: true
overview: 'SHOPLINE is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Commerce, Retail, and Point-of-Sale.


  The SHOPLINE catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SHOPLINE''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Shopline Plans Pricing
  plan_count: 9
  slug: shopline-plans-pricing
- name: Shopline Price Estimates
  plan_count: 0
  slug: shopline-price-estimates
random_paper: 2
scopes:
- name: Shopline Scopes
  scope_count: 63
  slug: shopline-scopes
  summary_line: 63 scopes · authorizationCode
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 76.2
    discoverability: 78.6
    operational_transparency: 50.0
  previous_composite: 58.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shopline/shopline-2026-08-17T081839.png
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
- Point-of-Sale
- Storefront
- Payments
- Webhook
- GraphQL
- Developer Platform
- Application
website: https://shoplineapp.com
---
