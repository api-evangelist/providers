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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Amazon Application Discovery Service Agentic Access
  operation_count: 26
  slug: amazon-application-discovery-service-agentic-access
  summary_line: 26 operations · 26 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Operations for managing discovery agents and collectors
  name: Amazon Application Discovery Service Agents API
  slug: amazon-application-discovery-service-agents-api
- description: Operations for managing application groupings
  name: Amazon Application Discovery Service Applications API
  slug: amazon-application-discovery-service-applications-api
- description: Operations for querying discovered configuration items
  name: Amazon Application Discovery Service Configurations API
  slug: amazon-application-discovery-service-configurations-api
- description: Operations for exporting discovered data
  name: Amazon Application Discovery Service Exports API
  slug: amazon-application-discovery-service-exports-api
- description: Operations for importing server data
  name: Amazon Application Discovery Service Imports API
  slug: amazon-application-discovery-service-imports-api
- description: Operations for managing configuration item tags
  name: Amazon Application Discovery Service Tags API
  slug: amazon-application-discovery-service-tags-api
artifact_total: 237
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-application-discovery-service-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-application-discovery-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-application-discovery-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-application-discovery-service-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-application-discovery-service-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-application-discovery-service-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-application-discovery-service-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-application-discovery-service-security.txt
created: '2026-03-16'
description: Amazon Application Discovery Service helps enterprise customers plan application migration projects by automatically identifying servers, virtual machines, software, and software dependencies running in their on-premises data centers.
examples:
- key_count: 3
  name: Application Discovery Service Agent Configuration Status Example
  slug: application-discovery-service-agent-configuration-status-example
- key_count: 8
  name: Application Discovery Service Agent Info Example
  slug: application-discovery-service-agent-info-example
- key_count: 2
  name: Application Discovery Service Agent Network Info Example
  slug: application-discovery-service-agent-network-info-example
- key_count: 2
  name: Application Discovery Service Associate Configuration Items Request Example
  slug: application-discovery-service-associate-configuration-items-request-example
- key_count: 3
  name: Application Discovery Service Batch Delete Agent Error Example
  slug: application-discovery-service-batch-delete-agent-error-example
- key_count: 1
  name: Application Discovery Service Batch Delete Agents Request Example
  slug: application-discovery-service-batch-delete-agents-request-example
- key_count: 1
  name: Application Discovery Service Batch Delete Agents Response Example
  slug: application-discovery-service-batch-delete-agents-response-example
- key_count: 8
  name: Application Discovery Service Batch Delete Configuration Task Example
  slug: application-discovery-service-batch-delete-configuration-task-example
- key_count: 3
  name: Application Discovery Service Batch Delete Import Data Error Example
  slug: application-discovery-service-batch-delete-import-data-error-example
- key_count: 2
  name: Application Discovery Service Batch Delete Import Data Request Example
  slug: application-discovery-service-batch-delete-import-data-request-example
- key_count: 1
  name: Application Discovery Service Batch Delete Import Data Response Example
  slug: application-discovery-service-batch-delete-import-data-response-example
- key_count: 5
  name: Application Discovery Service Configuration Tag Example
  slug: application-discovery-service-configuration-tag-example
- key_count: 8
  name: Application Discovery Service Continuous Export Description Example
  slug: application-discovery-service-continuous-export-description-example
- key_count: 2
  name: Application Discovery Service Create Application Request Example
  slug: application-discovery-service-create-application-request-example
- key_count: 1
  name: Application Discovery Service Create Application Response Example
  slug: application-discovery-service-create-application-response-example
- key_count: 2
  name: Application Discovery Service Create Tags Request Example
  slug: application-discovery-service-create-tags-request-example
- key_count: 7
  name: Application Discovery Service Customer Agent Info Example
  slug: application-discovery-service-customer-agent-info-example
- key_count: 7
  name: Application Discovery Service Customer Connector Info Example
  slug: application-discovery-service-customer-connector-info-example
- key_count: 2
  name: Application Discovery Service Delete Agent Example
  slug: application-discovery-service-delete-agent-example
- key_count: 1
  name: Application Discovery Service Delete Applications Request Example
  slug: application-discovery-service-delete-applications-request-example
- key_count: 2
  name: Application Discovery Service Delete Tags Request Example
  slug: application-discovery-service-delete-tags-request-example
