---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Amazon Managed Prometheus Agentic Access
  operation_count: 21
  slug: amazon-managed-prometheus-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 1
apis:
- baseURL: https://aps.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon Managed Service for Prometheus — 2 operation(s) for tags.
  name: Amazon Managed Service for Prometheus Tags API
  slug: amazon-managed-prometheus-tags-api
- baseURL: https://aps.amazonaws.com
  baseurl_source: declared
  description: The Workspaces API from Amazon Managed Service for Prometheus — 7 operation(s) for workspaces.
  name: Amazon Managed Service for Prometheus Workspaces API
  slug: amazon-managed-prometheus-workspaces-api
artifact_total: 266
collections:
- collection_type: postman
  name: Amazon Prometheus Service Tags API
  slug: postman-amazon-managed-prometheus-tags-api
- collection_type: postman
  name: Amazon Prometheus Service Tags Workspaces API
  slug: postman-amazon-managed-prometheus-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Prometheus Service Tags API
  slug: open-amazon-managed-prometheus-tags-api
- collection_type: open
  name: Amazon Prometheus Service Tags Workspaces API
  slug: open-amazon-managed-prometheus-workspaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-managed-service-for-prometheus/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-managed-prometheus-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-managed-prometheus-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-managed-prometheus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-managed-prometheus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-managed-prometheus-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/prometheus/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/prometheus/
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
  url: https://aws.amazon.com/blogs/mt/tag/amazon-managed-service-for-prometheus/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/prometheus/
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
  url: rules/amazon-managed-prometheus-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-managed-prometheus-vocabulary.yaml
created: '2026-03-16'
description: Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics. It automatically scales as your monitoring needs increase, works with open-source tools, and integrates with Amazon EKS and other container environments. The service provides fully managed workspaces, alert manager definitions, and rule group namespaces for Prometheus-compatible monitoring at scale.
examples:
- key_count: 0
  name: Amazon Managed Prometheus Access Denied Exception Example
  slug: amazon-managed-prometheus-access-denied-exception-example
- key_count: 0
  name: Amazon Managed Prometheus Alert Manager Definition Data Example
  slug: amazon-managed-prometheus-alert-manager-definition-data-example
- key_count: 4
  name: Amazon Managed Prometheus Alert Manager Definition Description Example
  slug: amazon-managed-prometheus-alert-manager-definition-description-example
- key_count: 0
  name: Amazon Managed Prometheus Alert Manager Definition Status Code Example
  slug: amazon-managed-prometheus-alert-manager-definition-status-code-example
- key_count: 2
  name: Amazon Managed Prometheus Alert Manager Definition Status Example
  slug: amazon-managed-prometheus-alert-manager-definition-status-example
- key_count: 0
  name: Amazon Managed Prometheus Conflict Exception Example
  slug: amazon-managed-prometheus-conflict-exception-example
- key_count: 2
  name: Amazon Managed Prometheus Create Alert Manager Definition Request Example
  slug: amazon-managed-prometheus-create-alert-manager-definition-request-example
- key_count: 1
  name: Amazon Managed Prometheus Create Alert Manager Definition Response Example
  slug: amazon-managed-prometheus-create-alert-manager-definition-response-example
- key_count: 2
  name: Amazon Managed Prometheus Create Logging Configuration Request Example
  slug: amazon-managed-prometheus-create-logging-configuration-request-example
- key_count: 1
  name: Amazon Managed Prometheus Create Logging Configuration Response Example
  slug: amazon-managed-prometheus-create-logging-configuration-response-example
- key_count: 4
  name: Amazon Managed Prometheus Create Rule Groups Namespace Request Example
  slug: amazon-managed-prometheus-create-rule-groups-namespace-request-example
- key_count: 4
  name: Amazon Managed Prometheus Create Rule Groups Namespace Response Example
  slug: amazon-managed-prometheus-create-rule-groups-namespace-response-example
- key_count: 3
  name: Amazon Managed Prometheus Create Workspace Request Example
  slug: amazon-managed-prometheus-create-workspace-request-example
- key_count: 4
  name: Amazon Managed Prometheus Create Workspace Response Example
  slug: amazon-managed-prometheus-create-workspace-response-example
- key_count: 0
  name: Amazon Managed Prometheus Delete Alert Manager Definition Request Example
  slug: amazon-managed-prometheus-delete-alert-manager-definition-request-example
- key_count: 0
  name: Amazon Managed Prometheus Delete Logging Configuration Request Example
  slug: amazon-managed-prometheus-delete-logging-configuration-request-example
- key_count: 0
  name: Amazon Managed Prometheus Delete Rule Groups Namespace Request Example
  slug: amazon-managed-prometheus-delete-rule-groups-namespace-request-example
