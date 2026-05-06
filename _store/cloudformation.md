---
name: AWS CloudFormation
description: A collection of APIs provided by AWS for infrastructure as code provisioning and management of AWS and third-party resources using CloudFormation templates and the Cloud Control API.
image: https://aws.amazon.com/cloudformation/logo.png
created: '2024'
modified: '2026-04-18'
url: https://docs.aws.amazon.com/cloudformation/
specificationVersion: '0.19'
tags:
  - Automation
  - AWS
  - Cloud Resources
  - IaC
  - Infrastructure As Code
  - Stack Management
apis:
  - name: AWS CloudFormation API
    description: AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles. It uses templates to define stacks of resources and provides API operations for creating, updating, and deleting stacks.
    image: https://aws.amazon.com/cloudformation/logo.png
    humanURL: https://aws.amazon.com/cloudformation/
    baseURL: https://cloudformation.{region}.amazonaws.com
    tags:
      - Infrastructure
      - Resources
      - Stacks
      - Templates
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/cloudformation/
      - type: APIReference
        url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/cloudformation-api.yml
      - type: Pricing
        url: https://aws.amazon.com/cloudformation/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/cloudformation/getting-started/
      - type: ChangeLog
        url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/document-history.html
      - type: SDK
        url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
        title: Python SDK (Boto3)
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
        email: ''
  - name: AWS Cloud Control API
    description: AWS Cloud Control API provides a uniform CRUDL (create, read, update, delete, list) interface for managing AWS and third-party resources. It offers a standardized way to access and provision resource types available in the CloudFormation Registry without needing to learn each individual service API.
    image: https://aws.amazon.com/cloudformation/logo.png
    humanURL: https://aws.amazon.com/cloudcontrolapi/
    baseURL: https://cloudcontrolapi.{region}.amazonaws.com
    tags:
      - Cloud Control
      - CRUDL
      - Provisioning
      - Resources
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html
      - type: OpenAPI
        url: openapi/cloud-control-api.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/cloudcontrolapi/index.html
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
        email: ''
common:
  - type: Portal
    url: https://aws.amazon.com/cloudformation/resources/
  - type: GettingStarted
    url: https://aws.amazon.com/cloudformation/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
  - type: Pricing
    url: https://aws.amazon.com/cloudformation/pricing/
  - type: TermsOfService
    url: https://aws.amazon.com/terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Blog
    url: https://aws.amazon.com/blogs/devops/category/management-tools/aws-cloudformation/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Console
    url: https://console.aws.amazon.com/cloudformation/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws-cloudformation
  - type: GitHubRepository
    url: https://github.com/aws-cloudformation/aws-cloudformation-templates
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-cloudformation
  - type: Features
    data:
      - name: Infrastructure As Code
        description: Define and provision AWS infrastructure using declarative JSON/YAML templates
      - name: Stack Management
        description: Create, update, and delete collections of AWS resources as a single unit
      - name: Change Sets
        description: Preview changes before applying them to running stacks
      - name: Drift Detection
        description: Detect when stack resources have been modified outside of CloudFormation
      - name: Stack Sets
        description: Deploy stacks across multiple accounts and regions simultaneously
      - name: Cloud Control CRUDL
        description: Uniform interface for managing any resource in the CloudFormation Registry
  - type: UseCases
    data:
      - name: Multi-Account Deployment
        description: Deploy consistent infrastructure across multiple AWS accounts with Stack Sets
      - name: Environment Provisioning
        description: Spin up identical dev, staging, and production environments from templates
      - name: Compliance Auditing
        description: Detect configuration drift and enforce infrastructure compliance
  - type: Integrations
    data:
      - name: AWS CDK
        description: Define cloud infrastructure using familiar programming languages that compile to CloudFormation
      - name: AWS SAM
        description: Simplified syntax for serverless application deployment via CloudFormation
      - name: Terraform
        description: Alternative IaC tool that can import/export CloudFormation templates
  - type: SDK
    url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
    title: Python SDK (Boto3)
  - type: SDK
    url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/cloudformation-examples.html
    title: JavaScript SDK v3
  - type: SDK
    url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudformation.html
    title: Java SDK
  - type: SDK
    url: https://docs.aws.amazon.com/sdk-for-go/api/service/cloudformation/
    title: Go SDK
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/cloudformation/
    title: AWS CLI - CloudFormation
  - type: CLI
    url: https://github.com/aws-cloudformation/rain
    title: Rain - CloudFormation CLI
  - type: JSONSchema
    url: json-schema/stack.json
    title: Stack Schema
  - type: JSONSchema
    url: json-schema/template.json
    title: Template Schema
  - type: JSONSchema
    url: json-schema/resource.json
    title: Resource Schema
  - type: JSONSchema
    url: json-schema/change-set.json
    title: Change Set Schema
  - type: JSONSchema
    url: json-schema/cloudformation-change-schema.json
    title: Change Schema
  - type: JSONSchema
    url: json-schema/cloudformation-change-set-detail-schema.json
    title: Change Set Detail Schema
  - type: JSONSchema
    url: json-schema/cloudformation-change-set-summary-schema.json
    title: Change Set Summary Schema
  - type: JSONSchema
    url: json-schema/cloudformation-error-response-schema.json
    title: Error Response Schema
  - type: JSONSchema
    url: json-schema/cloudformation-stack-schema.json
    title: Stack Detail Schema
  - type: JSONSchema
    url: json-schema/cloudformation-stack-event-schema.json
    title: Stack Event Schema
  - type: JSONSchema
    url: json-schema/cloudformation-stack-resource-schema.json
    title: Stack Resource Schema
  - type: JSONSchema
    url: json-schema/cloudformation-stack-summary-schema.json
    title: Stack Summary Schema
  - type: JSONSchema
    url: json-schema/cloudformation-tag-schema.json
    title: Tag Schema
  - type: JSONSchema
    url: json-schema/cloud-control-progress-event-schema.json
    title: Cloud Control Progress Event Schema
  - type: JSONSchema
    url: json-schema/cloud-control-resource-description-schema.json
    title: Cloud Control Resource Description Schema
  - type: JSONSchema
    url: json-schema/cloud-control-error-response-schema.json
    title: Cloud Control Error Response Schema
  - type: JSONLD
    url: json-ld/context.jsonld
    title: JSON-LD Context
  - type: JSONLD
    url: json-ld/cloudformation-context.jsonld
    title: CloudFormation JSON-LD Context
  - type: JSONLD
    url: json-ld/cloud-control-context.jsonld
    title: Cloud Control JSON-LD Context
  - type: Vocabulary
    url: vocabulary/cloudformation-vocabulary.yaml
    title: CloudFormation Vocabulary
  - type: Rules
    url: rules/cloudformation-spectral-rules.yml
    title: Spectral Rules
  - type: Capabilities
    url: capabilities/infrastructure-provisioning.yaml
    title: Infrastructure Provisioning Workflow
  - type: Capabilities
    url: capabilities/shared/cloudformation.yaml
    title: CloudFormation Shared Capability
  - type: Capabilities
    url: capabilities/shared/cloud-control.yaml
    title: Cloud Control Shared Capability
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
