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
  name: Amazon Elastic Transcoder Agentic Access
  operation_count: 17
  slug: amazon-elastic-transcoder-agentic-access
  summary_line: 17 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Jobs API from Amazon Elastic Transcoder — 2 operation(s) for jobs.
  name: Amazon Elastic Transcoder Jobs API
  slug: amazon-elastic-transcoder-jobs-api
- description: The JobsByPipeline API from Amazon Elastic Transcoder — 1 operation(s) for jobsbypipeline.
  name: Amazon Elastic Transcoder JobsByPipeline API
  slug: amazon-elastic-transcoder-jobsbypipeline-api
- description: The JobsByStatus API from Amazon Elastic Transcoder — 1 operation(s) for jobsbystatus.
  name: Amazon Elastic Transcoder JobsByStatus API
  slug: amazon-elastic-transcoder-jobsbystatus-api
- description: The Pipelines API from Amazon Elastic Transcoder — 4 operation(s) for pipelines.
  name: Amazon Elastic Transcoder Pipelines API
  slug: amazon-elastic-transcoder-pipelines-api
- description: The Presets API from Amazon Elastic Transcoder — 2 operation(s) for presets.
  name: Amazon Elastic Transcoder Presets API
  slug: amazon-elastic-transcoder-presets-api
- description: The RoleTests API from Amazon Elastic Transcoder — 1 operation(s) for roletests.
  name: Amazon Elastic Transcoder RoleTests API
  slug: amazon-elastic-transcoder-roletests-api
arazzos:
- description: List jobs that are still in the Submitted state, then cancel the first one returned.
  name: Amazon Elastic Transcoder Find a Submitted Job by Status and Cancel It
  slug: amazon-elastic-transcoder-cancel-submitted-jobs-by-status-workflow
- description: List the jobs currently in a pipeline, then read detailed information about the first job returned.
  name: Amazon Elastic Transcoder List Jobs by Pipeline and Read the First Job
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-read-workflow
- description: Pause a pipeline so no new jobs start, then cancel a job that is still in the Submitted state.
  name: Amazon Elastic Transcoder Pause Pipeline and Cancel a Submitted Job
  slug: amazon-elastic-transcoder-pause-pipeline-cancel-submitted-jobs-workflow
- description: Stand up a transcoding pipeline, submit a job to it, then poll the job until it reaches a terminal status.
  name: Amazon Elastic Transcoder Create Pipeline, Submit Job, and Poll to Completion
  slug: amazon-elastic-transcoder-pipeline-job-poll-workflow
- description: Provision both a pipeline and a preset from scratch, submit a job that uses them, then poll the job to completion.
  name: Amazon Elastic Transcoder Provision Pipeline and Preset, Submit Job, and Poll
  slug: amazon-elastic-transcoder-pipeline-preset-job-poll-workflow
- description: Define a reusable output preset, then submit a transcoding job into an existing pipeline that uses the new preset.
  name: Amazon Elastic Transcoder Create Preset and Submit a Job Using It
  slug: amazon-elastic-transcoder-preset-job-workflow
artifact_total: 463
collections:
- collection_type: postman
  name: Amazon Elastic Transcoder Jobs API
  slug: postman-amazon-elastic-transcoder-jobs-api
- collection_type: postman
  name: Amazon Elastic Transcoder Jobs JobsByPipeline API
  slug: postman-amazon-elastic-transcoder-jobsbypipeline-api
- collection_type: postman
  name: Amazon Elastic Transcoder Jobs JobsByStatus API
  slug: postman-amazon-elastic-transcoder-jobsbystatus-api
- collection_type: postman
  name: Amazon Elastic Transcoder Jobs Pipelines API
  slug: postman-amazon-elastic-transcoder-pipelines-api
- collection_type: postman
  name: Amazon Elastic Transcoder Jobs Presets API
  slug: postman-amazon-elastic-transcoder-presets-api
- collection_type: postman
  name: Amazon Elastic Transcoder Jobs RoleTests API
  slug: postman-amazon-elastic-transcoder-roletests-api
- collection_type: postman
  name: Amazon Elastic Transcoder
  slug: postman-amazon-elastic-transcoder
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Elastic Transcoder Jobs API
  slug: open-amazon-elastic-transcoder-jobs-api
- collection_type: open
  name: Amazon Elastic Transcoder Jobs JobsByPipeline API
  slug: open-amazon-elastic-transcoder-jobsbypipeline-api
- collection_type: open
  name: Amazon Elastic Transcoder Jobs JobsByStatus API
  slug: open-amazon-elastic-transcoder-jobsbystatus-api
- collection_type: open
  name: Amazon Elastic Transcoder Jobs Pipelines API
  slug: open-amazon-elastic-transcoder-pipelines-api
- collection_type: open
  name: Amazon Elastic Transcoder Jobs Presets API
  slug: open-amazon-elastic-transcoder-presets-api
- collection_type: open
  name: Amazon Elastic Transcoder Jobs RoleTests API
  slug: open-amazon-elastic-transcoder-roletests-api
- collection_type: open
  name: Amazon Elastic Transcoder
  slug: open-amazon-elastic-transcoder
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-elastic-transcoder-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-elastic-transcoder-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-elastic-transcoder-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-elastic-transcoder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-elastic-transcoder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-elastic-transcoder-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-elastic-transcoder/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-transcoder-cancel-submitted-jobs-by-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-transcoder-list-jobs-by-pipeline-read-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-transcoder-pause-pipeline-cancel-submitted-jobs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-transcoder-pipeline-job-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-transcoder-pipeline-preset-job-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-transcoder-preset-job-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elastictranscoder/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elastictranscoder/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/elastictranscoder/
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
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/elastictranscoder/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elastictranscoder
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-elastic-transcoder-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-elastic-transcoder-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Transcoder is media transcoding in the cloud. It is designed to be a highly scalable, easy-to-use, and cost-effective way for developers and businesses to convert or transcode media files from their source format into versions that will play back on devices like smartphones, tablets, and PCs.
examples:
- key_count: 0
  name: Amazon Elastic Transcoder Access Denied Exception Example
  slug: amazon-elastic-transcoder-access-denied-exception-example
- key_count: 7
  name: Amazon Elastic Transcoder Artwork Example
  slug: amazon-elastic-transcoder-artwork-example
- key_count: 4
  name: Amazon Elastic Transcoder Audio Codec Options Example
  slug: amazon-elastic-transcoder-audio-codec-options-example
- key_count: 6
  name: Amazon Elastic Transcoder Audio Parameters Example
  slug: amazon-elastic-transcoder-audio-parameters-example
- key_count: 0
  name: Amazon Elastic Transcoder Cancel Job Request Example
  slug: amazon-elastic-transcoder-cancel-job-request-example
- key_count: 0
  name: Amazon Elastic Transcoder Cancel Job Response Example
  slug: amazon-elastic-transcoder-cancel-job-response-example
- key_count: 3
  name: Amazon Elastic Transcoder Caption Format Example
  slug: amazon-elastic-transcoder-caption-format-example
- key_count: 5
  name: Amazon Elastic Transcoder Caption Source Example
  slug: amazon-elastic-transcoder-caption-source-example
- key_count: 3
  name: Amazon Elastic Transcoder Captions Example
  slug: amazon-elastic-transcoder-captions-example
- key_count: 1
  name: Amazon Elastic Transcoder Clip Example
  slug: amazon-elastic-transcoder-clip-example
- key_count: 0
  name: Amazon Elastic Transcoder Codec Options Example
  slug: amazon-elastic-transcoder-codec-options-example
