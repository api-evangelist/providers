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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Apache Airflow Agentic Access
  operation_count: 73
  slug: apache-airflow-agentic-access
  summary_line: 73 operations · 32 acting
api_count: 19
apis:
- description: The experimental API that preceded the stable REST API. This is deprecated and should not be used for new implementations.
  name: Apache Airflow Experimental API (Deprecated)
  slug: apache-airflow-experimental-api
- description: The Config API from Apache Airflow — 1 operation(s) for config.
  name: Apache Airflow Config API
  slug: apache-airflow-config-api
- description: The Connection API from Apache Airflow — 3 operation(s) for connection.
  name: Apache Airflow Connection API
  slug: apache-airflow-connection-api
- description: The DAG API from Apache Airflow — 8 operation(s) for dag.
  name: Apache Airflow DAG API
  slug: apache-airflow-dag-api
- description: The DAGRun API from Apache Airflow — 6 operation(s) for dagrun.
  name: Apache Airflow DAGRun API
  slug: apache-airflow-dagrun-api
- description: The DagWarning API from Apache Airflow — 1 operation(s) for dagwarning.
  name: Apache Airflow DagWarning API
  slug: apache-airflow-dagwarning-api
- description: The Dataset API from Apache Airflow — 4 operation(s) for dataset.
  name: Apache Airflow Dataset API
  slug: apache-airflow-dataset-api
- description: The EventLog API from Apache Airflow — 2 operation(s) for eventlog.
  name: Apache Airflow EventLog API
  slug: apache-airflow-eventlog-api
- description: The ImportError API from Apache Airflow — 2 operation(s) for importerror.
  name: Apache Airflow ImportError API
  slug: apache-airflow-importerror-api
- description: The Monitoring API from Apache Airflow — 2 operation(s) for monitoring.
  name: Apache Airflow Monitoring API
  slug: apache-airflow-monitoring-api
- description: The Permission API from Apache Airflow — 1 operation(s) for permission.
  name: Apache Airflow Permission API
  slug: apache-airflow-permission-api
- description: The Plugin API from Apache Airflow — 1 operation(s) for plugin.
  name: Apache Airflow Plugin API
  slug: apache-airflow-plugin-api
- description: The Pool API from Apache Airflow — 2 operation(s) for pool.
  name: Apache Airflow Pool API
  slug: apache-airflow-pool-api
- description: The Provider API from Apache Airflow — 1 operation(s) for provider.
  name: Apache Airflow Provider API
  slug: apache-airflow-provider-api
- description: The Role API from Apache Airflow — 2 operation(s) for role.
  name: Apache Airflow Role API
  slug: apache-airflow-role-api
- description: The TaskInstance API from Apache Airflow — 9 operation(s) for taskinstance.
  name: Apache Airflow TaskInstance API
  slug: apache-airflow-taskinstance-api
- description: The User API from Apache Airflow — 2 operation(s) for user.
  name: Apache Airflow User API
  slug: apache-airflow-user-api
- description: The Variable API from Apache Airflow — 2 operation(s) for variable.
  name: Apache Airflow Variable API
  slug: apache-airflow-variable-api
- description: The XCom API from Apache Airflow — 2 operation(s) for xcom.
  name: Apache Airflow XCom API
  slug: apache-airflow-xcom-api
arazzos:
- description: Use the batch endpoints to pull failed runs and their task instances across many DAGs in a date window, then check the event log for who intervened.
  name: Apache Airflow Audit DAG Runs Across the Fleet
  slug: apache-airflow-audit-dag-runs-workflow
- description: Wait for a DAG run to finish, find the producing task instance, and pull its XCom return value.
  name: Apache Airflow Collect DAG Run Results from XCom
  slug: apache-airflow-collect-dag-run-results-workflow
- description: Find a dataset by URI, read the tasks that produce it and the DAGs that consume it, and trace the events that triggered a downstream run.
  name: Apache Airflow Trace Dataset-Driven Lineage
  slug: apache-airflow-dataset-lineage-workflow
- description: Verify scheduler and metadatabase health, capture the version, and surface DAG import errors and warnings before trusting a deployment.
  name: Apache Airflow Deployment Preflight Check
  slug: apache-airflow-deployment-preflight-workflow
- description: Isolate the failed task in a DAG run, pull its logs for the last attempt, and record the diagnosis as a note.
  name: Apache Airflow Diagnose a Failed DAG Run
  slug: apache-airflow-diagnose-failed-dag-run-workflow
- description: Preview and then set a task instance's state to unblock a stuck pipeline, verifying the DAG run recovers.
  name: Apache Airflow Force a Task Instance State
  slug: apache-airflow-force-task-instance-state-workflow
