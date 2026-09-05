---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://eigentech.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.sirion.ai/ — a different registrable domain (eigentech.com -> sirion.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eigen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eigentech.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eigentechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eigen-technologies
created: '2026-07-17'
description: Eigen Technologies is a London-based intelligent document processing (IDP) and data-extraction company that uses natural language processing, object detection and machine learning to extract, classify and interpret structured data from unstructured documents at scale. Its no-code platform lets teams in financial services, insurance, law and professional services pull hundreds of datapoints out of contracts, loan agreements and filings to manage risk, automate processes and meet regulatory obligations, with extracted data pushed downstream via its document-processing API. Founded in 2014 and backed by Goldman Sachs, Temasek, Lakestar, Dawn Capital, ING Ventures, Anthemis and the Sony Innovation Fund, Eigen was acquired by contract-lifecycle-management platform Sirion in June 2024.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eigen.png
layout: provider
modified: '2026-07-19'
name: Eigen
nav: Providers
network: true
overview: Eigen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Document AI, Intelligent Document Processing, Data Extraction, and Natural Language Processing.
random_paper: 16
score:
  band: minimal
  composite: 2.6
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eigen/refs/heads/main/screenshots/eigen-2026-07-25T213006.png
security:
- kind: domain-security
  name: Eigen Domain Security
  slug: eigen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eigen
tags:
- Company
- Document AI
- Intelligent Document Processing
- Data Extraction
- Natural Language Processing
- Machine-Learning
- Financial-Services
- Legal Tech
- Insurance
website: https://eigentech.com/
---
