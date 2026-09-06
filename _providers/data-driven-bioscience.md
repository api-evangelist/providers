---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://datadrivenbioscience.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.duoseq.com/ — a different registrable domain (datadrivenbioscience.com -> duoseq.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/data-driven-bioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datadrivenbioscience.com/
- group: company
  title: ''
  type: Website
  url: https://duoseq.com/
created: '2026-07-17'
description: Data Driven Bioscience (now operating as Duoseq, a ddb.bio service) is a cancer genomics testing company that performs comprehensive molecular profiling of both DNA and RNA from a single sample in an on-site workflow, delivering results from sample to report in roughly two days. Its platform detects mutations, expression levels, gene fusions, and clonotype information, and integrates directly with Epic and other leading EHR systems so results flow into the patient chart. The company is a portfolio company of initialized-capital and was added to the API Evangelist network as a stub for enrichment; as of this pass it publishes a marketing/clinical website but no public developer or API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-driven-bioscience.png
layout: provider
modified: '2026-07-18'
name: Data Driven Bioscience
nav: Providers
network: true
overview: Data Driven Bioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Genomics, Oncology, and Diagnostics.
random_paper: 8
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
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-driven-bioscience/refs/heads/main/screenshots/data-driven-bioscience-2026-07-25T211232.png
security:
- kind: domain-security
  name: Data Driven Bioscience Domain Security
  slug: data-driven-bioscience-domain-security
  summary_line: TLSv1.3 · HSTS
slug: data-driven-bioscience
tags:
- Company
- Healthcare
- Genomics
- Oncology
- Diagnostics
- Life Sciences
- Bioinformatics
website: https://datadrivenbioscience.com/
---
