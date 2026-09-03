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
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Amazon Eventbridge Pipes Agentic Access
  operation_count: 10
  slug: amazon-eventbridge-pipes-agentic-access
  summary_line: 10 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://pipes.amazonaws.com
  baseurl_source: declared
  description: The Pipes API from Amazon EventBridge Pipes — 4 operation(s) for pipes.
  name: Amazon EventBridge Pipes Pipes API
  slug: amazon-eventbridge-pipes-pipes-api
- baseURL: https://pipes.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon EventBridge Pipes — 2 operation(s) for tags.
  name: Amazon EventBridge Pipes Tags API
  slug: amazon-eventbridge-pipes-tags-api
arazzos:
- description: Create a pipe with DesiredState RUNNING, then poll DescribePipe until it reports CurrentState RUNNING.
  name: EventBridge Pipes Create Pipe and Await Running
  slug: amazon-eventbridge-pipes-create-pipe-await-running-workflow
- description: Create a pipe in the STOPPED state, explicitly start it, then describe it to confirm the running configuration.
  name: EventBridge Pipes Create, Start and Confirm
  slug: amazon-eventbridge-pipes-create-start-describe-workflow
- description: Read an existing pipe, apply a configuration update, then poll until the pipe settles back to a stable state.
  name: EventBridge Pipes Describe, Update and Await
  slug: amazon-eventbridge-pipes-describe-update-await-workflow
- description: Safely decommission a pipe by stopping it, polling until it is STOPPED, then deleting it.
  name: EventBridge Pipes Drain and Delete Pipe
  slug: amazon-eventbridge-pipes-drain-and-delete-pipe-workflow
- description: Stop a running pipe, then poll DescribePipe until it confirms the pipe has fully reached the STOPPED state.
  name: EventBridge Pipes Stop Pipe and Await Stopped
  slug: amazon-eventbridge-pipes-stop-pipe-await-stopped-workflow
- description: Resolve a pipe's ARN by name, apply tags to it, then list the resource tags to verify they were stored.
  name: EventBridge Pipes Tag Pipe and Verify
  slug: amazon-eventbridge-pipes-tag-pipe-and-verify-workflow
artifact_total: 513
collections:
- collection_type: postman
  name: Amazon EventBridge Pipes API
  slug: postman-amazon-eventbridge-pipes-pipes-api
- collection_type: postman
  name: Amazon EventBridge Pipes Tags API
  slug: postman-amazon-eventbridge-pipes-tags-api
- collection_type: postman
  name: Amazon EventBridge Pipes
  slug: postman-amazon-eventbridge-pipes
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EventBridge Pipes API
  slug: open-amazon-eventbridge-pipes-pipes-api
- collection_type: open
  name: Amazon EventBridge Pipes Tags API
  slug: open-amazon-eventbridge-pipes-tags-api
- collection_type: open
  name: Amazon EventBridge Pipes
  slug: open-amazon-eventbridge-pipes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-eventbridge-pipes-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-eventbridge-pipes-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-eventbridge-pipes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-eventbridge-pipes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-eventbridge-pipes-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-eventbridge-pipes/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-pipes-create-pipe-await-running-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-pipes-create-start-describe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-pipes-describe-update-await-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-pipes-drain-and-delete-pipe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-pipes-stop-pipe-await-stopped-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-pipes-tag-pipe-and-verify-workflow.yml
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
  url: https://console.aws.amazon.com/events/
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
  url: rules/amazon-eventbridge-pipes-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-eventbridge-pipes-vocabulary.yaml
created: '2024-01-15'
description: Amazon EventBridge Pipes helps you create point-to-point integrations between event producers and consumers with optional transform, filter, and enrich steps. It reduces the amount of integration code you need to write and maintain when building event-driven applications.
examples:
- key_count: 3
  name: Amazon Eventbridge Pipes Aws Vpc Configuration Example
  slug: amazon-eventbridge-pipes-aws-vpc-configuration-example
- key_count: 1
  name: Amazon Eventbridge Pipes Batch Array Properties Example
  slug: amazon-eventbridge-pipes-batch-array-properties-example
- key_count: 4
  name: Amazon Eventbridge Pipes Batch Container Overrides Example
  slug: amazon-eventbridge-pipes-batch-container-overrides-example
- key_count: 2
  name: Amazon Eventbridge Pipes Batch Environment Variable Example
  slug: amazon-eventbridge-pipes-batch-environment-variable-example
- key_count: 2
  name: Amazon Eventbridge Pipes Batch Job Dependency Example
  slug: amazon-eventbridge-pipes-batch-job-dependency-example
- key_count: 0
  name: Amazon Eventbridge Pipes Batch Parameters Map Example
  slug: amazon-eventbridge-pipes-batch-parameters-map-example
- key_count: 2
  name: Amazon Eventbridge Pipes Batch Resource Requirement Example
  slug: amazon-eventbridge-pipes-batch-resource-requirement-example
- key_count: 1
  name: Amazon Eventbridge Pipes Batch Retry Strategy Example
  slug: amazon-eventbridge-pipes-batch-retry-strategy-example
- key_count: 3
  name: Amazon Eventbridge Pipes Capacity Provider Strategy Item Example
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item-example
- key_count: 0
  name: Amazon Eventbridge Pipes Conflict Exception Example
  slug: amazon-eventbridge-pipes-conflict-exception-example
- key_count: 10
  name: Amazon Eventbridge Pipes Create Pipe Request Example
  slug: amazon-eventbridge-pipes-create-pipe-request-example
- key_count: 6
  name: Amazon Eventbridge Pipes Create Pipe Response Example
  slug: amazon-eventbridge-pipes-create-pipe-response-example
- key_count: 1
  name: Amazon Eventbridge Pipes Dead Letter Config Example
  slug: amazon-eventbridge-pipes-dead-letter-config-example
- key_count: 0
  name: Amazon Eventbridge Pipes Delete Pipe Request Example
  slug: amazon-eventbridge-pipes-delete-pipe-request-example
- key_count: 6
  name: Amazon Eventbridge Pipes Delete Pipe Response Example
  slug: amazon-eventbridge-pipes-delete-pipe-response-example
- key_count: 0
  name: Amazon Eventbridge Pipes Describe Pipe Request Example
  slug: amazon-eventbridge-pipes-describe-pipe-request-example
- key_count: 10
  name: Amazon Eventbridge Pipes Describe Pipe Response Example
  slug: amazon-eventbridge-pipes-describe-pipe-response-example
- key_count: 8
  name: Amazon Eventbridge Pipes Ecs Container Override Example
  slug: amazon-eventbridge-pipes-ecs-container-override-example
- key_count: 2
  name: Amazon Eventbridge Pipes Ecs Environment File Example
  slug: amazon-eventbridge-pipes-ecs-environment-file-example
- key_count: 2
  name: Amazon Eventbridge Pipes Ecs Environment Variable Example
  slug: amazon-eventbridge-pipes-ecs-environment-variable-example
- key_count: 1
  name: Amazon Eventbridge Pipes Ecs Ephemeral Storage Example
  slug: amazon-eventbridge-pipes-ecs-ephemeral-storage-example
- key_count: 2
  name: Amazon Eventbridge Pipes Ecs Inference Accelerator Override Example
  slug: amazon-eventbridge-pipes-ecs-inference-accelerator-override-example
