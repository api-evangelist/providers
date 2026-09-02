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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Eventbridge Scheduler Agentic Access
  operation_count: 12
  slug: amazon-eventbridge-scheduler-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- description: The Schedule Groups API from Amazon EventBridge Scheduler — 2 operation(s) for schedule groups.
  name: Amazon EventBridge Scheduler Schedule Groups API
  slug: amazon-eventbridge-scheduler-schedule-groups-api
- description: The Schedules API from Amazon EventBridge Scheduler — 2 operation(s) for schedules.
  name: Amazon EventBridge Scheduler Schedules API
  slug: amazon-eventbridge-scheduler-schedules-api
- description: The Tags API from Amazon EventBridge Scheduler — 2 operation(s) for tags.
  name: Amazon EventBridge Scheduler Tags API
  slug: amazon-eventbridge-scheduler-tags-api
arazzos:
- description: List schedule groups, inspect the first match, then list its tags.
  name: EventBridge Scheduler Audit Schedule Group Tags
  slug: amazon-eventbridge-scheduler-audit-schedule-group-tags-workflow
- description: Create a schedule, update its expression and state, then read it back.
  name: EventBridge Scheduler Create Then Update Schedule
  slug: amazon-eventbridge-scheduler-create-then-update-schedule-workflow
- description: List schedules in a group, inspect the first match, then delete it.
  name: EventBridge Scheduler List Inspect And Delete Schedule
  slug: amazon-eventbridge-scheduler-list-inspect-delete-schedule-workflow
- description: Create a schedule group, add a schedule to it, then read the schedule back.
  name: EventBridge Scheduler Provision Grouped Schedule
  slug: amazon-eventbridge-scheduler-provision-grouped-schedule-workflow
- description: Create a schedule group, confirm it, then delete it.
  name: EventBridge Scheduler Schedule Group Lifecycle
  slug: amazon-eventbridge-scheduler-schedule-group-lifecycle-workflow
- description: Create a schedule group, tag it, then list its tags to confirm.
  name: EventBridge Scheduler Tag Schedule Group
  slug: amazon-eventbridge-scheduler-tag-schedule-group-workflow
- description: Resolve a schedule group ARN, remove tag keys, then list remaining tags.
  name: EventBridge Scheduler Untag Schedule Group
  slug: amazon-eventbridge-scheduler-untag-schedule-group-workflow
artifact_total: 328
collections:
- collection_type: postman
  name: Amazon EventBridge Scheduler Schedule Groups API
  slug: postman-amazon-eventbridge-scheduler-schedule-groups-api
- collection_type: postman
  name: Amazon EventBridge Scheduler Schedule Groups Schedules API
  slug: postman-amazon-eventbridge-scheduler-schedules-api
- collection_type: postman
  name: Amazon EventBridge Scheduler Schedule Groups Tags API
  slug: postman-amazon-eventbridge-scheduler-tags-api
- collection_type: postman
  name: Amazon EventBridge Scheduler
  slug: postman-amazon-eventbridge-scheduler
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EventBridge Scheduler Schedule Groups API
  slug: open-amazon-eventbridge-scheduler-schedule-groups-api
- collection_type: open
  name: Amazon EventBridge Scheduler Schedule Groups Schedules API
  slug: open-amazon-eventbridge-scheduler-schedules-api
- collection_type: open
  name: Amazon EventBridge Scheduler Schedule Groups Tags API
  slug: open-amazon-eventbridge-scheduler-tags-api
- collection_type: open
  name: Amazon EventBridge Scheduler
  slug: open-amazon-eventbridge-scheduler
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-eventbridge-scheduler-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-eventbridge-scheduler-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-eventbridge-scheduler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-eventbridge-scheduler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-eventbridge-scheduler-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-eventbridge-scheduler/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-audit-schedule-group-tags-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-create-then-update-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-list-inspect-delete-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-provision-grouped-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-schedule-group-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-tag-schedule-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-scheduler-untag-schedule-group-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/eventbridge/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/eventbridge/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/scheduler/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/eventbridge/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/eventbridge
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-eventbridge-scheduler-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-eventbridge-scheduler-vocabulary.yaml
created: '2024-01-15'
description: Amazon EventBridge Scheduler is a fully managed, serverless scheduler that enables you to create, run, and manage tasks from one central, managed service. With EventBridge Scheduler, you can create millions of schedules using cron and rate expressions.
examples:
- key_count: 3
  name: Amazon Eventbridge Scheduler Aws Vpc Configuration Example
  slug: amazon-eventbridge-scheduler-aws-vpc-configuration-example
