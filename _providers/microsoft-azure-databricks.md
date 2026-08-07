---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 3
  name: Microsoft Azure Databricks Agentic Access
  operation_count: 32
  slug: microsoft-azure-databricks-agentic-access
  summary_line: 32 operations · 20 acting · 3 human-in-the-loop
api_count: 39
apis:
- description: Core REST API for managing Azure Databricks workspaces, clusters, jobs, notebooks, and other resources programmatically.
  name: Azure Databricks REST API
  slug: azure-databricks-rest-api
- description: Manage Databricks clusters for running Spark jobs including creating, starting, editing, listing, terminating, and deleting clusters.
  name: Clusters API
  slug: clusters-api
- description: Create, manage, and run jobs on Databricks clusters including scheduling, listing runs, and managing job permissions.
  name: Jobs API
  slug: jobs-api
- description: Manage notebooks, folders, and other workspace objects including listing, importing, exporting, and deleting workspace items.
  name: Workspace API
  slug: workspace-api
- description: Access Databricks File System (DBFS) for file operations including uploading, downloading, listing, and deleting files and directories.
  name: DBFS API
  slug: dbfs-api
- description: Manage libraries and dependencies on clusters including installing, uninstalling, and listing library statuses.
  name: Libraries API
  slug: libraries-api
- description: Manage secrets and secret scopes for secure credential storage including creating scopes, putting secrets, and managing ACLs.
  name: Secrets API
  slug: secrets-api
- description: Create and manage personal access tokens for API authentication including creating, listing, and revoking tokens.
  name: Token Management API
  slug: token-management-api
- description: Manage SQL warehouses, queries, and dashboards for Databricks SQL analytics workloads.
  name: SQL Analytics API
  slug: sql-analytics-api
- description: Track experiments, log metrics, and manage ML models using the MLflow tracking and registry APIs.
  name: MLflow API
  slug: mlflow-api
- description: Create and manage instance pools to reduce cluster start and autoscaling times by maintaining a set of idle ready-to-use cloud instances.
  name: Instance Pools API
  slug: instance-pools-api
- description: Create, list, and edit cluster policies to control cluster configurations and limit the ability to configure clusters based on a set of rules.
  name: Cluster Policies API
  slug: cluster-policies-api
- description: Manage Git repositories within Databricks workspaces for version control of notebooks and files.
  name: Repos API
  slug: repos-api
- description: Manage Git credentials for authenticating with Git providers when using Databricks Repos.
  name: Git Credentials API
  slug: git-credentials-api
- description: Create, edit, delete, start, and view details about Delta Live Tables pipelines for building reliable data pipelines.
  name: Pipelines API
  slug: pipelines-api
- description: Manage permissions on workspace objects including clusters, jobs, notebooks, and other resources using access control lists.
  name: Permissions API
  slug: permissions-api
- description: Manage Unity Catalog catalogs for organizing and governing data assets across workspaces.
  name: Unity Catalog - Catalogs API
  slug: unity-catalog-catalogs-api
- description: Manage schemas within Unity Catalog catalogs for organizing tables, views, and functions.
  name: Unity Catalog - Schemas API
  slug: unity-catalog-schemas-api
- description: Manage tables within Unity Catalog schemas including listing, getting, and deleting tables.
  name: Unity Catalog - Tables API
  slug: unity-catalog-tables-api
- description: Manage Unity Catalog volumes for governing non-tabular data such as files and directories.
  name: Unity Catalog - Volumes API
  slug: unity-catalog-volumes-api
- description: Manage permissions and grants on Unity Catalog objects including catalogs, schemas, tables, and other securable objects.
  name: Unity Catalog - Grants API
  slug: unity-catalog-grants-api
- description: Manage external locations in Unity Catalog for connecting to cloud storage paths.
  name: Unity Catalog - External Locations API
  slug: unity-catalog-external-locations-api
- description: Manage storage credentials in Unity Catalog for authenticating access to cloud storage.
  name: Unity Catalog - Storage Credentials API
  slug: unity-catalog-storage-credentials-api
- description: Manage Unity Catalog metastores which serve as the top-level container for data governance.
  name: Unity Catalog - Metastores API
  slug: unity-catalog-metastores-api
