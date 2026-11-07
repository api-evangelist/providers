---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 556
  human_in_the_loop: 30
  name: Cloudera Agentic Access
  operation_count: 778
  slug: cloudera-agentic-access
  summary_line: 778 operations · 556 acting · 30 human-in-the-loop
api_count: 38
apis:
- description: Cloudera Manager exposes a JSON REST API at /api/v{N} for managing clusters, services, roles, configurations, hosts, parcels, tags and audits. Authentication uses HTTP basic auth with the same credent
  name: Cloudera Manager API
  slug: manager
- description: Cruise Control on CDP exposes REST endpoints for rebalancing Kafka clusters, monitoring partition load, and triggering anomaly checks.
  name: Cloudera Cruise Control REST API
  slug: cruise-control
- description: Streams Replication Manager (SRM) exposes a REST API for inspecting cross-cluster Kafka replication topology, lag, and metrics.
  name: Streams Replication Manager Service REST API
  slug: srm
- description: The HBase REST Server provides a REST front-end to HBase tables for get/put/scan/delete, namespace and table management - installable via Cloudera Manager.
  name: HBase REST Server
  slug: hbase-rest
- description: YARN Queue Manager exposes a REST API for managing capacity scheduler queues, ACLs, and resource allocations on a CDP cluster.
  name: YARN Queue Manager API
  slug: yarn-queue-manager
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Audit API from Cloudera — 11 operation(s) for audit.
  name: Cloudera Audit API
  phrasing_intents:
  - id: archiveAuditEvents
    intent: Archive audit events for a time range now
    question: Can I force CDP audit events to be archived immediately instead of waiting for the schedule?
  - id: batchEventsForArchiving
    intent: Group audit events into batches for manual archiving
    question: How do I split audit events into batches so I can archive them to my own storage?
  - id: configureArchiving
    intent: Configure audit archiving to cloud storage
    question: How do I set up CDP to archive audit events to an external cloud storage bucket?
  - id: getArchivingConfig
    intent: Show the current audit archiving configuration
    question: Where are my audit events currently being archived to?
  - id: getArchivingStatus
    intent: Check the status of an audit archive run
    question: Did my on-demand audit archive job finish yet?
  - id: getBatchEventsForArchivingStatus
    intent: Check progress of creating archive batches
    question: Are my audit event batches ready to be archived yet?
  - id: listEvents
    intent: Search the audit log for a time window
    question: What audit events were recorded in my CDP account between two dates?
  - id: listEventsInArchiveBatch
    intent: List the events inside one archive batch
    question: What audit events are contained in a particular archive batch?
  phrasing_ops: 11
  slug: cloudera-audit-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The CDFLocalRPCAPIVersion1 API from Cloudera — 71 operation(s) for cdflocalrpcapiversion1.
  name: Cloudera CDF Local RPCAPI Version1 API
  phrasing_intents:
  - id: createCustomNarConfiguration
    intent: Create a custom NAR configuration
    question: How do I point DataFlow at a storage location holding my custom NiFi NAR files?
  - id: deleteCustomNarConfiguration
    intent: Delete an orphaned custom NAR configuration
    question: Can I remove a custom NAR configuration that no deployment uses anymore?
  - id: getCustomNarConfiguration
    intent: Get a custom NAR configuration
    question: Which custom NAR configuration is a given flow deployment using?
  - id: getDefaultCustomNarConfiguration
    intent: Get the default custom NAR configuration (deprecated)
    question: Is there still a default custom NAR configuration for an environment?
  - id: updateCustomNarConfiguration
    intent: Update a custom NAR configuration
    question: Can I change the storage location or password on an existing custom NAR configuration?
  - id: validateCustomNarConfiguration
    intent: Validate custom NAR configuration settings
    question: Can I test whether my NAR storage location and credentials work before saving them?
  - id: createCustomPythonConfiguration
    intent: Create a custom Python configuration
    question: How do I give DataFlow access to my own Python processors in cloud storage?
  - id: deleteCustomPythonConfiguration
    intent: Delete an orphaned custom Python configuration
    question: Can I delete a custom Python configuration that is no longer attached to anything?
  phrasing_ops: 71
  slug: cloudera-cdflocalrpcapiversion1-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Cloudprivatelinks API from Cloudera — 9 operation(s) for cloudprivatelinks.
  name: Cloudera Cloudprivatelinks API
  phrasing_intents:
  - id: authorizePrivateLinkServiceAccess
    intent: Authorize Private Link service access for an account
    question: How do I allow my cloud account to connect to CDP over Private Link?
  - id: createPrivateLinkEndpoint
    intent: Create Private Link endpoints for a service group
    question: What does it take to stand up Private Link endpoints to the CDP control plane?
  - id: deletePrivateLinkEndpoint
    intent: Delete Private Link endpoints
    question: How do I tear down the Private Link endpoints I created for CDP?
  - id: getPrivateLinkStatus
    intent: Check the status of a Private Link
    question: Is the Private Link for my VPC working right now?
  - id: listPrivateLinkEndpointStatuses
    intent: Track Private Link endpoints being created or deleted
    question: How far along is my Private Link endpoint creation?
  - id: listPrivateLinkServicesForRegion
    intent: List Private Link services supported in a region
    question: Which Private Link services are available in my cloud region?
  - id: migratePrivateLinkEndpoints
    intent: Migrate Private Link endpoints to control plane services
    question: How do I move my Private Link endpoints over to the control plane endpoint services?
  - id: revokePrivateLinkServiceAccess
    intent: Revoke Private Link service access for an account
    question: How do I take away a cloud account's Private Link access to CDP?
  phrasing_ops: 9
  slug: cloudera-cloudprivatelinks-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Compute API from Cloudera — 15 operation(s) for compute.
  name: Cloudera Compute API
  phrasing_intents:
  - id: createCluster
    intent: Create a compute cluster
    question: How do I create a new compute cluster in a CDP environment?
  - id: deleteCluster
    intent: Delete a compute cluster
    question: Can I force-delete a compute cluster that still has workloads on it?
  - id: describeCluster
    intent: Get details of a compute cluster
    question: What are the details and current state of one of my compute clusters?
  - id: describeDeployment
    intent: Get a deployment and its history
    question: What is the history of a specific Helm deployment on my compute cluster?
  - id: getOperationDetails
    intent: Get full details of a long-running operation
    question: Where can I see detailed step information for a long-running compute operation?
  - id: getOperationStatus
    intent: Check status of a long-running operation
    question: Is my long-running compute operation finished yet?
  - id: listClusters
    intent: List compute clusters
    question: Which compute clusters are running in my CDP environment?
  - id: listDeployments
    intent: List Helm deployments in a cluster
    question: Which Helm charts are deployed or available to deploy on my compute cluster?
  phrasing_ops: 15
  slug: cloudera-compute-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Consumption API from Cloudera — 1 operation(s) for consumption.
  name: Cloudera Consumption API
  phrasing_intents:
  - id: listComputeUsageRecords
    intent: List compute usage records for a period
    question: How much Cloudera compute did we use between two dates?
  phrasing_ops: 1
  slug: cloudera-consumption-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Datalake API from Cloudera — 56 operation(s) for datalake.
  name: Cloudera Datalake API
  phrasing_intents:
  - id: listRuntimes
    intent: List available Data Lake runtime versions
    question: Which Cloudera Runtime versions can I create a Data Lake with?
  - id: createAWSDatalake
    intent: Create a Data Lake on AWS
    question: How do I create a Data Lake in a commercial AWS environment?
  - id: createAWSGovCloudDatalake
    intent: Create a Data Lake on AWS GovCloud
    question: What is needed to stand up a Data Lake in a US government (GovCloud) region?
  - id: createAzureDatalake
    intent: Create a Data Lake on Azure
    question: How do I create a Data Lake in an Azure environment?
  - id: createGCPDatalake
    intent: Create a Data Lake on Google Cloud
    question: How do I create a Data Lake in a GCP environment?
  - id: listDatalakes
    intent: List Data Lakes
    question: Which datalakes exist across my CDP environments?
  - id: deleteDatalake
    intent: Delete a Data Lake
    question: How do I delete a Data Lake?
  - id: retryDatalake
    intent: Retry a Data Lake's last failed operation
    question: Can I retry the operation that just failed on my datalake?
  phrasing_ops: 56
  slug: cloudera-datalake-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The De API from Cloudera — 24 operation(s) for de.
  name: Cloudera De API
  phrasing_intents:
  - id: createBackup
    intent: Back up a Data Engineering service
    question: How do I back up my Cloudera Data Engineering service including its virtual clusters?
  - id: cancelBackup
    intent: Cancel a pending CDE service backup
    question: Can I stop a CDE backup that hasn't finished yet?
  - id: deleteBackup
    intent: Delete a CDE service backup
    question: How do I remove an old Data Engineering backup I no longer need?
  - id: describeBackup
    intent: Show details of a CDE service backup
    question: What's the status and content of a specific CDE backup?
  - id: getBackupLogs
    intent: Read the logs of a CDE backup
    question: Where can I see why a CDE service backup failed?
  - id: getServiceInitLogs
    intent: Read a CDE service's initialization logs
    question: Why did my Data Engineering service fail to come up?
  - id: listBackups
    intent: List CDE service backups
    question: What Data Engineering backups do I have?
  - id: restoreService
    intent: Restore a CDE service from a backup
    question: How do I recover a Data Engineering service from a backup into an environment?
  phrasing_ops: 24
  slug: cloudera-de-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Df API from Cloudera — 66 operation(s) for df.
  name: Cloudera Df API
  phrasing_intents:
  - id: addReadyflow
    intent: Add a ReadyFlow to my account
    question: Can I add a prebuilt ReadyFlow from the gallery into my DataFlow account?
  - id: assignToCollection
    intent: Assign a flow definition to a collection
    question: Can I group an existing flow definition into a catalog collection?
  - id: cancelDeleteProject
    intent: Cancel a pending project deletion
    question: Can I stop a DataFlow project from being deleted after I requested it?
  - id: createCollection
    intent: Create a catalog collection
    question: How do I create a new collection in the DataFlow catalog?
  - id: createFlowVersionTag
    intent: Tag a flow version
    question: Can I label a specific flow version with a colored tag?
  - id: createProject
    intent: Create a DataFlow project
    question: How do I create a project inside a DataFlow service?
  - id: deleteAddedReadyflow
    intent: Remove an added ReadyFlow from my account
    question: Can I remove a ReadyFlow I previously added to my account?
  - id: deleteCollection
    intent: Delete an empty catalog collection
    question: Can I delete a catalog collection that still has flows in it?
  phrasing_ops: 66
  slug: cloudera-df-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Drscp API from Cloudera — 9 operation(s) for drscp.
  name: Cloudera Drscp API
  phrasing_intents:
  - id: createBackup
    intent: Back up the control plane
    question: How do I take an on-demand backup of my CDP control plane?
  - id: restoreBackup
    intent: Restore the control plane from a backup
    question: How do I rebuild my control plane from an existing backup?
  - id: deleteBackup
    intent: Delete a control plane backup
    question: Can I delete an old control plane backup?
  - id: describeBackup
    intent: Describe a control plane backup
    question: What state is a particular control plane backup in?
  - id: describeRestore
    intent: Describe a control plane restore
    question: Has my control plane restore finished?
  - id: listBackupEntities
    intent: List what can be backed up
    question: Which control plane namespaces are eligible for backup?
  - id: listBackups
    intent: List control plane backups
    question: What control plane backups exist?
  - id: listRestores
    intent: List control plane restores
    question: Which control plane restores have been run?
  phrasing_ops: 9
  slug: cloudera-drscp-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Dw API from Cloudera — 95 operation(s) for dw.
  name: Cloudera Dw API
  phrasing_intents:
  - id: listClusters
    intent: List Data Warehouse clusters
    question: Which Cloudera Data Warehouse clusters are running in my environments?
  - id: describeCluster
    intent: Get details of one Data Warehouse cluster
    question: What are the settings and state of a specific CDW cluster?
  - id: createClusterDiagnosticDataJob
    intent: Collect cluster-level diagnostic logs and metrics
    question: How do I gather logs and metrics from a whole CDW cluster for a support case?
  - id: listClusterDiagnosticDataJobs
    intent: List diagnostic jobs for a cluster
    question: What cluster-level diagnostic bundles have been collected for my CDW cluster?
  - id: describeClusterDiagnosticDataJob
    intent: Get one cluster diagnostic job
    question: Has the cluster diagnostic bundle I requested finished?
  - id: deleteClusterDiagnosticDataJob
    intent: Delete a cluster diagnostic job
    question: Can I delete a cluster-level diagnostic job even while it's still running?
  - id: describeKubeconfig
    intent: Get the kubeconfig for a cluster
    question: How can I get kubectl access to the Kubernetes behind my CDW cluster?
  - id: describeAllowedInstanceTypes
    intent: List allowed compute instance types
    question: Which compute instance types can a CDW cluster use on AWS and Azure?
  phrasing_ops: 95
  slug: cloudera-dw-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Environments2 API from Cloudera — 104 operation(s) for environments2.
  name: Cloudera Environments2 API
  phrasing_intents:
  - id: getCredentialPrerequisites
    intent: Get credential prerequisites for a cloud provider
    question: What do I need to set up in my cloud account before creating a CDP credential?
  - id: getGovCloudCredentialPrerequisites
    intent: Get GovCloud credential prerequisites
    question: What prerequisites apply to a GovCloud credential in CDP?
  - id: createAWSEnvironment
    intent: Create an AWS environment
    question: How do I create a new CDP environment in AWS commercial regions?
  - id: createAWSGovCloudEnvironment
    intent: Create an AWS GovCloud environment
    question: How do I create a CDP environment in AWS GovCloud?
  - id: createAzureEnvironment
    intent: Create an Azure environment
    question: What's needed to create a CDP environment on Azure?
  - id: createGCPEnvironment
    intent: Create a GCP environment
    question: How do I create a CDP environment on Google Cloud?
  - id: createPrivateEnvironment
    intent: Create a Private Cloud environment
    question: How do I register an on-prem Private Cloud environment from Cloudera Manager?
  - id: createAWSCredential
    intent: Create an AWS credential
    question: How do I give CDP access to my AWS account with a cross-account role?
  phrasing_ops: 104
  slug: cloudera-environments2-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Iam API from Cloudera — 79 operation(s) for iam.
  name: Cloudera Iam API
  phrasing_intents:
  - id: getUser
    intent: Look up a CDP user's details
    question: How can I see the details of one user in my CDP account?
  - id: listUsers
    intent: List users in the CDP account
    question: Can I get a list of every human user in my Cloudera CDP account?
  - id: createUser
    intent: Create a CDP user
    question: How do I add a new person as a user in CDP with their email and identity provider ID?
  - id: updateUser
    intent: Activate or deactivate a CDP user
    question: Can I deactivate a CDP user without deleting them?
  - id: deleteUser
    intent: Delete a CDP user and their access
    question: What gets removed when I delete a human user from CDP?
  - id: createUserAccessKey
    intent: Create an API access key for a user
    question: How do I generate a CDP API access key for a human user?
  - id: createMachineUserAccessKey
    intent: Create an access key for a machine user
    question: How do I give a CDP machine user an API key for automation?
  - id: deleteAccessKey
    intent: Delete an API access key
    question: How do I permanently delete a CDP access key that leaked?
  phrasing_ops: 79
  slug: cloudera-iam-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Imagecatalog API from Cloudera — 11 operation(s) for imagecatalog.
  name: Cloudera Imagecatalog API
  phrasing_intents:
  - id: createCustomCatalog
    intent: Create a custom image catalog
    question: How do I set up my own image catalog for Cloudera Runtime and FreeIPA images?
  - id: deleteCustomCatalog
    intent: Delete a custom image catalog
    question: Can I remove a custom image catalog I no longer use?
  - id: deleteFreeipaImage
    intent: Delete a FreeIPA image from a catalog
    question: How do I take a FreeIPA image out of one of my custom catalogs?
  - id: deleteRuntimeImage
    intent: Delete a Cloudera Runtime image from a catalog
    question: Can I remove an outdated Cloudera Runtime image from my custom catalog?
  - id: describeCustomCatalog
    intent: Get details of a custom image catalog
    question: What images and settings does my custom image catalog contain?
  - id: describeCustomImage
    intent: Get details of an image in a custom catalog
    question: What do I know about a specific image stored in my custom catalog?
  - id: describeDefaultImage
    intent: Get an image from the default catalog by id
    question: How do I look up an image in Cloudera's default catalog when I already know its id?
  - id: findDefaultImage
    intent: Find a default image by provider and type
    question: Which default image should I use for a given cloud provider and image type?
  phrasing_ops: 11
  slug: cloudera-imagecatalog-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Lakehouseopt API from Cloudera — 30 operation(s) for lakehouseopt.
  name: Cloudera Lakehouseopt API
  phrasing_intents:
  - id: getHealth
    intent: Check health of Lakehouse Optimizer components
    question: Are the Lakehouse Optimizer scheduler, dispatcher and DAO services healthy?
  - id: listEnvironments
    intent: List environments with their CLO Data Hub
    question: Which of my environments have a Lakehouse Optimizer Data Hub enabled?
  - id: getDatahubCrn
    intent: Look up the Data Hub CRN for an environment
    question: What is the Data Hub CRN I should use for Lakehouse Optimizer calls in my environment?
  - id: getCloDatahub
    intent: Get the CLO Data Hub for an environment
    question: Which Data Hub runs Lakehouse Optimizer in a given environment, and what are its details?
  - id: listPolicies
    intent: List table maintenance policies
    question: What maintenance policies are defined in Lakehouse Optimizer?
  - id: getPolicy
    intent: Get details of a maintenance policy
    question: What actions, scope, versions and status does a particular policy have?
  - id: downloadPolicy
    intent: Download a policy version's definition
    question: How do I get the scripts and arguments behind a specific policy version?
  - id: getNamespaces
    intent: List namespaces in the catalog
    question: Which namespaces exist in the catalog Lakehouse Optimizer manages?
  phrasing_ops: 30
  slug: cloudera-lakehouseopt-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Ml API from Cloudera — 59 operation(s) for ml.
  name: Cloudera Ml API
  phrasing_intents:
  - id: addInstanceGroups
    intent: Add instance groups to an AI workbench
    question: How do I add more instance groups to a Cloudera AI workbench cluster?
  - id: addInstanceGroupsMlServingApp
    intent: Add instance groups to an inference service
    question: Can I add an instance group to an existing AI Inference Service instance?
  - id: backupWorkspace
    intent: Back up an AI workbench
    question: How do I back up a Cloudera AI workbench?
  - id: createFileReplica
    intent: Create a file system replica for a workbench
    question: Can I replicate a workbench's project files to a replica file system?
  - id: createMlServingApp
    intent: Deploy an AI Inference Service
    question: How do I deploy Cloudera AI Inference Service into an environment?
  - id: createModelRegistry
    intent: Create a model registry
    question: What does it take to create a new model registry?
  - id: createWorkspace
    intent: Create an AI workbench
    question: How do I provision a new Cloudera AI workbench?
  - id: deleteBackup
    intent: Delete a workbench backup
    question: Can I delete an old workbench backup snapshot?
  phrasing_ops: 59
  slug: cloudera-ml-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Opdb API from Cloudera — 19 operation(s) for opdb.
  name: Cloudera Opdb API
  phrasing_intents:
  - id: collectDiagnostics
    intent: Collect a diagnostic bundle from an operational database
    question: How do I gather diagnostic bundles from my operational database for support?
  - id: createDatabase
    intent: Create an operational database
    question: How do I spin up a new operational database in a CDP environment?
  - id: createSnapshot
    intent: Snapshot a table in an operational database
    question: How can I take a snapshot of a single table in my operational database?
  - id: deleteSnapshot
    intent: Delete a table snapshot
    question: How do I get rid of an old table snapshot in my operational database?
  - id: describeClientConnectivity
    intent: Get client connection details for a database
    question: How do my applications connect programmatically to my operational database?
  - id: describeDatabase
    intent: Describe an operational database
    question: What's the current configuration and state of my operational database?
  - id: describeUpgradeDatabase
    intent: Check whether a database upgrade is available
    question: Is there an upgrade available for my operational database?
  - id: dropDatabase
    intent: Drop an operational database
    question: How do I permanently drop an operational database?
  phrasing_ops: 19
  slug: cloudera-opdb-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Replicationmanager API from Cloudera — 24 operation(s) for replicationmanager.
  name: Cloudera Replicationmanager API
  phrasing_intents:
  - id: listClusters
    intent: List clusters available for replication
    question: Which clusters can Replication Manager see in my CDP account?
  - id: listClusterServiceStatuses
    intent: Show the status of cluster services
    question: Are HDFS, Hive and YARN healthy on my replication clusters?
  - id: listAllCredentials
    intent: List cloud credentials across all clusters
    question: What cloud credentials are registered across all my replication clusters?
  - id: getCredentials
    intent: Get the cloud credentials on one cluster
    question: Which cloud credentials are configured on a specific cluster?
  - id: createAwsCredential
    intent: Create an AWS cloud credential for replication
    question: How do I add AWS access keys so replication policies can write to S3?
  - id: createAbfsCredential
    intent: Create an Azure ABFS cloud credential
    question: How do I set up an ABFS credential so replication can reach Azure Data Lake storage?
  - id: deleteCredential
    intent: Delete a replication cloud credential
    question: How do I permanently remove a cloud credential from Replication Manager?
  - id: getClusterConfig
    intent: Get a cluster's configuration
    question: How is a particular replication cluster configured?
  phrasing_ops: 24
  slug: cloudera-replicationmanager-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Data Catalog API from Cloudera — 20 operation(s) for data catalog.
  name: Cloudera Data Catalog API
  phrasing_intents:
  - id: launchProfilers
    intent: Launch data profilers in a data lake
    question: How do I start the Data Catalog profilers on my data lake?
  - id: getDataShare
    intent: Get one Data Share's details
    question: What assets and external users are in a specific Data Share?
  - id: listDataShares
    intent: List Data Shares in a data lake
    question: Which Data Shares exist in my data lake?
  - id: createExternalUsers
    intent: Register external users for data sharing
    question: How do I let people outside Cloudera access shared data?
  - id: listExternalUsers
    intent: List external data-sharing users
    question: Who are the external users registered for data sharing?
  - id: regenerateExternalUserCredentials
    intent: Regenerate an external user's credentials
    question: How do I issue fresh credentials to an external data-sharing user?
  - id: deleteExternalUser
    intent: Permanently delete an external user
    question: How do I permanently remove an outside user from data sharing?
  - id: updateDataShare
    intent: Edit a Data Share's metadata
    question: Can I change the expiration time or terms of use on an existing Data Share?
  phrasing_ops: 20
  slug: cloudera-data-catalog-api
