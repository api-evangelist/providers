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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 2
  name: Amazon Appflow Agentic Access
  operation_count: 25
  slug: amazon-appflow-agentic-access
  summary_line: 25 operations · 24 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Operations for managing connector profiles and connector registrations
  name: Amazon AppFlow Connectors API
  slug: amazon-appflow-connectors-api
- description: Operations for creating and managing data flows
  name: Amazon AppFlow Flows API
  slug: amazon-appflow-flows-api
- description: Operations for managing resource tags
  name: Amazon AppFlow Tags API
  slug: amazon-appflow-tags-api
artifact_total: 213
collections:
- collection_type: postman
  name: Amazon AppFlow Connectors API
  slug: postman-amazon-appflow-connectors-api
- collection_type: postman
  name: Amazon AppFlow Connectors Flows API
  slug: postman-amazon-appflow-flows-api
- collection_type: postman
  name: Amazon AppFlow Connectors Tags API
  slug: postman-amazon-appflow-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-appflow/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-appflow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-appflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-appflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-appflow-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/appflow/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/appflow/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws/category/application-integration/amazon-appflow/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/appflow
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: operate
  title: ''
  type: FAQ
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-appflow
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-appflow-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-appflow-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-appflow-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-appflow-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-appflow-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-appflow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-appflow-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-appflow-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-appflow-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-appflow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-appflow-lifecycle.yml
created: '2024-01-15'
description: Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between SaaS applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow, and AWS services like Amazon S3 and Amazon Redshift, in just a few clicks.
examples:
- key_count: 10
  name: Amazon Appflow Example
  slug: amazon-appflow-example
- key_count: 2
  name: Appflow Cancel Flow Executions Request Example
  slug: appflow-cancel-flow-executions-request-example
- key_count: 1
  name: Appflow Cancel Flow Executions Response Example
  slug: appflow-cancel-flow-executions-response-example
- key_count: 10
  name: Appflow Connector Detail Example
  slug: appflow-connector-detail-example
- key_count: 3
  name: Appflow Connector Entity Example
  slug: appflow-connector-entity-example
- key_count: 10
  name: Appflow Connector Entity Field Example
  slug: appflow-connector-entity-field-example
- key_count: 10
  name: Appflow Connector Profile Example
  slug: appflow-connector-profile-example
- key_count: 7
  name: Appflow Create Connector Profile Request Example
  slug: appflow-create-connector-profile-request-example
- key_count: 1
  name: Appflow Create Connector Profile Response Example
  slug: appflow-create-connector-profile-response-example
- key_count: 10
  name: Appflow Create Flow Request Example
  slug: appflow-create-flow-request-example
- key_count: 2
  name: Appflow Create Flow Response Example
  slug: appflow-create-flow-response-example
- key_count: 2
  name: Appflow Delete Connector Profile Request Example
  slug: appflow-delete-connector-profile-request-example
- key_count: 2
  name: Appflow Delete Flow Request Example
  slug: appflow-delete-flow-request-example
- key_count: 4
  name: Appflow Describe Connector Entity Request Example
  slug: appflow-describe-connector-entity-request-example
- key_count: 1
  name: Appflow Describe Connector Entity Response Example
  slug: appflow-describe-connector-entity-response-example
- key_count: 5
  name: Appflow Describe Connector Profiles Request Example
  slug: appflow-describe-connector-profiles-request-example
- key_count: 2
  name: Appflow Describe Connector Profiles Response Example
  slug: appflow-describe-connector-profiles-response-example
- key_count: 2
  name: Appflow Describe Connector Request Example
  slug: appflow-describe-connector-request-example
- key_count: 1
  name: Appflow Describe Connector Response Example
  slug: appflow-describe-connector-response-example
- key_count: 3
  name: Appflow Describe Connectors Request Example
  slug: appflow-describe-connectors-request-example
- key_count: 3
  name: Appflow Describe Connectors Response Example
  slug: appflow-describe-connectors-response-example
- key_count: 3
  name: Appflow Describe Flow Execution Records Request Example
  slug: appflow-describe-flow-execution-records-request-example
