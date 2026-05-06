---
aid: databricks
url: https://raw.githubusercontent.com/api-evangelist/databricks/refs/heads/main/apis.yml
apis:
  - aid: databricks:databricks
    name: Databricks
    tags:
      - Analytics
      - Data
      - Visualize
    humanURL: ' https://www.databricks.com'
    properties:
      - url: ' https://www.databricks.com'
        type: Documentation
      - url: https://docs.databricks.com/api/workspace/introduction
        type: API Reference
    description: Databricks is a cloud-based data platform that simplifies and accelerates the process of preparing and analyzing large volumes of data. The platform integrates with popular data sources and tools, allowing data engineers and data scientists to collaborate and work more efficiently. Databricks offers powerful features such as data visualization, machine learning, and real-time analytics, helping organizations make data-driven decisions and improve their business outcomes.
  - aid: databricks:clusters-api
    name: Databricks Clusters API
    tags:
      - Clusters
      - Compute
      - Infrastructure
    humanURL: https://docs.databricks.com/api/workspace/clusters
    properties:
      - url: https://docs.databricks.com/api/workspace/clusters
        type: Documentation
      - url: openapi/databricks-openapi.yml
        type: OpenAPI
      - url: json-schema/databricks-cluster-schema.json
        type: JSONSchema
      - url: json-schema/databricks-create-cluster-request-schema.json
        type: JSONSchema
      - url: json-schema/databricks-edit-cluster-request-schema.json
        type: JSONSchema
      - url: json-schema/databricks-cluster-details-schema.json
        type: JSONSchema
      - url: json-schema/databricks-spark-node-schema.json
        type: JSONSchema
      - url: json-schema/databricks-auto-scale-schema.json
        type: JSONSchema
      - url: json-schema/databricks-aws-attributes-schema.json
        type: JSONSchema
      - url: json-schema/databricks-azure-attributes-schema.json
        type: JSONSchema
      - url: json-schema/databricks-gcp-attributes-schema.json
        type: JSONSchema
      - url: json-schema/databricks-init-script-info-schema.json
        type: JSONSchema
      - url: json-schema/databricks-cluster-event-schema.json
        type: JSONSchema
      - url: json-schema/databricks-error-response-schema.json
        type: JSONSchema
      - url: json-ld/databricks-context.jsonld
        type: JSONLD
    description: The Databricks Clusters API allows you to create, start, edit, list, terminate, and delete clusters. Clusters are managed cloud resources that enable you to run data engineering and data science workloads on Apache Spark in the cloud. The API provides programmatic control over cluster lifecycle management, configuration, and monitoring.
  - aid: databricks:jobs-api
    name: Databricks Jobs API
    tags:
      - Jobs
      - Orchestration
      - Scheduling
      - Workflows
    humanURL: https://docs.databricks.com/api/workspace/jobs
    properties:
      - url: https://docs.databricks.com/api/workspace/jobs
        type: Documentation
      - url: openapi/databricks-openapi.yml
        type: OpenAPI
      - url: json-schema/databricks-job-schema.json
        type: JSONSchema
      - url: json-schema/databricks-create-job-request-schema.json
        type: JSONSchema
      - url: json-schema/databricks-task-settings-schema.json
        type: JSONSchema
      - url: json-schema/databricks-job-cluster-schema.json
        type: JSONSchema
      - url: json-schema/databricks-job-email-notifications-schema.json
        type: JSONSchema
      - url: json-schema/databricks-webhook-notifications-schema.json
        type: JSONSchema
      - url: json-schema/databricks-cron-schedule-schema.json
        type: JSONSchema
      - url: json-schema/databricks-git-source-schema.json
        type: JSONSchema
      - url: json-schema/databricks-library-schema.json
        type: JSONSchema
      - url: json-schema/databricks-access-control-request-schema.json
        type: JSONSchema
      - url: json-schema/databricks-job-settings-schema.json
        type: JSONSchema
      - url: json-schema/databricks-run-schema.json
        type: JSONSchema
      - url: json-schema/databricks-run-task-schema.json
        type: JSONSchema
      - url: json-ld/databricks-context.jsonld
        type: JSONLD
    description: The Databricks Jobs API allows you to create, edit, delete, and trigger jobs. Jobs are the primary mechanism for running automated workloads on Databricks, including notebooks, JARs, Python scripts, and Spark submit applications. The API supports complex multi-task workflows with dependencies, scheduling, and monitoring capabilities.
  - aid: databricks:dbfs-api
    name: Databricks DBFS API
    tags:
      - Data
      - Files
      - Storage
    humanURL: https://docs.databricks.com/api/workspace/dbfs
    properties:
      - url: https://docs.databricks.com/api/workspace/dbfs
        type: Documentation
    description: The Databricks File System (DBFS) API is a distributed file system mounted into a Databricks workspace and available on Databricks clusters. The API enables you to interact with object storage using directory and file semantics, allowing you to put, get, list, and delete files and directories programmatically.
  - aid: databricks:workspace-api
    name: Databricks Workspace API
    tags:
      - Folders
      - Notebooks
      - Workspace
    humanURL: https://docs.databricks.com/api/workspace/workspace
    properties:
      - url: https://docs.databricks.com/api/workspace/workspace
        type: Documentation
      - url: openapi/databricks-openapi.yml
        type: OpenAPI
      - url: json-schema/databricks-workspace-object-schema.json
        type: JSONSchema
      - url: json-ld/databricks-context.jsonld
        type: JSONLD
    description: The Databricks Workspace API allows you to list, import, export, and delete notebooks, folders, and libraries in a Databricks workspace. It provides programmatic access to manage workspace objects, enabling automation of notebook deployment and workspace organization.
  - aid: databricks:sql-warehouses-api
    name: Databricks SQL Warehouses API
    tags:
      - Analytics
      - SQL
      - Warehouses
    humanURL: https://docs.databricks.com/api/workspace/warehouses
    properties:
      - url: https://docs.databricks.com/api/workspace/warehouses
        type: Documentation
    description: The Databricks SQL Warehouses API allows you to create, edit, list, start, stop, and delete SQL warehouses. SQL warehouses are compute resources that enable you to run SQL commands on data objects within Databricks SQL, providing serverless or classic compute options for analytical workloads.
  - aid: databricks:pipelines-api
    name: Databricks Pipelines API
    tags:
      - Delta Live Tables
      - ETL
      - Pipelines
    humanURL: https://docs.databricks.com/api/workspace/pipelines
    properties:
      - url: https://docs.databricks.com/api/workspace/pipelines
        type: Documentation
    description: The Databricks Pipelines API allows you to create, edit, delete, start, and stop Delta Live Tables pipelines. Delta Live Tables is a declarative framework for building reliable, maintainable, and testable data processing pipelines. The API provides full lifecycle management of ETL pipelines.
  - aid: databricks:serving-endpoints-api
    name: Databricks Serving Endpoints API
    tags:
      - AI
      - Machine Learning
      - Model Serving
    humanURL: https://docs.databricks.com/api/workspace/servingendpoints
    properties:
      - url: https://docs.databricks.com/api/workspace/servingendpoints
        type: Documentation
    description: The Databricks Serving Endpoints API allows you to create, update, query, and delete model serving endpoints. Mosaic AI Model Serving provides a unified interface to deploy, govern, and query AI models, including custom models, generative AI models, and large language models, with high availability and low latency.
  - aid: databricks:secrets-api
    name: Databricks Secrets API
    tags:
      - Credentials
      - Secrets
      - Security
    humanURL: https://docs.databricks.com/api/workspace/secrets
    properties:
      - url: https://docs.databricks.com/api/workspace/secrets
        type: Documentation
    description: The Databricks Secrets API allows you to manage secrets, secret scopes, and secret ACLs. Secrets provide a secure way to store and reference credentials and other sensitive information in notebooks and jobs without exposing them in plaintext.
  - aid: databricks:instance-pools-api
    name: Databricks Instance Pools API
    tags:
      - Clusters
      - Compute
      - Infrastructure
    humanURL: https://docs.databricks.com/api/workspace/instancepools
    properties:
      - url: https://docs.databricks.com/api/workspace/instancepools
        type: Documentation
    description: The Databricks Instance Pools API allows you to create, edit, delete, and list instance pools. Instance pools reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use cloud instances, improving performance and reducing costs for frequently used cluster configurations.
  - aid: databricks:token-management-api
    name: Databricks Token Management API
    tags:
      - Authentication
      - Security
      - Tokens
    humanURL: https://docs.databricks.com/api/workspace/tokenmanagement
    properties:
      - url: https://docs.databricks.com/api/workspace/tokenmanagement
        type: Documentation
    description: The Databricks Token Management API enables workspace administrators to manage personal access tokens for users and service principals. It allows creating, listing, and revoking tokens, providing centralized control over API authentication credentials.
  - aid: databricks:catalogs-api
    name: Databricks Catalogs API
    tags:
      - Data Governance
      - Metadata
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/catalogs
    properties:
      - url: https://docs.databricks.com/api/workspace/catalogs
        type: Documentation
    description: The Databricks Catalogs API is part of Unity Catalog and allows you to create, update, list, and delete catalogs. Catalogs are the top-level container for data objects in Unity Catalog, providing a three-level namespace (catalog.schema.table) for organizing and governing data assets across workspaces.
  - aid: databricks:vector-search-indexes-api
    name: Databricks Vector Search Indexes API
    tags:
      - AI
      - Embeddings
      - Vector Search
    humanURL: https://docs.databricks.com/api/workspace/vectorsearchindexes
    properties:
      - url: https://docs.databricks.com/api/workspace/vectorsearchindexes
        type: Documentation
    description: The Databricks Vector Search Indexes API allows you to create, manage, query, and delete vector search indexes. Vector Search enables you to store vector representations of your data and perform similarity searches, powering retrieval-augmented generation (RAG) applications and other AI use cases.
  - aid: databricks:model-versions-api
    name: Databricks Model Versions API
    tags:
      - Machine Learning
      - MLflow
      - Model Registry
    humanURL: https://docs.databricks.com/api/workspace/modelversions
    properties:
      - url: https://docs.databricks.com/api/workspace/modelversions
        type: Documentation
    description: The Databricks Model Versions API allows you to manage model versions within the Unity Catalog model registry. It provides programmatic access to create, update, list, and delete model versions, enabling automated ML lifecycle management and model governance.
  - aid: databricks:permissions-api
    name: Databricks Permissions API
    tags:
      - Access Control
      - Authorization
      - Security
    humanURL: https://docs.databricks.com/api/workspace/permissions
    properties:
      - url: https://docs.databricks.com/api/workspace/permissions
        type: Documentation
    description: The Databricks Permissions API allows you to manage permissions on workspace objects such as clusters, jobs, notebooks, and SQL warehouses. It provides programmatic access to get, set, and update access control lists for various Databricks resources, enabling fine-grained authorization management.
  - aid: databricks:repos-api
    name: Databricks Repos API
    tags:
      - Git
      - Repositories
      - Version Control
    humanURL: https://docs.databricks.com/api/workspace/repos
    properties:
      - url: https://docs.databricks.com/api/workspace/repos
        type: Documentation
    description: The Databricks Repos API allows you to manage Git repositories within a Databricks workspace. It provides programmatic access to create, update, delete, and list repos, as well as perform Git operations like pulling latest changes, enabling version-controlled notebook and code development.
  - aid: databricks:git-credentials-api
    name: Databricks Git Credentials API
    tags:
      - Authentication
      - Credentials
      - Git
    humanURL: https://docs.databricks.com/api/workspace/gitcredentials
    properties:
      - url: https://docs.databricks.com/api/workspace/gitcredentials
        type: Documentation
    description: The Databricks Git Credentials API allows you to manage Git credentials for authenticating with Git providers. It provides programmatic access to create, update, delete, and list stored Git credentials, enabling seamless integration with GitHub, GitLab, Bitbucket, and other Git hosting services.
  - aid: databricks:cluster-policies-api
    name: Databricks Cluster Policies API
    tags:
      - Clusters
      - Governance
      - Policies
    humanURL: https://docs.databricks.com/api/workspace/clusterpolicies
    properties:
      - url: https://docs.databricks.com/api/workspace/clusterpolicies
        type: Documentation
    description: The Databricks Cluster Policies API allows administrators to create, edit, delete, and list cluster policies. Cluster policies limit the ability to configure clusters based on a set of rules, enabling administrators to enforce cost controls and governance over compute resources.
  - aid: databricks:libraries-api
    name: Databricks Libraries API
    tags:
      - Clusters
      - Dependencies
      - Libraries
    humanURL: https://docs.databricks.com/api/workspace/libraries
    properties:
      - url: https://docs.databricks.com/api/workspace/libraries
        type: Documentation
    description: The Databricks Libraries API allows you to install, uninstall, and list libraries on clusters. It provides programmatic management of Python, Java, Scala, and R library dependencies for cluster workloads, enabling automated environment configuration.
  - aid: databricks:global-init-scripts-api
    name: Databricks Global Init Scripts API
    tags:
      - Administration
      - Compute
      - Configuration
    humanURL: https://docs.databricks.com/api/workspace/globalinitscripts
    properties:
      - url: https://docs.databricks.com/api/workspace/globalinitscripts
        type: Documentation
    description: The Databricks Global Init Scripts API enables workspace administrators to manage global initialization scripts that run on every cluster in the workspace. It provides programmatic access to create, update, delete, list, and reorder init scripts for consistent cluster configuration.
  - aid: databricks:command-execution-api
    name: Databricks Command Execution API
    tags:
      - Commands
      - Compute
      - Execution
    humanURL: https://docs.databricks.com/api/workspace/commandexecution
    properties:
      - url: https://docs.databricks.com/api/workspace/commandexecution
        type: Documentation
    description: The Databricks Command Execution API allows you to execute Python, Scala, SQL, or R commands on running Databricks clusters. It provides programmatic access to create execution contexts, run commands, check status, and retrieve results, enabling remote interactive cluster usage.
  - aid: databricks:statement-execution-api
    name: Databricks Statement Execution API
    tags:
      - Queries
      - SQL
      - Warehouses
    humanURL: https://docs.databricks.com/api/workspace/statementexecution
    properties:
      - url: https://docs.databricks.com/api/workspace/statementexecution
        type: Documentation
    description: The Databricks Statement Execution API allows you to execute SQL statements on Databricks SQL warehouses and retrieve results. It provides a synchronous and asynchronous interface for running SQL queries, checking execution status, fetching result data, and canceling statements.
  - aid: databricks:queries-api
    name: Databricks Queries API
    tags:
      - Analytics
      - Queries
      - SQL
    humanURL: https://docs.databricks.com/api/workspace/queries
    properties:
      - url: https://docs.databricks.com/api/workspace/queries
        type: Documentation
    description: The Databricks Queries API allows you to create, update, delete, list, and run saved SQL queries in Databricks SQL. It provides programmatic management of SQL query objects, enabling automation of analytical workflows and query lifecycle management.
  - aid: databricks:alerts-api
    name: Databricks Alerts API
    tags:
      - Alerts
      - Monitoring
      - SQL
    humanURL: https://docs.databricks.com/api/workspace/alerts
    properties:
      - url: https://docs.databricks.com/api/workspace/alerts
        type: Documentation
    description: The Databricks Alerts API allows you to create, update, delete, and list alerts in Databricks SQL. Alerts automate query execution, evaluate custom conditions, and deliver notifications when those conditions are met, enabling proactive monitoring of business data.
  - aid: databricks:schemas-api
    name: Databricks Schemas API
    tags:
      - Data Governance
      - Schemas
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/schemas
    properties:
      - url: https://docs.databricks.com/api/workspace/schemas
        type: Documentation
    description: The Databricks Schemas API is part of Unity Catalog and allows you to create, update, list, and delete schemas. Schemas, also known as databases, reside within catalogs and contain tables, views, volumes, functions, and models, providing the second level of the three-level namespace for data organization.
  - aid: databricks:tables-api
    name: Databricks Tables API
    tags:
      - Data Governance
      - Tables
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/tables
    properties:
      - url: https://docs.databricks.com/api/workspace/tables
        type: Documentation
    description: The Databricks Tables API is part of Unity Catalog and allows you to create, update, list, and delete tables. Tables reside within schemas and represent structured data assets, supporting managed and external table types with full governance and access control through Unity Catalog.
  - aid: databricks:volumes-api
    name: Databricks Volumes API
    tags:
      - Storage
      - Unity Catalog
      - Volumes
    humanURL: https://docs.databricks.com/api/workspace/volumes
    properties:
      - url: https://docs.databricks.com/api/workspace/volumes
        type: Documentation
    description: The Databricks Volumes API is part of Unity Catalog and allows you to create, update, list, and delete volumes. Volumes provide a governed location for storing and accessing non-tabular data files such as images, documents, and other unstructured data within the Unity Catalog namespace.
  - aid: databricks:functions-api
    name: Databricks Functions API
    tags:
      - Functions
      - SQL
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/functions
    properties:
      - url: https://docs.databricks.com/api/workspace/functions
        type: Documentation
    description: The Databricks Functions API is part of Unity Catalog and allows you to create, list, and delete user-defined functions. Functions reside within schemas and can be used in SQL queries and notebooks, with full governance and access control managed through Unity Catalog.
  - aid: databricks:grants-api
    name: Databricks Grants API
    tags:
      - Access Control
      - Security
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/grants
    properties:
      - url: https://docs.databricks.com/api/workspace/grants
        type: Documentation
    description: The Databricks Grants API is part of Unity Catalog and allows you to get, update, and manage permissions on Unity Catalog securable objects. It provides programmatic control over access to catalogs, schemas, tables, volumes, and other data assets, enabling fine-grained data governance.
  - aid: databricks:external-locations-api
    name: Databricks External Locations API
    tags:
      - Cloud Storage
      - Storage
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/externallocations
    properties:
      - url: https://docs.databricks.com/api/workspace/externallocations
        type: Documentation
    description: The Databricks External Locations API is part of Unity Catalog and allows you to create, update, list, and delete external locations. External locations combine a cloud storage path with a storage credential, enabling governed access to data stored in external cloud storage systems.
  - aid: databricks:storage-credentials-api
    name: Databricks Storage Credentials API
    tags:
      - Cloud Storage
      - Security
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/storagecredentials
    properties:
      - url: https://docs.databricks.com/api/workspace/storagecredentials
        type: Documentation
    description: The Databricks Storage Credentials API is part of Unity Catalog and allows you to create, update, list, and delete storage credentials. Storage credentials contain long-term cloud credentials that provide access to cloud storage, and are referenced when creating external locations for governing data access.
  - aid: databricks:metastores-api
    name: Databricks Metastores API
    tags:
      - Data Governance
      - Metadata
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/metastores
    properties:
      - url: https://docs.databricks.com/api/workspace/metastores
        type: Documentation
    description: The Databricks Metastores API is part of Unity Catalog and allows you to create, update, list, and delete metastores. A metastore is the top-level container of objects in Unity Catalog, providing centralized metadata management, access control, and data governance across workspaces.
  - aid: databricks:connections-api
    name: Databricks Connections API
    tags:
      - Connections
      - External Data
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/connections
    properties:
      - url: https://docs.databricks.com/api/workspace/connections
        type: Documentation
    description: The Databricks Connections API is part of Unity Catalog and allows you to create, update, list, and delete connections to external data sources. Connections enable federated queries across external databases and data systems, extending Unity Catalog governance to data outside the lakehouse.
  - aid: databricks:registered-models-api
    name: Databricks Registered Models API
    tags:
      - Machine Learning
      - MLflow
      - Model Registry
    humanURL: https://docs.databricks.com/api/workspace/registeredmodels
    properties:
      - url: https://docs.databricks.com/api/workspace/registeredmodels
        type: Documentation
    description: The Databricks Registered Models API allows you to create, update, list, and delete registered models in the Unity Catalog model registry. It provides centralized model lifecycle management with versioning, aliasing, and governance capabilities for machine learning models.
  - aid: databricks:experiments-api
    name: Databricks Experiments API
    tags:
      - Experiments
      - Machine Learning
      - MLflow
    humanURL: https://docs.databricks.com/api/workspace/experiments
    properties:
      - url: https://docs.databricks.com/api/workspace/experiments
        type: Documentation
    description: The Databricks Experiments API allows you to create, update, list, and manage MLflow experiments. Experiments are the primary unit of organization in MLflow, grouping runs that track parameters, metrics, and artifacts for machine learning model development and comparison.
  - aid: databricks:online-tables-api
    name: Databricks Online Tables API
    tags:
      - Feature Serving
      - Real-Time
      - Tables
    humanURL: https://docs.databricks.com/api/workspace/onlinetables
    properties:
      - url: https://docs.databricks.com/api/workspace/onlinetables
        type: Documentation
    description: The Databricks Online Tables API allows you to create, get, and delete online tables. Online tables are materialized copies of Delta tables optimized for low-latency lookups, enabling real-time feature serving and online inference workloads for machine learning applications.
  - aid: databricks:quality-monitors-api
    name: Databricks Quality Monitors API
    tags:
      - Data Quality
      - Monitoring
      - Observability
    humanURL: https://docs.databricks.com/api/workspace/qualitymonitors
    properties:
      - url: https://docs.databricks.com/api/workspace/qualitymonitors
        type: Documentation
    description: The Databricks Quality Monitors API allows you to create, update, get, and delete data quality monitors for tables. Quality monitors enable automated data profiling and anomaly detection, providing continuous monitoring of data quality metrics and statistical properties.
  - aid: databricks:vector-search-endpoints-api
    name: Databricks Vector Search Endpoints API
    tags:
      - AI
      - Compute
      - Vector Search
    humanURL: https://docs.databricks.com/api/workspace/vectorsearchendpoints
    properties:
      - url: https://docs.databricks.com/api/workspace/vectorsearchendpoints
        type: Documentation
    description: The Databricks Vector Search Endpoints API allows you to create, list, get, and delete vector search endpoints. Vector search endpoints are compute resources that host vector search indexes, enabling similarity search queries for retrieval-augmented generation and other AI applications.
  - aid: databricks:shares-api
    name: Databricks Shares API
    tags:
      - Collaboration
      - Data Sharing
      - Delta Sharing
    humanURL: https://docs.databricks.com/api/workspace/shares
    properties:
      - url: https://docs.databricks.com/api/workspace/shares
        type: Documentation
    description: The Databricks Shares API is part of Delta Sharing and allows you to create, update, list, and delete shares. A share is a read-only logical collection of tables and table partitions that a data provider wants to share with one or more recipients for secure cross-organization data sharing.
  - aid: databricks:recipients-api
    name: Databricks Recipients API
    tags:
      - Access Control
      - Data Sharing
      - Delta Sharing
    humanURL: https://docs.databricks.com/api/workspace/recipients
    properties:
      - url: https://docs.databricks.com/api/workspace/recipients
        type: Documentation
    description: The Databricks Recipients API is part of Delta Sharing and allows you to create, update, list, and delete recipients. A recipient is an entity that receives shared data from a provider, and can be either a Databricks workspace or an open-protocol recipient using bearer tokens.
  - aid: databricks:providers-api
    name: Databricks Providers API
    tags:
      - Data Sharing
      - Delta Sharing
      - Marketplace
    humanURL: https://docs.databricks.com/api/workspace/providers
    properties:
      - url: https://docs.databricks.com/api/workspace/providers
        type: Documentation
    description: The Databricks Providers API is part of Delta Sharing and allows you to create, update, list, and delete data providers. Providers represent organizations that share data through Delta Sharing, enabling secure and governed cross-organization data exchange.
  - aid: databricks:clean-rooms-api
    name: Databricks Clean Rooms API
    tags:
      - Clean Rooms
      - Collaboration
      - Privacy
    humanURL: https://docs.databricks.com/api/workspace/cleanrooms
    properties:
      - url: https://docs.databricks.com/api/workspace/cleanrooms
        type: Documentation
    description: The Databricks Clean Rooms API allows you to create, update, list, and delete clean rooms. Clean rooms use Delta Sharing and serverless compute to provide a secure and privacy-protecting environment where multiple parties can collaborate on sensitive enterprise data without exposing raw data.
  - aid: databricks:notification-destinations-api
    name: Databricks Notification Destinations API
    tags:
      - Alerts
      - Integration
      - Notifications
    humanURL: https://docs.databricks.com/api/workspace/notificationdestinations
    properties:
      - url: https://docs.databricks.com/api/workspace/notificationdestinations
        type: Documentation
    description: The Databricks Notification Destinations API allows you to create, update, list, and delete notification destinations for a workspace. Notification destinations define where alerts and notifications are sent, supporting integrations with email, Slack, PagerDuty, webhooks, and other channels.
  - aid: databricks:apps-api
    name: Databricks Apps API
    tags:
      - Applications
      - Deployment
      - Development
    humanURL: https://docs.databricks.com/api/workspace/apps
    properties:
      - url: https://docs.databricks.com/api/workspace/apps
        type: Documentation
    description: The Databricks Apps API allows you to create, deploy, manage, and delete Databricks Apps. Apps run directly on a Databricks workspace, integrating with workspace data and services to build custom data applications, dashboards, and tools with built-in authentication and authorization.
  - aid: databricks:lakeview-api
    name: Databricks Lakeview API
    tags:
      - Analytics
      - Dashboards
      - Visualization
    humanURL: https://docs.databricks.com/api/workspace/lakeview
    properties:
      - url: https://docs.databricks.com/api/workspace/lakeview
        type: Documentation
    description: The Databricks Lakeview API allows you to create, update, get, list, and delete AI/BI dashboards. Lakeview dashboards provide a modern visualization experience built on top of Databricks SQL, enabling interactive data exploration and business intelligence reporting.
  - aid: databricks:files-api
    name: Databricks Files API
    tags:
      - Files
      - Storage
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/files
    properties:
      - url: https://docs.databricks.com/api/workspace/files
        type: Documentation
    description: The Databricks Files API provides a standard HTTP interface for reading, writing, listing, and deleting files and directories in Unity Catalog volumes and other workspace storage locations. It supports direct file access by URI, enabling seamless file management for data and ML workloads.
  - aid: databricks:tokens-api
    name: Databricks Tokens API
    tags:
      - Authentication
      - Security
      - Tokens
    humanURL: https://docs.databricks.com/api/workspace/tokens
    properties:
      - url: https://docs.databricks.com/api/workspace/tokens
        type: Documentation
    description: The Databricks Tokens API allows you to create, list, and revoke personal access tokens. Personal access tokens are used to authenticate with the Databricks REST API and integrations, providing an alternative to OAuth for programmatic access.
  - aid: databricks:ip-access-lists-api
    name: Databricks IP Access Lists API
    tags:
      - Access Control
      - Networking
      - Security
    humanURL: https://docs.databricks.com/api/workspace/ipaccesslists
    properties:
      - url: https://docs.databricks.com/api/workspace/ipaccesslists
        type: Documentation
    description: The Databricks IP Access Lists API allows administrators to configure IP allow lists and block lists for a workspace. It provides programmatic management of network security rules to restrict access to the workspace based on IP addresses or CIDR ranges.
  - aid: databricks:current-user-api
    name: Databricks Current User API
    tags:
      - Authentication
      - Identity
      - Users
    humanURL: https://docs.databricks.com/api/workspace/currentuser
    properties:
      - url: https://docs.databricks.com/api/workspace/currentuser
        type: Documentation
    description: The Databricks Current User API allows you to retrieve information about the currently authenticated user or service principal. It returns identity details including username, display name, and group memberships for the caller making the API request.
  - aid: databricks:groups-api
    name: Databricks Groups API
    tags:
      - Access Control
      - Groups
      - Identity
    humanURL: https://docs.databricks.com/api/workspace/groups
    properties:
      - url: https://docs.databricks.com/api/workspace/groups
        type: Documentation
    description: The Databricks Groups API allows you to create, update, list, and delete groups in a workspace. Groups simplify identity management by enabling administrators to assign access permissions to collections of users and service principals rather than managing them individually.
  - aid: databricks:service-principals-api
    name: Databricks Service Principals API
    tags:
      - Automation
      - Identity
      - Service Principals
    humanURL: https://docs.databricks.com/api/workspace/serviceprincipals
    properties:
      - url: https://docs.databricks.com/api/workspace/serviceprincipals
        type: Documentation
    description: The Databricks Service Principals API allows you to create, update, list, and delete service principals in a workspace. Service principals are identities for automated tools, jobs, scripts, apps, and CI/CD platforms, enabling secure non-interactive authentication with Databricks resources.
  - aid: databricks:users-api
    name: Databricks Users API
    tags:
      - Administration
      - Identity
      - Users
    humanURL: https://docs.databricks.com/api/workspace/users
    properties:
      - url: https://docs.databricks.com/api/workspace/users
        type: Documentation
    description: The Databricks Users API allows you to create, update, list, and delete users in a workspace. It provides programmatic management of user identities and their workspace access, supporting SCIM protocol for identity provider integration and automated user provisioning.
  - aid: databricks:dashboards-api
    name: Databricks Dashboards API
    tags:
      - Dashboards
      - SQL
      - Visualization
    humanURL: https://docs.databricks.com/api/workspace/dashboards
    properties:
      - url: https://docs.databricks.com/api/workspace/dashboards
        type: Documentation
    description: The Databricks Dashboards API allows you to create, update, list, and delete legacy SQL dashboards. Dashboards provide visual representations of query results, enabling business intelligence reporting and data visualization directly within Databricks SQL.
  - aid: databricks:model-registry-api
    name: Databricks Model Registry API
    tags:
      - Machine Learning
      - MLflow
      - Model Registry
    humanURL: https://docs.databricks.com/api/workspace/modelregistry
    properties:
      - url: https://docs.databricks.com/api/workspace/modelregistry
        type: Documentation
    description: The Databricks Model Registry API provides the workspace model registry for managing the full lifecycle of ML models. It enables creating registered models, managing model versions, transitioning stages, and setting permissions for collaborative model governance and deployment.
  - aid: databricks:workspace-bindings-api
    name: Databricks Workspace Bindings API
    tags:
      - Governance
      - Unity Catalog
      - Workspace
    humanURL: https://docs.databricks.com/api/workspace/workspacebindings
    properties:
      - url: https://docs.databricks.com/api/workspace/workspacebindings
        type: Documentation
    description: The Databricks Workspace Bindings API allows you to manage the binding of Unity Catalog securables to specific workspaces. It enables configuring whether catalogs and other objects are available across all workspaces or isolated to specific ones, supporting multi-workspace governance.
  - aid: databricks:system-schemas-api
    name: Databricks System Schemas API
    tags:
      - Monitoring
      - System Tables
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/systemschemas
    properties:
      - url: https://docs.databricks.com/api/workspace/systemschemas
        type: Documentation
    description: The Databricks System Schemas API allows you to enable, disable, and list system schemas within a metastore. System schemas contain system tables that provide operational data about your Databricks account, including audit logs, billing usage, lineage, and access history.
  - aid: databricks:table-constraints-api
    name: Databricks Table Constraints API
    tags:
      - Data Quality
      - Tables
      - Unity Catalog
    humanURL: https://docs.databricks.com/api/workspace/tableconstraints
    properties:
      - url: https://docs.databricks.com/api/workspace/tableconstraints
        type: Documentation
    description: The Databricks Table Constraints API allows you to create and delete primary key and foreign key constraints on Unity Catalog tables. Table constraints define relationships between tables, supporting data integrity and enabling query optimization across the lakehouse.
