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
  url: security/mosanna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mosanna.com
created: '2026-07-17'
description: Mosanna Therapeutics is a clinical-stage pharmaceutical company developing a nighttime nasal spray therapy for obstructive sleep apnea (OSA). Headquartered in Redwood City, California with an office in Basel, Switzerland, the company is pursuing a pharmacological alternative to mechanical CPAP devices by reactivating the upper-airway muscles that keep the airway open during sleep. Surfaced as a portfolio company of Norwest Venture Partners, Mosanna operates a corporate marketing website and publishes no public API, developer portal, or developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mosanna.png
layout: provider
modified: '2026-07-20'
name: Mosanna
nav: Providers
network: true
overview: Mosanna is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Healthcare, and Sleep Apnea.
random_paper: 14
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
screenshot: https://raw.githubusercontent.com/api-evangelist/mosanna/refs/heads/main/screenshots/mosanna-2026-08-07T184316.png
security:
- kind: domain-security
  name: Mosanna Domain Security
  slug: mosanna-domain-security
  summary_line: TLSv1.3
slug: mosanna
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Healthcare
- Sleep Apnea
- Therapeutics
website: https://mosanna.com
---
