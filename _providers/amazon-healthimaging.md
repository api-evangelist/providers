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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Healthimaging Agentic Access
  operation_count: 18
  slug: amazon-healthimaging-agentic-access
  summary_line: 18 operations · 13 acting
api_count: 5
apis:
- description: The Datastore API from Amazon HealthImaging — 10 operation(s) for datastore.
  name: Amazon HealthImaging Datastore API
  slug: amazon-healthimaging-datastore-api
- description: The GetDICOMImportJob API from Amazon HealthImaging — 1 operation(s) for getdicomimportjob.
  name: Amazon HealthImaging GetDICOMImportJob API
  slug: amazon-healthimaging-getdicomimportjob-api
- description: The ListDICOMImportJobs API from Amazon HealthImaging — 1 operation(s) for listdicomimportjobs.
  name: Amazon HealthImaging ListDICOMImportJobs API
  slug: amazon-healthimaging-listdicomimportjobs-api
- description: The StartDICOMImportJob API from Amazon HealthImaging — 1 operation(s) for startdicomimportjob.
  name: Amazon HealthImaging StartDICOMImportJob API
  slug: amazon-healthimaging-startdicomimportjob-api
- description: The Tags API from Amazon HealthImaging — 2 operation(s) for tags.
  name: Amazon HealthImaging Tags API
  slug: amazon-healthimaging-tags-api
arazzos:
- description: List completed import jobs, read the most recent job's detail, then search the imported image sets.
  name: Amazon HealthImaging Audit Completed Imports
  slug: amazon-healthimaging-audit-completed-imports-workflow
- description: Resolve a source image set version, copy it to a destination, then poll until ACTIVE.
  name: Amazon HealthImaging Copy Image Set
  slug: amazon-healthimaging-copy-image-set-workflow
- description: Search image sets by DICOM patient ID, then read the top match's properties and metadata.
  name: Amazon HealthImaging Find Image Set by Patient
  slug: amazon-healthimaging-find-image-set-by-patient-workflow
- description: Start a DICOM import job, poll until COMPLETED, then search the imported image sets.
  name: Amazon HealthImaging Import DICOM and Search
  slug: amazon-healthimaging-import-dicom-and-search-workflow
- description: Read image set properties, fetch its metadata, then retrieve an image frame.
  name: Amazon HealthImaging Inspect Image Set
  slug: amazon-healthimaging-inspect-image-set-workflow
- description: Create a data store, wait until ACTIVE, then start a DICOM import and poll to completion.
  name: Amazon HealthImaging Onboard Data Store and Import
  slug: amazon-healthimaging-onboard-datastore-and-import-workflow
- description: Create a data store and poll until it becomes ACTIVE before use.
  name: Amazon HealthImaging Provision Data Store
  slug: amazon-healthimaging-provision-datastore-workflow
- description: Resolve an image set's ARN, attach tags to it, then list the tags back.
  name: Amazon HealthImaging Tag Image Set
  slug: amazon-healthimaging-tag-image-set-workflow
- description: Read an image set's latest version, apply DICOM metadata updates, then list its versions.
  name: Amazon HealthImaging Update Image Set Metadata
  slug: amazon-healthimaging-update-image-set-metadata-workflow
artifact_total: 326
collections:
- collection_type: postman
  name: AWS Health Imaging Datastore API
  slug: postman-amazon-healthimaging-datastore-api
- collection_type: postman
  name: AWS Health Imaging Datastore GetDICOMImportJob API
  slug: postman-amazon-healthimaging-getdicomimportjob-api
- collection_type: postman
  name: AWS Health Imaging Datastore ListDICOMImportJobs API
  slug: postman-amazon-healthimaging-listdicomimportjobs-api
- collection_type: postman
  name: AWS Health Imaging Datastore StartDICOMImportJob API
  slug: postman-amazon-healthimaging-startdicomimportjob-api
- collection_type: postman
  name: AWS Health Imaging Datastore Tags API
  slug: postman-amazon-healthimaging-tags-api
- collection_type: postman
  name: AWS Health Imaging
  slug: postman-amazon-healthimaging
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-healthimaging-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-healthimaging-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-healthimaging-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-healthimaging-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-healthimaging-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-healthimaging/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-audit-completed-imports-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-copy-image-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-find-image-set-by-patient-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-import-dicom-and-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-inspect-image-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-onboard-datastore-and-import-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-provision-datastore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-tag-image-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthimaging-update-image-set-metadata-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/healthimaging/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/healthimaging/
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
  url: https://console.aws.amazon.com/healthimaging/
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
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/index.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-healthimaging-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-healthimaging-vocabulary.yaml
created: '2026-03-16'
description: AWS HealthImaging is a HIPAA-eligible service that helps healthcare providers and their software partners store, transform, and apply machine learning to medical images. It provides sub-second image retrieval and enables scaling from hundreds to millions of medical images.
examples:
- key_count: 2
  name: Healthimaging Copy Destination Image Set Example
  slug: healthimaging-copy-destination-image-set-example
- key_count: 7
  name: Healthimaging Copy Destination Image Set Properties Example
  slug: healthimaging-copy-destination-image-set-properties-example