- key_count: 0
  name: Amazon Managed Prometheus Delete Workspace Request Example
  slug: amazon-managed-prometheus-delete-workspace-request-example
- key_count: 0
  name: Amazon Managed Prometheus Describe Alert Manager Definition Request Example
  slug: amazon-managed-prometheus-describe-alert-manager-definition-request-example
- key_count: 1
  name: Amazon Managed Prometheus Describe Alert Manager Definition Response Example
  slug: amazon-managed-prometheus-describe-alert-manager-definition-response-example
- key_count: 0
  name: Amazon Managed Prometheus Describe Logging Configuration Request Example
  slug: amazon-managed-prometheus-describe-logging-configuration-request-example
- key_count: 1
  name: Amazon Managed Prometheus Describe Logging Configuration Response Example
  slug: amazon-managed-prometheus-describe-logging-configuration-response-example
- key_count: 0
  name: Amazon Managed Prometheus Describe Rule Groups Namespace Request Example
  slug: amazon-managed-prometheus-describe-rule-groups-namespace-request-example
- key_count: 1
  name: Amazon Managed Prometheus Describe Rule Groups Namespace Response Example
  slug: amazon-managed-prometheus-describe-rule-groups-namespace-response-example
- key_count: 0
  name: Amazon Managed Prometheus Describe Workspace Request Example
  slug: amazon-managed-prometheus-describe-workspace-request-example
- key_count: 1
  name: Amazon Managed Prometheus Describe Workspace Response Example
  slug: amazon-managed-prometheus-describe-workspace-response-example
- key_count: 0
  name: Amazon Managed Prometheus Idempotency Token Example
  slug: amazon-managed-prometheus-idempotency-token-example
- key_count: 0
  name: Amazon Managed Prometheus Internal Server Exception Example
  slug: amazon-managed-prometheus-internal-server-exception-example
- key_count: 0
  name: Amazon Managed Prometheus List Rule Groups Namespaces Request Example
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-request-example
- key_count: 0
  name: Amazon Managed Prometheus List Rule Groups Namespaces Request Max Results Integer Example
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-request-max-results-integer-example
- key_count: 2
  name: Amazon Managed Prometheus List Rule Groups Namespaces Response Example
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-response-example
- key_count: 0
  name: Amazon Managed Prometheus List Tags For Resource Request Example
  slug: amazon-managed-prometheus-list-tags-for-resource-request-example
- key_count: 1
  name: Amazon Managed Prometheus List Tags For Resource Response Example
  slug: amazon-managed-prometheus-list-tags-for-resource-response-example
- key_count: 0
  name: Amazon Managed Prometheus List Workspaces Request Example
  slug: amazon-managed-prometheus-list-workspaces-request-example
- key_count: 0
  name: Amazon Managed Prometheus List Workspaces Request Max Results Integer Example
  slug: amazon-managed-prometheus-list-workspaces-request-max-results-integer-example
- key_count: 2
  name: Amazon Managed Prometheus List Workspaces Response Example
  slug: amazon-managed-prometheus-list-workspaces-response-example
- key_count: 0
  name: Amazon Managed Prometheus Log Group Arn Example
  slug: amazon-managed-prometheus-log-group-arn-example
- key_count: 5
  name: Amazon Managed Prometheus Logging Configuration Metadata Example
  slug: amazon-managed-prometheus-logging-configuration-metadata-example
- key_count: 0
  name: Amazon Managed Prometheus Logging Configuration Status Code Example
  slug: amazon-managed-prometheus-logging-configuration-status-code-example
- key_count: 2
  name: Amazon Managed Prometheus Logging Configuration Status Example
  slug: amazon-managed-prometheus-logging-configuration-status-example
- key_count: 0
  name: Amazon Managed Prometheus Pagination Token Example
  slug: amazon-managed-prometheus-pagination-token-example
- key_count: 2
  name: Amazon Managed Prometheus Put Alert Manager Definition Request Example
  slug: amazon-managed-prometheus-put-alert-manager-definition-request-example
- key_count: 1
  name: Amazon Managed Prometheus Put Alert Manager Definition Response Example
  slug: amazon-managed-prometheus-put-alert-manager-definition-response-example
- key_count: 2
  name: Amazon Managed Prometheus Put Rule Groups Namespace Request Example
  slug: amazon-managed-prometheus-put-rule-groups-namespace-request-example
- key_count: 4
  name: Amazon Managed Prometheus Put Rule Groups Namespace Response Example
  slug: amazon-managed-prometheus-put-rule-groups-namespace-response-example
