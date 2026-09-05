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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/immunitastx/monkeybread/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.immunitastx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.immunitastx.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.immunitastx.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.immunitastx.com/home#contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/immunitastx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/immunitas/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/immunitastx/monkeybread
- group: build
  title: ''
  type: Packages
  url: packages/immunitas-therapeutics-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/immunitas-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/immunitas-therapeutics-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Immunitas Therapeutics is a clinical-stage antibody drug developer (IMT-009, anti-CD161) whose entire public web presence is a four-page Squarespace marketing site — its own sitemap.xml lists only /home, /privacy-policy, /terms-and-conditions and /rdday, with no developer, docs or API page anywhere — so the only machine-readable software it publishes is the MIT-licensed monkeybread Python package for spatial-transcriptomics analysis, which calls no Immunitas service.
  evidence:
  - status: 200
    url: https://www.immunitastx.com/sitemap.xml
  - status: 404
    url: https://www.immunitastx.com/openapi.json
  - status: 404
    url: https://www.immunitastx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.immunitastx.com/llms.txt
  - status: 200
    url: https://pypi.org/pypi/monkeybread/json
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: Immunitas Therapeutics is a Boston, Massachusetts clinical-stage biotechnology company that discovers and develops novel antibody therapeutics for patients with cancer and autoimmune disease. It was founded by cancer-research and therapeutic-antibody scientists from Dana-Farber Cancer Institute, Mass General Cancer Center, the Broad Institute and MIT, whose single-cell analysis drug-discovery platform identified CD161 as a T-cell target. The lead program, IMT-009, is an anti-CD161 antibody in a Phase 1/2a study in solid tumors and hematological malignancies; a second, preclinical anti-CD161 program (IMT-380) for chronic inflammatory disease was licensed to Boehringer Ingelheim in May 2026. Immunitas publishes no public API, developer portal or machine-readable API contract. Its only public software is open source research tooling from the immunitastx GitHub organization, notably the MIT-licensed Python package monkeybread for analyzing cellular niches in single-cell spatial
  transcriptomics data.
image: https://static1.squarespace.com/static/6164da62fcac550608373bab/t/6182f75661dfa17d0caa4ec2/1635972950201/immunitas_logo.png?format=1500w
layout: provider
modified: '2026-08-23'
name: Immunitas Therapeutics
nav: Providers
network: true
overview: 'Immunitas Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Oncology, and Immunology.


  Immunitas Therapeutics'' developer surface includes support and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/immunitas-therapeutics/refs/heads/main/screenshots/immunitas-therapeutics-2026-09-02T145838.png
security:
- kind: domain-security
  name: Immunitas Therapeutics Domain Security
  slug: immunitas-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: immunitas-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Oncology
- Immunology
- Autoimmune Disease
- Single Cell Analysis
- Spatial Transcriptomics
- Bioinformatics
- Open-Source
- Life Sciences
website: https://www.immunitastx.com/
---
