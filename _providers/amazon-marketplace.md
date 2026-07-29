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
    error_semantics: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Marketplace Agentic Access
  operation_count: 12
  slug: amazon-marketplace-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 12
apis:
- description: The CancelChangeSet#catalog&changeSetId API from Amazon Marketplace — 1 operation(s) for cancelchangeset#catalog&changesetid.
  name: Amazon Marketplace CancelChangeSet#catalog&changeSetId API
  slug: amazon-marketplace-cancelchangeset-catalog-changesetid-api
- description: The DeleteResourcePolicy#resourceArn API from Amazon Marketplace — 1 operation(s) for deleteresourcepolicy#resourcearn.
  name: Amazon Marketplace DeleteResourcePolicy#resourceArn API
  slug: amazon-marketplace-deleteresourcepolicy-resourcearn-api
- description: The DescribeChangeSet#catalog&changeSetId API from Amazon Marketplace — 1 operation(s) for describechangeset#catalog&changesetid.
  name: Amazon Marketplace DescribeChangeSet#catalog&changeSetId API
  slug: amazon-marketplace-describechangeset-catalog-changesetid-api
- description: The DescribeEntity#catalog&entityId API from Amazon Marketplace — 1 operation(s) for describeentity#catalog&entityid.
  name: Amazon Marketplace DescribeEntity#catalog&entityId API
  slug: amazon-marketplace-describeentity-catalog-entityid-api
- description: The GetResourcePolicy#resourceArn API from Amazon Marketplace — 1 operation(s) for getresourcepolicy#resourcearn.
  name: Amazon Marketplace GetResourcePolicy#resourceArn API
  slug: amazon-marketplace-getresourcepolicy-resourcearn-api
- description: The ListChangeSets API from Amazon Marketplace — 1 operation(s) for listchangesets.
  name: Amazon Marketplace ListChangeSets API
  slug: amazon-marketplace-listchangesets-api
- description: The ListEntities API from Amazon Marketplace — 1 operation(s) for listentities.
  name: Amazon Marketplace ListEntities API
  slug: amazon-marketplace-listentities-api
- description: The ListTagsForResource API from Amazon Marketplace — 1 operation(s) for listtagsforresource.
  name: Amazon Marketplace ListTagsForResource API
  slug: amazon-marketplace-listtagsforresource-api
- description: The PutResourcePolicy API from Amazon Marketplace — 1 operation(s) for putresourcepolicy.
  name: Amazon Marketplace PutResourcePolicy API
  slug: amazon-marketplace-putresourcepolicy-api
- description: The StartChangeSet API from Amazon Marketplace — 1 operation(s) for startchangeset.
  name: Amazon Marketplace StartChangeSet API
  slug: amazon-marketplace-startchangeset-api
- description: The TagResource API from Amazon Marketplace — 1 operation(s) for tagresource.
  name: Amazon Marketplace TagResource API
  slug: amazon-marketplace-tagresource-api
- description: The UntagResource API from Amazon Marketplace — 1 operation(s) for untagresource.
  name: Amazon Marketplace UntagResource API
  slug: amazon-marketplace-untagresource-api
artifact_total: 286
collections:
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId API
  slug: postman-amazon-marketplace-cancelchangeset-catalog-changesetid-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId DeleteResourcePolicy#resourceArn API
  slug: postman-amazon-marketplace-deleteresourcepolicy-resourcearn-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId DescribeChangeSet#catalog&changeSetId API
  slug: postman-amazon-marketplace-describechangeset-catalog-changesetid-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId DescribeEntity#catalog&entityId API
  slug: postman-amazon-marketplace-describeentity-catalog-entityid-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId GetResourcePolicy#resourceArn API
  slug: postman-amazon-marketplace-getresourcepolicy-resourcearn-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId ListChangeSets API
  slug: postman-amazon-marketplace-listchangesets-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId ListEntities API
  slug: postman-amazon-marketplace-listentities-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId ListTagsForResource API
  slug: postman-amazon-marketplace-listtagsforresource-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId PutResourcePolicy API
  slug: postman-amazon-marketplace-putresourcepolicy-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId StartChangeSet API
  slug: postman-amazon-marketplace-startchangeset-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId TagResource API
  slug: postman-amazon-marketplace-tagresource-api
- collection_type: postman
  name: AWS Marketplace Catalog Service CancelChangeSet#catalog&changeSetId UntagResource API
  slug: postman-amazon-marketplace-untagresource-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-marketplace/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-marketplace-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-marketplace-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-marketplace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-marketplace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-marketplace-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/marketplace/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/marketplace/
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
  url: https://aws.amazon.com/blogs/awsmarketplace/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/marketplace/
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
  url: rules/amazon-marketplace-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-marketplace-vocabulary.yaml
