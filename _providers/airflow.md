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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Airflow Agentic Access
  operation_count: 110
  slug: airflow-agentic-access
  summary_line: 110 operations · 47 acting
api_count: 26
apis:
- description: The Asset API from Apache Airflow — 9 operation(s) for asset.
  name: Apache Airflow Asset API
  slug: airflow-asset-api
- description: The Backfill API from Apache Airflow — 6 operation(s) for backfill.
  name: Apache Airflow Backfill API
  slug: airflow-backfill-api
- description: The Config API from Apache Airflow — 2 operation(s) for config.
  name: Apache Airflow Config API
  slug: airflow-config-api
- description: The Connection API from Apache Airflow — 4 operation(s) for connection.
  name: Apache Airflow Connection API
  slug: airflow-connection-api
- description: The DAG API from Apache Airflow — 6 operation(s) for dag.
  name: Apache Airflow DAG API
  slug: airflow-dag-api
- description: The DAG Parsing API from Apache Airflow — 1 operation(s) for dag parsing.
  name: Apache Airflow DAG Parsing API
  slug: airflow-dag-parsing-api
- description: The DagRun API from Apache Airflow — 6 operation(s) for dagrun.
  name: Apache Airflow DagRun API
  slug: airflow-dagrun-api
- description: The DagSource API from Apache Airflow — 1 operation(s) for dagsource.
  name: Apache Airflow DagSource API
  slug: airflow-dagsource-api
- description: The DagStats API from Apache Airflow — 1 operation(s) for dagstats.
  name: Apache Airflow DagStats API
  slug: airflow-dagstats-api
- description: The DagVersion API from Apache Airflow — 2 operation(s) for dagversion.
  name: Apache Airflow DagVersion API
  slug: airflow-dagversion-api
- description: The DagWarning API from Apache Airflow — 1 operation(s) for dagwarning.
  name: Apache Airflow DagWarning API
  slug: airflow-dagwarning-api
- description: The Event Log API from Apache Airflow — 2 operation(s) for event log.
  name: Apache Airflow Event Log API
  slug: airflow-event-log-api
- description: The experimental API from Apache Airflow — 1 operation(s) for experimental.
  name: Apache Airflow experimental API
  slug: airflow-experimental-api
- description: The Extra Links API from Apache Airflow — 1 operation(s) for extra links.
  name: Apache Airflow Extra Links API
  slug: airflow-extra-links-api
- description: The Import Error API from Apache Airflow — 2 operation(s) for import error.
  name: Apache Airflow Import Error API
  slug: airflow-import-error-api
- description: The Job API from Apache Airflow — 1 operation(s) for job.
  name: Apache Airflow Job API
  slug: airflow-job-api
- description: The Login API from Apache Airflow — 2 operation(s) for login.
  name: Apache Airflow Login API
  slug: airflow-login-api
- description: The Monitor API from Apache Airflow — 1 operation(s) for monitor.
  name: Apache Airflow Monitor API
  slug: airflow-monitor-api
- description: The Plugin API from Apache Airflow — 2 operation(s) for plugin.
  name: Apache Airflow Plugin API
  slug: airflow-plugin-api
- description: The Pool API from Apache Airflow — 2 operation(s) for pool.
  name: Apache Airflow Pool API
  slug: airflow-pool-api
- description: The Provider API from Apache Airflow — 1 operation(s) for provider.
  name: Apache Airflow Provider API
  slug: airflow-provider-api
- description: The Task API from Apache Airflow — 2 operation(s) for task.
  name: Apache Airflow Task API
  slug: airflow-task-api
- description: The Task Instance API from Apache Airflow — 20 operation(s) for task instance.
  name: Apache Airflow Task Instance API
  slug: airflow-task-instance-api
- description: The Variable API from Apache Airflow — 2 operation(s) for variable.
  name: Apache Airflow Variable API
  slug: airflow-variable-api
- description: The Version API from Apache Airflow — 1 operation(s) for version.
  name: Apache Airflow Version API
  slug: airflow-version-api
- description: The XCom API from Apache Airflow — 2 operation(s) for xcom.
  name: Apache Airflow XCom API
  slug: airflow-xcom-api
artifact_total: 475
collections:
- collection_type: open
  name: Airflow API
  slug: open-airflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airflow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airflow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airflow-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-airflow
- group: start
  title: ''
  type: Portal
  url: https://airflow.apache.org
- group: start
  title: ''
  type: GettingStarted
  url: https://airflow.apache.org/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/airflow
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/airflow
- group: company
  title: ''
  type: Blog
  url: https://airflow.apache.org/blog/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/airflow
- group: operate
  title: ''
  type: ChangeLog
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/projects/AIRFLOW
- group: build
  title: Docker Image
  type: SDKs
  url: https://hub.docker.com/r/apache/airflow
- group: build
  title: Helm Chart
  type: SDKs
  url: https://artifacthub.io/packages/helm/airflow-helm/airflow
- group: design
  title: Airflow Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/rules/airflow-spectral-rules.yml
- group: design
  title: Airflow Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/vocabulary/airflow-vocabulary.yaml
created: '2026-01-02'
description: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. Airflow uses directed acyclic graphs (DAGs) to manage workflow orchestration. The Airflow REST API provides programmatic access to DAGs, DAG runs, tasks, connections, variables, pools, and monitoring for both Airflow OSS and cloud-managed deployments.
examples:
- key_count: 3
  name: Airflow App Builder Menu Item Response Example
  slug: airflow-app-builder-menu-item-response-example
- key_count: 4
  name: Airflow App Builder View Response Example
  slug: airflow-app-builder-view-response-example
- key_count: 2
  name: Airflow Asset Alias Collection Response Example
  slug: airflow-asset-alias-collection-response-example
- key_count: 3
  name: Airflow Asset Alias Response Example
  slug: airflow-asset-alias-response-example
- key_count: 2
  name: Airflow Asset Collection Response Example
  slug: airflow-asset-collection-response-example
- key_count: 2
  name: Airflow Asset Event Collection Response Example
  slug: airflow-asset-event-collection-response-example
- key_count: 13
  name: Airflow Asset Event Response Example
  slug: airflow-asset-event-response-example
- key_count: 13
  name: Airflow Asset Response Example
  slug: airflow-asset-response-example
- key_count: 3
  name: Airflow Asset Watcher Response Example
  slug: airflow-asset-watcher-response-example
- key_count: 2
  name: Airflow Backfill Collection Response Example
  slug: airflow-backfill-collection-response-example
- key_count: 8
  name: Airflow Backfill Post Body Example
  slug: airflow-backfill-post-body-example
- key_count: 12
  name: Airflow Backfill Response Example
  slug: airflow-backfill-response-example
- key_count: 1
  name: Airflow Base Info Response Example
  slug: airflow-base-info-response-example
- key_count: 0
  name: Airflow Bulk Action Not On Existence Example
  slug: airflow-bulk-action-not-on-existence-example
