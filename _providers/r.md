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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: R Agentic Access
  operation_count: 14
  slug: r-agentic-access
  summary_line: 14 operations
api_count: 3
apis:
- baseURL: https://crandb.r-pkg.org
  baseurl_source: declared
  description: Download count badge endpoints
  name: R Badges API
  slug: r-badges-api
- baseURL: https://crandb.r-pkg.org
  baseurl_source: declared
  description: Package download statistics
  name: R Downloads API
  slug: r-downloads-api
- baseURL: https://crandb.r-pkg.org
  baseurl_source: declared
  description: CRAN package metadata
  name: R Packages API
  slug: r-packages-api
- baseURL: https://crandb.r-pkg.org
  baseurl_source: declared
  description: Most-downloaded CRAN packages
  name: R Top Packages API
  slug: r-top-packages-api
- baseURL: https://crandb.r-pkg.org
  baseurl_source: declared
  description: R release version information
  name: R Versions API
  slug: r-versions-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: METACRAN CranDB Badges API
  slug: open-r-badges-api
- collection_type: open
  name: METACRAN CranDB Badges Downloads API
  slug: open-r-downloads-api
- collection_type: open
  name: METACRAN CranDB API
  slug: open-r-metacran-crandb
- collection_type: open
  name: METACRAN CranLogs API
  slug: open-r-metacran-cranlogs
- collection_type: open
  name: METACRAN CranDB Badges Packages API
  slug: open-r-packages-api
- collection_type: open
  name: R Versions API
  slug: open-r-rversions
- collection_type: open
  name: METACRAN CranDB Badges Top Packages API
  slug: open-r-top-packages-api
- collection_type: open
  name: METACRAN CranDB Badges Versions API
  slug: open-r-versions-api
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
overview: 'R publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Badges API, Downloads API, Packages API, and 2 more. Tagged areas include R, Statistics, Data Science, Open-Source, and Programming Language.


  The R catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  R''s developer surface includes documentation, engineering blog, Stack Overflow tag, and 10 more developer resources.'
plans:
- name: R Plans Pricing
  plan_count: 3
  slug: r-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: R Rate Limits
  slug: r-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: R API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: r-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: R API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 10
  slug: r-spectral-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 55.8
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- Programming Language
website: https://www.r-project.org/
---