- key_count: 2
  name: Amazon Eventbridge Pipes Ecs Resource Requirement Example
  slug: amazon-eventbridge-pipes-ecs-resource-requirement-example
- key_count: 7
  name: Amazon Eventbridge Pipes Ecs Task Override Example
  slug: amazon-eventbridge-pipes-ecs-task-override-example
- key_count: 1
  name: Amazon Eventbridge Pipes Filter Criteria Example
  slug: amazon-eventbridge-pipes-filter-criteria-example
- key_count: 1
  name: Amazon Eventbridge Pipes Filter Example
  slug: amazon-eventbridge-pipes-filter-example
- key_count: 0
  name: Amazon Eventbridge Pipes Header Parameters Map Example
  slug: amazon-eventbridge-pipes-header-parameters-map-example
- key_count: 0
  name: Amazon Eventbridge Pipes Internal Exception Example
  slug: amazon-eventbridge-pipes-internal-exception-example
- key_count: 0
  name: Amazon Eventbridge Pipes List Pipes Request Example
  slug: amazon-eventbridge-pipes-list-pipes-request-example
- key_count: 2
  name: Amazon Eventbridge Pipes List Pipes Response Example
  slug: amazon-eventbridge-pipes-list-pipes-response-example
- key_count: 0
  name: Amazon Eventbridge Pipes List Tags For Resource Request Example
  slug: amazon-eventbridge-pipes-list-tags-for-resource-request-example
- key_count: 1
  name: Amazon Eventbridge Pipes List Tags For Resource Response Example
  slug: amazon-eventbridge-pipes-list-tags-for-resource-response-example
- key_count: 1
  name: Amazon Eventbridge Pipes Mq Broker Access Credentials Example
  slug: amazon-eventbridge-pipes-mq-broker-access-credentials-example
- key_count: 2
  name: Amazon Eventbridge Pipes Msk Access Credentials Example
  slug: amazon-eventbridge-pipes-msk-access-credentials-example
- key_count: 1
  name: Amazon Eventbridge Pipes Network Configuration Example
  slug: amazon-eventbridge-pipes-network-configuration-example
- key_count: 0
  name: Amazon Eventbridge Pipes Not Found Exception Example
  slug: amazon-eventbridge-pipes-not-found-exception-example
- key_count: 3
  name: Amazon Eventbridge Pipes Pipe Enrichment Http Parameters Example
  slug: amazon-eventbridge-pipes-pipe-enrichment-http-parameters-example
- key_count: 2
  name: Amazon Eventbridge Pipes Pipe Enrichment Parameters Example
  slug: amazon-eventbridge-pipes-pipe-enrichment-parameters-example
- key_count: 10
  name: Amazon Eventbridge Pipes Pipe Example
  slug: amazon-eventbridge-pipes-pipe-example
- key_count: 4
  name: Amazon Eventbridge Pipes Pipe Source Active Mq Broker Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-active-mq-broker-parameters-example
- key_count: 8
  name: Amazon Eventbridge Pipes Pipe Source Dynamo Db Stream Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-dynamo-db-stream-parameters-example
- key_count: 9
  name: Amazon Eventbridge Pipes Pipe Source Kinesis Stream Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-kinesis-stream-parameters-example
- key_count: 6
  name: Amazon Eventbridge Pipes Pipe Source Managed Streaming Kafka Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-managed-streaming-kafka-parameters-example
- key_count: 8
  name: Amazon Eventbridge Pipes Pipe Source Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-parameters-example
- key_count: 5
  name: Amazon Eventbridge Pipes Pipe Source Rabbit Mq Broker Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-rabbit-mq-broker-parameters-example
- key_count: 9
  name: Amazon Eventbridge Pipes Pipe Source Self Managed Kafka Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-self-managed-kafka-parameters-example
- key_count: 2
  name: Amazon Eventbridge Pipes Pipe Source Sqs Queue Parameters Example
  slug: amazon-eventbridge-pipes-pipe-source-sqs-queue-parameters-example
- key_count: 7
  name: Amazon Eventbridge Pipes Pipe Target Batch Job Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-batch-job-parameters-example
- key_count: 2
  name: Amazon Eventbridge Pipes Pipe Target Cloud Watch Logs Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-cloud-watch-logs-parameters-example
- key_count: 10
  name: Amazon Eventbridge Pipes Pipe Target Ecs Task Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-ecs-task-parameters-example
- key_count: 5
  name: Amazon Eventbridge Pipes Pipe Target Event Bridge Event Bus Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-event-bridge-event-bus-parameters-example
- key_count: 3
  name: Amazon Eventbridge Pipes Pipe Target Http Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-http-parameters-example
- key_count: 1
  name: Amazon Eventbridge Pipes Pipe Target Kinesis Stream Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-kinesis-stream-parameters-example
- key_count: 1
  name: Amazon Eventbridge Pipes Pipe Target Lambda Function Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-lambda-function-parameters-example
- key_count: 10
  name: Amazon Eventbridge Pipes Pipe Target Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-parameters-example
- key_count: 6
  name: Amazon Eventbridge Pipes Pipe Target Redshift Data Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-redshift-data-parameters-example
- key_count: 1
  name: Amazon Eventbridge Pipes Pipe Target Sage Maker Pipeline Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-sage-maker-pipeline-parameters-example
- key_count: 2
  name: Amazon Eventbridge Pipes Pipe Target Sqs Queue Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-sqs-queue-parameters-example
- key_count: 1
  name: Amazon Eventbridge Pipes Pipe Target State Machine Parameters Example
  slug: amazon-eventbridge-pipes-pipe-target-state-machine-parameters-example
- key_count: 2
  name: Amazon Eventbridge Pipes Placement Constraint Example
  slug: amazon-eventbridge-pipes-placement-constraint-example
- key_count: 2
  name: Amazon Eventbridge Pipes Placement Strategy Example
  slug: amazon-eventbridge-pipes-placement-strategy-example
- key_count: 0
  name: Amazon Eventbridge Pipes Query String Parameters Map Example
  slug: amazon-eventbridge-pipes-query-string-parameters-map-example
- key_count: 2
  name: Amazon Eventbridge Pipes Sage Maker Pipeline Parameter Example
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-example
- key_count: 4
  name: Amazon Eventbridge Pipes Self Managed Kafka Access Configuration Credentials Example
  slug: amazon-eventbridge-pipes-self-managed-kafka-access-configuration-credentials-example
- key_count: 2
  name: Amazon Eventbridge Pipes Self Managed Kafka Access Configuration Vpc Example
  slug: amazon-eventbridge-pipes-self-managed-kafka-access-configuration-vpc-example
- key_count: 0
  name: Amazon Eventbridge Pipes Service Quota Exceeded Exception Example
  slug: amazon-eventbridge-pipes-service-quota-exceeded-exception-example
- key_count: 0
  name: Amazon Eventbridge Pipes Start Pipe Request Example
  slug: amazon-eventbridge-pipes-start-pipe-request-example
- key_count: 6
  name: Amazon Eventbridge Pipes Start Pipe Response Example
  slug: amazon-eventbridge-pipes-start-pipe-response-example
- key_count: 0
  name: Amazon Eventbridge Pipes Stop Pipe Request Example
  slug: amazon-eventbridge-pipes-stop-pipe-request-example
- key_count: 6
  name: Amazon Eventbridge Pipes Stop Pipe Response Example
  slug: amazon-eventbridge-pipes-stop-pipe-response-example