- key_count: 3
  name: Amazon Eventbridge Scheduler Capacity Provider Strategy Item Example
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Conflict Exception Example
  slug: amazon-eventbridge-scheduler-conflict-exception-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Create Schedule Group Input Example
  slug: amazon-eventbridge-scheduler-create-schedule-group-input-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Create Schedule Group Output Example
  slug: amazon-eventbridge-scheduler-create-schedule-group-output-example
- key_count: 10
  name: Amazon Eventbridge Scheduler Create Schedule Input Example
  slug: amazon-eventbridge-scheduler-create-schedule-input-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Create Schedule Output Example
  slug: amazon-eventbridge-scheduler-create-schedule-output-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Dead Letter Config Example
  slug: amazon-eventbridge-scheduler-dead-letter-config-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Delete Schedule Group Input Example
  slug: amazon-eventbridge-scheduler-delete-schedule-group-input-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Delete Schedule Group Output Example
  slug: amazon-eventbridge-scheduler-delete-schedule-group-output-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Delete Schedule Input Example
  slug: amazon-eventbridge-scheduler-delete-schedule-input-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Delete Schedule Output Example
  slug: amazon-eventbridge-scheduler-delete-schedule-output-example
- key_count: 10
  name: Amazon Eventbridge Scheduler Ecs Parameters Example
  slug: amazon-eventbridge-scheduler-ecs-parameters-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Event Bridge Parameters Example
  slug: amazon-eventbridge-scheduler-event-bridge-parameters-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Flexible Time Window Example
  slug: amazon-eventbridge-scheduler-flexible-time-window-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Get Schedule Group Input Example
  slug: amazon-eventbridge-scheduler-get-schedule-group-input-example
- key_count: 5
  name: Amazon Eventbridge Scheduler Get Schedule Group Output Example
  slug: amazon-eventbridge-scheduler-get-schedule-group-output-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Get Schedule Input Example
  slug: amazon-eventbridge-scheduler-get-schedule-input-example
- key_count: 10
  name: Amazon Eventbridge Scheduler Get Schedule Output Example
  slug: amazon-eventbridge-scheduler-get-schedule-output-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Internal Server Exception Example
  slug: amazon-eventbridge-scheduler-internal-server-exception-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Kinesis Parameters Example
  slug: amazon-eventbridge-scheduler-kinesis-parameters-example
- key_count: 0
  name: Amazon Eventbridge Scheduler List Schedule Groups Input Example
  slug: amazon-eventbridge-scheduler-list-schedule-groups-input-example
- key_count: 2
  name: Amazon Eventbridge Scheduler List Schedule Groups Output Example
  slug: amazon-eventbridge-scheduler-list-schedule-groups-output-example
- key_count: 0
  name: Amazon Eventbridge Scheduler List Schedules Input Example
  slug: amazon-eventbridge-scheduler-list-schedules-input-example
- key_count: 2
  name: Amazon Eventbridge Scheduler List Schedules Output Example
  slug: amazon-eventbridge-scheduler-list-schedules-output-example
- key_count: 0
  name: Amazon Eventbridge Scheduler List Tags For Resource Input Example
  slug: amazon-eventbridge-scheduler-list-tags-for-resource-input-example
- key_count: 1
  name: Amazon Eventbridge Scheduler List Tags For Resource Output Example
  slug: amazon-eventbridge-scheduler-list-tags-for-resource-output-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Network Configuration Example
  slug: amazon-eventbridge-scheduler-network-configuration-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Placement Constraint Example
  slug: amazon-eventbridge-scheduler-placement-constraint-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Placement Strategy Example
  slug: amazon-eventbridge-scheduler-placement-strategy-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Resource Not Found Exception Example
  slug: amazon-eventbridge-scheduler-resource-not-found-exception-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Retry Policy Example
  slug: amazon-eventbridge-scheduler-retry-policy-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameter Example
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameters Example
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameters-example
- key_count: 5
  name: Amazon Eventbridge Scheduler Schedule Group Summary Example
  slug: amazon-eventbridge-scheduler-schedule-group-summary-example
- key_count: 7
  name: Amazon Eventbridge Scheduler Schedule Summary Example
  slug: amazon-eventbridge-scheduler-schedule-summary-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Service Quota Exceeded Exception Example
  slug: amazon-eventbridge-scheduler-service-quota-exceeded-exception-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Sqs Parameters Example
  slug: amazon-eventbridge-scheduler-sqs-parameters-example
