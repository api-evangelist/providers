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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Amazon Eventbridge Agentic Access
  operation_count: 14
  slug: amazon-eventbridge-agentic-access
  summary_line: 14 operations · 14 acting
api_count: 5
apis:
- description: Operations for managing event archives.
  name: Amazon EventBridge Archives API
  slug: amazon-eventbridge-archives-api
- description: Operations for managing event buses.
  name: Amazon EventBridge Event Buses API
  slug: amazon-eventbridge-event-buses-api
- description: Operations for putting events to EventBridge.
  name: Amazon EventBridge Events API
  slug: amazon-eventbridge-events-api
- description: Operations for managing EventBridge rules.
  name: Amazon EventBridge Rules API
  slug: amazon-eventbridge-rules-api
- description: Operations for managing rule targets.
  name: Amazon EventBridge Targets API
  slug: amazon-eventbridge-targets-api
arazzos:
- description: Create a bus, resolve its ARN, then archive matching events from it.
  name: Amazon EventBridge Archive Event Bus
  slug: amazon-eventbridge-archive-event-bus-workflow
- description: List event buses, list a bus's rules, then describe a chosen rule.
  name: Amazon EventBridge Audit Bus Rules
  slug: amazon-eventbridge-audit-bus-rules-workflow
- description: Create an event archive, then list archives to confirm it exists.
  name: Amazon EventBridge Create and Verify Archive
  slug: amazon-eventbridge-create-and-verify-archive-workflow
- description: Create a rule on an existing event bus, attach targets, and verify them.
  name: Amazon EventBridge Create Rule with Targets
  slug: amazon-eventbridge-create-rule-with-targets-workflow
- description: List a rule's targets, remove them, then delete the rule cleanly.
  name: Amazon EventBridge Decommission Rule
  slug: amazon-eventbridge-decommission-rule-workflow
- description: Describe a rule's configuration, then list the targets attached to it.
  name: Amazon EventBridge Inspect Rule and Targets
  slug: amazon-eventbridge-inspect-rule-and-targets-workflow
- description: Stand up a custom event bus, attach a rule, wire targets, and confirm the wiring.
  name: Amazon EventBridge Provision Event Bus Routing
  slug: amazon-eventbridge-provision-event-bus-routing-workflow
- description: Create a rule, attach a target, then publish a matching event onto the bus.
  name: Amazon EventBridge Route and Emit Event
  slug: amazon-eventbridge-route-and-emit-event-workflow
- description: Inspect a bus's rules, delete a rule, then delete the custom event bus.
  name: Amazon EventBridge Teardown Event Bus
  slug: amazon-eventbridge-teardown-event-bus-workflow
artifact_total: 139
asyncapis:
- description: Amazon EventBridge delivers events from event sources to targets based on rules you define. This AsyncAPI specification documents the event channels and message schemas for events delivered by EventBr
  name: Amazon EventBridge Event Delivery
  slug: amazon-eventbridge-asyncapi
collections:
- collection_type: postman
  name: Amazon EventBridge API
  slug: postman-amazon-eventbridge
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EventBridge Archives API
  slug: open-amazon-eventbridge-archives-api
- collection_type: open
  name: Amazon EventBridge Archives Event Buses API
  slug: open-amazon-eventbridge-event-buses-api
- collection_type: open
  name: Amazon EventBridge Archives Events API
  slug: open-amazon-eventbridge-events-api
- collection_type: open
  name: Amazon EventBridge Archives Rules API
  slug: open-amazon-eventbridge-rules-api
- collection_type: open
  name: Amazon EventBridge Archives Targets API
  slug: open-amazon-eventbridge-targets-api
- collection_type: open
  name: Amazon EventBridge API
  slug: open-amazon-eventbridge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-eventbridge-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-eventbridge-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-eventbridge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-eventbridge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-eventbridge-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-eventbridge/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-archive-event-bus-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-audit-bus-rules-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-create-and-verify-archive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-create-rule-with-targets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-decommission-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-inspect-rule-and-targets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-provision-event-bus-routing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-route-and-emit-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-eventbridge-teardown-event-bus-workflow.yml
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
  url: rules/amazon-eventbridge-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-eventbridge-vocabulary.yaml
created: '2024-01-15'
description: Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, SaaS applications, and AWS services and routes that data to targets such as Lambda, SNS, SQS, and more.
examples:
- key_count: 5
  name: Amazon Eventbridge Create Archive Request Example
  slug: amazon-eventbridge-create-archive-request-example
- key_count: 3
  name: Amazon Eventbridge Create Archive Response Example
  slug: amazon-eventbridge-create-archive-response-example
- key_count: 3
  name: Amazon Eventbridge Create Event Bus Request Example
  slug: amazon-eventbridge-create-event-bus-request-example
