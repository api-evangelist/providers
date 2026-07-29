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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Amazon Iot Events Agentic Access
  operation_count: 26
  slug: amazon-iot-events-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 8
apis:
- description: The Alarm Models API from Amazon IoT Events — 3 operation(s) for alarm models.
  name: Amazon IoT Events Alarm Models API
  slug: amazon-iot-events-alarm-models-api
- description: The Analysis API from Amazon IoT Events — 3 operation(s) for analysis.
  name: Amazon IoT Events Analysis API
  slug: amazon-iot-events-analysis-api
- description: The Detector Models API from Amazon IoT Events — 3 operation(s) for detector models.
  name: Amazon IoT Events Detector Models API
  slug: amazon-iot-events-detector-models-api
- description: The Input Routings API from Amazon IoT Events — 1 operation(s) for input routings.
  name: Amazon IoT Events Input Routings API
  slug: amazon-iot-events-input-routings-api
- description: The Inputs API from Amazon IoT Events — 2 operation(s) for inputs.
  name: Amazon IoT Events Inputs API
  slug: amazon-iot-events-inputs-api
- description: The Logging API from Amazon IoT Events — 1 operation(s) for logging.
  name: Amazon IoT Events Logging API
  slug: amazon-iot-events-logging-api
- description: The Tags#resourceArn API from Amazon IoT Events — 1 operation(s) for tags#resourcearn.
  name: Amazon IoT Events Tags#resourceArn API
  slug: amazon-iot-events-tags-resourcearn-api
- description: The Tags#resourceArn&tagKeys API from Amazon IoT Events — 1 operation(s) for tags#resourcearn&tagkeys.
  name: Amazon IoT Events Tags#resourceArn&tagKeys API
  slug: amazon-iot-events-tags-resourcearn-tagkeys-api
artifact_total: 454
collections:
- collection_type: postman
  name: AWS IoT Events Alarm Models API
  slug: postman-amazon-iot-events-alarm-models-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Analysis API
  slug: postman-amazon-iot-events-analysis-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Detector Models API
  slug: postman-amazon-iot-events-detector-models-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Input Routings API
  slug: postman-amazon-iot-events-input-routings-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Inputs API
  slug: postman-amazon-iot-events-inputs-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Logging API
  slug: postman-amazon-iot-events-logging-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Tags#resourceArn API
  slug: postman-amazon-iot-events-tags-resourcearn-api
- collection_type: postman
  name: AWS IoT Events Alarm Models Tags#resourceArn&tagKeys API
  slug: postman-amazon-iot-events-tags-resourcearn-tagkeys-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-iot-events/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-iot-events-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-iot-events-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-iot-events-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-iot-events-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-iot-events-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/iot-events/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/iot-events/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iotevents/
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
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-events/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/iotevents/
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
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-iot-events-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-events-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-iot-events-context.jsonld
created: '2026-03-16'
description: AWS IoT Events is a managed service that makes it easy to detect and respond to events from IoT sensors and applications. You can use it to build complex event detection logic, create state machines for IoT workflows, and trigger alerts or actions when specific conditions are met.
examples:
- key_count: 1
  name: Iot Events Acknowledge Flow Example
  slug: iot-events-acknowledge-flow-example
- key_count: 13
  name: Iot Events Action Example
  slug: iot-events-action-example
- key_count: 0
  name: Iot Events Actions Example
  slug: iot-events-actions-example
- key_count: 9
  name: Iot Events Alarm Action Example
  slug: iot-events-alarm-action-example
- key_count: 0
  name: Iot Events Alarm Actions Example
  slug: iot-events-alarm-actions-example
- key_count: 2
  name: Iot Events Alarm Capabilities Example
  slug: iot-events-alarm-capabilities-example
- key_count: 1
  name: Iot Events Alarm Event Actions Example
  slug: iot-events-alarm-event-actions-example
- key_count: 0
  name: Iot Events Alarm Model Summaries Example
  slug: iot-events-alarm-model-summaries-example
- key_count: 3
  name: Iot Events Alarm Model Summary Example
  slug: iot-events-alarm-model-summary-example
- key_count: 0
  name: Iot Events Alarm Model Version Summaries Example
  slug: iot-events-alarm-model-version-summaries-example
- key_count: 8
  name: Iot Events Alarm Model Version Summary Example
  slug: iot-events-alarm-model-version-summary-example
- key_count: 1
  name: Iot Events Alarm Notification Example
  slug: iot-events-alarm-notification-example
- key_count: 1
  name: Iot Events Alarm Rule Example
  slug: iot-events-alarm-rule-example
- key_count: 4
  name: Iot Events Analysis Result Example
  slug: iot-events-analysis-result-example
- key_count: 1
  name: Iot Events Analysis Result Location Example
  slug: iot-events-analysis-result-location-example
- key_count: 0
  name: Iot Events Analysis Result Locations Example
  slug: iot-events-analysis-result-locations-example
- key_count: 0
  name: Iot Events Analysis Results Example
  slug: iot-events-analysis-results-example
- key_count: 2
  name: Iot Events Asset Property Timestamp Example
  slug: iot-events-asset-property-timestamp-example
- key_count: 3
  name: Iot Events Asset Property Value Example
  slug: iot-events-asset-property-value-example
- key_count: 4
  name: Iot Events Asset Property Variant Example
  slug: iot-events-asset-property-variant-example
- key_count: 1
  name: Iot Events Attribute Example
  slug: iot-events-attribute-example
- key_count: 0
  name: Iot Events Attributes Example
  slug: iot-events-attributes-example
- key_count: 1
  name: Iot Events Clear Timer Action Example
  slug: iot-events-clear-timer-action-example
- key_count: 10
  name: Iot Events Create Alarm Model Request Example
  slug: iot-events-create-alarm-model-request-example
- key_count: 5
  name: Iot Events Create Alarm Model Response Example
  slug: iot-events-create-alarm-model-response-example
- key_count: 7
  name: Iot Events Create Detector Model Request Example
  slug: iot-events-create-detector-model-request-example
- key_count: 1
  name: Iot Events Create Detector Model Response Example
  slug: iot-events-create-detector-model-response-example
- key_count: 4
  name: Iot Events Create Input Request Example
  slug: iot-events-create-input-request-example
- key_count: 1
  name: Iot Events Create Input Response Example
  slug: iot-events-create-input-response-example
- key_count: 0
  name: Iot Events Delete Alarm Model Request Example
  slug: iot-events-delete-alarm-model-request-example