- key_count: 2
  name: Amazon Eventbridge Pipes Tag Example
  slug: amazon-eventbridge-pipes-tag-example
- key_count: 0
  name: Amazon Eventbridge Pipes Tag Map Example
  slug: amazon-eventbridge-pipes-tag-map-example
- key_count: 1
  name: Amazon Eventbridge Pipes Tag Resource Request Example
  slug: amazon-eventbridge-pipes-tag-resource-request-example
- key_count: 0
  name: Amazon Eventbridge Pipes Tag Resource Response Example
  slug: amazon-eventbridge-pipes-tag-resource-response-example
- key_count: 0
  name: Amazon Eventbridge Pipes Throttling Exception Example
  slug: amazon-eventbridge-pipes-throttling-exception-example
- key_count: 0
  name: Amazon Eventbridge Pipes Untag Resource Request Example
  slug: amazon-eventbridge-pipes-untag-resource-request-example
- key_count: 0
  name: Amazon Eventbridge Pipes Untag Resource Response Example
  slug: amazon-eventbridge-pipes-untag-resource-response-example
- key_count: 8
  name: Amazon Eventbridge Pipes Update Pipe Request Example
  slug: amazon-eventbridge-pipes-update-pipe-request-example
- key_count: 6
  name: Amazon Eventbridge Pipes Update Pipe Response Example
  slug: amazon-eventbridge-pipes-update-pipe-response-example
- key_count: 3
  name: Amazon Eventbridge Pipes Update Pipe Source Active Mq Broker Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-active-mq-broker-parameters-example
- key_count: 7
  name: Amazon Eventbridge Pipes Update Pipe Source Dynamo Db Stream Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-dynamo-db-stream-parameters-example
- key_count: 7
  name: Amazon Eventbridge Pipes Update Pipe Source Kinesis Stream Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-kinesis-stream-parameters-example
- key_count: 3
  name: Amazon Eventbridge Pipes Update Pipe Source Managed Streaming Kafka Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-managed-streaming-kafka-parameters-example
- key_count: 8
  name: Amazon Eventbridge Pipes Update Pipe Source Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-parameters-example
- key_count: 3
  name: Amazon Eventbridge Pipes Update Pipe Source Rabbit Mq Broker Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-rabbit-mq-broker-parameters-example
- key_count: 5
  name: Amazon Eventbridge Pipes Update Pipe Source Self Managed Kafka Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-self-managed-kafka-parameters-example
- key_count: 2
  name: Amazon Eventbridge Pipes Update Pipe Source Sqs Queue Parameters Example
  slug: amazon-eventbridge-pipes-update-pipe-source-sqs-queue-parameters-example
- key_count: 0
  name: Amazon Eventbridge Pipes Validation Exception Example
  slug: amazon-eventbridge-pipes-validation-exception-example
features:
- description: Connect event sources directly to targets with minimal code
  name: Point-to-Point Integration
- description: Filter events before processing to reduce costs and noise
  name: Event Filtering
- description: Enrich events with data from Lambda, Step Functions, or API destinations
  name: Event Enrichment
- description: Transform event payloads using input transformers
  name: Event Transformation
- description: Process events in batches for improved throughput
  name: Batching Support
finops:
- name: Amazon Eventbridge Pipes Finops
  service_category: API
  slug: amazon-eventbridge-pipes-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: ArnOrJsonPath
  property_count: 0
  slug: amazon-eventbridge-pipes-arn-or-json-path
- name: ArnOrUrl
  property_count: 0
  slug: amazon-eventbridge-pipes-arn-or-url
- name: Arn
  property_count: 0
  slug: amazon-eventbridge-pipes-arn
- name: AssignPublicIp
  property_count: 0
  slug: amazon-eventbridge-pipes-assign-public-ip
- name: AwsVpcConfiguration
  property_count: 3
  slug: amazon-eventbridge-pipes-aws-vpc-configuration
- name: BatchArrayProperties
  property_count: 1
  slug: amazon-eventbridge-pipes-batch-array-properties
- name: BatchArraySize
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-array-size
- name: BatchContainerOverrides
  property_count: 4
  slug: amazon-eventbridge-pipes-batch-container-overrides
- name: BatchDependsOn
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-depends-on
- name: BatchEnvironmentVariableList
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-environment-variable-list
- name: BatchEnvironmentVariable
  property_count: 2
  slug: amazon-eventbridge-pipes-batch-environment-variable
- name: BatchJobDependency
  property_count: 2
  slug: amazon-eventbridge-pipes-batch-job-dependency
- name: BatchJobDependencyType
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-job-dependency-type
- name: BatchParametersMap
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-parameters-map
- name: BatchResourceRequirement
  property_count: 2
  slug: amazon-eventbridge-pipes-batch-resource-requirement
- name: BatchResourceRequirementType
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-resource-requirement-type
- name: BatchResourceRequirementsList
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-resource-requirements-list
- name: BatchRetryAttempts
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-retry-attempts
- name: BatchRetryStrategy
  property_count: 1
  slug: amazon-eventbridge-pipes-batch-retry-strategy
- name: Boolean
  property_count: 0
  slug: amazon-eventbridge-pipes-boolean
- name: CapacityProvider
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider
- name: CapacityProviderStrategyItemBase
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item-base
- name: CapacityProviderStrategyItem
  property_count: 3
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item
- name: CapacityProviderStrategyItemWeight
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item-weight
- name: CapacityProviderStrategy
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-strategy
- name: ConflictException
  property_count: 0
  slug: amazon-eventbridge-pipes-conflict-exception
- name: CreatePipeRequest
  property_count: 10
  slug: amazon-eventbridge-pipes-create-pipe-request
- name: CreatePipeResponse
  property_count: 6
  slug: amazon-eventbridge-pipes-create-pipe-response
- name: Database
  property_count: 0
  slug: amazon-eventbridge-pipes-database
- name: DbUser
  property_count: 0
  slug: amazon-eventbridge-pipes-db-user
- name: DeadLetterConfig
  property_count: 1
  slug: amazon-eventbridge-pipes-dead-letter-config
- name: DeletePipeRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-delete-pipe-request
- name: DeletePipeResponse
  property_count: 6
  slug: amazon-eventbridge-pipes-delete-pipe-response
- name: DescribePipeRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-describe-pipe-request
- name: DescribePipeResponse
  property_count: 16
  slug: amazon-eventbridge-pipes-describe-pipe-response
- name: DynamoDBStreamStartPosition
  property_count: 0
  slug: amazon-eventbridge-pipes-dynamo-db-stream-start-position
- name: EcsContainerOverrideList
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-container-override-list
- name: EcsContainerOverride
  property_count: 8
  slug: amazon-eventbridge-pipes-ecs-container-override
- name: EcsEnvironmentFileList
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-environment-file-list
- name: EcsEnvironmentFile
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-environment-file
- name: EcsEnvironmentFileType
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-environment-file-type
- name: EcsEnvironmentVariableList
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-environment-variable-list
- name: EcsEnvironmentVariable
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-environment-variable
- name: EcsEphemeralStorage
  property_count: 1
  slug: amazon-eventbridge-pipes-ecs-ephemeral-storage
