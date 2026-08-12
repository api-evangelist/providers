---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Healthlake Agentic Access
  operation_count: 13
  slug: amazon-healthlake-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 13
apis:
- description: 'The #X Amz Target=HealthLake.CreateFHIRDatastore API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.createfhirdatastore.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore API'
  slug: amazon-healthlake-x-amz-target-healthlake-createfhirdatastore-api
- description: 'The #X Amz Target=HealthLake.DeleteFHIRDatastore API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.deletefhirdatastore.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.DeleteFHIRDatastore API'
  slug: amazon-healthlake-x-amz-target-healthlake-deletefhirdatastore-api
- description: 'The #X Amz Target=HealthLake.DescribeFHIRDatastore API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.describefhirdatastore.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.DescribeFHIRDatastore API'
  slug: amazon-healthlake-x-amz-target-healthlake-describefhirdatastore-api
- description: 'The #X Amz Target=HealthLake.DescribeFHIRExportJob API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.describefhirexportjob.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.DescribeFHIRExportJob API'
  slug: amazon-healthlake-x-amz-target-healthlake-describefhirexportjob-api
- description: 'The #X Amz Target=HealthLake.DescribeFHIRImportJob API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.describefhirimportjob.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.DescribeFHIRImportJob API'
  slug: amazon-healthlake-x-amz-target-healthlake-describefhirimportjob-api
- description: 'The #X Amz Target=HealthLake.ListFHIRDatastores API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.listfhirdatastores.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.ListFHIRDatastores API'
  slug: amazon-healthlake-x-amz-target-healthlake-listfhirdatastores-api
- description: 'The #X Amz Target=HealthLake.ListFHIRExportJobs API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.listfhirexportjobs.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.ListFHIRExportJobs API'
  slug: amazon-healthlake-x-amz-target-healthlake-listfhirexportjobs-api
- description: 'The #X Amz Target=HealthLake.ListFHIRImportJobs API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.listfhirimportjobs.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.ListFHIRImportJobs API'
  slug: amazon-healthlake-x-amz-target-healthlake-listfhirimportjobs-api
- description: 'The #X Amz Target=HealthLake.ListTagsForResource API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.listtagsforresource.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.ListTagsForResource API'
  slug: amazon-healthlake-x-amz-target-healthlake-listtagsforresource-api
- description: 'The #X Amz Target=HealthLake.StartFHIRExportJob API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.startfhirexportjob.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.StartFHIRExportJob API'
  slug: amazon-healthlake-x-amz-target-healthlake-startfhirexportjob-api
- description: 'The #X Amz Target=HealthLake.StartFHIRImportJob API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.startfhirimportjob.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.StartFHIRImportJob API'
  slug: amazon-healthlake-x-amz-target-healthlake-startfhirimportjob-api
- description: 'The #X Amz Target=HealthLake.TagResource API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.tagresource.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.TagResource API'
  slug: amazon-healthlake-x-amz-target-healthlake-tagresource-api
- description: 'The #X Amz Target=HealthLake.UntagResource API from Amazon HealthLake — 1 operation(s) for #x amz target=healthlake.untagresource.'
  name: 'Amazon HealthLake #X Amz Target=HealthLake.UntagResource API'
  slug: amazon-healthlake-x-amz-target-healthlake-untagresource-api
arazzos:
- description: Create a FHIR data store and poll its status until it becomes ACTIVE.
  name: Amazon HealthLake Create FHIR Data Store and Wait Until Active
  slug: amazon-healthlake-create-fhir-datastore-and-wait-active-workflow
- description: Delete a FHIR data store and poll its status until it reports DELETED.
  name: Amazon HealthLake Delete FHIR Data Store and Confirm Removal
  slug: amazon-healthlake-delete-fhir-datastore-and-confirm-workflow
- description: Create a FHIR data store, wait until ACTIVE, then export FHIR data and wait until COMPLETED.
  name: Amazon HealthLake Provision FHIR Data Store and Export Data
  slug: amazon-healthlake-provision-datastore-and-export-workflow