- baseURL: https://api.us-west-1.cdp.cloudera.com
  baseurl_source: declared
  description: The Data Hub API from Cloudera — 75 operation(s) for data hub.
  name: Cloudera Data Hub API
  phrasing_intents:
  - id: deleteInstances
    intent: Delete specific instances from a cluster
    question: Can I remove particular VM instances from a Data Hub cluster by id?
  - id: listClusters
    intent: List Data Hub workload clusters
    question: Which Data Hub clusters do I have?
  - id: listScalingActivities
    intent: List scaling activities for a cluster
    question: What scaling activity has happened on my Data Hub cluster recently?
  - id: describeScalingActivity
    intent: Get details of one scaling activity
    question: What happened during a specific scaling operation on my cluster?
  - id: listClusterLifecycleEvents
    intent: List lifecycle events of a cluster
    question: What lifecycle events has my Data Hub cluster gone through?
  - id: createAWSCluster
    intent: Create a Data Hub cluster on AWS
    question: How do I spin up a new Data Hub cluster on AWS?
  - id: createAWSGovCloudCluster
    intent: Create a Data Hub cluster on AWS GovCloud
    question: Can I create a Data Hub cluster in AWS GovCloud?
  - id: createAzureCluster
    intent: Create a Data Hub cluster on Azure
    question: How do I create a Data Hub cluster in an Azure environment?
  phrasing_ops: 75
  slug: cloudera-data-hub-api