- name: EcsInferenceAcceleratorOverrideList
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-inference-accelerator-override-list
- name: EcsInferenceAcceleratorOverride
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-inference-accelerator-override
- name: EcsResourceRequirement
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-resource-requirement
- name: EcsResourceRequirementType
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-resource-requirement-type
- name: EcsResourceRequirementsList
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-resource-requirements-list
- name: EcsTaskOverride
  property_count: 7
  slug: amazon-eventbridge-pipes-ecs-task-override
- name: EndpointString
  property_count: 0
  slug: amazon-eventbridge-pipes-endpoint-string
- name: EphemeralStorageSize
  property_count: 0
  slug: amazon-eventbridge-pipes-ephemeral-storage-size
- name: EventBridgeDetailType
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-detail-type
- name: EventBridgeEndpointId
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-endpoint-id
- name: EventBridgeEventResourceList
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-event-resource-list
- name: EventBridgeEventSource
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-event-source
- name: EventPattern
  property_count: 0
  slug: amazon-eventbridge-pipes-event-pattern
- name: FilterCriteria
  property_count: 1
  slug: amazon-eventbridge-pipes-filter-criteria
- name: FilterList
  property_count: 0
  slug: amazon-eventbridge-pipes-filter-list
- name: Filter
  property_count: 1
  slug: amazon-eventbridge-pipes-filter
- name: HeaderKey
  property_count: 0
  slug: amazon-eventbridge-pipes-header-key
- name: HeaderParametersMap
  property_count: 0
  slug: amazon-eventbridge-pipes-header-parameters-map
- name: HeaderValue
  property_count: 0
  slug: amazon-eventbridge-pipes-header-value
- name: InputTemplate
  property_count: 0
  slug: amazon-eventbridge-pipes-input-template
- name: Integer
  property_count: 0
  slug: amazon-eventbridge-pipes-integer
- name: InternalException
  property_count: 0
  slug: amazon-eventbridge-pipes-internal-exception
- name: JsonPath
  property_count: 0
  slug: amazon-eventbridge-pipes-json-path
- name: KafkaBootstrapServers
  property_count: 0
  slug: amazon-eventbridge-pipes-kafka-bootstrap-servers
- name: KafkaTopicName
  property_count: 0
  slug: amazon-eventbridge-pipes-kafka-topic-name
- name: KinesisPartitionKey
  property_count: 0
  slug: amazon-eventbridge-pipes-kinesis-partition-key
- name: KinesisStreamStartPosition
  property_count: 0
  slug: amazon-eventbridge-pipes-kinesis-stream-start-position
- name: LaunchType
  property_count: 0
  slug: amazon-eventbridge-pipes-launch-type
- name: LimitMax10
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-max10
- name: LimitMax100
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-max100
- name: LimitMax10000
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-max10000
- name: LimitMin1
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-min1
- name: ListPipesRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-list-pipes-request
- name: ListPipesResponse
  property_count: 2
  slug: amazon-eventbridge-pipes-list-pipes-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-eventbridge-pipes-list-tags-for-resource-response
- name: LogStreamName
  property_count: 0
  slug: amazon-eventbridge-pipes-log-stream-name
- name: MaximumBatchingWindowInSeconds
  property_count: 0
  slug: amazon-eventbridge-pipes-maximum-batching-window-in-seconds
- name: MaximumRecordAgeInSeconds
  property_count: 0
  slug: amazon-eventbridge-pipes-maximum-record-age-in-seconds
- name: MaximumRetryAttemptsESM
  property_count: 0
  slug: amazon-eventbridge-pipes-maximum-retry-attempts-esm
- name: MessageDeduplicationId
  property_count: 0
  slug: amazon-eventbridge-pipes-message-deduplication-id
- name: MessageGroupId
  property_count: 0
  slug: amazon-eventbridge-pipes-message-group-id
- name: MQBrokerAccessCredentials
  property_count: 1
  slug: amazon-eventbridge-pipes-mq-broker-access-credentials
- name: MQBrokerQueueName
  property_count: 0
  slug: amazon-eventbridge-pipes-mq-broker-queue-name
- name: MSKAccessCredentials
  property_count: 2
  slug: amazon-eventbridge-pipes-msk-access-credentials
- name: MSKStartPosition
  property_count: 0
  slug: amazon-eventbridge-pipes-msk-start-position
- name: NetworkConfiguration
  property_count: 1
  slug: amazon-eventbridge-pipes-network-configuration
- name: NextToken
  property_count: 0
  slug: amazon-eventbridge-pipes-next-token
- name: NotFoundException
  property_count: 0
  slug: amazon-eventbridge-pipes-not-found-exception
- name: OnPartialBatchItemFailureStreams
  property_count: 0
  slug: amazon-eventbridge-pipes-on-partial-batch-item-failure-streams
- name: OptionalArn
  property_count: 0
  slug: amazon-eventbridge-pipes-optional-arn
- name: PathParameterList
  property_count: 0
  slug: amazon-eventbridge-pipes-path-parameter-list
- name: PathParameter
  property_count: 0
  slug: amazon-eventbridge-pipes-path-parameter
- name: PipeArn
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-arn
- name: PipeDescription
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-description
- name: PipeEnrichmentHttpParameters
  property_count: 3
  slug: amazon-eventbridge-pipes-pipe-enrichment-http-parameters
- name: PipeEnrichmentParameters
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-enrichment-parameters
- name: PipeList
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-list
- name: PipeName
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-name
- name: Pipe
  property_count: 10
  slug: amazon-eventbridge-pipes-pipe
- name: PipeSourceActiveMQBrokerParameters
  property_count: 4
  slug: amazon-eventbridge-pipes-pipe-source-active-mq-broker-parameters
- name: PipeSourceDynamoDBStreamParameters
  property_count: 8
  slug: amazon-eventbridge-pipes-pipe-source-dynamo-db-stream-parameters
- name: PipeSourceKinesisStreamParameters
  property_count: 9
  slug: amazon-eventbridge-pipes-pipe-source-kinesis-stream-parameters
- name: PipeSourceManagedStreamingKafkaParameters
  property_count: 6
  slug: amazon-eventbridge-pipes-pipe-source-managed-streaming-kafka-parameters
- name: PipeSourceParameters
  property_count: 8
  slug: amazon-eventbridge-pipes-pipe-source-parameters
- name: PipeSourceRabbitMQBrokerParameters
  property_count: 5
  slug: amazon-eventbridge-pipes-pipe-source-rabbit-mq-broker-parameters
- name: PipeSourceSelfManagedKafkaParameters
  property_count: 9
  slug: amazon-eventbridge-pipes-pipe-source-self-managed-kafka-parameters
- name: PipeSourceSqsQueueParameters
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-source-sqs-queue-parameters
- name: PipeStateReason
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-state-reason
- name: PipeState
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-state
- name: PipeTargetBatchJobParameters
  property_count: 7
  slug: amazon-eventbridge-pipes-pipe-target-batch-job-parameters
- name: PipeTargetCloudWatchLogsParameters
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-target-cloud-watch-logs-parameters
- name: PipeTargetEcsTaskParameters
  property_count: 15
  slug: amazon-eventbridge-pipes-pipe-target-ecs-task-parameters
- name: PipeTargetEventBridgeEventBusParameters
  property_count: 5
  slug: amazon-eventbridge-pipes-pipe-target-event-bridge-event-bus-parameters
