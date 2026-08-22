---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 69
  human_in_the_loop: 7
  name: Amazon Neptune Agentic Access
  operation_count: 130
  slug: amazon-neptune-agentic-access
  summary_line: 130 operations · 69 acting · 7 human-in-the-loop
api_count: 29
apis:
- description: The ?Action=AddTagsToResource API from Amazon Neptune — 1 operation(s) for ?action=addtagstoresource.
  name: Amazon Neptune ?Action=AddTagsToResource API
  slug: amazon-neptune-action-addtagstoresource-api
- description: The ?Action=ListTagsForResource API from Amazon Neptune — 1 operation(s) for ?action=listtagsforresource.
  name: Amazon Neptune ?Action=ListTagsForResource API
  slug: amazon-neptune-action-listtagsforresource-api
- description: ML data processing job operations
  name: Amazon Neptune Data Processing API
  slug: amazon-neptune-data-processing-api
- description: Operations for managing Neptune DB clusters
  name: Amazon Neptune DB Clusters API
  slug: amazon-neptune-db-clusters-api
- description: Operations for managing Neptune DB instances
  name: Amazon Neptune DB Instances API
  slug: amazon-neptune-db-instances-api
- description: Operations for querying engine version information
  name: Amazon Neptune Engine API
  slug: amazon-neptune-engine-api
- description: Operations for managing event subscriptions and viewing events
  name: Amazon Neptune Events API
  slug: amazon-neptune-events-api
- description: Operations for managing Neptune global database clusters
  name: Amazon Neptune Global Clusters API
  slug: amazon-neptune-global-clusters-api
- description: Operations for managing graph snapshots
  name: Amazon Neptune Graph Snapshots API
  slug: amazon-neptune-graph-snapshots-api
- description: Operations for managing Neptune Analytics graph resources
  name: Amazon Neptune Graphs API
  slug: amazon-neptune-graphs-api
- description: Execute Gremlin graph traversal queries
  name: Amazon Neptune Gremlin API
  slug: amazon-neptune-gremlin-api
- description: Operations for importing data into graphs
  name: Amazon Neptune Import Tasks API
  slug: amazon-neptune-import-tasks-api
- description: ML inference endpoint management operations
  name: Amazon Neptune Inference Endpoints API
  slug: amazon-neptune-inference-endpoints-api
- description: Bulk data loading operations
  name: Amazon Neptune Loader API
  slug: amazon-neptune-loader-api
- description: Operations for managing pending maintenance actions
  name: Amazon Neptune Maintenance API
  slug: amazon-neptune-maintenance-api
- description: Machine learning operations
  name: Amazon Neptune ML API
  slug: amazon-neptune-ml-api
- description: ML model training job operations
  name: Amazon Neptune Model Training API
  slug: amazon-neptune-model-training-api
- description: ML model transform job operations
  name: Amazon Neptune Model Transform API
  slug: amazon-neptune-model-transform-api
- description: Execute openCypher graph queries
  name: Amazon Neptune openCypher API
  slug: amazon-neptune-opencypher-api
- description: Operations for managing DB and cluster parameter groups
  name: Amazon Neptune Parameter Groups API
  slug: amazon-neptune-parameter-groups-api
- description: Operations for managing private graph endpoints in VPCs
  name: Amazon Neptune Private Graph Endpoints API
  slug: amazon-neptune-private-graph-endpoints-api
- description: Change data capture for property graph (Gremlin/openCypher) data
  name: Amazon Neptune Property Graph Stream API
  slug: amazon-neptune-property-graph-stream-api
- description: Submit Gremlin graph traversal queries
  name: Amazon Neptune Query API
  slug: amazon-neptune-query-api
- description: Operations for managing cluster snapshots
  name: Amazon Neptune Snapshots API
  slug: amazon-neptune-snapshots-api
- description: Execute SPARQL queries against RDF data
  name: Amazon Neptune SPARQL API
  slug: amazon-neptune-sparql-api
- description: Change data capture for RDF (SPARQL) data
  name: Amazon Neptune SPARQL Stream API
  slug: amazon-neptune-sparql-stream-api
- description: Query engine status and statistics
  name: Amazon Neptune Status API
  slug: amazon-neptune-status-api
- description: Change data capture stream operations
  name: Amazon Neptune Streams API
  slug: amazon-neptune-streams-api
- description: Operations for managing DB subnet groups
  name: Amazon Neptune Subnet Groups API
  slug: amazon-neptune-subnet-groups-api
arazzos:
- description: Inspect a Neptune Analytics import task and cancel it only if it is still running.
  name: Amazon Neptune Analytics Cancel Import Task
  slug: amazon-neptune-analytics-cancel-import-task-workflow
- description: Create a Neptune Analytics graph and poll until it becomes AVAILABLE.
  name: Amazon Neptune Analytics Create Graph and Wait
  slug: amazon-neptune-analytics-create-graph-workflow
- description: Create a Neptune Analytics graph populated from S3 and poll the import task to completion.
  name: Amazon Neptune Analytics Create Graph from Import Task
  slug: amazon-neptune-analytics-import-task-workflow
- description: Create a VPC private endpoint for a Neptune Analytics graph and poll until it is AVAILABLE.
  name: Amazon Neptune Analytics Create Private Graph Endpoint
  slug: amazon-neptune-analytics-private-endpoint-workflow
- description: Empty a Neptune Analytics graph of all data, then wait until it is AVAILABLE again.
  name: Amazon Neptune Analytics Reset Graph
  slug: amazon-neptune-analytics-reset-graph-workflow
- description: Snapshot a Neptune Analytics graph, wait for the snapshot, then restore it into a new graph.
  name: Amazon Neptune Analytics Snapshot and Restore
  slug: amazon-neptune-analytics-snapshot-and-restore-workflow
- description: Start a bulk loader job from S3 and poll its status until the load completes.
  name: Amazon Neptune Bulk Loader Start and Poll
  slug: amazon-neptune-bulk-loader-poll-workflow
- description: Add a labeled vertex over the Gremlin HTTP endpoint, then count vertices to confirm the write landed.
  name: Amazon Neptune Gremlin Add and Count Vertices
  slug: amazon-neptune-gremlin-add-and-count-vertices-workflow
- description: Look up a specific Gremlin query's status, then cancel it if it has not already been cancelled.
  name: Amazon Neptune Cancel a Running Gremlin Query
  slug: amazon-neptune-gremlin-cancel-query-workflow
- description: Inspect a Gremlin query's execution plan, then profile it with runtime statistics.
  name: Amazon Neptune Gremlin Explain then Profile
  slug: amazon-neptune-gremlin-explain-profile-workflow
- description: Run a Gremlin traversal via the Data API and confirm the engine and query queue are healthy.
  name: Amazon Neptune Gremlin Query with Status Check
  slug: amazon-neptune-gremlin-query-with-status-workflow
- description: Look up a bulk load job's status and cancel it only if it is still in progress.
  name: Amazon Neptune Cancel a Running Bulk Load
  slug: amazon-neptune-loader-cancel-running-job-workflow
- description: Start a bulk load via the Loader endpoint, verify it appears in the job list, and poll its status.
  name: Amazon Neptune Bulk Load Job Lifecycle
  slug: amazon-neptune-loader-job-lifecycle-workflow
- description: Create an ML inference endpoint from a trained model and poll it until it is in service.
  name: Amazon Neptune ML Create and Verify Inference Endpoint
  slug: amazon-neptune-ml-create-inference-endpoint-workflow
- description: Run a Neptune ML data processing job to completion, then launch and poll model training.
  name: Amazon Neptune ML Data Processing to Model Training
  slug: amazon-neptune-ml-dataprocessing-to-training-workflow
- description: Launch a Neptune ML model transform job from a trained model and poll it to completion.
  name: Amazon Neptune ML Model Transform Job
  slug: amazon-neptune-ml-model-transform-workflow
- description: Inspect a Neptune ML data processing job and stop it with cleanup only if it is still running.
  name: Amazon Neptune ML Stop Data Processing Job
  slug: amazon-neptune-ml-stop-dataprocessing-job-workflow
- description: Create a node over the openCypher HTTP endpoint, then read nodes back to confirm the write.
  name: Amazon Neptune openCypher Create and Read Node
  slug: amazon-neptune-opencypher-create-and-read-node-workflow
- description: Inspect an openCypher query's execution plan, then run it for real.
  name: Amazon Neptune openCypher Explain then Execute
  slug: amazon-neptune-opencypher-explain-query-workflow
- description: Run an openCypher query via the Data API and inspect the openCypher query queue.
  name: Amazon Neptune openCypher Query with Status Check
  slug: amazon-neptune-opencypher-query-with-status-workflow
- description: Trigger a property graph statistics refresh and read back the updated graph summary counts.
  name: Amazon Neptune Property Graph Statistics Refresh
  slug: amazon-neptune-propertygraph-statistics-refresh-workflow
- description: Read property graph change records from the start of the stream, then continue from the last event id.
  name: Amazon Neptune Property Graph Stream Replay
  slug: amazon-neptune-propertygraph-stream-replay-workflow
- description: Run a SPARQL query via the Data API and inspect the SPARQL query queue.
  name: Amazon Neptune SPARQL Query with Status Check
  slug: amazon-neptune-sparql-query-with-status-workflow
- description: Trigger an RDF statistics refresh and read back the updated triple-store counts.
  name: Amazon Neptune SPARQL Statistics Refresh
  slug: amazon-neptune-sparql-statistics-refresh-workflow
- description: Run a SPARQL INSERT DATA update, then run a SELECT query to confirm the triples landed.
  name: Amazon Neptune SPARQL Update and Verify
  slug: amazon-neptune-sparql-update-and-verify-workflow
