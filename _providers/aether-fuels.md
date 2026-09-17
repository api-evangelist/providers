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
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aether-fuels/refs/heads/main/security/aether-fuels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aether-fuels-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aetherfuels.com/
- group: company
  title: ''
  type: About
  url: https://aetherfuels.com/about
- group: other
  title: ''
  type: Technology
  url: https://aetherfuels.com/technology
- group: company
  title: ''
  type: News
  url: https://aetherfuels.com/news
- group: company
  title: ''
  type: Blog
  url: https://aetherfuels.com/news
- group: operate
  title: ''
  type: PressReleases
  url: https://aetherfuels.com/news
- group: company
  title: ''
  type: Careers
  url: https://aetherfuels.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://aetherfuels.com/contact
- group: operate
  title: ''
  type: Support
  url: https://aetherfuels.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aether-fuels/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aether-fuels/refs/heads/main/llms/aether-fuels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aether-fuels-llms.txt
coverage:
  checked: '2026-09-12'
  detail: Aether Fuels is a Singapore- and Chicago-based sustainable-fuels company that sells Aether Aurora gas-to-liquid process technology and the SAF it produces; its entire web presence is a seven-page Craft CMS marketing site (home, approach, technology, about, news, careers, contact) whose own sitemap index lists no developer, docs or API section, no api./developer./docs./portal./app./data./status. subdomain of aetherfuels.com resolves in DNS at all, and every OpenAPI, APIs.json, agent-card and .well-known path probed on the one live host returns a hard 404 that a negative-control probe confirms is a real 404 and not a catch-all.
  evidence:
  - status: 200
    url: https://aetherfuels.com/
  - status: 404
    url: https://aetherfuels.com/openapi.json
  - status: 404
    url: https://aetherfuels.com/apis.json
  - status: 404
    url: https://aetherfuels.com/llms.txt
  - status: 404
    url: https://aetherfuels.com/.well-known/agent-card.json
  - status: 404
    url: https://aetherfuels.com/.well-known/security.txt
  - status: 404
    url: https://aetherfuels.com/.well-known/aether-fuels-negative-control-7f3ab91c.json
  - status: 0
    url: https://api.aetherfuels.com/
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'Aether Fuels is a sustainable-fuels technology company founded in April 2022 by Conor Madigan with Xora Innovation, headquartered at Republic Plaza in Singapore with a U.S. R&D center on the GTI Energy campus in the Chicago area. Its Aether Aurora process is a radically simplified gas-to-liquid route that converts waste carbon — CO2, CO, methane and other hydrocarbons from gasified biomass, municipal solid waste, biogas and industrial off-gases — into drop-in sustainable liquid fuels for aviation and ocean shipping, combining an electrified thermochemical syngas reactor, three proprietary catalysts and by-product recycling to cut capital cost and raise carbon conversion efficiency at medium plant scale. The company runs a 1.5 gallon-per-day integrated pilot line with strategic partner GTI Energy, whose technology it licenses, and is building a 1+ barrel-per-day demonstration plant; it has signed MOUs with JetBlue and FlyORO and is partnered with Aster on a first commercial
  SAF plant in Singapore. Aether Fuels sells fuel and process technology, not software: it publishes no developer program, no public API, and no machine-readable API contract of any kind.'
image: https://aetherfuels.com/android-chrome-512x512.png
layout: provider
modified: '2026-09-12'
name: Aether Fuels
nav: Providers
network: true
overview: 'Aether Fuels is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Sustainable Aviation Fuel, Synthetic Fuels, and Clean Energy.


  Aether Fuels'' developer surface includes product news, engineering blog, support, and 9 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aether Fuels Domain Security
  slug: aether-fuels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aether-fuels
tags:
- Company
- Energy
- Sustainable Aviation Fuel
- Synthetic Fuels
- Clean Energy
- Decarbonization
- Carbon Capture and Utilization
- Climate Tech
- Chemicals
- Deep Tech
- Manufacturing
- Singapore
website: https://aetherfuels.com/
---