- key_count: 10
  name: Amazon Elastic Transcoder Create Job Output Example
  slug: amazon-elastic-transcoder-create-job-output-example
- key_count: 5
  name: Amazon Elastic Transcoder Create Job Playlist Example
  slug: amazon-elastic-transcoder-create-job-playlist-example
- key_count: 8
  name: Amazon Elastic Transcoder Create Job Request Example
  slug: amazon-elastic-transcoder-create-job-request-example
- key_count: 1
  name: Amazon Elastic Transcoder Create Job Response Example
  slug: amazon-elastic-transcoder-create-job-response-example
- key_count: 8
  name: Amazon Elastic Transcoder Create Pipeline Request Example
  slug: amazon-elastic-transcoder-create-pipeline-request-example
- key_count: 2
  name: Amazon Elastic Transcoder Create Pipeline Response Example
  slug: amazon-elastic-transcoder-create-pipeline-response-example
- key_count: 6
  name: Amazon Elastic Transcoder Create Preset Request Example
  slug: amazon-elastic-transcoder-create-preset-request-example
- key_count: 2
  name: Amazon Elastic Transcoder Create Preset Response Example
  slug: amazon-elastic-transcoder-create-preset-response-example
- key_count: 0
  name: Amazon Elastic Transcoder Delete Pipeline Request Example
  slug: amazon-elastic-transcoder-delete-pipeline-request-example
- key_count: 0
  name: Amazon Elastic Transcoder Delete Pipeline Response Example
  slug: amazon-elastic-transcoder-delete-pipeline-response-example
- key_count: 0
  name: Amazon Elastic Transcoder Delete Preset Request Example
  slug: amazon-elastic-transcoder-delete-preset-request-example
- key_count: 0
  name: Amazon Elastic Transcoder Delete Preset Response Example
  slug: amazon-elastic-transcoder-delete-preset-response-example
- key_count: 5
  name: Amazon Elastic Transcoder Detected Properties Example
  slug: amazon-elastic-transcoder-detected-properties-example
- key_count: 4
  name: Amazon Elastic Transcoder Encryption Example
  slug: amazon-elastic-transcoder-encryption-example
- key_count: 6
  name: Amazon Elastic Transcoder Hls Content Protection Example
  slug: amazon-elastic-transcoder-hls-content-protection-example
- key_count: 0
  name: Amazon Elastic Transcoder Incompatible Version Exception Example
  slug: amazon-elastic-transcoder-incompatible-version-exception-example
- key_count: 2
  name: Amazon Elastic Transcoder Input Captions Example
  slug: amazon-elastic-transcoder-input-captions-example
- key_count: 0
  name: Amazon Elastic Transcoder Internal Service Exception Example
  slug: amazon-elastic-transcoder-internal-service-exception-example
- key_count: 2
  name: Amazon Elastic Transcoder Job Album Art Example
  slug: amazon-elastic-transcoder-job-album-art-example
- key_count: 10
  name: Amazon Elastic Transcoder Job Example
  slug: amazon-elastic-transcoder-job-example
- key_count: 10
  name: Amazon Elastic Transcoder Job Input Example
  slug: amazon-elastic-transcoder-job-input-example
- key_count: 10
  name: Amazon Elastic Transcoder Job Output Example
  slug: amazon-elastic-transcoder-job-output-example
- key_count: 3
  name: Amazon Elastic Transcoder Job Watermark Example
  slug: amazon-elastic-transcoder-job-watermark-example
- key_count: 0
  name: Amazon Elastic Transcoder Limit Exceeded Exception Example
  slug: amazon-elastic-transcoder-limit-exceeded-exception-example
- key_count: 0
  name: Amazon Elastic Transcoder List Jobs By Pipeline Request Example
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-request-example
- key_count: 2
  name: Amazon Elastic Transcoder List Jobs By Pipeline Response Example
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-response-example
- key_count: 0
  name: Amazon Elastic Transcoder List Jobs By Status Request Example
  slug: amazon-elastic-transcoder-list-jobs-by-status-request-example
- key_count: 2
  name: Amazon Elastic Transcoder List Jobs By Status Response Example
  slug: amazon-elastic-transcoder-list-jobs-by-status-response-example
- key_count: 0
  name: Amazon Elastic Transcoder List Pipelines Request Example
  slug: amazon-elastic-transcoder-list-pipelines-request-example
- key_count: 2
  name: Amazon Elastic Transcoder List Pipelines Response Example
  slug: amazon-elastic-transcoder-list-pipelines-response-example
- key_count: 0
  name: Amazon Elastic Transcoder List Presets Request Example
  slug: amazon-elastic-transcoder-list-presets-request-example
- key_count: 2
  name: Amazon Elastic Transcoder List Presets Response Example
  slug: amazon-elastic-transcoder-list-presets-response-example
- key_count: 4
  name: Amazon Elastic Transcoder Notifications Example
  slug: amazon-elastic-transcoder-notifications-example
- key_count: 3
  name: Amazon Elastic Transcoder Permission Example
  slug: amazon-elastic-transcoder-permission-example
- key_count: 10
  name: Amazon Elastic Transcoder Pipeline Example
  slug: amazon-elastic-transcoder-pipeline-example
- key_count: 3
  name: Amazon Elastic Transcoder Pipeline Output Config Example
  slug: amazon-elastic-transcoder-pipeline-output-config-example
- key_count: 6
  name: Amazon Elastic Transcoder Play Ready Drm Example
  slug: amazon-elastic-transcoder-play-ready-drm-example
- key_count: 7
  name: Amazon Elastic Transcoder Playlist Example
  slug: amazon-elastic-transcoder-playlist-example
- key_count: 9
  name: Amazon Elastic Transcoder Preset Example
  slug: amazon-elastic-transcoder-preset-example
- key_count: 10
  name: Amazon Elastic Transcoder Preset Watermark Example
  slug: amazon-elastic-transcoder-preset-watermark-example
- key_count: 0
  name: Amazon Elastic Transcoder Read Job Request Example
  slug: amazon-elastic-transcoder-read-job-request-example
- key_count: 1
  name: Amazon Elastic Transcoder Read Job Response Example
  slug: amazon-elastic-transcoder-read-job-response-example
- key_count: 0
  name: Amazon Elastic Transcoder Read Pipeline Request Example
  slug: amazon-elastic-transcoder-read-pipeline-request-example
- key_count: 2
  name: Amazon Elastic Transcoder Read Pipeline Response Example
  slug: amazon-elastic-transcoder-read-pipeline-response-example
- key_count: 0
  name: Amazon Elastic Transcoder Read Preset Request Example
  slug: amazon-elastic-transcoder-read-preset-request-example
- key_count: 1
  name: Amazon Elastic Transcoder Read Preset Response Example
  slug: amazon-elastic-transcoder-read-preset-response-example
- key_count: 0
  name: Amazon Elastic Transcoder Resource In Use Exception Example
  slug: amazon-elastic-transcoder-resource-in-use-exception-example
- key_count: 0
  name: Amazon Elastic Transcoder Resource Not Found Exception Example
  slug: amazon-elastic-transcoder-resource-not-found-exception-example
- key_count: 4
  name: Amazon Elastic Transcoder Test Role Request Example
  slug: amazon-elastic-transcoder-test-role-request-example
- key_count: 2
  name: Amazon Elastic Transcoder Test Role Response Example
  slug: amazon-elastic-transcoder-test-role-response-example
- key_count: 8
  name: Amazon Elastic Transcoder Thumbnails Example
  slug: amazon-elastic-transcoder-thumbnails-example
