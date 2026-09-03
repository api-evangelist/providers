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
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Entity Resolution Agentic Access
  operation_count: 16
  slug: amazon-entity-resolution-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- baseURL: https://entityresolution.amazonaws.com
  baseurl_source: declared
  description: The Matchingworkflows API from Amazon Entity Resolution — 5 operation(s) for matchingworkflows.
  name: Amazon Entity Resolution Matchingworkflows API
  slug: amazon-entity-resolution-matchingworkflows-api
- baseURL: https://entityresolution.amazonaws.com
  baseurl_source: declared
  description: The Schemas API from Amazon Entity Resolution — 2 operation(s) for schemas.
  name: Amazon Entity Resolution Schemas API
  slug: amazon-entity-resolution-schemas-api
- baseURL: https://entityresolution.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon Entity Resolution — 2 operation(s) for tags.
  name: Amazon Entity Resolution Tags API
  slug: amazon-entity-resolution-tags-api
arazzos:
- description: List the jobs for a workflow and pull the full status and metrics of the most recent one.
  name: Amazon Entity Resolution Audit Latest Matching Job
  slug: amazon-entity-resolution-audit-latest-job-workflow
- description: Register a schema mapping and create a matching workflow that references it.
  name: Amazon Entity Resolution Provision Matching Workflow
  slug: amazon-entity-resolution-provision-workflow-workflow
- description: Confirm a processed workflow exists, then look up the Match ID for a single customer record.
  name: Amazon Entity Resolution Resolve Record Match ID
  slug: amazon-entity-resolution-resolve-record-match-id-workflow
- description: Stand up a schema mapping and matching workflow, start a job, and poll it to completion.
  name: Amazon Entity Resolution Run Matching Pipeline
  slug: amazon-entity-resolution-run-matching-pipeline-workflow
- description: Start a matching job on an existing workflow and poll until it reaches a terminal status.
  name: Amazon Entity Resolution Start And Await Matching Job
  slug: amazon-entity-resolution-start-and-await-job-workflow
- description: Update an existing matching workflow's configuration, then start a fresh job and poll it.
  name: Amazon Entity Resolution Update And Rerun Matching Workflow
  slug: amazon-entity-resolution-update-and-rerun-workflow
artifact_total: 276
collections:
- collection_type: postman
  name: AWS EntityResolution Matchingworkflows API
  slug: postman-amazon-entity-resolution-matchingworkflows-api
- collection_type: postman
  name: AWS EntityResolution Matchingworkflows Schemas API
  slug: postman-amazon-entity-resolution-schemas-api
- collection_type: postman
  name: AWS EntityResolution Matchingworkflows Tags API
  slug: postman-amazon-entity-resolution-tags-api
- collection_type: postman
  name: AWS EntityResolution
  slug: postman-amazon-entity-resolution
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS EntityResolution Matchingworkflows API
  slug: open-amazon-entity-resolution-matchingworkflows-api
- collection_type: open
  name: AWS EntityResolution Matchingworkflows Schemas API
  slug: open-amazon-entity-resolution-schemas-api
- collection_type: open
  name: AWS EntityResolution Matchingworkflows Tags API
  slug: open-amazon-entity-resolution-tags-api
- collection_type: open
  name: AWS EntityResolution
  slug: open-amazon-entity-resolution
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-entity-resolution-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-entity-resolution-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-entity-resolution-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-entity-resolution-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-entity-resolution-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-entity-resolution/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-entity-resolution-audit-latest-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-entity-resolution-provision-workflow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-entity-resolution-resolve-record-match-id-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-entity-resolution-run-matching-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-entity-resolution-start-and-await-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-entity-resolution-update-and-rerun-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/entity-resolution/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/entity-resolution/
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
  url: https://console.aws.amazon.com/entityresolution/
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
  url: https://aws.amazon.com/entity-resolution/faqs/
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
  url: https://stackoverflow.com/questions/tagged/entity-resolution
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
  url: rules/amazon-entity-resolution-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-entity-resolution-vocabulary.yaml
created: '2024-01-15'
description: Amazon Entity Resolution is a service that helps you match and link related records across multiple applications, channels, and data stores using machine learning and configurable matching techniques to identify and consolidate records that refer to the same entity.
examples:
- key_count: 0
  name: Amazon Entity Resolution Access Denied Exception Example
  slug: amazon-entity-resolution-access-denied-exception-example
- key_count: 0
  name: Amazon Entity Resolution Conflict Exception Example
  slug: amazon-entity-resolution-conflict-exception-example
- key_count: 8
  name: Amazon Entity Resolution Create Matching Workflow Input Example
  slug: amazon-entity-resolution-create-matching-workflow-input-example
- key_count: 8
  name: Amazon Entity Resolution Create Matching Workflow Output Example
  slug: amazon-entity-resolution-create-matching-workflow-output-example
