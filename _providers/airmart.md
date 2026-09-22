---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airmart/refs/heads/main/security/airmart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goairmart.com/
- group: company
  title: ''
  type: Blog
  url: https://goairmart.com/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://goairmart.com/articles/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.goairmart.com/en/lp/pricing
- group: start
  title: ''
  type: SignUp
  url: https://shop.goairmart.com/en/s/signup
- group: start
  title: ''
  type: Login
  url: https://my.goairmart.com/login
- group: operate
  title: ''
  type: Support
  url: https://airmart.notion.site/Help-Center-eff67628703a45db9108ddd3e55e0002
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.goairmart.com/en/s/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.goairmart.com/en/s/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goairmart
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/goairmart/
- group: other
  title: ''
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=com.goairmart.airmart_customer_flutter
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airmart/refs/heads/main/plans/airmart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airmart-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airmart/refs/heads/main/llms/airmart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airmart-llms.txt
coverage:
  checked: '2026-09-19'
  detail: 'Airmart ships a seller storefront product with no developer program: goairmart.com is a Next.js SPA whose /developers, /docs and /api paths return its 404 page, developers.goairmart.com and docs.goairmart.com wildcard-redirect into the storefront, api.goairmart.com and ts-api.goairmart.com are private NestJS backends answering every probed path with {"statusCode":404} (no OpenAPI, GraphQL, MCP or agent card), and no SDK exists on npm, PyPI or GitHub.'
  evidence:
  - status: 404
    url: https://www.goairmart.com/developers
  - status: 302
    url: https://developers.goairmart.com/
  - status: 404
    url: https://ts-api.goairmart.com/openapi.json
  - status: 404
    url: https://api.goairmart.com/openapi.json
  - status: 404
    url: https://ts-api.goairmart.com/graphql
  - status: 404
    url: https://www.goairmart.com/.well-known/api-catalog
  - status: 200
    url: https://shop.goairmart.com/en/lp/pricing
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: Airmart (goairmart.com) is a Redwood City, California e-commerce platform founded in 2018 that lets small sellers such as home bakers, farms, restaurants, cottage-food makers, creators and community group buys open a link-based online storefront, take orders and payments (Stripe card checkout, PayPal, Venmo, Zelle, cash), manage customers and marketing, and fulfil through pickup, shipping, DoorDash on-demand delivery or its own route-planned delivery service. Sellers run their shop from my.goairmart.com or the Airmart mobile apps and buyers shop at shop.goairmart.com; plans start at a free Basic tier with a Standard plan at $19/month ($16/month billed annually). As of this profile Airmart publishes no public developer program, API documentation, SDK, webhooks or machine-readable contract; api.goairmart.com and ts-api.goairmart.com are private first-party backends for its own web and mobile apps.
image: https://shop.goairmart.com/logo/logo_black_text.svg
layout: provider
modified: '2026-09-19'
name: Airmart
nav: Providers
network: true
overview: 'Airmart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Commerce, Online Storefront, Social Commerce, and Payments.


  Airmart''s developer surface includes engineering blog, pricing, signup flow, support, and 11 more developer resources.'
plans:
- name: Airmart Plans Pricing
  plan_count: 3
  slug: airmart-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airmart Domain Security
  slug: airmart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airmart
tags:
- E-Commerce
- Commerce
- Online Storefront
- Social Commerce
- Payments
- Delivery
- Small Business
- Food
- United States
- Company
website: https://www.goairmart.com/
---