- name: PipeTargetHttpParameters
  property_count: 3
  slug: amazon-eventbridge-pipes-pipe-target-http-parameters
- name: PipeTargetInvocationType
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-target-invocation-type
- name: PipeTargetKinesisStreamParameters
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-kinesis-stream-parameters
- name: PipeTargetLambdaFunctionParameters
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-lambda-function-parameters
- name: PipeTargetParameters
  property_count: 12
  slug: amazon-eventbridge-pipes-pipe-target-parameters
- name: PipeTargetRedshiftDataParameters
  property_count: 6
  slug: amazon-eventbridge-pipes-pipe-target-redshift-data-parameters
- name: PipeTargetSageMakerPipelineParameters
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-sage-maker-pipeline-parameters
- name: PipeTargetSqsQueueParameters
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-target-sqs-queue-parameters
- name: PipeTargetStateMachineParameters
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-state-machine-parameters
- name: PlacementConstraintExpression
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-constraint-expression
- name: PlacementConstraint
  property_count: 2
  slug: amazon-eventbridge-pipes-placement-constraint
- name: PlacementConstraintType
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-constraint-type
- name: PlacementConstraints
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-constraints
- name: PlacementStrategies
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-strategies
- name: PlacementStrategyField
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-strategy-field
- name: PlacementStrategy
  property_count: 2
  slug: amazon-eventbridge-pipes-placement-strategy
- name: PlacementStrategyType
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-strategy-type
- name: PropagateTags
  property_count: 0
  slug: amazon-eventbridge-pipes-propagate-tags
- name: QueryStringKey
  property_count: 0
  slug: amazon-eventbridge-pipes-query-string-key
- name: QueryStringParametersMap
  property_count: 0
  slug: amazon-eventbridge-pipes-query-string-parameters-map
- name: QueryStringValue
  property_count: 0
  slug: amazon-eventbridge-pipes-query-string-value
- name: ReferenceId
  property_count: 0
  slug: amazon-eventbridge-pipes-reference-id
- name: RequestedPipeStateDescribeResponse
  property_count: 0
  slug: amazon-eventbridge-pipes-requested-pipe-state-describe-response
- name: RequestedPipeState
  property_count: 0
  slug: amazon-eventbridge-pipes-requested-pipe-state
- name: ResourceArn
  property_count: 0
  slug: amazon-eventbridge-pipes-resource-arn
- name: RoleArn
  property_count: 0
  slug: amazon-eventbridge-pipes-role-arn
- name: SageMakerPipelineParameterList
  property_count: 0
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-list
- name: SageMakerPipelineParameterName
  property_count: 0
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-name
- name: SageMakerPipelineParameter
  property_count: 2
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter
- name: SageMakerPipelineParameterValue
  property_count: 0
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-value
- name: SecretManagerArnOrJsonPath
  property_count: 0
  slug: amazon-eventbridge-pipes-secret-manager-arn-or-json-path
- name: SecretManagerArn
  property_count: 0
  slug: amazon-eventbridge-pipes-secret-manager-arn
- name: SecurityGroupId
  property_count: 0
  slug: amazon-eventbridge-pipes-security-group-id
- name: SecurityGroupIds
  property_count: 0
  slug: amazon-eventbridge-pipes-security-group-ids
- name: SecurityGroup
  property_count: 0
  slug: amazon-eventbridge-pipes-security-group
- name: SecurityGroups
  property_count: 0
  slug: amazon-eventbridge-pipes-security-groups
- name: SelfManagedKafkaAccessConfigurationCredentials
  property_count: 4
  slug: amazon-eventbridge-pipes-self-managed-kafka-access-configuration-credentials
- name: SelfManagedKafkaAccessConfigurationVpc
  property_count: 2
  slug: amazon-eventbridge-pipes-self-managed-kafka-access-configuration-vpc
- name: SelfManagedKafkaStartPosition
  property_count: 0
  slug: amazon-eventbridge-pipes-self-managed-kafka-start-position
- name: ServiceQuotaExceededException
  property_count: 0
  slug: amazon-eventbridge-pipes-service-quota-exceeded-exception
- name: Sql
  property_count: 0
  slug: amazon-eventbridge-pipes-sql
- name: Sqls
  property_count: 0
  slug: amazon-eventbridge-pipes-sqls
- name: StartPipeRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-start-pipe-request
- name: StartPipeResponse
  property_count: 6
  slug: amazon-eventbridge-pipes-start-pipe-response
- name: StatementName
  property_count: 0
  slug: amazon-eventbridge-pipes-statement-name
- name: StopPipeRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-stop-pipe-request
- name: StopPipeResponse
  property_count: 6
  slug: amazon-eventbridge-pipes-stop-pipe-response
- name: StringList
  property_count: 0
  slug: amazon-eventbridge-pipes-string-list
- name: String
  property_count: 0
  slug: amazon-eventbridge-pipes-string
- name: SubnetId
  property_count: 0
  slug: amazon-eventbridge-pipes-subnet-id
- name: SubnetIds
  property_count: 0
  slug: amazon-eventbridge-pipes-subnet-ids
- name: Subnet
  property_count: 0
  slug: amazon-eventbridge-pipes-subnet
- name: Subnets
  property_count: 0
  slug: amazon-eventbridge-pipes-subnets
- name: TagKeyList
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-key-list
- name: TagKey
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-key
- name: TagList
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-list
- name: TagMap
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: amazon-eventbridge-pipes-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-resource-response
- name: Tag
  property_count: 2
  slug: amazon-eventbridge-pipes-tag
- name: TagValue
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-value
- name: ThrottlingException
  property_count: 0
  slug: amazon-eventbridge-pipes-throttling-exception
- name: Timestamp
  property_count: 0
  slug: amazon-eventbridge-pipes-timestamp
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-eventbridge-pipes-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-eventbridge-pipes-untag-resource-response
- name: UpdatePipeRequest
  property_count: 8
  slug: amazon-eventbridge-pipes-update-pipe-request
- name: UpdatePipeResponse
  property_count: 6
  slug: amazon-eventbridge-pipes-update-pipe-response
- name: UpdatePipeSourceActiveMQBrokerParameters
  property_count: 3
  slug: amazon-eventbridge-pipes-update-pipe-source-active-mq-broker-parameters
- name: UpdatePipeSourceDynamoDBStreamParameters
  property_count: 7
  slug: amazon-eventbridge-pipes-update-pipe-source-dynamo-db-stream-parameters
- name: UpdatePipeSourceKinesisStreamParameters
  property_count: 7
  slug: amazon-eventbridge-pipes-update-pipe-source-kinesis-stream-parameters
- name: UpdatePipeSourceManagedStreamingKafkaParameters
  property_count: 3
  slug: amazon-eventbridge-pipes-update-pipe-source-managed-streaming-kafka-parameters
- name: UpdatePipeSourceParameters
  property_count: 8
  slug: amazon-eventbridge-pipes-update-pipe-source-parameters
- name: UpdatePipeSourceRabbitMQBrokerParameters
  property_count: 3
  slug: amazon-eventbridge-pipes-update-pipe-source-rabbit-mq-broker-parameters
- name: UpdatePipeSourceSelfManagedKafkaParameters
  property_count: 5
  slug: amazon-eventbridge-pipes-update-pipe-source-self-managed-kafka-parameters