artifact_total: 609
collections:
- collection_type: postman
  name: Amazon Neptune Neptune Analytics API
  slug: postman-amazon-neptune-analytics
- collection_type: postman
  name: Amazon Neptune Data API
  slug: postman-amazon-neptune-data
- collection_type: postman
  name: Amazon Neptune Neptune Gremlin API
  slug: postman-amazon-neptune-gremlin
- collection_type: postman
  name: Amazon Neptune Neptune Loader API
  slug: postman-amazon-neptune-loader
- collection_type: postman
  name: Amazon Neptune Management API
  slug: postman-amazon-neptune-management
- collection_type: postman
  name: Amazon Neptune Neptune ML API
  slug: postman-amazon-neptune-ml
- collection_type: postman
  name: Amazon Neptune Neptune openCypher API
  slug: postman-amazon-neptune-opencypher
- collection_type: postman
  name: Amazon Neptune Neptune SPARQL API
  slug: postman-amazon-neptune-sparql
- collection_type: postman
  name: Amazon Neptune Neptune Streams API
  slug: postman-amazon-neptune-streams
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource ?Action=AddTagsToResource API
  slug: open-amazon-neptune-action-addtagstoresource-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource ?Action=ListTagsForResource API
  slug: open-amazon-neptune-action-listtagsforresource-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics API
  slug: open-amazon-neptune-analytics
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Data Processing API
  slug: open-amazon-neptune-data-processing-api
- collection_type: open
  name: Amazon Neptune Data API
  slug: open-amazon-neptune-data
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource DB Clusters API
  slug: open-amazon-neptune-db-clusters-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource DB Instances API
  slug: open-amazon-neptune-db-instances-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Engine API
  slug: open-amazon-neptune-engine-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Events API
  slug: open-amazon-neptune-events-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Global Clusters API
  slug: open-amazon-neptune-global-clusters-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Graph Snapshots API
  slug: open-amazon-neptune-graph-snapshots-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Graphs API
  slug: open-amazon-neptune-graphs-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Gremlin API
  slug: open-amazon-neptune-gremlin-api
- collection_type: open
  name: Amazon Neptune Neptune Gremlin API
  slug: open-amazon-neptune-gremlin
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Import Tasks API
  slug: open-amazon-neptune-import-tasks-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Inference Endpoints API
  slug: open-amazon-neptune-inference-endpoints-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Loader API
  slug: open-amazon-neptune-loader-api
- collection_type: open
  name: Amazon Neptune Neptune Loader API
  slug: open-amazon-neptune-loader
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Maintenance API
  slug: open-amazon-neptune-maintenance-api
- collection_type: open
  name: Amazon Neptune Management API
  slug: open-amazon-neptune-management
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource ML API
  slug: open-amazon-neptune-ml-api
- collection_type: open
  name: Amazon Neptune Neptune ML API
  slug: open-amazon-neptune-ml
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Model Training API
  slug: open-amazon-neptune-model-training-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Model Transform API
  slug: open-amazon-neptune-model-transform-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource openCypher API
  slug: open-amazon-neptune-opencypher-api
- collection_type: open
  name: Amazon Neptune Neptune openCypher API
  slug: open-amazon-neptune-opencypher
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Parameter Groups API
  slug: open-amazon-neptune-parameter-groups-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Private Graph Endpoints API
  slug: open-amazon-neptune-private-graph-endpoints-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Property Graph Stream API
  slug: open-amazon-neptune-property-graph-stream-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Query API
  slug: open-amazon-neptune-query-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Snapshots API
  slug: open-amazon-neptune-snapshots-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource SPARQL API
  slug: open-amazon-neptune-sparql-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource SPARQL Stream API
  slug: open-amazon-neptune-sparql-stream-api
- collection_type: open
  name: Amazon Neptune Neptune SPARQL API
  slug: open-amazon-neptune-sparql
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Status API
  slug: open-amazon-neptune-status-api
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Streams API
  slug: open-amazon-neptune-streams-api
- collection_type: open
  name: Amazon Neptune Neptune Streams API
  slug: open-amazon-neptune-streams
- collection_type: open
  name: Amazon Neptune Neptune Analytics ?Action=AddTagsToResource ?Action=AddTagsToResource Subnet Groups API
  slug: open-amazon-neptune-subnet-groups-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-neptune-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-neptune-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-neptune-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-neptune-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-neptune-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-neptune/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-analytics-cancel-import-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-analytics-create-graph-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-analytics-import-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-analytics-private-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-analytics-reset-graph-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-analytics-snapshot-and-restore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-bulk-loader-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-gremlin-add-and-count-vertices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-gremlin-cancel-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-gremlin-explain-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-gremlin-query-with-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-loader-cancel-running-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-loader-job-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-ml-create-inference-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-ml-dataprocessing-to-training-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-ml-model-transform-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-ml-stop-dataprocessing-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-opencypher-create-and-read-node-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-opencypher-explain-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-opencypher-query-with-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-propertygraph-statistics-refresh-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-propertygraph-stream-replay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-sparql-query-with-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-sparql-statistics-refresh-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-neptune-sparql-update-and-verify-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/neptune/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/neptune/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/neptune/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/category/database/amazon-neptune/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/neptune/latest/userguide/doc-history.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/
- group: operate
  title: ''
  type: Support
  url: https://repost.aws/tags/TAxVAEdWg1SrS0lClUSX-m_Q
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: Community
  url: https://repost.aws/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/neptune/
- group: start
  title: ''
  type: Login
  url: https://console.aws.amazon.com/neptune/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/neptune/faqs/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/neptune/latest/userguide/security.html
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://aws.amazon.com/neptune/sla/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/neptune/
- group: build
  title: ''
  type: GitHub Samples
  url: https://github.com/aws-samples/amazon-neptune-samples
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/neptune/latest/userguide/using-neptune-apis.html
- group: build
  title: ''
  type: Tools
  url: https://github.com/awslabs/amazon-neptune-tools
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/neptune/pricing/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-neptune-context.jsonld
- group: docs
  title: DB Cluster Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-db-cluster-schema.json
- group: docs
  title: DB Instance Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-db-instance-schema.json
- group: docs
  title: Graph Element Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-graph-element-schema.json
- group: docs
  title: Loader Job Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-loader-job-schema.json
- group: docs
  title: Stream Record Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-stream-record-schema.json
- group: docs
  title: Analytics Graph Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-analytics-graph-schema.json
- group: docs
  title: ML Job Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-ml-job-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-neptune-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-neptune-vocabulary.yaml
- group: design
  title: Analytics Context
  type: JSONLD
  url: json-ld/amazon-neptune-analytics-context.jsonld
- group: design
  title: Data Context
  type: JSONLD
  url: json-ld/amazon-neptune-data-context.jsonld
- group: design
  title: Gremlin Context
  type: JSONLD
  url: json-ld/amazon-neptune-gremlin-context.jsonld
- group: design
  title: Loader Context
  type: JSONLD
  url: json-ld/amazon-neptune-loader-context.jsonld
- group: design
  title: Management Context
  type: JSONLD
  url: json-ld/amazon-neptune-management-context.jsonld
- group: design
  title: Ml Context
  type: JSONLD
  url: json-ld/amazon-neptune-ml-context.jsonld
- group: design
  title: Opencypher Context
  type: JSONLD
  url: json-ld/amazon-neptune-opencypher-context.jsonld
- group: design
  title: Sparql Context
  type: JSONLD
  url: json-ld/amazon-neptune-sparql-context.jsonld
- group: design
  title: Streams Context
  type: JSONLD
  url: json-ld/amazon-neptune-streams-context.jsonld
created: '2024'
description: Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. It supports property graph and RDF models, with multiple query languages including Gremlin, SPARQL, and openCypher.
examples:
- key_count: 15
  name: Amazon Neptune Analytics Graph Example
  slug: amazon-neptune-analytics-graph-example
- key_count: 6
  name: Amazon Neptune Cancelbulkloadjob Example
  slug: amazon-neptune-cancelbulkloadjob-example
- key_count: 6
  name: Amazon Neptune Createdataprocessingjob Example
  slug: amazon-neptune-createdataprocessingjob-example
- key_count: 6
  name: Amazon Neptune Createdbcluster Example
  slug: amazon-neptune-createdbcluster-example
- key_count: 6
  name: Amazon Neptune Createdbclustersnapshot Example
  slug: amazon-neptune-createdbclustersnapshot-example
- key_count: 6
  name: Amazon Neptune Createdbinstance Example
  slug: amazon-neptune-createdbinstance-example
- key_count: 6
  name: Amazon Neptune Createdbsubnetgroup Example
  slug: amazon-neptune-createdbsubnetgroup-example
- key_count: 6
  name: Amazon Neptune Creategraph Example
  slug: amazon-neptune-creategraph-example
- key_count: 6
  name: Amazon Neptune Creategraphsnapshot Example
  slug: amazon-neptune-creategraphsnapshot-example
- key_count: 6
  name: Amazon Neptune Creategraphusingimporttask Example
  slug: amazon-neptune-creategraphusingimporttask-example
- key_count: 6
  name: Amazon Neptune Createinferenceendpoint Example
  slug: amazon-neptune-createinferenceendpoint-example
- key_count: 6
  name: Amazon Neptune Createmlendpoint Example
  slug: amazon-neptune-createmlendpoint-example
- key_count: 6
  name: Amazon Neptune Createmodeltrainingjob Example
  slug: amazon-neptune-createmodeltrainingjob-example
- key_count: 6
  name: Amazon Neptune Createmodeltransformjob Example
  slug: amazon-neptune-createmodeltransformjob-example