- key_count: 0
  name: Amazon Managed Prometheus Resource Not Found Exception Example
  slug: amazon-managed-prometheus-resource-not-found-exception-example
- key_count: 0
  name: Amazon Managed Prometheus Rule Groups Namespace Arn Example
  slug: amazon-managed-prometheus-rule-groups-namespace-arn-example
- key_count: 0
  name: Amazon Managed Prometheus Rule Groups Namespace Data Example
  slug: amazon-managed-prometheus-rule-groups-namespace-data-example
- key_count: 7
  name: Amazon Managed Prometheus Rule Groups Namespace Description Example
  slug: amazon-managed-prometheus-rule-groups-namespace-description-example
- key_count: 0
  name: Amazon Managed Prometheus Rule Groups Namespace Name Example
  slug: amazon-managed-prometheus-rule-groups-namespace-name-example
- key_count: 0
  name: Amazon Managed Prometheus Rule Groups Namespace Status Code Example
  slug: amazon-managed-prometheus-rule-groups-namespace-status-code-example
- key_count: 2
  name: Amazon Managed Prometheus Rule Groups Namespace Status Example
  slug: amazon-managed-prometheus-rule-groups-namespace-status-example
- key_count: 6
  name: Amazon Managed Prometheus Rule Groups Namespace Summary Example
  slug: amazon-managed-prometheus-rule-groups-namespace-summary-example
- key_count: 0
  name: Amazon Managed Prometheus Rule Groups Namespace Summary List Example
  slug: amazon-managed-prometheus-rule-groups-namespace-summary-list-example
- key_count: 0
  name: Amazon Managed Prometheus Service Quota Exceeded Exception Example
  slug: amazon-managed-prometheus-service-quota-exceeded-exception-example
- key_count: 0
  name: Amazon Managed Prometheus String Example
  slug: amazon-managed-prometheus-string-example
- key_count: 0
  name: Amazon Managed Prometheus Tag Key Example
  slug: amazon-managed-prometheus-tag-key-example
- key_count: 0
  name: Amazon Managed Prometheus Tag Keys Example
  slug: amazon-managed-prometheus-tag-keys-example
- key_count: 0
  name: Amazon Managed Prometheus Tag Map Example
  slug: amazon-managed-prometheus-tag-map-example
- key_count: 1
  name: Amazon Managed Prometheus Tag Resource Request Example
  slug: amazon-managed-prometheus-tag-resource-request-example
- key_count: 0
  name: Amazon Managed Prometheus Tag Resource Response Example
  slug: amazon-managed-prometheus-tag-resource-response-example
- key_count: 0
  name: Amazon Managed Prometheus Tag Value Example
  slug: amazon-managed-prometheus-tag-value-example
- key_count: 0
  name: Amazon Managed Prometheus Throttling Exception Example
  slug: amazon-managed-prometheus-throttling-exception-example
- key_count: 0
  name: Amazon Managed Prometheus Timestamp Example
  slug: amazon-managed-prometheus-timestamp-example
- key_count: 0
  name: Amazon Managed Prometheus Untag Resource Request Example
  slug: amazon-managed-prometheus-untag-resource-request-example
- key_count: 0
  name: Amazon Managed Prometheus Untag Resource Response Example
  slug: amazon-managed-prometheus-untag-resource-response-example
- key_count: 2
  name: Amazon Managed Prometheus Update Logging Configuration Request Example
  slug: amazon-managed-prometheus-update-logging-configuration-request-example
- key_count: 1
  name: Amazon Managed Prometheus Update Logging Configuration Response Example
  slug: amazon-managed-prometheus-update-logging-configuration-response-example
- key_count: 2
  name: Amazon Managed Prometheus Update Workspace Alias Request Example
  slug: amazon-managed-prometheus-update-workspace-alias-request-example
- key_count: 0
  name: Amazon Managed Prometheus Uri Example
  slug: amazon-managed-prometheus-uri-example
- key_count: 0
  name: Amazon Managed Prometheus Validation Exception Example
  slug: amazon-managed-prometheus-validation-exception-example
- key_count: 0
  name: Amazon Managed Prometheus Workspace Alias Example
  slug: amazon-managed-prometheus-workspace-alias-example
- key_count: 0
  name: Amazon Managed Prometheus Workspace Arn Example
  slug: amazon-managed-prometheus-workspace-arn-example
- key_count: 7
  name: Amazon Managed Prometheus Workspace Description Example
  slug: amazon-managed-prometheus-workspace-description-example
- key_count: 0
  name: Amazon Managed Prometheus Workspace Id Example
  slug: amazon-managed-prometheus-workspace-id-example