created: '2026-03-16'
description: AWS Marketplace is a curated digital catalog that makes it easy to find, buy, deploy, and manage third-party software, data, and services that run on AWS. It offers thousands of software listings from independent software vendors. The Marketplace Catalog API enables programmatic management of marketplace entities including products, offers, and data products through change sets and entity description operations.
examples:
- key_count: 0
  name: Amazon Marketplace Access Denied Exception Example
  slug: amazon-marketplace-access-denied-exception-example
- key_count: 0
  name: Amazon Marketplace Arn Example
  slug: amazon-marketplace-arn-example
- key_count: 0
  name: Amazon Marketplace Cancel Change Set Request Example
  slug: amazon-marketplace-cancel-change-set-request-example
- key_count: 2
  name: Amazon Marketplace Cancel Change Set Response Example
  slug: amazon-marketplace-cancel-change-set-response-example
- key_count: 0
  name: Amazon Marketplace Catalog Example
  slug: amazon-marketplace-catalog-example
- key_count: 5
  name: Amazon Marketplace Change Example
  slug: amazon-marketplace-change-example
- key_count: 0
  name: Amazon Marketplace Change Name Example
  slug: amazon-marketplace-change-name-example
- key_count: 0
  name: Amazon Marketplace Change Set Description Example
  slug: amazon-marketplace-change-set-description-example
- key_count: 0
  name: Amazon Marketplace Change Set Name Example
  slug: amazon-marketplace-change-set-name-example
- key_count: 0
  name: Amazon Marketplace Change Set Summary List Example
  slug: amazon-marketplace-change-set-summary-list-example
- key_count: 8
  name: Amazon Marketplace Change Set Summary List Item Example
  slug: amazon-marketplace-change-set-summary-list-item-example
- key_count: 0
  name: Amazon Marketplace Change Status Example
  slug: amazon-marketplace-change-status-example
- key_count: 5
  name: Amazon Marketplace Change Summary Example
  slug: amazon-marketplace-change-summary-example
- key_count: 0
  name: Amazon Marketplace Change Type Example
  slug: amazon-marketplace-change-type-example
- key_count: 0
  name: Amazon Marketplace Client Request Token Example
  slug: amazon-marketplace-client-request-token-example
- key_count: 0
  name: Amazon Marketplace Date Time Iso8601 Example
  slug: amazon-marketplace-date-time-iso8601-example
- key_count: 0
  name: Amazon Marketplace Delete Resource Policy Request Example
  slug: amazon-marketplace-delete-resource-policy-request-example
- key_count: 0
  name: Amazon Marketplace Delete Resource Policy Response Example
  slug: amazon-marketplace-delete-resource-policy-response-example
- key_count: 0
  name: Amazon Marketplace Describe Change Set Request Example
  slug: amazon-marketplace-describe-change-set-request-example
- key_count: 9
  name: Amazon Marketplace Describe Change Set Response Example
  slug: amazon-marketplace-describe-change-set-response-example
- key_count: 0
  name: Amazon Marketplace Describe Entity Request Example
  slug: amazon-marketplace-describe-entity-request-example
- key_count: 5
  name: Amazon Marketplace Describe Entity Response Example
  slug: amazon-marketplace-describe-entity-response-example
- key_count: 2
  name: Amazon Marketplace Entity Example
  slug: amazon-marketplace-entity-example
- key_count: 0
  name: Amazon Marketplace Entity Name String Example
  slug: amazon-marketplace-entity-name-string-example
- key_count: 6
  name: Amazon Marketplace Entity Summary Example
  slug: amazon-marketplace-entity-summary-example
- key_count: 0
  name: Amazon Marketplace Entity Summary List Example
  slug: amazon-marketplace-entity-summary-list-example
- key_count: 0
  name: Amazon Marketplace Entity Type Example
  slug: amazon-marketplace-entity-type-example
- key_count: 0
  name: Amazon Marketplace Error Code String Example
  slug: amazon-marketplace-error-code-string-example
- key_count: 2
  name: Amazon Marketplace Error Detail Example
  slug: amazon-marketplace-error-detail-example
- key_count: 0
  name: Amazon Marketplace Error Detail List Example
  slug: amazon-marketplace-error-detail-list-example
- key_count: 0
  name: Amazon Marketplace Exception Message Content Example
  slug: amazon-marketplace-exception-message-content-example
- key_count: 0
  name: Amazon Marketplace Failure Code Example
  slug: amazon-marketplace-failure-code-example
- key_count: 2
  name: Amazon Marketplace Filter Example
  slug: amazon-marketplace-filter-example
