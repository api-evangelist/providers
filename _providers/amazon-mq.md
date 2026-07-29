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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Amazon Mq Agentic Access
  operation_count: 22
  slug: amazon-mq-agentic-access
  summary_line: 22 operations · 11 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Broker Engine Types API from Amazon MQ — 1 operation(s) for broker engine types.
  name: Amazon MQ Broker Engine Types API
  slug: amazon-mq-broker-engine-types-api
- description: The Broker Instance Options API from Amazon MQ — 1 operation(s) for broker instance options.
  name: Amazon MQ Broker Instance Options API
  slug: amazon-mq-broker-instance-options-api
- description: The Brokers API from Amazon MQ — 5 operation(s) for brokers.
  name: Amazon MQ Brokers API
  slug: amazon-mq-brokers-api
- description: The Configurations API from Amazon MQ — 4 operation(s) for configurations.
  name: Amazon MQ Configurations API
  slug: amazon-mq-configurations-api
- description: The Tags API from Amazon MQ — 2 operation(s) for tags.
  name: Amazon MQ Tags API
  slug: amazon-mq-tags-api
artifact_total: 254
collections:
- collection_type: postman
  name: AmazonMQ Broker Engine Types API
  slug: postman-amazon-mq-broker-engine-types-api
- collection_type: postman
  name: AmazonMQ Broker Engine Types Broker Instance Options API
  slug: postman-amazon-mq-broker-instance-options-api
- collection_type: postman
  name: AmazonMQ Broker Engine Types Brokers API
  slug: postman-amazon-mq-brokers-api
- collection_type: postman
  name: AmazonMQ Broker Engine Types Configurations API
  slug: postman-amazon-mq-configurations-api
- collection_type: postman
  name: AmazonMQ Broker Engine Types Tags API
  slug: postman-amazon-mq-tags-api
- collection_type: open
  name: Amazon MQ API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-mq/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-mq-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-mq-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-mq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-mq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-mq-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/mq/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mq/
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
  url: https://aws.amazon.com/blogs/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/mq/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
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
  url: rules/amazon-mq-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-mq-vocabulary.yaml
created: '2026-03-16'
description: Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud, enabling you to migrate to a message broker without writing the code that typically enables interoperability with existing applications.
examples:
- key_count: 2
  name: Mq Api Action Required Example
  slug: mq-api-action-required-example
- key_count: 0
  name: Mq Api Authentication Strategy Example
  slug: mq-api-authentication-strategy-example
- key_count: 1
  name: Mq Api Availability Zone Example
  slug: mq-api-availability-zone-example
- key_count: 2
  name: Mq Api Broker Engine Type Example
  slug: mq-api-broker-engine-type-example
- key_count: 3
  name: Mq Api Broker Instance Example
  slug: mq-api-broker-instance-example
- key_count: 6
  name: Mq Api Broker Instance Option Example
  slug: mq-api-broker-instance-option-example
- key_count: 0
  name: Mq Api Broker State Example
  slug: mq-api-broker-state-example
- key_count: 0
  name: Mq Api Broker Storage Type Example
  slug: mq-api-broker-storage-type-example
- key_count: 8
  name: Mq Api Broker Summary Example
  slug: mq-api-broker-summary-example
- key_count: 0
  name: Mq Api Change Type Example
  slug: mq-api-change-type-example
- key_count: 10
  name: Mq Api Configuration Example
  slug: mq-api-configuration-example
- key_count: 2
  name: Mq Api Configuration Id Example
  slug: mq-api-configuration-id-example
- key_count: 3
  name: Mq Api Configuration Revision Example
  slug: mq-api-configuration-revision-example
- key_count: 3
  name: Mq Api Configurations Example
  slug: mq-api-configurations-example
- key_count: 19
  name: Mq Api Create Broker Request Example
  slug: mq-api-create-broker-request-example
- key_count: 2
  name: Mq Api Create Broker Response Example
  slug: mq-api-create-broker-response-example
- key_count: 5
  name: Mq Api Create Configuration Request Example
  slug: mq-api-create-configuration-request-example