- description: Orient on an unfamiliar DAG by reading its metadata, schedule details, task graph, source code, and recent run history.
  name: Apache Airflow Onboard a DAG
  slug: apache-airflow-onboard-dag-workflow
- description: Ensure a role exists with the intended permissions, create a user bound to it, and verify the assignment.
  name: Apache Airflow Provision a User with a Role
  slug: apache-airflow-provision-user-workflow
- description: Test a connection's credentials against the target system before saving it, then create and verify the stored connection.
  name: Apache Airflow Register a Connection After Testing It
  slug: apache-airflow-register-connection-workflow
- description: Preview which task instances a clear would touch, clear the failed ones for real, and wait for the re-run to settle.
  name: Apache Airflow Retry Failed Tasks in a DAG Run
  slug: apache-airflow-retry-failed-tasks-workflow
- description: Unpause a DAG if needed, trigger a run with a configuration payload, and poll until the run reaches a terminal state.
  name: Apache Airflow Trigger a DAG Run and Wait for Completion
  slug: apache-airflow-trigger-dag-run-workflow
- description: Create or resize an Airflow pool by name, then read back its slot accounting.
  name: Apache Airflow Upsert a Slot Pool
  slug: apache-airflow-upsert-pool-workflow
- description: Look up an Airflow variable and update it if it exists, otherwise create it, then read the result back.
  name: Apache Airflow Upsert a Variable
  slug: apache-airflow-upsert-variable-workflow
artifact_total: 283
collections:
- collection_type: postman
  name: Airflow API (Stable) Config API
  slug: postman-apache-airflow-config-api
- collection_type: postman
  name: Airflow API (Stable) Config Connection API
  slug: postman-apache-airflow-connection-api
- collection_type: postman
  name: Airflow API (Stable) Config DAG API
  slug: postman-apache-airflow-dag-api
- collection_type: postman
  name: Airflow API (Stable) Config DAGRun API
  slug: postman-apache-airflow-dagrun-api
- collection_type: postman
  name: Airflow API (Stable) Config DagWarning API
  slug: postman-apache-airflow-dagwarning-api
- collection_type: postman
  name: Airflow API (Stable) Config Dataset API
  slug: postman-apache-airflow-dataset-api
- collection_type: postman
  name: Airflow API (Stable) Config EventLog API
  slug: postman-apache-airflow-eventlog-api
- collection_type: postman
  name: Airflow API (Stable) Config ImportError API
  slug: postman-apache-airflow-importerror-api
- collection_type: postman
  name: Airflow API (Stable) Config Monitoring API
  slug: postman-apache-airflow-monitoring-api
- collection_type: postman
  name: Airflow API (Stable) Config Permission API
  slug: postman-apache-airflow-permission-api
- collection_type: postman
  name: Airflow API (Stable) Config Plugin API
  slug: postman-apache-airflow-plugin-api
- collection_type: postman
  name: Airflow API (Stable) Config Pool API
  slug: postman-apache-airflow-pool-api
- collection_type: postman
  name: Airflow API (Stable) Config Provider API
  slug: postman-apache-airflow-provider-api
- collection_type: postman
  name: Airflow API (Stable) Config Role API
  slug: postman-apache-airflow-role-api
- collection_type: postman
  name: Airflow API (Stable) Config TaskInstance API
  slug: postman-apache-airflow-taskinstance-api
- collection_type: postman
  name: Airflow API (Stable) Config User API
  slug: postman-apache-airflow-user-api
- collection_type: postman
  name: Airflow API (Stable) Config Variable API
  slug: postman-apache-airflow-variable-api
- collection_type: postman
  name: Airflow API (Stable) Config XCom API
  slug: postman-apache-airflow-xcom-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-airflow/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-airflow-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/apache-airflow-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apache-airflow-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/apache-airflow-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apache-airflow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apache-airflow-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/apache-airflow-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apache-airflow-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apache-airflow-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apache-airflow-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/apache-airflow-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apache-airflow-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-airflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-airflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-airflow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-airflow
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/airflow
- group: docs
  title: ''
  type: Documentation
  url: https://airflow.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://airflow.apache.org/docs/apache-airflow/stable/start.html
- group: learn
  title: ''
  type: Tutorials
  url: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html
- group: build
  title: Python Package (PyPI)
  type: SDKs
  url: https://pypi.org/project/apache-airflow/
- group: build
  title: Docker Image
  type: SDKs
  url: https://hub.docker.com/r/apache/airflow
- group: auth
  title: ''
  type: Security
  url: https://airflow.apache.org/docs/apache-airflow/stable/security/
