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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 43
  human_in_the_loop: 1
  name: Amazon Application Migration Service Agentic Access
  operation_count: 45
  slug: amazon-application-migration-service-agentic-access
  summary_line: 45 operations · 43 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Application groupings for migration
  name: Amazon Application Migration Service Applications API
  slug: amazon-application-migration-service-applications-api
- description: Source server export tasks
  name: Amazon Application Migration Service Exports API
  slug: amazon-application-migration-service-exports-api
- description: Migration and conversion jobs
  name: Amazon Application Migration Service Jobs API
  slug: amazon-application-migration-service-jobs-api
- description: Launch configuration and templates
  name: Amazon Application Migration Service Launch API
  slug: amazon-application-migration-service-launch-api
- description: Lifecycle action hooks for automated workflows
  name: Amazon Application Migration Service Lifecycle Hooks API
  slug: amazon-application-migration-service-lifecycle-hooks-api
- description: Replication configuration and templates
  name: Amazon Application Migration Service Replication API
  slug: amazon-application-migration-service-replication-api
- description: Manage source servers being migrated
  name: Amazon Application Migration Service Source Servers API
  slug: amazon-application-migration-service-source-servers-api
- description: Resource tagging operations
  name: Amazon Application Migration Service Tags API
  slug: amazon-application-migration-service-tags-api
- description: VMware vCenter client management
  name: Amazon Application Migration Service Vcenter Clients API
  slug: amazon-application-migration-service-vcenter-clients-api
- description: Wave-based migration orchestration
  name: Amazon Application Migration Service Waves API
  slug: amazon-application-migration-service-waves-api
artifact_total: 355
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Application Migration Service Applications API
  slug: open-amazon-application-migration-service-applications-api
- collection_type: open
  name: Amazon Application Migration Service Applications Exports API
  slug: open-amazon-application-migration-service-exports-api
- collection_type: open
  name: Amazon Application Migration Service Applications Jobs API
  slug: open-amazon-application-migration-service-jobs-api
- collection_type: open
  name: Amazon Application Migration Service Applications Launch API
  slug: open-amazon-application-migration-service-launch-api
- collection_type: open
  name: Amazon Application Migration Service Applications Lifecycle Hooks API
  slug: open-amazon-application-migration-service-lifecycle-hooks-api
- collection_type: open
  name: Amazon Application Migration Service Applications Replication API
  slug: open-amazon-application-migration-service-replication-api
- collection_type: open
  name: Amazon Application Migration Service Applications Source Servers API
  slug: open-amazon-application-migration-service-source-servers-api
- collection_type: open
  name: Amazon Application Migration Service Applications Tags API
  slug: open-amazon-application-migration-service-tags-api
- collection_type: open
  name: Amazon Application Migration Service Applications Vcenter Clients API
  slug: open-amazon-application-migration-service-vcenter-clients-api
- collection_type: open
  name: Amazon Application Migration Service Applications Waves API
  slug: open-amazon-application-migration-service-waves-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-application-migration-service-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-application-migration-service-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-application-migration-service-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-application-migration-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-application-migration-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-application-migration-service-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-application-migration-service-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-application-migration-service-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-application-migration-service-llms.txt
created: '2026-03-16'
description: AWS Application Migration Service (MGN) is the primary migration service recommended for lift-and-shift migrations to AWS. It allows organizations to quickly realize the benefits of migrating applications to the cloud without changes and with minimal downtime.
examples:
- key_count: 4
  name: Application Migration Service Application Aggregated Status Example
  slug: application-migration-service-application-aggregated-status-example
- key_count: 10
  name: Application Migration Service Application Example
  slug: application-migration-service-application-example
- key_count: 2
  name: Application Migration Service Archive Application Request Example
  slug: application-migration-service-archive-application-request-example
- key_count: 3
  name: Application Migration Service Associate Applications Request Example
  slug: application-migration-service-associate-applications-request-example
- key_count: 3
  name: Application Migration Service Associate Source Servers Request Example
  slug: application-migration-service-associate-source-servers-request-example
- key_count: 2
  name: Application Migration Service Cpu Example
  slug: application-migration-service-cpu-example
- key_count: 4
  name: Application Migration Service Create Application Request Example
  slug: application-migration-service-create-application-request-example
- key_count: 6
  name: Application Migration Service Create Launch Configuration Template Request Example
  slug: application-migration-service-create-launch-configuration-template-request-example
- key_count: 12
  name: Application Migration Service Create Replication Configuration Template Request Example
  slug: application-migration-service-create-replication-configuration-template-request-example
- key_count: 4
  name: Application Migration Service Create Wave Request Example
  slug: application-migration-service-create-wave-request-example
- key_count: 2
  name: Application Migration Service Data Replication Error Example
  slug: application-migration-service-data-replication-error-example
- key_count: 7
  name: Application Migration Service Data Replication Info Example
  slug: application-migration-service-data-replication-info-example
- key_count: 5
  name: Application Migration Service Data Replication Info Replicated Disk Example
  slug: application-migration-service-data-replication-info-replicated-disk-example
- key_count: 3
  name: Application Migration Service Data Replication Initiation Example
  slug: application-migration-service-data-replication-initiation-example
- key_count: 2
  name: Application Migration Service Data Replication Initiation Step Example
  slug: application-migration-service-data-replication-initiation-step-example
