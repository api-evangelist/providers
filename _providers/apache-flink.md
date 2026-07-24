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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 2
  name: Apache Flink Agentic Access
  operation_count: 69
  slug: apache-flink-agentic-access
  summary_line: 69 operations · 14 acting · 2 human-in-the-loop
api_count: 10
apis:
- description: Monitoring REST API for accessing job metrics, checkpoints, and cluster statistics for Apache Flink deployments.
  name: Apache Flink Monitoring API
  slug: apache-flink-monitoring
- description: The Cluster API from Apache Flink — 1 operation(s) for cluster.
  name: Apache Flink Cluster API
  slug: apache-flink-cluster-api
- description: The Config API from Apache Flink — 1 operation(s) for config.
  name: Apache Flink Config API
  slug: apache-flink-config-api
- description: The Datasets API from Apache Flink — 3 operation(s) for datasets.
  name: Apache Flink Datasets API
  slug: apache-flink-datasets-api
- description: The Jars API from Apache Flink — 5 operation(s) for jars.
  name: Apache Flink Jars API
  slug: apache-flink-jars-api
- description: The Jobmanager API from Apache Flink — 5 operation(s) for jobmanager.
  name: Apache Flink Jobmanager API
  slug: apache-flink-jobmanager-api
- description: The Jobs API from Apache Flink — 42 operation(s) for jobs.
  name: Apache Flink Jobs API
  slug: apache-flink-jobs-api
- description: The Overview API from Apache Flink — 1 operation(s) for overview.
  name: Apache Flink Overview API
  slug: apache-flink-overview-api
- description: The Savepoint Disposal API from Apache Flink — 2 operation(s) for savepoint disposal.
  name: Apache Flink Savepoint Disposal API
  slug: apache-flink-savepoint-disposal-api
- description: The Taskmanagers API from Apache Flink — 6 operation(s) for taskmanagers.
  name: Apache Flink Taskmanagers API
  slug: apache-flink-taskmanagers-api
artifact_total: 436
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-flink-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-flink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-flink-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/local_installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/flink
- group: company
  title: ''
  type: Blog
  url: https://flink.apache.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://flink.apache.org/community.html
- group: learn
  title: ''
  type: Training
  url: https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/overview/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apache-flink
- group: other
  title: ''
  type: X
  url: https://twitter.com/apacheflink
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-flink-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-flink-vocabulary.yaml
created: '2024-01-01'
description: Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. It provides a REST API for job management, cluster operations, metrics collection, and checkpoint management for real-time streaming and batch processing workloads.
examples:
- key_count: 0
  name: Flink Rest Aggregated Metrics Response Body Example
  slug: flink-rest-aggregated-metrics-response-body-example
- key_count: 2
  name: Flink Rest Aggregated Task Details Info Example
  slug: flink-rest-aggregated-task-details-info-example
- key_count: 0
  name: Flink Rest Aggregation Mode Example
  slug: flink-rest-aggregation-mode-example
- key_count: 0
  name: Flink Rest Application Status Example
  slug: flink-rest-application-status-example
- key_count: 1
  name: Flink Rest Asynchronous Operation Info Example
  slug: flink-rest-asynchronous-operation-info-example
- key_count: 2
  name: Flink Rest Asynchronous Operation Result Example
  slug: flink-rest-asynchronous-operation-result-example
- key_count: 4
  name: Flink Rest Checkpoint Alignment Example
  slug: flink-rest-checkpoint-alignment-example
- key_count: 4
  name: Flink Rest Checkpoint Alignment Summary Example
  slug: flink-rest-checkpoint-alignment-summary-example
- key_count: 15
  name: Flink Rest Checkpoint Config Info Example
  slug: flink-rest-checkpoint-config-info-example
- key_count: 2
  name: Flink Rest Checkpoint Duration Example
  slug: flink-rest-checkpoint-duration-example
- key_count: 2
  name: Flink Rest Checkpoint Duration Summary Example
  slug: flink-rest-checkpoint-duration-summary-example
- key_count: 2
  name: Flink Rest Checkpoint Info Example
  slug: flink-rest-checkpoint-info-example
- key_count: 17
  name: Flink Rest Checkpoint Statistics Example
  slug: flink-rest-checkpoint-statistics-example
- key_count: 6
  name: Flink Rest Checkpoint Statistics Summary Example
  slug: flink-rest-checkpoint-statistics-summary-example
- key_count: 0
  name: Flink Rest Checkpoint Stats Status Example
  slug: flink-rest-checkpoint-stats-status-example
- key_count: 2
  name: Flink Rest Checkpoint Trigger Request Body Example
  slug: flink-rest-checkpoint-trigger-request-body-example
- key_count: 0
  name: Flink Rest Checkpoint Type Example
  slug: flink-rest-checkpoint-type-example
- key_count: 4
  name: Flink Rest Checkpointing Statistics Example
  slug: flink-rest-checkpointing-statistics-example
- key_count: 2
  name: Flink Rest Cluster Data Set Entry Example
  slug: flink-rest-cluster-data-set-entry-example
- key_count: 1
  name: Flink Rest Cluster Data Set List Response Body Example
  slug: flink-rest-cluster-data-set-list-response-body-example
- key_count: 11
  name: Flink Rest Cluster Overview With Version Example
  slug: flink-rest-cluster-overview-with-version-example
- key_count: 0
  name: Flink Rest Completed Checkpoint Statistics Example
  slug: flink-rest-completed-checkpoint-statistics-example
- key_count: 0
  name: Flink Rest Completed Subtask Checkpoint Statistics Example
  slug: flink-rest-completed-subtask-checkpoint-statistics-example
- key_count: 2
  name: Flink Rest Configuration Info Entry Example
  slug: flink-rest-configuration-info-entry-example
- key_count: 0
  name: Flink Rest Configuration Info Example
  slug: flink-rest-configuration-info-example
- key_count: 5
  name: Flink Rest Counts Example
  slug: flink-rest-counts-example
- key_count: 6
  name: Flink Rest Dashboard Configuration Example
  slug: flink-rest-dashboard-configuration-example
- key_count: 2
  name: Flink Rest Environment Info Example
  slug: flink-rest-environment-info-example
- key_count: 7
  name: Flink Rest Exception Info Example
  slug: flink-rest-exception-info-example
- key_count: 4
  name: Flink Rest Execution Config Info Example
  slug: flink-rest-execution-config-info-example
- key_count: 0
  name: Flink Rest Execution State Example
  slug: flink-rest-execution-state-example
- key_count: 2
  name: Flink Rest Externalized Checkpoint Info Example
  slug: flink-rest-externalized-checkpoint-info-example
- key_count: 0
  name: Flink Rest Failed Checkpoint Statistics Example
  slug: flink-rest-failed-checkpoint-statistics-example
