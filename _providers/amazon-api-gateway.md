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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 78
  human_in_the_loop: 0
  name: Amazon Api Gateway Agentic Access
  operation_count: 134
  slug: amazon-api-gateway-agentic-access
  summary_line: 134 operations · 78 acting
api_count: 18
apis:
- description: Build real-time two-way communication applications with WebSocket APIs.
  name: Amazon API Gateway WebSocket API
  slug: websocket-api
- description: Lower latency and lower cost alternative to REST APIs with essential features for building HTTP-based APIs.
  name: Amazon API Gateway HTTP API
  slug: http-api
- description: API for directly managing runtime aspects of deployed APIs, including sending data to connected WebSocket clients via the @connections endpoint and managing connection state.
  name: Amazon API Gateway Management API
  slug: management-api
- description: Operations for managing API keys
  name: Amazon API Gateway API Keys API
  slug: amazon-api-gateway-api-keys-api
- description: Operations for managing API authorizers
  name: Amazon API Gateway Authorizers API
  slug: amazon-api-gateway-authorizers-api
- description: Operations for managing base path mappings
  name: Amazon API Gateway Base Path Mappings API
  slug: amazon-api-gateway-base-path-mappings-api
- description: Operations for managing API deployments
  name: Amazon API Gateway Deployments API
  slug: amazon-api-gateway-deployments-api
- description: Operations for managing API documentation
  name: Amazon API Gateway Documentation API
  slug: amazon-api-gateway-documentation-api
- description: Operations for managing custom domain names
  name: Amazon API Gateway Domain Names API
  slug: amazon-api-gateway-domain-names-api
- description: Operations for managing gateway responses
  name: Amazon API Gateway Gateway Responses API
  slug: amazon-api-gateway-gateway-responses-api
- description: Operations for managing HTTP methods on resources
  name: Amazon API Gateway Methods API
  slug: amazon-api-gateway-methods-api
- description: Operations for managing API data models
  name: Amazon API Gateway Models API
  slug: amazon-api-gateway-models-api
- description: Operations for managing request validators
  name: Amazon API Gateway Request Validators API
  slug: amazon-api-gateway-request-validators-api
- description: Operations for managing API resources (URL paths)
  name: Amazon API Gateway Resources API
  slug: amazon-api-gateway-resources-api
- description: Operations for creating and managing REST APIs
  name: Amazon API Gateway REST APIs API
  slug: amazon-api-gateway-rest-apis-api
- description: Operations for managing deployment stages
  name: Amazon API Gateway Stages API
  slug: amazon-api-gateway-stages-api
- description: Operations for managing usage plans and throttling
  name: Amazon API Gateway Usage Plans API
  slug: amazon-api-gateway-usage-plans-api
- description: Operations for managing VPC links
  name: Amazon API Gateway VPC Links API
  slug: amazon-api-gateway-vpc-links-api
artifact_total: 232
asyncapis:
- description: Amazon API Gateway WebSocket APIs enable real-time two-way communication between clients and backend services. Clients connect via WebSocket protocol and exchange messages through routes that map to L
  name: Amazon API Gateway WebSocket API
  slug: amazon-api-gateway-websocket-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-api-gateway-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-api-gateway-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-api-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-api-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-api-gateway-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/category/application-services/amazon-api-gateway/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/apigateway
- group: docs
  title: ''
  type: CLIReference
  url: https://docs.aws.amazon.com/cli/latest/reference/apigateway/
- group: build
  title: ''
  type: SDK
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: Status
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/api-gateway/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/apigateway/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/api-gateway/pricing/
- group: start
  title: ''
  type: Getting Started
  url: https://aws.amazon.com/api-gateway/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/api-gateway/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-api-gateway
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_code_examples.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-api-gateway-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-api-gateway-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-api-gateway-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-api-gateway-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-api-gateway-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-api-gateway-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-api-gateway-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-api-gateway-llms-full.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-api-gateway-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-api-gateway-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-api-gateway-lifecycle.yml
created: '2024-01-15'
description: Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
examples:
- key_count: 2
  name: Amazon Api Gateway Accesslogsettings Example
  slug: amazon-api-gateway-accesslogsettings-example
- key_count: 10
  name: Amazon Api Gateway Apikey Example
  slug: amazon-api-gateway-apikey-example