- key_count: 2
  name: Appflow Describe Flow Execution Records Response Example
  slug: appflow-describe-flow-execution-records-response-example
- key_count: 1
  name: Appflow Describe Flow Request Example
  slug: appflow-describe-flow-request-example
- key_count: 10
  name: Appflow Describe Flow Response Example
  slug: appflow-describe-flow-response-example
- key_count: 4
  name: Appflow Destination Flow Config Example
  slug: appflow-destination-flow-config-example
- key_count: 3
  name: Appflow Execution Details Example
  slug: appflow-execution-details-example
- key_count: 5
  name: Appflow Execution Result Example
  slug: appflow-execution-result-example
- key_count: 10
  name: Appflow Flow Definition Example
  slug: appflow-flow-definition-example
- key_count: 7
  name: Appflow Flow Execution Example
  slug: appflow-flow-execution-example
- key_count: 6
  name: Appflow List Connector Entities Request Example
  slug: appflow-list-connector-entities-request-example
- key_count: 2
  name: Appflow List Connector Entities Response Example
  slug: appflow-list-connector-entities-response-example
- key_count: 2
  name: Appflow List Connectors Request Example
  slug: appflow-list-connectors-request-example
- key_count: 2
  name: Appflow List Connectors Response Example
  slug: appflow-list-connectors-response-example
- key_count: 2
  name: Appflow List Flows Request Example
  slug: appflow-list-flows-request-example
- key_count: 2
  name: Appflow List Flows Response Example
  slug: appflow-list-flows-response-example
- key_count: 1
  name: Appflow List Tags For Resource Response Example
  slug: appflow-list-tags-for-resource-response-example
- key_count: 1
  name: Appflow Metadata Catalog Config Example
  slug: appflow-metadata-catalog-config-example
- key_count: 5
  name: Appflow Register Connector Request Example
  slug: appflow-register-connector-request-example
- key_count: 1
  name: Appflow Register Connector Response Example
  slug: appflow-register-connector-response-example
- key_count: 5
  name: Appflow Reset Connector Metadata Cache Request Example
  slug: appflow-reset-connector-metadata-cache-request-example
- key_count: 8
  name: Appflow Scheduled Trigger Properties Example
  slug: appflow-scheduled-trigger-properties-example
- key_count: 5
  name: Appflow Source Flow Config Example
  slug: appflow-source-flow-config-example
- key_count: 2
  name: Appflow Start Flow Request Example
  slug: appflow-start-flow-request-example
- key_count: 3
  name: Appflow Start Flow Response Example
  slug: appflow-start-flow-response-example
- key_count: 1
  name: Appflow Stop Flow Request Example
  slug: appflow-stop-flow-request-example
- key_count: 2
  name: Appflow Stop Flow Response Example
  slug: appflow-stop-flow-response-example
- key_count: 1
  name: Appflow Tag Resource Request Example
  slug: appflow-tag-resource-request-example
- key_count: 5
  name: Appflow Task Example
  slug: appflow-task-example
- key_count: 2
  name: Appflow Trigger Config Example
  slug: appflow-trigger-config-example
- key_count: 2
  name: Appflow Unregister Connector Request Example
  slug: appflow-unregister-connector-request-example
- key_count: 4
  name: Appflow Update Connector Profile Request Example
  slug: appflow-update-connector-profile-request-example
- key_count: 1
  name: Appflow Update Connector Profile Response Example
  slug: appflow-update-connector-profile-response-example
- key_count: 4
  name: Appflow Update Connector Registration Request Example
  slug: appflow-update-connector-registration-request-example
- key_count: 1
  name: Appflow Update Connector Registration Response Example
  slug: appflow-update-connector-registration-response-example
- key_count: 8
  name: Appflow Update Flow Request Example
  slug: appflow-update-flow-request-example
- key_count: 1
  name: Appflow Update Flow Response Example
  slug: appflow-update-flow-response-example
features:
- description: Create data flows between SaaS applications and AWS services without writing code.
  name: No-Code Data Flows
- description: Schedule data flows to run at configurable intervals using cron or rate expressions.
  name: Scheduled Transfers
- description: Trigger data flows in response to business events from connected SaaS applications.
  name: Event-Triggered Flows
