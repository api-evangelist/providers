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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Amazon Appsync Agentic Access
  operation_count: 44
  slug: amazon-appsync-agentic-access
  summary_line: 44 operations · 27 acting
api_count: 9
apis:
- description: Manage API keys for authentication
  name: Amazon AppSync Api Keys API
  slug: amazon-appsync-api-keys-api
- description: Manage data sources connected to GraphQL APIs
  name: Amazon AppSync Data Sources API
  slug: amazon-appsync-data-sources-api
- description: Manage custom domain names for AppSync APIs
  name: Amazon AppSync Domain Names API
  slug: amazon-appsync-domain-names-api
- description: Manage reusable pipeline resolver functions
  name: Amazon AppSync Functions API
  slug: amazon-appsync-functions-api
- description: Manage GraphQL API configurations
  name: Amazon AppSync GraphQL APIs API
  slug: amazon-appsync-graphql-apis-api
- description: Manage field resolvers for GraphQL types
  name: Amazon AppSync Resolvers API
  slug: amazon-appsync-resolvers-api
- description: Manage GraphQL schema documents
  name: Amazon AppSync Schema API
  slug: amazon-appsync-schema-api
- description: Resource tagging operations
  name: Amazon AppSync Tags API
  slug: amazon-appsync-tags-api
- description: Manage GraphQL type definitions
  name: Amazon AppSync Types API
  slug: amazon-appsync-types-api
artifact_total: 275
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon AppSync Api Keys API
  slug: open-amazon-appsync-api-keys-api
- collection_type: open
  name: Amazon AppSync Api Keys Data Sources API
  slug: open-amazon-appsync-data-sources-api
- collection_type: open
  name: Amazon AppSync Api Keys Domain Names API
  slug: open-amazon-appsync-domain-names-api
- collection_type: open
  name: Amazon AppSync Api Keys Functions API
  slug: open-amazon-appsync-functions-api
- collection_type: open
  name: Amazon AppSync Api Keys GraphQL APIs API
  slug: open-amazon-appsync-graphql-apis-api
- collection_type: open
  name: Amazon AppSync Api Keys Resolvers API
  slug: open-amazon-appsync-resolvers-api
- collection_type: open
  name: Amazon AppSync Api Keys Schema API
  slug: open-amazon-appsync-schema-api
- collection_type: open
  name: Amazon AppSync Api Keys Tags API
  slug: open-amazon-appsync-tags-api
- collection_type: open
  name: Amazon AppSync Api Keys Types API
  slug: open-amazon-appsync-types-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-appsync-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-appsync-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-appsync-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-appsync-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-appsync-authentication.yml
- group: build
  title: ''
  type: Packages
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/packages/amazon-appsync-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/mcp/amazon-appsync-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/llms/amazon-appsync-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/well-known/amazon-appsync-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/well-known/amazon-appsync-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/lifecycle/amazon-appsync-lifecycle.yml
created: '2024-01-15'
description: Amazon AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint to securely query, update, or publish data.
examples:
- key_count: 3
  name: Appsync Additional Authentication Provider Example
  slug: appsync-additional-authentication-provider-example
- key_count: 4
  name: Appsync Api Association Example
  slug: appsync-api-association-example
- key_count: 4
  name: Appsync Api Key Example
  slug: appsync-api-key-example
- key_count: 2
  name: Appsync App Sync Runtime Example
  slug: appsync-app-sync-runtime-example
- key_count: 1
  name: Appsync Associate Api Request Example
  slug: appsync-associate-api-request-example
- key_count: 1
  name: Appsync Associate Api Response Example
  slug: appsync-associate-api-response-example
- key_count: 2
  name: Appsync Caching Config Example
  slug: appsync-caching-config-example
- key_count: 3
  name: Appsync Cognito User Pool Config Example
  slug: appsync-cognito-user-pool-config-example
- key_count: 2
  name: Appsync Create Api Key Request Example
  slug: appsync-create-api-key-request-example
- key_count: 1
  name: Appsync Create Api Key Response Example
  slug: appsync-create-api-key-response-example
- key_count: 7
  name: Appsync Create Data Source Request Example
  slug: appsync-create-data-source-request-example
