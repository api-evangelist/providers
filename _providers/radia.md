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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radia-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/radia-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/radia-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/radia-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/radia-llms.txt
- group: company
  title: ''
  type: Website
  url: https://radia.com/
- group: company
  title: ''
  type: About
  url: https://radia.com/about
- group: company
  title: ''
  type: Press
  url: https://radia.com/media
- group: operate
  title: ''
  type: Contact
  url: https://radia.com/contact
- group: other
  title: ''
  type: Product
  url: https://radia.com/windrunner
- group: build
  title: ''
  type: CodeOfConduct
  url: https://radia.com/strapi/uploads/Supplier_Code_of_Conduct_Nov_2024_c5e004e354.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radiainc
- group: other
  title: ''
  type: X
  url: https://x.com/RadiaWindRunner
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/radia_stock/
created: '2026-08-02'
description: 'Radia is a dual-use aerospace company founded in 2016 by MIT-trained aerospace engineer Mark Lundstrom, headquartered in Boulder, Colorado with a second operating base in Italy led by Giuseppe Giordo. After roughly seven years in stealth the company emerged in March 2024 with WindRunner, an aircraft it describes as the largest ever built: roughly ten times the cargo volume of a Boeing 777, sized to carry onshore wind turbine blades of up to about 105 metres, and designed to land on semi-prepared packed-dirt or gravel strips so that oversized cargo can be flown directly to a wind farm, a forward operating site or a disaster zone rather than trucked over highways it cannot fit on. Radia frames WindRunner as a deliberately low-novelty airframe assembled from existing certified technologies to shorten the certification path, targeting entry into service in the early 2030s across three markets: energy (delivering the very large blades that make low-wind onshore sites economic),
  defense (outsized-volume strategic airlift), and commercial supply-chain logistics. It has assembled an industrial ecosystem of more than twenty suppliers and technology partners including Aernnova, Leonardo, AFuzion, Atitech, Latecoere, Stirling Dynamics, Collier Aerospace and Maximus Air, and has raised roughly USD 128 million from investors including ConocoPhillips, Lauder Partners, LS Power Development and HCVC. Radia is an aircraft manufacturer and logistics operator rather than a software vendor: as of August 2026 it publishes no developer portal, no API documentation, no SDK and no machine-readable API contract of any kind. Its only machine-readable public surface is the Strapi headless-CMS backend at radia.com/strapi that renders its own marketing site, whose content API is permission-locked and undocumented.'
image: https://radia.com/strapi/uploads/About_radia_og2_6b94798e36.jpg
layout: provider
modified: '2026-08-02'
name: Radia
nav: Providers
network: true
overview: Radia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Aviation, Air Cargo, and Logistics.
random_paper: 9
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radia/refs/heads/main/screenshots/radia-2026-09-02T152743.png
security:
- kind: domain-security
  name: Radia Domain Security
  slug: radia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: radia
tags:
- Company
- Aerospace
- Aviation
- Air Cargo
- Logistics
- Wind Energy
- Renewable Energy
- Defense
- Manufacturing
- United States
website: https://radia.com/
---
