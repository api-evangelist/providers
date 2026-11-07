---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 71
  human_in_the_loop: 7
  name: Microsoft Azure Data Factory Agentic Access
  operation_count: 104
  slug: microsoft-azure-data-factory-agentic-access
  summary_line: 104 operations · 71 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Activityruns operations on the Microsoft.DataFactory resource provider (1 operation): ActivityRuns_QueryByPipelineRun.'
  name: Azure Data Factory Activityruns API
  phrasing_intents:
  - id: ActivityRuns_QueryByPipelineRun
    intent: Query activity runs within a pipeline run
    question: Which activities ran inside a particular Data Factory pipeline run, and did any fail?
  phrasing_ops: 1
  slug: microsoft-azure-data-factory-activityruns-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Credentials operations on the Microsoft.DataFactory resource provider (4 operations): CredentialOperations_ListByFactory, CredentialOperations_Get, CredentialOperations_CreateOrUpdate, CredentialOpera'
  name: Azure Data Factory Credentials API
  phrasing_intents:
  - id: CredentialOperations_ListByFactory
    intent: List credentials in a factory
    question: Which credentials are stored in my Azure Data Factory?
  - id: CredentialOperations_Get
    intent: Get a credential
    question: How do I read the definition of one credential in a data factory?
  - id: CredentialOperations_CreateOrUpdate
    intent: Create or update a credential
    question: How do I add a new credential, like a managed identity, to a data factory?
  - id: CredentialOperations_Delete
    intent: Delete a credential
    question: Can I remove a credential that my factory no longer uses?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-credentials-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Datasets operations on the Microsoft.DataFactory resource provider (4 operations): Datasets_ListByFactory, Datasets_Get, Datasets_CreateOrUpdate, Datasets_Delete.'
  name: Azure Data Factory Datasets API
  phrasing_intents:
  - id: Datasets_ListByFactory
    intent: List datasets in a factory
    question: Which datasets are defined in my data factory?
  - id: Datasets_Get
    intent: Get a dataset
    question: How do I read the definition of one dataset?
  - id: Datasets_CreateOrUpdate
    intent: Create or update a dataset
    question: How do I define a new dataset pointing at my source or sink data?
  - id: Datasets_Delete
    intent: Delete a dataset
    question: Can I delete a dataset from a data factory?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-datasets-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Factories operations on the Microsoft.DataFactory resource provider (9 operations): Factories_List, Factories_ConfigureFactoryRepo, Factories_ListByResourceGroup, Factories_Get, Factories_CreateOrUpda'
  name: Azure Data Factory Factories API
  phrasing_intents:
  - id: Factories_List
    intent: List every data factory in my subscription
    question: Which data factories exist across my whole Azure subscription?
  - id: Factories_ConfigureFactoryRepo
    intent: Set a factory's git repository configuration
    question: How do I connect my data factory to a git repo for source control?
  - id: Factories_ListByResourceGroup
    intent: List data factories in a resource group
    question: Which data factories live in my current resource group?
  - id: Factories_Get
    intent: Get a data factory
    question: How do I look up the details of one data factory, like its identity and repo settings?
  - id: Factories_CreateOrUpdate
    intent: Create or update a data factory
    question: How do I create a new Azure Data Factory instance through the API?
  - id: Factories_Update
    intent: Patch a factory's tags or identity
    question: Can I change just the tags on a data factory without resending its full definition?
  - id: Factories_Delete
    intent: Delete a data factory
    question: Can I delete an entire data factory, including everything in it?
  - id: Factories_GetDataPlaneAccess
    intent: Get a data plane access token for a factory
    question: How do I get a time-limited data plane access token for my data factory?
  phrasing_ops: 13
  slug: microsoft-azure-data-factory-factories-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Operations operations on the Microsoft.DataFactory resource provider (1 operation): Operations_List.'
  name: Azure Data Factory Operations API
  phrasing_intents:
  - id: Operations_List
    intent: List available Data Factory API operations
    question: What operations does the Azure Data Factory resource provider expose?
  phrasing_ops: 1
  slug: microsoft-azure-data-factory-operations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Pipelineruns operations on the Microsoft.DataFactory resource provider (3 operations): PipelineRuns_Get, PipelineRuns_Cancel, PipelineRuns_QueryByFactory.'
  name: Azure Data Factory Pipelineruns API
  phrasing_intents:
  - id: PipelineRuns_Get
    intent: Get a pipeline run by its run ID
    question: How do I check whether a specific pipeline run succeeded or failed?
  - id: PipelineRuns_Cancel
    intent: Cancel a pipeline run
    question: How do I cancel a pipeline run that is stuck or taking too long?
  - id: PipelineRuns_QueryByFactory
    intent: Search pipeline runs in a factory
    question: Which pipeline runs happened in my factory during a given time window?
  phrasing_ops: 3
  slug: microsoft-azure-data-factory-pipelineruns-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Pipelines operations on the Microsoft.DataFactory resource provider (5 operations): Pipelines_ListByFactory, Pipelines_Get, Pipelines_CreateOrUpdate, Pipelines_Delete, Pipelines_CreateRun.'
  name: Azure Data Factory Pipelines API
  phrasing_intents:
  - id: Pipelines_ListByFactory
    intent: List pipelines in a factory
    question: Which pipelines are defined in my data factory?
  - id: Pipelines_Get
    intent: Get a pipeline definition
    question: How do I read the activities and parameters of one pipeline?
  - id: Pipelines_CreateOrUpdate
    intent: Create or update a pipeline
    question: How do I create a new pipeline in a data factory through the API?
  - id: Pipelines_Delete
    intent: Delete a pipeline
    question: Can I delete a pipeline from my data factory?
  - id: Pipelines_CreateRun
    intent: Run a pipeline
    question: How do I trigger a pipeline run on demand?
  phrasing_ops: 5
  slug: microsoft-azure-data-factory-pipelines-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Trigger operations on the Microsoft.DataFactory resource provider (1 operation): Triggers_Get.'
  name: Azure Data Factory Trigger API
  phrasing_intents:
  - id: Triggers_Get
    intent: Get a trigger
    question: How do I read the schedule and settings of one trigger?
  phrasing_ops: 1
  slug: microsoft-azure-data-factory-trigger-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Triggerruns operations on the Microsoft.DataFactory resource provider (3 operations): TriggerRuns_QueryByFactory, TriggerRuns_Cancel, TriggerRuns_Rerun.'
  name: Azure Data Factory Triggerruns API
  phrasing_intents:
  - id: TriggerRuns_QueryByFactory
    intent: Search trigger runs in a factory
    question: Which triggers fired in my factory during a time window?
  - id: TriggerRuns_Cancel
    intent: Cancel a single trigger run
    question: How do I cancel one in-progress trigger run?
  - id: TriggerRuns_Rerun
    intent: Rerun a single trigger run
    question: How do I rerun a trigger run that failed?
  phrasing_ops: 3
  slug: microsoft-azure-data-factory-triggerruns-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Triggers operations on the Microsoft.DataFactory resource provider (9 operations): Triggers_QueryByFactory, Triggers_ListByFactory, Triggers_CreateOrUpdate, Triggers_Delete, Triggers_GetEventSubscript'
  name: Azure Data Factory Triggers API
  phrasing_intents:
  - id: Triggers_QueryByFactory
    intent: Search triggers in a factory
    question: Can I find the child triggers that belong to a parent trigger?
  - id: Triggers_ListByFactory
    intent: List triggers in a factory
    question: What triggers are defined in my data factory?
  - id: Triggers_CreateOrUpdate
    intent: Create or update a trigger
    question: How do I create a schedule trigger that runs my pipeline every night?
  - id: Triggers_Delete
    intent: Delete a trigger
    question: Can I delete a trigger I no longer need?
  - id: Triggers_GetEventSubscriptionStatus
    intent: Check a trigger's event subscription status
    question: Is my event trigger subscribed to events yet, or still provisioning?
  - id: Triggers_Start
    intent: Start a trigger
    question: How do I activate a trigger so it starts firing pipelines?
  - id: Triggers_Stop
    intent: Stop a trigger
    question: How do I pause a trigger so it stops firing pipelines?
  - id: Triggers_SubscribeToEvents
    intent: Subscribe an event trigger to events
    question: How do I subscribe an event trigger to its storage events?
  phrasing_ops: 9
  slug: microsoft-azure-data-factory-triggers-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The changeDataCapture API from Azure Data Factory — 5 operation(s) for changedatacapture.
  name: Azure Data Factory Change Data Capture API
  phrasing_intents:
  - id: ChangeDataCapture_ListByFactory
    intent: List change data capture resources in a factory
    question: Which change data capture resources are set up in my data factory?
  - id: ChangeDataCapture_Get
    intent: Get a change data capture resource
    question: How do I look up the definition of one change data capture resource?
  - id: ChangeDataCapture_CreateOrUpdate
    intent: Create or update a change data capture resource
    question: How do I define a new change data capture resource in a data factory?
  - id: ChangeDataCapture_Delete
    intent: Delete a change data capture resource
    question: Can I permanently remove a change data capture resource from a factory?
  - id: ChangeDataCapture_Start
    intent: Start a change data capture resource
    question: How do I start capturing changes with a CDC resource I already defined?
  - id: ChangeDataCapture_Status
    intent: Check whether a change data capture is running
    question: Is my change data capture resource currently running or stopped?
  - id: ChangeDataCapture_Stop
    intent: Stop a change data capture resource
    question: How do I pause a change data capture resource that is currently running?
  phrasing_ops: 7
  slug: microsoft-azure-data-factory-changedatacapture-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The dataFlowDebugSession API from Azure Data Factory — 5 operation(s) for dataflowdebugsession.
  name: Azure Data Factory Data Flow Debug Session API
  phrasing_intents:
  - id: DataFlowDebugSession_AddDataFlow
    intent: Add a data flow to a debug session
    question: How do I load a data flow into a running debug session so I can test it?
  - id: DataFlowDebugSession_Create
    intent: Start a data flow debug session
    question: How do I spin up a debug cluster to test data flows interactively?
  - id: DataFlowDebugSession_Delete
    intent: End a data flow debug session
    question: How do I shut down a data flow debug session when I'm done testing?
  - id: DataFlowDebugSession_ExecuteCommand
    intent: Run a command in a data flow debug session
    question: Can I preview data or run a debug command against a data flow in a live session?
  - id: DataFlowDebugSession_QueryByFactory
    intent: List active data flow debug sessions
    question: Which data flow debug sessions are active in my factory right now?
  phrasing_ops: 5
  slug: microsoft-azure-data-factory-dataflowdebugsession-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The dataFlows API from Azure Data Factory — 2 operation(s) for dataflows.
  name: Azure Data Factory Data Flows API
  phrasing_intents:
  - id: DataFlows_ListByFactory
    intent: List data flows in a factory
    question: Which data flows exist in my data factory?
  - id: DataFlows_Get
    intent: Get a data flow
    question: How do I read the definition of a single data flow?
  - id: DataFlows_CreateOrUpdate
    intent: Create or update a data flow
    question: How do I create a new data flow in a factory through the API?
  - id: DataFlows_Delete
    intent: Delete a data flow
    question: Can I delete a data flow I no longer need?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-dataflows-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The exposureControl API from Azure Data Factory — 3 operation(s) for exposurecontrol.
  name: Azure Data Factory Exposure Control API
  phrasing_intents:
  - id: ExposureControl_GetFeatureValue
    intent: Check a feature flag for an Azure region
    question: Is a particular Data Factory exposure control feature enabled in an Azure region?
  - id: ExposureControl_GetFeatureValueByFactory
    intent: Check a feature flag for one factory
    question: Is a specific exposure control feature turned on for my data factory?
  - id: ExposureControl_QueryFeatureValuesByFactory
    intent: Check several feature flags for a factory
    question: Can I check many exposure control features for a factory in one request?
  phrasing_ops: 3
  slug: microsoft-azure-data-factory-exposurecontrol-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The globalParameters API from Azure Data Factory — 2 operation(s) for globalparameters.
  name: Azure Data Factory Global Parameters API
  phrasing_intents:
  - id: GlobalParameters_ListByFactory
    intent: List global parameters in a factory
    question: Which global parameters are defined in my data factory?
  - id: GlobalParameters_Get
    intent: Get a global parameter
    question: How do I read the value of one global parameter?
  - id: GlobalParameters_CreateOrUpdate
    intent: Create or update a global parameter
    question: How do I add a new global parameter to a data factory?
  - id: GlobalParameters_Delete
    intent: Delete a global parameter
    question: Can I delete a global parameter from a factory?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-globalparameters-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The integrationRuntimeDisableInteractiveQuery API from Azure Data Factory — 1 operation(s) for integrationruntimedisableinteractivequery.
  name: Azure Data Factory Integration Runtime Disable Interactive Query API
  phrasing_intents:
  - id: IntegrationRuntime_DisableInteractiveQuery
    intent: Disable interactive authoring on a runtime
    question: How do I turn off interactive authoring on a Managed Virtual Network integration runtime?
  phrasing_ops: 1
  slug: microsoft-azure-data-factory-integrationruntimedisableinteractivequery-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The integrationRuntimeEnableInteractiveQuery API from Azure Data Factory — 1 operation(s) for integrationruntimeenableinteractivequery.
  name: Azure Data Factory Integration Runtime Enable Interactive Query API
  phrasing_intents:
  - id: IntegrationRuntime_EnableInteractiveQuery
    intent: Enable interactive authoring on a runtime
    question: How do I turn on interactive authoring for a Managed Virtual Network integration runtime?
  phrasing_ops: 1
  slug: microsoft-azure-data-factory-integrationruntimeenableinteractivequery-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The integrationRuntimeNodes API from Azure Data Factory — 2 operation(s) for integrationruntimenodes.
  name: Azure Data Factory Integration Runtime Nodes API
  phrasing_intents:
  - id: IntegrationRuntimeNodes_Get
    intent: Get a self-hosted runtime node
    question: How do I check the details of one node in my self-hosted integration runtime?
  - id: IntegrationRuntimeNodes_Update
    intent: Set concurrent job limit on a runtime node
    question: Can I change how many concurrent jobs a self-hosted runtime node will run?
  - id: IntegrationRuntimeNodes_Delete
    intent: Remove a node from a self-hosted runtime
    question: Can I remove a decommissioned machine from my self-hosted integration runtime?
  - id: IntegrationRuntimeNodes_GetIpAddress
    intent: Get the IP address of a runtime node
    question: What IP address does a self-hosted integration runtime node use?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-integrationruntimenodes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The integrationRuntimeObjectMetadata API from Azure Data Factory — 2 operation(s) for integrationruntimeobjectmetadata.
  name: Azure Data Factory Integration Runtime Object Metadata API
  phrasing_intents:
  - id: IntegrationRuntimeObjectMetadata_Get
    intent: Browse SSIS object metadata on a runtime
    question: How do I browse the SSIS catalog folders, projects and packages on an Azure-SSIS runtime?
  - id: IntegrationRuntimeObjectMetadata_Refresh
    intent: Refresh SSIS object metadata on a runtime
    question: How do I refresh the cached SSIS object metadata after deploying new packages?
  phrasing_ops: 2
  slug: microsoft-azure-data-factory-integrationruntimeobjectmetadata-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The integrationRuntimes API from Azure Data Factory — 14 operation(s) for integrationruntimes.
  name: Azure Data Factory Integration Runtimes API
  phrasing_intents:
  - id: IntegrationRuntimes_ListByFactory
    intent: List integration runtimes in a factory
    question: Which integration runtimes are set up in my data factory?
  - id: IntegrationRuntimes_Get
    intent: Get an integration runtime definition
    question: How do I read the configuration of one integration runtime?
  - id: IntegrationRuntimes_CreateOrUpdate
    intent: Create or update an integration runtime
    question: How do I create a new self-hosted or Azure integration runtime?
  - id: IntegrationRuntimes_Update
    intent: Change auto-update settings on a runtime
    question: Can I turn auto-update on or off for a self-hosted integration runtime?
  - id: IntegrationRuntimes_Delete
    intent: Delete an integration runtime
    question: Can I delete an integration runtime my pipelines no longer use?
  - id: IntegrationRuntimes_GetConnectionInfo
    intent: Get connection info for encrypting credentials
    question: How do I get the connection info needed to encrypt on-premises data source credentials?
  - id: IntegrationRuntimes_GetStatus
    intent: Get detailed status of an integration runtime
    question: Is my integration runtime online, and what state are its nodes in?
  - id: IntegrationRuntimes_CreateLinkedIntegrationRuntime
    intent: Share a self-hosted runtime with another factory
    question: How do I share my self-hosted integration runtime with a different data factory?
  phrasing_ops: 17
  slug: microsoft-azure-data-factory-integrationruntimes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The linkedServices API from Azure Data Factory — 2 operation(s) for linkedservices.
  name: Azure Data Factory Linked Services API
  phrasing_intents:
  - id: LinkedServices_ListByFactory
    intent: List linked services in a factory
    question: Which connections to data stores and compute are defined in my data factory?
  - id: LinkedServices_Get
    intent: Get a linked service
    question: How do I read the connection settings of one linked service?
  - id: LinkedServices_CreateOrUpdate
    intent: Create or update a linked service
    question: How do I add a connection to a new database or storage account in my factory?
  - id: LinkedServices_Delete
    intent: Delete a linked service
    question: Can I delete a linked service connection I no longer need?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-linkedservices-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The managedPrivateEndpoints API from Azure Data Factory — 2 operation(s) for managedprivateendpoints.
  name: Azure Data Factory Managed Private Endpoints API
  phrasing_intents:
  - id: ManagedPrivateEndpoints_ListByFactory
    intent: List managed private endpoints in a virtual network
    question: Which managed private endpoints exist in my factory's managed virtual network?
  - id: ManagedPrivateEndpoints_Get
    intent: Get a managed private endpoint
    question: How do I check the details and approval state of one managed private endpoint?
  - id: ManagedPrivateEndpoints_CreateOrUpdate
    intent: Create or update a managed private endpoint
    question: How do I create a managed private endpoint so my factory reaches a data store privately?
  - id: ManagedPrivateEndpoints_Delete
    intent: Delete a managed private endpoint
    question: Can I delete a managed private endpoint my factory no longer uses?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-managedprivateendpoints-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The managedVirtualNetworks API from Azure Data Factory — 2 operation(s) for managedvirtualnetworks.
  name: Azure Data Factory Managed Virtual Networks API
  phrasing_intents:
  - id: ManagedVirtualNetworks_ListByFactory
    intent: List managed virtual networks in a factory
    question: Which managed virtual networks does my data factory have?
  - id: ManagedVirtualNetworks_Get
    intent: Get a managed virtual network
    question: How do I look up the details of one managed virtual network?
  - id: ManagedVirtualNetworks_CreateOrUpdate
    intent: Create or update a managed virtual network
    question: How do I create a managed virtual network for my data factory?
  phrasing_ops: 3
  slug: microsoft-azure-data-factory-managedvirtualnetworks-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The privateEndPointConnections API from Azure Data Factory — 2 operation(s) for privateendpointconnections.
  name: Azure Data Factory Private End Point Connections API
  phrasing_intents:
  - id: privateEndPointConnections_ListByFactory
    intent: List private endpoint connections to a factory
    question: Which private endpoint connections have been requested to my data factory?
  - id: PrivateEndpointConnection_Get
    intent: Get a private endpoint connection
    question: How do I check the status of one private endpoint connection to my factory?
  - id: PrivateEndpointConnection_CreateOrUpdate
    intent: Approve or reject a private endpoint connection
    question: How do I approve a pending private endpoint connection to my data factory?
  - id: PrivateEndpointConnection_Delete
    intent: Delete a private endpoint connection
    question: Can I delete a private endpoint connection to my factory?
  phrasing_ops: 4
  slug: microsoft-azure-data-factory-privateendpointconnections-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The privateLinkResources API from Azure Data Factory — 1 operation(s) for privatelinkresources.
  name: Azure Data Factory Private Link Resources API
  phrasing_intents:
  - id: privateLinkResources_Get
    intent: List private link resources for a factory
    question: Which private link resources and group IDs does my data factory support?
  phrasing_ops: 1
  slug: microsoft-azure-data-factory-privatelinkresources-api
