---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: R Agentic Access
  operation_count: 14
  slug: r-agentic-access
  summary_line: 14 operations
api_count: 5
apis:
- description: Download count badge endpoints
  name: R Badges API
  slug: r-badges-api
- description: Package download statistics
  name: R Downloads API
  slug: r-downloads-api
- description: CRAN package metadata
  name: R Packages API
  slug: r-packages-api
- description: Most-downloaded CRAN packages
  name: R Top Packages API
  slug: r-top-packages-api
- description: R release version information
  name: R Versions API
  slug: r-versions-api
artifact_total: 23
collections:
- collection_type: open
  name: METACRAN CranDB API
  slug: open-r-metacran-crandb
- collection_type: open
  name: METACRAN CranLogs API
  slug: open-r-metacran-cranlogs
- collection_type: open
  name: R Versions API
  slug: open-r-rversions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/r-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/r-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.r-project.org/
- group: docs
  title: ''
  type: Documentation
  url: https://cran.r-project.org/manuals.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/r-lib
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/r-devel
- group: start
  title: ''
  type: PackageRegistry
  url: https://cran.r-project.org/
- group: start
  title: ''
  type: PackageRegistry
  url: https://bioconductor.org/
- group: build
  title: ''
  type: PackageSearch
  url: https://www.rdocumentation.org/
- group: build
  title: ''
  type: PackageSearch
  url: https://rdrr.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.r-project.org/
- group: operate
  title: ''
  type: Forums
  url: https://stat.ethz.ch/mailman/listinfo/r-help
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/r
created: '2025-01-01'
description: R is a free, open-source programming language and statistical computing environment maintained by the R Core Team and supported by the R Foundation. It provides a wide variety of statistical and graphical techniques and is highly extensible through its package ecosystem on CRAN (Comprehensive R Archive Network), Bioconductor, and GitHub. R is widely used among statisticians, data scientists, and researchers for data analysis, visualization, and reproducible research.
examples:
- key_count: 2
  name: R Get Package Download Totals Example
  slug: r-get-package-download-totals-example
- key_count: 2
  name: R Get Package Metadata Example
  slug: r-get-package-metadata-example
- key_count: 2
  name: R Get R Release Example
  slug: r-get-r-release-example
finops:
- name: R Finops
  service_category: API
  slug: r-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/r.png
json_schemas:
- name: CRAN Package
  property_count: 18
  slug: r-cran-package
- name: CRAN Package Download Statistics
  property_count: 4
  slug: r-download-stats
- name: R Version
  property_count: 3
  slug: r-version
json_structures:
- name: R Cran Package Structure
  property_count: 0
  slug: r-cran-package-structure
jsonld:
- class_count: 8
  name: R Context
  property_count: 10
  slug: r-context
layout: provider
modified: '2026-05-19'
name: R
nav: Providers
network: true
overview: 'R publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Badges API, Downloads API, Packages API, and 2 more. Tagged areas include R, Statistics, Data Science, Open Source, and Programming Language.


  The R catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  R''s developer surface includes documentation, engineering blog, Stack Overflow tag, and 10 more developer resources.'
plans:
- name: R Plans Pricing
  plan_count: 3
  slug: r-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 5
  name: R Rate Limits
  slug: r-rate-limits
rules:
- name: R API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: r-jsonschema-spectral-rules
- name: R API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 10
  slug: r-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/r/refs/heads/main/screenshots/r-2026-06-20T192458.png
security:
- kind: domain-security
  name: R Domain Security
  slug: r-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: r
tags:
- R
- Statistics
- Data Science
- Open Source
- Programming Language
website: https://www.r-project.org/
---
