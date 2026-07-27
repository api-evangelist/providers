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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Aws Api Gateway Agentic Access
  operation_count: 32
  slug: aws-api-gateway-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 13
apis:
- description: The API Gateway Portals control plane (introduced November 19, 2025) lets you create branded developer portals that catalog REST APIs. A portal contains PortalProducts (logical groupings of REST APIs)
  name: Amazon API Gateway Portals
  slug: aws-api-gateway-portals
- description: Manage API keys
  name: Amazon API Gateway ApiKeys API
  slug: aws-api-gateway-apikeys-api
- description: The Apis API from Amazon API Gateway — 2 operation(s) for apis.
  name: Amazon API Gateway Apis API
  slug: aws-api-gateway-apis-api
- description: Manage authorizers
  name: Amazon API Gateway Authorizers API
  slug: aws-api-gateway-authorizers-api
- description: Manage and message active WebSocket connections
  name: Amazon API Gateway Connections API
  slug: aws-api-gateway-connections-api
- description: Manage API deployments
  name: Amazon API Gateway Deployments API
  slug: aws-api-gateway-deployments-api
- description: Manage backend integrations
  name: Amazon API Gateway Integrations API
  slug: aws-api-gateway-integrations-api
- description: Manage HTTP methods on resources
  name: Amazon API Gateway Methods API
  slug: aws-api-gateway-methods-api
- description: Manage resources within a REST API
  name: Amazon API Gateway Resources API
  slug: aws-api-gateway-resources-api
- description: Manage REST API definitions
  name: Amazon API Gateway RestApis API
  slug: aws-api-gateway-restapis-api
- description: Manage routes within an API
  name: Amazon API Gateway Routes API
  slug: aws-api-gateway-routes-api
- description: Manage deployment stages
  name: Amazon API Gateway Stages API
  slug: aws-api-gateway-stages-api
- description: Manage usage plans
  name: Amazon API Gateway UsagePlans API
  slug: aws-api-gateway-usageplans-api
arazzos:
- description: Verify a REST API exists, attach a method to one of its resources, and publish a fresh deployment.
  name: AWS API Gateway Add a Method and Redeploy
  slug: aws-api-gateway-add-method-and-redeploy-workflow
- description: Confirm an HTTP API and enumerate its routes, integrations, and stages in a single read-only pass.
  name: AWS API Gateway Audit an HTTP API Surface
  slug: aws-api-gateway-audit-http-api-workflow
- description: Create an HTTP API, attach a backend integration, wire a route to it, and publish a stage.
  name: AWS API Gateway Build an HTTP API
  slug: aws-api-gateway-build-http-api-workflow
- description: Create a WebSocket API, add an integration, and wire the $connect route to it.
  name: AWS API Gateway Build a WebSocket API
  slug: aws-api-gateway-build-websocket-api-workflow
- description: Create an API key, create a throttled and quota-limited usage plan, and confirm the plan was registered.
  name: AWS API Gateway Create an API Key and Usage Plan
  slug: aws-api-gateway-create-api-key-and-usage-plan-workflow
- description: Confirm an HTTP API, check for published stages, and delete the API when it is safe to remove.
  name: AWS API Gateway Decommission an HTTP API
  slug: aws-api-gateway-decommission-http-api-workflow
- description: Confirm an HTTP API, create a deployment, and publish it to a new stage bound to that deployment.
  name: AWS API Gateway Deploy an HTTP API to a New Stage
  slug: aws-api-gateway-deploy-http-api-stage-workflow
- description: Confirm a REST API, list its resources, and read the method configuration for a chosen resource and verb.
  name: AWS API Gateway Inspect a REST API Method
  slug: aws-api-gateway-inspect-rest-api-method-workflow
- description: Create a REST API with a key-protected method and branch into usage-plan setup when an API key is required.
  name: AWS API Gateway Provision a Metered REST API
  slug: aws-api-gateway-metered-rest-api-workflow
- description: Create a REST API, configure a method on its root resource, deploy it, and confirm the stage.
  name: AWS API Gateway Provision and Deploy a REST API
  slug: aws-api-gateway-provision-rest-api-workflow
