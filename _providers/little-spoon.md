---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.littlespoon.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://learn.littlespoon.com/
- group: operate
  title: ''
  type: Support
  url: https://www.littlespoon.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.littlespoon.com/plan-type
- group: start
  title: ''
  type: Login
  url: https://www.littlespoon.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.littlespoon.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.littlespoon.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/little-spoon-dev
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/little-spoon-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/little-spoon-packages.yml
- group: design
  title: ''
  type: Components
  url: components/little-spoon-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/little-spoon-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/little-spoon-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/little-spoon-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/little-spoon-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/little-spoon-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/little-spoon-domain-security.yml
- group: other
  title: ''
  type: ListingVenue
  url: https://www.hiive.com/securities/little-spoon-stock
coverage:
  checked: '2026-08-25'
  detail: 'Little Spoon runs no developer program at all — no portal, no docs, no signup, no spec: its storefront is served by an undocumented first-party JSON backend at api.littlespoon.com that answers /v1/products and /v1/labels unauthenticated but 404s every discovery path (/openapi.json, /swagger.json, /graphql, /docs, /.well-known/*), so the only machine-readable things it publishes are a marketing llms.txt and a React design system on npm.'
  evidence:
  - status: 200
    url: https://api.littlespoon.com/v1/products
  - status: 404
    url: https://api.littlespoon.com/openapi.json
  - status: 404
    url: https://www.littlespoon.com/openapi.json
  - status: 200
    url: https://www.littlespoon.com/llms.txt
  - status: 522
    url: https://developer.littlespoon.com/
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Little Spoon is a New York-based direct-to-consumer children''s food and nutrition brand, founded in 2017, that delivers fresh, organic, stage-based meals, snacks and infant formula for babies, toddlers and kids on a subscription basis across the United States. Its product architecture maps to feeding stages — Formula, Babyblends purees, Biteables finger foods, Baby Puffs, Baby Cereal, Smoothies and YoGos, Lunchers, Plates and a snack line — with a frozen line sold exclusively through Target. The brand competes on ingredient transparency: a published No-No List of 100+ banned ingredients, EU-level food safety standards, 500+ toxin and contaminant tests, and 2000+ safety tests per batch of Formula. Little Spoon operates no public developer program and publishes no API contract; its storefront is a Next.js front end backed by an undocumented first-party JSON API at api.littlespoon.com. It does publish two machine-readable public artifacts — an llms.txt at the site root and an
  open-source React design system distributed as fifteen @littlespoon/* npm packages from the little-spoon-dev GitHub org.'
image: https://ik.imagekit.io/littlespoon/web/fe-assets/public/imgs/og-image.jpg
layout: provider
modified: '2026-08-25'
name: Little Spoon
nav: Providers
network: true
overview: 'Little Spoon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Products, E-Commerce, and Subscription.


  Little Spoon''s developer surface includes support, signup flow, and 16 more developer resources.'
plans:
- name: Little Spoon Plans Pricing
  plan_count: 0
  slug: little-spoon-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Little Spoon Rate Limits
  slug: little-spoon-rate-limits
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 16.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/little-spoon/refs/heads/main/screenshots/little-spoon-2026-09-02T150331.png
security:
- kind: domain-security
  name: Little Spoon Domain Security
  slug: little-spoon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: little-spoon
tags:
- Company
- Food and Beverage
- Consumer Products
- E-Commerce
- Subscription
- Direct to Consumer
- Baby Food
- Nutrition
- Retail
- Design System
website: https://www.littlespoon.com
---