- key_count: 0
  name: Amazon Managed Prometheus Workspace Status Code Example
  slug: amazon-managed-prometheus-workspace-status-code-example
- key_count: 1
  name: Amazon Managed Prometheus Workspace Status Example
  slug: amazon-managed-prometheus-workspace-status-example
- key_count: 6
  name: Amazon Managed Prometheus Workspace Summary Example
  slug: amazon-managed-prometheus-workspace-summary-example
- key_count: 0
  name: Amazon Managed Prometheus Workspace Summary List Example
  slug: amazon-managed-prometheus-workspace-summary-list-example
features:
- description: Run Prometheus-compatible monitoring without managing servers, scaling, or high availability.
  name: Serverless Prometheus
- description: Configure Prometheus AlertManager rules for routing, grouping, and suppressing alerts.
  name: Alert Manager Definitions
- description: Define and manage Prometheus recording and alerting rules organized in namespaces.
  name: Rule Groups Namespaces
- description: Create managed scrapers to automatically collect metrics from Amazon EKS clusters.
  name: Managed Scrapers
- description: Configure logging for Prometheus workspaces to capture operational events.
  name: Logging Configuration
- description: Use standard Prometheus remote write and query APIs with existing tooling and clients.
  name: Prometheus-Compatible APIs
finops:
- name: Amazon Managed Prometheus Finops
  service_category: API
  slug: amazon-managed-prometheus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-managed-prometheus.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: amazon-managed-prometheus-access-denied-exception
- name: AlertManagerDefinitionData
  property_count: 0
  slug: amazon-managed-prometheus-alert-manager-definition-data
- name: AlertManagerDefinitionDescription
  property_count: 4
  slug: amazon-managed-prometheus-alert-manager-definition-description
- name: AlertManagerDefinitionStatusCode
  property_count: 0
  slug: amazon-managed-prometheus-alert-manager-definition-status-code
- name: AlertManagerDefinitionStatus
  property_count: 2
  slug: amazon-managed-prometheus-alert-manager-definition-status
- name: ConflictException
  property_count: 0
  slug: amazon-managed-prometheus-conflict-exception
- name: CreateAlertManagerDefinitionRequest
  property_count: 2
  slug: amazon-managed-prometheus-create-alert-manager-definition-request
- name: CreateAlertManagerDefinitionResponse
  property_count: 1
  slug: amazon-managed-prometheus-create-alert-manager-definition-response
- name: CreateLoggingConfigurationRequest
  property_count: 2
  slug: amazon-managed-prometheus-create-logging-configuration-request
- name: CreateLoggingConfigurationResponse
  property_count: 1
  slug: amazon-managed-prometheus-create-logging-configuration-response
- name: CreateRuleGroupsNamespaceRequest
  property_count: 4
  slug: amazon-managed-prometheus-create-rule-groups-namespace-request
- name: CreateRuleGroupsNamespaceResponse
  property_count: 4
  slug: amazon-managed-prometheus-create-rule-groups-namespace-response
- name: CreateWorkspaceRequest
  property_count: 3
  slug: amazon-managed-prometheus-create-workspace-request
- name: CreateWorkspaceResponse
  property_count: 4
  slug: amazon-managed-prometheus-create-workspace-response
- name: DeleteAlertManagerDefinitionRequest
  property_count: 0
  slug: amazon-managed-prometheus-delete-alert-manager-definition-request
- name: DeleteLoggingConfigurationRequest
  property_count: 0
  slug: amazon-managed-prometheus-delete-logging-configuration-request
- name: DeleteRuleGroupsNamespaceRequest
  property_count: 0
  slug: amazon-managed-prometheus-delete-rule-groups-namespace-request
- name: DeleteWorkspaceRequest
  property_count: 0
  slug: amazon-managed-prometheus-delete-workspace-request
- name: DescribeAlertManagerDefinitionRequest
  property_count: 0
  slug: amazon-managed-prometheus-describe-alert-manager-definition-request
- name: DescribeAlertManagerDefinitionResponse
  property_count: 1
  slug: amazon-managed-prometheus-describe-alert-manager-definition-response
- name: DescribeLoggingConfigurationRequest
  property_count: 0
  slug: amazon-managed-prometheus-describe-logging-configuration-request
- name: DescribeLoggingConfigurationResponse
  property_count: 1
  slug: amazon-managed-prometheus-describe-logging-configuration-response
- name: DescribeRuleGroupsNamespaceRequest
  property_count: 0
  slug: amazon-managed-prometheus-describe-rule-groups-namespace-request
- name: DescribeRuleGroupsNamespaceResponse
  property_count: 1
  slug: amazon-managed-prometheus-describe-rule-groups-namespace-response
