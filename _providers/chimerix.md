---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.chimerix.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.jazzpharma.com/ — a different registrable domain (chimerix.com -> jazzpharma.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/jazz-pharmaceuticals/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chimerix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chimerix.com
created: '2026-07-17'
description: 'Chimerix, Inc. was a biopharmaceutical company headquartered in Durham, North Carolina, focused on developing medicines for serious and life-threatening diseases. It is best known for brincidofovir (TEMBEXA), an antiviral approved by the U.S. FDA in 2021 as a smallpox medical countermeasure, and for dordaviprone (ONC201), an investigational small-molecule therapy for H3 K27M-mutant diffuse glioma, a form of brain cancer. Chimerix was a publicly traded company (NASDAQ: CMRX) and was acquired by Jazz Pharmaceuticals in 2025, primarily for dordaviprone; the chimerix.com domain now redirects to jazzpharma.com. As a clinical-stage pharmaceutical company, Chimerix does not operate a public developer program or API surface — this profile tracks it as a company entity within the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chimerix.png
layout: provider
modified: '2026-07-18'
name: Chimerix
nav: Providers
network: true
overview: Chimerix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharmaceutical, Pharmaceuticals, Oncology, and Antivirals.
random_paper: 17
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
screenshot: https://raw.githubusercontent.com/api-evangelist/chimerix/refs/heads/main/screenshots/chimerix-2026-07-25T205222.png
security:
- kind: domain-security
  name: Chimerix Domain Security
  slug: chimerix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chimerix
tags:
- Company
- Biopharmaceutical
- Pharmaceuticals
- Oncology
- Antivirals
- Life Sciences
- Clinical Stage
website: https://www.chimerix.com
---
