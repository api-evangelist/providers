---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Aws Healthlake Agentic Access
  operation_count: 13
  slug: aws-healthlake-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 8
apis:
- description: Asynchronous bulk import API for loading FHIR R4 resources from Amazon S3 into a HealthLake data store. Supports starting, describing, and listing import jobs with up to 1 million files and 5 TB total
  name: AWS HealthLake FHIR Import API
  slug: aws-healthlake-fhir-import-api
- description: Asynchronous bulk export API for exporting FHIR R4 resources from a HealthLake data store to Amazon S3. Supports starting, describing, listing, and canceling export jobs, and exporting to analytics-re
  name: AWS HealthLake FHIR Export API
  slug: aws-healthlake-fhir-export-api
- description: 'Transactional FHIR R4 server endpoints for reading, writing, searching, and validating FHIR resources within a data store. Supports SMART on FHIR authorization, FHIR Bulk Data Access, US Core IG, HL7 '
  name: AWS HealthLake FHIR R4 Server API
  slug: aws-healthlake-fhir-r4-server-api
- description: API operations for adding, listing, and removing tags on HealthLake resources such as data stores. Supports up to 200 tags per resource for cost allocation and resource management.
  name: AWS HealthLake Resource Tagging API
  slug: aws-healthlake-resource-tagging-api
- description: Operations for creating, describing, listing, and deleting FHIR R4 data stores
  name: AWS HealthLake Datastore API
  slug: aws-healthlake-datastore-api
- description: Asynchronous bulk export operations for exporting FHIR resources to Amazon S3
  name: AWS HealthLake Export API
  slug: aws-healthlake-export-api
- description: Asynchronous bulk import operations for loading FHIR resources from Amazon S3
  name: AWS HealthLake Import API
  slug: aws-healthlake-import-api
- description: Resource tagging operations for cost allocation and resource management
  name: AWS HealthLake Tags API
  slug: aws-healthlake-tags-api
artifact_total: 72
collections:
- collection_type: postman
  name: Amazon HealthLake Datastore API
  slug: postman-aws-healthlake-datastore-api
- collection_type: postman
  name: Amazon HealthLake Datastore Export API
  slug: postman-aws-healthlake-export-api
- collection_type: postman
  name: Amazon HealthLake Datastore Import API
  slug: postman-aws-healthlake-import-api
- collection_type: postman
  name: Amazon HealthLake Datastore Tags API
  slug: postman-aws-healthlake-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-healthlake/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-healthlake-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-healthlake-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-healthlake-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-healthlake-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-healthlake-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/healthlake/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/healthlake/latest/devguide/what-is-amazon-health-lake.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/healthlake/latest/APIReference/Welcome.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/healthlake/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started-amazon-health-lake.html
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/healthlake/home
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/developer/tools/
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/healthlake/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/healthlake/latest/devguide/releases.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/healthlake/latest/devguide/security-iam.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/hipaa-compliance/
- group: other
  title: ''
  type: PrivateLink
  url: https://docs.aws.amazon.com/healthlake/latest/devguide/vpc-endpoints.html
- group: commercial
  title: ''
  type: Plans
  url: plans/aws-healthlake-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aws-healthlake-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aws-healthlake-finops.yml
- group: company
  title: ''
  type: Partners
  url: https://aws.amazon.com/healthlake/partners/
- group: operate
  title: ''
  type: Forums
  url: https://repost.aws/tags/questions/TAFhiamjeiTUCXp3LbfpEJhw/aws-health-lake
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/publicsector/feed/
created: '2026-06-13'
description: Amazon HealthLake is a HIPAA-eligible, FHIR R4-compliant managed service for importing, transforming, storing, and querying health data from patients and clinical systems. It provides a transactional FHIR server with bulk import/export, medical NLP for unstructured data extraction, SMART on FHIR authorization, and integration with AWS analytics services.
examples:
- key_count: 5
  name: Createfhirdatastore
  slug: CreateFHIRDatastore
- key_count: 5
  name: Deletefhirdatastore
  slug: DeleteFHIRDatastore
- key_count: 5
  name: Describefhirdatastore
  slug: DescribeFHIRDatastore
- key_count: 5
  name: Describefhirexportjob
  slug: DescribeFHIRExportJob
- key_count: 5
  name: Describefhirimportjob
  slug: DescribeFHIRImportJob
- key_count: 5
  name: Listfhirdatastores
  slug: ListFHIRDatastores
- key_count: 5
  name: Listfhirexportjobs
  slug: ListFHIRExportJobs
- key_count: 5
  name: Listfhirimportjobs
  slug: ListFHIRImportJobs
- key_count: 5
  name: Listtagsforresource
  slug: ListTagsForResource
- key_count: 5
  name: Startfhirexportjob
  slug: StartFHIRExportJob
- key_count: 5
  name: Startfhirimportjob
  slug: StartFHIRImportJob
- key_count: 5
  name: Tagresource
  slug: TagResource
- key_count: 5
  name: Untagresource
  slug: UntagResource
finops:
- name: Aws Healthlake Finops
  service_category: ''
  slug: aws-healthlake-finops
graphqls:
- description: 'AWS HealthLake is a HIPAA-eligible, FHIR R4-compliant managed service for importing, transforming, storing, and querying health data from patients and clinical systems. This conceptual GraphQL schema '
  name: AWS HealthLake GraphQL Schema
  slug: aws-healthlake-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-healthlake.png
