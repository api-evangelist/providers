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
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Amazon Mediapackage Agentic Access
  operation_count: 19
  slug: amazon-mediapackage-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 4
apis:
- description: The Channels API from Amazon MediaPackage — 5 operation(s) for channels.
  name: Amazon MediaPackage Channels API
  slug: amazon-mediapackage-channels-api
- description: The Harvest Jobs API from Amazon MediaPackage — 2 operation(s) for harvest jobs.
  name: Amazon MediaPackage Harvest Jobs API
  slug: amazon-mediapackage-harvest-jobs-api
- description: The Origin Endpoints API from Amazon MediaPackage — 2 operation(s) for origin endpoints.
  name: Amazon MediaPackage Origin Endpoints API
  slug: amazon-mediapackage-origin-endpoints-api
- description: The Tags API from Amazon MediaPackage — 2 operation(s) for tags.
  name: Amazon MediaPackage Tags API
  slug: amazon-mediapackage-tags-api
artifact_total: 256
collections:
- collection_type: postman
  name: AWS Elemental MediaPackage Channels API
  slug: postman-amazon-mediapackage-channels-api
- collection_type: postman
  name: AWS Elemental MediaPackage Channels Harvest Jobs API
  slug: postman-amazon-mediapackage-harvest-jobs-api
- collection_type: postman
  name: AWS Elemental MediaPackage Channels Origin Endpoints API
  slug: postman-amazon-mediapackage-origin-endpoints-api
- collection_type: postman
  name: AWS Elemental MediaPackage Channels Tags API
  slug: postman-amazon-mediapackage-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-mediapackage/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-mediapackage-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-mediapackage-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-mediapackage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-mediapackage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-mediapackage-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/mediapackage/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediapackage/
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
  url: https://aws.amazon.com/blogs/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/mediapackage/
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
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-mediapackage-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediapackage-vocabulary.yaml
created: '2026-03-16'
description: AWS Elemental MediaPackage is a video origination and just-in-time packaging service that reliably prepares and protects video for delivery over the internet, creating multiple output formats from a single video input.
examples:
- key_count: 0
  name: Mediapackage Api Ad Markers Example
  slug: mediapackage-api-ad-markers-example
- key_count: 0
  name: Mediapackage Api Ad Triggers Example
  slug: mediapackage-api-ad-triggers-example
- key_count: 0
  name: Mediapackage Api Ads On Delivery Restrictions Example
  slug: mediapackage-api-ads-on-delivery-restrictions-example
- key_count: 2
  name: Mediapackage Api Authorization Example
  slug: mediapackage-api-authorization-example
- key_count: 8
  name: Mediapackage Api Channel Example
  slug: mediapackage-api-channel-example
- key_count: 4
  name: Mediapackage Api Cmaf Encryption Example
  slug: mediapackage-api-cmaf-encryption-example
- key_count: 0
  name: Mediapackage Api Cmaf Encryption Method Example
  slug: mediapackage-api-cmaf-encryption-method-example
- key_count: 5
  name: Mediapackage Api Cmaf Package Create Or Update Parameters Example
  slug: mediapackage-api-cmaf-package-create-or-update-parameters-example
- key_count: 5
  name: Mediapackage Api Cmaf Package Example
  slug: mediapackage-api-cmaf-package-example
- key_count: 2
  name: Mediapackage Api Configure Logs Request Example
  slug: mediapackage-api-configure-logs-request-example
- key_count: 8
  name: Mediapackage Api Configure Logs Response Example
  slug: mediapackage-api-configure-logs-response-example
- key_count: 3
  name: Mediapackage Api Create Channel Request Example
  slug: mediapackage-api-create-channel-request-example
- key_count: 8
  name: Mediapackage Api Create Channel Response Example
  slug: mediapackage-api-create-channel-response-example
- key_count: 5
  name: Mediapackage Api Create Harvest Job Request Example
  slug: mediapackage-api-create-harvest-job-request-example
- key_count: 9
  name: Mediapackage Api Create Harvest Job Response Example
  slug: mediapackage-api-create-harvest-job-response-example
- key_count: 14
  name: Mediapackage Api Create Origin Endpoint Request Example
  slug: mediapackage-api-create-origin-endpoint-request-example