- key_count: 2
  name: Amazon Eventbridge Scheduler Tag Example
  slug: amazon-eventbridge-scheduler-tag-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Tag Map Example
  slug: amazon-eventbridge-scheduler-tag-map-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Tag Resource Input Example
  slug: amazon-eventbridge-scheduler-tag-resource-input-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Tag Resource Output Example
  slug: amazon-eventbridge-scheduler-tag-resource-output-example
- key_count: 10
  name: Amazon Eventbridge Scheduler Target Example
  slug: amazon-eventbridge-scheduler-target-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Target Summary Example
  slug: amazon-eventbridge-scheduler-target-summary-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Throttling Exception Example
  slug: amazon-eventbridge-scheduler-throttling-exception-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Untag Resource Input Example
  slug: amazon-eventbridge-scheduler-untag-resource-input-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Untag Resource Output Example
  slug: amazon-eventbridge-scheduler-untag-resource-output-example
- key_count: 10
  name: Amazon Eventbridge Scheduler Update Schedule Input Example
  slug: amazon-eventbridge-scheduler-update-schedule-input-example
- key_count: 1
  name: Amazon Eventbridge Scheduler Update Schedule Output Example
  slug: amazon-eventbridge-scheduler-update-schedule-output-example
- key_count: 0
  name: Amazon Eventbridge Scheduler Validation Exception Example
  slug: amazon-eventbridge-scheduler-validation-exception-example
features:
- description: Schedule tasks using flexible cron expressions or simple rate expressions
  name: Cron and Rate Scheduling
- description: Create one-time schedules for future tasks with precise timing
  name: One-Time Schedules
- description: Organize schedules into groups for bulk management and operations
  name: Schedule Groups
- description: Allow schedules to run within flexible time windows for load distribution
  name: Flexible Time Windows
- description: Specify schedules in any timezone for global deployments
  name: Timezone Support
finops:
- name: Amazon Eventbridge Scheduler Finops
  service_category: API
  slug: amazon-eventbridge-scheduler-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Invoke Lambda functions on a schedule
  name: AWS Lambda
- description: Send messages to SQS queues at scheduled intervals
  name: Amazon SQS
- description: Start Step Functions state machine executions on a schedule
  name: AWS Step Functions
- description: Run ECS tasks on a scheduled basis
  name: Amazon ECS
- description: Send events to EventBridge event buses on a schedule
  name: Amazon EventBridge
json_schemas:
- name: ActionAfterCompletion
  property_count: 0
  slug: amazon-eventbridge-scheduler-action-after-completion
- name: AssignPublicIp
  property_count: 0
  slug: amazon-eventbridge-scheduler-assign-public-ip
- name: AwsVpcConfiguration
  property_count: 3
  slug: amazon-eventbridge-scheduler-aws-vpc-configuration
- name: CapacityProvider
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider
- name: CapacityProviderStrategyItemBase
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item-base
- name: CapacityProviderStrategyItem
  property_count: 3
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item
- name: CapacityProviderStrategyItemWeight
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item-weight
- name: CapacityProviderStrategy
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy
- name: ClientToken
  property_count: 0
  slug: amazon-eventbridge-scheduler-client-token
- name: ConflictException
  property_count: 0
  slug: amazon-eventbridge-scheduler-conflict-exception
- name: CreateScheduleGroupInput
  property_count: 2
  slug: amazon-eventbridge-scheduler-create-schedule-group-input
- name: CreateScheduleGroupOutput
  property_count: 1
  slug: amazon-eventbridge-scheduler-create-schedule-group-output
- name: CreateScheduleInput
  property_count: 12
  slug: amazon-eventbridge-scheduler-create-schedule-input
- name: CreateScheduleOutput
  property_count: 1
  slug: amazon-eventbridge-scheduler-create-schedule-output
- name: CreationDate
  property_count: 0
  slug: amazon-eventbridge-scheduler-creation-date
- name: DeadLetterConfigArnString
  property_count: 0
  slug: amazon-eventbridge-scheduler-dead-letter-config-arn-string
- name: DeadLetterConfig
  property_count: 1
  slug: amazon-eventbridge-scheduler-dead-letter-config
- name: DeleteScheduleGroupInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-group-input
- name: DeleteScheduleGroupOutput
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-group-output
- name: DeleteScheduleInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-input
- name: DeleteScheduleOutput
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-output
- name: Description
  property_count: 0
  slug: amazon-eventbridge-scheduler-description
