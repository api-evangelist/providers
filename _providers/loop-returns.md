---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Loop Returns Agentic Access
  operation_count: 32
  slug: loop-returns-agentic-access
  summary_line: 32 operations · 22 acting
api_count: 7
apis:
- description: The Cart API from Loop Returns — 2 operation(s) for cart.
  name: Loop Returns Cart API
  slug: loop-returns-cart-api
- description: The Destinations API from Loop Returns — 2 operation(s) for destinations.
  name: Loop Returns Destinations API
  slug: loop-returns-destinations-api
- description: The Fraud Reports API from Loop Returns — 1 operation(s) for fraud reports.
  name: Loop Returns Fraud Reports API
  slug: loop-returns-fraud-reports-api
- description: The Label Requests API from Loop Returns — 6 operation(s) for label requests.
  name: Loop Returns Label Requests API
  slug: loop-returns-label-requests-api
- description: The Programmatic Webhooks API from Loop Returns — 2 operation(s) for programmatic webhooks.
  name: Loop Returns Programmatic Webhooks API
  slug: loop-returns-programmatic-webhooks-api
- description: The Return Actions API from Loop Returns — 9 operation(s) for return actions.
  name: Loop Returns Return Actions API
  slug: loop-returns-return-actions-api
- description: The Return Data API from Loop Returns — 3 operation(s) for return data.
  name: Loop Returns Return Data API
  slug: loop-returns-return-data-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loop-returns-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/loop-returns-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loop-returns-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loop-returns-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/loop-returns-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.loopreturns.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.loopreturns.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loopreturns.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.loopreturns.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.loopreturns.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loopreturns.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.loopreturns.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LoopReturns
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loop-returns
- group: other
  title: ''
  type: X
  url: https://x.com/loop
- group: commercial
  title: ''
  type: Plans
  url: plans/loop-returns-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loop-returns-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loop-returns-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/loop-returns-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/loop-returns-context.jsonld
created: '2026-06-12'
description: Loop Returns is an AI-powered post-purchase operations platform built for e-commerce retention that unites tracking, returns, exchanges, fraud prevention, and shipping into a single platform. Originally built for Shopify, Loop now supports all e-commerce platforms and enables brands to transform returns into revenue-retaining exchanges. The platform provides a REST API for creating return authorizations, tracking return status, managing exchange workflows, generating labels, and triggering refunds. Developers can also configure programmatic webhooks to receive real-time event notifications for returns, shipments, labels, and gift cards. API access is gated by scoped API keys passed via the X-Authorization header, with OAuth 2.0 required for the Label and Webhooks APIs.
examples:
- key_count: 9
  name: Loop Returns Label Request Example
  slug: loop-returns-label-request-example
- key_count: 35
  name: Loop Returns Return Example
  slug: loop-returns-return-example
- key_count: 6
  name: Loop Returns Webhook Example
  slug: loop-returns-webhook-example
finops:
- name: Loop Returns Finops
  service_category: ''
  slug: loop-returns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loop-returns.png
json_schemas:
- name: Loop Returns - Label Request
  property_count: 9
  slug: loop-returns-label-request
- name: Loop Returns - Return
  property_count: 24
  slug: loop-returns-return
- name: Loop Returns - Webhook
  property_count: 6
  slug: loop-returns-webhook
jsonld:
- class_count: 9
  name: Loop Returns Context
  property_count: 49
  slug: loop-returns-context
layout: provider
modified: '2026-06-12'
name: Loop Returns
nav: Providers
network: true
overview: 'Loop Returns publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Destinations API, Fraud Reports API, and 4 more. Tagged areas include Returns, E-Commerce, Exchanges, Refunds, and Shipping.


  The Loop Returns catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Loop Returns'' developer surface includes authentication, documentation, pricing, engineering blog, changelog, and 15 more developer resources.'
plans:
- name: Loop Returns Plans Pricing
  plan_count: 3
  slug: loop-returns-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Loop Returns Rate Limits
  slug: loop-returns-rate-limits
rules:
- name: Loop Returns API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: loop-returns-jsonschema-spectral-rules
scopes:
- name: Loop Returns Scopes
  scope_count: 6
  slug: loop-returns-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 62.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 69.9
    developer_ergonomics: 26.1
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 57.9
  previous_composite: 62.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loop-returns/refs/heads/main/screenshots/loop-returns-2026-06-20T184717.png
security:
- kind: authentication
  name: Loop Returns Authentication
  slug: loop-returns-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Loop Returns Domain Security
  slug: loop-returns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loop Returns Trust Center
  slug: loop-returns-trust-center
  summary_line: SOC 2, GDPR
slug: loop-returns
tags:
- Returns
- E-Commerce
- Exchanges
- Refunds
- Shipping
- Post-Purchase
- Shopify
- Fraud Prevention
- Retail
website: https://www.loopreturns.com/
---
