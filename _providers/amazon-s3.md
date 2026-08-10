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
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 48
  human_in_the_loop: 1
  name: Amazon S3 Agentic Access
  operation_count: 82
  slug: amazon-s3-agentic-access
  summary_line: 82 operations · 48 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Amazon S3 Tables API provides operations for managing table buckets and tables stored in Apache Iceberg format, enabling structured tabular data storage in Apache Parquet format within Amazon S3.
  name: Amazon S3 Tables API
  slug: amazon-s3-tables-api
- description: Operations for managing bucket and object access control lists (ACLs)
  name: Amazon S3 Access Control API
  slug: amazon-s3-access-control-api
- description: Operations for S3 Access Grants management
  name: Amazon S3 Access Grants API
  slug: amazon-s3-access-grants-api
- description: Operations for creating and managing S3 access points
  name: Amazon S3 Access Points API
  slug: amazon-s3-access-points-api
- description: Operations for creating and managing S3 Batch Operations jobs
  name: Amazon S3 Batch Operations API
  slug: amazon-s3-batch-operations-api
- description: Operations for managing bucket-level configuration such as versioning, lifecycle, CORS, and encryption
  name: Amazon S3 Bucket Configuration API
  slug: amazon-s3-bucket-configuration-api
- description: Operations for creating, listing, and managing S3 buckets
  name: Amazon S3 Buckets API
  slug: amazon-s3-buckets-api
- description: Operations for Multi-Region Access Points
  name: Amazon S3 Multi-Region Access Points API
  slug: amazon-s3-multi-region-access-points-api
- description: Operations for multipart upload of large objects
  name: Amazon S3 Multipart Upload API
  slug: amazon-s3-multipart-upload-api
- description: Operations for managing namespaces within table buckets
  name: Amazon S3 Namespaces API
  slug: amazon-s3-namespaces-api
- description: Operations for uploading, downloading, copying, and deleting objects
  name: Amazon S3 Objects API
  slug: amazon-s3-objects-api
- description: Operations for managing public access block settings
  name: Amazon S3 Public Access Block API
  slug: amazon-s3-public-access-block-api
- description: Operations for S3 Storage Lens configurations
  name: Amazon S3 Storage Lens API
  slug: amazon-s3-storage-lens-api
- description: Operations for creating and managing S3 table buckets
  name: Amazon S3 Table Buckets API
  slug: amazon-s3-table-buckets-api
- description: Operations for managing table maintenance configurations
  name: Amazon S3 Table Maintenance API
  slug: amazon-s3-table-maintenance-api
- description: Operations for managing table and table bucket policies
  name: Amazon S3 Table Policy API
  slug: amazon-s3-table-policy-api
- description: Operations for managing bucket and object tags
  name: Amazon S3 Tagging API
  slug: amazon-s3-tagging-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Initiate a multipart upload then abort it to release any staged storage.
  name: Amazon S3 Start and Abort a Multipart Upload
  slug: amazon-s3-abort-multipart-upload-workflow
- description: Copy an object into an archival storage class then delete the hot original.
  name: Amazon S3 Archive an Object to a Cold Storage Class
  slug: amazon-s3-archive-object-workflow
- description: HEAD an object to read its ETag, then GET it only when it is present.
  name: Amazon S3 Conditional Download of an Object
  slug: amazon-s3-conditional-download-object-workflow
- description: Confirm a source object exists, copy it to a destination, and verify the copy.
  name: Amazon S3 Copy Object Between Keys
  slug: amazon-s3-copy-object-workflow
- description: Create a bucket, confirm it exists, upload an object, and read it back.
  name: Amazon S3 Create Bucket and Store an Object
  slug: amazon-s3-create-bucket-put-object-workflow
- description: Delete an object then HEAD it to confirm it is gone.
  name: Amazon S3 Delete Object and Confirm Removal
  slug: amazon-s3-delete-object-workflow
- description: List the bucket, batch-delete its objects, then delete the empty bucket.
  name: Amazon S3 Empty and Delete a Bucket
  slug: amazon-s3-empty-and-delete-bucket-workflow
