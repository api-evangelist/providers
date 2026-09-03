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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orna-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ornatx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OrnaComputationTeam
- group: other
  title: ''
  type: ParentCompany
  url: https://www.lilly.com/science/subsidiaries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ornatx
coverage:
  checked: '2026-08-26'
  detail: Orna Therapeutics is a clinical-stage RNA therapeutics developer with no software product, and since Eli Lilly's acquisition (definitive agreement announced 2026-02-09) its entire domain ornatx.com answers HTTP 301 to https://lilly.com/science/subsidiaries — every /.well-known/* path included — so the only surface it still operates is a GitHub org of 44 forked third-party RNA structure-prediction tools and one internal CodeCommit sync action, none of which is an API.
  evidence:
  - status: 301
    url: https://www.ornatx.com/
  - status: 301
    url: https://www.ornatx.com/.well-known/api-catalog
  - status: 404
    url: https://www.ornatx.com/openapi.json
  - status: 404
    url: https://www.ornatx.com/llms.txt
  - status: 200
    url: https://github.com/OrnaComputationTeam
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Orna Therapeutics is a Cambridge, Massachusetts biotechnology company, founded in 2019 on research from MIT and built by MPM Capital, that engineers circular RNA (oRNA) paired with lipid nanoparticle delivery so a patient''s own body generates cell therapies — its lead program ORN-252 is a CD19-targeting in vivo CAR-T designed for B-cell-driven autoimmune disease. Orna acquired ReNAgade Therapeutics in 2024, combining its circular RNA platform with ReNAgade''s LNP delivery and RNA editing capabilities, and Eli Lilly announced a definitive agreement to acquire Orna on 2026-02-09 for up to $2.4B. Orna is a therapeutics developer, not a software vendor: it publishes no API, developer portal, SDK or machine-readable contract, and as of this profile its own domain ornatx.com redirects in whole to Eli Lilly''s subsidiaries page.'
layout: provider
modified: '2026-08-26'
name: Orna Therapeutics
nav: Providers
network: true
overview: Orna Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, RNA, and Life Sciences.
random_paper: 10
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/orna-therapeutics/refs/heads/main/screenshots/orna-therapeutics-2026-09-02T150857.png
security:
- kind: domain-security
  name: Orna Therapeutics Domain Security
  slug: orna-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: orna-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- RNA
- Life Sciences
- Pharmaceuticals
- Cell Therapy
- Research
website: https://www.ornatx.com/
---