- name: DetailType
  property_count: 0
  slug: amazon-eventbridge-scheduler-detail-type
- name: EcsParameters
  property_count: 14
  slug: amazon-eventbridge-scheduler-ecs-parameters
- name: EnableECSManagedTags
  property_count: 0
  slug: amazon-eventbridge-scheduler-enable-ecs-managed-tags
- name: EnableExecuteCommand
  property_count: 0
  slug: amazon-eventbridge-scheduler-enable-execute-command
- name: EndDate
  property_count: 0
  slug: amazon-eventbridge-scheduler-end-date
- name: EventBridgeParameters
  property_count: 2
  slug: amazon-eventbridge-scheduler-event-bridge-parameters
- name: FlexibleTimeWindowMode
  property_count: 0
  slug: amazon-eventbridge-scheduler-flexible-time-window-mode
- name: FlexibleTimeWindow
  property_count: 2
  slug: amazon-eventbridge-scheduler-flexible-time-window
- name: GetScheduleGroupInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-get-schedule-group-input
- name: GetScheduleGroupOutput
  property_count: 5
  slug: amazon-eventbridge-scheduler-get-schedule-group-output
- name: GetScheduleInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-get-schedule-input
- name: GetScheduleOutput
  property_count: 15
  slug: amazon-eventbridge-scheduler-get-schedule-output
- name: Group
  property_count: 0
  slug: amazon-eventbridge-scheduler-group
- name: InternalServerException
  property_count: 0
  slug: amazon-eventbridge-scheduler-internal-server-exception
- name: KinesisParameters
  property_count: 1
  slug: amazon-eventbridge-scheduler-kinesis-parameters
- name: KmsKeyArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-kms-key-arn
- name: LastModificationDate
  property_count: 0
  slug: amazon-eventbridge-scheduler-last-modification-date
- name: LaunchType
  property_count: 0
  slug: amazon-eventbridge-scheduler-launch-type
- name: ListScheduleGroupsInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-list-schedule-groups-input
- name: ListScheduleGroupsOutput
  property_count: 2
  slug: amazon-eventbridge-scheduler-list-schedule-groups-output
- name: ListSchedulesInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-list-schedules-input
- name: ListSchedulesOutput
  property_count: 2
  slug: amazon-eventbridge-scheduler-list-schedules-output
- name: ListTagsForResourceInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-list-tags-for-resource-input
- name: ListTagsForResourceOutput
  property_count: 1
  slug: amazon-eventbridge-scheduler-list-tags-for-resource-output
- name: MaxResults
  property_count: 0
  slug: amazon-eventbridge-scheduler-max-results
- name: MaximumEventAgeInSeconds
  property_count: 0
  slug: amazon-eventbridge-scheduler-maximum-event-age-in-seconds
- name: MaximumRetryAttempts
  property_count: 0
  slug: amazon-eventbridge-scheduler-maximum-retry-attempts
- name: MaximumWindowInMinutes
  property_count: 0
  slug: amazon-eventbridge-scheduler-maximum-window-in-minutes
- name: MessageGroupId
  property_count: 0
  slug: amazon-eventbridge-scheduler-message-group-id
- name: NamePrefix
  property_count: 0
  slug: amazon-eventbridge-scheduler-name-prefix
- name: Name
  property_count: 0
  slug: amazon-eventbridge-scheduler-name
- name: NetworkConfiguration
  property_count: 1
  slug: amazon-eventbridge-scheduler-network-configuration
- name: NextToken
  property_count: 0
  slug: amazon-eventbridge-scheduler-next-token
- name: PlacementConstraintExpression
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-constraint-expression
- name: PlacementConstraint
  property_count: 2
  slug: amazon-eventbridge-scheduler-placement-constraint
- name: PlacementConstraintType
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-constraint-type
- name: PlacementConstraints
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-constraints
- name: PlacementStrategies
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-strategies
- name: PlacementStrategyField
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-strategy-field
- name: PlacementStrategy
  property_count: 2
  slug: amazon-eventbridge-scheduler-placement-strategy
- name: PlacementStrategyType
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-strategy-type
- name: PlatformVersion
  property_count: 0
  slug: amazon-eventbridge-scheduler-platform-version
- name: PropagateTags
  property_count: 0
  slug: amazon-eventbridge-scheduler-propagate-tags
