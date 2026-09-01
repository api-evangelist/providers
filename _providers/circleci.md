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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Circleci Agentic Access
  operation_count: 74
  slug: circleci-agentic-access
  summary_line: 74 operations · 30 acting
api_count: 2
apis:
- description: The CircleCI Self-Hosted Runner API enables management and execution of jobs on self-hosted runner infrastructure. It provides endpoints for listing available runners, managing runner tasks, and query
  name: CircleCI Self-Hosted Runner API
  slug: runner-api
- description: CircleCI Webhooks allow developers to receive real-time notifications about events in their CI/CD pipelines by configuring HTTP callbacks. Webhooks can be set up through project settings to notify ext
  name: CircleCI Webhooks
  slug: webhooks
- description: CircleCI Orbs are shareable, reusable packages of CircleCI configuration that simplify build setup and integration with third-party tools. The Orbs Registry on the CircleCI Developer Hub provides a se
  name: CircleCI Orbs Registry
  slug: orbs
- description: Endpoints for listing and downloading build artifacts.
  name: CircleCI Artifact API
  slug: circleci-artifact-api
- description: Endpoints for retrieving build details, triggering builds, retrying builds, and canceling builds.
  name: CircleCI Build API
  slug: circleci-build-api
- description: Endpoints for managing contexts, which are used to secure and share environment variables across projects.
  name: CircleCI Context API
  slug: circleci-context-api
- description: Endpoints for retrieving workflow and job metrics, summary data, and test performance insights.
  name: CircleCI Insights API
  slug: circleci-insights-api
- description: Endpoints for retrieving job details, artifacts, and test metadata associated with pipeline jobs.
  name: CircleCI Job API
  slug: circleci-job-api
- description: Endpoints for triggering, retrieving, and managing pipelines and their configurations.
  name: CircleCI Pipeline API
  slug: circleci-pipeline-api
- description: Endpoints for listing followed projects and managing project settings.
  name: CircleCI Project API
  slug: circleci-project-api
- description: Endpoints for managing runner resource classes, which define the compute resources available for self-hosted runner jobs.
  name: CircleCI Resource Class API
  slug: circleci-resource-class-api
- description: Endpoints for querying task counts and managing tasks assigned to self-hosted runners.
  name: CircleCI Runner Task API
  slug: circleci-runner-task-api
- description: Endpoints for creating, updating, and managing scheduled pipeline triggers.
  name: CircleCI Schedule API
  slug: circleci-schedule-api
- description: Endpoints for managing SSH keys and checkout keys for projects.
  name: CircleCI SSH Key API
  slug: circleci-ssh-key-api
- description: Endpoints for retrieving test metadata collected during builds.
  name: CircleCI Test Metadata API
  slug: circleci-test-metadata-api
- description: Endpoints for retrieving information about the authenticated user.
  name: CircleCI User API
  slug: circleci-user-api
- description: Endpoints for creating, updating, listing, and deleting outbound webhook subscriptions.
  name: CircleCI Webhook API
  slug: circleci-webhook-api
- description: Endpoints for retrieving workflow details, managing workflow status, and rerunning workflows.
  name: CircleCI Workflow API
  slug: circleci-workflow-api
artifact_total: 132
asyncapis:
- description: CircleCI Webhooks allow developers to receive real-time notifications about events in their CI/CD pipelines by configuring HTTP callbacks. Webhooks can be set up through project settings or the API to
  name: CircleCI Webhooks
  slug: circleci-webhooks-asyncapi
collections:
- collection_type: postman
  name: CircleCI REST API v1 Artifact API
  slug: postman-circleci-artifact-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Build API
  slug: postman-circleci-build-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Context API
  slug: postman-circleci-context-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Insights API
  slug: postman-circleci-insights-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Job API
  slug: postman-circleci-job-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Pipeline API
  slug: postman-circleci-pipeline-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Project API
  slug: postman-circleci-project-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Resource Class API
  slug: postman-circleci-resource-class-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Runner API
  slug: postman-circleci-runner-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Runner Task API
  slug: postman-circleci-runner-task-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Schedule API
  slug: postman-circleci-schedule-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact SSH Key API
  slug: postman-circleci-ssh-key-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Test Metadata API
  slug: postman-circleci-test-metadata-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact User API
  slug: postman-circleci-user-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Webhook API
  slug: postman-circleci-webhook-api