- description: Turn on bucket versioning, confirm it, then write a versioned object.
  name: Amazon S3 Enable Versioning Then Store an Object
  slug: amazon-s3-enable-versioning-put-object-workflow
- description: Check whether an object exists with HEAD and upload it only if missing.
  name: Amazon S3 Get Object or Create It
  slug: amazon-s3-get-or-create-object-workflow
- description: List objects under a prefix then delete a batch of keys in one request.
  name: Amazon S3 List and Batch Delete Objects
  slug: amazon-s3-list-and-batch-delete-objects-workflow
- description: Copy an object to a new key, verify it, then delete the original.
  name: Amazon S3 Move an Object
  slug: amazon-s3-move-object-workflow
- description: Initiate a multipart upload, upload a part, and complete the upload.
  name: Amazon S3 Multipart Upload a Large Object
  slug: amazon-s3-multipart-upload-workflow
- description: List a first page of objects then fetch the next page by continuation token.
  name: Amazon S3 Paginate Through Bucket Objects
  slug: amazon-s3-paginate-list-objects-workflow
- description: Create a bucket, enable versioning, and apply default encryption.
  name: Amazon S3 Provision a Secure Bucket
  slug: amazon-s3-provision-secure-bucket-workflow
- description: Upload an object then list the bucket contents to confirm it appears.
  name: Amazon S3 Upload and List Objects
  slug: amazon-s3-put-object-list-objects-workflow
- description: Set a bucket access control policy then read it back to confirm.
  name: Amazon S3 Apply and Verify a Bucket ACL
  slug: amazon-s3-set-bucket-acl-workflow
- description: Put a bucket CORS configuration then read it back to confirm.
  name: Amazon S3 Configure and Verify Bucket CORS
  slug: amazon-s3-set-bucket-cors-workflow
- description: Put a bucket default-encryption configuration then read it back.
  name: Amazon S3 Configure and Verify Default Encryption
  slug: amazon-s3-set-bucket-encryption-workflow
- description: Put a bucket lifecycle configuration then read it back to confirm.
  name: Amazon S3 Apply and Verify a Lifecycle Configuration
  slug: amazon-s3-set-bucket-lifecycle-workflow
- description: Write a bucket tag set then read it back to confirm it was stored.
  name: Amazon S3 Set and Verify Bucket Tags
  slug: amazon-s3-set-bucket-tagging-workflow
artifact_total: 239
collections:
- collection_type: postman
  name: Amazon S3 Control API
  slug: postman-amazon-s3-control-api
- collection_type: postman
  name: Amazon S3 REST API
  slug: postman-amazon-s3-rest-api
- collection_type: postman
  name: Amazon S3 Tables API
  slug: postman-amazon-s3-tables-api
- collection_type: open
  name: Amazon S3 Control API
  slug: open-amazon-s3-control-api
- collection_type: open
  name: Amazon S3 REST API
  slug: open-amazon-s3-rest-api
- collection_type: open
  name: Amazon S3 Tables API
  slug: open-amazon-s3-tables-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-s3-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-s3-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-s3-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-s3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-s3-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-s3-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-s3-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-s3-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-s3-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-s3-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-s3-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-s3-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-s3-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-s3-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-s3-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-s3-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-s3-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-s3/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-abort-multipart-upload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-archive-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-conditional-download-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-copy-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-create-bucket-put-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-delete-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-empty-and-delete-bucket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-enable-versioning-put-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-get-or-create-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-list-and-batch-delete-objects-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-move-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-multipart-upload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-paginate-list-objects-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-provision-secure-bucket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-put-object-list-objects-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-acl-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-cors-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-encryption-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-tagging-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/s3/
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
  url: https://aws.amazon.com/blogs/storage/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/s3/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-s3
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-compliance.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
created: '2024-01-15'
description: Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.
examples:
- key_count: 4
  name: Amazon S3 Control Access Grants Instance Example
  slug: amazon-s3-control-access-grants-instance-example