- key_count: 2
  name: Healthimaging Copy Image Set Information Example
  slug: healthimaging-copy-image-set-information-example
- key_count: 1
  name: Healthimaging Copy Image Set Request Example
  slug: healthimaging-copy-image-set-request-example
- key_count: 3
  name: Healthimaging Copy Image Set Response Example
  slug: healthimaging-copy-image-set-response-example
- key_count: 1
  name: Healthimaging Copy Source Image Set Information Example
  slug: healthimaging-copy-source-image-set-information-example
- key_count: 7
  name: Healthimaging Copy Source Image Set Properties Example
  slug: healthimaging-copy-source-image-set-properties-example
- key_count: 4
  name: Healthimaging Create Datastore Request Example
  slug: healthimaging-create-datastore-request-example
- key_count: 2
  name: Healthimaging Create Datastore Response Example
  slug: healthimaging-create-datastore-response-example
- key_count: 7
  name: Healthimaging Datastore Properties Example
  slug: healthimaging-datastore-properties-example
- key_count: 6
  name: Healthimaging Datastore Summary Example
  slug: healthimaging-datastore-summary-example
- key_count: 0
  name: Healthimaging Delete Datastore Request Example
  slug: healthimaging-delete-datastore-request-example
- key_count: 2
  name: Healthimaging Delete Datastore Response Example
  slug: healthimaging-delete-datastore-response-example
- key_count: 0
  name: Healthimaging Delete Image Set Request Example
  slug: healthimaging-delete-image-set-request-example
- key_count: 4
  name: Healthimaging Delete Image Set Response Example
  slug: healthimaging-delete-image-set-response-example
- key_count: 10
  name: Healthimaging Dicom Import Job Properties Example
  slug: healthimaging-dicom-import-job-properties-example
- key_count: 8
  name: Healthimaging Dicom Import Job Summary Example
  slug: healthimaging-dicom-import-job-summary-example
- key_count: 2
  name: Healthimaging Dicom Study Date And Time Example
  slug: healthimaging-dicom-study-date-and-time-example
- key_count: 12
  name: Healthimaging Dicom Tags Example
  slug: healthimaging-dicom-tags-example
- key_count: 2
  name: Healthimaging Dicom Updates Example
  slug: healthimaging-dicom-updates-example
- key_count: 0
  name: Healthimaging Get Datastore Request Example
  slug: healthimaging-get-datastore-request-example
- key_count: 1
  name: Healthimaging Get Datastore Response Example
  slug: healthimaging-get-datastore-response-example
- key_count: 0
  name: Healthimaging Get Dicom Import Job Request Example
  slug: healthimaging-get-dicom-import-job-request-example
- key_count: 1
  name: Healthimaging Get Dicom Import Job Response Example
  slug: healthimaging-get-dicom-import-job-response-example
- key_count: 1
  name: Healthimaging Get Image Frame Request Example
  slug: healthimaging-get-image-frame-request-example
- key_count: 1
  name: Healthimaging Get Image Frame Response Example
  slug: healthimaging-get-image-frame-response-example
- key_count: 0
  name: Healthimaging Get Image Set Metadata Request Example
  slug: healthimaging-get-image-set-metadata-request-example
- key_count: 1
  name: Healthimaging Get Image Set Metadata Response Example
  slug: healthimaging-get-image-set-metadata-response-example
- key_count: 0
  name: Healthimaging Get Image Set Request Example
  slug: healthimaging-get-image-set-request-example
- key_count: 10
  name: Healthimaging Get Image Set Response Example
  slug: healthimaging-get-image-set-response-example
- key_count: 1
  name: Healthimaging Image Frame Information Example
  slug: healthimaging-image-frame-information-example
- key_count: 8
  name: Healthimaging Image Set Properties Example
  slug: healthimaging-image-set-properties-example
- key_count: 5
  name: Healthimaging Image Sets Metadata Summary Example
  slug: healthimaging-image-sets-metadata-summary-example
- key_count: 0
  name: Healthimaging List Datastores Request Example
  slug: healthimaging-list-datastores-request-example
- key_count: 2
  name: Healthimaging List Datastores Response Example
  slug: healthimaging-list-datastores-response-example
- key_count: 0
  name: Healthimaging List Dicom Import Jobs Request Example
  slug: healthimaging-list-dicom-import-jobs-request-example
- key_count: 2
  name: Healthimaging List Dicom Import Jobs Response Example
  slug: healthimaging-list-dicom-import-jobs-response-example
- key_count: 0
  name: Healthimaging List Image Set Versions Request Example
  slug: healthimaging-list-image-set-versions-request-example
- key_count: 2
  name: Healthimaging List Image Set Versions Response Example
  slug: healthimaging-list-image-set-versions-response-example
- key_count: 0
  name: Healthimaging List Tags For Resource Request Example
  slug: healthimaging-list-tags-for-resource-request-example
- key_count: 1
  name: Healthimaging List Tags For Resource Response Example
  slug: healthimaging-list-tags-for-resource-response-example
- key_count: 1
  name: Healthimaging Metadata Updates Example
  slug: healthimaging-metadata-updates-example