- key_count: 0
  name: Iot Events Delete Alarm Model Response Example
  slug: iot-events-delete-alarm-model-response-example
- key_count: 0
  name: Iot Events Delete Detector Model Request Example
  slug: iot-events-delete-detector-model-request-example
- key_count: 0
  name: Iot Events Delete Detector Model Response Example
  slug: iot-events-delete-detector-model-response-example
- key_count: 0
  name: Iot Events Delete Input Request Example
  slug: iot-events-delete-input-request-example
- key_count: 0
  name: Iot Events Delete Input Response Example
  slug: iot-events-delete-input-response-example
- key_count: 0
  name: Iot Events Describe Alarm Model Request Example
  slug: iot-events-describe-alarm-model-request-example
- key_count: 15
  name: Iot Events Describe Alarm Model Response Example
  slug: iot-events-describe-alarm-model-response-example
- key_count: 0
  name: Iot Events Describe Detector Model Analysis Request Example
  slug: iot-events-describe-detector-model-analysis-request-example
- key_count: 1
  name: Iot Events Describe Detector Model Analysis Response Example
  slug: iot-events-describe-detector-model-analysis-response-example
- key_count: 0
  name: Iot Events Describe Detector Model Request Example
  slug: iot-events-describe-detector-model-request-example
- key_count: 1
  name: Iot Events Describe Detector Model Response Example
  slug: iot-events-describe-detector-model-response-example
- key_count: 0
  name: Iot Events Describe Input Request Example
  slug: iot-events-describe-input-request-example
- key_count: 1
  name: Iot Events Describe Input Response Example
  slug: iot-events-describe-input-response-example
- key_count: 0
  name: Iot Events Describe Logging Options Request Example
  slug: iot-events-describe-logging-options-request-example
- key_count: 1
  name: Iot Events Describe Logging Options Response Example
  slug: iot-events-describe-logging-options-response-example
- key_count: 2
  name: Iot Events Detector Debug Option Example
  slug: iot-events-detector-debug-option-example
- key_count: 0
  name: Iot Events Detector Debug Options Example
  slug: iot-events-detector-debug-options-example
- key_count: 10
  name: Iot Events Detector Model Configuration Example
  slug: iot-events-detector-model-configuration-example
- key_count: 2
  name: Iot Events Detector Model Definition Example
  slug: iot-events-detector-model-definition-example
- key_count: 2
  name: Iot Events Detector Model Example
  slug: iot-events-detector-model-example
- key_count: 0
  name: Iot Events Detector Model Summaries Example
  slug: iot-events-detector-model-summaries-example
- key_count: 3
  name: Iot Events Detector Model Summary Example
  slug: iot-events-detector-model-summary-example
- key_count: 0
  name: Iot Events Detector Model Version Summaries Example
  slug: iot-events-detector-model-version-summaries-example
- key_count: 8
  name: Iot Events Detector Model Version Summary Example
  slug: iot-events-detector-model-version-summary-example
- key_count: 10
  name: Iot Events Dynamo D B Action Example
  slug: iot-events-dynamo-d-b-action-example
- key_count: 2
  name: Iot Events Dynamo D Bv2 Action Example
  slug: iot-events-dynamo-d-bv2-action-example
- key_count: 3
  name: Iot Events Email Configuration Example
  slug: iot-events-email-configuration-example
- key_count: 0
  name: Iot Events Email Configurations Example
  slug: iot-events-email-configurations-example
- key_count: 2
  name: Iot Events Email Content Example
  slug: iot-events-email-content-example
- key_count: 1
  name: Iot Events Email Recipients Example
  slug: iot-events-email-recipients-example
- key_count: 3
  name: Iot Events Event Example
  slug: iot-events-event-example
- key_count: 0
  name: Iot Events Events Example
  slug: iot-events-events-example
- key_count: 3
  name: Iot Events Firehose Action Example
  slug: iot-events-firehose-action-example
- key_count: 0
  name: Iot Events Get Detector Model Analysis Results Request Example
  slug: iot-events-get-detector-model-analysis-results-request-example
- key_count: 2
  name: Iot Events Get Detector Model Analysis Results Response Example
  slug: iot-events-get-detector-model-analysis-results-response-example
- key_count: 1
  name: Iot Events Initialization Configuration Example
  slug: iot-events-initialization-configuration-example
- key_count: 6
  name: Iot Events Input Configuration Example
  slug: iot-events-input-configuration-example
- key_count: 1
  name: Iot Events Input Definition Example
  slug: iot-events-input-definition-example
- key_count: 2
  name: Iot Events Input Example
  slug: iot-events-input-example
- key_count: 2
  name: Iot Events Input Identifier Example
  slug: iot-events-input-identifier-example
- key_count: 0
  name: Iot Events Input Summaries Example
  slug: iot-events-input-summaries-example
- key_count: 6
  name: Iot Events Input Summary Example
  slug: iot-events-input-summary-example
- key_count: 2
  name: Iot Events Iot Events Action Example
  slug: iot-events-iot-events-action-example
- key_count: 1
  name: Iot Events Iot Events Input Identifier Example
  slug: iot-events-iot-events-input-identifier-example
- key_count: 5
  name: Iot Events Iot Site Wise Action Example
  slug: iot-events-iot-site-wise-action-example
- key_count: 2
  name: Iot Events Iot Site Wise Asset Model Property Identifier Example
  slug: iot-events-iot-site-wise-asset-model-property-identifier-example
- key_count: 1
  name: Iot Events Iot Site Wise Input Identifier Example
  slug: iot-events-iot-site-wise-input-identifier-example
- key_count: 2
  name: Iot Events Iot Topic Publish Action Example
  slug: iot-events-iot-topic-publish-action-example
- key_count: 2
  name: Iot Events Lambda Action Example
  slug: iot-events-lambda-action-example
- key_count: 0
  name: Iot Events List Alarm Model Versions Request Example
  slug: iot-events-list-alarm-model-versions-request-example
- key_count: 2
  name: Iot Events List Alarm Model Versions Response Example
  slug: iot-events-list-alarm-model-versions-response-example
- key_count: 0
  name: Iot Events List Alarm Models Request Example
  slug: iot-events-list-alarm-models-request-example
- key_count: 2
  name: Iot Events List Alarm Models Response Example
  slug: iot-events-list-alarm-models-response-example
- key_count: 0
  name: Iot Events List Detector Model Versions Request Example
  slug: iot-events-list-detector-model-versions-request-example