- key_count: 6
  name: Amazon Neptune Createprivategraphendpoint Example
  slug: amazon-neptune-createprivategraphendpoint-example
- key_count: 15
  name: Amazon Neptune Db Cluster Example
  slug: amazon-neptune-db-cluster-example
- key_count: 15
  name: Amazon Neptune Db Instance Example
  slug: amazon-neptune-db-instance-example
- key_count: 6
  name: Amazon Neptune Deletedbcluster Example
  slug: amazon-neptune-deletedbcluster-example
- key_count: 6
  name: Amazon Neptune Deletedbinstance Example
  slug: amazon-neptune-deletedbinstance-example
- key_count: 6
  name: Amazon Neptune Deletegraph Example
  slug: amazon-neptune-deletegraph-example
- key_count: 6
  name: Amazon Neptune Describedbclusters Example
  slug: amazon-neptune-describedbclusters-example
- key_count: 6
  name: Amazon Neptune Describedbclustersnapshots Example
  slug: amazon-neptune-describedbclustersnapshots-example
- key_count: 6
  name: Amazon Neptune Describedbinstances Example
  slug: amazon-neptune-describedbinstances-example
- key_count: 6
  name: Amazon Neptune Describedbsubnetgroups Example
  slug: amazon-neptune-describedbsubnetgroups-example
- key_count: 6
  name: Amazon Neptune Executegremlinquery Example
  slug: amazon-neptune-executegremlinquery-example
- key_count: 6
  name: Amazon Neptune Executegremlintraversal Example
  slug: amazon-neptune-executegremlintraversal-example
- key_count: 6
  name: Amazon Neptune Executegremlintraversalget Example
  slug: amazon-neptune-executegremlintraversalget-example
- key_count: 6
  name: Amazon Neptune Executeopencypherquery Example
  slug: amazon-neptune-executeopencypherquery-example
- key_count: 6
  name: Amazon Neptune Executeopencypherqueryget Example
  slug: amazon-neptune-executeopencypherqueryget-example
- key_count: 6
  name: Amazon Neptune Executesparqlquery Example
  slug: amazon-neptune-executesparqlquery-example
- key_count: 6
  name: Amazon Neptune Failoverdbcluster Example
  slug: amazon-neptune-failoverdbcluster-example
- key_count: 6
  name: Amazon Neptune Getbulkloadjobstatus Example
  slug: amazon-neptune-getbulkloadjobstatus-example
- key_count: 6
  name: Amazon Neptune Getdataprocessingjobstatus Example
  slug: amazon-neptune-getdataprocessingjobstatus-example
- key_count: 6
  name: Amazon Neptune Getenginestatus Example
  slug: amazon-neptune-getenginestatus-example
- key_count: 6
  name: Amazon Neptune Getgraph Example
  slug: amazon-neptune-getgraph-example
- key_count: 6
  name: Amazon Neptune Getgraphsnapshot Example
  slug: amazon-neptune-getgraphsnapshot-example
- key_count: 6
  name: Amazon Neptune Getgremlinquerystatus Example
  slug: amazon-neptune-getgremlinquerystatus-example
- key_count: 6
  name: Amazon Neptune Getgremlinquerystatusbyid Example
  slug: amazon-neptune-getgremlinquerystatusbyid-example
- key_count: 6
  name: Amazon Neptune Getimporttask Example
  slug: amazon-neptune-getimporttask-example
- key_count: 6
  name: Amazon Neptune Getinferenceendpointstatus Example
  slug: amazon-neptune-getinferenceendpointstatus-example
- key_count: 6
  name: Amazon Neptune Getloaderjobstatus Example
  slug: amazon-neptune-getloaderjobstatus-example
- key_count: 6
  name: Amazon Neptune Getmldataprocessingjobstatus Example
  slug: amazon-neptune-getmldataprocessingjobstatus-example
- key_count: 6
  name: Amazon Neptune Getmlendpointstatus Example
  slug: amazon-neptune-getmlendpointstatus-example
- key_count: 6
  name: Amazon Neptune Getmlmodeltrainingjobstatus Example
  slug: amazon-neptune-getmlmodeltrainingjobstatus-example
- key_count: 6
  name: Amazon Neptune Getmlmodeltransformjobstatus Example
  slug: amazon-neptune-getmlmodeltransformjobstatus-example
- key_count: 6
  name: Amazon Neptune Getmodeltrainingjobstatus Example
  slug: amazon-neptune-getmodeltrainingjobstatus-example
- key_count: 6
  name: Amazon Neptune Getmodeltransformjobstatus Example
  slug: amazon-neptune-getmodeltransformjobstatus-example
- key_count: 6
  name: Amazon Neptune Getopencypherquerystatus Example
  slug: amazon-neptune-getopencypherquerystatus-example
- key_count: 6
  name: Amazon Neptune Getopencypherquerystatusbyid Example
  slug: amazon-neptune-getopencypherquerystatusbyid-example
- key_count: 6
  name: Amazon Neptune Getprivategraphendpoint Example
  slug: amazon-neptune-getprivategraphendpoint-example
- key_count: 6
  name: Amazon Neptune Getpropertygraphstatistics Example
  slug: amazon-neptune-getpropertygraphstatistics-example
- key_count: 6
  name: Amazon Neptune Getpropertygraphstream Example
  slug: amazon-neptune-getpropertygraphstream-example
- key_count: 6
  name: Amazon Neptune Getpropertygraphstreamalias Example
  slug: amazon-neptune-getpropertygraphstreamalias-example
- key_count: 6
  name: Amazon Neptune Getsparqlquerystatus Example
  slug: amazon-neptune-getsparqlquerystatus-example
- key_count: 6
  name: Amazon Neptune Getsparqlquerystatusbyid Example
  slug: amazon-neptune-getsparqlquerystatusbyid-example
- key_count: 6
  name: Amazon Neptune Getsparqlstatistics Example
  slug: amazon-neptune-getsparqlstatistics-example
- key_count: 6
  name: Amazon Neptune Getsparqlstream Example
  slug: amazon-neptune-getsparqlstream-example
- key_count: 0
  name: Amazon Neptune Graph Element Example
  slug: amazon-neptune-graph-element-example
- key_count: 6
  name: Amazon Neptune Listbulkloadjobs Example
  slug: amazon-neptune-listbulkloadjobs-example
- key_count: 6
  name: Amazon Neptune Listdataprocessingjobs Example
  slug: amazon-neptune-listdataprocessingjobs-example
- key_count: 6
  name: Amazon Neptune Listgraphs Example
  slug: amazon-neptune-listgraphs-example
- key_count: 6
  name: Amazon Neptune Listgraphsnapshots Example
  slug: amazon-neptune-listgraphsnapshots-example
- key_count: 6
  name: Amazon Neptune Listimporttasks Example
  slug: amazon-neptune-listimporttasks-example
- key_count: 6
  name: Amazon Neptune Listinferenceendpoints Example
  slug: amazon-neptune-listinferenceendpoints-example
- key_count: 6
  name: Amazon Neptune Listloaderjobs Example
  slug: amazon-neptune-listloaderjobs-example
- key_count: 6
  name: Amazon Neptune Listmldataprocessingjobs Example
  slug: amazon-neptune-listmldataprocessingjobs-example
- key_count: 6
  name: Amazon Neptune Listmlmodeltrainingjobs Example
  slug: amazon-neptune-listmlmodeltrainingjobs-example
- key_count: 6
  name: Amazon Neptune Listmodeltrainingjobs Example
  slug: amazon-neptune-listmodeltrainingjobs-example
- key_count: 6
  name: Amazon Neptune Listmodeltransformjobs Example
  slug: amazon-neptune-listmodeltransformjobs-example
- key_count: 12
  name: Amazon Neptune Loader Job Example
  slug: amazon-neptune-loader-job-example
- key_count: 0
  name: Amazon Neptune Ml Job Example
  slug: amazon-neptune-ml-job-example
- key_count: 6
  name: Amazon Neptune Modifydbcluster Example
  slug: amazon-neptune-modifydbcluster-example
- key_count: 6
  name: Amazon Neptune Modifydbinstance Example
  slug: amazon-neptune-modifydbinstance-example
- key_count: 6
  name: Amazon Neptune Rebootdbinstance Example
  slug: amazon-neptune-rebootdbinstance-example
- key_count: 6
  name: Amazon Neptune Resetgraph Example
  slug: amazon-neptune-resetgraph-example
- key_count: 6
  name: Amazon Neptune Restoredbclusterfromsnapshot Example
  slug: amazon-neptune-restoredbclusterfromsnapshot-example
- key_count: 6
  name: Amazon Neptune Restoregraphfromsnapshot Example
  slug: amazon-neptune-restoregraphfromsnapshot-example
- key_count: 6
  name: Amazon Neptune Startbulkloadjob Example
  slug: amazon-neptune-startbulkloadjob-example
- key_count: 6
  name: Amazon Neptune Startdbcluster Example
  slug: amazon-neptune-startdbcluster-example
- key_count: 6
  name: Amazon Neptune Startloaderjob Example
  slug: amazon-neptune-startloaderjob-example
- key_count: 6
  name: Amazon Neptune Startmldataprocessingjob Example
  slug: amazon-neptune-startmldataprocessingjob-example
- key_count: 6
  name: Amazon Neptune Startmlmodeltrainingjob Example
  slug: amazon-neptune-startmlmodeltrainingjob-example
- key_count: 6
  name: Amazon Neptune Startmlmodeltransformjob Example
  slug: amazon-neptune-startmlmodeltransformjob-example