artifact_total: 220
collections:
- collection_type: open
  name: Azure Data Factory REST Factories API
  slug: open-microsoft-azure-data-factory-factories-api
- collection_type: open
  name: Azure Data Factory REST Factories Operations API
  slug: open-microsoft-azure-data-factory-operations-api
- collection_type: open
  name: Azure Data Factory REST API
  slug: open-microsoft-azure-data-factory
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/rules/microsoft-azure-data-factory-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-data-factory-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/json-ld/microsoft-azure-data-factory-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-data-factory-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/vocabulary/microsoft-azure-data-factory-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-data-factory-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/hosts/microsoft-azure-data-factory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-data-factory-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/vendors/microsoft-azure-data-factory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-data-factory-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/capabilities/microsoft-azure-data-factory-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-data-factory-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-change-data-capture-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-change-data-capture-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-data-flow-debug-session-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-data-flow-debug-session-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-data-flows-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-data-flows-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-exposure-control-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-exposure-control-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-global-parameters-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-global-parameters-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-integration-runtime-disable-interactive-query-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-integration-runtime-disable-interactive-query-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-integration-runtime-enable-interactive-query-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-integration-runtime-enable-interactive-query-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-integration-runtime-nodes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-integration-runtime-nodes-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-integration-runtime-object-metadata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-integration-runtime-object-metadata-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-integration-runtimes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-integration-runtimes-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-linked-services-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-linked-services-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-managed-private-endpoints-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-managed-private-endpoints-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-managed-virtual-networks-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-managed-virtual-networks-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-private-endpoint-connections-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-private-endpoint-connections-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-data-factory/overlays/microsoft-azure-data-factory-private-link-resources-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-data-factory-private-link-resources-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/data-factory/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/datafactory/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory-rest-api
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://learn.microsoft.com/en-us/answers/tags/194/azure-data-factory
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/analytics/blog/azuredatafactoryblog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: operate
  title: ''
  type: Roadmap
  url: https://azure.microsoft.com/en-us/updates/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/data-factory/data-pipeline/