artifact_total: 140
common:
- group: design
  href: https://artifacts.apis.io/cloudera/vocabulary/cloudera-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudera-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/cloudera/hosts/cloudera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudera-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudera/vendors/cloudera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudera-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.cloudera.com/about/leadership/board.html
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-audit-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-audit-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-cloudprivatelinks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-cloudprivatelinks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-compute-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-compute-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-consumption-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-consumption-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-datacatalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-datacatalog-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-datahub-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-datahub-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-datalake-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-datalake-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-de-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-de-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-df-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-df-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-dfworkload-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-dfworkload-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-drscp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-drscp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-dw-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-dw-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-environments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-environments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-iam-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-iam-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-imagecatalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-imagecatalog-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-lakehouseopt-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-lakehouseopt-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-ml-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-ml-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-opdb-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-opdb-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudera/overlays/cloudera-replicationmanager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudera-replicationmanager-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cloudera/agentic-access/cloudera-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudera-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudera/security/cloudera-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudera-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cloudera/security/cloudera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudera-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudera/authentication/cloudera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudera-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudera
- group: company
  title: ''
  type: Website
  url: https://www.cloudera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudera.com/
- group: operate
  title: ''
  type: Support
  url: https://community.cloudera.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudera
- group: design
  href: https://artifacts.apis.io/cloudera/json-ld/cloudera-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudera-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudera/rules/cloudera-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudera-rules.yml
