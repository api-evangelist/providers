---
aid: amazon-datazone
name: Amazon DataZone
description: Amazon DataZone is a data management service that helps you catalog, discover, govern, share, and analyze your data across your organization and beyond. It enables data producers and consumers to collaborate, with built-in governance, data catalog capabilities, and a business data catalog to organize and share data across your AWS environment. DataZone provides domain-based governance, project workspaces, subscription-based access control, and integration with AWS analytics services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Catalog
  - Data Governance
  - Data Management
  - Data Sharing
  - Analytics
url: https://raw.githubusercontent.com/api-evangelist/amazon-datazone/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-datazone:amazon-datazone-api
    name: Amazon DataZone API
    description: The Amazon DataZone API provides programmatic access to create and manage data domains, data assets, data catalogs, projects, subscriptions, and governance policies for enterprise-wide data management and sharing. Supports domain-based governance, asset cataloging, subscription workflows, and environment provisioning for data analytics access.
    humanURL: https://aws.amazon.com/datazone/
    baseURL: https://datazone.amazonaws.com
    tags:
      - Data Catalog
      - Data Governance
      - Data Sharing
      - Analytics
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/datazone/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-datazone-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/datazone/2018-05-10/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/datazone/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/datazone/pricing/
      - type: FAQ
        url: https://aws.amazon.com/datazone/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/datazone/latest/APIReference/
      - type: JSONSchema
        url: json-schema/domain-schema.json
      - type: JSONSchema
        url: json-schema/project-schema.json
      - type: JSONSchema
        url: json-schema/asset-schema.json
      - type: JSONLD
        url: json-ld/amazon-datazone-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/datazone/
  - type: DeveloperPortal
    url: https://aws.amazon.com/datazone/
  - type: Documentation
    url: https://docs.aws.amazon.com/datazone/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/datazone/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-datazone-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-datazone-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-catalog-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/datazone.yaml
  - type: Features
    data:
      - name: Business Data Catalog
        description: Central catalog where data producers publish assets and data consumers can discover, understand, and request access to data products.
      - name: Domain-Based Governance
        description: Organize data assets, users, and governance policies within domains that reflect your organizational structure and data ownership.
      - name: Subscription Workflow
        description: Built-in request/approval workflow for data consumers to request access to data assets with business justification and audit trail.
      - name: Project Workspaces
        description: Isolated project containers within domains where teams organize their data assets, environments, and members.
      - name: Analytics Environment Provisioning
        description: Automatically provision data access environments with Athena, Glue, Redshift, or other tools when subscriptions are approved.
      - name: Glue Data Catalog Integration
        description: Automatically discover and import tables from AWS Glue Data Catalog into DataZone for cataloging and governance.
      - name: Data Lineage
        description: Track data lineage across assets to understand data origins, transformations, and dependencies for trust and compliance.
  - type: UseCases
    data:
      - name: Enterprise Data Marketplace
        description: Build an internal data marketplace where business units publish their data products for discovery and consumption by other teams.
      - name: Data Access Governance
        description: Implement governed data access with approval workflows ensuring data consumers have proper authorization and business justification.
      - name: Cross-Account Data Sharing
        description: Share data assets across AWS accounts within an organization using DataZone's subscription and access management capabilities.
      - name: Self-Service Analytics
        description: Enable analysts to discover and access data independently through the DataZone catalog with automatic environment provisioning.
      - name: Regulatory Data Compliance
        description: Maintain audit trails of data access, govern sensitive data assets, and enforce data residency policies through domain governance.
  - type: Integrations
    data:
      - name: AWS Glue
        description: DataZone integrates with Glue Data Catalog to automatically discover, import, and catalog Glue tables for sharing and governance.
      - name: Amazon Redshift
        description: Catalog Redshift tables and views and govern cross-cluster data sharing through DataZone subscription workflows.
      - name: Amazon Athena
        description: DataZone environments provision Athena as a query engine for subscribers accessing S3-based data assets.
      - name: Amazon S3
        description: Catalog S3-based datasets in DataZone and control access through subscription-based Lake Formation permissions.
      - name: AWS Lake Formation
        description: DataZone uses Lake Formation for fine-grained column and row-level access control when subscriptions are approved.
      - name: AWS IAM
        description: IAM roles provide domain execution context and identity-based access control for DataZone resources and catalog operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
