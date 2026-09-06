---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.antora.com/
- group: company
  title: ''
  type: About
  url: https://www.antora.com/company
- group: other
  title: ''
  type: Technology
  url: https://www.antora.com/technology
- group: other
  title: ''
  type: Product
  url: https://www.antora.com/solutions
- group: other
  title: ''
  type: Manufacturing
  url: https://www.antora.com/manufacturing
- group: other
  title: ''
  type: CaseStudy
  url: https://www.antora.com/project-big-stone
- group: company
  title: ''
  type: Blog
  url: https://www.antora.com/insights
- group: operate
  title: ''
  type: PressReleases
  url: https://www.antora.com/insights?category=press
- group: company
  title: ''
  type: Careers
  url: https://www.antora.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.antora.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.antora.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.antora.com/privacy
- group: build
  title: ''
  type: SupplierCodeOfConduct
  url: https://www.antora.com/suppliercoc
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/antora-energy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/antoraenergy
- group: other
  title: ''
  type: Application
  url: https://app.antora.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/antora-energy_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antora-energy-domain-security.yml
- group: other
  title: ''
  type: DiscoveryProbe
  url: well-known/antora-energy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antora-energy-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Antora Energy manufactures thermal battery hardware and sells industrial heat and power under long-term offtake agreements, so there is no product to expose as an API; its only software surface is Insight, an authenticated dashboard at app.antora.com built for POET and Antora project stakeholders, whose client bundle contains no first-party API host, and api./developers./docs./portal.antora.com do not resolve in DNS at all.
  evidence:
  - status: 404
    url: https://www.antora.com/openapi.json
  - status: 404
    url: https://www.antora.com/llms.txt
  - status: 404
    url: https://www.antora.com/.well-known/agent-card.json
  - status: 404
    url: https://www.antora.com/.well-known/security.txt
  - status: 404
    url: https://app.antora.com/graphql
  - status: 404
    url: https://app.antora.com/definitely-not-a-real-path-zzz9
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Antora Energy is a San Jose, California clean-energy hardware company founded by Justin Briggs, Andrew Ponec and David Bierman that designs, manufactures and deploys factory-built thermal batteries for heavy industry, data centers and the grid. Antora''s system resistively heats blocks of solid carbon to temperatures up to 2,400C when electricity is cheapest, stores that energy for multiple days in a compact modular unit, and discharges it around the clock as radiant heat delivered directly to industrial processes or paired with off-the-shelf steam turbine equipment for firm power; the company also develops thermophotovoltaic (TPV) heat-to-power cells at what it describes as the world''s largest TPV manufacturing line. Its HeatCore product delivers heat up to 375C at 300 kW-thermal per module, and its power block is rated at 50 MW-electric. Antora''s first giga-scale deployment, Project Big Stone, is a 5 GWh system of more than 200 thermal batteries at POET''s bioprocessing
  plant in Big Stone City, South Dakota, built from empty lot to energy delivery in under twelve months. The company closed a $550 million Series C in 2026. Antora sells energy hardware and long-term energy offtake rather than software: it publishes no developer program, no public API, no SDK and no machine-readable API contract, and its only public software surface is Insight, an authenticated steam and power optimization dashboard for named project stakeholders.'
image: https://www.antora.com/android-chrome-512x512.png
layout: provider
modified: '2026-08-06'
name: Antora Energy
nav: Providers
network: true
overview: 'Antora Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Clean Energy, Thermal Energy Storage, and Energy Storage.


  Antora Energy''s developer surface includes engineering blog and 19 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antora-energy/refs/heads/main/screenshots/antora-energy-2026-08-07T161427.png
security:
- kind: domain-security
  name: Antora Energy Domain Security
  slug: antora-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antora-energy
tags:
- Company
- Energy
- Clean Energy
- Thermal Energy Storage
- Energy Storage
- Industrial Heat
- Thermophotovoltaics
- Manufacturing
- Data Centers
- Decarbonization
- Climate Tech
- California
website: https://www.antora.com/
---