- key_count: 17
  name: Mediapackage Api Create Origin Endpoint Response Example
  slug: mediapackage-api-create-origin-endpoint-response-example
- key_count: 2
  name: Mediapackage Api Dash Encryption Example
  slug: mediapackage-api-dash-encryption-example
- key_count: 16
  name: Mediapackage Api Dash Package Example
  slug: mediapackage-api-dash-package-example
- key_count: 0
  name: Mediapackage Api Delete Channel Request Example
  slug: mediapackage-api-delete-channel-request-example
- key_count: 0
  name: Mediapackage Api Delete Channel Response Example
  slug: mediapackage-api-delete-channel-response-example
- key_count: 0
  name: Mediapackage Api Delete Origin Endpoint Request Example
  slug: mediapackage-api-delete-origin-endpoint-request-example
- key_count: 0
  name: Mediapackage Api Delete Origin Endpoint Response Example
  slug: mediapackage-api-delete-origin-endpoint-response-example
- key_count: 0
  name: Mediapackage Api Describe Channel Request Example
  slug: mediapackage-api-describe-channel-request-example
- key_count: 8
  name: Mediapackage Api Describe Channel Response Example
  slug: mediapackage-api-describe-channel-response-example
- key_count: 0
  name: Mediapackage Api Describe Harvest Job Request Example
  slug: mediapackage-api-describe-harvest-job-request-example
- key_count: 9
  name: Mediapackage Api Describe Harvest Job Response Example
  slug: mediapackage-api-describe-harvest-job-response-example
- key_count: 0
  name: Mediapackage Api Describe Origin Endpoint Request Example
  slug: mediapackage-api-describe-origin-endpoint-request-example
- key_count: 17
  name: Mediapackage Api Describe Origin Endpoint Response Example
  slug: mediapackage-api-describe-origin-endpoint-response-example
- key_count: 1
  name: Mediapackage Api Egress Access Logs Example
  slug: mediapackage-api-egress-access-logs-example
- key_count: 2
  name: Mediapackage Api Encryption Contract Configuration Example
  slug: mediapackage-api-encryption-contract-configuration-example
- key_count: 0
  name: Mediapackage Api Encryption Method Example
  slug: mediapackage-api-encryption-method-example
- key_count: 9
  name: Mediapackage Api Harvest Job Example
  slug: mediapackage-api-harvest-job-example
- key_count: 5
  name: Mediapackage Api Hls Encryption Example
  slug: mediapackage-api-hls-encryption-example
- key_count: 1
  name: Mediapackage Api Hls Ingest Example
  slug: mediapackage-api-hls-ingest-example
- key_count: 9
  name: Mediapackage Api Hls Manifest Create Or Update Parameters Example
  slug: mediapackage-api-hls-manifest-create-or-update-parameters-example
- key_count: 10
  name: Mediapackage Api Hls Manifest Example
  slug: mediapackage-api-hls-manifest-example
- key_count: 12
  name: Mediapackage Api Hls Package Example
  slug: mediapackage-api-hls-package-example
- key_count: 4
  name: Mediapackage Api Ingest Endpoint Example
  slug: mediapackage-api-ingest-endpoint-example
- key_count: 1
  name: Mediapackage Api Ingress Access Logs Example
  slug: mediapackage-api-ingress-access-logs-example
- key_count: 0
  name: Mediapackage Api List Channels Request Example
  slug: mediapackage-api-list-channels-request-example
- key_count: 2
  name: Mediapackage Api List Channels Response Example
  slug: mediapackage-api-list-channels-response-example
- key_count: 0
  name: Mediapackage Api List Harvest Jobs Request Example
  slug: mediapackage-api-list-harvest-jobs-request-example
- key_count: 2
  name: Mediapackage Api List Harvest Jobs Response Example
  slug: mediapackage-api-list-harvest-jobs-response-example
- key_count: 0
  name: Mediapackage Api List Origin Endpoints Request Example
  slug: mediapackage-api-list-origin-endpoints-request-example
- key_count: 2
  name: Mediapackage Api List Origin Endpoints Response Example
  slug: mediapackage-api-list-origin-endpoints-response-example