- key_count: 2
  name: Iot Events List Detector Model Versions Response Example
  slug: iot-events-list-detector-model-versions-response-example
- key_count: 0
  name: Iot Events List Detector Models Request Example
  slug: iot-events-list-detector-models-request-example
- key_count: 2
  name: Iot Events List Detector Models Response Example
  slug: iot-events-list-detector-models-response-example
- key_count: 3
  name: Iot Events List Input Routings Request Example
  slug: iot-events-list-input-routings-request-example
- key_count: 2
  name: Iot Events List Input Routings Response Example
  slug: iot-events-list-input-routings-response-example
- key_count: 0
  name: Iot Events List Inputs Request Example
  slug: iot-events-list-inputs-request-example
- key_count: 2
  name: Iot Events List Inputs Response Example
  slug: iot-events-list-inputs-response-example
- key_count: 0
  name: Iot Events List Tags For Resource Request Example
  slug: iot-events-list-tags-for-resource-request-example
- key_count: 1
  name: Iot Events List Tags For Resource Response Example
  slug: iot-events-list-tags-for-resource-response-example
- key_count: 4
  name: Iot Events Logging Options Example
  slug: iot-events-logging-options-example
- key_count: 3
  name: Iot Events Notification Action Example
  slug: iot-events-notification-action-example
- key_count: 0
  name: Iot Events Notification Actions Example
  slug: iot-events-notification-actions-example
- key_count: 1
  name: Iot Events Notification Target Actions Example
  slug: iot-events-notification-target-actions-example
- key_count: 1
  name: Iot Events On Enter Lifecycle Example
  slug: iot-events-on-enter-lifecycle-example
- key_count: 1
  name: Iot Events On Exit Lifecycle Example
  slug: iot-events-on-exit-lifecycle-example
- key_count: 2
  name: Iot Events On Input Lifecycle Example
  slug: iot-events-on-input-lifecycle-example
- key_count: 2
  name: Iot Events Payload Example
  slug: iot-events-payload-example
- key_count: 1
  name: Iot Events Put Logging Options Request Example
  slug: iot-events-put-logging-options-request-example
- key_count: 1
  name: Iot Events Recipient Detail Example
  slug: iot-events-recipient-detail-example
- key_count: 0
  name: Iot Events Recipient Details Example
  slug: iot-events-recipient-details-example
- key_count: 1
  name: Iot Events Reset Timer Action Example
  slug: iot-events-reset-timer-action-example
- key_count: 2
  name: Iot Events Routed Resource Example
  slug: iot-events-routed-resource-example
- key_count: 0
  name: Iot Events Routed Resources Example
  slug: iot-events-routed-resources-example
- key_count: 3
  name: Iot Events S M S Configuration Example
  slug: iot-events-s-m-s-configuration-example
- key_count: 0
  name: Iot Events S M S Configurations Example
  slug: iot-events-s-m-s-configurations-example
- key_count: 2
  name: Iot Events S N S Topic Publish Action Example
  slug: iot-events-s-n-s-topic-publish-action-example
- key_count: 2
  name: Iot Events S S O Identity Example
  slug: iot-events-s-s-o-identity-example
- key_count: 3
  name: Iot Events Set Timer Action Example
  slug: iot-events-set-timer-action-example
- key_count: 2
  name: Iot Events Set Variable Action Example
  slug: iot-events-set-variable-action-example
- key_count: 3
  name: Iot Events Simple Rule Example
  slug: iot-events-simple-rule-example
- key_count: 3
  name: Iot Events Sqs Action Example
  slug: iot-events-sqs-action-example
- key_count: 1
  name: Iot Events Start Detector Model Analysis Request Example
  slug: iot-events-start-detector-model-analysis-request-example
- key_count: 1
  name: Iot Events Start Detector Model Analysis Response Example
  slug: iot-events-start-detector-model-analysis-response-example
- key_count: 4
  name: Iot Events State Example
  slug: iot-events-state-example
- key_count: 0
  name: Iot Events States Example
  slug: iot-events-states-example
- key_count: 2
  name: Iot Events Tag Example
  slug: iot-events-tag-example
- key_count: 0
  name: Iot Events Tag Keys Example
  slug: iot-events-tag-keys-example
- key_count: 1
  name: Iot Events Tag Resource Request Example
  slug: iot-events-tag-resource-request-example
- key_count: 0
  name: Iot Events Tag Resource Response Example
  slug: iot-events-tag-resource-response-example
- key_count: 0
  name: Iot Events Tags Example
  slug: iot-events-tags-example
- key_count: 4
  name: Iot Events Transition Event Example
  slug: iot-events-transition-event-example
- key_count: 0
  name: Iot Events Transition Events Example
  slug: iot-events-transition-events-example
- key_count: 0
  name: Iot Events Untag Resource Request Example
  slug: iot-events-untag-resource-request-example
- key_count: 0
  name: Iot Events Untag Resource Response Example
  slug: iot-events-untag-resource-response-example
- key_count: 7
  name: Iot Events Update Alarm Model Request Example
  slug: iot-events-update-alarm-model-request-example
- key_count: 5
  name: Iot Events Update Alarm Model Response Example
  slug: iot-events-update-alarm-model-response-example
- key_count: 4
  name: Iot Events Update Detector Model Request Example
  slug: iot-events-update-detector-model-request-example
- key_count: 1
  name: Iot Events Update Detector Model Response Example
  slug: iot-events-update-detector-model-response-example
- key_count: 2
  name: Iot Events Update Input Request Example
  slug: iot-events-update-input-request-example
- key_count: 1
  name: Iot Events Update Input Response Example
  slug: iot-events-update-input-response-example
features:
- description: Create state machines to detect complex event patterns across IoT data streams.
  name: Detector Models
- description: Built-in alarm management for monitoring IoT sensor thresholds.
  name: Alarm Management
- description: Define structured event inputs and route IoT data to detector models.
  name: Event Inputs
- description: Trigger actions to SNS, SQS, Lambda, and other services when events are detected.
  name: Multi-Trigger Actions
finops:
- name: Amazon Iot Events Finops
  service_category: API
  slug: amazon-iot-events-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-iot-events.png
json_schemas:
- name: AcknowledgeFlow
  property_count: 1
  slug: iot-events-acknowledge-flow
- name: Action
  property_count: 13
  slug: iot-events-action
- name: Actions
  property_count: 0
  slug: iot-events-actions