- key_count: 6
  name: Mq Api Create Configuration Response Example
  slug: mq-api-create-configuration-response-example
- key_count: 1
  name: Mq Api Create Tags Request Example
  slug: mq-api-create-tags-request-example
- key_count: 3
  name: Mq Api Create User Request Example
  slug: mq-api-create-user-request-example
- key_count: 0
  name: Mq Api Create User Response Example
  slug: mq-api-create-user-response-example
- key_count: 0
  name: Mq Api Day Of Week Example
  slug: mq-api-day-of-week-example
- key_count: 0
  name: Mq Api Delete Broker Request Example
  slug: mq-api-delete-broker-request-example
- key_count: 1
  name: Mq Api Delete Broker Response Example
  slug: mq-api-delete-broker-response-example
- key_count: 0
  name: Mq Api Delete Tags Request Example
  slug: mq-api-delete-tags-request-example
- key_count: 0
  name: Mq Api Delete User Request Example
  slug: mq-api-delete-user-request-example
- key_count: 0
  name: Mq Api Delete User Response Example
  slug: mq-api-delete-user-response-example
- key_count: 0
  name: Mq Api Deployment Mode Example
  slug: mq-api-deployment-mode-example
- key_count: 0
  name: Mq Api Describe Broker Engine Types Request Example
  slug: mq-api-describe-broker-engine-types-request-example
- key_count: 3
  name: Mq Api Describe Broker Engine Types Response Example
  slug: mq-api-describe-broker-engine-types-response-example
- key_count: 0
  name: Mq Api Describe Broker Instance Options Request Example
  slug: mq-api-describe-broker-instance-options-request-example
- key_count: 3
  name: Mq Api Describe Broker Instance Options Response Example
  slug: mq-api-describe-broker-instance-options-response-example
- key_count: 0
  name: Mq Api Describe Broker Request Example
  slug: mq-api-describe-broker-request-example
- key_count: 29
  name: Mq Api Describe Broker Response Example
  slug: mq-api-describe-broker-response-example
- key_count: 0
  name: Mq Api Describe Configuration Request Example
  slug: mq-api-describe-configuration-request-example
- key_count: 10
  name: Mq Api Describe Configuration Response Example
  slug: mq-api-describe-configuration-response-example
- key_count: 0
  name: Mq Api Describe Configuration Revision Request Example
  slug: mq-api-describe-configuration-revision-request-example
- key_count: 4
  name: Mq Api Describe Configuration Revision Response Example
  slug: mq-api-describe-configuration-revision-response-example
- key_count: 0
  name: Mq Api Describe User Request Example
  slug: mq-api-describe-user-request-example
- key_count: 5
  name: Mq Api Describe User Response Example
  slug: mq-api-describe-user-response-example
- key_count: 2
  name: Mq Api Encryption Options Example
  slug: mq-api-encryption-options-example
- key_count: 0
  name: Mq Api Engine Type Example
  slug: mq-api-engine-type-example
- key_count: 1
  name: Mq Api Engine Version Example
  slug: mq-api-engine-version-example
- key_count: 11
  name: Mq Api Ldap Server Metadata Input Example
  slug: mq-api-ldap-server-metadata-input-example
- key_count: 10
  name: Mq Api Ldap Server Metadata Output Example
  slug: mq-api-ldap-server-metadata-output-example
- key_count: 0
  name: Mq Api List Brokers Request Example
  slug: mq-api-list-brokers-request-example
- key_count: 2
  name: Mq Api List Brokers Response Example
  slug: mq-api-list-brokers-response-example
- key_count: 0
  name: Mq Api List Configuration Revisions Request Example
  slug: mq-api-list-configuration-revisions-request-example
- key_count: 4
  name: Mq Api List Configuration Revisions Response Example
  slug: mq-api-list-configuration-revisions-response-example
- key_count: 0
  name: Mq Api List Configurations Request Example
  slug: mq-api-list-configurations-request-example
- key_count: 3
  name: Mq Api List Configurations Response Example
  slug: mq-api-list-configurations-response-example
- key_count: 0
  name: Mq Api List Tags Request Example
  slug: mq-api-list-tags-request-example