- key_count: 0
  name: Mediapackage Api List Tags For Resource Request Example
  slug: mediapackage-api-list-tags-for-resource-request-example
- key_count: 1
  name: Mediapackage Api List Tags For Resource Response Example
  slug: mediapackage-api-list-tags-for-resource-response-example
- key_count: 0
  name: Mediapackage Api Manifest Layout Example
  slug: mediapackage-api-manifest-layout-example
- key_count: 0
  name: Mediapackage Api Max Results Example
  slug: mediapackage-api-max-results-example
- key_count: 1
  name: Mediapackage Api Mss Encryption Example
  slug: mediapackage-api-mss-encryption-example
- key_count: 4
  name: Mediapackage Api Mss Package Example
  slug: mediapackage-api-mss-package-example
- key_count: 17
  name: Mediapackage Api Origin Endpoint Example
  slug: mediapackage-api-origin-endpoint-example
- key_count: 0
  name: Mediapackage Api Origination Example
  slug: mediapackage-api-origination-example
- key_count: 0
  name: Mediapackage Api Playlist Type Example
  slug: mediapackage-api-playlist-type-example
- key_count: 0
  name: Mediapackage Api Preset Speke20 Audio Example
  slug: mediapackage-api-preset-speke20-audio-example
- key_count: 0
  name: Mediapackage Api Preset Speke20 Video Example
  slug: mediapackage-api-preset-speke20-video-example
- key_count: 0
  name: Mediapackage Api Profile Example
  slug: mediapackage-api-profile-example
- key_count: 0
  name: Mediapackage Api Rotate Channel Credentials Request Example
  slug: mediapackage-api-rotate-channel-credentials-request-example
- key_count: 8
  name: Mediapackage Api Rotate Channel Credentials Response Example
  slug: mediapackage-api-rotate-channel-credentials-response-example
- key_count: 0
  name: Mediapackage Api Rotate Ingest Endpoint Credentials Request Example
  slug: mediapackage-api-rotate-ingest-endpoint-credentials-request-example
- key_count: 8
  name: Mediapackage Api Rotate Ingest Endpoint Credentials Response Example
  slug: mediapackage-api-rotate-ingest-endpoint-credentials-response-example
- key_count: 3
  name: Mediapackage Api S3 Destination Example
  slug: mediapackage-api-s3-destination-example
- key_count: 0
  name: Mediapackage Api Segment Template Format Example
  slug: mediapackage-api-segment-template-format-example
- key_count: 6
  name: Mediapackage Api Speke Key Provider Example
  slug: mediapackage-api-speke-key-provider-example
- key_count: 0
  name: Mediapackage Api Status Example
  slug: mediapackage-api-status-example
- key_count: 0
  name: Mediapackage Api Stream Order Example
  slug: mediapackage-api-stream-order-example
- key_count: 3
  name: Mediapackage Api Stream Selection Example
  slug: mediapackage-api-stream-selection-example
- key_count: 1
  name: Mediapackage Api Tag Resource Request Example
  slug: mediapackage-api-tag-resource-request-example
- key_count: 0
  name: Mediapackage Api Tags Example
  slug: mediapackage-api-tags-example
- key_count: 0
  name: Mediapackage Api Untag Resource Request Example
  slug: mediapackage-api-untag-resource-request-example
- key_count: 1
  name: Mediapackage Api Update Channel Request Example
  slug: mediapackage-api-update-channel-request-example
- key_count: 8
  name: Mediapackage Api Update Channel Response Example
  slug: mediapackage-api-update-channel-response-example
- key_count: 11
  name: Mediapackage Api Update Origin Endpoint Request Example
  slug: mediapackage-api-update-origin-endpoint-request-example
- key_count: 17
  name: Mediapackage Api Update Origin Endpoint Response Example
  slug: mediapackage-api-update-origin-endpoint-response-example
- key_count: 0
  name: Mediapackage Api Utc Timing Example
  slug: mediapackage-api-utc-timing-example
features:
- description: Package live video into HLS, DASH, CMAF, and Microsoft Smooth Streaming formats on demand.
  name: Just-in-Time Packaging
