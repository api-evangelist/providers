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
  url: security/ouromedicines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ouromedicines.com
- group: company
  title: ''
  type: Blog
  url: https://ouromedicines.com/news/
created: '2026-07-17'
description: Ouro Medicines is a clinical-stage biotechnology company based in South San Francisco, California, defining the future of treatment for people with immune-mediated diseases. Its pipeline centers on T cell engager programs for autoimmune conditions, including the lead candidate OM336 (evaluated in the AIC-1001 clinical trial), alongside an expanded access policy. The company was surfaced as a portfolio company of Norwest Venture Partners and added to the API Evangelist network as a lead. As a therapeutics developer, Ouro Medicines publishes a corporate and scientific website but no public developer program, API, or technical documentation surface. Recent company news includes a definitive agreement for Gilead Sciences to acquire Ouro Medicines to advance its first-in-class T cell engager program for autoimmune diseases.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ouromedicines.png
layout: provider
modified: '2026-07-20'
name: Ouro Medicines
nav: Providers
network: true
overview: 'Ouro Medicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunology, and Immune-Mediated Diseases.


  Ouro Medicines'' developer surface includes engineering blog and 2 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ouromedicines/refs/heads/main/screenshots/ouromedicines-2026-08-07T191047.png
security:
- kind: domain-security
  name: Ouromedicines Domain Security
  slug: ouromedicines-domain-security
  summary_line: TLSv1.3
slug: ouromedicines
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunology
- Immune-Mediated Diseases
- Autoimmune Diseases
- Clinical Trials
- Life Sciences
- Therapeutics
website: https://ouromedicines.com
---
