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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 2
  name: Databricks Agentic Access
  operation_count: 25
  slug: databricks-agentic-access
  summary_line: 25 operations · 15 acting · 2 human-in-the-loop
api_count: 57
apis:
- description: Databricks is a cloud-based data platform that simplifies and accelerates the process of preparing and analyzing large volumes of data. The platform integrates with popular data sources and tools, all
  name: Databricks
  slug: databricks
- description: The Databricks File System (DBFS) API is a distributed file system mounted into a Databricks workspace and available on Databricks clusters. The API enables you to interact with object storage using d
  name: Databricks DBFS API
  slug: dbfs-api
- description: The Databricks SQL Warehouses API allows you to create, edit, list, start, stop, and delete SQL warehouses. SQL warehouses are compute resources that enable you to run SQL commands on data objects wit
  name: Databricks SQL Warehouses API
  slug: sql-warehouses-api
- description: The Databricks Pipelines API allows you to create, edit, delete, start, and stop Delta Live Tables pipelines. Delta Live Tables is a declarative framework for building reliable, maintainable, and test
  name: Databricks Pipelines API
  slug: pipelines-api
- description: The Databricks Serving Endpoints API allows you to create, update, query, and delete model serving endpoints. Mosaic AI Model Serving provides a unified interface to deploy, govern, and query AI model
  name: Databricks Serving Endpoints API
  slug: serving-endpoints-api
- description: The Databricks Secrets API allows you to manage secrets, secret scopes, and secret ACLs. Secrets provide a secure way to store and reference credentials and other sensitive information in notebooks an
  name: Databricks Secrets API
  slug: secrets-api
- description: The Databricks Instance Pools API allows you to create, edit, delete, and list instance pools. Instance pools reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use clo
  name: Databricks Instance Pools API
  slug: instance-pools-api
- description: The Databricks Token Management API enables workspace administrators to manage personal access tokens for users and service principals. It allows creating, listing, and revoking tokens, providing cent
  name: Databricks Token Management API
  slug: token-management-api
- description: The Databricks Catalogs API is part of Unity Catalog and allows you to create, update, list, and delete catalogs. Catalogs are the top-level container for data objects in Unity Catalog, providing a th
  name: Databricks Catalogs API
  slug: catalogs-api
- description: The Databricks Vector Search Indexes API allows you to create, manage, query, and delete vector search indexes. Vector Search enables you to store vector representations of your data and perform simil
  name: Databricks Vector Search Indexes API
  slug: vector-search-indexes-api
- description: The Databricks Model Versions API allows you to manage model versions within the Unity Catalog model registry. It provides programmatic access to create, update, list, and delete model versions, enabl
  name: Databricks Model Versions API
  slug: model-versions-api
- description: The Databricks Permissions API allows you to manage permissions on workspace objects such as clusters, jobs, notebooks, and SQL warehouses. It provides programmatic access to get, set, and update acce
  name: Databricks Permissions API
  slug: permissions-api
- description: The Databricks Repos API allows you to manage Git repositories within a Databricks workspace. It provides programmatic access to create, update, delete, and list repos, as well as perform Git operatio
  name: Databricks Repos API
  slug: repos-api
- description: The Databricks Git Credentials API allows you to manage Git credentials for authenticating with Git providers. It provides programmatic access to create, update, delete, and list stored Git credential
  name: Databricks Git Credentials API
  slug: git-credentials-api
- description: The Databricks Cluster Policies API allows administrators to create, edit, delete, and list cluster policies. Cluster policies limit the ability to configure clusters based on a set of rules, enabling
  name: Databricks Cluster Policies API
  slug: cluster-policies-api
- description: The Databricks Libraries API allows you to install, uninstall, and list libraries on clusters. It provides programmatic management of Python, Java, Scala, and R library dependencies for cluster worklo
  name: Databricks Libraries API
  slug: libraries-api
- description: The Databricks Global Init Scripts API enables workspace administrators to manage global initialization scripts that run on every cluster in the workspace. It provides programmatic access to create, u
  name: Databricks Global Init Scripts API
  slug: global-init-scripts-api
- description: The Databricks Command Execution API allows you to execute Python, Scala, SQL, or R commands on running Databricks clusters. It provides programmatic access to create execution contexts, run commands,
  name: Databricks Command Execution API
  slug: command-execution-api
- description: The Databricks Statement Execution API allows you to execute SQL statements on Databricks SQL warehouses and retrieve results. It provides a synchronous and asynchronous interface for running SQL quer
  name: Databricks Statement Execution API
  slug: statement-execution-api
- description: The Databricks Queries API allows you to create, update, delete, list, and run saved SQL queries in Databricks SQL. It provides programmatic management of SQL query objects, enabling automation of ana
  name: Databricks Queries API
  slug: queries-api