- name: AlarmAction
  property_count: 9
  slug: iot-events-alarm-action
- name: AlarmActions
  property_count: 0
  slug: iot-events-alarm-actions
- name: AlarmCapabilities
  property_count: 2
  slug: iot-events-alarm-capabilities
- name: AlarmEventActions
  property_count: 1
  slug: iot-events-alarm-event-actions
- name: AlarmModelSummaries
  property_count: 0
  slug: iot-events-alarm-model-summaries
- name: AlarmModelSummary
  property_count: 3
  slug: iot-events-alarm-model-summary
- name: AlarmModelVersionStatus
  property_count: 0
  slug: iot-events-alarm-model-version-status
- name: AlarmModelVersionSummaries
  property_count: 0
  slug: iot-events-alarm-model-version-summaries
- name: AlarmModelVersionSummary
  property_count: 8
  slug: iot-events-alarm-model-version-summary
- name: AlarmNotification
  property_count: 1
  slug: iot-events-alarm-notification
- name: AlarmRule
  property_count: 1
  slug: iot-events-alarm-rule
- name: AnalysisResultLevel
  property_count: 0
  slug: iot-events-analysis-result-level
- name: AnalysisResultLocation
  property_count: 1
  slug: iot-events-analysis-result-location
- name: AnalysisResultLocations
  property_count: 0
  slug: iot-events-analysis-result-locations
- name: AnalysisResult
  property_count: 4
  slug: iot-events-analysis-result
- name: AnalysisResults
  property_count: 0
  slug: iot-events-analysis-results
- name: AnalysisStatus
  property_count: 0
  slug: iot-events-analysis-status
- name: AssetPropertyTimestamp
  property_count: 2
  slug: iot-events-asset-property-timestamp
- name: AssetPropertyValue
  property_count: 3
  slug: iot-events-asset-property-value
- name: AssetPropertyVariant
  property_count: 4
  slug: iot-events-asset-property-variant
- name: Attribute
  property_count: 1
  slug: iot-events-attribute
- name: Attributes
  property_count: 0
  slug: iot-events-attributes
- name: ClearTimerAction
  property_count: 1
  slug: iot-events-clear-timer-action
- name: ComparisonOperator
  property_count: 0
  slug: iot-events-comparison-operator
- name: CreateAlarmModelRequest
  property_count: 10
  slug: iot-events-create-alarm-model-request
- name: CreateAlarmModelResponse
  property_count: 5
  slug: iot-events-create-alarm-model-response
- name: CreateDetectorModelRequest
  property_count: 7
  slug: iot-events-create-detector-model-request
- name: CreateDetectorModelResponse
  property_count: 1
  slug: iot-events-create-detector-model-response
- name: CreateInputRequest
  property_count: 4
  slug: iot-events-create-input-request
- name: CreateInputResponse
  property_count: 1
  slug: iot-events-create-input-response
- name: DeleteAlarmModelRequest
  property_count: 0
  slug: iot-events-delete-alarm-model-request
- name: DeleteAlarmModelResponse
  property_count: 0
  slug: iot-events-delete-alarm-model-response
- name: DeleteDetectorModelRequest
  property_count: 0
  slug: iot-events-delete-detector-model-request
- name: DeleteDetectorModelResponse
  property_count: 0
  slug: iot-events-delete-detector-model-response
- name: DeleteInputRequest
  property_count: 0
  slug: iot-events-delete-input-request
- name: DeleteInputResponse
  property_count: 0
  slug: iot-events-delete-input-response
- name: DescribeAlarmModelRequest
  property_count: 0
  slug: iot-events-describe-alarm-model-request
- name: DescribeAlarmModelResponse
  property_count: 15
  slug: iot-events-describe-alarm-model-response
- name: DescribeDetectorModelAnalysisRequest
  property_count: 0
  slug: iot-events-describe-detector-model-analysis-request
- name: DescribeDetectorModelAnalysisResponse
  property_count: 1
  slug: iot-events-describe-detector-model-analysis-response
- name: DescribeDetectorModelRequest
  property_count: 0
  slug: iot-events-describe-detector-model-request
- name: DescribeDetectorModelResponse
  property_count: 1
  slug: iot-events-describe-detector-model-response
- name: DescribeInputRequest
  property_count: 0
  slug: iot-events-describe-input-request
- name: DescribeInputResponse
  property_count: 1
  slug: iot-events-describe-input-response
- name: DescribeLoggingOptionsRequest
  property_count: 0
  slug: iot-events-describe-logging-options-request
- name: DescribeLoggingOptionsResponse
  property_count: 1
  slug: iot-events-describe-logging-options-response
- name: DetectorDebugOption
  property_count: 2
  slug: iot-events-detector-debug-option
- name: DetectorDebugOptions
  property_count: 0
  slug: iot-events-detector-debug-options
- name: DetectorModelConfiguration
  property_count: 10
  slug: iot-events-detector-model-configuration
- name: DetectorModelDefinition
  property_count: 2
  slug: iot-events-detector-model-definition
- name: DetectorModel
  property_count: 2
  slug: iot-events-detector-model
- name: DetectorModelSummaries
  property_count: 0
  slug: iot-events-detector-model-summaries
- name: DetectorModelSummary
  property_count: 3
  slug: iot-events-detector-model-summary
- name: DetectorModelVersionStatus
  property_count: 0
  slug: iot-events-detector-model-version-status
- name: DetectorModelVersionSummaries
  property_count: 0
  slug: iot-events-detector-model-version-summaries
- name: DetectorModelVersionSummary
  property_count: 8
  slug: iot-events-detector-model-version-summary
- name: DynamoDBAction
  property_count: 10
  slug: iot-events-dynamo-d-b-action
- name: DynamoDBv2Action
  property_count: 2
  slug: iot-events-dynamo-d-bv2-action
- name: EmailConfiguration
  property_count: 3
  slug: iot-events-email-configuration
- name: EmailConfigurations
  property_count: 0
  slug: iot-events-email-configurations
- name: EmailContent
  property_count: 2
  slug: iot-events-email-content
- name: EmailRecipients
  property_count: 1
  slug: iot-events-email-recipients
- name: EvaluationMethod
  property_count: 0
  slug: iot-events-evaluation-method
- name: Event
  property_count: 3
  slug: iot-events-event
- name: Events
  property_count: 0
  slug: iot-events-events
- name: FirehoseAction
  property_count: 3
  slug: iot-events-firehose-action