- description: Confirm a REST API, review its existing deployments, and publish a fresh deployment to a stage.
  name: AWS API Gateway Redeploy a REST API Stage
  slug: aws-api-gateway-redeploy-rest-api-stage-workflow
- description: Create an HTTP API, attach an authorizer, and add a route that uses it.
  name: AWS API Gateway Secure an HTTP API with an Authorizer
  slug: aws-api-gateway-secure-http-api-authorizer-workflow
artifact_total: 224
asyncapis:
- description: AsyncAPI description of the *platform protocol* exposed by Amazon API Gateway WebSocket APIs. Customer-deployed WebSocket APIs are message-routed based on a route selection expression evaluated agains
  name: Amazon API Gateway WebSocket API Protocol
  slug: aws-api-gateway-asyncapi
collections:
- collection_type: postman
  name: Amazon API Gateway Management API
  slug: postman-aws-api-gateway-management
- collection_type: postman
  name: Amazon API Gateway V1 (REST)
  slug: postman-aws-api-gateway-v1
- collection_type: postman
  name: Amazon API Gateway V2 (HTTP and WebSocket)
  slug: postman-aws-api-gateway-v2
- collection_type: open
  name: Amazon API Gateway Management API
  slug: open-aws-api-gateway-management
- collection_type: open
  name: Amazon API Gateway V1 (REST)
  slug: open-aws-api-gateway-v1
- collection_type: open
  name: Amazon API Gateway V2 (HTTP and WebSocket)
  slug: open-aws-api-gateway-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-api-gateway-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-api-gateway-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-api-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-api-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-api-gateway-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-api-gateway/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-add-method-and-redeploy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-audit-http-api-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-build-http-api-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-build-websocket-api-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-create-api-key-and-usage-plan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-decommission-http-api-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-deploy-http-api-stage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-inspect-rest-api-method-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-metered-rest-api-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-provision-rest-api-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-redeploy-rest-api-stage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aws-api-gateway-secure-http-api-authorizer-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/api-gateway/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/apigateway/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/api-gateway/pricing/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html
- group: build
  title: AWS SDKs
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/apigateway/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/apigateway/latest/developerguide/history.html
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/category/compute/amazon-api-gateway/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/apigateway/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: build
  title: AWS Samples (121+ API Gateway sample repos)
  type: GitHubOrganization
  url: https://github.com/aws-samples
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-api-gateway
- group: design
  title: ''
  type: SpectralRules
  url: rules/aws-api-gateway-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aws-api-gateway-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/aws-api-gateway-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimitsArtifact
  url: rate-limits/aws-api-gateway-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aws-api-gateway-finops.yml
created: '2026-03-27'
description: Amazon API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale. It acts as the front door for applications to access backend services, supporting REST APIs, HTTP APIs, and WebSocket APIs with built-in traffic management, authorization, monitoring, and API version management. API Gateway integrates natively with AWS Lambda, CloudWatch, CloudFront, IAM, and Cognito, and (as of December 2025) can expose REST APIs as MCP-compatible tools for Amazon Bedrock AgentCore Gateway for agent-driven API consumption.
examples:
- key_count: 3
  name: Management Connection Example
  slug: management-connection-example
- key_count: 2
  name: Management Identity Example
  slug: management-identity-example
- key_count: 4
  name: V1 Api Key Example
  slug: v1-api-key-example
- key_count: 1
  name: V1 Api Keys Example
  slug: v1-api-keys-example
- key_count: 3
  name: V1 Create Api Key Request Example
  slug: v1-create-api-key-request-example
- key_count: 2
  name: V1 Create Deployment Request Example
  slug: v1-create-deployment-request-example
- key_count: 4
  name: V1 Create Rest Api Request Example
  slug: v1-create-rest-api-request-example
- key_count: 4
  name: V1 Create Usage Plan Request Example
  slug: v1-create-usage-plan-request-example
- key_count: 3
  name: V1 Deployment Example
  slug: v1-deployment-example
- key_count: 1
  name: V1 Deployments Example
  slug: v1-deployments-example
- key_count: 1
  name: V1 Endpoint Configuration Example
  slug: v1-endpoint-configuration-example
