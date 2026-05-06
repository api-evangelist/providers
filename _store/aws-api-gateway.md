---
aid: aws-api-gateway
name: Amazon API Gateway
description: Amazon API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale. It acts as the front door for applications to access backend services, supporting REST APIs, HTTP APIs, and WebSocket APIs with built-in traffic management, authorization, monitoring, and API version management. API Gateway integrates natively with AWS Lambda, CloudWatch, CloudFront, IAM, and Cognito for comprehensive serverless and secure API deployment.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - AWS
  - Cloud
  - REST
  - WebSocket
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-api-gateway:aws-api-gateway-v1
    name: Amazon API Gateway V1 (REST)
    description: The API Gateway V1 control plane API is used to create, deploy, and manage REST APIs in Amazon API Gateway. It exposes resources for RestApis, Resources, Methods, Stages, Deployments, Authorizers, API keys, usage plans, and related configuration.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
    baseURL: https://apigateway.{region}.amazonaws.com
    tags:
      - API Gateway
      - AWS
      - REST
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/apigateway/latest/api/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html
      - type: Authentication
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html
      - type: OpenAPI
        url: openapi/aws-api-gateway-v1-openapi.yml
  - aid: aws-api-gateway:aws-api-gateway-v2
    name: Amazon API Gateway V2 (HTTP and WebSocket)
    description: The API Gateway V2 control plane API is used to create, deploy, and manage HTTP APIs and WebSocket APIs in Amazon API Gateway. It provides resources for Apis, Routes, Integrations, Stages, Deployments, and Authorizers for the newer HTTP and WebSocket API types.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
    baseURL: https://apigateway.{region}.amazonaws.com
    tags:
      - API Gateway
      - AWS
      - HTTP
      - WebSocket
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
      - type: APIReference
        url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html
      - type: Documentation
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html
        title: WebSocket API Guide
      - type: OpenAPI
        url: openapi/aws-api-gateway-v2-openapi.yml
  - aid: aws-api-gateway:aws-api-gateway-management
    name: Amazon API Gateway Management API
    description: The API Gateway Management API allows backend services to send messages to connected clients of a deployed WebSocket API and to disconnect clients. Requests are made against the deployed stage's callback URL.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/apigatewaymanagementapi/latest/reference/Welcome.html
    baseURL: https://{api-id}.execute-api.{region}.amazonaws.com/{stage}
    tags:
      - API Gateway
      - AWS
      - Callback
      - WebSocket
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html
      - type: APIReference
        url: https://docs.aws.amazon.com/apigatewaymanagementapi/latest/reference/Welcome.html
      - type: OpenAPI
        url: openapi/aws-api-gateway-management-openapi.yml
common:
  - type: Website
    url: https://aws.amazon.com/api-gateway/
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/
  - type: GettingStarted
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html
  - type: Pricing
    url: https://aws.amazon.com/api-gateway/pricing/
  - type: RateLimits
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html
  - type: SDK
    url: https://aws.amazon.com/tools/
    title: AWS SDKs
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/apigateway/
  - type: ChangeLog
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/history.html
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/category/compute/amazon-api-gateway/
  - type: Console
    url: https://console.aws.amazon.com/apigateway/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-api-gateway
  - type: SpectralRules
    url: rules/aws-api-gateway-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-api-gateway-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/api-management-workflow.yaml
  - type: Features
    data:
      - name: REST API Management
        description: Create, deploy, and manage REST APIs with full lifecycle control including stages, deployments, and versioning.
      - name: HTTP API Support
        description: Build lightweight HTTP APIs optimized for serverless workloads at up to 71% lower cost than REST APIs.
      - name: WebSocket APIs
        description: Enable real-time bidirectional communication for chat platforms, streaming dashboards, and live applications.
      - name: Traffic Management
        description: Handle hundreds of thousands of concurrent API calls with built-in throttling and request validation.
      - name: Authorization and Security
        description: Supports IAM policies, Lambda authorizers, Amazon Cognito user pools, and OAuth2/OIDC for API access control.
      - name: Monitoring and Logging
        description: Integration with CloudWatch metrics, access logging, and CloudTrail for full API observability.
      - name: Custom Domain Names
        description: Map APIs to branded custom domains with TLS certificates managed through AWS Certificate Manager.
      - name: Canary Releases
        description: Safely roll out API changes using canary deployment stages with configurable traffic splitting.
      - name: AWS WAF Integration
        description: Protect APIs against common web exploits and DDoS attacks using AWS Web Application Firewall.
      - name: SDK Generation
        description: Automatically generate client SDKs for deployed APIs in multiple programming languages.
      - name: API Caching
        description: Reduce backend load and improve response times with configurable response caching at the stage level.
      - name: CloudFront Edge Distribution
        description: Leverage Amazon CloudFront edge locations for global low-latency API distribution.
  - type: UseCases
    data:
      - name: Serverless API Backend
        description: Build fully serverless APIs with API Gateway as the front door and AWS Lambda as the backend compute layer.
      - name: Microservices Gateway
        description: Consolidate access to multiple microservices behind a single API endpoint with routing and load balancing.
      - name: Real-Time Applications
        description: Enable chat apps, collaborative tools, and live dashboards using WebSocket APIs for persistent bidirectional connections.
      - name: Mobile and Web Application APIs
        description: Create secure, scalable REST and HTTP APIs for mobile and web front-ends with Cognito authentication.
      - name: Legacy API Modernization
        description: Expose existing on-premises or EC2-hosted services as modern REST APIs without rewriting backend logic.
      - name: Third-Party API Integration
        description: Aggregate and normalize third-party APIs behind a consistent API surface with transformation and mapping.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Invoke Lambda functions as API backends for fully serverless request handling.
      - name: Amazon Cognito
        description: Authenticate and authorize API requests using Cognito user pools and identity pools.
      - name: Amazon CloudWatch
        description: Monitor API performance metrics, error rates, and latency with CloudWatch dashboards and alarms.
      - name: AWS CloudTrail
        description: Audit all API Gateway management API calls for compliance and security monitoring.
      - name: Amazon CloudFront
        description: Distribute APIs globally through CloudFront edge locations for reduced latency.
      - name: AWS WAF
        description: Apply web application firewall rules to protect APIs from malicious traffic.
      - name: AWS X-Ray
        description: Trace requests end-to-end through API Gateway and backend services for performance analysis.
      - name: AWS IAM
        description: Control API access using IAM policies and resource-based policies for fine-grained authorization.
      - name: AWS Certificate Manager
        description: Provision and manage TLS certificates for custom domain names on API Gateway.
      - name: Amazon VPC
        description: Create private APIs accessible only within a VPC using VPC endpoint integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