- description: Create a FHIR data store, wait until ACTIVE, then import FHIR data and wait until COMPLETED.
  name: Amazon HealthLake Provision FHIR Data Store and Import Data
  slug: amazon-healthlake-provision-datastore-and-import-workflow
- description: Start a FHIR export job, poll it until COMPLETED, then list all export jobs.
  name: Amazon HealthLake Start FHIR Export Job, Poll, and List
  slug: amazon-healthlake-start-export-poll-and-list-workflow
- description: Start a FHIR import job and poll its status until it reaches COMPLETED.
  name: Amazon HealthLake Start FHIR Import Job and Wait Until Completed
  slug: amazon-healthlake-start-import-and-wait-completed-workflow
- description: Start a FHIR import job, poll it until COMPLETED, then list all import jobs.
  name: Amazon HealthLake Start FHIR Import Job, Poll, and List
  slug: amazon-healthlake-start-import-poll-and-list-workflow
artifact_total: 247
collections:
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-createfhirdatastore-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.DeleteFHIRDatastore API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-deletefhirdatastore-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.DescribeFHIRDatastore API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-describefhirdatastore-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.DescribeFHIRExportJob API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-describefhirexportjob-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.DescribeFHIRImportJob API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-describefhirimportjob-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.ListFHIRDatastores API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-listfhirdatastores-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.ListFHIRExportJobs API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-listfhirexportjobs-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.ListFHIRImportJobs API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-listfhirimportjobs-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.ListTagsForResource API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-listtagsforresource-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.StartFHIRExportJob API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-startfhirexportjob-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.StartFHIRImportJob API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-startfhirimportjob-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.TagResource API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-tagresource-api
- collection_type: postman
  name: 'Amazon HealthLake #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.CreateFHIRDatastore #X Amz Target=HealthLake.UntagResource API'
  slug: postman-amazon-healthlake-x-amz-target-healthlake-untagresource-api
- collection_type: postman
  name: Amazon HealthLake
  slug: postman-amazon-healthlake
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-healthlake-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-healthlake-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-healthlake-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-healthlake-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-healthlake-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-healthlake/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-create-fhir-datastore-and-wait-active-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-delete-fhir-datastore-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-provision-datastore-and-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-provision-datastore-and-import-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-start-export-poll-and-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-start-import-and-wait-completed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthlake-start-import-poll-and-list-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/healthlake/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/healthlake/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/industries/healthcare/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/healthlake/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/developer/tools/
- group: build
  title: ''
  type: CLI
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-healthlake-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-healthlake-vocabulary.yaml
created: '2026-03-16'
description: Amazon HealthLake is a HIPAA-eligible service that gives healthcare providers, health insurance companies, and pharmaceutical companies the ability to store, transform, query, and analyze health data at scale in the cloud. It uses the Fast Healthcare Interoperability Resources (FHIR) standard.
examples:
- key_count: 7
  name: Healthlake Create Fhir Datastore Request Example
  slug: healthlake-create-fhir-datastore-request-example
- key_count: 4
  name: Healthlake Create Fhir Datastore Response Example
  slug: healthlake-create-fhir-datastore-response-example
- key_count: 4
  name: Healthlake Datastore Filter Example
  slug: healthlake-datastore-filter-example
- key_count: 10
  name: Healthlake Datastore Properties Example
  slug: healthlake-datastore-properties-example
- key_count: 1
  name: Healthlake Delete Fhir Datastore Request Example
  slug: healthlake-delete-fhir-datastore-request-example
- key_count: 4
  name: Healthlake Delete Fhir Datastore Response Example
  slug: healthlake-delete-fhir-datastore-response-example
- key_count: 1
  name: Healthlake Describe Fhir Datastore Request Example
  slug: healthlake-describe-fhir-datastore-request-example