- key_count: 1
  name: Appsync Create Data Source Response Example
  slug: appsync-create-data-source-response-example
- key_count: 3
  name: Appsync Create Domain Name Request Example
  slug: appsync-create-domain-name-request-example
- key_count: 1
  name: Appsync Create Domain Name Response Example
  slug: appsync-create-domain-name-response-example
- key_count: 10
  name: Appsync Create Function Request Example
  slug: appsync-create-function-request-example
- key_count: 1
  name: Appsync Create Function Response Example
  slug: appsync-create-function-response-example
- key_count: 9
  name: Appsync Create Graphql Api Request Example
  slug: appsync-create-graphql-api-request-example
- key_count: 1
  name: Appsync Create Graphql Api Response Example
  slug: appsync-create-graphql-api-response-example
- key_count: 11
  name: Appsync Create Resolver Request Example
  slug: appsync-create-resolver-request-example
- key_count: 1
  name: Appsync Create Resolver Response Example
  slug: appsync-create-resolver-response-example
- key_count: 2
  name: Appsync Create Type Request Example
  slug: appsync-create-type-request-example
- key_count: 1
  name: Appsync Create Type Response Example
  slug: appsync-create-type-response-example
- key_count: 9
  name: Appsync Data Source Example
  slug: appsync-data-source-example
- key_count: 5
  name: Appsync Domain Name Config Example
  slug: appsync-domain-name-config-example
- key_count: 5
  name: Appsync Dynamodb Data Source Config Example
  slug: appsync-dynamodb-data-source-config-example
- key_count: 2
  name: Appsync Elasticsearch Data Source Config Example
  slug: appsync-elasticsearch-data-source-config-example
- key_count: 2
  name: Appsync Error Response Example
  slug: appsync-error-response-example
- key_count: 2
  name: Appsync Evaluate Mapping Template Request Example
  slug: appsync-evaluate-mapping-template-request-example
- key_count: 3
  name: Appsync Evaluate Mapping Template Response Example
  slug: appsync-evaluate-mapping-template-response-example
- key_count: 12
  name: Appsync Function Configuration Example
  slug: appsync-function-configuration-example
- key_count: 1
  name: Appsync Get Api Association Response Example
  slug: appsync-get-api-association-response-example
- key_count: 1
  name: Appsync Get Data Source Response Example
  slug: appsync-get-data-source-response-example
- key_count: 1
  name: Appsync Get Domain Name Response Example
  slug: appsync-get-domain-name-response-example
- key_count: 1
  name: Appsync Get Function Response Example
  slug: appsync-get-function-response-example
- key_count: 1
  name: Appsync Get Graphql Api Response Example
  slug: appsync-get-graphql-api-response-example
- key_count: 1
  name: Appsync Get Introspection Schema Response Example
  slug: appsync-get-introspection-schema-response-example
- key_count: 1
  name: Appsync Get Resolver Response Example
  slug: appsync-get-resolver-response-example
- key_count: 2
  name: Appsync Get Schema Creation Status Response Example
  slug: appsync-get-schema-creation-status-response-example
- key_count: 1
  name: Appsync Get Type Response Example
  slug: appsync-get-type-response-example
- key_count: 13
  name: Appsync Graphql Api Example
  slug: appsync-graphql-api-example
- key_count: 2
  name: Appsync Http Data Source Config Example
  slug: appsync-http-data-source-config-example
- key_count: 3
  name: Appsync Lambda Authorizer Config Example
  slug: appsync-lambda-authorizer-config-example
- key_count: 1
  name: Appsync Lambda Data Source Config Example
  slug: appsync-lambda-data-source-config-example
- key_count: 2
  name: Appsync List Api Keys Response Example
  slug: appsync-list-api-keys-response-example
- key_count: 2
  name: Appsync List Data Sources Response Example
  slug: appsync-list-data-sources-response-example
- key_count: 2
  name: Appsync List Domain Names Response Example
  slug: appsync-list-domain-names-response-example
- key_count: 2
  name: Appsync List Functions Response Example
  slug: appsync-list-functions-response-example
