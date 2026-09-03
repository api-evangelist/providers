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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://nuprobe.com/
- group: company
  title: ''
  type: Blog
  url: https://nuprobe.com/all-news/
- group: operate
  title: ''
  type: Support
  url: https://nuprobe.com/contact_us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuprobe.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuprobe.com/nuprobe-usa-terms-and-conditions/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuprobe-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: NuProbe sells BDA and QASeq molecular-diagnostics assay kits, custom assay development and biopharma lab services rather than software; 1,199 archived URLs for nuprobe.com contain no /developers, /docs, /api, swagger, openapi or graphql path, both company GitHub organizations (NuProbeUSA, NuProbe-Bioinfo) hold zero public repositories, no nuprobe package exists on npm, PyPI, crates.io or RubyGems, and the marketing site itself is additionally returning a Cloudflare 526 origin error on every path during this pass.
  evidence:
  - status: 526
    url: https://nuprobe.com/openapi.json
  - status: 526
    url: https://nuprobe.com/.well-known/api-catalog
  - status: 200
    url: http://web.archive.org/cdx/search/cdx?url=nuprobe.com*&output=text&fl=original,statuscode&collapse=urlkey&limit=3000
  - status: 200
    url: https://api.github.com/orgs/NuProbeUSA/repos
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=nuprobe
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'NuProbe is a genomics and molecular diagnostics company founded in 2016 on technology licensed from the Wyss Institute at Harvard University and Rice University, with headquarters in Shanghai, China and a US subsidiary, NuProbe USA, in Houston, Texas. Its two core chemistries are Blocker Displacement Amplification (BDA), which enriches low-frequency DNA variants ahead of sequencing or PCR, and Quantitative Amplicon Sequencing (QASeq), a UMI-based multiplexed amplicon method for the simultaneous ultrasensitive detection of mutations and copy number variations from FFPE tissue, fresh or frozen tissue and cell-free DNA. The company sells research-use assay panels for oncology and reproductive health, custom assay development, and biopharma services, and has licensed or co-developed its chemistry with Bio-Rad, Oxford Nanopore, QIAGEN, Illumina and Bionano. NuProbe is an assay and reagent company: its bioinformatics and primer-design algorithms are delivered inside its products
  and services rather than as a public developer platform, and it publishes no API, SDK, developer portal or machine-readable specification of any kind.'
image: https://nuprobe.com/wp-content/uploads/2021/04/NuProbe-PMS-Logo_for-website.png
layout: provider
modified: '2026-08-26'
name: NuProbe
nav: Providers
network: true
overview: 'NuProbe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Genomics, Molecular Diagnostics, and Next-Generation Sequencing.


  NuProbe''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Nuprobe Domain Security
  slug: nuprobe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nuprobe
tags:
- Company
- Life Sciences
- Genomics
- Molecular Diagnostics
- Next-Generation Sequencing
- Oncology
- Biotechnology
- Precision Medicine
- Laboratory
website: https://nuprobe.com/
---