- key_count: 2
  name: Amazon Elastic Transcoder Time Span Example
  slug: amazon-elastic-transcoder-time-span-example
- key_count: 3
  name: Amazon Elastic Transcoder Timing Example
  slug: amazon-elastic-transcoder-timing-example
- key_count: 1
  name: Amazon Elastic Transcoder Update Pipeline Notifications Request Example
  slug: amazon-elastic-transcoder-update-pipeline-notifications-request-example
- key_count: 1
  name: Amazon Elastic Transcoder Update Pipeline Notifications Response Example
  slug: amazon-elastic-transcoder-update-pipeline-notifications-response-example
- key_count: 7
  name: Amazon Elastic Transcoder Update Pipeline Request Example
  slug: amazon-elastic-transcoder-update-pipeline-request-example
- key_count: 2
  name: Amazon Elastic Transcoder Update Pipeline Response Example
  slug: amazon-elastic-transcoder-update-pipeline-response-example
- key_count: 1
  name: Amazon Elastic Transcoder Update Pipeline Status Request Example
  slug: amazon-elastic-transcoder-update-pipeline-status-request-example
- key_count: 1
  name: Amazon Elastic Transcoder Update Pipeline Status Response Example
  slug: amazon-elastic-transcoder-update-pipeline-status-response-example
- key_count: 0
  name: Amazon Elastic Transcoder User Metadata Example
  slug: amazon-elastic-transcoder-user-metadata-example
- key_count: 0
  name: Amazon Elastic Transcoder Validation Exception Example
  slug: amazon-elastic-transcoder-validation-exception-example
- key_count: 10
  name: Amazon Elastic Transcoder Video Parameters Example
  slug: amazon-elastic-transcoder-video-parameters-example
- key_count: 2
  name: Amazon Elastic Transcoder Warning Example
  slug: amazon-elastic-transcoder-warning-example
features:
- description: Create pipelines that manage media transcoding jobs with configurable input/output settings
  name: Managed Transcoding Pipelines
- description: Use built-in presets optimized for popular devices and formats
  name: Preset Library
- description: Create custom presets for specific output requirements
  name: Custom Presets
- description: Automatically generate thumbnails from video files during transcoding
  name: Thumbnail Generation
- description: Apply HLS content protection and digital rights management
  name: Content Protection
finops:
- name: Amazon Elastic Transcoder Finops
  service_category: API
  slug: amazon-elastic-transcoder-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AccessControl
  property_count: 0
  slug: amazon-elastic-transcoder-access-control
- name: AccessControls
  property_count: 0
  slug: amazon-elastic-transcoder-access-controls
- name: AccessDeniedException
  property_count: 0
  slug: amazon-elastic-transcoder-access-denied-exception
- name: Artwork
  property_count: 7
  slug: amazon-elastic-transcoder-artwork
- name: Artworks
  property_count: 0
  slug: amazon-elastic-transcoder-artworks
- name: Ascending
  property_count: 0
  slug: amazon-elastic-transcoder-ascending
- name: AspectRatio
  property_count: 0
  slug: amazon-elastic-transcoder-aspect-ratio
- name: AudioBitDepth
  property_count: 0
  slug: amazon-elastic-transcoder-audio-bit-depth
- name: AudioBitOrder
  property_count: 0
  slug: amazon-elastic-transcoder-audio-bit-order
- name: AudioBitRate
  property_count: 0
  slug: amazon-elastic-transcoder-audio-bit-rate
- name: AudioChannels
  property_count: 0
  slug: amazon-elastic-transcoder-audio-channels
- name: AudioCodecOptions
  property_count: 4
  slug: amazon-elastic-transcoder-audio-codec-options
- name: AudioCodecProfile
  property_count: 0
  slug: amazon-elastic-transcoder-audio-codec-profile
- name: AudioCodec
  property_count: 0
  slug: amazon-elastic-transcoder-audio-codec
- name: AudioPackingMode
  property_count: 0
  slug: amazon-elastic-transcoder-audio-packing-mode
- name: AudioParameters
  property_count: 6
  slug: amazon-elastic-transcoder-audio-parameters
- name: AudioSampleRate
  property_count: 0
  slug: amazon-elastic-transcoder-audio-sample-rate
- name: AudioSigned
  property_count: 0
  slug: amazon-elastic-transcoder-audio-signed
- name: Base64EncodedString
  property_count: 0
  slug: amazon-elastic-transcoder-base64-encoded-string
- name: BucketName
  property_count: 0
  slug: amazon-elastic-transcoder-bucket-name
- name: CancelJobRequest
  property_count: 0
  slug: amazon-elastic-transcoder-cancel-job-request
- name: CancelJobResponse
  property_count: 0
  slug: amazon-elastic-transcoder-cancel-job-response
- name: CaptionFormatFormat
  property_count: 0
  slug: amazon-elastic-transcoder-caption-format-format
- name: CaptionFormatPattern
  property_count: 0
  slug: amazon-elastic-transcoder-caption-format-pattern
- name: CaptionFormat
  property_count: 3
  slug: amazon-elastic-transcoder-caption-format
- name: CaptionFormats
  property_count: 0
  slug: amazon-elastic-transcoder-caption-formats
- name: CaptionMergePolicy
  property_count: 0
  slug: amazon-elastic-transcoder-caption-merge-policy
- name: CaptionSource
  property_count: 5
  slug: amazon-elastic-transcoder-caption-source
- name: CaptionSources
  property_count: 0
  slug: amazon-elastic-transcoder-caption-sources
- name: Captions
  property_count: 3
  slug: amazon-elastic-transcoder-captions
- name: Clip
  property_count: 1
  slug: amazon-elastic-transcoder-clip
- name: CodecOption
  property_count: 0
  slug: amazon-elastic-transcoder-codec-option
- name: CodecOptions
  property_count: 0
  slug: amazon-elastic-transcoder-codec-options
- name: Composition
  property_count: 0
  slug: amazon-elastic-transcoder-composition
- name: CreateJobOutput
  property_count: 11
  slug: amazon-elastic-transcoder-create-job-output
- name: CreateJobOutputs
  property_count: 0
  slug: amazon-elastic-transcoder-create-job-outputs
- name: CreateJobPlaylist
  property_count: 5
  slug: amazon-elastic-transcoder-create-job-playlist
- name: CreateJobPlaylists
  property_count: 0
  slug: amazon-elastic-transcoder-create-job-playlists
- name: CreateJobRequest
  property_count: 8
  slug: amazon-elastic-transcoder-create-job-request
- name: CreateJobResponse
  property_count: 1
  slug: amazon-elastic-transcoder-create-job-response
- name: CreatePipelineRequest
  property_count: 8
  slug: amazon-elastic-transcoder-create-pipeline-request
- name: CreatePipelineResponse
  property_count: 2
  slug: amazon-elastic-transcoder-create-pipeline-response
- name: CreatePresetRequest
  property_count: 6
  slug: amazon-elastic-transcoder-create-preset-request
- name: CreatePresetResponse
  property_count: 2
  slug: amazon-elastic-transcoder-create-preset-response
- name: DeletePipelineRequest
  property_count: 0
  slug: amazon-elastic-transcoder-delete-pipeline-request
- name: DeletePipelineResponse
  property_count: 0
  slug: amazon-elastic-transcoder-delete-pipeline-response
- name: DeletePresetRequest
  property_count: 0
  slug: amazon-elastic-transcoder-delete-preset-request
