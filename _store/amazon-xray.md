---
aid: amazon-xray
name: Amazon X-Ray
description: AWS X-Ray is a distributed tracing service that helps developers analyze and debug production applications, providing end-to-end visibility into requests as they travel through the application. X-Ray provides service maps, trace analysis, sampling rules, group filtering, and AI-powered insights for identifying performance bottlenecks and errors across microservices and serverless architectures.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/amazon-xray/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
type: Index
tags:
  - Application Performance
  - AWS
  - Debugging
  - Distributed Tracing
  - Monitoring
  - Observability
apis:
  - aid: amazon-xray:amazon-xray-rest-api
    name: Amazon X-Ray REST API
    description: RESTful API for AWS X-Ray distributed tracing operations including trace retrieval, service map generation, sampling rule management, group management, and insights analysis for application performance monitoring. 30 operations for traces, service graphs, sampling, groups, and insights.
    humanURL: https://aws.amazon.com/xray/
    baseURL: https://xray.amazonaws.com
    tags:
      - AWS
      - Distributed Tracing
      - Observability
      - Tracing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/xray/latest/api/
      - type: OpenAPI
        url: openapi/amazon-xray-openapi-original.yaml
      - type: JSONSchema
        url: json-schema/xray-trace-summary-schema.json
      - type: JSONLD
        url: json-ld/amazon-xray-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/xray/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/xray/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/xray/latest/api/CommonParameters.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: StatusPage
        url: https://status.aws.amazon.com/
      - type: FAQ
        url: https://aws.amazon.com/xray/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/xray/latest/api/Welcome.html
      - type: CodeExamples
        url: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-sample.html
      - type: Security
        url: https://docs.aws.amazon.com/xray/latest/devguide/security.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/xray/
  - type: Documentation
    url: https://docs.aws.amazon.com/xray/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/developer/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/xray/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-xray
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-xray-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-xray-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/distributed-tracing.yaml
  - type: Features
    data:
      - name: End-to-End Distributed Tracing
        description: Trace requests as they travel across services, microservices, and serverless functions to identify bottlenecks and errors.
      - name: Service Map Visualization
        description: Automatically generate visual service maps showing all connected services and their health status and latency.
      - name: Trace Filtering and Groups
        description: Create groups with filter expressions to organize and analyze subsets of traces based on service names, URLs, or annotations.
      - name: Adaptive Sampling
        description: Configurable sampling rules to control the percentage of requests traced, balancing coverage with cost.
      - name: X-Ray Insights
        description: AI-powered automatic detection of anomalies and performance issues with root cause analysis across the service map.
      - name: AWS Service Integration
        description: Native tracing support across Lambda, EC2, ECS, EKS, API Gateway, SNS, SQS, and 200+ other AWS services.
      - name: SDK and Agent Support
        description: X-Ray SDKs for Java, Node.js, Python, Go, Ruby, and .NET for custom application instrumentation.
      - name: CloudWatch Integration
        description: Deep integration with Amazon CloudWatch for correlating traces with metrics, logs, and alarms.
  - type: UseCases
    data:
      - name: Microservices Debugging
        description: Trace requests across microservices to identify which service is causing latency or errors in distributed applications.
      - name: Serverless Application Monitoring
        description: Monitor Lambda function execution chains and identify cold start impacts and downstream service bottlenecks.
      - name: Performance Optimization
        description: Use trace data and service maps to identify and eliminate performance bottlenecks in production applications.
      - name: Root Cause Analysis
        description: Drill into traces to understand the exact call chain that caused an error or latency spike.
      - name: SLA Compliance Monitoring
        description: Track end-to-end latency and error rates across services to ensure application SLAs are being met.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Automatic tracing of Lambda function invocations and downstream calls.
      - name: Amazon API Gateway
        description: Native tracing of API Gateway requests through backend services.
      - name: Amazon CloudWatch
        description: Correlation of traces with CloudWatch metrics, logs, and alarms.
      - name: AWS App Mesh
        description: Service mesh integration for automatic tracing of Envoy-based microservices.
      - name: OpenTelemetry
        description: X-Ray supports the OpenTelemetry standard via the AWS Distro for OpenTelemetry.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
