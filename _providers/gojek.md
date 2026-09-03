---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The GoBiz Partner Integration API is Gojek's merchant-side REST API. It covers outlet information and outlet linking, GoFood catalog sync and out-of-stock updates, order acceptance / rejection / food-
  name: GoBiz Partner Integration API
  slug: gobiz-partner-integration-api
artifact_total: 7
asyncapis:
- description: ''
  name: Gojek Gobiz Webhooks
  slug: gojek-gobiz-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gojek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gojek.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gobiz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gobiz.com/docs/docs/intro/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.gobiz.com/docs/api/intro/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gobiz.com/docs/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://developer.gobiz.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://gojek.my.site.com/gobizmerchant/s/
- group: company
  title: ''
  type: Blog
  url: https://www.gojek.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gojek
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.gobiz.com/files/terms-and-condition/gobiz-developer-portal-v01.2022
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gojek.com/en-id/privacy-policies/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/gojek_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/gojek-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gojek-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gojek-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gojek-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gojek-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gojek-gobiz-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gojek-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gojek-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gojek-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gojek-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gojek-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/gojek-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gojek-llms.txt
created: '2026-08-22'
description: Gojek (PT Aplikasi Karya Anak Bangsa, part of GoTo Group) is Indonesia's on-demand super app, running ride hailing (GoRide, GoCar), food delivery (GoFood), parcel and logistics (GoSend, GoBox), shopping (GoMart, GoShop) and payments (GoPay) across Indonesia, Singapore and Vietnam. Its developer-facing surface is not the consumer app but the GoBiz Platform - the merchant operating system Gojek runs its restaurants and small businesses on - which publishes the GoBiz Partner Integration API at developer.gobiz.com. That REST API lets POS vendors, online-food aggregators and enterprise merchants link outlets, sync GoFood catalogs, accept/reject and mark orders ready, create SKU-level promotions, take QRIS payment transactions, pull MokaPOS reporting and subscribe to webhook notifications. It is OAuth 2.0 only - client credentials for direct merchant integrations and authorization code with OpenID Connect for facilitators - across sandbox (api.partner-sandbox.gobiz.co.id) and production
  (api.gobiz.co.id) environments. Gojek Engineering also runs a substantial open-source organisation at github.com/gojek (Heimdall, Courier, Ziggurat, Weaver, Darkroom, Clickstream).
image: https://developer.gobiz.com/img/favicon/apple-touch-icon.png
layout: provider
modified: '2026-08-22'
name: GoJek
nav: Providers
network: true
overview: 'GoJek publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Super App, Ride Hailing, Food Delivery, and Point-of-Sale.


  The GoJek catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoJek''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Gojek Plans Pricing
  plan_count: 0
  slug: gojek-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Gojek Rate Limits
  slug: gojek-rate-limits
scopes:
- name: Gojek Scopes
  scope_count: 20
  slug: gojek-scopes
  summary_line: 20 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 41.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gojek/refs/heads/main/screenshots/gojek-2026-09-02T145618.png
security:
- kind: authentication
  name: Gojek Authentication
  slug: gojek-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Gojek Domain Security
  slug: gojek-domain-security
  summary_line: TLSv1.2 · DMARC
slug: gojek
tags:
- Company
- Super App
- Ride Hailing
- Food Delivery
- Point-of-Sale
- Merchant Platform
- Payments
- QRIS
- Logistics
- Indonesia
- Southeast Asia
- Webhook
- Authentication
website: https://www.gojek.com/
---