- key_count: 1
  name: Healthlake Describe Fhir Datastore Response Example
  slug: healthlake-describe-fhir-datastore-response-example
- key_count: 2
  name: Healthlake Describe Fhir Export Job Request Example
  slug: healthlake-describe-fhir-export-job-request-example
- key_count: 1
  name: Healthlake Describe Fhir Export Job Response Example
  slug: healthlake-describe-fhir-export-job-response-example
- key_count: 2
  name: Healthlake Describe Fhir Import Job Request Example
  slug: healthlake-describe-fhir-import-job-request-example
- key_count: 1
  name: Healthlake Describe Fhir Import Job Response Example
  slug: healthlake-describe-fhir-import-job-response-example
- key_count: 9
  name: Healthlake Export Job Properties Example
  slug: healthlake-export-job-properties-example
- key_count: 4
  name: Healthlake Identity Provider Configuration Example
  slug: healthlake-identity-provider-configuration-example
- key_count: 10
  name: Healthlake Import Job Properties Example
  slug: healthlake-import-job-properties-example
- key_count: 1
  name: Healthlake Input Data Config Example
  slug: healthlake-input-data-config-example
- key_count: 2
  name: Healthlake Kms Encryption Config Example
  slug: healthlake-kms-encryption-config-example
- key_count: 3
  name: Healthlake List Fhir Datastores Request Example
  slug: healthlake-list-fhir-datastores-request-example
- key_count: 2
  name: Healthlake List Fhir Datastores Response Example
  slug: healthlake-list-fhir-datastores-response-example
- key_count: 7
  name: Healthlake List Fhir Export Jobs Request Example
  slug: healthlake-list-fhir-export-jobs-request-example
- key_count: 2
  name: Healthlake List Fhir Export Jobs Response Example
  slug: healthlake-list-fhir-export-jobs-response-example
- key_count: 7
  name: Healthlake List Fhir Import Jobs Request Example
  slug: healthlake-list-fhir-import-jobs-request-example
- key_count: 2
  name: Healthlake List Fhir Import Jobs Response Example
  slug: healthlake-list-fhir-import-jobs-response-example
- key_count: 1
  name: Healthlake List Tags For Resource Request Example
  slug: healthlake-list-tags-for-resource-request-example
- key_count: 1
  name: Healthlake List Tags For Resource Response Example
  slug: healthlake-list-tags-for-resource-response-example
- key_count: 1
  name: Healthlake Output Data Config Example
  slug: healthlake-output-data-config-example
- key_count: 1
  name: Healthlake Preload Data Config Example
  slug: healthlake-preload-data-config-example
- key_count: 2
  name: Healthlake S3 Configuration Example
  slug: healthlake-s3-configuration-example
- key_count: 1
  name: Healthlake Sse Configuration Example
  slug: healthlake-sse-configuration-example
- key_count: 5
  name: Healthlake Start Fhir Export Job Request Example
  slug: healthlake-start-fhir-export-job-request-example
- key_count: 3
  name: Healthlake Start Fhir Export Job Response Example
  slug: healthlake-start-fhir-export-job-response-example
- key_count: 6
  name: Healthlake Start Fhir Import Job Request Example
  slug: healthlake-start-fhir-import-job-request-example
- key_count: 3
  name: Healthlake Start Fhir Import Job Response Example
  slug: healthlake-start-fhir-import-job-response-example
- key_count: 2
  name: Healthlake Tag Example
  slug: healthlake-tag-example
- key_count: 2
  name: Healthlake Tag Resource Request Example
  slug: healthlake-tag-resource-request-example
- key_count: 0
  name: Healthlake Tag Resource Response Example
  slug: healthlake-tag-resource-response-example
- key_count: 2
  name: Healthlake Untag Resource Request Example
  slug: healthlake-untag-resource-request-example
- key_count: 0
  name: Healthlake Untag Resource Response Example
  slug: healthlake-untag-resource-response-example