- key_count: 6
  name: Healthimaging Search By Attribute Value Example
  slug: healthimaging-search-by-attribute-value-example
- key_count: 1
  name: Healthimaging Search Criteria Example
  slug: healthimaging-search-criteria-example
- key_count: 2
  name: Healthimaging Search Filter Example
  slug: healthimaging-search-filter-example
- key_count: 1
  name: Healthimaging Search Image Sets Request Example
  slug: healthimaging-search-image-sets-request-example
- key_count: 2
  name: Healthimaging Search Image Sets Response Example
  slug: healthimaging-search-image-sets-response-example
- key_count: 5
  name: Healthimaging Start Dicom Import Job Request Example
  slug: healthimaging-start-dicom-import-job-request-example
- key_count: 4
  name: Healthimaging Start Dicom Import Job Response Example
  slug: healthimaging-start-dicom-import-job-response-example
- key_count: 0
  name: Healthimaging Tag Map Example
  slug: healthimaging-tag-map-example
- key_count: 1
  name: Healthimaging Tag Resource Request Example
  slug: healthimaging-tag-resource-request-example
- key_count: 0
  name: Healthimaging Tag Resource Response Example
  slug: healthimaging-tag-resource-response-example
- key_count: 0
  name: Healthimaging Untag Resource Request Example
  slug: healthimaging-untag-resource-request-example
- key_count: 0
  name: Healthimaging Untag Resource Response Example
  slug: healthimaging-untag-resource-response-example
- key_count: 1
  name: Healthimaging Update Image Set Metadata Request Example
  slug: healthimaging-update-image-set-metadata-request-example
- key_count: 8
  name: Healthimaging Update Image Set Metadata Response Example
  slug: healthimaging-update-image-set-metadata-response-example
features:
- description: Fully HIPAA-eligible service for storing protected health information including medical images.
  name: HIPAA-Eligible Storage
- description: Native support for DICOM format, the standard for medical imaging data exchange and storage.
  name: DICOM Support
- description: Optimized storage architecture enabling sub-second retrieval of medical images at any scale.
  name: Sub-Second Retrieval
- description: Built-in support for applying machine learning models to medical imaging data for analysis.
  name: Machine Learning Integration
- description: Create and manage datastores that scale from hundreds to millions of medical images.
  name: Scalable Datastores
- description: Organize medical images into sets with comprehensive metadata management and versioning.
  name: Image Set Management
- description: DICOM import jobs enable bulk import of medical imaging data from Amazon S3.
  name: Bulk Import
finops:
- name: Amazon Healthimaging Finops
  service_category: API
  slug: amazon-healthimaging-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the AWS HealthImaging service. AWS HealthImaging is a HIPAA-eligible service that enables healthcare providers and software partners to store, a
  name: AWS HealthImaging GraphQL Schema
  slug: amazon-healthimaging-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-healthimaging.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: healthimaging-access-denied-exception
- name: Arn
  property_count: 0
  slug: healthimaging-arn
- name: ClientToken
  property_count: 0
  slug: healthimaging-client-token
- name: ConflictException
  property_count: 0
  slug: healthimaging-conflict-exception
- name: CopyDestinationImageSetProperties
  property_count: 7
  slug: healthimaging-copy-destination-image-set-properties
- name: CopyDestinationImageSet
  property_count: 2
  slug: healthimaging-copy-destination-image-set
- name: CopyImageSetInformation
  property_count: 2
  slug: healthimaging-copy-image-set-information
- name: CopyImageSetRequest
  property_count: 1
  slug: healthimaging-copy-image-set-request
- name: CopyImageSetResponse
  property_count: 3
  slug: healthimaging-copy-image-set-response
- name: CopySourceImageSetInformation
  property_count: 1
  slug: healthimaging-copy-source-image-set-information
- name: CopySourceImageSetProperties
  property_count: 7
  slug: healthimaging-copy-source-image-set-properties
- name: CreateDatastoreRequest
  property_count: 4
  slug: healthimaging-create-datastore-request
- name: CreateDatastoreResponse
  property_count: 2
  slug: healthimaging-create-datastore-response
- name: DatastoreId
  property_count: 0
  slug: healthimaging-datastore-id
- name: DatastoreName
  property_count: 0
  slug: healthimaging-datastore-name
- name: DatastoreProperties
  property_count: 7
  slug: healthimaging-datastore-properties
- name: DatastoreStatus
  property_count: 0
  slug: healthimaging-datastore-status
- name: DatastoreSummaries
  property_count: 0
  slug: healthimaging-datastore-summaries
- name: DatastoreSummary
  property_count: 6
  slug: healthimaging-datastore-summary
- name: Date
  property_count: 0
  slug: healthimaging-date
- name: DeleteDatastoreRequest
  property_count: 0
  slug: healthimaging-delete-datastore-request
- name: DeleteDatastoreResponse
  property_count: 2
  slug: healthimaging-delete-datastore-response
- name: DeleteImageSetRequest
  property_count: 0
  slug: healthimaging-delete-image-set-request
