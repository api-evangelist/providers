---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Commercial REST API over the Tastewise food and beverage intelligence graph. Publicly documented operations span recipes (popular/trending), ingredients, dishes and side dishes, restaurants (search, d
  name: Tastewise API
  slug: tastewise-api
artifact_total: 7
asyncapis:
- description: ''
  name: Tastewise Webhooks
  slug: tastewise-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tastewise-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tastewise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tastewise.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tastewise.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tastewise.io/
- group: operate
  title: ''
  type: Support
  url: https://help.tastewise.io/knowledge
- group: company
  title: ''
  type: Blog
  url: https://tastewise.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tastewise
- group: commercial
  title: ''
  type: Pricing
  url: https://tastewise.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.tastewise.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tastewise.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tastewise.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://tastewise.io/trust
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tastewise-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tastewise-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tastewise-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tastewise-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tastewise-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tastewise-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tastewise-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tastewise-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tastewise-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/tastewise-packages.yml
created: '2026-08-29'
description: 'Tastewise is a food and beverage consumer-intelligence platform that reads live demand across social posts, recipes, restaurant menus and retail data, and exposes it to product-innovation, marketing, foodservice and retail-sales teams at CPG brands. The platform is built on menus from 1.4M+ restaurants, 12K+ retail brands, social signals from 90M+ consumers and a proprietary consumer panel. Tastewise sells a commercial REST API — documented publicly at docs.tastewise.io and served from api.tastewise.io — covering recipes, ingredients, dishes, restaurants, menus, consumer motivations, content discovery, trend validation and trend performance, plus an embedded widgets surface and bulk product-list operations with webhook callbacks. Access is per-customer: a bearer API key plus an X-Customer-Id header, with per-route permissions granted per contract. Customers include Nestle and Mars.'
image: https://tastewise.io/wp-content/uploads/2024/01/favicon-150x150.png
layout: provider
modified: '2026-08-29'
name: Tastewise
nav: Providers
network: true
overview: 'Tastewise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Insights, Market Intelligence, and Restaurant.


  The Tastewise catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tastewise''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Tastewise Plans Pricing
  plan_count: 0
  slug: tastewise-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Tastewise Rate Limits
  slug: tastewise-rate-limits
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 42.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tastewise Authentication
  slug: tastewise-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tastewise Domain Security
  slug: tastewise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tastewise Trust Center
  slug: tastewise-trust-center
  summary_line: ISO 27001, ISO 27017, GDPR
slug: tastewise
tags:
- Company
- Food and Beverage
- Consumer Insights
- Market Intelligence
- Restaurant
- Menus
- Recipes
- Trends
- CPG
- Artificial Intelligence
- Data
- Analytics
website: https://tastewise.io/
---