- key_count: 3
  name: Amazon S3 Control Create Access Point Request Example
  slug: amazon-s3-control-create-access-point-request-example
- key_count: 8
  name: Amazon S3 Control Create Job Request Example
  slug: amazon-s3-control-create-job-request-example
- key_count: 2
  name: Amazon S3 Control Create Multi Region Access Point Request Example
  slug: amazon-s3-control-create-multi-region-access-point-request-example
- key_count: 4
  name: Amazon S3 Control Error Example
  slug: amazon-s3-control-error-example
- key_count: 9
  name: Amazon S3 Control Get Access Point Result Example
  slug: amazon-s3-control-get-access-point-result-example
- key_count: 16
  name: Amazon S3 Control Job Descriptor Example
  slug: amazon-s3-control-job-descriptor-example
- key_count: 2
  name: Amazon S3 Control List Access Points Result Example
  slug: amazon-s3-control-list-access-points-result-example
- key_count: 2
  name: Amazon S3 Control List Jobs Result Example
  slug: amazon-s3-control-list-jobs-result-example
- key_count: 2
  name: Amazon S3 Control List Multi Region Access Points Result Example
  slug: amazon-s3-control-list-multi-region-access-points-result-example
- key_count: 2
  name: Amazon S3 Control List Storage Lens Configurations Result Example
  slug: amazon-s3-control-list-storage-lens-configurations-result-example
- key_count: 5
  name: Amazon S3 Control Multi Region Access Point Report Example
  slug: amazon-s3-control-multi-region-access-point-report-example
- key_count: 4
  name: Amazon S3 Control Public Access Block Configuration Example
  slug: amazon-s3-control-public-access-block-configuration-example
- key_count: 2
  name: Amazon S3 Control S3 Tag Example
  slug: amazon-s3-control-s3-tag-example
- key_count: 8
  name: Amazon S3 Control Storage Lens Configuration Example
  slug: amazon-s3-control-storage-lens-configuration-example
- key_count: 1
  name: Amazon S3 Rest Access Control Policy Example
  slug: amazon-s3-rest-access-control-policy-example
- key_count: 2
  name: Amazon S3 Rest Bucket Example
  slug: amazon-s3-rest-bucket-example
- key_count: 1
  name: Amazon S3 Rest Bucket Lifecycle Configuration Example
  slug: amazon-s3-rest-bucket-lifecycle-configuration-example
- key_count: 1
  name: Amazon S3 Rest Common Prefix Example
  slug: amazon-s3-rest-common-prefix-example
- key_count: 1
  name: Amazon S3 Rest Complete Multipart Upload Example
  slug: amazon-s3-rest-complete-multipart-upload-example
- key_count: 8
  name: Amazon S3 Rest Complete Multipart Upload Result Example
  slug: amazon-s3-rest-complete-multipart-upload-result-example
- key_count: 6
  name: Amazon S3 Rest Copy Object Result Example
  slug: amazon-s3-rest-copy-object-result-example
- key_count: 1
  name: Amazon S3 Rest Cors Configuration Example
  slug: amazon-s3-rest-cors-configuration-example
- key_count: 3
  name: Amazon S3 Rest Create Bucket Configuration Example
  slug: amazon-s3-rest-create-bucket-configuration-example
- key_count: 2
  name: Amazon S3 Rest Delete Example
  slug: amazon-s3-rest-delete-example
- key_count: 2
  name: Amazon S3 Rest Delete Result Example
  slug: amazon-s3-rest-delete-result-example
- key_count: 5
  name: Amazon S3 Rest Error Example
  slug: amazon-s3-rest-error-example
- key_count: 2
  name: Amazon S3 Rest Grant Example
  slug: amazon-s3-rest-grant-example
- key_count: 3
  name: Amazon S3 Rest Initiate Multipart Upload Result Example
  slug: amazon-s3-rest-initiate-multipart-upload-result-example
- key_count: 8
  name: Amazon S3 Rest Lifecycle Rule Example
  slug: amazon-s3-rest-lifecycle-rule-example
