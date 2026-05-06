---
name: Amazon Serverless Application Repository
description: The AWS Serverless Application Repository enables teams, organizations, and individual developers to find, deploy, and publish serverless applications. It enables you to quickly deploy code samples, components, and complete applications for common use cases such as web and mobile backends, data processing, and IoT applications using AWS SAM templates.
url: https://aws.amazon.com/serverless/serverlessrepo/
baseURL: https://serverlessrepo.amazonaws.com
x-type: company
created: '2026-03-16'
modified: '2026-04-19'
tags:
  - Application Repository
  - AWS
  - Lambda
  - SAM
  - Serverless
apis:
  - name: AWS Serverless Application Repository API
    description: The AWS Serverless Application Repository API provides programmatic access to create and manage serverless applications, application versions, and deployment configurations for publishing and sharing SAM applications.
    humanURL: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/appendix-api-reference.html
    baseURL: https://serverlessrepo.{region}.amazonaws.com
    tags:
      - Application Repository
      - Lambda
      - Serverless
      - SAM
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/appendix-api-reference.html
      - type: OpenAPI
        url: openapi/amazon-serverless-application-repository-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-serverless-application-repository-application-schema.json
      - type: JSONSchema
        url: json-schema/amazon-serverless-application-repository-version-summary-schema.json
common:
  - type: Portal
    url: https://aws.amazon.com/serverless/serverlessrepo/
  - type: GettingStarted
    url: https://aws.amazon.com/serverless/serverlessrepo/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/serverlessrepo/
  - type: APIReference
    url: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/appendix-api-reference.html
  - type: Console
    url: https://console.aws.amazon.com/serverlessrepo/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Pricing
    url: https://aws.amazon.com/serverless/serverlessrepo/pricing/
  - type: FAQ
    url: https://aws.amazon.com/serverless/serverlessrepo/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/tag/serverless-application-repository/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/serverless-application-repository
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: SpectralRules
    url: rules/amazon-serverless-application-repository-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-serverless-application-repository-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/serverless-app-management.yaml
  - type: Features
    data:
      - name: One-Click Deployment
        description: Deploy pre-built serverless applications with a single click from the SAR console.
      - name: SAM Template Support
        description: Publish applications as AWS SAM templates with full CloudFormation resource support.
      - name: Semantic Versioning
        description: Manage multiple application versions using semantic versioning for controlled updates.
      - name: Public and Private Sharing
        description: Share applications publicly to the entire AWS community or privately within your organization.
      - name: Nested Applications
        description: Compose complex serverless architectures using nested SAM application references.
      - name: Policy Sharing
        description: Control who can deploy your application using resource-based policies.
      - name: License Management
        description: Attach open source licenses to applications using SPDX license identifiers.
      - name: CloudFormation Integration
        description: Deploy applications through CloudFormation changesets for full infrastructure-as-code support.
  - type: UseCases
    data:
      - name: Rapid Prototyping
        description: Quickly deploy serverless application templates for common patterns like APIs, data processing, and IoT.
      - name: Internal Application Sharing
        description: Share production-ready serverless building blocks across teams within your organization.
      - name: Open Source Distribution
        description: Publish open source serverless applications to the public SAR catalog.
      - name: Partner Integration Patterns
        description: Distribute serverless integration patterns to AWS partner customers.
      - name: Microservice Templates
        description: Package and share reusable microservice patterns as deployable SAR applications.
      - name: DevOps Automation
        description: Automate deployment of pre-vetted serverless infrastructure patterns via CI/CD pipelines.
  - type: Integrations
    data:
      - name: AWS SAM
        description: Native integration with the AWS Serverless Application Model for packaging and publishing.
      - name: AWS CloudFormation
        description: Applications are deployed via CloudFormation change sets for full IaC integration.
      - name: AWS Lambda
        description: The primary compute runtime for all SAR-deployed serverless applications.
      - name: Amazon API Gateway
        description: Commonly bundled with SAR applications for HTTP API exposure.
      - name: AWS CodePipeline
        description: Automate SAR application publishing as part of CI/CD pipelines.
      - name: AWS Serverless Framework
        description: Third-party Serverless Framework plugins support SAR publishing workflows.
      - name: Amazon DynamoDB
        description: Frequently included as a data store in SAR application templates.
      - name: Amazon S3
        description: Used for hosting static content and storing SAR application artifacts.
  - type: JSON-LD
    url: json-ld/amazon-serverless-application-repository-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-serverless-application-repository-application-policy-statement-schema.json
  - type: JSONSchema
    url: json-schema/amazon-serverless-application-repository-application-summary-schema.json
  - type: JSONStructure
    url: json-structure/amazon-serverless-application-repository-application-policy-statement-structure.json
  - type: JSONStructure
    url: json-structure/amazon-serverless-application-repository-application-structure.json
  - type: JSONStructure
    url: json-structure/amazon-serverless-application-repository-application-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-serverless-application-repository-version-summary-structure.json
  - type: Example
    url: examples/amazon-serverless-application-repository-application-example.json
  - type: Example
    url: examples/amazon-serverless-application-repository-application-policy-statement-example.json
  - type: Example
    url: examples/amazon-serverless-application-repository-application-summary-example.json
  - type: Example
    url: examples/amazon-serverless-application-repository-version-summary-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-serverless-application-repository.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