name: Databricks
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
type: Index
image: https://www.databricks.com/en-website-assets/static/f9f2b15ae456c41f7d2e5b303c8c6c6e/databricks-logo.svg
access: 3rd-Party
created: '2025-01-14'
modified: '2026-05-04'
position: Consumer
description: Collection of Databricks REST APIs for managing workspaces, clusters, jobs, and data operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Databricks
    email: support@databricks.com
    url: https://www.databricks.com/
specificationVersion: '0.19'
common:
  - url: https://docs.databricks.com/dev-tools/auth.html
    type: Authentication
  - url: https://docs.databricks.com/getting-started/index.html
    type: Getting Started
  - url: https://docs.databricks.com/dev-tools/sdks.html
    type: SDKs
  - url: https://status.databricks.com/
    type: StatusPage
  - url: https://help.databricks.com/
    type: Support
  - url: https://docs.databricks.com/api/workspace/introduction
    type: API Reference
  - url: https://docs.databricks.com/aws/en/reference/api
    type: Documentation
  - url: https://www.databricks.com/product/pricing
    type: Pricing
  - url: https://www.databricks.com/try-databricks
    type: Sign Up
  - url: https://www.databricks.com/legal/privacynotice
    type: PrivacyPolicy
  - url: https://www.databricks.com/legal/terms-of-use
    type: TermsOfService
  - url: https://www.databricks.com/trust
    type: Security
  - url: https://docs.databricks.com/aws/en/resources/limits
    type: RateLimits
  - url: https://docs.databricks.com/aws/en/release-notes/
    type: ChangeLog
  - url: https://www.databricks.com/blog
    type: Blog
  - url: https://community.databricks.com/
    type: Support
    title: Community Forum
  - url: https://github.com/databricks
    type: GitHubOrganization
  - url: https://github.com/databricks/databricks-sdk-py
    type: SDK
    title: Python SDK
  - url: https://github.com/databricks/databricks-sdk-go
    type: SDK
    title: Go SDK
  - url: https://github.com/databricks/cli
    type: CLI
  - url: https://docs.databricks.com/aws/en/dev-tools/cli
    type: Documentation
  - url: https://twitter.com/databricks
    type: X
  - url: https://www.linkedin.com/company/databricks
    type: LinkedIn
  - url: https://login.databricks.com/
    type: Login
  - url: https://www.databricks.com/company/contact
    type: Contact
  - url: https://www.databricks.com/learn/training/home
    type: Training
  - url: https://customer-academy.databricks.com/learn
    type: Academy
  - url: https://github.com/databricks/databricks-sdk-java
    type: SDK
    title: Java SDK
  - url: https://github.com/databricks/databricks-sql-python
    type: SDK
    title: Python SQL SDK
  - url: https://github.com/databricks/terraform-provider-databricks
    type: SDK
    title: Terraform Provider
  - url: https://docs.databricks.com/aws/en/reference/mlflow-api
    type: APIReference
    title: MLflow API Reference
  - url: https://www.databricks.com/trust/security-features
    type: Security
  - url: https://docs.databricks.com/aws/en/dev-tools/auth
    type: Authentication
  - url: https://api-docs.databricks.com/
    type: APIReference
  - url: openapi/databricks-openapi.yml
    type: OpenAPI
  - url: json-schema/databricks-cluster-schema.json
    type: JSONSchema
  - url: json-schema/databricks-job-schema.json
    type: JSONSchema
  - url: json-ld/databricks-context.jsonld
    type: JSONLD
  - url: rules/databricks-spectral-rules.yml
    type: SpectralRules
  - url: capabilities/data-engineering.yaml
    type: NaftikoCapability
  - type: Features
    data:
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
    sources:
      - https://www.databricks.com/product/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Data Engineering
        description: Build and orchestrate ETL pipelines with Delta Live Tables and multi-task workflows.
      - name: Data Warehousing
        description: Run analytical SQL queries on lakehouse data with serverless SQL warehouses.
      - name: Machine Learning
        description: Train, track, and deploy ML models with MLflow experiment tracking and model registry.
      - name: Real-Time Analytics
        description: Process streaming data with structured streaming and serve results through online tables.
      - name: Data Governance
        description: Govern data assets across the organization with Unity Catalog metadata management.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Native integration with Apache Spark for distributed data processing at scale.
      - name: Delta Lake
        description: Built on Delta Lake open format for ACID transactions and time travel on data lakes.
      - name: MLflow
        description: Open-source platform for managing the complete machine learning lifecycle.
      - name: Terraform
        description: Infrastructure-as-code provider for automating Databricks workspace provisioning.
      - name: dbt
        description: Integration with dbt for SQL-based data transformation workflows.
---