- name: DeletePresetResponse
  property_count: 0
  slug: amazon-elastic-transcoder-delete-preset-response
- name: Description
  property_count: 0
  slug: amazon-elastic-transcoder-description
- name: DetectedProperties
  property_count: 5
  slug: amazon-elastic-transcoder-detected-properties
- name: DigitsOrAuto
  property_count: 0
  slug: amazon-elastic-transcoder-digits-or-auto
- name: Digits
  property_count: 0
  slug: amazon-elastic-transcoder-digits
- name: EncryptionMode
  property_count: 0
  slug: amazon-elastic-transcoder-encryption-mode
- name: Encryption
  property_count: 4
  slug: amazon-elastic-transcoder-encryption
- name: ExceptionMessages
  property_count: 0
  slug: amazon-elastic-transcoder-exception-messages
- name: Filename
  property_count: 0
  slug: amazon-elastic-transcoder-filename
- name: FixedGOP
  property_count: 0
  slug: amazon-elastic-transcoder-fixed-gop
- name: FloatString
  property_count: 0
  slug: amazon-elastic-transcoder-float-string
- name: FrameRate
  property_count: 0
  slug: amazon-elastic-transcoder-frame-rate
- name: Grantee
  property_count: 0
  slug: amazon-elastic-transcoder-grantee
- name: GranteeType
  property_count: 0
  slug: amazon-elastic-transcoder-grantee-type
- name: HlsContentProtectionMethod
  property_count: 0
  slug: amazon-elastic-transcoder-hls-content-protection-method
- name: HlsContentProtection
  property_count: 6
  slug: amazon-elastic-transcoder-hls-content-protection
- name: HorizontalAlign
  property_count: 0
  slug: amazon-elastic-transcoder-horizontal-align
- name: Id
  property_count: 0
  slug: amazon-elastic-transcoder-id
- name: IncompatibleVersionException
  property_count: 0
  slug: amazon-elastic-transcoder-incompatible-version-exception
- name: InputCaptions
  property_count: 2
  slug: amazon-elastic-transcoder-input-captions
- name: Interlaced
  property_count: 0
  slug: amazon-elastic-transcoder-interlaced
- name: InternalServiceException
  property_count: 0
  slug: amazon-elastic-transcoder-internal-service-exception
- name: JobAlbumArt
  property_count: 2
  slug: amazon-elastic-transcoder-job-album-art
- name: JobContainer
  property_count: 0
  slug: amazon-elastic-transcoder-job-container
- name: JobInput
  property_count: 10
  slug: amazon-elastic-transcoder-job-input
- name: JobInputs
  property_count: 0
  slug: amazon-elastic-transcoder-job-inputs
- name: JobOutput
  property_count: 21
  slug: amazon-elastic-transcoder-job-output
- name: JobOutputs
  property_count: 0
  slug: amazon-elastic-transcoder-job-outputs
- name: Job
  property_count: 12
  slug: amazon-elastic-transcoder-job
- name: JobStatus
  property_count: 0
  slug: amazon-elastic-transcoder-job-status
- name: JobWatermark
  property_count: 3
  slug: amazon-elastic-transcoder-job-watermark
- name: JobWatermarks
  property_count: 0
  slug: amazon-elastic-transcoder-job-watermarks
- name: Jobs
  property_count: 0
  slug: amazon-elastic-transcoder-jobs
- name: JpgOrPng
  property_count: 0
  slug: amazon-elastic-transcoder-jpg-or-png
- name: KeyArn
  property_count: 0
  slug: amazon-elastic-transcoder-key-arn
- name: KeyIdGuid
  property_count: 0
  slug: amazon-elastic-transcoder-key-id-guid
- name: Key
  property_count: 0
  slug: amazon-elastic-transcoder-key
- name: KeyStoragePolicy
  property_count: 0
  slug: amazon-elastic-transcoder-key-storage-policy
- name: KeyframesMaxDist
  property_count: 0
  slug: amazon-elastic-transcoder-keyframes-max-dist
- name: LimitExceededException
  property_count: 0
  slug: amazon-elastic-transcoder-limit-exceeded-exception
- name: ListJobsByPipelineRequest
  property_count: 0
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-request
- name: ListJobsByPipelineResponse
  property_count: 2
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-response
- name: ListJobsByStatusRequest
  property_count: 0
  slug: amazon-elastic-transcoder-list-jobs-by-status-request
- name: ListJobsByStatusResponse
  property_count: 2
  slug: amazon-elastic-transcoder-list-jobs-by-status-response
- name: ListPipelinesRequest
  property_count: 0
  slug: amazon-elastic-transcoder-list-pipelines-request
- name: ListPipelinesResponse
  property_count: 2
  slug: amazon-elastic-transcoder-list-pipelines-response
- name: ListPresetsRequest
  property_count: 0
  slug: amazon-elastic-transcoder-list-presets-request
- name: ListPresetsResponse
  property_count: 2
  slug: amazon-elastic-transcoder-list-presets-response
- name: LongKey
  property_count: 0
  slug: amazon-elastic-transcoder-long-key
- name: MaxFrameRate
  property_count: 0
  slug: amazon-elastic-transcoder-max-frame-rate
- name: MergePolicy
  property_count: 0
  slug: amazon-elastic-transcoder-merge-policy
- name: Name
  property_count: 0
  slug: amazon-elastic-transcoder-name
- name: NonEmptyBase64EncodedString
  property_count: 0
  slug: amazon-elastic-transcoder-non-empty-base64-encoded-string
- name: Notifications
  property_count: 4
  slug: amazon-elastic-transcoder-notifications
- name: NullableInteger
  property_count: 0
  slug: amazon-elastic-transcoder-nullable-integer
- name: NullableLong
  property_count: 0
  slug: amazon-elastic-transcoder-nullable-long
- name: OneTo512String
  property_count: 0
  slug: amazon-elastic-transcoder-one-to512-string
- name: Opacity
  property_count: 0
  slug: amazon-elastic-transcoder-opacity
- name: OutputKeys
  property_count: 0
  slug: amazon-elastic-transcoder-output-keys
- name: PaddingPolicy
  property_count: 0
  slug: amazon-elastic-transcoder-padding-policy
- name: Permission
  property_count: 3
  slug: amazon-elastic-transcoder-permission
- name: Permissions
  property_count: 0
  slug: amazon-elastic-transcoder-permissions
- name: PipelineOutputConfig
  property_count: 3
  slug: amazon-elastic-transcoder-pipeline-output-config
- name: Pipeline
  property_count: 11
  slug: amazon-elastic-transcoder-pipeline
- name: PipelineStatus
  property_count: 0
  slug: amazon-elastic-transcoder-pipeline-status
- name: Pipelines
  property_count: 0
  slug: amazon-elastic-transcoder-pipelines
- name: PixelsOrPercent
  property_count: 0
  slug: amazon-elastic-transcoder-pixels-or-percent
- name: PlayReadyDrmFormatString
  property_count: 0
  slug: amazon-elastic-transcoder-play-ready-drm-format-string
- name: PlayReadyDrm
  property_count: 6
  slug: amazon-elastic-transcoder-play-ready-drm
- name: PlaylistFormat
  property_count: 0
  slug: amazon-elastic-transcoder-playlist-format
- name: Playlist
  property_count: 7
  slug: amazon-elastic-transcoder-playlist
- name: Playlists
  property_count: 0
  slug: amazon-elastic-transcoder-playlists
- name: PresetContainer
  property_count: 0
  slug: amazon-elastic-transcoder-preset-container
