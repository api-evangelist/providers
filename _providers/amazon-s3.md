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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 48
  human_in_the_loop: 1
  name: Amazon S3 Agentic Access
  operation_count: 82
  slug: amazon-s3-agentic-access
  summary_line: 82 operations · 48 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: The abac API from Amazon S3 — 1 operation(s) for abac.
  name: Amazon S3 Abac API
  phrasing_intents:
  - id: GetBucketAbac
    intent: Check whether a bucket uses tag-based access
    question: Is attribute-based access control enabled on my bucket?
  phrasing_ops: 1
  slug: amazon-s3-abac-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for managing bucket and object access control lists (ACLs)
  name: Amazon S3 Access Control API
  phrasing_intents:
  - id: GetBucketAcl
    intent: View a bucket's access control list
    question: Who has been granted access to my bucket through its ACL?
  - id: PutBucketAcl
    intent: Set a bucket's access control list
    question: How do I grant another account read access to a bucket with an ACL?
  phrasing_ops: 2
  slug: amazon-s3-access-control-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for S3 Access Grants management
  name: Amazon S3 Access Grants API
  phrasing_intents:
  - id: GetAccessGrantsInstance
    intent: Get the Access Grants instance
    question: Does my account already have an S3 Access Grants instance in this region?
  - id: CreateAccessGrantsInstance
    intent: Create an Access Grants instance
    question: How do I start using S3 Access Grants in a region?
  - id: DeleteAccessGrantsInstance
    intent: Delete the Access Grants instance
    question: How do I tear down S3 Access Grants in a region?
  phrasing_ops: 3
  slug: amazon-s3-access-grants-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing S3 access points
  name: Amazon S3 Access Points API
  phrasing_intents:
  - id: GetAccessPoint
    intent: Get an access point's configuration
    question: What bucket and network settings does an access point use?
  - id: CreateAccessPoint
    intent: Create an access point for a bucket
    question: How do I give an application its own entry point into a shared S3 bucket?
  - id: DeleteAccessPoint
    intent: Delete an access point
    question: How do I remove an access point I no longer need?
  - id: ListAccessPoints
    intent: List access points
    question: Which access points exist for a given bucket?
  - id: GetAccessPointPolicy
    intent: View an access point's policy
    question: What permissions does the policy on my access point grant?
  - id: PutAccessPointPolicy
    intent: Set an access point's policy
    question: How do I control who can use a specific access point?
  - id: DeleteAccessPointPolicy
    intent: Remove an access point's policy
    question: How do I detach the resource policy from an access point?
  phrasing_ops: 7
  slug: amazon-s3-access-points-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: The acl API from Amazon S3 — 1 operation(s) for acl.
  name: Amazon S3 Acl API
  phrasing_intents:
  - id: GetObjectAcl
    intent: View an object's access control list
    question: Who can read or modify a specific file according to its ACL?
  - id: PutObjectAcl
    intent: Set an object's access control list
    question: How do I make a single object publicly readable with a canned ACL?
  phrasing_ops: 2
  slug: amazon-s3-acl-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: The annotation API from Amazon S3 — 1 operation(s) for annotation.
  name: Amazon S3 Annotation API
  phrasing_intents:
  - id: DeleteObjectAnnotation
    intent: Delete an annotation from an object
    question: How do I remove a named annotation from an S3 object?
  phrasing_ops: 1
  slug: amazon-s3-annotation-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing S3 Batch Operations jobs
  name: Amazon S3 Batch Operations API
  phrasing_intents:
  - id: ListJobs
    intent: List Batch Operations jobs
    question: Which S3 Batch Operations jobs are running in my account?
  - id: CreateJob
    intent: Create a Batch Operations job
    question: How do I run one action against millions of objects listed in a manifest?
  - id: DescribeJob
    intent: Get a Batch Operations job's status
    question: What's the current status and progress of my batch job?
  - id: UpdateJobPriority
    intent: Change a batch job's priority
    question: How do I make a batch job run ahead of others?
  - id: UpdateJobStatus
    intent: Confirm or cancel a batch job
    question: How do I confirm a batch job that is waiting before it runs?
  phrasing_ops: 5
  slug: amazon-s3-batch-operations-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: The bucket API from Amazon S3 — 1 operation(s) for bucket.
  name: Amazon S3 Bucket API
  phrasing_intents:
  - id: WriteGetObjectResponse
    intent: Return a transformed object from Object Lambda
    question: How does my Object Lambda function send the transformed object back to the caller?
  phrasing_ops: 1
  slug: amazon-s3-bucket-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for managing bucket-level configuration such as versioning, lifecycle, CORS, and encryption
  name: Amazon S3 Bucket Configuration API
  phrasing_intents:
  - id: GetBucketVersioning
    intent: Check a bucket's versioning state
    question: Is versioning turned on for my S3 bucket?
  - id: PutBucketVersioning
    intent: Turn bucket versioning on or suspend it
    question: How do I enable versioning on an existing bucket so old object versions are kept?
  - id: GetBucketEncryption
    intent: View a bucket's default encryption
    question: What default encryption is applied to new objects in my bucket?
  - id: PutBucketEncryption
    intent: Set a bucket's default encryption
    question: How do I make every new object in a bucket encrypted with my KMS key by default?
  - id: DeleteBucketEncryption
    intent: Reset a bucket's default encryption to SSE-S3
    question: How do I remove a custom default encryption setting and go back to S3-managed keys?
  - id: GetBucketLifecycleConfiguration
    intent: View a bucket's lifecycle rules
    question: Which lifecycle rules are set up to transition or expire objects in my bucket?
  - id: PutBucketLifecycleConfiguration
    intent: Create or replace bucket lifecycle rules
    question: How do I automatically expire old objects in a bucket after a number of days?
  - id: DeleteBucketLifecycle
    intent: Remove all lifecycle rules from a bucket
    question: How do I stop all automatic expirations and transitions on a bucket?
  phrasing_ops: 11
  slug: amazon-s3-bucket-configuration-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for creating, listing, and managing S3 buckets
  name: Amazon S3 Buckets API
  phrasing_intents:
  - id: ListBuckets
    intent: List my buckets
    question: What S3 buckets do I own?
  - id: CreateBucket
    intent: Create a bucket
    question: How do I create a new S3 bucket?
  - id: DeleteBucket
    intent: Delete a bucket
    question: How do I delete an S3 bucket?
  - id: HeadBucket
    intent: Check a bucket exists and is accessible
    question: How do I check whether a bucket exists and I have access to it?
  phrasing_ops: 4
  slug: amazon-s3-buckets-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: The delete API from Amazon S3 — 1 operation(s) for delete.
  name: Amazon S3 Delete API
  phrasing_intents:
  - id: DeleteObjects
    intent: Delete multiple objects in a single request
    question: How do I remove several known keys from a bucket with one request?
  phrasing_ops: 1
  slug: amazon-s3-delete-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for Multi-Region Access Points
  name: Amazon S3 Multi-Region Access Points API
  phrasing_intents:
  - id: CreateMultiRegionAccessPoint
    intent: Create a Multi-Region Access Point
    question: How do I put one global endpoint in front of buckets in several regions?
  - id: ListMultiRegionAccessPoints
    intent: List Multi-Region Access Points
    question: Which Multi-Region Access Points does my account have?
  - id: GetMultiRegionAccessPoint
    intent: Get a Multi-Region Access Point
    question: Which buckets sit behind a particular Multi-Region Access Point?
  phrasing_ops: 3
  slug: amazon-s3-multi-region-access-points-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for multipart upload of large objects
  name: Amazon S3 Multipart Upload API
  phrasing_intents:
  - id: CreateMultipartUpload
    intent: Start a multipart upload
    question: How do I begin uploading a very large file in parts?
  - id: UploadPart
    intent: Upload one part of a multipart upload
    question: What size does each part of a multipart upload need to be?
  - id: CompleteMultipartUpload
    intent: Finish a multipart upload
    question: How do I assemble my uploaded parts into the final object?
  - id: AbortMultipartUpload
    intent: Abort a multipart upload
    question: How do I cancel an unfinished multipart upload and free the storage its parts use?
  phrasing_ops: 4
  slug: amazon-s3-multipart-upload-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: The object API from Amazon S3 — 1 operation(s) for object.
  name: Amazon S3 Object API
  phrasing_intents:
  - id: CompleteMultipartUpload
    intent: Complete a multipart upload into an object
    question: How do I finalize a multipart upload once every part is uploaded?
  - id: HeadObject
    intent: Read an object's metadata without the body
    question: How do I get a file's size, ETag and content type without downloading it?
  phrasing_ops: 2
  slug: amazon-s3-object-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for uploading, downloading, copying, and deleting objects
  name: Amazon S3 Objects API
  phrasing_intents:
  - id: ListObjectsV2
    intent: List objects in a bucket
    question: How do I see what files are stored in a bucket?
  - id: GetObject
    intent: Download an object
    question: How do I download a file from an S3 bucket?
  - id: PutObject
    intent: Upload an object
    question: How do I upload a file to an S3 bucket?
  - id: DeleteObject
    intent: Delete a single object
    question: How do I delete one file from a bucket?
  - id: HeadObject
    intent: Check an object's metadata
    question: How can I check if a file exists in a bucket without downloading it?
  - id: CopyObject
    intent: Copy an object
    question: How do I copy a file from one bucket to another?
  - id: DeleteObjects
    intent: Delete many objects in one request
    question: How do I delete a batch of files from a bucket at once?
  phrasing_ops: 7
  slug: amazon-s3-objects-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for managing public access block settings
  name: Amazon S3 Public Access Block API
  phrasing_intents:
  - id: GetPublicAccessBlock
    intent: View account-wide public access block
    question: Is public access blocked across my whole AWS account in S3?
  - id: PutPublicAccessBlock
    intent: Set account-wide public access block
    question: How do I stop any bucket in my account from being made public?
  - id: DeletePublicAccessBlock
    intent: Remove account-wide public access block
    question: How do I remove the account-level public access block?
  phrasing_ops: 3
  slug: amazon-s3-public-access-block-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for S3 Storage Lens configurations
  name: Amazon S3 Storage Lens API
  phrasing_intents:
  - id: ListStorageLensConfigurations
    intent: List Storage Lens dashboards
    question: Which S3 Storage Lens configurations exist in my account?
  - id: GetStorageLensConfiguration
    intent: Get a Storage Lens configuration
    question: What metrics and scope does a Storage Lens dashboard cover?
  - id: PutStorageLensConfiguration
    intent: Create or update a Storage Lens configuration
    question: How do I set up a Storage Lens dashboard for storage usage across my account?
  - id: DeleteStorageLensConfiguration
    intent: Delete a Storage Lens configuration
    question: How do I remove a Storage Lens dashboard I no longer use?
  phrasing_ops: 4
  slug: amazon-s3-storage-lens-api
