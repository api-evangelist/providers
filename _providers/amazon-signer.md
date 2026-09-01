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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Amazon Signer Agentic Access
  operation_count: 19
  slug: amazon-signer-agentic-access
  summary_line: 19 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes API from Amazon Signer — 1 operation(s) for revocations#signaturetimestamp&platformid&profileversionarn&jobarn&
  name: Amazon Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes API
  slug: amazon-signer-revocations-signaturetimestamp-platformid-profileversionarn-jobarn-certificatehashes-api
- description: The Signing Jobs API from Amazon Signer — 4 operation(s) for signing jobs.
  name: Amazon Signer Signing Jobs API
  slug: amazon-signer-signing-jobs-api
- description: The Signing Platforms API from Amazon Signer — 2 operation(s) for signing platforms.
  name: Amazon Signer Signing Platforms API
  slug: amazon-signer-signing-platforms-api
- description: The Signing Profiles API from Amazon Signer — 5 operation(s) for signing profiles.
  name: Amazon Signer Signing Profiles API
  slug: amazon-signer-signing-profiles-api
- description: The Tags API from Amazon Signer — 2 operation(s) for tags.
  name: Amazon Signer Tags API
  slug: amazon-signer-tags-api
artifact_total: 225
collections:
- collection_type: postman
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes API
  slug: postman-amazon-signer-revocations-signaturetimestamp-platformid-profileversionarn-jobarn-certificatehashes-api
- collection_type: postman
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Signing Jobs API
  slug: postman-amazon-signer-signing-jobs-api
- collection_type: postman
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Signing Platforms API
  slug: postman-amazon-signer-signing-platforms-api
- collection_type: postman
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Signing Profiles API
  slug: postman-amazon-signer-signing-profiles-api
- collection_type: postman
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Tags API
  slug: postman-amazon-signer-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes API
  slug: open-amazon-signer-revocations-signaturetimestamp-platformid-profileversionarn-jobarn-certificatehashes-api
- collection_type: open
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Signing Jobs API
  slug: open-amazon-signer-signing-jobs-api
- collection_type: open
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Signing Platforms API
  slug: open-amazon-signer-signing-platforms-api
- collection_type: open
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Signing Profiles API
  slug: open-amazon-signer-signing-profiles-api
- collection_type: open
  name: AWS Signer Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes Tags API
  slug: open-amazon-signer-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-signer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-signer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-signer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-signer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-signer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-signer-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/signer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/signer/
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
  url: https://aws.amazon.com/blogs/compute/tag/aws-signer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/signer/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-signer-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-signer-vocabulary.yaml
created: '2026-03-16'
description: AWS Signer is a fully managed code-signing service to ensure the trust and integrity of your code. It manages the code-signing certificate public and private keys and enables central management and deployment of code signing certificates for Lambda functions and IoT devices.
examples:
- key_count: 5
  name: Amazon Signer Add Profile Permission Request Example
  slug: amazon-signer-add-profile-permission-request-example
- key_count: 1
  name: Amazon Signer Add Profile Permission Response Example
  slug: amazon-signer-add-profile-permission-response-example
- key_count: 0
  name: Amazon Signer Cancel Signing Profile Request Example
  slug: amazon-signer-cancel-signing-profile-request-example
- key_count: 0
  name: Amazon Signer Describe Signing Job Request Example
  slug: amazon-signer-describe-signing-job-request-example
- key_count: 19
  name: Amazon Signer Describe Signing Job Response Example
  slug: amazon-signer-describe-signing-job-response-example
- key_count: 1
  name: Amazon Signer Destination Example
  slug: amazon-signer-destination-example
- key_count: 2
  name: Amazon Signer Encryption Algorithm Options Example
  slug: amazon-signer-encryption-algorithm-options-example
- key_count: 0
  name: Amazon Signer Get Revocation Status Request Example
  slug: amazon-signer-get-revocation-status-request-example
