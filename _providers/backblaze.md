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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Backblaze Agentic Access
  operation_count: 27
  slug: backblaze-agentic-access
  summary_line: 27 operations · 24 acting
api_count: 7
apis:
- description: The Backblaze S3-Compatible API allows existing applications built for Amazon S3 to work with Backblaze B2 Cloud Storage with minimal code changes. Supports S3 authentication (AWS Signature V4) and S3
  name: Backblaze S3-Compatible API
  slug: backblaze-s3-compatible-api
- baseURL: https://api.backblazeb2.com
  baseurl_source: spec
  description: Create and manage application keys for access control
  name: Backblaze Application Keys API
  slug: backblaze-application-keys-api
- baseURL: https://api.backblazeb2.com
  baseurl_source: spec
  description: Account authorization and token management
  name: Backblaze Authorization API
  slug: backblaze-authorization-api
- baseURL: https://api.backblazeb2.com
  baseurl_source: spec
  description: Bucket creation, management, and configuration
  name: Backblaze Buckets API
  slug: backblaze-buckets-api
- baseURL: https://api.backblazeb2.com
  baseurl_source: spec
  description: File upload, download, listing, deletion, and metadata
  name: Backblaze Files API
  slug: backblaze-files-api
- baseURL: https://api.backblazeb2.com
  baseurl_source: spec
  description: Multi-part upload for large files
  name: Backblaze Large Files API
  slug: backblaze-large-files-api
- baseURL: https://api.backblazeb2.com
  baseurl_source: spec
  description: Bucket event notification configuration
  name: Backblaze Notifications API
  slug: backblaze-notifications-api
arazzos:
- description: Authorize the account, then create a new private bucket using the returned account context.
  name: Backblaze Authorize and Provision Bucket
  slug: backblaze-authorize-and-provision-bucket-workflow
- description: Authorize, list buckets, list the file names in a bucket, then fetch full info for the first file.
  name: Backblaze Browse Bucket Files
  slug: backblaze-browse-bucket-files-workflow
- description: Authorize, list unfinished large files in a bucket, then cancel the first stalled upload found.
  name: Backblaze Clean Up Unfinished Large Files
  slug: backblaze-cleanup-unfinished-large-files-workflow
- description: Authorize, set a webhook notification rule on a bucket, then read the rules back to confirm.
  name: Backblaze Configure Bucket Event Notifications
  slug: backblaze-configure-bucket-notifications-workflow
- description: Authorize, locate a source file by listing, then server-side copy it into a destination bucket.
  name: Backblaze Copy a File Into Another Bucket
  slug: backblaze-copy-file-into-bucket-workflow
- description: Authorize, create a capability-scoped application key, then confirm it appears in the key list.
  name: Backblaze Create Scoped Application Key
  slug: backblaze-create-application-key-workflow
- description: Authorize, start a large file, get a part upload URL, then finish the large file from its parts.
  name: Backblaze Large File Multi-Part Upload
  slug: backblaze-large-file-upload-workflow
- description: Authorize, create a bucket, get its upload URL, and upload the first file end to end.
  name: Backblaze Provision Bucket and Upload First File
  slug: backblaze-provision-bucket-and-upload-workflow
- description: Authorize, list a file's versions by prefix, then delete the most recent version found.
  name: Backblaze Purge a File's Versions
  slug: backblaze-purge-file-versions-workflow
- description: Authorize, create a replacement application key, then delete the old key it supersedes.
  name: Backblaze Rotate Application Key
  slug: backblaze-rotate-application-key-workflow
- description: Authorize, mint a prefix-scoped download authorization token, then download a private file by name.
  name: Backblaze Share Private Files
  slug: backblaze-share-private-files-workflow
- description: Authorize, list a bucket's file names, delete the first file version, then delete the empty bucket.
  name: Backblaze Tear Down a Bucket
  slug: backblaze-teardown-bucket-workflow
- description: Authorize, request a bucket upload URL, then upload a single file to that bucket.
  name: Backblaze Upload a File
  slug: backblaze-upload-file-workflow
artifact_total: 182
collections:
- collection_type: postman
  name: Backblaze B2 Native API
  slug: postman-backblaze-b2-native-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Backblaze B2 Native Application Keys API
  slug: open-backblaze-application-keys-api
- collection_type: open
  name: Backblaze B2 Native Application Keys Authorization API
  slug: open-backblaze-authorization-api
