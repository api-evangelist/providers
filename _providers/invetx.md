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
  url: security/invetx-domain-security.yml
created: '2026-07-17'
description: Invetx was a Boston-based veterinary biotechnology company developing protein-based therapeutics — species-specific, half-life-extended monoclonal antibodies (mAbs) — for chronic conditions in companion animals (dogs and cats). Its integrated platform spanned antibody discovery, optimization, Fc-variant half-life extension, development and manufacturing, with lead program IVX-01. Backed by GV, F-Prime Capital, Novo Holdings, Eight Roads, Anterra Capital, Casdin Capital and Tekla, Invetx was acquired by Dechra Pharmaceuticals in July 2024 for up to $520M. It exposes no public API, developer, or documentation surface, and its standalone website (invetx.com) has been decommissioned since the acquisition; this profile is retained as a network lead / portfolio record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/invetx.png
layout: provider
modified: '2026-07-19'
name: Invetx *
nav: Providers
network: true
overview: Invetx * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biotechnology, Animal Health, and Veterinary.
random_paper: 19
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
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
security:
- kind: domain-security
  name: Invetx Domain Security
  slug: invetx-domain-security
  summary_line: DMARC
slug: invetx
tags:
- Company
- Life Sciences
- Biotechnology
- Animal Health
- Veterinary
- Monoclonal Antibodies
- Therapeutics
- Acquired
---