- group: build
  href: https://artifacts.apis.io/cloudera/packages/cloudera-packages.yml
  title: ''
  type: Packages
  url: packages/cloudera-packages.yml
- group: build
  href: https://artifacts.apis.io/cloudera/packages/cloudera-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudera-packages.yml
- group: build
  href: https://artifacts.apis.io/cloudera/cli/cloudera-cli.yml
  title: ''
  type: CLI
  url: cli/cloudera-cli.yml
- group: agent
  href: https://artifacts.apis.io/cloudera/mcp/cloudera-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloudera-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cloudera/llms/cloudera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudera-llms.txt
- group: design
  href: https://artifacts.apis.io/cloudera/conformance/cloudera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudera-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cloudera/conformance/cloudera-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cloudera-conformance.yml
- group: design
  href: https://artifacts.apis.io/cloudera/errors/cloudera-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudera-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudera/lifecycle/cloudera-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudera-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cloudera/conventions/cloudera-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudera-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudera/conventions/cloudera-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloudera-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudera/data-model/cloudera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudera-data-model.yml
- group: start
  href: https://artifacts.apis.io/cloudera/sandbox/cloudera-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cloudera-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/cloudera/changelog/cloudera-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudera-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/cloudera/plans/cloudera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudera-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudera/rate-limits/cloudera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudera-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/cloudera/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cloudera.com/cdp-public-cloud/cloud/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://cloudera.github.io/cdp-dev-docs/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudera.com/cdp-public-cloud/cloud/index.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudera.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.cloudera.com/services-and-support/support-lifecycle-policy.html