- group: company
  title: ''
  type: Blog
  url: https://airflow.apache.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://airflow.apache.org/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-airflow-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-airflow-vocabulary.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-trigger-dag-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-collect-dag-run-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-diagnose-failed-dag-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-retry-failed-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-force-task-instance-state-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-upsert-variable-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-register-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-upsert-pool-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-onboard-dag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-deployment-preflight-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-audit-dag-runs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-dataset-lineage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apache-airflow-provision-user-workflow.yml
created: '2024-01-15'
description: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows, developed by the Apache Software Foundation. It allows you to define workflows as Directed Acyclic Graphs (DAGs) in Python code, making them maintainable, versionable, testable, and collaborative. Airflow provides a stable REST API for managing DAGs, DAG runs, tasks, connections, variables, pools, and users, along with a web-based UI for monitoring and managing pipeline execution.
examples:
- key_count: 0
  name: Openapi.Yaml Action Collection Example
  slug: openapi.yaml-action-collection-example
- key_count: 1
  name: Openapi.Yaml Action Example
  slug: openapi.yaml-action-example
- key_count: 2
  name: Openapi.Yaml Action Resource Example
  slug: openapi.yaml-action-resource-example
- key_count: 8
  name: Openapi.Yaml Basic Dag Run Example
  slug: openapi.yaml-basic-dag-run-example
- key_count: 2
  name: Openapi.Yaml Class Reference Example
  slug: openapi.yaml-class-reference-example
- key_count: 1
  name: Openapi.Yaml Clear Dag Run Example
  slug: openapi.yaml-clear-dag-run-example
- key_count: 10
  name: Openapi.Yaml Clear Task Instances Example
  slug: openapi.yaml-clear-task-instances-example
- key_count: 1
  name: Openapi.Yaml Collection Info Example
  slug: openapi.yaml-collection-info-example
- key_count: 0
  name: Openapi.Yaml Color Example
  slug: openapi.yaml-color-example
- key_count: 1
  name: Openapi.Yaml Config Example
  slug: openapi.yaml-config-example
- key_count: 2
  name: Openapi.Yaml Config Option Example
  slug: openapi.yaml-config-option-example
- key_count: 2
  name: Openapi.Yaml Config Section Example
  slug: openapi.yaml-config-section-example
- key_count: 0
  name: Openapi.Yaml Connection Collection Example
  slug: openapi.yaml-connection-collection-example
- key_count: 7
  name: Openapi.Yaml Connection Collection Item Example
  slug: openapi.yaml-connection-collection-item-example
- key_count: 0
  name: Openapi.Yaml Connection Example
  slug: openapi.yaml-connection-example
- key_count: 2
  name: Openapi.Yaml Connection Test Example
  slug: openapi.yaml-connection-test-example
- key_count: 2
  name: Openapi.Yaml Cron Expression Example
  slug: openapi.yaml-cron-expression-example
- key_count: 0
  name: Openapi.Yaml Dag Collection Example
  slug: openapi.yaml-dag-collection-example
- key_count: 0
  name: Openapi.Yaml Dag Detail Example
  slug: openapi.yaml-dag-detail-example
- key_count: 10
  name: Openapi.Yaml Dag Example
  slug: openapi.yaml-dag-example
- key_count: 0
  name: Openapi.Yaml Dag Run Collection Example
  slug: openapi.yaml-dag-run-collection-example
- key_count: 10
  name: Openapi.Yaml Dag Run Example
  slug: openapi.yaml-dag-run-example
- key_count: 3
  name: Openapi.Yaml Dag Schedule Dataset Reference Example
  slug: openapi.yaml-dag-schedule-dataset-reference-example
- key_count: 0
  name: Openapi.Yaml Dag State Example
  slug: openapi.yaml-dag-state-example
- key_count: 0
  name: Openapi.Yaml Dag Warning Collection Example
  slug: openapi.yaml-dag-warning-collection-example
- key_count: 4
  name: Openapi.Yaml Dag Warning Example
  slug: openapi.yaml-dag-warning-example
- key_count: 0
  name: Openapi.Yaml Dataset Collection Example
  slug: openapi.yaml-dataset-collection-example
- key_count: 0
  name: Openapi.Yaml Dataset Event Collection Example
  slug: openapi.yaml-dataset-event-collection-example
- key_count: 9
  name: Openapi.Yaml Dataset Event Example
  slug: openapi.yaml-dataset-event-example
- key_count: 7
  name: Openapi.Yaml Dataset Example
  slug: openapi.yaml-dataset-example
features:
- description: Define workflows as Python code (Directed Acyclic Graphs) for version control, testing, and collaboration.
  name: DAG-as-Code