- key_count: 2
  name: Flink Rest Failure Label Example
  slug: flink-rest-failure-label-example
- key_count: 4
  name: Flink Rest Features Example
  slug: flink-rest-features-example
- key_count: 3
  name: Flink Rest Garbage Collector Info Example
  slug: flink-rest-garbage-collector-info-example
- key_count: 4
  name: Flink Rest Hardware Description Example
  slug: flink-rest-hardware-description-example
- key_count: 0
  name: Flink Rest Id Example
  slug: flink-rest-id-example
- key_count: 0
  name: Flink Rest Intermediate Data Set Id Example
  slug: flink-rest-intermediate-data-set-id-example
- key_count: 11
  name: Flink Rest Io Metrics Info Example
  slug: flink-rest-io-metrics-info-example
- key_count: 2
  name: Flink Rest Jar Entry Info Example
  slug: flink-rest-jar-entry-info-example
- key_count: 4
  name: Flink Rest Jar File Info Example
  slug: flink-rest-jar-file-info-example
- key_count: 2
  name: Flink Rest Jar List Info Example
  slug: flink-rest-jar-list-info-example
- key_count: 5
  name: Flink Rest Jar Plan Request Body Example
  slug: flink-rest-jar-plan-request-body-example
- key_count: 9
  name: Flink Rest Jar Run Request Body Example
  slug: flink-rest-jar-run-request-body-example
- key_count: 1
  name: Flink Rest Jar Run Response Body Example
  slug: flink-rest-jar-run-response-body-example
- key_count: 2
  name: Flink Rest Jar Upload Response Body Example
  slug: flink-rest-jar-upload-response-body-example
- key_count: 0
  name: Flink Rest Job Accumulator Example
  slug: flink-rest-job-accumulator-example
- key_count: 3
  name: Flink Rest Job Accumulators Info Example
  slug: flink-rest-job-accumulators-info-example
- key_count: 1
  name: Flink Rest Job Client Heartbeat Request Body Example
  slug: flink-rest-job-client-heartbeat-request-body-example
- key_count: 3
  name: Flink Rest Job Config Info Example
  slug: flink-rest-job-config-info-example
- key_count: 9
  name: Flink Rest Job Details Example
  slug: flink-rest-job-details-example
- key_count: 16
  name: Flink Rest Job Details Info Example
  slug: flink-rest-job-details-info-example
- key_count: 11
  name: Flink Rest Job Details Vertex Info Example
  slug: flink-rest-job-details-vertex-info-example
- key_count: 2
  name: Flink Rest Job Exception History Example
  slug: flink-rest-job-exception-history-example
- key_count: 1
  name: Flink Rest Job Exceptions Info With History Example
  slug: flink-rest-job-exceptions-info-with-history-example
- key_count: 2
  name: Flink Rest Job Execution Result Response Body Example
  slug: flink-rest-job-execution-result-response-body-example
- key_count: 0
  name: Flink Rest Job Id Example
  slug: flink-rest-job-id-example
- key_count: 2
  name: Flink Rest Job Id With Status Example
  slug: flink-rest-job-id-with-status-example
- key_count: 1
  name: Flink Rest Job Ids With Status Overview Example
  slug: flink-rest-job-ids-with-status-overview-example
- key_count: 1
  name: Flink Rest Job Plan Info Example
  slug: flink-rest-job-plan-info-example
- key_count: 0
  name: Flink Rest Job Resource Requirements Body Example
  slug: flink-rest-job-resource-requirements-body-example
- key_count: 6
  name: Flink Rest Job Result Example
  slug: flink-rest-job-result-example
- key_count: 0
  name: Flink Rest Job Status Example
  slug: flink-rest-job-status-example
- key_count: 1
  name: Flink Rest Job Status Info Example
  slug: flink-rest-job-status-info-example
- key_count: 0
  name: Flink Rest Job Type Example
  slug: flink-rest-job-type-example
- key_count: 2
  name: Flink Rest Job Vertex Accumulators Info Example
  slug: flink-rest-job-vertex-accumulators-info-example
- key_count: 4
  name: Flink Rest Job Vertex Back Pressure Info Example
  slug: flink-rest-job-vertex-back-pressure-info-example
- key_count: 7
  name: Flink Rest Job Vertex Details Info Example
  slug: flink-rest-job-vertex-details-info-example
- key_count: 0
  name: Flink Rest Job Vertex Id Example
  slug: flink-rest-job-vertex-id-example
- key_count: 1
  name: Flink Rest Job Vertex Resource Requirements Example
  slug: flink-rest-job-vertex-resource-requirements-example
- key_count: 9
  name: Flink Rest Job Vertex Task Manager Info Example
  slug: flink-rest-job-vertex-task-manager-info-example
- key_count: 4
  name: Flink Rest Job Vertex Task Managers Info Example
  slug: flink-rest-job-vertex-task-managers-info-example
- key_count: 3
  name: Flink Rest Jvm Info Example
  slug: flink-rest-jvm-info-example
- key_count: 4
  name: Flink Rest Latest Checkpoints Example
  slug: flink-rest-latest-checkpoints-example
- key_count: 3
  name: Flink Rest Log Info Example
  slug: flink-rest-log-info-example
- key_count: 1
  name: Flink Rest Log List Info Example
  slug: flink-rest-log-list-info-example
- key_count: 1
  name: Flink Rest Log Url Response Example
  slug: flink-rest-log-url-response-example
- key_count: 1
  name: Flink Rest Metric Collection Response Body Example
  slug: flink-rest-metric-collection-response-body-example
- key_count: 2
  name: Flink Rest Metric Example
  slug: flink-rest-metric-example
- key_count: 1
  name: Flink Rest Multiple Jobs Details Example
  slug: flink-rest-multiple-jobs-details-example
- key_count: 3
  name: Flink Rest Node Example
  slug: flink-rest-node-example
- key_count: 2
  name: Flink Rest Parallelism Example
  slug: flink-rest-parallelism-example
- key_count: 0
  name: Flink Rest Pending Checkpoint Statistics Example
  slug: flink-rest-pending-checkpoint-statistics-example
- key_count: 0
  name: Flink Rest Pending Subtask Checkpoint Statistics Example
  slug: flink-rest-pending-subtask-checkpoint-statistics-example
- key_count: 0
  name: Flink Rest Processing Mode Example
  slug: flink-rest-processing-mode-example
- key_count: 1
  name: Flink Rest Queue Status Example
  slug: flink-rest-queue-status-example
- key_count: 0
  name: Flink Rest Raw Json Example
  slug: flink-rest-raw-json-example
- key_count: 0
  name: Flink Rest Recovery Claim Mode Example
  slug: flink-rest-recovery-claim-mode-example