- group: company
  title: ''
  type: Blog
  url: https://www.cloudera.com/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudera
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudera.com/products/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.cloudera.com/campaign/try-cdp-public-cloud.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudera.com/legal/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudera.com/legal/policies.html
- group: other
  href: https://artifacts.apis.io/cloudera/capabilities/cloudera-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudera-capability-edges.yml
- group: build
  href: https://artifacts.apis.io/cloudera/mcp/cloudera-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudera-tool-crosswalk.yml
created: '2024-01-01'
description: Cloudera is a hybrid data platform company offering the Cloudera Data Platform (CDP) for data engineering, data warehousing, machine learning, streaming, and operational data. The platform exposes multiple REST APIs including the CDP Public Cloud Control Plane API for managing environments, datalakes, data hubs and workloads, the Cloudera Manager API for cluster lifecycle and configuration management, and per-service REST APIs across the runtime (Cruise Control, Streams Replication Manager, HBase REST, YARN Queue Manager, etc.). APIs are JSON, support standard CRUD, and are typically authenticated via API access keys, basic auth, or session cookies.
finops:
- has_sources: true
  method: derived
  name: Cloudera Finops
  primary_unit: ccu
  service_category: ''
  slug: cloudera-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudera.png
json_schemas:
- name: AddFlowToDeploymentRequest
  property_count: 13
  slug: cloudera-add-flow-to-deployment-request