- key_count: 1
  name: Amazon Eventbridge Create Event Bus Response Example
  slug: amazon-eventbridge-create-event-bus-response-example
- key_count: 1
  name: Amazon Eventbridge Delete Event Bus Request Example
  slug: amazon-eventbridge-delete-event-bus-request-example
- key_count: 3
  name: Amazon Eventbridge Delete Rule Request Example
  slug: amazon-eventbridge-delete-rule-request-example
- key_count: 1
  name: Amazon Eventbridge Describe Event Bus Request Example
  slug: amazon-eventbridge-describe-event-bus-request-example
- key_count: 3
  name: Amazon Eventbridge Describe Event Bus Response Example
  slug: amazon-eventbridge-describe-event-bus-response-example
- key_count: 2
  name: Amazon Eventbridge Describe Rule Request Example
  slug: amazon-eventbridge-describe-rule-request-example
- key_count: 8
  name: Amazon Eventbridge Describe Rule Response Example
  slug: amazon-eventbridge-describe-rule-response-example
- key_count: 3
  name: Amazon Eventbridge Event Bus Example
  slug: amazon-eventbridge-event-bus-example
- key_count: 9
  name: Amazon Eventbridge Event Example
  slug: amazon-eventbridge-event-example
- key_count: 5
  name: Amazon Eventbridge List Archives Request Example
  slug: amazon-eventbridge-list-archives-request-example
- key_count: 2
  name: Amazon Eventbridge List Archives Response Example
  slug: amazon-eventbridge-list-archives-response-example
- key_count: 3
  name: Amazon Eventbridge List Event Buses Request Example
  slug: amazon-eventbridge-list-event-buses-request-example
- key_count: 2
  name: Amazon Eventbridge List Event Buses Response Example
  slug: amazon-eventbridge-list-event-buses-response-example
- key_count: 4
  name: Amazon Eventbridge List Rules Request Example
  slug: amazon-eventbridge-list-rules-request-example
- key_count: 2
  name: Amazon Eventbridge List Rules Response Example
  slug: amazon-eventbridge-list-rules-response-example
- key_count: 4
  name: Amazon Eventbridge List Targets By Rule Request Example
  slug: amazon-eventbridge-list-targets-by-rule-request-example
- key_count: 2
  name: Amazon Eventbridge List Targets By Rule Response Example
  slug: amazon-eventbridge-list-targets-by-rule-response-example
- key_count: 1
  name: Amazon Eventbridge Put Events Request Example
  slug: amazon-eventbridge-put-events-request-example
- key_count: 2
  name: Amazon Eventbridge Put Events Response Example
  slug: amazon-eventbridge-put-events-response-example
- key_count: 8
  name: Amazon Eventbridge Put Rule Request Example
  slug: amazon-eventbridge-put-rule-request-example
- key_count: 1
  name: Amazon Eventbridge Put Rule Response Example
  slug: amazon-eventbridge-put-rule-response-example
- key_count: 3
  name: Amazon Eventbridge Put Targets Request Example
  slug: amazon-eventbridge-put-targets-request-example
- key_count: 2
  name: Amazon Eventbridge Put Targets Response Example
  slug: amazon-eventbridge-put-targets-response-example
- key_count: 4
  name: Amazon Eventbridge Remove Targets Request Example
  slug: amazon-eventbridge-remove-targets-request-example
- key_count: 2
  name: Amazon Eventbridge Remove Targets Response Example
  slug: amazon-eventbridge-remove-targets-response-example
- key_count: 8
  name: Amazon Eventbridge Rule Example
  slug: amazon-eventbridge-rule-example
- key_count: 6
  name: Amazon Eventbridge Target Example
  slug: amazon-eventbridge-target-example
features:
- description: Central event bus for routing events between AWS services and applications
  name: Event Bus
- description: Create rules to filter and route events to specific targets
  name: Event Rules
- description: Discover, create, and manage event schemas with code binding generation
  name: Schema Registry
- description: Receive events from SaaS partners like Zendesk, Datadog, and PagerDuty
  name: SaaS Integrations
- description: Send events to external HTTP endpoints via API Destinations
  name: API Destinations
finops:
- name: Amazon Eventbridge Finops
  service_category: API
  slug: amazon-eventbridge-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Invoke Lambda functions in response to events
  name: AWS Lambda
- description: Fan out events to multiple subscribers via SNS topics
  name: Amazon SNS
- description: Queue events for reliable processing with SQS
  name: Amazon SQS
- description: Start state machine executions in response to events
  name: AWS Step Functions
- description: Receive Zendesk support ticket and activity events
  name: Zendesk
json_schemas:
- name: CreateArchiveRequest
  property_count: 5
  slug: amazon-eventbridge-create-archive-request