- key_count: 0
  name: Airflow Bulk Action On Existence Example
  slug: airflow-bulk-action-on-existence-example
- key_count: 2
  name: Airflow Bulk Action Response Example
  slug: airflow-bulk-action-response-example
- key_count: 1
  name: Airflow Bulk Body_ Bulk Task Instance Body_ Example
  slug: airflow-bulk-body_-bulk-task-instance-body_-example
- key_count: 1
  name: Airflow Bulk Body_ Connection Body_ Example
  slug: airflow-bulk-body_-connection-body_-example
- key_count: 1
  name: Airflow Bulk Body_ Pool Body_ Example
  slug: airflow-bulk-body_-pool-body_-example
- key_count: 1
  name: Airflow Bulk Body_ Variable Body_ Example
  slug: airflow-bulk-body_-variable-body_-example
- key_count: 3
  name: Airflow Bulk Create Action_ Bulk Task Instance Body_ Example
  slug: airflow-bulk-create-action_-bulk-task-instance-body_-example
- key_count: 3
  name: Airflow Bulk Create Action_ Connection Body_ Example
  slug: airflow-bulk-create-action_-connection-body_-example
- key_count: 3
  name: Airflow Bulk Create Action_ Pool Body_ Example
  slug: airflow-bulk-create-action_-pool-body_-example
- key_count: 3
  name: Airflow Bulk Create Action_ Variable Body_ Example
  slug: airflow-bulk-create-action_-variable-body_-example
- key_count: 3
  name: Airflow Bulk Delete Action_ Bulk Task Instance Body_ Example
  slug: airflow-bulk-delete-action_-bulk-task-instance-body_-example
- key_count: 3
  name: Airflow Bulk Delete Action_ Connection Body_ Example
  slug: airflow-bulk-delete-action_-connection-body_-example
- key_count: 3
  name: Airflow Bulk Delete Action_ Pool Body_ Example
  slug: airflow-bulk-delete-action_-pool-body_-example
- key_count: 3
  name: Airflow Bulk Delete Action_ Variable Body_ Example
  slug: airflow-bulk-delete-action_-variable-body_-example
- key_count: 3
  name: Airflow Bulk Response Example
  slug: airflow-bulk-response-example
- key_count: 10
  name: Airflow Bulk Task Instance Body Example
  slug: airflow-bulk-task-instance-body-example
- key_count: 4
  name: Airflow Bulk Update Action_ Bulk Task Instance Body_ Example
  slug: airflow-bulk-update-action_-bulk-task-instance-body_-example
- key_count: 4
  name: Airflow Bulk Update Action_ Connection Body_ Example
  slug: airflow-bulk-update-action_-connection-body_-example
- key_count: 4
  name: Airflow Bulk Update Action_ Pool Body_ Example
  slug: airflow-bulk-update-action_-pool-body_-example
- key_count: 4
  name: Airflow Bulk Update Action_ Variable Body_ Example
  slug: airflow-bulk-update-action_-variable-body_-example
- key_count: 15
  name: Airflow Clear Task Instances Body Example
  slug: airflow-clear-task-instances-body-example
- key_count: 1
  name: Airflow Config Example
  slug: airflow-config-example
- key_count: 2
  name: Airflow Config Option Example
  slug: airflow-config-option-example
- key_count: 2
  name: Airflow Config Section Example
  slug: airflow-config-section-example
- key_count: 10
  name: Airflow Connection Body Example
  slug: airflow-connection-body-example
- key_count: 2
  name: Airflow Connection Collection Response Example
  slug: airflow-connection-collection-response-example
- key_count: 10
  name: Airflow Connection Response Example
  slug: airflow-connection-response-example
- key_count: 2
  name: Airflow Connection Test Response Example
  slug: airflow-connection-test-response-example
- key_count: 3
  name: Airflow Create Asset Events Body Example
  slug: airflow-create-asset-events-body-example
- key_count: 2
  name: Airflow Dag Collection Response Example
  slug: airflow-dag-collection-response-example
- key_count: 48
  name: Airflow Dag Details Response Example
  slug: airflow-dag-details-response-example
- key_count: 1
  name: Airflow Dag Patch Body Example
  slug: airflow-dag-patch-body-example
- key_count: 2
  name: Airflow Dag Processor Info Response Example
  slug: airflow-dag-processor-info-response-example
- key_count: 30
  name: Airflow Dag Response Example
  slug: airflow-dag-response-example
- key_count: 9
  name: Airflow Dag Run Asset Reference Example
  slug: airflow-dag-run-asset-reference-example
- key_count: 3
  name: Airflow Dag Run Clear Body Example
  slug: airflow-dag-run-clear-body-example
- key_count: 2
  name: Airflow Dag Run Collection Response Example
  slug: airflow-dag-run-collection-response-example
- key_count: 2
  name: Airflow Dag Run Patch Body Example
  slug: airflow-dag-run-patch-body-example
- key_count: 0
  name: Airflow Dag Run Patch States Example
  slug: airflow-dag-run-patch-states-example
- key_count: 21
  name: Airflow Dag Run Response Example
  slug: airflow-dag-run-response-example
- key_count: 0
  name: Airflow Dag Run State Example
  slug: airflow-dag-run-state-example
- key_count: 0
  name: Airflow Dag Run Triggered By Type Example
  slug: airflow-dag-run-triggered-by-type-example
- key_count: 0
  name: Airflow Dag Run Type Example
  slug: airflow-dag-run-type-example
- key_count: 26
  name: Airflow Dag Runs Batch Body Example
  slug: airflow-dag-runs-batch-body-example
- key_count: 3
  name: Airflow Dag Schedule Asset Reference Example
  slug: airflow-dag-schedule-asset-reference-example
- key_count: 4
  name: Airflow Dag Source Response Example
  slug: airflow-dag-source-response-example
- key_count: 2
  name: Airflow Dag Stats Collection Response Example
  slug: airflow-dag-stats-collection-response-example
- key_count: 3
  name: Airflow Dag Stats Response Example
  slug: airflow-dag-stats-response-example
- key_count: 2
  name: Airflow Dag Stats State Response Example
  slug: airflow-dag-stats-state-response-example
- key_count: 2
  name: Airflow Dag Tag Collection Response Example
  slug: airflow-dag-tag-collection-response-example
- key_count: 3
  name: Airflow Dag Tag Response Example
  slug: airflow-dag-tag-response-example
- key_count: 2
  name: Airflow Dag Version Collection Response Example
  slug: airflow-dag-version-collection-response-example
- key_count: 8
  name: Airflow Dag Version Response Example
  slug: airflow-dag-version-response-example
- key_count: 2
  name: Airflow Dag Warning Collection Response Example
  slug: airflow-dag-warning-collection-response-example
- key_count: 5
  name: Airflow Dag Warning Response Example
  slug: airflow-dag-warning-response-example
- key_count: 0
  name: Airflow Dag Warning Type Example
  slug: airflow-dag-warning-type-example
