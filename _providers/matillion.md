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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-10-04'
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
artifact_total: 49
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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/well-known/matillion-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/matillion-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/well-known/matillion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/matillion-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/rules/matillion-rules.yml
  title: ''
  type: Spectral
  url: rules/matillion-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/json-ld/matillion-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/matillion-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/vocabulary/matillion-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/matillion-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/data-model/matillion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/matillion-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/conformance/matillion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/matillion-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/hosts/matillion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/matillion-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/vendors/matillion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/matillion-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.matillion.com/trust-center
- group: operate
  title: ''
  type: Support
  url: https://support.matillion.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.matillion.com/
- group: auth
  title: ''
  type: Security
  url: https://www.matillion.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matillion.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.matillion.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.matillion.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.matillion.com/leadership/tim-oneil
- group: operate
  title: ''
  type: ChangeLog
  url: https://roadmap.matillion.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.matillion.com/data-productivity-cloud/cdc/docs/cdc-getting-started/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/agentic-access/matillion-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/matillion-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/security/matillion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/matillion-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/authentication/matillion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/matillion-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/scopes/matillion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/matillion-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matillion
- group: company
  title: ''
  type: Website
  url: https://www.matillion.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.matillion.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/plans/matillion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/matillion-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/rate-limits/matillion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/matillion-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/matillion/refs/heads/main/finops/matillion-finops.yml
  title: ''
  type: FinOps
  url: finops/matillion-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.matillion.com/blog
coverage:
  checked: '2026-10-04'
  detail: Documentation site renders via JavaScript, preventing retrieval of machine-readable specs.
  evidence:
  - status: 200
    url: https://docs.matillion.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-07-01'
description: Matillion is a data integration and transformation (ETL/ELT) company whose Data Productivity Cloud (DPC) lets teams build, orchestrate, and schedule data pipelines against cloud data warehouses. The DPC API is an OAuth2-secured REST control plane for projects, environments, pipeline executions, schedules, and Agents, while the legacy instance-hosted Matillion ETL API exposes groups, projects, versions, jobs, tasks, and schedules over HTTP Basic auth.
finops:
- name: Matillion Finops
  service_category: Analytics and Data Integration
  slug: matillion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matillion.png
json_schemas:
- name: AgentCreate
  property_count: 1
  slug: matillion-agent-create
- name: AgentCredentials
  property_count: 2
  slug: matillion-agent-credentials
- name: AgentList
  property_count: 1
  slug: matillion-agent-list
- name: Agent
  property_count: 3
  slug: matillion-agent
- name: EnvironmentCreate
  property_count: 2
  slug: matillion-environment-create
- name: EnvironmentList
  property_count: 1
  slug: matillion-environment-list
- name: Environment
  property_count: 3
  slug: matillion-environment
- name: EtlJobRunRequest
  property_count: 2
  slug: matillion-etl-job-run-request
- name: EtlJobRunResponse
  property_count: 2
  slug: matillion-etl-job-run-response
- name: PipelineExecutionList
  property_count: 1
  slug: matillion-pipeline-execution-list
- name: PipelineExecutionRequest
  property_count: 3
  slug: matillion-pipeline-execution-request
- name: PipelineExecution
  property_count: 3
  slug: matillion-pipeline-execution
- name: PipelineExecutionStatus
  property_count: 2
  slug: matillion-pipeline-execution-status
- name: PipelineExecutionSteps
  property_count: 1
  slug: matillion-pipeline-execution-steps
- name: ProjectCreate
  property_count: 2
  slug: matillion-project-create
- name: ProjectList
  property_count: 1
  slug: matillion-project-list
- name: Project
  property_count: 3
  slug: matillion-project
- name: ScheduleCreate
  property_count: 5
  slug: matillion-schedule-create
- name: ScheduleList
  property_count: 1
  slug: matillion-schedule-list
- name: Schedule
  property_count: 6
  slug: matillion-schedule
jsonld:
- class_count: 20
  name: Matillion Context
  property_count: 18
  slug: matillion-context
layout: provider
modified: '2026-07-01'
name: Matillion
nav: Providers
network: true
overview: 'Matillion publishes 9 APIs on the [APIs.io](https://apis.io/) network, including DPC Agents API, DPC Environments API, DPC Pipeline Executions API, and 6 more. Tagged areas include Data Integration, ETL, ELT, Data Pipeline, and Cloud Data Warehouse.


  The Matillion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Matillion''s developer surface includes support, pricing, changelog, getting-started guide, authentication, documentation, engineering blog, and 24 more developer resources.'
plans:
- name: Matillion Plans Pricing
  plan_count: 5
  slug: matillion-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Matillion Rate Limits
  slug: matillion-rate-limits
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Matillion API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: matillion-rules
scopes:
- name: Matillion Scopes
  scope_count: 1
  slug: matillion-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.6
    catalog_earned_first_party: 0.0
    catalog_gap: 28.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.7
  facets:
    access_clarity: 65.3
    contract_governance: 19.7
    contract_quality: 53.0
    developer_ergonomics: 42.3
    discoverability: 69.6
    operational_transparency: 73.2
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
