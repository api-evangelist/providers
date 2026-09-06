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
  url: security/bayomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bayomics.com
created: '2026-07-17'
description: Bayomics (贝普奥生物) is a Shenzhen-based biotechnology company specializing in spatial proteomics and trace (micro) proteomics solutions for pharmaceutical research and drug development. Its product lines include the SISPROT protein sample-preparation kits built on proprietary Spintip centrifuge-pipette technology that process nanogram-level samples in roughly two hours, VistaProX spatial visualization proteomics combining immunofluorescence staining with high-depth mass-spectrometry detection on a single slice, and high-throughput automation systems capable of processing up to 400 proteomics samples per day. Bayomics operates as a B2B reagent supplier and research-services provider and does not currently publish any public developer API, SDKs, or programmatic developer resources. This profile was surfaced as a portfolio company of Qiming Venture Partners and added to the API Evangelist network for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bayomics.png
layout: provider
modified: '2026-07-18'
name: bayomics
nav: Providers
network: true
overview: bayomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Proteomics, Mass Spectrometry, and Life Sciences.
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
    - greater-china
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
screenshot: https://raw.githubusercontent.com/api-evangelist/bayomics/refs/heads/main/screenshots/bayomics-2026-07-25T202529.png
security:
- kind: domain-security
  name: Bayomics Domain Security
  slug: bayomics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bayomics
tags:
- Company
- Biotechnology
- Proteomics
- Mass Spectrometry
- Life Sciences
- Drug Discovery
- Laboratory
website: https://bayomics.com
---
