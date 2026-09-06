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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monolith-materials-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monolith-corp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monolith-corp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monolith-corp.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://monolith-corp.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monolith-corp/
coverage:
  checked: '2026-08-26'
  detail: Monolith Inc. is a physical carbon-black and clean-hydrogen manufacturer in Lincoln, Nebraska whose entire corporate site is six marketing pages (carbon-black, technology, resiliency, about, contact, privacy/terms) with no developer, docs, portal or integration link anywhere in the nav or footer; every OpenAPI/GraphQL/MCP/agent-card path probed on monolith-corp.com returns a hard 404, no api./docs./developer./status. subdomain resolves at all, and the only other host, carbonblack.monolith-corp.com, is an SPA catch-all that answers 200 with the same 21,174-byte shell for a random control path.
  evidence:
  - status: 404
    url: https://monolith-corp.com/openapi.json
  - status: 404
    url: https://monolith-corp.com/.well-known/agent-card.json
  - status: 404
    url: https://monolith-corp.com/developers
  - status: 404
    url: https://monolith-corp.com/llms.txt
  - status: 200
    url: https://carbonblack.monolith-corp.com/zz-api-evangelist-control
  - status: 200
    url: https://monolith-corp.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Monolith (legally Monolith Inc., formerly Monolith Materials) is an American chemicals and advanced-materials manufacturer headquartered in Lincoln, Nebraska and founded in 2012. It is the first company to run methane pyrolysis at commercial scale, using an electrified thermal-plasma process to split natural gas or renewable biogas into solid carbon and clean hydrogen with no direct CO2 combustion. The solid carbon is finished into carbon black for tire, rubber, plastics, battery and electronics manufacturing, and the co-produced hydrogen is used on-site or converted into anhydrous ammonia. Monolith operates a demonstration plant in Redwood City, California and its commercial Olive Creek facility in Hallam, Nebraska, which since 2023 has supplied made-in-Nebraska carbon black to Goodyear. Monolith is a physical materials producer and sells industrial product, not software: it publishes no developer program, no public API, and no machine-readable API contract of any kind.'
layout: provider
modified: '2026-08-26'
name: Monolith Materials
nav: Providers
network: true
overview: 'Monolith Materials is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advanced Materials, Chemicals, Manufacturing, and Clean Hydrogen.


  Monolith Materials'' developer surface includes support and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monolith-materials/refs/heads/main/screenshots/monolith-materials-2026-09-02T150626.png
security:
- kind: domain-security
  name: Monolith Materials Domain Security
  slug: monolith-materials-domain-security
  summary_line: TLSv1.3 · DMARC
slug: monolith-materials
tags:
- Company
- Advanced Materials
- Chemicals
- Manufacturing
- Clean Hydrogen
- Carbon Black
- Energy Transition
- Industrial
website: https://monolith-corp.com/
---