- key_count: 0
  name: Flink Rest Resource Id Example
  slug: flink-rest-resource-id-example
- key_count: 6
  name: Flink Rest Resource Profile Info Example
  slug: flink-rest-resource-profile-info-example
- key_count: 0
  name: Flink Rest Rest Api Checkpoint Type Example
  slug: flink-rest-rest-api-checkpoint-type-example
- key_count: 4
  name: Flink Rest Restored Checkpoint Statistics Example
  slug: flink-rest-restored-checkpoint-statistics-example
- key_count: 8
  name: Flink Rest Root Exception Info Example
  slug: flink-rest-root-exception-info-example
- key_count: 1
  name: Flink Rest Savepoint Disposal Request Example
  slug: flink-rest-savepoint-disposal-request-example
- key_count: 0
  name: Flink Rest Savepoint Format Type Example
  slug: flink-rest-savepoint-format-type-example
- key_count: 2
  name: Flink Rest Savepoint Info Example
  slug: flink-rest-savepoint-info-example
- key_count: 4
  name: Flink Rest Savepoint Trigger Request Body Example
  slug: flink-rest-savepoint-trigger-request-body-example
- key_count: 1
  name: Flink Rest Serialized Throwable Example
  slug: flink-rest-serialized-throwable-example
- key_count: 1
  name: Flink Rest Serialized Value Optional Failure Object Example
  slug: flink-rest-serialized-value-optional-failure-object-example
- key_count: 2
  name: Flink Rest Slot Info Example
  slug: flink-rest-slot-info-example
- key_count: 3
  name: Flink Rest Slot Sharing Group Id Example
  slug: flink-rest-slot-sharing-group-id-example
- key_count: 8
  name: Flink Rest Stats Summary Dto Example
  slug: flink-rest-stats-summary-dto-example
- key_count: 4
  name: Flink Rest Stop With Savepoint Request Body Example
  slug: flink-rest-stop-with-savepoint-request-body-example
- key_count: 4
  name: Flink Rest Subtask Accumulators Info Example
  slug: flink-rest-subtask-accumulators-info-example
- key_count: 7
  name: Flink Rest Subtask Back Pressure Info Example
  slug: flink-rest-subtask-back-pressure-info-example
- key_count: 3
  name: Flink Rest Subtask Checkpoint Statistics Example
  slug: flink-rest-subtask-checkpoint-statistics-example
- key_count: 4
  name: Flink Rest Subtask Execution Attempt Accumulators Info Example
  slug: flink-rest-subtask-execution-attempt-accumulators-info-example
- key_count: 11
  name: Flink Rest Subtask Execution Attempt Details Info Example
  slug: flink-rest-subtask-execution-attempt-details-info-example
- key_count: 4
  name: Flink Rest Subtask Time Info Example
  slug: flink-rest-subtask-time-info-example
- key_count: 3
  name: Flink Rest Subtasks All Accumulators Info Example
  slug: flink-rest-subtasks-all-accumulators-info-example
- key_count: 4
  name: Flink Rest Subtasks Times Info Example
  slug: flink-rest-subtasks-times-info-example
- key_count: 11
  name: Flink Rest Task Checkpoint Statistics Example
  slug: flink-rest-task-checkpoint-statistics-example
- key_count: 13
  name: Flink Rest Task Checkpoint Statistics With Subtask Details Example
  slug: flink-rest-task-checkpoint-statistics-with-subtask-details-example
- key_count: 6
  name: Flink Rest Task Checkpoint Statistics With Subtask Details Summary Example
  slug: flink-rest-task-checkpoint-statistics-with-subtask-details-summary-example
- key_count: 10
  name: Flink Rest Task Executor Memory Configuration Example
  slug: flink-rest-task-executor-memory-configuration-example
- key_count: 14
  name: Flink Rest Task Manager Details Info Example
  slug: flink-rest-task-manager-details-info-example
- key_count: 12
  name: Flink Rest Task Manager Info Example
  slug: flink-rest-task-manager-info-example
- key_count: 19
  name: Flink Rest Task Manager Metrics Info Example
  slug: flink-rest-task-manager-metrics-info-example
- key_count: 1
  name: Flink Rest Task Managers Info Example
  slug: flink-rest-task-managers-info-example
- key_count: 0
  name: Flink Rest Termination Mode Example
  slug: flink-rest-termination-mode-example
- key_count: 1
  name: Flink Rest Thread Dump Info Example
  slug: flink-rest-thread-dump-info-example
- key_count: 2
  name: Flink Rest Thread Info Example
  slug: flink-rest-thread-info-example
- key_count: 0
  name: Flink Rest Thread States Example
  slug: flink-rest-thread-states-example
- key_count: 0
  name: Flink Rest Trigger Id Example
  slug: flink-rest-trigger-id-example
- key_count: 1
  name: Flink Rest Trigger Response Example
  slug: flink-rest-trigger-response-example
- key_count: 0
  name: Flink Rest Upload Status Example
  slug: flink-rest-upload-status-example
- key_count: 3
  name: Flink Rest User Accumulator Example
  slug: flink-rest-user-accumulator-example
- key_count: 3
  name: Flink Rest User Task Accumulator Example
  slug: flink-rest-user-task-accumulator-example
- key_count: 0
  name: Flink Rest Vertex Back Pressure Level Example
  slug: flink-rest-vertex-back-pressure-level-example
- key_count: 0
  name: Flink Rest Vertex Back Pressure Status Example
  slug: flink-rest-vertex-back-pressure-status-example
- key_count: 2
  name: Flink Rest Vertex Flame Graph Example
  slug: flink-rest-vertex-flame-graph-example
features:
- description: Single engine for both unbounded stream processing and bounded batch workloads with a unified API.
  name: Unified Stream and Batch Processing
- description: Rich stateful processing with managed state backends (RocksDB, heap), exactly-once guarantees, and state versioning.
  name: Stateful Computations
- description: End-to-end exactly-once processing guarantees with distributed snapshots and transactional sinks.
  name: Exactly-Once Semantics
- description: Native event-time support with watermarks for out-of-order event handling in streaming workloads.
  name: Event Time Processing
- description: Automatic fault-tolerance via checkpointing and manual savepoints for job migration and upgrades.
  name: Checkpointing and Savepoints
- description: JobManager HA via ZooKeeper or Kubernetes for zero-downtime cluster operations.
  name: High Availability
- description: Horizontally scalable TaskManagers with fine-grained resource management and dynamic slot allocation.
  name: Scalable Architecture
- description: Comprehensive REST API for job submission, monitoring, metrics collection, and cluster administration.
  name: REST API Management
- description: Declarative SQL and Table API for streaming analytics with connector ecosystem support.
  name: SQL and Table API
