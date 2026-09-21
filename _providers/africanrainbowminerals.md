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
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/africanrainbowminerals/refs/heads/main/security/africanrainbowminerals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/africanrainbowminerals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arm.co.za/
- group: company
  title: ''
  type: About
  url: https://arm.co.za/about-us/
- group: operate
  title: ''
  type: Support
  url: https://arm.co.za/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arm.co.za/wp-content/uploads/2021/07/ARM-Privacy.pdf
- group: operate
  title: ''
  type: PressReleases
  url: https://arm.co.za/press-release/
- group: company
  title: ''
  type: InvestorRelations
  url: https://arm.co.za/financial-results/
- group: company
  title: ''
  type: Careers
  url: https://arm.co.za/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/african-rainbow-minerals/
coverage:
  checked: '2026-09-12'
  detail: African Rainbow Minerals is a JSE-listed South African mining house that sells iron ore, manganese, chrome, PGMs, nickel and coal, and its only web property is a 30-page WordPress corporate/investor site (arm.co.za) whose sitemap contains no developer, docs, portal, API or integration page at all; every OpenAPI, Swagger, GraphQL, MCP, llms.txt and agent-card path probed on arm.co.za returned a hard 404 with an empty body (a random control path 404s the same way, so these are real misses and not an SPA catch-all), no api./dev./docs./developer./ portal./data./gis./geo./maps. subdomain resolves in DNS on either arm.co.za or arm-online.co.za, and the only machine-readable surface on the domain is the stock WordPress /wp-json/wp/v2 route index, which describes the CMS that renders the investor site rather than any African Rainbow Minerals product, so it was deliberately not registered as a contract.
  evidence:
  - status: 200
    url: https://arm.co.za/
  - status: 404
    url: https://arm.co.za/openapi.json
  - status: 404
    url: https://arm.co.za/swagger.json
  - status: 404
    url: https://arm.co.za/api-docs
  - status: 404
    url: https://arm.co.za/llms.txt
  - status: 404
    url: https://arm.co.za/developers
  - status: 404
    url: https://arm.co.za/.well-known/agent-card.json
  - status: 404
    url: https://arm.co.za/.well-known/agent.json
  - status: 404
    url: https://arm.co.za/.well-known/security.txt
  - status: 404
    url: https://arm.co.za/.well-known/api-catalog
  - status: 404
    url: https://arm.co.za/zz-api-evangelist-control
  - status: 200
    url: https://arm.co.za/wp-json/
  - status: 404
    url: https://www.arm-online.co.za/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'African Rainbow Minerals Limited (ARM) is a niche, diversified South African mining and minerals company, founded by Dr Patrice Motsepe and created in its present form in May 2004 through the merger of ARMgold and Harmony assets. ARM is listed on the Johannesburg Stock Exchange under the ticker ARI and is headquartered in Sandton, Gauteng. The company mines and beneficiates iron ore, manganese ore and alloys, chrome ore, platinum group metals, nickel and coal through ARM Ferrous, ARM Platinum and ARM Coal, plus a strategic gold investment in Harmony Gold Mining Company — spanning Khumani iron ore, Black Rock manganese, Two Rivers, Modikwa and Bokoni platinum, Nkomati nickel, Goedgevonden coal and Sakura Ferroalloys in Malaysia. ARM sells physical mined commodity, not software: it runs no developer program and publishes no public API, SDK, webhook or machine-readable API contract of any kind.'
image: https://arm.co.za/wp-content/themes/african_rainbow_minerals/theme-default-images/resources/arm-logo.png
layout: provider
modified: '2026-09-12'
name: African Rainbow Minerals
nav: Providers
network: true
overview: 'African Rainbow Minerals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mining, Metals And Mining, Natural Resources, and Commodities.


  African Rainbow Minerals'' developer surface includes support and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-africa
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 8.1
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Africanrainbowminerals Domain Security
  slug: africanrainbowminerals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: africanrainbowminerals
tags:
- Company
- Mining
- Metals And Mining
- Natural Resources
- Commodities
- Iron Ore
- Manganese
- Platinum Group Metals
- Coal
- South Africa
- Publicly Traded
website: https://arm.co.za/
---