- key_count: 3
  name: Amazon Api Gateway Apikeys Example
  slug: amazon-api-gateway-apikeys-example
- key_count: 3
  name: Amazon Api Gateway Apistage Example
  slug: amazon-api-gateway-apistage-example
- key_count: 10
  name: Amazon Api Gateway Authorizer Example
  slug: amazon-api-gateway-authorizer-example
- key_count: 2
  name: Amazon Api Gateway Authorizers Example
  slug: amazon-api-gateway-authorizers-example
- key_count: 3
  name: Amazon Api Gateway Basepathmapping Example
  slug: amazon-api-gateway-basepathmapping-example
- key_count: 2
  name: Amazon Api Gateway Basepathmappings Example
  slug: amazon-api-gateway-basepathmappings-example
- key_count: 3
  name: Amazon Api Gateway Canarysettings Example
  slug: amazon-api-gateway-canarysettings-example
- key_count: 8
  name: Amazon Api Gateway Createapikeyrequest Example
  slug: amazon-api-gateway-createapikeyrequest-example
- key_count: 9
  name: Amazon Api Gateway Createauthorizerrequest Example
  slug: amazon-api-gateway-createauthorizerrequest-example
- key_count: 3
  name: Amazon Api Gateway Createbasepathmappingrequest Example
  slug: amazon-api-gateway-createbasepathmappingrequest-example
- key_count: 8
  name: Amazon Api Gateway Createdeploymentrequest Example
  slug: amazon-api-gateway-createdeploymentrequest-example
- key_count: 2
  name: Amazon Api Gateway Createdocumentationpartrequest Example
  slug: amazon-api-gateway-createdocumentationpartrequest-example
- key_count: 3
  name: Amazon Api Gateway Createdocumentationversionrequest Example
  slug: amazon-api-gateway-createdocumentationversionrequest-example
- key_count: 12
  name: Amazon Api Gateway Createdomainnamerequest Example
  slug: amazon-api-gateway-createdomainnamerequest-example
- key_count: 4
  name: Amazon Api Gateway Createmodelrequest Example
  slug: amazon-api-gateway-createmodelrequest-example
- key_count: 3
  name: Amazon Api Gateway Createrequestvalidatorrequest Example
  slug: amazon-api-gateway-createrequestvalidatorrequest-example
- key_count: 11
  name: Amazon Api Gateway Createrestapirequest Example
  slug: amazon-api-gateway-createrestapirequest-example
- key_count: 10
  name: Amazon Api Gateway Createstagerequest Example
  slug: amazon-api-gateway-createstagerequest-example
- key_count: 6
  name: Amazon Api Gateway Createusageplanrequest Example
  slug: amazon-api-gateway-createusageplanrequest-example
- key_count: 4
  name: Amazon Api Gateway Createvpclinkrequest Example
  slug: amazon-api-gateway-createvpclinkrequest-example
- key_count: 4
  name: Amazon Api Gateway Deployment Example
  slug: amazon-api-gateway-deployment-example
- key_count: 2
  name: Amazon Api Gateway Deploymentcanarysettings Example
  slug: amazon-api-gateway-deploymentcanarysettings-example
- key_count: 2
  name: Amazon Api Gateway Deployments Example
  slug: amazon-api-gateway-deployments-example
- key_count: 3
  name: Amazon Api Gateway Documentationpart Example
  slug: amazon-api-gateway-documentationpart-example
- key_count: 2
  name: Amazon Api Gateway Documentationparts Example
  slug: amazon-api-gateway-documentationparts-example
- key_count: 3
  name: Amazon Api Gateway Documentationversion Example
  slug: amazon-api-gateway-documentationversion-example
- key_count: 2
  name: Amazon Api Gateway Documentationversions Example
  slug: amazon-api-gateway-documentationversions-example
- key_count: 16
  name: Amazon Api Gateway Domainname Example
  slug: amazon-api-gateway-domainname-example
- key_count: 2
  name: Amazon Api Gateway Domainnames Example
  slug: amazon-api-gateway-domainnames-example
- key_count: 2
  name: Amazon Api Gateway Endpointconfiguration Example
  slug: amazon-api-gateway-endpointconfiguration-example
- key_count: 2
  name: Amazon Api Gateway Error Example
  slug: amazon-api-gateway-error-example
- key_count: 5
  name: Amazon Api Gateway Gatewayresponse Example
  slug: amazon-api-gateway-gatewayresponse-example
