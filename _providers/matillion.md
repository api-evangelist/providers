---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Matillion Agentic Access
  operation_count: 44
  slug: matillion-agentic-access
  summary_line: 44 operations · 19 acting
api_count: 1
apis:
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Data Productivity Cloud Agents (hybrid runtime).
  name: Matillion DPC Agents API
  slug: matillion-dpc-agents-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Data Productivity Cloud environments (warehouse connection contexts).
  name: Matillion DPC Environments API
  slug: matillion-dpc-environments-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Launch, inspect, and cancel Data Productivity Cloud pipeline executions.
  name: Matillion DPC Pipeline Executions API
  slug: matillion-dpc-pipeline-executions-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Data Productivity Cloud projects.
  name: Matillion DPC Projects API
  slug: matillion-dpc-projects-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Data Productivity Cloud pipeline schedules.
  name: Matillion DPC Schedules API
  slug: matillion-dpc-schedules-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Legacy Matillion ETL groups, projects, and versions.
  name: Matillion ETL Groups & Projects API
  slug: matillion-etl-groups-projects-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Legacy Matillion ETL job execution and validation.
  name: Matillion ETL Jobs & Runs API
  slug: matillion-etl-jobs-runs-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Legacy Matillion ETL schedules.
  name: Matillion ETL Schedules API
  slug: matillion-etl-schedules-api
- baseURL: https://eu1.api.matillion.com/dpc
  baseurl_source: declared
  description: Legacy Matillion ETL task monitoring and control.
  name: Matillion ETL Tasks API
  slug: matillion-etl-tasks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Matillion DPC Agents API
  slug: open-matillion-dpc-agents-api
- collection_type: open
  name: Matillion DPC Agents DPC Environments API
  slug: open-matillion-dpc-environments-api
- collection_type: open
  name: Matillion DPC Agents DPC Pipeline Executions API
  slug: open-matillion-dpc-pipeline-executions-api
- collection_type: open
  name: Matillion DPC Agents DPC Projects API
  slug: open-matillion-dpc-projects-api
- collection_type: open
  name: Matillion DPC Agents DPC Schedules API
  slug: open-matillion-dpc-schedules-api
- collection_type: open
  name: Matillion DPC Agents ETL Groups & Projects API
  slug: open-matillion-etl-groups-projects-api
- collection_type: open
  name: Matillion DPC Agents ETL Jobs & Runs API
  slug: open-matillion-etl-jobs-runs-api
- collection_type: open
  name: Matillion DPC Agents ETL Schedules API
  slug: open-matillion-etl-schedules-api
- collection_type: open
  name: Matillion DPC Agents ETL Tasks API
  slug: open-matillion-etl-tasks-api
- collection_type: open
  name: Matillion API
  slug: open-matillion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matillion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matillion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matillion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/matillion-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matillion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matillion
- group: company
  title: ''
  type: Website
  url: https://www.matillion.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.matillion.com
- group: commercial
  title: ''
  type: Plans
  url: plans/matillion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matillion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/matillion-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.matillion.com/blog
created: '2026-07-01'
description: Matillion is a data integration and transformation (ETL/ELT) company whose Data Productivity Cloud (DPC) lets teams build, orchestrate, and schedule data pipelines against cloud data warehouses. The DPC API is an OAuth2-secured REST control plane for projects, environments, pipeline executions, schedules, and Agents, while the legacy instance-hosted Matillion ETL API exposes groups, projects, versions, jobs, tasks, and schedules over HTTP Basic auth.
finops:
- name: Matillion Finops
  service_category: Analytics and Data Integration
  slug: matillion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matillion.png
layout: provider
modified: '2026-07-01'
name: Matillion
nav: Providers
network: true
overview: 'Matillion publishes 9 APIs on the [APIs.io](https://apis.io/) network, including DPC Agents API, DPC Environments API, DPC Pipeline Executions API, and 6 more. Tagged areas include Data Integration, ETL, ELT, Data Pipeline, and Cloud Data Warehouse.


  Matillion''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Matillion Plans Pricing
  plan_count: 5
  slug: matillion-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Matillion Rate Limits
  slug: matillion-rate-limits
scopes:
- name: Matillion Scopes
  scope_count: 1
  slug: matillion-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 46.5
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/screenshots/matillion-2026-07-25T230414.png
security:
- kind: authentication
  name: Matillion Authentication
  slug: matillion-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Matillion Domain Security
  slug: matillion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matillion
tags:
- Data Integration
- ETL
- ELT
- Data Pipeline
- Cloud Data Warehouse
website: https://www.matillion.com
---