- key_count: 2
  name: Appsync List Graphql Apis Response Example
  slug: appsync-list-graphql-apis-response-example
- key_count: 2
  name: Appsync List Resolvers Response Example
  slug: appsync-list-resolvers-response-example
- key_count: 1
  name: Appsync List Tags For Resource Response Example
  slug: appsync-list-tags-for-resource-response-example
- key_count: 2
  name: Appsync List Types Response Example
  slug: appsync-list-types-response-example
- key_count: 3
  name: Appsync Log Config Example
  slug: appsync-log-config-example
- key_count: 1
  name: Appsync Pipeline Config Example
  slug: appsync-pipeline-config-example
- key_count: 13
  name: Appsync Resolver Example
  slug: appsync-resolver-example
- key_count: 1
  name: Appsync Start Schema Creation Request Example
  slug: appsync-start-schema-creation-request-example
- key_count: 1
  name: Appsync Start Schema Creation Response Example
  slug: appsync-start-schema-creation-response-example
- key_count: 2
  name: Appsync Sync Config Example
  slug: appsync-sync-config-example
- key_count: 1
  name: Appsync Tag Resource Request Example
  slug: appsync-tag-resource-request-example
- key_count: 5
  name: Appsync Type Example
  slug: appsync-type-example
- key_count: 2
  name: Appsync Update Api Key Request Example
  slug: appsync-update-api-key-request-example
- key_count: 1
  name: Appsync Update Api Key Response Example
  slug: appsync-update-api-key-response-example
- key_count: 4
  name: Appsync Update Data Source Request Example
  slug: appsync-update-data-source-request-example
- key_count: 1
  name: Appsync Update Data Source Response Example
  slug: appsync-update-data-source-response-example
- key_count: 1
  name: Appsync Update Domain Name Request Example
  slug: appsync-update-domain-name-request-example
- key_count: 1
  name: Appsync Update Domain Name Response Example
  slug: appsync-update-domain-name-response-example
- key_count: 6
  name: Appsync Update Function Request Example
  slug: appsync-update-function-request-example
- key_count: 1
  name: Appsync Update Function Response Example
  slug: appsync-update-function-response-example
- key_count: 4
  name: Appsync Update Graphql Api Request Example
  slug: appsync-update-graphql-api-request-example
- key_count: 1
  name: Appsync Update Graphql Api Response Example
  slug: appsync-update-graphql-api-response-example
- key_count: 5
  name: Appsync Update Resolver Request Example
  slug: appsync-update-resolver-request-example
- key_count: 1
  name: Appsync Update Resolver Response Example
  slug: appsync-update-resolver-response-example
- key_count: 2
  name: Appsync Update Type Request Example
  slug: appsync-update-type-request-example
- key_count: 1
  name: Appsync Update Type Response Example
  slug: appsync-update-type-response-example
features:
- Managed GraphQL API hosting with automatic scaling
- Multiple authentication modes including API key, IAM, Cognito, and Lambda
- Real-time subscriptions via WebSocket connections
- Pipeline resolvers for composing multi-step data access patterns
- Direct Lambda resolvers with APPSYNC_JS runtime support
- Built-in caching for improved performance
- Conflict detection and resolution for offline sync use cases
- Custom domain names with ACM certificate integration
- X-Ray tracing and CloudWatch logging integration
- Merged APIs for combining multiple GraphQL APIs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-appsync.png
integrations:
- Amazon DynamoDB
- AWS Lambda
- Amazon OpenSearch Service
- Amazon RDS
- Amazon EventBridge
- Amazon Cognito
- AWS IAM
- AWS WAF
- Amazon CloudWatch
- AWS X-Ray
- AWS Certificate Manager
- Amazon Route 53
json_schemas:
- name: Amazon AppSync GraphQL API
  property_count: 15
  slug: amazon-appsync
- name: AdditionalAuthenticationProvider
  property_count: 3
  slug: appsync-additional-authentication-provider
- name: ApiAssociation
  property_count: 4
  slug: appsync-api-association
- name: ApiKey
  property_count: 4
  slug: appsync-api-key
- name: AppSyncRuntime
  property_count: 2
  slug: appsync-app-sync-runtime