- name: DescribeWorkspaceRequest
  property_count: 0
  slug: amazon-managed-prometheus-describe-workspace-request
- name: DescribeWorkspaceResponse
  property_count: 1
  slug: amazon-managed-prometheus-describe-workspace-response
- name: IdempotencyToken
  property_count: 0
  slug: amazon-managed-prometheus-idempotency-token
- name: InternalServerException
  property_count: 0
  slug: amazon-managed-prometheus-internal-server-exception
- name: ListRuleGroupsNamespacesRequestMaxResultsInteger
  property_count: 0
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-request-max-results-integer
- name: ListRuleGroupsNamespacesRequest
  property_count: 0
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-request
- name: ListRuleGroupsNamespacesResponse
  property_count: 2
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-managed-prometheus-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-managed-prometheus-list-tags-for-resource-response
- name: ListWorkspacesRequestMaxResultsInteger
  property_count: 0
  slug: amazon-managed-prometheus-list-workspaces-request-max-results-integer
- name: ListWorkspacesRequest
  property_count: 0
  slug: amazon-managed-prometheus-list-workspaces-request
- name: ListWorkspacesResponse
  property_count: 2
  slug: amazon-managed-prometheus-list-workspaces-response
- name: LogGroupArn
  property_count: 0
  slug: amazon-managed-prometheus-log-group-arn
- name: LoggingConfigurationMetadata
  property_count: 5
  slug: amazon-managed-prometheus-logging-configuration-metadata
- name: LoggingConfigurationStatusCode
  property_count: 0
  slug: amazon-managed-prometheus-logging-configuration-status-code
- name: LoggingConfigurationStatus
  property_count: 2
  slug: amazon-managed-prometheus-logging-configuration-status
- name: PaginationToken
  property_count: 0
  slug: amazon-managed-prometheus-pagination-token
- name: PutAlertManagerDefinitionRequest
  property_count: 2
  slug: amazon-managed-prometheus-put-alert-manager-definition-request
- name: PutAlertManagerDefinitionResponse
  property_count: 1
  slug: amazon-managed-prometheus-put-alert-manager-definition-response
- name: PutRuleGroupsNamespaceRequest
  property_count: 2
  slug: amazon-managed-prometheus-put-rule-groups-namespace-request
- name: PutRuleGroupsNamespaceResponse
  property_count: 4
  slug: amazon-managed-prometheus-put-rule-groups-namespace-response
- name: ResourceNotFoundException
  property_count: 0
  slug: amazon-managed-prometheus-resource-not-found-exception
- name: RuleGroupsNamespaceArn
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-arn
- name: RuleGroupsNamespaceData
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-data
- name: RuleGroupsNamespaceDescription
  property_count: 7
  slug: amazon-managed-prometheus-rule-groups-namespace-description
- name: RuleGroupsNamespaceName
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-name
- name: RuleGroupsNamespaceStatusCode
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-status-code
- name: RuleGroupsNamespaceStatus
  property_count: 2
  slug: amazon-managed-prometheus-rule-groups-namespace-status
- name: RuleGroupsNamespaceSummaryList
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-summary-list
- name: RuleGroupsNamespaceSummary
  property_count: 6
  slug: amazon-managed-prometheus-rule-groups-namespace-summary
- name: ServiceQuotaExceededException
  property_count: 0
  slug: amazon-managed-prometheus-service-quota-exceeded-exception
- name: String
  property_count: 0
  slug: amazon-managed-prometheus-string
- name: TagKey
  property_count: 0
  slug: amazon-managed-prometheus-tag-key
- name: TagKeys
  property_count: 0
  slug: amazon-managed-prometheus-tag-keys
- name: TagMap
  property_count: 0
  slug: amazon-managed-prometheus-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: amazon-managed-prometheus-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-managed-prometheus-tag-resource-response
- name: TagValue
  property_count: 0
  slug: amazon-managed-prometheus-tag-value
- name: ThrottlingException
  property_count: 0
  slug: amazon-managed-prometheus-throttling-exception
- name: Timestamp
  property_count: 0
  slug: amazon-managed-prometheus-timestamp
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-managed-prometheus-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-managed-prometheus-untag-resource-response
- name: UpdateLoggingConfigurationRequest
  property_count: 2
  slug: amazon-managed-prometheus-update-logging-configuration-request
- name: UpdateLoggingConfigurationResponse
  property_count: 1
  slug: amazon-managed-prometheus-update-logging-configuration-response
- name: UpdateWorkspaceAliasRequest
  property_count: 2
  slug: amazon-managed-prometheus-update-workspace-alias-request
