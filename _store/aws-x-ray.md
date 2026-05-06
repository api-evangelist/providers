---
aid: aws-x-ray
name: AWS X-Ray
description: AWS X-Ray is a service that helps developers analyze and debug distributed applications by providing end-to-end tracing of requests as they travel through the application, identifying performance bottlenecks and errors. It is now part of Amazon CloudWatch Application Signals for unified observability.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Debugging
  - Distributed Tracing
  - Microservices
  - Observability
url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-x-ray:aws-x-ray
    name: AWS X-Ray
    description: AWS X-Ray is a service that helps developers analyze and debug distributed applications by providing end-to-end tracing of requests as they travel through the application, identifying performance bottlenecks and errors. It is now part of Amazon CloudWatch Application Signals for unified observability.
    humanURL: https://aws.amazon.com/xray/
    baseURL: https://xray.{region}.amazonaws.com
    tags:
      - AWS
      - Debugging
      - Distributed Tracing
      - Microservices
      - Observability
    properties:
      - type: OpenAPI
        url: openapi/aws-x-ray-openapi.yml
      - type: JSONSchema
        url: json-schema/aws-x-ray-trace-segment.yml
      - type: Documentation
        url: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html
      - type: APIReference
        url: https://docs.aws.amazon.com/xray/latest/api/Welcome.html
common:
  - type: Website
    url: https://aws.amazon.com/xray/
  - type: Documentation
    url: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html
  - type: GettingStarted
    url: https://aws.amazon.com/xray/getting-started/
  - type: Pricing
    url: https://aws.amazon.com/xray/pricing/
  - type: FAQ
    url: https://aws.amazon.com/xray/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/devops/category/management-tools/aws-x-ray/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SpectralRules
    url: rules/aws-x-ray-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-x-ray-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/distributed-tracing-workflow.yaml
  - type: Features
    data:
      - name: End-to-End Tracing
        description: Trace requests from client to backend across all services in your distributed application.
      - name: Service Map
        description: Visualize service dependencies and real-time health indicators in an interactive map.
      - name: Trace Analytics
        description: Filter, search, and analyze traces using filter expressions and groups.
      - name: Sampling Rules
        description: Control trace collection rates with dynamic sampling rules to manage cost and volume.
      - name: Annotations and Metadata
        description: Add indexed annotations and non-indexed metadata to traces for custom filtering and context.
      - name: Error Analysis
        description: Identify and analyze errors, faults, and throttling across distributed services.
      - name: Latency Analysis
        description: Identify performance bottlenecks with detailed latency histograms and percentile data.
      - name: CloudWatch Integration
        description: Integrated with CloudWatch Application Signals for unified observability and alerting.
      - name: SDK Support
        description: Instrument applications with X-Ray SDKs for Java, Python, Go, Node.js, Ruby, and .NET.
  - type: UseCases
    data:
      - name: Performance Optimization
        description: Identify and resolve latency bottlenecks in distributed microservices applications.
      - name: Error Debugging
        description: Trace errors and exceptions to their root cause across service boundaries.
      - name: Dependency Analysis
        description: Understand service dependencies and the impact of downstream failures.
      - name: SLA Monitoring
        description: Monitor request latency and error rates against service level agreements.
      - name: Microservices Visibility
        description: Gain observability into complex microservices architectures and their interactions.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Automatically instrument Lambda functions with X-Ray active tracing.
      - name: Amazon API Gateway
        description: Enable X-Ray tracing on API Gateway stages for end-to-end visibility.
      - name: Amazon ECS
        description: Collect traces from containerized applications running on ECS.
      - name: AWS Elastic Beanstalk
        description: Enable X-Ray on Elastic Beanstalk environments for application tracing.
      - name: Amazon CloudWatch
        description: Unified observability with CloudWatch Application Signals and alarms.
      - name: AWS Step Functions
        description: Trace state machine executions through Step Functions workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
