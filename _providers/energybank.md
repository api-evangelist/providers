---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  url: security/energybank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.energybank.nz/
- group: company
  title: ''
  type: Careers
  url: https://www.energybank.nz/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energybank-llms.txt
created: '2026-07-17'
description: EnergyBank is a New Zealand deep-tech energy company developing next-generation energy storage for the offshore wind market. Its core approach firms floating offshore wind generation at the turbine so that compute modules can be co-located with the generation itself — taking "data to the power rather than electricity to the data" — which removes the need for a grid connection, enables consentless high-seas deployment, and allows direct ocean cooling of the co-located compute. The company was founded by CEO Tim Hawkey and CTO Alex Szczepaniak, and its team combines applied mathematicians, electronics engineers, and business development staff with advisors drawn from subsea turbomachinery. EnergyBank is venture backed by Version One Ventures, Blackbird, Icehouse Ventures, Outset Ventures, Promus Ventures, Nuance Capital, and Boost VC. As of this enrichment pass EnergyBank publishes no public API, developer portal, SDK, or machine-readable specification — it is a hardware and energy-infrastructure
  company rather than an API provider.
image: https://cdn.prod.website-files.com/613030d31a2013fa372a2bf6/615cf267b464835b36e1f5cf_eb.png
layout: provider
modified: '2026-07-20'
name: EnergyBank
nav: Providers
network: true
overview: EnergyBank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Storage, Offshore Wind, and Renewable Energy.
random_paper: 12
score:
  band: minimal
  composite: 4.0
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
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energybank/refs/heads/main/screenshots/energybank-2026-07-25T213332.png
security:
- kind: domain-security
  name: Energybank Domain Security
  slug: energybank-domain-security
  summary_line: TLSv1.3 · HSTS
slug: energybank
tags:
- Company
- Energy
- Energy Storage
- Offshore Wind
- Renewable Energy
- Data Centers
- Deep Tech
- New Zealand
website: https://www.energybank.nz/
---