- description: Manually trigger data flows for ad-hoc data transfers.
  name: On-Demand Execution
- description: Apply field mapping, filtering, masking, merging, and arithmetic transformations during transfer.
  name: Data Transformations
- description: Transfer only new or changed records since the last flow run using datetime-based incremental pulls.
  name: Incremental Data Pull
- description: Register custom Lambda-backed connectors for proprietary or unsupported data sources.
  name: Custom Connectors
- description: Automatically catalog transferred data in AWS Glue Data Catalog for discoverability.
  name: Data Catalog Integration
- description: Encrypt data in transit and at rest using AWS KMS customer-managed keys.
  name: KMS Encryption
- description: Transfer data privately over AWS PrivateLink without traversing the public internet.
  name: Private Link Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-appflow.png
integrations:
- description: Bidirectional data transfer between Salesforce CRM and AWS services.
  name: Salesforce
- description: Transfer data from SAP ERP systems via SAPOData connector.
  name: SAP
- description: Sync ServiceNow ITSM data to AWS for analytics and reporting.
  name: ServiceNow
- description: Export Slack workspace data to Amazon S3.
  name: Slack
- description: Transfer Zendesk customer support tickets and data to AWS.
  name: Zendesk
- description: Import Marketo marketing automation data into Amazon Redshift or S3.
  name: Marketo
- description: Export Google Analytics data to Amazon S3 for custom analytics pipelines.
  name: Google Analytics
- description: Use Amazon S3 as both source and destination for AppFlow data flows.
  name: Amazon S3
- description: Load SaaS data directly into Amazon Redshift for SQL analytics.
  name: Amazon Redshift
- description: Send AppFlow data to Amazon EventBridge for event-driven architectures.
  name: Amazon EventBridge
- description: Catalog AppFlow output data automatically in AWS Glue Data Catalog.
  name: AWS Glue
- description: Feed SaaS data into SageMaker Data Wrangler for ML preparation.
  name: Amazon SageMaker
json_schemas:
- name: Amazon AppFlow Flow Definition
  property_count: 11
  slug: amazon-appflow
- name: CancelFlowExecutionsRequest
  property_count: 2
  slug: appflow-cancel-flow-executions-request
- name: CancelFlowExecutionsResponse
  property_count: 1
  slug: appflow-cancel-flow-executions-response
- name: ConnectorDetail
  property_count: 12
  slug: appflow-connector-detail
- name: ConnectorEntityField
  property_count: 10
  slug: appflow-connector-entity-field
- name: ConnectorEntity
  property_count: 3
  slug: appflow-connector-entity
- name: ConnectorProfile
  property_count: 10
  slug: appflow-connector-profile
- name: CreateConnectorProfileRequest
  property_count: 7
  slug: appflow-create-connector-profile-request
- name: CreateConnectorProfileResponse
  property_count: 1
  slug: appflow-create-connector-profile-response
- name: CreateFlowRequest
  property_count: 10
  slug: appflow-create-flow-request
- name: CreateFlowResponse
  property_count: 2
  slug: appflow-create-flow-response
- name: DeleteConnectorProfileRequest
  property_count: 2
  slug: appflow-delete-connector-profile-request
- name: DeleteFlowRequest
  property_count: 2
  slug: appflow-delete-flow-request
- name: DescribeConnectorEntityRequest
  property_count: 4
  slug: appflow-describe-connector-entity-request
- name: DescribeConnectorEntityResponse
  property_count: 1
  slug: appflow-describe-connector-entity-response
- name: DescribeConnectorProfilesRequest
  property_count: 5
  slug: appflow-describe-connector-profiles-request
- name: DescribeConnectorProfilesResponse
  property_count: 2
  slug: appflow-describe-connector-profiles-response
- name: DescribeConnectorRequest
  property_count: 2
  slug: appflow-describe-connector-request
- name: DescribeConnectorResponse
  property_count: 1
  slug: appflow-describe-connector-response
- name: DescribeConnectorsRequest
  property_count: 3
  slug: appflow-describe-connectors-request
- name: DescribeConnectorsResponse
  property_count: 3
  slug: appflow-describe-connectors-response