- key_count: 4
  name: Amazon Entity Resolution Create Schema Mapping Input Example
  slug: amazon-entity-resolution-create-schema-mapping-input-example
- key_count: 4
  name: Amazon Entity Resolution Create Schema Mapping Output Example
  slug: amazon-entity-resolution-create-schema-mapping-output-example
- key_count: 0
  name: Amazon Entity Resolution Delete Matching Workflow Input Example
  slug: amazon-entity-resolution-delete-matching-workflow-input-example
- key_count: 1
  name: Amazon Entity Resolution Delete Matching Workflow Output Example
  slug: amazon-entity-resolution-delete-matching-workflow-output-example
- key_count: 0
  name: Amazon Entity Resolution Delete Schema Mapping Input Example
  slug: amazon-entity-resolution-delete-schema-mapping-input-example
- key_count: 1
  name: Amazon Entity Resolution Delete Schema Mapping Output Example
  slug: amazon-entity-resolution-delete-schema-mapping-output-example
- key_count: 1
  name: Amazon Entity Resolution Error Details Example
  slug: amazon-entity-resolution-error-details-example
- key_count: 0
  name: Amazon Entity Resolution Exceeds Limit Exception Example
  slug: amazon-entity-resolution-exceeds-limit-exception-example
- key_count: 1
  name: Amazon Entity Resolution Get Match Id Input Example
  slug: amazon-entity-resolution-get-match-id-input-example
- key_count: 1
  name: Amazon Entity Resolution Get Match Id Output Example
  slug: amazon-entity-resolution-get-match-id-output-example
- key_count: 0
  name: Amazon Entity Resolution Get Matching Job Input Example
  slug: amazon-entity-resolution-get-matching-job-input-example
- key_count: 6
  name: Amazon Entity Resolution Get Matching Job Output Example
  slug: amazon-entity-resolution-get-matching-job-output-example
- key_count: 0
  name: Amazon Entity Resolution Get Matching Workflow Input Example
  slug: amazon-entity-resolution-get-matching-workflow-input-example
- key_count: 10
  name: Amazon Entity Resolution Get Matching Workflow Output Example
  slug: amazon-entity-resolution-get-matching-workflow-output-example
- key_count: 0
  name: Amazon Entity Resolution Get Schema Mapping Input Example
  slug: amazon-entity-resolution-get-schema-mapping-input-example
- key_count: 7
  name: Amazon Entity Resolution Get Schema Mapping Output Example
  slug: amazon-entity-resolution-get-schema-mapping-output-example
- key_count: 1
  name: Amazon Entity Resolution Incremental Run Config Example
  slug: amazon-entity-resolution-incremental-run-config-example
- key_count: 3
  name: Amazon Entity Resolution Input Source Example
  slug: amazon-entity-resolution-input-source-example
- key_count: 0
  name: Amazon Entity Resolution Internal Server Exception Example
  slug: amazon-entity-resolution-internal-server-exception-example
- key_count: 4
  name: Amazon Entity Resolution Job Metrics Example
  slug: amazon-entity-resolution-job-metrics-example
- key_count: 4
  name: Amazon Entity Resolution Job Summary Example
  slug: amazon-entity-resolution-job-summary-example
- key_count: 0
  name: Amazon Entity Resolution List Matching Jobs Input Example
  slug: amazon-entity-resolution-list-matching-jobs-input-example
- key_count: 2
  name: Amazon Entity Resolution List Matching Jobs Output Example
  slug: amazon-entity-resolution-list-matching-jobs-output-example
- key_count: 0
  name: Amazon Entity Resolution List Matching Workflows Input Example
  slug: amazon-entity-resolution-list-matching-workflows-input-example
- key_count: 2
  name: Amazon Entity Resolution List Matching Workflows Output Example
  slug: amazon-entity-resolution-list-matching-workflows-output-example
- key_count: 0
  name: Amazon Entity Resolution List Schema Mappings Input Example
  slug: amazon-entity-resolution-list-schema-mappings-input-example
- key_count: 2
  name: Amazon Entity Resolution List Schema Mappings Output Example
  slug: amazon-entity-resolution-list-schema-mappings-output-example
- key_count: 0
  name: Amazon Entity Resolution List Tags For Resource Input Example
  slug: amazon-entity-resolution-list-tags-for-resource-input-example
- key_count: 1
  name: Amazon Entity Resolution List Tags For Resource Output Example
  slug: amazon-entity-resolution-list-tags-for-resource-output-example
- key_count: 4
  name: Amazon Entity Resolution Matching Workflow Summary Example
  slug: amazon-entity-resolution-matching-workflow-summary-example
- key_count: 2
  name: Amazon Entity Resolution Output Attribute Example
  slug: amazon-entity-resolution-output-attribute-example
- key_count: 4
  name: Amazon Entity Resolution Output Source Example
  slug: amazon-entity-resolution-output-source-example
- key_count: 0
  name: Amazon Entity Resolution Record Attribute Map Example
  slug: amazon-entity-resolution-record-attribute-map-example