- key_count: 3
  name: Application Discovery Service Deletion Warning Example
  slug: application-discovery-service-deletion-warning-example
- key_count: 4
  name: Application Discovery Service Describe Agents Request Example
  slug: application-discovery-service-describe-agents-request-example
- key_count: 2
  name: Application Discovery Service Describe Agents Response Example
  slug: application-discovery-service-describe-agents-response-example
- key_count: 1
  name: Application Discovery Service Describe Batch Delete Configuration Task Request Example
  slug: application-discovery-service-describe-batch-delete-configuration-task-request-example
- key_count: 1
  name: Application Discovery Service Describe Batch Delete Configuration Task Response Example
  slug: application-discovery-service-describe-batch-delete-configuration-task-response-example
- key_count: 1
  name: Application Discovery Service Describe Configurations Request Example
  slug: application-discovery-service-describe-configurations-request-example
- key_count: 1
  name: Application Discovery Service Describe Configurations Response Example
  slug: application-discovery-service-describe-configurations-response-example
- key_count: 3
  name: Application Discovery Service Describe Continuous Exports Request Example
  slug: application-discovery-service-describe-continuous-exports-request-example
- key_count: 2
  name: Application Discovery Service Describe Continuous Exports Response Example
  slug: application-discovery-service-describe-continuous-exports-response-example
- key_count: 4
  name: Application Discovery Service Describe Export Tasks Request Example
  slug: application-discovery-service-describe-export-tasks-request-example
- key_count: 2
  name: Application Discovery Service Describe Export Tasks Response Example
  slug: application-discovery-service-describe-export-tasks-response-example
- key_count: 3
  name: Application Discovery Service Describe Import Tasks Request Example
  slug: application-discovery-service-describe-import-tasks-request-example
- key_count: 2
  name: Application Discovery Service Describe Import Tasks Response Example
  slug: application-discovery-service-describe-import-tasks-response-example
- key_count: 3
  name: Application Discovery Service Describe Tags Request Example
  slug: application-discovery-service-describe-tags-request-example
- key_count: 2
  name: Application Discovery Service Describe Tags Response Example
  slug: application-discovery-service-describe-tags-response-example
- key_count: 2
  name: Application Discovery Service Disassociate Configuration Items Request Example
  slug: application-discovery-service-disassociate-configuration-items-request-example
- key_count: 3
  name: Application Discovery Service Export Filter Example
  slug: application-discovery-service-export-filter-example
- key_count: 8
  name: Application Discovery Service Export Info Example
  slug: application-discovery-service-export-info-example
- key_count: 3
  name: Application Discovery Service Failed Configuration Example
  slug: application-discovery-service-failed-configuration-example
- key_count: 3
  name: Application Discovery Service Filter Example
  slug: application-discovery-service-filter-example
- key_count: 8
  name: Application Discovery Service Get Discovery Summary Response Example
  slug: application-discovery-service-get-discovery-summary-response-example
- key_count: 8
  name: Application Discovery Service Import Task Example
  slug: application-discovery-service-import-task-example
- key_count: 2
  name: Application Discovery Service Import Task Filter Example
  slug: application-discovery-service-import-task-filter-example
- key_count: 5
  name: Application Discovery Service List Configurations Request Example
  slug: application-discovery-service-list-configurations-request-example
- key_count: 2
  name: Application Discovery Service List Configurations Response Example
  slug: application-discovery-service-list-configurations-response-example
- key_count: 5
  name: Application Discovery Service List Server Neighbors Request Example
  slug: application-discovery-service-list-server-neighbors-request-example
- key_count: 3
  name: Application Discovery Service List Server Neighbors Response Example
  slug: application-discovery-service-list-server-neighbors-response-example
- key_count: 5
  name: Application Discovery Service Neighbor Connection Detail Example
  slug: application-discovery-service-neighbor-connection-detail-example
- key_count: 2
  name: Application Discovery Service Order By Element Example
  slug: application-discovery-service-order-by-element-example
- key_count: 2
  name: Application Discovery Service Start Batch Delete Configuration Task Request Example
  slug: application-discovery-service-start-batch-delete-configuration-task-request-example
- key_count: 1
  name: Application Discovery Service Start Batch Delete Configuration Task Response Example
  slug: application-discovery-service-start-batch-delete-configuration-task-response-example