- group: start
  title: ''
  type: SignUp
  url: https://signup.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-data-factory/changelog/microsoft-azure-data-factory-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-data-factory-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/data-factory/whats-new
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-data-factory/lifecycle/microsoft-azure-data-factory-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-azure-data-factory-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/lifecycle/microsoft-azure-data-factory-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-data-factory-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/authentication/microsoft-azure-data-factory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-data-factory-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/scopes/microsoft-azure-data-factory-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-data-factory-scopes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/conventions/microsoft-azure-data-factory-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-data-factory-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/conventions/microsoft-azure-data-factory-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-data-factory-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/errors/microsoft-azure-data-factory-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-data-factory-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-data-factory/rate-limits/microsoft-azure-data-factory-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-data-factory-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-data-factory/plans/microsoft-azure-data-factory-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-data-factory-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-data-factory/finops/microsoft-azure-data-factory-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-data-factory-finops.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/data-model/microsoft-azure-data-factory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-data-factory-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-data-factory/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-data-factory/packages/microsoft-azure-data-factory-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-data-factory-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-data-factory/packages/microsoft-azure-data-factory-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-data-factory-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-data-factory/cli/microsoft-azure-data-factory-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-data-factory-cli.yml
- group: start
  href: https://artifacts.apis.io/microsoft-azure-data-factory/sandbox/microsoft-azure-data-factory-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-azure-data-factory-sandbox.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-data-factory/conformance/microsoft-azure-data-factory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-data-factory-conformance.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/conformance/microsoft-azure-data-factory-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-data-factory-conformance.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/security/microsoft-azure-data-factory-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-data-factory-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/security/microsoft-azure-data-factory-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-data-factory-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/security/microsoft-azure-data-factory-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-data-factory-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/well-known/microsoft-azure-data-factory-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-data-factory-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-data-factory/well-known/microsoft-azure-data-factory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-data-factory-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-data-factory/security/microsoft-azure-data-factory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-data-factory-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-data-factory/agentic-access/microsoft-azure-data-factory-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-data-factory-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-data-factory/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-data-factory/llms/microsoft-azure-data-factory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-data-factory-llms.txt