- name: Uri
  property_count: 0
  slug: amazon-managed-prometheus-uri
- name: ValidationException
  property_count: 0
  slug: amazon-managed-prometheus-validation-exception
- name: WorkspaceAlias
  property_count: 0
  slug: amazon-managed-prometheus-workspace-alias
- name: WorkspaceArn
  property_count: 0
  slug: amazon-managed-prometheus-workspace-arn
- name: WorkspaceDescription
  property_count: 7
  slug: amazon-managed-prometheus-workspace-description
- name: WorkspaceId
  property_count: 0
  slug: amazon-managed-prometheus-workspace-id
- name: WorkspaceStatusCode
  property_count: 0
  slug: amazon-managed-prometheus-workspace-status-code
- name: WorkspaceStatus
  property_count: 1
  slug: amazon-managed-prometheus-workspace-status
- name: WorkspaceSummaryList
  property_count: 0
  slug: amazon-managed-prometheus-workspace-summary-list
- name: WorkspaceSummary
  property_count: 6
  slug: amazon-managed-prometheus-workspace-summary
json_structures:
- name: Amazon Managed Prometheus Access Denied Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-access-denied-exception-structure
- name: Amazon Managed Prometheus Alert Manager Definition Data Structure
  property_count: 0
  slug: amazon-managed-prometheus-alert-manager-definition-data-structure
- name: Amazon Managed Prometheus Alert Manager Definition Description Structure
  property_count: 4
  slug: amazon-managed-prometheus-alert-manager-definition-description-structure
- name: Amazon Managed Prometheus Alert Manager Definition Status Code Structure
  property_count: 0
  slug: amazon-managed-prometheus-alert-manager-definition-status-code-structure
- name: Amazon Managed Prometheus Alert Manager Definition Status Structure
  property_count: 2
  slug: amazon-managed-prometheus-alert-manager-definition-status-structure
- name: Amazon Managed Prometheus Conflict Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-conflict-exception-structure
- name: Amazon Managed Prometheus Create Alert Manager Definition Request Structure
  property_count: 2
  slug: amazon-managed-prometheus-create-alert-manager-definition-request-structure
- name: Amazon Managed Prometheus Create Alert Manager Definition Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-create-alert-manager-definition-response-structure
- name: Amazon Managed Prometheus Create Logging Configuration Request Structure
  property_count: 2
  slug: amazon-managed-prometheus-create-logging-configuration-request-structure
- name: Amazon Managed Prometheus Create Logging Configuration Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-create-logging-configuration-response-structure
- name: Amazon Managed Prometheus Create Rule Groups Namespace Request Structure
  property_count: 4
  slug: amazon-managed-prometheus-create-rule-groups-namespace-request-structure
- name: Amazon Managed Prometheus Create Rule Groups Namespace Response Structure
  property_count: 4
  slug: amazon-managed-prometheus-create-rule-groups-namespace-response-structure
- name: Amazon Managed Prometheus Create Workspace Request Structure
  property_count: 3
  slug: amazon-managed-prometheus-create-workspace-request-structure
- name: Amazon Managed Prometheus Create Workspace Response Structure
  property_count: 4
  slug: amazon-managed-prometheus-create-workspace-response-structure
- name: Amazon Managed Prometheus Delete Alert Manager Definition Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-delete-alert-manager-definition-request-structure
- name: Amazon Managed Prometheus Delete Logging Configuration Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-delete-logging-configuration-request-structure
- name: Amazon Managed Prometheus Delete Rule Groups Namespace Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-delete-rule-groups-namespace-request-structure
- name: Amazon Managed Prometheus Delete Workspace Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-delete-workspace-request-structure
- name: Amazon Managed Prometheus Describe Alert Manager Definition Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-describe-alert-manager-definition-request-structure
- name: Amazon Managed Prometheus Describe Alert Manager Definition Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-describe-alert-manager-definition-response-structure
- name: Amazon Managed Prometheus Describe Logging Configuration Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-describe-logging-configuration-request-structure
- name: Amazon Managed Prometheus Describe Logging Configuration Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-describe-logging-configuration-response-structure
- name: Amazon Managed Prometheus Describe Rule Groups Namespace Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-describe-rule-groups-namespace-request-structure
- name: Amazon Managed Prometheus Describe Rule Groups Namespace Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-describe-rule-groups-namespace-response-structure
- name: Amazon Managed Prometheus Describe Workspace Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-describe-workspace-request-structure
- name: Amazon Managed Prometheus Describe Workspace Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-describe-workspace-response-structure
- name: Amazon Managed Prometheus Idempotency Token Structure
  property_count: 0
  slug: amazon-managed-prometheus-idempotency-token-structure