finops:
- name: Apache Flink Finops
  service_category: API
  slug: apache-flink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-flink.png
integrations:
- description: Kafka source and sink connectors for high-throughput event streaming ingestion and output.
  name: Apache Kafka
- description: HDFS integration for batch data reading and writing in distributed storage.
  name: Apache Hadoop / HDFS
- description: Hive catalog integration and batch SQL queries over Hive tables.
  name: Apache Hive
- description: Native Kubernetes deployment with FlinkDeployment CRD and the Flink Kubernetes Operator.
  name: Kubernetes
- description: Iceberg table format integration for lakehouse workloads with ACID guarantees.
  name: Apache Iceberg
- description: Elasticsearch sink connector for real-time search index updates from Flink jobs.
  name: Elasticsearch
- description: Kinesis source and sink connectors for AWS-native streaming pipelines.
  name: Amazon Kinesis
json_schemas:
- name: AggregatedMetricsResponseBody
  property_count: 0
  slug: flink-rest-aggregated-metrics-response-body
- name: AggregatedTaskDetailsInfo
  property_count: 2
  slug: flink-rest-aggregated-task-details-info
- name: AggregationMode
  property_count: 0
  slug: flink-rest-aggregation-mode
- name: ApplicationStatus
  property_count: 0
  slug: flink-rest-application-status
- name: AsynchronousOperationInfo
  property_count: 1
  slug: flink-rest-asynchronous-operation-info
- name: AsynchronousOperationResult
  property_count: 2
  slug: flink-rest-asynchronous-operation-result
- name: CheckpointAlignment
  property_count: 4
  slug: flink-rest-checkpoint-alignment
- name: CheckpointAlignmentSummary
  property_count: 4
  slug: flink-rest-checkpoint-alignment-summary
- name: CheckpointConfigInfo
  property_count: 15
  slug: flink-rest-checkpoint-config-info
- name: CheckpointDuration
  property_count: 2
  slug: flink-rest-checkpoint-duration
- name: CheckpointDurationSummary
  property_count: 2
  slug: flink-rest-checkpoint-duration-summary
- name: CheckpointInfo
  property_count: 2
  slug: flink-rest-checkpoint-info
- name: CheckpointStatistics
  property_count: 17
  slug: flink-rest-checkpoint-statistics
- name: CheckpointStatisticsSummary
  property_count: 6
  slug: flink-rest-checkpoint-statistics-summary
- name: CheckpointStatsStatus
  property_count: 0
  slug: flink-rest-checkpoint-stats-status
- name: CheckpointTriggerRequestBody
  property_count: 2
  slug: flink-rest-checkpoint-trigger-request-body
- name: CheckpointType
  property_count: 0
  slug: flink-rest-checkpoint-type
- name: CheckpointingStatistics
  property_count: 4
  slug: flink-rest-checkpointing-statistics
- name: ClusterDataSetEntry
  property_count: 2
  slug: flink-rest-cluster-data-set-entry
- name: ClusterDataSetListResponseBody
  property_count: 1
  slug: flink-rest-cluster-data-set-list-response-body
- name: ClusterOverviewWithVersion
  property_count: 11
  slug: flink-rest-cluster-overview-with-version
- name: CompletedCheckpointStatistics
  property_count: 0
  slug: flink-rest-completed-checkpoint-statistics
- name: CompletedSubtaskCheckpointStatistics
  property_count: 0
  slug: flink-rest-completed-subtask-checkpoint-statistics
- name: ConfigurationInfoEntry
  property_count: 2
  slug: flink-rest-configuration-info-entry
- name: ConfigurationInfo
  property_count: 0
  slug: flink-rest-configuration-info
- name: Counts
  property_count: 5
  slug: flink-rest-counts
- name: DashboardConfiguration
  property_count: 6
  slug: flink-rest-dashboard-configuration
- name: EnvironmentInfo
  property_count: 2
  slug: flink-rest-environment-info
- name: ExceptionInfo
  property_count: 7
  slug: flink-rest-exception-info
- name: ExecutionConfigInfo
  property_count: 4
  slug: flink-rest-execution-config-info
- name: ExecutionState
  property_count: 0
  slug: flink-rest-execution-state
- name: ExternalizedCheckpointInfo
  property_count: 2
  slug: flink-rest-externalized-checkpoint-info
- name: FailedCheckpointStatistics
  property_count: 0
  slug: flink-rest-failed-checkpoint-statistics
- name: FailureLabel
  property_count: 2
  slug: flink-rest-failure-label
- name: Features
  property_count: 4
  slug: flink-rest-features
- name: GarbageCollectorInfo
  property_count: 3
  slug: flink-rest-garbage-collector-info
- name: HardwareDescription
  property_count: 4
  slug: flink-rest-hardware-description
- name: Id
  property_count: 0
  slug: flink-rest-id
- name: IntermediateDataSetID
  property_count: 0
  slug: flink-rest-intermediate-data-set-id
- name: IOMetricsInfo
  property_count: 11
  slug: flink-rest-io-metrics-info
- name: JarEntryInfo
  property_count: 2
  slug: flink-rest-jar-entry-info
- name: JarFileInfo
  property_count: 4
  slug: flink-rest-jar-file-info
- name: JarListInfo
  property_count: 2
  slug: flink-rest-jar-list-info
- name: JarPlanRequestBody
  property_count: 5
  slug: flink-rest-jar-plan-request-body
- name: JarRunRequestBody
  property_count: 9
  slug: flink-rest-jar-run-request-body
- name: JarRunResponseBody
  property_count: 1
  slug: flink-rest-jar-run-response-body
- name: JarUploadResponseBody
  property_count: 2
  slug: flink-rest-jar-upload-response-body
- name: JobAccumulator
  property_count: 0
  slug: flink-rest-job-accumulator
- name: JobAccumulatorsInfo
  property_count: 3
  slug: flink-rest-job-accumulators-info
- name: JobClientHeartbeatRequestBody
  property_count: 1
  slug: flink-rest-job-client-heartbeat-request-body
- name: JobConfigInfo
  property_count: 3
  slug: flink-rest-job-config-info
- name: JobDetailsInfo
  property_count: 16
  slug: flink-rest-job-details-info
- name: JobDetails
  property_count: 9
  slug: flink-rest-job-details
- name: JobDetailsVertexInfo
  property_count: 11
  slug: flink-rest-job-details-vertex-info
- name: JobExceptionHistory
  property_count: 2
  slug: flink-rest-job-exception-history
- name: JobExceptionsInfoWithHistory
  property_count: 1
  slug: flink-rest-job-exceptions-info-with-history
- name: JobExecutionResultResponseBody
  property_count: 2
  slug: flink-rest-job-execution-result-response-body