- name: Preset
  property_count: 9
  slug: amazon-elastic-transcoder-preset
- name: PresetType
  property_count: 0
  slug: amazon-elastic-transcoder-preset-type
- name: PresetWatermarkId
  property_count: 0
  slug: amazon-elastic-transcoder-preset-watermark-id
- name: PresetWatermark
  property_count: 10
  slug: amazon-elastic-transcoder-preset-watermark
- name: PresetWatermarks
  property_count: 0
  slug: amazon-elastic-transcoder-preset-watermarks
- name: Presets
  property_count: 0
  slug: amazon-elastic-transcoder-presets
- name: ReadJobRequest
  property_count: 0
  slug: amazon-elastic-transcoder-read-job-request
- name: ReadJobResponse
  property_count: 1
  slug: amazon-elastic-transcoder-read-job-response
- name: ReadPipelineRequest
  property_count: 0
  slug: amazon-elastic-transcoder-read-pipeline-request
- name: ReadPipelineResponse
  property_count: 2
  slug: amazon-elastic-transcoder-read-pipeline-response
- name: ReadPresetRequest
  property_count: 0
  slug: amazon-elastic-transcoder-read-preset-request
- name: ReadPresetResponse
  property_count: 1
  slug: amazon-elastic-transcoder-read-preset-response
- name: Resolution
  property_count: 0
  slug: amazon-elastic-transcoder-resolution
- name: ResourceInUseException
  property_count: 0
  slug: amazon-elastic-transcoder-resource-in-use-exception
- name: ResourceNotFoundException
  property_count: 0
  slug: amazon-elastic-transcoder-resource-not-found-exception
- name: Role
  property_count: 0
  slug: amazon-elastic-transcoder-role
- name: Rotate
  property_count: 0
  slug: amazon-elastic-transcoder-rotate
- name: SizingPolicy
  property_count: 0
  slug: amazon-elastic-transcoder-sizing-policy
- name: SnsTopic
  property_count: 0
  slug: amazon-elastic-transcoder-sns-topic
- name: SnsTopics
  property_count: 0
  slug: amazon-elastic-transcoder-sns-topics
- name: StorageClass
  property_count: 0
  slug: amazon-elastic-transcoder-storage-class
- name: String
  property_count: 0
  slug: amazon-elastic-transcoder-string
- name: Success
  property_count: 0
  slug: amazon-elastic-transcoder-success
- name: Target
  property_count: 0
  slug: amazon-elastic-transcoder-target
- name: TestRoleRequest
  property_count: 4
  slug: amazon-elastic-transcoder-test-role-request
- name: TestRoleResponse
  property_count: 2
  slug: amazon-elastic-transcoder-test-role-response
- name: ThumbnailPattern
  property_count: 0
  slug: amazon-elastic-transcoder-thumbnail-pattern
- name: ThumbnailResolution
  property_count: 0
  slug: amazon-elastic-transcoder-thumbnail-resolution
- name: Thumbnails
  property_count: 8
  slug: amazon-elastic-transcoder-thumbnails
- name: TimeOffset
  property_count: 0
  slug: amazon-elastic-transcoder-time-offset
- name: Time
  property_count: 0
  slug: amazon-elastic-transcoder-time
- name: TimeSpan
  property_count: 2
  slug: amazon-elastic-transcoder-time-span
- name: Timing
  property_count: 3
  slug: amazon-elastic-transcoder-timing
- name: UpdatePipelineNotificationsRequest
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-notifications-request
- name: UpdatePipelineNotificationsResponse
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-notifications-response
- name: UpdatePipelineRequest
  property_count: 7
  slug: amazon-elastic-transcoder-update-pipeline-request
- name: UpdatePipelineResponse
  property_count: 2
  slug: amazon-elastic-transcoder-update-pipeline-response
- name: UpdatePipelineStatusRequest
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-status-request
- name: UpdatePipelineStatusResponse
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-status-response
- name: UserMetadata
  property_count: 0
  slug: amazon-elastic-transcoder-user-metadata
- name: ValidationException
  property_count: 0
  slug: amazon-elastic-transcoder-validation-exception
- name: VerticalAlign
  property_count: 0
  slug: amazon-elastic-transcoder-vertical-align
- name: VideoBitRate
  property_count: 0
  slug: amazon-elastic-transcoder-video-bit-rate
- name: VideoCodec
  property_count: 0
  slug: amazon-elastic-transcoder-video-codec
- name: VideoParameters
  property_count: 15
  slug: amazon-elastic-transcoder-video-parameters
- name: Warning
  property_count: 2
  slug: amazon-elastic-transcoder-warning
- name: Warnings
  property_count: 0
  slug: amazon-elastic-transcoder-warnings
- name: WatermarkKey
  property_count: 0
  slug: amazon-elastic-transcoder-watermark-key
- name: WatermarkSizingPolicy
  property_count: 0
  slug: amazon-elastic-transcoder-watermark-sizing-policy
- name: ZeroTo255String
  property_count: 0
  slug: amazon-elastic-transcoder-zero-to255-string
- name: ZeroTo512String
  property_count: 0
  slug: amazon-elastic-transcoder-zero-to512-string
json_structures:
- name: Amazon Elastic Transcoder Access Control Structure
  property_count: 0
  slug: amazon-elastic-transcoder-access-control-structure
- name: Amazon Elastic Transcoder Access Controls Structure
  property_count: 0
  slug: amazon-elastic-transcoder-access-controls-structure
- name: Amazon Elastic Transcoder Access Denied Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-access-denied-exception-structure
- name: Amazon Elastic Transcoder Artwork Structure
  property_count: 7
  slug: amazon-elastic-transcoder-artwork-structure
- name: Amazon Elastic Transcoder Artworks Structure
  property_count: 0
  slug: amazon-elastic-transcoder-artworks-structure
- name: Amazon Elastic Transcoder Ascending Structure
  property_count: 0
  slug: amazon-elastic-transcoder-ascending-structure
- name: Amazon Elastic Transcoder Aspect Ratio Structure
  property_count: 0
  slug: amazon-elastic-transcoder-aspect-ratio-structure
- name: Amazon Elastic Transcoder Audio Bit Depth Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-bit-depth-structure
- name: Amazon Elastic Transcoder Audio Bit Order Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-bit-order-structure
- name: Amazon Elastic Transcoder Audio Bit Rate Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-bit-rate-structure
- name: Amazon Elastic Transcoder Audio Channels Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-channels-structure
- name: Amazon Elastic Transcoder Audio Codec Options Structure
  property_count: 4
  slug: amazon-elastic-transcoder-audio-codec-options-structure
- name: Amazon Elastic Transcoder Audio Codec Profile Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-codec-profile-structure
- name: Amazon Elastic Transcoder Audio Codec Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-codec-structure
- name: Amazon Elastic Transcoder Audio Packing Mode Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-packing-mode-structure
- name: Amazon Elastic Transcoder Audio Parameters Structure
  property_count: 6
  slug: amazon-elastic-transcoder-audio-parameters-structure
- name: Amazon Elastic Transcoder Audio Sample Rate Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-sample-rate-structure
- name: Amazon Elastic Transcoder Audio Signed Structure
  property_count: 0
  slug: amazon-elastic-transcoder-audio-signed-structure
- name: Amazon Elastic Transcoder Base64 Encoded String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-base64-encoded-string-structure
- name: Amazon Elastic Transcoder Bucket Name Structure
  property_count: 0
  slug: amazon-elastic-transcoder-bucket-name-structure