- key_count: 0
  name: Amazon Marketplace Filter List Example
  slug: amazon-marketplace-filter-list-example
- key_count: 0
  name: Amazon Marketplace Filter Name Example
  slug: amazon-marketplace-filter-name-example
- key_count: 0
  name: Amazon Marketplace Filter Value Content Example
  slug: amazon-marketplace-filter-value-content-example
- key_count: 0
  name: Amazon Marketplace Get Resource Policy Request Example
  slug: amazon-marketplace-get-resource-policy-request-example
- key_count: 1
  name: Amazon Marketplace Get Resource Policy Response Example
  slug: amazon-marketplace-get-resource-policy-response-example
- key_count: 0
  name: Amazon Marketplace Identifier Example
  slug: amazon-marketplace-identifier-example
- key_count: 0
  name: Amazon Marketplace Internal Service Exception Example
  slug: amazon-marketplace-internal-service-exception-example
- key_count: 0
  name: Amazon Marketplace Json Example
  slug: amazon-marketplace-json-example
- key_count: 0
  name: Amazon Marketplace List Change Sets Max Result Integer Example
  slug: amazon-marketplace-list-change-sets-max-result-integer-example
- key_count: 5
  name: Amazon Marketplace List Change Sets Request Example
  slug: amazon-marketplace-list-change-sets-request-example
- key_count: 2
  name: Amazon Marketplace List Change Sets Response Example
  slug: amazon-marketplace-list-change-sets-response-example
- key_count: 0
  name: Amazon Marketplace List Entities Max Result Integer Example
  slug: amazon-marketplace-list-entities-max-result-integer-example
- key_count: 7
  name: Amazon Marketplace List Entities Request Example
  slug: amazon-marketplace-list-entities-request-example
- key_count: 2
  name: Amazon Marketplace List Entities Response Example
  slug: amazon-marketplace-list-entities-response-example
- key_count: 1
  name: Amazon Marketplace List Tags For Resource Request Example
  slug: amazon-marketplace-list-tags-for-resource-request-example
- key_count: 2
  name: Amazon Marketplace List Tags For Resource Response Example
  slug: amazon-marketplace-list-tags-for-resource-response-example
- key_count: 0
  name: Amazon Marketplace Next Token Example
  slug: amazon-marketplace-next-token-example
- key_count: 0
  name: Amazon Marketplace Ownership Type Example
  slug: amazon-marketplace-ownership-type-example
- key_count: 2
  name: Amazon Marketplace Put Resource Policy Request Example
  slug: amazon-marketplace-put-resource-policy-request-example
- key_count: 0
  name: Amazon Marketplace Put Resource Policy Response Example
  slug: amazon-marketplace-put-resource-policy-response-example
- key_count: 0
  name: Amazon Marketplace Requested Change List Example
  slug: amazon-marketplace-requested-change-list-example
- key_count: 0
  name: Amazon Marketplace Resource Arn Example
  slug: amazon-marketplace-resource-arn-example
- key_count: 0
  name: Amazon Marketplace Resource Id Example
  slug: amazon-marketplace-resource-id-example
- key_count: 0
  name: Amazon Marketplace Resource Id List Example
  slug: amazon-marketplace-resource-id-list-example
- key_count: 0
  name: Amazon Marketplace Resource In Use Exception Example
  slug: amazon-marketplace-resource-in-use-exception-example
- key_count: 0
  name: Amazon Marketplace Resource Not Found Exception Example
  slug: amazon-marketplace-resource-not-found-exception-example
- key_count: 0
  name: Amazon Marketplace Resource Not Supported Exception Example
  slug: amazon-marketplace-resource-not-supported-exception-example
- key_count: 0
  name: Amazon Marketplace Resource Policy Json Example
  slug: amazon-marketplace-resource-policy-json-example
- key_count: 0
  name: Amazon Marketplace Service Quota Exceeded Exception Example
  slug: amazon-marketplace-service-quota-exceeded-exception-example
- key_count: 0
  name: Amazon Marketplace Sort By Example
  slug: amazon-marketplace-sort-by-example
- key_count: 2
  name: Amazon Marketplace Sort Example
  slug: amazon-marketplace-sort-example
- key_count: 0
  name: Amazon Marketplace Sort Order Example
  slug: amazon-marketplace-sort-order-example
- key_count: 5
  name: Amazon Marketplace Start Change Set Request Example
  slug: amazon-marketplace-start-change-set-request-example
- key_count: 2
  name: Amazon Marketplace Start Change Set Response Example
  slug: amazon-marketplace-start-change-set-response-example
- key_count: 2
  name: Amazon Marketplace Tag Example
  slug: amazon-marketplace-tag-example
