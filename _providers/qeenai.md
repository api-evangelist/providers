---
access_model:
  confidence: high
  label: Paid with trial, gated credentials
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://apps.shopify.com/qeen-ai
  - https://qeen.ai/en
  - https://github.com/fodoole/qeen-mobile-sdk-ios
  trial: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Qeen's first-party mobile analytics and commerce-event SDK, shipped as a binary XCFramework for iOS (Swift Package Manager) and an AAR for Android (self-hosted Maven). It exposes a typed commerce even
  name: Qeen Mobile Analytics SDK
  slug: qeen-mobile-analytics-sdk
- description: The browser-side data plane the published qeen.js SDK and loader snippet call. The loader hashes the page URL and a persisted device id and requests a per-page content-replacement script; the SDK then
  name: Qeen Web Content and Analytics API
  slug: qeen-web-content-and-analytics-api
- description: 'The backend the Qeen customer web application (app.qeen.ai, a Nuxt single-page app) calls — a path-versioned Django REST Framework service covering websites, content, organizations and subscriptions, '
  name: Qeen Customer Platform API
  slug: qeen-customer-platform-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://qeen.ai
- group: company
  title: ''
  type: Blog
  url: https://blog.qeen.ai
- group: start
  title: ''
  type: Login
  url: https://app.qeen.ai/en
- group: start
  title: ''
  type: SignUp
  url: https://app.qeen.ai/en/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qeen.ai/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qeen.ai/en/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fodoole
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/fodoole/qeen-mobile-sdk-ios#usage
- group: operate
  title: ''
  type: Support
  url: mailto:info@qeen.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://apps.shopify.com/qeen-ai
- group: build
  title: ''
  type: Packages
  url: packages/qeenai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qeenai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/qeenai-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qeenai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qeenai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qeenai-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qeenai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qeenai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qeenai-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qeenai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qeenai-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qeenai-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qeenai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qeenai-domain-security.yml
created: '2026-07-17'
description: 'Qeen (qeen.ai) is a Dubai-based AI company serving e-commerce brands across the GCC and wider MENA region. Founded in 2023 by former Google and DeepMind researchers and backed by a $10M seed led by Prosus Ventures ($12M total), it sells two things: a self-serve content-optimization product that generates, localizes and A/B-tests Arabic and English product titles, descriptions and meta descriptions, and a commission-based growth marketing engagement priced at 5% of generated revenue with no retainer. Qeen publishes no OpenAPI, no developer portal and no public API reference. Its machine-readable surface is three first-party client SDKs — a binary Swift package for iOS and an Android AAR, both at 1.5.0 and shipping roughly weekly, plus a browser SDK and embedded search widget served from its own CDN. Ingestion credentials (an API key and a customer-provisioned host) are issued privately by email rather than through self-service, and the customer platform API at users.qeen.ai
  is a session-gated Django REST Framework backend for the web application rather than a developer API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qeenai.png
layout: provider
modified: '2026-08-12'
name: Qeen.AI
nav: Providers
network: true
overview: 'Qeen.AI publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Marketing, Ecommerce, and Advertising.


  Qeen.AI''s developer surface includes engineering blog, signup flow, documentation, support, pricing, authentication, changelog, and 17 more developer resources.'
plans:
- name: Qeenai Plans Pricing
  plan_count: 4
  slug: qeenai-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 0
  name: Qeenai Rate Limits
  slug: qeenai-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 35.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Qeenai Authentication
  slug: qeenai-authentication
  summary_line: apiKey/cookie · 3 schemes
- kind: domain-security
  name: Qeenai Domain Security
  slug: qeenai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qeenai
tags:
- Company
- Ai
- Marketing
- Ecommerce
- Advertising
- MENA
- Analytics
- Personalization
- Mobile SDK
- Content Optimization
- Search
- Attribution
website: https://qeen.ai
---
