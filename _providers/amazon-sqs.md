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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Amazon Sqs Agentic Access
  operation_count: 23
  slug: amazon-sqs-agentic-access
  summary_line: 23 operations · 16 acting
api_count: 1
apis:
- description: Operations for sending, receiving, and deleting messages in SQS queues
  name: Amazon SQS Messages API
  slug: amazon-sqs-messages-api
- description: Operations for managing queue access permissions
  name: Amazon SQS Permissions API
  slug: amazon-sqs-permissions-api
- description: Operations for creating, managing, and deleting SQS queues
  name: Amazon SQS Queues API
  slug: amazon-sqs-queues-api
- description: The Tags API from Amazon SQS — 1 operation(s) for tags.
  name: Amazon SQS Tags API
  slug: amazon-sqs-tags-api
artifact_total: 100
asyncapis:
- description: AsyncAPI specification for Amazon SQS event-driven messaging patterns. Amazon SQS provides reliable, highly-scalable hosted queues for storing messages as they travel between applications or microserv
  name: Amazon Simple Queue Service (SQS) Event Source Mapping
  slug: amazon-sqs-asyncapi
collections:
- collection_type: postman
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages API
  slug: postman-amazon-sqs-messages-api
- collection_type: postman
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages Permissions API
  slug: postman-amazon-sqs-permissions-api
- collection_type: postman
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages Queues API
  slug: postman-amazon-sqs-queues-api
- collection_type: postman
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages Tags API
  slug: postman-amazon-sqs-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages API
  slug: open-amazon-sqs-messages-api
- collection_type: open
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages Permissions API
  slug: open-amazon-sqs-permissions-api
- collection_type: open
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages Queues API
  slug: open-amazon-sqs-queues-api
- collection_type: open
  name: Amazon SQS Amazon Simple Queue Service (SQS) Messages Tags API
  slug: open-amazon-sqs-tags-api
- collection_type: open
  name: Amazon SQS Amazon Simple Queue Service (SQS) API
  slug: open-amazon-sqs
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-sqs/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-sqs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-sqs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-sqs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-sqs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-sqs-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/sqs/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
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
  url: https://console.aws.amazon.com/support/home
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_code_examples.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/awsdocs/aws-doc-sdk-examples
created: '2024-01-01'
description: Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.
examples:
- key_count: 4
  name: Amazon Sqs Batch Result Error Entry Example
  slug: amazon-sqs-batch-result-error-entry-example
- key_count: 1
  name: Amazon Sqs Cancel Message Move Task Response Example
  slug: amazon-sqs-cancel-message-move-task-response-example
- key_count: 1
  name: Amazon Sqs Change Message Visibility Batch Response Example
  slug: amazon-sqs-change-message-visibility-batch-response-example
- key_count: 1
  name: Amazon Sqs Create Queue Response Example
  slug: amazon-sqs-create-queue-response-example
- key_count: 1
  name: Amazon Sqs Delete Message Batch Response Example
  slug: amazon-sqs-delete-message-batch-response-example
- key_count: 2
  name: Amazon Sqs Error Response Example
  slug: amazon-sqs-error-response-example
- key_count: 0
  name: Amazon Sqs Generic Response Example
  slug: amazon-sqs-generic-response-example
- key_count: 1
  name: Amazon Sqs Get Queue Attributes Response Example
  slug: amazon-sqs-get-queue-attributes-response-example
- key_count: 1
  name: Amazon Sqs Get Queue Url Response Example
  slug: amazon-sqs-get-queue-url-response-example
- key_count: 1
  name: Amazon Sqs List Dead Letter Source Queues Response Example
  slug: amazon-sqs-list-dead-letter-source-queues-response-example
- key_count: 1
  name: Amazon Sqs List Message Move Tasks Response Example
  slug: amazon-sqs-list-message-move-tasks-response-example
- key_count: 1
  name: Amazon Sqs List Queue Tags Response Example
  slug: amazon-sqs-list-queue-tags-response-example
- key_count: 1
  name: Amazon Sqs List Queues Response Example
  slug: amazon-sqs-list-queues-response-example
- key_count: 6
  name: Amazon Sqs Message Example
  slug: amazon-sqs-message-example
- key_count: 1
  name: Amazon Sqs Receive Message Response Example
  slug: amazon-sqs-receive-message-response-example