- key_count: 5
  name: Application Discovery Service Start Continuous Export Response Example
  slug: application-discovery-service-start-continuous-export-response-example
- key_count: 1
  name: Application Discovery Service Start Data Collection By Agent Ids Request Example
  slug: application-discovery-service-start-data-collection-by-agent-ids-request-example
- key_count: 1
  name: Application Discovery Service Start Data Collection By Agent Ids Response Example
  slug: application-discovery-service-start-data-collection-by-agent-ids-response-example
- key_count: 5
  name: Application Discovery Service Start Export Task Request Example
  slug: application-discovery-service-start-export-task-request-example
- key_count: 1
  name: Application Discovery Service Start Export Task Response Example
  slug: application-discovery-service-start-export-task-response-example
- key_count: 3
  name: Application Discovery Service Start Import Task Request Example
  slug: application-discovery-service-start-import-task-request-example
- key_count: 1
  name: Application Discovery Service Start Import Task Response Example
  slug: application-discovery-service-start-import-task-response-example
- key_count: 1
  name: Application Discovery Service Stop Continuous Export Request Example
  slug: application-discovery-service-stop-continuous-export-request-example
- key_count: 2
  name: Application Discovery Service Stop Continuous Export Response Example
  slug: application-discovery-service-stop-continuous-export-response-example
- key_count: 1
  name: Application Discovery Service Stop Data Collection By Agent Ids Request Example
  slug: application-discovery-service-stop-data-collection-by-agent-ids-request-example
- key_count: 1
  name: Application Discovery Service Stop Data Collection By Agent Ids Response Example
  slug: application-discovery-service-stop-data-collection-by-agent-ids-response-example
- key_count: 2
  name: Application Discovery Service Tag Example
  slug: application-discovery-service-tag-example
- key_count: 2
  name: Application Discovery Service Tag Filter Example
  slug: application-discovery-service-tag-filter-example
- key_count: 3
  name: Application Discovery Service Update Application Request Example
  slug: application-discovery-service-update-application-request-example
features:
- Agentless Discovery via VMware vCenter integration
- Agent-based discovery for physical and virtual servers
- Automatic server dependency mapping via network traffic analysis
- Application grouping and tagging for migration planning
- Data export to Amazon S3 in CSV and GraphML formats
- Bulk import of server inventory via CSV files
- Integration with AWS Migration Hub for centralized tracking
- Continuous data collection with configurable intervals
- Server neighbor discovery for dependency visualization
- Tag-based filtering and organization of discovered assets
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-application-discovery-service.png
integrations:
- AWS Migration Hub
- AWS Server Migration Service
- AWS Application Migration Service
- Amazon EC2
- Amazon S3
- VMware vCenter
- AWS Database Migration Service
- AWS CloudFormation
- AWS Systems Manager
- AWS Cost Explorer
json_schemas:
- name: AgentConfigurationStatus
  property_count: 3
  slug: application-discovery-service-agent-configuration-status
- name: AgentInfo
  property_count: 10
  slug: application-discovery-service-agent-info
- name: AgentNetworkInfo
  property_count: 2
  slug: application-discovery-service-agent-network-info
- name: AssociateConfigurationItemsRequest
  property_count: 2
  slug: application-discovery-service-associate-configuration-items-request
- name: BatchDeleteAgentError
  property_count: 3
  slug: application-discovery-service-batch-delete-agent-error
- name: BatchDeleteAgentsRequest
  property_count: 1
  slug: application-discovery-service-batch-delete-agents-request
- name: BatchDeleteAgentsResponse
  property_count: 1
  slug: application-discovery-service-batch-delete-agents-response
- name: BatchDeleteConfigurationTask
  property_count: 9
  slug: application-discovery-service-batch-delete-configuration-task
- name: BatchDeleteImportDataError
  property_count: 3
  slug: application-discovery-service-batch-delete-import-data-error
- name: BatchDeleteImportDataRequest
  property_count: 2
  slug: application-discovery-service-batch-delete-import-data-request
- name: BatchDeleteImportDataResponse
  property_count: 1
  slug: application-discovery-service-batch-delete-import-data-response
- name: ConfigurationTag
  property_count: 5
  slug: application-discovery-service-configuration-tag