- key_count: 2
  name: Amazon Api Gateway Gatewayresponses Example
  slug: amazon-api-gateway-gatewayresponses-example
- key_count: 15
  name: Amazon Api Gateway Integration Example
  slug: amazon-api-gateway-integration-example
- key_count: 5
  name: Amazon Api Gateway Integrationresponse Example
  slug: amazon-api-gateway-integrationresponse-example
- key_count: 10
  name: Amazon Api Gateway Method Example
  slug: amazon-api-gateway-method-example
- key_count: 3
  name: Amazon Api Gateway Methodresponse Example
  slug: amazon-api-gateway-methodresponse-example
- key_count: 9
  name: Amazon Api Gateway Methodsetting Example
  slug: amazon-api-gateway-methodsetting-example
- key_count: 2
  name: Amazon Api Gateway Methodsnapshot Example
  slug: amazon-api-gateway-methodsnapshot-example
- key_count: 5
  name: Amazon Api Gateway Model Example
  slug: amazon-api-gateway-model-example
- key_count: 2
  name: Amazon Api Gateway Models Example
  slug: amazon-api-gateway-models-example
- key_count: 4
  name: Amazon Api Gateway Patchoperation Example
  slug: amazon-api-gateway-patchoperation-example
- key_count: 1
  name: Amazon Api Gateway Patchoperations Example
  slug: amazon-api-gateway-patchoperations-example
- key_count: 3
  name: Amazon Api Gateway Putgatewayresponserequest Example
  slug: amazon-api-gateway-putgatewayresponserequest-example
- key_count: 13
  name: Amazon Api Gateway Putintegrationrequest Example
  slug: amazon-api-gateway-putintegrationrequest-example
- key_count: 7
  name: Amazon Api Gateway Putmethodrequest Example
  slug: amazon-api-gateway-putmethodrequest-example
- key_count: 3
  name: Amazon Api Gateway Quotasettings Example
  slug: amazon-api-gateway-quotasettings-example
- key_count: 4
  name: Amazon Api Gateway Requestvalidator Example
  slug: amazon-api-gateway-requestvalidator-example
- key_count: 2
  name: Amazon Api Gateway Requestvalidators Example
  slug: amazon-api-gateway-requestvalidators-example
- key_count: 5
  name: Amazon Api Gateway Resource Example
  slug: amazon-api-gateway-resource-example
- key_count: 2
  name: Amazon Api Gateway Resources Example
  slug: amazon-api-gateway-resources-example
- key_count: 13
  name: Amazon Api Gateway Restapi Example
  slug: amazon-api-gateway-restapi-example
- key_count: 2
  name: Amazon Api Gateway Restapis Example
  slug: amazon-api-gateway-restapis-example
- key_count: 17
  name: Amazon Api Gateway Stage Example
  slug: amazon-api-gateway-stage-example
- key_count: 2
  name: Amazon Api Gateway Stagekey Example
  slug: amazon-api-gateway-stagekey-example
- key_count: 1
  name: Amazon Api Gateway Stages Example
  slug: amazon-api-gateway-stages-example
- key_count: 1
  name: Amazon Api Gateway Throttlesettings Example
  slug: amazon-api-gateway-throttlesettings-example
- key_count: 8
  name: Amazon Api Gateway Usageplan Example
  slug: amazon-api-gateway-usageplan-example
- key_count: 2
  name: Amazon Api Gateway Usageplans Example
  slug: amazon-api-gateway-usageplans-example
- key_count: 7
  name: Amazon Api Gateway Vpclink Example
  slug: amazon-api-gateway-vpclink-example
- key_count: 2
  name: Amazon Api Gateway Vpclinks Example
  slug: amazon-api-gateway-vpclinks-example
features:
- description: Create, configure, and manage REST APIs with resources, methods, integrations, and request/response transformations.
  name: REST API Management
- description: Build real-time two-way communication applications with WebSocket APIs supporting persistent connections and message routing.
  name: WebSocket API Support
- description: Deploy lightweight HTTP APIs with lower latency and cost than REST APIs, optimized for Lambda and HTTP backends.
  name: HTTP API Support
- description: Manage deployment stages with canary releases, stage variables, and throttling configurations for blue/green deployments.
  name: Stage and Deployment Management