- description: Full-featured REST API for programmatic management of DAGs, runs, tasks, connections, variables, pools, and users.
  name: Stable REST API
- description: Generate DAGs dynamically using Python, supporting complex conditional and parametric pipelines.
  name: Dynamic Pipeline Generation
- description: Rich ecosystem of provider packages for integrating with AWS, GCP, Azure, databases, and hundreds of external services.
  name: Extensible Providers
- description: Browser-based dashboard for monitoring DAG runs, task statuses, logs, and Gantt charts.
  name: Rich Web UI
- description: Control concurrency and resource allocation across tasks using configurable pools.
  name: Resource Pools
- description: Define dependencies between DAGs using sensors, dataset-driven scheduling, and external task sensors.
  name: Cross-DAG Dependencies
- description: Supports Sequential, Local, Celery, Kubernetes, and DASK executors for flexible deployment.
  name: Pluggable Executors
- description: Define and track Service Level Agreements on task and DAG completion times.
  name: SLA Monitoring
- description: Centrally manage environment-specific configuration via Airflow variables and connections.
  name: Variable and Connection Management
finops:
- name: Apache Airflow Finops
  service_category: API
  slug: apache-airflow-finops
image: https://airflow.apache.org/images/feature-image.png
integrations:
- description: Native Spark submit and Livy operator integration for distributed data processing.
  name: Apache Spark
- description: Comprehensive GCP provider for BigQuery, Cloud Storage, Dataflow, Dataproc, and more.
  name: Google Cloud
- description: AWS provider for S3, Redshift, EMR, Glue, Lambda, and other services.
  name: Amazon Web Services
- description: Azure provider for Blob Storage, Data Factory, HDInsight, and Databricks.
  name: Microsoft Azure
- description: dbt operator for running dbt transformations within Airflow pipelines.
  name: dbt
- description: KubernetesPodOperator for running tasks in isolated Kubernetes pods.
  name: Kubernetes
- description: DockerOperator for running tasks in Docker containers with isolated environments.
  name: Docker
- description: Kafka producers and consumers as Airflow tasks via the Kafka provider.
  name: Apache Kafka
json_schemas:
- name: ActionCollection
  property_count: 0
  slug: openapi.yaml-action-collection
- name: ActionResource
  property_count: 2
  slug: openapi.yaml-action-resource
- name: Action
  property_count: 1
  slug: openapi.yaml-action
- name: BasicDAGRun
  property_count: 8
  slug: openapi.yaml-basic-dag-run
- name: ClassReference
  property_count: 2
  slug: openapi.yaml-class-reference
- name: ClearDagRun
  property_count: 1
  slug: openapi.yaml-clear-dag-run
- name: ClearTaskInstances
  property_count: 14
  slug: openapi.yaml-clear-task-instances
- name: CollectionInfo
  property_count: 1
  slug: openapi.yaml-collection-info
- name: Color
  property_count: 0
  slug: openapi.yaml-color
- name: ConfigOption
  property_count: 2
  slug: openapi.yaml-config-option
- name: Config
  property_count: 1
  slug: openapi.yaml-config
- name: ConfigSection
  property_count: 2
  slug: openapi.yaml-config-section
- name: ConnectionCollectionItem
  property_count: 7
  slug: openapi.yaml-connection-collection-item
- name: ConnectionCollection
  property_count: 0
  slug: openapi.yaml-connection-collection
- name: Connection
  property_count: 0
  slug: openapi.yaml-connection
- name: ConnectionTest
  property_count: 2
  slug: openapi.yaml-connection-test
- name: CronExpression
  property_count: 2
  slug: openapi.yaml-cron-expression
- name: DAGCollection
  property_count: 0
  slug: openapi.yaml-dag-collection
- name: DAGDetail
  property_count: 0
  slug: openapi.yaml-dag-detail
- name: DAGRunCollection
  property_count: 0
  slug: openapi.yaml-dag-run-collection
- name: DAGRun
  property_count: 14
  slug: openapi.yaml-dag-run
- name: DagScheduleDatasetReference
  property_count: 3
  slug: openapi.yaml-dag-schedule-dataset-reference
- name: DAG
  property_count: 26
  slug: openapi.yaml-dag
- name: DagState
  property_count: 0
  slug: openapi.yaml-dag-state
- name: DagWarningCollection
  property_count: 0
  slug: openapi.yaml-dag-warning-collection
- name: DagWarning
  property_count: 4
  slug: openapi.yaml-dag-warning
- name: DatasetCollection
  property_count: 0
  slug: openapi.yaml-dataset-collection