- name: DescribeFlowExecutionRecordsRequest
  property_count: 3
  slug: appflow-describe-flow-execution-records-request
- name: DescribeFlowExecutionRecordsResponse
  property_count: 2
  slug: appflow-describe-flow-execution-records-response
- name: DescribeFlowRequest
  property_count: 1
  slug: appflow-describe-flow-request
- name: DescribeFlowResponse
  property_count: 18
  slug: appflow-describe-flow-response
- name: DestinationFlowConfig
  property_count: 4
  slug: appflow-destination-flow-config
- name: ExecutionDetails
  property_count: 3
  slug: appflow-execution-details
- name: ExecutionResult
  property_count: 5
  slug: appflow-execution-result
- name: FlowDefinition
  property_count: 15
  slug: appflow-flow-definition
- name: FlowExecution
  property_count: 7
  slug: appflow-flow-execution
- name: ListConnectorEntitiesRequest
  property_count: 6
  slug: appflow-list-connector-entities-request
- name: ListConnectorEntitiesResponse
  property_count: 2
  slug: appflow-list-connector-entities-response
- name: ListConnectorsRequest
  property_count: 2
  slug: appflow-list-connectors-request
- name: ListConnectorsResponse
  property_count: 2
  slug: appflow-list-connectors-response
- name: ListFlowsRequest
  property_count: 2
  slug: appflow-list-flows-request
- name: ListFlowsResponse
  property_count: 2
  slug: appflow-list-flows-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: appflow-list-tags-for-resource-response
- name: MetadataCatalogConfig
  property_count: 1
  slug: appflow-metadata-catalog-config
- name: RegisterConnectorRequest
  property_count: 5
  slug: appflow-register-connector-request
- name: RegisterConnectorResponse
  property_count: 1
  slug: appflow-register-connector-response
- name: ResetConnectorMetadataCacheRequest
  property_count: 5
  slug: appflow-reset-connector-metadata-cache-request
- name: ScheduledTriggerProperties
  property_count: 8
  slug: appflow-scheduled-trigger-properties
- name: SourceFlowConfig
  property_count: 5
  slug: appflow-source-flow-config
- name: StartFlowRequest
  property_count: 2
  slug: appflow-start-flow-request
- name: StartFlowResponse
  property_count: 3
  slug: appflow-start-flow-response
- name: StopFlowRequest
  property_count: 1
  slug: appflow-stop-flow-request
- name: StopFlowResponse
  property_count: 2
  slug: appflow-stop-flow-response
- name: TagResourceRequest
  property_count: 1
  slug: appflow-tag-resource-request
- name: Task
  property_count: 5
  slug: appflow-task
- name: TriggerConfig
  property_count: 2
  slug: appflow-trigger-config
- name: UnregisterConnectorRequest
  property_count: 2
  slug: appflow-unregister-connector-request
- name: UpdateConnectorProfileRequest
  property_count: 4
  slug: appflow-update-connector-profile-request
- name: UpdateConnectorProfileResponse
  property_count: 1
  slug: appflow-update-connector-profile-response
- name: UpdateConnectorRegistrationRequest
  property_count: 4
  slug: appflow-update-connector-registration-request
- name: UpdateConnectorRegistrationResponse
  property_count: 1
  slug: appflow-update-connector-registration-response
- name: UpdateFlowRequest
  property_count: 8
  slug: appflow-update-flow-request
- name: UpdateFlowResponse
  property_count: 1
  slug: appflow-update-flow-response
json_structures:
- name: Amazon Appflow Structure
  property_count: 11
  slug: amazon-appflow-structure
- name: Appflow Cancel Flow Executions Request Structure
  property_count: 2
  slug: appflow-cancel-flow-executions-request-structure
- name: Appflow Cancel Flow Executions Response Structure
  property_count: 1
  slug: appflow-cancel-flow-executions-response-structure
- name: Appflow Connector Detail Structure
  property_count: 12
  slug: appflow-connector-detail-structure
- name: Appflow Connector Entity Field Structure
  property_count: 10
  slug: appflow-connector-entity-field-structure
- name: Appflow Connector Entity Structure
  property_count: 3
  slug: appflow-connector-entity-structure