- name: AssociateApiRequest
  property_count: 1
  slug: appsync-associate-api-request
- name: AssociateApiResponse
  property_count: 1
  slug: appsync-associate-api-response
- name: CachingConfig
  property_count: 2
  slug: appsync-caching-config
- name: CognitoUserPoolConfig
  property_count: 3
  slug: appsync-cognito-user-pool-config
- name: CreateApiKeyRequest
  property_count: 2
  slug: appsync-create-api-key-request
- name: CreateApiKeyResponse
  property_count: 1
  slug: appsync-create-api-key-response
- name: CreateDataSourceRequest
  property_count: 7
  slug: appsync-create-data-source-request
- name: CreateDataSourceResponse
  property_count: 1
  slug: appsync-create-data-source-response
- name: CreateDomainNameRequest
  property_count: 3
  slug: appsync-create-domain-name-request
- name: CreateDomainNameResponse
  property_count: 1
  slug: appsync-create-domain-name-response
- name: CreateFunctionRequest
  property_count: 10
  slug: appsync-create-function-request
- name: CreateFunctionResponse
  property_count: 1
  slug: appsync-create-function-response
- name: CreateGraphqlApiRequest
  property_count: 9
  slug: appsync-create-graphql-api-request
- name: CreateGraphqlApiResponse
  property_count: 1
  slug: appsync-create-graphql-api-response
- name: CreateResolverRequest
  property_count: 11
  slug: appsync-create-resolver-request
- name: CreateResolverResponse
  property_count: 1
  slug: appsync-create-resolver-response
- name: CreateTypeRequest
  property_count: 2
  slug: appsync-create-type-request
- name: CreateTypeResponse
  property_count: 1
  slug: appsync-create-type-response
- name: DataSource
  property_count: 9
  slug: appsync-data-source
- name: DomainNameConfig
  property_count: 5
  slug: appsync-domain-name-config
- name: DynamodbDataSourceConfig
  property_count: 5
  slug: appsync-dynamodb-data-source-config
- name: ElasticsearchDataSourceConfig
  property_count: 2
  slug: appsync-elasticsearch-data-source-config
- name: ErrorResponse
  property_count: 2
  slug: appsync-error-response
- name: EvaluateMappingTemplateRequest
  property_count: 2
  slug: appsync-evaluate-mapping-template-request
- name: EvaluateMappingTemplateResponse
  property_count: 3
  slug: appsync-evaluate-mapping-template-response
- name: FunctionConfiguration
  property_count: 12
  slug: appsync-function-configuration
- name: GetApiAssociationResponse
  property_count: 1
  slug: appsync-get-api-association-response
- name: GetDataSourceResponse
  property_count: 1
  slug: appsync-get-data-source-response
- name: GetDomainNameResponse
  property_count: 1
  slug: appsync-get-domain-name-response
- name: GetFunctionResponse
  property_count: 1
  slug: appsync-get-function-response
- name: GetGraphqlApiResponse
  property_count: 1
  slug: appsync-get-graphql-api-response
- name: GetIntrospectionSchemaResponse
  property_count: 1
  slug: appsync-get-introspection-schema-response
- name: GetResolverResponse
  property_count: 1
  slug: appsync-get-resolver-response
- name: GetSchemaCreationStatusResponse
  property_count: 2
  slug: appsync-get-schema-creation-status-response
- name: GetTypeResponse
  property_count: 1
  slug: appsync-get-type-response
- name: GraphqlApi
  property_count: 13
  slug: appsync-graphql-api
- name: HttpDataSourceConfig
  property_count: 2
  slug: appsync-http-data-source-config
- name: LambdaAuthorizerConfig
  property_count: 3
  slug: appsync-lambda-authorizer-config
- name: LambdaDataSourceConfig
  property_count: 1
  slug: appsync-lambda-data-source-config
- name: ListApiKeysResponse
  property_count: 2
  slug: appsync-list-api-keys-response
- name: ListDataSourcesResponse
  property_count: 2
  slug: appsync-list-data-sources-response
- name: ListDomainNamesResponse
  property_count: 2
  slug: appsync-list-domain-names-response