- name: GetDetectorModelAnalysisResultsRequest
  property_count: 0
  slug: iot-events-get-detector-model-analysis-results-request
- name: GetDetectorModelAnalysisResultsResponse
  property_count: 2
  slug: iot-events-get-detector-model-analysis-results-response
- name: InitializationConfiguration
  property_count: 1
  slug: iot-events-initialization-configuration
- name: InputConfiguration
  property_count: 6
  slug: iot-events-input-configuration
- name: InputDefinition
  property_count: 1
  slug: iot-events-input-definition
- name: InputIdentifier
  property_count: 2
  slug: iot-events-input-identifier
- name: Input
  property_count: 2
  slug: iot-events-input
- name: InputStatus
  property_count: 0
  slug: iot-events-input-status
- name: InputSummaries
  property_count: 0
  slug: iot-events-input-summaries
- name: InputSummary
  property_count: 6
  slug: iot-events-input-summary
- name: IotEventsAction
  property_count: 2
  slug: iot-events-iot-events-action
- name: IotEventsInputIdentifier
  property_count: 1
  slug: iot-events-iot-events-input-identifier
- name: IotSiteWiseAction
  property_count: 5
  slug: iot-events-iot-site-wise-action
- name: IotSiteWiseAssetModelPropertyIdentifier
  property_count: 2
  slug: iot-events-iot-site-wise-asset-model-property-identifier
- name: IotSiteWiseInputIdentifier
  property_count: 1
  slug: iot-events-iot-site-wise-input-identifier
- name: IotTopicPublishAction
  property_count: 2
  slug: iot-events-iot-topic-publish-action
- name: LambdaAction
  property_count: 2
  slug: iot-events-lambda-action
- name: ListAlarmModelVersionsRequest
  property_count: 0
  slug: iot-events-list-alarm-model-versions-request
- name: ListAlarmModelVersionsResponse
  property_count: 2
  slug: iot-events-list-alarm-model-versions-response
- name: ListAlarmModelsRequest
  property_count: 0
  slug: iot-events-list-alarm-models-request
- name: ListAlarmModelsResponse
  property_count: 2
  slug: iot-events-list-alarm-models-response
- name: ListDetectorModelVersionsRequest
  property_count: 0
  slug: iot-events-list-detector-model-versions-request
- name: ListDetectorModelVersionsResponse
  property_count: 2
  slug: iot-events-list-detector-model-versions-response
- name: ListDetectorModelsRequest
  property_count: 0
  slug: iot-events-list-detector-models-request
- name: ListDetectorModelsResponse
  property_count: 2
  slug: iot-events-list-detector-models-response
- name: ListInputRoutingsRequest
  property_count: 3
  slug: iot-events-list-input-routings-request
- name: ListInputRoutingsResponse
  property_count: 2
  slug: iot-events-list-input-routings-response
- name: ListInputsRequest
  property_count: 0
  slug: iot-events-list-inputs-request
- name: ListInputsResponse
  property_count: 2
  slug: iot-events-list-inputs-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: iot-events-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: iot-events-list-tags-for-resource-response
- name: LoggingLevel
  property_count: 0
  slug: iot-events-logging-level
- name: LoggingOptions
  property_count: 4
  slug: iot-events-logging-options
- name: NotificationAction
  property_count: 3
  slug: iot-events-notification-action
- name: NotificationActions
  property_count: 0
  slug: iot-events-notification-actions
- name: NotificationTargetActions
  property_count: 1
  slug: iot-events-notification-target-actions
- name: OnEnterLifecycle
  property_count: 1
  slug: iot-events-on-enter-lifecycle
- name: OnExitLifecycle
  property_count: 1
  slug: iot-events-on-exit-lifecycle
- name: OnInputLifecycle
  property_count: 2
  slug: iot-events-on-input-lifecycle
- name: Payload
  property_count: 2
  slug: iot-events-payload
- name: PayloadType
  property_count: 0
  slug: iot-events-payload-type
- name: PutLoggingOptionsRequest
  property_count: 1
  slug: iot-events-put-logging-options-request
- name: RecipientDetail
  property_count: 1
  slug: iot-events-recipient-detail
- name: RecipientDetails
  property_count: 0
  slug: iot-events-recipient-details
- name: ResetTimerAction
  property_count: 1
  slug: iot-events-reset-timer-action
- name: RoutedResource
  property_count: 2
  slug: iot-events-routed-resource
- name: RoutedResources
  property_count: 0
  slug: iot-events-routed-resources
- name: SMSConfiguration
  property_count: 3
  slug: iot-events-s-m-s-configuration
- name: SMSConfigurations
  property_count: 0
  slug: iot-events-s-m-s-configurations
- name: SNSTopicPublishAction
  property_count: 2
  slug: iot-events-s-n-s-topic-publish-action
- name: SSOIdentity
  property_count: 2
  slug: iot-events-s-s-o-identity
- name: SetTimerAction
  property_count: 3
  slug: iot-events-set-timer-action
- name: SetVariableAction
  property_count: 2
  slug: iot-events-set-variable-action
- name: SimpleRule
  property_count: 3
  slug: iot-events-simple-rule
- name: SqsAction
  property_count: 3
  slug: iot-events-sqs-action
- name: StartDetectorModelAnalysisRequest
  property_count: 1
  slug: iot-events-start-detector-model-analysis-request
- name: StartDetectorModelAnalysisResponse
  property_count: 1
  slug: iot-events-start-detector-model-analysis-response
- name: State
  property_count: 4
  slug: iot-events-state
- name: States
  property_count: 0
  slug: iot-events-states
- name: TagKeys
  property_count: 0
  slug: iot-events-tag-keys
- name: TagResourceRequest
  property_count: 1
  slug: iot-events-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: iot-events-tag-resource-response
- name: Tag
  property_count: 2
  slug: iot-events-tag
- name: Tags
  property_count: 0
  slug: iot-events-tags
- name: TransitionEvent
  property_count: 4
  slug: iot-events-transition-event
- name: TransitionEvents
  property_count: 0
  slug: iot-events-transition-events
- name: UntagResourceRequest
  property_count: 0
  slug: iot-events-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: iot-events-untag-resource-response
- name: UpdateAlarmModelRequest
  property_count: 7
  slug: iot-events-update-alarm-model-request
- name: UpdateAlarmModelResponse
  property_count: 5
  slug: iot-events-update-alarm-model-response
- name: UpdateDetectorModelRequest
  property_count: 4
  slug: iot-events-update-detector-model-request
