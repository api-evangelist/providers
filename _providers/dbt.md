---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Dbt Agentic Access
  operation_count: 12
  slug: dbt-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 3
apis:
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Accounts API from dbt — 1 operation(s) for accounts.
  name: dbt Accounts API
  slug: dbt-accounts-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Environments API from dbt — 1 operation(s) for environments.
  name: dbt Environments API
  slug: dbt-environments-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Jobs API from dbt — 1 operation(s) for jobs.
  name: dbt Jobs API
  slug: dbt-jobs-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Metrics API from dbt — 1 operation(s) for metrics.
  name: dbt Metrics API
  slug: dbt-metrics-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Projects API from dbt — 2 operation(s) for projects.
  name: dbt Projects API
  slug: dbt-projects-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Runs API from dbt — 4 operation(s) for runs.
  name: dbt Runs API
  slug: dbt-runs-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The FastAPI API from dbt — 1 operation(s) for fastapi.
  name: dbt Fast API
  slug: dbt-fastapi-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Private API from dbt — 1 operation(s) for private.
  name: dbt Private API
  slug: dbt-private-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Ready API from dbt — 1 operation(s) for ready.
  name: dbt Ready API
  slug: dbt-ready-api
- baseURL: https://cloud.getdbt.com/api/v3
  baseurl_source: declared
  description: The Graph QL API from dbt — 1 operation(s) for graph ql.
  name: dbt Graph QL API
  slug: dbt-graph-ql-api
arazzos:
- description: Walk from the first account to its projects to its jobs to build a hierarchy snapshot.
  name: dbt Cloud Account, Project and Job Inventory
  slug: dbt-account-project-job-inventory-workflow
- description: Resolve account, project and environment, create a job, and trigger its first run.
  name: dbt Cloud Bootstrap From Account to First Run
  slug: dbt-bootstrap-account-and-run-workflow
- description: Create a new job in a project environment, then immediately trigger a run of it.
  name: dbt Cloud Create Job and Run It
  slug: dbt-create-job-and-run-workflow
- description: Create a job, trigger it, poll the run to success (status 10), and list artifacts.
  name: dbt Cloud Create, Run, Poll and Collect Artifacts
  slug: dbt-create-run-poll-artifacts-workflow
- description: Pick an environment, create a job in it, and trigger the job's first run.
  name: dbt Cloud Environment-Scoped Job Run
  slug: dbt-environment-job-run-workflow
- description: List jobs in an account, fetch the job's configuration, then trigger a run of it.
  name: dbt Cloud Find Job and Trigger Run
  slug: dbt-find-job-and-run-workflow
- description: List runs, read the most recent run, and fetch its artifacts when it succeeded.
  name: dbt Cloud Job Run History and Latest Artifacts
  slug: dbt-job-run-history-workflow
- description: Resolve a project and one of its environments, then create a job bound to both.
  name: dbt Cloud Provision a Job in a Project Environment
  slug: dbt-provision-job-in-environment-workflow
- description: Inspect the most recent run, and if it failed, re-trigger its job.
  name: dbt Cloud Re-run the Latest Failed Run
  slug: dbt-rerun-latest-failed-run-workflow
- description: Read a run, branch on whether it succeeded, and list its artifacts only on success.
  name: dbt Cloud Get Run and Fetch Its Artifacts
  slug: dbt-run-and-fetch-artifacts-workflow
- description: Confirm a run succeeded, then query the Discovery API for the models it produced.
  name: dbt Cloud Run Completion to Metadata Discovery
  slug: dbt-run-metadata-discovery-workflow
- description: Confirm a run succeeded, then query the Semantic Layer API for available metrics.
  name: dbt Cloud Run Completion to Semantic Layer Metrics
  slug: dbt-run-to-semantic-metrics-workflow
- description: Trigger a dbt Cloud job run, poll the run until it succeeds, then list its artifacts.
  name: dbt Cloud Trigger Run and Poll to Completion
  slug: dbt-trigger-run-and-poll-workflow
artifact_total: 50
collections:
- collection_type: postman
  name: dbt Cloud Administrative API
  slug: postman-dbt-cloud-administrative-api
- collection_type: postman
  name: dbt Cloud Discovery API
  slug: postman-dbt-cloud-discovery-api
- collection_type: postman
  name: dbt Cloud Semantic Layer API
  slug: postman-dbt-cloud-semantic-layer-api
- collection_type: open
  name: dbt Cloud Administrative Accounts API
  slug: open-dbt-accounts-api
- collection_type: open
  name: dbt Cloud Administrative API
  slug: open-dbt-cloud-administrative-api
- collection_type: open
  name: dbt Cloud Discovery API
  slug: open-dbt-cloud-discovery-api
- collection_type: open
  name: dbt Cloud Semantic Layer API
  slug: open-dbt-cloud-semantic-layer-api
- collection_type: open
  name: dbt Cloud Administrative Accounts Environments API
  slug: open-dbt-environments-api
- collection_type: open
  name: dbt Cloud Administrative Accounts Jobs API
  slug: open-dbt-jobs-api