- collection_type: open
  name: Backblaze B2 Native Application Keys Buckets API
  slug: open-backblaze-buckets-api
- collection_type: open
  name: Backblaze B2 Native Application Keys Files API
  slug: open-backblaze-files-api
- collection_type: open
  name: Backblaze B2 Native Application Keys Large Files API
  slug: open-backblaze-large-files-api
- collection_type: open
  name: Backblaze B2 Native Application Keys Notifications API
  slug: open-backblaze-notifications-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/backblaze-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/backblaze-b2-native-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Backblaze/b2-sdk-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Backblaze/b2-sdk-python/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Backblaze/b2-sdk-python/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/backblaze-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backblaze-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/backblaze-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/backblaze-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/backblaze-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backblaze-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/backblaze-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/backblaze-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/backblaze-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/backblaze-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/backblaze-cli.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/backblaze-trust-center.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/backblaze/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-authorize-and-provision-bucket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-browse-bucket-files-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-cleanup-unfinished-large-files-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-configure-bucket-notifications-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-copy-file-into-bucket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-create-application-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-large-file-upload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-provision-bucket-and-upload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-purge-file-versions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-rotate-application-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-share-private-files-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-teardown-bucket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backblaze-upload-file-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/backblaze
- group: company
  title: ''
  type: Website
  url: https://www.backblaze.com
- group: start
  title: ''
  type: Portal
  url: https://www.backblaze.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.backblaze.com/apidocs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.backblaze.com/docs/cloud-storage-native-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.backblaze.com/cloud-storage/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.backblaze.com/b2/sign-up.html
- group: company
  title: ''
  type: Blog
  url: https://www.backblaze.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.backblaze.com
- group: operate
  title: ''
  type: Support
  url: https://help.backblaze.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backblaze.com/company/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backblaze.com/company/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Backblaze
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Backblaze/b2-sdk-python
- group: build
  title: Python SDK (B2 CLI & SDK)
  type: SDKs
  url: https://pypi.org/project/b2/
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/Backblaze/b2-sdk-java
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/Backblaze/blazer
- group: build
  title: B2 Command Line Tool
  type: CLI
  url: https://github.com/Backblaze/B2_Command_Line_Tool
- group: build
  title: Terraform Provider
  type: Tools
  url: https://github.com/Backblaze/terraform-provider-b2
- group: design
  title: ''
  type: SpectralRules
  url: rules/backblaze-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/backblaze-vocabulary.yaml
created: '2025-03-01'
description: Backblaze is a cloud storage and data backup provider offering B2 Cloud Storage - a low-cost, S3-compatible object storage service. Backblaze provides both a native B2 API and an S3-compatible API, enabling developers to build applications that store unlimited data at a fraction of major cloud provider costs. Features include file versioning, lifecycle rules, event notifications, object lock, cross-region replication, and a Cloudflare bandwidth alliance for zero-egress CDN delivery.
examples:
- key_count: 4
  name: B2 Native Api Allowed Capabilities Example
  slug: b2-native-api-allowed-capabilities-example
- key_count: 1
  name: B2 Native Api Api Info Example
  slug: b2-native-api-api-info-example
- key_count: 8
  name: B2 Native Api Application Key Example
  slug: b2-native-api-application-key-example
- key_count: 4
  name: B2 Native Api Authorize Account Response Example
  slug: b2-native-api-authorize-account-response-example
- key_count: 8
  name: B2 Native Api Bucket Example
  slug: b2-native-api-bucket-example
- key_count: 2
  name: B2 Native Api Bucket Notification Rules Response Example
  slug: b2-native-api-bucket-notification-rules-response-example
- key_count: 1
  name: B2 Native Api Cancel Large File Request Example
  slug: b2-native-api-cancel-large-file-request-example
- key_count: 4
  name: B2 Native Api Cancel Large File Response Example
  slug: b2-native-api-cancel-large-file-response-example
- key_count: 5
  name: B2 Native Api Copy File Request Example
  slug: b2-native-api-copy-file-request-example
- key_count: 6
  name: B2 Native Api Create Bucket Request Example
  slug: b2-native-api-create-bucket-request-example
- key_count: 6
  name: B2 Native Api Create Key Request Example
  slug: b2-native-api-create-key-request-example
- key_count: 2
  name: B2 Native Api Delete Bucket Request Example
  slug: b2-native-api-delete-bucket-request-example
- key_count: 3
  name: B2 Native Api Delete File Version Request Example
  slug: b2-native-api-delete-file-version-request-example