- description: Create and manage model serving endpoints for deploying machine learning models as REST API endpoints.
  name: Model Serving Endpoints API
  slug: model-serving-endpoints-api
- description: Manage registered models and model versions in the Databricks Model Registry for model lifecycle management.
  name: Model Registry API
  slug: model-registry-api
- description: Manage registered models in Unity Catalog for centralized model governance and sharing.
  name: Registered Models API
  slug: registered-models-api
- description: Manage global cluster initialization scripts that run on every cluster in the workspace.
  name: Global Init Scripts API
  slug: global-init-scripts-api
- description: Manage IP access lists to control network access to Azure Databricks workspaces.
  name: IP Access Lists API
  slug: ip-access-lists-api
- description: Execute SQL statements on SQL warehouses and retrieve results for programmatic SQL access.
  name: Statement Execution API
  slug: statement-execution-api
- description: Execute commands on running clusters and retrieve results programmatically.
  name: Command Execution API
  slug: command-execution-api
- description: Manage files in Unity Catalog volumes and workspace filesystem with operations for uploading, downloading, and deleting files.
  name: Files API
  slug: files-api
- description: Deploy and manage Databricks Apps including creating, starting, stopping, and listing custom applications.
  name: Apps API
  slug: apps-api
- description: Manage Lakeview dashboards programmatically including creating, updating, and publishing dashboards.
  name: Lakeview API
  slug: lakeview-api
- description: Manage online tables for low-latency serving of feature data in Unity Catalog.
  name: Online Tables API
  slug: online-tables-api
- description: Manage vector search indexes for similarity search and retrieval-augmented generation workloads.
  name: Vector Search Indexes API
  slug: vector-search-indexes-api
- description: Manage vector search endpoints for hosting vector search indexes.
  name: Vector Search Endpoints API
  slug: vector-search-endpoints-api
- description: Retrieve query history for SQL warehouses including query text, status, and performance metrics.
  name: Query History API
  slug: query-history-api
- description: Manage users, groups, and service principals across the Databricks account using SCIM 2.0 protocol.
  name: Account SCIM API
  slug: account-scim-api
arazzos:
- description: Confirm a notebook, export its content, and re-import it to a backup path.
  name: Azure Databricks Back Up a Notebook by Export and Re-import
  slug: azure-databricks-backup-notebook-workflow
- description: Cancel a run and poll until its life cycle state is TERMINATED.
  name: Azure Databricks Cancel an Active Job Run
  slug: azure-databricks-cancel-active-run-workflow
- description: Find a job's latest completed run, confirm it, and delete it.
  name: Azure Databricks Clean Up the Latest Completed Job Run
  slug: azure-databricks-cleanup-latest-job-run-workflow
- description: Read a cluster's state then pull its recent events for diagnosis.
  name: Azure Databricks Cluster Health Diagnostics
  slug: azure-databricks-cluster-health-diagnostics-workflow
- description: Make a workspace directory, import a notebook into it, then verify it.
  name: Azure Databricks Create a Directory and Import a Notebook
  slug: azure-databricks-create-directory-and-import-notebook-workflow
- description: Create a notebook job, trigger a run, and poll until TERMINATED.
  name: Azure Databricks Create a Job and Run It to Completion
  slug: azure-databricks-create-job-and-run-workflow
- description: List a directory, confirm it is a directory, then recursively delete it.
  name: Azure Databricks Safely Delete a Workspace Directory
  slug: azure-databricks-delete-workspace-directory-workflow
- description: Import a notebook, confirm it landed, then submit a run of it.
  name: Azure Databricks Import a Notebook and Run It
  slug: azure-databricks-import-notebook-and-run-workflow
- description: List clusters, pick the first, and pin it so it is always retained.
  name: Azure Databricks Pin the First Listed Cluster
  slug: azure-databricks-pin-most-recent-cluster-workflow
- description: Resolve a valid Spark version and node type, then create a cluster.
  name: Azure Databricks Preflight and Create a Cluster
  slug: azure-databricks-preflight-create-cluster-workflow
- description: Create a cluster, wait until RUNNING, create a job on it, then run it.
  name: Azure Databricks Provision a Cluster and Run a Job on It
  slug: azure-databricks-provision-cluster-and-run-job-workflow