- key_count: 2
  name: Airflow Dry Run Backfill Collection Response Example
  slug: airflow-dry-run-backfill-collection-response-example
- key_count: 3
  name: Airflow Dry Run Backfill Response Example
  slug: airflow-dry-run-backfill-response-example
- key_count: 2
  name: Airflow Event Log Collection Response Example
  slug: airflow-event-log-collection-response-example
- key_count: 13
  name: Airflow Event Log Response Example
  slug: airflow-event-log-response-example
- key_count: 1
  name: Airflow External Log Url Response Example
  slug: airflow-external-log-url-response-example
- key_count: 7
  name: Airflow External View Response Example
  slug: airflow-external-view-response-example
- key_count: 2
  name: Airflow Extra Link Collection Response Example
  slug: airflow-extra-link-collection-response-example
- key_count: 3
  name: Airflow Fast Api App Response Example
  slug: airflow-fast-api-app-response-example
- key_count: 2
  name: Airflow Fast Api Root Middleware Response Example
  slug: airflow-fast-api-root-middleware-response-example
- key_count: 4
  name: Airflow Health Info Response Example
  slug: airflow-health-info-response-example
- key_count: 2
  name: Airflow Hitl Detail Collection Example
  slug: airflow-hitl-detail-collection-example
- key_count: 14
  name: Airflow Hitl Detail Example
  slug: airflow-hitl-detail-example
- key_count: 14
  name: Airflow Hitl Detail History Example
  slug: airflow-hitl-detail-history-example
- key_count: 4
  name: Airflow Hitl Detail Response Example
  slug: airflow-hitl-detail-response-example
- key_count: 2
  name: Airflow Hitl User Example
  slug: airflow-hitl-user-example
- key_count: 1
  name: Airflow Http Exception Response Example
  slug: airflow-http-exception-response-example
- key_count: 2
  name: Airflow Import Error Collection Response Example
  slug: airflow-import-error-collection-response-example
- key_count: 5
  name: Airflow Import Error Response Example
  slug: airflow-import-error-response-example
- key_count: 2
  name: Airflow Job Collection Response Example
  slug: airflow-job-collection-response-example
- key_count: 11
  name: Airflow Job Response Example
  slug: airflow-job-response-example
- key_count: 0
  name: Airflow Json Value Example
  slug: airflow-json-value-example
- key_count: 2
  name: Airflow Last Asset Event Response Example
  slug: airflow-last-asset-event-response-example
- key_count: 8
  name: Airflow Materialize Asset Body Example
  slug: airflow-materialize-asset-body-example
- key_count: 6
  name: Airflow Patch Task Instance Body Example
  slug: airflow-patch-task-instance-body-example
- key_count: 2
  name: Airflow Plugin Collection Response Example
  slug: airflow-plugin-collection-response-example
- key_count: 2
  name: Airflow Plugin Import Error Collection Response Example
  slug: airflow-plugin-import-error-collection-response-example
- key_count: 2
  name: Airflow Plugin Import Error Response Example
  slug: airflow-plugin-import-error-response-example
- key_count: 14
  name: Airflow Plugin Response Example
  slug: airflow-plugin-response-example
- key_count: 5
  name: Airflow Pool Body Example
  slug: airflow-pool-body-example
- key_count: 2
  name: Airflow Pool Collection Response Example
  slug: airflow-pool-collection-response-example
- key_count: 5
  name: Airflow Pool Patch Body Example
  slug: airflow-pool-patch-body-example
- key_count: 11
  name: Airflow Pool Response Example
  slug: airflow-pool-response-example
- key_count: 2
  name: Airflow Provider Collection Response Example
  slug: airflow-provider-collection-response-example
- key_count: 4
  name: Airflow Provider Response Example
  slug: airflow-provider-response-example
- key_count: 2
  name: Airflow Queued Event Collection Response Example
  slug: airflow-queued-event-collection-response-example
- key_count: 4
  name: Airflow Queued Event Response Example
  slug: airflow-queued-event-response-example
- key_count: 7
  name: Airflow React App Response Example
  slug: airflow-react-app-response-example
- key_count: 0
  name: Airflow Reprocess Behavior Example
  slug: airflow-reprocess-behavior-example
- key_count: 2
  name: Airflow Scheduler Info Response Example
  slug: airflow-scheduler-info-response-example
- key_count: 2
  name: Airflow Structured Log Message Example
  slug: airflow-structured-log-message-example
- key_count: 2
  name: Airflow Task Collection Response Example
  slug: airflow-task-collection-response-example
- key_count: 1
  name: Airflow Task Dependency Collection Response Example
  slug: airflow-task-dependency-collection-response-example
- key_count: 2
  name: Airflow Task Dependency Response Example
  slug: airflow-task-dependency-response-example
- key_count: 4
  name: Airflow Task Inlet Asset Reference Example
  slug: airflow-task-inlet-asset-reference-example
- key_count: 4
  name: Airflow Task Instance Collection Response Example
  slug: airflow-task-instance-collection-response-example
- key_count: 2
  name: Airflow Task Instance History Collection Response Example
  slug: airflow-task-instance-history-collection-response-example
- key_count: 26
  name: Airflow Task Instance History Response Example
  slug: airflow-task-instance-history-response-example
- key_count: 34
  name: Airflow Task Instance Response Example
  slug: airflow-task-instance-response-example
- key_count: 0
  name: Airflow Task Instance State Example
  slug: airflow-task-instance-state-example
- key_count: 30
  name: Airflow Task Instances Batch Body Example
  slug: airflow-task-instances-batch-body-example
- key_count: 2
  name: Airflow Task Instances Log Response Example
  slug: airflow-task-instances-log-response-example
- key_count: 4
  name: Airflow Task Outlet Asset Reference Example
  slug: airflow-task-outlet-asset-reference-example
- key_count: 27
  name: Airflow Task Response Example
  slug: airflow-task-response-example
- key_count: 4
  name: Airflow Time Delta Example
  slug: airflow-time-delta-example
- key_count: 8
  name: Airflow Trigger Dag Run Post Body Example
  slug: airflow-trigger-dag-run-post-body-example
- key_count: 6
  name: Airflow Trigger Response Example
  slug: airflow-trigger-response-example
- key_count: 2
  name: Airflow Triggerer Info Response Example
  slug: airflow-triggerer-info-response-example
- key_count: 2
  name: Airflow Update Hitl Detail Payload Example
  slug: airflow-update-hitl-detail-payload-example
- key_count: 4
  name: Airflow Variable Body Example
  slug: airflow-variable-body-example
- key_count: 2
  name: Airflow Variable Collection Response Example
  slug: airflow-variable-collection-response-example
- key_count: 5
  name: Airflow Variable Response Example
  slug: airflow-variable-response-example
- key_count: 2
  name: Airflow Version Info Example
  slug: airflow-version-info-example
