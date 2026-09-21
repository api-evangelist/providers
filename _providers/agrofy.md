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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'Agrofy Developers is the company''s marketed partner-integration program for marketplace sellers — listing management, lead management and catalog synchronisation. Agrofy publishes no machine-readable '
  name: Agrofy Marketplace API
  slug: agrofy-marketplace-api
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrofy/refs/heads/main/security/agrofy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrofy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agrofy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.agrofy.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://contenido.agrofy.com.ar/es/
- group: operate
  title: ''
  type: Support
  url: https://www.agrofy.com.ar/contacts
- group: company
  title: ''
  type: Blog
  url: https://news.agrofy.com.ar/
- group: start
  title: ''
  type: Login
  url: https://www.agrofy.com.ar/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agrofy.com.ar/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agrofy.com.ar/politicas-de-privacidad
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrofy/refs/heads/main/llms/agrofy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrofy-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agrofy/refs/heads/main/plans/agrofy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agrofy-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agrofy/refs/heads/main/rate-limits/agrofy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agrofy-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: Agrofy markets an integration program at developers.agrofy.com whose own four-step onboarding is a contact form an advisor answers before any reference guide is shared, and all eight of that portal's per-country "API docs" links fail before HTTP — developers.agrofy.com.ar, .com.br and .com.bo are CNAMEs pointing at NXDOMAIN targets under route53.prod-us-1.eks.agrofy.com, and developers.agrofy.cl, .com.co, .com.pe, .com.py and .com.uy have no DNS record at all.
  evidence:
  - status: 200
    url: https://developers.agrofy.com/
  - status: 0
    url: https://developers.agrofy.com.ar/docs
  - status: 403
    url: https://apigateway-argentina.agrofy.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-09-13'
description: Agrofy is a Latin American agribusiness technology company founded in 2015 in Rosario, Argentina, operating the region's largest online marketplace for agricultural inputs, machinery, farmland, vehicles and services. The company runs three business units — Agrofy Market (the marketplace, live in Argentina and Brazil with country storefronts across Bolivia, Chile, Colombia, Paraguay, Peru and Uruguay), Agrofy News (an agricultural news publication) and Agrofy Pay (payments, credit and financing for agribusiness transactions). Agrofy markets a partner integration program, Agrofy Developers, for sellers who want to automate listings and lead management inside the marketplace.
image: https://www.agrofy.com/imagenes/logo-agrofy-sin-tag.png
layout: provider
modified: '2026-09-13'
name: Agrofy
nav: Providers
network: true
overview: 'Agrofy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agribusiness, AgTech, and Marketplace.


  Agrofy''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Agrofy Plans Pricing
  plan_count: 0
  slug: agrofy-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Agrofy Rate Limits
  slug: agrofy-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - argentina
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 14.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrofy Domain Security
  slug: agrofy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agrofy
tags:
- Company
- Agriculture
- Agribusiness
- AgTech
- Marketplace
- E-Commerce
- Payments
- Latin America
- Argentina
- Brazil
website: https://www.agrofy.com/
---