- description: Create a cluster and poll its state until it reaches RUNNING.
  name: Azure Databricks Provision and Wait for Cluster
  slug: azure-databricks-provision-cluster-workflow
- description: Reset all of a job's settings, then read the job back to confirm.
  name: Azure Databricks Overwrite Job Settings and Verify
  slug: azure-databricks-reset-job-and-verify-workflow
- description: Edit a running cluster's worker count and poll until it is RUNNING.
  name: Azure Databricks Resize a Running Cluster and Wait
  slug: azure-databricks-resize-running-cluster-workflow
- description: Restart a running cluster and poll until it returns to RUNNING.
  name: Azure Databricks Restart a Running Cluster and Wait
  slug: azure-databricks-restart-cluster-and-wait-workflow
- description: Trigger an existing job with parameters and poll the run to completion.
  name: Azure Databricks Run an Existing Job and Wait
  slug: azure-databricks-run-existing-job-and-wait-workflow
- description: Start a terminated cluster and poll its state until RUNNING.
  name: Azure Databricks Start a Terminated Cluster and Wait
  slug: azure-databricks-start-cluster-and-wait-workflow
- description: Submit a one-time notebook run without a job and poll to completion.
  name: Azure Databricks Submit a One-time Run and Wait
  slug: azure-databricks-submit-one-time-run-workflow
- description: Terminate a cluster, wait until TERMINATED, then permanently delete it.
  name: Azure Databricks Terminate and Permanently Delete a Cluster
  slug: azure-databricks-terminate-and-purge-cluster-workflow
- description: Partially update a job's settings, then trigger and poll a fresh run.
  name: Azure Databricks Update a Job and Re-run It
  slug: azure-databricks-update-job-and-rerun-workflow
artifact_total: 227
collections:
- collection_type: postman
  name: Azure Databricks REST API
  slug: postman-azure-databricks
- collection_type: open
  name: Azure Databricks REST API
  slug: open-azure-databricks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-databricks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-databricks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-databricks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-databricks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-databricks-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-databricks/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-backup-notebook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-cancel-active-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-cleanup-latest-job-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-cluster-health-diagnostics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-create-directory-and-import-notebook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-create-job-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-delete-workspace-directory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-import-notebook-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-pin-most-recent-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-preflight-create-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-provision-cluster-and-run-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-provision-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-reset-job-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-resize-running-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-restart-cluster-and-wait-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-run-existing-job-and-wait-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-start-cluster-and-wait-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-submit-one-time-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-terminate-and-purge-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-databricks-update-job-and-rerun-workflow.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/azure/databricks/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/pricing/details/databricks/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azuredatabricks.net/
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/azure/databricks/security/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/azure/databricks/dev-tools/
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/azure/databricks/dev-tools/cli/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/azure/databricks/dev-tools/auth/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/azure/databricks/reference/api
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/azure/databricks/release-notes/product/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/azure/databricks/release-notes/
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/answers/tags/166/azure-databricks
- group: build
  title: Python SDK
  type: SDKs
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-python
- group: build
  title: Java SDK
  type: SDKs
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-java
- group: build
  title: Go SDK
  type: SDKs
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-go
- group: build
  title: R SDK
  type: SDKs
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-r
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-databricks-client
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/azure-databricks-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-databricks-cluster-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/azure-databricks-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/azure-databricks-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/azure-databricks-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.databricks.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.databricks.com/feed
created: '2024-01-01'
description: Azure Databricks is an Apache Spark-based analytics platform optimized for Microsoft Azure. It provides a collaborative workspace for data engineers, data scientists, and analysts to work together on big data and machine learning workloads.
examples:
- key_count: 2
  name: Azure Databricks Auto Scale Example
  slug: azure-databricks-auto-scale-example
- key_count: 3
  name: Azure Databricks Azure Attributes Example
  slug: azure-databricks-azure-attributes-example
- key_count: 4
  name: Azure Databricks Cluster Event Example
  slug: azure-databricks-cluster-event-example
- key_count: 33
  name: Azure Databricks Cluster Info Example
  slug: azure-databricks-cluster-info-example
- key_count: 2
  name: Azure Databricks Cluster Log Conf Example
  slug: azure-databricks-cluster-log-conf-example
- key_count: 17
  name: Azure Databricks Create Cluster Request Example
  slug: azure-databricks-create-cluster-request-example
