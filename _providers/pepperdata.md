---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://dashboard.pepperdata.com/pepperdata-demonstration/api
  baseurl_source: declared
  description: Create, retrieve, revise, and delete metric alarms.
  name: Pepperdata Alarms API
  slug: pepperdata-alarms-api
- baseURL: https://dashboard.pepperdata.com/pepperdata-demonstration/api
  baseurl_source: declared
  description: Query application/job details, counters, and tuning recommendations.
  name: Pepperdata Job Details API
  slug: pepperdata-job-details-api
- baseURL: https://dashboard.pepperdata.com/pepperdata-demonstration/api
  baseurl_source: declared
  description: Retrieve time-series metrics, series, and filters.
  name: Pepperdata Metrics API
  slug: pepperdata-metrics-api
artifact_total: 12
collections:
- collection_type: open
  name: Pepperdata REST Alarms API
  slug: open-pepperdata-alarms-api
- collection_type: open
  name: Pepperdata REST Alarms Job Details API
  slug: open-pepperdata-job-details-api
- collection_type: open
  name: Pepperdata REST Alarms Metrics API
  slug: open-pepperdata-metrics-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.pepperdata.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.pepperdata.com/feed/
- group: other
  href: https://artifacts.apis.io/pepperdata/overlays/pepperdata-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pepperdata-rest-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/pepperdata/authentication/pepperdata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pepperdata-authentication.yml
- group: design
  href: https://artifacts.apis.io/pepperdata/conventions/pepperdata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pepperdata-conventions.yml
- group: design
  href: https://artifacts.apis.io/pepperdata/errors/pepperdata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pepperdata-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pepperdata/conformance/pepperdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pepperdata-conformance.yml
- group: design
  href: https://artifacts.apis.io/pepperdata/data-model/pepperdata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pepperdata-data-model.yml
- group: build
  href: https://artifacts.apis.io/pepperdata/packages/pepperdata-packages.yml
  title: ''
  type: Packages
  url: packages/pepperdata-packages.yml
- group: agent
  href: https://artifacts.apis.io/pepperdata/mcp/pepperdata-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/pepperdata-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pepperdata/llms/pepperdata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pepperdata-llms.txt
- group: agent
  href: https://artifacts.apis.io/pepperdata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/pepperdata/security/pepperdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pepperdata-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pepperdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pepperdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pepperdata.com/rest-api/
- group: company
  title: ''
  type: Blog
  url: https://www.pepperdata.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.pepperdata.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pepperdata.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.pepperdata.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://dashboard.pepperdata.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pepperdata.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pepperdata.com/legal/privacy-policy#terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pepperdata
- group: company
  title: ''
  type: Website
  url: https://www.pepperdata.com/
created: '2026-07-17'
description: 'Pepperdata provides dynamic Kubernetes resource optimization and observability for data-intensive workloads, increasing cluster utilization, improving performance, and reducing cost in real time across Spark, MapReduce, Tez, and Kubernetes environments. Its REST API gives programmatic access to the same observability data available in the Pepperdata dashboard: time-series metrics with series breakdowns and filters (/m), application and job details including counters and cost/performance tuning recommendations (/jobdetails), and full CRUD over metric alarms (/alarms). Authentication uses a custom API-key header. Pepperdata is a portfolio company of Wing Venture Capital.'
image: https://www.pepperdata.com/wp-content/uploads/2025/03/normal-logo-1200px.png
layout: provider
modified: '2026-10-06'
name: Pepperdata
nav: Providers
network: true
overview: 'Pepperdata is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Alarms API, Job Details API, and Metrics API. Tagged areas include Company, Observability, Monitoring, Kubernetes, and Big Data.


  The Pepperdata catalog on APIs.io includes 1 Spectral governance ruleset.


  Pepperdata''s developer surface includes engineering blog, authentication, documentation, API reference, support, pricing, signup flow, and 18 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Pepperdata API Rules
  rule_count: 63
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 2
  slug: pepperdata-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 17.7
    developer_ergonomics: 42.3
    discoverability: 78.6
    operational_transparency: 2.6
  previous_composite: 32.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pepperdata/pepperdata-2026-08-17T081155.png
security:
- kind: authentication
  name: Pepperdata Authentication
  slug: pepperdata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pepperdata Domain Security
  slug: pepperdata-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 3
skills:
- name: Pull Pepperdata job tuning recommendations
  slug: pepperdata-analyze-job-recommendations
- name: Create a Pepperdata metric alarm
  slug: pepperdata-create-alarm
- name: Query Pepperdata time-series metrics
  slug: pepperdata-query-metrics
slug: pepperdata
tags:
- Company
- Observability
- Monitoring
- Kubernetes
- Big Data
- Cost Optimization
- Metrics
- APM
website: https://www.pepperdata.com/
---