- key_count: 2
  name: Airflow X Com Collection Response Example
  slug: airflow-x-com-collection-response-example
- key_count: 3
  name: Airflow X Com Create Body Example
  slug: airflow-x-com-create-body-example
- key_count: 10
  name: Airflow X Com Response Example
  slug: airflow-x-com-response-example
- key_count: 11
  name: Airflow X Com Response Native Example
  slug: airflow-x-com-response-native-example
- key_count: 11
  name: Airflow X Com Response String Example
  slug: airflow-x-com-response-string-example
- key_count: 2
  name: Airflow X Com Update Body Example
  slug: airflow-x-com-update-body-example
features:
- description: Define workflows as Python code using Directed Acyclic Graphs (DAGs).
  name: DAG Authoring
- description: Programmatically generate DAGs and tasks based on configuration or data.
  name: Dynamic DAG Generation
- description: Pre-built operators for databases, cloud services, APIs, and data tools.
  name: Rich Operator Library
- description: Stable REST API for programmatic management of DAGs, runs, tasks, and infrastructure.
  name: REST API v2
- description: Built-in web interface for monitoring, triggering, and debugging workflows.
  name: Web UI
- description: Robust scheduler with support for CRON and timed triggers.
  name: Scheduler
- description: Plugin system and provider packages for extending functionality.
  name: Extensible
- description: Provider packages for AWS, GCP, Azure, and other cloud platforms.
  name: Multi-Cloud Support
- description: Available as managed service from AWS (MWAA), GCP (Cloud Composer), and Astronomer.
  name: Managed Services
finops:
- name: Airflow Finops
  service_category: API
  slug: airflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airflow.png
integrations:
- description: Run Spark jobs from Airflow DAGs.
  name: Apache Spark
- description: Orchestrate dbt model runs via the dbt operator.
  name: dbt
- description: Run tasks in Kubernetes pods with the KubernetesPodOperator.
  name: Kubernetes
- description: Provider package for S3, Redshift, EMR, Lambda, and other AWS services.
  name: AWS
- description: Provider package for BigQuery, Dataflow, GCS, and other GCP services.
  name: Google Cloud
- description: Provider package for Azure Data Factory, Blob Storage, and other Azure services.
  name: Azure
- description: SnowflakeOperator for running SQL in Snowflake data warehouse.
  name: Snowflake
- description: Trigger Airbyte syncs from Airflow DAGs.
  name: Airbyte
json_schemas:
- name: AppBuilderMenuItemResponse
  property_count: 3
  slug: airflow-app-builder-menu-item-response
- name: AppBuilderViewResponse
  property_count: 4
  slug: airflow-app-builder-view-response
- name: AssetAliasCollectionResponse
  property_count: 2
  slug: airflow-asset-alias-collection-response
- name: AssetAliasResponse
  property_count: 3
  slug: airflow-asset-alias-response
- name: AssetCollectionResponse
  property_count: 2
  slug: airflow-asset-collection-response
- name: AssetEventCollectionResponse
  property_count: 2
  slug: airflow-asset-event-collection-response
- name: AssetEventResponse
  property_count: 13
  slug: airflow-asset-event-response
- name: AssetResponse
  property_count: 13
  slug: airflow-asset-response
- name: AssetWatcherResponse
  property_count: 3
  slug: airflow-asset-watcher-response
- name: BackfillCollectionResponse
  property_count: 2
  slug: airflow-backfill-collection-response
- name: BackfillPostBody
  property_count: 8
  slug: airflow-backfill-post-body
- name: BackfillResponse
  property_count: 12
  slug: airflow-backfill-response
- name: BaseInfoResponse
  property_count: 1
  slug: airflow-base-info-response
- name: BulkActionNotOnExistence
  property_count: 0
  slug: airflow-bulk-action-not-on-existence
- name: BulkActionOnExistence
  property_count: 0
  slug: airflow-bulk-action-on-existence
- name: BulkActionResponse
  property_count: 2
  slug: airflow-bulk-action-response
- name: BulkBody_BulkTaskInstanceBody_
  property_count: 1
  slug: airflow-bulk-body_-bulk-task-instance-body_
- name: BulkBody_ConnectionBody_
  property_count: 1
  slug: airflow-bulk-body_-connection-body_
- name: BulkBody_PoolBody_
  property_count: 1
  slug: airflow-bulk-body_-pool-body_
- name: BulkBody_VariableBody_
  property_count: 1
  slug: airflow-bulk-body_-variable-body_
- name: BulkCreateAction_BulkTaskInstanceBody_
  property_count: 3
  slug: airflow-bulk-create-action_-bulk-task-instance-body_
- name: BulkCreateAction_ConnectionBody_
  property_count: 3
  slug: airflow-bulk-create-action_-connection-body_
- name: BulkCreateAction_PoolBody_
  property_count: 3
  slug: airflow-bulk-create-action_-pool-body_
- name: BulkCreateAction_VariableBody_
  property_count: 3
  slug: airflow-bulk-create-action_-variable-body_
- name: BulkDeleteAction_BulkTaskInstanceBody_
  property_count: 3
  slug: airflow-bulk-delete-action_-bulk-task-instance-body_
- name: BulkDeleteAction_ConnectionBody_
  property_count: 3
  slug: airflow-bulk-delete-action_-connection-body_
- name: BulkDeleteAction_PoolBody_
  property_count: 3
  slug: airflow-bulk-delete-action_-pool-body_
- name: BulkDeleteAction_VariableBody_
  property_count: 3
  slug: airflow-bulk-delete-action_-variable-body_
- name: BulkResponse
  property_count: 3
  slug: airflow-bulk-response
- name: BulkTaskInstanceBody
  property_count: 10
  slug: airflow-bulk-task-instance-body
- name: BulkUpdateAction_BulkTaskInstanceBody_
  property_count: 4
  slug: airflow-bulk-update-action_-bulk-task-instance-body_
- name: BulkUpdateAction_ConnectionBody_
  property_count: 4
  slug: airflow-bulk-update-action_-connection-body_
- name: BulkUpdateAction_PoolBody_
  property_count: 4
  slug: airflow-bulk-update-action_-pool-body_
- name: BulkUpdateAction_VariableBody_
  property_count: 4
  slug: airflow-bulk-update-action_-variable-body_
- name: ClearTaskInstancesBody
  property_count: 15
  slug: airflow-clear-task-instances-body
- name: ConfigOption
  property_count: 2
  slug: airflow-config-option
- name: Config
  property_count: 1
  slug: airflow-config
- name: ConfigSection
  property_count: 2
  slug: airflow-config-section
- name: ConnectionBody
  property_count: 10
  slug: airflow-connection-body
- name: ConnectionCollectionResponse
  property_count: 2
  slug: airflow-connection-collection-response
- name: ConnectionResponse
  property_count: 10
  slug: airflow-connection-response
- name: ConnectionTestResponse
  property_count: 2
  slug: airflow-connection-test-response
