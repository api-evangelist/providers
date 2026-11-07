---
access_model:
  confidence: high
  label: Free, no registration, anonymous access
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://data-openjustice.doj.ca.gov/jsonapi
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: California Attorney General Agentic Access
  operation_count: 68
  slug: california-attorney-general-agentic-access
  summary_line: 68 operations · 3 acting
api_count: 1
apis:
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: Datasets, publications, stats pages, data stories and site pages (node entities).
  name: California Attorney General Content API
  slug: california-attorney-general-content-api
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: The JSON:API index.
  name: California Attorney General Discovery API
  slug: california-attorney-general-discovery-api
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: The three anonymous feedback creates the site footer uses.
  name: California Attorney General Feedback API
  slug: california-attorney-general-feedback-api
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: Downloadable distributions.
  name: California Attorney General Files API
  slug: california-attorney-general-files-api
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: Composable page fragments (charts, tabs, report years, blocks).
  name: California Attorney General Paragraphs API
  slug: california-attorney-general-paragraphs-api
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: Drupal config entities readable anonymously.
  name: California Attorney General Site Configuration API
  slug: california-attorney-general-site-configuration-api
- baseURL: https://data-openjustice.doj.ca.gov/jsonapi
  baseurl_source: declared
  description: Vocabularies used to classify content.
  name: California Attorney General Taxonomies API
  slug: california-attorney-general-taxonomies-api
artifact_total: 21
common:
- group: commercial
  href: https://artifacts.apis.io/california-attorney-general/plans/california-attorney-general-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/california-attorney-general-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/california-attorney-general/rate-limits/california-attorney-general-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/california-attorney-general-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/california-attorney-general/overlays/california-attorney-general-openjustice-jsonapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/california-attorney-general-openjustice-jsonapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/california-attorney-general/agentic-access/california-attorney-general-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/california-attorney-general-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/california-attorney-general/security/california-attorney-general-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/california-attorney-general-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oag.ca.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://openjustice.doj.ca.gov/data
- group: operate
  title: ''
  type: Support
  url: https://oag.ca.gov/research-services/request-process
- group: company
  title: ''
  type: Blog
  url: https://oag.ca.gov/media/news
- group: company
  title: ''
  type: BlogRSS
  url: https://oag.ca.gov/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oag.ca.gov/conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oag.ca.gov/privacy-policy
- group: agent
  href: https://artifacts.apis.io/california-attorney-general/well-known/california-attorney-general-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/california-attorney-general-well-known.yml
- group: build
  href: https://artifacts.apis.io/california-attorney-general/packages/california-attorney-general-packages.yml
  title: ''
  type: Packages
  url: packages/california-attorney-general-packages.yml
- group: agent
  href: https://artifacts.apis.io/california-attorney-general/llms/california-attorney-general-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/california-attorney-general-llms.txt
- group: agent
  href: https://artifacts.apis.io/california-attorney-general/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/california-attorney-general/datasets/california-attorney-general-datasets.yml
  title: ''
  type: Datasets
  url: datasets/california-attorney-general-datasets.yml
created: '2026-09-17'
description: The California Attorney General is the chief law officer of the State of California and heads the California Department of Justice (DOJ). The office runs OpenJustice, the DOJ Criminal Justice Statistics Center's open-data initiative, whose Open Data Portal publishes 26 criminal-justice datasets (Arrests, Crimes and Clearances, Homicide, Hate Crime, Use of Force, RIPA stop data, deaths in custody and more) as CSV/XLSX/ZIP files with context PDFs. The DOJ publishes no developer portal, API documentation or OpenAPI, but the OpenJustice single-page app reads its content from a live, anonymous, standards-conformant JSON:API 1.0 surface at https://data-openjustice.doj.ca.gov/jsonapi (Drupal 9) carrying every dataset, its distributions, the CJSC publications and the data stories — verified here. The California Data Broker Registry that first brought this office into the catalog is now maintained by the California Privacy Protection Agency, per the AG's own page, and is attributed there.
examples:
- key_count: 5
  name: California Attorney General Datasets Include Example
  slug: california-attorney-general-datasets-include-example
- key_count: 4
  name: California Attorney General Datasets Sparse Fieldset Example
  slug: california-attorney-general-datasets-sparse-fieldset-example
- key_count: 2
  name: California Attorney General Error 400 Example
  slug: california-attorney-general-error-400-example
- key_count: 2
  name: California Attorney General Error 401 Write Example
  slug: california-attorney-general-error-401-write-example
- key_count: 2
  name: California Attorney General Error 404 Example
  slug: california-attorney-general-error-404-example
- key_count: 3
  name: California Attorney General Jsonapi Index Example
  slug: california-attorney-general-jsonapi-index-example
- key_count: 3
  name: California Attorney General Stats Filter Example
  slug: california-attorney-general-stats-filter-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-09-17'
name: California Attorney General
nav: Providers
network: true
overview: 'California Attorney General publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Content API, Discovery API, Feedback API, and 4 more. Tagged areas include State Government, California, Criminal Justice, Open Data, and Law Enforcement.


  The California Attorney General catalog on APIs.io includes 1 Spectral governance ruleset.


  California Attorney General''s developer surface includes documentation, support, engineering blog, and 14 more developer resources.'
plans:
- name: California Attorney General Plans Pricing
  plan_count: 0
  slug: california-attorney-general-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: California Attorney General Rate Limits
  slug: california-attorney-general-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: California Attorney General API Rules
  rule_count: 60
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 9
  slug: california-attorney-general-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 33.7
    developer_ergonomics: 20.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/california-attorney-general/california-attorney-general-2026-10-11T102652.png
security:
- kind: authentication
  name: California Attorney General Authentication
  slug: california-attorney-general-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: California Attorney General Domain Security
  slug: california-attorney-general-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
skill_count: 1
skills:
- name: california-doj-download-openjustice-dataset
  slug: california-attorney-general-download-openjustice-dataset
slug: california-attorney-general
tags:
- State Government
- California
- Criminal Justice
- Open Data
- Law Enforcement
- Crime Statistics
- Government Data
- JSON:API
- Public Records
- Attorney General
website: https://oag.ca.gov/
---
