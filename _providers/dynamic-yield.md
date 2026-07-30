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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Server-side Experience APIs and related product APIs for personalization, recommendations, event collection, product catalog sync, search, and the Shopping Muse AI assistant. Authenticated with a DY-A
  name: Dynamic Yield Experience OS API
  slug: dynamic-yield-experience-os-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dynamic-yield-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dynamicyield.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://dy.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dy.dev/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dy.dev/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://dy.dev/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.dynamicyield.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.dynamicyield.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DynamicYield
- group: start
  title: ''
  type: Login
  url: https://marketing.dynamicyield.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynamicyield.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynamicyield.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/dynamic-yield-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/dynamic-yield-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dynamic-yield-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dynamic-yield-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dynamic-yield-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dynamic-yield-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dynamic-yield-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dynamic-yield-llms.txt
created: '2026-07-17'
description: Dynamic Yield (a Mastercard company) is an experience optimization and personalization platform — branded "Experience OS" — used by retail, eCommerce, media, travel, and financial-services brands to individualize content, product recommendations, offers, search, and messaging across web, mobile app, email, and kiosk channels. The platform is MACH Alliance certified (microservices-based, API-first, cloud-native, headless) and exposes server-side Experience APIs (choose/collect for personalization and event tracking), a Product Feed / catalog API, a User Event API, Recommendation APIs, a Search API (query, pagination, filtering, sorting, autosuggest), and the Shopping Muse AI shopping-assistant API, alongside client-side script snippets and native mobile SDKs for iOS (Swift), Android (Kotlin), and React Native. Developer documentation, API reference, and a quarterly technical changelog are published at dy.dev. This profile was surfaced as a Bessemer Venture Partners portfolio
  company and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dynamic-yield.png
layout: provider
modified: '2026-07-18'
name: Dynamic Yield
nav: Providers
network: true
overview: 'Dynamic Yield publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Personalization, Experience Optimization, and Recommendations.


  Dynamic Yield''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 31.5
  delta: 0.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 30.6
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/screenshots/dynamic-yield-2026-07-25T212557.png
security:
- kind: authentication
  name: Dynamic Yield Authentication
  slug: dynamic-yield-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dynamic Yield Domain Security
  slug: dynamic-yield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dynamic-yield
tags:
- Company
- Cloud
- Personalization
- Experience Optimization
- Recommendations
- A/B Testing
- Search
- eCommerce
- Retail
- Machine Learning
- MACH
- Mastercard
website: https://www.dynamicyield.com/
---
