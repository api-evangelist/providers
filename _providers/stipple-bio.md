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
  url: security/stipple-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stipple.bio
created: '2026-07-17'
description: Stipple Bio is a preclinical precision-oncology biotechnology company based in Cambridge, Massachusetts, founded in 2022 by cancer-biology researchers Aaron Ring (Fred Hutch) and Aashish Manglik (UCSF). Its Pointillist Platform performs cellular profiling and tumor-specific epitope discovery to design antibody binders and antibody-drug conjugates (ADCs) that target tumor-specific cell-surface epitopes while avoiding on-target, off-tumor toxicity. Its lead asset, STP-100, is an ADC advancing toward early clinical studies. The company emerged from stealth in April 2026 with an oversubscribed $100M Series A co-led by RA Capital, a16z Bio+Health and Nextech Invest, with participation from Google Ventures (gv). As a therapeutics company, Stipple Bio publishes no public API, developer portal, or software developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stipple-bio.png
layout: provider
modified: '2026-07-21'
name: Stipple Bio
nav: Providers
network: true
overview: Stipple Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biotechnology, Oncology, and Precision Medicine.
random_paper: 15
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stipple-bio/refs/heads/main/screenshots/stipple-bio-2026-09-02T160905.png
security:
- kind: domain-security
  name: Stipple Bio Domain Security
  slug: stipple-bio-domain-security
  summary_line: TLSv1.3
slug: stipple-bio
tags:
- Company
- Life Sciences
- Biotechnology
- Oncology
- Precision Medicine
- Drug Discovery
- Therapeutics
- Antibody-Drug Conjugates
website: https://stipple.bio
---