- name: UpdateDetectorModelResponse
  property_count: 1
  slug: iot-events-update-detector-model-response
- name: UpdateInputRequest
  property_count: 2
  slug: iot-events-update-input-request
- name: UpdateInputResponse
  property_count: 1
  slug: iot-events-update-input-response
json_structures:
- name: Iot Events Acknowledge Flow Structure
  property_count: 1
  slug: iot-events-acknowledge-flow-structure
- name: Iot Events Action Structure
  property_count: 13
  slug: iot-events-action-structure
- name: Iot Events Actions Structure
  property_count: 0
  slug: iot-events-actions-structure
- name: Iot Events Alarm Action Structure
  property_count: 9
  slug: iot-events-alarm-action-structure
- name: Iot Events Alarm Actions Structure
  property_count: 0
  slug: iot-events-alarm-actions-structure
- name: Iot Events Alarm Capabilities Structure
  property_count: 2
  slug: iot-events-alarm-capabilities-structure
- name: Iot Events Alarm Event Actions Structure
  property_count: 1
  slug: iot-events-alarm-event-actions-structure
- name: Iot Events Alarm Model Summaries Structure
  property_count: 0
  slug: iot-events-alarm-model-summaries-structure
- name: Iot Events Alarm Model Summary Structure
  property_count: 3
  slug: iot-events-alarm-model-summary-structure
- name: Iot Events Alarm Model Version Status Structure
  property_count: 0
  slug: iot-events-alarm-model-version-status-structure
- name: Iot Events Alarm Model Version Summaries Structure
  property_count: 0
  slug: iot-events-alarm-model-version-summaries-structure
- name: Iot Events Alarm Model Version Summary Structure
  property_count: 8
  slug: iot-events-alarm-model-version-summary-structure
- name: Iot Events Alarm Notification Structure
  property_count: 1
  slug: iot-events-alarm-notification-structure
- name: Iot Events Alarm Rule Structure
  property_count: 1
  slug: iot-events-alarm-rule-structure
- name: Iot Events Analysis Result Level Structure
  property_count: 0
  slug: iot-events-analysis-result-level-structure
- name: Iot Events Analysis Result Location Structure
  property_count: 1
  slug: iot-events-analysis-result-location-structure
- name: Iot Events Analysis Result Locations Structure
  property_count: 0
  slug: iot-events-analysis-result-locations-structure
- name: Iot Events Analysis Result Structure
  property_count: 4
  slug: iot-events-analysis-result-structure
- name: Iot Events Analysis Results Structure
  property_count: 0
  slug: iot-events-analysis-results-structure
- name: Iot Events Analysis Status Structure
  property_count: 0
  slug: iot-events-analysis-status-structure
- name: Iot Events Asset Property Timestamp Structure
  property_count: 2
  slug: iot-events-asset-property-timestamp-structure
- name: Iot Events Asset Property Value Structure
  property_count: 3
  slug: iot-events-asset-property-value-structure
- name: Iot Events Asset Property Variant Structure
  property_count: 4
  slug: iot-events-asset-property-variant-structure
- name: Iot Events Attribute Structure
  property_count: 1
  slug: iot-events-attribute-structure
- name: Iot Events Attributes Structure
  property_count: 0
  slug: iot-events-attributes-structure
- name: Iot Events Clear Timer Action Structure
  property_count: 1
  slug: iot-events-clear-timer-action-structure
- name: Iot Events Comparison Operator Structure
  property_count: 0
  slug: iot-events-comparison-operator-structure
- name: Iot Events Create Alarm Model Request Structure
  property_count: 10
  slug: iot-events-create-alarm-model-request-structure
- name: Iot Events Create Alarm Model Response Structure
  property_count: 5
  slug: iot-events-create-alarm-model-response-structure
- name: Iot Events Create Detector Model Request Structure
  property_count: 7
  slug: iot-events-create-detector-model-request-structure
- name: Iot Events Create Detector Model Response Structure
  property_count: 1
  slug: iot-events-create-detector-model-response-structure
- name: Iot Events Create Input Request Structure
  property_count: 4
  slug: iot-events-create-input-request-structure
- name: Iot Events Create Input Response Structure
  property_count: 1
  slug: iot-events-create-input-response-structure
- name: Iot Events Delete Alarm Model Request Structure
  property_count: 0
  slug: iot-events-delete-alarm-model-request-structure
- name: Iot Events Delete Alarm Model Response Structure
  property_count: 0
  slug: iot-events-delete-alarm-model-response-structure
- name: Iot Events Delete Detector Model Request Structure
  property_count: 0
  slug: iot-events-delete-detector-model-request-structure
- name: Iot Events Delete Detector Model Response Structure
  property_count: 0
  slug: iot-events-delete-detector-model-response-structure
- name: Iot Events Delete Input Request Structure
  property_count: 0
  slug: iot-events-delete-input-request-structure
- name: Iot Events Delete Input Response Structure
  property_count: 0
  slug: iot-events-delete-input-response-structure
- name: Iot Events Describe Alarm Model Request Structure
  property_count: 0
  slug: iot-events-describe-alarm-model-request-structure
- name: Iot Events Describe Alarm Model Response Structure
  property_count: 15
  slug: iot-events-describe-alarm-model-response-structure
- name: Iot Events Describe Detector Model Analysis Request Structure
  property_count: 0
  slug: iot-events-describe-detector-model-analysis-request-structure
- name: Iot Events Describe Detector Model Analysis Response Structure
  property_count: 1
  slug: iot-events-describe-detector-model-analysis-response-structure
- name: Iot Events Describe Detector Model Request Structure
  property_count: 0
  slug: iot-events-describe-detector-model-request-structure
- name: Iot Events Describe Detector Model Response Structure
  property_count: 1
  slug: iot-events-describe-detector-model-response-structure
- name: Iot Events Describe Input Request Structure
  property_count: 0
  slug: iot-events-describe-input-request-structure
- name: Iot Events Describe Input Response Structure
  property_count: 1
  slug: iot-events-describe-input-response-structure
- name: Iot Events Describe Logging Options Request Structure
  property_count: 0
  slug: iot-events-describe-logging-options-request-structure
- name: Iot Events Describe Logging Options Response Structure
  property_count: 1
  slug: iot-events-describe-logging-options-response-structure
- name: Iot Events Detector Debug Option Structure
  property_count: 2
  slug: iot-events-detector-debug-option-structure