- name: ListFunctionsResponse
  property_count: 2
  slug: appsync-list-functions-response
- name: ListGraphqlApisResponse
  property_count: 2
  slug: appsync-list-graphql-apis-response
- name: ListResolversResponse
  property_count: 2
  slug: appsync-list-resolvers-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: appsync-list-tags-for-resource-response
- name: ListTypesResponse
  property_count: 2
  slug: appsync-list-types-response
- name: LogConfig
  property_count: 3
  slug: appsync-log-config
- name: PipelineConfig
  property_count: 1
  slug: appsync-pipeline-config
- name: Resolver
  property_count: 13
  slug: appsync-resolver
- name: StartSchemaCreationRequest
  property_count: 1
  slug: appsync-start-schema-creation-request
- name: StartSchemaCreationResponse
  property_count: 1
  slug: appsync-start-schema-creation-response
- name: SyncConfig
  property_count: 2
  slug: appsync-sync-config
- name: TagResourceRequest
  property_count: 1
  slug: appsync-tag-resource-request
- name: Type
  property_count: 5
  slug: appsync-type
- name: UpdateApiKeyRequest
  property_count: 2
  slug: appsync-update-api-key-request
- name: UpdateApiKeyResponse
  property_count: 1
  slug: appsync-update-api-key-response
- name: UpdateDataSourceRequest
  property_count: 4
  slug: appsync-update-data-source-request
- name: UpdateDataSourceResponse
  property_count: 1
  slug: appsync-update-data-source-response
- name: UpdateDomainNameRequest
  property_count: 1
  slug: appsync-update-domain-name-request
- name: UpdateDomainNameResponse
  property_count: 1
  slug: appsync-update-domain-name-response
- name: UpdateFunctionRequest
  property_count: 6
  slug: appsync-update-function-request
- name: UpdateFunctionResponse
  property_count: 1
  slug: appsync-update-function-response
- name: UpdateGraphqlApiRequest
  property_count: 4
  slug: appsync-update-graphql-api-request
- name: UpdateGraphqlApiResponse
  property_count: 1
  slug: appsync-update-graphql-api-response
- name: UpdateResolverRequest
  property_count: 5
  slug: appsync-update-resolver-request
- name: UpdateResolverResponse
  property_count: 1
  slug: appsync-update-resolver-response
- name: UpdateTypeRequest
  property_count: 2
  slug: appsync-update-type-request
- name: UpdateTypeResponse
  property_count: 1
  slug: appsync-update-type-response
json_structures:
- name: Appsync Additional Authentication Provider Structure
  property_count: 0
  slug: appsync-additional-authentication-provider-structure
- name: Appsync Api Association Structure
  property_count: 0
  slug: appsync-api-association-structure
- name: Appsync Api Key Structure
  property_count: 0
  slug: appsync-api-key-structure
- name: Appsync App Sync Runtime Structure
  property_count: 0
  slug: appsync-app-sync-runtime-structure
- name: Appsync Associate Api Request Structure
  property_count: 0
  slug: appsync-associate-api-request-structure
- name: Appsync Associate Api Response Structure
  property_count: 0
  slug: appsync-associate-api-response-structure
- name: Appsync Caching Config Structure
  property_count: 0
  slug: appsync-caching-config-structure
- name: Appsync Cognito User Pool Config Structure
  property_count: 0
  slug: appsync-cognito-user-pool-config-structure
- name: Appsync Create Api Key Request Structure
  property_count: 0
  slug: appsync-create-api-key-request-structure
- name: Appsync Create Api Key Response Structure
  property_count: 0
  slug: appsync-create-api-key-response-structure
- name: Appsync Create Data Source Request Structure
  property_count: 0
  slug: appsync-create-data-source-request-structure
- name: Appsync Create Data Source Response Structure
  property_count: 0
  slug: appsync-create-data-source-response-structure
- name: Appsync Create Domain Name Request Structure
  property_count: 0
  slug: appsync-create-domain-name-request-structure
- name: Appsync Create Domain Name Response Structure
  property_count: 0
  slug: appsync-create-domain-name-response-structure