features:
- description: Fully compliant with the FHIR R4 standard for healthcare data interoperability.
  name: FHIR Compliance
- description: HIPAA-eligible service for storing and processing protected health information.
  name: HIPAA-Eligible
- description: Bulk import FHIR-formatted health data from Amazon S3 with automated validation.
  name: Integrated Data Import
- description: Export FHIR health data to Amazon S3 for analytics, archiving, or migration.
  name: Data Export
- description: Query FHIR resources using standard FHIR search operations for clinical workflows.
  name: Integrated Search
- description: Built-in de-identification capabilities for removing PHI from health data.
  name: Automated De-identification
- description: Integrated analytics with Amazon Comprehend Medical and other AWS analytics services.
  name: Analytics Integration
finops:
- name: Amazon Healthlake Finops
  service_category: API
  slug: amazon-healthlake-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-healthlake.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: healthlake-access-denied-exception
- name: AmazonResourceName
  property_count: 0
  slug: healthlake-amazon-resource-name
- name: AuthorizationStrategy
  property_count: 0
  slug: healthlake-authorization-strategy
- name: Boolean
  property_count: 0
  slug: healthlake-boolean
- name: BoundedLengthString
  property_count: 0
  slug: healthlake-bounded-length-string
- name: ClientTokenString
  property_count: 0
  slug: healthlake-client-token-string
- name: CmkType
  property_count: 0
  slug: healthlake-cmk-type
- name: ConfigurationMetadata
  property_count: 0
  slug: healthlake-configuration-metadata
- name: ConflictException
  property_count: 0
  slug: healthlake-conflict-exception
- name: CreateFHIRDatastoreRequest
  property_count: 7
  slug: healthlake-create-fhir-datastore-request
- name: CreateFHIRDatastoreResponse
  property_count: 4
  slug: healthlake-create-fhir-datastore-response
- name: DatastoreArn
  property_count: 0
  slug: healthlake-datastore-arn
- name: DatastoreFilter
  property_count: 4
  slug: healthlake-datastore-filter
- name: DatastoreId
  property_count: 0
  slug: healthlake-datastore-id
- name: DatastoreName
  property_count: 0
  slug: healthlake-datastore-name
- name: DatastorePropertiesList
  property_count: 0
  slug: healthlake-datastore-properties-list
- name: DatastoreProperties
  property_count: 10
  slug: healthlake-datastore-properties
- name: DatastoreStatus
  property_count: 0
  slug: healthlake-datastore-status
- name: DeleteFHIRDatastoreRequest
  property_count: 1
  slug: healthlake-delete-fhir-datastore-request
- name: DeleteFHIRDatastoreResponse
  property_count: 4
  slug: healthlake-delete-fhir-datastore-response
- name: DescribeFHIRDatastoreRequest
  property_count: 1
  slug: healthlake-describe-fhir-datastore-request
- name: DescribeFHIRDatastoreResponse
  property_count: 1
  slug: healthlake-describe-fhir-datastore-response
- name: DescribeFHIRExportJobRequest
  property_count: 2
  slug: healthlake-describe-fhir-export-job-request
- name: DescribeFHIRExportJobResponse
  property_count: 1
  slug: healthlake-describe-fhir-export-job-response
- name: DescribeFHIRImportJobRequest
  property_count: 2
  slug: healthlake-describe-fhir-import-job-request
- name: DescribeFHIRImportJobResponse
  property_count: 1
  slug: healthlake-describe-fhir-import-job-response
- name: EncryptionKeyID
  property_count: 0
  slug: healthlake-encryption-key-id
- name: ExportJobPropertiesList
  property_count: 0
  slug: healthlake-export-job-properties-list
- name: ExportJobProperties
  property_count: 9
  slug: healthlake-export-job-properties
- name: FHIRVersion
  property_count: 0
  slug: healthlake-fhir-version
- name: IamRoleArn
  property_count: 0
  slug: healthlake-iam-role-arn