- key_count: 2
  name: Amazon Entity Resolution Resolution Techniques Example
  slug: amazon-entity-resolution-resolution-techniques-example
- key_count: 0
  name: Amazon Entity Resolution Resource Not Found Exception Example
  slug: amazon-entity-resolution-resource-not-found-exception-example
- key_count: 2
  name: Amazon Entity Resolution Rule Based Properties Example
  slug: amazon-entity-resolution-rule-based-properties-example
- key_count: 2
  name: Amazon Entity Resolution Rule Example
  slug: amazon-entity-resolution-rule-example
- key_count: 4
  name: Amazon Entity Resolution Schema Input Attribute Example
  slug: amazon-entity-resolution-schema-input-attribute-example
- key_count: 4
  name: Amazon Entity Resolution Schema Mapping Summary Example
  slug: amazon-entity-resolution-schema-mapping-summary-example
- key_count: 0
  name: Amazon Entity Resolution Start Matching Job Input Example
  slug: amazon-entity-resolution-start-matching-job-input-example
- key_count: 1
  name: Amazon Entity Resolution Start Matching Job Output Example
  slug: amazon-entity-resolution-start-matching-job-output-example
- key_count: 0
  name: Amazon Entity Resolution Tag Map Example
  slug: amazon-entity-resolution-tag-map-example
- key_count: 1
  name: Amazon Entity Resolution Tag Resource Input Example
  slug: amazon-entity-resolution-tag-resource-input-example
- key_count: 0
  name: Amazon Entity Resolution Tag Resource Output Example
  slug: amazon-entity-resolution-tag-resource-output-example
- key_count: 0
  name: Amazon Entity Resolution Throttling Exception Example
  slug: amazon-entity-resolution-throttling-exception-example
- key_count: 0
  name: Amazon Entity Resolution Untag Resource Input Example
  slug: amazon-entity-resolution-untag-resource-input-example
- key_count: 0
  name: Amazon Entity Resolution Untag Resource Output Example
  slug: amazon-entity-resolution-untag-resource-output-example
- key_count: 6
  name: Amazon Entity Resolution Update Matching Workflow Input Example
  slug: amazon-entity-resolution-update-matching-workflow-input-example
- key_count: 7
  name: Amazon Entity Resolution Update Matching Workflow Output Example
  slug: amazon-entity-resolution-update-matching-workflow-output-example
- key_count: 0
  name: Amazon Entity Resolution Validation Exception Example
  slug: amazon-entity-resolution-validation-exception-example
features:
- description: Use machine learning models to match records across disparate datasets
  name: ML-Based Matching
- description: Configure deterministic matching rules for exact and fuzzy matching
  name: Rule-Based Matching
- description: Create and manage identity graphs linking records across data sources
  name: ID Mapping
- description: Map input data schemas to standardized formats for consistent matching
  name: Schema Mapping
- description: Enrich records with data from LiveRamp, Unified ID 2.0, and others
  name: Third-Party Data Providers
finops:
- name: Amazon Entity Resolution Finops
  service_category: API
  slug: amazon-entity-resolution-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: amazon-entity-resolution-access-denied-exception
- name: AttributeMatchingModel
  property_count: 0
  slug: amazon-entity-resolution-attribute-matching-model
- name: AttributeName
  property_count: 0
  slug: amazon-entity-resolution-attribute-name
- name: Boolean
  property_count: 0
  slug: amazon-entity-resolution-boolean
- name: ConflictException
  property_count: 0
  slug: amazon-entity-resolution-conflict-exception
- name: CreateMatchingWorkflowInput
  property_count: 8
  slug: amazon-entity-resolution-create-matching-workflow-input
- name: CreateMatchingWorkflowOutput
  property_count: 8
  slug: amazon-entity-resolution-create-matching-workflow-output
- name: CreateSchemaMappingInput
  property_count: 4
  slug: amazon-entity-resolution-create-schema-mapping-input
- name: CreateSchemaMappingOutput
  property_count: 4
  slug: amazon-entity-resolution-create-schema-mapping-output
- name: DeleteMatchingWorkflowInput
  property_count: 0
  slug: amazon-entity-resolution-delete-matching-workflow-input
- name: DeleteMatchingWorkflowOutput
  property_count: 1
  slug: amazon-entity-resolution-delete-matching-workflow-output
- name: DeleteSchemaMappingInput
  property_count: 0
  slug: amazon-entity-resolution-delete-schema-mapping-input
- name: DeleteSchemaMappingOutput
  property_count: 1
  slug: amazon-entity-resolution-delete-schema-mapping-output
- name: Description
  property_count: 0
  slug: amazon-entity-resolution-description
- name: EntityName
  property_count: 0
  slug: amazon-entity-resolution-entity-name
- name: ErrorDetails
  property_count: 1
  slug: amazon-entity-resolution-error-details
