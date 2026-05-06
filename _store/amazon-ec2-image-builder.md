---
name: Amazon EC2 Image Builder
description: EC2 Image Builder simplifies the building, testing, and deployment of Virtual Machine and container images for use on AWS or on-premises. It provides an automated pipeline to create and maintain secure, up-to-date server images without requiring scripting expertise.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/image-builder/
created: '2026-03-16'
modified: '2026-04-19'
tags:
  - Amazon Web Services
  - Automation
  - AWS
  - Container Images
  - EC2
  - Image Building
  - Virtual Machine Images
apis:
  - name: Amazon EC2 Image Builder API
    description: The EC2 Image Builder API provides programmatic access to create and manage image pipelines, recipes, components, infrastructure configurations, and distribution settings for automated VM and container image building workflows.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/image-builder/
    baseURL: https://imagebuilder.amazonaws.com
    tags:
      - Automation
      - EC2
      - Image Building
      - Pipeline
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-ec2-image-builder-openapi.yaml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/imagebuilder/2019-12-02/openapi.yaml
      - type: JSONSchema
        url: json-schema/ec2-image-builder-image-pipeline-schema.json
      - type: JSONLD
        url: json-ld/amazon-ec2-image-builder-context.jsonld
      - type: GettingStarted
        url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/getting-started-image-builder.html
      - type: Pricing
        url: https://aws.amazon.com/image-builder/pricing/
      - type: FAQ
        url: https://aws.amazon.com/image-builder/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/
      - type: Authentication
        url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/CommonParameters.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/limits.html
      - type: JSONSchema
        url: json-schema/ec2-image-builder-account-aggregation-schema.json
      - type: JSONStructure
        url: json-structure/ec2-image-builder-account-aggregation-structure.json
      - type: Example
        url: examples/ec2-image-builder-account-aggregation-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/developer/
  - type: Documentation
    url: https://docs.aws.amazon.com/imagebuilder/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/tag/ec2-image-builder/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/imagebuilder/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/ec2-image-builder
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Automated Image Pipelines
        description: Define end-to-end image creation workflows with build, test, and distribution phases without scripting expertise.
      - name: Image Recipes
        description: Compose reusable image definitions from components including OS, software packages, and custom scripts.
      - name: Component Library
        description: Catalog of pre-built AWS-managed and custom components for common software installation and configuration tasks.
      - name: Automated Testing
        description: Run automated tests on images before distribution to validate software, security, and compliance requirements.
      - name: Multi-Region Distribution
        description: Automatically distribute approved images to multiple AWS regions with configurable permissions.
      - name: Container Image Support
        description: Build, test, and publish container images to Amazon ECR alongside traditional AMI workflows.
      - name: CIS and STIG Hardening
        description: Built-in support for CIS Benchmarks and DISA STIG security hardening standards for compliance.
      - name: Scheduled Builds
        description: Automatically rebuild images on a schedule to incorporate OS patches and security updates.
  - type: UseCases
    data:
      - name: Golden AMI Management
        description: Create and maintain standardized, secure, and up-to-date base AMIs for all EC2 workloads across the organization.
      - name: Security Patch Automation
        description: Automatically rebuild images with the latest OS security patches and distribute them across regions.
      - name: Compliance Image Hardening
        description: Apply CIS or STIG security benchmarks to create compliant images for regulated environments.
      - name: Container Base Image Management
        description: Maintain secure, up-to-date container base images and publish them to ECR for development teams.
      - name: Multi-Account Image Sharing
        description: Build images in a central account and distribute them to multiple AWS accounts and regions.
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Produces AMIs that can be launched as EC2 instances across regions and accounts.
      - name: Amazon ECR
        description: Publishes container images to ECR repositories as part of container image build pipelines.
      - name: AWS Systems Manager
        description: Uses SSM Agent for image build and test execution on temporary build instances.
      - name: Amazon Inspector
        description: Integrates with Amazon Inspector for automated vulnerability scanning of built images.
      - name: AWS Key Management Service
        description: Encrypts AMIs and snapshots using KMS customer-managed keys during distribution.
      - name: AWS CloudTrail
        description: Logs all Image Builder API calls for auditing and compliance tracking.
  - type: SpectralRules
    url: rules/amazon-ec2-image-builder-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ec2-image-builder-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ec2-image-builder-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
