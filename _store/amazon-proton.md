---
name: Amazon Proton
description: AWS Proton is a managed service for platform engineers that helps them publish standardized container and serverless application templates to empower developers. It provides automated infrastructure provisioning and manages deployment pipelines for all your applications, enabling self-service developer workflows with platform-team guardrails.
url: https://raw.githubusercontent.com/api-evangelist/amazon-proton/refs/heads/main/apis.yml
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - DevOps
  - Infrastructure as Code
  - Platform Engineering
  - Serverless
  - Templates
  - Self-Service
  - CI/CD
created: '2026-03-16'
modified: '2026-04-19'
apis:
  - name: AWS Proton API
    description: The AWS Proton API provides programmatic access to create and manage environment templates, service templates, environments, services, components, and deployment pipelines for standardized application deployments with automated infrastructure provisioning.
    humanURL: https://aws.amazon.com/proton/
    baseURL: https://proton.amazonaws.com
    tags:
      - DevOps
      - Infrastructure as Code
      - Platform Engineering
      - Templates
      - Environments
      - Services
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/proton/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-proton-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/proton/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/proton/pricing/
      - type: FAQ
        url: https://aws.amazon.com/proton/faqs/
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html
common:
  - type: Portal
    url: https://aws.amazon.com/proton/
  - type: Documentation
    url: https://docs.aws.amazon.com/proton/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/containers/tag/aws-proton/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/proton/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SpectralRules
    url: rules/amazon-proton-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/platform-engineering.yaml
  - type: Vocabulary
    url: vocabulary/amazon-proton-vocabulary.yaml
  - type: Features
    data:
      - name: Environment Templates
        description: Create standardized environment templates with infrastructure-as-code definitions for platform engineers to publish.
      - name: Service Templates
        description: Define reusable service templates that developers can use for self-service application deployments.
      - name: Automated Provisioning
        description: Automatically provision and manage infrastructure for environments and services using CloudFormation or Terraform.
      - name: CI/CD Pipeline Management
        description: Manage deployment pipelines for services with automatic updates when templates change.
      - name: Template Versioning
        description: Version control environment and service templates with major and minor version support.
      - name: Components
        description: Create infrastructure components that can be shared across services and environments.
      - name: Repository Connections
        description: Connect to GitHub and Bitbucket repositories for template source and service pipeline definitions.
      - name: Drift Detection
        description: Detect and remediate configuration drift in deployed environments and services.
  - type: UseCases
    data:
      - name: Developer Self-Service
        description: Enable developers to deploy containerized and serverless applications without deep infrastructure knowledge.
      - name: Platform Standardization
        description: Enforce organizational standards for infrastructure, security, and compliance through templates.
      - name: Multi-Account Deployment
        description: Deploy standardized environments and services across multiple AWS accounts.
      - name: Microservices Orchestration
        description: Manage the infrastructure for complex microservices architectures with consistent templates.
      - name: Serverless Workflows
        description: Deploy Lambda-based serverless applications with standardized infrastructure patterns.
  - type: Integrations
    data:
      - name: AWS CloudFormation
        description: Use CloudFormation as the IaC engine for provisioning environment and service infrastructure.
      - name: HashiCorp Terraform
        description: Use Terraform as an alternative IaC engine for environment and service provisioning.
      - name: AWS CodePipeline
        description: Automatically create CI/CD pipelines for services using CodePipeline.
      - name: GitHub
        description: Connect GitHub repositories as sources for environment templates and service pipeline definitions.
      - name: AWS CodeCommit
        description: Use CodeCommit repositories for template and configuration management.
  - type: JSON-LD
    url: json-ld/amazon-proton-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-proton-accept-environment-account-connection-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-accept-environment-account-connection-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-account-settings-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-blocker-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-blocker-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-component-deployment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-component-deployment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-environment-deployment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-environment-deployment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-service-instance-deployment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-service-instance-deployment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-service-pipeline-deployment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-cancel-service-pipeline-deployment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-compatible-environment-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-compatible-environment-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-component-deployment-update-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-component-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-component-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-counts-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-component-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-component-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-account-connection-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-account-connection-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-environment-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-repository-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-repository-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-instance-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-instance-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-service-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-template-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-create-template-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-component-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-component-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-account-connection-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-account-connection-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-environment-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-repository-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-repository-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-service-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-template-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-delete-template-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-deployment-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-deployment-update-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-account-connection-requester-account-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-account-connection-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-account-connection-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-account-connection-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-template-filter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-template-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-template-version-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-environment-template-version-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-account-settings-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-component-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-component-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-account-connection-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-account-connection-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-environment-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-repository-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-repository-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-repository-sync-status-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-repository-sync-status-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-resources-summary-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-instance-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-instance-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-instance-sync-status-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-instance-sync-status-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-sync-blocker-summary-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-sync-blocker-summary-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-service-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-template-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-template-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-template-sync-status-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-get-template-sync-status-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-component-outputs-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-component-outputs-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-component-provisioned-resources-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-component-provisioned-resources-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-components-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-components-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-account-connections-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-account-connections-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-outputs-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-outputs-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-provisioned-resources-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-provisioned-resources-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-template-versions-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-template-versions-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-templates-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environment-templates-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environments-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-environments-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-repositories-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-repositories-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-repository-sync-definitions-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-repository-sync-definitions-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instance-outputs-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instance-outputs-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instance-provisioned-resources-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instance-provisioned-resources-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instances-filter-by-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instances-filter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instances-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instances-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-instances-sort-by-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-pipeline-outputs-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-pipeline-outputs-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-pipeline-provisioned-resources-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-pipeline-provisioned-resources-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-template-versions-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-template-versions-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-templates-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-service-templates-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-services-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-services-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-tags-for-resource-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-list-tags-for-resource-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-notify-resource-deployment-status-change-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-provisioned-resource-engine-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-provisioned-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-provisioning-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-reject-environment-account-connection-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-reject-environment-account-connection-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-branch-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-branch-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-provider-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-sync-attempt-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-sync-definition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-sync-event-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-repository-sync-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-resource-counts-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-resource-deployment-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-resource-sync-attempt-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-resource-sync-event-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-resource-sync-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-revision-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-s3object-source-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-instance-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-instance-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-pipeline-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-sync-blocker-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-sync-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-template-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-template-supported-component-source-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-template-version-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-service-template-version-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-sort-order-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-sync-blocker-context-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-sync-blocker-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-sync-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-tag-resource-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-tag-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-template-sync-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-template-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-template-version-source-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-template-version-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-untag-resource-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-account-settings-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-account-settings-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-component-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-component-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-account-connection-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-account-connection-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-environment-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-instance-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-instance-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-pipeline-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-pipeline-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-sync-blocker-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-sync-blocker-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-sync-config-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-template-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-template-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-template-version-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-service-template-version-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-template-sync-config-input-schema.json
  - type: JSONSchema
    url: json-schema/amazon-proton-update-template-sync-config-output-schema.json
  - type: JSONStructure
    url: json-structure/amazon-proton-accept-environment-account-connection-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-accept-environment-account-connection-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-account-settings-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-blocker-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-blocker-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-component-deployment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-component-deployment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-environment-deployment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-environment-deployment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-service-instance-deployment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-service-instance-deployment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-service-pipeline-deployment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-cancel-service-pipeline-deployment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-compatible-environment-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-compatible-environment-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-component-deployment-update-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-component-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-component-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-counts-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-component-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-component-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-account-connection-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-account-connection-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-environment-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-repository-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-repository-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-instance-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-instance-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-service-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-template-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-create-template-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-component-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-component-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-account-connection-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-account-connection-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-environment-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-repository-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-repository-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-service-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-template-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-delete-template-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-deployment-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-deployment-update-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-account-connection-requester-account-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-account-connection-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-account-connection-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-account-connection-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-template-filter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-template-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-template-version-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-environment-template-version-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-account-settings-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-component-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-component-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-account-connection-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-account-connection-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-environment-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-repository-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-repository-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-repository-sync-status-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-repository-sync-status-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-resources-summary-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-instance-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-instance-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-instance-sync-status-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-instance-sync-status-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-sync-blocker-summary-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-sync-blocker-summary-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-service-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-template-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-template-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-template-sync-status-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-get-template-sync-status-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-component-outputs-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-component-outputs-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-component-provisioned-resources-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-component-provisioned-resources-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-components-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-components-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-account-connections-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-account-connections-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-outputs-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-outputs-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-provisioned-resources-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-provisioned-resources-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-template-versions-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-template-versions-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-templates-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environment-templates-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environments-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-environments-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-repositories-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-repositories-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-repository-sync-definitions-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-repository-sync-definitions-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instance-outputs-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instance-outputs-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instance-provisioned-resources-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instance-provisioned-resources-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instances-filter-by-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instances-filter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instances-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instances-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-instances-sort-by-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-pipeline-outputs-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-pipeline-outputs-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-pipeline-provisioned-resources-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-pipeline-provisioned-resources-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-template-versions-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-template-versions-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-templates-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-service-templates-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-services-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-services-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-tags-for-resource-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-list-tags-for-resource-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-notify-resource-deployment-status-change-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-provisioned-resource-engine-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-provisioned-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-provisioning-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-reject-environment-account-connection-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-reject-environment-account-connection-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-branch-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-branch-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-provider-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-sync-attempt-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-sync-definition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-sync-event-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-repository-sync-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-resource-counts-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-resource-deployment-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-resource-sync-attempt-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-resource-sync-event-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-resource-sync-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-revision-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-s3object-source-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-instance-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-instance-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-pipeline-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-sync-blocker-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-sync-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-template-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-template-supported-component-source-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-template-version-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-service-template-version-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-sort-order-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-sync-blocker-context-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-sync-blocker-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-sync-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-tag-resource-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-tag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-template-sync-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-template-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-template-version-source-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-template-version-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-untag-resource-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-account-settings-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-account-settings-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-component-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-component-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-account-connection-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-account-connection-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-environment-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-instance-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-instance-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-pipeline-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-pipeline-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-sync-blocker-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-sync-blocker-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-sync-config-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-template-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-template-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-template-version-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-service-template-version-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-template-sync-config-input-structure.json
  - type: JSONStructure
    url: json-structure/amazon-proton-update-template-sync-config-output-structure.json
  - type: Example
    url: examples/amazon-proton-cancel-service-instance-deployment-input-example.json
  - type: Example
    url: examples/amazon-proton-compatible-environment-template-example.json
  - type: Example
    url: examples/amazon-proton-component-summary-example.json
  - type: Example
    url: examples/amazon-proton-create-component-input-example.json
  - type: Example
    url: examples/amazon-proton-create-environment-account-connection-input-example.json
  - type: Example
    url: examples/amazon-proton-create-environment-template-output-example.json
  - type: Example
    url: examples/amazon-proton-create-repository-input-example.json
  - type: Example
    url: examples/amazon-proton-create-service-instance-output-example.json
  - type: Example
    url: examples/amazon-proton-create-service-sync-config-input-example.json
  - type: Example
    url: examples/amazon-proton-create-service-sync-config-output-example.json
  - type: Example
    url: examples/amazon-proton-create-template-sync-config-input-example.json
  - type: Example
    url: examples/amazon-proton-delete-component-output-example.json
  - type: Example
    url: examples/amazon-proton-delete-environment-account-connection-input-example.json
  - type: Example
    url: examples/amazon-proton-delete-environment-input-example.json
  - type: Example
    url: examples/amazon-proton-delete-environment-output-example.json
  - type: Example
    url: examples/amazon-proton-delete-environment-template-input-example.json
  - type: Example
    url: examples/amazon-proton-delete-environment-template-version-input-example.json
  - type: Example
    url: examples/amazon-proton-delete-repository-output-example.json
  - type: Example
    url: examples/amazon-proton-delete-service-input-example.json
  - type: Example
    url: examples/amazon-proton-environment-account-connection-example.json
  - type: Example
    url: examples/amazon-proton-environment-template-summary-example.json
  - type: Example
    url: examples/amazon-proton-get-account-settings-output-example.json
  - type: Example
    url: examples/amazon-proton-get-component-input-example.json
  - type: Example
    url: examples/amazon-proton-get-environment-template-input-example.json
  - type: Example
    url: examples/amazon-proton-get-environment-template-output-example.json
  - type: Example
    url: examples/amazon-proton-get-environment-template-version-output-example.json
  - type: Example
    url: examples/amazon-proton-get-service-output-example.json
  - type: Example
    url: examples/amazon-proton-get-service-sync-blocker-summary-output-example.json
  - type: Example
    url: examples/amazon-proton-get-service-template-output-example.json
  - type: Example
    url: examples/amazon-proton-list-components-output-example.json
  - type: Example
    url: examples/amazon-proton-list-environment-account-connections-output-example.json
  - type: Example
    url: examples/amazon-proton-list-environment-outputs-input-example.json
  - type: Example
    url: examples/amazon-proton-list-environment-provisioned-resources-input-example.json
  - type: Example
    url: examples/amazon-proton-list-environment-provisioned-resources-output-example.json
  - type: Example
    url: examples/amazon-proton-list-environment-template-versions-input-example.json
  - type: Example
    url: examples/amazon-proton-list-repositories-output-example.json
  - type: Example
    url: examples/amazon-proton-list-repository-sync-definitions-input-example.json
  - type: Example
    url: examples/amazon-proton-list-repository-sync-definitions-output-example.json
  - type: Example
    url: examples/amazon-proton-list-service-instance-outputs-output-example.json
  - type: Example
    url: examples/amazon-proton-list-service-instance-provisioned-resources-input-example.json
  - type: Example
    url: examples/amazon-proton-list-service-instance-provisioned-resources-output-example.json
  - type: Example
    url: examples/amazon-proton-list-service-instances-input-example.json
  - type: Example
    url: examples/amazon-proton-list-service-pipeline-outputs-input-example.json
  - type: Example
    url: examples/amazon-proton-list-service-pipeline-outputs-output-example.json
  - type: Example
    url: examples/amazon-proton-list-service-pipeline-provisioned-resources-output-example.json
  - type: Example
    url: examples/amazon-proton-list-service-template-versions-input-example.json
  - type: Example
    url: examples/amazon-proton-list-services-output-example.json
  - type: Example
    url: examples/amazon-proton-output-example.json
  - type: Example
    url: examples/amazon-proton-reject-environment-account-connection-input-example.json
  - type: Example
    url: examples/amazon-proton-reject-environment-account-connection-output-example.json
  - type: Example
    url: examples/amazon-proton-repository-sync-attempt-example.json
  - type: Example
    url: examples/amazon-proton-repository-sync-definition-example.json
  - type: Example
    url: examples/amazon-proton-resource-counts-summary-example.json
  - type: Example
    url: examples/amazon-proton-resource-sync-attempt-example.json
  - type: Example
    url: examples/amazon-proton-resource-sync-event-example.json
  - type: Example
    url: examples/amazon-proton-service-instance-example.json
  - type: Example
    url: examples/amazon-proton-service-pipeline-example.json
  - type: Example
    url: examples/amazon-proton-service-summary-example.json
  - type: Example
    url: examples/amazon-proton-service-sync-config-example.json
  - type: Example
    url: examples/amazon-proton-service-template-version-summary-example.json
  - type: Example
    url: examples/amazon-proton-sync-blocker-example.json
  - type: Example
    url: examples/amazon-proton-tag-example.json
  - type: Example
    url: examples/amazon-proton-untag-resource-input-example.json
  - type: Example
    url: examples/amazon-proton-update-component-input-example.json
  - type: Example
    url: examples/amazon-proton-update-component-output-example.json
  - type: Example
    url: examples/amazon-proton-update-environment-account-connection-input-example.json
  - type: Example
    url: examples/amazon-proton-update-environment-template-version-input-example.json
  - type: Example
    url: examples/amazon-proton-update-service-input-example.json
  - type: Example
    url: examples/amazon-proton-update-service-output-example.json
  - type: Example
    url: examples/amazon-proton-update-service-sync-blocker-output-example.json
  - type: Example
    url: examples/amazon-proton-update-service-sync-config-input-example.json
  - type: Example
    url: examples/amazon-proton-update-service-template-input-example.json
  - type: Example
    url: examples/amazon-proton-update-service-template-version-input-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-proton.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