- name: DeleteImageSetResponse
  property_count: 4
  slug: healthimaging-delete-image-set-response
- name: DICOMAccessionNumber
  property_count: 0
  slug: healthimaging-dicom-accession-number
- name: DICOMAttribute
  property_count: 0
  slug: healthimaging-dicom-attribute
- name: DICOMImportJobProperties
  property_count: 10
  slug: healthimaging-dicom-import-job-properties
- name: DICOMImportJobSummaries
  property_count: 0
  slug: healthimaging-dicom-import-job-summaries
- name: DICOMImportJobSummary
  property_count: 8
  slug: healthimaging-dicom-import-job-summary
- name: DICOMNumberOfStudyRelatedInstances
  property_count: 0
  slug: healthimaging-dicom-number-of-study-related-instances
- name: DICOMNumberOfStudyRelatedSeries
  property_count: 0
  slug: healthimaging-dicom-number-of-study-related-series
- name: DICOMPatientBirthDate
  property_count: 0
  slug: healthimaging-dicom-patient-birth-date
- name: DICOMPatientId
  property_count: 0
  slug: healthimaging-dicom-patient-id
- name: DICOMPatientName
  property_count: 0
  slug: healthimaging-dicom-patient-name
- name: DICOMPatientSex
  property_count: 0
  slug: healthimaging-dicom-patient-sex
- name: DICOMStudyDateAndTime
  property_count: 2
  slug: healthimaging-dicom-study-date-and-time
- name: DICOMStudyDate
  property_count: 0
  slug: healthimaging-dicom-study-date
- name: DICOMStudyDescription
  property_count: 0
  slug: healthimaging-dicom-study-description
- name: DICOMStudyId
  property_count: 0
  slug: healthimaging-dicom-study-id
- name: DICOMStudyInstanceUID
  property_count: 0
  slug: healthimaging-dicom-study-instance-uid
- name: DICOMStudyTime
  property_count: 0
  slug: healthimaging-dicom-study-time
- name: DICOMTags
  property_count: 12
  slug: healthimaging-dicom-tags
- name: DICOMUpdates
  property_count: 2
  slug: healthimaging-dicom-updates
- name: GetDatastoreRequest
  property_count: 0
  slug: healthimaging-get-datastore-request
- name: GetDatastoreResponse
  property_count: 1
  slug: healthimaging-get-datastore-response
- name: GetDICOMImportJobRequest
  property_count: 0
  slug: healthimaging-get-dicom-import-job-request
- name: GetDICOMImportJobResponse
  property_count: 1
  slug: healthimaging-get-dicom-import-job-response
- name: GetImageFrameRequest
  property_count: 1
  slug: healthimaging-get-image-frame-request
- name: GetImageFrameResponse
  property_count: 1
  slug: healthimaging-get-image-frame-response
- name: GetImageSetMetadataRequest
  property_count: 0
  slug: healthimaging-get-image-set-metadata-request
- name: GetImageSetMetadataResponse
  property_count: 1
  slug: healthimaging-get-image-set-metadata-response
- name: GetImageSetRequest
  property_count: 0
  slug: healthimaging-get-image-set-request
- name: GetImageSetResponse
  property_count: 10
  slug: healthimaging-get-image-set-response
- name: ImageFrameId
  property_count: 0
  slug: healthimaging-image-frame-id
- name: ImageFrameInformation
  property_count: 1
  slug: healthimaging-image-frame-information
- name: ImageSetExternalVersionId
  property_count: 0
  slug: healthimaging-image-set-external-version-id
- name: ImageSetId
  property_count: 0
  slug: healthimaging-image-set-id
- name: ImageSetMetadataBlob
  property_count: 0
  slug: healthimaging-image-set-metadata-blob
- name: ImageSetPropertiesList
  property_count: 0
  slug: healthimaging-image-set-properties-list
- name: ImageSetProperties
  property_count: 8
  slug: healthimaging-image-set-properties
- name: ImageSetState
  property_count: 0
  slug: healthimaging-image-set-state
- name: ImageSetWorkflowStatus
  property_count: 0
  slug: healthimaging-image-set-workflow-status
- name: ImageSetsMetadataSummaries
  property_count: 0
  slug: healthimaging-image-sets-metadata-summaries
- name: ImageSetsMetadataSummary
  property_count: 5
  slug: healthimaging-image-sets-metadata-summary
- name: Integer
  property_count: 0
  slug: healthimaging-integer
- name: InternalServerException
  property_count: 0
  slug: healthimaging-internal-server-exception
- name: JobId
  property_count: 0
  slug: healthimaging-job-id
- name: JobName
  property_count: 0
  slug: healthimaging-job-name
- name: JobStatus
  property_count: 0
  slug: healthimaging-job-status
- name: KmsKeyArn
  property_count: 0
  slug: healthimaging-kms-key-arn
- name: ListDatastoresRequestMaxResultsInteger
  property_count: 0
  slug: healthimaging-list-datastores-request-max-results-integer
- name: ListDatastoresRequest
  property_count: 0
  slug: healthimaging-list-datastores-request
- name: ListDatastoresResponse
  property_count: 2
  slug: healthimaging-list-datastores-response