- key_count: 2
  name: B2 Native Api Delete File Version Response Example
  slug: b2-native-api-delete-file-version-response-example
- key_count: 1
  name: B2 Native Api Delete Key Request Example
  slug: b2-native-api-delete-key-request-example
- key_count: 10
  name: B2 Native Api File Info Example
  slug: b2-native-api-file-info-example
- key_count: 2
  name: B2 Native Api Finish Large File Request Example
  slug: b2-native-api-finish-large-file-request-example
- key_count: 1
  name: B2 Native Api Get Bucket Notification Rules Request Example
  slug: b2-native-api-get-bucket-notification-rules-request-example
- key_count: 3
  name: B2 Native Api Get Download Authorization Request Example
  slug: b2-native-api-get-download-authorization-request-example
- key_count: 3
  name: B2 Native Api Get Download Authorization Response Example
  slug: b2-native-api-get-download-authorization-response-example
- key_count: 1
  name: B2 Native Api Get File Info Request Example
  slug: b2-native-api-get-file-info-request-example
- key_count: 1
  name: B2 Native Api Get Upload Part Url Request Example
  slug: b2-native-api-get-upload-part-url-request-example
- key_count: 3
  name: B2 Native Api Get Upload Part Url Response Example
  slug: b2-native-api-get-upload-part-url-response-example
- key_count: 1
  name: B2 Native Api Get Upload Url Request Example
  slug: b2-native-api-get-upload-url-request-example
- key_count: 3
  name: B2 Native Api Get Upload Url Response Example
  slug: b2-native-api-get-upload-url-response-example
- key_count: 2
  name: B2 Native Api Hide File Request Example
  slug: b2-native-api-hide-file-request-example
- key_count: 4
  name: B2 Native Api List Buckets Request Example
  slug: b2-native-api-list-buckets-request-example
- key_count: 1
  name: B2 Native Api List Buckets Response Example
  slug: b2-native-api-list-buckets-response-example
- key_count: 5
  name: B2 Native Api List File Names Request Example
  slug: b2-native-api-list-file-names-request-example
- key_count: 2
  name: B2 Native Api List File Names Response Example
  slug: b2-native-api-list-file-names-response-example
- key_count: 6
  name: B2 Native Api List File Versions Request Example
  slug: b2-native-api-list-file-versions-request-example
- key_count: 3
  name: B2 Native Api List File Versions Response Example
  slug: b2-native-api-list-file-versions-response-example
- key_count: 3
  name: B2 Native Api List Keys Request Example
  slug: b2-native-api-list-keys-request-example
- key_count: 2
  name: B2 Native Api List Keys Response Example
  slug: b2-native-api-list-keys-response-example
- key_count: 3
  name: B2 Native Api List Parts Request Example
  slug: b2-native-api-list-parts-request-example
- key_count: 2
  name: B2 Native Api List Parts Response Example
  slug: b2-native-api-list-parts-response-example
- key_count: 4
  name: B2 Native Api List Unfinished Large Files Request Example
  slug: b2-native-api-list-unfinished-large-files-request-example
- key_count: 2
  name: B2 Native Api List Unfinished Large Files Response Example
  slug: b2-native-api-list-unfinished-large-files-response-example
- key_count: 4
  name: B2 Native Api Notification Rule Example
  slug: b2-native-api-notification-rule-example
- key_count: 2
  name: B2 Native Api Set Bucket Notification Rules Request Example
  slug: b2-native-api-set-bucket-notification-rules-request-example
- key_count: 5
  name: B2 Native Api Start Large File Request Example
  slug: b2-native-api-start-large-file-request-example
- key_count: 7
  name: B2 Native Api Update Bucket Request Example
  slug: b2-native-api-update-bucket-request-example
features:
- description: Store and retrieve any amount of data with a simple flat namespace and unique file IDs.
  name: Object Storage
- description: Use existing S3 tools and libraries without modification via the S3-compatible API endpoint.
  name: S3-Compatible API
- description: Upload files larger than 5GB using the multi-part upload API (b2_start_large_file / b2_upload_part / b2_finish_large_file).
  name: Large File Multi-Part Upload
- description: Create and manage scoped application keys with per-bucket and per-prefix restrictions.
  name: Application Key Management
- description: Automatically delete or hide files after a specified number of days using lifecycle rules.
  name: Lifecycle Rules
- description: Keep multiple versions of files; older versions are preserved and accessible by file ID.
  name: File Versioning