- name: JobID
  property_count: 0
  slug: flink-rest-job-id
- name: JobIdWithStatus
  property_count: 2
  slug: flink-rest-job-id-with-status
- name: JobIdsWithStatusOverview
  property_count: 1
  slug: flink-rest-job-ids-with-status-overview
- name: JobPlanInfo
  property_count: 1
  slug: flink-rest-job-plan-info
- name: JobResourceRequirementsBody
  property_count: 0
  slug: flink-rest-job-resource-requirements-body
- name: JobResult
  property_count: 6
  slug: flink-rest-job-result
- name: JobStatusInfo
  property_count: 1
  slug: flink-rest-job-status-info
- name: JobStatus
  property_count: 0
  slug: flink-rest-job-status
- name: JobType
  property_count: 0
  slug: flink-rest-job-type
- name: JobVertexAccumulatorsInfo
  property_count: 2
  slug: flink-rest-job-vertex-accumulators-info
- name: JobVertexBackPressureInfo
  property_count: 4
  slug: flink-rest-job-vertex-back-pressure-info
- name: JobVertexDetailsInfo
  property_count: 7
  slug: flink-rest-job-vertex-details-info
- name: JobVertexID
  property_count: 0
  slug: flink-rest-job-vertex-id
- name: JobVertexResourceRequirements
  property_count: 1
  slug: flink-rest-job-vertex-resource-requirements
- name: JobVertexTaskManagerInfo
  property_count: 9
  slug: flink-rest-job-vertex-task-manager-info
- name: JobVertexTaskManagersInfo
  property_count: 4
  slug: flink-rest-job-vertex-task-managers-info
- name: JVMInfo
  property_count: 3
  slug: flink-rest-jvm-info
- name: LatestCheckpoints
  property_count: 4
  slug: flink-rest-latest-checkpoints
- name: LogInfo
  property_count: 3
  slug: flink-rest-log-info
- name: LogListInfo
  property_count: 1
  slug: flink-rest-log-list-info
- name: LogUrlResponse
  property_count: 1
  slug: flink-rest-log-url-response
- name: MetricCollectionResponseBody
  property_count: 1
  slug: flink-rest-metric-collection-response-body
- name: Metric
  property_count: 2
  slug: flink-rest-metric
- name: MultipleJobsDetails
  property_count: 1
  slug: flink-rest-multiple-jobs-details
- name: Node
  property_count: 3
  slug: flink-rest-node
- name: Parallelism
  property_count: 2
  slug: flink-rest-parallelism
- name: PendingCheckpointStatistics
  property_count: 0
  slug: flink-rest-pending-checkpoint-statistics
- name: PendingSubtaskCheckpointStatistics
  property_count: 0
  slug: flink-rest-pending-subtask-checkpoint-statistics
- name: ProcessingMode
  property_count: 0
  slug: flink-rest-processing-mode
- name: QueueStatus
  property_count: 1
  slug: flink-rest-queue-status
- name: RawJson
  property_count: 0
  slug: flink-rest-raw-json
- name: RecoveryClaimMode
  property_count: 0
  slug: flink-rest-recovery-claim-mode
- name: ResourceID
  property_count: 0
  slug: flink-rest-resource-id
- name: ResourceProfileInfo
  property_count: 6
  slug: flink-rest-resource-profile-info
- name: RestAPICheckpointType
  property_count: 0
  slug: flink-rest-rest-api-checkpoint-type
- name: RestoredCheckpointStatistics
  property_count: 4
  slug: flink-rest-restored-checkpoint-statistics
- name: RootExceptionInfo
  property_count: 8
  slug: flink-rest-root-exception-info
- name: SavepointDisposalRequest
  property_count: 1
  slug: flink-rest-savepoint-disposal-request
- name: SavepointFormatType
  property_count: 0
  slug: flink-rest-savepoint-format-type
- name: SavepointInfo
  property_count: 2
  slug: flink-rest-savepoint-info
- name: SavepointTriggerRequestBody
  property_count: 4
  slug: flink-rest-savepoint-trigger-request-body
- name: SerializedThrowable
  property_count: 1
  slug: flink-rest-serialized-throwable
- name: SerializedValueOptionalFailureObject
  property_count: 1
  slug: flink-rest-serialized-value-optional-failure-object
- name: SlotInfo
  property_count: 2
  slug: flink-rest-slot-info
- name: SlotSharingGroupId
  property_count: 3
  slug: flink-rest-slot-sharing-group-id
- name: StatsSummaryDto
  property_count: 8
  slug: flink-rest-stats-summary-dto
- name: StopWithSavepointRequestBody
  property_count: 4
  slug: flink-rest-stop-with-savepoint-request-body
- name: SubtaskAccumulatorsInfo
  property_count: 4
  slug: flink-rest-subtask-accumulators-info
- name: SubtaskBackPressureInfo
  property_count: 7
  slug: flink-rest-subtask-back-pressure-info
- name: SubtaskCheckpointStatistics
  property_count: 3
  slug: flink-rest-subtask-checkpoint-statistics
- name: SubtaskExecutionAttemptAccumulatorsInfo
  property_count: 4
  slug: flink-rest-subtask-execution-attempt-accumulators-info
- name: SubtaskExecutionAttemptDetailsInfo
  property_count: 11
  slug: flink-rest-subtask-execution-attempt-details-info
- name: SubtaskTimeInfo
  property_count: 4
  slug: flink-rest-subtask-time-info
- name: SubtasksAllAccumulatorsInfo
  property_count: 3
  slug: flink-rest-subtasks-all-accumulators-info
- name: SubtasksTimesInfo
  property_count: 4
  slug: flink-rest-subtasks-times-info
- name: TaskCheckpointStatistics
  property_count: 11
  slug: flink-rest-task-checkpoint-statistics
- name: TaskCheckpointStatisticsWithSubtaskDetails
  property_count: 13
  slug: flink-rest-task-checkpoint-statistics-with-subtask-details
- name: TaskCheckpointStatisticsWithSubtaskDetailsSummary
  property_count: 6
  slug: flink-rest-task-checkpoint-statistics-with-subtask-details-summary
- name: TaskExecutorMemoryConfiguration
  property_count: 10
  slug: flink-rest-task-executor-memory-configuration
- name: TaskManagerDetailsInfo
  property_count: 14
  slug: flink-rest-task-manager-details-info
- name: TaskManagerInfo
  property_count: 12
  slug: flink-rest-task-manager-info
- name: TaskManagerMetricsInfo
  property_count: 19
  slug: flink-rest-task-manager-metrics-info
- name: TaskManagersInfo
  property_count: 1
  slug: flink-rest-task-managers-info
- name: TerminationMode
  property_count: 0
  slug: flink-rest-termination-mode