- key_count: 2
  name: Application Migration Service Delete Application Request Example
  slug: application-migration-service-delete-application-request-example
- key_count: 1
  name: Application Migration Service Delete Launch Configuration Template Request Example
  slug: application-migration-service-delete-launch-configuration-template-request-example
- key_count: 1
  name: Application Migration Service Delete Replication Configuration Template Request Example
  slug: application-migration-service-delete-replication-configuration-template-request-example
- key_count: 2
  name: Application Migration Service Delete Source Server Request Example
  slug: application-migration-service-delete-source-server-request-example
- key_count: 2
  name: Application Migration Service Delete Wave Request Example
  slug: application-migration-service-delete-wave-request-example
- key_count: 4
  name: Application Migration Service Describe Job Log Items Request Example
  slug: application-migration-service-describe-job-log-items-request-example
- key_count: 2
  name: Application Migration Service Describe Job Log Items Response Example
  slug: application-migration-service-describe-job-log-items-response-example
- key_count: 4
  name: Application Migration Service Describe Jobs Request Example
  slug: application-migration-service-describe-jobs-request-example
- key_count: 3
  name: Application Migration Service Describe Jobs Request Filters Example
  slug: application-migration-service-describe-jobs-request-filters-example
- key_count: 2
  name: Application Migration Service Describe Jobs Response Example
  slug: application-migration-service-describe-jobs-response-example
- key_count: 3
  name: Application Migration Service Describe Launch Configuration Templates Request Example
  slug: application-migration-service-describe-launch-configuration-templates-request-example
- key_count: 2
  name: Application Migration Service Describe Launch Configuration Templates Response Example
  slug: application-migration-service-describe-launch-configuration-templates-response-example
- key_count: 3
  name: Application Migration Service Describe Replication Configuration Templates Request Example
  slug: application-migration-service-describe-replication-configuration-templates-request-example
- key_count: 2
  name: Application Migration Service Describe Replication Configuration Templates Response Example
  slug: application-migration-service-describe-replication-configuration-templates-response-example
- key_count: 4
  name: Application Migration Service Describe Source Servers Request Example
  slug: application-migration-service-describe-source-servers-request-example
- key_count: 5
  name: Application Migration Service Describe Source Servers Request Filters Example
  slug: application-migration-service-describe-source-servers-request-filters-example
- key_count: 2
  name: Application Migration Service Describe Source Servers Response Example
  slug: application-migration-service-describe-source-servers-response-example
- key_count: 2
  name: Application Migration Service Describe Vcenter Clients Response Example
  slug: application-migration-service-describe-vcenter-clients-response-example
- key_count: 3
  name: Application Migration Service Disassociate Source Servers Request Example
  slug: application-migration-service-disassociate-source-servers-request-example
- key_count: 2
  name: Application Migration Service Disconnect From Service Request Example
  slug: application-migration-service-disconnect-from-service-request-example
- key_count: 2
  name: Application Migration Service Disk Example
  slug: application-migration-service-disk-example
- key_count: 2
  name: Application Migration Service Error Response Example
  slug: application-migration-service-error-response-example
- key_count: 3
  name: Application Migration Service Export Errors Request Example
  slug: application-migration-service-export-errors-request-example
- key_count: 2
  name: Application Migration Service Export Errors Response Example
  slug: application-migration-service-export-errors-response-example
- key_count: 1
  name: Application Migration Service Export Task Error Data Example
  slug: application-migration-service-export-task-error-data-example
- key_count: 2
  name: Application Migration Service Export Task Error Example
  slug: application-migration-service-export-task-error-example
- key_count: 2
  name: Application Migration Service Finalize Cutover Request Example
  slug: application-migration-service-finalize-cutover-request-example
- key_count: 2
  name: Application Migration Service Get Launch Configuration Request Example
  slug: application-migration-service-get-launch-configuration-request-example
- key_count: 2
  name: Application Migration Service Get Replication Configuration Request Example
  slug: application-migration-service-get-replication-configuration-request-example
- key_count: 5
  name: Application Migration Service Identification Hints Example
  slug: application-migration-service-identification-hints-example
- key_count: 9
  name: Application Migration Service Job Example
  slug: application-migration-service-job-example
- key_count: 4
  name: Application Migration Service Job Log Event Data Example
  slug: application-migration-service-job-log-event-data-example
- key_count: 3
  name: Application Migration Service Job Log Item Example
  slug: application-migration-service-job-log-item-example
- key_count: 12
  name: Application Migration Service Launch Configuration Example
  slug: application-migration-service-launch-configuration-example
- key_count: 9
  name: Application Migration Service Launch Configuration Template Example
  slug: application-migration-service-launch-configuration-template-example
- key_count: 3
  name: Application Migration Service Launched Instance Example
  slug: application-migration-service-launched-instance-example
- key_count: 1
  name: Application Migration Service Licensing Example
  slug: application-migration-service-licensing-example
- key_count: 11
  name: Application Migration Service Life Cycle Example
  slug: application-migration-service-life-cycle-example
- key_count: 4
  name: Application Migration Service Life Cycle Last Cutover Example
  slug: application-migration-service-life-cycle-last-cutover-example
- key_count: 4
  name: Application Migration Service Life Cycle Last Test Example
  slug: application-migration-service-life-cycle-last-test-example
- key_count: 4
  name: Application Migration Service List Applications Request Example
  slug: application-migration-service-list-applications-request-example