- key_count: 6
  name: Amazon Neptune Stopdbcluster Example
  slug: amazon-neptune-stopdbcluster-example
- key_count: 5
  name: Amazon Neptune Stream Record Example
  slug: amazon-neptune-stream-record-example
- key_count: 6
  name: Amazon Neptune Updategraph Example
  slug: amazon-neptune-updategraph-example
- key_count: 8
  name: Analytics Create Graph Input Example
  slug: analytics-create-graph-input-example
- key_count: 3
  name: Analytics Create Graph Snapshot Input Example
  slug: analytics-create-graph-snapshot-input-example
- key_count: 12
  name: Analytics Create Graph Using Import Task Input Example
  slug: analytics-create-graph-using-import-task-input-example
- key_count: 3
  name: Analytics Create Private Graph Endpoint Input Example
  slug: analytics-create-private-graph-endpoint-input-example
- key_count: 15
  name: Analytics Graph Output Example
  slug: analytics-graph-output-example
- key_count: 7
  name: Analytics Graph Snapshot Output Example
  slug: analytics-graph-snapshot-output-example
- key_count: 8
  name: Analytics Import Task Output Example
  slug: analytics-import-task-output-example
- key_count: 2
  name: Analytics List Graph Snapshots Output Example
  slug: analytics-list-graph-snapshots-output-example
- key_count: 2
  name: Analytics List Graphs Output Example
  slug: analytics-list-graphs-output-example
- key_count: 2
  name: Analytics List Import Tasks Output Example
  slug: analytics-list-import-tasks-output-example
- key_count: 4
  name: Analytics Private Graph Endpoint Output Example
  slug: analytics-private-graph-endpoint-output-example
- key_count: 6
  name: Analytics Restore Graph From Snapshot Input Example
  slug: analytics-restore-graph-from-snapshot-input-example
- key_count: 3
  name: Analytics Update Graph Input Example
  slug: analytics-update-graph-input-example
- key_count: 9
  name: Data Create Ml Endpoint Input Example
  slug: data-create-ml-endpoint-input-example
- key_count: 10
  name: Data Engine Status Output Example
  slug: data-engine-status-output-example
- key_count: 5
  name: Data Execute Gremlin Profile Input Example
  slug: data-execute-gremlin-profile-input-example
- key_count: 1
  name: Data Execute Gremlin Query Input Example
  slug: data-execute-gremlin-query-input-example
- key_count: 3
  name: Data Execute Gremlin Query Output Example
  slug: data-execute-gremlin-query-output-example
- key_count: 3
  name: Data Execute Open Cypher Explain Input Example
  slug: data-execute-open-cypher-explain-input-example
- key_count: 2
  name: Data Execute Open Cypher Query Input Example
  slug: data-execute-open-cypher-query-input-example
- key_count: 1
  name: Data Execute Open Cypher Query Output Example
  slug: data-execute-open-cypher-query-output-example
- key_count: 2
  name: Data Execute Sparql Query Input Example
  slug: data-execute-sparql-query-input-example
- key_count: 3
  name: Data Gremlin Query Status Example
  slug: data-gremlin-query-status-example
- key_count: 3
  name: Data Gremlin Query Status Output Example
  slug: data-gremlin-query-status-output-example
- key_count: 2
  name: Data Loader Job Status Output Example
  slug: data-loader-job-status-output-example
- key_count: 4
  name: Data Ml Endpoint Status Output Example
  slug: data-ml-endpoint-status-output-example
- key_count: 3
  name: Data Ml Job Status Output Example
  slug: data-ml-job-status-output-example
- key_count: 3
  name: Data Open Cypher Query Status Output Example
  slug: data-open-cypher-query-status-output-example
- key_count: 2
  name: Data Propertygraph Statistics Output Example
  slug: data-propertygraph-statistics-output-example
- key_count: 5
  name: Data Propertygraph Stream Output Example
  slug: data-propertygraph-stream-output-example
- key_count: 5
  name: Data Propertygraph Stream Record Example
  slug: data-propertygraph-stream-record-example
- key_count: 2
  name: Data Sparql Query Output Example
  slug: data-sparql-query-output-example
- key_count: 2
  name: Data Sparql Statistics Output Example
  slug: data-sparql-statistics-output-example
- key_count: 5
  name: Data Sparql Stream Output Example
  slug: data-sparql-stream-output-example
- key_count: 12
  name: Data Start Loader Job Input Example
  slug: data-start-loader-job-input-example
- key_count: 2
  name: Data Start Loader Job Output Example
  slug: data-start-loader-job-output-example
- key_count: 15
  name: Data Start Ml Data Processing Job Input Example
  slug: data-start-ml-data-processing-job-input-example
- key_count: 15
  name: Data Start Ml Model Training Job Input Example
  slug: data-start-ml-model-training-job-input-example
- key_count: 15
  name: Data Start Ml Model Transform Job Input Example
  slug: data-start-ml-model-transform-job-input-example
- key_count: 3
  name: Gremlin Gremlin Error Response Example
  slug: gremlin-gremlin-error-response-example
- key_count: 1
  name: Gremlin Gremlin Query Request Example
  slug: gremlin-gremlin-query-request-example
- key_count: 3
  name: Gremlin Gremlin Query Response Example
  slug: gremlin-gremlin-query-response-example
- key_count: 3
  name: Gremlin Gremlin Query Status Detail Example
  slug: gremlin-gremlin-query-status-detail-example
- key_count: 3
  name: Gremlin Gremlin Query Status List Example
  slug: gremlin-gremlin-query-status-list-example
- key_count: 3
  name: Loader Loader Error Response Example
  slug: loader-loader-error-response-example
- key_count: 2
  name: Loader Loader List Response Example
  slug: loader-loader-list-response-example
- key_count: 12
  name: Loader Loader Request Example
  slug: loader-loader-request-example
- key_count: 2
  name: Loader Loader Start Response Example
  slug: loader-loader-start-response-example
- key_count: 2
  name: Loader Loader Status Response Example
  slug: loader-loader-status-response-example
- key_count: 13
  name: Management Create Db Cluster Request Example
  slug: management-create-db-cluster-request-example
- key_count: 8
  name: Management Create Db Instance Request Example
  slug: management-create-db-instance-request-example
- key_count: 15
  name: Management Db Cluster Example
  slug: management-db-cluster-example
- key_count: 4
  name: Management Db Cluster Member Example
  slug: management-db-cluster-member-example
- key_count: 2
  name: Management Db Cluster Role Example
  slug: management-db-cluster-role-example
- key_count: 13
  name: Management Db Cluster Snapshot Example
  slug: management-db-cluster-snapshot-example
- key_count: 14
  name: Management Db Instance Example
  slug: management-db-instance-example
- key_count: 6
  name: Management Db Subnet Group Example
  slug: management-db-subnet-group-example
- key_count: 2
  name: Management Describe Db Cluster Snapshots Response Example
  slug: management-describe-db-cluster-snapshots-response-example
- key_count: 2
  name: Management Describe Db Clusters Response Example
  slug: management-describe-db-clusters-response-example
- key_count: 2
  name: Management Describe Db Instances Response Example
  slug: management-describe-db-instances-response-example
- key_count: 2
  name: Management Describe Db Subnet Groups Response Example
  slug: management-describe-db-subnet-groups-response-example
- key_count: 11
  name: Management Modify Db Cluster Request Example
  slug: management-modify-db-cluster-request-example
- key_count: 7
  name: Management Modify Db Instance Request Example
  slug: management-modify-db-instance-request-example
- key_count: 9
  name: Management Restore Db Cluster From Snapshot Request Example
  slug: management-restore-db-cluster-from-snapshot-request-example
- key_count: 15
  name: Ml Create Data Processing Job Request Example
  slug: ml-create-data-processing-job-request-example
- key_count: 9
  name: Ml Create Inference Endpoint Request Example
  slug: ml-create-inference-endpoint-request-example
- key_count: 15
  name: Ml Create Model Training Job Request Example
  slug: ml-create-model-training-job-request-example
- key_count: 15
  name: Ml Create Model Transform Job Request Example
  slug: ml-create-model-transform-job-request-example
- key_count: 1
  name: Ml Endpoint Created Response Example
  slug: ml-endpoint-created-response-example
- key_count: 1
  name: Ml Endpoint List Response Example
  slug: ml-endpoint-list-response-example
- key_count: 5
  name: Ml Endpoint Status Response Example
  slug: ml-endpoint-status-response-example
- key_count: 1
  name: Ml Job Created Response Example
  slug: ml-job-created-response-example
- key_count: 1
  name: Ml Job List Response Example
  slug: ml-job-list-response-example
- key_count: 3
  name: Ml Job Status Response Example
  slug: ml-job-status-response-example
- key_count: 3
  name: Opencypher Open Cypher Error Response Example
  slug: opencypher-open-cypher-error-response-example
- key_count: 4
  name: Opencypher Open Cypher Node Example
  slug: opencypher-open-cypher-node-example
- key_count: 1
  name: Opencypher Open Cypher Query Request Example
  slug: opencypher-open-cypher-query-request-example
- key_count: 1
  name: Opencypher Open Cypher Query Response Example
  slug: opencypher-open-cypher-query-response-example
- key_count: 3
  name: Opencypher Open Cypher Query Status Detail Example
  slug: opencypher-open-cypher-query-status-detail-example
- key_count: 3
  name: Opencypher Open Cypher Query Status List Example
  slug: opencypher-open-cypher-query-status-list-example
- key_count: 6
  name: Opencypher Open Cypher Relationship Example
  slug: opencypher-open-cypher-relationship-example
- key_count: 3
  name: Sparql Sparql Error Response Example
  slug: sparql-sparql-error-response-example
