---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://aceabio.com.cn'', ''status'': 301, ''note'': ''declared website redirects to https://www.agilent.com/acea-bio/ — a different registrable domain (aceabio.com.cn -> agilent.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/agilent-technologies/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aceabio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aceabio.com.cn
created: '2026-07-17'
description: ACEA Biosciences (aceabio) is a life-sciences company known for cell-analysis instrumentation that was acquired by Agilent Technologies; its aceabio.com.cn domain now redirects to an Agilent landing page (explore.agilent.com/ACEA-joins-Agilent). It was surfaced as a portfolio company of the Qiming venture firm and added to the API Evangelist network as a stub. Enrichment found no independent developer portal, API documentation, OpenAPI/AsyncAPI specification, SDKs, or public API surface for the standalone entity — the operating web presence has been folded into Agilent.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aceabio.png
layout: provider
modified: '2026-07-17'
name: aceabio
nav: Providers
network: true
overview: aceabio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Analysis, and Diagnostics.
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aceabio/refs/heads/main/screenshots/aceabio-2026-07-25T181446.png
security:
- kind: domain-security
  name: Aceabio Domain Security
  slug: aceabio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aceabio
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Analysis
- Diagnostics
- Scientific Instruments
- Acquired
website: https://aceabio.com.cn
---