- name: Appflow Connector Profile Structure
  property_count: 10
  slug: appflow-connector-profile-structure
- name: Appflow Create Connector Profile Request Structure
  property_count: 7
  slug: appflow-create-connector-profile-request-structure
- name: Appflow Create Connector Profile Response Structure
  property_count: 1
  slug: appflow-create-connector-profile-response-structure
- name: Appflow Create Flow Request Structure
  property_count: 10
  slug: appflow-create-flow-request-structure
- name: Appflow Create Flow Response Structure
  property_count: 2
  slug: appflow-create-flow-response-structure
- name: Appflow Delete Connector Profile Request Structure
  property_count: 2
  slug: appflow-delete-connector-profile-request-structure
- name: Appflow Delete Flow Request Structure
  property_count: 2
  slug: appflow-delete-flow-request-structure
- name: Appflow Describe Connector Entity Request Structure
  property_count: 4
  slug: appflow-describe-connector-entity-request-structure
- name: Appflow Describe Connector Entity Response Structure
  property_count: 1
  slug: appflow-describe-connector-entity-response-structure
- name: Appflow Describe Connector Profiles Request Structure
  property_count: 5
  slug: appflow-describe-connector-profiles-request-structure
- name: Appflow Describe Connector Profiles Response Structure
  property_count: 2
  slug: appflow-describe-connector-profiles-response-structure
- name: Appflow Describe Connector Request Structure
  property_count: 2
  slug: appflow-describe-connector-request-structure
- name: Appflow Describe Connector Response Structure
  property_count: 1
  slug: appflow-describe-connector-response-structure
- name: Appflow Describe Connectors Request Structure
  property_count: 3
  slug: appflow-describe-connectors-request-structure
- name: Appflow Describe Connectors Response Structure
  property_count: 3
  slug: appflow-describe-connectors-response-structure
- name: Appflow Describe Flow Execution Records Request Structure
  property_count: 3
  slug: appflow-describe-flow-execution-records-request-structure
- name: Appflow Describe Flow Execution Records Response Structure
  property_count: 2
  slug: appflow-describe-flow-execution-records-response-structure
- name: Appflow Describe Flow Request Structure
  property_count: 1
  slug: appflow-describe-flow-request-structure
- name: Appflow Describe Flow Response Structure
  property_count: 18
  slug: appflow-describe-flow-response-structure
- name: Appflow Destination Flow Config Structure
  property_count: 4
  slug: appflow-destination-flow-config-structure
- name: Appflow Execution Details Structure
  property_count: 3
  slug: appflow-execution-details-structure
- name: Appflow Execution Result Structure
  property_count: 5
  slug: appflow-execution-result-structure
- name: Appflow Flow Definition Structure
  property_count: 15
  slug: appflow-flow-definition-structure
- name: Appflow Flow Execution Structure
  property_count: 7
  slug: appflow-flow-execution-structure
- name: Appflow List Connector Entities Request Structure
  property_count: 6
  slug: appflow-list-connector-entities-request-structure
- name: Appflow List Connector Entities Response Structure
  property_count: 2
  slug: appflow-list-connector-entities-response-structure
- name: Appflow List Connectors Request Structure
  property_count: 2
  slug: appflow-list-connectors-request-structure
- name: Appflow List Connectors Response Structure
  property_count: 2
  slug: appflow-list-connectors-response-structure
- name: Appflow List Flows Request Structure
  property_count: 2
  slug: appflow-list-flows-request-structure
- name: Appflow List Flows Response Structure
  property_count: 2
  slug: appflow-list-flows-response-structure
- name: Appflow List Tags For Resource Response Structure
  property_count: 1
  slug: appflow-list-tags-for-resource-response-structure
- name: Appflow Metadata Catalog Config Structure
  property_count: 1
  slug: appflow-metadata-catalog-config-structure
- name: Appflow Register Connector Request Structure
  property_count: 5
  slug: appflow-register-connector-request-structure
- name: Appflow Register Connector Response Structure
  property_count: 1
  slug: appflow-register-connector-response-structure