- key_count: 3
  name: Azure Databricks Cron Schedule Example
  slug: azure-databricks-cron-schedule-example
- key_count: 5
  name: Azure Databricks Email Notifications Example
  slug: azure-databricks-email-notifications-example
- key_count: 2
  name: Azure Databricks Error Example
  slug: azure-databricks-error-example
- key_count: 5
  name: Azure Databricks Git Source Example
  slug: azure-databricks-git-source-example
- key_count: 4
  name: Azure Databricks Init Script Info Example
  slug: azure-databricks-init-script-info-example
- key_count: 1
  name: Azure Databricks Job Cluster Example
  slug: azure-databricks-job-cluster-example
- key_count: 4
  name: Azure Databricks Job Example
  slug: azure-databricks-job-example
- key_count: 13
  name: Azure Databricks Job Settings Example
  slug: azure-databricks-job-settings-example
- key_count: 7
  name: Azure Databricks Library Example
  slug: azure-databricks-library-example
- key_count: 8
  name: Azure Databricks Node Type Example
  slug: azure-databricks-node-type-example
- key_count: 18
  name: Azure Databricks Run Example
  slug: azure-databricks-run-example
- key_count: 4
  name: Azure Databricks Run State Example
  slug: azure-databricks-run-state-example
- key_count: 6
  name: Azure Databricks Spark Node Example
  slug: azure-databricks-spark-node-example
- key_count: 19
  name: Azure Databricks Task Settings Example
  slug: azure-databricks-task-settings-example
- key_count: 4
  name: Azure Databricks Webhook Notifications Example
  slug: azure-databricks-webhook-notifications-example
- key_count: 7
  name: Azure Databricks Workspace Object Example
  slug: azure-databricks-workspace-object-example
- key_count: 6
  name: Microsoft Azure Databricks Canceljobrun Example
  slug: microsoft-azure-databricks-canceljobrun-example
- key_count: 6
  name: Microsoft Azure Databricks Createcluster Example
  slug: microsoft-azure-databricks-createcluster-example
- key_count: 6
  name: Microsoft Azure Databricks Createjob Example
  slug: microsoft-azure-databricks-createjob-example
- key_count: 6
  name: Microsoft Azure Databricks Createworkspacedirectory Example
  slug: microsoft-azure-databricks-createworkspacedirectory-example
- key_count: 6
  name: Microsoft Azure Databricks Deletejob Example
  slug: microsoft-azure-databricks-deletejob-example
- key_count: 6
  name: Microsoft Azure Databricks Deletejobrun Example
  slug: microsoft-azure-databricks-deletejobrun-example
- key_count: 6
  name: Microsoft Azure Databricks Deleteworkspaceobject Example
  slug: microsoft-azure-databricks-deleteworkspaceobject-example
- key_count: 6
  name: Microsoft Azure Databricks Editcluster Example
  slug: microsoft-azure-databricks-editcluster-example
- key_count: 6
  name: Microsoft Azure Databricks Exportworkspaceobject Example
  slug: microsoft-azure-databricks-exportworkspaceobject-example
- key_count: 6
  name: Microsoft Azure Databricks Getcluster Example
  slug: microsoft-azure-databricks-getcluster-example
- key_count: 6
  name: Microsoft Azure Databricks Getjob Example
  slug: microsoft-azure-databricks-getjob-example
- key_count: 6
  name: Microsoft Azure Databricks Getjobrun Example
  slug: microsoft-azure-databricks-getjobrun-example
- key_count: 6
  name: Microsoft Azure Databricks Getjobrunoutput Example
  slug: microsoft-azure-databricks-getjobrunoutput-example
- key_count: 6
  name: Microsoft Azure Databricks Getworkspaceobjectstatus Example
  slug: microsoft-azure-databricks-getworkspaceobjectstatus-example
- key_count: 6
  name: Microsoft Azure Databricks Importworkspaceobject Example
  slug: microsoft-azure-databricks-importworkspaceobject-example
- key_count: 6
  name: Microsoft Azure Databricks Listclusterevents Example
  slug: microsoft-azure-databricks-listclusterevents-example
- key_count: 6
  name: Microsoft Azure Databricks Listclusters Example
  slug: microsoft-azure-databricks-listclusters-example