- name: ThreadDumpInfo
  property_count: 1
  slug: flink-rest-thread-dump-info
- name: ThreadInfo
  property_count: 2
  slug: flink-rest-thread-info
- name: ThreadStates
  property_count: 0
  slug: flink-rest-thread-states
- name: TriggerId
  property_count: 0
  slug: flink-rest-trigger-id
- name: TriggerResponse
  property_count: 1
  slug: flink-rest-trigger-response
- name: UploadStatus
  property_count: 0
  slug: flink-rest-upload-status
- name: UserAccumulator
  property_count: 3
  slug: flink-rest-user-accumulator
- name: UserTaskAccumulator
  property_count: 3
  slug: flink-rest-user-task-accumulator
- name: VertexBackPressureLevel
  property_count: 0
  slug: flink-rest-vertex-back-pressure-level
- name: VertexBackPressureStatus
  property_count: 0
  slug: flink-rest-vertex-back-pressure-status
- name: VertexFlameGraph
  property_count: 2
  slug: flink-rest-vertex-flame-graph
json_structures:
- name: Flink Rest Aggregated Metrics Response Body Structure
  property_count: 0
  slug: flink-rest-aggregated-metrics-response-body-structure
- name: Flink Rest Aggregated Task Details Info Structure
  property_count: 2
  slug: flink-rest-aggregated-task-details-info-structure
- name: Flink Rest Aggregation Mode Structure
  property_count: 0
  slug: flink-rest-aggregation-mode-structure
- name: Flink Rest Application Status Structure
  property_count: 0
  slug: flink-rest-application-status-structure
- name: Flink Rest Asynchronous Operation Info Structure
  property_count: 1
  slug: flink-rest-asynchronous-operation-info-structure
- name: Flink Rest Asynchronous Operation Result Structure
  property_count: 2
  slug: flink-rest-asynchronous-operation-result-structure
- name: Flink Rest Checkpoint Alignment Structure
  property_count: 4
  slug: flink-rest-checkpoint-alignment-structure
- name: Flink Rest Checkpoint Alignment Summary Structure
  property_count: 4
  slug: flink-rest-checkpoint-alignment-summary-structure
- name: Flink Rest Checkpoint Config Info Structure
  property_count: 15
  slug: flink-rest-checkpoint-config-info-structure
- name: Flink Rest Checkpoint Duration Structure
  property_count: 2
  slug: flink-rest-checkpoint-duration-structure
- name: Flink Rest Checkpoint Duration Summary Structure
  property_count: 2
  slug: flink-rest-checkpoint-duration-summary-structure
- name: Flink Rest Checkpoint Info Structure
  property_count: 2
  slug: flink-rest-checkpoint-info-structure
- name: Flink Rest Checkpoint Statistics Structure
  property_count: 17
  slug: flink-rest-checkpoint-statistics-structure
- name: Flink Rest Checkpoint Statistics Summary Structure
  property_count: 6
  slug: flink-rest-checkpoint-statistics-summary-structure
- name: Flink Rest Checkpoint Stats Status Structure
  property_count: 0
  slug: flink-rest-checkpoint-stats-status-structure
- name: Flink Rest Checkpoint Trigger Request Body Structure
  property_count: 2
  slug: flink-rest-checkpoint-trigger-request-body-structure
- name: Flink Rest Checkpoint Type Structure
  property_count: 0
  slug: flink-rest-checkpoint-type-structure
- name: Flink Rest Checkpointing Statistics Structure
  property_count: 4
  slug: flink-rest-checkpointing-statistics-structure
- name: Flink Rest Cluster Data Set Entry Structure
  property_count: 2
  slug: flink-rest-cluster-data-set-entry-structure
- name: Flink Rest Cluster Data Set List Response Body Structure
  property_count: 1
  slug: flink-rest-cluster-data-set-list-response-body-structure
- name: Flink Rest Cluster Overview With Version Structure
  property_count: 11
  slug: flink-rest-cluster-overview-with-version-structure
- name: Flink Rest Completed Checkpoint Statistics Structure
  property_count: 0
  slug: flink-rest-completed-checkpoint-statistics-structure
- name: Flink Rest Completed Subtask Checkpoint Statistics Structure
  property_count: 0
  slug: flink-rest-completed-subtask-checkpoint-statistics-structure
- name: Flink Rest Configuration Info Entry Structure
  property_count: 2
  slug: flink-rest-configuration-info-entry-structure
- name: Flink Rest Configuration Info Structure
  property_count: 0
  slug: flink-rest-configuration-info-structure
- name: Flink Rest Counts Structure
  property_count: 5
  slug: flink-rest-counts-structure
- name: Flink Rest Dashboard Configuration Structure
  property_count: 6
  slug: flink-rest-dashboard-configuration-structure
- name: Flink Rest Environment Info Structure
  property_count: 2
  slug: flink-rest-environment-info-structure
- name: Flink Rest Exception Info Structure
  property_count: 7
  slug: flink-rest-exception-info-structure
- name: Flink Rest Execution Config Info Structure
  property_count: 4
  slug: flink-rest-execution-config-info-structure
- name: Flink Rest Execution State Structure
  property_count: 0
  slug: flink-rest-execution-state-structure
- name: Flink Rest Externalized Checkpoint Info Structure
  property_count: 2
  slug: flink-rest-externalized-checkpoint-info-structure
- name: Flink Rest Failed Checkpoint Statistics Structure
  property_count: 0
  slug: flink-rest-failed-checkpoint-statistics-structure
- name: Flink Rest Failure Label Structure
  property_count: 2
  slug: flink-rest-failure-label-structure
- name: Flink Rest Features Structure
  property_count: 4
  slug: flink-rest-features-structure
- name: Flink Rest Garbage Collector Info Structure
  property_count: 3
  slug: flink-rest-garbage-collector-info-structure
- name: Flink Rest Hardware Description Structure
  property_count: 4
  slug: flink-rest-hardware-description-structure
- name: Flink Rest Id Structure
  property_count: 0
  slug: flink-rest-id-structure
- name: Flink Rest Intermediate Data Set Id Structure
  property_count: 0
  slug: flink-rest-intermediate-data-set-id-structure
- name: Flink Rest Io Metrics Info Structure
  property_count: 11
  slug: flink-rest-io-metrics-info-structure
- name: Flink Rest Jar Entry Info Structure
  property_count: 2
  slug: flink-rest-jar-entry-info-structure
- name: Flink Rest Jar File Info Structure
  property_count: 4
  slug: flink-rest-jar-file-info-structure
- name: Flink Rest Jar List Info Structure
  property_count: 2
  slug: flink-rest-jar-list-info-structure
- name: Flink Rest Jar Plan Request Body Structure
  property_count: 5
  slug: flink-rest-jar-plan-request-body-structure