- name: CreateArchiveResponse
  property_count: 3
  slug: amazon-eventbridge-create-archive-response
- name: CreateEventBusRequest
  property_count: 3
  slug: amazon-eventbridge-create-event-bus-request
- name: CreateEventBusResponse
  property_count: 1
  slug: amazon-eventbridge-create-event-bus-response
- name: DeleteEventBusRequest
  property_count: 1
  slug: amazon-eventbridge-delete-event-bus-request
- name: DeleteRuleRequest
  property_count: 3
  slug: amazon-eventbridge-delete-rule-request
- name: DescribeEventBusRequest
  property_count: 1
  slug: amazon-eventbridge-describe-event-bus-request
- name: DescribeEventBusResponse
  property_count: 3
  slug: amazon-eventbridge-describe-event-bus-response
- name: DescribeRuleRequest
  property_count: 2
  slug: amazon-eventbridge-describe-rule-request
- name: DescribeRuleResponse
  property_count: 8
  slug: amazon-eventbridge-describe-rule-response
- name: EventBus
  property_count: 3
  slug: amazon-eventbridge-event-bus
- name: Amazon EventBridge Event
  property_count: 9
  slug: amazon-eventbridge-event
- name: ListArchivesRequest
  property_count: 5
  slug: amazon-eventbridge-list-archives-request
- name: ListArchivesResponse
  property_count: 2
  slug: amazon-eventbridge-list-archives-response
- name: ListEventBusesRequest
  property_count: 3
  slug: amazon-eventbridge-list-event-buses-request
- name: ListEventBusesResponse
  property_count: 2
  slug: amazon-eventbridge-list-event-buses-response
- name: ListRulesRequest
  property_count: 4
  slug: amazon-eventbridge-list-rules-request
- name: ListRulesResponse
  property_count: 2
  slug: amazon-eventbridge-list-rules-response
- name: ListTargetsByRuleRequest
  property_count: 4
  slug: amazon-eventbridge-list-targets-by-rule-request
- name: ListTargetsByRuleResponse
  property_count: 2
  slug: amazon-eventbridge-list-targets-by-rule-response
- name: PutEventsRequest
  property_count: 1
  slug: amazon-eventbridge-put-events-request
- name: PutEventsResponse
  property_count: 2
  slug: amazon-eventbridge-put-events-response
- name: PutRuleRequest
  property_count: 8
  slug: amazon-eventbridge-put-rule-request
- name: PutRuleResponse
  property_count: 1
  slug: amazon-eventbridge-put-rule-response
- name: PutTargetsRequest
  property_count: 3
  slug: amazon-eventbridge-put-targets-request
- name: PutTargetsResponse
  property_count: 2
  slug: amazon-eventbridge-put-targets-response
- name: RemoveTargetsRequest
  property_count: 4
  slug: amazon-eventbridge-remove-targets-request
- name: RemoveTargetsResponse
  property_count: 2
  slug: amazon-eventbridge-remove-targets-response
- name: Rule
  property_count: 8
  slug: amazon-eventbridge-rule
- name: Target
  property_count: 6
  slug: amazon-eventbridge-target
json_structures:
- name: Amazon Eventbridge Create Archive Request Structure
  property_count: 5
  slug: amazon-eventbridge-create-archive-request-structure
- name: Amazon Eventbridge Create Archive Response Structure
  property_count: 3
  slug: amazon-eventbridge-create-archive-response-structure
- name: Amazon Eventbridge Create Event Bus Request Structure
  property_count: 3
  slug: amazon-eventbridge-create-event-bus-request-structure
- name: Amazon Eventbridge Create Event Bus Response Structure
  property_count: 1
  slug: amazon-eventbridge-create-event-bus-response-structure
- name: Amazon Eventbridge Delete Event Bus Request Structure
  property_count: 1
  slug: amazon-eventbridge-delete-event-bus-request-structure
- name: Amazon Eventbridge Delete Rule Request Structure
  property_count: 3
  slug: amazon-eventbridge-delete-rule-request-structure
- name: Amazon Eventbridge Describe Event Bus Request Structure
  property_count: 1
  slug: amazon-eventbridge-describe-event-bus-request-structure
- name: Amazon Eventbridge Describe Event Bus Response Structure
  property_count: 3
  slug: amazon-eventbridge-describe-event-bus-response-structure
- name: Amazon Eventbridge Describe Rule Request Structure
  property_count: 2
  slug: amazon-eventbridge-describe-rule-request-structure
- name: Amazon Eventbridge Describe Rule Response Structure
  property_count: 8
  slug: amazon-eventbridge-describe-rule-response-structure
- name: Amazon Eventbridge Event Bus Structure
  property_count: 3
  slug: amazon-eventbridge-event-bus-structure
- name: Amazon Eventbridge Event Structure
  property_count: 9
  slug: amazon-eventbridge-event-structure