- key_count: 1
  name: Amazon S3 Rest List All My Buckets Result Example
  slug: amazon-s3-rest-list-all-my-buckets-result-example
- key_count: 12
  name: Amazon S3 Rest List Bucket Result Example
  slug: amazon-s3-rest-list-bucket-result-example
- key_count: 7
  name: Amazon S3 Rest Object Example
  slug: amazon-s3-rest-object-example
- key_count: 2
  name: Amazon S3 Rest Owner Example
  slug: amazon-s3-rest-owner-example
- key_count: 1
  name: Amazon S3 Rest Server Side Encryption Configuration Example
  slug: amazon-s3-rest-server-side-encryption-configuration-example
- key_count: 2
  name: Amazon S3 Rest Tag Example
  slug: amazon-s3-rest-tag-example
- key_count: 1
  name: Amazon S3 Rest Tagging Example
  slug: amazon-s3-rest-tagging-example
- key_count: 2
  name: Amazon S3 Rest Versioning Configuration Example
  slug: amazon-s3-rest-versioning-configuration-example
- key_count: 1
  name: Amazon S3 Tables Create Table Bucket Request Example
  slug: amazon-s3-tables-create-table-bucket-request-example
- key_count: 2
  name: Amazon S3 Tables Create Table Request Example
  slug: amazon-s3-tables-create-table-request-example
- key_count: 2
  name: Amazon S3 Tables Error Example
  slug: amazon-s3-tables-error-example
- key_count: 2
  name: Amazon S3 Tables List Namespaces Response Example
  slug: amazon-s3-tables-list-namespaces-response-example
- key_count: 2
  name: Amazon S3 Tables List Table Buckets Response Example
  slug: amazon-s3-tables-list-table-buckets-response-example
- key_count: 2
  name: Amazon S3 Tables List Tables Response Example
  slug: amazon-s3-tables-list-tables-response-example
- key_count: 5
  name: Amazon S3 Tables Namespace Detail Example
  slug: amazon-s3-tables-namespace-detail-example
- key_count: 2
  name: Amazon S3 Tables Put Table Bucket Maintenance Configuration Request Example
  slug: amazon-s3-tables-put-table-bucket-maintenance-configuration-request-example
- key_count: 2
  name: Amazon S3 Tables Put Table Maintenance Configuration Request Example
  slug: amazon-s3-tables-put-table-maintenance-configuration-request-example
- key_count: 5
  name: Amazon S3 Tables Table Bucket Example
  slug: amazon-s3-tables-table-bucket-example
- key_count: 2
  name: Amazon S3 Tables Table Bucket Maintenance Configuration Example
  slug: amazon-s3-tables-table-bucket-maintenance-configuration-example
- key_count: 4
  name: Amazon S3 Tables Table Bucket Summary Example
  slug: amazon-s3-tables-table-bucket-summary-example
- key_count: 14
  name: Amazon S3 Tables Table Detail Example
  slug: amazon-s3-tables-table-detail-example
- key_count: 2
  name: Amazon S3 Tables Table Maintenance Configuration Example
  slug: amazon-s3-tables-table-maintenance-configuration-example
- key_count: 2
  name: Amazon S3 Tables Table Maintenance Job Status Example
  slug: amazon-s3-tables-table-maintenance-job-status-example
- key_count: 6
  name: Amazon S3 Tables Table Summary Example
  slug: amazon-s3-tables-table-summary-example
features:
- Industry-leading scalability and 99.999999999% durability
- Multiple storage classes for cost optimization
- Object versioning and lifecycle management
- Server-side encryption and access control
- S3 Object Lock for WORM compliance
- Cross-region and same-region replication
- S3 Tables for Apache Iceberg tabular data
- S3 Access Grants for identity-based access
- Storage Lens analytics and insights
- Batch Operations for large-scale object processing
finops:
- name: Amazon S3 Finops
  service_category: Storage / Object Storage
  slug: amazon-s3-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon S3 Bucket
  property_count: 16
  slug: amazon-s3-bucket