- name: DatasetEventCollection
  property_count: 0
  slug: openapi.yaml-dataset-event-collection
- name: DatasetEvent
  property_count: 9
  slug: openapi.yaml-dataset-event
- name: Dataset
  property_count: 7
  slug: openapi.yaml-dataset
- name: EventLogCollection
  property_count: 0
  slug: openapi.yaml-event-log-collection
- name: EventLog
  property_count: 8
  slug: openapi.yaml-event-log
- name: ExtraLinkCollection
  property_count: 1
  slug: openapi.yaml-extra-link-collection
- name: ExtraLink
  property_count: 3
  slug: openapi.yaml-extra-link
- name: HealthInfo
  property_count: 2
  slug: openapi.yaml-health-info
- name: HealthStatus
  property_count: 0
  slug: openapi.yaml-health-status
- name: ImportErrorCollection
  property_count: 0
  slug: openapi.yaml-import-error-collection
- name: ImportError
  property_count: 4
  slug: openapi.yaml-import-error
- name: Job
  property_count: 10
  slug: openapi.yaml-job
- name: ListDagRunsForm
  property_count: 11
  slug: openapi.yaml-list-dag-runs-form
- name: ListTaskInstanceForm
  property_count: 12
  slug: openapi.yaml-list-task-instance-form
- name: MetadatabaseStatus
  property_count: 1
  slug: openapi.yaml-metadatabase-status
- name: PluginCollectionItem
  property_count: 10
  slug: openapi.yaml-plugin-collection-item
- name: PluginCollection
  property_count: 0
  slug: openapi.yaml-plugin-collection
- name: PoolCollection
  property_count: 0
  slug: openapi.yaml-pool-collection
- name: Pool
  property_count: 7
  slug: openapi.yaml-pool
- name: ProviderCollection
  property_count: 1
  slug: openapi.yaml-provider-collection
- name: Provider
  property_count: 3
  slug: openapi.yaml-provider
- name: RelativeDelta
  property_count: 16
  slug: openapi.yaml-relative-delta
- name: Resource
  property_count: 1
  slug: openapi.yaml-resource
- name: RoleCollection
  property_count: 0
  slug: openapi.yaml-role-collection
- name: Role
  property_count: 2
  slug: openapi.yaml-role
- name: ScheduleInterval
  property_count: 0
  slug: openapi.yaml-schedule-interval
- name: SchedulerStatus
  property_count: 2
  slug: openapi.yaml-scheduler-status
- name: SetDagRunNote
  property_count: 1
  slug: openapi.yaml-set-dag-run-note
- name: SetTaskInstanceNote
  property_count: 1
  slug: openapi.yaml-set-task-instance-note
- name: SLAMiss
  property_count: 7
  slug: openapi.yaml-sla-miss
- name: Tag
  property_count: 1
  slug: openapi.yaml-tag
- name: TaskCollection
  property_count: 1
  slug: openapi.yaml-task-collection
- name: TaskInstanceCollection
  property_count: 0
  slug: openapi.yaml-task-instance-collection
- name: TaskInstanceReferenceCollection
  property_count: 1
  slug: openapi.yaml-task-instance-reference-collection
- name: TaskInstanceReference
  property_count: 4
  slug: openapi.yaml-task-instance-reference
- name: TaskInstance
  property_count: 26
  slug: openapi.yaml-task-instance
- name: TaskOutletDatasetReference
  property_count: 4
  slug: openapi.yaml-task-outlet-dataset-reference
- name: Task
  property_count: 24
  slug: openapi.yaml-task
- name: TaskState
  property_count: 0
  slug: openapi.yaml-task-state
- name: TimeDelta
  property_count: 4
  slug: openapi.yaml-time-delta
- name: Timezone
  property_count: 0
  slug: openapi.yaml-timezone
- name: TriggerRule
  property_count: 0
  slug: openapi.yaml-trigger-rule
- name: Trigger
  property_count: 5
  slug: openapi.yaml-trigger
- name: UpdateDagRunState
  property_count: 1
  slug: openapi.yaml-update-dag-run-state
- name: UpdateTaskInstance
  property_count: 2
  slug: openapi.yaml-update-task-instance
- name: UpdateTaskInstancesState
  property_count: 9
  slug: openapi.yaml-update-task-instances-state
- name: UserCollectionItem
  property_count: 11
  slug: openapi.yaml-user-collection-item
- name: UserCollection
  property_count: 0
  slug: openapi.yaml-user-collection
- name: User
  property_count: 0
  slug: openapi.yaml-user
- name: VariableCollectionItem
  property_count: 2
  slug: openapi.yaml-variable-collection-item