- description: Secure APIs with IAM authorization, Lambda authorizers, Cognito user pools, and resource-based policies.
  name: API Security and Authorization
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-api-gateway.png
integrations:
- description: Integrate API Gateway with Lambda functions for serverless request processing without managing infrastructure.
  name: AWS Lambda
- description: Use Cognito user pools and identity pools for managed authentication and authorization in API Gateway.
  name: AWS Cognito
- description: Protect API Gateway endpoints with AWS WAF rules for rate limiting and protection against common web exploits.
  name: AWS WAF
- description: Monitor API performance, errors, and latency using CloudWatch metrics and logs integrated with API Gateway.
  name: AWS CloudWatch
json_schemas:
- name: AccessLogSettings
  property_count: 2
  slug: amazon-api-gateway-accesslogsettings
- name: Amazon API Gateway REST API Definition
  property_count: 20
  slug: amazon-api-gateway-api
- name: ApiKey
  property_count: 10
  slug: amazon-api-gateway-apikey
- name: ApiKeys
  property_count: 3
  slug: amazon-api-gateway-apikeys
- name: ApiStage
  property_count: 3
  slug: amazon-api-gateway-apistage
- name: Authorizer
  property_count: 10
  slug: amazon-api-gateway-authorizer
- name: Authorizers
  property_count: 2
  slug: amazon-api-gateway-authorizers
- name: BasePathMapping
  property_count: 3
  slug: amazon-api-gateway-basepathmapping
- name: BasePathMappings
  property_count: 2
  slug: amazon-api-gateway-basepathmappings
- name: CanarySettings
  property_count: 4
  slug: amazon-api-gateway-canarysettings
- name: CreateApiKeyRequest
  property_count: 8
  slug: amazon-api-gateway-createapikeyrequest
- name: CreateAuthorizerRequest
  property_count: 9
  slug: amazon-api-gateway-createauthorizerrequest
- name: CreateBasePathMappingRequest
  property_count: 3
  slug: amazon-api-gateway-createbasepathmappingrequest
- name: CreateDeploymentRequest
  property_count: 8
  slug: amazon-api-gateway-createdeploymentrequest
- name: CreateDocumentationPartRequest
  property_count: 2
  slug: amazon-api-gateway-createdocumentationpartrequest
- name: CreateDocumentationVersionRequest
  property_count: 3
  slug: amazon-api-gateway-createdocumentationversionrequest
- name: CreateDomainNameRequest
  property_count: 12
  slug: amazon-api-gateway-createdomainnamerequest
- name: CreateModelRequest
  property_count: 4
  slug: amazon-api-gateway-createmodelrequest
- name: CreateRequestValidatorRequest
  property_count: 3
  slug: amazon-api-gateway-createrequestvalidatorrequest
- name: CreateRestApiRequest
  property_count: 11
  slug: amazon-api-gateway-createrestapirequest
- name: CreateStageRequest
  property_count: 10
  slug: amazon-api-gateway-createstagerequest
- name: CreateUsagePlanRequest
  property_count: 6
  slug: amazon-api-gateway-createusageplanrequest
- name: CreateVpcLinkRequest
  property_count: 4
  slug: amazon-api-gateway-createvpclinkrequest
- name: Deployment
  property_count: 4
  slug: amazon-api-gateway-deployment
- name: DeploymentCanarySettings
  property_count: 3
  slug: amazon-api-gateway-deploymentcanarysettings
- name: Deployments
  property_count: 2
  slug: amazon-api-gateway-deployments
- name: DocumentationPart
  property_count: 3
  slug: amazon-api-gateway-documentationpart
- name: DocumentationParts
  property_count: 2
  slug: amazon-api-gateway-documentationparts
- name: DocumentationVersion
  property_count: 3
  slug: amazon-api-gateway-documentationversion
- name: DocumentationVersions
  property_count: 2
  slug: amazon-api-gateway-documentationversions
- name: DomainName
  property_count: 16
  slug: amazon-api-gateway-domainname
- name: DomainNames
  property_count: 2
  slug: amazon-api-gateway-domainnames
- name: EndpointConfiguration
  property_count: 2
  slug: amazon-api-gateway-endpointconfiguration
- name: Error
  property_count: 2
  slug: amazon-api-gateway-error
- name: GatewayResponse
  property_count: 5
  slug: amazon-api-gateway-gatewayresponse