- name: AccessGrantsInstance
  property_count: 4
  slug: amazon-s3-control-access-grants-instance
- name: CreateAccessPointRequest
  property_count: 3
  slug: amazon-s3-control-create-access-point-request
- name: CreateJobRequest
  property_count: 8
  slug: amazon-s3-control-create-job-request
- name: CreateMultiRegionAccessPointRequest
  property_count: 2
  slug: amazon-s3-control-create-multi-region-access-point-request
- name: Error
  property_count: 4
  slug: amazon-s3-control-error
- name: GetAccessPointResult
  property_count: 9
  slug: amazon-s3-control-get-access-point-result
- name: JobDescriptor
  property_count: 16
  slug: amazon-s3-control-job-descriptor
- name: ListAccessPointsResult
  property_count: 2
  slug: amazon-s3-control-list-access-points-result
- name: ListJobsResult
  property_count: 2
  slug: amazon-s3-control-list-jobs-result
- name: ListMultiRegionAccessPointsResult
  property_count: 2
  slug: amazon-s3-control-list-multi-region-access-points-result
- name: ListStorageLensConfigurationsResult
  property_count: 2
  slug: amazon-s3-control-list-storage-lens-configurations-result
- name: MultiRegionAccessPointReport
  property_count: 5
  slug: amazon-s3-control-multi-region-access-point-report
- name: PublicAccessBlockConfiguration
  property_count: 4
  slug: amazon-s3-control-public-access-block-configuration
- name: S3Tag
  property_count: 2
  slug: amazon-s3-control-s3-tag
- name: StorageLensConfiguration
  property_count: 8
  slug: amazon-s3-control-storage-lens-configuration
- name: Amazon S3 Object
  property_count: 39
  slug: amazon-s3-object
- name: AccessControlPolicy
  property_count: 1
  slug: amazon-s3-rest-access-control-policy
- name: BucketLifecycleConfiguration
  property_count: 1
  slug: amazon-s3-rest-bucket-lifecycle-configuration
- name: Bucket
  property_count: 2
  slug: amazon-s3-rest-bucket
- name: CommonPrefix
  property_count: 1
  slug: amazon-s3-rest-common-prefix
- name: CompleteMultipartUploadResult
  property_count: 8
  slug: amazon-s3-rest-complete-multipart-upload-result
- name: CompleteMultipartUpload
  property_count: 1
  slug: amazon-s3-rest-complete-multipart-upload
- name: CopyObjectResult
  property_count: 6
  slug: amazon-s3-rest-copy-object-result
- name: CORSConfiguration
  property_count: 1
  slug: amazon-s3-rest-cors-configuration
- name: CreateBucketConfiguration
  property_count: 3
  slug: amazon-s3-rest-create-bucket-configuration
- name: DeleteResult
  property_count: 2
  slug: amazon-s3-rest-delete-result
- name: Delete
  property_count: 2
  slug: amazon-s3-rest-delete
- name: Error
  property_count: 5
  slug: amazon-s3-rest-error
- name: Grant
  property_count: 2
  slug: amazon-s3-rest-grant
- name: InitiateMultipartUploadResult
  property_count: 3
  slug: amazon-s3-rest-initiate-multipart-upload-result
- name: LifecycleRule
  property_count: 8
  slug: amazon-s3-rest-lifecycle-rule
- name: ListAllMyBucketsResult
  property_count: 1
  slug: amazon-s3-rest-list-all-my-buckets-result
- name: ListBucketResult
  property_count: 12
  slug: amazon-s3-rest-list-bucket-result
- name: Object
  property_count: 7
  slug: amazon-s3-rest-object
- name: Owner
  property_count: 2
  slug: amazon-s3-rest-owner
- name: ServerSideEncryptionConfiguration
  property_count: 1
  slug: amazon-s3-rest-server-side-encryption-configuration
- name: Tag
  property_count: 2
  slug: amazon-s3-rest-tag
- name: Tagging
  property_count: 1
  slug: amazon-s3-rest-tagging