- collection_type: open
  name: dbt Cloud Administrative Accounts Metadata API
  slug: open-dbt-metadata-api
- collection_type: open
  name: dbt Cloud Administrative Accounts Metrics API
  slug: open-dbt-metrics-api
- collection_type: open
  name: dbt Cloud Administrative Accounts Projects API
  slug: open-dbt-projects-api
- collection_type: open
  name: dbt Cloud Administrative Accounts Runs API
  slug: open-dbt-runs-api
common:
- group: commercial
  href: https://artifacts.apis.io/dbt/plans/dbt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dbt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dbt/rate-limits/dbt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dbt-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dbt/finops/dbt-finops.yml
  title: ''
  type: FinOps
  url: finops/dbt-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.getdbt.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://docs.getdbt.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/dbt/capabilities/dbt-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dbt-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/dbt/agentic-access/dbt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dbt-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dbt/security/dbt-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dbt-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dbt/security/dbt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dbt-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dbt/authentication/dbt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dbt-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dbt/overview
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-account-project-job-inventory-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-account-project-job-inventory-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-bootstrap-account-and-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-bootstrap-account-and-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-create-job-and-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-create-job-and-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-create-run-poll-artifacts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-create-run-poll-artifacts-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-environment-job-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-environment-job-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-find-job-and-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-find-job-and-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-job-run-history-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-job-run-history-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-provision-job-in-environment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-provision-job-in-environment-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-rerun-latest-failed-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-rerun-latest-failed-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-run-and-fetch-artifacts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-run-and-fetch-artifacts-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-run-metadata-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-run-metadata-discovery-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-run-to-semantic-metrics-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-run-to-semantic-metrics-workflow.yml
- group: design
  href: https://artifacts.apis.io/dbt/arazzo/dbt-trigger-run-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dbt-trigger-run-and-poll-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dbtlabs
- group: company
  title: ''
  type: Website
  url: https://www.getdbt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getdbt.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.getdbt.com/docs/dbt-cloud-apis/overview
- group: auth
  title: ''
  type: Authentication
  url: https://docs.getdbt.com/docs/dbt-cloud-apis/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getdbt.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dbt-labs/dbt-core
- group: build
  title: ''
  type: SDKs
  url: https://docs.getdbt.com/docs/dbt-cloud-apis/sl-python
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getdbt.com/cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getdbt.com/cloud/privacy-policy
- group: design
  href: https://artifacts.apis.io/dbt/json-ld/dbt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dbt-context.jsonld
- group: design
  href: https://artifacts.apis.io/dbt/vocabulary/dbt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dbt-vocabulary.yml
created: '2025-01-08'
description: dbt Labs operates dbt Cloud, the managed platform for the open-source dbt (data build tool) used to transform data inside cloud warehouses. dbt Cloud exposes a set of APIs for managing accounts, projects, jobs, and runs programmatically (Administrative API), inspecting project metadata (Discovery API), and querying governed metrics (Semantic Layer API).
finops:
- has_sources: true
  method: derived
  name: Dbt Finops
  primary_unit: user
  service_category: ''
  slug: dbt-finops
  template: false
graphqls:
- description: Every time dbt Cloud runs a project, it generates and stores information about the project. The Discovery API exposes that metadata including details about models, sources, exposures, and execution re
  name: dbt GraphQL API
  slug: dbt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dbt.png
json_schemas:
- name: dbt Cloud Job
  property_count: 12
  slug: dbt-job
- name: dbt Cloud Run
  property_count: 13
  slug: dbt-run
jsonld:
- class_count: 6
  name: Dbt Context
  property_count: 10
  slug: dbt-context
layout: provider
modified: '2026-10-06'
name: dbt
nav: Providers
network: true
overview: 'dbt publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Environments API, Jobs API, and 7 more. Tagged areas include Analytics Engineering, Data, ELT, Metrics, and Project.


  The dbt catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  dbt''s developer surface includes engineering blog, authentication, documentation, developer portal, pricing, GitHub presence, and 30 more developer resources.'
plans:
- name: Dbt Plans Pricing
  plan_count: 6
  slug: dbt-plans-pricing
- name: Dbt Price Estimates
  plan_count: 0
  slug: dbt-price-estimates
random_paper: 2
rate_limits:
- limit_count: 5
  name: Dbt Rate Limits
  slug: dbt-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: dbt — cloud administrative api rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dbt-cloud-administrative-api-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: dbt — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dbt-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 87.0
    catalog_earned_first_party: 12.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 78.9
    contract_governance: 27.3
    contract_quality: 56.6
    developer_ergonomics: 41.7
    discoverability: 71.4
    operational_transparency: 13.2
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 33.3
      total: 12
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dbt/dbt-2026-06-20T175739.png
security:
- kind: authentication
  name: Dbt Authentication
  slug: dbt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dbt Domain Security
  slug: dbt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dbt Trust Center
  slug: dbt-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: dbt
tags:
- Analytics Engineering
- Data
- ELT
- Metrics
- Project
- SQL
- Transformation
website: https://www.getdbt.com/
---