- key_count: 3
  name: Application Migration Service List Applications Request Filters Example
  slug: application-migration-service-list-applications-request-filters-example
- key_count: 2
  name: Application Migration Service List Applications Response Example
  slug: application-migration-service-list-applications-response-example
- key_count: 3
  name: Application Migration Service List Export Errors Request Example
  slug: application-migration-service-list-export-errors-request-example
- key_count: 2
  name: Application Migration Service List Export Errors Response Example
  slug: application-migration-service-list-export-errors-response-example
- key_count: 5
  name: Application Migration Service List Source Server Actions Request Example
  slug: application-migration-service-list-source-server-actions-request-example
- key_count: 2
  name: Application Migration Service List Source Server Actions Response Example
  slug: application-migration-service-list-source-server-actions-response-example
- key_count: 1
  name: Application Migration Service List Tags For Resource Response Example
  slug: application-migration-service-list-tags-for-resource-response-example
- key_count: 4
  name: Application Migration Service List Template Actions Request Example
  slug: application-migration-service-list-template-actions-request-example
- key_count: 2
  name: Application Migration Service List Template Actions Response Example
  slug: application-migration-service-list-template-actions-response-example
- key_count: 4
  name: Application Migration Service List Waves Request Example
  slug: application-migration-service-list-waves-request-example
- key_count: 2
  name: Application Migration Service List Waves Request Filters Example
  slug: application-migration-service-list-waves-request-filters-example
- key_count: 2
  name: Application Migration Service List Waves Response Example
  slug: application-migration-service-list-waves-response-example
- key_count: 2
  name: Application Migration Service Mark As Archived Request Example
  slug: application-migration-service-mark-as-archived-request-example
- key_count: 3
  name: Application Migration Service Network Interface Example
  slug: application-migration-service-network-interface-example
- key_count: 1
  name: Application Migration Service Os Example
  slug: application-migration-service-os-example
- key_count: 4
  name: Application Migration Service Participating Server Example
  slug: application-migration-service-participating-server-example
- key_count: 5
  name: Application Migration Service Post Launch Actions Example
  slug: application-migration-service-post-launch-actions-example
- key_count: 2
  name: Application Migration Service Post Launch Actions Status Example
  slug: application-migration-service-post-launch-actions-status-example
- key_count: 15
  name: Application Migration Service Replication Configuration Example
  slug: application-migration-service-replication-configuration-example
- key_count: 6
  name: Application Migration Service Replication Configuration Replicated Disk Example
  slug: application-migration-service-replication-configuration-replicated-disk-example
- key_count: 14
  name: Application Migration Service Replication Configuration Template Example
  slug: application-migration-service-replication-configuration-template-example
- key_count: 2
  name: Application Migration Service Retry Data Replication Request Example
  slug: application-migration-service-retry-data-replication-request-example
- key_count: 8
  name: Application Migration Service Source Properties Example
  slug: application-migration-service-source-properties-example
- key_count: 12
  name: Application Migration Service Source Server Action Example
  slug: application-migration-service-source-server-action-example
- key_count: 13
  name: Application Migration Service Source Server Example
  slug: application-migration-service-source-server-example
- key_count: 5
  name: Application Migration Service Ssm Document Example
  slug: application-migration-service-ssm-document-example
- key_count: 2
  name: Application Migration Service Ssm Parameter Store Parameter Example
  slug: application-migration-service-ssm-parameter-store-parameter-example
- key_count: 3
  name: Application Migration Service Start Cutover Request Example
  slug: application-migration-service-start-cutover-request-example
- key_count: 1
  name: Application Migration Service Start Cutover Response Example
  slug: application-migration-service-start-cutover-response-example
- key_count: 3
  name: Application Migration Service Start Test Request Example
  slug: application-migration-service-start-test-request-example
- key_count: 1
  name: Application Migration Service Start Test Response Example
  slug: application-migration-service-start-test-response-example
- key_count: 1
  name: Application Migration Service Tag Resource Request Example
  slug: application-migration-service-tag-resource-request-example
- key_count: 3
  name: Application Migration Service Terminate Target Instances Request Example
  slug: application-migration-service-terminate-target-instances-request-example
- key_count: 1
  name: Application Migration Service Terminate Target Instances Response Example
  slug: application-migration-service-terminate-target-instances-response-example
- key_count: 2
  name: Application Migration Service Unarchive Application Request Example
  slug: application-migration-service-unarchive-application-request-example
- key_count: 4
  name: Application Migration Service Update Application Request Example
  slug: application-migration-service-update-application-request-example
- key_count: 8
  name: Application Migration Service Update Launch Configuration Request Example
  slug: application-migration-service-update-launch-configuration-request-example
- key_count: 5
  name: Application Migration Service Update Launch Configuration Template Request Example
  slug: application-migration-service-update-launch-configuration-template-request-example
- key_count: 9
  name: Application Migration Service Update Replication Configuration Request Example
  slug: application-migration-service-update-replication-configuration-request-example
- key_count: 7
  name: Application Migration Service Update Replication Configuration Template Request Example
  slug: application-migration-service-update-replication-configuration-template-request-example
- key_count: 4
  name: Application Migration Service Update Wave Request Example
  slug: application-migration-service-update-wave-request-example
- key_count: 8
  name: Application Migration Service Vcenter Client Example
  slug: application-migration-service-vcenter-client-example