- name: VersioningConfiguration
  property_count: 2
  slug: amazon-s3-rest-versioning-configuration
- name: CreateTableBucketRequest
  property_count: 1
  slug: amazon-s3-tables-create-table-bucket-request
- name: CreateTableRequest
  property_count: 2
  slug: amazon-s3-tables-create-table-request
- name: Error
  property_count: 2
  slug: amazon-s3-tables-error
- name: ListNamespacesResponse
  property_count: 2
  slug: amazon-s3-tables-list-namespaces-response
- name: ListTableBucketsResponse
  property_count: 2
  slug: amazon-s3-tables-list-table-buckets-response
- name: ListTablesResponse
  property_count: 2
  slug: amazon-s3-tables-list-tables-response
- name: NamespaceDetail
  property_count: 5
  slug: amazon-s3-tables-namespace-detail
- name: PutTableBucketMaintenanceConfigurationRequest
  property_count: 2
  slug: amazon-s3-tables-put-table-bucket-maintenance-configuration-request
- name: PutTableMaintenanceConfigurationRequest
  property_count: 2
  slug: amazon-s3-tables-put-table-maintenance-configuration-request
- name: TableBucketMaintenanceConfiguration
  property_count: 2
  slug: amazon-s3-tables-table-bucket-maintenance-configuration
- name: TableBucket
  property_count: 5
  slug: amazon-s3-tables-table-bucket
- name: TableBucketSummary
  property_count: 4
  slug: amazon-s3-tables-table-bucket-summary
- name: TableDetail
  property_count: 14
  slug: amazon-s3-tables-table-detail
- name: TableMaintenanceConfiguration
  property_count: 2
  slug: amazon-s3-tables-table-maintenance-configuration
- name: TableMaintenanceJobStatus
  property_count: 2
  slug: amazon-s3-tables-table-maintenance-job-status
- name: TableSummary
  property_count: 6
  slug: amazon-s3-tables-table-summary
json_structures:
- name: Amazon S3 Control Access Grants Instance Structure
  property_count: 4
  slug: amazon-s3-control-access-grants-instance-structure
- name: Amazon S3 Control Create Access Point Request Structure
  property_count: 3
  slug: amazon-s3-control-create-access-point-request-structure
- name: Amazon S3 Control Create Job Request Structure
  property_count: 8
  slug: amazon-s3-control-create-job-request-structure
- name: Amazon S3 Control Create Multi Region Access Point Request Structure
  property_count: 2
  slug: amazon-s3-control-create-multi-region-access-point-request-structure
- name: Amazon S3 Control Error Structure
  property_count: 4
  slug: amazon-s3-control-error-structure
- name: Amazon S3 Control Get Access Point Result Structure
  property_count: 9
  slug: amazon-s3-control-get-access-point-result-structure
- name: Amazon S3 Control Job Descriptor Structure
  property_count: 16
  slug: amazon-s3-control-job-descriptor-structure
- name: Amazon S3 Control List Access Points Result Structure
  property_count: 2
  slug: amazon-s3-control-list-access-points-result-structure
- name: Amazon S3 Control List Jobs Result Structure
  property_count: 2
  slug: amazon-s3-control-list-jobs-result-structure
- name: Amazon S3 Control List Multi Region Access Points Result Structure
  property_count: 2
  slug: amazon-s3-control-list-multi-region-access-points-result-structure
- name: Amazon S3 Control List Storage Lens Configurations Result Structure
  property_count: 2
  slug: amazon-s3-control-list-storage-lens-configurations-result-structure
- name: Amazon S3 Control Multi Region Access Point Report Structure
  property_count: 5
  slug: amazon-s3-control-multi-region-access-point-report-structure
- name: Amazon S3 Control Public Access Block Configuration Structure
  property_count: 4
  slug: amazon-s3-control-public-access-block-configuration-structure
- name: Amazon S3 Control S3 Tag Structure
  property_count: 2
  slug: amazon-s3-control-s3-tag-structure