- name: ReferenceId
  property_count: 0
  slug: amazon-eventbridge-scheduler-reference-id
- name: ResourceNotFoundException
  property_count: 0
  slug: amazon-eventbridge-scheduler-resource-not-found-exception
- name: RetryPolicy
  property_count: 2
  slug: amazon-eventbridge-scheduler-retry-policy
- name: RoleArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-role-arn
- name: SageMakerPipelineParameterList
  property_count: 0
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-list
- name: SageMakerPipelineParameterName
  property_count: 0
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-name
- name: SageMakerPipelineParameter
  property_count: 2
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter
- name: SageMakerPipelineParameterValue
  property_count: 0
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-value
- name: SageMakerPipelineParameters
  property_count: 1
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameters
- name: ScheduleArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-arn
- name: ScheduleExpression
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-expression
- name: ScheduleExpressionTimezone
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-expression-timezone
- name: ScheduleGroupArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-arn
- name: ScheduleGroupList
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-list
- name: ScheduleGroupNamePrefix
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-name-prefix
- name: ScheduleGroupName
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-name
- name: ScheduleGroupState
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-state
- name: ScheduleGroupSummary
  property_count: 5
  slug: amazon-eventbridge-scheduler-schedule-group-summary
- name: ScheduleList
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-list
- name: ScheduleState
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-state
- name: ScheduleSummary
  property_count: 7
  slug: amazon-eventbridge-scheduler-schedule-summary
- name: SecurityGroup
  property_count: 0
  slug: amazon-eventbridge-scheduler-security-group
- name: SecurityGroups
  property_count: 0
  slug: amazon-eventbridge-scheduler-security-groups
- name: ServiceQuotaExceededException
  property_count: 0
  slug: amazon-eventbridge-scheduler-service-quota-exceeded-exception
- name: Source
  property_count: 0
  slug: amazon-eventbridge-scheduler-source
- name: SqsParameters
  property_count: 1
  slug: amazon-eventbridge-scheduler-sqs-parameters
- name: StartDate
  property_count: 0
  slug: amazon-eventbridge-scheduler-start-date
- name: Subnet
  property_count: 0
  slug: amazon-eventbridge-scheduler-subnet
- name: Subnets
  property_count: 0
  slug: amazon-eventbridge-scheduler-subnets
- name: TagKeyList
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-key-list
- name: TagKey
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-key
- name: TagList
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-list
- name: TagMap
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-map
- name: TagResourceArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-resource-arn
- name: TagResourceInput
  property_count: 1
  slug: amazon-eventbridge-scheduler-tag-resource-input
- name: TagResourceOutput
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-resource-output
- name: Tag
  property_count: 2
  slug: amazon-eventbridge-scheduler-tag
- name: TagValue
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-value
- name: Tags
  property_count: 0
  slug: amazon-eventbridge-scheduler-tags
- name: TargetArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-target-arn
- name: TargetInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-target-input
- name: TargetPartitionKey
  property_count: 0
  slug: amazon-eventbridge-scheduler-target-partition-key
- name: Target
  property_count: 10
  slug: amazon-eventbridge-scheduler-target
- name: TargetSummary
  property_count: 1
  slug: amazon-eventbridge-scheduler-target-summary
- name: TaskCount
  property_count: 0
  slug: amazon-eventbridge-scheduler-task-count
- name: TaskDefinitionArn
  property_count: 0
  slug: amazon-eventbridge-scheduler-task-definition-arn
- name: ThrottlingException
  property_count: 0
  slug: amazon-eventbridge-scheduler-throttling-exception
- name: UntagResourceInput
  property_count: 0
  slug: amazon-eventbridge-scheduler-untag-resource-input
- name: UntagResourceOutput
  property_count: 0
  slug: amazon-eventbridge-scheduler-untag-resource-output
- name: UpdateScheduleInput
  property_count: 12
  slug: amazon-eventbridge-scheduler-update-schedule-input
- name: UpdateScheduleOutput
  property_count: 1
  slug: amazon-eventbridge-scheduler-update-schedule-output
- name: ValidationException
  property_count: 0
  slug: amazon-eventbridge-scheduler-validation-exception
json_structures:
- name: Amazon Eventbridge Scheduler Action After Completion Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-action-after-completion-structure
- name: Amazon Eventbridge Scheduler Assign Public Ip Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-assign-public-ip-structure
- name: Amazon Eventbridge Scheduler Aws Vpc Configuration Structure
  property_count: 3
  slug: amazon-eventbridge-scheduler-aws-vpc-configuration-structure