- key_count: 1
  name: Amazon Sqs Response Metadata Example
  slug: amazon-sqs-response-metadata-example
- key_count: 1
  name: Amazon Sqs Send Message Batch Response Example
  slug: amazon-sqs-send-message-batch-response-example
- key_count: 1
  name: Amazon Sqs Send Message Response Example
  slug: amazon-sqs-send-message-response-example
- key_count: 1
  name: Amazon Sqs Start Message Move Task Response Example
  slug: amazon-sqs-start-message-move-task-response-example
features:
- description: Maximum throughput, best-effort ordering, and at-least-once delivery for high-volume messaging workloads.
  name: Standard Queues
- description: Exactly-once processing and strict ordering guarantees for applications requiring message sequence preservation.
  name: FIFO Queues
- description: Automatic routing of failed messages to dead-letter queues for debugging and reprocessing.
  name: Dead-Letter Queues
- description: Bulk movement of messages between queues for reprocessing dead-letter queue contents.
  name: Message Move Tasks
- description: Automatic encryption of messages at rest using AWS KMS keys for data protection.
  name: Server-Side Encryption
- description: Reduced API costs and latency by allowing consumers to wait for messages to arrive before responding.
  name: Long Polling
finops:
- name: Amazon Sqs Finops
  service_category: API
  slug: amazon-sqs-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Automatically invoke Lambda functions when messages arrive in SQS queues for serverless processing.
  name: AWS Lambda
- description: Fan out SNS notifications to multiple SQS queues for parallel processing of published messages.
  name: Amazon SNS
- description: Route events from EventBridge to SQS queues for reliable event-driven architectures.
  name: Amazon EventBridge
- description: Provision and manage SQS queues as infrastructure-as-code using CloudFormation templates.
  name: AWS CloudFormation
- description: Create and manage SQS resources using HashiCorp Terraform infrastructure-as-code provider.
  name: Terraform
json_schemas:
- name: BatchResultErrorEntry
  property_count: 4
  slug: amazon-sqs-batch-result-error-entry
- name: CancelMessageMoveTaskResponse
  property_count: 1
  slug: amazon-sqs-cancel-message-move-task-response
- name: ChangeMessageVisibilityBatchResponse
  property_count: 1
  slug: amazon-sqs-change-message-visibility-batch-response
- name: CreateQueueResponse
  property_count: 1
  slug: amazon-sqs-create-queue-response
- name: DeleteMessageBatchResponse
  property_count: 1
  slug: amazon-sqs-delete-message-batch-response
- name: ErrorResponse
  property_count: 2
  slug: amazon-sqs-error-response
- name: GenericResponse
  property_count: 0
  slug: amazon-sqs-generic-response
- name: GetQueueAttributesResponse
  property_count: 1
  slug: amazon-sqs-get-queue-attributes-response
- name: GetQueueUrlResponse
  property_count: 1
  slug: amazon-sqs-get-queue-url-response
- name: ListDeadLetterSourceQueuesResponse
  property_count: 1
  slug: amazon-sqs-list-dead-letter-source-queues-response
- name: ListMessageMoveTasksResponse
  property_count: 1
  slug: amazon-sqs-list-message-move-tasks-response
- name: ListQueueTagsResponse
  property_count: 1
  slug: amazon-sqs-list-queue-tags-response
- name: ListQueuesResponse
  property_count: 1
  slug: amazon-sqs-list-queues-response
- name: Message
  property_count: 6
  slug: amazon-sqs-message
- name: ReceiveMessageResponse
  property_count: 1
  slug: amazon-sqs-receive-message-response
- name: ResponseMetadata
  property_count: 1
  slug: amazon-sqs-response-metadata
- name: SendMessageBatchResponse
  property_count: 1
  slug: amazon-sqs-send-message-batch-response
- name: SendMessageResponse
  property_count: 1
  slug: amazon-sqs-send-message-response
- name: StartMessageMoveTaskResponse
  property_count: 1
  slug: amazon-sqs-start-message-move-task-response
json_structures:
- name: Amazon Sqs Batch Result Error Entry Structure
  property_count: 4
  slug: amazon-sqs-batch-result-error-entry-structure
- name: Amazon Sqs Cancel Message Move Task Response Structure
  property_count: 1
  slug: amazon-sqs-cancel-message-move-task-response-structure
- name: Amazon Sqs Change Message Visibility Batch Response Structure
  property_count: 1
  slug: amazon-sqs-change-message-visibility-batch-response-structure