- baseURL: https://s3.amazonaws.com
  baseurl_source: declared
  description: Operations for managing bucket and object tags
  name: Amazon S3 Tagging API
  phrasing_intents:
  - id: GetBucketTagging
    intent: View a bucket's tags
    question: What tags are on my S3 bucket?
  - id: PutBucketTagging
    intent: Set a bucket's tags
    question: How do I tag a bucket so its costs show up by project on my bill?
  - id: DeleteBucketTagging
    intent: Remove all tags from a bucket
    question: How do I clear every tag off a bucket?
  phrasing_ops: 3
  slug: amazon-s3-tagging-api
arazzos:
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
artifact_total: 255
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon S3 Control Access Control API
  slug: open-amazon-s3-access-control-api
- collection_type: open
  name: Amazon S3 Control Access Control Access Grants API
  slug: open-amazon-s3-access-grants-api
- collection_type: open
  name: Amazon S3 Control Access Control Access Points API
  slug: open-amazon-s3-access-points-api
- collection_type: open
  name: Amazon S3 Control Access Control Batch Operations API
  slug: open-amazon-s3-batch-operations-api
- collection_type: open
  name: Amazon S3 Control Access Control Bucket Configuration API
  slug: open-amazon-s3-bucket-configuration-api
- collection_type: open
  name: Amazon S3 Control Access Control Buckets API
  slug: open-amazon-s3-buckets-api