- name: Amazon Eventbridge Scheduler Capacity Provider Strategy Item Base Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item-base-structure
- name: Amazon Eventbridge Scheduler Capacity Provider Strategy Item Structure
  property_count: 3
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item-structure
- name: Amazon Eventbridge Scheduler Capacity Provider Strategy Item Weight Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-item-weight-structure
- name: Amazon Eventbridge Scheduler Capacity Provider Strategy Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-strategy-structure
- name: Amazon Eventbridge Scheduler Capacity Provider Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-capacity-provider-structure
- name: Amazon Eventbridge Scheduler Client Token Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-client-token-structure
- name: Amazon Eventbridge Scheduler Conflict Exception Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-conflict-exception-structure
- name: Amazon Eventbridge Scheduler Create Schedule Group Input Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-create-schedule-group-input-structure
- name: Amazon Eventbridge Scheduler Create Schedule Group Output Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-create-schedule-group-output-structure
- name: Amazon Eventbridge Scheduler Create Schedule Input Structure
  property_count: 12
  slug: amazon-eventbridge-scheduler-create-schedule-input-structure
- name: Amazon Eventbridge Scheduler Create Schedule Output Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-create-schedule-output-structure
- name: Amazon Eventbridge Scheduler Creation Date Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-creation-date-structure
- name: Amazon Eventbridge Scheduler Dead Letter Config Arn String Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-dead-letter-config-arn-string-structure
- name: Amazon Eventbridge Scheduler Dead Letter Config Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-dead-letter-config-structure
- name: Amazon Eventbridge Scheduler Delete Schedule Group Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-group-input-structure
- name: Amazon Eventbridge Scheduler Delete Schedule Group Output Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-group-output-structure
- name: Amazon Eventbridge Scheduler Delete Schedule Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-input-structure
- name: Amazon Eventbridge Scheduler Delete Schedule Output Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-delete-schedule-output-structure
- name: Amazon Eventbridge Scheduler Description Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-description-structure
- name: Amazon Eventbridge Scheduler Detail Type Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-detail-type-structure
- name: Amazon Eventbridge Scheduler Ecs Parameters Structure
  property_count: 14
  slug: amazon-eventbridge-scheduler-ecs-parameters-structure
- name: Amazon Eventbridge Scheduler Enable Ecs Managed Tags Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-enable-ecs-managed-tags-structure
- name: Amazon Eventbridge Scheduler Enable Execute Command Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-enable-execute-command-structure
- name: Amazon Eventbridge Scheduler End Date Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-end-date-structure
- name: Amazon Eventbridge Scheduler Event Bridge Parameters Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-event-bridge-parameters-structure
- name: Amazon Eventbridge Scheduler Flexible Time Window Mode Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-flexible-time-window-mode-structure
- name: Amazon Eventbridge Scheduler Flexible Time Window Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-flexible-time-window-structure
- name: Amazon Eventbridge Scheduler Get Schedule Group Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-get-schedule-group-input-structure
- name: Amazon Eventbridge Scheduler Get Schedule Group Output Structure
  property_count: 5
  slug: amazon-eventbridge-scheduler-get-schedule-group-output-structure
- name: Amazon Eventbridge Scheduler Get Schedule Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-get-schedule-input-structure
- name: Amazon Eventbridge Scheduler Get Schedule Output Structure
  property_count: 15
  slug: amazon-eventbridge-scheduler-get-schedule-output-structure