- name: IdentityProviderConfiguration
  property_count: 4
  slug: healthlake-identity-provider-configuration
- name: ImportJobPropertiesList
  property_count: 0
  slug: healthlake-import-job-properties-list
- name: ImportJobProperties
  property_count: 10
  slug: healthlake-import-job-properties
- name: InputDataConfig
  property_count: 1
  slug: healthlake-input-data-config
- name: InternalServerException
  property_count: 0
  slug: healthlake-internal-server-exception
- name: JobId
  property_count: 0
  slug: healthlake-job-id
- name: JobName
  property_count: 0
  slug: healthlake-job-name
- name: JobStatus
  property_count: 0
  slug: healthlake-job-status
- name: KmsEncryptionConfig
  property_count: 2
  slug: healthlake-kms-encryption-config
- name: LambdaArn
  property_count: 0
  slug: healthlake-lambda-arn
- name: ListFHIRDatastoresRequest
  property_count: 3
  slug: healthlake-list-fhir-datastores-request
- name: ListFHIRDatastoresResponse
  property_count: 2
  slug: healthlake-list-fhir-datastores-response
- name: ListFHIRExportJobsRequest
  property_count: 7
  slug: healthlake-list-fhir-export-jobs-request
- name: ListFHIRExportJobsResponse
  property_count: 2
  slug: healthlake-list-fhir-export-jobs-response
- name: ListFHIRImportJobsRequest
  property_count: 7
  slug: healthlake-list-fhir-import-jobs-request
- name: ListFHIRImportJobsResponse
  property_count: 2
  slug: healthlake-list-fhir-import-jobs-response
- name: ListTagsForResourceRequest
  property_count: 1
  slug: healthlake-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: healthlake-list-tags-for-resource-response
- name: MaxResultsInteger
  property_count: 0
  slug: healthlake-max-results-integer
- name: Message
  property_count: 0
  slug: healthlake-message
- name: NextToken
  property_count: 0
  slug: healthlake-next-token
- name: OutputDataConfig
  property_count: 1
  slug: healthlake-output-data-config
- name: PreloadDataConfig
  property_count: 1
  slug: healthlake-preload-data-config
- name: PreloadDataType
  property_count: 0
  slug: healthlake-preload-data-type
- name: ResourceNotFoundException
  property_count: 0
  slug: healthlake-resource-not-found-exception
- name: S3Configuration
  property_count: 2
  slug: healthlake-s3-configuration
- name: S3Uri
  property_count: 0
  slug: healthlake-s3-uri
- name: SseConfiguration
  property_count: 1
  slug: healthlake-sse-configuration
- name: StartFHIRExportJobRequest
  property_count: 5
  slug: healthlake-start-fhir-export-job-request
- name: StartFHIRExportJobResponse
  property_count: 3
  slug: healthlake-start-fhir-export-job-response
- name: StartFHIRImportJobRequest
  property_count: 6
  slug: healthlake-start-fhir-import-job-request
- name: StartFHIRImportJobResponse
  property_count: 3
  slug: healthlake-start-fhir-import-job-response
- name: String
  property_count: 0
  slug: healthlake-string
- name: TagKeyList
  property_count: 0
  slug: healthlake-tag-key-list
- name: TagKey
  property_count: 0
  slug: healthlake-tag-key
- name: TagList
  property_count: 0
  slug: healthlake-tag-list
- name: TagResourceRequest
  property_count: 2
  slug: healthlake-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: healthlake-tag-resource-response
- name: Tag
  property_count: 2
  slug: healthlake-tag
- name: TagValue
  property_count: 0
  slug: healthlake-tag-value
- name: ThrottlingException
  property_count: 0
  slug: healthlake-throttling-exception
- name: Timestamp
  property_count: 0
  slug: healthlake-timestamp
- name: UntagResourceRequest
  property_count: 2
  slug: healthlake-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: healthlake-untag-resource-response