- key_count: 6
  name: Microsoft Azure Databricks Listjobruns Example
  slug: microsoft-azure-databricks-listjobruns-example
- key_count: 6
  name: Microsoft Azure Databricks Listjobs Example
  slug: microsoft-azure-databricks-listjobs-example
- key_count: 6
  name: Microsoft Azure Databricks Listnodetypes Example
  slug: microsoft-azure-databricks-listnodetypes-example
- key_count: 6
  name: Microsoft Azure Databricks Listsparkversions Example
  slug: microsoft-azure-databricks-listsparkversions-example
- key_count: 6
  name: Microsoft Azure Databricks Listworkspaceobjects Example
  slug: microsoft-azure-databricks-listworkspaceobjects-example
- key_count: 6
  name: Microsoft Azure Databricks Permanentdeletecluster Example
  slug: microsoft-azure-databricks-permanentdeletecluster-example
- key_count: 6
  name: Microsoft Azure Databricks Pincluster Example
  slug: microsoft-azure-databricks-pincluster-example
- key_count: 6
  name: Microsoft Azure Databricks Resetjob Example
  slug: microsoft-azure-databricks-resetjob-example
- key_count: 6
  name: Microsoft Azure Databricks Restartcluster Example
  slug: microsoft-azure-databricks-restartcluster-example
- key_count: 6
  name: Microsoft Azure Databricks Runjobnow Example
  slug: microsoft-azure-databricks-runjobnow-example
- key_count: 6
  name: Microsoft Azure Databricks Startcluster Example
  slug: microsoft-azure-databricks-startcluster-example
- key_count: 6
  name: Microsoft Azure Databricks Submitrun Example
  slug: microsoft-azure-databricks-submitrun-example
- key_count: 6
  name: Microsoft Azure Databricks Terminatecluster Example
  slug: microsoft-azure-databricks-terminatecluster-example
- key_count: 6
  name: Microsoft Azure Databricks Unpincluster Example
  slug: microsoft-azure-databricks-unpincluster-example
- key_count: 6
  name: Microsoft Azure Databricks Updatejob Example
  slug: microsoft-azure-databricks-updatejob-example
features:
- Collaborative notebooks with multi-language support
- Auto-scaling Apache Spark clusters
- Delta Lake for reliable data lakehouse architecture
- Unity Catalog for unified data governance
- MLflow integration for ML lifecycle management
- Model serving endpoints for real-time inference
- Delta Live Tables for declarative ETL pipelines
- SQL analytics with serverless SQL warehouses
- Vector search for RAG and similarity search
- Lakeview dashboards for data visualization
- Git integration for version control of notebooks
- SCIM 2.0 for identity and access management
finops:
- name: Azure Databricks Finops
  service_category: Data Analytics
  slug: azure-databricks-finops
- name: Microsoft Azure Databricks Finops
  service_category: Analytics / Data + AI Platform
  slug: microsoft-azure-databricks-finops
image: https://azure.microsoft.com/svghandler/databricks/
integrations:
- Azure Data Factory for orchestration
- Azure Synapse Analytics for data warehousing
- Azure Data Lake Storage for scalable storage
- Azure Key Vault for secret management
- Azure Active Directory for authentication
- Power BI for business intelligence dashboards
- Terraform for infrastructure as code
- Apache Kafka for streaming data ingestion
json_schemas:
- name: AutoScale
  property_count: 2
  slug: azure-databricks-auto-scale
- name: AzureAttributes
  property_count: 3
  slug: azure-databricks-azure-attributes
- name: ClusterEvent
  property_count: 4
  slug: azure-databricks-cluster-event
- name: ClusterInfo
  property_count: 33
  slug: azure-databricks-cluster-info
- name: ClusterLogConf
  property_count: 2
  slug: azure-databricks-cluster-log-conf
- name: Azure Databricks Cluster
  property_count: 40
  slug: azure-databricks-cluster
- name: CreateClusterRequest
  property_count: 17
  slug: azure-databricks-create-cluster-request
- name: CronSchedule
  property_count: 3
  slug: azure-databricks-cron-schedule
- name: EmailNotifications
  property_count: 5
  slug: azure-databricks-email-notifications
- name: Error
  property_count: 2
  slug: azure-databricks-error