- name: Appsync Create Function Request Structure
  property_count: 0
  slug: appsync-create-function-request-structure
- name: Appsync Create Function Response Structure
  property_count: 0
  slug: appsync-create-function-response-structure
- name: Appsync Create Graphql Api Request Structure
  property_count: 0
  slug: appsync-create-graphql-api-request-structure
- name: Appsync Create Graphql Api Response Structure
  property_count: 0
  slug: appsync-create-graphql-api-response-structure
- name: Appsync Create Resolver Request Structure
  property_count: 0
  slug: appsync-create-resolver-request-structure
- name: Appsync Create Resolver Response Structure
  property_count: 0
  slug: appsync-create-resolver-response-structure
- name: Appsync Create Type Request Structure
  property_count: 0
  slug: appsync-create-type-request-structure
- name: Appsync Create Type Response Structure
  property_count: 0
  slug: appsync-create-type-response-structure
- name: Appsync Data Source Structure
  property_count: 0
  slug: appsync-data-source-structure
- name: Appsync Domain Name Config Structure
  property_count: 0
  slug: appsync-domain-name-config-structure
- name: Appsync Dynamodb Data Source Config Structure
  property_count: 0
  slug: appsync-dynamodb-data-source-config-structure
- name: Appsync Elasticsearch Data Source Config Structure
  property_count: 0
  slug: appsync-elasticsearch-data-source-config-structure
- name: Appsync Error Response Structure
  property_count: 0
  slug: appsync-error-response-structure
- name: Appsync Evaluate Mapping Template Request Structure
  property_count: 0
  slug: appsync-evaluate-mapping-template-request-structure
- name: Appsync Evaluate Mapping Template Response Structure
  property_count: 0
  slug: appsync-evaluate-mapping-template-response-structure
- name: Appsync Function Configuration Structure
  property_count: 0
  slug: appsync-function-configuration-structure
- name: Appsync Get Api Association Response Structure
  property_count: 0
  slug: appsync-get-api-association-response-structure
- name: Appsync Get Data Source Response Structure
  property_count: 0
  slug: appsync-get-data-source-response-structure
- name: Appsync Get Domain Name Response Structure
  property_count: 0
  slug: appsync-get-domain-name-response-structure
- name: Appsync Get Function Response Structure
  property_count: 0
  slug: appsync-get-function-response-structure
- name: Appsync Get Graphql Api Response Structure
  property_count: 0
  slug: appsync-get-graphql-api-response-structure
- name: Appsync Get Introspection Schema Response Structure
  property_count: 0
  slug: appsync-get-introspection-schema-response-structure
- name: Appsync Get Resolver Response Structure
  property_count: 0
  slug: appsync-get-resolver-response-structure
- name: Appsync Get Schema Creation Status Response Structure
  property_count: 0
  slug: appsync-get-schema-creation-status-response-structure
- name: Appsync Get Type Response Structure
  property_count: 0
  slug: appsync-get-type-response-structure
- name: Appsync Graphql Api Structure
  property_count: 0
  slug: appsync-graphql-api-structure
- name: Appsync Http Data Source Config Structure
  property_count: 0
  slug: appsync-http-data-source-config-structure
- name: Appsync Lambda Authorizer Config Structure
  property_count: 0
  slug: appsync-lambda-authorizer-config-structure
- name: Appsync Lambda Data Source Config Structure
  property_count: 0
  slug: appsync-lambda-data-source-config-structure
- name: Appsync List Api Keys Response Structure
  property_count: 0
  slug: appsync-list-api-keys-response-structure
- name: Appsync List Data Sources Response Structure
  property_count: 0
  slug: appsync-list-data-sources-response-structure
- name: Appsync List Domain Names Response Structure
  property_count: 0
  slug: appsync-list-domain-names-response-structure
- name: Appsync List Functions Response Structure
  property_count: 0
  slug: appsync-list-functions-response-structure
- name: Appsync List Graphql Apis Response Structure
  property_count: 0
  slug: appsync-list-graphql-apis-response-structure
- name: Appsync List Resolvers Response Structure
  property_count: 0
  slug: appsync-list-resolvers-response-structure
