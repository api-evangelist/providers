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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/absology-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/absology-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.absology.co.kr/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/absology-co-ltd
created: '2026-09-06'
description: Absology Co., Ltd. is a South Korean in-vitro diagnostics (IVD) company founded in 2017 and headquartered in Anyang, Gyeonggi-do. It designs and manufactures point-of-care immunoassay analyzers and the reagent cartridges that run on them, built on microfluidic immunoassay and photo-oxidation-induced fluorescence amplification chemistry. Its Absol analyzer line runs rapid and ultra-sensitive quantitative blood tests — testosterone, vitamin D, PSA, TSH, free T4, PCT, cortisol and cardiac markers — for human and companion-animal use, with stated research programs in anti-cancer therapy monitoring, cardiovascular disease and neurodegenerative disease. Absology is a hardware and consumables manufacturer rather than a software vendor, and no public developer program, API, SDK or machine-readable contract has been found on its corporate site or in any public package registry or code host.
layout: provider
modified: '2026-09-06'
name: Absology
nav: Providers
network: true
overview: Absology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Medical Devices, Diagnostics, and In-Vitro Diagnostics.
random_paper: 3
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Absology Domain Security
  slug: absology-domain-security
  summary_line: TLSv1.2
slug: absology
tags:
- Company
- Health Care
- Medical Devices
- Diagnostics
- In-Vitro Diagnostics
- Point Of Care
- Laboratory
- South Korea
website: https://www.absology.co.kr/
---
