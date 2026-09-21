---
access_model:
  confidence: high
  label: No developer access - no API, developer portal, keys or reference exists; product sign-up only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - well-known/airpos-well-known.yml
  - plans/airpos-plans-pricing.yml
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airpos/refs/heads/main/security/airpos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airpos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airpointofsale.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airpointofsale.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.airpointofsale.com/register
- group: start
  title: ''
  type: Login
  url: https://backoffice.airpointofsale.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.airpointofsale.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.airpointofsale.com/
- group: company
  title: ''
  type: Blog
  url: https://retail.airpointofsale.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://retail.airpointofsale.com/rss/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airpointofsale.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airpointofsale.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AirPOS
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/retail-point-of-sale
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/airpos
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airpos/refs/heads/main/plans/airpos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airpos-plans-pricing.yml
coverage:
  checked: '2026-09-19'
  detail: 'AirPOS sells an end-user POS product only: the www.airpointofsale.com SPA has just seven routes (/, /pricing, /contact, /register, /terms, /privacy-policy, /audit) and its catch-all answers 200 with the same 9,379-byte HTML shell for /openapi.json, /llms.txt, /developers and every /.well-known/* path; backoffice.airpointofsale.com 302s to a Rails sign-in and 404s /api, /openapi.json and /api-docs; the 284-URL help-center sitemap has no API, webhook or developer article (integrations are Shopify/Xero/SumUp/Zettle connectors configured in the product); and the GitHub org AirPOS (37 repos) holds only forked Kohana/Rails/Heroku infrastructure libraries with no client, spec or SDK. The slug domain airpos.com is an unrelated parking lander.'
  evidence:
  - status: 200
    url: https://www.airpointofsale.com/openapi.json
  - status: 200
    url: https://www.airpointofsale.com/developers
  - status: 404
    url: https://backoffice.airpointofsale.com/api
  - status: 404
    url: https://backoffice.airpointofsale.com/openapi.json
  - status: 200
    url: https://help.airpointofsale.com/sitemap-posts.xml
  - status: 200
    url: https://api.github.com/orgs/AirPOS
  - status: 200
    url: https://airpos.com/
  - status: 403
    url: https://equityzen.com/company/airpos
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: AirPOS Ltd is a Belfast, Northern Ireland software company that sells AirPOS Pay, a subscription-free cloud point-of-sale, integrated card payments, stock control, reporting and e-commerce platform for independent retailers in the UK and Ireland. The POS software is free and the company charges a single fee per card transaction (advertised at 1.4% + 14p for new businesses, from 0.8% for existing businesses), with the platform hosted on Amazon EC2 in Dublin. AirPOS ships an Android POS app and a web backoffice and integrates with Shopify, Xero, SumUp and Zettle, but it publishes no public API, SDK, webhook surface or developer program of any kind; its GitHub organization holds only forked infrastructure libraries. Surfaced via the API Evangelist secondary-market harvest (EquityZen listing), and profiled here as a company with no public API surface.
image: https://avatars.githubusercontent.com/u/600339?v=4
layout: provider
modified: '2026-09-19'
name: AirPOS
nav: Providers
network: true
overview: 'AirPOS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Retail, Payments, and Inventory Management.


  AirPOS''s developer surface includes pricing, signup flow, support, engineering blog, and 11 more developer resources.'
plans:
- name: Airpos Plans Pricing
  plan_count: 2
  slug: airpos-plans-pricing
random_paper: 16
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airpos Domain Security
  slug: airpos-domain-security
  summary_line: TLSv1.3
slug: airpos
tags:
- Company
- Point-of-Sale
- Retail
- Payments
- Inventory Management
- E-Commerce
- United Kingdom
- Northern Ireland
website: https://www.airpointofsale.com
---