- collection_type: postman
  name: CircleCI REST API v1 Artifact Workflow API
  slug: postman-circleci-workflow-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CircleCI REST API v1 Artifact API
  slug: open-circleci-artifact-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Build API
  slug: open-circleci-build-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Context API
  slug: open-circleci-context-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Insights API
  slug: open-circleci-insights-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Job API
  slug: open-circleci-job-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Pipeline API
  slug: open-circleci-pipeline-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Project API
  slug: open-circleci-project-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Resource Class API
  slug: open-circleci-resource-class-api
- collection_type: open
  name: CircleCI REST API v1
  slug: open-circleci-rest-api-v1
- collection_type: open
  name: CircleCI REST API v2
  slug: open-circleci-rest-api-v2
- collection_type: open
  name: CircleCI REST API v1 Artifact Runner API
  slug: open-circleci-runner-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Runner Task API
  slug: open-circleci-runner-task-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Schedule API
  slug: open-circleci-schedule-api
- collection_type: open
  name: CircleCI REST API v1 Artifact SSH Key API
  slug: open-circleci-ssh-key-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Test Metadata API
  slug: open-circleci-test-metadata-api
- collection_type: open
  name: CircleCI REST API v1 Artifact User API
  slug: open-circleci-user-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Webhook API
  slug: open-circleci-webhook-api
- collection_type: open
  name: CircleCI REST API v1 Artifact Workflow API
  slug: open-circleci-workflow-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/circleci/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/circleci-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/circleci-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/circleci-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circleci-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circleci-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/circleci
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circleci
- group: company
  title: ''
  type: Website
  url: https://circleci.com/
- group: start
  title: ''
  type: Portal
  url: https://circleci.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://circleci.com/docs/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.circleci.com/
- group: operate
  title: ''
  type: Support
  url: https://support.circleci.com/
- group: company
  title: ''
  type: Blog
  url: https://circleci.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circleci.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circleci.com/terms-of-service/
- group: start
  title: ''
  type: Login
  url: https://app.circleci.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/circleci-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/circleci-pipeline-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/circleci-workflow-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/circleci-webhook-event-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/circleci-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://circleci.com/llms.txt
created: '2025-03-05'
description: CircleCI is a continuous integration and continuous delivery (CI/CD) platform that automates software build, test, and deployment pipelines. Their developer surface includes the REST API v2 (the recommended modern interface), the legacy v1 REST API, a Self-Hosted Runner API, webhooks for real-time event notifications, and the Orbs Registry of reusable configuration packages. Authentication is via a personal or project Circle-Token sent in the Circle-Token header; responses are JSON.
features:
- 'Free: 30K credits/mo, 6K build minutes, 5 active users'
- 'Performance from $15/mo: 30K credits + $15/25K credits, 80x concurrency'
- 'Scale: custom annual, 200 GB storage, GPU, SSO, config policies'
- REST API v2 at circleci.com/api/v2
- Default 3,000 req/min API rate limit
- Self-hosted runners (Linux, Windows, macOS, Arm)
- Docker layer caching (Performance+)
- Orbs marketplace for reusable config
- Webhooks for pipeline events
- OAuth 2.0 + personal API tokens
- Test splitting and parallel execution
- GPU executors (Scale)
- Insights API for build analytics
- OIDC token federation for cloud auth
- Config policies for governance (Scale)
- SOC 2, FedRAMP Moderate (Scale)
finops:
- name: Circleci Finops
  service_category: CI/CD
  slug: circleci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circleci.png
json_schemas:
- name: Artifact
  property_count: 4
  slug: circleci-artifact
- name: ArtifactList
  property_count: 2
  slug: circleci-artifactlist
- name: Build
  property_count: 19
  slug: circleci-build
- name: BuildDetail
  property_count: 0
  slug: circleci-builddetail
- name: BuildSummary
  property_count: 4
  slug: circleci-buildsummary
- name: CheckoutKey
  property_count: 6
  slug: circleci-checkoutkey
- name: CheckoutKeyList
  property_count: 2
  slug: circleci-checkoutkeylist
- name: Collaboration
  property_count: 5
  slug: circleci-collaboration
- name: Context
  property_count: 3
  slug: circleci-context
- name: ContextList
  property_count: 2
  slug: circleci-contextlist
- name: CreateContextRequest
  property_count: 2
  slug: circleci-createcontextrequest
- name: CreateScheduleRequest
  property_count: 5
  slug: circleci-createschedulerequest
- name: CreateWebhookRequest
  property_count: 6
  slug: circleci-createwebhookrequest