- key_count: 4
  name: Application Migration Service Wave Aggregated Status Example
  slug: application-migration-service-wave-aggregated-status-example
- key_count: 9
  name: Application Migration Service Wave Example
  slug: application-migration-service-wave-example
features:
- Continuous block-level replication with near-zero RPO
- Automated lift-and-shift migration without application changes
- Test migration capability without impacting production servers
- Wave and application grouping for phased migration management
- Agentless migration via VMware vCenter connector
- Post-launch automation via AWS Systems Manager documents
- Right-sizing recommendations for target instance types
- Cross-account and cross-region migration support
- Integration with AWS Migration Hub for centralized tracking
- Automatic EC2 launch template creation for migrated servers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-application-migration-service.png
integrations:
- AWS Migration Hub
- Amazon EC2
- Amazon EBS
- AWS Systems Manager
- VMware vCenter
- AWS IAM
- Amazon CloudWatch
- AWS CloudTrail
- Amazon S3
- AWS KMS
json_schemas:
- name: ApplicationAggregatedStatus
  property_count: 4
  slug: application-migration-service-application-aggregated-status
- name: Application
  property_count: 10
  slug: application-migration-service-application
- name: ArchiveApplicationRequest
  property_count: 2
  slug: application-migration-service-archive-application-request
- name: AssociateApplicationsRequest
  property_count: 3
  slug: application-migration-service-associate-applications-request
- name: AssociateSourceServersRequest
  property_count: 3
  slug: application-migration-service-associate-source-servers-request
- name: CPU
  property_count: 2
  slug: application-migration-service-cpu
- name: CreateApplicationRequest
  property_count: 4
  slug: application-migration-service-create-application-request
- name: CreateLaunchConfigurationTemplateRequest
  property_count: 6
  slug: application-migration-service-create-launch-configuration-template-request
- name: CreateReplicationConfigurationTemplateRequest
  property_count: 12
  slug: application-migration-service-create-replication-configuration-template-request
- name: CreateWaveRequest
  property_count: 4
  slug: application-migration-service-create-wave-request
- name: DataReplicationError
  property_count: 2
  slug: application-migration-service-data-replication-error
- name: DataReplicationInfoReplicatedDisk
  property_count: 5
  slug: application-migration-service-data-replication-info-replicated-disk
- name: DataReplicationInfo
  property_count: 7
  slug: application-migration-service-data-replication-info
- name: DataReplicationInitiation
  property_count: 3
  slug: application-migration-service-data-replication-initiation
- name: DataReplicationInitiationStep
  property_count: 2
  slug: application-migration-service-data-replication-initiation-step
- name: DeleteApplicationRequest
  property_count: 2
  slug: application-migration-service-delete-application-request
- name: DeleteLaunchConfigurationTemplateRequest
  property_count: 1
  slug: application-migration-service-delete-launch-configuration-template-request
- name: DeleteReplicationConfigurationTemplateRequest
  property_count: 1
  slug: application-migration-service-delete-replication-configuration-template-request
- name: DeleteSourceServerRequest
  property_count: 2
  slug: application-migration-service-delete-source-server-request
- name: DeleteWaveRequest
  property_count: 2
  slug: application-migration-service-delete-wave-request
- name: DescribeJobLogItemsRequest
  property_count: 4
  slug: application-migration-service-describe-job-log-items-request
- name: DescribeJobLogItemsResponse
  property_count: 2
  slug: application-migration-service-describe-job-log-items-response
- name: DescribeJobsRequestFilters
  property_count: 3
  slug: application-migration-service-describe-jobs-request-filters
- name: DescribeJobsRequest
  property_count: 4
  slug: application-migration-service-describe-jobs-request
- name: DescribeJobsResponse
  property_count: 2
  slug: application-migration-service-describe-jobs-response
- name: DescribeLaunchConfigurationTemplatesRequest
  property_count: 3
  slug: application-migration-service-describe-launch-configuration-templates-request
- name: DescribeLaunchConfigurationTemplatesResponse
  property_count: 2
  slug: application-migration-service-describe-launch-configuration-templates-response
- name: DescribeReplicationConfigurationTemplatesRequest
  property_count: 3
  slug: application-migration-service-describe-replication-configuration-templates-request
- name: DescribeReplicationConfigurationTemplatesResponse
  property_count: 2
  slug: application-migration-service-describe-replication-configuration-templates-response
- name: DescribeSourceServersRequestFilters
  property_count: 5
  slug: application-migration-service-describe-source-servers-request-filters
- name: DescribeSourceServersRequest
  property_count: 4
  slug: application-migration-service-describe-source-servers-request
- name: DescribeSourceServersResponse
  property_count: 2
  slug: application-migration-service-describe-source-servers-response
- name: DescribeVcenterClientsResponse
  property_count: 2
  slug: application-migration-service-describe-vcenter-clients-response
- name: DisassociateSourceServersRequest
  property_count: 3
  slug: application-migration-service-disassociate-source-servers-request
- name: DisconnectFromServiceRequest
  property_count: 2
  slug: application-migration-service-disconnect-from-service-request
- name: Disk
  property_count: 2
  slug: application-migration-service-disk
- name: ErrorResponse
  property_count: 2
  slug: application-migration-service-error-response
- name: ExportErrorsRequest
  property_count: 3
  slug: application-migration-service-export-errors-request