- description: The Databricks Alerts API allows you to create, update, delete, and list alerts in Databricks SQL. Alerts automate query execution, evaluate custom conditions, and deliver notifications when those con
  name: Databricks Alerts API
  slug: alerts-api
- description: The Databricks Schemas API is part of Unity Catalog and allows you to create, update, list, and delete schemas. Schemas, also known as databases, reside within catalogs and contain tables, views, volu
  name: Databricks Schemas API
  slug: schemas-api
- description: 'The Databricks Tables API is part of Unity Catalog and allows you to create, update, list, and delete tables. Tables reside within schemas and represent structured data assets, supporting managed and '
  name: Databricks Tables API
  slug: tables-api
- description: The Databricks Volumes API is part of Unity Catalog and allows you to create, update, list, and delete volumes. Volumes provide a governed location for storing and accessing non-tabular data files suc
  name: Databricks Volumes API
  slug: volumes-api
- description: The Databricks Functions API is part of Unity Catalog and allows you to create, list, and delete user-defined functions. Functions reside within schemas and can be used in SQL queries and notebooks, w
  name: Databricks Functions API
  slug: functions-api
- description: The Databricks Grants API is part of Unity Catalog and allows you to get, update, and manage permissions on Unity Catalog securable objects. It provides programmatic control over access to catalogs, s
  name: Databricks Grants API
  slug: grants-api
- description: The Databricks External Locations API is part of Unity Catalog and allows you to create, update, list, and delete external locations. External locations combine a cloud storage path with a storage cre
  name: Databricks External Locations API
  slug: external-locations-api
- description: The Databricks Storage Credentials API is part of Unity Catalog and allows you to create, update, list, and delete storage credentials. Storage credentials contain long-term cloud credentials that pro
  name: Databricks Storage Credentials API
  slug: storage-credentials-api
- description: The Databricks Metastores API is part of Unity Catalog and allows you to create, update, list, and delete metastores. A metastore is the top-level container of objects in Unity Catalog, providing cent
  name: Databricks Metastores API
  slug: metastores-api
- description: The Databricks Connections API is part of Unity Catalog and allows you to create, update, list, and delete connections to external data sources. Connections enable federated queries across external da
  name: Databricks Connections API
  slug: connections-api
- description: The Databricks Registered Models API allows you to create, update, list, and delete registered models in the Unity Catalog model registry. It provides centralized model lifecycle management with versi
  name: Databricks Registered Models API
  slug: registered-models-api
- description: The Databricks Experiments API allows you to create, update, list, and manage MLflow experiments. Experiments are the primary unit of organization in MLflow, grouping runs that track parameters, metri
  name: Databricks Experiments API
  slug: experiments-api
- description: The Databricks Online Tables API allows you to create, get, and delete online tables. Online tables are materialized copies of Delta tables optimized for low-latency lookups, enabling real-time featur
  name: Databricks Online Tables API
  slug: online-tables-api
- description: The Databricks Quality Monitors API allows you to create, update, get, and delete data quality monitors for tables. Quality monitors enable automated data profiling and anomaly detection, providing co
  name: Databricks Quality Monitors API
  slug: quality-monitors-api
- description: 'The Databricks Vector Search Endpoints API allows you to create, list, get, and delete vector search endpoints. Vector search endpoints are compute resources that host vector search indexes, enabling '
  name: Databricks Vector Search Endpoints API
  slug: vector-search-endpoints-api
- description: The Databricks Shares API is part of Delta Sharing and allows you to create, update, list, and delete shares. A share is a read-only logical collection of tables and table partitions that a data provi
  name: Databricks Shares API
  slug: shares-api
- description: The Databricks Recipients API is part of Delta Sharing and allows you to create, update, list, and delete recipients. A recipient is an entity that receives shared data from a provider, and can be eit
  name: Databricks Recipients API
  slug: recipients-api
- description: The Databricks Providers API is part of Delta Sharing and allows you to create, update, list, and delete data providers. Providers represent organizations that share data through Delta Sharing, enabli
  name: Databricks Providers API
  slug: providers-api
- description: The Databricks Clean Rooms API allows you to create, update, list, and delete clean rooms. Clean rooms use Delta Sharing and serverless compute to provide a secure and privacy-protecting environment w
  name: Databricks Clean Rooms API
  slug: clean-rooms-api
- description: The Databricks Notification Destinations API allows you to create, update, list, and delete notification destinations for a workspace. Notification destinations define where alerts and notifications a
  name: Databricks Notification Destinations API
  slug: notification-destinations-api