- name: Flink Rest Jar Run Request Body Structure
  property_count: 9
  slug: flink-rest-jar-run-request-body-structure
- name: Flink Rest Jar Run Response Body Structure
  property_count: 1
  slug: flink-rest-jar-run-response-body-structure
- name: Flink Rest Jar Upload Response Body Structure
  property_count: 2
  slug: flink-rest-jar-upload-response-body-structure
- name: Flink Rest Job Accumulator Structure
  property_count: 0
  slug: flink-rest-job-accumulator-structure
- name: Flink Rest Job Accumulators Info Structure
  property_count: 3
  slug: flink-rest-job-accumulators-info-structure
- name: Flink Rest Job Client Heartbeat Request Body Structure
  property_count: 1
  slug: flink-rest-job-client-heartbeat-request-body-structure
- name: Flink Rest Job Config Info Structure
  property_count: 3
  slug: flink-rest-job-config-info-structure
- name: Flink Rest Job Details Info Structure
  property_count: 16
  slug: flink-rest-job-details-info-structure
- name: Flink Rest Job Details Structure
  property_count: 9
  slug: flink-rest-job-details-structure
- name: Flink Rest Job Details Vertex Info Structure
  property_count: 11
  slug: flink-rest-job-details-vertex-info-structure
- name: Flink Rest Job Exception History Structure
  property_count: 2
  slug: flink-rest-job-exception-history-structure
- name: Flink Rest Job Exceptions Info With History Structure
  property_count: 1
  slug: flink-rest-job-exceptions-info-with-history-structure
- name: Flink Rest Job Execution Result Response Body Structure
  property_count: 2
  slug: flink-rest-job-execution-result-response-body-structure
- name: Flink Rest Job Id Structure
  property_count: 0
  slug: flink-rest-job-id-structure
- name: Flink Rest Job Id With Status Structure
  property_count: 2
  slug: flink-rest-job-id-with-status-structure
- name: Flink Rest Job Ids With Status Overview Structure
  property_count: 1
  slug: flink-rest-job-ids-with-status-overview-structure
- name: Flink Rest Job Plan Info Structure
  property_count: 1
  slug: flink-rest-job-plan-info-structure
- name: Flink Rest Job Resource Requirements Body Structure
  property_count: 0
  slug: flink-rest-job-resource-requirements-body-structure
- name: Flink Rest Job Result Structure
  property_count: 6
  slug: flink-rest-job-result-structure
- name: Flink Rest Job Status Info Structure
  property_count: 1
  slug: flink-rest-job-status-info-structure
- name: Flink Rest Job Status Structure
  property_count: 0
  slug: flink-rest-job-status-structure
- name: Flink Rest Job Type Structure
  property_count: 0
  slug: flink-rest-job-type-structure
- name: Flink Rest Job Vertex Accumulators Info Structure
  property_count: 2
  slug: flink-rest-job-vertex-accumulators-info-structure
- name: Flink Rest Job Vertex Back Pressure Info Structure
  property_count: 4
  slug: flink-rest-job-vertex-back-pressure-info-structure
- name: Flink Rest Job Vertex Details Info Structure
  property_count: 7
  slug: flink-rest-job-vertex-details-info-structure
- name: Flink Rest Job Vertex Id Structure
  property_count: 0
  slug: flink-rest-job-vertex-id-structure
- name: Flink Rest Job Vertex Resource Requirements Structure
  property_count: 1
  slug: flink-rest-job-vertex-resource-requirements-structure
- name: Flink Rest Job Vertex Task Manager Info Structure
  property_count: 9
  slug: flink-rest-job-vertex-task-manager-info-structure
- name: Flink Rest Job Vertex Task Managers Info Structure
  property_count: 4
  slug: flink-rest-job-vertex-task-managers-info-structure
- name: Flink Rest Jvm Info Structure
  property_count: 3
  slug: flink-rest-jvm-info-structure
- name: Flink Rest Latest Checkpoints Structure
  property_count: 4
  slug: flink-rest-latest-checkpoints-structure
- name: Flink Rest Log Info Structure
  property_count: 3
  slug: flink-rest-log-info-structure
- name: Flink Rest Log List Info Structure
  property_count: 1
  slug: flink-rest-log-list-info-structure
- name: Flink Rest Log Url Response Structure
  property_count: 1
  slug: flink-rest-log-url-response-structure
- name: Flink Rest Metric Collection Response Body Structure
  property_count: 1
  slug: flink-rest-metric-collection-response-body-structure
- name: Flink Rest Metric Structure
  property_count: 2
  slug: flink-rest-metric-structure
- name: Flink Rest Multiple Jobs Details Structure
  property_count: 1
  slug: flink-rest-multiple-jobs-details-structure
- name: Flink Rest Node Structure
  property_count: 3
  slug: flink-rest-node-structure
- name: Flink Rest Parallelism Structure
  property_count: 2
  slug: flink-rest-parallelism-structure
- name: Flink Rest Pending Checkpoint Statistics Structure
  property_count: 0
  slug: flink-rest-pending-checkpoint-statistics-structure
- name: Flink Rest Pending Subtask Checkpoint Statistics Structure
  property_count: 0
  slug: flink-rest-pending-subtask-checkpoint-statistics-structure
- name: Flink Rest Processing Mode Structure
  property_count: 0
  slug: flink-rest-processing-mode-structure
- name: Flink Rest Queue Status Structure
  property_count: 1
  slug: flink-rest-queue-status-structure
- name: Flink Rest Raw Json Structure
  property_count: 0
  slug: flink-rest-raw-json-structure
- name: Flink Rest Recovery Claim Mode Structure
  property_count: 0
  slug: flink-rest-recovery-claim-mode-structure
- name: Flink Rest Resource Id Structure
  property_count: 0
  slug: flink-rest-resource-id-structure
- name: Flink Rest Resource Profile Info Structure
  property_count: 6
  slug: flink-rest-resource-profile-info-structure
- name: Flink Rest Rest Api Checkpoint Type Structure
  property_count: 0
  slug: flink-rest-rest-api-checkpoint-type-structure
- name: Flink Rest Restored Checkpoint Statistics Structure
  property_count: 4
  slug: flink-rest-restored-checkpoint-statistics-structure
- name: Flink Rest Root Exception Info Structure
  property_count: 8
  slug: flink-rest-root-exception-info-structure
- name: Flink Rest Savepoint Disposal Request Structure
  property_count: 1
  slug: flink-rest-savepoint-disposal-request-structure
- name: Flink Rest Savepoint Format Type Structure
  property_count: 0
  slug: flink-rest-savepoint-format-type-structure
- name: Flink Rest Savepoint Info Structure
  property_count: 2
  slug: flink-rest-savepoint-info-structure
