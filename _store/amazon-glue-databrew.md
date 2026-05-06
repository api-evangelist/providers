---
aid: amazon-glue-databrew
name: Amazon Glue DataBrew
description: AWS Glue DataBrew is a visual data preparation tool that makes it easy for data analysts and data scientists to clean and normalize data to prepare it for analytics and machine learning. It provides over 250 pre-built transformations to automate data preparation tasks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Analytics
  - Data Preparation
  - ETL
  - Machine Learning
url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-glue-databrew:aws-glue-databrew-api
    name: AWS Glue DataBrew API
    description: The AWS Glue DataBrew API provides programmatic access to create and manage datasets, recipes, projects, jobs, and rulesets for visual data preparation and transformation workflows.
    humanURL: https://aws.amazon.com/glue/features/databrew/
    baseURL: https://databrew.amazonaws.com
    tags:
      - Data Analytics
      - Data Preparation
      - ETL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/databrew/latest/dg/API_Reference.html
      - type: OpenAPI
        url: openapi/amazon-glue-databrew-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/glue/features/databrew/
      - type: Pricing
        url: https://aws.amazon.com/glue/pricing/
      - type: FAQ
        url: https://aws.amazon.com/glue/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/databrew/latest/dg/API_Reference.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: JSONSchema
        url: json-schema/glue-databrew-dataset-schema.json
      - type: JSONLD
        url: json-ld/amazon-glue-databrew-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/glue/features/databrew/
  - type: Documentation
    url: https://docs.aws.amazon.com/databrew/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/tag/aws-glue-databrew/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/databrew/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-glue-databrew-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-glue-databrew-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-glue-databrew-data-preparation.yaml
  - type: Features
    data:
      - name: 250+ Pre-Built Transformations
        description: Apply over 250 ready-to-use transformations without writing code, including filtering, normalizing, aggregating, and reformatting data.
      - name: Visual Data Preparation Interface
        description: Interactive visual interface to explore and transform data without writing code.
      - name: Recipe-Based Transformations
        description: Save transformation steps as reusable recipes that can be versioned and shared across teams.
      - name: Data Profiling
        description: Automatically profile datasets to understand data quality, distribution, and statistics.
      - name: Data Quality Rules
        description: Define and enforce data quality rules with rulesets to validate data before processing.
      - name: Collaborative Projects
        description: Create shared projects for team-based data preparation with centralized management.
  - type: UseCases
    data:
      - name: Analytics Data Preparation
        description: Clean, normalize, and transform raw data for business analytics dashboards and reports.
      - name: Machine Learning Feature Engineering
        description: Prepare and transform features from raw data for training machine learning models.
      - name: Data Quality Validation
        description: Profile datasets and apply quality rules to ensure data meets standards before processing.
      - name: ETL Pipeline Automation
        description: Automate recurring data transformation jobs as part of data pipeline workflows.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Read input datasets from and write transformed output to S3 buckets.
      - name: AWS Glue Data Catalog
        description: Connect to Glue Data Catalog tables as data sources.
      - name: Amazon Redshift
        description: Connect to Redshift databases as data sources for preparation.
      - name: Amazon RDS
        description: Use RDS databases as input sources for DataBrew transformation.
      - name: AWS Lake Formation
        description: Integrate with Lake Formation for secure data lake access.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
