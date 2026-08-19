---
access_model:
  confidence: high
  label: Enterprise sales only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.luckycart.com/en/contact
  - https://github.com/lucky-cart/luckycart-js-sdk#initialization
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: 'The core Lucky Cart API. POST /cart/ticket submits a validated shopping cart — cart identifier, shopper identifier, gross and net amounts, and product lines — and Lucky Cart determines whether a game '
  name: Lucky Cart Core API
  slug: core-api
- description: Event ingest for shopper behaviour on a retailer storefront. A single POST /event endpoint accepts {shopperId, siteKey, eventName, payload}, where eventName is a Lucky Cart event such as pageViewed or
  name: Lucky Cart Shopper Events API
  slug: shopper-events-api
- description: Returns the set of Lucky Cart experiences currently available to a given shopper. GET /experiences takes shopperId, siteKey and an experienceType filter as query parameters and answers with the experi
  name: Lucky Cart Shopper Experience API
  slug: shopper-experience-api
- description: Grants access to the gamified post-purchase experiences a shopper has earned. GET /game-experiences-access takes shopperId, siteKey and a count parameter capping how many experiences to return, and an
  name: Lucky Cart Game Experience API
  slug: game-experience-api
- description: Selects and returns the promotional banner to render for a given page context. The route encodes the whole selection key in the path — /{siteKey}/{shopper}/banner/{platform}/ {pageType}/{format} for a
  name: Lucky Cart Displayer API
  slug: displayer-api
- description: The promo-matching and creative-delivery host used by the JavaScript SDK. It serves the same banner selection routes as the displayer — /{siteKey}/{shopper}/banner|banners/{subset}/ {pageType}/{format
  name: Lucky Cart Promo Matching API
  slug: promo-matching-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucky-cart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.luckycart.com/
- group: operate
  title: ''
  type: Support
  url: https://www.luckycart.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.luckycart.com/actualites
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.luckycart.com/politique-de-confidentialite
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.luckycart.com/mentions-legales
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucky-cart
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/lucky-cart/luckycart-js-sdk#readme
- group: start
  title: ''
  type: Login
  url: https://app.luckycart.com/
- group: build
  title: ''
  type: Packages
  url: packages/lucky-cart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lucky-cart-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucky-cart-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lucky-cart-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/lucky-cart-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lucky-cart-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.luckycart.com/en/certifications
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucky-cart-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lucky-cart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucky-cart-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucky-cart-llms.txt
created: '2026-07-17'
description: 'Lucky Cart is a French MarTech company specializing in retail media and smart commerce for grocery and consumer-goods retailers. It combines first-party transactional data with e-retail media, machine learning, and AI to power personalized shopper engagement, gamified promotions, and the monetization of retailer audiences at scale. Lucky Cart works with major French grocery retailers and CPG brands to activate transactional data into targeted advertising, loyalty, and measurable campaigns. Its integration surface is a set of HTTP APIs consumed through three first-party SDKs published on GitHub — a shopper-event ingest, a promotional banner displayer, a cart-to-ticket endpoint that mints the post-purchase game, and a hosted game experience. Lucky Cart publishes no OpenAPI, no developer portal and no self-service signup: API keys are issued manually by its integration team to contracted retailers, and its Help Centre is access-restricted.'
image: https://cdn.prod.website-files.com/68c2baa88e31954e039031a7/68d2e246b13b0428fe573013_lucky-cart-share.avif
layout: provider
modified: '2026-08-12'
name: Lucky Cart
nav: Providers
network: true
overview: 'Lucky Cart publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail Media, MarTech, E-Commerce, and Advertising.


  Lucky Cart''s developer surface includes support, engineering blog, documentation, authentication, and 16 more developer resources.'
plans:
- name: Lucky Cart Plans Pricing
  plan_count: 0
  slug: lucky-cart-plans-pricing
random_paper: 129
rate_limits:
- limit_count: 0
  name: Lucky Cart Rate Limits
  slug: lucky-cart-rate-limits
score:
  band: emerging
  composite: 24.9
  delta: -0.4
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.3
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucky-cart/refs/heads/main/screenshots/lucky-cart-2026-07-25T225646.png
security:
- kind: authentication
  name: Lucky Cart Authentication
  slug: lucky-cart-authentication
  summary_line: apiKey/custom-hmac-signature · 3 schemes
- kind: domain-security
  name: Lucky Cart Domain Security
  slug: lucky-cart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lucky-cart
tags:
- Company
- Retail Media
- MarTech
- E-Commerce
- Advertising
- Personalization
- Loyalty
- CPG
- Grocery
- Promotions
- Gamification
- Shopper Marketing
- First-Party Data
- France
website: https://www.luckycart.com/
---
