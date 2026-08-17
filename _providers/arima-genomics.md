---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://arimagenomics.com/
- group: other
  title: ''
  type: ResearchSite
  url: https://discovery.arimagenomics.com/
- group: company
  title: ''
  type: Blog
  url: https://discovery.arimagenomics.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://discovery.arimagenomics.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://discovery.arimagenomics.com/faqs/
- group: operate
  title: ''
  type: ContactUs
  url: https://arimagenomics.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArimaGenomics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arimagenomics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arimagenomics.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arima-genomics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arima-genomics-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Arima Genomics sells Hi-C reagent kits, lab services and the Aventa clinical tests; its "Documentation" library is wet-lab kit PDFs, its open-source output is command-line bioinformatics pipelines on GitHub, and every OpenAPI and /.well-known probe across arimagenomics.com, discovery.arimagenomics.com and courses.arimagenomics.com returned 404 while api./developer./docs.arimagenomics.com do not resolve.
  evidence:
  - status: 404
    url: https://arimagenomics.com/openapi.json
  - status: 404
    url: https://discovery.arimagenomics.com/openapi.json
  - status: 404
    url: https://arimagenomics.com/.well-known/agent-card.json
  - status: 200
    url: https://discovery.arimagenomics.com/documentation/
  - status: 200
    url: https://github.com/ArimaGenomics
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Arima Genomics is a San Diego based cancer diagnostics company built on Hi-C sequencing and 3D genome science. Founded in 2015 to study how DNA is organized in three dimensions, the company now develops clinical tests and technology platforms that detect cancer-driving structural alterations — noncanonical fusions, enhancer hijacking, extrachromosomal DNA (ecDNA) and complex rearrangements — from routine FFPE tumor tissue that conventional DNA and RNA profiling can leave unresolved. Its surface spans research products (Arima-HiC+, Arima High Coverage HiC, Promoter and Custom Capture HiC, HiC FFPE, Arima CiFi), lab services including Single Cell Methyl-3C and multi-omics, the Aventa FusionPlus and Aventa Lymphoma clinical tests, and biopharma partnership programs. Arima publishes open-source bioinformatics pipelines on GitHub (Arima-HiC mapping pipeline, Arima-CHiC, Arima-SV-Pipeline) but operates no public web API, developer portal or machine-readable specification.
image: http://static1.squarespace.com/static/69efef935d9d4c389c1f1e7a/t/6a06451aea5c316731756a9f/1778795802107/ArimaGenomics_Logo_FullColor_Large_150dpi.png?format=1500w
layout: provider
modified: '2026-08-06'
name: Arima Genomics
nav: Providers
network: true
overview: 'Arima Genomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Cancer Diagnostics, Life Sciences, and Sequencing.


  Arima Genomics'' developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 79
score:
  band: minimal
  composite: 12.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arima-genomics/refs/heads/main/screenshots/arima-genomics-2026-08-07T161705.png
security:
- kind: domain-security
  name: Arima Genomics Domain Security
  slug: arima-genomics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arima-genomics
tags:
- Company
- Genomics
- Cancer Diagnostics
- Life Sciences
- Sequencing
- Bioinformatics
- Precision Medicine
- Biotechnology
website: https://arimagenomics.com/
---