- key_count: 3
  name: V1 Method Example
  slug: v1-method-example
- key_count: 2
  name: V1 Put Method Request Example
  slug: v1-put-method-request-example
- key_count: 2
  name: V1 Quota Settings Example
  slug: v1-quota-settings-example
- key_count: 4
  name: V1 Resource Example
  slug: v1-resource-example
- key_count: 1
  name: V1 Resources Example
  slug: v1-resources-example
- key_count: 6
  name: V1 Rest Api Example
  slug: v1-rest-api-example
- key_count: 1
  name: V1 Rest Apis Example
  slug: v1-rest-apis-example
- key_count: 3
  name: V1 Stage Example
  slug: v1-stage-example
- key_count: 1
  name: V1 Stages Example
  slug: v1-stages-example
- key_count: 2
  name: V1 Throttle Settings Example
  slug: v1-throttle-settings-example
- key_count: 4
  name: V1 Usage Plan Example
  slug: v1-usage-plan-example
- key_count: 1
  name: V1 Usage Plans Example
  slug: v1-usage-plans-example
- key_count: 6
  name: V2 Api Example
  slug: v2-api-example
- key_count: 1
  name: V2 Apis Example
  slug: v2-apis-example
- key_count: 4
  name: V2 Authorizer Example
  slug: v2-authorizer-example
- key_count: 1
  name: V2 Authorizers Example
  slug: v2-authorizers-example
- key_count: 5
  name: V2 Create Api Request Example
  slug: v2-create-api-request-example
- key_count: 4
  name: V2 Create Authorizer Request Example
  slug: v2-create-authorizer-request-example
- key_count: 2
  name: V2 Create Deployment Request Example
  slug: v2-create-deployment-request-example
- key_count: 3
  name: V2 Create Integration Request Example
  slug: v2-create-integration-request-example
- key_count: 3
  name: V2 Create Route Request Example
  slug: v2-create-route-request-example
- key_count: 3
  name: V2 Create Stage Request Example
  slug: v2-create-stage-request-example
- key_count: 4
  name: V2 Deployment Example
  slug: v2-deployment-example
- key_count: 1
  name: V2 Deployments Example
  slug: v2-deployments-example
- key_count: 4
  name: V2 Integration Example
  slug: v2-integration-example
- key_count: 1
  name: V2 Integrations Example
  slug: v2-integrations-example
- key_count: 4
  name: V2 Route Example
  slug: v2-route-example
- key_count: 1
  name: V2 Routes Example
  slug: v2-routes-example
- key_count: 4
  name: V2 Stage Example
  slug: v2-stage-example
- key_count: 1
  name: V2 Stages Example
  slug: v2-stages-example
features:
- description: Create, deploy, and manage REST APIs with full lifecycle control including stages, deployments, and versioning.
  name: REST API Management
- description: Build lightweight HTTP APIs optimized for serverless workloads at up to 71% lower cost than REST APIs.
  name: HTTP API Support
- description: Enable real-time bidirectional communication for chat platforms, streaming dashboards, and live applications.
  name: WebSocket APIs
- description: Handle hundreds of thousands of concurrent API calls with built-in throttling and request validation.
  name: Traffic Management
- description: Supports IAM policies, Lambda authorizers, Amazon Cognito user pools, and OAuth2/OIDC for API access control.
  name: Authorization and Security
- description: Integration with CloudWatch metrics, access logging, and CloudTrail for full API observability.
  name: Monitoring and Logging
- description: Map APIs to branded custom domains with TLS certificates managed through AWS Certificate Manager.
  name: Custom Domain Names
- description: Safely roll out API changes using canary deployment stages with configurable traffic splitting.
  name: Canary Releases
- description: Protect APIs against common web exploits and DDoS attacks using AWS Web Application Firewall.
  name: AWS WAF Integration
- description: Automatically generate client SDKs for deployed APIs in multiple programming languages.
  name: SDK Generation
- description: Reduce backend load and improve response times with configurable response caching at the stage level.
  name: API Caching
- description: Leverage Amazon CloudFront edge locations for global low-latency API distribution.
  name: CloudFront Edge Distribution