- description: Integrated DRM support with PlayReady, Widevine, FairPlay, and SPEKE standard.
  name: Content Protection
- description: Enable start-over, catch-up TV, and pause live TV with configurable time windows.
  name: Time-Shifted Viewing
- description: Direct integration with CloudFront for scalable content delivery.
  name: CDN Integration
- description: Clip and archive live stream segments to S3 for VOD asset creation.
  name: Harvest Jobs
finops:
- name: Amazon Mediapackage Finops
  service_category: API
  slug: amazon-mediapackage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-mediapackage.png
json_schemas:
- name: AdMarkers
  property_count: 0
  slug: mediapackage-api-ad-markers
- name: AdTriggers
  property_count: 0
  slug: mediapackage-api-ad-triggers
- name: AdsOnDeliveryRestrictions
  property_count: 0
  slug: mediapackage-api-ads-on-delivery-restrictions
- name: Authorization
  property_count: 2
  slug: mediapackage-api-authorization
- name: Channel
  property_count: 8
  slug: mediapackage-api-channel
- name: CmafEncryptionMethod
  property_count: 0
  slug: mediapackage-api-cmaf-encryption-method
- name: CmafEncryption
  property_count: 4
  slug: mediapackage-api-cmaf-encryption
- name: CmafPackageCreateOrUpdateParameters
  property_count: 5
  slug: mediapackage-api-cmaf-package-create-or-update-parameters
- name: CmafPackage
  property_count: 5
  slug: mediapackage-api-cmaf-package
- name: ConfigureLogsRequest
  property_count: 2
  slug: mediapackage-api-configure-logs-request
- name: ConfigureLogsResponse
  property_count: 8
  slug: mediapackage-api-configure-logs-response
- name: CreateChannelRequest
  property_count: 3
  slug: mediapackage-api-create-channel-request
- name: CreateChannelResponse
  property_count: 8
  slug: mediapackage-api-create-channel-response
- name: CreateHarvestJobRequest
  property_count: 5
  slug: mediapackage-api-create-harvest-job-request
- name: CreateHarvestJobResponse
  property_count: 9
  slug: mediapackage-api-create-harvest-job-response
- name: CreateOriginEndpointRequest
  property_count: 14
  slug: mediapackage-api-create-origin-endpoint-request
- name: CreateOriginEndpointResponse
  property_count: 17
  slug: mediapackage-api-create-origin-endpoint-response
- name: DashEncryption
  property_count: 2
  slug: mediapackage-api-dash-encryption
- name: DashPackage
  property_count: 16
  slug: mediapackage-api-dash-package
- name: DeleteChannelRequest
  property_count: 0
  slug: mediapackage-api-delete-channel-request
- name: DeleteChannelResponse
  property_count: 0
  slug: mediapackage-api-delete-channel-response
- name: DeleteOriginEndpointRequest
  property_count: 0
  slug: mediapackage-api-delete-origin-endpoint-request
- name: DeleteOriginEndpointResponse
  property_count: 0
  slug: mediapackage-api-delete-origin-endpoint-response
- name: DescribeChannelRequest
  property_count: 0
  slug: mediapackage-api-describe-channel-request
- name: DescribeChannelResponse
  property_count: 8
  slug: mediapackage-api-describe-channel-response
- name: DescribeHarvestJobRequest
  property_count: 0
  slug: mediapackage-api-describe-harvest-job-request
- name: DescribeHarvestJobResponse
  property_count: 9
  slug: mediapackage-api-describe-harvest-job-response
- name: DescribeOriginEndpointRequest
  property_count: 0
  slug: mediapackage-api-describe-origin-endpoint-request
- name: DescribeOriginEndpointResponse
  property_count: 17
  slug: mediapackage-api-describe-origin-endpoint-response
- name: EgressAccessLogs
  property_count: 1
  slug: mediapackage-api-egress-access-logs
- name: EncryptionContractConfiguration
  property_count: 2
  slug: mediapackage-api-encryption-contract-configuration
- name: EncryptionMethod
  property_count: 0
  slug: mediapackage-api-encryption-method
- name: HarvestJob
  property_count: 9
  slug: mediapackage-api-harvest-job