- key_count: 1
  name: Amazon Signer Get Revocation Status Response Example
  slug: amazon-signer-get-revocation-status-response-example
- key_count: 0
  name: Amazon Signer Get Signing Platform Request Example
  slug: amazon-signer-get-signing-platform-request-example
- key_count: 9
  name: Amazon Signer Get Signing Platform Response Example
  slug: amazon-signer-get-signing-platform-response-example
- key_count: 0
  name: Amazon Signer Get Signing Profile Request Example
  slug: amazon-signer-get-signing-profile-request-example
- key_count: 14
  name: Amazon Signer Get Signing Profile Response Example
  slug: amazon-signer-get-signing-profile-response-example
- key_count: 2
  name: Amazon Signer Hash Algorithm Options Example
  slug: amazon-signer-hash-algorithm-options-example
- key_count: 0
  name: Amazon Signer List Profile Permissions Request Example
  slug: amazon-signer-list-profile-permissions-request-example
- key_count: 4
  name: Amazon Signer List Profile Permissions Response Example
  slug: amazon-signer-list-profile-permissions-response-example
- key_count: 0
  name: Amazon Signer List Signing Jobs Request Example
  slug: amazon-signer-list-signing-jobs-request-example
- key_count: 2
  name: Amazon Signer List Signing Jobs Response Example
  slug: amazon-signer-list-signing-jobs-response-example
- key_count: 0
  name: Amazon Signer List Signing Platforms Request Example
  slug: amazon-signer-list-signing-platforms-request-example
- key_count: 2
  name: Amazon Signer List Signing Platforms Response Example
  slug: amazon-signer-list-signing-platforms-response-example
- key_count: 0
  name: Amazon Signer List Signing Profiles Request Example
  slug: amazon-signer-list-signing-profiles-request-example
- key_count: 2
  name: Amazon Signer List Signing Profiles Response Example
  slug: amazon-signer-list-signing-profiles-response-example
- key_count: 0
  name: Amazon Signer List Tags For Resource Request Example
  slug: amazon-signer-list-tags-for-resource-request-example
- key_count: 1
  name: Amazon Signer List Tags For Resource Response Example
  slug: amazon-signer-list-tags-for-resource-response-example
- key_count: 0
  name: Amazon Signer Metadata Example
  slug: amazon-signer-metadata-example
- key_count: 4
  name: Amazon Signer Permission Example
  slug: amazon-signer-permission-example
- key_count: 6
  name: Amazon Signer Put Signing Profile Request Example
  slug: amazon-signer-put-signing-profile-request-example
- key_count: 3
  name: Amazon Signer Put Signing Profile Response Example
  slug: amazon-signer-put-signing-profile-response-example
- key_count: 0
  name: Amazon Signer Remove Profile Permission Request Example
  slug: amazon-signer-remove-profile-permission-request-example
- key_count: 1
  name: Amazon Signer Remove Profile Permission Response Example
  slug: amazon-signer-remove-profile-permission-response-example
- key_count: 2
  name: Amazon Signer Revoke Signature Request Example
  slug: amazon-signer-revoke-signature-request-example
- key_count: 3
  name: Amazon Signer Revoke Signing Profile Request Example
  slug: amazon-signer-revoke-signing-profile-request-example
- key_count: 2
  name: Amazon Signer S3 Destination Example
  slug: amazon-signer-s3-destination-example
- key_count: 2
  name: Amazon Signer S3 Signed Object Example
  slug: amazon-signer-s3-signed-object-example
- key_count: 3
  name: Amazon Signer S3 Source Example
  slug: amazon-signer-s3-source-example
- key_count: 4
  name: Amazon Signer Sign Payload Request Example
  slug: amazon-signer-sign-payload-request-example
- key_count: 4
  name: Amazon Signer Sign Payload Response Example
  slug: amazon-signer-sign-payload-response-example
- key_count: 2
  name: Amazon Signer Signature Validity Period Example
  slug: amazon-signer-signature-validity-period-example