- name: CreateAssetEventsBody
  property_count: 3
  slug: airflow-create-asset-events-body
- name: DAGCollectionResponse
  property_count: 2
  slug: airflow-dag-collection-response
- name: DAGDetailsResponse
  property_count: 48
  slug: airflow-dag-details-response
- name: DAGPatchBody
  property_count: 1
  slug: airflow-dag-patch-body
- name: DagProcessorInfoResponse
  property_count: 2
  slug: airflow-dag-processor-info-response
- name: DAGResponse
  property_count: 30
  slug: airflow-dag-response
- name: DagRunAssetReference
  property_count: 9
  slug: airflow-dag-run-asset-reference
- name: DAGRunClearBody
  property_count: 3
  slug: airflow-dag-run-clear-body
- name: DAGRunCollectionResponse
  property_count: 2
  slug: airflow-dag-run-collection-response
- name: DAGRunPatchBody
  property_count: 2
  slug: airflow-dag-run-patch-body
- name: DAGRunPatchStates
  property_count: 0
  slug: airflow-dag-run-patch-states
- name: DAGRunResponse
  property_count: 21
  slug: airflow-dag-run-response
- name: DagRunState
  property_count: 0
  slug: airflow-dag-run-state
- name: DagRunTriggeredByType
  property_count: 0
  slug: airflow-dag-run-triggered-by-type
- name: DagRunType
  property_count: 0
  slug: airflow-dag-run-type
- name: DAGRunsBatchBody
  property_count: 26
  slug: airflow-dag-runs-batch-body
- name: DagScheduleAssetReference
  property_count: 3
  slug: airflow-dag-schedule-asset-reference
- name: DAGSourceResponse
  property_count: 4
  slug: airflow-dag-source-response
- name: DagStatsCollectionResponse
  property_count: 2
  slug: airflow-dag-stats-collection-response
- name: DagStatsResponse
  property_count: 3
  slug: airflow-dag-stats-response
- name: DagStatsStateResponse
  property_count: 2
  slug: airflow-dag-stats-state-response
- name: DAGTagCollectionResponse
  property_count: 2
  slug: airflow-dag-tag-collection-response
- name: DagTagResponse
  property_count: 3
  slug: airflow-dag-tag-response
- name: DAGVersionCollectionResponse
  property_count: 2
  slug: airflow-dag-version-collection-response
- name: DagVersionResponse
  property_count: 8
  slug: airflow-dag-version-response
- name: DAGWarningCollectionResponse
  property_count: 2
  slug: airflow-dag-warning-collection-response
- name: DAGWarningResponse
  property_count: 5
  slug: airflow-dag-warning-response
- name: DagWarningType
  property_count: 0
  slug: airflow-dag-warning-type
- name: DryRunBackfillCollectionResponse
  property_count: 2
  slug: airflow-dry-run-backfill-collection-response
- name: DryRunBackfillResponse
  property_count: 3
  slug: airflow-dry-run-backfill-response
- name: EventLogCollectionResponse
  property_count: 2
  slug: airflow-event-log-collection-response
- name: EventLogResponse
  property_count: 13
  slug: airflow-event-log-response
- name: ExternalLogUrlResponse
  property_count: 1
  slug: airflow-external-log-url-response
- name: ExternalViewResponse
  property_count: 7
  slug: airflow-external-view-response
- name: ExtraLinkCollectionResponse
  property_count: 2
  slug: airflow-extra-link-collection-response
- name: FastAPIAppResponse
  property_count: 3
  slug: airflow-fast-api-app-response
- name: FastAPIRootMiddlewareResponse
  property_count: 2
  slug: airflow-fast-api-root-middleware-response
- name: HealthInfoResponse
  property_count: 4
  slug: airflow-health-info-response
- name: HITLDetailCollection
  property_count: 2
  slug: airflow-hitl-detail-collection
- name: HITLDetailHistory
  property_count: 14
  slug: airflow-hitl-detail-history
- name: HITLDetailResponse
  property_count: 4
  slug: airflow-hitl-detail-response
- name: HITLDetail
  property_count: 14
  slug: airflow-hitl-detail
- name: HITLUser
  property_count: 2
  slug: airflow-hitl-user
- name: HTTPExceptionResponse
  property_count: 1
  slug: airflow-http-exception-response
- name: ImportErrorCollectionResponse
  property_count: 2
  slug: airflow-import-error-collection-response
- name: ImportErrorResponse
  property_count: 5
  slug: airflow-import-error-response
- name: JobCollectionResponse
  property_count: 2
  slug: airflow-job-collection-response
- name: JobResponse
  property_count: 11
  slug: airflow-job-response
- name: JsonValue
  property_count: 0
  slug: airflow-json-value
- name: LastAssetEventResponse
  property_count: 2
  slug: airflow-last-asset-event-response
- name: MaterializeAssetBody
  property_count: 8
  slug: airflow-materialize-asset-body
- name: PatchTaskInstanceBody
  property_count: 6
  slug: airflow-patch-task-instance-body
- name: PluginCollectionResponse
  property_count: 2
  slug: airflow-plugin-collection-response
- name: PluginImportErrorCollectionResponse
  property_count: 2
  slug: airflow-plugin-import-error-collection-response
- name: PluginImportErrorResponse
  property_count: 2
  slug: airflow-plugin-import-error-response
- name: PluginResponse
  property_count: 14
  slug: airflow-plugin-response
- name: PoolBody
  property_count: 5
  slug: airflow-pool-body
- name: PoolCollectionResponse
  property_count: 2
  slug: airflow-pool-collection-response
- name: PoolPatchBody
  property_count: 5
  slug: airflow-pool-patch-body
- name: PoolResponse
  property_count: 11
  slug: airflow-pool-response
- name: ProviderCollectionResponse
  property_count: 2
  slug: airflow-provider-collection-response
- name: ProviderResponse
  property_count: 4
  slug: airflow-provider-response
- name: QueuedEventCollectionResponse
  property_count: 2
  slug: airflow-queued-event-collection-response
- name: QueuedEventResponse
  property_count: 4
  slug: airflow-queued-event-response
- name: ReactAppResponse
  property_count: 7
  slug: airflow-react-app-response
- name: ReprocessBehavior
  property_count: 0
  slug: airflow-reprocess-behavior
- name: SchedulerInfoResponse
  property_count: 2
  slug: airflow-scheduler-info-response
- name: StructuredLogMessage
  property_count: 2
  slug: airflow-structured-log-message
- name: TaskCollectionResponse
  property_count: 2
  slug: airflow-task-collection-response
- name: TaskDependencyCollectionResponse
  property_count: 1
  slug: airflow-task-dependency-collection-response
- name: TaskDependencyResponse
  property_count: 2
  slug: airflow-task-dependency-response
- name: TaskInletAssetReference
  property_count: 4
  slug: airflow-task-inlet-asset-reference
- name: TaskInstanceCollectionResponse
  property_count: 4
  slug: airflow-task-instance-collection-response
