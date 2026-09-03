---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Huel US customer forum at discourse.huel.com runs Discourse 2026.8.0 and therefore serves the standard Discourse REST API on a Huel-controlled host. Anonymous GET requests to /site.json, /categori
  name: Huel Community API (Discourse)
  slug: community
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://huel.com/
- group: company
  title: ''
  type: About
  url: https://huel.com/pages/about-us
- group: operate
  title: ''
  type: Support
  url: https://huel.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://huel.com/pages/faq
- group: operate
  title: ''
  type: Community
  url: https://discourse.huel.com/
- group: company
  title: ''
  type: Blog
  url: https://huel.com/pages/journal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://huel.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://huel.com/pages/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://huel.com/pages/accessibility-policy
- group: start
  title: ''
  type: SignUp
  url: https://huel.com/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/huel-global
- group: company
  title: ''
  type: Careers
  url: https://careers.huel.com/jobs
- group: company
  title: ''
  type: Press
  url: https://huel.com/pages/press-coverage
- group: other
  title: ''
  type: Sustainability
  url: https://huel.com/pages/sustainability-page
- group: build
  title: ''
  type: Packages
  url: packages/huel-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/huel-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huel-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/huel-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/huel_stock/
created: '2026-08-01'
description: 'Huel (a contraction of "Human Fuel") is a British nutritionally-complete food company founded in June 2015 by Julian Hearn with nutritionist James Collier, headquartered in Tring, Hertfordshire, and operating offices in the UK, US and Europe. It sells plant-based, nutritionally complete powders, ready-to-drink shakes, hot and savoury instant meals, bars and supplements direct to consumers in more than 100 countries, reporting GBP 214 million of revenue in FY2024. Danone SA agreed to acquire Huel in March 2026 in a deal reported at roughly EUR 1 billion / USD 1.1 billion. Huel is a direct-to-consumer commerce and subscription business, not an API provider: it publishes no developer portal, no API documentation and no machine-readable API contract. Its storefront runs as a Next.js application on Vercel in front of a Shopify commerce backend; the only anonymously callable machine-readable surface observed on a Huel-controlled host is the standard Discourse platform REST API served
  by its North American customer community at discourse.huel.com.'
image: https://cdn.huel.io/favicons/android-icon-192x192.png
layout: provider
modified: '2026-08-01'
name: Huel
nav: Providers
network: true
overview: 'Huel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Nutrition, Consumer Packaged Goods, and Direct to Consumer.


  Huel''s developer surface includes support, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huel/refs/heads/main/screenshots/huel-2026-08-07T170354.png
security:
- kind: authentication
  name: Huel Authentication
  slug: huel-authentication
  summary_line: none/apiKey · 3 schemes
- kind: domain-security
  name: Huel Domain Security
  slug: huel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: huel
tags:
- Company
- Food and Beverage
- Nutrition
- Consumer Packaged Goods
- Direct to Consumer
- E-Commerce
- Subscription Commerce
- Health and Wellness
- Retail
- United Kingdom
website: https://huel.com/
---