- name: Appsync List Tags For Resource Response Structure
  property_count: 0
  slug: appsync-list-tags-for-resource-response-structure
- name: Appsync List Types Response Structure
  property_count: 0
  slug: appsync-list-types-response-structure
- name: Appsync Log Config Structure
  property_count: 0
  slug: appsync-log-config-structure
- name: Appsync Pipeline Config Structure
  property_count: 0
  slug: appsync-pipeline-config-structure
- name: Appsync Resolver Structure
  property_count: 0
  slug: appsync-resolver-structure
- name: Appsync Start Schema Creation Request Structure
  property_count: 0
  slug: appsync-start-schema-creation-request-structure
- name: Appsync Start Schema Creation Response Structure
  property_count: 0
  slug: appsync-start-schema-creation-response-structure
- name: Appsync Sync Config Structure
  property_count: 0
  slug: appsync-sync-config-structure
- name: Appsync Tag Resource Request Structure
  property_count: 0
  slug: appsync-tag-resource-request-structure
- name: Appsync Type Structure
  property_count: 0
  slug: appsync-type-structure
- name: Appsync Update Api Key Request Structure
  property_count: 0
  slug: appsync-update-api-key-request-structure
- name: Appsync Update Api Key Response Structure
  property_count: 0
  slug: appsync-update-api-key-response-structure
- name: Appsync Update Data Source Request Structure
  property_count: 0
  slug: appsync-update-data-source-request-structure
- name: Appsync Update Data Source Response Structure
  property_count: 0
  slug: appsync-update-data-source-response-structure
- name: Appsync Update Domain Name Request Structure
  property_count: 0
  slug: appsync-update-domain-name-request-structure
- name: Appsync Update Domain Name Response Structure
  property_count: 0
  slug: appsync-update-domain-name-response-structure
- name: Appsync Update Function Request Structure
  property_count: 0
  slug: appsync-update-function-request-structure
- name: Appsync Update Function Response Structure
  property_count: 0
  slug: appsync-update-function-response-structure
- name: Appsync Update Graphql Api Request Structure
  property_count: 0
  slug: appsync-update-graphql-api-request-structure
- name: Appsync Update Graphql Api Response Structure
  property_count: 0
  slug: appsync-update-graphql-api-response-structure
- name: Appsync Update Resolver Request Structure
  property_count: 0
  slug: appsync-update-resolver-request-structure
- name: Appsync Update Resolver Response Structure
  property_count: 0
  slug: appsync-update-resolver-response-structure
- name: Appsync Update Type Request Structure
  property_count: 0
  slug: appsync-update-type-request-structure
- name: Appsync Update Type Response Structure
  property_count: 0
  slug: appsync-update-type-response-structure
jsonld:
- class_count: 73
  name: Amazon Appsync Context
  property_count: 0
  slug: amazon-appsync-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon AppSync MCP Server
  slug: amazon-appsync-mcp-server
modified: '2026-06-20'
name: Amazon AppSync
nav: Providers
network: true
overview: 'Amazon AppSync publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Api Keys API, Data Sources API, Domain Names API, and 6 more. Tagged areas include Amazon AppSync, GraphQL, API Management, and Serverless.


  The Amazon AppSync catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon AppSync''s developer surface includes authentication and 10 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon AppSync API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-appsync-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Amazon AppSync API Rules
  rule_count: 28
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 12
  slug: amazon-appsync-spectral-rules
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 76.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/screenshots/amazon-appsync-2026-07-25T195928.png
security:
- kind: authentication
  name: Amazon Appsync Authentication
  slug: amazon-appsync-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Appsync Domain Security
  slug: amazon-appsync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Appsync Vulnerability Disclosure
  slug: amazon-appsync-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-appsync
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
use_cases:
- Build mobile and web applications with a unified GraphQL data layer
- Implement real-time features like live notifications and chat with subscriptions
- Create a unified data access layer across multiple microservices
- Build offline-capable mobile apps with automatic conflict resolution
- Expose DynamoDB tables, Lambda functions, and OpenSearch as GraphQL APIs
- Implement federated GraphQL across multiple teams with Merged APIs
---