- name: TaskInstanceHistoryCollectionResponse
  property_count: 2
  slug: airflow-task-instance-history-collection-response
- name: TaskInstanceHistoryResponse
  property_count: 26
  slug: airflow-task-instance-history-response
- name: TaskInstanceResponse
  property_count: 34
  slug: airflow-task-instance-response
- name: TaskInstanceState
  property_count: 0
  slug: airflow-task-instance-state
- name: TaskInstancesBatchBody
  property_count: 30
  slug: airflow-task-instances-batch-body
- name: TaskInstancesLogResponse
  property_count: 2
  slug: airflow-task-instances-log-response
- name: TaskOutletAssetReference
  property_count: 4
  slug: airflow-task-outlet-asset-reference
- name: TaskResponse
  property_count: 27
  slug: airflow-task-response
- name: TimeDelta
  property_count: 4
  slug: airflow-time-delta
- name: TriggerDAGRunPostBody
  property_count: 8
  slug: airflow-trigger-dag-run-post-body
- name: TriggerResponse
  property_count: 6
  slug: airflow-trigger-response
- name: TriggererInfoResponse
  property_count: 2
  slug: airflow-triggerer-info-response
- name: UpdateHITLDetailPayload
  property_count: 2
  slug: airflow-update-hitl-detail-payload
- name: VariableBody
  property_count: 4
  slug: airflow-variable-body
- name: VariableCollectionResponse
  property_count: 2
  slug: airflow-variable-collection-response
- name: VariableResponse
  property_count: 5
  slug: airflow-variable-response
- name: VersionInfo
  property_count: 2
  slug: airflow-version-info
- name: XComCollectionResponse
  property_count: 2
  slug: airflow-x-com-collection-response
- name: XComCreateBody
  property_count: 3
  slug: airflow-x-com-create-body
- name: XComResponseNative
  property_count: 11
  slug: airflow-x-com-response-native
- name: XComResponse
  property_count: 10
  slug: airflow-x-com-response
- name: XComResponseString
  property_count: 11
  slug: airflow-x-com-response-string
- name: XComUpdateBody
  property_count: 2
  slug: airflow-x-com-update-body
json_structures:
- name: Airflow App Builder Menu Item Response Structure
  property_count: 3
  slug: airflow-app-builder-menu-item-response-structure
- name: Airflow App Builder View Response Structure
  property_count: 4
  slug: airflow-app-builder-view-response-structure
- name: Airflow Asset Alias Collection Response Structure
  property_count: 2
  slug: airflow-asset-alias-collection-response-structure
- name: Airflow Asset Alias Response Structure
  property_count: 3
  slug: airflow-asset-alias-response-structure
- name: Airflow Asset Collection Response Structure
  property_count: 2
  slug: airflow-asset-collection-response-structure
- name: Airflow Asset Event Collection Response Structure
  property_count: 2
  slug: airflow-asset-event-collection-response-structure
- name: Airflow Asset Event Response Structure
  property_count: 13
  slug: airflow-asset-event-response-structure
- name: Airflow Asset Response Structure
  property_count: 13
  slug: airflow-asset-response-structure
- name: Airflow Asset Watcher Response Structure
  property_count: 3
  slug: airflow-asset-watcher-response-structure
- name: Airflow Backfill Collection Response Structure
  property_count: 2
  slug: airflow-backfill-collection-response-structure
- name: Airflow Backfill Post Body Structure
  property_count: 8
  slug: airflow-backfill-post-body-structure
- name: Airflow Backfill Response Structure
  property_count: 12
  slug: airflow-backfill-response-structure
- name: Airflow Base Info Response Structure
  property_count: 1
  slug: airflow-base-info-response-structure
- name: Airflow Bulk Action Not On Existence Structure
  property_count: 0
  slug: airflow-bulk-action-not-on-existence-structure
- name: Airflow Bulk Action On Existence Structure
  property_count: 0
  slug: airflow-bulk-action-on-existence-structure
- name: Airflow Bulk Action Response Structure
  property_count: 2
  slug: airflow-bulk-action-response-structure
- name: Airflow Bulk Body_ Bulk Task Instance Body_ Structure
  property_count: 1
  slug: airflow-bulk-body_-bulk-task-instance-body_-structure
- name: Airflow Bulk Body_ Connection Body_ Structure
  property_count: 1
  slug: airflow-bulk-body_-connection-body_-structure
- name: Airflow Bulk Body_ Pool Body_ Structure
  property_count: 1
  slug: airflow-bulk-body_-pool-body_-structure
- name: Airflow Bulk Body_ Variable Body_ Structure
  property_count: 1
  slug: airflow-bulk-body_-variable-body_-structure
- name: Airflow Bulk Create Action_ Bulk Task Instance Body_ Structure
  property_count: 3
  slug: airflow-bulk-create-action_-bulk-task-instance-body_-structure
- name: Airflow Bulk Create Action_ Connection Body_ Structure
  property_count: 3
  slug: airflow-bulk-create-action_-connection-body_-structure
- name: Airflow Bulk Create Action_ Pool Body_ Structure
  property_count: 3
  slug: airflow-bulk-create-action_-pool-body_-structure
- name: Airflow Bulk Create Action_ Variable Body_ Structure
  property_count: 3
  slug: airflow-bulk-create-action_-variable-body_-structure
- name: Airflow Bulk Delete Action_ Bulk Task Instance Body_ Structure
  property_count: 3
  slug: airflow-bulk-delete-action_-bulk-task-instance-body_-structure
- name: Airflow Bulk Delete Action_ Connection Body_ Structure
  property_count: 3
  slug: airflow-bulk-delete-action_-connection-body_-structure
- name: Airflow Bulk Delete Action_ Pool Body_ Structure
  property_count: 3
  slug: airflow-bulk-delete-action_-pool-body_-structure
- name: Airflow Bulk Delete Action_ Variable Body_ Structure
  property_count: 3
  slug: airflow-bulk-delete-action_-variable-body_-structure
- name: Airflow Bulk Response Structure
  property_count: 3
  slug: airflow-bulk-response-structure
- name: Airflow Bulk Task Instance Body Structure
  property_count: 10
  slug: airflow-bulk-task-instance-body-structure
- name: Airflow Bulk Update Action_ Bulk Task Instance Body_ Structure
  property_count: 4
  slug: airflow-bulk-update-action_-bulk-task-instance-body_-structure
- name: Airflow Bulk Update Action_ Connection Body_ Structure
  property_count: 4
  slug: airflow-bulk-update-action_-connection-body_-structure
- name: Airflow Bulk Update Action_ Pool Body_ Structure
  property_count: 4
  slug: airflow-bulk-update-action_-pool-body_-structure
- name: Airflow Bulk Update Action_ Variable Body_ Structure
  property_count: 4
  slug: airflow-bulk-update-action_-variable-body_-structure
- name: Airflow Clear Task Instances Body Structure
  property_count: 15
  slug: airflow-clear-task-instances-body-structure