- key_count: 0
  name: Amazon Marketplace Tag Key Example
  slug: amazon-marketplace-tag-key-example
- key_count: 0
  name: Amazon Marketplace Tag Key List Example
  slug: amazon-marketplace-tag-key-list-example
- key_count: 0
  name: Amazon Marketplace Tag List Example
  slug: amazon-marketplace-tag-list-example
- key_count: 2
  name: Amazon Marketplace Tag Resource Request Example
  slug: amazon-marketplace-tag-resource-request-example
- key_count: 0
  name: Amazon Marketplace Tag Resource Response Example
  slug: amazon-marketplace-tag-resource-response-example
- key_count: 0
  name: Amazon Marketplace Tag Value Example
  slug: amazon-marketplace-tag-value-example
- key_count: 0
  name: Amazon Marketplace Throttling Exception Example
  slug: amazon-marketplace-throttling-exception-example
- key_count: 2
  name: Amazon Marketplace Untag Resource Request Example
  slug: amazon-marketplace-untag-resource-request-example
- key_count: 0
  name: Amazon Marketplace Untag Resource Response Example
  slug: amazon-marketplace-untag-resource-response-example
- key_count: 0
  name: Amazon Marketplace Validation Exception Example
  slug: amazon-marketplace-validation-exception-example
- key_count: 0
  name: Amazon Marketplace Value List Example
  slug: amazon-marketplace-value-list-example
- key_count: 0
  name: Amazon Marketplace Visibility Value Example
  slug: amazon-marketplace-visibility-value-example
features:
- description: Programmatically list and describe marketplace entities including software products, data products, and offers.
  name: Entity Management
- description: Start, monitor, and cancel change sets for publishing new listings or updating existing ones.
  name: Change Set Lifecycle
- description: Attach, retrieve, and remove resource-based policies to control access to marketplace entities.
  name: Resource Policies
- description: Tag marketplace resources with key-value pairs for organization and cost allocation.
  name: Resource Tagging
- description: Access marketplace entities across multiple AWS regions through regional catalog endpoints.
  name: Multi-Region Support
- description: Integrate catalog API with CI/CD pipelines for automated product publishing and updates.
  name: Publishing Automation
finops:
- name: Amazon Marketplace Finops
  service_category: API
  slug: amazon-marketplace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-marketplace.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: amazon-marketplace-access-denied-exception
- name: ARN
  property_count: 0
  slug: amazon-marketplace-arn
- name: CancelChangeSetRequest
  property_count: 0
  slug: amazon-marketplace-cancel-change-set-request
- name: CancelChangeSetResponse
  property_count: 2
  slug: amazon-marketplace-cancel-change-set-response
- name: Catalog
  property_count: 0
  slug: amazon-marketplace-catalog
- name: ChangeName
  property_count: 0
  slug: amazon-marketplace-change-name
- name: Change
  property_count: 5
  slug: amazon-marketplace-change
- name: ChangeSetDescription
  property_count: 0
  slug: amazon-marketplace-change-set-description
- name: ChangeSetName
  property_count: 0
  slug: amazon-marketplace-change-set-name
- name: ChangeSetSummaryListItem
  property_count: 8
  slug: amazon-marketplace-change-set-summary-list-item
- name: ChangeSetSummaryList
  property_count: 0
  slug: amazon-marketplace-change-set-summary-list
- name: ChangeStatus
  property_count: 0
  slug: amazon-marketplace-change-status
- name: ChangeSummary
  property_count: 5
  slug: amazon-marketplace-change-summary
- name: ChangeType
  property_count: 0
  slug: amazon-marketplace-change-type
- name: ClientRequestToken
  property_count: 0
  slug: amazon-marketplace-client-request-token
- name: DateTimeISO8601
  property_count: 0
  slug: amazon-marketplace-date-time-iso8601
- name: DeleteResourcePolicyRequest
  property_count: 0
  slug: amazon-marketplace-delete-resource-policy-request
- name: DeleteResourcePolicyResponse
  property_count: 0
  slug: amazon-marketplace-delete-resource-policy-response
- name: DescribeChangeSetRequest
  property_count: 0
  slug: amazon-marketplace-describe-change-set-request
- name: DescribeChangeSetResponse
  property_count: 9
  slug: amazon-marketplace-describe-change-set-response
- name: DescribeEntityRequest
  property_count: 0
  slug: amazon-marketplace-describe-entity-request
- name: DescribeEntityResponse
  property_count: 5
  slug: amazon-marketplace-describe-entity-response
- name: EntityNameString
  property_count: 0
  slug: amazon-marketplace-entity-name-string
