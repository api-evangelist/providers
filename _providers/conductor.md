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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Conductor Agentic Access
  operation_count: 39
  slug: conductor-agentic-access
  summary_line: 39 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Administrative and health check APIs
  name: Conductor Admin API
  slug: conductor-admin-api
- description: APIs for managing event handlers
  name: Conductor Event API
  slug: conductor-event-api
- description: APIs for managing task definitions
  name: Conductor Metadata - Task API
  slug: conductor-metadata-task-api
- description: APIs for managing workflow definitions
  name: Conductor Metadata - Workflow API
  slug: conductor-metadata-workflow-api
- description: APIs for polling and updating tasks
  name: Conductor Task API
  slug: conductor-task-api
- description: APIs for managing workflow executions
  name: Conductor Workflow API
  slug: conductor-workflow-api
artifact_total: 89
asyncapis:
- description: 'Asynchronous event API for Conductor workflow orchestration platform. Conductor emits events when workflows and tasks change state, enabling reactive event-driven architectures. Event handlers can be '
  name: Conductor Events API
  slug: conductor-conductor-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Conductor Admin API
  slug: open-conductor-admin-api
- collection_type: open
  name: Conductor API
  slug: open-conductor-conductor
- collection_type: open
  name: Conductor Admin Event API
  slug: open-conductor-event-api
- collection_type: open
  name: Conductor Admin Metadata - Task API
  slug: open-conductor-metadata-task-api
- collection_type: open
  name: Conductor Admin Metadata - Workflow API
  slug: open-conductor-metadata-workflow-api
- collection_type: open
  name: Conductor Admin Task API
  slug: open-conductor-task-api
- collection_type: open
  name: Conductor Admin Workflow API
  slug: open-conductor-workflow-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/conductor-oss/conductor/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/conductor-oss/conductor/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/conductor-oss/conductor/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/conductor-oss/conductor/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/conductor-oss/conductor/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/conductor-oss/conductor/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conductor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conductor-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conductor-inc-
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/conductor-oss/conductor
- group: design
  title: ''
  type: SpectralRules
  url: rules/conductor-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/conductor-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://orkes.io/blog/
created: '2025-01-08'
description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps track of the state, calls tasks in the right order (sequentially or in parallel, as defined by you), retry calls if needed, handle failure scenarios gracefully, and outputs the final result.
examples:
- key_count: 5
  name: Conductor Conductor Event Handler Action Example
  slug: conductor-conductor-event-handler-action-example
- key_count: 6
  name: Conductor Conductor Event Handler Example
  slug: conductor-conductor-event-handler-example
- key_count: 2
  name: Conductor Conductor Search Result Task Summary Example
  slug: conductor-conductor-search-result-task-summary-example
- key_count: 2
  name: Conductor Conductor Search Result Workflow Summary Example
  slug: conductor-conductor-search-result-workflow-summary-example
- key_count: 2
  name: Conductor Conductor Skip Task Request Example
  slug: conductor-conductor-skip-task-request-example
- key_count: 7
  name: Conductor Conductor Start Workflow Request Example
  slug: conductor-conductor-start-workflow-request-example
- key_count: 20
  name: Conductor Conductor Task Def Example
  slug: conductor-conductor-task-def-example
- key_count: 24
  name: Conductor Conductor Task Example
  slug: conductor-conductor-task-example
- key_count: 3
  name: Conductor Conductor Task Exec Log Example
  slug: conductor-conductor-task-exec-log-example
- key_count: 9
  name: Conductor Conductor Task Result Example
  slug: conductor-conductor-task-result-example
- key_count: 16
  name: Conductor Conductor Task Summary Example
  slug: conductor-conductor-task-summary-example
- key_count: 15
  name: Conductor Conductor Workflow Def Example
  slug: conductor-conductor-workflow-def-example
- key_count: 20
  name: Conductor Conductor Workflow Example
  slug: conductor-conductor-workflow-example
- key_count: 15
  name: Conductor Conductor Workflow Summary Example
  slug: conductor-conductor-workflow-summary-example
- key_count: 17
  name: Conductor Conductor Workflow Task Example
  slug: conductor-conductor-workflow-task-example
features:
- description: Define and execute complex workflows with sequential and parallel task execution.
  name: Workflow Orchestration
- description: Register, poll, and update granular task definitions with timeout and retry policies.
  name: Task Management
- description: Create event handlers to trigger workflows or tasks based on external events.
  name: Event Handling
- description: Search and filter workflow executions by status, type, and custom parameters.
  name: Workflow Search
- description: Automatic retries, pause/resume, and graceful failure handling for long-running workflows.
  name: Fault Tolerance
- description: Pause, resume, restart, retry, and terminate workflows programmatically.
  name: Workflow Lifecycle Control
finops:
- name: Conductor Finops
  service_category: API
  slug: conductor-finops
graphqls:
- description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps tra
  name: Conductor GraphQL API
  slug: conductor-graphql
image: /assets/icons/conductor.png
integrations:
- description: Trigger workflows and tasks from Kafka events using event handler subscriptions.
  name: Apache Kafka
- description: Integrate with SQS for message-driven workflow initiation and task completion.
  name: Amazon SQS
- description: Run Conductor server and workers in containerized environments for scalable deployment.
  name: Docker