- name: Amazon Eventbridge List Archives Request Structure
  property_count: 5
  slug: amazon-eventbridge-list-archives-request-structure
- name: Amazon Eventbridge List Archives Response Structure
  property_count: 2
  slug: amazon-eventbridge-list-archives-response-structure
- name: Amazon Eventbridge List Event Buses Request Structure
  property_count: 3
  slug: amazon-eventbridge-list-event-buses-request-structure
- name: Amazon Eventbridge List Event Buses Response Structure
  property_count: 2
  slug: amazon-eventbridge-list-event-buses-response-structure
- name: Amazon Eventbridge List Rules Request Structure
  property_count: 4
  slug: amazon-eventbridge-list-rules-request-structure
- name: Amazon Eventbridge List Rules Response Structure
  property_count: 2
  slug: amazon-eventbridge-list-rules-response-structure
- name: Amazon Eventbridge List Targets By Rule Request Structure
  property_count: 4
  slug: amazon-eventbridge-list-targets-by-rule-request-structure
- name: Amazon Eventbridge List Targets By Rule Response Structure
  property_count: 2
  slug: amazon-eventbridge-list-targets-by-rule-response-structure
- name: Amazon Eventbridge Put Events Request Structure
  property_count: 1
  slug: amazon-eventbridge-put-events-request-structure
- name: Amazon Eventbridge Put Events Response Structure
  property_count: 2
  slug: amazon-eventbridge-put-events-response-structure
- name: Amazon Eventbridge Put Rule Request Structure
  property_count: 8
  slug: amazon-eventbridge-put-rule-request-structure
- name: Amazon Eventbridge Put Rule Response Structure
  property_count: 1
  slug: amazon-eventbridge-put-rule-response-structure
- name: Amazon Eventbridge Put Targets Request Structure
  property_count: 3
  slug: amazon-eventbridge-put-targets-request-structure
- name: Amazon Eventbridge Put Targets Response Structure
  property_count: 2
  slug: amazon-eventbridge-put-targets-response-structure
- name: Amazon Eventbridge Remove Targets Request Structure
  property_count: 4
  slug: amazon-eventbridge-remove-targets-request-structure
- name: Amazon Eventbridge Remove Targets Response Structure
  property_count: 2
  slug: amazon-eventbridge-remove-targets-response-structure
- name: Amazon Eventbridge Rule Structure
  property_count: 8
  slug: amazon-eventbridge-rule-structure
- name: Amazon Eventbridge Target Structure
  property_count: 6
  slug: amazon-eventbridge-target-structure
jsonld:
- class_count: 5
  name: Amazon Eventbridge Context
  property_count: 9
  slug: amazon-eventbridge-context
layout: provider
modified: '2026-05-19'
name: Amazon EventBridge
nav: Providers
network: true
overview: 'Amazon EventBridge publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Archives API, Event Buses API, Events API, and 2 more. Tagged areas include Amazon Web Services, Event Bus, Event-Driven, Events, and Integration.


  The Amazon EventBridge catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Amazon EventBridge''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 29 more developer resources.'
plans:
- name: Amazon Eventbridge Plans Pricing
  plan_count: 3
  slug: amazon-eventbridge-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Amazon Eventbridge Rate Limits
  slug: amazon-eventbridge-rate-limits
rules:
- name: Amazon EventBridge API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: amazon-eventbridge-asyncapi-spectral-rules
- name: Amazon EventBridge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-eventbridge-jsonschema-spectral-rules
- name: Amazon EventBridge API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 14
  slug: amazon-eventbridge-spectral-rules
score:
  band: strong
  composite: 62.1
  delta: 0.0
  facets:
    commercial_clarity: 65.8
    contract_quality: 88.1
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 37.5
    operational_transparency: 39.5
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-eventbridge/refs/heads/main/screenshots/amazon-eventbridge-2026-06-20T171644.png
security:
- kind: authentication
  name: Amazon Eventbridge Authentication
  slug: amazon-eventbridge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Eventbridge Domain Security
  slug: amazon-eventbridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Eventbridge Vulnerability Disclosure
  slug: amazon-eventbridge-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Eventbridge Trust Center
  slug: amazon-eventbridge-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-eventbridge
tags:
- Amazon Web Services
- Event Bus
- Event-Driven
- Events
- Integration
- Serverless
use_cases:
- description: Decouple microservices by routing events through a central event bus
  name: Microservices Decoupling
- description: React to CloudWatch alarms and AWS service events in real time
  name: Application Monitoring
- description: Receive and process events from SaaS applications without polling
  name: SaaS Event Processing
- description: Route events across AWS accounts and regions for enterprise architectures
  name: Multi-Account Event Routing
website: https://aws.amazon.com/eventbridge/
---