- name: Appflow Reset Connector Metadata Cache Request Structure
  property_count: 5
  slug: appflow-reset-connector-metadata-cache-request-structure
- name: Appflow Scheduled Trigger Properties Structure
  property_count: 8
  slug: appflow-scheduled-trigger-properties-structure
- name: Appflow Source Flow Config Structure
  property_count: 5
  slug: appflow-source-flow-config-structure
- name: Appflow Start Flow Request Structure
  property_count: 2
  slug: appflow-start-flow-request-structure
- name: Appflow Start Flow Response Structure
  property_count: 3
  slug: appflow-start-flow-response-structure
- name: Appflow Stop Flow Request Structure
  property_count: 1
  slug: appflow-stop-flow-request-structure
- name: Appflow Stop Flow Response Structure
  property_count: 2
  slug: appflow-stop-flow-response-structure
- name: Appflow Tag Resource Request Structure
  property_count: 1
  slug: appflow-tag-resource-request-structure
- name: Appflow Task Structure
  property_count: 5
  slug: appflow-task-structure
- name: Appflow Trigger Config Structure
  property_count: 2
  slug: appflow-trigger-config-structure
- name: Appflow Unregister Connector Request Structure
  property_count: 2
  slug: appflow-unregister-connector-request-structure
- name: Appflow Update Connector Profile Request Structure
  property_count: 4
  slug: appflow-update-connector-profile-request-structure
- name: Appflow Update Connector Profile Response Structure
  property_count: 1
  slug: appflow-update-connector-profile-response-structure
- name: Appflow Update Connector Registration Request Structure
  property_count: 4
  slug: appflow-update-connector-registration-request-structure
- name: Appflow Update Connector Registration Response Structure
  property_count: 1
  slug: appflow-update-connector-registration-response-structure
- name: Appflow Update Flow Request Structure
  property_count: 8
  slug: appflow-update-flow-request-structure
- name: Appflow Update Flow Response Structure
  property_count: 1
  slug: appflow-update-flow-response-structure
jsonld:
- class_count: 61
  name: Amazon Appflow Context
  property_count: 120
  slug: amazon-appflow-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-appflow-mcp.yml
  slug: amazon-appflow-mcpyml
modified: '2026-06-20'
name: Amazon AppFlow
nav: Providers
network: true
overview: 'Amazon AppFlow publishes 3 APIs on the [APIs.io](https://apis.io/) network: Connectors API, Flows API, and Tags API. Tagged areas include Connectors, Data Flow, Data Integration, ETL, and Integration.


  The Amazon AppFlow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon AppFlow''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 27 more developer resources.'
random_paper: 96
rules:
- name: Amazon AppFlow API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-appflow-jsonschema-spectral-rules
- name: Amazon AppFlow API Rules
  rule_count: 41
  severity_counts:
    error: 17
    hint: 0
    info: 3
    warn: 21
  slug: amazon-appflow-spectral-rules
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 33.3
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 80.2
    operational_transparency: 31.6
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-appflow/refs/heads/main/screenshots/amazon-appflow-2026-07-25T195916.png
security:
- kind: authentication
  name: Amazon Appflow Authentication
  slug: amazon-appflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Appflow Domain Security
  slug: amazon-appflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Appflow Vulnerability Disclosure
  slug: amazon-appflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-appflow
tags:
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
use_cases:
- description: Consolidate marketing, sales, and support data from Salesforce, Marketo, and ServiceNow into Amazon Redshift or S3 for unified customer analytics.
  name: Customer 360
- description: Ingest SaaS data into Amazon SageMaker Data Wrangler for machine learning feature engineering and model training.
  name: ML Data Preparation
- description: Load SaaS application data into Amazon S3 data lakes for centralized analytics and reporting.
  name: Data Lake Ingestion
- description: Transfer Salesforce data in near real-time to Amazon Redshift for operational dashboards and BI reporting.
  name: Real-Time Analytics
- description: Automate workflows by triggering data flows when records are created or updated in SaaS applications.
  name: Cross-Application Automation
- description: Securely extract and archive regulated data from SaaS applications into encrypted AWS storage for compliance auditing.
  name: Data Compliance
website: https://aws.amazon.com/appflow/
---