- key_count: 1
  name: Mq Api List Tags Response Example
  slug: mq-api-list-tags-response-example
- key_count: 0
  name: Mq Api List Users Request Example
  slug: mq-api-list-users-request-example
- key_count: 4
  name: Mq Api List Users Response Example
  slug: mq-api-list-users-response-example
- key_count: 2
  name: Mq Api Logs Example
  slug: mq-api-logs-example
- key_count: 5
  name: Mq Api Logs Summary Example
  slug: mq-api-logs-summary-example
- key_count: 0
  name: Mq Api Max Results Example
  slug: mq-api-max-results-example
- key_count: 2
  name: Mq Api Pending Logs Example
  slug: mq-api-pending-logs-example
- key_count: 0
  name: Mq Api Reboot Broker Request Example
  slug: mq-api-reboot-broker-request-example
- key_count: 0
  name: Mq Api Reboot Broker Response Example
  slug: mq-api-reboot-broker-response-example
- key_count: 3
  name: Mq Api Sanitization Warning Example
  slug: mq-api-sanitization-warning-example
- key_count: 0
  name: Mq Api Sanitization Warning Reason Example
  slug: mq-api-sanitization-warning-reason-example
- key_count: 0
  name: Mq Api Unauthorized Exception Example
  slug: mq-api-unauthorized-exception-example
- key_count: 9
  name: Mq Api Update Broker Request Example
  slug: mq-api-update-broker-request-example
- key_count: 10
  name: Mq Api Update Broker Response Example
  slug: mq-api-update-broker-response-example
- key_count: 2
  name: Mq Api Update Configuration Request Example
  slug: mq-api-update-configuration-request-example
- key_count: 6
  name: Mq Api Update Configuration Response Example
  slug: mq-api-update-configuration-response-example
- key_count: 3
  name: Mq Api Update User Request Example
  slug: mq-api-update-user-request-example
- key_count: 0
  name: Mq Api Update User Response Example
  slug: mq-api-update-user-response-example
- key_count: 4
  name: Mq Api User Example
  slug: mq-api-user-example
- key_count: 3
  name: Mq Api User Pending Changes Example
  slug: mq-api-user-pending-changes-example
- key_count: 2
  name: Mq Api User Summary Example
  slug: mq-api-user-summary-example
- key_count: 3
  name: Mq Api Weekly Start Time Example
  slug: mq-api-weekly-start-time-example
features:
- description: Fully managed Apache ActiveMQ and RabbitMQ brokers with automated provisioning and maintenance.
  name: Managed Message Brokers
- description: Supports AMQP, MQTT, OpenWire, STOMP, and WebSocket protocols for broad compatibility.
  name: Protocol Support
- description: Active/standby configurations with automatic failover for high availability.
  name: High Availability
- description: Create networks of brokers for distributed messaging across regions and availability zones.
  name: Network of Brokers
- description: Programmatically create, configure, and manage brokers and configurations.
  name: Broker Management API
- description: Encryption at rest and in transit, VPC isolation, and IAM integration.
  name: Security
finops:
- name: Amazon Mq Finops
  service_category: API
  slug: amazon-mq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-mq.png
json_schemas:
- name: ActionRequired
  property_count: 2
  slug: mq-api-action-required
- name: AuthenticationStrategy
  property_count: 0
  slug: mq-api-authentication-strategy
- name: AvailabilityZone
  property_count: 1
  slug: mq-api-availability-zone
- name: BrokerEngineType
  property_count: 2
  slug: mq-api-broker-engine-type
- name: BrokerInstanceOption
  property_count: 6
  slug: mq-api-broker-instance-option
- name: BrokerInstance
  property_count: 3
  slug: mq-api-broker-instance
- name: BrokerState
  property_count: 0
  slug: mq-api-broker-state
- name: BrokerStorageType
  property_count: 0
  slug: mq-api-broker-storage-type
- name: BrokerSummary
  property_count: 8
  slug: mq-api-broker-summary
- name: ChangeType
  property_count: 0
  slug: mq-api-change-type
- name: ConfigurationId
  property_count: 2
  slug: mq-api-configuration-id