- name: ExportErrorsResponse
  property_count: 2
  slug: application-migration-service-export-errors-response
- name: ExportTaskErrorData
  property_count: 1
  slug: application-migration-service-export-task-error-data
- name: ExportTaskError
  property_count: 2
  slug: application-migration-service-export-task-error
- name: FinalizeCutoverRequest
  property_count: 2
  slug: application-migration-service-finalize-cutover-request
- name: GetLaunchConfigurationRequest
  property_count: 2
  slug: application-migration-service-get-launch-configuration-request
- name: GetReplicationConfigurationRequest
  property_count: 2
  slug: application-migration-service-get-replication-configuration-request
- name: IdentificationHints
  property_count: 5
  slug: application-migration-service-identification-hints
- name: JobLogEventData
  property_count: 4
  slug: application-migration-service-job-log-event-data
- name: JobLogItem
  property_count: 3
  slug: application-migration-service-job-log-item
- name: Job
  property_count: 9
  slug: application-migration-service-job
- name: LaunchConfiguration
  property_count: 12
  slug: application-migration-service-launch-configuration
- name: LaunchConfigurationTemplate
  property_count: 9
  slug: application-migration-service-launch-configuration-template
- name: LaunchedInstance
  property_count: 3
  slug: application-migration-service-launched-instance
- name: Licensing
  property_count: 1
  slug: application-migration-service-licensing
- name: LifeCycleLastCutover
  property_count: 4
  slug: application-migration-service-life-cycle-last-cutover
- name: LifeCycleLastTest
  property_count: 4
  slug: application-migration-service-life-cycle-last-test
- name: LifeCycle
  property_count: 11
  slug: application-migration-service-life-cycle
- name: ListApplicationsRequestFilters
  property_count: 3
  slug: application-migration-service-list-applications-request-filters
- name: ListApplicationsRequest
  property_count: 4
  slug: application-migration-service-list-applications-request
- name: ListApplicationsResponse
  property_count: 2
  slug: application-migration-service-list-applications-response
- name: ListExportErrorsRequest
  property_count: 3
  slug: application-migration-service-list-export-errors-request
- name: ListExportErrorsResponse
  property_count: 2
  slug: application-migration-service-list-export-errors-response
- name: ListSourceServerActionsRequest
  property_count: 5
  slug: application-migration-service-list-source-server-actions-request
- name: ListSourceServerActionsResponse
  property_count: 2
  slug: application-migration-service-list-source-server-actions-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: application-migration-service-list-tags-for-resource-response
- name: ListTemplateActionsRequest
  property_count: 4
  slug: application-migration-service-list-template-actions-request
- name: ListTemplateActionsResponse
  property_count: 2
  slug: application-migration-service-list-template-actions-response
- name: ListWavesRequestFilters
  property_count: 2
  slug: application-migration-service-list-waves-request-filters
- name: ListWavesRequest
  property_count: 4
  slug: application-migration-service-list-waves-request
- name: ListWavesResponse
  property_count: 2
  slug: application-migration-service-list-waves-response
- name: MarkAsArchivedRequest
  property_count: 2
  slug: application-migration-service-mark-as-archived-request
- name: NetworkInterface
  property_count: 3
  slug: application-migration-service-network-interface
- name: OS
  property_count: 1
  slug: application-migration-service-os
- name: ParticipatingServer
  property_count: 4
  slug: application-migration-service-participating-server
- name: PostLaunchActions
  property_count: 5
  slug: application-migration-service-post-launch-actions
- name: PostLaunchActionsStatus
  property_count: 2
  slug: application-migration-service-post-launch-actions-status
- name: ReplicationConfigurationReplicatedDisk
  property_count: 6
  slug: application-migration-service-replication-configuration-replicated-disk
- name: ReplicationConfiguration
  property_count: 15
  slug: application-migration-service-replication-configuration
- name: ReplicationConfigurationTemplate
  property_count: 14
  slug: application-migration-service-replication-configuration-template
- name: RetryDataReplicationRequest
  property_count: 2
  slug: application-migration-service-retry-data-replication-request
- name: SourceProperties
  property_count: 8
  slug: application-migration-service-source-properties
- name: SourceServerAction
  property_count: 12
  slug: application-migration-service-source-server-action
- name: SourceServer
  property_count: 13
  slug: application-migration-service-source-server
- name: SsmDocument
  property_count: 5
  slug: application-migration-service-ssm-document
- name: SsmParameterStoreParameter
  property_count: 2
  slug: application-migration-service-ssm-parameter-store-parameter
- name: StartCutoverRequest
  property_count: 3
  slug: application-migration-service-start-cutover-request
- name: StartCutoverResponse
  property_count: 1
  slug: application-migration-service-start-cutover-response
- name: StartTestRequest
  property_count: 3
  slug: application-migration-service-start-test-request
- name: StartTestResponse
  property_count: 1
  slug: application-migration-service-start-test-response
- name: TagResourceRequest
  property_count: 1
  slug: application-migration-service-tag-resource-request
- name: TerminateTargetInstancesRequest
  property_count: 3
  slug: application-migration-service-terminate-target-instances-request
- name: TerminateTargetInstancesResponse
  property_count: 1
  slug: application-migration-service-terminate-target-instances-response
- name: UnarchiveApplicationRequest
  property_count: 2
  slug: application-migration-service-unarchive-application-request