- name: Entity
  property_count: 2
  slug: amazon-marketplace-entity
- name: EntitySummaryList
  property_count: 0
  slug: amazon-marketplace-entity-summary-list
- name: EntitySummary
  property_count: 6
  slug: amazon-marketplace-entity-summary
- name: EntityType
  property_count: 0
  slug: amazon-marketplace-entity-type
- name: ErrorCodeString
  property_count: 0
  slug: amazon-marketplace-error-code-string
- name: ErrorDetailList
  property_count: 0
  slug: amazon-marketplace-error-detail-list
- name: ErrorDetail
  property_count: 2
  slug: amazon-marketplace-error-detail
- name: ExceptionMessageContent
  property_count: 0
  slug: amazon-marketplace-exception-message-content
- name: FailureCode
  property_count: 0
  slug: amazon-marketplace-failure-code
- name: FilterList
  property_count: 0
  slug: amazon-marketplace-filter-list
- name: FilterName
  property_count: 0
  slug: amazon-marketplace-filter-name
- name: Filter
  property_count: 2
  slug: amazon-marketplace-filter
- name: FilterValueContent
  property_count: 0
  slug: amazon-marketplace-filter-value-content
- name: GetResourcePolicyRequest
  property_count: 0
  slug: amazon-marketplace-get-resource-policy-request
- name: GetResourcePolicyResponse
  property_count: 1
  slug: amazon-marketplace-get-resource-policy-response
- name: Identifier
  property_count: 0
  slug: amazon-marketplace-identifier
- name: InternalServiceException
  property_count: 0
  slug: amazon-marketplace-internal-service-exception
- name: Json
  property_count: 0
  slug: amazon-marketplace-json
- name: ListChangeSetsMaxResultInteger
  property_count: 0
  slug: amazon-marketplace-list-change-sets-max-result-integer
- name: ListChangeSetsRequest
  property_count: 5
  slug: amazon-marketplace-list-change-sets-request
- name: ListChangeSetsResponse
  property_count: 2
  slug: amazon-marketplace-list-change-sets-response
- name: ListEntitiesMaxResultInteger
  property_count: 0
  slug: amazon-marketplace-list-entities-max-result-integer
- name: ListEntitiesRequest
  property_count: 7
  slug: amazon-marketplace-list-entities-request
- name: ListEntitiesResponse
  property_count: 2
  slug: amazon-marketplace-list-entities-response
- name: ListTagsForResourceRequest
  property_count: 1
  slug: amazon-marketplace-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 2
  slug: amazon-marketplace-list-tags-for-resource-response
- name: NextToken
  property_count: 0
  slug: amazon-marketplace-next-token
- name: OwnershipType
  property_count: 0
  slug: amazon-marketplace-ownership-type
- name: PutResourcePolicyRequest
  property_count: 2
  slug: amazon-marketplace-put-resource-policy-request
- name: PutResourcePolicyResponse
  property_count: 0
  slug: amazon-marketplace-put-resource-policy-response
- name: RequestedChangeList
  property_count: 0
  slug: amazon-marketplace-requested-change-list
- name: ResourceARN
  property_count: 0
  slug: amazon-marketplace-resource-arn
- name: ResourceIdList
  property_count: 0
  slug: amazon-marketplace-resource-id-list
- name: ResourceId
  property_count: 0
  slug: amazon-marketplace-resource-id
- name: ResourceInUseException
  property_count: 0
  slug: amazon-marketplace-resource-in-use-exception
- name: ResourceNotFoundException
  property_count: 0
  slug: amazon-marketplace-resource-not-found-exception
- name: ResourceNotSupportedException
  property_count: 0
  slug: amazon-marketplace-resource-not-supported-exception
- name: ResourcePolicyJson
  property_count: 0
  slug: amazon-marketplace-resource-policy-json
- name: ServiceQuotaExceededException
  property_count: 0
  slug: amazon-marketplace-service-quota-exceeded-exception
- name: SortBy
  property_count: 0
  slug: amazon-marketplace-sort-by
- name: SortOrder
  property_count: 0
  slug: amazon-marketplace-sort-order
- name: Sort
  property_count: 2
  slug: amazon-marketplace-sort
- name: StartChangeSetRequest
  property_count: 5
  slug: amazon-marketplace-start-change-set-request
- name: StartChangeSetResponse
  property_count: 2
  slug: amazon-marketplace-start-change-set-response
- name: TagKeyList
  property_count: 0
  slug: amazon-marketplace-tag-key-list
- name: TagKey
  property_count: 0
  slug: amazon-marketplace-tag-key
- name: TagList
  property_count: 0
  slug: amazon-marketplace-tag-list
