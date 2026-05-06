---
aid: amazon-healthomics
name: Amazon HealthOmics
description: AWS HealthOmics is a purpose-built service for healthcare and life sciences organizations that helps store, query, and analyze genomic, transcriptomic, and other omics data to generate insights and accelerate scientific discoveries and improve healthcare.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Bioinformatics
  - Genomics
  - Healthcare
  - Life Sciences
  - Cloud Computing
url: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-healthomics:aws-healthomics-api
    name: AWS HealthOmics API
    description: The AWS HealthOmics API provides programmatic access to manage omics storage, workflows, run groups, annotation stores, and variant stores for genomics and other omics data analysis.
    humanURL: https://aws.amazon.com/healthomics/
    baseURL: https://omics.amazonaws.com
    tags:
      - Genomics
      - Healthcare
      - Life Sciences
      - Bioinformatics
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/omics/latest/api/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-healthomics-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/healthomics/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/healthomics/pricing/
      - type: FAQ
        url: https://aws.amazon.com/healthomics/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/omics/latest/api/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/omics/latest/api/CommonParameters.html
      - type: JSONSchema
        url: json-schema/healthomics-abort-multipart-read-set-upload-request-schema.json
      - type: JSONLD
        url: json-ld/amazon-healthomics-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/healthomics/
  - type: Documentation
    url: https://docs.aws.amazon.com/omics/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/industries/healthcare/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/omics/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SDK
    url: https://aws.amazon.com/developer/tools/
  - type: CLI
    url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html
  - type: Features
    data:
      - name: Omics Storage
        description: Purpose-built storage for genomic, transcriptomic, and other omics data with automatic optimization.
      - name: Bioinformatics Workflows
        description: Run industry-standard bioinformatics tools and pipelines using WDL and Nextflow workflow definitions.
      - name: Annotation Stores
        description: Store and query genomic annotation data from sources like ClinVar, Ensembl, and custom datasets.
      - name: Variant Stores
        description: Store and query genomic variant data in VCF and other standard bioinformatics formats.
      - name: Sequence Stores
        description: Efficiently store and retrieve genomic sequence read sets in FASTQ, BAM, and CRAM formats.
      - name: Reference Genomes
        description: Store and access reference genome files for alignment and analysis workflows.
      - name: Managed Compute
        description: Fully managed compute infrastructure for running bioinformatics workflows at scale.
  - type: UseCases
    data:
      - name: Whole Genome Sequencing
        description: Store, analyze, and interpret whole genome sequencing data for research and clinical applications.
      - name: Variant Calling Pipelines
        description: Run standard variant calling workflows on genomic data to identify genetic variants.
      - name: Pharmacogenomics Research
        description: Analyze genomic data to understand drug response and develop personalized medicine approaches.
      - name: Population Genomics
        description: Process and analyze large-scale genomic datasets across patient populations for research.
      - name: Clinical Genomics
        description: Support clinical genomics workflows for diagnosis and treatment of genetic disorders.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Import and export omics data using S3 as the primary data source and destination.
      - name: AWS IAM
        description: Control access to HealthOmics resources using IAM roles and policies.
      - name: Amazon CloudWatch
        description: Monitor HealthOmics workflows and storage operations through CloudWatch metrics.
      - name: AWS Lake Formation
        description: Govern and secure genomic data lake access using Lake Formation permissions.
      - name: Amazon Athena
        description: Query genomic annotation and variant data stored in HealthOmics using Athena.
      - name: AWS Batch
        description: Supplement HealthOmics workflows with custom compute jobs using AWS Batch.
  - type: SpectralRules
    url: rules/amazon-healthomics-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-healthomics-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-healthomics-genomics-operations.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