- name: UpdateApplicationRequest
  property_count: 4
  slug: application-migration-service-update-application-request
- name: UpdateLaunchConfigurationRequest
  property_count: 8
  slug: application-migration-service-update-launch-configuration-request
- name: UpdateLaunchConfigurationTemplateRequest
  property_count: 5
  slug: application-migration-service-update-launch-configuration-template-request
- name: UpdateReplicationConfigurationRequest
  property_count: 9
  slug: application-migration-service-update-replication-configuration-request
- name: UpdateReplicationConfigurationTemplateRequest
  property_count: 7
  slug: application-migration-service-update-replication-configuration-template-request
- name: UpdateWaveRequest
  property_count: 4
  slug: application-migration-service-update-wave-request
- name: VcenterClient
  property_count: 8
  slug: application-migration-service-vcenter-client
- name: WaveAggregatedStatus
  property_count: 4
  slug: application-migration-service-wave-aggregated-status
- name: Wave
  property_count: 9
  slug: application-migration-service-wave
json_structures:
- name: Application Migration Service Application Aggregated Status Structure
  property_count: 0
  slug: application-migration-service-application-aggregated-status-structure
- name: Application Migration Service Application Structure
  property_count: 0
  slug: application-migration-service-application-structure
- name: Application Migration Service Archive Application Request Structure
  property_count: 0
  slug: application-migration-service-archive-application-request-structure
- name: Application Migration Service Associate Applications Request Structure
  property_count: 0
  slug: application-migration-service-associate-applications-request-structure
- name: Application Migration Service Associate Source Servers Request Structure
  property_count: 0
  slug: application-migration-service-associate-source-servers-request-structure
- name: Application Migration Service Cpu Structure
  property_count: 0
  slug: application-migration-service-cpu-structure
- name: Application Migration Service Create Application Request Structure
  property_count: 0
  slug: application-migration-service-create-application-request-structure
- name: Application Migration Service Create Launch Configuration Template Request Structure
  property_count: 0
  slug: application-migration-service-create-launch-configuration-template-request-structure
- name: Application Migration Service Create Replication Configuration Template Request Structure
  property_count: 0
  slug: application-migration-service-create-replication-configuration-template-request-structure
- name: Application Migration Service Create Wave Request Structure
  property_count: 0
  slug: application-migration-service-create-wave-request-structure
- name: Application Migration Service Data Replication Error Structure
  property_count: 0
  slug: application-migration-service-data-replication-error-structure
- name: Application Migration Service Data Replication Info Replicated Disk Structure
  property_count: 0
  slug: application-migration-service-data-replication-info-replicated-disk-structure
- name: Application Migration Service Data Replication Info Structure
  property_count: 0
  slug: application-migration-service-data-replication-info-structure
- name: Application Migration Service Data Replication Initiation Step Structure
  property_count: 0
  slug: application-migration-service-data-replication-initiation-step-structure
- name: Application Migration Service Data Replication Initiation Structure
  property_count: 0
  slug: application-migration-service-data-replication-initiation-structure
- name: Application Migration Service Delete Application Request Structure
  property_count: 0
  slug: application-migration-service-delete-application-request-structure
- name: Application Migration Service Delete Launch Configuration Template Request Structure
  property_count: 0
  slug: application-migration-service-delete-launch-configuration-template-request-structure
- name: Application Migration Service Delete Replication Configuration Template Request Structure
  property_count: 0
  slug: application-migration-service-delete-replication-configuration-template-request-structure
- name: Application Migration Service Delete Source Server Request Structure
  property_count: 0
  slug: application-migration-service-delete-source-server-request-structure
- name: Application Migration Service Delete Wave Request Structure
  property_count: 0
  slug: application-migration-service-delete-wave-request-structure
- name: Application Migration Service Describe Job Log Items Request Structure
  property_count: 0
  slug: application-migration-service-describe-job-log-items-request-structure
- name: Application Migration Service Describe Job Log Items Response Structure
  property_count: 0
  slug: application-migration-service-describe-job-log-items-response-structure
- name: Application Migration Service Describe Jobs Request Filters Structure
  property_count: 0
  slug: application-migration-service-describe-jobs-request-filters-structure
- name: Application Migration Service Describe Jobs Request Structure
  property_count: 0
  slug: application-migration-service-describe-jobs-request-structure
- name: Application Migration Service Describe Jobs Response Structure
  property_count: 0
  slug: application-migration-service-describe-jobs-response-structure
- name: Application Migration Service Describe Launch Configuration Templates Request Structure
  property_count: 0
  slug: application-migration-service-describe-launch-configuration-templates-request-structure
- name: Application Migration Service Describe Launch Configuration Templates Response Structure
  property_count: 0
  slug: application-migration-service-describe-launch-configuration-templates-response-structure
- name: Application Migration Service Describe Replication Configuration Templates Request Structure
  property_count: 0
  slug: application-migration-service-describe-replication-configuration-templates-request-structure
- name: Application Migration Service Describe Replication Configuration Templates Response Structure
  property_count: 0
  slug: application-migration-service-describe-replication-configuration-templates-response-structure
- name: Application Migration Service Describe Source Servers Request Filters Structure
  property_count: 0
  slug: application-migration-service-describe-source-servers-request-filters-structure
- name: Application Migration Service Describe Source Servers Request Structure
  property_count: 0
  slug: application-migration-service-describe-source-servers-request-structure