- name: ListDICOMImportJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthimaging-list-dicom-import-jobs-request-max-results-integer
- name: ListDICOMImportJobsRequest
  property_count: 0
  slug: healthimaging-list-dicom-import-jobs-request
- name: ListDICOMImportJobsResponse
  property_count: 2
  slug: healthimaging-list-dicom-import-jobs-response
- name: ListImageSetVersionsRequestMaxResultsInteger
  property_count: 0
  slug: healthimaging-list-image-set-versions-request-max-results-integer
- name: ListImageSetVersionsRequest
  property_count: 0
  slug: healthimaging-list-image-set-versions-request
- name: ListImageSetVersionsResponse
  property_count: 2
  slug: healthimaging-list-image-set-versions-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: healthimaging-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: healthimaging-list-tags-for-resource-response
- name: Message
  property_count: 0
  slug: healthimaging-message
- name: MetadataUpdates
  property_count: 1
  slug: healthimaging-metadata-updates
- name: NextToken
  property_count: 0
  slug: healthimaging-next-token
- name: Operator
  property_count: 0
  slug: healthimaging-operator
- name: PayloadBlob
  property_count: 0
  slug: healthimaging-payload-blob
- name: ResourceNotFoundException
  property_count: 0
  slug: healthimaging-resource-not-found-exception
- name: RoleArn
  property_count: 0
  slug: healthimaging-role-arn
- name: S3Uri
  property_count: 0
  slug: healthimaging-s3-uri
- name: SearchByAttributeValue
  property_count: 6
  slug: healthimaging-search-by-attribute-value
- name: SearchCriteriaFiltersList
  property_count: 0
  slug: healthimaging-search-criteria-filters-list
- name: SearchCriteria
  property_count: 1
  slug: healthimaging-search-criteria
- name: SearchFilter
  property_count: 2
  slug: healthimaging-search-filter
- name: SearchFilterValuesList
  property_count: 0
  slug: healthimaging-search-filter-values-list
- name: SearchImageSetsRequestMaxResultsInteger
  property_count: 0
  slug: healthimaging-search-image-sets-request-max-results-integer
- name: SearchImageSetsRequest
  property_count: 1
  slug: healthimaging-search-image-sets-request
- name: SearchImageSetsResponse
  property_count: 2
  slug: healthimaging-search-image-sets-response
- name: ServiceQuotaExceededException
  property_count: 0
  slug: healthimaging-service-quota-exceeded-exception
- name: StartDICOMImportJobRequest
  property_count: 5
  slug: healthimaging-start-dicom-import-job-request
- name: StartDICOMImportJobResponse
  property_count: 4
  slug: healthimaging-start-dicom-import-job-response
- name: String
  property_count: 0
  slug: healthimaging-string
- name: TagKeyList
  property_count: 0
  slug: healthimaging-tag-key-list
- name: TagKey
  property_count: 0
  slug: healthimaging-tag-key
- name: TagMap
  property_count: 0
  slug: healthimaging-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: healthimaging-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: healthimaging-tag-resource-response
- name: TagValue
  property_count: 0
  slug: healthimaging-tag-value
- name: ThrottlingException
  property_count: 0
  slug: healthimaging-throttling-exception
- name: UntagResourceRequest
  property_count: 0
  slug: healthimaging-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: healthimaging-untag-resource-response
- name: UpdateImageSetMetadataRequest
  property_count: 1
  slug: healthimaging-update-image-set-metadata-request
- name: UpdateImageSetMetadataResponse
  property_count: 8
  slug: healthimaging-update-image-set-metadata-response
- name: ValidationException
  property_count: 0
  slug: healthimaging-validation-exception
json_structures:
- name: Healthimaging Access Denied Exception Structure
  property_count: 0
  slug: healthimaging-access-denied-exception-structure
- name: Healthimaging Arn Structure
  property_count: 0
  slug: healthimaging-arn-structure
- name: Healthimaging Client Token Structure
  property_count: 0
  slug: healthimaging-client-token-structure
- name: Healthimaging Conflict Exception Structure
  property_count: 0
  slug: healthimaging-conflict-exception-structure
- name: Healthimaging Copy Destination Image Set Properties Structure
  property_count: 7
  slug: healthimaging-copy-destination-image-set-properties-structure
- name: Healthimaging Copy Destination Image Set Structure
  property_count: 2
  slug: healthimaging-copy-destination-image-set-structure
- name: Healthimaging Copy Image Set Information Structure
  property_count: 2
  slug: healthimaging-copy-image-set-information-structure
- name: Healthimaging Copy Image Set Request Structure
  property_count: 1
  slug: healthimaging-copy-image-set-request-structure
- name: Healthimaging Copy Image Set Response Structure
  property_count: 3
  slug: healthimaging-copy-image-set-response-structure
- name: Healthimaging Copy Source Image Set Information Structure
  property_count: 1
  slug: healthimaging-copy-source-image-set-information-structure
- name: Healthimaging Copy Source Image Set Properties Structure
  property_count: 7
  slug: healthimaging-copy-source-image-set-properties-structure