- name: ValidationException
  property_count: 0
  slug: healthlake-validation-exception
json_structures:
- name: Healthlake Access Denied Exception Structure
  property_count: 0
  slug: healthlake-access-denied-exception-structure
- name: Healthlake Amazon Resource Name Structure
  property_count: 0
  slug: healthlake-amazon-resource-name-structure
- name: Healthlake Authorization Strategy Structure
  property_count: 0
  slug: healthlake-authorization-strategy-structure
- name: Healthlake Boolean Structure
  property_count: 0
  slug: healthlake-boolean-structure
- name: Healthlake Bounded Length String Structure
  property_count: 0
  slug: healthlake-bounded-length-string-structure
- name: Healthlake Client Token String Structure
  property_count: 0
  slug: healthlake-client-token-string-structure
- name: Healthlake Cmk Type Structure
  property_count: 0
  slug: healthlake-cmk-type-structure
- name: Healthlake Configuration Metadata Structure
  property_count: 0
  slug: healthlake-configuration-metadata-structure
- name: Healthlake Conflict Exception Structure
  property_count: 0
  slug: healthlake-conflict-exception-structure
- name: Healthlake Create Fhir Datastore Request Structure
  property_count: 7
  slug: healthlake-create-fhir-datastore-request-structure
- name: Healthlake Create Fhir Datastore Response Structure
  property_count: 4
  slug: healthlake-create-fhir-datastore-response-structure
- name: Healthlake Datastore Arn Structure
  property_count: 0
  slug: healthlake-datastore-arn-structure
- name: Healthlake Datastore Filter Structure
  property_count: 4
  slug: healthlake-datastore-filter-structure
- name: Healthlake Datastore Id Structure
  property_count: 0
  slug: healthlake-datastore-id-structure
- name: Healthlake Datastore Name Structure
  property_count: 0
  slug: healthlake-datastore-name-structure
- name: Healthlake Datastore Properties List Structure
  property_count: 0
  slug: healthlake-datastore-properties-list-structure
- name: Healthlake Datastore Properties Structure
  property_count: 10
  slug: healthlake-datastore-properties-structure
- name: Healthlake Datastore Status Structure
  property_count: 0
  slug: healthlake-datastore-status-structure
- name: Healthlake Delete Fhir Datastore Request Structure
  property_count: 1
  slug: healthlake-delete-fhir-datastore-request-structure
- name: Healthlake Delete Fhir Datastore Response Structure
  property_count: 4
  slug: healthlake-delete-fhir-datastore-response-structure
- name: Healthlake Describe Fhir Datastore Request Structure
  property_count: 1
  slug: healthlake-describe-fhir-datastore-request-structure
- name: Healthlake Describe Fhir Datastore Response Structure
  property_count: 1
  slug: healthlake-describe-fhir-datastore-response-structure
- name: Healthlake Describe Fhir Export Job Request Structure
  property_count: 2
  slug: healthlake-describe-fhir-export-job-request-structure
- name: Healthlake Describe Fhir Export Job Response Structure
  property_count: 1
  slug: healthlake-describe-fhir-export-job-response-structure
- name: Healthlake Describe Fhir Import Job Request Structure
  property_count: 2
  slug: healthlake-describe-fhir-import-job-request-structure
- name: Healthlake Describe Fhir Import Job Response Structure
  property_count: 1
  slug: healthlake-describe-fhir-import-job-response-structure
- name: Healthlake Encryption Key Id Structure
  property_count: 0
  slug: healthlake-encryption-key-id-structure
- name: Healthlake Export Job Properties List Structure
  property_count: 0
  slug: healthlake-export-job-properties-list-structure
- name: Healthlake Export Job Properties Structure
  property_count: 9
  slug: healthlake-export-job-properties-structure
- name: Healthlake Fhir Version Structure
  property_count: 0
  slug: healthlake-fhir-version-structure
- name: Healthlake Iam Role Arn Structure
  property_count: 0
  slug: healthlake-iam-role-arn-structure