- name: Application Migration Service Describe Source Servers Response Structure
  property_count: 0
  slug: application-migration-service-describe-source-servers-response-structure
- name: Application Migration Service Describe Vcenter Clients Response Structure
  property_count: 0
  slug: application-migration-service-describe-vcenter-clients-response-structure
- name: Application Migration Service Disassociate Source Servers Request Structure
  property_count: 0
  slug: application-migration-service-disassociate-source-servers-request-structure
- name: Application Migration Service Disconnect From Service Request Structure
  property_count: 0
  slug: application-migration-service-disconnect-from-service-request-structure
- name: Application Migration Service Disk Structure
  property_count: 0
  slug: application-migration-service-disk-structure
- name: Application Migration Service Error Response Structure
  property_count: 0
  slug: application-migration-service-error-response-structure
- name: Application Migration Service Export Errors Request Structure
  property_count: 0
  slug: application-migration-service-export-errors-request-structure
- name: Application Migration Service Export Errors Response Structure
  property_count: 0
  slug: application-migration-service-export-errors-response-structure
- name: Application Migration Service Export Task Error Data Structure
  property_count: 0
  slug: application-migration-service-export-task-error-data-structure
- name: Application Migration Service Export Task Error Structure
  property_count: 0
  slug: application-migration-service-export-task-error-structure
- name: Application Migration Service Finalize Cutover Request Structure
  property_count: 0
  slug: application-migration-service-finalize-cutover-request-structure
- name: Application Migration Service Get Launch Configuration Request Structure
  property_count: 0
  slug: application-migration-service-get-launch-configuration-request-structure
- name: Application Migration Service Get Replication Configuration Request Structure
  property_count: 0
  slug: application-migration-service-get-replication-configuration-request-structure
- name: Application Migration Service Identification Hints Structure
  property_count: 0
  slug: application-migration-service-identification-hints-structure
- name: Application Migration Service Job Log Event Data Structure
  property_count: 0
  slug: application-migration-service-job-log-event-data-structure
- name: Application Migration Service Job Log Item Structure
  property_count: 0
  slug: application-migration-service-job-log-item-structure
- name: Application Migration Service Job Structure
  property_count: 0
  slug: application-migration-service-job-structure
- name: Application Migration Service Launch Configuration Structure
  property_count: 0
  slug: application-migration-service-launch-configuration-structure
- name: Application Migration Service Launch Configuration Template Structure
  property_count: 0
  slug: application-migration-service-launch-configuration-template-structure
- name: Application Migration Service Launched Instance Structure
  property_count: 0
  slug: application-migration-service-launched-instance-structure
- name: Application Migration Service Licensing Structure
  property_count: 0
  slug: application-migration-service-licensing-structure
- name: Application Migration Service Life Cycle Last Cutover Structure
  property_count: 0
  slug: application-migration-service-life-cycle-last-cutover-structure
- name: Application Migration Service Life Cycle Last Test Structure
  property_count: 0
  slug: application-migration-service-life-cycle-last-test-structure
- name: Application Migration Service Life Cycle Structure
  property_count: 0
  slug: application-migration-service-life-cycle-structure
- name: Application Migration Service List Applications Request Filters Structure
  property_count: 0
  slug: application-migration-service-list-applications-request-filters-structure
- name: Application Migration Service List Applications Request Structure
  property_count: 0
  slug: application-migration-service-list-applications-request-structure
- name: Application Migration Service List Applications Response Structure
  property_count: 0
  slug: application-migration-service-list-applications-response-structure
- name: Application Migration Service List Export Errors Request Structure
  property_count: 0
  slug: application-migration-service-list-export-errors-request-structure
- name: Application Migration Service List Export Errors Response Structure
  property_count: 0
  slug: application-migration-service-list-export-errors-response-structure
- name: Application Migration Service List Source Server Actions Request Structure
  property_count: 0
  slug: application-migration-service-list-source-server-actions-request-structure
- name: Application Migration Service List Source Server Actions Response Structure
  property_count: 0
  slug: application-migration-service-list-source-server-actions-response-structure
- name: Application Migration Service List Tags For Resource Response Structure
  property_count: 0
  slug: application-migration-service-list-tags-for-resource-response-structure
- name: Application Migration Service List Template Actions Request Structure
  property_count: 0
  slug: application-migration-service-list-template-actions-request-structure
- name: Application Migration Service List Template Actions Response Structure
  property_count: 0
  slug: application-migration-service-list-template-actions-response-structure
- name: Application Migration Service List Waves Request Filters Structure
  property_count: 0
  slug: application-migration-service-list-waves-request-filters-structure
- name: Application Migration Service List Waves Request Structure
  property_count: 0
  slug: application-migration-service-list-waves-request-structure
- name: Application Migration Service List Waves Response Structure
  property_count: 0
  slug: application-migration-service-list-waves-response-structure
- name: Application Migration Service Mark As Archived Request Structure
  property_count: 0
  slug: application-migration-service-mark-as-archived-request-structure
- name: Application Migration Service Network Interface Structure
  property_count: 0
  slug: application-migration-service-network-interface-structure
- name: Application Migration Service Os Structure
  property_count: 0
  slug: application-migration-service-os-structure
- name: Application Migration Service Participating Server Structure
  property_count: 0
  slug: application-migration-service-participating-server-structure
- name: Application Migration Service Post Launch Actions Status Structure
  property_count: 0
  slug: application-migration-service-post-launch-actions-status-structure