- name: Amazon Elastic Transcoder Cancel Job Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-cancel-job-request-structure
- name: Amazon Elastic Transcoder Cancel Job Response Structure
  property_count: 0
  slug: amazon-elastic-transcoder-cancel-job-response-structure
- name: Amazon Elastic Transcoder Caption Format Format Structure
  property_count: 0
  slug: amazon-elastic-transcoder-caption-format-format-structure
- name: Amazon Elastic Transcoder Caption Format Pattern Structure
  property_count: 0
  slug: amazon-elastic-transcoder-caption-format-pattern-structure
- name: Amazon Elastic Transcoder Caption Format Structure
  property_count: 3
  slug: amazon-elastic-transcoder-caption-format-structure
- name: Amazon Elastic Transcoder Caption Formats Structure
  property_count: 0
  slug: amazon-elastic-transcoder-caption-formats-structure
- name: Amazon Elastic Transcoder Caption Merge Policy Structure
  property_count: 0
  slug: amazon-elastic-transcoder-caption-merge-policy-structure
- name: Amazon Elastic Transcoder Caption Source Structure
  property_count: 5
  slug: amazon-elastic-transcoder-caption-source-structure
- name: Amazon Elastic Transcoder Caption Sources Structure
  property_count: 0
  slug: amazon-elastic-transcoder-caption-sources-structure
- name: Amazon Elastic Transcoder Captions Structure
  property_count: 3
  slug: amazon-elastic-transcoder-captions-structure
- name: Amazon Elastic Transcoder Clip Structure
  property_count: 1
  slug: amazon-elastic-transcoder-clip-structure
- name: Amazon Elastic Transcoder Codec Option Structure
  property_count: 0
  slug: amazon-elastic-transcoder-codec-option-structure
- name: Amazon Elastic Transcoder Codec Options Structure
  property_count: 0
  slug: amazon-elastic-transcoder-codec-options-structure
- name: Amazon Elastic Transcoder Composition Structure
  property_count: 0
  slug: amazon-elastic-transcoder-composition-structure
- name: Amazon Elastic Transcoder Create Job Output Structure
  property_count: 11
  slug: amazon-elastic-transcoder-create-job-output-structure
- name: Amazon Elastic Transcoder Create Job Outputs Structure
  property_count: 0
  slug: amazon-elastic-transcoder-create-job-outputs-structure
- name: Amazon Elastic Transcoder Create Job Playlist Structure
  property_count: 5
  slug: amazon-elastic-transcoder-create-job-playlist-structure
- name: Amazon Elastic Transcoder Create Job Playlists Structure
  property_count: 0
  slug: amazon-elastic-transcoder-create-job-playlists-structure
- name: Amazon Elastic Transcoder Create Job Request Structure
  property_count: 8
  slug: amazon-elastic-transcoder-create-job-request-structure
- name: Amazon Elastic Transcoder Create Job Response Structure
  property_count: 1
  slug: amazon-elastic-transcoder-create-job-response-structure
- name: Amazon Elastic Transcoder Create Pipeline Request Structure
  property_count: 8
  slug: amazon-elastic-transcoder-create-pipeline-request-structure
- name: Amazon Elastic Transcoder Create Pipeline Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-create-pipeline-response-structure
- name: Amazon Elastic Transcoder Create Preset Request Structure
  property_count: 6
  slug: amazon-elastic-transcoder-create-preset-request-structure
- name: Amazon Elastic Transcoder Create Preset Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-create-preset-response-structure
- name: Amazon Elastic Transcoder Delete Pipeline Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-delete-pipeline-request-structure
- name: Amazon Elastic Transcoder Delete Pipeline Response Structure
  property_count: 0
  slug: amazon-elastic-transcoder-delete-pipeline-response-structure
- name: Amazon Elastic Transcoder Delete Preset Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-delete-preset-request-structure
- name: Amazon Elastic Transcoder Delete Preset Response Structure
  property_count: 0
  slug: amazon-elastic-transcoder-delete-preset-response-structure
- name: Amazon Elastic Transcoder Description Structure
  property_count: 0
  slug: amazon-elastic-transcoder-description-structure
- name: Amazon Elastic Transcoder Detected Properties Structure
  property_count: 5
  slug: amazon-elastic-transcoder-detected-properties-structure
- name: Amazon Elastic Transcoder Digits Or Auto Structure
  property_count: 0
  slug: amazon-elastic-transcoder-digits-or-auto-structure
- name: Amazon Elastic Transcoder Digits Structure
  property_count: 0
  slug: amazon-elastic-transcoder-digits-structure
- name: Amazon Elastic Transcoder Encryption Mode Structure
  property_count: 0
  slug: amazon-elastic-transcoder-encryption-mode-structure
- name: Amazon Elastic Transcoder Encryption Structure
  property_count: 4
  slug: amazon-elastic-transcoder-encryption-structure
- name: Amazon Elastic Transcoder Exception Messages Structure
  property_count: 0
  slug: amazon-elastic-transcoder-exception-messages-structure
- name: Amazon Elastic Transcoder Filename Structure
  property_count: 0
  slug: amazon-elastic-transcoder-filename-structure
- name: Amazon Elastic Transcoder Fixed Gop Structure
  property_count: 0
  slug: amazon-elastic-transcoder-fixed-gop-structure
- name: Amazon Elastic Transcoder Float String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-float-string-structure
- name: Amazon Elastic Transcoder Frame Rate Structure
  property_count: 0
  slug: amazon-elastic-transcoder-frame-rate-structure
- name: Amazon Elastic Transcoder Grantee Structure
  property_count: 0
  slug: amazon-elastic-transcoder-grantee-structure
- name: Amazon Elastic Transcoder Grantee Type Structure
  property_count: 0
  slug: amazon-elastic-transcoder-grantee-type-structure
- name: Amazon Elastic Transcoder Hls Content Protection Method Structure
  property_count: 0
  slug: amazon-elastic-transcoder-hls-content-protection-method-structure
- name: Amazon Elastic Transcoder Hls Content Protection Structure
  property_count: 6
  slug: amazon-elastic-transcoder-hls-content-protection-structure
- name: Amazon Elastic Transcoder Horizontal Align Structure
  property_count: 0
  slug: amazon-elastic-transcoder-horizontal-align-structure
- name: Amazon Elastic Transcoder Id Structure
  property_count: 0
  slug: amazon-elastic-transcoder-id-structure
- name: Amazon Elastic Transcoder Incompatible Version Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-incompatible-version-exception-structure
- name: Amazon Elastic Transcoder Input Captions Structure
  property_count: 2
  slug: amazon-elastic-transcoder-input-captions-structure
- name: Amazon Elastic Transcoder Interlaced Structure
  property_count: 0
  slug: amazon-elastic-transcoder-interlaced-structure
- name: Amazon Elastic Transcoder Internal Service Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-internal-service-exception-structure
- name: Amazon Elastic Transcoder Job Album Art Structure
  property_count: 2
  slug: amazon-elastic-transcoder-job-album-art-structure
- name: Amazon Elastic Transcoder Job Container Structure
  property_count: 0
  slug: amazon-elastic-transcoder-job-container-structure
- name: Amazon Elastic Transcoder Job Input Structure
  property_count: 10
  slug: amazon-elastic-transcoder-job-input-structure
- name: Amazon Elastic Transcoder Job Inputs Structure
  property_count: 0
  slug: amazon-elastic-transcoder-job-inputs-structure
- name: Amazon Elastic Transcoder Job Output Structure
  property_count: 21
  slug: amazon-elastic-transcoder-job-output-structure