- name: Healthimaging Create Datastore Request Structure
  property_count: 4
  slug: healthimaging-create-datastore-request-structure
- name: Healthimaging Create Datastore Response Structure
  property_count: 2
  slug: healthimaging-create-datastore-response-structure
- name: Healthimaging Datastore Id Structure
  property_count: 0
  slug: healthimaging-datastore-id-structure
- name: Healthimaging Datastore Name Structure
  property_count: 0
  slug: healthimaging-datastore-name-structure
- name: Healthimaging Datastore Properties Structure
  property_count: 7
  slug: healthimaging-datastore-properties-structure
- name: Healthimaging Datastore Status Structure
  property_count: 0
  slug: healthimaging-datastore-status-structure
- name: Healthimaging Datastore Summaries Structure
  property_count: 0
  slug: healthimaging-datastore-summaries-structure
- name: Healthimaging Datastore Summary Structure
  property_count: 6
  slug: healthimaging-datastore-summary-structure
- name: Healthimaging Date Structure
  property_count: 0
  slug: healthimaging-date-structure
- name: Healthimaging Delete Datastore Request Structure
  property_count: 0
  slug: healthimaging-delete-datastore-request-structure
- name: Healthimaging Delete Datastore Response Structure
  property_count: 2
  slug: healthimaging-delete-datastore-response-structure
- name: Healthimaging Delete Image Set Request Structure
  property_count: 0
  slug: healthimaging-delete-image-set-request-structure
- name: Healthimaging Delete Image Set Response Structure
  property_count: 4
  slug: healthimaging-delete-image-set-response-structure
- name: Healthimaging Dicom Accession Number Structure
  property_count: 0
  slug: healthimaging-dicom-accession-number-structure
- name: Healthimaging Dicom Attribute Structure
  property_count: 0
  slug: healthimaging-dicom-attribute-structure
- name: Healthimaging Dicom Import Job Properties Structure
  property_count: 10
  slug: healthimaging-dicom-import-job-properties-structure
- name: Healthimaging Dicom Import Job Summaries Structure
  property_count: 0
  slug: healthimaging-dicom-import-job-summaries-structure
- name: Healthimaging Dicom Import Job Summary Structure
  property_count: 8
  slug: healthimaging-dicom-import-job-summary-structure
- name: Healthimaging Dicom Number Of Study Related Instances Structure
  property_count: 0
  slug: healthimaging-dicom-number-of-study-related-instances-structure
- name: Healthimaging Dicom Number Of Study Related Series Structure
  property_count: 0
  slug: healthimaging-dicom-number-of-study-related-series-structure
- name: Healthimaging Dicom Patient Birth Date Structure
  property_count: 0
  slug: healthimaging-dicom-patient-birth-date-structure
- name: Healthimaging Dicom Patient Id Structure
  property_count: 0
  slug: healthimaging-dicom-patient-id-structure
- name: Healthimaging Dicom Patient Name Structure
  property_count: 0
  slug: healthimaging-dicom-patient-name-structure
- name: Healthimaging Dicom Patient Sex Structure
  property_count: 0
  slug: healthimaging-dicom-patient-sex-structure
- name: Healthimaging Dicom Study Date And Time Structure
  property_count: 2
  slug: healthimaging-dicom-study-date-and-time-structure
- name: Healthimaging Dicom Study Date Structure
  property_count: 0
  slug: healthimaging-dicom-study-date-structure
- name: Healthimaging Dicom Study Description Structure
  property_count: 0
  slug: healthimaging-dicom-study-description-structure
- name: Healthimaging Dicom Study Id Structure
  property_count: 0
  slug: healthimaging-dicom-study-id-structure
- name: Healthimaging Dicom Study Instance Uid Structure
  property_count: 0
  slug: healthimaging-dicom-study-instance-uid-structure
- name: Healthimaging Dicom Study Time Structure
  property_count: 0
  slug: healthimaging-dicom-study-time-structure
- name: Healthimaging Dicom Tags Structure
  property_count: 12
  slug: healthimaging-dicom-tags-structure
- name: Healthimaging Dicom Updates Structure
  property_count: 2
  slug: healthimaging-dicom-updates-structure
- name: Healthimaging Get Datastore Request Structure
  property_count: 0
  slug: healthimaging-get-datastore-request-structure
- name: Healthimaging Get Datastore Response Structure
  property_count: 1
  slug: healthimaging-get-datastore-response-structure
- name: Healthimaging Get Dicom Import Job Request Structure
  property_count: 0
  slug: healthimaging-get-dicom-import-job-request-structure
- name: Healthimaging Get Dicom Import Job Response Structure
  property_count: 1
  slug: healthimaging-get-dicom-import-job-response-structure
- name: Healthimaging Get Image Frame Request Structure
  property_count: 1
  slug: healthimaging-get-image-frame-request-structure
- name: Healthimaging Get Image Frame Response Structure
  property_count: 1
  slug: healthimaging-get-image-frame-response-structure
- name: Healthimaging Get Image Set Metadata Request Structure
  property_count: 0
  slug: healthimaging-get-image-set-metadata-request-structure