- name: ContinuousExportDescription
  property_count: 8
  slug: application-discovery-service-continuous-export-description
- name: CreateApplicationRequest
  property_count: 2
  slug: application-discovery-service-create-application-request
- name: CreateApplicationResponse
  property_count: 1
  slug: application-discovery-service-create-application-response
- name: CreateTagsRequest
  property_count: 2
  slug: application-discovery-service-create-tags-request
- name: CustomerAgentInfo
  property_count: 7
  slug: application-discovery-service-customer-agent-info
- name: CustomerConnectorInfo
  property_count: 7
  slug: application-discovery-service-customer-connector-info
- name: DeleteAgent
  property_count: 2
  slug: application-discovery-service-delete-agent
- name: DeleteApplicationsRequest
  property_count: 1
  slug: application-discovery-service-delete-applications-request
- name: DeleteTagsRequest
  property_count: 2
  slug: application-discovery-service-delete-tags-request
- name: DeletionWarning
  property_count: 3
  slug: application-discovery-service-deletion-warning
- name: DescribeAgentsRequest
  property_count: 4
  slug: application-discovery-service-describe-agents-request
- name: DescribeAgentsResponse
  property_count: 2
  slug: application-discovery-service-describe-agents-response
- name: DescribeBatchDeleteConfigurationTaskRequest
  property_count: 1
  slug: application-discovery-service-describe-batch-delete-configuration-task-request
- name: DescribeBatchDeleteConfigurationTaskResponse
  property_count: 1
  slug: application-discovery-service-describe-batch-delete-configuration-task-response
- name: DescribeConfigurationsRequest
  property_count: 1
  slug: application-discovery-service-describe-configurations-request
- name: DescribeConfigurationsResponse
  property_count: 1
  slug: application-discovery-service-describe-configurations-response
- name: DescribeContinuousExportsRequest
  property_count: 3
  slug: application-discovery-service-describe-continuous-exports-request
- name: DescribeContinuousExportsResponse
  property_count: 2
  slug: application-discovery-service-describe-continuous-exports-response
- name: DescribeExportTasksRequest
  property_count: 4
  slug: application-discovery-service-describe-export-tasks-request
- name: DescribeExportTasksResponse
  property_count: 2
  slug: application-discovery-service-describe-export-tasks-response
- name: DescribeImportTasksRequest
  property_count: 3
  slug: application-discovery-service-describe-import-tasks-request
- name: DescribeImportTasksResponse
  property_count: 2
  slug: application-discovery-service-describe-import-tasks-response
- name: DescribeTagsRequest
  property_count: 3
  slug: application-discovery-service-describe-tags-request
- name: DescribeTagsResponse
  property_count: 2
  slug: application-discovery-service-describe-tags-response
- name: DisassociateConfigurationItemsRequest
  property_count: 2
  slug: application-discovery-service-disassociate-configuration-items-request
- name: ExportFilter
  property_count: 3
  slug: application-discovery-service-export-filter
- name: ExportInfo
  property_count: 8
  slug: application-discovery-service-export-info
- name: FailedConfiguration
  property_count: 3
  slug: application-discovery-service-failed-configuration
- name: Filter
  property_count: 3
  slug: application-discovery-service-filter
- name: GetDiscoverySummaryResponse
  property_count: 8
  slug: application-discovery-service-get-discovery-summary-response
- name: ImportTaskFilter
  property_count: 2
  slug: application-discovery-service-import-task-filter
- name: ImportTask
  property_count: 13
  slug: application-discovery-service-import-task
- name: ListConfigurationsRequest
  property_count: 5
  slug: application-discovery-service-list-configurations-request
- name: ListConfigurationsResponse
  property_count: 2
  slug: application-discovery-service-list-configurations-response
- name: ListServerNeighborsRequest
  property_count: 5
  slug: application-discovery-service-list-server-neighbors-request
- name: ListServerNeighborsResponse
  property_count: 3
  slug: application-discovery-service-list-server-neighbors-response
- name: NeighborConnectionDetail
  property_count: 5
  slug: application-discovery-service-neighbor-connection-detail
- name: OrderByElement
  property_count: 2
  slug: application-discovery-service-order-by-element
- name: StartBatchDeleteConfigurationTaskRequest
  property_count: 2
  slug: application-discovery-service-start-batch-delete-configuration-task-request