- key_count: 3
  name: Sparql Sparql Query Status Detail Example
  slug: sparql-sparql-query-status-detail-example
- key_count: 3
  name: Sparql Sparql Query Status List Example
  slug: sparql-sparql-query-status-list-example
- key_count: 4
  name: Sparql Sparql Request Body Example
  slug: sparql-sparql-request-body-example
- key_count: 3
  name: Sparql Sparql Select Response Example
  slug: sparql-sparql-select-response-example
- key_count: 6
  name: Streams Property Graph Data Example
  slug: streams-property-graph-data-example
- key_count: 5
  name: Streams Property Graph Stream Record Example
  slug: streams-property-graph-stream-record-example
- key_count: 5
  name: Streams Property Graph Stream Response Example
  slug: streams-property-graph-stream-response-example
- key_count: 5
  name: Streams Sparql Stream Record Example
  slug: streams-sparql-stream-record-example
- key_count: 5
  name: Streams Sparql Stream Response Example
  slug: streams-sparql-stream-response-example
- key_count: 2
  name: Streams Stream Event Id Example
  slug: streams-stream-event-id-example
features:
- description: Automatically scales compute and memory resources based on workload demands without requiring capacity planning.
  name: Serverless Graph Database
- description: Supports Apache TinkerPop Gremlin, openCypher, and SPARQL 1.1 query languages for property graph and RDF models.
  name: Multiple Query Language Support
- description: Multi-AZ deployment with up to 15 read replicas, automated failover, and continuous backups with point-in-time recovery up to 35 days.
  name: High Availability
- description: Multi-region replication with sub-second latency across up to five secondary clusters for global applications.
  name: Global Database
- description: Memory-optimized graph analytics engine for analyzing tens of billions of relationships within seconds with vector search capabilities.
  name: Neptune Analytics
- description: Fully managed GraphRAG with Amazon Bedrock Knowledge Bases for AI-enhanced graph retrieval augmented generation.
  name: GraphRAG Support
- description: Native graph neural network support via Neptune ML powered by Amazon SageMaker for link prediction and node classification.
  name: Machine Learning on Graphs
- description: Full ACID transaction support ensuring data consistency and integrity across graph operations.
  name: ACID Transactions
- description: VPC network isolation, IAM resource permissions, AWS KMS encryption, TLS in-transit encryption, and CloudWatch audit logging.
  name: AWS Security Integration
- description: Storage automatically grows up to 128 TiB with self-healing architecture spanning three availability zones.
  name: Auto-Expanding Storage
finops:
- name: Amazon Neptune Finops
  service_category: Database / Graph
  slug: amazon-neptune-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Neptune Analytics Graph
  property_count: 17
  slug: amazon-neptune-analytics-graph
- name: CreateDataProcessingJobRequest
  property_count: 16
  slug: amazon-neptune-createdataprocessingjobrequest
- name: CreateDBClusterRequest
  property_count: 13
  slug: amazon-neptune-createdbclusterrequest
- name: CreateDBInstanceRequest
  property_count: 8
  slug: amazon-neptune-createdbinstancerequest
- name: CreateGraphInput
  property_count: 8
  slug: amazon-neptune-creategraphinput
- name: CreateGraphSnapshotInput
  property_count: 3
  slug: amazon-neptune-creategraphsnapshotinput
- name: CreateGraphUsingImportTaskInput
  property_count: 12
  slug: amazon-neptune-creategraphusingimporttaskinput
- name: CreateInferenceEndpointRequest
  property_count: 9
  slug: amazon-neptune-createinferenceendpointrequest
- name: CreateMLEndpointInput
  property_count: 9
  slug: amazon-neptune-createmlendpointinput
- name: CreateModelTrainingJobRequest
  property_count: 20
  slug: amazon-neptune-createmodeltrainingjobrequest
- name: CreateModelTransformJobRequest
  property_count: 15
  slug: amazon-neptune-createmodeltransformjobrequest
- name: CreatePrivateGraphEndpointInput
  property_count: 3
  slug: amazon-neptune-createprivategraphendpointinput
- name: Amazon Neptune DB Cluster
  property_count: 27
  slug: amazon-neptune-db-cluster
- name: Amazon Neptune DB Instance
  property_count: 21
  slug: amazon-neptune-db-instance
- name: DBCluster
  property_count: 22
  slug: amazon-neptune-dbcluster
- name: DBClusterMember
  property_count: 4
  slug: amazon-neptune-dbclustermember
- name: DBClusterRole
  property_count: 2
  slug: amazon-neptune-dbclusterrole
- name: DBClusterSnapshot
  property_count: 13
  slug: amazon-neptune-dbclustersnapshot
- name: DBInstance
  property_count: 14
  slug: amazon-neptune-dbinstance
- name: DBSubnetGroup
  property_count: 6
  slug: amazon-neptune-dbsubnetgroup
- name: DescribeDBClusterSnapshotsResponse
  property_count: 2
  slug: amazon-neptune-describedbclustersnapshotsresponse
- name: DescribeDBClustersResponse
  property_count: 2
  slug: amazon-neptune-describedbclustersresponse
- name: DescribeDBInstancesResponse
  property_count: 2
  slug: amazon-neptune-describedbinstancesresponse
- name: DescribeDBSubnetGroupsResponse
  property_count: 2
  slug: amazon-neptune-describedbsubnetgroupsresponse
- name: EndpointCreatedResponse
  property_count: 1
  slug: amazon-neptune-endpointcreatedresponse
- name: EndpointListResponse
  property_count: 1
  slug: amazon-neptune-endpointlistresponse
- name: EndpointStatusResponse
  property_count: 5
  slug: amazon-neptune-endpointstatusresponse
- name: EngineStatusOutput
  property_count: 10
  slug: amazon-neptune-enginestatusoutput
- name: ErrorResponse
  property_count: 3
  slug: amazon-neptune-errorresponse
- name: ExecuteGremlinProfileInput
  property_count: 5
  slug: amazon-neptune-executegremlinprofileinput
- name: ExecuteGremlinQueryInput
  property_count: 1
  slug: amazon-neptune-executegremlinqueryinput
- name: ExecuteGremlinQueryOutput
  property_count: 3
  slug: amazon-neptune-executegremlinqueryoutput
- name: ExecuteOpenCypherExplainInput
  property_count: 3
  slug: amazon-neptune-executeopencypherexplaininput
- name: ExecuteOpenCypherQueryInput
  property_count: 2
  slug: amazon-neptune-executeopencypherqueryinput
- name: ExecuteOpenCypherQueryOutput
  property_count: 1
  slug: amazon-neptune-executeopencypherqueryoutput
- name: ExecuteSparqlQueryInput
  property_count: 2
  slug: amazon-neptune-executesparqlqueryinput
- name: Amazon Neptune Graph Element
  property_count: 0
  slug: amazon-neptune-graph-element
- name: GraphOutput
  property_count: 15
  slug: amazon-neptune-graphoutput
- name: GraphSnapshotOutput
  property_count: 7
  slug: amazon-neptune-graphsnapshotoutput
- name: GremlinErrorResponse
  property_count: 3
  slug: amazon-neptune-gremlinerrorresponse
- name: GremlinQueryRequest
  property_count: 1
  slug: amazon-neptune-gremlinqueryrequest
- name: GremlinQueryResponse
  property_count: 3
  slug: amazon-neptune-gremlinqueryresponse
- name: GremlinQueryStatus
  property_count: 3
  slug: amazon-neptune-gremlinquerystatus
- name: GremlinQueryStatusDetail
  property_count: 3
  slug: amazon-neptune-gremlinquerystatusdetail
- name: GremlinQueryStatusList
  property_count: 3
  slug: amazon-neptune-gremlinquerystatuslist
- name: GremlinQueryStatusOutput
  property_count: 3
  slug: amazon-neptune-gremlinquerystatusoutput
- name: ImportTaskOutput
  property_count: 8
  slug: amazon-neptune-importtaskoutput
- name: JobCreatedResponse
  property_count: 1
  slug: amazon-neptune-jobcreatedresponse
- name: JobListResponse
  property_count: 1
  slug: amazon-neptune-joblistresponse
- name: JobStatusResponse
  property_count: 3
  slug: amazon-neptune-jobstatusresponse
- name: ListGraphSnapshotsOutput
  property_count: 2
  slug: amazon-neptune-listgraphsnapshotsoutput
- name: ListGraphsOutput
  property_count: 2
  slug: amazon-neptune-listgraphsoutput
- name: ListImportTasksOutput
  property_count: 2
  slug: amazon-neptune-listimporttasksoutput
- name: Amazon Neptune Loader Job
  property_count: 12
  slug: amazon-neptune-loader-job
- name: LoaderErrorResponse
  property_count: 3
  slug: amazon-neptune-loadererrorresponse
- name: LoaderJobStatusOutput
  property_count: 2
  slug: amazon-neptune-loaderjobstatusoutput
- name: LoaderListResponse
  property_count: 2
  slug: amazon-neptune-loaderlistresponse
- name: LoaderRequest
  property_count: 12
  slug: amazon-neptune-loaderrequest
- name: LoaderStartResponse
  property_count: 2
  slug: amazon-neptune-loaderstartresponse
- name: LoaderStatusResponse
  property_count: 2
  slug: amazon-neptune-loaderstatusresponse
- name: Amazon Neptune ML Job
  property_count: 0
  slug: amazon-neptune-ml-job
- name: MLEndpointStatusOutput
  property_count: 4
  slug: amazon-neptune-mlendpointstatusoutput
- name: MLJobStatusOutput
  property_count: 3
  slug: amazon-neptune-mljobstatusoutput
