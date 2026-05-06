---
name: Azure Databricks
description: Azure Databricks is an Apache Spark-based analytics platform optimized for Microsoft Azure. It provides a collaborative workspace for data engineers, data scientists, and analysts to work together on big data and machine learning workloads.
image: https://azure.microsoft.com/svghandler/databricks/
tags:
  - Analytics
  - Apache Spark
  - Big Data
  - Data Engineering
  - Machine Learning
created: '2024-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/azure-databricks/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - name: Azure Databricks REST API
    description: Core REST API for managing Azure Databricks workspaces, clusters, jobs, notebooks, and other resources programmatically.
    image: https://azure.microsoft.com/svghandler/databricks/
    humanURL: https://learn.microsoft.com/azure/databricks/
    baseURL: https://<databricks-instance>.azuredatabricks.net/api
    tags:
      - Clusters
      - Jobs
      - Notebooks
      - Workspace
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/
      - type: OpenAPI
        url: openapi/azure-databricks-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/authentication
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/introduction
      - type: JSONSchema
        url: json-schema/azure-databricks-cluster-schema.json
      - type: JSONLD
        url: json-ld/azure-databricks-context.jsonld
    contact:
      - type: Support
        url: https://learn.microsoft.com/answers/tags/166/azure-databricks
  - name: Clusters API
    description: Manage Databricks clusters for running Spark jobs including creating, starting, editing, listing, terminating, and deleting clusters.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/clusters
    tags:
      - Clusters
      - Compute
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/clusters
      - type: OpenAPI
        url: openapi/azure-databricks-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-databricks-cluster-schema.json
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/clusters
  - name: Jobs API
    description: Create, manage, and run jobs on Databricks clusters including scheduling, listing runs, and managing job permissions.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/jobs
    tags:
      - Automation
      - Jobs
      - Scheduling
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/jobs
      - type: OpenAPI
        url: openapi/azure-databricks-openapi.yml
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/jobs
  - name: Workspace API
    description: Manage notebooks, folders, and other workspace objects including listing, importing, exporting, and deleting workspace items.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/workspace
    tags:
      - Folders
      - Notebooks
      - Workspace
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/workspace
      - type: OpenAPI
        url: openapi/azure-databricks-openapi.yml
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/workspace
  - name: DBFS API
    description: Access Databricks File System (DBFS) for file operations including uploading, downloading, listing, and deleting files and directories.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/dbfs
    tags:
      - Files
      - Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/dbfs
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/dbfs
  - name: Libraries API
    description: Manage libraries and dependencies on clusters including installing, uninstalling, and listing library statuses.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/libraries
    tags:
      - Dependencies
      - Libraries
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/libraries
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/libraries
  - name: Secrets API
    description: Manage secrets and secret scopes for secure credential storage including creating scopes, putting secrets, and managing ACLs.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/secrets
    tags:
      - Credentials
      - Secrets
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/secrets
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/secrets
  - name: Token Management API
    description: Create and manage personal access tokens for API authentication including creating, listing, and revoking tokens.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/token
    tags:
      - Authentication
      - Security
      - Tokens
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/token-management
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/tokenmanagement
  - name: SQL Analytics API
    description: Manage SQL warehouses, queries, and dashboards for Databricks SQL analytics workloads.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/sql
    tags:
      - Analytics
      - Queries
      - Sql
      - Warehouses
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/sql/api/
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/warehouses
  - name: MLflow API
    description: Track experiments, log metrics, and manage ML models using the MLflow tracking and registry APIs.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/mlflow
    tags:
      - Experiments
      - Machine Learning
      - Mlops
      - Model Tracking
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/mlflow/
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/experiments
  - name: Instance Pools API
    description: Create and manage instance pools to reduce cluster start and autoscaling times by maintaining a set of idle ready-to-use cloud instances.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/instance-pools
    tags:
      - Clusters
      - Compute
      - Instance Pools
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/compute/pool-index
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/instancepools
  - name: Cluster Policies API
    description: Create, list, and edit cluster policies to control cluster configurations and limit the ability to configure clusters based on a set of rules.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/policies/clusters
    tags:
      - Clusters
      - Governance
      - Policies
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/admin/clusters/policy-definition
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/clusterpolicies
  - name: Repos API
    description: Manage Git repositories within Databricks workspaces for version control of notebooks and files.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/repos
    tags:
      - Git
      - Repositories
      - Version Control
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/repos/
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/repos
  - name: Git Credentials API
    description: Manage Git credentials for authenticating with Git providers when using Databricks Repos.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/git-credentials
    tags:
      - Authentication
      - Credentials
      - Git
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/gitcredentials
  - name: Pipelines API
    description: Create, edit, delete, start, and view details about Delta Live Tables pipelines for building reliable data pipelines.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/pipelines
    tags:
      - Data Engineering
      - Delta Live Tables
      - ETL
      - Pipelines
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/ldp/
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/pipelines
  - name: Permissions API
    description: Manage permissions on workspace objects including clusters, jobs, notebooks, and other resources using access control lists.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/permissions
    tags:
      - Access Control
      - Permissions
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/security/auth/access-control/
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/permissions
  - name: Unity Catalog - Catalogs API
    description: Manage Unity Catalog catalogs for organizing and governing data assets across workspaces.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/catalogs
    tags:
      - Catalogs
      - Data Governance
      - Unity Catalog
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/data-governance/unity-catalog/
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/catalogs
  - name: Unity Catalog - Schemas API
    description: Manage schemas within Unity Catalog catalogs for organizing tables, views, and functions.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/schemas
    tags:
      - Data Governance
      - Schemas
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/schemas
  - name: Unity Catalog - Tables API
    description: Manage tables within Unity Catalog schemas including listing, getting, and deleting tables.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/tables
    tags:
      - Data Governance
      - Tables
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/tables
  - name: Unity Catalog - Volumes API
    description: Manage Unity Catalog volumes for governing non-tabular data such as files and directories.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/volumes
    tags:
      - Storage
      - Unity Catalog
      - Volumes
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/volumes
  - name: Unity Catalog - Grants API
    description: Manage permissions and grants on Unity Catalog objects including catalogs, schemas, tables, and other securable objects.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/permissions
    tags:
      - Data Governance
      - Permissions
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/grants
  - name: Unity Catalog - External Locations API
    description: Manage external locations in Unity Catalog for connecting to cloud storage paths.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/external-locations
    tags:
      - External Locations
      - Storage
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/externallocations
  - name: Unity Catalog - Storage Credentials API
    description: Manage storage credentials in Unity Catalog for authenticating access to cloud storage.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/storage-credentials
    tags:
      - Credentials
      - Security
      - Storage
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/storagecredentials
  - name: Unity Catalog - Metastores API
    description: Manage Unity Catalog metastores which serve as the top-level container for data governance.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/metastores
    tags:
      - Data Governance
      - Metastores
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/metastores
  - name: Model Serving Endpoints API
    description: Create and manage model serving endpoints for deploying machine learning models as REST API endpoints.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/serving-endpoints
    tags:
      - Deployment
      - Inference
      - Machine Learning
      - Model Serving
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/machine-learning/model-serving/create-manage-serving-endpoints
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/servingendpoints
  - name: Model Registry API
    description: Manage registered models and model versions in the Databricks Model Registry for model lifecycle management.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/mlflow/databricks
    tags:
      - Machine Learning
      - Mlops
      - Model Registry
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/modelregistry
  - name: Registered Models API
    description: Manage registered models in Unity Catalog for centralized model governance and sharing.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.1/unity-catalog/models
    tags:
      - Machine Learning
      - Model Registry
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/registeredmodels
  - name: Global Init Scripts API
    description: Manage global cluster initialization scripts that run on every cluster in the workspace.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/global-init-scripts
    tags:
      - Administration
      - Clusters
      - Initialization
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/globalinitscripts
  - name: IP Access Lists API
    description: Manage IP access lists to control network access to Azure Databricks workspaces.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/ip-access-lists
    tags:
      - Access Control
      - Networking
      - Security
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/ipaccesslists
  - name: Statement Execution API
    description: Execute SQL statements on SQL warehouses and retrieve results for programmatic SQL access.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/sql/statements
    tags:
      - Query Execution
      - Sql
      - Warehouses
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/statementexecution
  - name: Command Execution API
    description: Execute commands on running clusters and retrieve results programmatically.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/1.2
    tags:
      - Clusters
      - Commands
      - Execution
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/commandexecution
  - name: Files API
    description: Manage files in Unity Catalog volumes and workspace filesystem with operations for uploading, downloading, and deleting files.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/fs/files
    tags:
      - Files
      - Storage
      - Unity Catalog
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/files
  - name: Apps API
    description: Deploy and manage Databricks Apps including creating, starting, stopping, and listing custom applications.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/apps
    tags:
      - Applications
      - Deployment
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/apps
  - name: Lakeview API
    description: Manage Lakeview dashboards programmatically including creating, updating, and publishing dashboards.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/lakeview
    tags:
      - Dashboards
      - Lakeview
      - Visualization
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/lakeview
  - name: Online Tables API
    description: Manage online tables for low-latency serving of feature data in Unity Catalog.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/online-tables
    tags:
      - Feature Serving
      - Machine Learning
      - Online Tables
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/onlinetables
  - name: Vector Search Indexes API
    description: Manage vector search indexes for similarity search and retrieval-augmented generation workloads.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/vector-search/indexes
    tags:
      - AI
      - RAG
      - Similarity Search
      - Vector Search
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/vectorsearchindexes
  - name: Vector Search Endpoints API
    description: Manage vector search endpoints for hosting vector search indexes.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/vector-search/endpoints
    tags:
      - AI
      - Endpoints
      - Vector Search
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/vectorsearchendpoints
  - name: Query History API
    description: Retrieve query history for SQL warehouses including query text, status, and performance metrics.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/sql/history/queries
    tags:
      - Monitoring
      - Query History
      - Sql
    properties:
      - type: APIReference
        url: https://docs.databricks.com/api/azure/workspace/queryhistory
  - name: Account SCIM API
    description: Manage users, groups, and service principals across the Databricks account using SCIM 2.0 protocol.
    baseURL: https://<databricks-instance>.azuredatabricks.net/api/2.0/account/scim/v2
    tags:
      - Groups
      - Identity Management
      - SCIM
      - Users
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/azure/databricks/reference/scim-2-1
      - type: APIReference
        url: https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/scim/scim-groups