- name: ConfigurationRevision
  property_count: 3
  slug: mq-api-configuration-revision
- name: Configuration
  property_count: 10
  slug: mq-api-configuration
- name: Configurations
  property_count: 3
  slug: mq-api-configurations
- name: CreateBrokerRequest
  property_count: 19
  slug: mq-api-create-broker-request
- name: CreateBrokerResponse
  property_count: 2
  slug: mq-api-create-broker-response
- name: CreateConfigurationRequest
  property_count: 5
  slug: mq-api-create-configuration-request
- name: CreateConfigurationResponse
  property_count: 6
  slug: mq-api-create-configuration-response
- name: CreateTagsRequest
  property_count: 1
  slug: mq-api-create-tags-request
- name: CreateUserRequest
  property_count: 3
  slug: mq-api-create-user-request
- name: CreateUserResponse
  property_count: 0
  slug: mq-api-create-user-response
- name: DayOfWeek
  property_count: 0
  slug: mq-api-day-of-week
- name: DeleteBrokerRequest
  property_count: 0
  slug: mq-api-delete-broker-request
- name: DeleteBrokerResponse
  property_count: 1
  slug: mq-api-delete-broker-response
- name: DeleteTagsRequest
  property_count: 0
  slug: mq-api-delete-tags-request
- name: DeleteUserRequest
  property_count: 0
  slug: mq-api-delete-user-request
- name: DeleteUserResponse
  property_count: 0
  slug: mq-api-delete-user-response
- name: DeploymentMode
  property_count: 0
  slug: mq-api-deployment-mode
- name: DescribeBrokerEngineTypesRequest
  property_count: 0
  slug: mq-api-describe-broker-engine-types-request
- name: DescribeBrokerEngineTypesResponse
  property_count: 3
  slug: mq-api-describe-broker-engine-types-response
- name: DescribeBrokerInstanceOptionsRequest
  property_count: 0
  slug: mq-api-describe-broker-instance-options-request
- name: DescribeBrokerInstanceOptionsResponse
  property_count: 3
  slug: mq-api-describe-broker-instance-options-response
- name: DescribeBrokerRequest
  property_count: 0
  slug: mq-api-describe-broker-request
- name: DescribeBrokerResponse
  property_count: 29
  slug: mq-api-describe-broker-response
- name: DescribeConfigurationRequest
  property_count: 0
  slug: mq-api-describe-configuration-request
- name: DescribeConfigurationResponse
  property_count: 10
  slug: mq-api-describe-configuration-response
- name: DescribeConfigurationRevisionRequest
  property_count: 0
  slug: mq-api-describe-configuration-revision-request
- name: DescribeConfigurationRevisionResponse
  property_count: 4
  slug: mq-api-describe-configuration-revision-response
- name: DescribeUserRequest
  property_count: 0
  slug: mq-api-describe-user-request
- name: DescribeUserResponse
  property_count: 5
  slug: mq-api-describe-user-response
- name: EncryptionOptions
  property_count: 2
  slug: mq-api-encryption-options
- name: EngineType
  property_count: 0
  slug: mq-api-engine-type
- name: EngineVersion
  property_count: 1
  slug: mq-api-engine-version
- name: LdapServerMetadataInput
  property_count: 11
  slug: mq-api-ldap-server-metadata-input
- name: LdapServerMetadataOutput
  property_count: 10
  slug: mq-api-ldap-server-metadata-output
- name: ListBrokersRequest
  property_count: 0
  slug: mq-api-list-brokers-request
- name: ListBrokersResponse
  property_count: 2
  slug: mq-api-list-brokers-response
- name: ListConfigurationRevisionsRequest
  property_count: 0
  slug: mq-api-list-configuration-revisions-request
- name: ListConfigurationRevisionsResponse
  property_count: 4
  slug: mq-api-list-configuration-revisions-response
- name: ListConfigurationsRequest
  property_count: 0
  slug: mq-api-list-configurations-request
- name: ListConfigurationsResponse
  property_count: 3
  slug: mq-api-list-configurations-response
- name: ListTagsRequest
  property_count: 0
  slug: mq-api-list-tags-request