created: '2026-05-04'
description: 'Azure Data Factory is Microsoft''s cloud-based data integration service, orchestrating and automating the movement and transformation of data across ETL and ELT workloads that span cloud and on-premises stores. Its public interface is the Microsoft.DataFactory resource provider behind Azure Resource Manager: 104 operations over 75 paths at api-version 2018-06-01, covering factories, pipelines and pipeline runs, datasets, linked services, mapping data flows, triggers, integration runtimes, credentials, global parameters, managed virtual networks and private endpoints, and change data capture resources. Authentication is OAuth 2.0 against Microsoft Entra ID with a single delegated scope, and authorization is Azure RBAC role assignment rather than API scopes. The contract is notable for its type system: 1,199 schema definitions, of which 121 are linked-service connector subtypes and 105 are dataset subtypes, all resolved through OpenAPI discriminators.'
examples:
- key_count: 4
  name: Microsoft Azure Data Factory Activityruns_Querybypipelinerun
  slug: microsoft-azure-data-factory-ActivityRuns_QueryByPipelineRun
- key_count: 4
  name: Microsoft Azure Data Factory Approverejectprivateendpointconnection
  slug: microsoft-azure-data-factory-ApproveRejectPrivateEndpointConnection
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Create
  slug: microsoft-azure-data-factory-ChangeDataCapture_Create
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Delete
  slug: microsoft-azure-data-factory-ChangeDataCapture_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Get
  slug: microsoft-azure-data-factory-ChangeDataCapture_Get
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Listbyfactory
  slug: microsoft-azure-data-factory-ChangeDataCapture_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Start
  slug: microsoft-azure-data-factory-ChangeDataCapture_Start
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Status
  slug: microsoft-azure-data-factory-ChangeDataCapture_Status
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Stop
  slug: microsoft-azure-data-factory-ChangeDataCapture_Stop