- collection_type: open
  name: Amazon S3 Control API
  slug: open-amazon-s3-control-api
- collection_type: open
  name: Amazon S3 Control Access Control Multi-Region Access Points API
  slug: open-amazon-s3-multi-region-access-points-api
- collection_type: open
  name: Amazon S3 Control Access Control Multipart Upload API
  slug: open-amazon-s3-multipart-upload-api
- collection_type: open
  name: Amazon S3 Control Access Control Namespaces API
  slug: open-amazon-s3-namespaces-api
- collection_type: open
  name: Amazon S3 Control Access Control Objects API
  slug: open-amazon-s3-objects-api
- collection_type: open
  name: Amazon S3 Control Access Control Public Access Block API
  slug: open-amazon-s3-public-access-block-api
- collection_type: open
  name: Amazon S3 REST API
  slug: open-amazon-s3-rest-api
- collection_type: open
  name: Amazon S3 Control Access Control Storage Lens API
  slug: open-amazon-s3-storage-lens-api
- collection_type: open
  name: Amazon S3 Control Access Control Table Buckets API
  slug: open-amazon-s3-table-buckets-api
- collection_type: open
  name: Amazon S3 Control Access Control Table Maintenance API
  slug: open-amazon-s3-table-maintenance-api
- collection_type: open
  name: Amazon S3 Control Access Control Table Policy API
  slug: open-amazon-s3-table-policy-api