- name: ListTagsResponse
  property_count: 1
  slug: mq-api-list-tags-response
- name: ListUsersRequest
  property_count: 0
  slug: mq-api-list-users-request
- name: ListUsersResponse
  property_count: 4
  slug: mq-api-list-users-response
- name: Logs
  property_count: 2
  slug: mq-api-logs
- name: LogsSummary
  property_count: 5
  slug: mq-api-logs-summary
- name: MaxResults
  property_count: 0
  slug: mq-api-max-results
- name: PendingLogs
  property_count: 2
  slug: mq-api-pending-logs
- name: RebootBrokerRequest
  property_count: 0
  slug: mq-api-reboot-broker-request
- name: RebootBrokerResponse
  property_count: 0
  slug: mq-api-reboot-broker-response
- name: SanitizationWarningReason
  property_count: 0
  slug: mq-api-sanitization-warning-reason
- name: SanitizationWarning
  property_count: 3
  slug: mq-api-sanitization-warning
- name: UnauthorizedException
  property_count: 0
  slug: mq-api-unauthorized-exception
- name: UpdateBrokerRequest
  property_count: 9
  slug: mq-api-update-broker-request
- name: UpdateBrokerResponse
  property_count: 10
  slug: mq-api-update-broker-response
- name: UpdateConfigurationRequest
  property_count: 2
  slug: mq-api-update-configuration-request
- name: UpdateConfigurationResponse
  property_count: 6
  slug: mq-api-update-configuration-response
- name: UpdateUserRequest
  property_count: 3
  slug: mq-api-update-user-request
- name: UpdateUserResponse
  property_count: 0
  slug: mq-api-update-user-response
- name: UserPendingChanges
  property_count: 3
  slug: mq-api-user-pending-changes
- name: User
  property_count: 4
  slug: mq-api-user
- name: UserSummary
  property_count: 2
  slug: mq-api-user-summary
- name: WeeklyStartTime
  property_count: 3
  slug: mq-api-weekly-start-time
json_structures:
- name: Mq Api Action Required Structure
  property_count: 2
  slug: mq-api-action-required-structure
- name: Mq Api Authentication Strategy Structure
  property_count: 0
  slug: mq-api-authentication-strategy-structure
- name: Mq Api Availability Zone Structure
  property_count: 1
  slug: mq-api-availability-zone-structure
- name: Mq Api Broker Engine Type Structure
  property_count: 2
  slug: mq-api-broker-engine-type-structure
- name: Mq Api Broker Instance Option Structure
  property_count: 6
  slug: mq-api-broker-instance-option-structure
- name: Mq Api Broker Instance Structure
  property_count: 3
  slug: mq-api-broker-instance-structure
- name: Mq Api Broker State Structure
  property_count: 0
  slug: mq-api-broker-state-structure
- name: Mq Api Broker Storage Type Structure
  property_count: 0
  slug: mq-api-broker-storage-type-structure
- name: Mq Api Broker Summary Structure
  property_count: 8
  slug: mq-api-broker-summary-structure
- name: Mq Api Change Type Structure
  property_count: 0
  slug: mq-api-change-type-structure
- name: Mq Api Configuration Id Structure
  property_count: 2
  slug: mq-api-configuration-id-structure
- name: Mq Api Configuration Revision Structure
  property_count: 3
  slug: mq-api-configuration-revision-structure
- name: Mq Api Configuration Structure
  property_count: 10
  slug: mq-api-configuration-structure
- name: Mq Api Configurations Structure
  property_count: 3
  slug: mq-api-configurations-structure
- name: Mq Api Create Broker Request Structure
  property_count: 19
  slug: mq-api-create-broker-request-structure
- name: Mq Api Create Broker Response Structure
  property_count: 2
  slug: mq-api-create-broker-response-structure
- name: Mq Api Create Configuration Request Structure
  property_count: 5
  slug: mq-api-create-configuration-request-structure
- name: Mq Api Create Configuration Response Structure
  property_count: 6
  slug: mq-api-create-configuration-response-structure
- name: Mq Api Create Tags Request Structure
  property_count: 1
  slug: mq-api-create-tags-request-structure