- name: ArchiveAuditEventsResponse
  property_count: 3
  slug: cloudera-archive-audit-events-response
- name: AuthorizePrivateLinkServiceAccessRequest
  property_count: 5
  slug: cloudera-authorize-private-link-service-access-request
- name: ChangeFlowVersionInDeploymentRequest
  property_count: 13
  slug: cloudera-change-flow-version-in-deployment-request
- name: ChangeFlowVersionRequest
  property_count: 11
  slug: cloudera-change-flow-version-request
- name: ChangeTablePolicyRequest
  property_count: 5
  slug: cloudera-change-table-policy-request
- name: CollectCmDiagnosticsRequest
  property_count: 11
  slug: cloudera-collect-cm-diagnostics-request
- name: CollectDatahubDiagnosticsRequest
  property_count: 17
  slug: cloudera-collect-datahub-diagnostics-request
- name: CollectDatalakeDiagnosticsRequest
  property_count: 17
  slug: cloudera-collect-datalake-diagnostics-request
- name: CollectDiagnosticBundleResponse
  property_count: 5
  slug: cloudera-collect-diagnostic-bundle-response
- name: CollectDiagnosticsRequest
  property_count: 7
  slug: cloudera-collect-diagnostics-request
- name: CollectFreeipaDiagnosticsRequest
  property_count: 17
  slug: cloudera-collect-freeipa-diagnostics-request
- name: ConfigureArchivingRequest
  property_count: 5
  slug: cloudera-configure-archiving-request
- name: CreateAbfsCredentialRequest
  property_count: 8
  slug: cloudera-create-abfs-credential-request
- name: CreateAwsClusterRequest
  property_count: 17
  slug: cloudera-create-aws-cluster-request
- name: CreateAwsCredentialRequest
  property_count: 5
  slug: cloudera-create-aws-credential-request
- name: CreateAWSClusterRequest
  property_count: 20
  slug: cloudera-create-awscluster-request
- name: CreateAWSDatalakeRequest
  property_count: 14
  slug: cloudera-create-awsdatalake-request
- name: CreateAWSEnvironmentRequest
  property_count: 25
  slug: cloudera-create-awsenvironment-request
- name: CreateAWSGovCloudClusterRequest
  property_count: 15
  slug: cloudera-create-awsgov-cloud-cluster-request
- name: CreateAWSGovCloudDatalakeRequest
  property_count: 12
  slug: cloudera-create-awsgov-cloud-datalake-request
- name: CreateAWSGovCloudEnvironmentRequest
  property_count: 23
  slug: cloudera-create-awsgov-cloud-environment-request