- name: Iot Events Detector Debug Options Structure
  property_count: 0
  slug: iot-events-detector-debug-options-structure
- name: Iot Events Detector Model Configuration Structure
  property_count: 10
  slug: iot-events-detector-model-configuration-structure
- name: Iot Events Detector Model Definition Structure
  property_count: 2
  slug: iot-events-detector-model-definition-structure
- name: Iot Events Detector Model Structure
  property_count: 2
  slug: iot-events-detector-model-structure
- name: Iot Events Detector Model Summaries Structure
  property_count: 0
  slug: iot-events-detector-model-summaries-structure
- name: Iot Events Detector Model Summary Structure
  property_count: 3
  slug: iot-events-detector-model-summary-structure
- name: Iot Events Detector Model Version Status Structure
  property_count: 0
  slug: iot-events-detector-model-version-status-structure
- name: Iot Events Detector Model Version Summaries Structure
  property_count: 0
  slug: iot-events-detector-model-version-summaries-structure
- name: Iot Events Detector Model Version Summary Structure
  property_count: 8
  slug: iot-events-detector-model-version-summary-structure
- name: Iot Events Dynamo D B Action Structure
  property_count: 10
  slug: iot-events-dynamo-d-b-action-structure
- name: Iot Events Dynamo D Bv2 Action Structure
  property_count: 2
  slug: iot-events-dynamo-d-bv2-action-structure
- name: Iot Events Email Configuration Structure
  property_count: 3
  slug: iot-events-email-configuration-structure
- name: Iot Events Email Configurations Structure
  property_count: 0
  slug: iot-events-email-configurations-structure
- name: Iot Events Email Content Structure
  property_count: 2
  slug: iot-events-email-content-structure
- name: Iot Events Email Recipients Structure
  property_count: 1
  slug: iot-events-email-recipients-structure
- name: Iot Events Evaluation Method Structure
  property_count: 0
  slug: iot-events-evaluation-method-structure
- name: Iot Events Event Structure
  property_count: 3
  slug: iot-events-event-structure
- name: Iot Events Events Structure
  property_count: 0
  slug: iot-events-events-structure
- name: Iot Events Firehose Action Structure
  property_count: 3
  slug: iot-events-firehose-action-structure
- name: Iot Events Get Detector Model Analysis Results Request Structure
  property_count: 0
  slug: iot-events-get-detector-model-analysis-results-request-structure
- name: Iot Events Get Detector Model Analysis Results Response Structure
  property_count: 2
  slug: iot-events-get-detector-model-analysis-results-response-structure
- name: Iot Events Initialization Configuration Structure
  property_count: 1
  slug: iot-events-initialization-configuration-structure
- name: Iot Events Input Configuration Structure
  property_count: 6
  slug: iot-events-input-configuration-structure
- name: Iot Events Input Definition Structure
  property_count: 1
  slug: iot-events-input-definition-structure
- name: Iot Events Input Identifier Structure
  property_count: 2
  slug: iot-events-input-identifier-structure
- name: Iot Events Input Status Structure
  property_count: 0
  slug: iot-events-input-status-structure
- name: Iot Events Input Structure
  property_count: 2
  slug: iot-events-input-structure
- name: Iot Events Input Summaries Structure
  property_count: 0
  slug: iot-events-input-summaries-structure
- name: Iot Events Input Summary Structure
  property_count: 6
  slug: iot-events-input-summary-structure
- name: Iot Events Iot Events Action Structure
  property_count: 2
  slug: iot-events-iot-events-action-structure
- name: Iot Events Iot Events Input Identifier Structure
  property_count: 1
  slug: iot-events-iot-events-input-identifier-structure
- name: Iot Events Iot Site Wise Action Structure
  property_count: 5
  slug: iot-events-iot-site-wise-action-structure
- name: Iot Events Iot Site Wise Asset Model Property Identifier Structure
  property_count: 2
  slug: iot-events-iot-site-wise-asset-model-property-identifier-structure
- name: Iot Events Iot Site Wise Input Identifier Structure
  property_count: 1
  slug: iot-events-iot-site-wise-input-identifier-structure
- name: Iot Events Iot Topic Publish Action Structure
  property_count: 2
  slug: iot-events-iot-topic-publish-action-structure
- name: Iot Events Lambda Action Structure
  property_count: 2
  slug: iot-events-lambda-action-structure
- name: Iot Events List Alarm Model Versions Request Structure
  property_count: 0
  slug: iot-events-list-alarm-model-versions-request-structure
- name: Iot Events List Alarm Model Versions Response Structure
  property_count: 2
  slug: iot-events-list-alarm-model-versions-response-structure
- name: Iot Events List Alarm Models Request Structure
  property_count: 0
  slug: iot-events-list-alarm-models-request-structure
- name: Iot Events List Alarm Models Response Structure
  property_count: 2
  slug: iot-events-list-alarm-models-response-structure
- name: Iot Events List Detector Model Versions Request Structure
  property_count: 0
  slug: iot-events-list-detector-model-versions-request-structure
- name: Iot Events List Detector Model Versions Response Structure
  property_count: 2
  slug: iot-events-list-detector-model-versions-response-structure
- name: Iot Events List Detector Models Request Structure
  property_count: 0
  slug: iot-events-list-detector-models-request-structure
- name: Iot Events List Detector Models Response Structure
  property_count: 2
  slug: iot-events-list-detector-models-response-structure
- name: Iot Events List Input Routings Request Structure
  property_count: 3
  slug: iot-events-list-input-routings-request-structure
- name: Iot Events List Input Routings Response Structure
  property_count: 2
  slug: iot-events-list-input-routings-response-structure
- name: Iot Events List Inputs Request Structure
  property_count: 0
  slug: iot-events-list-inputs-request-structure
- name: Iot Events List Inputs Response Structure
  property_count: 2
  slug: iot-events-list-inputs-response-structure
- name: Iot Events List Tags For Resource Request Structure
  property_count: 0
  slug: iot-events-list-tags-for-resource-request-structure
- name: Iot Events List Tags For Resource Response Structure
  property_count: 1
  slug: iot-events-list-tags-for-resource-response-structure
- name: Iot Events Logging Level Structure
  property_count: 0
  slug: iot-events-logging-level-structure
- name: Iot Events Logging Options Structure
  property_count: 4
  slug: iot-events-logging-options-structure
- name: Iot Events Notification Action Structure
  property_count: 3
  slug: iot-events-notification-action-structure
- name: Iot Events Notification Actions Structure
  property_count: 0
  slug: iot-events-notification-actions-structure