- name: GatewayResponses
  property_count: 2
  slug: amazon-api-gateway-gatewayresponses
- name: Integration
  property_count: 15
  slug: amazon-api-gateway-integration
- name: IntegrationResponse
  property_count: 5
  slug: amazon-api-gateway-integrationresponse
- name: Method
  property_count: 10
  slug: amazon-api-gateway-method
- name: MethodResponse
  property_count: 3
  slug: amazon-api-gateway-methodresponse
- name: MethodSetting
  property_count: 10
  slug: amazon-api-gateway-methodsetting
- name: MethodSnapshot
  property_count: 2
  slug: amazon-api-gateway-methodsnapshot
- name: Model
  property_count: 5
  slug: amazon-api-gateway-model
- name: Models
  property_count: 2
  slug: amazon-api-gateway-models
- name: PatchOperation
  property_count: 4
  slug: amazon-api-gateway-patchoperation
- name: PatchOperations
  property_count: 1
  slug: amazon-api-gateway-patchoperations
- name: PutGatewayResponseRequest
  property_count: 3
  slug: amazon-api-gateway-putgatewayresponserequest
- name: PutIntegrationRequest
  property_count: 13
  slug: amazon-api-gateway-putintegrationrequest
- name: PutMethodRequest
  property_count: 7
  slug: amazon-api-gateway-putmethodrequest
- name: QuotaSettings
  property_count: 3
  slug: amazon-api-gateway-quotasettings
- name: RequestValidator
  property_count: 4
  slug: amazon-api-gateway-requestvalidator
- name: RequestValidators
  property_count: 2
  slug: amazon-api-gateway-requestvalidators
- name: Resource
  property_count: 5
  slug: amazon-api-gateway-resource
- name: Resources
  property_count: 2
  slug: amazon-api-gateway-resources
- name: RestApi
  property_count: 13
  slug: amazon-api-gateway-restapi
- name: RestApis
  property_count: 2
  slug: amazon-api-gateway-restapis
- name: Stage
  property_count: 17
  slug: amazon-api-gateway-stage
- name: StageKey
  property_count: 2
  slug: amazon-api-gateway-stagekey
- name: Stages
  property_count: 1
  slug: amazon-api-gateway-stages
- name: ThrottleSettings
  property_count: 2
  slug: amazon-api-gateway-throttlesettings
- name: UsagePlan
  property_count: 8
  slug: amazon-api-gateway-usageplan
- name: UsagePlans
  property_count: 2
  slug: amazon-api-gateway-usageplans
- name: VpcLink
  property_count: 7
  slug: amazon-api-gateway-vpclink
- name: VpcLinks
  property_count: 2
  slug: amazon-api-gateway-vpclinks
json_structures:
- name: Amazon Api Gateway Accesslogsettings Structure
  property_count: 0
  slug: amazon-api-gateway-accesslogsettings-structure
- name: Amazon Api Gateway Apikey Structure
  property_count: 0
  slug: amazon-api-gateway-apikey-structure
- name: Amazon Api Gateway Apikeys Structure
  property_count: 0
  slug: amazon-api-gateway-apikeys-structure
- name: Amazon Api Gateway Apistage Structure
  property_count: 0
  slug: amazon-api-gateway-apistage-structure
- name: Amazon Api Gateway Authorizer Structure
  property_count: 0
  slug: amazon-api-gateway-authorizer-structure
- name: Amazon Api Gateway Authorizers Structure
  property_count: 0
  slug: amazon-api-gateway-authorizers-structure
- name: Amazon Api Gateway Basepathmapping Structure
  property_count: 0
  slug: amazon-api-gateway-basepathmapping-structure
- name: Amazon Api Gateway Basepathmappings Structure
  property_count: 0
  slug: amazon-api-gateway-basepathmappings-structure
- name: Amazon Api Gateway Canarysettings Structure
  property_count: 0
  slug: amazon-api-gateway-canarysettings-structure
- name: Amazon Api Gateway Createapikeyrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createapikeyrequest-structure
- name: Amazon Api Gateway Createauthorizerrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createauthorizerrequest-structure
- name: Amazon Api Gateway Createbasepathmappingrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createbasepathmappingrequest-structure
- name: Amazon Api Gateway Createdeploymentrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createdeploymentrequest-structure
- name: Amazon Api Gateway Createdocumentationpartrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createdocumentationpartrequest-structure
- name: Amazon Api Gateway Createdocumentationversionrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createdocumentationversionrequest-structure
- name: Amazon Api Gateway Createdomainnamerequest Structure
  property_count: 0
  slug: amazon-api-gateway-createdomainnamerequest-structure