- name: Amazon Managed Prometheus Internal Server Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-internal-server-exception-structure
- name: Amazon Managed Prometheus List Rule Groups Namespaces Request Max Results Integer Structure
  property_count: 0
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-request-max-results-integer-structure
- name: Amazon Managed Prometheus List Rule Groups Namespaces Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-request-structure
- name: Amazon Managed Prometheus List Rule Groups Namespaces Response Structure
  property_count: 2
  slug: amazon-managed-prometheus-list-rule-groups-namespaces-response-structure
- name: Amazon Managed Prometheus List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-list-tags-for-resource-request-structure
- name: Amazon Managed Prometheus List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-list-tags-for-resource-response-structure
- name: Amazon Managed Prometheus List Workspaces Request Max Results Integer Structure
  property_count: 0
  slug: amazon-managed-prometheus-list-workspaces-request-max-results-integer-structure
- name: Amazon Managed Prometheus List Workspaces Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-list-workspaces-request-structure
- name: Amazon Managed Prometheus List Workspaces Response Structure
  property_count: 2
  slug: amazon-managed-prometheus-list-workspaces-response-structure
- name: Amazon Managed Prometheus Log Group Arn Structure
  property_count: 0
  slug: amazon-managed-prometheus-log-group-arn-structure
- name: Amazon Managed Prometheus Logging Configuration Metadata Structure
  property_count: 5
  slug: amazon-managed-prometheus-logging-configuration-metadata-structure
- name: Amazon Managed Prometheus Logging Configuration Status Code Structure
  property_count: 0
  slug: amazon-managed-prometheus-logging-configuration-status-code-structure
- name: Amazon Managed Prometheus Logging Configuration Status Structure
  property_count: 2
  slug: amazon-managed-prometheus-logging-configuration-status-structure
- name: Amazon Managed Prometheus Pagination Token Structure
  property_count: 0
  slug: amazon-managed-prometheus-pagination-token-structure
- name: Amazon Managed Prometheus Put Alert Manager Definition Request Structure
  property_count: 2
  slug: amazon-managed-prometheus-put-alert-manager-definition-request-structure
- name: Amazon Managed Prometheus Put Alert Manager Definition Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-put-alert-manager-definition-response-structure
- name: Amazon Managed Prometheus Put Rule Groups Namespace Request Structure
  property_count: 2
  slug: amazon-managed-prometheus-put-rule-groups-namespace-request-structure
- name: Amazon Managed Prometheus Put Rule Groups Namespace Response Structure
  property_count: 4
  slug: amazon-managed-prometheus-put-rule-groups-namespace-response-structure
- name: Amazon Managed Prometheus Resource Not Found Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-resource-not-found-exception-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Arn Structure
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-arn-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Data Structure
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-data-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Description Structure
  property_count: 7
  slug: amazon-managed-prometheus-rule-groups-namespace-description-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Name Structure
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-name-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Status Code Structure
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-status-code-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Status Structure
  property_count: 2
  slug: amazon-managed-prometheus-rule-groups-namespace-status-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Summary List Structure
  property_count: 0
  slug: amazon-managed-prometheus-rule-groups-namespace-summary-list-structure
- name: Amazon Managed Prometheus Rule Groups Namespace Summary Structure
  property_count: 6
  slug: amazon-managed-prometheus-rule-groups-namespace-summary-structure
- name: Amazon Managed Prometheus Service Quota Exceeded Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-service-quota-exceeded-exception-structure
- name: Amazon Managed Prometheus String Structure
  property_count: 0
  slug: amazon-managed-prometheus-string-structure
- name: Amazon Managed Prometheus Tag Key Structure
  property_count: 0
  slug: amazon-managed-prometheus-tag-key-structure
- name: Amazon Managed Prometheus Tag Keys Structure
  property_count: 0
  slug: amazon-managed-prometheus-tag-keys-structure
- name: Amazon Managed Prometheus Tag Map Structure
  property_count: 0
  slug: amazon-managed-prometheus-tag-map-structure
- name: Amazon Managed Prometheus Tag Resource Request Structure
  property_count: 1
  slug: amazon-managed-prometheus-tag-resource-request-structure
- name: Amazon Managed Prometheus Tag Resource Response Structure
  property_count: 0
  slug: amazon-managed-prometheus-tag-resource-response-structure
- name: Amazon Managed Prometheus Tag Value Structure
  property_count: 0
  slug: amazon-managed-prometheus-tag-value-structure
- name: Amazon Managed Prometheus Throttling Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-throttling-exception-structure
- name: Amazon Managed Prometheus Timestamp Structure
  property_count: 0
  slug: amazon-managed-prometheus-timestamp-structure