- name: Healthimaging Get Image Set Metadata Response Structure
  property_count: 1
  slug: healthimaging-get-image-set-metadata-response-structure
- name: Healthimaging Get Image Set Request Structure
  property_count: 0
  slug: healthimaging-get-image-set-request-structure
- name: Healthimaging Get Image Set Response Structure
  property_count: 10
  slug: healthimaging-get-image-set-response-structure
- name: Healthimaging Image Frame Id Structure
  property_count: 0
  slug: healthimaging-image-frame-id-structure
- name: Healthimaging Image Frame Information Structure
  property_count: 1
  slug: healthimaging-image-frame-information-structure
- name: Healthimaging Image Set External Version Id Structure
  property_count: 0
  slug: healthimaging-image-set-external-version-id-structure
- name: Healthimaging Image Set Id Structure
  property_count: 0
  slug: healthimaging-image-set-id-structure
- name: Healthimaging Image Set Metadata Blob Structure
  property_count: 0
  slug: healthimaging-image-set-metadata-blob-structure
- name: Healthimaging Image Set Properties List Structure
  property_count: 0
  slug: healthimaging-image-set-properties-list-structure
- name: Healthimaging Image Set Properties Structure
  property_count: 8
  slug: healthimaging-image-set-properties-structure
- name: Healthimaging Image Set State Structure
  property_count: 0
  slug: healthimaging-image-set-state-structure
- name: Healthimaging Image Set Workflow Status Structure
  property_count: 0
  slug: healthimaging-image-set-workflow-status-structure
- name: Healthimaging Image Sets Metadata Summaries Structure
  property_count: 0
  slug: healthimaging-image-sets-metadata-summaries-structure
- name: Healthimaging Image Sets Metadata Summary Structure
  property_count: 5
  slug: healthimaging-image-sets-metadata-summary-structure
- name: Healthimaging Integer Structure
  property_count: 0
  slug: healthimaging-integer-structure
- name: Healthimaging Internal Server Exception Structure
  property_count: 0
  slug: healthimaging-internal-server-exception-structure
- name: Healthimaging Job Id Structure
  property_count: 0
  slug: healthimaging-job-id-structure
- name: Healthimaging Job Name Structure
  property_count: 0
  slug: healthimaging-job-name-structure
- name: Healthimaging Job Status Structure
  property_count: 0
  slug: healthimaging-job-status-structure
- name: Healthimaging Kms Key Arn Structure
  property_count: 0
  slug: healthimaging-kms-key-arn-structure
- name: Healthimaging List Datastores Request Max Results Integer Structure
  property_count: 0
  slug: healthimaging-list-datastores-request-max-results-integer-structure
- name: Healthimaging List Datastores Request Structure
  property_count: 0
  slug: healthimaging-list-datastores-request-structure
- name: Healthimaging List Datastores Response Structure
  property_count: 2
  slug: healthimaging-list-datastores-response-structure
- name: Healthimaging List Dicom Import Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthimaging-list-dicom-import-jobs-request-max-results-integer-structure
- name: Healthimaging List Dicom Import Jobs Request Structure
  property_count: 0
  slug: healthimaging-list-dicom-import-jobs-request-structure
- name: Healthimaging List Dicom Import Jobs Response Structure
  property_count: 2
  slug: healthimaging-list-dicom-import-jobs-response-structure
- name: Healthimaging List Image Set Versions Request Max Results Integer Structure
  property_count: 0
  slug: healthimaging-list-image-set-versions-request-max-results-integer-structure
- name: Healthimaging List Image Set Versions Request Structure
  property_count: 0
  slug: healthimaging-list-image-set-versions-request-structure
- name: Healthimaging List Image Set Versions Response Structure
  property_count: 2
  slug: healthimaging-list-image-set-versions-response-structure
- name: Healthimaging List Tags For Resource Request Structure
  property_count: 0
  slug: healthimaging-list-tags-for-resource-request-structure
- name: Healthimaging List Tags For Resource Response Structure
  property_count: 1
  slug: healthimaging-list-tags-for-resource-response-structure
- name: Healthimaging Message Structure
  property_count: 0
  slug: healthimaging-message-structure
- name: Healthimaging Metadata Updates Structure
  property_count: 1
  slug: healthimaging-metadata-updates-structure
- name: Healthimaging Next Token Structure
  property_count: 0
  slug: healthimaging-next-token-structure
- name: Healthimaging Operator Structure
  property_count: 0
  slug: healthimaging-operator-structure
- name: Healthimaging Payload Blob Structure
  property_count: 0
  slug: healthimaging-payload-blob-structure
- name: Healthimaging Resource Not Found Exception Structure
  property_count: 0
  slug: healthimaging-resource-not-found-exception-structure
- name: Healthimaging Role Arn Structure
  property_count: 0
  slug: healthimaging-role-arn-structure
- name: Healthimaging S3 Uri Structure
  property_count: 0
  slug: healthimaging-s3-uri-structure
- name: Healthimaging Search By Attribute Value Structure
  property_count: 6
  slug: healthimaging-search-by-attribute-value-structure
- name: Healthimaging Search Criteria Filters List Structure
  property_count: 0
  slug: healthimaging-search-criteria-filters-list-structure