- description: Expose REST API stages as Model Context Protocol (MCP) tools for AI agents via Bedrock AgentCore Gateway. AgentCore translates incoming MCP requests into HTTP requests, supports tools/list and tools/call methods, and accepts API_KEY, NO_AUTH, or GATEWAY_IAM_ROLE outbound auth. Launched December 2, 2025.
  name: Bedrock AgentCore Gateway MCP Target
- description: Native API Gateway Portals (launched November 19, 2025) let you publish PortalProducts containing REST APIs and per-endpoint documentation. Portals can be shared across AWS accounts and access-controlled via Cognito user pools.
  name: Developer Portals
- description: REST APIs can progressively stream response payloads to clients as they become available (launched November 19, 2025), enabling long-running and incremental response patterns.
  name: REST API Response Streaming
- description: REST APIs support private integrations with Application Load Balancers (launched November 21, 2025), expanding private integration options beyond NLB and AWS Cloud Map.
  name: Private Integration with Application Load Balancer
- description: REST APIs now support AWS Signature Version 4a (launched August 19, 2025), enabling multi-Region signing for cross-Region API invocations.
  name: SIGv4a Authentication for REST APIs
- description: Configurable TLS security policies for REST APIs and custom domain names (launched November 19, 2025) allow tighter control over accepted protocols and ciphers.
  name: Enhanced TLS Security Policies
- description: REST, HTTP, and WebSocket APIs and custom domain names support dual-stack endpoints (launched March 28, 2025).
  name: Dual-Stack IPv4/IPv6 Endpoints
finops:
- name: Aws Api Gateway Finops
  service_category: API Management / Serverless
  slug: aws-api-gateway-finops
graphqls:
- description: ''
  name: Amazon API Gateway GraphQL API
  slug: aws-api-gateway-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-api-gateway.png
json_schemas:
- name: Connection
  property_count: 3
  slug: management-connection
- name: Identity
  property_count: 2
  slug: management-identity
- name: ApiKey
  property_count: 4
  slug: v1-api-key
- name: ApiKeys
  property_count: 1
  slug: v1-api-keys
- name: CreateApiKeyRequest
  property_count: 3
  slug: v1-create-api-key-request
- name: CreateDeploymentRequest
  property_count: 2
  slug: v1-create-deployment-request
- name: CreateRestApiRequest
  property_count: 4
  slug: v1-create-rest-api-request
- name: CreateUsagePlanRequest
  property_count: 4
  slug: v1-create-usage-plan-request
- name: Deployment
  property_count: 3
  slug: v1-deployment
- name: Deployments
  property_count: 1
  slug: v1-deployments
- name: EndpointConfiguration
  property_count: 1
  slug: v1-endpoint-configuration
- name: Method
  property_count: 3
  slug: v1-method
- name: PutMethodRequest
  property_count: 2
  slug: v1-put-method-request
- name: QuotaSettings
  property_count: 2
  slug: v1-quota-settings
- name: Resource
  property_count: 4
  slug: v1-resource
- name: Resources
  property_count: 1
  slug: v1-resources
- name: RestApi
  property_count: 6
  slug: v1-rest-api
- name: RestApis
  property_count: 1
  slug: v1-rest-apis
- name: Stage
  property_count: 3
  slug: v1-stage
- name: Stages
  property_count: 1
  slug: v1-stages
- name: ThrottleSettings
  property_count: 2
  slug: v1-throttle-settings
- name: UsagePlan
  property_count: 4
  slug: v1-usage-plan
- name: UsagePlans
  property_count: 1
  slug: v1-usage-plans
- name: Api
  property_count: 6
  slug: v2-api
- name: Apis
  property_count: 1
  slug: v2-apis
- name: Authorizer
  property_count: 4
  slug: v2-authorizer
- name: Authorizers
  property_count: 1
  slug: v2-authorizers
- name: CreateApiRequest
  property_count: 5
  slug: v2-create-api-request
- name: CreateAuthorizerRequest
  property_count: 4
  slug: v2-create-authorizer-request
- name: CreateDeploymentRequest
  property_count: 2
  slug: v2-create-deployment-request