- key_count: 4
  name: Microsoft Azure Data Factory Changedatacapture_Update
  slug: microsoft-azure-data-factory-ChangeDataCapture_Update
- key_count: 4
  name: Microsoft Azure Data Factory Credentials_Create
  slug: microsoft-azure-data-factory-Credentials_Create
- key_count: 4
  name: Microsoft Azure Data Factory Credentials_Delete
  slug: microsoft-azure-data-factory-Credentials_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Credentials_Get
  slug: microsoft-azure-data-factory-Credentials_Get
- key_count: 4
  name: Microsoft Azure Data Factory Credentials_Listbyfactory
  slug: microsoft-azure-data-factory-Credentials_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Dataflowdebugsession_Adddataflow
  slug: microsoft-azure-data-factory-DataFlowDebugSession_AddDataFlow
- key_count: 4
  name: Microsoft Azure Data Factory Dataflowdebugsession_Create
  slug: microsoft-azure-data-factory-DataFlowDebugSession_Create
- key_count: 4
  name: Microsoft Azure Data Factory Dataflowdebugsession_Delete
  slug: microsoft-azure-data-factory-DataFlowDebugSession_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Dataflowdebugsession_Executecommand
  slug: microsoft-azure-data-factory-DataFlowDebugSession_ExecuteCommand
- key_count: 4
  name: Microsoft Azure Data Factory Dataflowdebugsession_Querybyfactory
  slug: microsoft-azure-data-factory-DataFlowDebugSession_QueryByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Dataflows_Create
  slug: microsoft-azure-data-factory-DataFlows_Create
- key_count: 4
  name: Microsoft Azure Data Factory Dataflows_Delete
  slug: microsoft-azure-data-factory-DataFlows_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Dataflows_Get
  slug: microsoft-azure-data-factory-DataFlows_Get
- key_count: 4
  name: Microsoft Azure Data Factory Dataflows_Listbyfactory
  slug: microsoft-azure-data-factory-DataFlows_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Dataflows_Update
  slug: microsoft-azure-data-factory-DataFlows_Update
- key_count: 4
  name: Microsoft Azure Data Factory Datasets_Create
  slug: microsoft-azure-data-factory-Datasets_Create
- key_count: 4
  name: Microsoft Azure Data Factory Datasets_Delete
  slug: microsoft-azure-data-factory-Datasets_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Datasets_Get
  slug: microsoft-azure-data-factory-Datasets_Get
- key_count: 4
  name: Microsoft Azure Data Factory Datasets_Listbyfactory
  slug: microsoft-azure-data-factory-Datasets_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Datasets_Update
  slug: microsoft-azure-data-factory-Datasets_Update
- key_count: 4
  name: Microsoft Azure Data Factory Deleteprivateendpointconnection
  slug: microsoft-azure-data-factory-DeletePrivateEndpointConnection
- key_count: 4
  name: Microsoft Azure Data Factory Exposurecontrol_Getfeaturevalue
  slug: microsoft-azure-data-factory-ExposureControl_GetFeatureValue
- key_count: 4
  name: Microsoft Azure Data Factory Exposurecontrol_Getfeaturevaluebyfactory
  slug: microsoft-azure-data-factory-ExposureControl_GetFeatureValueByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Exposurecontrol_Queryfeaturevaluesbyfactory
  slug: microsoft-azure-data-factory-ExposureControl_QueryFeatureValuesByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Configurefactoryrepo
  slug: microsoft-azure-data-factory-Factories_ConfigureFactoryRepo
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Createorupdate
  slug: microsoft-azure-data-factory-Factories_CreateOrUpdate
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Delete
  slug: microsoft-azure-data-factory-Factories_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Get
  slug: microsoft-azure-data-factory-Factories_Get
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Getdataplaneaccess
  slug: microsoft-azure-data-factory-Factories_GetDataPlaneAccess
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Getgithubaccesstoken
  slug: microsoft-azure-data-factory-Factories_GetGitHubAccessToken
- key_count: 4
  name: Microsoft Azure Data Factory Factories_List
  slug: microsoft-azure-data-factory-Factories_List
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Listbyresourcegroup
  slug: microsoft-azure-data-factory-Factories_ListByResourceGroup
- key_count: 4
  name: Microsoft Azure Data Factory Factories_Update
  slug: microsoft-azure-data-factory-Factories_Update
- key_count: 4
  name: Microsoft Azure Data Factory Getprivateendpointconnection
  slug: microsoft-azure-data-factory-GetPrivateEndpointConnection