- name: StartBatchDeleteConfigurationTaskResponse
  property_count: 1
  slug: application-discovery-service-start-batch-delete-configuration-task-response
- name: StartContinuousExportResponse
  property_count: 5
  slug: application-discovery-service-start-continuous-export-response
- name: StartDataCollectionByAgentIdsRequest
  property_count: 1
  slug: application-discovery-service-start-data-collection-by-agent-ids-request
- name: StartDataCollectionByAgentIdsResponse
  property_count: 1
  slug: application-discovery-service-start-data-collection-by-agent-ids-response
- name: StartExportTaskRequest
  property_count: 5
  slug: application-discovery-service-start-export-task-request
- name: StartExportTaskResponse
  property_count: 1
  slug: application-discovery-service-start-export-task-response
- name: StartImportTaskRequest
  property_count: 3
  slug: application-discovery-service-start-import-task-request
- name: StartImportTaskResponse
  property_count: 1
  slug: application-discovery-service-start-import-task-response
- name: StopContinuousExportRequest
  property_count: 1
  slug: application-discovery-service-stop-continuous-export-request
- name: StopContinuousExportResponse
  property_count: 2
  slug: application-discovery-service-stop-continuous-export-response
- name: StopDataCollectionByAgentIdsRequest
  property_count: 1
  slug: application-discovery-service-stop-data-collection-by-agent-ids-request
- name: StopDataCollectionByAgentIdsResponse
  property_count: 1
  slug: application-discovery-service-stop-data-collection-by-agent-ids-response
- name: TagFilter
  property_count: 2
  slug: application-discovery-service-tag-filter
- name: Tag
  property_count: 2
  slug: application-discovery-service-tag
- name: UpdateApplicationRequest
  property_count: 3
  slug: application-discovery-service-update-application-request
json_structures:
- name: Application Discovery Service Agent Configuration Status Structure
  property_count: 3
  slug: application-discovery-service-agent-configuration-status-structure
- name: Application Discovery Service Agent Info Structure
  property_count: 10
  slug: application-discovery-service-agent-info-structure
- name: Application Discovery Service Agent Network Info Structure
  property_count: 2
  slug: application-discovery-service-agent-network-info-structure
- name: Application Discovery Service Associate Configuration Items Request Structure
  property_count: 2
  slug: application-discovery-service-associate-configuration-items-request-structure
- name: Application Discovery Service Batch Delete Agent Error Structure
  property_count: 3
  slug: application-discovery-service-batch-delete-agent-error-structure
- name: Application Discovery Service Batch Delete Agents Request Structure
  property_count: 1
  slug: application-discovery-service-batch-delete-agents-request-structure
- name: Application Discovery Service Batch Delete Agents Response Structure
  property_count: 1
  slug: application-discovery-service-batch-delete-agents-response-structure
- name: Application Discovery Service Batch Delete Configuration Task Structure
  property_count: 9
  slug: application-discovery-service-batch-delete-configuration-task-structure
- name: Application Discovery Service Batch Delete Import Data Error Structure
  property_count: 3
  slug: application-discovery-service-batch-delete-import-data-error-structure
- name: Application Discovery Service Batch Delete Import Data Request Structure
  property_count: 2
  slug: application-discovery-service-batch-delete-import-data-request-structure
- name: Application Discovery Service Batch Delete Import Data Response Structure
  property_count: 1
  slug: application-discovery-service-batch-delete-import-data-response-structure
- name: Application Discovery Service Configuration Tag Structure
  property_count: 5
  slug: application-discovery-service-configuration-tag-structure
- name: Application Discovery Service Continuous Export Description Structure
  property_count: 8
  slug: application-discovery-service-continuous-export-description-structure
- name: Application Discovery Service Create Application Request Structure
  property_count: 2
  slug: application-discovery-service-create-application-request-structure
- name: Application Discovery Service Create Application Response Structure
  property_count: 1
  slug: application-discovery-service-create-application-response-structure
- name: Application Discovery Service Create Tags Request Structure
  property_count: 2
  slug: application-discovery-service-create-tags-request-structure
- name: Application Discovery Service Customer Agent Info Structure
  property_count: 7
  slug: application-discovery-service-customer-agent-info-structure
- name: Application Discovery Service Customer Connector Info Structure
  property_count: 7
  slug: application-discovery-service-customer-connector-info-structure