- key_count: 1
  name: Amazon Signer Signed Object Example
  slug: amazon-signer-signed-object-example
- key_count: 2
  name: Amazon Signer Signing Configuration Example
  slug: amazon-signer-signing-configuration-example
- key_count: 2
  name: Amazon Signer Signing Configuration Overrides Example
  slug: amazon-signer-signing-configuration-overrides-example
- key_count: 2
  name: Amazon Signer Signing Image Format Example
  slug: amazon-signer-signing-image-format-example
- key_count: 14
  name: Amazon Signer Signing Job Example
  slug: amazon-signer-signing-job-example
- key_count: 3
  name: Amazon Signer Signing Job Revocation Record Example
  slug: amazon-signer-signing-job-revocation-record-example
- key_count: 1
  name: Amazon Signer Signing Material Example
  slug: amazon-signer-signing-material-example
- key_count: 0
  name: Amazon Signer Signing Parameters Example
  slug: amazon-signer-signing-parameters-example
- key_count: 9
  name: Amazon Signer Signing Platform Example
  slug: amazon-signer-signing-platform-example
- key_count: 2
  name: Amazon Signer Signing Platform Overrides Example
  slug: amazon-signer-signing-platform-overrides-example
- key_count: 11
  name: Amazon Signer Signing Profile Example
  slug: amazon-signer-signing-profile-example
- key_count: 3
  name: Amazon Signer Signing Profile Revocation Record Example
  slug: amazon-signer-signing-profile-revocation-record-example
- key_count: 1
  name: Amazon Signer Source Example
  slug: amazon-signer-source-example
- key_count: 5
  name: Amazon Signer Start Signing Job Request Example
  slug: amazon-signer-start-signing-job-request-example
- key_count: 2
  name: Amazon Signer Start Signing Job Response Example
  slug: amazon-signer-start-signing-job-response-example
- key_count: 0
  name: Amazon Signer Tag Map Example
  slug: amazon-signer-tag-map-example
- key_count: 1
  name: Amazon Signer Tag Resource Request Example
  slug: amazon-signer-tag-resource-request-example
- key_count: 0
  name: Amazon Signer Tag Resource Response Example
  slug: amazon-signer-tag-resource-response-example
- key_count: 0
  name: Amazon Signer Untag Resource Request Example
  slug: amazon-signer-untag-resource-request-example
- key_count: 0
  name: Amazon Signer Untag Resource Response Example
  slug: amazon-signer-untag-resource-response-example
features:
- description: Security administrators define signing policies and which IAM roles can sign code.
  name: Centralized Code Signing
- description: Automatically manages code-signing certificate public and private keys.
  name: Certificate Management
- description: Central management and deployment of code-signing certificates.
  name: Lifecycle Management
- description: Integration with AWS CloudTrail tracks who generates signatures for compliance.
  name: Compliance Tracking
- description: No infrastructure to maintain — fully managed code signing service.
  name: Fully Managed
- description: Revoke signing profiles and individual signatures with effective timestamps.
  name: Signature Revocation
finops:
- name: Amazon Signer Finops
  service_category: API
  slug: amazon-signer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-signer.png
json_schemas:
- name: AddProfilePermissionRequest
  property_count: 5
  slug: amazon-signer-add-profile-permission-request
- name: AddProfilePermissionResponse
  property_count: 1
  slug: amazon-signer-add-profile-permission-response
- name: CancelSigningProfileRequest
  property_count: 0
  slug: amazon-signer-cancel-signing-profile-request
- name: Category
  property_count: 0
  slug: amazon-signer-category
- name: DescribeSigningJobRequest
  property_count: 0
  slug: amazon-signer-describe-signing-job-request
- name: DescribeSigningJobResponse
  property_count: 19
  slug: amazon-signer-describe-signing-job-response
- name: Destination
  property_count: 1
  slug: amazon-signer-destination
- name: EncryptionAlgorithmOptions
  property_count: 2
  slug: amazon-signer-encryption-algorithm-options