- description: The Databricks Apps API allows you to create, deploy, manage, and delete Databricks Apps. Apps run directly on a Databricks workspace, integrating with workspace data and services to build custom data
  name: Databricks Apps API
  slug: apps-api
- description: The Databricks Lakeview API allows you to create, update, get, list, and delete AI/BI dashboards. Lakeview dashboards provide a modern visualization experience built on top of Databricks SQL, enabling
  name: Databricks Lakeview API
  slug: lakeview-api
- description: The Databricks Files API provides a standard HTTP interface for reading, writing, listing, and deleting files and directories in Unity Catalog volumes and other workspace storage locations. It support
  name: Databricks Files API
  slug: files-api
- description: The Databricks Tokens API allows you to create, list, and revoke personal access tokens. Personal access tokens are used to authenticate with the Databricks REST API and integrations, providing an alt
  name: Databricks Tokens API
  slug: tokens-api
- description: The Databricks IP Access Lists API allows administrators to configure IP allow lists and block lists for a workspace. It provides programmatic management of network security rules to restrict access t
  name: Databricks IP Access Lists API
  slug: ip-access-lists-api
- description: 'The Databricks Current User API allows you to retrieve information about the currently authenticated user or service principal. It returns identity details including username, display name, and group '
  name: Databricks Current User API
  slug: current-user-api
- description: The Databricks Groups API allows you to create, update, list, and delete groups in a workspace. Groups simplify identity management by enabling administrators to assign access permissions to collectio
  name: Databricks Groups API
  slug: groups-api
- description: 'The Databricks Service Principals API allows you to create, update, list, and delete service principals in a workspace. Service principals are identities for automated tools, jobs, scripts, apps, and '
  name: Databricks Service Principals API
  slug: service-principals-api
- description: The Databricks Users API allows you to create, update, list, and delete users in a workspace. It provides programmatic management of user identities and their workspace access, supporting SCIM protoco
  name: Databricks Users API
  slug: users-api
- description: The Databricks Dashboards API allows you to create, update, list, and delete legacy SQL dashboards. Dashboards provide visual representations of query results, enabling business intelligence reporting
  name: Databricks Dashboards API
  slug: dashboards-api
- description: The Databricks Model Registry API provides the workspace model registry for managing the full lifecycle of ML models. It enables creating registered models, managing model versions, transitioning stag
  name: Databricks Model Registry API
  slug: model-registry-api
- description: The Databricks Workspace Bindings API allows you to manage the binding of Unity Catalog securables to specific workspaces. It enables configuring whether catalogs and other objects are available acros
  name: Databricks Workspace Bindings API
  slug: workspace-bindings-api
- description: The Databricks System Schemas API allows you to enable, disable, and list system schemas within a metastore. System schemas contain system tables that provide operational data about your Databricks ac
  name: Databricks System Schemas API
  slug: system-schemas-api
- description: 'The Databricks Table Constraints API allows you to create and delete primary key and foreign key constraints on Unity Catalog tables. Table constraints define relationships between tables, supporting '
  name: Databricks Table Constraints API
  slug: table-constraints-api
- description: Manage Databricks clusters for running data engineering and data science workloads on Apache Spark.
  name: Databricks Clusters API
  slug: databricks-clusters-api
- description: Create and manage automated workloads including notebooks, JARs, Python scripts, and multi-task workflows.
  name: Databricks Jobs API
  slug: databricks-jobs-api
- description: Manage workspace objects such as notebooks, folders, and libraries.
  name: Databricks Workspace API
  slug: databricks-workspace-api
arazzos:
- description: Resolve a cluster's current state, then pull its recent lifecycle events.
  name: Databricks Audit Cluster Lifecycle Events
  slug: databricks-audit-cluster-events-workflow
- description: Find a job's active run and cancel it, then confirm cancellation.
  name: Databricks Cancel a Job's Active Run
  slug: databricks-cancel-all-active-runs-workflow
- description: Cancel an active run and poll until it reaches a terminal state.
  name: Databricks Cancel Job Run and Confirm Terminal
  slug: databricks-cancel-run-and-confirm-workflow
- description: List a workspace directory's contents, then recursively delete it.
  name: Databricks Inspect and Recursively Delete a Directory
  slug: databricks-cleanup-workspace-directory-workflow
- description: Read an existing job's settings and create a new job that reuses them.
  name: Databricks Clone a Job From an Existing One
  slug: databricks-clone-job-settings-workflow
- description: Create a new job from settings, then immediately trigger its first run.
  name: Databricks Create Job and Trigger First Run
  slug: databricks-create-and-run-job-workflow
- description: Cancel a job's active run if present, then delete the job and its runs.
  name: Databricks Drain Active Runs Then Delete Job
  slug: databricks-delete-job-and-cleanup-runs-workflow