- name: Mq Api Create User Request Structure
  property_count: 3
  slug: mq-api-create-user-request-structure
- name: Mq Api Create User Response Structure
  property_count: 0
  slug: mq-api-create-user-response-structure
- name: Mq Api Day Of Week Structure
  property_count: 0
  slug: mq-api-day-of-week-structure
- name: Mq Api Delete Broker Request Structure
  property_count: 0
  slug: mq-api-delete-broker-request-structure
- name: Mq Api Delete Broker Response Structure
  property_count: 1
  slug: mq-api-delete-broker-response-structure
- name: Mq Api Delete Tags Request Structure
  property_count: 0
  slug: mq-api-delete-tags-request-structure
- name: Mq Api Delete User Request Structure
  property_count: 0
  slug: mq-api-delete-user-request-structure
- name: Mq Api Delete User Response Structure
  property_count: 0
  slug: mq-api-delete-user-response-structure
- name: Mq Api Deployment Mode Structure
  property_count: 0
  slug: mq-api-deployment-mode-structure
- name: Mq Api Describe Broker Engine Types Request Structure
  property_count: 0
  slug: mq-api-describe-broker-engine-types-request-structure
- name: Mq Api Describe Broker Engine Types Response Structure
  property_count: 3
  slug: mq-api-describe-broker-engine-types-response-structure
- name: Mq Api Describe Broker Instance Options Request Structure
  property_count: 0
  slug: mq-api-describe-broker-instance-options-request-structure
- name: Mq Api Describe Broker Instance Options Response Structure
  property_count: 3
  slug: mq-api-describe-broker-instance-options-response-structure
- name: Mq Api Describe Broker Request Structure
  property_count: 0
  slug: mq-api-describe-broker-request-structure
- name: Mq Api Describe Broker Response Structure
  property_count: 29
  slug: mq-api-describe-broker-response-structure
- name: Mq Api Describe Configuration Request Structure
  property_count: 0
  slug: mq-api-describe-configuration-request-structure
- name: Mq Api Describe Configuration Response Structure
  property_count: 10
  slug: mq-api-describe-configuration-response-structure
- name: Mq Api Describe Configuration Revision Request Structure
  property_count: 0
  slug: mq-api-describe-configuration-revision-request-structure
- name: Mq Api Describe Configuration Revision Response Structure
  property_count: 4
  slug: mq-api-describe-configuration-revision-response-structure
- name: Mq Api Describe User Request Structure
  property_count: 0
  slug: mq-api-describe-user-request-structure
- name: Mq Api Describe User Response Structure
  property_count: 5
  slug: mq-api-describe-user-response-structure
- name: Mq Api Encryption Options Structure
  property_count: 2
  slug: mq-api-encryption-options-structure
- name: Mq Api Engine Type Structure
  property_count: 0
  slug: mq-api-engine-type-structure
- name: Mq Api Engine Version Structure
  property_count: 1
  slug: mq-api-engine-version-structure
- name: Mq Api Ldap Server Metadata Input Structure
  property_count: 11
  slug: mq-api-ldap-server-metadata-input-structure
- name: Mq Api Ldap Server Metadata Output Structure
  property_count: 10
  slug: mq-api-ldap-server-metadata-output-structure
- name: Mq Api List Brokers Request Structure
  property_count: 0
  slug: mq-api-list-brokers-request-structure
- name: Mq Api List Brokers Response Structure
  property_count: 2
  slug: mq-api-list-brokers-response-structure
- name: Mq Api List Configuration Revisions Request Structure
  property_count: 0
  slug: mq-api-list-configuration-revisions-request-structure
- name: Mq Api List Configuration Revisions Response Structure
  property_count: 4
  slug: mq-api-list-configuration-revisions-response-structure
- name: Mq Api List Configurations Request Structure
  property_count: 0
  slug: mq-api-list-configurations-request-structure
- name: Mq Api List Configurations Response Structure
  property_count: 3
  slug: mq-api-list-configurations-response-structure
- name: Mq Api List Tags Request Structure
  property_count: 0
  slug: mq-api-list-tags-request-structure