- name: EncryptionAlgorithm
  property_count: 0
  slug: amazon-signer-encryption-algorithm
- name: GetRevocationStatusRequest
  property_count: 0
  slug: amazon-signer-get-revocation-status-request
- name: GetRevocationStatusResponse
  property_count: 1
  slug: amazon-signer-get-revocation-status-response
- name: GetSigningPlatformRequest
  property_count: 0
  slug: amazon-signer-get-signing-platform-request
- name: GetSigningPlatformResponse
  property_count: 9
  slug: amazon-signer-get-signing-platform-response
- name: GetSigningProfileRequest
  property_count: 0
  slug: amazon-signer-get-signing-profile-request
- name: GetSigningProfileResponse
  property_count: 14
  slug: amazon-signer-get-signing-profile-response
- name: HashAlgorithmOptions
  property_count: 2
  slug: amazon-signer-hash-algorithm-options
- name: HashAlgorithm
  property_count: 0
  slug: amazon-signer-hash-algorithm
- name: ImageFormat
  property_count: 0
  slug: amazon-signer-image-format
- name: ListProfilePermissionsRequest
  property_count: 0
  slug: amazon-signer-list-profile-permissions-request
- name: ListProfilePermissionsResponse
  property_count: 4
  slug: amazon-signer-list-profile-permissions-response
- name: ListSigningJobsRequest
  property_count: 0
  slug: amazon-signer-list-signing-jobs-request
- name: ListSigningJobsResponse
  property_count: 2
  slug: amazon-signer-list-signing-jobs-response
- name: ListSigningPlatformsRequest
  property_count: 0
  slug: amazon-signer-list-signing-platforms-request
- name: ListSigningPlatformsResponse
  property_count: 2
  slug: amazon-signer-list-signing-platforms-response
- name: ListSigningProfilesRequest
  property_count: 0
  slug: amazon-signer-list-signing-profiles-request
- name: ListSigningProfilesResponse
  property_count: 2
  slug: amazon-signer-list-signing-profiles-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-signer-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-signer-list-tags-for-resource-response
- name: Metadata
  property_count: 0
  slug: amazon-signer-metadata
- name: Permission
  property_count: 4
  slug: amazon-signer-permission
- name: PutSigningProfileRequest
  property_count: 6
  slug: amazon-signer-put-signing-profile-request
- name: PutSigningProfileResponse
  property_count: 3
  slug: amazon-signer-put-signing-profile-response
- name: RemoveProfilePermissionRequest
  property_count: 0
  slug: amazon-signer-remove-profile-permission-request
- name: RemoveProfilePermissionResponse
  property_count: 1
  slug: amazon-signer-remove-profile-permission-response
- name: RevokeSignatureRequest
  property_count: 2
  slug: amazon-signer-revoke-signature-request
- name: RevokeSigningProfileRequest
  property_count: 3
  slug: amazon-signer-revoke-signing-profile-request
- name: S3Destination
  property_count: 2
  slug: amazon-signer-s3-destination
- name: S3SignedObject
  property_count: 2
  slug: amazon-signer-s3-signed-object
- name: S3Source
  property_count: 3
  slug: amazon-signer-s3-source
- name: SignPayloadRequest
  property_count: 4
  slug: amazon-signer-sign-payload-request
- name: SignPayloadResponse
  property_count: 4
  slug: amazon-signer-sign-payload-response
- name: SignatureValidityPeriod
  property_count: 2
  slug: amazon-signer-signature-validity-period
- name: SignedObject
  property_count: 1
  slug: amazon-signer-signed-object
- name: SigningConfigurationOverrides
  property_count: 2
  slug: amazon-signer-signing-configuration-overrides
- name: SigningConfiguration
  property_count: 2
  slug: amazon-signer-signing-configuration
- name: SigningImageFormat
  property_count: 2
  slug: amazon-signer-signing-image-format