- name: Healthimaging Search Criteria Structure
  property_count: 1
  slug: healthimaging-search-criteria-structure
- name: Healthimaging Search Filter Structure
  property_count: 2
  slug: healthimaging-search-filter-structure
- name: Healthimaging Search Filter Values List Structure
  property_count: 0
  slug: healthimaging-search-filter-values-list-structure
- name: Healthimaging Search Image Sets Request Max Results Integer Structure
  property_count: 0
  slug: healthimaging-search-image-sets-request-max-results-integer-structure
- name: Healthimaging Search Image Sets Request Structure
  property_count: 1
  slug: healthimaging-search-image-sets-request-structure
- name: Healthimaging Search Image Sets Response Structure
  property_count: 2
  slug: healthimaging-search-image-sets-response-structure
- name: Healthimaging Service Quota Exceeded Exception Structure
  property_count: 0
  slug: healthimaging-service-quota-exceeded-exception-structure
- name: Healthimaging Start Dicom Import Job Request Structure
  property_count: 5
  slug: healthimaging-start-dicom-import-job-request-structure
- name: Healthimaging Start Dicom Import Job Response Structure
  property_count: 4
  slug: healthimaging-start-dicom-import-job-response-structure
- name: Healthimaging String Structure
  property_count: 0
  slug: healthimaging-string-structure
- name: Healthimaging Tag Key List Structure
  property_count: 0
  slug: healthimaging-tag-key-list-structure
- name: Healthimaging Tag Key Structure
  property_count: 0
  slug: healthimaging-tag-key-structure
- name: Healthimaging Tag Map Structure
  property_count: 0
  slug: healthimaging-tag-map-structure
- name: Healthimaging Tag Resource Request Structure
  property_count: 1
  slug: healthimaging-tag-resource-request-structure
- name: Healthimaging Tag Resource Response Structure
  property_count: 0
  slug: healthimaging-tag-resource-response-structure
- name: Healthimaging Tag Value Structure
  property_count: 0
  slug: healthimaging-tag-value-structure
- name: Healthimaging Throttling Exception Structure
  property_count: 0
  slug: healthimaging-throttling-exception-structure
- name: Healthimaging Untag Resource Request Structure
  property_count: 0
  slug: healthimaging-untag-resource-request-structure
- name: Healthimaging Untag Resource Response Structure
  property_count: 0
  slug: healthimaging-untag-resource-response-structure
- name: Healthimaging Update Image Set Metadata Request Structure
  property_count: 1
  slug: healthimaging-update-image-set-metadata-request-structure
- name: Healthimaging Update Image Set Metadata Response Structure
  property_count: 8
  slug: healthimaging-update-image-set-metadata-response-structure
- name: Healthimaging Validation Exception Structure
  property_count: 0
  slug: healthimaging-validation-exception-structure
jsonld:
- class_count: 113
  name: Amazon Healthimaging Context
  property_count: 0
  slug: amazon-healthimaging-context
layout: provider
modified: '2026-05-19'
name: Amazon HealthImaging
nav: Providers
network: true
overview: 'Amazon HealthImaging publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Datastore API, GetDICOMImportJob API, ListDICOMImportJobs API, and 2 more. Tagged areas include Healthcare, HIPAA, Machine Learning, Medical Imaging, and DICOM.


  The Amazon HealthImaging catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon HealthImaging''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 23 more developer resources.'
plans:
- name: Amazon Healthimaging Plans Pricing
  plan_count: 3
  slug: amazon-healthimaging-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Amazon Healthimaging Rate Limits
  slug: amazon-healthimaging-rate-limits
rules:
- name: Amazon HealthImaging API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-healthimaging-jsonschema-spectral-rules
- name: Amazon HealthImaging API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 8
  slug: amazon-healthimaging-spectral-rules
score:
  band: strong
  composite: 64.0
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 77.7
    developer_ergonomics: 58.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-healthimaging/refs/heads/main/screenshots/amazon-healthimaging-2026-07-25T200012.png
security:
- kind: authentication
  name: Amazon Healthimaging Authentication
  slug: amazon-healthimaging-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Healthimaging Domain Security
  slug: amazon-healthimaging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Healthimaging Vulnerability Disclosure
  slug: amazon-healthimaging-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Healthimaging Trust Center
  slug: amazon-healthimaging-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-healthimaging
tags:
- Healthcare
- HIPAA
- Machine Learning
- Medical Imaging
- DICOM
use_cases:
- description: Streamline radiology workflows by centralizing medical image storage and enabling rapid retrieval.
  name: Radiology Workflow
- description: Apply machine learning models to medical images for automated diagnostic assistance.
  name: AI-Powered Diagnostics
- description: Archive medical imaging data in a HIPAA-eligible, scalable environment with long-term retention.
  name: Healthcare Data Archiving
- description: Centralize medical imaging data from multiple healthcare sites for unified access and analysis.
  name: Multi-Site Imaging
- description: Support clinical research by providing scalable access to large medical imaging datasets.
  name: Clinical Research
website: https://aws.amazon.com/healthimaging/
---
