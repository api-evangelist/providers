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
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vizgen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vizgen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vizgen.github.io/vizgen-postprocessing/
- group: start
  title: ''
  type: GettingStarted
  url: https://vizgen.github.io/vizgen-postprocessing/installation.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vizgen
- group: operate
  title: ''
  type: Support
  url: https://vizgen.com/vizgen-support-vizgen/
- group: company
  title: ''
  type: Blog
  url: https://vizgen.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vizgen.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vizgen.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vizgen_stock/
- group: build
  title: ''
  type: Packages
  url: packages/vizgen-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vizgen-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vizgen-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vizgen-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vizgen-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/vizgen-segmentation-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vizgen-llms.txt
created: '2026-08-05'
description: Vizgen is a spatial biology company building integrated spatial multiomics platforms for single-cell research. Its MERSCOPE and MERSCOPE Ultra instruments use MERFISH imaging-based spatial transcriptomics to map up to 1,000 RNA targets in intact tissue at subcellular resolution, complemented by InSituPlex multiplex protein immunofluorescence assays (OmniVUE and custom U-VUE panels) and the STARVUE analysis software. Vizgen publishes no public REST, GraphQL, or event API; its developer surface is open-source data tooling — the Apache-2.0 Vizgen Post-processing Tool (VPT), a Python CLI and library distributed on PyPI and Docker Hub with a plugin architecture for segmentation algorithms, published from the Vizgen GitHub organization alongside documented MERSCOPE output data formats.
examples:
- key_count: 4
  name: Vizgen Cellpose_Default_1_Zlevel
  slug: vizgen-cellpose_default_1_ZLevel
- key_count: 4
  name: Vizgen Cellpose_Default_3_Zlevel
  slug: vizgen-cellpose_default_3_ZLevel
- key_count: 4
  name: Vizgen Cellpose_Default_3_Zlevel_Nuclei_Only
  slug: vizgen-cellpose_default_3_ZLevel_nuclei_only
- key_count: 4
  name: Vizgen Watershed_Default
  slug: vizgen-watershed_default
image: https://vizgen.com/wp-content/uploads/2021/05/cropped-Favicon-1-270x270.png
layout: provider
modified: '2026-08-05'
name: Vizgen
nav: Providers
network: true
overview: 'Vizgen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spatial Biology, Spatial Transcriptomics, Genomics, and Life Sciences.


  Vizgen''s developer surface includes documentation, getting-started guide, support, engineering blog, CLI, changelog, code examples, and 10 more developer resources.'
random_paper: 63
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Vizgen Domain Security
  slug: vizgen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vizgen
tags:
- Company
- Spatial Biology
- Spatial Transcriptomics
- Genomics
- Life Sciences
- Bioinformatics
- Single Cell Analysis
- Scientific Instruments
- Open Source
- Command Line Tools
website: https://vizgen.com/
---