- name: CreateIntegrationRequest
  property_count: 3
  slug: v2-create-integration-request
- name: CreateRouteRequest
  property_count: 3
  slug: v2-create-route-request
- name: CreateStageRequest
  property_count: 3
  slug: v2-create-stage-request
- name: Deployment
  property_count: 4
  slug: v2-deployment
- name: Deployments
  property_count: 1
  slug: v2-deployments
- name: Integration
  property_count: 4
  slug: v2-integration
- name: Integrations
  property_count: 1
  slug: v2-integrations
- name: Route
  property_count: 4
  slug: v2-route
- name: Routes
  property_count: 1
  slug: v2-routes
- name: Stage
  property_count: 4
  slug: v2-stage
- name: Stages
  property_count: 1
  slug: v2-stages
json_structures:
- name: Management Connection Structure
  property_count: 3
  slug: management-connection-structure
- name: Management Identity Structure
  property_count: 2
  slug: management-identity-structure
- name: V1 Api Key Structure
  property_count: 4
  slug: v1-api-key-structure
- name: V1 Api Keys Structure
  property_count: 1
  slug: v1-api-keys-structure
- name: V1 Create Api Key Request Structure
  property_count: 3
  slug: v1-create-api-key-request-structure
- name: V1 Create Deployment Request Structure
  property_count: 2
  slug: v1-create-deployment-request-structure
- name: V1 Create Rest Api Request Structure
  property_count: 4
  slug: v1-create-rest-api-request-structure
- name: V1 Create Usage Plan Request Structure
  property_count: 4
  slug: v1-create-usage-plan-request-structure
- name: V1 Deployment Structure
  property_count: 3
  slug: v1-deployment-structure
- name: V1 Deployments Structure
  property_count: 1
  slug: v1-deployments-structure
- name: V1 Endpoint Configuration Structure
  property_count: 1
  slug: v1-endpoint-configuration-structure
- name: V1 Method Structure
  property_count: 3
  slug: v1-method-structure
- name: V1 Put Method Request Structure
  property_count: 2
  slug: v1-put-method-request-structure
- name: V1 Quota Settings Structure
  property_count: 2
  slug: v1-quota-settings-structure
- name: V1 Resource Structure
  property_count: 4
  slug: v1-resource-structure
- name: V1 Resources Structure
  property_count: 1
  slug: v1-resources-structure
- name: V1 Rest Api Structure
  property_count: 6
  slug: v1-rest-api-structure
- name: V1 Rest Apis Structure
  property_count: 1
  slug: v1-rest-apis-structure
- name: V1 Stage Structure
  property_count: 3
  slug: v1-stage-structure
- name: V1 Stages Structure
  property_count: 1
  slug: v1-stages-structure
- name: V1 Throttle Settings Structure
  property_count: 2
  slug: v1-throttle-settings-structure
- name: V1 Usage Plan Structure
  property_count: 4
  slug: v1-usage-plan-structure
- name: V1 Usage Plans Structure
  property_count: 1
  slug: v1-usage-plans-structure
- name: V2 Api Structure
  property_count: 6
  slug: v2-api-structure
- name: V2 Apis Structure
  property_count: 1
  slug: v2-apis-structure
- name: V2 Authorizer Structure
  property_count: 4
  slug: v2-authorizer-structure
- name: V2 Authorizers Structure
  property_count: 1
  slug: v2-authorizers-structure
- name: V2 Create Api Request Structure
  property_count: 5
  slug: v2-create-api-request-structure
- name: V2 Create Authorizer Request Structure
  property_count: 4
  slug: v2-create-authorizer-request-structure
- name: V2 Create Deployment Request Structure
  property_count: 2
  slug: v2-create-deployment-request-structure
- name: V2 Create Integration Request Structure
  property_count: 3
  slug: v2-create-integration-request-structure
- name: V2 Create Route Request Structure
  property_count: 3
  slug: v2-create-route-request-structure
- name: V2 Create Stage Request Structure
  property_count: 3
  slug: v2-create-stage-request-structure
- name: V2 Deployment Structure
  property_count: 4
  slug: v2-deployment-structure