- name: ModifyDBClusterRequest
  property_count: 11
  slug: amazon-neptune-modifydbclusterrequest
- name: ModifyDBInstanceRequest
  property_count: 7
  slug: amazon-neptune-modifydbinstancerequest
- name: OpenCypherErrorResponse
  property_count: 3
  slug: amazon-neptune-opencyphererrorresponse
- name: OpenCypherNode
  property_count: 4
  slug: amazon-neptune-opencyphernode
- name: OpenCypherQueryRequest
  property_count: 1
  slug: amazon-neptune-opencypherqueryrequest
- name: OpenCypherQueryResponse
  property_count: 1
  slug: amazon-neptune-opencypherqueryresponse
- name: OpenCypherQueryStatusDetail
  property_count: 3
  slug: amazon-neptune-opencypherquerystatusdetail
- name: OpenCypherQueryStatusList
  property_count: 3
  slug: amazon-neptune-opencypherquerystatuslist
- name: OpenCypherQueryStatusOutput
  property_count: 3
  slug: amazon-neptune-opencypherquerystatusoutput
- name: OpenCypherRelationship
  property_count: 6
  slug: amazon-neptune-opencypherrelationship
- name: PrivateGraphEndpointOutput
  property_count: 4
  slug: amazon-neptune-privategraphendpointoutput
- name: PropertyGraphData
  property_count: 6
  slug: amazon-neptune-propertygraphdata
- name: PropertygraphStatisticsOutput
  property_count: 2
  slug: amazon-neptune-propertygraphstatisticsoutput
- name: PropertygraphStreamOutput
  property_count: 5
  slug: amazon-neptune-propertygraphstreamoutput
- name: PropertygraphStreamRecord
  property_count: 5
  slug: amazon-neptune-propertygraphstreamrecord
- name: PropertyGraphStreamResponse
  property_count: 5
  slug: amazon-neptune-propertygraphstreamresponse
- name: RestoreDBClusterFromSnapshotRequest
  property_count: 9
  slug: amazon-neptune-restoredbclusterfromsnapshotrequest
- name: RestoreGraphFromSnapshotInput
  property_count: 6
  slug: amazon-neptune-restoregraphfromsnapshotinput
- name: SparqlErrorResponse
  property_count: 3
  slug: amazon-neptune-sparqlerrorresponse
- name: SparqlQueryOutput
  property_count: 2
  slug: amazon-neptune-sparqlqueryoutput
- name: SparqlQueryStatusDetail
  property_count: 3
  slug: amazon-neptune-sparqlquerystatusdetail
- name: SparqlQueryStatusList
  property_count: 3
  slug: amazon-neptune-sparqlquerystatuslist
- name: SparqlRequestBody
  property_count: 4
  slug: amazon-neptune-sparqlrequestbody
- name: SparqlSelectResponse
  property_count: 3
  slug: amazon-neptune-sparqlselectresponse
- name: SparqlStatisticsOutput
  property_count: 2
  slug: amazon-neptune-sparqlstatisticsoutput
- name: SparqlStreamOutput
  property_count: 5
  slug: amazon-neptune-sparqlstreamoutput
- name: SparqlStreamRecord
  property_count: 5
  slug: amazon-neptune-sparqlstreamrecord
- name: SparqlStreamResponse
  property_count: 5
  slug: amazon-neptune-sparqlstreamresponse
- name: StartLoaderJobInput
  property_count: 12
  slug: amazon-neptune-startloaderjobinput
- name: StartLoaderJobOutput
  property_count: 2
  slug: amazon-neptune-startloaderjoboutput
- name: StartMLDataProcessingJobInput
  property_count: 16
  slug: amazon-neptune-startmldataprocessingjobinput
- name: StartMLModelTrainingJobInput
  property_count: 20
  slug: amazon-neptune-startmlmodeltrainingjobinput
- name: StartMLModelTransformJobInput
  property_count: 15
  slug: amazon-neptune-startmlmodeltransformjobinput
- name: Amazon Neptune Stream Record
  property_count: 5
  slug: amazon-neptune-stream-record
- name: StreamEventId
  property_count: 2
  slug: amazon-neptune-streameventid
- name: UpdateGraphInput
  property_count: 3
  slug: amazon-neptune-updategraphinput
- name: CreateGraphInput
  property_count: 8
  slug: analytics-create-graph-input
- name: CreateGraphSnapshotInput
  property_count: 3
  slug: analytics-create-graph-snapshot-input
- name: CreateGraphUsingImportTaskInput
  property_count: 12
  slug: analytics-create-graph-using-import-task-input
- name: CreatePrivateGraphEndpointInput
  property_count: 3
  slug: analytics-create-private-graph-endpoint-input
- name: GraphOutput
  property_count: 15
  slug: analytics-graph-output
- name: GraphSnapshotOutput
  property_count: 7
  slug: analytics-graph-snapshot-output
- name: ImportTaskOutput
  property_count: 8
  slug: analytics-import-task-output
- name: ListGraphSnapshotsOutput
  property_count: 2
  slug: analytics-list-graph-snapshots-output
- name: ListGraphsOutput
  property_count: 2
  slug: analytics-list-graphs-output
- name: ListImportTasksOutput
  property_count: 2
  slug: analytics-list-import-tasks-output
- name: PrivateGraphEndpointOutput
  property_count: 4
  slug: analytics-private-graph-endpoint-output
- name: RestoreGraphFromSnapshotInput
  property_count: 6
  slug: analytics-restore-graph-from-snapshot-input
- name: UpdateGraphInput
  property_count: 3
  slug: analytics-update-graph-input
- name: CreateMLEndpointInput
  property_count: 9
  slug: data-create-ml-endpoint-input
- name: EngineStatusOutput
  property_count: 10
  slug: data-engine-status-output
- name: ExecuteGremlinProfileInput
  property_count: 5
  slug: data-execute-gremlin-profile-input
- name: ExecuteGremlinQueryInput
  property_count: 1
  slug: data-execute-gremlin-query-input
- name: ExecuteGremlinQueryOutput
  property_count: 3
  slug: data-execute-gremlin-query-output
- name: ExecuteOpenCypherExplainInput
  property_count: 3
  slug: data-execute-open-cypher-explain-input
- name: ExecuteOpenCypherQueryInput
  property_count: 2
  slug: data-execute-open-cypher-query-input
- name: ExecuteOpenCypherQueryOutput
  property_count: 1
  slug: data-execute-open-cypher-query-output
- name: ExecuteSparqlQueryInput
  property_count: 2
  slug: data-execute-sparql-query-input
- name: GremlinQueryStatusOutput
  property_count: 3
  slug: data-gremlin-query-status-output
- name: GremlinQueryStatus
  property_count: 3
  slug: data-gremlin-query-status
- name: LoaderJobStatusOutput
  property_count: 2
  slug: data-loader-job-status-output
- name: MLEndpointStatusOutput
  property_count: 4
  slug: data-ml-endpoint-status-output
- name: MLJobStatusOutput
  property_count: 3
  slug: data-ml-job-status-output
- name: OpenCypherQueryStatusOutput
  property_count: 3
  slug: data-open-cypher-query-status-output
- name: PropertygraphStatisticsOutput
  property_count: 2
  slug: data-propertygraph-statistics-output
- name: PropertygraphStreamOutput
  property_count: 5
  slug: data-propertygraph-stream-output
- name: PropertygraphStreamRecord
  property_count: 5
  slug: data-propertygraph-stream-record
- name: SparqlQueryOutput
  property_count: 2
  slug: data-sparql-query-output
- name: SparqlStatisticsOutput
  property_count: 2
  slug: data-sparql-statistics-output
- name: SparqlStreamOutput
  property_count: 5
  slug: data-sparql-stream-output
- name: StartLoaderJobInput
  property_count: 12
  slug: data-start-loader-job-input
- name: StartLoaderJobOutput
  property_count: 2
  slug: data-start-loader-job-output
- name: StartMLDataProcessingJobInput
  property_count: 16
  slug: data-start-ml-data-processing-job-input
- name: StartMLModelTrainingJobInput
  property_count: 20
  slug: data-start-ml-model-training-job-input
- name: StartMLModelTransformJobInput
  property_count: 15
  slug: data-start-ml-model-transform-job-input
- name: GremlinErrorResponse
  property_count: 3
  slug: gremlin-gremlin-error-response
- name: GremlinQueryRequest
  property_count: 1
  slug: gremlin-gremlin-query-request
- name: GremlinQueryResponse
  property_count: 3
  slug: gremlin-gremlin-query-response
- name: GremlinQueryStatusDetail
  property_count: 3
  slug: gremlin-gremlin-query-status-detail
- name: GremlinQueryStatusList
  property_count: 3
  slug: gremlin-gremlin-query-status-list
- name: LoaderErrorResponse
  property_count: 3
  slug: loader-loader-error-response
- name: LoaderListResponse
  property_count: 2
  slug: loader-loader-list-response
- name: LoaderRequest
  property_count: 12
  slug: loader-loader-request
- name: LoaderStartResponse
  property_count: 2
  slug: loader-loader-start-response
- name: LoaderStatusResponse
  property_count: 2
  slug: loader-loader-status-response
- name: CreateDBClusterRequest
  property_count: 13
  slug: management-create-db-cluster-request
- name: CreateDBInstanceRequest
  property_count: 8
  slug: management-create-db-instance-request
- name: DBClusterMember
  property_count: 4
  slug: management-db-cluster-member
- name: DBClusterRole
  property_count: 2
  slug: management-db-cluster-role
- name: DBCluster
  property_count: 22
  slug: management-db-cluster
- name: DBClusterSnapshot
  property_count: 13
  slug: management-db-cluster-snapshot