- name: CreateAzureClusterRequest
  property_count: 20
  slug: cloudera-create-azure-cluster-request
- name: CreateAzureDatalakeRequest
  property_count: 15
  slug: cloudera-create-azure-datalake-request
- name: CreateAzureEnvironmentRequest
  property_count: 31
  slug: cloudera-create-azure-environment-request
- name: CreateBackupRequest
  property_count: 7
  slug: cloudera-create-backup-request
- name: CreateClusterRequest
  property_count: 14
  slug: cloudera-create-cluster-request
- name: CreateDataShareRequest
  property_count: 9
  slug: cloudera-create-data-share-request
- name: CreateDatabaseRequest
  property_count: 22
  slug: cloudera-create-database-request
- name: CreateDeploymentRequest
  property_count: 26
  slug: cloudera-create-deployment-request
- name: CreateGCPClusterRequest
  property_count: 14
  slug: cloudera-create-gcpcluster-request
- name: CreateGCPDatalakeRequest
  property_count: 11
  slug: cloudera-create-gcpdatalake-request
- name: CreateGCPEnvironmentRequest
  property_count: 20
  slug: cloudera-create-gcpenvironment-request
- name: CreateLdapProviderRequest
  property_count: 18
  slug: cloudera-create-ldap-provider-request
- name: CreateMlServingAppRequest
  property_count: 11
  slug: cloudera-create-ml-serving-app-request
- name: CreateModelRegistryRequest
  property_count: 18
  slug: cloudera-create-model-registry-request
- name: CreatePrivateEnvironmentRequest
  property_count: 15
  slug: cloudera-create-private-environment-request
- name: CreatePrivateLinkEndpointRequest
  property_count: 6
  slug: cloudera-create-private-link-endpoint-request
- name: CreateVcRequest
  property_count: 18
  slug: cloudera-create-vc-request
- name: CreateVwRequest
  property_count: 23
  slug: cloudera-create-vw-request
- name: CreateWorkspaceRequest
  property_count: 24
  slug: cloudera-create-workspace-request
- name: DeletePolicyRequest
  property_count: 3
  slug: cloudera-delete-policy-request
- name: DeletePrivateLinkEndpointRequest
  property_count: 3
  slug: cloudera-delete-private-link-endpoint-request
- name: DescribeClusterResponse
  property_count: 36
  slug: cloudera-describe-cluster-response
- name: DescribeCustomCatalogResponse
  property_count: 3
  slug: cloudera-describe-custom-catalog-response
- name: DescribeCustomImageResponse
  property_count: 9
  slug: cloudera-describe-custom-image-response
- name: DescribeDefaultImageResponse
  property_count: 2
  slug: cloudera-describe-default-image-response
- name: DescribeUpgradeDatabaseResponse
  property_count: 5
  slug: cloudera-describe-upgrade-database-response
- name: EnableServiceRequest
  property_count: 36
  slug: cloudera-enable-service-request
- name: ExecutePolicyRequest
  property_count: 5
  slug: cloudera-execute-policy-request
- name: FindDefaultImageRequest
  property_count: 4
  slug: cloudera-find-default-image-request
- name: GetArchivingStatusResponse
  property_count: 3
  slug: cloudera-get-archiving-status-response
- name: GetClusterConfigResponse
  property_count: 6
  slug: cloudera-get-cluster-config-response
- name: GetCommandStatusResponse
  property_count: 10
  slug: cloudera-get-command-status-response
- name: GetDataShareResponse
  property_count: 13
  slug: cloudera-get-data-share-response
- name: GetOperationDetailsResponse
  property_count: 13
  slug: cloudera-get-operation-details-response
- name: GetOperationStatusResponse
  property_count: 10
  slug: cloudera-get-operation-status-response
- name: GetPolicyResponse
  property_count: 2
  slug: cloudera-get-policy-response
- name: GetPrivateLinkStatusRequest
  property_count: 4
  slug: cloudera-get-private-link-status-request
- name: GetTableStatusDetailsRequest
  property_count: 5
  slug: cloudera-get-table-status-details-request
- name: ImportFlowDefinitionResponse
  property_count: 10
  slug: cloudera-import-flow-definition-response
- name: LaunchProfilersRequest
  property_count: 5
  slug: cloudera-launch-profilers-request
- name: ListBackupEntitiesResponse
  property_count: 1
  slug: cloudera-list-backup-entities-response
- name: ListBackupsRequest
  property_count: 5
  slug: cloudera-list-backups-request
- name: ListBackupsResponse
  property_count: 1
  slug: cloudera-list-backups-response
- name: ListClustersRequest
  property_count: 8
  slug: cloudera-list-clusters-request
- name: ListClustersResponse
  property_count: 4
  slug: cloudera-list-clusters-response
- name: ListComputeUsageRecordsRequest
  property_count: 4
  slug: cloudera-list-compute-usage-records-request
- name: ListComputeUsageRecordsResponse
  property_count: 2
  slug: cloudera-list-compute-usage-records-response
- name: ListDataSharesRequest
  property_count: 5
  slug: cloudera-list-data-shares-request
- name: ListDeploymentEventsRequest
  property_count: 6
  slug: cloudera-list-deployment-events-request
- name: ListEventsRequest
  property_count: 13
  slug: cloudera-list-events-request
- name: ListExternalUsersRequest
  property_count: 5
  slug: cloudera-list-external-users-request