- collection_type: open
  name: Amazon S3 Control Access Control Tables API
  slug: open-amazon-s3-tables-api
- collection_type: open
  name: Amazon S3 Control Access Control Tagging API
  slug: open-amazon-s3-tagging-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/plans/amazon-s3-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-s3-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/overlays/amazon-s3-tables-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amazon-s3-tables-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/capabilities/amazon-s3-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-s3-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/agentic-access/amazon-s3-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-s3-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/security/amazon-s3-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-s3-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/security/amazon-s3-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-s3-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/security/amazon-s3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-s3-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/authentication/amazon-s3-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-s3-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/packages/amazon-s3-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-s3-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/well-known/amazon-s3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-s3-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/well-known/amazon-s3-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-s3-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/mcp/amazon-s3-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amazon-s3-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/llms/amazon-s3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-s3-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/conformance/amazon-s3-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-s3-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/errors/amazon-s3-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amazon-s3-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/lifecycle/amazon-s3-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-s3-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/conventions/amazon-s3-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amazon-s3-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/changelog/amazon-s3-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amazon-s3-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/cli/amazon-s3-cli.yml
  title: ''
  type: CLI
  url: cli/amazon-s3-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/data-model/amazon-s3-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-s3-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-s3/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-abort-multipart-upload-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-abort-multipart-upload-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-archive-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-archive-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-conditional-download-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-conditional-download-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-copy-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-copy-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-create-bucket-put-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-create-bucket-put-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-delete-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-delete-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-empty-and-delete-bucket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-empty-and-delete-bucket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-enable-versioning-put-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-enable-versioning-put-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-get-or-create-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-get-or-create-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-list-and-batch-delete-objects-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-list-and-batch-delete-objects-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-move-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-move-object-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-multipart-upload-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-multipart-upload-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-paginate-list-objects-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-paginate-list-objects-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-provision-secure-bucket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-provision-secure-bucket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-put-object-list-objects-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-put-object-list-objects-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-set-bucket-acl-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-acl-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-set-bucket-cors-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-cors-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-set-bucket-encryption-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-encryption-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-set-bucket-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-s3-set-bucket-lifecycle-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/arazzo/amazon-s3-set-bucket-tagging-workflow.yml
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
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/s3/
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
modified: '2026-09-16'
name: Amazon S3
nav: Providers
network: true
overview: 'Amazon S3 publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Abac API, Access Control API, Access Grants API, and 15 more. Tagged areas include Archives, Backup, Cloud Storage, Data Storage, and Object Storage.


  The Amazon S3 catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon S3''s developer surface includes authentication, changelog, CLI, developer portal, documentation, support, engineering blog, and 53 more developer resources.'
plans:
- name: Amazon S3 Plans Pricing
  plan_count: 10
  slug: amazon-s3-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Amazon S3 Rate Limits
  slug: amazon-s3-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon S3 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-s3-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Amazon S3 API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 5
  slug: amazon-s3-spectral-rules
score:
  band: exemplar
  composite: 70.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 74.5
    catalog_earned_first_party: 12.0
    catalog_gap: 40.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 64.1
    developer_ergonomics: 79.8
    discoverability: 71.4
    operational_transparency: 52.6
  previous_composite: 69.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fedramp
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 11.1
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
- Archives
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
- Storage
use_cases:
- Storing and serving static website content
- Data lake foundation for analytics workloads
- Backup and disaster recovery storage
- Archive storage with Glacier integration
- Hosting machine learning training datasets
- Storing application logs and audit trails
website: https://aws.amazon.com/s3/
---