- name: DBInstance
  property_count: 14
  slug: management-db-instance
- name: DBSubnetGroup
  property_count: 6
  slug: management-db-subnet-group
- name: DescribeDBClusterSnapshotsResponse
  property_count: 2
  slug: management-describe-db-cluster-snapshots-response
- name: DescribeDBClustersResponse
  property_count: 2
  slug: management-describe-db-clusters-response
- name: DescribeDBInstancesResponse
  property_count: 2
  slug: management-describe-db-instances-response
- name: DescribeDBSubnetGroupsResponse
  property_count: 2
  slug: management-describe-db-subnet-groups-response
- name: ModifyDBClusterRequest
  property_count: 11
  slug: management-modify-db-cluster-request
- name: ModifyDBInstanceRequest
  property_count: 7
  slug: management-modify-db-instance-request
- name: RestoreDBClusterFromSnapshotRequest
  property_count: 9
  slug: management-restore-db-cluster-from-snapshot-request
- name: CreateDataProcessingJobRequest
  property_count: 16
  slug: ml-create-data-processing-job-request
- name: CreateInferenceEndpointRequest
  property_count: 9
  slug: ml-create-inference-endpoint-request
- name: CreateModelTrainingJobRequest
  property_count: 20
  slug: ml-create-model-training-job-request
- name: CreateModelTransformJobRequest
  property_count: 15
  slug: ml-create-model-transform-job-request
- name: EndpointCreatedResponse
  property_count: 1
  slug: ml-endpoint-created-response
- name: EndpointListResponse
  property_count: 1
  slug: ml-endpoint-list-response
- name: EndpointStatusResponse
  property_count: 5
  slug: ml-endpoint-status-response
- name: JobCreatedResponse
  property_count: 1
  slug: ml-job-created-response
- name: JobListResponse
  property_count: 1
  slug: ml-job-list-response
- name: JobStatusResponse
  property_count: 3
  slug: ml-job-status-response
- name: OpenCypherErrorResponse
  property_count: 3
  slug: opencypher-open-cypher-error-response
- name: OpenCypherNode
  property_count: 4
  slug: opencypher-open-cypher-node
- name: OpenCypherQueryRequest
  property_count: 1
  slug: opencypher-open-cypher-query-request
- name: OpenCypherQueryResponse
  property_count: 1
  slug: opencypher-open-cypher-query-response
- name: OpenCypherQueryStatusDetail
  property_count: 3
  slug: opencypher-open-cypher-query-status-detail
- name: OpenCypherQueryStatusList
  property_count: 3
  slug: opencypher-open-cypher-query-status-list
- name: OpenCypherRelationship
  property_count: 6
  slug: opencypher-open-cypher-relationship
- name: SparqlErrorResponse
  property_count: 3
  slug: sparql-sparql-error-response
- name: SparqlQueryStatusDetail
  property_count: 3
  slug: sparql-sparql-query-status-detail
- name: SparqlQueryStatusList
  property_count: 3
  slug: sparql-sparql-query-status-list
- name: SparqlRequestBody
  property_count: 4
  slug: sparql-sparql-request-body
- name: SparqlSelectResponse
  property_count: 3
  slug: sparql-sparql-select-response
- name: PropertyGraphData
  property_count: 6
  slug: streams-property-graph-data
- name: PropertyGraphStreamRecord
  property_count: 5
  slug: streams-property-graph-stream-record
- name: PropertyGraphStreamResponse
  property_count: 5
  slug: streams-property-graph-stream-response
- name: SparqlStreamRecord
  property_count: 5
  slug: streams-sparql-stream-record
- name: SparqlStreamResponse
  property_count: 5
  slug: streams-sparql-stream-response
- name: StreamEventId
  property_count: 2
  slug: streams-stream-event-id
json_structures:
- name: Amazon Neptune Analytics Graph Structure
  property_count: 17
  slug: amazon-neptune-analytics-graph-structure
- name: Amazon Neptune Db Cluster Structure
  property_count: 27
  slug: amazon-neptune-db-cluster-structure
- name: Amazon Neptune Db Instance Structure
  property_count: 21
  slug: amazon-neptune-db-instance-structure
- name: Amazon Neptune Graph Element Structure
  property_count: 0
  slug: amazon-neptune-graph-element-structure
- name: Amazon Neptune Loader Job Structure
  property_count: 12
  slug: amazon-neptune-loader-job-structure
- name: Amazon Neptune Ml Job Structure
  property_count: 0
  slug: amazon-neptune-ml-job-structure
- name: Amazon Neptune Stream Record Structure
  property_count: 5
  slug: amazon-neptune-stream-record-structure
- name: Amazon Neptune Structure
  property_count: 0
  slug: amazon-neptune-structure
- name: Analytics Create Graph Input Structure
  property_count: 8
  slug: analytics-create-graph-input-structure
- name: Analytics Create Graph Snapshot Input Structure
  property_count: 3
  slug: analytics-create-graph-snapshot-input-structure
- name: Analytics Create Graph Using Import Task Input Structure
  property_count: 12
  slug: analytics-create-graph-using-import-task-input-structure
- name: Analytics Create Private Graph Endpoint Input Structure
  property_count: 3
  slug: analytics-create-private-graph-endpoint-input-structure
- name: Analytics Graph Output Structure
  property_count: 15
  slug: analytics-graph-output-structure
- name: Analytics Graph Snapshot Output Structure
  property_count: 7
  slug: analytics-graph-snapshot-output-structure
- name: Analytics Import Task Output Structure
  property_count: 8
  slug: analytics-import-task-output-structure
- name: Analytics List Graph Snapshots Output Structure
  property_count: 2
  slug: analytics-list-graph-snapshots-output-structure
- name: Analytics List Graphs Output Structure
  property_count: 2
  slug: analytics-list-graphs-output-structure
- name: Analytics List Import Tasks Output Structure
  property_count: 2
  slug: analytics-list-import-tasks-output-structure
- name: Analytics Private Graph Endpoint Output Structure
  property_count: 4
  slug: analytics-private-graph-endpoint-output-structure
- name: Analytics Restore Graph From Snapshot Input Structure
  property_count: 6
  slug: analytics-restore-graph-from-snapshot-input-structure
- name: Analytics Update Graph Input Structure
  property_count: 3
  slug: analytics-update-graph-input-structure
- name: Data Create Ml Endpoint Input Structure
  property_count: 9
  slug: data-create-ml-endpoint-input-structure
- name: Data Engine Status Output Structure
  property_count: 10
  slug: data-engine-status-output-structure
- name: Data Execute Gremlin Profile Input Structure
  property_count: 5
  slug: data-execute-gremlin-profile-input-structure
- name: Data Execute Gremlin Query Input Structure
  property_count: 1
  slug: data-execute-gremlin-query-input-structure
- name: Data Execute Gremlin Query Output Structure
  property_count: 3
  slug: data-execute-gremlin-query-output-structure
- name: Data Execute Open Cypher Explain Input Structure
  property_count: 3
  slug: data-execute-open-cypher-explain-input-structure
- name: Data Execute Open Cypher Query Input Structure
  property_count: 2
  slug: data-execute-open-cypher-query-input-structure
- name: Data Execute Open Cypher Query Output Structure
  property_count: 1
  slug: data-execute-open-cypher-query-output-structure
- name: Data Execute Sparql Query Input Structure
  property_count: 2
  slug: data-execute-sparql-query-input-structure
- name: Data Gremlin Query Status Output Structure
  property_count: 3
  slug: data-gremlin-query-status-output-structure
- name: Data Gremlin Query Status Structure
  property_count: 3
  slug: data-gremlin-query-status-structure
- name: Data Loader Job Status Output Structure
  property_count: 2
  slug: data-loader-job-status-output-structure
- name: Data Ml Endpoint Status Output Structure
  property_count: 4
  slug: data-ml-endpoint-status-output-structure
- name: Data Ml Job Status Output Structure
  property_count: 3
  slug: data-ml-job-status-output-structure
- name: Data Open Cypher Query Status Output Structure
  property_count: 3
  slug: data-open-cypher-query-status-output-structure
- name: Data Propertygraph Statistics Output Structure
  property_count: 2
  slug: data-propertygraph-statistics-output-structure
- name: Data Propertygraph Stream Output Structure
  property_count: 5
  slug: data-propertygraph-stream-output-structure
- name: Data Propertygraph Stream Record Structure
  property_count: 5
  slug: data-propertygraph-stream-record-structure
- name: Data Sparql Query Output Structure
  property_count: 2
  slug: data-sparql-query-output-structure
- name: Data Sparql Statistics Output Structure
  property_count: 2
  slug: data-sparql-statistics-output-structure
- name: Data Sparql Stream Output Structure
  property_count: 5
  slug: data-sparql-stream-output-structure
- name: Data Start Loader Job Input Structure
  property_count: 12
  slug: data-start-loader-job-input-structure
- name: Data Start Loader Job Output Structure
  property_count: 2
  slug: data-start-loader-job-output-structure
- name: Data Start Ml Data Processing Job Input Structure
  property_count: 16
  slug: data-start-ml-data-processing-job-input-structure
- name: Data Start Ml Model Training Job Input Structure
  property_count: 20
  slug: data-start-ml-model-training-job-input-structure
- name: Data Start Ml Model Transform Job Input Structure
  property_count: 15
  slug: data-start-ml-model-transform-job-input-structure
- name: Gremlin Gremlin Error Response Structure
  property_count: 3
  slug: gremlin-gremlin-error-response-structure
- name: Gremlin Gremlin Query Request Structure
  property_count: 1
  slug: gremlin-gremlin-query-request-structure