- name: VariableCollection
  property_count: 0
  slug: openapi.yaml-variable-collection
- name: Variable
  property_count: 0
  slug: openapi.yaml-variable
- name: VersionInfo
  property_count: 2
  slug: openapi.yaml-version-info
- name: WeightRule
  property_count: 0
  slug: openapi.yaml-weight-rule
- name: XComCollectionItem
  property_count: 5
  slug: openapi.yaml-x-com-collection-item
- name: XComCollection
  property_count: 0
  slug: openapi.yaml-x-com-collection
- name: XCom
  property_count: 0
  slug: openapi.yaml-x-com
json_structures:
- name: Openapi.Yaml Action Collection Structure
  property_count: 0
  slug: openapi.yaml-action-collection-structure
- name: Openapi.Yaml Action Resource Structure
  property_count: 2
  slug: openapi.yaml-action-resource-structure
- name: Openapi.Yaml Action Structure
  property_count: 1
  slug: openapi.yaml-action-structure
- name: Openapi.Yaml Basic Dag Run Structure
  property_count: 8
  slug: openapi.yaml-basic-dag-run-structure
- name: Openapi.Yaml Class Reference Structure
  property_count: 2
  slug: openapi.yaml-class-reference-structure
- name: Openapi.Yaml Clear Dag Run Structure
  property_count: 1
  slug: openapi.yaml-clear-dag-run-structure
- name: Openapi.Yaml Clear Task Instances Structure
  property_count: 14
  slug: openapi.yaml-clear-task-instances-structure
- name: Openapi.Yaml Collection Info Structure
  property_count: 1
  slug: openapi.yaml-collection-info-structure
- name: Openapi.Yaml Color Structure
  property_count: 0
  slug: openapi.yaml-color-structure
- name: Openapi.Yaml Config Option Structure
  property_count: 2
  slug: openapi.yaml-config-option-structure
- name: Openapi.Yaml Config Section Structure
  property_count: 2
  slug: openapi.yaml-config-section-structure
- name: Openapi.Yaml Config Structure
  property_count: 1
  slug: openapi.yaml-config-structure
- name: Openapi.Yaml Connection Collection Item Structure
  property_count: 7
  slug: openapi.yaml-connection-collection-item-structure
- name: Openapi.Yaml Connection Collection Structure
  property_count: 0
  slug: openapi.yaml-connection-collection-structure
- name: Openapi.Yaml Connection Structure
  property_count: 0
  slug: openapi.yaml-connection-structure
- name: Openapi.Yaml Connection Test Structure
  property_count: 2
  slug: openapi.yaml-connection-test-structure
- name: Openapi.Yaml Cron Expression Structure
  property_count: 2
  slug: openapi.yaml-cron-expression-structure
- name: Openapi.Yaml Dag Collection Structure
  property_count: 0
  slug: openapi.yaml-dag-collection-structure
- name: Openapi.Yaml Dag Detail Structure
  property_count: 0
  slug: openapi.yaml-dag-detail-structure
- name: Openapi.Yaml Dag Run Collection Structure
  property_count: 0
  slug: openapi.yaml-dag-run-collection-structure
- name: Openapi.Yaml Dag Run Structure
  property_count: 14
  slug: openapi.yaml-dag-run-structure
- name: Openapi.Yaml Dag Schedule Dataset Reference Structure
  property_count: 3
  slug: openapi.yaml-dag-schedule-dataset-reference-structure
- name: Openapi.Yaml Dag State Structure
  property_count: 0
  slug: openapi.yaml-dag-state-structure
- name: Openapi.Yaml Dag Structure
  property_count: 26
  slug: openapi.yaml-dag-structure
- name: Openapi.Yaml Dag Warning Collection Structure
  property_count: 0
  slug: openapi.yaml-dag-warning-collection-structure
- name: Openapi.Yaml Dag Warning Structure
  property_count: 4
  slug: openapi.yaml-dag-warning-structure
- name: Openapi.Yaml Dataset Collection Structure
  property_count: 0
  slug: openapi.yaml-dataset-collection-structure
- name: Openapi.Yaml Dataset Event Collection Structure
  property_count: 0
  slug: openapi.yaml-dataset-event-collection-structure
- name: Openapi.Yaml Dataset Event Structure
  property_count: 9
  slug: openapi.yaml-dataset-event-structure
- name: Openapi.Yaml Dataset Structure
  property_count: 7
  slug: openapi.yaml-dataset-structure
- name: Openapi.Yaml Event Log Collection Structure
  property_count: 0
  slug: openapi.yaml-event-log-collection-structure
- name: Openapi.Yaml Event Log Structure
  property_count: 8
  slug: openapi.yaml-event-log-structure