- name: GitSource
  property_count: 5
  slug: azure-databricks-git-source
- name: InitScriptInfo
  property_count: 4
  slug: azure-databricks-init-script-info
- name: JobCluster
  property_count: 1
  slug: azure-databricks-job-cluster
- name: Job
  property_count: 4
  slug: azure-databricks-job
- name: JobSettings
  property_count: 13
  slug: azure-databricks-job-settings
- name: Library
  property_count: 7
  slug: azure-databricks-library
- name: NodeType
  property_count: 8
  slug: azure-databricks-node-type
- name: Run
  property_count: 18
  slug: azure-databricks-run
- name: RunState
  property_count: 4
  slug: azure-databricks-run-state
- name: SparkNode
  property_count: 6
  slug: azure-databricks-spark-node
- name: TaskSettings
  property_count: 19
  slug: azure-databricks-task-settings
- name: WebhookNotifications
  property_count: 4
  slug: azure-databricks-webhook-notifications
- name: WorkspaceObject
  property_count: 7
  slug: azure-databricks-workspace-object
- name: AutoScale
  property_count: 2
  slug: microsoft-azure-databricks-autoscale
- name: AzureAttributes
  property_count: 3
  slug: microsoft-azure-databricks-azureattributes
- name: ClusterEvent
  property_count: 4
  slug: microsoft-azure-databricks-clusterevent
- name: ClusterInfo
  property_count: 37
  slug: microsoft-azure-databricks-clusterinfo
- name: ClusterLogConf
  property_count: 2
  slug: microsoft-azure-databricks-clusterlogconf
- name: CreateClusterRequest
  property_count: 20
  slug: microsoft-azure-databricks-createclusterrequest
- name: CronSchedule
  property_count: 3
  slug: microsoft-azure-databricks-cronschedule
- name: EmailNotifications
  property_count: 5
  slug: microsoft-azure-databricks-emailnotifications
- name: Error
  property_count: 2
  slug: microsoft-azure-databricks-error
- name: GitSource
  property_count: 5
  slug: microsoft-azure-databricks-gitsource
- name: InitScriptInfo
  property_count: 4
  slug: microsoft-azure-databricks-initscriptinfo
- name: Job
  property_count: 5
  slug: microsoft-azure-databricks-job
- name: JobCluster
  property_count: 2
  slug: microsoft-azure-databricks-jobcluster
- name: JobSettings
  property_count: 17
  slug: microsoft-azure-databricks-jobsettings
- name: Library
  property_count: 7
  slug: microsoft-azure-databricks-library
- name: NodeType
  property_count: 8
  slug: microsoft-azure-databricks-nodetype
- name: Run
  property_count: 20
  slug: microsoft-azure-databricks-run
- name: RunState
  property_count: 4
  slug: microsoft-azure-databricks-runstate
- name: SparkNode
  property_count: 6
  slug: microsoft-azure-databricks-sparknode
- name: TaskSettings
  property_count: 20
  slug: microsoft-azure-databricks-tasksettings
- name: WebhookNotifications
  property_count: 4
  slug: microsoft-azure-databricks-webhooknotifications
- name: WorkspaceObject
  property_count: 7
  slug: microsoft-azure-databricks-workspaceobject
json_structures:
- name: Azure Databricks Auto Scale Structure
  property_count: 2
  slug: azure-databricks-auto-scale-structure
- name: Azure Databricks Azure Attributes Structure
  property_count: 3
  slug: azure-databricks-azure-attributes-structure
- name: Azure Databricks Cluster Event Structure
  property_count: 4
  slug: azure-databricks-cluster-event-structure
- name: Azure Databricks Cluster Info Structure
  property_count: 33
  slug: azure-databricks-cluster-info-structure
- name: Azure Databricks Cluster Log Conf Structure
  property_count: 2
  slug: azure-databricks-cluster-log-conf-structure
- name: Azure Databricks Create Cluster Request Structure
  property_count: 17
  slug: azure-databricks-create-cluster-request-structure
- name: Azure Databricks Cron Schedule Structure
  property_count: 3
  slug: azure-databricks-cron-schedule-structure
- name: Azure Databricks Email Notifications Structure
  property_count: 5
  slug: azure-databricks-email-notifications-structure