json_schemas:
- name: CreateFHIRDatastoreRequest
  property_count: 7
  slug: CreateFHIRDatastoreRequest
- name: CreateFHIRDatastoreResponse
  property_count: 4
  slug: CreateFHIRDatastoreResponse
- name: DatastoreProperties
  property_count: 11
  slug: DatastoreProperties
- name: DeleteFHIRDatastoreRequest
  property_count: 1
  slug: DeleteFHIRDatastoreRequest
- name: DeleteFHIRDatastoreResponse
  property_count: 4
  slug: DeleteFHIRDatastoreResponse
- name: DescribeFHIRDatastoreRequest
  property_count: 1
  slug: DescribeFHIRDatastoreRequest
- name: DescribeFHIRDatastoreResponse
  property_count: 1
  slug: DescribeFHIRDatastoreResponse
- name: DescribeFHIRExportJobRequest
  property_count: 2
  slug: DescribeFHIRExportJobRequest
- name: DescribeFHIRExportJobResponse
  property_count: 1
  slug: DescribeFHIRExportJobResponse
- name: DescribeFHIRImportJobRequest
  property_count: 2
  slug: DescribeFHIRImportJobRequest
- name: DescribeFHIRImportJobResponse
  property_count: 1
  slug: DescribeFHIRImportJobResponse
- name: ErrorCause
  property_count: 2
  slug: ErrorCause
- name: ExportJobProperties
  property_count: 9
  slug: ExportJobProperties
- name: IdentityProviderConfiguration
  property_count: 4
  slug: IdentityProviderConfiguration
- name: ImportJobProperties
  property_count: 11
  slug: ImportJobProperties
- name: InputDataConfig
  property_count: 1
  slug: InputDataConfig
- name: KmsEncryptionConfig
  property_count: 2
  slug: KmsEncryptionConfig
- name: ListFHIRDatastoresRequest
  property_count: 3
  slug: ListFHIRDatastoresRequest
- name: ListFHIRDatastoresResponse
  property_count: 2
  slug: ListFHIRDatastoresResponse
- name: ListFHIRExportJobsRequest
  property_count: 7
  slug: ListFHIRExportJobsRequest
- name: ListFHIRExportJobsResponse
  property_count: 2
  slug: ListFHIRExportJobsResponse
- name: ListFHIRImportJobsRequest
  property_count: 7
  slug: ListFHIRImportJobsRequest
- name: ListFHIRImportJobsResponse
  property_count: 2
  slug: ListFHIRImportJobsResponse
- name: ListTagsForResourceRequest
  property_count: 1
  slug: ListTagsForResourceRequest
- name: ListTagsForResourceResponse
  property_count: 1
  slug: ListTagsForResourceResponse
- name: OutputDataConfig
  property_count: 1
  slug: OutputDataConfig
- name: PreloadDataConfig
  property_count: 1
  slug: PreloadDataConfig
- name: S3Configuration
  property_count: 2
  slug: S3Configuration
- name: SseConfiguration
  property_count: 1
  slug: SseConfiguration
- name: StartFHIRExportJobRequest
  property_count: 5
  slug: StartFHIRExportJobRequest
- name: StartFHIRExportJobResponse
  property_count: 3
  slug: StartFHIRExportJobResponse
- name: StartFHIRImportJobRequest
  property_count: 6
  slug: StartFHIRImportJobRequest
- name: StartFHIRImportJobResponse
  property_count: 3
  slug: StartFHIRImportJobResponse
- name: Tag
  property_count: 2
  slug: Tag
- name: TagResourceRequest
  property_count: 2
  slug: TagResourceRequest
- name: UntagResourceRequest
  property_count: 2
  slug: UntagResourceRequest
jsonld:
- class_count: 0
  name: context Context
  property_count: 42
  slug: context
layout: provider
modified: '2026-06-13'
name: AWS HealthLake
nav: Providers
network: true
overview: 'AWS HealthLake publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datastore API, Export API, Import API, and 1 more. Tagged areas include Healthcare, FHIR, Health Data, Clinical Data, and HIPAA.


  The AWS HealthLake catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AWS HealthLake''s developer surface includes authentication, documentation, API reference, pricing, getting-started guide, developer console, CLI, and 18 more developer resources.'
plans:
- name: Aws Healthlake Plans
  plan_count: 2
  slug: aws-healthlake-plans
random_paper: 89
rate_limits:
- limit_count: 33
  name: Aws Healthlake Rate Limits
  slug: aws-healthlake-rate-limits
rules:
- name: AWS HealthLake API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aws-healthlake-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.7
  delta: 3.5
  facets:
    commercial_clarity: 55.3
    contract_quality: 70.9
    developer_ergonomics: 63.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 35.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-healthlake/refs/heads/main/screenshots/aws-healthlake-2026-06-20T172758.png
security:
- kind: authentication
  name: Aws Healthlake Authentication
  slug: aws-healthlake-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Healthlake Domain Security
  slug: aws-healthlake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Healthlake Vulnerability Disclosure
  slug: aws-healthlake-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Healthlake Trust Center
  slug: aws-healthlake-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-healthlake
tags:
- Healthcare
- FHIR
- Health Data
- Clinical Data
- HIPAA
- Interoperability
- NLP
- Medical
- HL7
website: https://aws.amazon.com/healthlake/
---