- name: Amazon Elastic Transcoder Job Outputs Structure
  property_count: 0
  slug: amazon-elastic-transcoder-job-outputs-structure
- name: Amazon Elastic Transcoder Job Status Structure
  property_count: 0
  slug: amazon-elastic-transcoder-job-status-structure
- name: Amazon Elastic Transcoder Job Structure
  property_count: 12
  slug: amazon-elastic-transcoder-job-structure
- name: Amazon Elastic Transcoder Job Watermark Structure
  property_count: 3
  slug: amazon-elastic-transcoder-job-watermark-structure
- name: Amazon Elastic Transcoder Job Watermarks Structure
  property_count: 0
  slug: amazon-elastic-transcoder-job-watermarks-structure
- name: Amazon Elastic Transcoder Jobs Structure
  property_count: 0
  slug: amazon-elastic-transcoder-jobs-structure
- name: Amazon Elastic Transcoder Jpg Or Png Structure
  property_count: 0
  slug: amazon-elastic-transcoder-jpg-or-png-structure
- name: Amazon Elastic Transcoder Key Arn Structure
  property_count: 0
  slug: amazon-elastic-transcoder-key-arn-structure
- name: Amazon Elastic Transcoder Key Id Guid Structure
  property_count: 0
  slug: amazon-elastic-transcoder-key-id-guid-structure
- name: Amazon Elastic Transcoder Key Storage Policy Structure
  property_count: 0
  slug: amazon-elastic-transcoder-key-storage-policy-structure
- name: Amazon Elastic Transcoder Key Structure
  property_count: 0
  slug: amazon-elastic-transcoder-key-structure
- name: Amazon Elastic Transcoder Keyframes Max Dist Structure
  property_count: 0
  slug: amazon-elastic-transcoder-keyframes-max-dist-structure
- name: Amazon Elastic Transcoder Limit Exceeded Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-limit-exceeded-exception-structure
- name: Amazon Elastic Transcoder List Jobs By Pipeline Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-request-structure
- name: Amazon Elastic Transcoder List Jobs By Pipeline Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-list-jobs-by-pipeline-response-structure
- name: Amazon Elastic Transcoder List Jobs By Status Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-list-jobs-by-status-request-structure
- name: Amazon Elastic Transcoder List Jobs By Status Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-list-jobs-by-status-response-structure
- name: Amazon Elastic Transcoder List Pipelines Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-list-pipelines-request-structure
- name: Amazon Elastic Transcoder List Pipelines Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-list-pipelines-response-structure
- name: Amazon Elastic Transcoder List Presets Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-list-presets-request-structure
- name: Amazon Elastic Transcoder List Presets Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-list-presets-response-structure
- name: Amazon Elastic Transcoder Long Key Structure
  property_count: 0
  slug: amazon-elastic-transcoder-long-key-structure
- name: Amazon Elastic Transcoder Max Frame Rate Structure
  property_count: 0
  slug: amazon-elastic-transcoder-max-frame-rate-structure
- name: Amazon Elastic Transcoder Merge Policy Structure
  property_count: 0
  slug: amazon-elastic-transcoder-merge-policy-structure
- name: Amazon Elastic Transcoder Name Structure
  property_count: 0
  slug: amazon-elastic-transcoder-name-structure
- name: Amazon Elastic Transcoder Non Empty Base64 Encoded String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-non-empty-base64-encoded-string-structure
- name: Amazon Elastic Transcoder Notifications Structure
  property_count: 4
  slug: amazon-elastic-transcoder-notifications-structure
- name: Amazon Elastic Transcoder Nullable Integer Structure
  property_count: 0
  slug: amazon-elastic-transcoder-nullable-integer-structure
- name: Amazon Elastic Transcoder Nullable Long Structure
  property_count: 0
  slug: amazon-elastic-transcoder-nullable-long-structure
- name: Amazon Elastic Transcoder One To512 String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-one-to512-string-structure
- name: Amazon Elastic Transcoder Opacity Structure
  property_count: 0
  slug: amazon-elastic-transcoder-opacity-structure
- name: Amazon Elastic Transcoder Output Keys Structure
  property_count: 0
  slug: amazon-elastic-transcoder-output-keys-structure
- name: Amazon Elastic Transcoder Padding Policy Structure
  property_count: 0
  slug: amazon-elastic-transcoder-padding-policy-structure
- name: Amazon Elastic Transcoder Permission Structure
  property_count: 3
  slug: amazon-elastic-transcoder-permission-structure
- name: Amazon Elastic Transcoder Permissions Structure
  property_count: 0
  slug: amazon-elastic-transcoder-permissions-structure
- name: Amazon Elastic Transcoder Pipeline Output Config Structure
  property_count: 3
  slug: amazon-elastic-transcoder-pipeline-output-config-structure
- name: Amazon Elastic Transcoder Pipeline Status Structure
  property_count: 0
  slug: amazon-elastic-transcoder-pipeline-status-structure
- name: Amazon Elastic Transcoder Pipeline Structure
  property_count: 11
  slug: amazon-elastic-transcoder-pipeline-structure
- name: Amazon Elastic Transcoder Pipelines Structure
  property_count: 0
  slug: amazon-elastic-transcoder-pipelines-structure
- name: Amazon Elastic Transcoder Pixels Or Percent Structure
  property_count: 0
  slug: amazon-elastic-transcoder-pixels-or-percent-structure
- name: Amazon Elastic Transcoder Play Ready Drm Format String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-play-ready-drm-format-string-structure
- name: Amazon Elastic Transcoder Play Ready Drm Structure
  property_count: 6
  slug: amazon-elastic-transcoder-play-ready-drm-structure
- name: Amazon Elastic Transcoder Playlist Format Structure
  property_count: 0
  slug: amazon-elastic-transcoder-playlist-format-structure
- name: Amazon Elastic Transcoder Playlist Structure
  property_count: 7
  slug: amazon-elastic-transcoder-playlist-structure
- name: Amazon Elastic Transcoder Playlists Structure
  property_count: 0
  slug: amazon-elastic-transcoder-playlists-structure
- name: Amazon Elastic Transcoder Preset Container Structure
  property_count: 0
  slug: amazon-elastic-transcoder-preset-container-structure
- name: Amazon Elastic Transcoder Preset Structure
  property_count: 9
  slug: amazon-elastic-transcoder-preset-structure
- name: Amazon Elastic Transcoder Preset Type Structure
  property_count: 0
  slug: amazon-elastic-transcoder-preset-type-structure
- name: Amazon Elastic Transcoder Preset Watermark Id Structure
  property_count: 0
  slug: amazon-elastic-transcoder-preset-watermark-id-structure
- name: Amazon Elastic Transcoder Preset Watermark Structure
  property_count: 10
  slug: amazon-elastic-transcoder-preset-watermark-structure
- name: Amazon Elastic Transcoder Preset Watermarks Structure
  property_count: 0
  slug: amazon-elastic-transcoder-preset-watermarks-structure
- name: Amazon Elastic Transcoder Presets Structure
  property_count: 0
  slug: amazon-elastic-transcoder-presets-structure
- name: Amazon Elastic Transcoder Read Job Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-read-job-request-structure
- name: Amazon Elastic Transcoder Read Job Response Structure
  property_count: 1
  slug: amazon-elastic-transcoder-read-job-response-structure
- name: Amazon Elastic Transcoder Read Pipeline Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-read-pipeline-request-structure
- name: Amazon Elastic Transcoder Read Pipeline Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-read-pipeline-response-structure
- name: Amazon Elastic Transcoder Read Preset Request Structure
  property_count: 0
  slug: amazon-elastic-transcoder-read-preset-request-structure