- name: Airflow Config Option Structure
  property_count: 2
  slug: airflow-config-option-structure
- name: Airflow Config Section Structure
  property_count: 2
  slug: airflow-config-section-structure
- name: Airflow Config Structure
  property_count: 1
  slug: airflow-config-structure
- name: Airflow Connection Body Structure
  property_count: 10
  slug: airflow-connection-body-structure
- name: Airflow Connection Collection Response Structure
  property_count: 2
  slug: airflow-connection-collection-response-structure
- name: Airflow Connection Response Structure
  property_count: 10
  slug: airflow-connection-response-structure
- name: Airflow Connection Test Response Structure
  property_count: 2
  slug: airflow-connection-test-response-structure
- name: Airflow Create Asset Events Body Structure
  property_count: 3
  slug: airflow-create-asset-events-body-structure
- name: Airflow Dag Collection Response Structure
  property_count: 2
  slug: airflow-dag-collection-response-structure
- name: Airflow Dag Details Response Structure
  property_count: 48
  slug: airflow-dag-details-response-structure
- name: Airflow Dag Patch Body Structure
  property_count: 1
  slug: airflow-dag-patch-body-structure
- name: Airflow Dag Processor Info Response Structure
  property_count: 2
  slug: airflow-dag-processor-info-response-structure
- name: Airflow Dag Response Structure
  property_count: 30
  slug: airflow-dag-response-structure
- name: Airflow Dag Run Asset Reference Structure
  property_count: 9
  slug: airflow-dag-run-asset-reference-structure
- name: Airflow Dag Run Clear Body Structure
  property_count: 3
  slug: airflow-dag-run-clear-body-structure
- name: Airflow Dag Run Collection Response Structure
  property_count: 2
  slug: airflow-dag-run-collection-response-structure
- name: Airflow Dag Run Patch Body Structure
  property_count: 2
  slug: airflow-dag-run-patch-body-structure
- name: Airflow Dag Run Patch States Structure
  property_count: 0
  slug: airflow-dag-run-patch-states-structure
- name: Airflow Dag Run Response Structure
  property_count: 21
  slug: airflow-dag-run-response-structure
- name: Airflow Dag Run State Structure
  property_count: 0
  slug: airflow-dag-run-state-structure
- name: Airflow Dag Run Triggered By Type Structure
  property_count: 0
  slug: airflow-dag-run-triggered-by-type-structure
- name: Airflow Dag Run Type Structure
  property_count: 0
  slug: airflow-dag-run-type-structure
- name: Airflow Dag Runs Batch Body Structure
  property_count: 26
  slug: airflow-dag-runs-batch-body-structure
- name: Airflow Dag Schedule Asset Reference Structure
  property_count: 3
  slug: airflow-dag-schedule-asset-reference-structure
- name: Airflow Dag Source Response Structure
  property_count: 4
  slug: airflow-dag-source-response-structure
- name: Airflow Dag Stats Collection Response Structure
  property_count: 2
  slug: airflow-dag-stats-collection-response-structure
- name: Airflow Dag Stats Response Structure
  property_count: 3
  slug: airflow-dag-stats-response-structure
- name: Airflow Dag Stats State Response Structure
  property_count: 2
  slug: airflow-dag-stats-state-response-structure
- name: Airflow Dag Tag Collection Response Structure
  property_count: 2
  slug: airflow-dag-tag-collection-response-structure
- name: Airflow Dag Tag Response Structure
  property_count: 3
  slug: airflow-dag-tag-response-structure
- name: Airflow Dag Version Collection Response Structure
  property_count: 2
  slug: airflow-dag-version-collection-response-structure
- name: Airflow Dag Version Response Structure
  property_count: 8
  slug: airflow-dag-version-response-structure
- name: Airflow Dag Warning Collection Response Structure
  property_count: 2
  slug: airflow-dag-warning-collection-response-structure
- name: Airflow Dag Warning Response Structure
  property_count: 5
  slug: airflow-dag-warning-response-structure
- name: Airflow Dag Warning Type Structure
  property_count: 0
  slug: airflow-dag-warning-type-structure
- name: Airflow Dry Run Backfill Collection Response Structure
  property_count: 2
  slug: airflow-dry-run-backfill-collection-response-structure
- name: Airflow Dry Run Backfill Response Structure
  property_count: 3
  slug: airflow-dry-run-backfill-response-structure
- name: Airflow Event Log Collection Response Structure
  property_count: 2
  slug: airflow-event-log-collection-response-structure
- name: Airflow Event Log Response Structure
  property_count: 13
  slug: airflow-event-log-response-structure
- name: Airflow External Log Url Response Structure
  property_count: 1
  slug: airflow-external-log-url-response-structure
- name: Airflow External View Response Structure
  property_count: 7
  slug: airflow-external-view-response-structure
- name: Airflow Extra Link Collection Response Structure
  property_count: 2
  slug: airflow-extra-link-collection-response-structure
- name: Airflow Fast Api App Response Structure
  property_count: 3
  slug: airflow-fast-api-app-response-structure
- name: Airflow Fast Api Root Middleware Response Structure
  property_count: 2
  slug: airflow-fast-api-root-middleware-response-structure
- name: Airflow Health Info Response Structure
  property_count: 4
  slug: airflow-health-info-response-structure
- name: Airflow Hitl Detail Collection Structure
  property_count: 2
  slug: airflow-hitl-detail-collection-structure
- name: Airflow Hitl Detail History Structure
  property_count: 14
  slug: airflow-hitl-detail-history-structure
- name: Airflow Hitl Detail Response Structure
  property_count: 4
  slug: airflow-hitl-detail-response-structure
- name: Airflow Hitl Detail Structure
  property_count: 14
  slug: airflow-hitl-detail-structure
- name: Airflow Hitl User Structure
  property_count: 2
  slug: airflow-hitl-user-structure
- name: Airflow Http Exception Response Structure
  property_count: 1
  slug: airflow-http-exception-response-structure
- name: Airflow Import Error Collection Response Structure
  property_count: 2
  slug: airflow-import-error-collection-response-structure
- name: Airflow Import Error Response Structure
  property_count: 5
  slug: airflow-import-error-response-structure
- name: Airflow Job Collection Response Structure
  property_count: 2
  slug: airflow-job-collection-response-structure
- name: Airflow Job Response Structure
  property_count: 11
  slug: airflow-job-response-structure
- name: Airflow Json Value Structure
  property_count: 0
  slug: airflow-json-value-structure
- name: Airflow Last Asset Event Response Structure
  property_count: 2
  slug: airflow-last-asset-event-response-structure
- name: Airflow Materialize Asset Body Structure
  property_count: 8
  slug: airflow-materialize-asset-body-structure
- name: Airflow Patch Task Instance Body Structure
  property_count: 6
  slug: airflow-patch-task-instance-body-structure