- name: TagResourceRequest
  property_count: 2
  slug: amazon-marketplace-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-marketplace-tag-resource-response
- name: Tag
  property_count: 2
  slug: amazon-marketplace-tag
- name: TagValue
  property_count: 0
  slug: amazon-marketplace-tag-value
- name: ThrottlingException
  property_count: 0
  slug: amazon-marketplace-throttling-exception
- name: UntagResourceRequest
  property_count: 2
  slug: amazon-marketplace-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-marketplace-untag-resource-response
- name: ValidationException
  property_count: 0
  slug: amazon-marketplace-validation-exception
- name: ValueList
  property_count: 0
  slug: amazon-marketplace-value-list
- name: VisibilityValue
  property_count: 0
  slug: amazon-marketplace-visibility-value
json_structures:
- name: Amazon Marketplace Access Denied Exception Structure
  property_count: 0
  slug: amazon-marketplace-access-denied-exception-structure
- name: Amazon Marketplace Arn Structure
  property_count: 0
  slug: amazon-marketplace-arn-structure
- name: Amazon Marketplace Cancel Change Set Request Structure
  property_count: 0
  slug: amazon-marketplace-cancel-change-set-request-structure
- name: Amazon Marketplace Cancel Change Set Response Structure
  property_count: 2
  slug: amazon-marketplace-cancel-change-set-response-structure
- name: Amazon Marketplace Catalog Structure
  property_count: 0
  slug: amazon-marketplace-catalog-structure
- name: Amazon Marketplace Change Name Structure
  property_count: 0
  slug: amazon-marketplace-change-name-structure
- name: Amazon Marketplace Change Set Description Structure
  property_count: 0
  slug: amazon-marketplace-change-set-description-structure
- name: Amazon Marketplace Change Set Name Structure
  property_count: 0
  slug: amazon-marketplace-change-set-name-structure
- name: Amazon Marketplace Change Set Summary List Item Structure
  property_count: 8
  slug: amazon-marketplace-change-set-summary-list-item-structure
- name: Amazon Marketplace Change Set Summary List Structure
  property_count: 0
  slug: amazon-marketplace-change-set-summary-list-structure
- name: Amazon Marketplace Change Status Structure
  property_count: 0
  slug: amazon-marketplace-change-status-structure
- name: Amazon Marketplace Change Structure
  property_count: 5
  slug: amazon-marketplace-change-structure
- name: Amazon Marketplace Change Summary Structure
  property_count: 5
  slug: amazon-marketplace-change-summary-structure
- name: Amazon Marketplace Change Type Structure
  property_count: 0
  slug: amazon-marketplace-change-type-structure
- name: Amazon Marketplace Client Request Token Structure
  property_count: 0
  slug: amazon-marketplace-client-request-token-structure
- name: Amazon Marketplace Date Time Iso8601 Structure
  property_count: 0
  slug: amazon-marketplace-date-time-iso8601-structure
- name: Amazon Marketplace Delete Resource Policy Request Structure
  property_count: 0
  slug: amazon-marketplace-delete-resource-policy-request-structure
- name: Amazon Marketplace Delete Resource Policy Response Structure
  property_count: 0
  slug: amazon-marketplace-delete-resource-policy-response-structure
- name: Amazon Marketplace Describe Change Set Request Structure
  property_count: 0
  slug: amazon-marketplace-describe-change-set-request-structure
- name: Amazon Marketplace Describe Change Set Response Structure
  property_count: 9
  slug: amazon-marketplace-describe-change-set-response-structure
- name: Amazon Marketplace Describe Entity Request Structure
  property_count: 0
  slug: amazon-marketplace-describe-entity-request-structure
- name: Amazon Marketplace Describe Entity Response Structure
  property_count: 5
  slug: amazon-marketplace-describe-entity-response-structure
- name: Amazon Marketplace Entity Name String Structure
  property_count: 0
  slug: amazon-marketplace-entity-name-string-structure
- name: Amazon Marketplace Entity Structure
  property_count: 2
  slug: amazon-marketplace-entity-structure
- name: Amazon Marketplace Entity Summary List Structure
  property_count: 0
  slug: amazon-marketplace-entity-summary-list-structure
- name: Amazon Marketplace Entity Summary Structure
  property_count: 6
  slug: amazon-marketplace-entity-summary-structure
- name: Amazon Marketplace Entity Type Structure
  property_count: 0
  slug: amazon-marketplace-entity-type-structure
- name: Amazon Marketplace Error Code String Structure
  property_count: 0
  slug: amazon-marketplace-error-code-string-structure
- name: Amazon Marketplace Error Detail List Structure
  property_count: 0
  slug: amazon-marketplace-error-detail-list-structure
