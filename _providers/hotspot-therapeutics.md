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
  url: security/hotspot-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hotspotthera.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HotSpot-Therapeutics
- group: company
  title: ''
  type: Blog
  url: https://www.hotspotthera.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hotspotthera.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hotspotthera.com/terms-and-conditions/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/hotspot-therapeutics_stock/
coverage:
  checked: '2026-08-22'
  detail: HotSpot Therapeutics is a clinical-stage biopharmaceutical company whose product is an oral small-molecule drug pipeline (HST-1011, a CBL-B allosteric inhibitor), not software — its "Smart Allostery" AI platform is an internal discovery engine with no external interface, no api./docs./developer. host resolves in DNS, every /.well-known/ path 404s, and its only public GitHub repo is a fork of the third-party SETH bioinformatics tool.
  evidence:
  - status: 404
    url: https://www.hotspotthera.com/.well-known/api-catalog
  - status: 404
    url: https://www.hotspotthera.com/llms.txt
  - status: 404
    url: https://hotspotthera.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/HotSpot-Therapeutics/repos
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'HotSpot Therapeutics is a clinical-stage biopharmaceutical company headquartered in Boston, Massachusetts, pioneering allosteric drug discovery by targeting "natural hotspots" — the regulatory on/off switches on proteins. Its Smart Allostery platform combines AI-driven mining of large, diverse structural and biological data sets with a tailored pharmacology toolkit and bespoke medicinal chemistry to design first-in-class oral small molecules, and has been applied across E3 ligases, kinases and transcription factors. The company has raised roughly $190M across Series A, B and C financings and advanced its lead candidate HST-1011, an oral allosteric CBL-B inhibitor, into first-in-human dosing for cancer, alongside programs in autoimmune disease. HotSpot sells medicines and research collaborations, not software: it publishes no public developer program, API, SDK or machine-readable contract of any kind.'
image: https://avatars.githubusercontent.com/u/105356575?v=4
layout: provider
modified: '2026-08-22'
name: HotSpot Therapeutics
nav: Providers
network: true
overview: 'HotSpot Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  HotSpot Therapeutics'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotspot-therapeutics/refs/heads/main/screenshots/hotspot-therapeutics-2026-09-02T145744.png
security:
- kind: domain-security
  name: Hotspot Therapeutics Domain Security
  slug: hotspot-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hotspot-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Oncology
- Immunology
- Artificial Intelligence
- Health
website: https://www.hotspotthera.com/
---