- key_count: 4
  name: Microsoft Azure Data Factory Getprivatelinkresources
  slug: microsoft-azure-data-factory-GetPrivateLinkResources
- key_count: 4
  name: Microsoft Azure Data Factory Globalparameters_Create
  slug: microsoft-azure-data-factory-GlobalParameters_Create
- key_count: 4
  name: Microsoft Azure Data Factory Globalparameters_Delete
  slug: microsoft-azure-data-factory-GlobalParameters_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Globalparameters_Get
  slug: microsoft-azure-data-factory-GlobalParameters_Get
- key_count: 4
  name: Microsoft Azure Data Factory Globalparameters_Listbyfactory
  slug: microsoft-azure-data-factory-GlobalParameters_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Globalparameters_Update
  slug: microsoft-azure-data-factory-GlobalParameters_Update
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimenodes_Delete
  slug: microsoft-azure-data-factory-IntegrationRuntimeNodes_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimenodes_Get
  slug: microsoft-azure-data-factory-IntegrationRuntimeNodes_Get
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimenodes_Getipaddress
  slug: microsoft-azure-data-factory-IntegrationRuntimeNodes_GetIpAddress
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimenodes_Update
  slug: microsoft-azure-data-factory-IntegrationRuntimeNodes_Update
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimeobjectmetadata_Get
  slug: microsoft-azure-data-factory-IntegrationRuntimeObjectMetadata_Get
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimeobjectmetadata_Refresh
  slug: microsoft-azure-data-factory-IntegrationRuntimeObjectMetadata_Refresh
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Create
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Create
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Createlinkedintegrationruntime
  slug: microsoft-azure-data-factory-IntegrationRuntimes_CreateLinkedIntegrationRuntime
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Delete
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Disableinteractivequery
  slug: microsoft-azure-data-factory-IntegrationRuntimes_DisableInteractiveQuery
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Enableinteractivequery
  slug: microsoft-azure-data-factory-IntegrationRuntimes_EnableInteractiveQuery
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Get
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Get
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Getconnectioninfo
  slug: microsoft-azure-data-factory-IntegrationRuntimes_GetConnectionInfo
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Getmonitoringdata
  slug: microsoft-azure-data-factory-IntegrationRuntimes_GetMonitoringData
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Getstatus
  slug: microsoft-azure-data-factory-IntegrationRuntimes_GetStatus
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Listauthkeys
  slug: microsoft-azure-data-factory-IntegrationRuntimes_ListAuthKeys
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Listbyfactory
  slug: microsoft-azure-data-factory-IntegrationRuntimes_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Listoutboundnetworkdependenciesendpoints
  slug: microsoft-azure-data-factory-IntegrationRuntimes_ListOutboundNetworkDependenciesEndpoints
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Regenerateauthkey
  slug: microsoft-azure-data-factory-IntegrationRuntimes_RegenerateAuthKey
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Removelinks
  slug: microsoft-azure-data-factory-IntegrationRuntimes_RemoveLinks
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Start
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Start
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Stop
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Stop
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Synccredentials
  slug: microsoft-azure-data-factory-IntegrationRuntimes_SyncCredentials
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Update
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Update
- key_count: 4
  name: Microsoft Azure Data Factory Integrationruntimes_Upgrade
  slug: microsoft-azure-data-factory-IntegrationRuntimes_Upgrade
- key_count: 4
  name: Microsoft Azure Data Factory Linkedservices_Create
  slug: microsoft-azure-data-factory-LinkedServices_Create
- key_count: 4
  name: Microsoft Azure Data Factory Linkedservices_Delete
  slug: microsoft-azure-data-factory-LinkedServices_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Linkedservices_Get
  slug: microsoft-azure-data-factory-LinkedServices_Get
- key_count: 4
  name: Microsoft Azure Data Factory Linkedservices_Listbyfactory
  slug: microsoft-azure-data-factory-LinkedServices_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Linkedservices_Update
  slug: microsoft-azure-data-factory-LinkedServices_Update
- key_count: 4
  name: Microsoft Azure Data Factory Managedprivateendpoints_Create
  slug: microsoft-azure-data-factory-ManagedPrivateEndpoints_Create
- key_count: 4
  name: Microsoft Azure Data Factory Managedprivateendpoints_Delete
  slug: microsoft-azure-data-factory-ManagedPrivateEndpoints_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Managedprivateendpoints_Get
  slug: microsoft-azure-data-factory-ManagedPrivateEndpoints_Get
- key_count: 4
  name: Microsoft Azure Data Factory Managedprivateendpoints_Listbyfactory
  slug: microsoft-azure-data-factory-ManagedPrivateEndpoints_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Managedvirtualnetworks_Create
  slug: microsoft-azure-data-factory-ManagedVirtualNetworks_Create
- key_count: 4
  name: Microsoft Azure Data Factory Managedvirtualnetworks_Get
  slug: microsoft-azure-data-factory-ManagedVirtualNetworks_Get
- key_count: 4
  name: Microsoft Azure Data Factory Managedvirtualnetworks_Listbyfactory
  slug: microsoft-azure-data-factory-ManagedVirtualNetworks_ListByFactory
- key_count: 2
  name: Microsoft Azure Data Factory Netezzalinkedservice_Get
  slug: microsoft-azure-data-factory-NetezzaLinkedService_Get
- key_count: 4
  name: Microsoft Azure Data Factory Operations_List
  slug: microsoft-azure-data-factory-Operations_List
- key_count: 4
  name: Microsoft Azure Data Factory Pipelineruns_Cancel
  slug: microsoft-azure-data-factory-PipelineRuns_Cancel
- key_count: 4
  name: Microsoft Azure Data Factory Pipelineruns_Get
  slug: microsoft-azure-data-factory-PipelineRuns_Get
- key_count: 4
  name: Microsoft Azure Data Factory Pipelineruns_Querybyfactory
  slug: microsoft-azure-data-factory-PipelineRuns_QueryByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Pipelines_Create
  slug: microsoft-azure-data-factory-Pipelines_Create
- key_count: 4
  name: Microsoft Azure Data Factory Pipelines_Createrun
  slug: microsoft-azure-data-factory-Pipelines_CreateRun