- name: Azure Databricks Error Structure
  property_count: 2
  slug: azure-databricks-error-structure
- name: Azure Databricks Git Source Structure
  property_count: 5
  slug: azure-databricks-git-source-structure
- name: Azure Databricks Init Script Info Structure
  property_count: 4
  slug: azure-databricks-init-script-info-structure
- name: Azure Databricks Job Cluster Structure
  property_count: 1
  slug: azure-databricks-job-cluster-structure
- name: Azure Databricks Job Settings Structure
  property_count: 13
  slug: azure-databricks-job-settings-structure
- name: Azure Databricks Job Structure
  property_count: 4
  slug: azure-databricks-job-structure
- name: Azure Databricks Library Structure
  property_count: 7
  slug: azure-databricks-library-structure
- name: Azure Databricks Node Type Structure
  property_count: 8
  slug: azure-databricks-node-type-structure
- name: Azure Databricks Run State Structure
  property_count: 4
  slug: azure-databricks-run-state-structure
- name: Azure Databricks Run Structure
  property_count: 18
  slug: azure-databricks-run-structure
- name: Azure Databricks Spark Node Structure
  property_count: 6
  slug: azure-databricks-spark-node-structure
- name: Azure Databricks Task Settings Structure
  property_count: 19
  slug: azure-databricks-task-settings-structure
- name: Azure Databricks Webhook Notifications Structure
  property_count: 4
  slug: azure-databricks-webhook-notifications-structure
- name: Azure Databricks Workspace Object Structure
  property_count: 7
  slug: azure-databricks-workspace-object-structure
- name: Microsoft Azure Databricks Structure
  property_count: 0
  slug: microsoft-azure-databricks-structure
jsonld:
- class_count: 0
  name: Azure Databricks Context
  property_count: 0
  slug: azure-databricks-context
layout: provider
modified: '2026-05-19'
name: Azure Databricks
nav: Providers
network: true
overview: 'Azure Databricks publishes 4 APIs on the [APIs.io](https://apis.io/) network, including REST API, Clusters API, Jobs API, and 1 more. Tagged areas include Analytics, Apache Spark, Big Data, Data Engineering, and Machine Learning.


  The Azure Databricks catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Azure Databricks'' developer surface includes authentication, getting-started guide, pricing, CLI, API reference, release notes, changelog, and 42 more developer resources.'
plans:
- name: Azure Databricks Plans Pricing
  plan_count: 4
  slug: azure-databricks-plans-pricing
- name: Microsoft Azure Databricks Plans Pricing
  plan_count: 6
  slug: microsoft-azure-databricks-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 23
  name: Azure Databricks Rate Limits
  slug: azure-databricks-rate-limits
- limit_count: 5
  name: Microsoft Azure Databricks Rate Limits
  slug: microsoft-azure-databricks-rate-limits
rules:
- name: Azure Databricks API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-databricks-spectral-rules
- name: Azure Databricks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: microsoft-azure-databricks-jsonschema-spectral-rules
- name: Azure Databricks API Rules
  rule_count: 14
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 13
  slug: microsoft-azure-databricks-spectral-rules
scopes:
- name: Azure Databricks Scopes
  scope_count: 1
  slug: azure-databricks-scopes
  summary_line: 1 scope · authorizationCode
- name: Microsoft Azure Databricks Scopes
  scope_count: 1
  slug: microsoft-azure-databricks-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 56.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.1
    developer_ergonomics: 60.9
    discoverability: 64.8
    governance: 31.3
    operational_transparency: 73.7
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-databricks/refs/heads/main/screenshots/microsoft-azure-databricks-2026-06-20T185410.png
security:
- kind: authentication
  name: Azure Databricks Authentication
  slug: azure-databricks-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Azure Databricks Domain Security
  slug: azure-databricks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Databricks Vulnerability Disclosure
  slug: azure-databricks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-azure-databricks
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
use_cases:
- Building and managing data lakehouse architectures
- Training and deploying machine learning models at scale
- Running ETL pipelines for data transformation
- Interactive data exploration and ad-hoc analytics
- Real-time streaming analytics with Structured Streaming
- Building retrieval-augmented generation (RAG) applications
- Data governance and compliance with Unity Catalog
- Collaborative data science with shared notebooks
---