- name: UpdatePipeSourceSqsQueueParameters
  property_count: 2
  slug: amazon-eventbridge-pipes-update-pipe-source-sqs-queue-parameters
- name: URI
  property_count: 0
  slug: amazon-eventbridge-pipes-uri
- name: ValidationException
  property_count: 0
  slug: amazon-eventbridge-pipes-validation-exception
json_structures:
- name: Amazon Eventbridge Pipes Arn Or Json Path Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-arn-or-json-path-structure
- name: Amazon Eventbridge Pipes Arn Or Url Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-arn-or-url-structure
- name: Amazon Eventbridge Pipes Arn Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-arn-structure
- name: Amazon Eventbridge Pipes Assign Public Ip Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-assign-public-ip-structure
- name: Amazon Eventbridge Pipes Aws Vpc Configuration Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-aws-vpc-configuration-structure
- name: Amazon Eventbridge Pipes Batch Array Properties Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-batch-array-properties-structure
- name: Amazon Eventbridge Pipes Batch Array Size Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-array-size-structure
- name: Amazon Eventbridge Pipes Batch Container Overrides Structure
  property_count: 4
  slug: amazon-eventbridge-pipes-batch-container-overrides-structure
- name: Amazon Eventbridge Pipes Batch Depends On Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-depends-on-structure
- name: Amazon Eventbridge Pipes Batch Environment Variable List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-environment-variable-list-structure
- name: Amazon Eventbridge Pipes Batch Environment Variable Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-batch-environment-variable-structure
- name: Amazon Eventbridge Pipes Batch Job Dependency Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-batch-job-dependency-structure
- name: Amazon Eventbridge Pipes Batch Job Dependency Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-job-dependency-type-structure
- name: Amazon Eventbridge Pipes Batch Parameters Map Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-parameters-map-structure
- name: Amazon Eventbridge Pipes Batch Resource Requirement Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-batch-resource-requirement-structure
- name: Amazon Eventbridge Pipes Batch Resource Requirement Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-resource-requirement-type-structure
- name: Amazon Eventbridge Pipes Batch Resource Requirements List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-resource-requirements-list-structure
- name: Amazon Eventbridge Pipes Batch Retry Attempts Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-batch-retry-attempts-structure
- name: Amazon Eventbridge Pipes Batch Retry Strategy Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-batch-retry-strategy-structure
- name: Amazon Eventbridge Pipes Boolean Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-boolean-structure
- name: Amazon Eventbridge Pipes Capacity Provider Strategy Item Base Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item-base-structure
- name: Amazon Eventbridge Pipes Capacity Provider Strategy Item Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item-structure
- name: Amazon Eventbridge Pipes Capacity Provider Strategy Item Weight Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-item-weight-structure
- name: Amazon Eventbridge Pipes Capacity Provider Strategy Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-strategy-structure
- name: Amazon Eventbridge Pipes Capacity Provider Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-capacity-provider-structure
- name: Amazon Eventbridge Pipes Conflict Exception Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-conflict-exception-structure
- name: Amazon Eventbridge Pipes Create Pipe Request Structure
  property_count: 10
  slug: amazon-eventbridge-pipes-create-pipe-request-structure
- name: Amazon Eventbridge Pipes Create Pipe Response Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-create-pipe-response-structure
- name: Amazon Eventbridge Pipes Database Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-database-structure
- name: Amazon Eventbridge Pipes Db User Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-db-user-structure
- name: Amazon Eventbridge Pipes Dead Letter Config Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-dead-letter-config-structure
- name: Amazon Eventbridge Pipes Delete Pipe Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-delete-pipe-request-structure
- name: Amazon Eventbridge Pipes Delete Pipe Response Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-delete-pipe-response-structure
- name: Amazon Eventbridge Pipes Describe Pipe Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-describe-pipe-request-structure
- name: Amazon Eventbridge Pipes Describe Pipe Response Structure
  property_count: 16
  slug: amazon-eventbridge-pipes-describe-pipe-response-structure
- name: Amazon Eventbridge Pipes Dynamo Db Stream Start Position Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-dynamo-db-stream-start-position-structure
- name: Amazon Eventbridge Pipes Ecs Container Override List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-container-override-list-structure
- name: Amazon Eventbridge Pipes Ecs Container Override Structure
  property_count: 8
  slug: amazon-eventbridge-pipes-ecs-container-override-structure
- name: Amazon Eventbridge Pipes Ecs Environment File List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-environment-file-list-structure
- name: Amazon Eventbridge Pipes Ecs Environment File Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-environment-file-structure
- name: Amazon Eventbridge Pipes Ecs Environment File Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-environment-file-type-structure
- name: Amazon Eventbridge Pipes Ecs Environment Variable List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-environment-variable-list-structure
- name: Amazon Eventbridge Pipes Ecs Environment Variable Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-environment-variable-structure
- name: Amazon Eventbridge Pipes Ecs Ephemeral Storage Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-ecs-ephemeral-storage-structure
- name: Amazon Eventbridge Pipes Ecs Inference Accelerator Override List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-inference-accelerator-override-list-structure
- name: Amazon Eventbridge Pipes Ecs Inference Accelerator Override Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-inference-accelerator-override-structure
- name: Amazon Eventbridge Pipes Ecs Resource Requirement Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-ecs-resource-requirement-structure
- name: Amazon Eventbridge Pipes Ecs Resource Requirement Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-resource-requirement-type-structure
- name: Amazon Eventbridge Pipes Ecs Resource Requirements List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ecs-resource-requirements-list-structure
- name: Amazon Eventbridge Pipes Ecs Task Override Structure
  property_count: 7
  slug: amazon-eventbridge-pipes-ecs-task-override-structure