- description: Read a cluster, apply edited configuration, and poll until RUNNING.
  name: Databricks Edit Cluster Configuration and Verify
  slug: databricks-edit-cluster-and-verify-workflow
- description: Export a notebook's content and re-import it to a new workspace path.
  name: Databricks Export a Notebook and Re-Import as a Copy
  slug: databricks-export-and-reimport-notebook-workflow
- description: Resolve a cluster by name from the list, then start it if terminated.
  name: Databricks Find Terminated Cluster by Name and Start It
  slug: databricks-find-cluster-and-start-workflow
- description: Look up a job by exact name, then trigger an immediate run of it.
  name: Databricks Find Job by Name and Run It
  slug: databricks-find-job-and-run-workflow
- description: Create a workspace directory, import a notebook into it, then verify status.
  name: Databricks Create Directory and Import Notebook
  slug: databricks-import-notebook-and-verify-workflow
- description: Find a job's most recent completed run and retrieve its output.
  name: Databricks Fetch Latest Completed Run Output for a Job
  slug: databricks-latest-run-output-workflow
- description: Create a cluster, wait until RUNNING, then create a job bound to that cluster.
  name: Databricks Provision Cluster Then Create Job On It
  slug: databricks-provision-cluster-and-create-job-workflow
- description: Create a Spark cluster and poll its state until it reaches RUNNING.
  name: Databricks Provision Cluster and Wait Until Running
  slug: databricks-provision-cluster-workflow
- description: Restart a running cluster and poll until it returns to RUNNING.
  name: Databricks Restart Cluster and Verify Running
  slug: databricks-restart-cluster-and-verify-workflow
- description: Trigger a job run, wait for it to finish, then export the source notebook.
  name: Databricks Run Job, Wait, Then Export the Notebook
  slug: databricks-run-job-and-export-notebook-workflow
- description: Trigger a job run, poll the run until terminal, then fetch its output.
  name: Databricks Trigger Job Run and Wait for Output
  slug: databricks-run-job-and-wait-workflow
- description: Run a job, wait for terminal state, then branch on the result state.
  name: Databricks Run Job and Branch on Success or Failure
  slug: databricks-run-job-on-failure-export-output-workflow
- description: Import a notebook, create a job that runs it, then trigger the first run.
  name: Databricks Stage Notebook Then Create and Run a Job
  slug: databricks-stage-notebook-and-create-job-workflow
- description: Start a terminated cluster, wait until RUNNING, then trigger a job run.
  name: Databricks Start Cluster Then Run Job
  slug: databricks-start-cluster-and-run-job-workflow
- description: Terminate a cluster, confirm it is TERMINATED, then permanently delete it.
  name: Databricks Terminate Then Permanently Delete Cluster
  slug: databricks-terminate-and-delete-cluster-workflow
- description: Read a job, partially update its settings, then trigger a fresh run.
  name: Databricks Update Job Settings and Re-Run
  slug: databricks-update-job-and-rerun-workflow
artifact_total: 263
collections:
- collection_type: postman
  name: Databricks REST API
  slug: postman-databricks
- collection_type: open
  name: Databricks REST API
  slug: open-databricks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/databricks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/databricks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/databricks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/databricks-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.databricks.com/aws/en/generative-ai/mcp/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/databricks/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-audit-cluster-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-cancel-all-active-runs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-cancel-run-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-cleanup-workspace-directory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-clone-job-settings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-create-and-run-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-delete-job-and-cleanup-runs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-edit-cluster-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-export-and-reimport-notebook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-find-cluster-and-start-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-find-job-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-import-notebook-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-latest-run-output-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-provision-cluster-and-create-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-provision-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-restart-cluster-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-run-job-and-export-notebook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-run-job-and-wait-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-run-job-on-failure-export-output-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-stage-notebook-and-create-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-start-cluster-and-run-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-terminate-and-delete-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/databricks-update-job-and-rerun-workflow.yml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.databricks.com/dev-tools/auth.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.databricks.com/getting-started/index.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.databricks.com/dev-tools/sdks.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.databricks.com/
- group: operate
  title: ''
  type: Support
  url: https://help.databricks.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.databricks.com/api/workspace/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.databricks.com/aws/en/reference/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.databricks.com/product/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.databricks.com/try-databricks
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.databricks.com/legal/privacynotice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.databricks.com/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.databricks.com/trust
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.databricks.com/aws/en/resources/limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.databricks.com/aws/en/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.databricks.com/blog
- group: operate
  title: Community Forum
  type: Support
  url: https://community.databricks.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/databricks
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/databricks/databricks-sdk-py
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/databricks/databricks-sdk-go
- group: build
  title: ''
  type: CLI
  url: https://github.com/databricks/cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.databricks.com/aws/en/dev-tools/cli
