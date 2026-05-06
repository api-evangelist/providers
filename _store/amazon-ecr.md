---
name: Amazon ECR
description: Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy container images and artifacts. ECR eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure, and integrates with Amazon ECS and Amazon EKS for simplified development to production workflows.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/ecr/
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - Amazon Web Services
  - AWS
  - Container Images
  - Container Registry
  - Containers
  - Docker
  - ECR
  - OCI
apis:
  - name: Amazon ECR API
    description: API for managing Amazon ECR repositories, images, and related resources.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    url: https://aws.amazon.com/ecr/
    baseURL: https://api.ecr.amazonaws.com
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/
      - type: OpenAPI
        url: openapi/amazon-ecr-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/ecr/2015-09-21/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-ecr-repository-schema.json
      - type: JSONLD
        url: json-ld/amazon-ecr-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/ecr/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/ecr/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/ecr/faqs/
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/
      - type: Documentation
        url: https://docs.aws.amazon.com/cli/latest/reference/ecr/
      - type: Security
        url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/security.html
      - type: JSONStructure
        url: json-structure/amazon-ecr-repository-structure.json
      - type: Example
        url: examples/amazon-ecr-repository-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/
  - type: Documentation
    url: https://docs.aws.amazon.com/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-web-services
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Fully Managed Registry
        description: Eliminate the need to operate your own container repositories or worry about scaling infrastructure.
      - name: Image Vulnerability Scanning
        description: Automated vulnerability assessment via Amazon Inspector integration for continuous image security.
      - name: Lifecycle Policies
        description: Automatically expire and delete images based on rules to reduce storage costs.
      - name: Cross-Account Replication
        description: Replicate images to registries in other AWS accounts and regions for availability.
      - name: OCI Artifact Support
        description: Store and manage OCI-compliant artifacts including Helm charts and SBOMs.
      - name: Image Signing
        description: Sign and verify container images automatically without additional infrastructure.
      - name: Pull Through Cache
        description: Cache upstream public registry images in ECR for reduced egress costs and improved availability.
  - type: UseCases
    data:
      - name: CI/CD Pipeline Integration
        description: Store container images in ECR and deploy to ECS or EKS as part of automated pipelines.
      - name: Security and Compliance
        description: Automated vulnerability scanning and image signing for security-compliant container deployments.
      - name: Multi-Region Deployments
        description: Replicate images across regions for low-latency pulls and improved resilience.
      - name: Helm Chart Repository
        description: Store Helm charts as OCI artifacts for Kubernetes application deployment management.
      - name: Image Lifecycle Management
        description: Manage image retention policies to keep registries clean and reduce storage costs.
  - type: Integrations
    data:
      - name: Amazon ECS
        description: Natively integrated with ECS for pulling container images to run tasks and services.
      - name: Amazon EKS
        description: Authenticate and pull container images from ECR for Kubernetes workloads.
      - name: Amazon Inspector
        description: Continuous vulnerability scanning of images stored in ECR for security compliance.
      - name: AWS CodeBuild
        description: Build and push container images to ECR as part of CI/CD build processes.
      - name: AWS IAM
        description: Resource-based policies control who can push, pull, and manage images in ECR.
  - type: SpectralRules
    url: rules/amazon-ecr-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ecr-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ecr-management.yaml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