- name: V2 Deployments Structure
  property_count: 1
  slug: v2-deployments-structure
- name: V2 Integration Structure
  property_count: 4
  slug: v2-integration-structure
- name: V2 Integrations Structure
  property_count: 1
  slug: v2-integrations-structure
- name: V2 Route Structure
  property_count: 4
  slug: v2-route-structure
- name: V2 Routes Structure
  property_count: 1
  slug: v2-routes-structure
- name: V2 Stage Structure
  property_count: 4
  slug: v2-stage-structure
- name: V2 Stages Structure
  property_count: 1
  slug: v2-stages-structure
jsonld:
- class_count: 1
  name: Aws Api Gateway Management Connection Context
  property_count: 5
  slug: aws-api-gateway-management-connection-context
- class_count: 1
  name: Aws Api Gateway Management Identity Context
  property_count: 2
  slug: aws-api-gateway-management-identity-context
- class_count: 3
  name: Aws Api Gateway V1 Api Context
  property_count: 4
  slug: aws-api-gateway-v1-api-context
- class_count: 7
  name: Aws Api Gateway V1 Create Context
  property_count: 10
  slug: aws-api-gateway-v1-create-context
- class_count: 2
  name: Aws Api Gateway V1 Deployment Context
  property_count: 2
  slug: aws-api-gateway-v1-deployment-context
- class_count: 1
  name: Aws Api Gateway V1 Deployments Context
  property_count: 1
  slug: aws-api-gateway-v1-deployments-context
- class_count: 1
  name: Aws Api Gateway V1 Endpoint Context
  property_count: 1
  slug: aws-api-gateway-v1-endpoint-context
- class_count: 1
  name: Aws Api Gateway V1 Method Context
  property_count: 3
  slug: aws-api-gateway-v1-method-context
- class_count: 1
  name: Aws Api Gateway V1 Put Context
  property_count: 2
  slug: aws-api-gateway-v1-put-context
- class_count: 1
  name: Aws Api Gateway V1 Quota Context
  property_count: 2
  slug: aws-api-gateway-v1-quota-context
- class_count: 1
  name: Aws Api Gateway V1 Resource Context
  property_count: 4
  slug: aws-api-gateway-v1-resource-context
- class_count: 1
  name: Aws Api Gateway V1 Resources Context
  property_count: 1
  slug: aws-api-gateway-v1-resources-context
- class_count: 5
  name: Aws Api Gateway V1 Rest Context
  property_count: 5
  slug: aws-api-gateway-v1-rest-context
- class_count: 2
  name: Aws Api Gateway V1 Stage Context
  property_count: 2
  slug: aws-api-gateway-v1-stage-context
- class_count: 1
  name: Aws Api Gateway V1 Stages Context
  property_count: 1
  slug: aws-api-gateway-v1-stages-context
- class_count: 1
  name: Aws Api Gateway V1 Throttle Context
  property_count: 2
  slug: aws-api-gateway-v1-throttle-context
- class_count: 3
  name: Aws Api Gateway V1 Usage Context
  property_count: 8
  slug: aws-api-gateway-v1-usage-context
- class_count: 1
  name: Aws Api Gateway V2 Api Context
  property_count: 6
  slug: aws-api-gateway-v2-api-context
- class_count: 1
  name: Aws Api Gateway V2 Apis Context
  property_count: 1
  slug: aws-api-gateway-v2-apis-context
- class_count: 1
  name: Aws Api Gateway V2 Authorizer Context
  property_count: 4
  slug: aws-api-gateway-v2-authorizer-context
- class_count: 1
  name: Aws Api Gateway V2 Authorizers Context
  property_count: 1
  slug: aws-api-gateway-v2-authorizers-context
- class_count: 6
  name: Aws Api Gateway V2 Create Context
  property_count: 16
  slug: aws-api-gateway-v2-create-context
- class_count: 1
  name: Aws Api Gateway V2 Deployment Context
  property_count: 4
  slug: aws-api-gateway-v2-deployment-context
- class_count: 1
  name: Aws Api Gateway V2 Deployments Context
  property_count: 1
  slug: aws-api-gateway-v2-deployments-context
