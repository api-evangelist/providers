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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-09-17'
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
  slug: microsoft-azure-data-factory-activityruns-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Change Data Capture operations on the Microsoft.DataFactory resource provider (7 operations): ChangeDataCapture_ListByFactory, ChangeDataCapture_Get, ChangeDataCapture_CreateOrUpdate, ChangeDataCaptur'
  name: Azure Data Factory Change Data Capture API
  slug: microsoft-azure-data-factory-change-data-capture-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Credentials operations on the Microsoft.DataFactory resource provider (4 operations): CredentialOperations_ListByFactory, CredentialOperations_Get, CredentialOperations_CreateOrUpdate, CredentialOpera'
  name: Azure Data Factory Credentials API
  slug: microsoft-azure-data-factory-credentials-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Data Flow Debug Session operations on the Microsoft.DataFactory resource provider (5 operations): DataFlowDebugSession_AddDataFlow, DataFlowDebugSession_Create, DataFlowDebugSession_Delete, DataFlowDe'
  name: Azure Data Factory Data Flow Debug Session API
  slug: microsoft-azure-data-factory-data-flow-debug-session-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Data Flows operations on the Microsoft.DataFactory resource provider (4 operations): DataFlows_ListByFactory, DataFlows_Get, DataFlows_CreateOrUpdate, DataFlows_Delete.'
  name: Azure Data Factory Data Flows API
  slug: microsoft-azure-data-factory-data-flows-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Datasets operations on the Microsoft.DataFactory resource provider (4 operations): Datasets_ListByFactory, Datasets_Get, Datasets_CreateOrUpdate, Datasets_Delete.'
  name: Azure Data Factory Datasets API
  slug: microsoft-azure-data-factory-datasets-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Exposure Control operations on the Microsoft.DataFactory resource provider (3 operations): ExposureControl_GetFeatureValue, ExposureControl_GetFeatureValueByFactory, ExposureControl_QueryFeatureValues'
  name: Azure Data Factory Exposure Control API
  slug: microsoft-azure-data-factory-exposure-control-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Factories operations on the Microsoft.DataFactory resource provider (9 operations): Factories_List, Factories_ConfigureFactoryRepo, Factories_ListByResourceGroup, Factories_Get, Factories_CreateOrUpda'
  name: Azure Data Factory Factories API
  slug: microsoft-azure-data-factory-factories-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Global Parameters operations on the Microsoft.DataFactory resource provider (4 operations): GlobalParameters_ListByFactory, GlobalParameters_Get, GlobalParameters_CreateOrUpdate, GlobalParameters_Dele'
  name: Azure Data Factory Global Parameters API
  slug: microsoft-azure-data-factory-global-parameters-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Integration Runtime Disable Interactive Query operations on the Microsoft.DataFactory resource provider (1 operation): IntegrationRuntime_DisableInteractiveQuery.'
  name: Azure Data Factory Integration Runtime Disable Interactive Query API
  slug: microsoft-azure-data-factory-integration-runtime-disable-interactive-query-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Integration Runtime Enable Interactive Query operations on the Microsoft.DataFactory resource provider (1 operation): IntegrationRuntime_EnableInteractiveQuery.'
  name: Azure Data Factory Integration Runtime Enable Interactive Query API
  slug: microsoft-azure-data-factory-integration-runtime-enable-interactive-query-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Integration Runtime Nodes operations on the Microsoft.DataFactory resource provider (4 operations): IntegrationRuntimeNodes_Get, IntegrationRuntimeNodes_Update, IntegrationRuntimeNodes_Delete, Integra'
  name: Azure Data Factory Integration Runtime Nodes API
  slug: microsoft-azure-data-factory-integration-runtime-nodes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Integration Runtime Object Metadata operations on the Microsoft.DataFactory resource provider (2 operations): IntegrationRuntimeObjectMetadata_Get, IntegrationRuntimeObjectMetadata_Refresh.'
  name: Azure Data Factory Integration Runtime Object Metadata API
  slug: microsoft-azure-data-factory-integration-runtime-object-metadata-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Integration Runtimes operations on the Microsoft.DataFactory resource provider (17 operations): IntegrationRuntimes_ListByFactory, IntegrationRuntimes_Get, IntegrationRuntimes_CreateOrUpdate, Integrat'
  name: Azure Data Factory Integration Runtimes API
  slug: microsoft-azure-data-factory-integration-runtimes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Linked Services operations on the Microsoft.DataFactory resource provider (4 operations): LinkedServices_ListByFactory, LinkedServices_Get, LinkedServices_CreateOrUpdate, LinkedServices_Delete.'
  name: Azure Data Factory Linked Services API
  slug: microsoft-azure-data-factory-linked-services-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Managed Private Endpoints operations on the Microsoft.DataFactory resource provider (4 operations): ManagedPrivateEndpoints_ListByFactory, ManagedPrivateEndpoints_Get, ManagedPrivateEndpoints_CreateOr'
  name: Azure Data Factory Managed Private Endpoints API
  slug: microsoft-azure-data-factory-managed-private-endpoints-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Managed Virtual Networks operations on the Microsoft.DataFactory resource provider (3 operations): ManagedVirtualNetworks_ListByFactory, ManagedVirtualNetworks_Get, ManagedVirtualNetworks_CreateOrUpda'
  name: Azure Data Factory Managed Virtual Networks API
  slug: microsoft-azure-data-factory-managed-virtual-networks-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Operations operations on the Microsoft.DataFactory resource provider (1 operation): Operations_List.'
  name: Azure Data Factory Operations API
  slug: microsoft-azure-data-factory-operations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Pipelineruns operations on the Microsoft.DataFactory resource provider (3 operations): PipelineRuns_Get, PipelineRuns_Cancel, PipelineRuns_QueryByFactory.'
  name: Azure Data Factory Pipelineruns API
  slug: microsoft-azure-data-factory-pipelineruns-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Pipelines operations on the Microsoft.DataFactory resource provider (5 operations): Pipelines_ListByFactory, Pipelines_Get, Pipelines_CreateOrUpdate, Pipelines_Delete, Pipelines_CreateRun.'
  name: Azure Data Factory Pipelines API
  slug: microsoft-azure-data-factory-pipelines-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Private Endpoint Connections operations on the Microsoft.DataFactory resource provider (4 operations): privateEndPointConnections_ListByFactory, PrivateEndpointConnection_Get, PrivateEndpointConnectio'
  name: Azure Data Factory Private Endpoint Connections API
  slug: microsoft-azure-data-factory-private-endpoint-connections-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Private Link Resources operations on the Microsoft.DataFactory resource provider (1 operation): privateLinkResources_Get.'
  name: Azure Data Factory Private Link Resources API
  slug: microsoft-azure-data-factory-private-link-resources-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Trigger operations on the Microsoft.DataFactory resource provider (1 operation): Triggers_Get.'
  name: Azure Data Factory Trigger API
  slug: microsoft-azure-data-factory-trigger-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Triggerruns operations on the Microsoft.DataFactory resource provider (3 operations): TriggerRuns_QueryByFactory, TriggerRuns_Cancel, TriggerRuns_Rerun.'
  name: Azure Data Factory Triggerruns API
  slug: microsoft-azure-data-factory-triggerruns-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'Triggers operations on the Microsoft.DataFactory resource provider (9 operations): Triggers_QueryByFactory, Triggers_ListByFactory, Triggers_CreateOrUpdate, Triggers_Delete, Triggers_GetEventSubscript'
  name: Azure Data Factory Triggers API
  slug: microsoft-azure-data-factory-triggers-api