- name: HlsEncryption
  property_count: 5
  slug: mediapackage-api-hls-encryption
- name: HlsIngest
  property_count: 1
  slug: mediapackage-api-hls-ingest
- name: HlsManifestCreateOrUpdateParameters
  property_count: 9
  slug: mediapackage-api-hls-manifest-create-or-update-parameters
- name: HlsManifest
  property_count: 10
  slug: mediapackage-api-hls-manifest
- name: HlsPackage
  property_count: 12
  slug: mediapackage-api-hls-package
- name: IngestEndpoint
  property_count: 4
  slug: mediapackage-api-ingest-endpoint
- name: IngressAccessLogs
  property_count: 1
  slug: mediapackage-api-ingress-access-logs
- name: ListChannelsRequest
  property_count: 0
  slug: mediapackage-api-list-channels-request
- name: ListChannelsResponse
  property_count: 2
  slug: mediapackage-api-list-channels-response
- name: ListHarvestJobsRequest
  property_count: 0
  slug: mediapackage-api-list-harvest-jobs-request
- name: ListHarvestJobsResponse
  property_count: 2
  slug: mediapackage-api-list-harvest-jobs-response
- name: ListOriginEndpointsRequest
  property_count: 0
  slug: mediapackage-api-list-origin-endpoints-request
- name: ListOriginEndpointsResponse
  property_count: 2
  slug: mediapackage-api-list-origin-endpoints-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: mediapackage-api-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: mediapackage-api-list-tags-for-resource-response
- name: ManifestLayout
  property_count: 0
  slug: mediapackage-api-manifest-layout
- name: MaxResults
  property_count: 0
  slug: mediapackage-api-max-results
- name: MssEncryption
  property_count: 1
  slug: mediapackage-api-mss-encryption
- name: MssPackage
  property_count: 4
  slug: mediapackage-api-mss-package
- name: OriginEndpoint
  property_count: 17
  slug: mediapackage-api-origin-endpoint
- name: Origination
  property_count: 0
  slug: mediapackage-api-origination
- name: PlaylistType
  property_count: 0
  slug: mediapackage-api-playlist-type
- name: PresetSpeke20Audio
  property_count: 0
  slug: mediapackage-api-preset-speke20-audio
- name: PresetSpeke20Video
  property_count: 0
  slug: mediapackage-api-preset-speke20-video
- name: Profile
  property_count: 0
  slug: mediapackage-api-profile
- name: RotateChannelCredentialsRequest
  property_count: 0
  slug: mediapackage-api-rotate-channel-credentials-request
- name: RotateChannelCredentialsResponse
  property_count: 8
  slug: mediapackage-api-rotate-channel-credentials-response
- name: RotateIngestEndpointCredentialsRequest
  property_count: 0
  slug: mediapackage-api-rotate-ingest-endpoint-credentials-request
- name: RotateIngestEndpointCredentialsResponse
  property_count: 8
  slug: mediapackage-api-rotate-ingest-endpoint-credentials-response
- name: S3Destination
  property_count: 3
  slug: mediapackage-api-s3-destination
- name: SegmentTemplateFormat
  property_count: 0
  slug: mediapackage-api-segment-template-format
- name: SpekeKeyProvider
  property_count: 6
  slug: mediapackage-api-speke-key-provider
- name: Status
  property_count: 0
  slug: mediapackage-api-status
- name: StreamOrder
  property_count: 0
  slug: mediapackage-api-stream-order
- name: StreamSelection
  property_count: 3
  slug: mediapackage-api-stream-selection
- name: TagResourceRequest
  property_count: 1
  slug: mediapackage-api-tag-resource-request
- name: Tags
  property_count: 0
  slug: mediapackage-api-tags
- name: UntagResourceRequest
  property_count: 0
  slug: mediapackage-api-untag-resource-request
- name: UpdateChannelRequest
  property_count: 1
  slug: mediapackage-api-update-channel-request
- name: UpdateChannelResponse
  property_count: 8
  slug: mediapackage-api-update-channel-response
- name: UpdateOriginEndpointRequest
  property_count: 11
  slug: mediapackage-api-update-origin-endpoint-request
- name: UpdateOriginEndpointResponse
  property_count: 17
  slug: mediapackage-api-update-origin-endpoint-response