- name: Amazon S3 Control Storage Lens Configuration Structure
  property_count: 8
  slug: amazon-s3-control-storage-lens-configuration-structure
- name: Amazon S3 Rest Access Control Policy Structure
  property_count: 1
  slug: amazon-s3-rest-access-control-policy-structure
- name: Amazon S3 Rest Bucket Lifecycle Configuration Structure
  property_count: 1
  slug: amazon-s3-rest-bucket-lifecycle-configuration-structure
- name: Amazon S3 Rest Bucket Structure
  property_count: 2
  slug: amazon-s3-rest-bucket-structure
- name: Amazon S3 Rest Common Prefix Structure
  property_count: 1
  slug: amazon-s3-rest-common-prefix-structure
- name: Amazon S3 Rest Complete Multipart Upload Result Structure
  property_count: 8
  slug: amazon-s3-rest-complete-multipart-upload-result-structure
- name: Amazon S3 Rest Complete Multipart Upload Structure
  property_count: 1
  slug: amazon-s3-rest-complete-multipart-upload-structure
- name: Amazon S3 Rest Copy Object Result Structure
  property_count: 6
  slug: amazon-s3-rest-copy-object-result-structure
- name: Amazon S3 Rest Cors Configuration Structure
  property_count: 1
  slug: amazon-s3-rest-cors-configuration-structure
- name: Amazon S3 Rest Create Bucket Configuration Structure
  property_count: 3
  slug: amazon-s3-rest-create-bucket-configuration-structure
- name: Amazon S3 Rest Delete Result Structure
  property_count: 2
  slug: amazon-s3-rest-delete-result-structure
- name: Amazon S3 Rest Delete Structure
  property_count: 2
  slug: amazon-s3-rest-delete-structure
- name: Amazon S3 Rest Error Structure
  property_count: 5
  slug: amazon-s3-rest-error-structure
- name: Amazon S3 Rest Grant Structure
  property_count: 2
  slug: amazon-s3-rest-grant-structure
- name: Amazon S3 Rest Initiate Multipart Upload Result Structure
  property_count: 3
  slug: amazon-s3-rest-initiate-multipart-upload-result-structure
- name: Amazon S3 Rest Lifecycle Rule Structure
  property_count: 8
  slug: amazon-s3-rest-lifecycle-rule-structure
- name: Amazon S3 Rest List All My Buckets Result Structure
  property_count: 1
  slug: amazon-s3-rest-list-all-my-buckets-result-structure
- name: Amazon S3 Rest List Bucket Result Structure
  property_count: 12
  slug: amazon-s3-rest-list-bucket-result-structure
- name: Amazon S3 Rest Object Structure
  property_count: 7
  slug: amazon-s3-rest-object-structure
- name: Amazon S3 Rest Owner Structure
  property_count: 2
  slug: amazon-s3-rest-owner-structure
- name: Amazon S3 Rest Server Side Encryption Configuration Structure
  property_count: 1
  slug: amazon-s3-rest-server-side-encryption-configuration-structure
- name: Amazon S3 Rest Tag Structure
  property_count: 2
  slug: amazon-s3-rest-tag-structure
- name: Amazon S3 Rest Tagging Structure
  property_count: 1
  slug: amazon-s3-rest-tagging-structure
- name: Amazon S3 Rest Versioning Configuration Structure
  property_count: 2
  slug: amazon-s3-rest-versioning-configuration-structure
- name: Amazon S3 Tables Create Table Bucket Request Structure
  property_count: 1
  slug: amazon-s3-tables-create-table-bucket-request-structure
- name: Amazon S3 Tables Create Table Request Structure
  property_count: 2
  slug: amazon-s3-tables-create-table-request-structure
- name: Amazon S3 Tables Error Structure
  property_count: 2
  slug: amazon-s3-tables-error-structure
- name: Amazon S3 Tables List Namespaces Response Structure
  property_count: 2
  slug: amazon-s3-tables-list-namespaces-response-structure