- name: EnvironmentVariable
  property_count: 4
  slug: circleci-environmentvariable
- name: EnvironmentVariableList
  property_count: 2
  slug: circleci-environmentvariablelist
- name: ErrorResponse
  property_count: 1
  slug: circleci-errorresponse
- name: InsightsJobMetrics
  property_count: 2
  slug: circleci-insightsjobmetrics
- name: InsightsTestMetrics
  property_count: 4
  slug: circleci-insightstestmetrics
- name: InsightsWorkflowMetrics
  property_count: 2
  slug: circleci-insightsworkflowmetrics
- name: InsightsWorkflowRuns
  property_count: 2
  slug: circleci-insightsworkflowruns
- name: Job
  property_count: 14
  slug: circleci-job
- name: MessageResponse
  property_count: 1
  slug: circleci-messageresponse
- name: CircleCI Pipeline
  property_count: 10
  slug: circleci-pipeline
- name: PipelineConfig
  property_count: 4
  slug: circleci-pipelineconfig
- name: PipelineCreation
  property_count: 4
  slug: circleci-pipelinecreation
- name: PipelineList
  property_count: 2
  slug: circleci-pipelinelist
- name: Project
  property_count: 5
  slug: circleci-project
- name: ProjectEnvVar
  property_count: 2
  slug: circleci-projectenvvar
- name: ProjectEnvVarList
  property_count: 2
  slug: circleci-projectenvvarlist
- name: RerunWorkflowResponse
  property_count: 1
  slug: circleci-rerunworkflowresponse
- name: ResourceClass
  property_count: 3
  slug: circleci-resourceclass
- name: ResourceClassCreation
  property_count: 4
  slug: circleci-resourceclasscreation
- name: Runner
  property_count: 10
  slug: circleci-runner
- name: Schedule
  property_count: 9
  slug: circleci-schedule
- name: ScheduleList
  property_count: 2
  slug: circleci-schedulelist
- name: TestList
  property_count: 2
  slug: circleci-testlist
- name: TestMetadata
  property_count: 7
  slug: circleci-testmetadata
- name: Timetable
  property_count: 5
  slug: circleci-timetable
- name: TriggerPipelineRequest
  property_count: 3
  slug: circleci-triggerpipelinerequest
- name: UpdateScheduleRequest
  property_count: 5
  slug: circleci-updateschedulerequest
- name: UpdateWebhookRequest
  property_count: 5
  slug: circleci-updatewebhookrequest
- name: User
  property_count: 9
  slug: circleci-user
- name: CircleCI Webhook Event
  property_count: 9
  slug: circleci-webhook-event
- name: WebhookInfo
  property_count: 9
  slug: circleci-webhookinfo
- name: WebhookList
  property_count: 2
  slug: circleci-webhooklist
- name: CircleCI Workflow
  property_count: 10
  slug: circleci-workflow
- name: WorkflowJob
  property_count: 8
  slug: circleci-workflowjob
- name: WorkflowJobList
  property_count: 2
  slug: circleci-workflowjoblist
- name: WorkflowList
  property_count: 2
  slug: circleci-workflowlist
json_structures:
- name: Circleci Structure
  property_count: 0
  slug: circleci-structure
jsonld:
- class_count: 0
  name: Circleci Context
  property_count: 10
  slug: circleci-context
layout: provider
modified: '2026-05-19'
name: CircleCI
nav: Providers
network: true
overview: 'CircleCI publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Self-Hosted Runner API, Webhooks, Artifact API, and 14 more. Tagged areas include CI/CD, Continuous Integration, Continuous Deployment, DevOps, and Pipelines.


  The CircleCI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CircleCI''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 18 more developer resources.'
plans:
- name: Circleci Plans Pricing
  plan_count: 3
  slug: circleci-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Circleci Rate Limits
  slug: circleci-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: CircleCI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: circleci-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: CircleCI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: circleci-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: CircleCI API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: circleci-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 13.6
    contract_quality: 70.1
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/screenshots/circleci-2026-06-20T174349.png
security:
- kind: authentication
  name: Circleci Authentication
  slug: circleci-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Circleci Domain Security
  slug: circleci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Circleci Vulnerability Disclosure
  slug: circleci-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Circleci Trust Center
  slug: circleci-trust-center
  summary_line: SOC 2, FedRAMP, GDPR, CSA STAR
slug: circleci
tags:
- CI/CD
- Continuous Integration
- Continuous Deployment
- DevOps
- Pipelines
- Workflows
website: https://circleci.com/
---