- key_count: 4
  name: Microsoft Azure Data Factory Pipelines_Delete
  slug: microsoft-azure-data-factory-Pipelines_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Pipelines_Get
  slug: microsoft-azure-data-factory-Pipelines_Get
- key_count: 4
  name: Microsoft Azure Data Factory Pipelines_Listbyfactory
  slug: microsoft-azure-data-factory-Pipelines_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Pipelines_Update
  slug: microsoft-azure-data-factory-Pipelines_Update
- key_count: 4
  name: Microsoft Azure Data Factory Privateendpointconnections_Listbyfactory
  slug: microsoft-azure-data-factory-PrivateEndPointConnections_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Triggerruns_Cancel
  slug: microsoft-azure-data-factory-TriggerRuns_Cancel
- key_count: 4
  name: Microsoft Azure Data Factory Triggerruns_Querybyfactory
  slug: microsoft-azure-data-factory-TriggerRuns_QueryByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Triggerruns_Rerun
  slug: microsoft-azure-data-factory-TriggerRuns_Rerun
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Create
  slug: microsoft-azure-data-factory-Triggers_Create
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Delete
  slug: microsoft-azure-data-factory-Triggers_Delete
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Get
  slug: microsoft-azure-data-factory-Triggers_Get
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Geteventsubscriptionstatus
  slug: microsoft-azure-data-factory-Triggers_GetEventSubscriptionStatus
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Listbyfactory
  slug: microsoft-azure-data-factory-Triggers_ListByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Querybyfactory
  slug: microsoft-azure-data-factory-Triggers_QueryByFactory
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Start
  slug: microsoft-azure-data-factory-Triggers_Start
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Stop
  slug: microsoft-azure-data-factory-Triggers_Stop
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Subscribetoevents
  slug: microsoft-azure-data-factory-Triggers_SubscribeToEvents
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Unsubscribefromevents
  slug: microsoft-azure-data-factory-Triggers_UnsubscribeFromEvents
- key_count: 4
  name: Microsoft Azure Data Factory Triggers_Update
  slug: microsoft-azure-data-factory-Triggers_Update
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Data Factory Finops
  primary_unit: hour
  service_category: ''
  slug: microsoft-azure-data-factory-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-data-factory.png
json_schemas:
- name: AccessPolicyResponse
  property_count: 3
  slug: microsoft-azure-data-factory-access-policy-response
- name: ActivityRunsQueryResponse
  property_count: 2
  slug: microsoft-azure-data-factory-activity-runs-query-response
- name: ChangeDataCaptureListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-change-data-capture-list-response
- name: ChangeDataCaptureResource
  property_count: 2
  slug: microsoft-azure-data-factory-change-data-capture-resource
- name: ChangeDataCaptureStatusResponse
  property_count: 0
  slug: microsoft-azure-data-factory-change-data-capture-status-response
- name: CreateDataFlowDebugSessionRequest
  property_count: 4
  slug: microsoft-azure-data-factory-create-data-flow-debug-session-request
- name: CreateDataFlowDebugSessionResponse
  property_count: 2
  slug: microsoft-azure-data-factory-create-data-flow-debug-session-response
- name: CreateLinkedIntegrationRuntimeRequest
  property_count: 4
  slug: microsoft-azure-data-factory-create-linked-integration-runtime-request
- name: CreateRunResponse
  property_count: 1
  slug: microsoft-azure-data-factory-create-run-response
- name: CredentialListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-credential-list-response
- name: CredentialResource
  property_count: 2
  slug: microsoft-azure-data-factory-credential-resource
- name: DataFlowDebugCommandRequest
  property_count: 3
  slug: microsoft-azure-data-factory-data-flow-debug-command-request
- name: DataFlowDebugCommandResponse
  property_count: 2
  slug: microsoft-azure-data-factory-data-flow-debug-command-response
- name: DataFlowDebugPackage
  property_count: 7
  slug: microsoft-azure-data-factory-data-flow-debug-package
- name: DataFlowListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-data-flow-list-response
- name: DataFlowResource
  property_count: 2
  slug: microsoft-azure-data-factory-data-flow-resource
- name: DatasetListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-dataset-list-response
- name: DatasetResource
  property_count: 2
  slug: microsoft-azure-data-factory-dataset-resource
- name: EnableInteractiveQueryRequest
  property_count: 1
  slug: microsoft-azure-data-factory-enable-interactive-query-request
- name: ExposureControlBatchRequest
  property_count: 1
  slug: microsoft-azure-data-factory-exposure-control-batch-request
- name: ExposureControlBatchResponse
  property_count: 1
  slug: microsoft-azure-data-factory-exposure-control-batch-response
- name: ExposureControlRequest
  property_count: 2
  slug: microsoft-azure-data-factory-exposure-control-request
- name: ExposureControlResponse
  property_count: 2
  slug: microsoft-azure-data-factory-exposure-control-response
- name: Factory
  property_count: 5
  slug: microsoft-azure-data-factory-factory
- name: FactoryUpdateParameters
  property_count: 3
  slug: microsoft-azure-data-factory-factory-update-parameters
- name: GetSsisObjectMetadataRequest
  property_count: 1
  slug: microsoft-azure-data-factory-get-ssis-object-metadata-request
- name: GitHubAccessTokenRequest
  property_count: 4
  slug: microsoft-azure-data-factory-git-hub-access-token-request
- name: GlobalParameterListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-global-parameter-list-response
- name: GlobalParameterResource
  property_count: 2
  slug: microsoft-azure-data-factory-global-parameter-resource
- name: IntegrationRuntimeConnectionInfo
  property_count: 6
  slug: microsoft-azure-data-factory-integration-runtime-connection-info
- name: IntegrationRuntimeListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-integration-runtime-list-response
- name: IntegrationRuntimeNodeIpAddress
  property_count: 1
  slug: microsoft-azure-data-factory-integration-runtime-node-ip-address
- name: IntegrationRuntimeOutboundNetworkDependenciesEndpointsResponse
  property_count: 1
  slug: microsoft-azure-data-factory-integration-runtime-outbound-network-dependencies-endpoints-response
- name: IntegrationRuntimeResource
  property_count: 2
  slug: microsoft-azure-data-factory-integration-runtime-resource