- name: Amazon Eventbridge Pipes Endpoint String Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-endpoint-string-structure
- name: Amazon Eventbridge Pipes Ephemeral Storage Size Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-ephemeral-storage-size-structure
- name: Amazon Eventbridge Pipes Event Bridge Detail Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-detail-type-structure
- name: Amazon Eventbridge Pipes Event Bridge Endpoint Id Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-endpoint-id-structure
- name: Amazon Eventbridge Pipes Event Bridge Event Resource List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-event-resource-list-structure
- name: Amazon Eventbridge Pipes Event Bridge Event Source Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-event-bridge-event-source-structure
- name: Amazon Eventbridge Pipes Event Pattern Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-event-pattern-structure
- name: Amazon Eventbridge Pipes Filter Criteria Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-filter-criteria-structure
- name: Amazon Eventbridge Pipes Filter List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-filter-list-structure
- name: Amazon Eventbridge Pipes Filter Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-filter-structure
- name: Amazon Eventbridge Pipes Header Key Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-header-key-structure
- name: Amazon Eventbridge Pipes Header Parameters Map Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-header-parameters-map-structure
- name: Amazon Eventbridge Pipes Header Value Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-header-value-structure
- name: Amazon Eventbridge Pipes Input Template Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-input-template-structure
- name: Amazon Eventbridge Pipes Integer Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-integer-structure
- name: Amazon Eventbridge Pipes Internal Exception Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-internal-exception-structure
- name: Amazon Eventbridge Pipes Json Path Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-json-path-structure
- name: Amazon Eventbridge Pipes Kafka Bootstrap Servers Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-kafka-bootstrap-servers-structure
- name: Amazon Eventbridge Pipes Kafka Topic Name Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-kafka-topic-name-structure
- name: Amazon Eventbridge Pipes Kinesis Partition Key Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-kinesis-partition-key-structure
- name: Amazon Eventbridge Pipes Kinesis Stream Start Position Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-kinesis-stream-start-position-structure
- name: Amazon Eventbridge Pipes Launch Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-launch-type-structure
- name: Amazon Eventbridge Pipes Limit Max10 Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-max10-structure
- name: Amazon Eventbridge Pipes Limit Max100 Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-max100-structure
- name: Amazon Eventbridge Pipes Limit Max10000 Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-max10000-structure
- name: Amazon Eventbridge Pipes Limit Min1 Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-limit-min1-structure
- name: Amazon Eventbridge Pipes List Pipes Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-list-pipes-request-structure
- name: Amazon Eventbridge Pipes List Pipes Response Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-list-pipes-response-structure
- name: Amazon Eventbridge Pipes List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-list-tags-for-resource-request-structure
- name: Amazon Eventbridge Pipes List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-list-tags-for-resource-response-structure
- name: Amazon Eventbridge Pipes Log Stream Name Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-log-stream-name-structure
- name: Amazon Eventbridge Pipes Maximum Batching Window In Seconds Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-maximum-batching-window-in-seconds-structure
- name: Amazon Eventbridge Pipes Maximum Record Age In Seconds Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-maximum-record-age-in-seconds-structure
- name: Amazon Eventbridge Pipes Maximum Retry Attempts Esm Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-maximum-retry-attempts-esm-structure
- name: Amazon Eventbridge Pipes Message Deduplication Id Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-message-deduplication-id-structure
- name: Amazon Eventbridge Pipes Message Group Id Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-message-group-id-structure
- name: Amazon Eventbridge Pipes Mq Broker Access Credentials Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-mq-broker-access-credentials-structure
- name: Amazon Eventbridge Pipes Mq Broker Queue Name Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-mq-broker-queue-name-structure
- name: Amazon Eventbridge Pipes Msk Access Credentials Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-msk-access-credentials-structure
- name: Amazon Eventbridge Pipes Msk Start Position Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-msk-start-position-structure
- name: Amazon Eventbridge Pipes Network Configuration Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-network-configuration-structure
- name: Amazon Eventbridge Pipes Next Token Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-next-token-structure
- name: Amazon Eventbridge Pipes Not Found Exception Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-not-found-exception-structure
- name: Amazon Eventbridge Pipes On Partial Batch Item Failure Streams Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-on-partial-batch-item-failure-streams-structure
- name: Amazon Eventbridge Pipes Optional Arn Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-optional-arn-structure
- name: Amazon Eventbridge Pipes Path Parameter List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-path-parameter-list-structure
- name: Amazon Eventbridge Pipes Path Parameter Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-path-parameter-structure
- name: Amazon Eventbridge Pipes Pipe Arn Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-arn-structure
- name: Amazon Eventbridge Pipes Pipe Description Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-description-structure
- name: Amazon Eventbridge Pipes Pipe Enrichment Http Parameters Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-pipe-enrichment-http-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Enrichment Parameters Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-enrichment-parameters-structure
- name: Amazon Eventbridge Pipes Pipe List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-list-structure
- name: Amazon Eventbridge Pipes Pipe Name Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-name-structure
- name: Amazon Eventbridge Pipes Pipe Source Active Mq Broker Parameters Structure
  property_count: 4
  slug: amazon-eventbridge-pipes-pipe-source-active-mq-broker-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Dynamo Db Stream Parameters Structure
  property_count: 8
  slug: amazon-eventbridge-pipes-pipe-source-dynamo-db-stream-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Kinesis Stream Parameters Structure
  property_count: 9
  slug: amazon-eventbridge-pipes-pipe-source-kinesis-stream-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Managed Streaming Kafka Parameters Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-pipe-source-managed-streaming-kafka-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Parameters Structure
  property_count: 8
  slug: amazon-eventbridge-pipes-pipe-source-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Rabbit Mq Broker Parameters Structure
  property_count: 5
  slug: amazon-eventbridge-pipes-pipe-source-rabbit-mq-broker-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Self Managed Kafka Parameters Structure
  property_count: 9
  slug: amazon-eventbridge-pipes-pipe-source-self-managed-kafka-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Source Sqs Queue Parameters Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-source-sqs-queue-parameters-structure
- name: Amazon Eventbridge Pipes Pipe State Reason Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-state-reason-structure
- name: Amazon Eventbridge Pipes Pipe State Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-state-structure
- name: Amazon Eventbridge Pipes Pipe Structure
  property_count: 10
  slug: amazon-eventbridge-pipes-pipe-structure
- name: Amazon Eventbridge Pipes Pipe Target Batch Job Parameters Structure
  property_count: 7
  slug: amazon-eventbridge-pipes-pipe-target-batch-job-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Cloud Watch Logs Parameters Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-target-cloud-watch-logs-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Ecs Task Parameters Structure
  property_count: 15
  slug: amazon-eventbridge-pipes-pipe-target-ecs-task-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Event Bridge Event Bus Parameters Structure
  property_count: 5
  slug: amazon-eventbridge-pipes-pipe-target-event-bridge-event-bus-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Http Parameters Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-pipe-target-http-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Invocation Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-pipe-target-invocation-type-structure
- name: Amazon Eventbridge Pipes Pipe Target Kinesis Stream Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-kinesis-stream-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Lambda Function Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-lambda-function-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Parameters Structure
  property_count: 12
  slug: amazon-eventbridge-pipes-pipe-target-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Redshift Data Parameters Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-pipe-target-redshift-data-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Sage Maker Pipeline Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-sage-maker-pipeline-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target Sqs Queue Parameters Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-pipe-target-sqs-queue-parameters-structure
- name: Amazon Eventbridge Pipes Pipe Target State Machine Parameters Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-pipe-target-state-machine-parameters-structure
- name: Amazon Eventbridge Pipes Placement Constraint Expression Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-constraint-expression-structure
- name: Amazon Eventbridge Pipes Placement Constraint Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-placement-constraint-structure
- name: Amazon Eventbridge Pipes Placement Constraint Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-constraint-type-structure
- name: Amazon Eventbridge Pipes Placement Constraints Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-constraints-structure
- name: Amazon Eventbridge Pipes Placement Strategies Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-strategies-structure
- name: Amazon Eventbridge Pipes Placement Strategy Field Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-strategy-field-structure
- name: Amazon Eventbridge Pipes Placement Strategy Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-placement-strategy-structure
- name: Amazon Eventbridge Pipes Placement Strategy Type Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-placement-strategy-type-structure
- name: Amazon Eventbridge Pipes Propagate Tags Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-propagate-tags-structure
- name: Amazon Eventbridge Pipes Query String Key Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-query-string-key-structure
- name: Amazon Eventbridge Pipes Query String Parameters Map Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-query-string-parameters-map-structure
- name: Amazon Eventbridge Pipes Query String Value Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-query-string-value-structure
- name: Amazon Eventbridge Pipes Reference Id Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-reference-id-structure
- name: Amazon Eventbridge Pipes Requested Pipe State Describe Response Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-requested-pipe-state-describe-response-structure
- name: Amazon Eventbridge Pipes Requested Pipe State Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-requested-pipe-state-structure
- name: Amazon Eventbridge Pipes Resource Arn Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-resource-arn-structure
- name: Amazon Eventbridge Pipes Role Arn Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-role-arn-structure
- name: Amazon Eventbridge Pipes Sage Maker Pipeline Parameter List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-list-structure
- name: Amazon Eventbridge Pipes Sage Maker Pipeline Parameter Name Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-name-structure
- name: Amazon Eventbridge Pipes Sage Maker Pipeline Parameter Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-structure
- name: Amazon Eventbridge Pipes Sage Maker Pipeline Parameter Value Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-sage-maker-pipeline-parameter-value-structure
- name: Amazon Eventbridge Pipes Secret Manager Arn Or Json Path Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-secret-manager-arn-or-json-path-structure
- name: Amazon Eventbridge Pipes Secret Manager Arn Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-secret-manager-arn-structure
- name: Amazon Eventbridge Pipes Security Group Id Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-security-group-id-structure
- name: Amazon Eventbridge Pipes Security Group Ids Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-security-group-ids-structure
- name: Amazon Eventbridge Pipes Security Group Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-security-group-structure
- name: Amazon Eventbridge Pipes Security Groups Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-security-groups-structure
- name: Amazon Eventbridge Pipes Self Managed Kafka Access Configuration Credentials Structure
  property_count: 4
  slug: amazon-eventbridge-pipes-self-managed-kafka-access-configuration-credentials-structure
