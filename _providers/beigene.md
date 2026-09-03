---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.beigene.com'', ''status'': 301, ''note'': ''declared website redirects to https://beonemedicines.com/ — a different registrable domain (beigene.com -> beonemedicines.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beigene-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beigene.com
created: '2026-07-17'
description: BeiGene (rebranded as BeOne Medicines in 2025) is a global oncology biopharmaceutical company founded in 2010, developing and commercializing cancer therapies worldwide. Its portfolio spans blood cancers and solid tumors, led by BRUKINSA (zanubrutinib), a BTK inhibitor, alongside programs in protein degradation (CDACs) and antibody-drug conjugates (ADCs). The company is listed on NASDAQ (BGNE), HKEX, and the Shanghai STAR Market, with a global footprint across 30+ countries (beonemedicines.com). Surfaced as a portfolio company of Hillhouse; no public developer portal, API, or SDK program is currently published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beigene.png
layout: provider
modified: '2026-07-18'
name: BeiGene
nav: Providers
network: true
overview: BeiGene is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotech, Pharmaceuticals, Oncology, and Healthcare.
random_paper: 5
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beigene/refs/heads/main/screenshots/beigene-2026-07-25T202658.png
security:
- kind: domain-security
  name: Beigene Domain Security
  slug: beigene-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beigene
tags:
- Company
- Biotech
- Pharmaceuticals
- Oncology
- Healthcare
- Life Sciences
- Drug Development
website: https://www.beigene.com
---