- name: Amazon Sqs Create Queue Response Structure
  property_count: 1
  slug: amazon-sqs-create-queue-response-structure
- name: Amazon Sqs Delete Message Batch Response Structure
  property_count: 1
  slug: amazon-sqs-delete-message-batch-response-structure
- name: Amazon Sqs Error Response Structure
  property_count: 2
  slug: amazon-sqs-error-response-structure
- name: Amazon Sqs Generic Response Structure
  property_count: 0
  slug: amazon-sqs-generic-response-structure
- name: Amazon Sqs Get Queue Attributes Response Structure
  property_count: 1
  slug: amazon-sqs-get-queue-attributes-response-structure
- name: Amazon Sqs Get Queue Url Response Structure
  property_count: 1
  slug: amazon-sqs-get-queue-url-response-structure
- name: Amazon Sqs List Dead Letter Source Queues Response Structure
  property_count: 1
  slug: amazon-sqs-list-dead-letter-source-queues-response-structure
- name: Amazon Sqs List Message Move Tasks Response Structure
  property_count: 1
  slug: amazon-sqs-list-message-move-tasks-response-structure
- name: Amazon Sqs List Queue Tags Response Structure
  property_count: 1
  slug: amazon-sqs-list-queue-tags-response-structure
- name: Amazon Sqs List Queues Response Structure
  property_count: 1
  slug: amazon-sqs-list-queues-response-structure
- name: Amazon Sqs Message Structure
  property_count: 6
  slug: amazon-sqs-message-structure
- name: Amazon Sqs Receive Message Response Structure
  property_count: 1
  slug: amazon-sqs-receive-message-response-structure
- name: Amazon Sqs Response Metadata Structure
  property_count: 1
  slug: amazon-sqs-response-metadata-structure
- name: Amazon Sqs Send Message Batch Response Structure
  property_count: 1
  slug: amazon-sqs-send-message-batch-response-structure
- name: Amazon Sqs Send Message Response Structure
  property_count: 1
  slug: amazon-sqs-send-message-response-structure
- name: Amazon Sqs Start Message Move Task Response Structure
  property_count: 1
  slug: amazon-sqs-start-message-move-task-response-structure
jsonld:
- class_count: 0
  name: Amazon Sqs Context
  property_count: 0
  slug: amazon-sqs-context
layout: provider
modified: '2026-05-19'
name: Amazon SQS
nav: Providers
network: true
overview: 'Amazon SQS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Messages API, Permissions API, Queues API, and 1 more. Tagged areas include Cloud, Distributed Systems, Messaging, Microservices, and Queue.


  The Amazon SQS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Amazon SQS''s developer surface includes authentication, engineering blog, developer console, support, code examples, and 10 more developer resources.'
plans:
- name: Amazon Sqs Plans Pricing
  plan_count: 3
  slug: amazon-sqs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Amazon Sqs Rate Limits
  slug: amazon-sqs-rate-limits
rules:
- effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Amazon SQS API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: amazon-sqs-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Amazon SQS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-sqs-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Amazon SQS API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 9
  slug: amazon-sqs-spectral-rules
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 13.6
    contract_quality: 73.1
    developer_ergonomics: 73.8
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 44.7
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-sqs/refs/heads/main/screenshots/amazon-sqs-2026-06-20T171828.png
security:
- kind: authentication
  name: Amazon Sqs Authentication
  slug: amazon-sqs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Sqs Domain Security
  slug: amazon-sqs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Sqs Vulnerability Disclosure
  slug: amazon-sqs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Sqs Trust Center
  slug: amazon-sqs-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-sqs
tags:
- Cloud
- Distributed Systems
- Messaging
- Microservices
- Queue
use_cases:
- description: Decouple microservices by using SQS queues as asynchronous communication buffers between services.
  name: Microservices Decoupling
- description: Trigger AWS Lambda functions from SQS messages for event-driven serverless architectures.
  name: Serverless Event Processing
- description: Use FIFO queues to ensure ordered processing of e-commerce orders and financial transactions.
  name: Order Processing Pipelines
- description: Distribute compute-intensive tasks across multiple workers using standard queues for parallel processing.
  name: Work Queue Distribution
- description: Queue batch processing jobs and manage their execution across distributed compute resources.
  name: Batch Job Orchestration
---
