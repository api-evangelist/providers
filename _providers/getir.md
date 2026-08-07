---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 1
  name: Getir Agentic Access
  operation_count: 62
  slug: getir-agentic-access
  summary_line: 62 operations · 39 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The GetirFood (GetirYemek) partner integration API — a Swagger 2.0 contract with 62 operations across seven tags (auth, restaurants, products, chain-menus, food-orders, payment-methods, changelog, hea
  name: GetirFood API
  slug: getirfood-api
artifact_total: 6
asyncapis:
- description: ''
  name: Getir Food Webhooks
  slug: getir-food-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://getir.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getir.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getir.com/food/documentation/giris
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getir.com/food/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getir.com/food/documentation/giris
- group: operate
  title: ''
  type: Support
  url: mailto:getiryemekapi@getir.com
- group: operate
  title: ''
  type: StatusPage
  url: https://getir-food-integration.instatus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getir
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getir.com/yardim/gizlilik-politikasi/
- group: auth
  title: ''
  type: Authentication
  url: authentication/getir-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getir-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/getir-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/getir-food-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/getir-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getir-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getir-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getir-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getir-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/getir-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/getir-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getir-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getir-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getir-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/getir-food-overlay.yaml
created: '2026-07-31'
description: 'Getir is an Istanbul-based on-demand delivery company, founded in 2015, that pioneered the ultrafast "groceries in minutes" model and grew into a super-app spanning rapid grocery (Getir), large-basket grocery (GetirBüyük), water (GetirSu), restaurant food delivery (GetirYemek / GetirFood) and local-merchant commerce (GetirÇarşı / GetirLocals). Its developer-facing surface is a partner-integration platform rather than a public product API: Getir publishes the GetirFood API — a Swagger 2.0 contract at food-external-api-gateway.getirapi.com covering restaurant onboarding, menu and product status, working hours, delivery zones, payment methods and the full food-order lifecycle (verify, prepare, handover, deliver, cancel, transfer) — for POS and integrator companies that connect restaurant point-of-sale systems to GetirFood. Orders are pushed to partners over webhooks, with a documented rate limiter, a 99-entry service error registry, published test cards and a dedicated test environment.
  In February 2026 Uber agreed to acquire Getir''s Türkiye delivery business, cleared by the Turkish Competition Authority in June 2026.'
image: https://developers.getir.com/assets/getir-developers-logo-BbJf7m5Z.svg
layout: provider
modified: '2026-07-31'
name: Getir
nav: Providers
network: true
overview: 'Getir publishes 1 API on the [APIs.io](https://apis.io/) network: GetirFood API. Tagged areas include Company, Food Delivery, Grocery Delivery, On-Demand Delivery, and Logistics.


  The Getir catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Getir''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 18 more developer resources.'
random_paper: 87
rate_limits:
- limit_count: 3
  name: Getir Rate Limits
  slug: getir-rate-limits
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 46.5
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 76.3
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Getir Authentication
  slug: getir-authentication
  summary_line: custom-token · 1 scheme
- kind: domain-security
  name: Getir Domain Security
  slug: getir-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getir
tags:
- Company
- Food Delivery
- Grocery Delivery
- On-Demand Delivery
- Logistics
- Restaurants
- Point of Sale
- Marketplace
- Turkey
- Partner Integration
website: https://getir.com/
---