- name: Amazon Eventbridge Scheduler Group Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-group-structure
- name: Amazon Eventbridge Scheduler Internal Server Exception Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-internal-server-exception-structure
- name: Amazon Eventbridge Scheduler Kinesis Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-kinesis-parameters-structure
- name: Amazon Eventbridge Scheduler Kms Key Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-kms-key-arn-structure
- name: Amazon Eventbridge Scheduler Last Modification Date Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-last-modification-date-structure
- name: Amazon Eventbridge Scheduler Launch Type Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-launch-type-structure
- name: Amazon Eventbridge Scheduler List Schedule Groups Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-list-schedule-groups-input-structure
- name: Amazon Eventbridge Scheduler List Schedule Groups Output Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-list-schedule-groups-output-structure
- name: Amazon Eventbridge Scheduler List Schedules Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-list-schedules-input-structure
- name: Amazon Eventbridge Scheduler List Schedules Output Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-list-schedules-output-structure
- name: Amazon Eventbridge Scheduler List Tags For Resource Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-list-tags-for-resource-input-structure
- name: Amazon Eventbridge Scheduler List Tags For Resource Output Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-list-tags-for-resource-output-structure
- name: Amazon Eventbridge Scheduler Max Results Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-max-results-structure
- name: Amazon Eventbridge Scheduler Maximum Event Age In Seconds Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-maximum-event-age-in-seconds-structure
- name: Amazon Eventbridge Scheduler Maximum Retry Attempts Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-maximum-retry-attempts-structure
- name: Amazon Eventbridge Scheduler Maximum Window In Minutes Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-maximum-window-in-minutes-structure
- name: Amazon Eventbridge Scheduler Message Group Id Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-message-group-id-structure
- name: Amazon Eventbridge Scheduler Name Prefix Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-name-prefix-structure
- name: Amazon Eventbridge Scheduler Name Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-name-structure
- name: Amazon Eventbridge Scheduler Network Configuration Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-network-configuration-structure
- name: Amazon Eventbridge Scheduler Next Token Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-next-token-structure
- name: Amazon Eventbridge Scheduler Placement Constraint Expression Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-constraint-expression-structure
- name: Amazon Eventbridge Scheduler Placement Constraint Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-placement-constraint-structure
- name: Amazon Eventbridge Scheduler Placement Constraint Type Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-constraint-type-structure
- name: Amazon Eventbridge Scheduler Placement Constraints Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-constraints-structure
- name: Amazon Eventbridge Scheduler Placement Strategies Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-strategies-structure
- name: Amazon Eventbridge Scheduler Placement Strategy Field Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-strategy-field-structure
- name: Amazon Eventbridge Scheduler Placement Strategy Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-placement-strategy-structure
- name: Amazon Eventbridge Scheduler Placement Strategy Type Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-placement-strategy-type-structure
- name: Amazon Eventbridge Scheduler Platform Version Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-platform-version-structure
- name: Amazon Eventbridge Scheduler Propagate Tags Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-propagate-tags-structure
- name: Amazon Eventbridge Scheduler Reference Id Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-reference-id-structure
- name: Amazon Eventbridge Scheduler Resource Not Found Exception Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-resource-not-found-exception-structure
- name: Amazon Eventbridge Scheduler Retry Policy Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-retry-policy-structure
- name: Amazon Eventbridge Scheduler Role Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-role-arn-structure
- name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameter List Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-list-structure
- name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameter Name Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-name-structure
- name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameter Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-structure
- name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameter Value Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameter-value-structure
- name: Amazon Eventbridge Scheduler Sage Maker Pipeline Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-sage-maker-pipeline-parameters-structure
- name: Amazon Eventbridge Scheduler Schedule Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-arn-structure
- name: Amazon Eventbridge Scheduler Schedule Expression Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-expression-structure
- name: Amazon Eventbridge Scheduler Schedule Expression Timezone Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-expression-timezone-structure
- name: Amazon Eventbridge Scheduler Schedule Group Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-arn-structure
- name: Amazon Eventbridge Scheduler Schedule Group List Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-list-structure
- name: Amazon Eventbridge Scheduler Schedule Group Name Prefix Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-name-prefix-structure
- name: Amazon Eventbridge Scheduler Schedule Group Name Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-name-structure
- name: Amazon Eventbridge Scheduler Schedule Group State Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-group-state-structure
- name: Amazon Eventbridge Scheduler Schedule Group Summary Structure
  property_count: 5
  slug: amazon-eventbridge-scheduler-schedule-group-summary-structure
- name: Amazon Eventbridge Scheduler Schedule List Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-list-structure
- name: Amazon Eventbridge Scheduler Schedule State Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-schedule-state-structure
- name: Amazon Eventbridge Scheduler Schedule Summary Structure
  property_count: 7
  slug: amazon-eventbridge-scheduler-schedule-summary-structure
- name: Amazon Eventbridge Scheduler Security Group Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-security-group-structure
- name: Amazon Eventbridge Scheduler Security Groups Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-security-groups-structure
- name: Amazon Eventbridge Scheduler Service Quota Exceeded Exception Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-service-quota-exceeded-exception-structure
- name: Amazon Eventbridge Scheduler Source Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-source-structure
- name: Amazon Eventbridge Scheduler Sqs Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-sqs-parameters-structure
- name: Amazon Eventbridge Scheduler Start Date Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-start-date-structure
- name: Amazon Eventbridge Scheduler Subnet Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-subnet-structure
- name: Amazon Eventbridge Scheduler Subnets Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-subnets-structure
- name: Amazon Eventbridge Scheduler Tag Key List Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-key-list-structure
- name: Amazon Eventbridge Scheduler Tag Key Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-key-structure
- name: Amazon Eventbridge Scheduler Tag List Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-list-structure
- name: Amazon Eventbridge Scheduler Tag Map Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-map-structure
- name: Amazon Eventbridge Scheduler Tag Resource Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-resource-arn-structure
- name: Amazon Eventbridge Scheduler Tag Resource Input Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-tag-resource-input-structure
- name: Amazon Eventbridge Scheduler Tag Resource Output Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-resource-output-structure
- name: Amazon Eventbridge Scheduler Tag Structure
  property_count: 2
  slug: amazon-eventbridge-scheduler-tag-structure