- name: Openapi.Yaml Extra Link Collection Structure
  property_count: 1
  slug: openapi.yaml-extra-link-collection-structure
- name: Openapi.Yaml Extra Link Structure
  property_count: 3
  slug: openapi.yaml-extra-link-structure
- name: Openapi.Yaml Health Info Structure
  property_count: 2
  slug: openapi.yaml-health-info-structure
- name: Openapi.Yaml Health Status Structure
  property_count: 0
  slug: openapi.yaml-health-status-structure
- name: Openapi.Yaml Import Error Collection Structure
  property_count: 0
  slug: openapi.yaml-import-error-collection-structure
- name: Openapi.Yaml Import Error Structure
  property_count: 4
  slug: openapi.yaml-import-error-structure
- name: Openapi.Yaml Job Structure
  property_count: 10
  slug: openapi.yaml-job-structure
- name: Openapi.Yaml List Dag Runs Form Structure
  property_count: 11
  slug: openapi.yaml-list-dag-runs-form-structure
- name: Openapi.Yaml List Task Instance Form Structure
  property_count: 12
  slug: openapi.yaml-list-task-instance-form-structure
- name: Openapi.Yaml Metadatabase Status Structure
  property_count: 1
  slug: openapi.yaml-metadatabase-status-structure
- name: Openapi.Yaml Plugin Collection Item Structure
  property_count: 10
  slug: openapi.yaml-plugin-collection-item-structure
- name: Openapi.Yaml Plugin Collection Structure
  property_count: 0
  slug: openapi.yaml-plugin-collection-structure
- name: Openapi.Yaml Pool Collection Structure
  property_count: 0
  slug: openapi.yaml-pool-collection-structure
- name: Openapi.Yaml Pool Structure
  property_count: 7
  slug: openapi.yaml-pool-structure
- name: Openapi.Yaml Provider Collection Structure
  property_count: 1
  slug: openapi.yaml-provider-collection-structure
- name: Openapi.Yaml Provider Structure
  property_count: 3
  slug: openapi.yaml-provider-structure
- name: Openapi.Yaml Relative Delta Structure
  property_count: 16
  slug: openapi.yaml-relative-delta-structure
- name: Openapi.Yaml Resource Structure
  property_count: 1
  slug: openapi.yaml-resource-structure
- name: Openapi.Yaml Role Collection Structure
  property_count: 0
  slug: openapi.yaml-role-collection-structure
- name: Openapi.Yaml Role Structure
  property_count: 2
  slug: openapi.yaml-role-structure
- name: Openapi.Yaml Schedule Interval Structure
  property_count: 0
  slug: openapi.yaml-schedule-interval-structure
- name: Openapi.Yaml Scheduler Status Structure
  property_count: 2
  slug: openapi.yaml-scheduler-status-structure
- name: Openapi.Yaml Set Dag Run Note Structure
  property_count: 1
  slug: openapi.yaml-set-dag-run-note-structure
- name: Openapi.Yaml Set Task Instance Note Structure
  property_count: 1
  slug: openapi.yaml-set-task-instance-note-structure
- name: Openapi.Yaml Sla Miss Structure
  property_count: 7
  slug: openapi.yaml-sla-miss-structure
- name: Openapi.Yaml Tag Structure
  property_count: 1
  slug: openapi.yaml-tag-structure
- name: Openapi.Yaml Task Collection Structure
  property_count: 1
  slug: openapi.yaml-task-collection-structure
- name: Openapi.Yaml Task Instance Collection Structure
  property_count: 0
  slug: openapi.yaml-task-instance-collection-structure
- name: Openapi.Yaml Task Instance Reference Collection Structure
  property_count: 1
  slug: openapi.yaml-task-instance-reference-collection-structure
- name: Openapi.Yaml Task Instance Reference Structure
  property_count: 4
  slug: openapi.yaml-task-instance-reference-structure
- name: Openapi.Yaml Task Instance Structure
  property_count: 26
  slug: openapi.yaml-task-instance-structure
- name: Openapi.Yaml Task Outlet Dataset Reference Structure
  property_count: 4
  slug: openapi.yaml-task-outlet-dataset-reference-structure
- name: Openapi.Yaml Task State Structure
  property_count: 0
  slug: openapi.yaml-task-state-structure
- name: Openapi.Yaml Task Structure
  property_count: 24
  slug: openapi.yaml-task-structure
- name: Openapi.Yaml Time Delta Structure
  property_count: 4
  slug: openapi.yaml-time-delta-structure
- name: Openapi.Yaml Timezone Structure
  property_count: 0
  slug: openapi.yaml-timezone-structure