- name: Amazon Api Gateway Createmodelrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createmodelrequest-structure
- name: Amazon Api Gateway Createrequestvalidatorrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createrequestvalidatorrequest-structure
- name: Amazon Api Gateway Createrestapirequest Structure
  property_count: 0
  slug: amazon-api-gateway-createrestapirequest-structure
- name: Amazon Api Gateway Createstagerequest Structure
  property_count: 0
  slug: amazon-api-gateway-createstagerequest-structure
- name: Amazon Api Gateway Createusageplanrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createusageplanrequest-structure
- name: Amazon Api Gateway Createvpclinkrequest Structure
  property_count: 0
  slug: amazon-api-gateway-createvpclinkrequest-structure
- name: Amazon Api Gateway Deployment Structure
  property_count: 0
  slug: amazon-api-gateway-deployment-structure
- name: Amazon Api Gateway Deploymentcanarysettings Structure
  property_count: 0
  slug: amazon-api-gateway-deploymentcanarysettings-structure
- name: Amazon Api Gateway Deployments Structure
  property_count: 0
  slug: amazon-api-gateway-deployments-structure
- name: Amazon Api Gateway Documentationpart Structure
  property_count: 0
  slug: amazon-api-gateway-documentationpart-structure
- name: Amazon Api Gateway Documentationparts Structure
  property_count: 0
  slug: amazon-api-gateway-documentationparts-structure
- name: Amazon Api Gateway Documentationversion Structure
  property_count: 0
  slug: amazon-api-gateway-documentationversion-structure
- name: Amazon Api Gateway Documentationversions Structure
  property_count: 0
  slug: amazon-api-gateway-documentationversions-structure
- name: Amazon Api Gateway Domainname Structure
  property_count: 0
  slug: amazon-api-gateway-domainname-structure
- name: Amazon Api Gateway Domainnames Structure
  property_count: 0
  slug: amazon-api-gateway-domainnames-structure
- name: Amazon Api Gateway Endpointconfiguration Structure
  property_count: 0
  slug: amazon-api-gateway-endpointconfiguration-structure
- name: Amazon Api Gateway Error Structure
  property_count: 0
  slug: amazon-api-gateway-error-structure
- name: Amazon Api Gateway Gatewayresponse Structure
  property_count: 0
  slug: amazon-api-gateway-gatewayresponse-structure
- name: Amazon Api Gateway Gatewayresponses Structure
  property_count: 0
  slug: amazon-api-gateway-gatewayresponses-structure
- name: Amazon Api Gateway Integration Structure
  property_count: 0
  slug: amazon-api-gateway-integration-structure
- name: Amazon Api Gateway Integrationresponse Structure
  property_count: 0
  slug: amazon-api-gateway-integrationresponse-structure
- name: Amazon Api Gateway Method Structure
  property_count: 0
  slug: amazon-api-gateway-method-structure
- name: Amazon Api Gateway Methodresponse Structure
  property_count: 0
  slug: amazon-api-gateway-methodresponse-structure
- name: Amazon Api Gateway Methodsetting Structure
  property_count: 0
  slug: amazon-api-gateway-methodsetting-structure
- name: Amazon Api Gateway Methodsnapshot Structure
  property_count: 0
  slug: amazon-api-gateway-methodsnapshot-structure
- name: Amazon Api Gateway Model Structure
  property_count: 0
  slug: amazon-api-gateway-model-structure
- name: Amazon Api Gateway Models Structure
  property_count: 0
  slug: amazon-api-gateway-models-structure
- name: Amazon Api Gateway Patchoperation Structure
  property_count: 0
  slug: amazon-api-gateway-patchoperation-structure
- name: Amazon Api Gateway Patchoperations Structure
  property_count: 0
  slug: amazon-api-gateway-patchoperations-structure
- name: Amazon Api Gateway Putgatewayresponserequest Structure
  property_count: 0
  slug: amazon-api-gateway-putgatewayresponserequest-structure
- name: Amazon Api Gateway Putintegrationrequest Structure
  property_count: 0
  slug: amazon-api-gateway-putintegrationrequest-structure