- name: Amazon Marketplace Error Detail Structure
  property_count: 2
  slug: amazon-marketplace-error-detail-structure
- name: Amazon Marketplace Exception Message Content Structure
  property_count: 0
  slug: amazon-marketplace-exception-message-content-structure
- name: Amazon Marketplace Failure Code Structure
  property_count: 0
  slug: amazon-marketplace-failure-code-structure
- name: Amazon Marketplace Filter List Structure
  property_count: 0
  slug: amazon-marketplace-filter-list-structure
- name: Amazon Marketplace Filter Name Structure
  property_count: 0
  slug: amazon-marketplace-filter-name-structure
- name: Amazon Marketplace Filter Structure
  property_count: 2
  slug: amazon-marketplace-filter-structure
- name: Amazon Marketplace Filter Value Content Structure
  property_count: 0
  slug: amazon-marketplace-filter-value-content-structure
- name: Amazon Marketplace Get Resource Policy Request Structure
  property_count: 0
  slug: amazon-marketplace-get-resource-policy-request-structure
- name: Amazon Marketplace Get Resource Policy Response Structure
  property_count: 1
  slug: amazon-marketplace-get-resource-policy-response-structure
- name: Amazon Marketplace Identifier Structure
  property_count: 0
  slug: amazon-marketplace-identifier-structure
- name: Amazon Marketplace Internal Service Exception Structure
  property_count: 0
  slug: amazon-marketplace-internal-service-exception-structure
- name: Amazon Marketplace Json Structure
  property_count: 0
  slug: amazon-marketplace-json-structure
- name: Amazon Marketplace List Change Sets Max Result Integer Structure
  property_count: 0
  slug: amazon-marketplace-list-change-sets-max-result-integer-structure
- name: Amazon Marketplace List Change Sets Request Structure
  property_count: 5
  slug: amazon-marketplace-list-change-sets-request-structure
- name: Amazon Marketplace List Change Sets Response Structure
  property_count: 2
  slug: amazon-marketplace-list-change-sets-response-structure
- name: Amazon Marketplace List Entities Max Result Integer Structure
  property_count: 0
  slug: amazon-marketplace-list-entities-max-result-integer-structure
- name: Amazon Marketplace List Entities Request Structure
  property_count: 7
  slug: amazon-marketplace-list-entities-request-structure
- name: Amazon Marketplace List Entities Response Structure
  property_count: 2
  slug: amazon-marketplace-list-entities-response-structure
- name: Amazon Marketplace List Tags For Resource Request Structure
  property_count: 1
  slug: amazon-marketplace-list-tags-for-resource-request-structure
- name: Amazon Marketplace List Tags For Resource Response Structure
  property_count: 2
  slug: amazon-marketplace-list-tags-for-resource-response-structure
- name: Amazon Marketplace Next Token Structure
  property_count: 0
  slug: amazon-marketplace-next-token-structure
- name: Amazon Marketplace Ownership Type Structure
  property_count: 0
  slug: amazon-marketplace-ownership-type-structure
- name: Amazon Marketplace Put Resource Policy Request Structure
  property_count: 2
  slug: amazon-marketplace-put-resource-policy-request-structure
- name: Amazon Marketplace Put Resource Policy Response Structure
  property_count: 0
  slug: amazon-marketplace-put-resource-policy-response-structure
- name: Amazon Marketplace Requested Change List Structure
  property_count: 0
  slug: amazon-marketplace-requested-change-list-structure
- name: Amazon Marketplace Resource Arn Structure
  property_count: 0
  slug: amazon-marketplace-resource-arn-structure
- name: Amazon Marketplace Resource Id List Structure
  property_count: 0
  slug: amazon-marketplace-resource-id-list-structure
- name: Amazon Marketplace Resource Id Structure
  property_count: 0
  slug: amazon-marketplace-resource-id-structure
- name: Amazon Marketplace Resource In Use Exception Structure
  property_count: 0
  slug: amazon-marketplace-resource-in-use-exception-structure
- name: Amazon Marketplace Resource Not Found Exception Structure
  property_count: 0
  slug: amazon-marketplace-resource-not-found-exception-structure
- name: Amazon Marketplace Resource Not Supported Exception Structure
  property_count: 0
  slug: amazon-marketplace-resource-not-supported-exception-structure
- name: Amazon Marketplace Resource Policy Json Structure
  property_count: 0
  slug: amazon-marketplace-resource-policy-json-structure
- name: Amazon Marketplace Service Quota Exceeded Exception Structure
  property_count: 0
  slug: amazon-marketplace-service-quota-exceeded-exception-structure
- name: Amazon Marketplace Sort By Structure
  property_count: 0
  slug: amazon-marketplace-sort-by-structure
