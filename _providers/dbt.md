---
access_model:
  confidence: medium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
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
  description: The Metadata API from dbt — 1 operation(s) for metadata.
  name: dbt Metadata API
  slug: dbt-metadata-api
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
artifact_total: 47
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
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dbt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dbt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dbt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dbt-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dbt/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-account-project-job-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-bootstrap-account-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-create-job-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-create-run-poll-artifacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-environment-job-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-find-job-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-job-run-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-provision-job-in-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-rerun-latest-failed-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-run-and-fetch-artifacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-run-metadata-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dbt-run-to-semantic-metrics-workflow.yml
- group: design
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
  title: ''
  type: JSONLD
  url: json-ld/dbt-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dbt-vocabulary.yml
created: '2025-01-08'
description: dbt Labs operates dbt Cloud, the managed platform for the open-source dbt (data build tool) used to transform data inside cloud warehouses. dbt Cloud exposes a set of APIs for managing accounts, projects, jobs, and runs programmatically (Administrative API), inspecting project metadata (Discovery API), and querying governed metrics (Semantic Layer API).
finops:
- name: Dbt Finops
  service_category: API
  slug: dbt-finops
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
modified: '2026-05-19'
name: dbt
nav: Providers
network: true
overview: 'dbt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Environments API, Jobs API, and 4 more. Tagged areas include Analytics Engineering, Data, ELT, Metrics, and Project.


  The dbt catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  dbt''s developer surface includes authentication, documentation, developer portal, pricing, GitHub presence, and 25 more developer resources.'
plans:
- name: Dbt Plans Pricing
  plan_count: 3
  slug: dbt-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Dbt Rate Limits
  slug: dbt-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: dbt API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dbt-cloud-administrative-api-rules
- effective_rule_count: 5
  extends: []
  name: dbt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dbt-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 93.0
    catalog_earned_first_party: 0.0
    catalog_gap: 22.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 69.7
    contract_quality: 63.8
    developer_ergonomics: 39.3
    discoverability: 74.1
    governance: 69.7
    operational_transparency: 13.2
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/screenshots/dbt-2026-06-20T175739.png
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