- description: Configure webhook-based event notifications when objects are created, modified, or deleted.
  name: Event Notifications
- description: Protect files from deletion or modification for a specified retention period using object lock.
  name: Object Lock
- description: Replicate buckets to other regions or accounts for disaster recovery and data locality.
  name: Cross-Region Replication
- description: Encrypt data at rest using Backblaze-managed or customer-managed keys.
  name: Server-Side Encryption
- description: Zero egress fees when serving B2 data through Cloudflare CDN.
  name: Cloudflare Bandwidth Alliance
finops:
- name: Backblaze Finops
  service_category: API
  slug: backblaze-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/backblaze.png
json_schemas:
- name: AllowedCapabilities
  property_count: 4
  slug: b2-native-api-allowed-capabilities
- name: ApiInfo
  property_count: 1
  slug: b2-native-api-api-info
- name: ApplicationKey
  property_count: 8
  slug: b2-native-api-application-key
- name: AuthorizeAccountResponse
  property_count: 4
  slug: b2-native-api-authorize-account-response
- name: BucketNotificationRulesResponse
  property_count: 2
  slug: b2-native-api-bucket-notification-rules-response
- name: Bucket
  property_count: 8
  slug: b2-native-api-bucket
- name: CancelLargeFileRequest
  property_count: 1
  slug: b2-native-api-cancel-large-file-request
- name: CancelLargeFileResponse
  property_count: 4
  slug: b2-native-api-cancel-large-file-response
- name: CopyFileRequest
  property_count: 5
  slug: b2-native-api-copy-file-request
- name: CreateBucketRequest
  property_count: 6
  slug: b2-native-api-create-bucket-request
- name: CreateKeyRequest
  property_count: 6
  slug: b2-native-api-create-key-request
- name: DeleteBucketRequest
  property_count: 2
  slug: b2-native-api-delete-bucket-request
- name: DeleteFileVersionRequest
  property_count: 3
  slug: b2-native-api-delete-file-version-request
- name: DeleteFileVersionResponse
  property_count: 2
  slug: b2-native-api-delete-file-version-response
- name: DeleteKeyRequest
  property_count: 1
  slug: b2-native-api-delete-key-request
- name: FileInfo
  property_count: 10
  slug: b2-native-api-file-info
- name: FinishLargeFileRequest
  property_count: 2
  slug: b2-native-api-finish-large-file-request
- name: GetBucketNotificationRulesRequest
  property_count: 1
  slug: b2-native-api-get-bucket-notification-rules-request
- name: GetDownloadAuthorizationRequest
  property_count: 3
  slug: b2-native-api-get-download-authorization-request
- name: GetDownloadAuthorizationResponse
  property_count: 3
  slug: b2-native-api-get-download-authorization-response
- name: GetFileInfoRequest
  property_count: 1
  slug: b2-native-api-get-file-info-request
- name: GetUploadPartUrlRequest
  property_count: 1
  slug: b2-native-api-get-upload-part-url-request
- name: GetUploadPartUrlResponse
  property_count: 3
  slug: b2-native-api-get-upload-part-url-response
- name: GetUploadUrlRequest
  property_count: 1
  slug: b2-native-api-get-upload-url-request
- name: GetUploadUrlResponse
  property_count: 3
  slug: b2-native-api-get-upload-url-response
- name: HideFileRequest
  property_count: 2
  slug: b2-native-api-hide-file-request
- name: ListBucketsRequest
  property_count: 4
  slug: b2-native-api-list-buckets-request
- name: ListBucketsResponse
  property_count: 1
  slug: b2-native-api-list-buckets-response
- name: ListFileNamesRequest
  property_count: 5
  slug: b2-native-api-list-file-names-request
- name: ListFileNamesResponse
  property_count: 2
  slug: b2-native-api-list-file-names-response
- name: ListFileVersionsRequest
  property_count: 6
  slug: b2-native-api-list-file-versions-request
- name: ListFileVersionsResponse
  property_count: 3
  slug: b2-native-api-list-file-versions-response
- name: ListKeysRequest
  property_count: 3
  slug: b2-native-api-list-keys-request
- name: ListKeysResponse
  property_count: 2
  slug: b2-native-api-list-keys-response
- name: ListPartsRequest
  property_count: 3
  slug: b2-native-api-list-parts-request
- name: ListPartsResponse
  property_count: 2
  slug: b2-native-api-list-parts-response
- name: ListUnfinishedLargeFilesRequest
  property_count: 4
  slug: b2-native-api-list-unfinished-large-files-request