- name: Amazon Managed Prometheus Untag Resource Request Structure
  property_count: 0
  slug: amazon-managed-prometheus-untag-resource-request-structure
- name: Amazon Managed Prometheus Untag Resource Response Structure
  property_count: 0
  slug: amazon-managed-prometheus-untag-resource-response-structure
- name: Amazon Managed Prometheus Update Logging Configuration Request Structure
  property_count: 2
  slug: amazon-managed-prometheus-update-logging-configuration-request-structure
- name: Amazon Managed Prometheus Update Logging Configuration Response Structure
  property_count: 1
  slug: amazon-managed-prometheus-update-logging-configuration-response-structure
- name: Amazon Managed Prometheus Update Workspace Alias Request Structure
  property_count: 2
  slug: amazon-managed-prometheus-update-workspace-alias-request-structure
- name: Amazon Managed Prometheus Uri Structure
  property_count: 0
  slug: amazon-managed-prometheus-uri-structure
- name: Amazon Managed Prometheus Validation Exception Structure
  property_count: 0
  slug: amazon-managed-prometheus-validation-exception-structure
- name: Amazon Managed Prometheus Workspace Alias Structure
  property_count: 0
  slug: amazon-managed-prometheus-workspace-alias-structure
- name: Amazon Managed Prometheus Workspace Arn Structure
  property_count: 0
  slug: amazon-managed-prometheus-workspace-arn-structure
- name: Amazon Managed Prometheus Workspace Description Structure
  property_count: 7
  slug: amazon-managed-prometheus-workspace-description-structure
- name: Amazon Managed Prometheus Workspace Id Structure
  property_count: 0
  slug: amazon-managed-prometheus-workspace-id-structure
- name: Amazon Managed Prometheus Workspace Status Code Structure
  property_count: 0
  slug: amazon-managed-prometheus-workspace-status-code-structure
- name: Amazon Managed Prometheus Workspace Status Structure
  property_count: 1
  slug: amazon-managed-prometheus-workspace-status-structure
- name: Amazon Managed Prometheus Workspace Summary List Structure
  property_count: 0
  slug: amazon-managed-prometheus-workspace-summary-list-structure
- name: Amazon Managed Prometheus Workspace Summary Structure
  property_count: 6
  slug: amazon-managed-prometheus-workspace-summary-structure
jsonld:
- class_count: 48
  name: Amazon Managed Prometheus Context
  property_count: 21
  slug: amazon-managed-prometheus-context
layout: provider
modified: '2026-05-19'
name: Amazon Managed Service for Prometheus
nav: Providers
network: true
overview: 'Amazon Managed Service for Prometheus publishes 2 APIs on the [APIs.io](https://apis.io/) network: Tags API and Workspaces API. Tagged areas include Containers, Monitoring, Observability, and Prometheus.


  The Amazon Managed Service for Prometheus catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Managed Service for Prometheus'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Managed Prometheus Plans Pricing
  plan_count: 3
  slug: amazon-managed-prometheus-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Amazon Managed Prometheus Rate Limits
  slug: amazon-managed-prometheus-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Managed Service for Prometheus API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-managed-prometheus-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Amazon Managed Service for Prometheus API Rules
  rule_count: 22
  severity_counts:
    error: 7
    hint: 0
    info: 5
    warn: 10
  slug: amazon-managed-prometheus-spectral-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 67.5
    catalog_earned_first_party: 0.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 66.7
    developer_ergonomics: 46.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-managed-prometheus/refs/heads/main/screenshots/amazon-managed-prometheus-2026-06-20T171735.png
security:
- kind: authentication
  name: Amazon Managed Prometheus Authentication
  slug: amazon-managed-prometheus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Managed Prometheus Domain Security
  slug: amazon-managed-prometheus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Managed Prometheus Vulnerability Disclosure
  slug: amazon-managed-prometheus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Managed Prometheus Trust Center
  slug: amazon-managed-prometheus-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-managed-prometheus
tags:
- Containers
- Monitoring
- Observability
- Prometheus
use_cases:
- description: Monitor EKS clusters and Kubernetes workloads with Prometheus metrics at any scale.
  name: Kubernetes Cluster Monitoring
- description: Collect and analyze container CPU, memory, and network metrics for performance optimization.
  name: Container Performance Metrics
- description: Monitor distributed microservices with Prometheus metrics and custom alert rules.
  name: Microservices Observability
- description: Track resource utilization trends over time for infrastructure capacity planning.
  name: Infrastructure Capacity Planning
- description: Define SLO-based alerting rules to monitor service level agreements in real time.
  name: SLA Monitoring
website: https://aws.amazon.com/prometheus/
---