- name: Iot Events Notification Target Actions Structure
  property_count: 1
  slug: iot-events-notification-target-actions-structure
- name: Iot Events On Enter Lifecycle Structure
  property_count: 1
  slug: iot-events-on-enter-lifecycle-structure
- name: Iot Events On Exit Lifecycle Structure
  property_count: 1
  slug: iot-events-on-exit-lifecycle-structure
- name: Iot Events On Input Lifecycle Structure
  property_count: 2
  slug: iot-events-on-input-lifecycle-structure
- name: Iot Events Payload Structure
  property_count: 2
  slug: iot-events-payload-structure
- name: Iot Events Payload Type Structure
  property_count: 0
  slug: iot-events-payload-type-structure
- name: Iot Events Put Logging Options Request Structure
  property_count: 1
  slug: iot-events-put-logging-options-request-structure
- name: Iot Events Recipient Detail Structure
  property_count: 1
  slug: iot-events-recipient-detail-structure
- name: Iot Events Recipient Details Structure
  property_count: 0
  slug: iot-events-recipient-details-structure
- name: Iot Events Reset Timer Action Structure
  property_count: 1
  slug: iot-events-reset-timer-action-structure
- name: Iot Events Routed Resource Structure
  property_count: 2
  slug: iot-events-routed-resource-structure
- name: Iot Events Routed Resources Structure
  property_count: 0
  slug: iot-events-routed-resources-structure
- name: Iot Events S M S Configuration Structure
  property_count: 3
  slug: iot-events-s-m-s-configuration-structure
- name: Iot Events S M S Configurations Structure
  property_count: 0
  slug: iot-events-s-m-s-configurations-structure
- name: Iot Events S N S Topic Publish Action Structure
  property_count: 2
  slug: iot-events-s-n-s-topic-publish-action-structure
- name: Iot Events S S O Identity Structure
  property_count: 2
  slug: iot-events-s-s-o-identity-structure
- name: Iot Events Set Timer Action Structure
  property_count: 3
  slug: iot-events-set-timer-action-structure
- name: Iot Events Set Variable Action Structure
  property_count: 2
  slug: iot-events-set-variable-action-structure
- name: Iot Events Simple Rule Structure
  property_count: 3
  slug: iot-events-simple-rule-structure
- name: Iot Events Sqs Action Structure
  property_count: 3
  slug: iot-events-sqs-action-structure
- name: Iot Events Start Detector Model Analysis Request Structure
  property_count: 1
  slug: iot-events-start-detector-model-analysis-request-structure
- name: Iot Events Start Detector Model Analysis Response Structure
  property_count: 1
  slug: iot-events-start-detector-model-analysis-response-structure
- name: Iot Events State Structure
  property_count: 4
  slug: iot-events-state-structure
- name: Iot Events States Structure
  property_count: 0
  slug: iot-events-states-structure
- name: Iot Events Tag Keys Structure
  property_count: 0
  slug: iot-events-tag-keys-structure
- name: Iot Events Tag Resource Request Structure
  property_count: 1
  slug: iot-events-tag-resource-request-structure
- name: Iot Events Tag Resource Response Structure
  property_count: 0
  slug: iot-events-tag-resource-response-structure
- name: Iot Events Tag Structure
  property_count: 2
  slug: iot-events-tag-structure
- name: Iot Events Tags Structure
  property_count: 0
  slug: iot-events-tags-structure
- name: Iot Events Transition Event Structure
  property_count: 4
  slug: iot-events-transition-event-structure
- name: Iot Events Transition Events Structure
  property_count: 0
  slug: iot-events-transition-events-structure
- name: Iot Events Untag Resource Request Structure
  property_count: 0
  slug: iot-events-untag-resource-request-structure
- name: Iot Events Untag Resource Response Structure
  property_count: 0
  slug: iot-events-untag-resource-response-structure
- name: Iot Events Update Alarm Model Request Structure
  property_count: 7
  slug: iot-events-update-alarm-model-request-structure
- name: Iot Events Update Alarm Model Response Structure
  property_count: 5
  slug: iot-events-update-alarm-model-response-structure
- name: Iot Events Update Detector Model Request Structure
  property_count: 4
  slug: iot-events-update-detector-model-request-structure
- name: Iot Events Update Detector Model Response Structure
  property_count: 1
  slug: iot-events-update-detector-model-response-structure
- name: Iot Events Update Input Request Structure
  property_count: 2
  slug: iot-events-update-input-request-structure
- name: Iot Events Update Input Response Structure
  property_count: 1
  slug: iot-events-update-input-response-structure
jsonld:
- class_count: 101
  name: Amazon Iot Events Context
  property_count: 141
  slug: amazon-iot-events-context
layout: provider
modified: '2026-05-19'
name: Amazon IoT Events
nav: Providers
network: true
overview: 'Amazon IoT Events publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Alarm Models API, Analysis API, Detector Models API, and 5 more. Tagged areas include Event Detection, IoT, State Machine, and Automation.


  The Amazon IoT Events catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon IoT Events'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 15 more developer resources.'
plans:
- name: Amazon Iot Events Plans Pricing
  plan_count: 3
  slug: amazon-iot-events-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Amazon Iot Events Rate Limits
  slug: amazon-iot-events-rate-limits
rules:
- name: Amazon IoT Events API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-iot-events-jsonschema-spectral-rules
- name: Amazon IoT Events API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 9
  slug: amazon-iot-events-spectral-rules
score:
  band: strong
  composite: 64.2
  delta: -3.2
  facets:
    commercial_clarity: 81.6
    contract_quality: 68.5
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-iot-events/refs/heads/main/screenshots/amazon-iot-events-2026-06-20T171710.png
security:
- kind: authentication
  name: Amazon Iot Events Authentication
  slug: amazon-iot-events-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Iot Events Domain Security
  slug: amazon-iot-events-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Iot Events Vulnerability Disclosure
  slug: amazon-iot-events-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Iot Events Trust Center
  slug: amazon-iot-events-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-iot-events
tags:
- Event Detection
- IoT
- State Machine
- Automation
use_cases:
- description: Detect equipment failures and trigger maintenance workflows automatically.
  name: Industrial Alarm Management
- description: Detect patterns across multiple sensor streams over time.
  name: Complex Event Processing
- description: Alert operations teams when device metrics indicate impending failure.
  name: Predictive Maintenance
website: https://aws.amazon.com/iot-events/
---