- group: other
  title: ''
  type: X
  url: https://twitter.com/databricks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/databricks
- group: start
  title: ''
  type: Login
  url: https://login.databricks.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.databricks.com/company/contact
- group: learn
  title: ''
  type: Training
  url: https://www.databricks.com/learn/training/home
- group: learn
  title: ''
  type: Academy
  url: https://customer-academy.databricks.com/learn
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/databricks/databricks-sdk-java
- group: build
  title: Python SQL SDK
  type: SDKs
  url: https://github.com/databricks/databricks-sql-python
- group: build
  title: Terraform Provider
  type: SDKs
  url: https://github.com/databricks/terraform-provider-databricks
- group: docs
  title: MLflow API Reference
  type: APIReference
  url: https://docs.databricks.com/aws/en/reference/mlflow-api
- group: auth
  title: ''
  type: Security
  url: https://www.databricks.com/trust/security-features
- group: auth
  title: ''
  type: Authentication
  url: https://docs.databricks.com/aws/en/dev-tools/auth
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.databricks.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/databricks-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/databricks-cluster-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/databricks-job-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/databricks-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/databricks-spectral-rules.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/databricks/databricks-agent-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.databricks.com/llms.txt
created: '2025-01-14'
description: Collection of Databricks REST APIs for managing workspaces, clusters, jobs, and data operations.
examples:
- key_count: 4
  name: Databricks Access Control Request Example
  slug: databricks-access-control-request-example
- key_count: 2
  name: Databricks Auto Scale Example
  slug: databricks-auto-scale-example
- key_count: 8
  name: Databricks Aws Attributes Example
  slug: databricks-aws-attributes-example
- key_count: 3
  name: Databricks Azure Attributes Example
  slug: databricks-azure-attributes-example
- key_count: 6
  name: Databricks Canceljobrun Example
  slug: databricks-canceljobrun-example
- key_count: 32
  name: Databricks Cluster Details Example
  slug: databricks-cluster-details-example
- key_count: 4
  name: Databricks Cluster Event Example
  slug: databricks-cluster-event-example
- key_count: 18
  name: Databricks Create Cluster Request Example
  slug: databricks-create-cluster-request-example
- key_count: 14
  name: Databricks Create Job Request Example
  slug: databricks-create-job-request-example
- key_count: 6
  name: Databricks Createcluster Example
  slug: databricks-createcluster-example
- key_count: 6
  name: Databricks Createjob Example
  slug: databricks-createjob-example
- key_count: 6
  name: Databricks Createworkspacedirectory Example
  slug: databricks-createworkspacedirectory-example
- key_count: 3
  name: Databricks Cron Schedule Example
  slug: databricks-cron-schedule-example
- key_count: 6
  name: Databricks Deletejob Example
  slug: databricks-deletejob-example
- key_count: 6
  name: Databricks Deleteworkspaceobject Example
  slug: databricks-deleteworkspaceobject-example
- key_count: 16
  name: Databricks Edit Cluster Request Example
  slug: databricks-edit-cluster-request-example
- key_count: 6
  name: Databricks Editcluster Example
  slug: databricks-editcluster-example
- key_count: 2
  name: Databricks Error Response Example
  slug: databricks-error-response-example
- key_count: 6
  name: Databricks Exportworkspaceobject Example
  slug: databricks-exportworkspaceobject-example
- key_count: 3
  name: Databricks Gcp Attributes Example
  slug: databricks-gcp-attributes-example
- key_count: 6
  name: Databricks Getcluster Example
  slug: databricks-getcluster-example
- key_count: 6
  name: Databricks Getjob Example
  slug: databricks-getjob-example
- key_count: 6
  name: Databricks Getjobrun Example
  slug: databricks-getjobrun-example
- key_count: 6
  name: Databricks Getjobrunoutput Example
  slug: databricks-getjobrunoutput-example
- key_count: 6
  name: Databricks Getworkspaceobjectstatus Example
  slug: databricks-getworkspaceobjectstatus-example
- key_count: 5
  name: Databricks Git Source Example
  slug: databricks-git-source-example
- key_count: 6
  name: Databricks Importworkspaceobject Example
  slug: databricks-importworkspaceobject-example
- key_count: 3
  name: Databricks Init Script Info Example
  slug: databricks-init-script-info-example
- key_count: 1
  name: Databricks Job Cluster Example
  slug: databricks-job-cluster-example
- key_count: 5
  name: Databricks Job Email Notifications Example
  slug: databricks-job-email-notifications-example