- name: Application Migration Service Post Launch Actions Structure
  property_count: 0
  slug: application-migration-service-post-launch-actions-structure
- name: Application Migration Service Replication Configuration Replicated Disk Structure
  property_count: 0
  slug: application-migration-service-replication-configuration-replicated-disk-structure
- name: Application Migration Service Replication Configuration Structure
  property_count: 0
  slug: application-migration-service-replication-configuration-structure
- name: Application Migration Service Replication Configuration Template Structure
  property_count: 0
  slug: application-migration-service-replication-configuration-template-structure
- name: Application Migration Service Retry Data Replication Request Structure
  property_count: 0
  slug: application-migration-service-retry-data-replication-request-structure
- name: Application Migration Service Source Properties Structure
  property_count: 0
  slug: application-migration-service-source-properties-structure
- name: Application Migration Service Source Server Action Structure
  property_count: 0
  slug: application-migration-service-source-server-action-structure
- name: Application Migration Service Source Server Structure
  property_count: 0
  slug: application-migration-service-source-server-structure
- name: Application Migration Service Ssm Document Structure
  property_count: 0
  slug: application-migration-service-ssm-document-structure
- name: Application Migration Service Ssm Parameter Store Parameter Structure
  property_count: 0
  slug: application-migration-service-ssm-parameter-store-parameter-structure
- name: Application Migration Service Start Cutover Request Structure
  property_count: 0
  slug: application-migration-service-start-cutover-request-structure
- name: Application Migration Service Start Cutover Response Structure
  property_count: 0
  slug: application-migration-service-start-cutover-response-structure
- name: Application Migration Service Start Test Request Structure
  property_count: 0
  slug: application-migration-service-start-test-request-structure
- name: Application Migration Service Start Test Response Structure
  property_count: 0
  slug: application-migration-service-start-test-response-structure
- name: Application Migration Service Tag Resource Request Structure
  property_count: 0
  slug: application-migration-service-tag-resource-request-structure
- name: Application Migration Service Terminate Target Instances Request Structure
  property_count: 0
  slug: application-migration-service-terminate-target-instances-request-structure
- name: Application Migration Service Terminate Target Instances Response Structure
  property_count: 0
  slug: application-migration-service-terminate-target-instances-response-structure
- name: Application Migration Service Unarchive Application Request Structure
  property_count: 0
  slug: application-migration-service-unarchive-application-request-structure
- name: Application Migration Service Update Application Request Structure
  property_count: 0
  slug: application-migration-service-update-application-request-structure
- name: Application Migration Service Update Launch Configuration Request Structure
  property_count: 0
  slug: application-migration-service-update-launch-configuration-request-structure
- name: Application Migration Service Update Launch Configuration Template Request Structure
  property_count: 0
  slug: application-migration-service-update-launch-configuration-template-request-structure
- name: Application Migration Service Update Replication Configuration Request Structure
  property_count: 0
  slug: application-migration-service-update-replication-configuration-request-structure
- name: Application Migration Service Update Replication Configuration Template Request Structure
  property_count: 0
  slug: application-migration-service-update-replication-configuration-template-request-structure
- name: Application Migration Service Update Wave Request Structure
  property_count: 0
  slug: application-migration-service-update-wave-request-structure
- name: Application Migration Service Vcenter Client Structure
  property_count: 0
  slug: application-migration-service-vcenter-client-structure
- name: Application Migration Service Wave Aggregated Status Structure
  property_count: 0
  slug: application-migration-service-wave-aggregated-status-structure
- name: Application Migration Service Wave Structure
  property_count: 0
  slug: application-migration-service-wave-structure
jsonld:
- class_count: 100
  name: Amazon Application Migration Service Context
  property_count: 0
  slug: amazon-application-migration-service-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon Application Migration Service MCP Server
  slug: amazon-application-migration-service-mcp-server
modified: '2026-06-20'
name: Amazon Application Migration Service
nav: Providers
network: true
overview: 'Amazon Application Migration Service publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Exports API, Jobs API, and 7 more. Tagged areas include Amazon Application Migration Service, Migration, Lift And Shift, and Cloud Migration.


  The Amazon Application Migration Service catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Application Migration Service''s developer surface includes authentication and 8 more developer resources.'
random_paper: 1
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Application Migration Service API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-application-migration-service-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Amazon Application Migration Service API Rules
  rule_count: 28
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 12
  slug: amazon-application-migration-service-spectral-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 33.3
    contract_quality: 73.7
    developer_ergonomics: 11.9
    discoverability: 53.7
    governance: 33.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-application-migration-service/refs/heads/main/screenshots/amazon-application-migration-service-2026-07-25T195925.png
security:
- kind: authentication
  name: Amazon Application Migration Service Authentication
  slug: amazon-application-migration-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Application Migration Service Domain Security
  slug: amazon-application-migration-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Application Migration Service Vulnerability Disclosure
  slug: amazon-application-migration-service-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-application-migration-service
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- Cloud Migration
use_cases:
- Migrate on-premises data center servers to AWS with minimal downtime
- Execute phased migrations organized by application waves
- Test migration outcomes before executing production cutover
- Migrate VMware virtual machines to EC2 instances without agent installation
- Standardize migration configuration across hundreds of servers with templates
- Automate post-migration software installation and configuration with SSM
---