- name: Application Discovery Service Delete Agent Structure
  property_count: 2
  slug: application-discovery-service-delete-agent-structure
- name: Application Discovery Service Delete Applications Request Structure
  property_count: 1
  slug: application-discovery-service-delete-applications-request-structure
- name: Application Discovery Service Delete Tags Request Structure
  property_count: 2
  slug: application-discovery-service-delete-tags-request-structure
- name: Application Discovery Service Deletion Warning Structure
  property_count: 3
  slug: application-discovery-service-deletion-warning-structure
- name: Application Discovery Service Describe Agents Request Structure
  property_count: 4
  slug: application-discovery-service-describe-agents-request-structure
- name: Application Discovery Service Describe Agents Response Structure
  property_count: 2
  slug: application-discovery-service-describe-agents-response-structure
- name: Application Discovery Service Describe Batch Delete Configuration Task Request Structure
  property_count: 1
  slug: application-discovery-service-describe-batch-delete-configuration-task-request-structure
- name: Application Discovery Service Describe Batch Delete Configuration Task Response Structure
  property_count: 1
  slug: application-discovery-service-describe-batch-delete-configuration-task-response-structure
- name: Application Discovery Service Describe Configurations Request Structure
  property_count: 1
  slug: application-discovery-service-describe-configurations-request-structure
- name: Application Discovery Service Describe Configurations Response Structure
  property_count: 1
  slug: application-discovery-service-describe-configurations-response-structure
- name: Application Discovery Service Describe Continuous Exports Request Structure
  property_count: 3
  slug: application-discovery-service-describe-continuous-exports-request-structure
- name: Application Discovery Service Describe Continuous Exports Response Structure
  property_count: 2
  slug: application-discovery-service-describe-continuous-exports-response-structure
- name: Application Discovery Service Describe Export Tasks Request Structure
  property_count: 4
  slug: application-discovery-service-describe-export-tasks-request-structure
- name: Application Discovery Service Describe Export Tasks Response Structure
  property_count: 2
  slug: application-discovery-service-describe-export-tasks-response-structure
- name: Application Discovery Service Describe Import Tasks Request Structure
  property_count: 3
  slug: application-discovery-service-describe-import-tasks-request-structure
- name: Application Discovery Service Describe Import Tasks Response Structure
  property_count: 2
  slug: application-discovery-service-describe-import-tasks-response-structure
- name: Application Discovery Service Describe Tags Request Structure
  property_count: 3
  slug: application-discovery-service-describe-tags-request-structure
- name: Application Discovery Service Describe Tags Response Structure
  property_count: 2
  slug: application-discovery-service-describe-tags-response-structure
- name: Application Discovery Service Disassociate Configuration Items Request Structure
  property_count: 2
  slug: application-discovery-service-disassociate-configuration-items-request-structure
- name: Application Discovery Service Export Filter Structure
  property_count: 3
  slug: application-discovery-service-export-filter-structure
- name: Application Discovery Service Export Info Structure
  property_count: 8
  slug: application-discovery-service-export-info-structure
- name: Application Discovery Service Failed Configuration Structure
  property_count: 3
  slug: application-discovery-service-failed-configuration-structure
- name: Application Discovery Service Filter Structure
  property_count: 3
  slug: application-discovery-service-filter-structure
- name: Application Discovery Service Get Discovery Summary Response Structure
  property_count: 8
  slug: application-discovery-service-get-discovery-summary-response-structure
- name: Application Discovery Service Import Task Filter Structure
  property_count: 2
  slug: application-discovery-service-import-task-filter-structure
- name: Application Discovery Service Import Task Structure
  property_count: 13
  slug: application-discovery-service-import-task-structure
- name: Application Discovery Service List Configurations Request Structure
  property_count: 5
  slug: application-discovery-service-list-configurations-request-structure
- name: Application Discovery Service List Configurations Response Structure
  property_count: 2
  slug: application-discovery-service-list-configurations-response-structure
- name: Application Discovery Service List Server Neighbors Request Structure
  property_count: 5
  slug: application-discovery-service-list-server-neighbors-request-structure
- name: Application Discovery Service List Server Neighbors Response Structure
  property_count: 3
  slug: application-discovery-service-list-server-neighbors-response-structure