- name: Airflow Plugin Collection Response Structure
  property_count: 2
  slug: airflow-plugin-collection-response-structure
- name: Airflow Plugin Import Error Collection Response Structure
  property_count: 2
  slug: airflow-plugin-import-error-collection-response-structure
- name: Airflow Plugin Import Error Response Structure
  property_count: 2
  slug: airflow-plugin-import-error-response-structure
- name: Airflow Plugin Response Structure
  property_count: 14
  slug: airflow-plugin-response-structure
- name: Airflow Pool Body Structure
  property_count: 5
  slug: airflow-pool-body-structure
- name: Airflow Pool Collection Response Structure
  property_count: 2
  slug: airflow-pool-collection-response-structure
- name: Airflow Pool Patch Body Structure
  property_count: 5
  slug: airflow-pool-patch-body-structure
- name: Airflow Pool Response Structure
  property_count: 11
  slug: airflow-pool-response-structure
- name: Airflow Provider Collection Response Structure
  property_count: 2
  slug: airflow-provider-collection-response-structure
- name: Airflow Provider Response Structure
  property_count: 4
  slug: airflow-provider-response-structure
- name: Airflow Queued Event Collection Response Structure
  property_count: 2
  slug: airflow-queued-event-collection-response-structure
- name: Airflow Queued Event Response Structure
  property_count: 4
  slug: airflow-queued-event-response-structure
- name: Airflow React App Response Structure
  property_count: 7
  slug: airflow-react-app-response-structure
- name: Airflow Reprocess Behavior Structure
  property_count: 0
  slug: airflow-reprocess-behavior-structure
- name: Airflow Scheduler Info Response Structure
  property_count: 2
  slug: airflow-scheduler-info-response-structure
- name: Airflow Structured Log Message Structure
  property_count: 2
  slug: airflow-structured-log-message-structure
- name: Airflow Task Collection Response Structure
  property_count: 2
  slug: airflow-task-collection-response-structure
- name: Airflow Task Dependency Collection Response Structure
  property_count: 1
  slug: airflow-task-dependency-collection-response-structure
- name: Airflow Task Dependency Response Structure
  property_count: 2
  slug: airflow-task-dependency-response-structure
- name: Airflow Task Inlet Asset Reference Structure
  property_count: 4
  slug: airflow-task-inlet-asset-reference-structure
- name: Airflow Task Instance Collection Response Structure
  property_count: 4
  slug: airflow-task-instance-collection-response-structure
- name: Airflow Task Instance History Collection Response Structure
  property_count: 2
  slug: airflow-task-instance-history-collection-response-structure
- name: Airflow Task Instance History Response Structure
  property_count: 26
  slug: airflow-task-instance-history-response-structure
- name: Airflow Task Instance Response Structure
  property_count: 34
  slug: airflow-task-instance-response-structure
- name: Airflow Task Instance State Structure
  property_count: 0
  slug: airflow-task-instance-state-structure
- name: Airflow Task Instances Batch Body Structure
  property_count: 30
  slug: airflow-task-instances-batch-body-structure
- name: Airflow Task Instances Log Response Structure
  property_count: 2
  slug: airflow-task-instances-log-response-structure
- name: Airflow Task Outlet Asset Reference Structure
  property_count: 4
  slug: airflow-task-outlet-asset-reference-structure
- name: Airflow Task Response Structure
  property_count: 27
  slug: airflow-task-response-structure
- name: Airflow Time Delta Structure
  property_count: 4
  slug: airflow-time-delta-structure
- name: Airflow Trigger Dag Run Post Body Structure
  property_count: 8
  slug: airflow-trigger-dag-run-post-body-structure
- name: Airflow Trigger Response Structure
  property_count: 6
  slug: airflow-trigger-response-structure
- name: Airflow Triggerer Info Response Structure
  property_count: 2
  slug: airflow-triggerer-info-response-structure
- name: Airflow Update Hitl Detail Payload Structure
  property_count: 2
  slug: airflow-update-hitl-detail-payload-structure
- name: Airflow Variable Body Structure
  property_count: 4
  slug: airflow-variable-body-structure
- name: Airflow Variable Collection Response Structure
  property_count: 2
  slug: airflow-variable-collection-response-structure
- name: Airflow Variable Response Structure
  property_count: 5
  slug: airflow-variable-response-structure
- name: Airflow Version Info Structure
  property_count: 2
  slug: airflow-version-info-structure
- name: Airflow X Com Collection Response Structure
  property_count: 2
  slug: airflow-x-com-collection-response-structure
- name: Airflow X Com Create Body Structure
  property_count: 3
  slug: airflow-x-com-create-body-structure
- name: Airflow X Com Response Native Structure
  property_count: 11
  slug: airflow-x-com-response-native-structure
- name: Airflow X Com Response String Structure
  property_count: 11
  slug: airflow-x-com-response-string-structure
- name: Airflow X Com Response Structure
  property_count: 10
  slug: airflow-x-com-response-structure
- name: Airflow X Com Update Body Structure
  property_count: 2
  slug: airflow-x-com-update-body-structure
jsonld:
- class_count: 128
  name: Airflow Context
  property_count: 304
  slug: airflow-context
layout: provider
modified: '2026-05-30'
name: Apache Airflow
nav: Providers
network: true
overview: 'Apache Airflow publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Asset API, Backfill API, Config API, and 23 more. Tagged areas include Workflow Orchestration, Data Pipeline, Open Source, Apache, and DAG.


  The Apache Airflow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Airflow''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, Stack Overflow tag, changelog, and 12 more developer resources.'
plans:
- name: Airflow Plans Pricing
  plan_count: 3
  slug: airflow-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Airflow Rate Limits
  slug: airflow-rate-limits
rules:
- name: Apache Airflow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airflow-jsonschema-spectral-rules
- name: Apache Airflow API Rules
  rule_count: 33
  severity_counts:
    error: 8
    hint: 0
    info: 9
    warn: 16
  slug: airflow-spectral-rules
scopes:
- name: Airflow Scopes
  scope_count: 0
  slug: airflow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 57.2
  delta: 2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.0
    developer_ergonomics: 39.1
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 55.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/screenshots/airflow-2026-06-20T171427.png
security:
- kind: authentication
  name: Airflow Authentication
  slug: airflow-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Airflow Domain Security
  slug: airflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airflow Vulnerability Disclosure
  slug: airflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: airflow
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
use_cases:
- description: Schedule and monitor extract, transform, load data pipelines.
  name: ETL Pipeline Orchestration
- description: Orchestrate machine learning training, evaluation, and deployment workflows.
  name: ML Pipeline Management
- description: Schedule data validation and quality check jobs.
  name: Data Quality Checks
- description: Automate periodic report generation and distribution.
  name: Report Generation
- description: Coordinate calls to multiple APIs in complex workflows.
  name: API Orchestration
- description: Schedule database maintenance, migrations, and backup jobs.
  name: Database Operations
website: https://airflow.apache.org
---