- name: ExceedsLimitException
  property_count: 0
  slug: amazon-entity-resolution-exceeds-limit-exception
- name: GetMatchIdInput
  property_count: 1
  slug: amazon-entity-resolution-get-match-id-input
- name: GetMatchIdOutput
  property_count: 1
  slug: amazon-entity-resolution-get-match-id-output
- name: GetMatchingJobInput
  property_count: 0
  slug: amazon-entity-resolution-get-matching-job-input
- name: GetMatchingJobOutput
  property_count: 6
  slug: amazon-entity-resolution-get-matching-job-output
- name: GetMatchingWorkflowInput
  property_count: 0
  slug: amazon-entity-resolution-get-matching-workflow-input
- name: GetMatchingWorkflowOutput
  property_count: 11
  slug: amazon-entity-resolution-get-matching-workflow-output
- name: GetSchemaMappingInput
  property_count: 0
  slug: amazon-entity-resolution-get-schema-mapping-input
- name: GetSchemaMappingOutput
  property_count: 7
  slug: amazon-entity-resolution-get-schema-mapping-output
- name: IncrementalRunConfig
  property_count: 1
  slug: amazon-entity-resolution-incremental-run-config
- name: IncrementalRunType
  property_count: 0
  slug: amazon-entity-resolution-incremental-run-type
- name: InputSourceConfig
  property_count: 0
  slug: amazon-entity-resolution-input-source-config
- name: InputSourceInputSourceARNString
  property_count: 0
  slug: amazon-entity-resolution-input-source-input-source-arn-string
- name: InputSource
  property_count: 3
  slug: amazon-entity-resolution-input-source
- name: Integer
  property_count: 0
  slug: amazon-entity-resolution-integer
- name: InternalServerException
  property_count: 0
  slug: amazon-entity-resolution-internal-server-exception
- name: JobId
  property_count: 0
  slug: amazon-entity-resolution-job-id
- name: JobList
  property_count: 0
  slug: amazon-entity-resolution-job-list
- name: JobMetrics
  property_count: 4
  slug: amazon-entity-resolution-job-metrics
- name: JobStatus
  property_count: 0
  slug: amazon-entity-resolution-job-status
- name: JobSummary
  property_count: 4
  slug: amazon-entity-resolution-job-summary
- name: KMSArn
  property_count: 0
  slug: amazon-entity-resolution-kms-arn
- name: ListMatchingJobsInputMaxResultsInteger
  property_count: 0
  slug: amazon-entity-resolution-list-matching-jobs-input-max-results-integer
- name: ListMatchingJobsInput
  property_count: 0
  slug: amazon-entity-resolution-list-matching-jobs-input
- name: ListMatchingJobsOutput
  property_count: 2
  slug: amazon-entity-resolution-list-matching-jobs-output
- name: ListMatchingWorkflowsInputMaxResultsInteger
  property_count: 0
  slug: amazon-entity-resolution-list-matching-workflows-input-max-results-integer
- name: ListMatchingWorkflowsInput
  property_count: 0
  slug: amazon-entity-resolution-list-matching-workflows-input
- name: ListMatchingWorkflowsOutput
  property_count: 2
  slug: amazon-entity-resolution-list-matching-workflows-output
- name: ListSchemaMappingsInputMaxResultsInteger
  property_count: 0
  slug: amazon-entity-resolution-list-schema-mappings-input-max-results-integer
- name: ListSchemaMappingsInput
  property_count: 0
  slug: amazon-entity-resolution-list-schema-mappings-input
- name: ListSchemaMappingsOutput
  property_count: 2
  slug: amazon-entity-resolution-list-schema-mappings-output
- name: ListTagsForResourceInput
  property_count: 0
  slug: amazon-entity-resolution-list-tags-for-resource-input
- name: ListTagsForResourceOutput
  property_count: 1
  slug: amazon-entity-resolution-list-tags-for-resource-output
- name: MatchingWorkflowArn
  property_count: 0
  slug: amazon-entity-resolution-matching-workflow-arn
- name: MatchingWorkflowList
  property_count: 0
  slug: amazon-entity-resolution-matching-workflow-list
- name: MatchingWorkflowSummary
  property_count: 4
  slug: amazon-entity-resolution-matching-workflow-summary
- name: NextToken
  property_count: 0
  slug: amazon-entity-resolution-next-token
- name: OutputAttribute
  property_count: 2
  slug: amazon-entity-resolution-output-attribute
- name: OutputSourceConfig
  property_count: 0
  slug: amazon-entity-resolution-output-source-config
- name: OutputSourceOutputList
  property_count: 0
  slug: amazon-entity-resolution-output-source-output-list
- name: OutputSourceOutputS3PathString
  property_count: 0
  slug: amazon-entity-resolution-output-source-output-s3-path-string
- name: OutputSource
  property_count: 4
  slug: amazon-entity-resolution-output-source