- name: UtcTiming
  property_count: 0
  slug: mediapackage-api-utc-timing
json_structures:
- name: Mediapackage Api Ad Markers Structure
  property_count: 0
  slug: mediapackage-api-ad-markers-structure
- name: Mediapackage Api Ad Triggers Structure
  property_count: 0
  slug: mediapackage-api-ad-triggers-structure
- name: Mediapackage Api Ads On Delivery Restrictions Structure
  property_count: 0
  slug: mediapackage-api-ads-on-delivery-restrictions-structure
- name: Mediapackage Api Authorization Structure
  property_count: 2
  slug: mediapackage-api-authorization-structure
- name: Mediapackage Api Channel Structure
  property_count: 8
  slug: mediapackage-api-channel-structure
- name: Mediapackage Api Cmaf Encryption Method Structure
  property_count: 0
  slug: mediapackage-api-cmaf-encryption-method-structure
- name: Mediapackage Api Cmaf Encryption Structure
  property_count: 4
  slug: mediapackage-api-cmaf-encryption-structure
- name: Mediapackage Api Cmaf Package Create Or Update Parameters Structure
  property_count: 5
  slug: mediapackage-api-cmaf-package-create-or-update-parameters-structure
- name: Mediapackage Api Cmaf Package Structure
  property_count: 5
  slug: mediapackage-api-cmaf-package-structure
- name: Mediapackage Api Configure Logs Request Structure
  property_count: 2
  slug: mediapackage-api-configure-logs-request-structure
- name: Mediapackage Api Configure Logs Response Structure
  property_count: 8
  slug: mediapackage-api-configure-logs-response-structure
- name: Mediapackage Api Create Channel Request Structure
  property_count: 3
  slug: mediapackage-api-create-channel-request-structure
- name: Mediapackage Api Create Channel Response Structure
  property_count: 8
  slug: mediapackage-api-create-channel-response-structure
- name: Mediapackage Api Create Harvest Job Request Structure
  property_count: 5
  slug: mediapackage-api-create-harvest-job-request-structure
- name: Mediapackage Api Create Harvest Job Response Structure
  property_count: 9
  slug: mediapackage-api-create-harvest-job-response-structure
- name: Mediapackage Api Create Origin Endpoint Request Structure
  property_count: 14
  slug: mediapackage-api-create-origin-endpoint-request-structure
- name: Mediapackage Api Create Origin Endpoint Response Structure
  property_count: 17
  slug: mediapackage-api-create-origin-endpoint-response-structure
- name: Mediapackage Api Dash Encryption Structure
  property_count: 2
  slug: mediapackage-api-dash-encryption-structure
- name: Mediapackage Api Dash Package Structure
  property_count: 16
  slug: mediapackage-api-dash-package-structure
- name: Mediapackage Api Delete Channel Request Structure
  property_count: 0
  slug: mediapackage-api-delete-channel-request-structure
- name: Mediapackage Api Delete Channel Response Structure
  property_count: 0
  slug: mediapackage-api-delete-channel-response-structure
- name: Mediapackage Api Delete Origin Endpoint Request Structure
  property_count: 0
  slug: mediapackage-api-delete-origin-endpoint-request-structure
- name: Mediapackage Api Delete Origin Endpoint Response Structure
  property_count: 0
  slug: mediapackage-api-delete-origin-endpoint-response-structure
- name: Mediapackage Api Describe Channel Request Structure
  property_count: 0
  slug: mediapackage-api-describe-channel-request-structure
- name: Mediapackage Api Describe Channel Response Structure
  property_count: 8
  slug: mediapackage-api-describe-channel-response-structure
- name: Mediapackage Api Describe Harvest Job Request Structure
  property_count: 0
  slug: mediapackage-api-describe-harvest-job-request-structure
- name: Mediapackage Api Describe Harvest Job Response Structure
  property_count: 9
  slug: mediapackage-api-describe-harvest-job-response-structure
- name: Mediapackage Api Describe Origin Endpoint Request Structure
  property_count: 0
  slug: mediapackage-api-describe-origin-endpoint-request-structure