- name: Flink Rest Savepoint Trigger Request Body Structure
  property_count: 4
  slug: flink-rest-savepoint-trigger-request-body-structure
- name: Flink Rest Serialized Throwable Structure
  property_count: 1
  slug: flink-rest-serialized-throwable-structure
- name: Flink Rest Serialized Value Optional Failure Object Structure
  property_count: 1
  slug: flink-rest-serialized-value-optional-failure-object-structure
- name: Flink Rest Slot Info Structure
  property_count: 2
  slug: flink-rest-slot-info-structure
- name: Flink Rest Slot Sharing Group Id Structure
  property_count: 3
  slug: flink-rest-slot-sharing-group-id-structure
- name: Flink Rest Stats Summary Dto Structure
  property_count: 8
  slug: flink-rest-stats-summary-dto-structure
- name: Flink Rest Stop With Savepoint Request Body Structure
  property_count: 4
  slug: flink-rest-stop-with-savepoint-request-body-structure
- name: Flink Rest Subtask Accumulators Info Structure
  property_count: 4
  slug: flink-rest-subtask-accumulators-info-structure
- name: Flink Rest Subtask Back Pressure Info Structure
  property_count: 7
  slug: flink-rest-subtask-back-pressure-info-structure
- name: Flink Rest Subtask Checkpoint Statistics Structure
  property_count: 3
  slug: flink-rest-subtask-checkpoint-statistics-structure
- name: Flink Rest Subtask Execution Attempt Accumulators Info Structure
  property_count: 4
  slug: flink-rest-subtask-execution-attempt-accumulators-info-structure
- name: Flink Rest Subtask Execution Attempt Details Info Structure
  property_count: 11
  slug: flink-rest-subtask-execution-attempt-details-info-structure
- name: Flink Rest Subtask Time Info Structure
  property_count: 4
  slug: flink-rest-subtask-time-info-structure
- name: Flink Rest Subtasks All Accumulators Info Structure
  property_count: 3
  slug: flink-rest-subtasks-all-accumulators-info-structure
- name: Flink Rest Subtasks Times Info Structure
  property_count: 4
  slug: flink-rest-subtasks-times-info-structure
- name: Flink Rest Task Checkpoint Statistics Structure
  property_count: 11
  slug: flink-rest-task-checkpoint-statistics-structure
- name: Flink Rest Task Checkpoint Statistics With Subtask Details Structure
  property_count: 13
  slug: flink-rest-task-checkpoint-statistics-with-subtask-details-structure
- name: Flink Rest Task Checkpoint Statistics With Subtask Details Summary Structure
  property_count: 6
  slug: flink-rest-task-checkpoint-statistics-with-subtask-details-summary-structure
- name: Flink Rest Task Executor Memory Configuration Structure
  property_count: 10
  slug: flink-rest-task-executor-memory-configuration-structure
- name: Flink Rest Task Manager Details Info Structure
  property_count: 14
  slug: flink-rest-task-manager-details-info-structure
- name: Flink Rest Task Manager Info Structure
  property_count: 12
  slug: flink-rest-task-manager-info-structure
- name: Flink Rest Task Manager Metrics Info Structure
  property_count: 19
  slug: flink-rest-task-manager-metrics-info-structure
- name: Flink Rest Task Managers Info Structure
  property_count: 1
  slug: flink-rest-task-managers-info-structure
- name: Flink Rest Termination Mode Structure
  property_count: 0
  slug: flink-rest-termination-mode-structure
- name: Flink Rest Thread Dump Info Structure
  property_count: 1
  slug: flink-rest-thread-dump-info-structure
- name: Flink Rest Thread Info Structure
  property_count: 2
  slug: flink-rest-thread-info-structure
- name: Flink Rest Thread States Structure
  property_count: 0
  slug: flink-rest-thread-states-structure
- name: Flink Rest Trigger Id Structure
  property_count: 0
  slug: flink-rest-trigger-id-structure
- name: Flink Rest Trigger Response Structure
  property_count: 1
  slug: flink-rest-trigger-response-structure
- name: Flink Rest Upload Status Structure
  property_count: 0
  slug: flink-rest-upload-status-structure
- name: Flink Rest User Accumulator Structure
  property_count: 3
  slug: flink-rest-user-accumulator-structure
- name: Flink Rest User Task Accumulator Structure
  property_count: 3
  slug: flink-rest-user-task-accumulator-structure
- name: Flink Rest Vertex Back Pressure Level Structure
  property_count: 0
  slug: flink-rest-vertex-back-pressure-level-structure
- name: Flink Rest Vertex Back Pressure Status Structure
  property_count: 0
  slug: flink-rest-vertex-back-pressure-status-structure
- name: Flink Rest Vertex Flame Graph Structure
  property_count: 2
  slug: flink-rest-vertex-flame-graph-structure
jsonld:
- class_count: 52
  name: Apache Flink Rest Context
  property_count: 130
  slug: apache-flink-rest-context
layout: provider
modified: '2026-05-19'
name: Apache Flink
nav: Providers
network: true
overview: 'Apache Flink publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Config API, Datasets API, and 6 more. Tagged areas include Apache, Batch Processing, Big Data, Open Source, and Real-Time Analytics.


  The Apache Flink catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Flink''s developer surface includes getting-started guide, engineering blog, support, training material, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Apache Flink Plans Pricing
  plan_count: 3
  slug: apache-flink-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Apache Flink Rate Limits
  slug: apache-flink-rate-limits
rules:
- name: Apache Flink API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-flink-jsonschema-spectral-rules
- name: Apache Flink API Rules
  rule_count: 16
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 9
  slug: apache-flink-spectral-rules
score:
  band: developing
  composite: 49.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.0
    developer_ergonomics: 17.4
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 49.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-flink/refs/heads/main/screenshots/apache-flink-2026-06-20T172057.png
security:
- kind: domain-security
  name: Apache Flink Domain Security
  slug: apache-flink-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Apache Flink Vulnerability Disclosure
  slug: apache-flink-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-flink
tags:
- Apache
- Batch Processing
- Big Data
- Open Source
- Real-Time Analytics
- Stateful Computing
- Stream Processing
use_cases:
- description: Process and analyze event streams in real time for dashboards, alerts, and operational intelligence.
  name: Real-Time Analytics
- description: Build scalable ETL pipelines for data lake ingestion, transformation, and enrichment.
  name: ETL Pipelines
- description: Detect fraudulent transactions in real time using stateful pattern matching over event streams.
  name: Fraud Detection
- description: Process high-volume IoT device telemetry with stateful aggregations and time-window computations.
  name: IoT Data Processing
- description: Serve ML model predictions at scale with streaming feature computation and online inference.
  name: Machine Learning Inference
---