- name: RecordAttributeMapKeyString
  property_count: 0
  slug: amazon-entity-resolution-record-attribute-map-key-string
- name: RecordAttributeMap
  property_count: 0
  slug: amazon-entity-resolution-record-attribute-map
- name: RecordAttributeMapValueString
  property_count: 0
  slug: amazon-entity-resolution-record-attribute-map-value-string
- name: ResolutionTechniques
  property_count: 2
  slug: amazon-entity-resolution-resolution-techniques
- name: ResolutionType
  property_count: 0
  slug: amazon-entity-resolution-resolution-type
- name: ResourceNotFoundException
  property_count: 0
  slug: amazon-entity-resolution-resource-not-found-exception
- name: RuleBasedPropertiesRulesList
  property_count: 0
  slug: amazon-entity-resolution-rule-based-properties-rules-list
- name: RuleBasedProperties
  property_count: 2
  slug: amazon-entity-resolution-rule-based-properties
- name: RuleMatchingKeysList
  property_count: 0
  slug: amazon-entity-resolution-rule-matching-keys-list
- name: RuleRuleNameString
  property_count: 0
  slug: amazon-entity-resolution-rule-rule-name-string
- name: Rule
  property_count: 2
  slug: amazon-entity-resolution-rule
- name: SchemaAttributeType
  property_count: 0
  slug: amazon-entity-resolution-schema-attribute-type
- name: SchemaInputAttribute
  property_count: 4
  slug: amazon-entity-resolution-schema-input-attribute
- name: SchemaInputAttributes
  property_count: 0
  slug: amazon-entity-resolution-schema-input-attributes
- name: SchemaMappingArn
  property_count: 0
  slug: amazon-entity-resolution-schema-mapping-arn
- name: SchemaMappingList
  property_count: 0
  slug: amazon-entity-resolution-schema-mapping-list
- name: SchemaMappingSummary
  property_count: 4
  slug: amazon-entity-resolution-schema-mapping-summary
- name: StartMatchingJobInput
  property_count: 0
  slug: amazon-entity-resolution-start-matching-job-input
- name: StartMatchingJobOutput
  property_count: 1
  slug: amazon-entity-resolution-start-matching-job-output
- name: String
  property_count: 0
  slug: amazon-entity-resolution-string
- name: TagKeyList
  property_count: 0
  slug: amazon-entity-resolution-tag-key-list
- name: TagKey
  property_count: 0
  slug: amazon-entity-resolution-tag-key
- name: TagMap
  property_count: 0
  slug: amazon-entity-resolution-tag-map
- name: TagResourceInput
  property_count: 1
  slug: amazon-entity-resolution-tag-resource-input
- name: TagResourceOutput
  property_count: 0
  slug: amazon-entity-resolution-tag-resource-output
- name: TagValue
  property_count: 0
  slug: amazon-entity-resolution-tag-value
- name: ThrottlingException
  property_count: 0
  slug: amazon-entity-resolution-throttling-exception
- name: Timestamp
  property_count: 0
  slug: amazon-entity-resolution-timestamp
- name: UntagResourceInput
  property_count: 0
  slug: amazon-entity-resolution-untag-resource-input
- name: UntagResourceOutput
  property_count: 0
  slug: amazon-entity-resolution-untag-resource-output
- name: UpdateMatchingWorkflowInput
  property_count: 6
  slug: amazon-entity-resolution-update-matching-workflow-input
- name: UpdateMatchingWorkflowOutput
  property_count: 7
  slug: amazon-entity-resolution-update-matching-workflow-output
- name: ValidationException
  property_count: 0
  slug: amazon-entity-resolution-validation-exception
- name: VeniceGlobalArn
  property_count: 0
  slug: amazon-entity-resolution-venice-global-arn
json_structures:
- name: Amazon Entity Resolution Access Denied Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-access-denied-exception-structure
- name: Amazon Entity Resolution Attribute Matching Model Structure
  property_count: 0
  slug: amazon-entity-resolution-attribute-matching-model-structure
- name: Amazon Entity Resolution Attribute Name Structure
  property_count: 0
  slug: amazon-entity-resolution-attribute-name-structure
- name: Amazon Entity Resolution Boolean Structure
  property_count: 0
  slug: amazon-entity-resolution-boolean-structure
- name: Amazon Entity Resolution Conflict Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-conflict-exception-structure
- name: Amazon Entity Resolution Create Matching Workflow Input Structure
  property_count: 8
  slug: amazon-entity-resolution-create-matching-workflow-input-structure
- name: Amazon Entity Resolution Create Matching Workflow Output Structure
  property_count: 8
  slug: amazon-entity-resolution-create-matching-workflow-output-structure
- name: Amazon Entity Resolution Create Schema Mapping Input Structure
  property_count: 4
  slug: amazon-entity-resolution-create-schema-mapping-input-structure
- name: Amazon Entity Resolution Create Schema Mapping Output Structure
  property_count: 4
  slug: amazon-entity-resolution-create-schema-mapping-output-structure
