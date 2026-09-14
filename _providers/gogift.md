---
access_model:
  confidence: high
  label: Credentials issued by GoGift; no self-service API signup
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://global.gogift.com/en/pricing
  - https://docs.gogift.io/#authentication
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'The GoGift REST API for buying and sending digital gift cards. Five documented operations cover the purchase flow end to end: filter the product catalogue, read a product and its purchasable inventory'
  name: GoGift Commerce API
  slug: gogift
artifact_total: 8
asyncapis:
- description: ''
  name: Gogift Webhooks
  slug: gogift-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://global.gogift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gogift.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gogift.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gogift.io/#rest-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://global.gogift.com/en/get-started
- group: operate
  title: ''
  type: Support
  url: https://support.gogift.com/en
- group: company
  title: ''
  type: Blog
  url: https://global.gogift.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://global.gogift.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://global.gogift.com/en/create-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.gogift.com/en/article/dc0cc2
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.gogift.com/en/article/355f71
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoGift
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gogift
- group: auth
  title: ''
  type: Authentication
  url: authentication/gogift-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gogift-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.gogift.io/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gogift-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gogift-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gogift-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gogift-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gogift-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gogift-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gogift-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gogift-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gogift-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/gogift-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gogift-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gogift-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/gogift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gogift-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gogift-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gogift-domain-security.yml
created: '2025-02-08'
description: GoGift is a global digital gift-card and rewards distributor that sells and delivers gift cards from thousands of brands across more than a hundred markets. Its REST API lets a business filter that catalogue by sales channel, delivery method and the countries a reward must be redeemable in, build a basket of gift cards for named recipients, and finalize it into a paid order that GoGift fulfils by email, SMS, CSV, webhook or physical post. The API is HTTPS-only and JSON-only, authenticated with OpenID Connect client credentials against auth.gogift.io, and served unversioned from api.gogift.io with a full sandbox at api-pre.gogift.io. GoGift supports idempotent replay on basket update and finalisation, page -number pagination, ISO 8601 / 3166 / 4217 / 639 data conventions, and one signed outbound webhook that carries the issued gift-card credentials back to the integrator.
finops:
- name: Gogift Finops
  service_category: API
  slug: gogift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gogift.png
layout: provider
modified: '2026-09-12'
name: GoGift
nav: Providers
network: true
overview: 'GoGift publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gift Cards, Rewards, Incentives, Loyalty, and Commerce.


  The GoGift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoGift''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Gogift Plans Pricing
  plan_count: 0
  slug: gogift-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Gogift Rate Limits
  slug: gogift-rate-limits
scopes:
- name: Gogift Scopes
  scope_count: 0
  slug: gogift-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/gogift/refs/heads/main/screenshots/gogift-2026-06-20T181946.png
security:
- kind: authentication
  name: Gogift Authentication
  slug: gogift-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Gogift Domain Security
  slug: gogift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gogift
tags:
- Gift Cards
- Rewards
- Incentives
- Loyalty
- Commerce
- Payments
- Employee Recognition
website: https://global.gogift.com/
---