- name: Mediapackage Api Describe Origin Endpoint Response Structure
  property_count: 17
  slug: mediapackage-api-describe-origin-endpoint-response-structure
- name: Mediapackage Api Egress Access Logs Structure
  property_count: 1
  slug: mediapackage-api-egress-access-logs-structure
- name: Mediapackage Api Encryption Contract Configuration Structure
  property_count: 2
  slug: mediapackage-api-encryption-contract-configuration-structure
- name: Mediapackage Api Encryption Method Structure
  property_count: 0
  slug: mediapackage-api-encryption-method-structure
- name: Mediapackage Api Harvest Job Structure
  property_count: 9
  slug: mediapackage-api-harvest-job-structure
- name: Mediapackage Api Hls Encryption Structure
  property_count: 5
  slug: mediapackage-api-hls-encryption-structure
- name: Mediapackage Api Hls Ingest Structure
  property_count: 1
  slug: mediapackage-api-hls-ingest-structure
- name: Mediapackage Api Hls Manifest Create Or Update Parameters Structure
  property_count: 9
  slug: mediapackage-api-hls-manifest-create-or-update-parameters-structure
- name: Mediapackage Api Hls Manifest Structure
  property_count: 10
  slug: mediapackage-api-hls-manifest-structure
- name: Mediapackage Api Hls Package Structure
  property_count: 12
  slug: mediapackage-api-hls-package-structure
- name: Mediapackage Api Ingest Endpoint Structure
  property_count: 4
  slug: mediapackage-api-ingest-endpoint-structure
- name: Mediapackage Api Ingress Access Logs Structure
  property_count: 1
  slug: mediapackage-api-ingress-access-logs-structure
- name: Mediapackage Api List Channels Request Structure
  property_count: 0
  slug: mediapackage-api-list-channels-request-structure
- name: Mediapackage Api List Channels Response Structure
  property_count: 2
  slug: mediapackage-api-list-channels-response-structure
- name: Mediapackage Api List Harvest Jobs Request Structure
  property_count: 0
  slug: mediapackage-api-list-harvest-jobs-request-structure
- name: Mediapackage Api List Harvest Jobs Response Structure
  property_count: 2
  slug: mediapackage-api-list-harvest-jobs-response-structure
- name: Mediapackage Api List Origin Endpoints Request Structure
  property_count: 0
  slug: mediapackage-api-list-origin-endpoints-request-structure
- name: Mediapackage Api List Origin Endpoints Response Structure
  property_count: 2
  slug: mediapackage-api-list-origin-endpoints-response-structure
- name: Mediapackage Api List Tags For Resource Request Structure
  property_count: 0
  slug: mediapackage-api-list-tags-for-resource-request-structure
- name: Mediapackage Api List Tags For Resource Response Structure
  property_count: 1
  slug: mediapackage-api-list-tags-for-resource-response-structure
- name: Mediapackage Api Manifest Layout Structure
  property_count: 0
  slug: mediapackage-api-manifest-layout-structure
- name: Mediapackage Api Max Results Structure
  property_count: 0
  slug: mediapackage-api-max-results-structure
- name: Mediapackage Api Mss Encryption Structure
  property_count: 1
  slug: mediapackage-api-mss-encryption-structure
- name: Mediapackage Api Mss Package Structure
  property_count: 4
  slug: mediapackage-api-mss-package-structure
- name: Mediapackage Api Origin Endpoint Structure
  property_count: 17
  slug: mediapackage-api-origin-endpoint-structure
- name: Mediapackage Api Origination Structure
  property_count: 0
  slug: mediapackage-api-origination-structure
- name: Mediapackage Api Playlist Type Structure
  property_count: 0
  slug: mediapackage-api-playlist-type-structure
- name: Mediapackage Api Preset Speke20 Audio Structure
  property_count: 0
  slug: mediapackage-api-preset-speke20-audio-structure
- name: Mediapackage Api Preset Speke20 Video Structure
  property_count: 0
  slug: mediapackage-api-preset-speke20-video-structure
- name: Mediapackage Api Profile Structure
  property_count: 0
  slug: mediapackage-api-profile-structure