- name: Amazon Entity Resolution Delete Matching Workflow Input Structure
  property_count: 0
  slug: amazon-entity-resolution-delete-matching-workflow-input-structure
- name: Amazon Entity Resolution Delete Matching Workflow Output Structure
  property_count: 1
  slug: amazon-entity-resolution-delete-matching-workflow-output-structure
- name: Amazon Entity Resolution Delete Schema Mapping Input Structure
  property_count: 0
  slug: amazon-entity-resolution-delete-schema-mapping-input-structure
- name: Amazon Entity Resolution Delete Schema Mapping Output Structure
  property_count: 1
  slug: amazon-entity-resolution-delete-schema-mapping-output-structure
- name: Amazon Entity Resolution Description Structure
  property_count: 0
  slug: amazon-entity-resolution-description-structure
- name: Amazon Entity Resolution Entity Name Structure
  property_count: 0
  slug: amazon-entity-resolution-entity-name-structure
- name: Amazon Entity Resolution Error Details Structure
  property_count: 1
  slug: amazon-entity-resolution-error-details-structure
- name: Amazon Entity Resolution Exceeds Limit Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-exceeds-limit-exception-structure
- name: Amazon Entity Resolution Get Match Id Input Structure
  property_count: 1
  slug: amazon-entity-resolution-get-match-id-input-structure
- name: Amazon Entity Resolution Get Match Id Output Structure
  property_count: 1
  slug: amazon-entity-resolution-get-match-id-output-structure
- name: Amazon Entity Resolution Get Matching Job Input Structure
  property_count: 0
  slug: amazon-entity-resolution-get-matching-job-input-structure
- name: Amazon Entity Resolution Get Matching Job Output Structure
  property_count: 6
  slug: amazon-entity-resolution-get-matching-job-output-structure
- name: Amazon Entity Resolution Get Matching Workflow Input Structure
  property_count: 0
  slug: amazon-entity-resolution-get-matching-workflow-input-structure
- name: Amazon Entity Resolution Get Matching Workflow Output Structure
  property_count: 11
  slug: amazon-entity-resolution-get-matching-workflow-output-structure
- name: Amazon Entity Resolution Get Schema Mapping Input Structure
  property_count: 0
  slug: amazon-entity-resolution-get-schema-mapping-input-structure
- name: Amazon Entity Resolution Get Schema Mapping Output Structure
  property_count: 7
  slug: amazon-entity-resolution-get-schema-mapping-output-structure
- name: Amazon Entity Resolution Incremental Run Config Structure
  property_count: 1
  slug: amazon-entity-resolution-incremental-run-config-structure
- name: Amazon Entity Resolution Incremental Run Type Structure
  property_count: 0
  slug: amazon-entity-resolution-incremental-run-type-structure
- name: Amazon Entity Resolution Input Source Config Structure
  property_count: 0
  slug: amazon-entity-resolution-input-source-config-structure
- name: Amazon Entity Resolution Input Source Input Source Arn String Structure
  property_count: 0
  slug: amazon-entity-resolution-input-source-input-source-arn-string-structure
- name: Amazon Entity Resolution Input Source Structure
  property_count: 3
  slug: amazon-entity-resolution-input-source-structure
- name: Amazon Entity Resolution Integer Structure
  property_count: 0
  slug: amazon-entity-resolution-integer-structure
- name: Amazon Entity Resolution Internal Server Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-internal-server-exception-structure
- name: Amazon Entity Resolution Job Id Structure
  property_count: 0
  slug: amazon-entity-resolution-job-id-structure
- name: Amazon Entity Resolution Job List Structure
  property_count: 0
  slug: amazon-entity-resolution-job-list-structure
- name: Amazon Entity Resolution Job Metrics Structure
  property_count: 4
  slug: amazon-entity-resolution-job-metrics-structure
- name: Amazon Entity Resolution Job Status Structure
  property_count: 0
  slug: amazon-entity-resolution-job-status-structure
- name: Amazon Entity Resolution Job Summary Structure
  property_count: 4
  slug: amazon-entity-resolution-job-summary-structure
- name: Amazon Entity Resolution Kms Arn Structure
  property_count: 0
  slug: amazon-entity-resolution-kms-arn-structure
- name: Amazon Entity Resolution List Matching Jobs Input Max Results Integer Structure
  property_count: 0
  slug: amazon-entity-resolution-list-matching-jobs-input-max-results-integer-structure
- name: Amazon Entity Resolution List Matching Jobs Input Structure
  property_count: 0
  slug: amazon-entity-resolution-list-matching-jobs-input-structure
- name: Amazon Entity Resolution List Matching Jobs Output Structure
  property_count: 2
  slug: amazon-entity-resolution-list-matching-jobs-output-structure
- name: Amazon Entity Resolution List Matching Workflows Input Max Results Integer Structure
  property_count: 0
  slug: amazon-entity-resolution-list-matching-workflows-input-max-results-integer-structure