- name: Amazon Eventbridge Pipes Self Managed Kafka Access Configuration Vpc Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-self-managed-kafka-access-configuration-vpc-structure
- name: Amazon Eventbridge Pipes Self Managed Kafka Start Position Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-self-managed-kafka-start-position-structure
- name: Amazon Eventbridge Pipes Service Quota Exceeded Exception Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-service-quota-exceeded-exception-structure
- name: Amazon Eventbridge Pipes Sql Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-sql-structure
- name: Amazon Eventbridge Pipes Sqls Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-sqls-structure
- name: Amazon Eventbridge Pipes Start Pipe Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-start-pipe-request-structure
- name: Amazon Eventbridge Pipes Start Pipe Response Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-start-pipe-response-structure
- name: Amazon Eventbridge Pipes Statement Name Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-statement-name-structure
- name: Amazon Eventbridge Pipes Stop Pipe Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-stop-pipe-request-structure
- name: Amazon Eventbridge Pipes Stop Pipe Response Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-stop-pipe-response-structure
- name: Amazon Eventbridge Pipes String List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-string-list-structure
- name: Amazon Eventbridge Pipes String Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-string-structure
- name: Amazon Eventbridge Pipes Subnet Id Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-subnet-id-structure
- name: Amazon Eventbridge Pipes Subnet Ids Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-subnet-ids-structure
- name: Amazon Eventbridge Pipes Subnet Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-subnet-structure
- name: Amazon Eventbridge Pipes Subnets Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-subnets-structure
- name: Amazon Eventbridge Pipes Tag Key List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-key-list-structure
- name: Amazon Eventbridge Pipes Tag Key Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-key-structure
- name: Amazon Eventbridge Pipes Tag List Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-list-structure
- name: Amazon Eventbridge Pipes Tag Map Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-map-structure
- name: Amazon Eventbridge Pipes Tag Resource Request Structure
  property_count: 1
  slug: amazon-eventbridge-pipes-tag-resource-request-structure
- name: Amazon Eventbridge Pipes Tag Resource Response Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-resource-response-structure
- name: Amazon Eventbridge Pipes Tag Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-tag-structure
- name: Amazon Eventbridge Pipes Tag Value Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-tag-value-structure
- name: Amazon Eventbridge Pipes Throttling Exception Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-throttling-exception-structure
- name: Amazon Eventbridge Pipes Timestamp Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-timestamp-structure
- name: Amazon Eventbridge Pipes Untag Resource Request Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-untag-resource-request-structure
- name: Amazon Eventbridge Pipes Untag Resource Response Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-untag-resource-response-structure
- name: Amazon Eventbridge Pipes Update Pipe Request Structure
  property_count: 8
  slug: amazon-eventbridge-pipes-update-pipe-request-structure
- name: Amazon Eventbridge Pipes Update Pipe Response Structure
  property_count: 6
  slug: amazon-eventbridge-pipes-update-pipe-response-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Active Mq Broker Parameters Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-update-pipe-source-active-mq-broker-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Dynamo Db Stream Parameters Structure
  property_count: 7
  slug: amazon-eventbridge-pipes-update-pipe-source-dynamo-db-stream-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Kinesis Stream Parameters Structure
  property_count: 7
  slug: amazon-eventbridge-pipes-update-pipe-source-kinesis-stream-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Managed Streaming Kafka Parameters Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-update-pipe-source-managed-streaming-kafka-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Parameters Structure
  property_count: 8
  slug: amazon-eventbridge-pipes-update-pipe-source-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Rabbit Mq Broker Parameters Structure
  property_count: 3
  slug: amazon-eventbridge-pipes-update-pipe-source-rabbit-mq-broker-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Self Managed Kafka Parameters Structure
  property_count: 5
  slug: amazon-eventbridge-pipes-update-pipe-source-self-managed-kafka-parameters-structure
- name: Amazon Eventbridge Pipes Update Pipe Source Sqs Queue Parameters Structure
  property_count: 2
  slug: amazon-eventbridge-pipes-update-pipe-source-sqs-queue-parameters-structure
- name: Amazon Eventbridge Pipes Uri Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-uri-structure
- name: Amazon Eventbridge Pipes Validation Exception Structure
  property_count: 0
  slug: amazon-eventbridge-pipes-validation-exception-structure
jsonld:
- class_count: 83
  name: Amazon Eventbridge Pipes Context
  property_count: 130
  slug: amazon-eventbridge-pipes-context
layout: provider
modified: '2026-05-19'
name: Amazon EventBridge Pipes
nav: Providers
network: true
overview: 'Amazon EventBridge Pipes publishes 2 APIs on the [APIs.io](https://apis.io/) network: Pipes API and Tags API. Tagged areas include Amazon Web Services, Event-Driven, Integration, Messaging, and Serverless.


  The Amazon EventBridge Pipes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EventBridge Pipes'' developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 26 more developer resources.'
plans:
- name: Amazon Eventbridge Pipes Plans Pricing
  plan_count: 3
  slug: amazon-eventbridge-pipes-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Amazon Eventbridge Pipes Rate Limits
  slug: amazon-eventbridge-pipes-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon EventBridge Pipes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-eventbridge-pipes-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon EventBridge Pipes API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-eventbridge-pipes-spectral-rules
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
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-eventbridge-pipes/refs/heads/main/screenshots/amazon-eventbridge-pipes-2026-06-20T171645.png
security:
- kind: authentication
  name: Amazon Eventbridge Pipes Authentication
  slug: amazon-eventbridge-pipes-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Eventbridge Pipes Domain Security
  slug: amazon-eventbridge-pipes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Eventbridge Pipes Vulnerability Disclosure
  slug: amazon-eventbridge-pipes-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Eventbridge Pipes Trust Center
  slug: amazon-eventbridge-pipes-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-eventbridge-pipes
tags:
- Amazon Web Services
- Event-Driven
- Integration
- Messaging
- Serverless
use_cases:
- description: Stream DynamoDB or Aurora changes to downstream systems
  name: Database Change Data Capture
- description: Connect SQS queues to Lambda or Step Functions for message processing
  name: Queue Processing
- description: Process Kinesis or Kafka streams with filtering and enrichment
  name: Stream Analytics
- description: Connect SaaS event sources to AWS targets without custom code
  name: SaaS Integration
website: https://aws.amazon.com/eventbridge/
---