- name: Mq Api List Tags Response Structure
  property_count: 1
  slug: mq-api-list-tags-response-structure
- name: Mq Api List Users Request Structure
  property_count: 0
  slug: mq-api-list-users-request-structure
- name: Mq Api List Users Response Structure
  property_count: 4
  slug: mq-api-list-users-response-structure
- name: Mq Api Logs Structure
  property_count: 2
  slug: mq-api-logs-structure
- name: Mq Api Logs Summary Structure
  property_count: 5
  slug: mq-api-logs-summary-structure
- name: Mq Api Max Results Structure
  property_count: 0
  slug: mq-api-max-results-structure
- name: Mq Api Pending Logs Structure
  property_count: 2
  slug: mq-api-pending-logs-structure
- name: Mq Api Reboot Broker Request Structure
  property_count: 0
  slug: mq-api-reboot-broker-request-structure
- name: Mq Api Reboot Broker Response Structure
  property_count: 0
  slug: mq-api-reboot-broker-response-structure
- name: Mq Api Sanitization Warning Reason Structure
  property_count: 0
  slug: mq-api-sanitization-warning-reason-structure
- name: Mq Api Sanitization Warning Structure
  property_count: 3
  slug: mq-api-sanitization-warning-structure
- name: Mq Api Unauthorized Exception Structure
  property_count: 0
  slug: mq-api-unauthorized-exception-structure
- name: Mq Api Update Broker Request Structure
  property_count: 9
  slug: mq-api-update-broker-request-structure
- name: Mq Api Update Broker Response Structure
  property_count: 10
  slug: mq-api-update-broker-response-structure
- name: Mq Api Update Configuration Request Structure
  property_count: 2
  slug: mq-api-update-configuration-request-structure
- name: Mq Api Update Configuration Response Structure
  property_count: 6
  slug: mq-api-update-configuration-response-structure
- name: Mq Api Update User Request Structure
  property_count: 3
  slug: mq-api-update-user-request-structure
- name: Mq Api Update User Response Structure
  property_count: 0
  slug: mq-api-update-user-response-structure
- name: Mq Api User Pending Changes Structure
  property_count: 3
  slug: mq-api-user-pending-changes-structure
- name: Mq Api User Structure
  property_count: 4
  slug: mq-api-user-structure
- name: Mq Api User Summary Structure
  property_count: 2
  slug: mq-api-user-summary-structure
- name: Mq Api Weekly Start Time Structure
  property_count: 3
  slug: mq-api-weekly-start-time-structure
jsonld:
- class_count: 76
  name: Amazon Mq Mq Api Context
  property_count: 84
  slug: amazon-mq-mq-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MQ
nav: Providers
network: true
overview: 'Amazon MQ publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Broker Engine Types API, Broker Instance Options API, Brokers API, and 2 more. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MQ catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MQ''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Mq Plans Pricing
  plan_count: 3
  slug: amazon-mq-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Amazon Mq Rate Limits
  slug: amazon-mq-rate-limits
rules:
- name: Amazon MQ API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-mq-jsonschema-spectral-rules
- name: Amazon MQ API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 13
  slug: amazon-mq-spectral-rules
score:
  band: strong
  composite: 62.2
  delta: -3.3
  facets:
    commercial_clarity: 68.4
    contract_quality: 71.4
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-mq/refs/heads/main/screenshots/amazon-mq-2026-06-20T171747.png
security:
- kind: authentication
  name: Amazon Mq Authentication
  slug: amazon-mq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Mq Domain Security
  slug: amazon-mq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Mq Vulnerability Disclosure
  slug: amazon-mq-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Mq Trust Center
  slug: amazon-mq-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-mq
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Migrate on-premises ActiveMQ or RabbitMQ workloads to AWS without code changes.
  name: Application Migration
- description: Use message queues to decouple microservices for improved reliability and scalability.
  name: Microservices Decoupling
- description: Connect enterprise applications using standard messaging protocols.
  name: Enterprise Integration
- description: Build event-driven applications with reliable message delivery.
  name: Event-Driven Architecture
website: https://aws.amazon.com/mq/
---