- name: Openapi.Yaml Trigger Rule Structure
  property_count: 0
  slug: openapi.yaml-trigger-rule-structure
- name: Openapi.Yaml Trigger Structure
  property_count: 5
  slug: openapi.yaml-trigger-structure
- name: Openapi.Yaml Update Dag Run State Structure
  property_count: 1
  slug: openapi.yaml-update-dag-run-state-structure
- name: Openapi.Yaml Update Task Instance Structure
  property_count: 2
  slug: openapi.yaml-update-task-instance-structure
- name: Openapi.Yaml Update Task Instances State Structure
  property_count: 9
  slug: openapi.yaml-update-task-instances-state-structure
- name: Openapi.Yaml User Collection Item Structure
  property_count: 11
  slug: openapi.yaml-user-collection-item-structure
- name: Openapi.Yaml User Collection Structure
  property_count: 0
  slug: openapi.yaml-user-collection-structure
- name: Openapi.Yaml User Structure
  property_count: 0
  slug: openapi.yaml-user-structure
- name: Openapi.Yaml Variable Collection Item Structure
  property_count: 2
  slug: openapi.yaml-variable-collection-item-structure
- name: Openapi.Yaml Variable Collection Structure
  property_count: 0
  slug: openapi.yaml-variable-collection-structure
- name: Openapi.Yaml Variable Structure
  property_count: 0
  slug: openapi.yaml-variable-structure
- name: Openapi.Yaml Version Info Structure
  property_count: 2
  slug: openapi.yaml-version-info-structure
- name: Openapi.Yaml Weight Rule Structure
  property_count: 0
  slug: openapi.yaml-weight-rule-structure
- name: Openapi.Yaml X Com Collection Item Structure
  property_count: 5
  slug: openapi.yaml-x-com-collection-item-structure
- name: Openapi.Yaml X Com Collection Structure
  property_count: 0
  slug: openapi.yaml-x-com-collection-structure
- name: Openapi.Yaml X Com Structure
  property_count: 0
  slug: openapi.yaml-x-com-structure
jsonld:
- class_count: 88
  name: Apache Airflow Context
  property_count: 197
  slug: apache-airflow-context
layout: provider
mcp_servers:
- description: ''
  name: apache-airflow-mcp.yml
  slug: apache-airflow-mcpyml
modified: '2026-06-20'
name: Apache Airflow
nav: Providers
network: true
overview: 'Apache Airflow publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Config API, Connection API, DAG API, and 15 more. Tagged areas include Apache, DAG, Data Pipeline, ETL, and Open Source.


  The Apache Airflow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Airflow''s developer surface includes changelog, CLI, authentication, documentation, getting-started guide, engineering blog, support, and 36 more developer resources.'
plans:
- name: Apache Airflow Plans Pricing
  plan_count: 3
  slug: apache-airflow-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Apache Airflow Rate Limits
  slug: apache-airflow-rate-limits
rules:
- name: Apache Airflow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-airflow-jsonschema-spectral-rules
- name: Apache Airflow API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 19
  slug: apache-airflow-spectral-rules
score:
  band: strong
  composite: 61.2
  delta: -1.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.3
    developer_ergonomics: 56.5
    discoverability: 83.3
    governance: 80.2
    operational_transparency: 63.2
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-airflow/refs/heads/main/screenshots/apache-airflow-2026-06-20T172038.png
security:
- kind: authentication
  name: Apache Airflow Authentication
  slug: apache-airflow-authentication
  summary_line: http/openIdConnect · 3 schemes
- kind: domain-security
  name: Apache Airflow Domain Security
  slug: apache-airflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Airflow Vulnerability Disclosure
  slug: apache-airflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-airflow
tags:
- Apache
- DAG
- Data Pipeline
- ETL
- Open Source
- Orchestration
- Python
- Scheduling
- Workflow
use_cases:
- description: Schedule and manage extract, transform, load pipelines with dependency management and retry logic.
  name: ETL Pipeline Orchestration
- description: Orchestrate ML training, validation, and deployment pipelines with data dependency tracking.
  name: Machine Learning Workflows
- description: Coordinate data ingestion from multiple sources into data warehouses like BigQuery, Redshift, and Snowflake.
  name: Data Warehouse Loading
- description: Schedule periodic batch reporting jobs with email notification on completion or failure.
  name: Batch Report Generation
- description: Move data between AWS, GCP, and Azure using provider integrations with dependency control.
  name: Multi-Cloud Data Movement
- description: Trigger and monitor software deployment pipelines with upstream/downstream task dependencies.
  name: CI/CD Pipeline Orchestration
---
