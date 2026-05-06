---
aid: amazon-fault-injection-simulator
name: Amazon Fault Injection Simulator
description: AWS Fault Injection Simulator (FIS) is a fully managed service for running fault injection experiments on AWS. It allows you to improve an application's performance, observability, and resiliency by identifying and fixing weaknesses through controlled chaos engineering experiments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Chaos Engineering
  - DevOps
  - Fault Injection
  - Resilience Testing
url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-fault-injection-simulator:aws-fis-api
    name: AWS Fault Injection Simulator API
    description: The AWS Fault Injection Simulator API provides programmatic access to create and manage experiment templates, experiments, and actions for conducting chaos engineering experiments on AWS workloads.
    humanURL: https://aws.amazon.com/fis/
    baseURL: https://fis.amazonaws.com
    tags:
      - Chaos Engineering
      - Fault Injection
      - Resilience Testing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/fis/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-fis-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-fis-experiment-template-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fis-experiment-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fis-action-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fis-safety-lever-schema.json
      - type: JSONStructure
        url: json-structure/amazon-fis-experiment-template-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fis-experiment-structure.json
      - type: Example
        url: examples/amazon-fis-experiment-template-example.json
      - type: Example
        url: examples/amazon-fis-experiment-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/fis/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/fis/pricing/
      - type: FAQ
        url: https://aws.amazon.com/fis/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/fis/latest/APIReference/Welcome.html
common:
  - type: Portal
    url: https://aws.amazon.com/fis/
  - type: Website
    url: https://aws.amazon.com/fis/
  - type: Documentation
    url: https://docs.aws.amazon.com/fis/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/devops/tag/aws-fault-injection-simulator/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/fis/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-fis
  - type: SpectralRules
    url: rules/amazon-fis-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/fis.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-fis-chaos-engineering.yaml
  - type: Vocabulary
    url: vocabulary/amazon-fis-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-fis-context.jsonld
  - type: Features
    data:
      - name: Managed Fault Injection
        description: Fully managed service requiring no agent installation with pre-built fault injection actions for EC2, RDS, ECS, EKS, and more.
      - name: Pre-built Scenarios
        description: Ready-to-use resilience scenarios for AZ failures, power interruptions, network disruptions, and cross-region connectivity issues.
      - name: Safety Controls
        description: CloudWatch alarm-based stop conditions and safety levers prevent unintended impact during live testing.
      - name: Fine-grained Targeting
        description: Tag-based resource targeting scopes experiments to specific environments, applications, or resource subsets.
      - name: Multi-account Support
        description: Run experiments across multiple AWS accounts using target account configurations.
      - name: CI/CD Integration
        description: API and CLI access enables automated resilience testing in deployment pipelines.
      - name: Real-time Visibility
        description: Console and API provide real-time status of executing actions, affected resources, and triggered stop conditions.
      - name: IAM Security
        description: Fine-grained IAM controls restrict which users can create, run, or view experiments and affected resources.
  - type: UseCases
    data:
      - name: Application Resilience Testing
        description: Validate application behavior under resource failures before they occur in production.
      - name: Chaos Engineering
        description: Run structured fault injection experiments following chaos engineering principles.
      - name: Observability Validation
        description: Verify that monitoring and alerting systems detect and respond to failures correctly.
      - name: Game Days
        description: Conduct planned game day exercises simulating failure scenarios for team readiness.
      - name: Automated Pipeline Testing
        description: Integrate resilience testing into CI/CD pipelines for continuous validation.
      - name: Multi-region Failover Testing
        description: Test cross-region failover mechanisms and recovery time objectives.
  - type: Integrations
    data:
      - name: Amazon CloudWatch
        description: Stop conditions use CloudWatch alarms to automatically halt experiments.
      - name: AWS IAM
        description: Task execution roles define which AWS resources experiments can affect.
      - name: Amazon EC2
        description: Stop instances, terminate instances, and inject CPU/memory stress on EC2.
      - name: Amazon ECS
        description: Stop ECS tasks and inject faults into containerized workloads.
      - name: Amazon EKS
        description: Terminate Kubernetes nodes and pods running on EKS.
      - name: Amazon RDS
        description: Trigger RDS failovers, reboot instances, and pause cluster I/O.
      - name: AWS Lambda
        description: Inject latency and errors into Lambda function invocations.
      - name: Amazon DynamoDB
        description: Pause DynamoDB replication between replicas.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