- name: SigningJobRevocationRecord
  property_count: 3
  slug: amazon-signer-signing-job-revocation-record
- name: SigningJob
  property_count: 14
  slug: amazon-signer-signing-job
- name: SigningMaterial
  property_count: 1
  slug: amazon-signer-signing-material
- name: SigningParameters
  property_count: 0
  slug: amazon-signer-signing-parameters
- name: SigningPlatformOverrides
  property_count: 2
  slug: amazon-signer-signing-platform-overrides
- name: SigningPlatform
  property_count: 9
  slug: amazon-signer-signing-platform
- name: SigningProfileRevocationRecord
  property_count: 3
  slug: amazon-signer-signing-profile-revocation-record
- name: SigningProfile
  property_count: 11
  slug: amazon-signer-signing-profile
- name: SigningProfileStatus
  property_count: 0
  slug: amazon-signer-signing-profile-status
- name: SigningStatus
  property_count: 0
  slug: amazon-signer-signing-status
- name: Source
  property_count: 1
  slug: amazon-signer-source
- name: StartSigningJobRequest
  property_count: 5
  slug: amazon-signer-start-signing-job-request
- name: StartSigningJobResponse
  property_count: 2
  slug: amazon-signer-start-signing-job-response
- name: TagMap
  property_count: 0
  slug: amazon-signer-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: amazon-signer-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-signer-tag-resource-response
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-signer-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-signer-untag-resource-response
- name: ValidityType
  property_count: 0
  slug: amazon-signer-validity-type
json_structures:
- name: Amazon Signer Add Profile Permission Request Structure
  property_count: 5
  slug: amazon-signer-add-profile-permission-request-structure
- name: Amazon Signer Add Profile Permission Response Structure
  property_count: 1
  slug: amazon-signer-add-profile-permission-response-structure
- name: Amazon Signer Cancel Signing Profile Request Structure
  property_count: 0
  slug: amazon-signer-cancel-signing-profile-request-structure
- name: Amazon Signer Category Structure
  property_count: 0
  slug: amazon-signer-category-structure
- name: Amazon Signer Describe Signing Job Request Structure
  property_count: 0
  slug: amazon-signer-describe-signing-job-request-structure
- name: Amazon Signer Describe Signing Job Response Structure
  property_count: 19
  slug: amazon-signer-describe-signing-job-response-structure
- name: Amazon Signer Destination Structure
  property_count: 1
  slug: amazon-signer-destination-structure
- name: Amazon Signer Encryption Algorithm Options Structure
  property_count: 2
  slug: amazon-signer-encryption-algorithm-options-structure
- name: Amazon Signer Encryption Algorithm Structure
  property_count: 0
  slug: amazon-signer-encryption-algorithm-structure
- name: Amazon Signer Get Revocation Status Request Structure
  property_count: 0
  slug: amazon-signer-get-revocation-status-request-structure
- name: Amazon Signer Get Revocation Status Response Structure
  property_count: 1
  slug: amazon-signer-get-revocation-status-response-structure
- name: Amazon Signer Get Signing Platform Request Structure
  property_count: 0
  slug: amazon-signer-get-signing-platform-request-structure
- name: Amazon Signer Get Signing Platform Response Structure
  property_count: 9
  slug: amazon-signer-get-signing-platform-response-structure
- name: Amazon Signer Get Signing Profile Request Structure
  property_count: 0
  slug: amazon-signer-get-signing-profile-request-structure
- name: Amazon Signer Get Signing Profile Response Structure
  property_count: 14
  slug: amazon-signer-get-signing-profile-response-structure
- name: Amazon Signer Hash Algorithm Options Structure
  property_count: 2
  slug: amazon-signer-hash-algorithm-options-structure
- name: Amazon Signer Hash Algorithm Structure
  property_count: 0
  slug: amazon-signer-hash-algorithm-structure
- name: Amazon Signer Image Format Structure
  property_count: 0
  slug: amazon-signer-image-format-structure