- name: Amazon Api Gateway Putmethodrequest Structure
  property_count: 0
  slug: amazon-api-gateway-putmethodrequest-structure
- name: Amazon Api Gateway Quotasettings Structure
  property_count: 0
  slug: amazon-api-gateway-quotasettings-structure
- name: Amazon Api Gateway Requestvalidator Structure
  property_count: 0
  slug: amazon-api-gateway-requestvalidator-structure
- name: Amazon Api Gateway Requestvalidators Structure
  property_count: 0
  slug: amazon-api-gateway-requestvalidators-structure
- name: Amazon Api Gateway Resource Structure
  property_count: 0
  slug: amazon-api-gateway-resource-structure
- name: Amazon Api Gateway Resources Structure
  property_count: 0
  slug: amazon-api-gateway-resources-structure
- name: Amazon Api Gateway Restapi Structure
  property_count: 0
  slug: amazon-api-gateway-restapi-structure
- name: Amazon Api Gateway Restapis Structure
  property_count: 0
  slug: amazon-api-gateway-restapis-structure
- name: Amazon Api Gateway Stage Structure
  property_count: 0
  slug: amazon-api-gateway-stage-structure
- name: Amazon Api Gateway Stagekey Structure
  property_count: 0
  slug: amazon-api-gateway-stagekey-structure
- name: Amazon Api Gateway Stages Structure
  property_count: 0
  slug: amazon-api-gateway-stages-structure
- name: Amazon Api Gateway Throttlesettings Structure
  property_count: 0
  slug: amazon-api-gateway-throttlesettings-structure
- name: Amazon Api Gateway Usageplan Structure
  property_count: 0
  slug: amazon-api-gateway-usageplan-structure
- name: Amazon Api Gateway Usageplans Structure
  property_count: 0
  slug: amazon-api-gateway-usageplans-structure
- name: Amazon Api Gateway Vpclink Structure
  property_count: 0
  slug: amazon-api-gateway-vpclink-structure
- name: Amazon Api Gateway Vpclinks Structure
  property_count: 0
  slug: amazon-api-gateway-vpclinks-structure
jsonld:
- class_count: 0
  name: Amazon Api Gateway Context
  property_count: 13
  slug: amazon-api-gateway-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-api-gateway-mcp.yml
  slug: amazon-api-gateway-mcpyml
modified: '2026-06-20'
name: Amazon API Gateway
nav: Providers
network: true
overview: 'Amazon API Gateway publishes 16 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, API Keys API, Authorizers API, and 13 more. Tagged areas include Gateway, HTTP API, REST API, Serverless, and WebSocket.


  The Amazon API Gateway catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Amazon API Gateway''s developer surface includes authentication, engineering blog, support, developer console, SDKs, status page, documentation, and 27 more developer resources.'
random_paper: 33
rules:
- name: Amazon API Gateway API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: amazon-api-gateway-asyncapi-spectral-rules
- name: Amazon API Gateway API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-api-gateway-jsonschema-spectral-rules
- name: Amazon API Gateway API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 10
  slug: amazon-api-gateway-spectral-rules
score:
  band: strong
  composite: 58.0
  delta: -1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 83.2
    developer_ergonomics: 41.3
    discoverability: 77.8
    governance: 69.8
    operational_transparency: 5.3
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/screenshots/amazon-api-gateway-2026-07-25T195913.png
security:
- kind: authentication
  name: Amazon Api Gateway Authentication
  slug: amazon-api-gateway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Api Gateway Domain Security
  slug: amazon-api-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Api Gateway Vulnerability Disclosure
  slug: amazon-api-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Api Gateway Trust Center
  slug: amazon-api-gateway-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-api-gateway
tags:
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
use_cases:
- description: Build serverless REST APIs backed by Lambda functions using API Gateway as the front door for request routing.
  name: Serverless API Backend
- description: Use API Gateway as a unified entry point for microservices, providing routing, authentication, and rate limiting.
  name: Microservices Gateway
- description: Build chat, collaboration, and live data streaming applications using WebSocket APIs with persistent client connections.
  name: Real-Time Applications
- description: Automate API creation, deployment, and versioning using the API Gateway control plane API in CI/CD pipelines.
  name: API Lifecycle Automation
website: https://aws.amazon.com/api-gateway/
---