artifact_total: 150
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/changelog/microsoft-azure-data-factory-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-data-factory-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/data-factory/whats-new
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/lifecycle/microsoft-azure-data-factory-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-azure-data-factory-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/lifecycle/microsoft-azure-data-factory-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-data-factory-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/authentication/microsoft-azure-data-factory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-data-factory-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/scopes/microsoft-azure-data-factory-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-data-factory-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/conventions/microsoft-azure-data-factory-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-data-factory-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/conventions/microsoft-azure-data-factory-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-data-factory-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/errors/microsoft-azure-data-factory-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-data-factory-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/rate-limits/microsoft-azure-data-factory-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-data-factory-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/plans/microsoft-azure-data-factory-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-data-factory-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/finops/microsoft-azure-data-factory-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-data-factory-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/data-model/microsoft-azure-data-factory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-data-factory-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/packages/microsoft-azure-data-factory-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-data-factory-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/packages/microsoft-azure-data-factory-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-data-factory-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/cli/microsoft-azure-data-factory-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-data-factory-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/sandbox/microsoft-azure-data-factory-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-azure-data-factory-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/conformance/microsoft-azure-data-factory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-data-factory-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/conformance/microsoft-azure-data-factory-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-data-factory-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/security/microsoft-azure-data-factory-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-data-factory-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/security/microsoft-azure-data-factory-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-data-factory-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/security/microsoft-azure-data-factory-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-data-factory-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/well-known/microsoft-azure-data-factory-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-data-factory-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/well-known/microsoft-azure-data-factory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-data-factory-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/security/microsoft-azure-data-factory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-data-factory-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/agentic-access/microsoft-azure-data-factory-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-data-factory-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/llms/microsoft-azure-data-factory-llms.txt
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
- name: Microsoft Azure Data Factory Finops
  service_category: API
  slug: microsoft-azure-data-factory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-data-factory.png
layout: provider
modified: '2026-09-17'
name: Azure Data Factory
nav: Providers
network: true
overview: 'Azure Data Factory publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Activityruns API, Change Data Capture API, Credentials API, and 22 more. Tagged areas include Data Integration, ETL, ELT, Data Pipeline, and Data Movement.


  Azure Data Factory''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Microsoft Azure Data Factory Plans Pricing
  plan_count: 7
  slug: microsoft-azure-data-factory-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Microsoft Azure Data Factory Rate Limits
  slug: microsoft-azure-data-factory-rate-limits
scopes:
- name: Microsoft Azure Data Factory Scopes
  scope_count: 1
  slug: microsoft-azure-data-factory-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 70.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.1
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 80.4
    discoverability: 66.7
    operational_transparency: 89.5
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/screenshots/microsoft-azure-data-factory-2026-06-20T185409.png
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
- Azure
- Data Factory
website: https://www.microsoft.com/
---