- name: Mediapackage Api Rotate Channel Credentials Request Structure
  property_count: 0
  slug: mediapackage-api-rotate-channel-credentials-request-structure
- name: Mediapackage Api Rotate Channel Credentials Response Structure
  property_count: 8
  slug: mediapackage-api-rotate-channel-credentials-response-structure
- name: Mediapackage Api Rotate Ingest Endpoint Credentials Request Structure
  property_count: 0
  slug: mediapackage-api-rotate-ingest-endpoint-credentials-request-structure
- name: Mediapackage Api Rotate Ingest Endpoint Credentials Response Structure
  property_count: 8
  slug: mediapackage-api-rotate-ingest-endpoint-credentials-response-structure
- name: Mediapackage Api S3 Destination Structure
  property_count: 3
  slug: mediapackage-api-s3-destination-structure
- name: Mediapackage Api Segment Template Format Structure
  property_count: 0
  slug: mediapackage-api-segment-template-format-structure
- name: Mediapackage Api Speke Key Provider Structure
  property_count: 6
  slug: mediapackage-api-speke-key-provider-structure
- name: Mediapackage Api Status Structure
  property_count: 0
  slug: mediapackage-api-status-structure
- name: Mediapackage Api Stream Order Structure
  property_count: 0
  slug: mediapackage-api-stream-order-structure
- name: Mediapackage Api Stream Selection Structure
  property_count: 3
  slug: mediapackage-api-stream-selection-structure
- name: Mediapackage Api Tag Resource Request Structure
  property_count: 1
  slug: mediapackage-api-tag-resource-request-structure
- name: Mediapackage Api Tags Structure
  property_count: 0
  slug: mediapackage-api-tags-structure
- name: Mediapackage Api Untag Resource Request Structure
  property_count: 0
  slug: mediapackage-api-untag-resource-request-structure
- name: Mediapackage Api Update Channel Request Structure
  property_count: 1
  slug: mediapackage-api-update-channel-request-structure
- name: Mediapackage Api Update Channel Response Structure
  property_count: 8
  slug: mediapackage-api-update-channel-response-structure
- name: Mediapackage Api Update Origin Endpoint Request Structure
  property_count: 11
  slug: mediapackage-api-update-origin-endpoint-request-structure
- name: Mediapackage Api Update Origin Endpoint Response Structure
  property_count: 17
  slug: mediapackage-api-update-origin-endpoint-response-structure
- name: Mediapackage Api Utc Timing Structure
  property_count: 0
  slug: mediapackage-api-utc-timing-structure
jsonld:
- class_count: 79
  name: Amazon Mediapackage Mediapackage Api Context
  property_count: 73
  slug: amazon-mediapackage-mediapackage-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MediaPackage
nav: Providers
network: true
overview: 'Amazon MediaPackage publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Harvest Jobs API, Origin Endpoints API, and 1 more. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MediaPackage catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MediaPackage''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Mediapackage Plans Pricing
  plan_count: 3
  slug: amazon-mediapackage-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 5
  name: Amazon Mediapackage Rate Limits
  slug: amazon-mediapackage-rate-limits
rules:
- name: Amazon MediaPackage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-mediapackage-jsonschema-spectral-rules
- name: Amazon MediaPackage API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 13
  slug: amazon-mediapackage-spectral-rules
score:
  band: strong
  composite: 61.8
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 69.6
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-mediapackage/refs/heads/main/screenshots/amazon-mediapackage-2026-06-20T171746.png
security:
- kind: authentication
  name: Amazon Mediapackage Authentication
  slug: amazon-mediapackage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Mediapackage Domain Security
  slug: amazon-mediapackage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Mediapackage Vulnerability Disclosure
  slug: amazon-mediapackage-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Mediapackage Trust Center
  slug: amazon-mediapackage-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-mediapackage
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Package live video for over-the-top delivery to mobile and connected devices.
  name: Live OTT Streaming
- description: Enable catch-up TV and start-over viewing experiences.
  name: Time-Shifted Television
- description: Protect premium content with multiple DRM systems simultaneously.
  name: Multi-DRM Content Protection
- description: Create VOD clips from live streams for highlights and replays.
  name: Live Clipping
website: https://aws.amazon.com/mediapackage/
---