- description: Use managed Conductor service from Orkes for enterprise-grade orchestration without infrastructure management.
  name: Orkes Cloud
json_schemas:
- name: EventHandlerAction
  property_count: 5
  slug: conductor-conductor-event-handler-action
- name: EventHandler
  property_count: 6
  slug: conductor-conductor-event-handler
- name: SearchResultTaskSummary
  property_count: 2
  slug: conductor-conductor-search-result-task-summary
- name: SearchResultWorkflowSummary
  property_count: 2
  slug: conductor-conductor-search-result-workflow-summary
- name: SkipTaskRequest
  property_count: 2
  slug: conductor-conductor-skip-task-request
- name: StartWorkflowRequest
  property_count: 7
  slug: conductor-conductor-start-workflow-request
- name: TaskDef
  property_count: 20
  slug: conductor-conductor-task-def
- name: TaskExecLog
  property_count: 3
  slug: conductor-conductor-task-exec-log
- name: TaskResult
  property_count: 9
  slug: conductor-conductor-task-result
- name: Task
  property_count: 24
  slug: conductor-conductor-task
- name: TaskSummary
  property_count: 16
  slug: conductor-conductor-task-summary
- name: WorkflowDef
  property_count: 15
  slug: conductor-conductor-workflow-def
- name: Workflow
  property_count: 20
  slug: conductor-conductor-workflow
- name: WorkflowSummary
  property_count: 15
  slug: conductor-conductor-workflow-summary
- name: WorkflowTask
  property_count: 17
  slug: conductor-conductor-workflow-task
- name: EventHandler
  property_count: 6
  slug: event-handler
- name: TaskDef
  property_count: 20
  slug: task-def
- name: WorkflowDef
  property_count: 15
  slug: workflow-def
- name: WorkflowExecution
  property_count: 21
  slug: workflow-execution
json_structures:
- name: Conductor Conductor Event Handler Action Structure
  property_count: 5
  slug: conductor-conductor-event-handler-action-structure
- name: Conductor Conductor Event Handler Structure
  property_count: 6
  slug: conductor-conductor-event-handler-structure
- name: Conductor Conductor Search Result Task Summary Structure
  property_count: 2
  slug: conductor-conductor-search-result-task-summary-structure
- name: Conductor Conductor Search Result Workflow Summary Structure
  property_count: 2
  slug: conductor-conductor-search-result-workflow-summary-structure
- name: Conductor Conductor Skip Task Request Structure
  property_count: 2
  slug: conductor-conductor-skip-task-request-structure
- name: Conductor Conductor Start Workflow Request Structure
  property_count: 7
  slug: conductor-conductor-start-workflow-request-structure
- name: Conductor Conductor Task Def Structure
  property_count: 20
  slug: conductor-conductor-task-def-structure
- name: Conductor Conductor Task Exec Log Structure
  property_count: 3
  slug: conductor-conductor-task-exec-log-structure
- name: Conductor Conductor Task Result Structure
  property_count: 9
  slug: conductor-conductor-task-result-structure
- name: Conductor Conductor Task Structure
  property_count: 24
  slug: conductor-conductor-task-structure
- name: Conductor Conductor Task Summary Structure
  property_count: 16
  slug: conductor-conductor-task-summary-structure
- name: Conductor Conductor Workflow Def Structure
  property_count: 15
  slug: conductor-conductor-workflow-def-structure
- name: Conductor Conductor Workflow Structure
  property_count: 20
  slug: conductor-conductor-workflow-structure
- name: Conductor Conductor Workflow Summary Structure
  property_count: 15
  slug: conductor-conductor-workflow-summary-structure
- name: Conductor Conductor Workflow Task Structure
  property_count: 17
  slug: conductor-conductor-workflow-task-structure
jsonld:
- class_count: 0
  name: Conductor Conductor Context
  property_count: 0
  slug: conductor-conductor-context
- class_count: 7
  name: Conductor Context
  property_count: 40
  slug: conductor-context
layout: provider
modified: '2026-05-19'
name: Conductor
nav: Providers
network: true
overview: 'Conductor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Event API, Metadata - Task API, and 3 more. Tagged areas include Automation, Orchestration, States, Task, and Workflows.


  The Conductor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Conductor''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Conductor Plans Pricing
  plan_count: 3
  slug: conductor-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Conductor Rate Limits
  slug: conductor-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Conductor API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 2
  slug: conductor-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Conductor API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: conductor-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Conductor API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 4
  slug: conductor-spectral-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 78.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/conductor/refs/heads/main/screenshots/conductor-2026-06-20T174854.png
security:
- kind: domain-security
  name: Conductor Domain Security
  slug: conductor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conductor
tags:
- Automation
- Orchestration
- States
- Task
- Workflows
use_cases:
- description: Coordinate complex business processes across distributed microservices without tight coupling.
  name: Microservices Orchestration
- description: Build and manage ETL and data processing pipelines with dependency tracking and error recovery.
  name: Data Pipeline Automation
- description: Manage multi-step order fulfillment workflows including payment, inventory, and shipping.
  name: Order Processing
- description: Orchestrate build, test, and deployment workflows with conditional logic and parallel execution.
  name: CI/CD Pipelines
---