- name: ListUnfinishedLargeFilesResponse
  property_count: 2
  slug: b2-native-api-list-unfinished-large-files-response
- name: NotificationRule
  property_count: 4
  slug: b2-native-api-notification-rule
- name: SetBucketNotificationRulesRequest
  property_count: 2
  slug: b2-native-api-set-bucket-notification-rules-request
- name: StartLargeFileRequest
  property_count: 5
  slug: b2-native-api-start-large-file-request
- name: UpdateBucketRequest
  property_count: 7
  slug: b2-native-api-update-bucket-request
json_structures:
- name: B2 Native Api Allowed Capabilities Structure
  property_count: 4
  slug: b2-native-api-allowed-capabilities-structure
- name: B2 Native Api Api Info Structure
  property_count: 1
  slug: b2-native-api-api-info-structure
- name: B2 Native Api Application Key Structure
  property_count: 8
  slug: b2-native-api-application-key-structure
- name: B2 Native Api Authorize Account Response Structure
  property_count: 4
  slug: b2-native-api-authorize-account-response-structure
- name: B2 Native Api Bucket Notification Rules Response Structure
  property_count: 2
  slug: b2-native-api-bucket-notification-rules-response-structure
- name: B2 Native Api Bucket Structure
  property_count: 8
  slug: b2-native-api-bucket-structure
- name: B2 Native Api Cancel Large File Request Structure
  property_count: 1
  slug: b2-native-api-cancel-large-file-request-structure
- name: B2 Native Api Cancel Large File Response Structure
  property_count: 4
  slug: b2-native-api-cancel-large-file-response-structure
- name: B2 Native Api Copy File Request Structure
  property_count: 5
  slug: b2-native-api-copy-file-request-structure
- name: B2 Native Api Create Bucket Request Structure
  property_count: 6
  slug: b2-native-api-create-bucket-request-structure
- name: B2 Native Api Create Key Request Structure
  property_count: 6
  slug: b2-native-api-create-key-request-structure
- name: B2 Native Api Delete Bucket Request Structure
  property_count: 2
  slug: b2-native-api-delete-bucket-request-structure
- name: B2 Native Api Delete File Version Request Structure
  property_count: 3
  slug: b2-native-api-delete-file-version-request-structure
- name: B2 Native Api Delete File Version Response Structure
  property_count: 2
  slug: b2-native-api-delete-file-version-response-structure
- name: B2 Native Api Delete Key Request Structure
  property_count: 1
  slug: b2-native-api-delete-key-request-structure
- name: B2 Native Api File Info Structure
  property_count: 10
  slug: b2-native-api-file-info-structure
- name: B2 Native Api Finish Large File Request Structure
  property_count: 2
  slug: b2-native-api-finish-large-file-request-structure
- name: B2 Native Api Get Bucket Notification Rules Request Structure
  property_count: 1
  slug: b2-native-api-get-bucket-notification-rules-request-structure
- name: B2 Native Api Get Download Authorization Request Structure
  property_count: 3
  slug: b2-native-api-get-download-authorization-request-structure
- name: B2 Native Api Get Download Authorization Response Structure
  property_count: 3
  slug: b2-native-api-get-download-authorization-response-structure
- name: B2 Native Api Get File Info Request Structure
  property_count: 1
  slug: b2-native-api-get-file-info-request-structure
- name: B2 Native Api Get Upload Part Url Request Structure
  property_count: 1
  slug: b2-native-api-get-upload-part-url-request-structure
- name: B2 Native Api Get Upload Part Url Response Structure
  property_count: 3
  slug: b2-native-api-get-upload-part-url-response-structure
- name: B2 Native Api Get Upload Url Request Structure
  property_count: 1
  slug: b2-native-api-get-upload-url-request-structure
- name: B2 Native Api Get Upload Url Response Structure
  property_count: 3
  slug: b2-native-api-get-upload-url-response-structure
- name: B2 Native Api Hide File Request Structure
  property_count: 2
  slug: b2-native-api-hide-file-request-structure
- name: B2 Native Api List Buckets Request Structure
  property_count: 4
  slug: b2-native-api-list-buckets-request-structure
- name: B2 Native Api List Buckets Response Structure
  property_count: 1
  slug: b2-native-api-list-buckets-response-structure
- name: B2 Native Api List File Names Request Structure
  property_count: 5
  slug: b2-native-api-list-file-names-request-structure