common:
  - type: GettingStarted
    url: https://learn.microsoft.com/azure/databricks/getting-started/
  - type: Pricing
    url: https://azure.microsoft.com/pricing/details/databricks/
  - type: StatusPage
    url: https://status.azuredatabricks.net/
  - type: Security
    url: https://learn.microsoft.com/azure/databricks/security/
  - type: SDK
    url: https://learn.microsoft.com/azure/databricks/dev-tools/
  - type: CLI
    url: https://learn.microsoft.com/azure/databricks/dev-tools/cli/
  - type: Authentication
    url: https://learn.microsoft.com/azure/databricks/dev-tools/auth/
  - type: APIReference
    url: https://learn.microsoft.com/azure/databricks/reference/api
  - type: ReleaseNotes
    url: https://learn.microsoft.com/azure/databricks/release-notes/product/
  - type: ChangeLog
    url: https://learn.microsoft.com/azure/databricks/release-notes/
  - type: Support
    url: https://learn.microsoft.com/answers/tags/166/azure-databricks
  - type: SDK
    url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-python
    title: Python SDK
  - type: SDK
    url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-java
    title: Java SDK
  - type: SDK
    url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-go
    title: Go SDK
  - type: SDK
    url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-r
    title: R SDK
  - type: GitHubRepository
    url: https://github.com/Azure/azure-databricks-client
  - type: OpenAPI
    url: openapi/azure-databricks-openapi.yml
  - type: JSONSchema
    url: json-schema/azure-databricks-cluster-schema.json
  - type: JSONLD
    url: json-ld/azure-databricks-context.jsonld
  - type: SpectralRules
    url: rules/azure-databricks-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/azure-databricks-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-engineering.yaml
  - type: Features
    data:
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
  - type: UseCases
    data:
      - Building and managing data lakehouse architectures
      - Training and deploying machine learning models at scale
      - Running ETL pipelines for data transformation
      - Interactive data exploration and ad-hoc analytics
      - Real-time streaming analytics with Structured Streaming
      - Building retrieval-augmented generation (RAG) applications
      - Data governance and compliance with Unity Catalog
      - Collaborative data science with shared notebooks
  - type: Integrations
    data:
      - Azure Data Factory for orchestration
      - Azure Synapse Analytics for data warehousing
      - Azure Data Lake Storage for scalable storage
      - Azure Key Vault for secret management
      - Azure Active Directory for authentication
      - Power BI for business intelligence dashboards
      - Terraform for infrastructure as code
      - Apache Kafka for streaming data ingestion
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
