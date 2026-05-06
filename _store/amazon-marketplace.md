---
aid: amazon-marketplace
name: Amazon Marketplace
description: AWS Marketplace is a curated digital catalog that makes it easy to find, buy, deploy, and manage third-party software, data, and services that run on AWS. It offers thousands of software listings from independent software vendors. The Marketplace Catalog API enables programmatic management of marketplace entities including products, offers, and data products through change sets and entity description operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Commerce
  - ISV
  - Marketplace
  - Software Catalog
url: https://raw.githubusercontent.com/api-evangelist/amazon-marketplace/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-marketplace:aws-marketplace-catalog-api
    name: AWS Marketplace Catalog API
    description: The AWS Marketplace Catalog API provides programmatic access to manage entities and change sets for publishing and updating software products, data products, and machine learning products on AWS Marketplace. Covers 13 operations for entity discovery, change set lifecycle management, resource policies, and resource tagging.
    humanURL: https://aws.amazon.com/marketplace/
    baseURL: https://catalog.marketplace.amazonaws.com
    tags:
      - Commerce
      - ISV
      - Marketplace
      - Software Catalog
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html
      - type: OpenAPI
        url: openapi/amazon-marketplace-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/marketplace/management/portal/
      - type: Pricing
        url: https://aws.amazon.com/marketplace/pricing/
      - type: FAQ
        url: https://aws.amazon.com/marketplace/help/
      - type: JSONSchema
        url: json-schema/amazon-marketplace-change-set-summary-list-item-schema.json
      - type: JSONStructure
        url: json-structure/amazon-marketplace-change-set-summary-list-item-structure.json
      - type: JSON-LD
        url: json-ld/amazon-marketplace-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/marketplace/
  - type: Documentation
    url: https://docs.aws.amazon.com/marketplace/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/awsmarketplace/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/marketplace/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-marketplace-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-marketplace-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/marketplace-catalog-workflow.yaml
  - type: Features
    data:
      - name: Entity Management
        description: Programmatically list and describe marketplace entities including software products, data products, and offers.
      - name: Change Set Lifecycle
        description: Start, monitor, and cancel change sets for publishing new listings or updating existing ones.
      - name: Resource Policies
        description: Attach, retrieve, and remove resource-based policies to control access to marketplace entities.
      - name: Resource Tagging
        description: Tag marketplace resources with key-value pairs for organization and cost allocation.
      - name: Multi-Region Support
        description: Access marketplace entities across multiple AWS regions through regional catalog endpoints.
      - name: Publishing Automation
        description: Integrate catalog API with CI/CD pipelines for automated product publishing and updates.
  - type: UseCases
    data:
      - name: Product Publishing Automation
        description: Automate publishing and updating software listings on AWS Marketplace from CI/CD pipelines.
      - name: Marketplace Catalog Discovery
        description: Programmatically discover and evaluate available software products and data products.
      - name: Change Set Monitoring
        description: Track the status of publishing operations and receive change set completion notifications.
      - name: Multi-Account Marketplace Management
        description: Manage marketplace listings across multiple AWS accounts with shared resource policies.
      - name: ISV Self-Service Publishing
        description: Enable ISV teams to self-service publish and update product listings through the catalog API.
  - type: Integrations
    data:
      - name: AWS IAM
        description: Control access to catalog API operations through IAM policies and roles.
      - name: Amazon EventBridge
        description: Subscribe to marketplace events for change set completions and entity state changes.
      - name: AWS CloudFormation
        description: Deploy and manage marketplace subscriptions as infrastructure-as-code.
      - name: AWS Organizations
        description: Share private marketplace listings across accounts in an AWS organization.
      - name: Amazon SNS
        description: Receive notifications for marketplace change set status updates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