- name: Amazon S3 Tables List Table Buckets Response Structure
  property_count: 2
  slug: amazon-s3-tables-list-table-buckets-response-structure
- name: Amazon S3 Tables List Tables Response Structure
  property_count: 2
  slug: amazon-s3-tables-list-tables-response-structure
- name: Amazon S3 Tables Namespace Detail Structure
  property_count: 5
  slug: amazon-s3-tables-namespace-detail-structure
- name: Amazon S3 Tables Put Table Bucket Maintenance Configuration Request Structure
  property_count: 2
  slug: amazon-s3-tables-put-table-bucket-maintenance-configuration-request-structure
- name: Amazon S3 Tables Put Table Maintenance Configuration Request Structure
  property_count: 2
  slug: amazon-s3-tables-put-table-maintenance-configuration-request-structure
- name: Amazon S3 Tables Table Bucket Maintenance Configuration Structure
  property_count: 2
  slug: amazon-s3-tables-table-bucket-maintenance-configuration-structure
- name: Amazon S3 Tables Table Bucket Structure
  property_count: 5
  slug: amazon-s3-tables-table-bucket-structure
- name: Amazon S3 Tables Table Bucket Summary Structure
  property_count: 4
  slug: amazon-s3-tables-table-bucket-summary-structure
- name: Amazon S3 Tables Table Detail Structure
  property_count: 14
  slug: amazon-s3-tables-table-detail-structure
- name: Amazon S3 Tables Table Maintenance Configuration Structure
  property_count: 2
  slug: amazon-s3-tables-table-maintenance-configuration-structure
- name: Amazon S3 Tables Table Maintenance Job Status Structure
  property_count: 2
  slug: amazon-s3-tables-table-maintenance-job-status-structure
- name: Amazon S3 Tables Table Summary Structure
  property_count: 6
  slug: amazon-s3-tables-table-summary-structure
jsonld:
- class_count: 10
  name: Amazon S3 Context
  property_count: 11
  slug: amazon-s3-context
- class_count: 0
  name: Amazon S3 Control Context
  property_count: 0
  slug: amazon-s3-control-context
- class_count: 0
  name: Amazon S3 Rest Context
  property_count: 0
  slug: amazon-s3-rest-context
- class_count: 0
  name: Amazon S3 Tables Context
  property_count: 0
  slug: amazon-s3-tables-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-s3-mcp.yml
  slug: amazon-s3-mcpyml
modified: '2026-06-20'
name: Amazon S3
nav: Providers
network: true
overview: 'Amazon S3 publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Tables API, Access Control API, Access Grants API, and 14 more. Tagged areas include Archive, Backup, Cloud Storage, Data Storage, and Object Storage.


  The Amazon S3 catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon S3''s developer surface includes authentication, changelog, CLI, developer portal, documentation, support, engineering blog, and 49 more developer resources.'
plans:
- name: Amazon S3 Plans Pricing
  plan_count: 4
  slug: amazon-s3-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 4
  name: Amazon S3 Rate Limits
  slug: amazon-s3-rate-limits
rules:
- name: Amazon S3 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-s3-jsonschema-spectral-rules
- name: Amazon S3 API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 5
  slug: amazon-s3-spectral-rules
score:
  band: exemplar
  composite: 78.1
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 83.3
    developer_ergonomics: 60.9
    discoverability: 85.2
    governance: 69.8
    operational_transparency: 78.9
  previous_composite: 78.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/screenshots/amazon-s3-2026-06-20T171813.png
security:
- kind: authentication
  name: Amazon S3 Authentication
  slug: amazon-s3-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon S3 Domain Security
  slug: amazon-s3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon S3 Vulnerability Disclosure
  slug: amazon-s3-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon S3 Trust Center
  slug: amazon-s3-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-s3
tags:
- Archive
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
use_cases:
- Storing and serving static website content
- Data lake foundation for analytics workloads
- Backup and disaster recovery storage
- Archive storage with Glacier integration
- Hosting machine learning training datasets
- Storing application logs and audit trails
website: https://aws.amazon.com/
---
