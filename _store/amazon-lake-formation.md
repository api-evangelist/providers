---
name: Amazon Lake Formation
segments:
  - Data Lakes
  - Analytics
description: AWS Lake Formation is a service that makes it easy to set up a secure data lake in days, providing centralized governance and security for data stored in Amazon S3 and other AWS data stores with fine-grained access control.
url: https://aws.amazon.com/lake-formation/
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - Access Control
  - Analytics
  - AWS
  - Data Governance
  - Data Lake
  - S3
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Lake Formation API
    description: The AWS Lake Formation API provides programmatic access to create and manage data lakes, configure data permissions and access controls, register data sources, and manage data catalog resources for centralized data governance.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/lake-formation/
    baseURL: https://lakeformation.amazonaws.com
    tags:
      - Access Control
      - Data Governance
      - Data Lake
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/lakeformation/2017-03-31/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/lake-formation/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/lake-formation/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/lake-formation/faqs/
      - type: Features
        url: https://aws.amazon.com/lake-formation/features/
      - type: Documentation
        url: https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html
      - type: APIReference
        url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-lake-formation-openapi.yml
      - type: JSONLD
        url: json-ld/amazon-lake-formation-context.jsonld
      - type: JSONSchema
        url: json-schema/amazon-lake-formation-resource-schema.json
      - type: JSONSchema
        url: json-schema/amazon-lake-formation-permission-schema.json
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/category/analytics/aws-lake-formation/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Console
    url: https://console.aws.amazon.com/lakeformation/home
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/lakeformation/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: Portal
    url: https://aws.amazon.com/lake-formation/
  - type: Documentation
    url: https://docs.aws.amazon.com/lake-formation/
  - type: Pricing
    url: https://aws.amazon.com/lake-formation/pricing/
  - type: GettingStarted
    url: https://aws.amazon.com/lake-formation/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/lake-formation/faqs/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Features
    data:
      - name: Fine-Grained Access Control
        description: Grant table, column, row, and cell-level permissions to data in your data lake.
      - name: Centralized Governance
        description: Centrally define and manage security, governance, and auditing policies across the data lake.
      - name: Data Catalog Integration
        description: Integrates with AWS Glue Data Catalog to discover, catalog, and share metadata.
      - name: Cross-Account Data Sharing
        description: Securely share data across AWS accounts without copying it.
      - name: Governed Tables
        description: ACID transactions and automatic compaction for governed tables stored in S3.
  - type: UseCases
    data:
      - name: Data Lake Security
        description: Implement fine-grained access control for data stored in S3 with row and column-level security.
      - name: Self-Service Analytics
        description: Enable business users to discover and access approved data without manual provisioning.
      - name: Cross-Account Data Sharing
        description: Share data lake resources across AWS accounts and organizations.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Manage and secure data stored in S3 as the data lake storage layer.
      - name: AWS Glue
        description: Use Glue Data Catalog as the metadata store and Glue ETL for data transformation.
      - name: Amazon Athena
        description: Query data lake data using Athena with Lake Formation access controls enforced.
      - name: Amazon Redshift
        description: Use Redshift Spectrum to query data lake with Lake Formation permissions.
  - type: SpectralRules
    url: rules/amazon-lake-formation-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-lake-formation-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-lake-formation-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