- name: Application Discovery Service Neighbor Connection Detail Structure
  property_count: 5
  slug: application-discovery-service-neighbor-connection-detail-structure
- name: Application Discovery Service Order By Element Structure
  property_count: 2
  slug: application-discovery-service-order-by-element-structure
- name: Application Discovery Service Start Batch Delete Configuration Task Request Structure
  property_count: 2
  slug: application-discovery-service-start-batch-delete-configuration-task-request-structure
- name: Application Discovery Service Start Batch Delete Configuration Task Response Structure
  property_count: 1
  slug: application-discovery-service-start-batch-delete-configuration-task-response-structure
- name: Application Discovery Service Start Continuous Export Response Structure
  property_count: 5
  slug: application-discovery-service-start-continuous-export-response-structure
- name: Application Discovery Service Start Data Collection By Agent Ids Request Structure
  property_count: 1
  slug: application-discovery-service-start-data-collection-by-agent-ids-request-structure
- name: Application Discovery Service Start Data Collection By Agent Ids Response Structure
  property_count: 1
  slug: application-discovery-service-start-data-collection-by-agent-ids-response-structure
- name: Application Discovery Service Start Export Task Request Structure
  property_count: 5
  slug: application-discovery-service-start-export-task-request-structure
- name: Application Discovery Service Start Export Task Response Structure
  property_count: 1
  slug: application-discovery-service-start-export-task-response-structure
- name: Application Discovery Service Start Import Task Request Structure
  property_count: 3
  slug: application-discovery-service-start-import-task-request-structure
- name: Application Discovery Service Start Import Task Response Structure
  property_count: 1
  slug: application-discovery-service-start-import-task-response-structure
- name: Application Discovery Service Stop Continuous Export Request Structure
  property_count: 1
  slug: application-discovery-service-stop-continuous-export-request-structure
- name: Application Discovery Service Stop Continuous Export Response Structure
  property_count: 2
  slug: application-discovery-service-stop-continuous-export-response-structure
- name: Application Discovery Service Stop Data Collection By Agent Ids Request Structure
  property_count: 1
  slug: application-discovery-service-stop-data-collection-by-agent-ids-request-structure
- name: Application Discovery Service Stop Data Collection By Agent Ids Response Structure
  property_count: 1
  slug: application-discovery-service-stop-data-collection-by-agent-ids-response-structure
- name: Application Discovery Service Tag Filter Structure
  property_count: 2
  slug: application-discovery-service-tag-filter-structure
- name: Application Discovery Service Tag Structure
  property_count: 2
  slug: application-discovery-service-tag-structure
- name: Application Discovery Service Update Application Request Structure
  property_count: 3
  slug: application-discovery-service-update-application-request-structure
jsonld:
- class_count: 69
  name: Amazon Application Discovery Service Context
  property_count: 113
  slug: amazon-application-discovery-service-context
layout: provider
modified: '2026-06-20'
name: Amazon Application Discovery Service
nav: Providers
network: true
overview: 'Amazon Application Discovery Service publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Applications API, Configurations API, and 3 more. Tagged areas include Amazon Application Discovery Service, Migration, Discovery, and Infrastructure.


  The Amazon Application Discovery Service catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Application Discovery Service''s developer surface includes authentication and 7 more developer resources.'
random_paper: 18
rules:
- name: Amazon Application Discovery Service API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-application-discovery-service-jsonschema-spectral-rules
- name: Amazon Application Discovery Service API Rules
  rule_count: 28
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 12
  slug: amazon-application-discovery-service-spectral-rules
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 82.3
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 40.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/screenshots/amazon-application-discovery-service-2026-07-25T195925.png
security:
- kind: authentication
  name: Amazon Application Discovery Service Authentication
  slug: amazon-application-discovery-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Application Discovery Service Domain Security
  slug: amazon-application-discovery-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Application Discovery Service Vulnerability Disclosure
  slug: amazon-application-discovery-service-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-application-discovery-service
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
use_cases:
- Discover all servers and processes in on-premises data centers before migration
- Map application dependencies to create migration groups and waves
- Export inventory data for detailed analysis and migration planning in third-party tools
- Import existing server inventory from CMDBs or spreadsheets without installing agents
- Track migration readiness across thousands of servers in a single dashboard
- Identify unknown servers and shadow IT in large enterprise environments
---
