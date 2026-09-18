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
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrourbana/refs/heads/main/security/agrourbana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrourbana-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agrourbana/refs/heads/main/plans/agrourbana-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agrourbana-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agrourbana/refs/heads/main/rate-limits/agrourbana-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agrourbana-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrourbana/refs/heads/main/llms/agrourbana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrourbana-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.agrourbana.ag/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agrourbana.ag/terminos-y-condiciones
- group: operate
  title: ''
  type: ContactUs
  url: https://www.agrourbana.ag/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://cl.linkedin.com/company/agrourbana
- group: other
  title: ''
  type: x-SecondaryMarket
  url: https://equityzen.com/company/agrourbana
coverage:
  checked: '2026-09-13'
  detail: 'AgroUrbana sells physical produce, not software: its only public digital surface is the Urban Rabbit consumer storefront on the hosted Bootic platform, whose own product, cart and customer routes now 404, and no developer portal, API host, OpenAPI document or .well-known document exists on agrourbana.ag, www.agrourbana.ag or agrourbana.cl.'
  evidence:
  - status: 200
    url: https://www.agrourbana.ag/
  - status: 404
    url: https://agrourbana.ag/openapi.json
  - status: 404
    url: https://agrourbana.ag/.well-known/security.txt
  - status: 404
    url: https://www.agrourbana.ag/docs
  - status: 404
    url: https://api.github.com/orgs/agrourbana
  reason: not-a-software-company
  state: none
created: '2026-09-13'
description: AgroUrbana SpA is a Chilean vertical-farming company founded in 2018 in Santiago by Pablo Bunster and Cristian Sjogren, and widely described as the first commercial vertical farm in Latin America. It runs climate-controlled indoor grow facilities combining hydroponics, spectrum-programmed LED lighting, renewable energy, automation and data analytics to produce leafy greens year round, reporting up to twelve growing cycles a year and up to 95% less water use than open-field agriculture. Produce is sold to Chilean retailers including Cencosud and Walmart Chile, and direct to consumers under the Urban Rabbit brand through a hosted online store. The company has raised roughly USD 12 million, including a USD 4 million Series A led by Kayyak Ventures and a USD 6 million pre-Series B led by ALB Inversiones. AgroUrbana operates its technology internally to run its own farms and publishes no public API, SDK, developer portal or machine-readable API contract.
image: https://static.bolder.run/23001/logo/original/logo-logo-UR_AU-para-notificacionepurp.png
layout: provider
modified: '2026-09-13'
name: AgroUrbana
nav: Providers
network: true
overview: AgroUrbana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Vertical Farming, and Food and Beverage.
plans:
- name: Agrourbana Plans Pricing
  plan_count: 0
  slug: agrourbana-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Agrourbana Rate Limits
  slug: agrourbana-rate-limits
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - chile
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 7.1
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrourbana Domain Security
  slug: agrourbana-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agrourbana
tags:
- Company
- Agriculture
- AgTech
- Vertical Farming
- Food and Beverage
- Controlled Environment Agriculture
- Chile
- Latin America
- Sustainability
website: https://www.agrourbana.ag/
---