- name: LinkedServiceListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-linked-service-list-response
- name: LinkedServiceResource
  property_count: 2
  slug: microsoft-azure-data-factory-linked-service-resource
- name: managedPrivateEndpointListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-managed-private-endpoint-list-response
- name: ManagedPrivateEndpointResource
  property_count: 2
  slug: microsoft-azure-data-factory-managed-private-endpoint-resource
- name: ManagedVirtualNetworkListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-managed-virtual-network-list-response
- name: ManagedVirtualNetworkResource
  property_count: 2
  slug: microsoft-azure-data-factory-managed-virtual-network-resource
- name: OperationListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-operation-list-response
- name: PipelineListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-pipeline-list-response
- name: PipelineResource
  property_count: 2
  slug: microsoft-azure-data-factory-pipeline-resource
- name: PipelineRun
  property_count: 13
  slug: microsoft-azure-data-factory-pipeline-run
- name: PipelineRunsQueryResponse
  property_count: 2
  slug: microsoft-azure-data-factory-pipeline-runs-query-response
- name: PrivateEndpointConnectionListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-private-endpoint-connection-list-response
- name: PrivateEndpointConnectionResource
  property_count: 2
  slug: microsoft-azure-data-factory-private-endpoint-connection-resource
- name: PrivateLinkConnectionApprovalRequestResource
  property_count: 5
  slug: microsoft-azure-data-factory-private-link-connection-approval-request-resource
- name: PrivateLinkResourcesWrapper
  property_count: 1
  slug: microsoft-azure-data-factory-private-link-resources-wrapper
- name: QueryDataFlowDebugSessionsResponse
  property_count: 2
  slug: microsoft-azure-data-factory-query-data-flow-debug-sessions-response
- name: Resource
  property_count: 6
  slug: microsoft-azure-data-factory-resource
- name: RunFilterParameters
  property_count: 5
  slug: microsoft-azure-data-factory-run-filter-parameters
- name: SelfHostedIntegrationRuntimeNode
  property_count: 18
  slug: microsoft-azure-data-factory-self-hosted-integration-runtime-node
- name: SsisObjectMetadataListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-ssis-object-metadata-list-response
- name: SsisObjectMetadataStatusResponse
  property_count: 4
  slug: microsoft-azure-data-factory-ssis-object-metadata-status-response
- name: TriggerFilterParameters
  property_count: 2
  slug: microsoft-azure-data-factory-trigger-filter-parameters
- name: TriggerListResponse
  property_count: 2
  slug: microsoft-azure-data-factory-trigger-list-response
- name: TriggerQueryResponse
  property_count: 2
  slug: microsoft-azure-data-factory-trigger-query-response
- name: TriggerResource
  property_count: 2
  slug: microsoft-azure-data-factory-trigger-resource
- name: TriggerRunsQueryResponse
  property_count: 2
  slug: microsoft-azure-data-factory-trigger-runs-query-response
- name: TriggerSubscriptionOperationStatus
  property_count: 2
  slug: microsoft-azure-data-factory-trigger-subscription-operation-status
- name: UpdateIntegrationRuntimeNodeRequest
  property_count: 1
  slug: microsoft-azure-data-factory-update-integration-runtime-node-request
- name: UpdateIntegrationRuntimeRequest
  property_count: 2
  slug: microsoft-azure-data-factory-update-integration-runtime-request
- name: UserAccessPolicy
  property_count: 5
  slug: microsoft-azure-data-factory-user-access-policy
jsonld:
- class_count: 120
  name: Microsoft Azure Data Factory Context
  property_count: 178
  slug: microsoft-azure-data-factory-context
layout: provider
modified: '2026-09-17'
name: Azure Data Factory
nav: Providers
network: true
overview: 'Azure Data Factory publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activityruns API, Credentials API, Datasets API, and 22 more. Tagged areas include Data Integration, ETL, ELT, Data Pipeline, and Data Movement.


  The Azure Data Factory catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Data Factory''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 59 more developer resources.'
plans:
- name: Microsoft Azure Data Factory Plans Pricing
  plan_count: 18
  slug: microsoft-azure-data-factory-plans-pricing
- name: Microsoft Azure Data Factory Price Estimates
  plan_count: 0
  slug: microsoft-azure-data-factory-price-estimates
random_paper: 6
rate_limits:
- limit_count: 6
  name: Microsoft Azure Data Factory Rate Limits
  slug: microsoft-azure-data-factory-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Azure Data Factory API Rules
  rule_count: 53
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 12
  slug: microsoft-azure-data-factory-rules
scopes:
- name: Microsoft Azure Data Factory Scopes
  scope_count: 1
  slug: microsoft-azure-data-factory-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 78.9
  coverage:
    artifact_dirs: 37
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.2
  facets:
    access_clarity: 86.8
    contract_governance: 35.6
    contract_quality: 64.1
    developer_ergonomics: 80.4
    discoverability: 75.0
    operational_transparency: 89.5
  previous_composite: 73.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 92.3
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-data-factory/microsoft-azure-data-factory-2026-06-20T185409.png
security:
- kind: authentication
  name: Microsoft Azure Data Factory Authentication
  slug: microsoft-azure-data-factory-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Data Factory Domain Security
  slug: microsoft-azure-data-factory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Data Factory Vulnerability Disclosure
  slug: microsoft-azure-data-factory-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Data Factory Trust Center
  slug: microsoft-azure-data-factory-trust-center
  summary_line: GDPR
skill_count: 4
skills:
- name: microsoft-azure-data-factory-manage-factory-resources
  slug: microsoft-azure-data-factory-manage-factory-resources
- name: microsoft-azure-data-factory-manage-integration-runtimes
  slug: microsoft-azure-data-factory-manage-integration-runtimes
- name: microsoft-azure-data-factory-manage-triggers
  slug: microsoft-azure-data-factory-manage-triggers
- name: microsoft-azure-data-factory-run-a-pipeline
  slug: microsoft-azure-data-factory-run-a-pipeline
slug: microsoft-azure-data-factory
tags:
- Data Integration
- ETL
- ELT
- Data Pipeline
- Data Movement
- Orchestration
- Data Engineering
- Change Data Capture
- Integration Runtime
- Cloud
- Microsoft Azure
- Data Factory
website: https://www.microsoft.com/
---