- name: Amazon Entity Resolution List Matching Workflows Input Structure
  property_count: 0
  slug: amazon-entity-resolution-list-matching-workflows-input-structure
- name: Amazon Entity Resolution List Matching Workflows Output Structure
  property_count: 2
  slug: amazon-entity-resolution-list-matching-workflows-output-structure
- name: Amazon Entity Resolution List Schema Mappings Input Max Results Integer Structure
  property_count: 0
  slug: amazon-entity-resolution-list-schema-mappings-input-max-results-integer-structure
- name: Amazon Entity Resolution List Schema Mappings Input Structure
  property_count: 0
  slug: amazon-entity-resolution-list-schema-mappings-input-structure
- name: Amazon Entity Resolution List Schema Mappings Output Structure
  property_count: 2
  slug: amazon-entity-resolution-list-schema-mappings-output-structure
- name: Amazon Entity Resolution List Tags For Resource Input Structure
  property_count: 0
  slug: amazon-entity-resolution-list-tags-for-resource-input-structure
- name: Amazon Entity Resolution List Tags For Resource Output Structure
  property_count: 1
  slug: amazon-entity-resolution-list-tags-for-resource-output-structure
- name: Amazon Entity Resolution Matching Workflow Arn Structure
  property_count: 0
  slug: amazon-entity-resolution-matching-workflow-arn-structure
- name: Amazon Entity Resolution Matching Workflow List Structure
  property_count: 0
  slug: amazon-entity-resolution-matching-workflow-list-structure
- name: Amazon Entity Resolution Matching Workflow Summary Structure
  property_count: 4
  slug: amazon-entity-resolution-matching-workflow-summary-structure
- name: Amazon Entity Resolution Next Token Structure
  property_count: 0
  slug: amazon-entity-resolution-next-token-structure
- name: Amazon Entity Resolution Output Attribute Structure
  property_count: 2
  slug: amazon-entity-resolution-output-attribute-structure
- name: Amazon Entity Resolution Output Source Config Structure
  property_count: 0
  slug: amazon-entity-resolution-output-source-config-structure
- name: Amazon Entity Resolution Output Source Output List Structure
  property_count: 0
  slug: amazon-entity-resolution-output-source-output-list-structure
- name: Amazon Entity Resolution Output Source Output S3 Path String Structure
  property_count: 0
  slug: amazon-entity-resolution-output-source-output-s3-path-string-structure
- name: Amazon Entity Resolution Output Source Structure
  property_count: 4
  slug: amazon-entity-resolution-output-source-structure
- name: Amazon Entity Resolution Record Attribute Map Key String Structure
  property_count: 0
  slug: amazon-entity-resolution-record-attribute-map-key-string-structure
- name: Amazon Entity Resolution Record Attribute Map Structure
  property_count: 0
  slug: amazon-entity-resolution-record-attribute-map-structure
- name: Amazon Entity Resolution Record Attribute Map Value String Structure
  property_count: 0
  slug: amazon-entity-resolution-record-attribute-map-value-string-structure
- name: Amazon Entity Resolution Resolution Techniques Structure
  property_count: 2
  slug: amazon-entity-resolution-resolution-techniques-structure
- name: Amazon Entity Resolution Resolution Type Structure
  property_count: 0
  slug: amazon-entity-resolution-resolution-type-structure
- name: Amazon Entity Resolution Resource Not Found Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-resource-not-found-exception-structure
- name: Amazon Entity Resolution Rule Based Properties Rules List Structure
  property_count: 0
  slug: amazon-entity-resolution-rule-based-properties-rules-list-structure
- name: Amazon Entity Resolution Rule Based Properties Structure
  property_count: 2
  slug: amazon-entity-resolution-rule-based-properties-structure
- name: Amazon Entity Resolution Rule Matching Keys List Structure
  property_count: 0
  slug: amazon-entity-resolution-rule-matching-keys-list-structure
- name: Amazon Entity Resolution Rule Rule Name String Structure
  property_count: 0
  slug: amazon-entity-resolution-rule-rule-name-string-structure
- name: Amazon Entity Resolution Rule Structure
  property_count: 2
  slug: amazon-entity-resolution-rule-structure
- name: Amazon Entity Resolution Schema Attribute Type Structure
  property_count: 0
  slug: amazon-entity-resolution-schema-attribute-type-structure
- name: Amazon Entity Resolution Schema Input Attribute Structure
  property_count: 4
  slug: amazon-entity-resolution-schema-input-attribute-structure
- name: Amazon Entity Resolution Schema Input Attributes Structure
  property_count: 0
  slug: amazon-entity-resolution-schema-input-attributes-structure
- name: Amazon Entity Resolution Schema Mapping Arn Structure
  property_count: 0
  slug: amazon-entity-resolution-schema-mapping-arn-structure