- name: Amazon Marketplace Sort Order Structure
  property_count: 0
  slug: amazon-marketplace-sort-order-structure
- name: Amazon Marketplace Sort Structure
  property_count: 2
  slug: amazon-marketplace-sort-structure
- name: Amazon Marketplace Start Change Set Request Structure
  property_count: 5
  slug: amazon-marketplace-start-change-set-request-structure
- name: Amazon Marketplace Start Change Set Response Structure
  property_count: 2
  slug: amazon-marketplace-start-change-set-response-structure
- name: Amazon Marketplace Tag Key List Structure
  property_count: 0
  slug: amazon-marketplace-tag-key-list-structure
- name: Amazon Marketplace Tag Key Structure
  property_count: 0
  slug: amazon-marketplace-tag-key-structure
- name: Amazon Marketplace Tag List Structure
  property_count: 0
  slug: amazon-marketplace-tag-list-structure
- name: Amazon Marketplace Tag Resource Request Structure
  property_count: 2
  slug: amazon-marketplace-tag-resource-request-structure
- name: Amazon Marketplace Tag Resource Response Structure
  property_count: 0
  slug: amazon-marketplace-tag-resource-response-structure
- name: Amazon Marketplace Tag Structure
  property_count: 2
  slug: amazon-marketplace-tag-structure
- name: Amazon Marketplace Tag Value Structure
  property_count: 0
  slug: amazon-marketplace-tag-value-structure
- name: Amazon Marketplace Throttling Exception Structure
  property_count: 0
  slug: amazon-marketplace-throttling-exception-structure
- name: Amazon Marketplace Untag Resource Request Structure
  property_count: 2
  slug: amazon-marketplace-untag-resource-request-structure
- name: Amazon Marketplace Untag Resource Response Structure
  property_count: 0
  slug: amazon-marketplace-untag-resource-response-structure
- name: Amazon Marketplace Validation Exception Structure
  property_count: 0
  slug: amazon-marketplace-validation-exception-structure
- name: Amazon Marketplace Value List Structure
  property_count: 0
  slug: amazon-marketplace-value-list-structure
- name: Amazon Marketplace Visibility Value Structure
  property_count: 0
  slug: amazon-marketplace-visibility-value-structure
jsonld:
- class_count: 33
  name: Amazon Marketplace Context
  property_count: 44
  slug: amazon-marketplace-context
layout: provider
modified: '2026-05-19'
name: Amazon Marketplace
nav: Providers
network: true
overview: 'Amazon Marketplace publishes 12 APIs on the [APIs.io](https://apis.io/) network, including CancelChangeSet#catalog&changeSetId API, DeleteResourcePolicy#resourceArn API, DescribeChangeSet#catalog&changeSetId API, and 9 more. Tagged areas include Commerce, ISV, Marketplace, and Software Catalog.


  The Amazon Marketplace catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Marketplace''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Marketplace Plans Pricing
  plan_count: 3
  slug: amazon-marketplace-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Amazon Marketplace Rate Limits
  slug: amazon-marketplace-rate-limits
rules:
- name: Amazon Marketplace API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-marketplace-jsonschema-spectral-rules
- name: Amazon Marketplace API Rules
  rule_count: 23
  severity_counts:
    error: 7
    hint: 0
    info: 5
    warn: 11
  slug: amazon-marketplace-spectral-rules
score:
  band: strong
  composite: 65.7
  delta: -3.3
  facets:
    commercial_clarity: 81.6
    contract_quality: 74.6
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-marketplace/refs/heads/main/screenshots/amazon-marketplace-2026-06-20T171735.png
security:
- kind: authentication
  name: Amazon Marketplace Authentication
  slug: amazon-marketplace-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Marketplace Domain Security
  slug: amazon-marketplace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Marketplace Vulnerability Disclosure
  slug: amazon-marketplace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Marketplace Trust Center
  slug: amazon-marketplace-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-marketplace
tags:
- Commerce
- ISV
- Marketplace
- Software Catalog
use_cases:
- description: Automate publishing and updating software listings on AWS Marketplace from CI/CD pipelines.
  name: Product Publishing Automation
- description: Programmatically discover and evaluate available software products and data products.
  name: Marketplace Catalog Discovery
- description: Track the status of publishing operations and receive change set completion notifications.
  name: Change Set Monitoring
- description: Manage marketplace listings across multiple AWS accounts with shared resource policies.
  name: Multi-Account Marketplace Management
- description: Enable ISV teams to self-service publish and update product listings through the catalog API.
  name: ISV Self-Service Publishing
website: https://aws.amazon.com/marketplace/
---