- name: Gremlin Gremlin Query Response Structure
  property_count: 3
  slug: gremlin-gremlin-query-response-structure
- name: Gremlin Gremlin Query Status Detail Structure
  property_count: 3
  slug: gremlin-gremlin-query-status-detail-structure
- name: Gremlin Gremlin Query Status List Structure
  property_count: 3
  slug: gremlin-gremlin-query-status-list-structure
- name: Loader Loader Error Response Structure
  property_count: 3
  slug: loader-loader-error-response-structure
- name: Loader Loader List Response Structure
  property_count: 2
  slug: loader-loader-list-response-structure
- name: Loader Loader Request Structure
  property_count: 12
  slug: loader-loader-request-structure
- name: Loader Loader Start Response Structure
  property_count: 2
  slug: loader-loader-start-response-structure
- name: Loader Loader Status Response Structure
  property_count: 2
  slug: loader-loader-status-response-structure
- name: Management Create Db Cluster Request Structure
  property_count: 13
  slug: management-create-db-cluster-request-structure
- name: Management Create Db Instance Request Structure
  property_count: 8
  slug: management-create-db-instance-request-structure
- name: Management Db Cluster Member Structure
  property_count: 4
  slug: management-db-cluster-member-structure
- name: Management Db Cluster Role Structure
  property_count: 2
  slug: management-db-cluster-role-structure
- name: Management Db Cluster Snapshot Structure
  property_count: 13
  slug: management-db-cluster-snapshot-structure
- name: Management Db Cluster Structure
  property_count: 22
  slug: management-db-cluster-structure
- name: Management Db Instance Structure
  property_count: 14
  slug: management-db-instance-structure
- name: Management Db Subnet Group Structure
  property_count: 6
  slug: management-db-subnet-group-structure
- name: Management Describe Db Cluster Snapshots Response Structure
  property_count: 2
  slug: management-describe-db-cluster-snapshots-response-structure
- name: Management Describe Db Clusters Response Structure
  property_count: 2
  slug: management-describe-db-clusters-response-structure
- name: Management Describe Db Instances Response Structure
  property_count: 2
  slug: management-describe-db-instances-response-structure
- name: Management Describe Db Subnet Groups Response Structure
  property_count: 2
  slug: management-describe-db-subnet-groups-response-structure
- name: Management Modify Db Cluster Request Structure
  property_count: 11
  slug: management-modify-db-cluster-request-structure
- name: Management Modify Db Instance Request Structure
  property_count: 7
  slug: management-modify-db-instance-request-structure
- name: Management Restore Db Cluster From Snapshot Request Structure
  property_count: 9
  slug: management-restore-db-cluster-from-snapshot-request-structure
- name: Ml Create Data Processing Job Request Structure
  property_count: 16
  slug: ml-create-data-processing-job-request-structure
- name: Ml Create Inference Endpoint Request Structure
  property_count: 9
  slug: ml-create-inference-endpoint-request-structure
- name: Ml Create Model Training Job Request Structure
  property_count: 20
  slug: ml-create-model-training-job-request-structure
- name: Ml Create Model Transform Job Request Structure
  property_count: 15
  slug: ml-create-model-transform-job-request-structure
- name: Ml Endpoint Created Response Structure
  property_count: 1
  slug: ml-endpoint-created-response-structure
- name: Ml Endpoint List Response Structure
  property_count: 1
  slug: ml-endpoint-list-response-structure
- name: Ml Endpoint Status Response Structure
  property_count: 5
  slug: ml-endpoint-status-response-structure
- name: Ml Job Created Response Structure
  property_count: 1
  slug: ml-job-created-response-structure
- name: Ml Job List Response Structure
  property_count: 1
  slug: ml-job-list-response-structure
- name: Ml Job Status Response Structure
  property_count: 3
  slug: ml-job-status-response-structure
- name: Opencypher Open Cypher Error Response Structure
  property_count: 3
  slug: opencypher-open-cypher-error-response-structure
- name: Opencypher Open Cypher Node Structure
  property_count: 4
  slug: opencypher-open-cypher-node-structure
- name: Opencypher Open Cypher Query Request Structure
  property_count: 1
  slug: opencypher-open-cypher-query-request-structure
- name: Opencypher Open Cypher Query Response Structure
  property_count: 1
  slug: opencypher-open-cypher-query-response-structure
- name: Opencypher Open Cypher Query Status Detail Structure
  property_count: 3
  slug: opencypher-open-cypher-query-status-detail-structure
- name: Opencypher Open Cypher Query Status List Structure
  property_count: 3
  slug: opencypher-open-cypher-query-status-list-structure
- name: Opencypher Open Cypher Relationship Structure
  property_count: 6
  slug: opencypher-open-cypher-relationship-structure
- name: Sparql Sparql Error Response Structure
  property_count: 3
  slug: sparql-sparql-error-response-structure
- name: Sparql Sparql Query Status Detail Structure
  property_count: 3
  slug: sparql-sparql-query-status-detail-structure
- name: Sparql Sparql Query Status List Structure
  property_count: 3
  slug: sparql-sparql-query-status-list-structure
- name: Sparql Sparql Request Body Structure
  property_count: 4
  slug: sparql-sparql-request-body-structure
- name: Sparql Sparql Select Response Structure
  property_count: 3
  slug: sparql-sparql-select-response-structure
- name: Streams Property Graph Data Structure
  property_count: 6
  slug: streams-property-graph-data-structure
- name: Streams Property Graph Stream Record Structure
  property_count: 5
  slug: streams-property-graph-stream-record-structure
- name: Streams Property Graph Stream Response Structure
  property_count: 5
  slug: streams-property-graph-stream-response-structure
- name: Streams Sparql Stream Record Structure
  property_count: 5
  slug: streams-sparql-stream-record-structure
- name: Streams Sparql Stream Response Structure
  property_count: 5
  slug: streams-sparql-stream-response-structure
- name: Streams Stream Event Id Structure
  property_count: 2
  slug: streams-stream-event-id-structure
jsonld:
- class_count: 13
  name: Amazon Neptune Analytics Context
  property_count: 44
  slug: amazon-neptune-analytics-context
- class_count: 10
  name: Amazon Neptune Context
  property_count: 15
  slug: amazon-neptune-context
- class_count: 26
  name: Amazon Neptune Data Context
  property_count: 120
  slug: amazon-neptune-data-context
- class_count: 5
  name: Amazon Neptune Gremlin Context
  property_count: 20
  slug: amazon-neptune-gremlin-context
- class_count: 5
  name: Amazon Neptune Loader Context
  property_count: 21
  slug: amazon-neptune-loader-context
- class_count: 14
  name: Amazon Neptune Management Context
  property_count: 56
  slug: amazon-neptune-management-context
- class_count: 10
  name: Amazon Neptune Ml Context
  property_count: 50
  slug: amazon-neptune-ml-context
- class_count: 7
  name: Amazon Neptune Opencypher Context
  property_count: 21
  slug: amazon-neptune-opencypher-context
- class_count: 5
  name: Amazon Neptune Sparql Context
  property_count: 22
  slug: amazon-neptune-sparql-context
- class_count: 6
  name: Amazon Neptune Streams Context
  property_count: 20
  slug: amazon-neptune-streams-context
layout: provider
modified: '2026-05-19'
name: Amazon Neptune
nav: Providers
network: true
overview: 'Amazon Neptune publishes 29 APIs on the [APIs.io](https://apis.io/) network, including ?Action=AddTagsToResource API, ?Action=ListTagsForResource API, Data Processing API, and 26 more. Tagged areas include Database, Graph Database, Gremlin, Neptune, and Property Graph.


  The Amazon Neptune catalog on APIs.io includes 10 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Neptune''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, release notes, and 67 more developer resources.'
plans:
- name: Amazon Neptune Plans Pricing
  plan_count: 4
  slug: amazon-neptune-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Amazon Neptune Rate Limits
  slug: amazon-neptune-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon Neptune API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-neptune-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Amazon Neptune API Rules
  rule_count: 32
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 17
  slug: amazon-neptune-spectral-rules
score:
  band: strong
  composite: 59.4
  delta: -5.4
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 25.0
    contract_quality: 68.4
    developer_ergonomics: 69.0
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/screenshots/amazon-neptune-2026-06-20T171750.png
security:
- kind: authentication
  name: Amazon Neptune Authentication
  slug: amazon-neptune-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Neptune Domain Security
  slug: amazon-neptune-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Neptune Vulnerability Disclosure
  slug: amazon-neptune-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Neptune Trust Center
  slug: amazon-neptune-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-neptune
tags:
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
use_cases:
- description: Build knowledge graphs to enhance AI accuracy, comprehensiveness, and explainability using GraphRAG with Amazon Bedrock.
  name: Knowledge Graphs and GraphRAG
- description: Model transaction and account relationship networks to detect fraudulent patterns in near real-time using graph traversals.
  name: Fraud Detection
- description: Build unified customer profile graphs linking purchases, preferences, and interactions for personalization and marketing.
  name: Customer 360
- description: Model IT infrastructure as a connected graph to detect attack paths, anomalies, and proactive threats.
  name: Cybersecurity and Threat Detection
- description: Power product and content recommendation engines by traversing user-item relationship graphs.
  name: Recommendation Engines
- description: Model and query highly connected social graph data for applications requiring relationship traversal at scale.
  name: Social Networks
- description: Map network topology, dependencies, and configuration relationships for operations and impact analysis.
  name: Network and IT Operations
- description: Model complex supply chain relationships and dependencies for optimization and risk analysis.
  name: Supply Chain Management
website: https://aws.amazon.com/neptune/
---