- name: Amazon Entity Resolution Schema Mapping List Structure
  property_count: 0
  slug: amazon-entity-resolution-schema-mapping-list-structure
- name: Amazon Entity Resolution Schema Mapping Summary Structure
  property_count: 4
  slug: amazon-entity-resolution-schema-mapping-summary-structure
- name: Amazon Entity Resolution Start Matching Job Input Structure
  property_count: 0
  slug: amazon-entity-resolution-start-matching-job-input-structure
- name: Amazon Entity Resolution Start Matching Job Output Structure
  property_count: 1
  slug: amazon-entity-resolution-start-matching-job-output-structure
- name: Amazon Entity Resolution String Structure
  property_count: 0
  slug: amazon-entity-resolution-string-structure
- name: Amazon Entity Resolution Tag Key List Structure
  property_count: 0
  slug: amazon-entity-resolution-tag-key-list-structure
- name: Amazon Entity Resolution Tag Key Structure
  property_count: 0
  slug: amazon-entity-resolution-tag-key-structure
- name: Amazon Entity Resolution Tag Map Structure
  property_count: 0
  slug: amazon-entity-resolution-tag-map-structure
- name: Amazon Entity Resolution Tag Resource Input Structure
  property_count: 1
  slug: amazon-entity-resolution-tag-resource-input-structure
- name: Amazon Entity Resolution Tag Resource Output Structure
  property_count: 0
  slug: amazon-entity-resolution-tag-resource-output-structure
- name: Amazon Entity Resolution Tag Value Structure
  property_count: 0
  slug: amazon-entity-resolution-tag-value-structure
- name: Amazon Entity Resolution Throttling Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-throttling-exception-structure
- name: Amazon Entity Resolution Timestamp Structure
  property_count: 0
  slug: amazon-entity-resolution-timestamp-structure
- name: Amazon Entity Resolution Untag Resource Input Structure
  property_count: 0
  slug: amazon-entity-resolution-untag-resource-input-structure
- name: Amazon Entity Resolution Untag Resource Output Structure
  property_count: 0
  slug: amazon-entity-resolution-untag-resource-output-structure
- name: Amazon Entity Resolution Update Matching Workflow Input Structure
  property_count: 6
  slug: amazon-entity-resolution-update-matching-workflow-input-structure
- name: Amazon Entity Resolution Update Matching Workflow Output Structure
  property_count: 7
  slug: amazon-entity-resolution-update-matching-workflow-output-structure
- name: Amazon Entity Resolution Validation Exception Structure
  property_count: 0
  slug: amazon-entity-resolution-validation-exception-structure
- name: Amazon Entity Resolution Venice Global Arn Structure
  property_count: 0
  slug: amazon-entity-resolution-venice-global-arn-structure
jsonld:
- class_count: 49
  name: Amazon Entity Resolution Context
  property_count: 48
  slug: amazon-entity-resolution-context
layout: provider
modified: '2026-05-19'
name: Amazon Entity Resolution
nav: Providers
network: true
overview: 'Amazon Entity Resolution publishes 3 APIs on the [APIs.io](https://apis.io/) network: Matchingworkflows API, Schemas API, and Tags API. Tagged areas include Amazon Web Services, Data Integration, Data Matching, Entity Resolution, and Machine-Learning.


  The Amazon Entity Resolution catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Entity Resolution''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 26 more developer resources.'
plans:
- name: Amazon Entity Resolution Plans Pricing
  plan_count: 3
  slug: amazon-entity-resolution-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Amazon Entity Resolution Rate Limits
  slug: amazon-entity-resolution-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Entity Resolution API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-entity-resolution-jsonschema-spectral-rules
- effective_rule_count: 66
  extends:
  - spectral:oas
  name: Amazon Entity Resolution API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 13
  slug: amazon-entity-resolution-spectral-rules
score:
  band: strong
  composite: 60.7
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
    contract_quality: 78.2
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-entity-resolution/refs/heads/main/screenshots/amazon-entity-resolution-2026-06-20T171643.png
security:
- kind: authentication
  name: Amazon Entity Resolution Authentication
  slug: amazon-entity-resolution-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Entity Resolution Domain Security
  slug: amazon-entity-resolution-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Entity Resolution Vulnerability Disclosure
  slug: amazon-entity-resolution-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Entity Resolution Trust Center
  slug: amazon-entity-resolution-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-entity-resolution
tags:
- Amazon Web Services
- Data Integration
- Data Matching
- Entity Resolution
- Machine-Learning
use_cases:
- description: Create a single customer view by matching records across CRM, marketing, and transaction systems
  name: Customer Data Unification
- description: Identify and remove duplicate records from databases and data lakes
  name: Data Deduplication
- description: Link user identities across devices and channels for targeted advertising
  name: Identity Resolution for Advertising
- description: Match patient records across different healthcare providers and systems
  name: Healthcare Record Matching
website: https://aws.amazon.com/entity-resolution/
---
