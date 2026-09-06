---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 708
  human_in_the_loop: 4
  name: Cognite Agentic Access
  operation_count: 980
  slug: cognite-agentic-access
  summary_line: 980 operations · 708 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: The Cognite Data Fusion (CDF) REST API provides programmatic access to industrial data including assets, time series, events, files, sequences, 3D models, data modeling spaces and instances, entity ma
  name: Cognite Data Fusion API
  slug: cognite-data-fusion-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The 3D Asset Mapping API from Cognite — 5 operation(s) for 3d asset mapping.
  name: Cognite 3D Asset Mapping API
  slug: cognite-3d-asset-mapping-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The 3D Files API from Cognite — 2 operation(s) for 3d files.
  name: Cognite 3D Files API
  slug: cognite-3d-files-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The 3D Jobs API from Cognite — 6 operation(s) for 3d jobs.
  name: Cognite 3D Jobs API
  slug: cognite-3d-jobs-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The 3D Model Revisions API from Cognite — 11 operation(s) for 3d model revisions.
  name: Cognite 3D Model Revisions API
  slug: cognite-3d-model-revisions-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The 3D Models API from Cognite — 4 operation(s) for 3d models.
  name: Cognite 3D Models API
  slug: cognite-3d-models-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Annotations reflect contextual information in base CDF resource types, such as Files and Time series, that are not present on the object itself. The benefits of the annotations concept are threefold: '
  name: Cognite Annotations API
  slug: cognite-annotations-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The assets resource type stores digital representations of objects or groups of objects from the physical world. Assets are organized in hierarchies. For example, a water pump asset can be a part of a
  name: Cognite Assets API
  slug: cognite-assets-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Connections API from Cognite — 3 operation(s) for connections.
  name: Cognite Connections API
  slug: cognite-connections-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Containers API from Cognite — 9 operation(s) for containers.
  name: Cognite Containers API
  slug: cognite-containers-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Data models API from Cognite — 3 operation(s) for data models.
  name: Cognite Data models API
  slug: cognite-data-models-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A data point subscription is a way to listen to changes to time series data points, in ingestion order. A single subscription can listen to many time series, and a time series can be part of many subs
  name: Cognite Data point subscriptions API
  slug: cognite-data-point-subscriptions-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Data products are governed, ready-for-consumption data assets derived from data domains, following data mesh principles. **Key characteristics:** - **Clear ownership**: Defined data product owners wit'
  name: Cognite Data products API
  slug: cognite-data-products-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Data sets let you document and track data lineage, ensure data integrity, and allow 3rd parties to write their insights securely back to a Cognite Data Fusion (CDF) project. Data sets group and track '
  name: Cognite Data sets API
  slug: cognite-data-sets-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'A hosted extractor writes to a **destination**. The destination contains credentials for CDF, and additional information about where the data should land, such as data set ID. Multiple jobs can share '
  name: Cognite Destinations API
  slug: cognite-destinations-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Diagrams API from Cognite — 6 operation(s) for diagrams.
  name: Cognite Diagrams API
  slug: cognite-diagrams-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Document AI API from Cognite — 2 operation(s) for document ai.
  name: Cognite Document AI API
  slug: cognite-document-ai-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Document parsing API from Cognite — 1 operation(s) for document parsing.
  name: Cognite Document parsing API
  slug: cognite-document-parsing-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The document preview service is a utility API that can render most document types as an image or PDF. This can be very helpful if you want to display a preview of a file in a frontend, or for other ta
  name: Cognite Document preview API
  slug: cognite-document-preview-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A document is a file that has been indexed by the document search engine. Every time a file is uploaded, updated or deleted in the Files API, it will also be scheduled for processing by the document s
  name: Cognite Documents API
  slug: cognite-documents-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Engineering diagrams API from Cognite — 4 operation(s) for engineering diagrams.
  name: Cognite Engineering diagrams API
  slug: cognite-engineering-diagrams-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Entities API from Cognite — 4 operation(s) for entities.
  name: Cognite Entities API
  slug: cognite-entities-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'The entity matching contextualization endpoints lets you match CDF resources. For example, you can match time series to assets. The model uses similarity between string-fields from the source and the '
  name: Cognite Entity matching API
  slug: cognite-entity-matching-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Events objects store complex information about multiple assets over a time period. Typical types of events that would be stored in this service might include Alarms, Process Data, and Logs.\ For the s
  name: Cognite Events API
  slug: cognite-events-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Extraction Pipeline objects represent the applications and software that are deployed to ingest operational data into CDF. An extraction pipeline can consist of a number of different software componen
  name: Cognite Extraction Pipelines API
  slug: cognite-extraction-pipelines-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Extraction Pipelines Configs are configuration file revisions tied to an extraction pipeline. Users can create new configuration revisions, and extractors can fetch the latest, making it easy to deplo
  name: Cognite Extraction Pipelines Config API
  slug: cognite-extraction-pipelines-config-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Extraction Pipelines Runs are CDF objects to store statuses related to an extraction pipeline. The supported statuses are: success, failure and seen. The statuses are related to two different types of'
  name: Cognite Extraction Pipelines Runs API
  slug: cognite-extraction-pipelines-runs-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Extractors are tools used to move data from various source systems to CDF. The extractors API is used to manage extractor releases, give access to downloads, and contextualize which source systems eac
  name: Cognite Extractors API
  slug: cognite-extractors-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'A file stores a sequence of bytes connected to one or more assets. For example, a file can contain a piping and instrumentation diagram (P&IDs) showing how multiple assets are connected. Each file is '
  name: Cognite Files API
  slug: cognite-files-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Function calls let you execute functions asynchronously with a timeout of 15 minutes.
  name: Cognite Function calls API
  slug: cognite-function-calls-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Function schedules allow you to run functions with a specific input at intervals defined by a cron expression. These function calls will be asynchronous and show up in the function call list. Visit ht
  name: Cognite Function schedules API
  slug: cognite-function-schedules-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Functions enables Python code to be hosted and executed in the cloud, on demand or by using a schedule. Execution, status and logs are available through the API. A function is uploaded to the Files AP
  name: Cognite Functions API
  slug: cognite-functions-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Geometries API from Cognite — 4 operation(s) for geometries.
  name: Cognite Geometries API
  slug: cognite-geometries-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Geospatial API allows to model a problem domain when data has a geometric or geographic nature. The geospatial data is organized in feature types that are homogeneous collections of features (geos
  name: Cognite Geospatial API
  slug: cognite-geospatial-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Groups are used to give principals the capabilities to access CDF resources. One principal can be a member in multiple groups and one group can have multiple members. Note that having more than 20 gro
  name: Cognite Groups API
  slug: cognite-groups-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Instances API from Cognite — 9 operation(s) for instances.
  name: Cognite Instances API
  slug: cognite-instances-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Each integration represents an application running on-premises.
  name: Cognite Integrations API
  slug: cognite-integrations-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A hosted extractor **job** represents the running extractor. Jobs produce logs and metrics that give the state of the job. For details on available states and metrics see documentation [here](https://
  name: Cognite Jobs API
  slug: cognite-jobs-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Labels API from Cognite — 4 operation(s) for labels.
  name: Cognite Labels API
  slug: cognite-labels-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Libraries API from Cognite — 6 operation(s) for libraries.
  name: Cognite Libraries API
  slug: cognite-libraries-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A **mapping** is a custom transformation, translating the source format to a format that can be ingested into CDF. Mappings are written in the Cognite transformation language. For more details see doc
  name: Cognite Mappings API
  slug: cognite-mappings-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: An **organization** is used to group CDF projects and facilitate their management. An organization holds users, projects, and perhaps other organizations. The organization ID is what the users enter w
  name: Cognite Organizations API
  slug: cognite-organizations-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Parsing API from Cognite — 3 operation(s) for parsing.
  name: Cognite Parsing API
  slug: cognite-parsing-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: View and create foreign **tables** for a given **user**
  name: Cognite Postgres Gateway Tables API
  slug: cognite-postgres-gateway-tables-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A postgres gateway **user** (also a typical postgres user) owns the foreign tables (built in or custom). The created postgres user only has access to use foreign tables and cannot directly create tabl
  name: Cognite Postgres Gateway Users API
  slug: cognite-postgres-gateway-users-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A **preview** is a temporary job that runs until it times out, fails, or receives a single message, then stores the result. This is useful for development, as it allows you to easily inspect the outpu
  name: Cognite Previews API
  slug: cognite-previews-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: '**Principal** is an umbrella term for **user accounts** and **service accounts**. Both entities can be uniquely identified, authenticated, and authorized in CDF. Principals are unique within an organi'
  name: Cognite Principals API
  slug: cognite-principals-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Projects are used to isolate data in CDF from each other. All objects in CDF belong to a single project, and objects in different projects are generally isolated from each other.
  name: Cognite Projects API
  slug: cognite-projects-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Query lets the users preview the result of their queries.
  name: Cognite Query API
  slug: cognite-query-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Manage data in the raw NoSQL database. Each project will have a variable number of raw databases, each of which will have a variable number of tables, each of which will have a variable number of key-
  name: Cognite Raw API
  slug: cognite-raw-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Records are mutable or immutable data objects (depending on the stream template) stored in a stream. Records are created by ingesting data into a stream. Records are shaped similarly to instances in t
  name: Cognite Records API
  slug: cognite-records-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The relationships resource type represents connections between resource objects in CDF. Relationships allow you to organize assets in other structures in addition to the standard hierarchical asset st
  name: Cognite Relationships API
  slug: cognite-relationships-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: An SAP **endpoint** represents a configuration to an SAP S/4HANA OData endpoint (and its related OData entity) the API will send the writeback requests. It defines which SAP Instance destination and w
  name: Cognite SAP Endpoints API
  slug: cognite-sap-endpoints-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: An SAP **instance** represents a configuration to an external SAP S/4HANA destination system. The **instance** resource contains all the information this API service needs to connect to an SAP S/4HANA
  name: Cognite SAP Instances API
  slug: cognite-sap-instances-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Schema provides the expected schema for CDF resources.
  name: Cognite Schema API
  slug: cognite-schema-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'A **mapping** uses field and value mapping(s) to perform an in-flight transformation from source CDF entities to SAP S/4HANA entities. Mappings are written in the Cognite transformation language. For '
  name: Cognite Schema Mappings API
  slug: cognite-schema-mappings-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Manage security categories for a specific project. Security categories can be used to restrict access to a resource. Applying a security category to a resource means that only principals (users or ser
  name: Cognite Security categories API
  slug: cognite-security-categories-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'A sequence stores a table with up to 400 columns indexed by row number. There can be at most 400 numeric columns and 200 string columns. Each of the columns has a pre-defined type: a string, integer, '
  name: Cognite Sequences API
  slug: cognite-sequences-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Sessions are used to maintain access to CDF resources for an extended period of time. The methods available to extend a sessions lifetime are client credentials and token exchange. Sessions depend on '
  name: Cognite Sessions API
  slug: cognite-sessions-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A signal is a notification that something has occurred in a CDF process. Users and systems may listen to signals by creating a sink and attaching subscriptions with a filter that matches the signals t
  name: Cognite Signals API
  slug: cognite-signals-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Every time a simulation routine executes, a simulation run object is created. This object ensures that each execution of a routine is documented and traceable. Each run has an associated simulation da
  name: Cognite Simulation Runs API
  slug: cognite-simulation-runs-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'The simulator integration resource represents a simulator connector in Cognite Data Fusion (CDF). It provides information about the configured connectors for a given simulator, including their status '
  name: Cognite Simulator Integrations API
  slug: cognite-simulator-integrations-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Simulator logs track what happens during simulation runs, model parsing, and generic connector logic. They provide valuable information for monitoring, debugging, and auditing. Simulator logs capture '
  name: Cognite Simulator Logs API
  slug: cognite-simulator-logs-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The simulator model resource represents an asset modeled in a simulator. This asset could range from a pump or well to a complete processing facility or refinery. The simulator model is the root of it
  name: Cognite Simulator Models API
  slug: cognite-simulator-models-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'The simulator routine resource defines instructions on interacting with a simulator model. A simulator routine includes: - Inputs (values set into the simulator model) - Commands (actions to be perfor'
  name: Cognite Simulator Routines API
  slug: cognite-simulator-routines-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The simulator resource contains the definitions necessary for Cognite Data Fusion (CDF) to interact with a given simulator. It serves as a central contract that allows APIs, UIs, and integrations (con
  name: Cognite Simulators API
  slug: cognite-simulators-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A hosted extractor **source** represents an external source system on the internet. The **source** resource in CDF contains all the information the extractor needs to connect to the external source sy
  name: Cognite Sources API
  slug: cognite-sources-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Spaces API from Cognite — 3 operation(s) for spaces.
  name: Cognite Spaces API
  slug: cognite-spaces-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Statistics API from Cognite — 3 operation(s) for statistics.
  name: Cognite Statistics API
  slug: cognite-statistics-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Use the streams and records API to build high-volume extensions to industrial knowledge graphs that are built with [Data Modeling](https://docs.cognite.com/cdf/dm). The streams API lets you manage the
  name: Cognite Streams API
  slug: cognite-streams-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The SVG Data API from Cognite — 2 operation(s) for svg data.
  name: Cognite SVG Data API
  slug: cognite-svg-data-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Symbols API from Cognite — 4 operation(s) for symbols.
  name: Cognite Symbols API
  slug: cognite-symbols-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Synthetic Time Series (STS) is a way to combine various input time series, constants and operators, to create completely new time series. For example can we use the expression `24 * TS{externalId='pro
  name: Cognite Synthetic Time Series API
  slug: cognite-synthetic-time-series-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Tasks API from Cognite — 1 operation(s) for tasks.
  name: Cognite Tasks API
  slug: cognite-tasks-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A time series consists of a sequence of data points connected to a single asset. For example, a water pump asset can have a temperature time series that records a data point in units of Â°C every seco
  name: Cognite Time series API
  slug: cognite-time-series-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Access tokens issued by an IdP (Azure AD, Google, etc.) are used to access CDF resources.
  name: Cognite Token API
  slug: cognite-token-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Transformation jobs let you list jobs and their metrics. A maximum of 1000 jobs per transformation are retained, provided they are not older than 90 days.
  name: Cognite Transformation Jobs API
  slug: cognite-transformation-jobs-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Transformation notifications let users know when a job fails if subscribed.
  name: Cognite Transformation Notifications API
  slug: cognite-transformation-notifications-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Transformation schedules allow you to run transformations with a specific input at intervals defined by a cron expression. These transformation jobs will be asynchronous and show up in the transformat
  name: Cognite Transformation Schedules API
  slug: cognite-transformation-schedules-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Transformations enable users to use Spark SQL queries to transform data from the CDF staging area, RAW, into the CDF data model. ### Concurrency limits The number of concurrent (parallel) jobs are gov'
  name: Cognite Transformations API
  slug: cognite-transformations-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Unit system is a collection of default units for different quantities. This API provides a list of supported unit systems and their associated quantities and respective unit.
  name: Cognite Unit Systems API
  slug: cognite-unit-systems-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Units Catalog API provides a standardized list of units that can be used in Cognite Data Fusion. The content this API serves is based on the [CDF Units Catalog](https://github.com/cognitedata/units-ca
  name: Cognite Units API
  slug: cognite-units-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: User profiles is an authoritative source of core user profile information (email, name, job title, etc.) for principals based on data from the identity provider configured for the CDF project. User pr
  name: Cognite User profiles API
  slug: cognite-user-profiles-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Views API from Cognite — 3 operation(s) for views.
  name: Cognite Views API
  slug: cognite-views-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Vision API is deprecated. See [Deprecated and retired features](https://docs.cognite.com/cdf/deprecated) for details and timelines. The Vision contextualization endpoints enable extraction of informat
  name: Cognite Vision API
  slug: cognite-vision-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Workflow executions API from Cognite — 5 operation(s) for workflow executions.
  name: Cognite Workflow executions API
  slug: cognite-workflow-executions-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: Triggers allow you to automate the execution of your data workflows based on specific conditions, such as scheduled times (defined by cron expressions).
  name: Cognite Workflow triggers API
  slug: cognite-workflow-triggers-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: The Workflow versions API from Cognite — 4 operation(s) for workflow versions.
  name: Cognite Workflow versions API
  slug: cognite-workflow-versions-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: 'Define and orchestrate data workflows consisting of CDF Transformations, Cognite Functions, and other processes. This service enables you to build data pipelines and business solutions leveraging the '
  name: Cognite Workflows API
  slug: cognite-workflows-api
- baseURL: https://api.cognitedata.com
  baseurl_source: declared
  description: A writeback **request** to the SAP S/4HANA destination. The request body contains the target SAP endpoint destination, and the payload to send.
  name: Cognite Writeback Requests API
  slug: cognite-writeback-requests-api
artifact_total: 195
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cognite 3D Asset Mapping API
  slug: open-cognite-3d-asset-mapping-api
- collection_type: open
  name: Cognite 3D Asset Mapping 3D Files API
  slug: open-cognite-3d-files-api
- collection_type: open
  name: Cognite 3D Asset Mapping 3D Jobs API
  slug: open-cognite-3d-jobs-api
- collection_type: open
  name: Cognite 3D Asset Mapping 3D Model Revisions API
  slug: open-cognite-3d-model-revisions-api
- collection_type: open
  name: Cognite 3D Asset Mapping 3D Models API
  slug: open-cognite-3d-models-api
- collection_type: open
  name: Cognite 3D Asset Mapping Annotations API
  slug: open-cognite-annotations-api
- collection_type: open
  name: Cognite 3D Asset Mapping Assets API
  slug: open-cognite-assets-api
- collection_type: open
  name: Cognite 3D Asset Mapping Connections API
  slug: open-cognite-connections-api
- collection_type: open
  name: Cognite 3D Asset Mapping Containers API
  slug: open-cognite-containers-api
- collection_type: open
  name: Cognite 3D Asset Mapping Data models API
  slug: open-cognite-data-models-api
- collection_type: open
  name: Cognite 3D Asset Mapping Data point subscriptions API
  slug: open-cognite-data-point-subscriptions-api
- collection_type: open
  name: Cognite 3D Asset Mapping Data products API
  slug: open-cognite-data-products-api
- collection_type: open
  name: Cognite 3D Asset Mapping Data sets API
  slug: open-cognite-data-sets-api
- collection_type: open
  name: Cognite 3D Asset Mapping Destinations API
  slug: open-cognite-destinations-api
- collection_type: open
  name: Cognite 3D Asset Mapping Diagrams API
  slug: open-cognite-diagrams-api
- collection_type: open
  name: Cognite 3D Asset Mapping Document AI API
  slug: open-cognite-document-ai-api
- collection_type: open
  name: Cognite 3D Asset Mapping Document parsing API
  slug: open-cognite-document-parsing-api
- collection_type: open
  name: Cognite 3D Asset Mapping Documents API
  slug: open-cognite-documents-api
- collection_type: open
  name: Cognite 3D Asset Mapping Engineering diagrams API
  slug: open-cognite-engineering-diagrams-api
- collection_type: open
  name: Cognite 3D Asset Mapping Entities API
  slug: open-cognite-entities-api
- collection_type: open
  name: Cognite 3D Asset Mapping Entity matching API
  slug: open-cognite-entity-matching-api
- collection_type: open
  name: Cognite 3D Asset Mapping Events API
  slug: open-cognite-events-api
- collection_type: open
  name: Cognite 3D Asset Mapping Extraction Pipelines API
  slug: open-cognite-extraction-pipelines-api
- collection_type: open
  name: Cognite 3D Asset Mapping Extraction Pipelines Config API
  slug: open-cognite-extraction-pipelines-config-api
- collection_type: open
  name: Cognite 3D Asset Mapping Extraction Pipelines Runs API
  slug: open-cognite-extraction-pipelines-runs-api
- collection_type: open
  name: Cognite 3D Asset Mapping Extractors API
  slug: open-cognite-extractors-api
- collection_type: open
  name: Cognite 3D Asset Mapping Files API
  slug: open-cognite-files-api
- collection_type: open
  name: Cognite 3D Asset Mapping Function calls API
  slug: open-cognite-function-calls-api
- collection_type: open
  name: Cognite 3D Asset Mapping Function schedules API
  slug: open-cognite-function-schedules-api
- collection_type: open
  name: Cognite 3D Asset Mapping Functions API
  slug: open-cognite-functions-api
- collection_type: open
  name: Cognite 3D Asset Mapping Geometries API
  slug: open-cognite-geometries-api
- collection_type: open
  name: Cognite 3D Asset Mapping Geospatial API
  slug: open-cognite-geospatial-api
- collection_type: open
  name: Cognite 3D Asset Mapping Groups API
  slug: open-cognite-groups-api
- collection_type: open
  name: Cognite 3D Asset Mapping Instances API
  slug: open-cognite-instances-api
- collection_type: open
  name: Cognite 3D Asset Mapping Integrations API
  slug: open-cognite-integrations-api
- collection_type: open
  name: Cognite 3D Asset Mapping Jobs API
  slug: open-cognite-jobs-api
- collection_type: open
  name: Cognite 3D Asset Mapping Labels API
  slug: open-cognite-labels-api
- collection_type: open
  name: Cognite 3D Asset Mapping Libraries API
  slug: open-cognite-libraries-api
- collection_type: open
  name: Cognite 3D Asset Mapping Mappings API
  slug: open-cognite-mappings-api
- collection_type: open
  name: Cognite 3D Asset Mapping Organizations API
  slug: open-cognite-organizations-api
- collection_type: open
  name: Cognite 3D Asset Mapping Parsing API
  slug: open-cognite-parsing-api
- collection_type: open
  name: Cognite 3D Asset Mapping Postgres Gateway Tables API
  slug: open-cognite-postgres-gateway-tables-api
- collection_type: open
  name: Cognite 3D Asset Mapping Postgres Gateway Users API
  slug: open-cognite-postgres-gateway-users-api
- collection_type: open
  name: Cognite 3D Asset Mapping Principals API
  slug: open-cognite-principals-api
- collection_type: open
  name: Cognite 3D Asset Mapping Projects API
  slug: open-cognite-projects-api
- collection_type: open
  name: Cognite 3D Asset Mapping Query API
  slug: open-cognite-query-api
- collection_type: open
  name: Cognite 3D Asset Mapping Raw API
  slug: open-cognite-raw-api
- collection_type: open
  name: Cognite 3D Asset Mapping Records API
  slug: open-cognite-records-api
- collection_type: open
  name: Cognite 3D Asset Mapping Relationships API
  slug: open-cognite-relationships-api
- collection_type: open
  name: Cognite 3D Asset Mapping SAP Endpoints API
  slug: open-cognite-sap-endpoints-api
- collection_type: open
  name: Cognite 3D Asset Mapping SAP Instances API
  slug: open-cognite-sap-instances-api
- collection_type: open
  name: Cognite 3D Asset Mapping Schema API
  slug: open-cognite-schema-api
- collection_type: open
  name: Cognite 3D Asset Mapping Schema Mappings API
  slug: open-cognite-schema-mappings-api
- collection_type: open
  name: Cognite 3D Asset Mapping Security categories API
  slug: open-cognite-security-categories-api
- collection_type: open
  name: Cognite 3D Asset Mapping Sequences API
  slug: open-cognite-sequences-api
- collection_type: open
  name: Cognite 3D Asset Mapping Sessions API
  slug: open-cognite-sessions-api
- collection_type: open
  name: Cognite 3D Asset Mapping Signals API
  slug: open-cognite-signals-api
- collection_type: open
  name: Cognite 3D Asset Mapping Simulation Runs API
  slug: open-cognite-simulation-runs-api
- collection_type: open
  name: Cognite 3D Asset Mapping Simulator Integrations API
  slug: open-cognite-simulator-integrations-api
- collection_type: open
  name: Cognite 3D Asset Mapping Simulator Logs API
  slug: open-cognite-simulator-logs-api
- collection_type: open
  name: Cognite 3D Asset Mapping Simulator Models API
  slug: open-cognite-simulator-models-api
- collection_type: open
  name: Cognite 3D Asset Mapping Simulator Routines API
  slug: open-cognite-simulator-routines-api
- collection_type: open
  name: Cognite 3D Asset Mapping Simulators API
  slug: open-cognite-simulators-api
- collection_type: open
  name: Cognite 3D Asset Mapping Sources API
  slug: open-cognite-sources-api
- collection_type: open
  name: Cognite 3D Asset Mapping Spaces API
  slug: open-cognite-spaces-api
- collection_type: open
  name: Cognite 3D Asset Mapping Statistics API
  slug: open-cognite-statistics-api
- collection_type: open
  name: Cognite 3D Asset Mapping Streams API
  slug: open-cognite-streams-api
- collection_type: open
  name: Cognite 3D Asset Mapping SVG Data API
  slug: open-cognite-svg-data-api
- collection_type: open
  name: Cognite 3D Asset Mapping Symbols API
  slug: open-cognite-symbols-api
- collection_type: open
  name: Cognite 3D Asset Mapping Synthetic Time Series API
  slug: open-cognite-synthetic-time-series-api
- collection_type: open
  name: Cognite 3D Asset Mapping Tasks API
  slug: open-cognite-tasks-api
- collection_type: open
  name: Cognite 3D Asset Mapping Time series API
  slug: open-cognite-time-series-api
- collection_type: open
  name: Cognite 3D Asset Mapping Token API
  slug: open-cognite-token-api
- collection_type: open
  name: Cognite 3D Asset Mapping Transformation Jobs API
  slug: open-cognite-transformation-jobs-api
- collection_type: open
  name: Cognite 3D Asset Mapping Transformation Notifications API
  slug: open-cognite-transformation-notifications-api
- collection_type: open
  name: Cognite 3D Asset Mapping Transformation Schedules API
  slug: open-cognite-transformation-schedules-api
- collection_type: open
  name: Cognite 3D Asset Mapping Transformations API
  slug: open-cognite-transformations-api
- collection_type: open
  name: Cognite 3D Asset Mapping Unit Systems API
  slug: open-cognite-unit-systems-api
- collection_type: open
  name: Cognite 3D Asset Mapping Units API
  slug: open-cognite-units-api
- collection_type: open
  name: Cognite 3D Asset Mapping User profiles API
  slug: open-cognite-user-profiles-api
- collection_type: open
  name: Cognite 3D Asset Mapping Views API
  slug: open-cognite-views-api
- collection_type: open
  name: Cognite 3D Asset Mapping Vision API
  slug: open-cognite-vision-api
- collection_type: open
  name: Cognite 3D Asset Mapping Workflow executions API
  slug: open-cognite-workflow-executions-api
- collection_type: open
  name: Cognite 3D Asset Mapping Workflow triggers API
  slug: open-cognite-workflow-triggers-api
- collection_type: open
  name: Cognite 3D Asset Mapping Workflow versions API
  slug: open-cognite-workflow-versions-api
- collection_type: open
  name: Cognite 3D Asset Mapping Workflows API
  slug: open-cognite-workflows-api
- collection_type: open
  name: Cognite 3D Asset Mapping Writeback Requests API
  slug: open-cognite-writeback-requests-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cognite-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cognite-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cognite-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cognite-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cognite.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cognite.com/
- group: start
  title: ''
  type: Portal
  url: https://api-docs.cognite.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cognite.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cognitedata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognite
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CogniteData
- group: build
  title: ''
  type: SDKs
  url: https://developer.cognite.com/sdks/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cognite.com/en/pricing
- group: company
  title: ''
  type: About
  url: https://www.cognite.com/en/about
created: '2026-06-05'
description: Cognite is an industrial AI and data platform provider whose core product, Cognite Data Fusion (CDF), contextualizes and integrates data from OT, IT, and ET systems across oil and gas, energy, manufacturing, and mining industries. CDF exposes a comprehensive REST API covering assets, time series, events, files, 3D models, data modeling, entity matching, transformations, functions, and workflows, with SDKs available for Python, JavaScript, Java, .NET, and Rust.
examples:
- key_count: 2
  name: Cognite Assets List Example
  slug: cognite-assets-list-example
- key_count: 2
  name: Cognite Events Create Example
  slug: cognite-events-create-example
- key_count: 2
  name: Cognite Timeseries Datapoints Example
  slug: cognite-timeseries-datapoints-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognite.png
json_schemas:
- name: Asset
  property_count: 15
  slug: cognite-asset
- name: Event
  property_count: 13
  slug: cognite-event
- name: TimeSeries
  property_count: 16
  slug: cognite-timeseries
json_structures:
- name: Cognite Asset Structure
  property_count: 0
  slug: cognite-asset-structure
- name: Cognite Timeseries Structure
  property_count: 0
  slug: cognite-timeseries-structure
jsonld:
- class_count: 11
  name: Cognite Context
  property_count: 36
  slug: cognite-context
layout: provider
modified: '2026-06-05'
name: Cognite
nav: Providers
network: true
overview: 'Cognite publishes 89 APIs on the [APIs.io](https://apis.io/) network, including 3D Asset Mapping API, 3D Files API, 3D Jobs API, and 86 more. Tagged areas include Industrial IoT, Manufacturing, Industrial Data, Digital Twin, and Asset Management.


  The Cognite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cognite''s developer surface includes authentication, documentation, developer portal, engineering blog, YouTube channel, pricing, and 11 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 5
  extends: []
  name: Cognite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cognite-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Cognite API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 5
  slug: cognite-rules
scopes:
- name: Cognite Scopes
  scope_count: 3
  slug: cognite-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 66.3
    developer_ergonomics: 40.5
    discoverability: 63.0
    governance: 13.6
    operational_transparency: 2.6
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 89
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognite/refs/heads/main/screenshots/cognite-2026-06-20T174714.png
security:
- kind: authentication
  name: Cognite Authentication
  slug: cognite-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Cognite Domain Security
  slug: cognite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognite Vulnerability Disclosure
  slug: cognite-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cognite Trust Center
  slug: cognite-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR, CSA STAR
slug: cognite
tags:
- Industrial IoT
- Manufacturing
- Industrial Data
- Digital Twin
- Asset Management
- Time Series
- Industrial AI
website: https://www.cognite.com
---