- name: Amazon Signer List Profile Permissions Request Structure
  property_count: 0
  slug: amazon-signer-list-profile-permissions-request-structure
- name: Amazon Signer List Profile Permissions Response Structure
  property_count: 4
  slug: amazon-signer-list-profile-permissions-response-structure
- name: Amazon Signer List Signing Jobs Request Structure
  property_count: 0
  slug: amazon-signer-list-signing-jobs-request-structure
- name: Amazon Signer List Signing Jobs Response Structure
  property_count: 2
  slug: amazon-signer-list-signing-jobs-response-structure
- name: Amazon Signer List Signing Platforms Request Structure
  property_count: 0
  slug: amazon-signer-list-signing-platforms-request-structure
- name: Amazon Signer List Signing Platforms Response Structure
  property_count: 2
  slug: amazon-signer-list-signing-platforms-response-structure
- name: Amazon Signer List Signing Profiles Request Structure
  property_count: 0
  slug: amazon-signer-list-signing-profiles-request-structure
- name: Amazon Signer List Signing Profiles Response Structure
  property_count: 2
  slug: amazon-signer-list-signing-profiles-response-structure
- name: Amazon Signer List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-signer-list-tags-for-resource-request-structure
- name: Amazon Signer List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-signer-list-tags-for-resource-response-structure
- name: Amazon Signer Metadata Structure
  property_count: 0
  slug: amazon-signer-metadata-structure
- name: Amazon Signer Permission Structure
  property_count: 4
  slug: amazon-signer-permission-structure
- name: Amazon Signer Put Signing Profile Request Structure
  property_count: 6
  slug: amazon-signer-put-signing-profile-request-structure
- name: Amazon Signer Put Signing Profile Response Structure
  property_count: 3
  slug: amazon-signer-put-signing-profile-response-structure
- name: Amazon Signer Remove Profile Permission Request Structure
  property_count: 0
  slug: amazon-signer-remove-profile-permission-request-structure
- name: Amazon Signer Remove Profile Permission Response Structure
  property_count: 1
  slug: amazon-signer-remove-profile-permission-response-structure
- name: Amazon Signer Revoke Signature Request Structure
  property_count: 2
  slug: amazon-signer-revoke-signature-request-structure
- name: Amazon Signer Revoke Signing Profile Request Structure
  property_count: 3
  slug: amazon-signer-revoke-signing-profile-request-structure
- name: Amazon Signer S3 Destination Structure
  property_count: 2
  slug: amazon-signer-s3-destination-structure
- name: Amazon Signer S3 Signed Object Structure
  property_count: 2
  slug: amazon-signer-s3-signed-object-structure
- name: Amazon Signer S3 Source Structure
  property_count: 3
  slug: amazon-signer-s3-source-structure
- name: Amazon Signer Sign Payload Request Structure
  property_count: 4
  slug: amazon-signer-sign-payload-request-structure
- name: Amazon Signer Sign Payload Response Structure
  property_count: 4
  slug: amazon-signer-sign-payload-response-structure
- name: Amazon Signer Signature Validity Period Structure
  property_count: 2
  slug: amazon-signer-signature-validity-period-structure
- name: Amazon Signer Signed Object Structure
  property_count: 1
  slug: amazon-signer-signed-object-structure
- name: Amazon Signer Signing Configuration Overrides Structure
  property_count: 2
  slug: amazon-signer-signing-configuration-overrides-structure
- name: Amazon Signer Signing Configuration Structure
  property_count: 2
  slug: amazon-signer-signing-configuration-structure
- name: Amazon Signer Signing Image Format Structure
  property_count: 2
  slug: amazon-signer-signing-image-format-structure
- name: Amazon Signer Signing Job Revocation Record Structure
  property_count: 3
  slug: amazon-signer-signing-job-revocation-record-structure
- name: Amazon Signer Signing Job Structure
  property_count: 14
  slug: amazon-signer-signing-job-structure