- name: ListFlowsInDeploymentRequest
  property_count: 6
  slug: cloudera-list-flows-in-deployment-request
- name: ListInstanceTypeConfigurationRequest
  property_count: 6
  slug: cloudera-list-instance-type-configuration-request
- name: ListOutstandingArchiveBatchesRequest
  property_count: 4
  slug: cloudera-list-outstanding-archive-batches-request
- name: ListOutstandingArchiveBatchesResponse
  property_count: 2
  slug: cloudera-list-outstanding-archive-batches-response
- name: ListRelevantInstancesRequest
  property_count: 6
  slug: cloudera-list-relevant-instances-request
- name: ListRestoreSnapshotsRequest
  property_count: 8
  slug: cloudera-list-restore-snapshots-request
- name: ListRestoresRequest
  property_count: 2
  slug: cloudera-list-restores-request
- name: ListRestoresResponse
  property_count: 1
  slug: cloudera-list-restores-response
- name: ListTasksRequest
  property_count: 4
  slug: cloudera-list-tasks-request
- name: ModifyClusterInstanceGroupRequest
  property_count: 7
  slug: cloudera-modify-cluster-instance-group-request
- name: RestoreDatalakeRequest
  property_count: 11
  slug: cloudera-restore-datalake-request
- name: RestoreSnapshotResponse
  property_count: 9
  slug: cloudera-restore-snapshot-response
- name: RevokePrivateLinkServiceAccessRequest
  property_count: 5
  slug: cloudera-revoke-private-link-service-access-request
- name: SetFreeipaImageRequest
  property_count: 5
  slug: cloudera-set-freeipa-image-request
- name: SetRuntimeImageRequest
  property_count: 5
  slug: cloudera-set-runtime-image-request
- name: StartGetDiagnosticsCollectionRequest
  property_count: 10
  slug: cloudera-start-get-diagnostics-collection-request
- name: UpdateClusterRequest
  property_count: 8
  slug: cloudera-update-cluster-request
- name: UpdateDataShareRequest
  property_count: 8
  slug: cloudera-update-data-share-request
- name: UpdateDatabaseRequest
  property_count: 7
  slug: cloudera-update-database-request
- name: UpdateDeploymentRequest
  property_count: 17
  slug: cloudera-update-deployment-request
- name: UpdateFlowInDeploymentRequest
  property_count: 8
  slug: cloudera-update-flow-in-deployment-request
- name: UpdateLdapProviderRequest
  property_count: 18
  slug: cloudera-update-ldap-provider-request
- name: UpdatePrivateLinkEndpointRequest
  property_count: 7
  slug: cloudera-update-private-link-endpoint-request
- name: UpdateServiceRequest
  property_count: 11
  slug: cloudera-update-service-request
- name: UpdateVcRequest
  property_count: 10
  slug: cloudera-update-vc-request
- name: UpdateVwRequest
  property_count: 15
  slug: cloudera-update-vw-request
- name: UpgradeDeploymentResponse
  property_count: 6
  slug: cloudera-upgrade-deployment-response
- name: VerifyHbaseClusterPairResponse
  property_count: 5
  slug: cloudera-verify-hbase-cluster-pair-response
jsonld:
- class_count: 0
  name: Cloudera Context
  property_count: 7
  slug: cloudera-context
layout: provider
mcp_servers:
- description: ''
  name: Cloudera MCP Server
  slug: cloudera-mcp-yml
modified: '2026-09-05'
name: Cloudera
nav: Providers
network: true
overview: 'Cloudera publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, CDF Local RPCAPI Version1 API, Cloudprivatelinks API, and 21 more. Tagged areas include Big Data, Data Engineering, Data Lakehouse, Data Platform, and Data Warehouse.


  The Cloudera catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudera''s developer surface includes authentication, documentation, support, GitHub presence, CLI, sandbox, changelog, and 57 more developer resources.'
plans:
- name: Cloudera Plans Pricing
  plan_count: 17
  slug: cloudera-plans-pricing
- name: Cloudera Price Estimates
  plan_count: 0
  slug: cloudera-price-estimates
random_paper: 7
rate_limits:
- limit_count: 0
  name: Cloudera Rate Limits
  slug: cloudera-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Cloudera API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: cloudera-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 100.0
    contract_governance: 19.7
    contract_quality: 45.5
    developer_ergonomics: 80.4
    discoverability: 69.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 68.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/cloudera/cloudera-2026-06-20T174548.png
security:
- kind: authentication
  name: Cloudera Authentication
  slug: cloudera-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Cloudera Domain Security
  slug: cloudera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudera Trust Center
  slug: cloudera-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
skill_count: 4
skills:
- name: cloudera-backup-restore-datalake
  slug: cloudera-backup-restore-datalake
- name: cloudera-machine-user-access-keys
  slug: cloudera-machine-user-access-keys
- name: cloudera-manage-datahub-cluster
  slug: cloudera-manage-datahub-cluster
- name: cloudera-provision-cdp-environment
  slug: cloudera-provision-cdp-environment
slug: cloudera
tags:
- Big Data
- Data Engineering
- Data Lakehouse
- Data Platform
- Data Warehouse
- Hadoop
- Hybrid Cloud
- Machine Learning
- Streaming
website: https://www.cloudera.com/
---