- name: Healthlake Identity Provider Configuration Structure
  property_count: 4
  slug: healthlake-identity-provider-configuration-structure
- name: Healthlake Import Job Properties List Structure
  property_count: 0
  slug: healthlake-import-job-properties-list-structure
- name: Healthlake Import Job Properties Structure
  property_count: 10
  slug: healthlake-import-job-properties-structure
- name: Healthlake Input Data Config Structure
  property_count: 1
  slug: healthlake-input-data-config-structure
- name: Healthlake Internal Server Exception Structure
  property_count: 0
  slug: healthlake-internal-server-exception-structure
- name: Healthlake Job Id Structure
  property_count: 0
  slug: healthlake-job-id-structure
- name: Healthlake Job Name Structure
  property_count: 0
  slug: healthlake-job-name-structure
- name: Healthlake Job Status Structure
  property_count: 0
  slug: healthlake-job-status-structure
- name: Healthlake Kms Encryption Config Structure
  property_count: 2
  slug: healthlake-kms-encryption-config-structure
- name: Healthlake Lambda Arn Structure
  property_count: 0
  slug: healthlake-lambda-arn-structure
- name: Healthlake List Fhir Datastores Request Structure
  property_count: 3
  slug: healthlake-list-fhir-datastores-request-structure
- name: Healthlake List Fhir Datastores Response Structure
  property_count: 2
  slug: healthlake-list-fhir-datastores-response-structure
- name: Healthlake List Fhir Export Jobs Request Structure
  property_count: 7
  slug: healthlake-list-fhir-export-jobs-request-structure
- name: Healthlake List Fhir Export Jobs Response Structure
  property_count: 2
  slug: healthlake-list-fhir-export-jobs-response-structure
- name: Healthlake List Fhir Import Jobs Request Structure
  property_count: 7
  slug: healthlake-list-fhir-import-jobs-request-structure
- name: Healthlake List Fhir Import Jobs Response Structure
  property_count: 2
  slug: healthlake-list-fhir-import-jobs-response-structure
- name: Healthlake List Tags For Resource Request Structure
  property_count: 1
  slug: healthlake-list-tags-for-resource-request-structure
- name: Healthlake List Tags For Resource Response Structure
  property_count: 1
  slug: healthlake-list-tags-for-resource-response-structure
- name: Healthlake Max Results Integer Structure
  property_count: 0
  slug: healthlake-max-results-integer-structure
- name: Healthlake Message Structure
  property_count: 0
  slug: healthlake-message-structure
- name: Healthlake Next Token Structure
  property_count: 0
  slug: healthlake-next-token-structure
- name: Healthlake Output Data Config Structure
  property_count: 1
  slug: healthlake-output-data-config-structure
- name: Healthlake Preload Data Config Structure
  property_count: 1
  slug: healthlake-preload-data-config-structure
- name: Healthlake Preload Data Type Structure
  property_count: 0
  slug: healthlake-preload-data-type-structure
- name: Healthlake Resource Not Found Exception Structure
  property_count: 0
  slug: healthlake-resource-not-found-exception-structure
- name: Healthlake S3 Configuration Structure
  property_count: 2
  slug: healthlake-s3-configuration-structure
- name: Healthlake S3 Uri Structure
  property_count: 0
  slug: healthlake-s3-uri-structure
- name: Healthlake Sse Configuration Structure
  property_count: 1
  slug: healthlake-sse-configuration-structure
- name: Healthlake Start Fhir Export Job Request Structure
  property_count: 5
  slug: healthlake-start-fhir-export-job-request-structure
- name: Healthlake Start Fhir Export Job Response Structure
  property_count: 3
  slug: healthlake-start-fhir-export-job-response-structure
- name: Healthlake Start Fhir Import Job Request Structure
  property_count: 6
  slug: healthlake-start-fhir-import-job-request-structure