- name: Amazon Elastic Transcoder Read Preset Response Structure
  property_count: 1
  slug: amazon-elastic-transcoder-read-preset-response-structure
- name: Amazon Elastic Transcoder Resolution Structure
  property_count: 0
  slug: amazon-elastic-transcoder-resolution-structure
- name: Amazon Elastic Transcoder Resource In Use Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-resource-in-use-exception-structure
- name: Amazon Elastic Transcoder Resource Not Found Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-resource-not-found-exception-structure
- name: Amazon Elastic Transcoder Role Structure
  property_count: 0
  slug: amazon-elastic-transcoder-role-structure
- name: Amazon Elastic Transcoder Rotate Structure
  property_count: 0
  slug: amazon-elastic-transcoder-rotate-structure
- name: Amazon Elastic Transcoder Sizing Policy Structure
  property_count: 0
  slug: amazon-elastic-transcoder-sizing-policy-structure
- name: Amazon Elastic Transcoder Sns Topic Structure
  property_count: 0
  slug: amazon-elastic-transcoder-sns-topic-structure
- name: Amazon Elastic Transcoder Sns Topics Structure
  property_count: 0
  slug: amazon-elastic-transcoder-sns-topics-structure
- name: Amazon Elastic Transcoder Storage Class Structure
  property_count: 0
  slug: amazon-elastic-transcoder-storage-class-structure
- name: Amazon Elastic Transcoder String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-string-structure
- name: Amazon Elastic Transcoder Success Structure
  property_count: 0
  slug: amazon-elastic-transcoder-success-structure
- name: Amazon Elastic Transcoder Target Structure
  property_count: 0
  slug: amazon-elastic-transcoder-target-structure
- name: Amazon Elastic Transcoder Test Role Request Structure
  property_count: 4
  slug: amazon-elastic-transcoder-test-role-request-structure
- name: Amazon Elastic Transcoder Test Role Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-test-role-response-structure
- name: Amazon Elastic Transcoder Thumbnail Pattern Structure
  property_count: 0
  slug: amazon-elastic-transcoder-thumbnail-pattern-structure
- name: Amazon Elastic Transcoder Thumbnail Resolution Structure
  property_count: 0
  slug: amazon-elastic-transcoder-thumbnail-resolution-structure
- name: Amazon Elastic Transcoder Thumbnails Structure
  property_count: 8
  slug: amazon-elastic-transcoder-thumbnails-structure
- name: Amazon Elastic Transcoder Time Offset Structure
  property_count: 0
  slug: amazon-elastic-transcoder-time-offset-structure
- name: Amazon Elastic Transcoder Time Span Structure
  property_count: 2
  slug: amazon-elastic-transcoder-time-span-structure
- name: Amazon Elastic Transcoder Time Structure
  property_count: 0
  slug: amazon-elastic-transcoder-time-structure
- name: Amazon Elastic Transcoder Timing Structure
  property_count: 3
  slug: amazon-elastic-transcoder-timing-structure
- name: Amazon Elastic Transcoder Update Pipeline Notifications Request Structure
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-notifications-request-structure
- name: Amazon Elastic Transcoder Update Pipeline Notifications Response Structure
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-notifications-response-structure
- name: Amazon Elastic Transcoder Update Pipeline Request Structure
  property_count: 7
  slug: amazon-elastic-transcoder-update-pipeline-request-structure
- name: Amazon Elastic Transcoder Update Pipeline Response Structure
  property_count: 2
  slug: amazon-elastic-transcoder-update-pipeline-response-structure
- name: Amazon Elastic Transcoder Update Pipeline Status Request Structure
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-status-request-structure
- name: Amazon Elastic Transcoder Update Pipeline Status Response Structure
  property_count: 1
  slug: amazon-elastic-transcoder-update-pipeline-status-response-structure
- name: Amazon Elastic Transcoder User Metadata Structure
  property_count: 0
  slug: amazon-elastic-transcoder-user-metadata-structure
- name: Amazon Elastic Transcoder Validation Exception Structure
  property_count: 0
  slug: amazon-elastic-transcoder-validation-exception-structure
- name: Amazon Elastic Transcoder Vertical Align Structure
  property_count: 0
  slug: amazon-elastic-transcoder-vertical-align-structure
- name: Amazon Elastic Transcoder Video Bit Rate Structure
  property_count: 0
  slug: amazon-elastic-transcoder-video-bit-rate-structure
- name: Amazon Elastic Transcoder Video Codec Structure
  property_count: 0
  slug: amazon-elastic-transcoder-video-codec-structure
- name: Amazon Elastic Transcoder Video Parameters Structure
  property_count: 15
  slug: amazon-elastic-transcoder-video-parameters-structure
- name: Amazon Elastic Transcoder Warning Structure
  property_count: 2
  slug: amazon-elastic-transcoder-warning-structure
- name: Amazon Elastic Transcoder Warnings Structure
  property_count: 0
  slug: amazon-elastic-transcoder-warnings-structure
- name: Amazon Elastic Transcoder Watermark Key Structure
  property_count: 0
  slug: amazon-elastic-transcoder-watermark-key-structure
- name: Amazon Elastic Transcoder Watermark Sizing Policy Structure
  property_count: 0
  slug: amazon-elastic-transcoder-watermark-sizing-policy-structure
- name: Amazon Elastic Transcoder Zero To255 String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-zero-to255-string-structure
- name: Amazon Elastic Transcoder Zero To512 String Structure
  property_count: 0
  slug: amazon-elastic-transcoder-zero-to512-string-structure
jsonld:
- class_count: 67
  name: Amazon Elastic Transcoder Context
  property_count: 108
  slug: amazon-elastic-transcoder-context
layout: provider
modified: '2026-05-19'
name: Amazon Elastic Transcoder
nav: Providers
network: true
overview: 'Amazon Elastic Transcoder publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Jobs API, JobsByPipeline API, JobsByStatus API, and 3 more. Tagged areas include Amazon Web Services, Media, Transcoding, and Video.


  The Amazon Elastic Transcoder catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Elastic Transcoder''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 27 more developer resources.'
plans:
- name: Amazon Elastic Transcoder Plans Pricing
  plan_count: 3
  slug: amazon-elastic-transcoder-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Amazon Elastic Transcoder Rate Limits
  slug: amazon-elastic-transcoder-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Elastic Transcoder API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-elastic-transcoder-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Elastic Transcoder API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-elastic-transcoder-spectral-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 77.4
    developer_ergonomics: 45.2
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-transcoder/refs/heads/main/screenshots/amazon-elastic-transcoder-2026-06-20T171639.png
security:
- kind: authentication
  name: Amazon Elastic Transcoder Authentication
  slug: amazon-elastic-transcoder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Elastic Transcoder Domain Security
  slug: amazon-elastic-transcoder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Elastic Transcoder Vulnerability Disclosure
  slug: amazon-elastic-transcoder-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Elastic Transcoder Trust Center
  slug: amazon-elastic-transcoder-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-elastic-transcoder
tags:
- Amazon Web Services
- Media
- Transcoding
- Video
use_cases:
- description: Convert video files for streaming across different devices and bandwidths
  name: Video-on-Demand Transcoding
- description: Transcode content optimized for smartphone and tablet playback
  name: Mobile Video Delivery
- description: Create adaptive bitrate HLS streams for seamless playback
  name: HLS Streaming
- description: Convert audio files between different formats and bitrates
  name: Audio File Conversion
website: https://aws.amazon.com/elastictranscoder/
---