- class_count: 1
  name: Aws Api Gateway V2 Integration Context
  property_count: 4
  slug: aws-api-gateway-v2-integration-context
- class_count: 1
  name: Aws Api Gateway V2 Integrations Context
  property_count: 1
  slug: aws-api-gateway-v2-integrations-context
- class_count: 1
  name: Aws Api Gateway V2 Route Context
  property_count: 4
  slug: aws-api-gateway-v2-route-context
- class_count: 1
  name: Aws Api Gateway V2 Routes Context
  property_count: 1
  slug: aws-api-gateway-v2-routes-context
- class_count: 1
  name: Aws Api Gateway V2 Stage Context
  property_count: 4
  slug: aws-api-gateway-v2-stage-context
- class_count: 1
  name: Aws Api Gateway V2 Stages Context
  property_count: 1
  slug: aws-api-gateway-v2-stages-context
layout: provider
modified: '2026-05-29'
name: Amazon API Gateway
nav: Providers
network: true
overview: 'Amazon API Gateway publishes 12 APIs on the [APIs.io](https://apis.io/) network, including ApiKeys API, Apis API, Authorizers API, and 9 more. Tagged areas include API Gateway, Cloud, REST, HTTP, and WebSocket.


  The Amazon API Gateway catalog on APIs.io includes 1 event-driven AsyncAPI specification, 30 JSON-LD contexts, and 3 Spectral governance rulesets.


  Amazon API Gateway''s developer surface includes authentication, documentation, getting-started guide, pricing, CLI, changelog, support, and 33 more developer resources.'
plans:
- name: Aws Api Gateway Plans Pricing
  plan_count: 6
  slug: aws-api-gateway-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 12
  name: Aws Api Gateway Rate Limits
  slug: aws-api-gateway-rate-limits
rules:
- name: Amazon API Gateway API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: aws-api-gateway-asyncapi-spectral-rules
- name: Amazon API Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aws-api-gateway-jsonschema-spectral-rules
- name: Amazon API Gateway API Rules
  rule_count: 40
  severity_counts:
    error: 17
    hint: 0
    info: 2
    warn: 21
  slug: aws-api-gateway-spectral-rules
score:
  band: exemplar
  composite: 75.1
  delta: 2.5
  facets:
    commercial_clarity: 78.9
    contract_quality: 80.8
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 68.4
  previous_composite: 72.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/screenshots/aws-api-gateway-2026-06-20T172738.png
security:
- kind: authentication
  name: Aws Api Gateway Authentication
  slug: aws-api-gateway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Api Gateway Domain Security
  slug: aws-api-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Api Gateway Vulnerability Disclosure
  slug: aws-api-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Api Gateway Trust Center
  slug: aws-api-gateway-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-api-gateway
tags:
- API Gateway
- Cloud
- REST
- HTTP
- WebSocket
- Serverless
- MCP
- AgentCore
- Developer Portal
use_cases:
- description: Build fully serverless APIs with API Gateway as the front door and AWS Lambda as the backend compute layer.
  name: Serverless API Backend
- description: Consolidate access to multiple microservices behind a single API endpoint with routing and load balancing.
  name: Microservices Gateway
- description: Enable chat apps, collaborative tools, and live dashboards using WebSocket APIs for persistent bidirectional connections.
  name: Real-Time Applications
- description: Create secure, scalable REST and HTTP APIs for mobile and web front-ends with Cognito authentication.
  name: Mobile and Web Application APIs
- description: Expose existing on-premises or EC2-hosted services as modern REST APIs without rewriting backend logic.
  name: Legacy API Modernization
- description: Aggregate and normalize third-party APIs behind a consistent API surface with transformation and mapping.
  name: Third-Party API Integration
- description: Expose REST APIs as MCP-compatible tool catalogs via Bedrock AgentCore Gateway so AI agents can list and invoke operations without bespoke client code.
  name: MCP Tool Server for AI Agents
- description: Use native API Gateway Portals to publish partner-facing REST APIs with branded documentation, Cognito-gated access, and self-service key issuance.
  name: Developer Portal for Partner APIs
website: https://aws.amazon.com/api-gateway/
---