- key_count: 4
  name: Databricks Job Example
  slug: databricks-job-example
- key_count: 11
  name: Databricks Job Settings Example
  slug: databricks-job-settings-example
- key_count: 7
  name: Databricks Library Example
  slug: databricks-library-example
- key_count: 6
  name: Databricks Listclusterevents Example
  slug: databricks-listclusterevents-example
- key_count: 6
  name: Databricks Listclusters Example
  slug: databricks-listclusters-example
- key_count: 6
  name: Databricks Listjobruns Example
  slug: databricks-listjobruns-example
- key_count: 6
  name: Databricks Listjobs Example
  slug: databricks-listjobs-example
- key_count: 6
  name: Databricks Listworkspaceobjects Example
  slug: databricks-listworkspaceobjects-example
- key_count: 6
  name: Databricks Permanentdeletecluster Example
  slug: databricks-permanentdeletecluster-example
- key_count: 6
  name: Databricks Restartcluster Example
  slug: databricks-restartcluster-example
- key_count: 21
  name: Databricks Run Example
  slug: databricks-run-example
- key_count: 18
  name: Databricks Run Task Example
  slug: databricks-run-task-example
- key_count: 6
  name: Databricks Runjobnow Example
  slug: databricks-runjobnow-example
- key_count: 6
  name: Databricks Spark Node Example
  slug: databricks-spark-node-example
- key_count: 6
  name: Databricks Startcluster Example
  slug: databricks-startcluster-example
- key_count: 19
  name: Databricks Task Settings Example
  slug: databricks-task-settings-example
- key_count: 6
  name: Databricks Terminatecluster Example
  slug: databricks-terminatecluster-example
- key_count: 6
  name: Databricks Updatejob Example
  slug: databricks-updatejob-example
- key_count: 4
  name: Databricks Webhook Notifications Example
  slug: databricks-webhook-notifications-example
- key_count: 8
  name: Databricks Workspace Object Example
  slug: databricks-workspace-object-example
features:
- 'Jobs Compute: ~$0.07-$0.15/DBU (cheapest)'
- 'All-Purpose Compute: ~$0.55/DBU (interactive)'
- 'SQL Serverless: ~$0.70/DBU (infra included)'
- 'Serverless Jobs: $0.35-$0.40/DBU'
- 'Editions: Standard (Azure legacy), Premium (default), Enterprise (AWS)'
- 'Multi-cloud: AWS, Azure, GCP'
- 'REST API: 30 req/sec default, 10 req/sec for jobs/run-now'
- DBSQL Statement Execution API
- Unity Catalog for governance
- Delta Lake table format
- Mosaic AI / MLflow for ML lifecycle
- Genie / AI/BI for natural-language analytics
- Workflows for orchestration
- Lakeflow Connect for data ingestion
- Model Serving for low-latency inference
- Committed Use Contracts for volume discounts
finops:
- name: Databricks Finops
  service_category: Data Lakehouse
  slug: databricks-finops