- name: Healthlake Start Fhir Import Job Response Structure
  property_count: 3
  slug: healthlake-start-fhir-import-job-response-structure
- name: Healthlake String Structure
  property_count: 0
  slug: healthlake-string-structure
- name: Healthlake Tag Key List Structure
  property_count: 0
  slug: healthlake-tag-key-list-structure
- name: Healthlake Tag Key Structure
  property_count: 0
  slug: healthlake-tag-key-structure
- name: Healthlake Tag List Structure
  property_count: 0
  slug: healthlake-tag-list-structure
- name: Healthlake Tag Resource Request Structure
  property_count: 2
  slug: healthlake-tag-resource-request-structure
- name: Healthlake Tag Resource Response Structure
  property_count: 0
  slug: healthlake-tag-resource-response-structure
- name: Healthlake Tag Structure
  property_count: 2
  slug: healthlake-tag-structure
- name: Healthlake Tag Value Structure
  property_count: 0
  slug: healthlake-tag-value-structure
- name: Healthlake Throttling Exception Structure
  property_count: 0
  slug: healthlake-throttling-exception-structure
- name: Healthlake Timestamp Structure
  property_count: 0
  slug: healthlake-timestamp-structure
- name: Healthlake Untag Resource Request Structure
  property_count: 2
  slug: healthlake-untag-resource-request-structure
- name: Healthlake Untag Resource Response Structure
  property_count: 0
  slug: healthlake-untag-resource-response-structure
- name: Healthlake Validation Exception Structure
  property_count: 0
  slug: healthlake-validation-exception-structure
jsonld:
- class_count: 76
  name: Amazon Healthlake Context
  property_count: 0
  slug: amazon-healthlake-context
layout: provider
modified: '2026-05-19'
name: Amazon HealthLake
nav: Providers
network: true
overview: 'Amazon HealthLake publishes 13 APIs on the [APIs.io](https://apis.io/) network, including #X Amz Target=HealthLake.CreateFHIRDatastore API, #X Amz Target=HealthLake.DeleteFHIRDatastore API, #X Amz Target=HealthLake.DescribeFHIRDatastore API, and 10 more. Tagged areas include FHIR, Health Data, Healthcare, HIPAA, and Cloud Computing.


  The Amazon HealthLake catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon HealthLake''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 21 more developer resources.'
plans:
- name: Amazon Healthlake Plans Pricing
  plan_count: 3
  slug: amazon-healthlake-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 5
  name: Amazon Healthlake Rate Limits
  slug: amazon-healthlake-rate-limits
rules:
- name: Amazon HealthLake API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-healthlake-jsonschema-spectral-rules
- name: Amazon HealthLake API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 8
  slug: amazon-healthlake-spectral-rules
score:
  band: strong
  composite: 58.3
  delta: -5.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 71.6
    developer_ergonomics: 58.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-healthlake/refs/heads/main/screenshots/amazon-healthlake-2026-07-25T200010.png
security:
- kind: authentication
  name: Amazon Healthlake Authentication
  slug: amazon-healthlake-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Healthlake Domain Security
  slug: amazon-healthlake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Healthlake Vulnerability Disclosure
  slug: amazon-healthlake-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Healthlake Trust Center
  slug: amazon-healthlake-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-healthlake
tags:
- FHIR
- Health Data
- Healthcare
- HIPAA
- Cloud Computing
use_cases:
- description: Create a centralized FHIR-compliant repository for clinical data from multiple sources.
  name: Clinical Data Repository
- description: Enable interoperable health data exchange between healthcare providers and payers.
  name: Health Data Exchange
- description: Analyze aggregated health data to identify trends and manage population health programs.
  name: Population Health Management
- description: Apply machine learning to FHIR data to generate clinical insights and predictions.
  name: AI-Powered Clinical Insights
- description: Create de-identified research datasets from FHIR health records for clinical studies.
  name: Research Data Platform
website: https://aws.amazon.com/healthlake/
---