- name: Amazon Eventbridge Scheduler Tag Value Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tag-value-structure
- name: Amazon Eventbridge Scheduler Tags Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-tags-structure
- name: Amazon Eventbridge Scheduler Target Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-target-arn-structure
- name: Amazon Eventbridge Scheduler Target Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-target-input-structure
- name: Amazon Eventbridge Scheduler Target Partition Key Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-target-partition-key-structure
- name: Amazon Eventbridge Scheduler Target Structure
  property_count: 10
  slug: amazon-eventbridge-scheduler-target-structure
- name: Amazon Eventbridge Scheduler Target Summary Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-target-summary-structure
- name: Amazon Eventbridge Scheduler Task Count Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-task-count-structure
- name: Amazon Eventbridge Scheduler Task Definition Arn Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-task-definition-arn-structure
- name: Amazon Eventbridge Scheduler Throttling Exception Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-throttling-exception-structure
- name: Amazon Eventbridge Scheduler Untag Resource Input Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-untag-resource-input-structure
- name: Amazon Eventbridge Scheduler Untag Resource Output Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-untag-resource-output-structure
- name: Amazon Eventbridge Scheduler Update Schedule Input Structure
  property_count: 12
  slug: amazon-eventbridge-scheduler-update-schedule-input-structure
- name: Amazon Eventbridge Scheduler Update Schedule Output Structure
  property_count: 1
  slug: amazon-eventbridge-scheduler-update-schedule-output-structure
- name: Amazon Eventbridge Scheduler Validation Exception Structure
  property_count: 0
  slug: amazon-eventbridge-scheduler-validation-exception-structure
jsonld:
- class_count: 44
  name: Amazon Eventbridge Scheduler Context
  property_count: 54
  slug: amazon-eventbridge-scheduler-context
layout: provider
modified: '2026-05-19'
name: Amazon EventBridge Scheduler
nav: Providers
network: true
overview: 'Amazon EventBridge Scheduler publishes 3 APIs on the [APIs.io](https://apis.io/) network: Schedule Groups API, Schedules API, and Tags API. Tagged areas include Amazon Web Services, Cron, Event-Driven, Scheduling, and Serverless.


  The Amazon EventBridge Scheduler catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EventBridge Scheduler''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 27 more developer resources.'
plans:
- name: Amazon Eventbridge Scheduler Plans Pricing
  plan_count: 3
  slug: amazon-eventbridge-scheduler-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Amazon Eventbridge Scheduler Rate Limits
  slug: amazon-eventbridge-scheduler-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon EventBridge Scheduler API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-eventbridge-scheduler-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon EventBridge Scheduler API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-eventbridge-scheduler-spectral-rules
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 74.8
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-eventbridge-scheduler/refs/heads/main/screenshots/amazon-eventbridge-scheduler-2026-06-20T171646.png
security:
- kind: authentication
  name: Amazon Eventbridge Scheduler Authentication
  slug: amazon-eventbridge-scheduler-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Eventbridge Scheduler Domain Security
  slug: amazon-eventbridge-scheduler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Eventbridge Scheduler Vulnerability Disclosure
  slug: amazon-eventbridge-scheduler-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Eventbridge Scheduler Trust Center
  slug: amazon-eventbridge-scheduler-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-eventbridge-scheduler
tags:
- Amazon Web Services
- Cron
- Event-Driven
- Scheduling
- Serverless
use_cases:
- description: Schedule periodic data processing and ETL batch jobs
  name: Batch Job Scheduling
- description: Automatically generate and deliver reports on a schedule
  name: Report Generation
- description: Schedule automatic cleanup of temporary resources and old data
  name: Resource Cleanup
- description: Send scheduled notifications and reminders to users
  name: Reminder Notifications
website: https://aws.amazon.com/eventbridge/
---