- name: Amazon Signer Signing Material Structure
  property_count: 1
  slug: amazon-signer-signing-material-structure
- name: Amazon Signer Signing Parameters Structure
  property_count: 0
  slug: amazon-signer-signing-parameters-structure
- name: Amazon Signer Signing Platform Overrides Structure
  property_count: 2
  slug: amazon-signer-signing-platform-overrides-structure
- name: Amazon Signer Signing Platform Structure
  property_count: 9
  slug: amazon-signer-signing-platform-structure
- name: Amazon Signer Signing Profile Revocation Record Structure
  property_count: 3
  slug: amazon-signer-signing-profile-revocation-record-structure
- name: Amazon Signer Signing Profile Status Structure
  property_count: 0
  slug: amazon-signer-signing-profile-status-structure
- name: Amazon Signer Signing Profile Structure
  property_count: 11
  slug: amazon-signer-signing-profile-structure
- name: Amazon Signer Signing Status Structure
  property_count: 0
  slug: amazon-signer-signing-status-structure
- name: Amazon Signer Source Structure
  property_count: 1
  slug: amazon-signer-source-structure
- name: Amazon Signer Start Signing Job Request Structure
  property_count: 5
  slug: amazon-signer-start-signing-job-request-structure
- name: Amazon Signer Start Signing Job Response Structure
  property_count: 2
  slug: amazon-signer-start-signing-job-response-structure
- name: Amazon Signer Tag Map Structure
  property_count: 0
  slug: amazon-signer-tag-map-structure
- name: Amazon Signer Tag Resource Request Structure
  property_count: 1
  slug: amazon-signer-tag-resource-request-structure
- name: Amazon Signer Tag Resource Response Structure
  property_count: 0
  slug: amazon-signer-tag-resource-response-structure
- name: Amazon Signer Untag Resource Request Structure
  property_count: 0
  slug: amazon-signer-untag-resource-request-structure
- name: Amazon Signer Untag Resource Response Structure
  property_count: 0
  slug: amazon-signer-untag-resource-response-structure
- name: Amazon Signer Validity Type Structure
  property_count: 0
  slug: amazon-signer-validity-type-structure
jsonld:
- class_count: 60
  name: Amazon Signer Context
  property_count: 69
  slug: amazon-signer-context
layout: provider
modified: '2026-05-19'
name: Amazon Signer
nav: Providers
network: true
overview: 'Amazon Signer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Revocations#signatureTimestamp&platformId&profileVersionArn&jobArn&certificateHashes API, Signing Jobs API, Signing Platforms API, and 2 more. Tagged areas include Code Signing, IoT, Lambda, and Security.


  The Amazon Signer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Signer''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Signer Plans Pricing
  plan_count: 3
  slug: amazon-signer-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Amazon Signer Rate Limits
  slug: amazon-signer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Signer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-signer-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: Amazon Signer API Rules
  rule_count: 30
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 14
  slug: amazon-signer-spectral-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 28.8
    contract_quality: 68.0
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/screenshots/amazon-signer-2026-06-20T171827.png
security:
- kind: authentication
  name: Amazon Signer Authentication
  slug: amazon-signer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Signer Domain Security
  slug: amazon-signer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Signer Vulnerability Disclosure
  slug: amazon-signer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Signer Trust Center
  slug: amazon-signer-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-signer
tags:
- Code Signing
- IoT
- Lambda
- Security
use_cases:
- description: Sign Lambda deployment packages to ensure only trusted code is deployed.
  name: Lambda Code Signing
- description: Sign firmware images for microcontrollers and over-the-air (OTA) updates via Amazon FreeRTOS.
  name: IoT Firmware Signing
- description: Sign container images using Notation CLI with Amazon ECR and verify at EKS deployment.
  name: Container Image Signing
- description: Track all signing operations via CloudTrail for audit and compliance requirements.
  name: Audit and Compliance
website: https://aws.amazon.com/signer/
---