graphqls:
- description: Databricks does not currently offer a native GraphQL API. Its public surface area is entirely REST-based, documented at [https://docs.databricks.com/api/workspace/introduction](https://docs.databricks
  name: Databricks GraphQL Schema
  slug: databricks-graphql
image: https://www.databricks.com/en-website-assets/static/f9f2b15ae456c41f7d2e5b303c8c6c6e/databricks-logo.svg
json_schemas:
- name: AccessControlRequest
  property_count: 4
  slug: databricks-access-control-request
- name: AccessControlRequest
  property_count: 4
  slug: databricks-accesscontrolrequest
- name: AutoScale
  property_count: 2
  slug: databricks-auto-scale
- name: AutoScale
  property_count: 2
  slug: databricks-autoscale
- name: AwsAttributes
  property_count: 8
  slug: databricks-aws-attributes
- name: AwsAttributes
  property_count: 8
  slug: databricks-awsattributes
- name: AzureAttributes
  property_count: 3
  slug: databricks-azure-attributes
- name: AzureAttributes
  property_count: 3
  slug: databricks-azureattributes
- name: ClusterDetails
  property_count: 32
  slug: databricks-cluster-details
- name: ClusterEvent
  property_count: 4
  slug: databricks-cluster-event
- name: Databricks Cluster
  property_count: 40
  slug: databricks-cluster
- name: ClusterDetails
  property_count: 34
  slug: databricks-clusterdetails
- name: ClusterEvent
  property_count: 4
  slug: databricks-clusterevent
- name: CreateClusterRequest
  property_count: 18
  slug: databricks-create-cluster-request
- name: CreateJobRequest
  property_count: 14
  slug: databricks-create-job-request
- name: CreateClusterRequest
  property_count: 22
  slug: databricks-createclusterrequest
- name: CreateJobRequest
  property_count: 18
  slug: databricks-createjobrequest
- name: CronSchedule
  property_count: 3
  slug: databricks-cron-schedule
- name: CronSchedule
  property_count: 3
  slug: databricks-cronschedule
- name: EditClusterRequest
  property_count: 16
  slug: databricks-edit-cluster-request
- name: EditClusterRequest
  property_count: 17
  slug: databricks-editclusterrequest
- name: ErrorResponse
  property_count: 2
  slug: databricks-error-response
- name: ErrorResponse
  property_count: 2
  slug: databricks-errorresponse
- name: GcpAttributes
  property_count: 3
  slug: databricks-gcp-attributes
- name: GcpAttributes
  property_count: 3
  slug: databricks-gcpattributes
- name: GitSource
  property_count: 5
  slug: databricks-git-source
- name: GitSource
  property_count: 5
  slug: databricks-gitsource
- name: InitScriptInfo
  property_count: 3
  slug: databricks-init-script-info
- name: InitScriptInfo
  property_count: 3
  slug: databricks-initscriptinfo
- name: JobCluster
  property_count: 1
  slug: databricks-job-cluster
- name: JobEmailNotifications
  property_count: 5
  slug: databricks-job-email-notifications
- name: Job
  property_count: 4
  slug: databricks-job
- name: JobSettings
  property_count: 11
  slug: databricks-job-settings
- name: JobCluster
  property_count: 2
  slug: databricks-jobcluster
- name: JobEmailNotifications
  property_count: 5
  slug: databricks-jobemailnotifications
- name: JobSettings
  property_count: 15
  slug: databricks-jobsettings
- name: Library
  property_count: 7
  slug: databricks-library
- name: Run
  property_count: 21
  slug: databricks-run
- name: RunTask
  property_count: 18
  slug: databricks-run-task
- name: RunTask
  property_count: 19
  slug: databricks-runtask
- name: SparkNode
  property_count: 6
  slug: databricks-spark-node
- name: SparkNode
  property_count: 6
  slug: databricks-sparknode
- name: TaskSettings
  property_count: 19
  slug: databricks-task-settings
- name: TaskSettings
  property_count: 21
  slug: databricks-tasksettings
- name: WebhookNotifications
  property_count: 4
  slug: databricks-webhook-notifications
- name: WebhookNotifications
  property_count: 4
  slug: databricks-webhooknotifications
- name: WorkspaceObject
  property_count: 8
  slug: databricks-workspace-object
- name: WorkspaceObject
  property_count: 8
  slug: databricks-workspaceobject
json_structures:
- name: Databricks Access Control Request Structure
  property_count: 4
  slug: databricks-access-control-request-structure
- name: Databricks Auto Scale Structure
  property_count: 2
  slug: databricks-auto-scale-structure
- name: Databricks Aws Attributes Structure
  property_count: 8
  slug: databricks-aws-attributes-structure
- name: Databricks Azure Attributes Structure
  property_count: 3
  slug: databricks-azure-attributes-structure
- name: Databricks Cluster Details Structure
  property_count: 32
  slug: databricks-cluster-details-structure
- name: Databricks Cluster Event Structure
  property_count: 4
  slug: databricks-cluster-event-structure
- name: Databricks Create Cluster Request Structure
  property_count: 18
  slug: databricks-create-cluster-request-structure
- name: Databricks Create Job Request Structure
  property_count: 14
  slug: databricks-create-job-request-structure
- name: Databricks Cron Schedule Structure
  property_count: 3
  slug: databricks-cron-schedule-structure
- name: Databricks Edit Cluster Request Structure
  property_count: 16
  slug: databricks-edit-cluster-request-structure
- name: Databricks Error Response Structure
  property_count: 2
  slug: databricks-error-response-structure
- name: Databricks Gcp Attributes Structure
  property_count: 3
  slug: databricks-gcp-attributes-structure
- name: Databricks Git Source Structure
  property_count: 5
  slug: databricks-git-source-structure
- name: Databricks Init Script Info Structure
  property_count: 3
  slug: databricks-init-script-info-structure
- name: Databricks Job Cluster Structure
  property_count: 1
  slug: databricks-job-cluster-structure
- name: Databricks Job Email Notifications Structure
  property_count: 5
  slug: databricks-job-email-notifications-structure
- name: Databricks Job Settings Structure
  property_count: 11
  slug: databricks-job-settings-structure
- name: Databricks Job Structure
  property_count: 4
  slug: databricks-job-structure
- name: Databricks Library Structure
  property_count: 7
  slug: databricks-library-structure
- name: Databricks Run Structure
  property_count: 21
  slug: databricks-run-structure
- name: Databricks Run Task Structure
  property_count: 18
  slug: databricks-run-task-structure
- name: Databricks Spark Node Structure
  property_count: 6
  slug: databricks-spark-node-structure
- name: Databricks Structure
  property_count: 0
  slug: databricks-structure
- name: Databricks Task Settings Structure
  property_count: 19
  slug: databricks-task-settings-structure
- name: Databricks Webhook Notifications Structure
  property_count: 4
  slug: databricks-webhook-notifications-structure
- name: Databricks Workspace Object Structure
  property_count: 8
  slug: databricks-workspace-object-structure
jsonld:
- class_count: 0
  name: Databricks Context
  property_count: 0
  slug: databricks-context
layout: provider
mcp_servers:
- description: Databricks managed MCP servers for Unity Catalog functions, Genie spaces, Databricks SQL, and Vector Search, with Unity Catalog permissions always enforced.
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Databricks
nav: Providers
network: true
overview: 'Databricks publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, Jobs API, and Workspace API. Tagged areas include AI, Analytics, Apache Spark, Big Data, and Clean Rooms.


  The Databricks catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Databricks'' developer surface includes authentication, getting-started guide, support, API reference, documentation, pricing, signup flow, and 63 more developer resources.'
plans:
- name: Databricks Plans Pricing
  plan_count: 5
  slug: databricks-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 4
  name: Databricks Rate Limits
  slug: databricks-rate-limits
rules:
- name: Databricks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: databricks-jsonschema-spectral-rules
- name: Databricks API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 9
  slug: databricks-spectral-rules
score:
  band: exemplar
  composite: 72.2
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 69.6
    developer_ergonomics: 78.3
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 78.9
  previous_composite: 72.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/databricks/refs/heads/main/screenshots/databricks-2026-06-20T175634.png
security:
- kind: authentication
  name: Databricks Authentication
  slug: databricks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Databricks Domain Security
  slug: databricks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Databricks Vulnerability Disclosure
  slug: databricks-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 26
skills:
- name: databricks-agent-bricks
  slug: databricks-agent-bricks
- name: databricks-ai-functions
  slug: databricks-ai-functions
- name: databricks-aibi-dashboards
  slug: databricks-aibi-dashboards
- name: databricks-apps-python
  slug: databricks-apps-python
- name: databricks-apps
  slug: databricks-apps
- name: databricks-core
  slug: databricks-core
- name: databricks-dabs
  slug: databricks-dabs
- name: databricks-dbsql
  slug: databricks-dbsql
- name: databricks-docs
  slug: databricks-docs
- name: databricks-execution-compute
  slug: databricks-execution-compute
- name: databricks-iceberg
  slug: databricks-iceberg
- name: databricks-jobs
  slug: databricks-jobs
- name: databricks-lakebase
  slug: databricks-lakebase
- name: databricks-metric-views
  slug: databricks-metric-views
- name: databricks-mlflow-evaluation
  slug: databricks-mlflow-evaluation
- name: databricks-model-serving
  slug: databricks-model-serving
- name: databricks-pipelines
  slug: databricks-pipelines
- name: databricks-python-sdk
  slug: databricks-python-sdk
- name: databricks-serverless-migration
  slug: databricks-serverless-migration
- name: databricks-spark-structured-streaming
  slug: databricks-spark-structured-streaming
- name: databricks-synthetic-data-gen
  slug: databricks-synthetic-data-gen
- name: databricks-unity-catalog
  slug: databricks-unity-catalog
- name: databricks-unstructured-pdf-generation
  slug: databricks-unstructured-pdf-generation
- name: databricks-vector-search
  slug: databricks-vector-search
slug: databricks
tags:
- AI
- Analytics
- Apache Spark
- Big Data
- Clean Rooms
- Cloud Computing
- Data
- Data Analytics
- Data Engineering
- Data Governance
- Delta Lake
- Delta Sharing
- ETL
- Identity Management
- Lakehouse
- Machine Learning
- MLflow
- Model Serving
- Security
- SQL
- Unity Catalog
- Vector Search
- Visualize
use_cases:
- description: Build and orchestrate ETL pipelines with Delta Live Tables and multi-task workflows.
  name: Data Engineering
- description: Run analytical SQL queries on lakehouse data with serverless SQL warehouses.
  name: Data Warehousing
- description: Train, track, and deploy ML models with MLflow experiment tracking and model registry.
  name: Machine Learning
- description: Process streaming data with structured streaming and serve results through online tables.
  name: Real-Time Analytics
- description: Govern data assets across the organization with Unity Catalog metadata management.
  name: Data Governance
---