- name: B2 Native Api List File Names Response Structure
  property_count: 2
  slug: b2-native-api-list-file-names-response-structure
- name: B2 Native Api List File Versions Request Structure
  property_count: 6
  slug: b2-native-api-list-file-versions-request-structure
- name: B2 Native Api List File Versions Response Structure
  property_count: 3
  slug: b2-native-api-list-file-versions-response-structure
- name: B2 Native Api List Keys Request Structure
  property_count: 3
  slug: b2-native-api-list-keys-request-structure
- name: B2 Native Api List Keys Response Structure
  property_count: 2
  slug: b2-native-api-list-keys-response-structure
- name: B2 Native Api List Parts Request Structure
  property_count: 3
  slug: b2-native-api-list-parts-request-structure
- name: B2 Native Api List Parts Response Structure
  property_count: 2
  slug: b2-native-api-list-parts-response-structure
- name: B2 Native Api List Unfinished Large Files Request Structure
  property_count: 4
  slug: b2-native-api-list-unfinished-large-files-request-structure
- name: B2 Native Api List Unfinished Large Files Response Structure
  property_count: 2
  slug: b2-native-api-list-unfinished-large-files-response-structure
- name: B2 Native Api Notification Rule Structure
  property_count: 4
  slug: b2-native-api-notification-rule-structure
- name: B2 Native Api Set Bucket Notification Rules Request Structure
  property_count: 2
  slug: b2-native-api-set-bucket-notification-rules-request-structure
- name: B2 Native Api Start Large File Request Structure
  property_count: 5
  slug: b2-native-api-start-large-file-request-structure
- name: B2 Native Api Update Bucket Request Structure
  property_count: 7
  slug: b2-native-api-update-bucket-request-structure
jsonld:
- class_count: 42
  name: Backblaze B2 Context
  property_count: 68
  slug: backblaze-b2-context
layout: provider
mcp_servers:
- description: 'Backblaze does not operate an official hosted/remote MCP server. Several community MCP servers wrap B2 (e.g. BraveRam/backblaze-mcp on Glama, a Pipedream connector), but none are first-party. This is '
  name: Backblaze MCP Server
  slug: backblaze-mcp-server
modified: '2026-06-20'
name: Backblaze
nav: Providers
network: true
overview: 'Backblaze publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Application Keys API, Authorization API, Buckets API, and 3 more. Tagged areas include Cloud Storage, Object Storage, Storage, and Backup.


  The Backblaze catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Backblaze''s developer surface includes authentication, changelog, CLI, developer portal, documentation, getting-started guide, pricing, and 45 more developer resources.'
plans:
- name: Backblaze Plans Pricing
  plan_count: 3
  slug: backblaze-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Backblaze Rate Limits
  slug: backblaze-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Backblaze API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: backblaze-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Backblaze API Rules
  rule_count: 36
  severity_counts:
    error: 12
    hint: 0
    info: 8
    warn: 16
  slug: backblaze-spectral-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 30
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 33.3
    contract_quality: 23.0
    developer_ergonomics: 85.7
    discoverability: 55.6
    governance: 33.3
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backblaze/refs/heads/main/screenshots/backblaze-2026-07-25T202216.png
security:
- kind: authentication
  name: Backblaze Authentication
  slug: backblaze-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Backblaze Domain Security
  slug: backblaze-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Backblaze Trust Center
  slug: backblaze-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, HIPAA, GDPR, UK GDPR, CCPA/CPRA, PCI-DSS, GovRAMP, TX-RAMP, HECVAT, TPN (Trusted Partner Network) Blue Shield, VPAT (Section 508), Internet2 Cloud Scorecard
slug: backblaze
tags:
- Cloud Storage
- Object Storage
- Storage
- Backup
use_cases:
- description: Store application data, user-uploaded content, and media files in the cloud.
  name: Application Data Storage
- description: Use Backblaze B2 as the storage backend for backup tools like Arq, MSP360, and Veeam.
  name: Backup and Disaster Recovery
- description: Host images, videos, and other media files and serve them via CDN integration.
  name: Media Hosting and Delivery
- description: Store infrequently accessed archival data at low cost with lifecycle-based management.
  name: Archival Storage
- description: Migrate data from S3 or other cloud storage providers using the S3-compatible API.
  name: Data Migration
- description: Store build artifacts, logs, and deployment packages in B2 buckets.
  name: CI/CD Artifact Storage
website: https://www.backblaze.com
---
