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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 18
  human_in_the_loop: 3
  name: Amazon Mediaconvert Agentic Access
  operation_count: 28
  slug: amazon-mediaconvert-agentic-access
  summary_line: 28 operations · 18 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Certificates API from Amazon MediaConvert — 2 operation(s) for certificates.
  name: Amazon MediaConvert Certificates API
  slug: amazon-mediaconvert-certificates-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Endpoints API from Amazon MediaConvert — 1 operation(s) for endpoints.
  name: Amazon MediaConvert Endpoints API
  slug: amazon-mediaconvert-endpoints-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Jobs API from Amazon MediaConvert — 2 operation(s) for jobs.
  name: Amazon MediaConvert Jobs API
  slug: amazon-mediaconvert-jobs-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The JobTemplates API from Amazon MediaConvert — 2 operation(s) for jobtemplates.
  name: Amazon MediaConvert JobTemplates API
  slug: amazon-mediaconvert-jobtemplates-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Policy API from Amazon MediaConvert — 1 operation(s) for policy.
  name: Amazon MediaConvert Policy API
  slug: amazon-mediaconvert-policy-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Presets API from Amazon MediaConvert — 2 operation(s) for presets.
  name: Amazon MediaConvert Presets API
  slug: amazon-mediaconvert-presets-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Queues API from Amazon MediaConvert — 2 operation(s) for queues.
  name: Amazon MediaConvert Queues API
  slug: amazon-mediaconvert-queues-api
- baseURL: http://mediaconvert.{region}.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon MediaConvert — 2 operation(s) for tags.
  name: Amazon MediaConvert Tags API
  slug: amazon-mediaconvert-tags-api
artifact_total: 1945
collections:
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates API
  slug: postman-amazon-mediaconvert-certificates-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates Endpoints API
  slug: postman-amazon-mediaconvert-endpoints-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates Jobs API
  slug: postman-amazon-mediaconvert-jobs-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates JobTemplates API
  slug: postman-amazon-mediaconvert-jobtemplates-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates Policy API
  slug: postman-amazon-mediaconvert-policy-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates Presets API
  slug: postman-amazon-mediaconvert-presets-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates Queues API
  slug: postman-amazon-mediaconvert-queues-api
- collection_type: postman
  name: AWS Elemental MediaConvert Certificates Tags API
  slug: postman-amazon-mediaconvert-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Elemental MediaConvert Certificates API
  slug: open-amazon-mediaconvert-certificates-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates Endpoints API
  slug: open-amazon-mediaconvert-endpoints-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates Jobs API
  slug: open-amazon-mediaconvert-jobs-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates JobTemplates API
  slug: open-amazon-mediaconvert-jobtemplates-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates Policy API
  slug: open-amazon-mediaconvert-policy-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates Presets API
  slug: open-amazon-mediaconvert-presets-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates Queues API
  slug: open-amazon-mediaconvert-queues-api
- collection_type: open
  name: AWS Elemental MediaConvert Certificates Tags API
  slug: open-amazon-mediaconvert-tags-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-mediaconvert-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-mediaconvert/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-mediaconvert-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-mediaconvert-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-mediaconvert-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-mediaconvert-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-mediaconvert-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/mediaconvert/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediaconvert/
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
  url: https://console.aws.amazon.com/mediaconvert/
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
  url: rules/amazon-mediaconvert-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediaconvert-vocabulary.yaml
created: '2026-03-16'
description: AWS Elemental MediaConvert is a file-based video transcoding service that allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. It supports broadcast-grade features including graphic overlays, content protection, multi-language audio, closed captioning, and a comprehensive range of video formats.
examples:
- key_count: 0
  name: Mediaconvert Api Aac Audio Description Broadcaster Mix Example
  slug: mediaconvert-api-aac-audio-description-broadcaster-mix-example
- key_count: 0
  name: Mediaconvert Api Aac Codec Profile Example
  slug: mediaconvert-api-aac-codec-profile-example
- key_count: 0
  name: Mediaconvert Api Aac Coding Mode Example
  slug: mediaconvert-api-aac-coding-mode-example
- key_count: 0
  name: Mediaconvert Api Aac Rate Control Mode Example
  slug: mediaconvert-api-aac-rate-control-mode-example
- key_count: 0
  name: Mediaconvert Api Aac Raw Format Example
  slug: mediaconvert-api-aac-raw-format-example
- key_count: 9
  name: Mediaconvert Api Aac Settings Example
  slug: mediaconvert-api-aac-settings-example
- key_count: 0
  name: Mediaconvert Api Aac Specification Example
  slug: mediaconvert-api-aac-specification-example
- key_count: 0
  name: Mediaconvert Api Aac Vbr Quality Example
  slug: mediaconvert-api-aac-vbr-quality-example
- key_count: 0
  name: Mediaconvert Api Ac3 Bitstream Mode Example
  slug: mediaconvert-api-ac3-bitstream-mode-example
- key_count: 0
  name: Mediaconvert Api Ac3 Coding Mode Example
  slug: mediaconvert-api-ac3-coding-mode-example
- key_count: 0
  name: Mediaconvert Api Ac3 Dynamic Range Compression Line Example
  slug: mediaconvert-api-ac3-dynamic-range-compression-line-example
- key_count: 0
  name: Mediaconvert Api Ac3 Dynamic Range Compression Profile Example
  slug: mediaconvert-api-ac3-dynamic-range-compression-profile-example
- key_count: 0
  name: Mediaconvert Api Ac3 Dynamic Range Compression Rf Example
  slug: mediaconvert-api-ac3-dynamic-range-compression-rf-example
- key_count: 0
  name: Mediaconvert Api Ac3 Lfe Filter Example
  slug: mediaconvert-api-ac3-lfe-filter-example
- key_count: 0
  name: Mediaconvert Api Ac3 Metadata Control Example
  slug: mediaconvert-api-ac3-metadata-control-example
- key_count: 10
  name: Mediaconvert Api Ac3 Settings Example
  slug: mediaconvert-api-ac3-settings-example
- key_count: 0
  name: Mediaconvert Api Acceleration Mode Example
  slug: mediaconvert-api-acceleration-mode-example
- key_count: 1
  name: Mediaconvert Api Acceleration Settings Example
  slug: mediaconvert-api-acceleration-settings-example
- key_count: 0
  name: Mediaconvert Api Acceleration Status Example
  slug: mediaconvert-api-acceleration-status-example
- key_count: 0
  name: Mediaconvert Api Afd Signaling Example
  slug: mediaconvert-api-afd-signaling-example
- key_count: 3
  name: Mediaconvert Api Aiff Settings Example
  slug: mediaconvert-api-aiff-settings-example
- key_count: 3
  name: Mediaconvert Api Allowed Rendition Size Example
  slug: mediaconvert-api-allowed-rendition-size-example
- key_count: 0
  name: Mediaconvert Api Alpha Behavior Example
  slug: mediaconvert-api-alpha-behavior-example
- key_count: 0
  name: Mediaconvert Api Ancillary Convert608 To708 Example
  slug: mediaconvert-api-ancillary-convert608-to708-example
- key_count: 3
  name: Mediaconvert Api Ancillary Source Settings Example
  slug: mediaconvert-api-ancillary-source-settings-example
- key_count: 0
  name: Mediaconvert Api Ancillary Terminate Captions Example
  slug: mediaconvert-api-ancillary-terminate-captions-example
- key_count: 0
  name: Mediaconvert Api Anti Alias Example
  slug: mediaconvert-api-anti-alias-example
- key_count: 1
  name: Mediaconvert Api Associate Certificate Request Example
  slug: mediaconvert-api-associate-certificate-request-example
- key_count: 0
  name: Mediaconvert Api Associate Certificate Response Example
  slug: mediaconvert-api-associate-certificate-response-example
- key_count: 0
  name: Mediaconvert Api Audio Channel Tag Example
  slug: mediaconvert-api-audio-channel-tag-example
- key_count: 1
  name: Mediaconvert Api Audio Channel Tagging Settings Example
  slug: mediaconvert-api-audio-channel-tagging-settings-example
- key_count: 0
  name: Mediaconvert Api Audio Codec Example
  slug: mediaconvert-api-audio-codec-example
- key_count: 11
  name: Mediaconvert Api Audio Codec Settings Example
  slug: mediaconvert-api-audio-codec-settings-example
- key_count: 0
  name: Mediaconvert Api Audio Default Selection Example
  slug: mediaconvert-api-audio-default-selection-example
- key_count: 11
  name: Mediaconvert Api Audio Description Example
  slug: mediaconvert-api-audio-description-example
- key_count: 0
  name: Mediaconvert Api Audio Duration Correction Example
  slug: mediaconvert-api-audio-duration-correction-example
- key_count: 0
  name: Mediaconvert Api Audio Language Code Control Example
  slug: mediaconvert-api-audio-language-code-control-example
- key_count: 0
  name: Mediaconvert Api Audio Normalization Algorithm Control Example
  slug: mediaconvert-api-audio-normalization-algorithm-control-example
- key_count: 0
  name: Mediaconvert Api Audio Normalization Algorithm Example
  slug: mediaconvert-api-audio-normalization-algorithm-example
- key_count: 0
  name: Mediaconvert Api Audio Normalization Loudness Logging Example
  slug: mediaconvert-api-audio-normalization-loudness-logging-example
- key_count: 0
  name: Mediaconvert Api Audio Normalization Peak Calculation Example
  slug: mediaconvert-api-audio-normalization-peak-calculation-example
- key_count: 7
  name: Mediaconvert Api Audio Normalization Settings Example
  slug: mediaconvert-api-audio-normalization-settings-example
- key_count: 12
  name: Mediaconvert Api Audio Selector Example
  slug: mediaconvert-api-audio-selector-example
- key_count: 1
  name: Mediaconvert Api Audio Selector Group Example
  slug: mediaconvert-api-audio-selector-group-example
- key_count: 0
  name: Mediaconvert Api Audio Selector Type Example
  slug: mediaconvert-api-audio-selector-type-example
- key_count: 0
  name: Mediaconvert Api Audio Type Control Example
  slug: mediaconvert-api-audio-type-control-example
- key_count: 5
  name: Mediaconvert Api Automated Abr Rule Example
  slug: mediaconvert-api-automated-abr-rule-example
- key_count: 4
  name: Mediaconvert Api Automated Abr Settings Example
  slug: mediaconvert-api-automated-abr-settings-example
- key_count: 1
  name: Mediaconvert Api Automated Encoding Settings Example
  slug: mediaconvert-api-automated-encoding-settings-example
- key_count: 0
  name: Mediaconvert Api Av1 Adaptive Quantization Example
  slug: mediaconvert-api-av1-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Av1 Bit Depth Example
  slug: mediaconvert-api-av1-bit-depth-example
- key_count: 0
  name: Mediaconvert Api Av1 Framerate Control Example
  slug: mediaconvert-api-av1-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Av1 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-av1-framerate-conversion-algorithm-example
- key_count: 2
  name: Mediaconvert Api Av1 Qvbr Settings Example
  slug: mediaconvert-api-av1-qvbr-settings-example
- key_count: 0
  name: Mediaconvert Api Av1 Rate Control Mode Example
  slug: mediaconvert-api-av1-rate-control-mode-example
- key_count: 13
  name: Mediaconvert Api Av1 Settings Example
  slug: mediaconvert-api-av1-settings-example
- key_count: 0
  name: Mediaconvert Api Av1 Spatial Adaptive Quantization Example
  slug: mediaconvert-api-av1-spatial-adaptive-quantization-example
- key_count: 1
  name: Mediaconvert Api Avail Blanking Example
  slug: mediaconvert-api-avail-blanking-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Class Example
  slug: mediaconvert-api-avc-intra-class-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Framerate Control Example
  slug: mediaconvert-api-avc-intra-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Framerate Conversion Algorithm Example
  slug: mediaconvert-api-avc-intra-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Interlace Mode Example
  slug: mediaconvert-api-avc-intra-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Scan Type Conversion Mode Example
  slug: mediaconvert-api-avc-intra-scan-type-conversion-mode-example
- key_count: 10
  name: Mediaconvert Api Avc Intra Settings Example
  slug: mediaconvert-api-avc-intra-settings-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Slow Pal Example
  slug: mediaconvert-api-avc-intra-slow-pal-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Telecine Example
  slug: mediaconvert-api-avc-intra-telecine-example
- key_count: 0
  name: Mediaconvert Api Avc Intra Uhd Quality Tuning Level Example
  slug: mediaconvert-api-avc-intra-uhd-quality-tuning-level-example
- key_count: 1
  name: Mediaconvert Api Avc Intra Uhd Settings Example
  slug: mediaconvert-api-avc-intra-uhd-settings-example
- key_count: 2
  name: Mediaconvert Api Bandwidth Reduction Filter Example
  slug: mediaconvert-api-bandwidth-reduction-filter-example
- key_count: 0
  name: Mediaconvert Api Bandwidth Reduction Filter Sharpening Example
  slug: mediaconvert-api-bandwidth-reduction-filter-sharpening-example
- key_count: 0
  name: Mediaconvert Api Bandwidth Reduction Filter Strength Example
  slug: mediaconvert-api-bandwidth-reduction-filter-strength-example
- key_count: 0
  name: Mediaconvert Api Billing Tags Source Example
  slug: mediaconvert-api-billing-tags-source-example
- key_count: 0
  name: Mediaconvert Api Burn In Subtitle Style Passthrough Example
  slug: mediaconvert-api-burn-in-subtitle-style-passthrough-example
- key_count: 21
  name: Mediaconvert Api Burnin Destination Settings Example
  slug: mediaconvert-api-burnin-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Alignment Example
  slug: mediaconvert-api-burnin-subtitle-alignment-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Apply Font Color Example
  slug: mediaconvert-api-burnin-subtitle-apply-font-color-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Background Color Example
  slug: mediaconvert-api-burnin-subtitle-background-color-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Fallback Font Example
  slug: mediaconvert-api-burnin-subtitle-fallback-font-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Font Color Example
  slug: mediaconvert-api-burnin-subtitle-font-color-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Outline Color Example
  slug: mediaconvert-api-burnin-subtitle-outline-color-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Shadow Color Example
  slug: mediaconvert-api-burnin-subtitle-shadow-color-example
- key_count: 0
  name: Mediaconvert Api Burnin Subtitle Teletext Spacing Example
  slug: mediaconvert-api-burnin-subtitle-teletext-spacing-example
- key_count: 0
  name: Mediaconvert Api Cancel Job Request Example
  slug: mediaconvert-api-cancel-job-request-example
- key_count: 0
  name: Mediaconvert Api Cancel Job Response Example
  slug: mediaconvert-api-cancel-job-response-example
- key_count: 5
  name: Mediaconvert Api Caption Description Example
  slug: mediaconvert-api-caption-description-example
- key_count: 4
  name: Mediaconvert Api Caption Description Preset Example
  slug: mediaconvert-api-caption-description-preset-example
- key_count: 10
  name: Mediaconvert Api Caption Destination Settings Example
  slug: mediaconvert-api-caption-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Caption Destination Type Example
  slug: mediaconvert-api-caption-destination-type-example
- key_count: 3
  name: Mediaconvert Api Caption Selector Example
  slug: mediaconvert-api-caption-selector-example
- key_count: 2
  name: Mediaconvert Api Caption Source Framerate Example
  slug: mediaconvert-api-caption-source-framerate-example
- key_count: 8
  name: Mediaconvert Api Caption Source Settings Example
  slug: mediaconvert-api-caption-source-settings-example
- key_count: 0
  name: Mediaconvert Api Caption Source Type Example
  slug: mediaconvert-api-caption-source-type-example
- key_count: 1
  name: Mediaconvert Api Channel Mapping Example
  slug: mediaconvert-api-channel-mapping-example
- key_count: 4
  name: Mediaconvert Api Clip Limits Example
  slug: mediaconvert-api-clip-limits-example
- key_count: 2
  name: Mediaconvert Api Cmaf Additional Manifest Example
  slug: mediaconvert-api-cmaf-additional-manifest-example
- key_count: 0
  name: Mediaconvert Api Cmaf Client Cache Example
  slug: mediaconvert-api-cmaf-client-cache-example
- key_count: 0
  name: Mediaconvert Api Cmaf Codec Specification Example
  slug: mediaconvert-api-cmaf-codec-specification-example
- key_count: 6
  name: Mediaconvert Api Cmaf Encryption Settings Example
  slug: mediaconvert-api-cmaf-encryption-settings-example
- key_count: 0
  name: Mediaconvert Api Cmaf Encryption Type Example
  slug: mediaconvert-api-cmaf-encryption-type-example
- key_count: 27
  name: Mediaconvert Api Cmaf Group Settings Example
  slug: mediaconvert-api-cmaf-group-settings-example
- key_count: 0
  name: Mediaconvert Api Cmaf Image Based Trick Play Example
  slug: mediaconvert-api-cmaf-image-based-trick-play-example
- key_count: 6
  name: Mediaconvert Api Cmaf Image Based Trick Play Settings Example
  slug: mediaconvert-api-cmaf-image-based-trick-play-settings-example
- key_count: 0
  name: Mediaconvert Api Cmaf Initialization Vector In Manifest Example
  slug: mediaconvert-api-cmaf-initialization-vector-in-manifest-example
- key_count: 0
  name: Mediaconvert Api Cmaf Interval Cadence Example
  slug: mediaconvert-api-cmaf-interval-cadence-example
- key_count: 0
  name: Mediaconvert Api Cmaf Key Provider Type Example
  slug: mediaconvert-api-cmaf-key-provider-type-example
- key_count: 0
  name: Mediaconvert Api Cmaf Manifest Compression Example
  slug: mediaconvert-api-cmaf-manifest-compression-example
- key_count: 0
  name: Mediaconvert Api Cmaf Manifest Duration Format Example
  slug: mediaconvert-api-cmaf-manifest-duration-format-example
- key_count: 0
  name: Mediaconvert Api Cmaf Mpd Manifest Bandwidth Type Example
  slug: mediaconvert-api-cmaf-mpd-manifest-bandwidth-type-example
- key_count: 0
  name: Mediaconvert Api Cmaf Mpd Profile Example
  slug: mediaconvert-api-cmaf-mpd-profile-example
- key_count: 0
  name: Mediaconvert Api Cmaf Pts Offset Handling For B Frames Example
  slug: mediaconvert-api-cmaf-pts-offset-handling-for-b-frames-example
- key_count: 0
  name: Mediaconvert Api Cmaf Segment Control Example
  slug: mediaconvert-api-cmaf-segment-control-example
- key_count: 0
  name: Mediaconvert Api Cmaf Segment Length Control Example
  slug: mediaconvert-api-cmaf-segment-length-control-example
- key_count: 0
  name: Mediaconvert Api Cmaf Stream Inf Resolution Example
  slug: mediaconvert-api-cmaf-stream-inf-resolution-example
- key_count: 0
  name: Mediaconvert Api Cmaf Target Duration Compatibility Mode Example
  slug: mediaconvert-api-cmaf-target-duration-compatibility-mode-example
- key_count: 0
  name: Mediaconvert Api Cmaf Video Composition Offsets Example
  slug: mediaconvert-api-cmaf-video-composition-offsets-example
- key_count: 0
  name: Mediaconvert Api Cmaf Write Dash Manifest Example
  slug: mediaconvert-api-cmaf-write-dash-manifest-example
- key_count: 0
  name: Mediaconvert Api Cmaf Write Hls Manifest Example
  slug: mediaconvert-api-cmaf-write-hls-manifest-example
- key_count: 0
  name: Mediaconvert Api Cmaf Write Segment Timeline In Representation Example
  slug: mediaconvert-api-cmaf-write-segment-timeline-in-representation-example
- key_count: 0
  name: Mediaconvert Api Cmfc Audio Duration Example
  slug: mediaconvert-api-cmfc-audio-duration-example
- key_count: 0
  name: Mediaconvert Api Cmfc Audio Track Type Example
  slug: mediaconvert-api-cmfc-audio-track-type-example
- key_count: 0
  name: Mediaconvert Api Cmfc Descriptive Video Service Flag Example
  slug: mediaconvert-api-cmfc-descriptive-video-service-flag-example
- key_count: 0
  name: Mediaconvert Api Cmfc I Frame Only Manifest Example
  slug: mediaconvert-api-cmfc-i-frame-only-manifest-example
- key_count: 0
  name: Mediaconvert Api Cmfc Klv Metadata Example
  slug: mediaconvert-api-cmfc-klv-metadata-example
- key_count: 0
  name: Mediaconvert Api Cmfc Manifest Metadata Signaling Example
  slug: mediaconvert-api-cmfc-manifest-metadata-signaling-example
- key_count: 0
  name: Mediaconvert Api Cmfc Scte35 Esam Example
  slug: mediaconvert-api-cmfc-scte35-esam-example
- key_count: 0
  name: Mediaconvert Api Cmfc Scte35 Source Example
  slug: mediaconvert-api-cmfc-scte35-source-example
- key_count: 14
  name: Mediaconvert Api Cmfc Settings Example
  slug: mediaconvert-api-cmfc-settings-example
- key_count: 0
  name: Mediaconvert Api Cmfc Timed Metadata Box Version Example
  slug: mediaconvert-api-cmfc-timed-metadata-box-version-example
- key_count: 0
  name: Mediaconvert Api Cmfc Timed Metadata Example
  slug: mediaconvert-api-cmfc-timed-metadata-example
- key_count: 10
  name: Mediaconvert Api Color Corrector Example
  slug: mediaconvert-api-color-corrector-example
- key_count: 0
  name: Mediaconvert Api Color Metadata Example
  slug: mediaconvert-api-color-metadata-example
- key_count: 0
  name: Mediaconvert Api Color Space Conversion Example
  slug: mediaconvert-api-color-space-conversion-example
- key_count: 0
  name: Mediaconvert Api Color Space Example
  slug: mediaconvert-api-color-space-example
- key_count: 0
  name: Mediaconvert Api Color Space Usage Example
  slug: mediaconvert-api-color-space-usage-example
- key_count: 0
  name: Mediaconvert Api Commitment Example
  slug: mediaconvert-api-commitment-example
- key_count: 9
  name: Mediaconvert Api Container Settings Example
  slug: mediaconvert-api-container-settings-example
- key_count: 0
  name: Mediaconvert Api Container Type Example
  slug: mediaconvert-api-container-type-example
- key_count: 0
  name: Mediaconvert Api Copy Protection Action Example
  slug: mediaconvert-api-copy-protection-action-example
- key_count: 13
  name: Mediaconvert Api Create Job Request Example
  slug: mediaconvert-api-create-job-request-example
- key_count: 1
  name: Mediaconvert Api Create Job Response Example
  slug: mediaconvert-api-create-job-response-example
- key_count: 10
  name: Mediaconvert Api Create Job Template Request Example
  slug: mediaconvert-api-create-job-template-request-example
- key_count: 1
  name: Mediaconvert Api Create Job Template Response Example
  slug: mediaconvert-api-create-job-template-response-example
- key_count: 5
  name: Mediaconvert Api Create Preset Request Example
  slug: mediaconvert-api-create-preset-request-example
- key_count: 1
  name: Mediaconvert Api Create Preset Response Example
  slug: mediaconvert-api-create-preset-response-example
- key_count: 6
  name: Mediaconvert Api Create Queue Request Example
  slug: mediaconvert-api-create-queue-request-example
- key_count: 1
  name: Mediaconvert Api Create Queue Response Example
  slug: mediaconvert-api-create-queue-response-example
- key_count: 2
  name: Mediaconvert Api Dash Additional Manifest Example
  slug: mediaconvert-api-dash-additional-manifest-example
- key_count: 2
  name: Mediaconvert Api Dash Iso Encryption Settings Example
  slug: mediaconvert-api-dash-iso-encryption-settings-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Group Audio Channel Config Scheme Id Uri Example
  slug: mediaconvert-api-dash-iso-group-audio-channel-config-scheme-id-uri-example
- key_count: 21
  name: Mediaconvert Api Dash Iso Group Settings Example
  slug: mediaconvert-api-dash-iso-group-settings-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Hbbtv Compliance Example
  slug: mediaconvert-api-dash-iso-hbbtv-compliance-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Image Based Trick Play Example
  slug: mediaconvert-api-dash-iso-image-based-trick-play-example
- key_count: 6
  name: Mediaconvert Api Dash Iso Image Based Trick Play Settings Example
  slug: mediaconvert-api-dash-iso-image-based-trick-play-settings-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Interval Cadence Example
  slug: mediaconvert-api-dash-iso-interval-cadence-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Mpd Manifest Bandwidth Type Example
  slug: mediaconvert-api-dash-iso-mpd-manifest-bandwidth-type-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Mpd Profile Example
  slug: mediaconvert-api-dash-iso-mpd-profile-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Playback Device Compatibility Example
  slug: mediaconvert-api-dash-iso-playback-device-compatibility-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Pts Offset Handling For B Frames Example
  slug: mediaconvert-api-dash-iso-pts-offset-handling-for-b-frames-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Segment Control Example
  slug: mediaconvert-api-dash-iso-segment-control-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Segment Length Control Example
  slug: mediaconvert-api-dash-iso-segment-length-control-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Video Composition Offsets Example
  slug: mediaconvert-api-dash-iso-video-composition-offsets-example
- key_count: 0
  name: Mediaconvert Api Dash Iso Write Segment Timeline In Representation Example
  slug: mediaconvert-api-dash-iso-write-segment-timeline-in-representation-example
- key_count: 0
  name: Mediaconvert Api Dash Manifest Style Example
  slug: mediaconvert-api-dash-manifest-style-example
- key_count: 0
  name: Mediaconvert Api Decryption Mode Example
  slug: mediaconvert-api-decryption-mode-example
- key_count: 0
  name: Mediaconvert Api Deinterlace Algorithm Example
  slug: mediaconvert-api-deinterlace-algorithm-example
- key_count: 0
  name: Mediaconvert Api Deinterlacer Control Example
  slug: mediaconvert-api-deinterlacer-control-example
- key_count: 3
  name: Mediaconvert Api Deinterlacer Example
  slug: mediaconvert-api-deinterlacer-example
- key_count: 0
  name: Mediaconvert Api Deinterlacer Mode Example
  slug: mediaconvert-api-deinterlacer-mode-example
- key_count: 0
  name: Mediaconvert Api Delete Job Template Request Example
  slug: mediaconvert-api-delete-job-template-request-example
- key_count: 0
  name: Mediaconvert Api Delete Job Template Response Example
  slug: mediaconvert-api-delete-job-template-response-example
- key_count: 0
  name: Mediaconvert Api Delete Policy Request Example
  slug: mediaconvert-api-delete-policy-request-example
- key_count: 0
  name: Mediaconvert Api Delete Policy Response Example
  slug: mediaconvert-api-delete-policy-response-example
- key_count: 0
  name: Mediaconvert Api Delete Preset Request Example
  slug: mediaconvert-api-delete-preset-request-example
- key_count: 0
  name: Mediaconvert Api Delete Preset Response Example
  slug: mediaconvert-api-delete-preset-response-example
- key_count: 0
  name: Mediaconvert Api Delete Queue Request Example
  slug: mediaconvert-api-delete-queue-request-example
- key_count: 0
  name: Mediaconvert Api Delete Queue Response Example
  slug: mediaconvert-api-delete-queue-response-example
- key_count: 0
  name: Mediaconvert Api Describe Endpoints Mode Example
  slug: mediaconvert-api-describe-endpoints-mode-example
- key_count: 3
  name: Mediaconvert Api Describe Endpoints Request Example
  slug: mediaconvert-api-describe-endpoints-request-example
- key_count: 2
  name: Mediaconvert Api Describe Endpoints Response Example
  slug: mediaconvert-api-describe-endpoints-response-example
- key_count: 1
  name: Mediaconvert Api Destination Settings Example
  slug: mediaconvert-api-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Disassociate Certificate Request Example
  slug: mediaconvert-api-disassociate-certificate-request-example
- key_count: 0
  name: Mediaconvert Api Disassociate Certificate Response Example
  slug: mediaconvert-api-disassociate-certificate-response-example
- key_count: 4
  name: Mediaconvert Api Dolby Vision Example
  slug: mediaconvert-api-dolby-vision-example
- key_count: 2
  name: Mediaconvert Api Dolby Vision Level6 Metadata Example
  slug: mediaconvert-api-dolby-vision-level6-metadata-example
- key_count: 0
  name: Mediaconvert Api Dolby Vision Level6 Mode Example
  slug: mediaconvert-api-dolby-vision-level6-mode-example
- key_count: 0
  name: Mediaconvert Api Dolby Vision Mapping Example
  slug: mediaconvert-api-dolby-vision-mapping-example
- key_count: 0
  name: Mediaconvert Api Dolby Vision Profile Example
  slug: mediaconvert-api-dolby-vision-profile-example
- key_count: 0
  name: Mediaconvert Api Drop Frame Timecode Example
  slug: mediaconvert-api-drop-frame-timecode-example
- key_count: 3
  name: Mediaconvert Api Dvb Nit Settings Example
  slug: mediaconvert-api-dvb-nit-settings-example
- key_count: 4
  name: Mediaconvert Api Dvb Sdt Settings Example
  slug: mediaconvert-api-dvb-sdt-settings-example
- key_count: 27
  name: Mediaconvert Api Dvb Sub Destination Settings Example
  slug: mediaconvert-api-dvb-sub-destination-settings-example
- key_count: 1
  name: Mediaconvert Api Dvb Sub Source Settings Example
  slug: mediaconvert-api-dvb-sub-source-settings-example
- key_count: 0
  name: Mediaconvert Api Dvb Sub Subtitle Fallback Font Example
  slug: mediaconvert-api-dvb-sub-subtitle-fallback-font-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Alignment Example
  slug: mediaconvert-api-dvb-subtitle-alignment-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Apply Font Color Example
  slug: mediaconvert-api-dvb-subtitle-apply-font-color-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Background Color Example
  slug: mediaconvert-api-dvb-subtitle-background-color-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Font Color Example
  slug: mediaconvert-api-dvb-subtitle-font-color-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Outline Color Example
  slug: mediaconvert-api-dvb-subtitle-outline-color-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Shadow Color Example
  slug: mediaconvert-api-dvb-subtitle-shadow-color-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Style Passthrough Example
  slug: mediaconvert-api-dvb-subtitle-style-passthrough-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitle Teletext Spacing Example
  slug: mediaconvert-api-dvb-subtitle-teletext-spacing-example
- key_count: 0
  name: Mediaconvert Api Dvb Subtitling Type Example
  slug: mediaconvert-api-dvb-subtitling-type-example
- key_count: 1
  name: Mediaconvert Api Dvb Tdt Settings Example
  slug: mediaconvert-api-dvb-tdt-settings-example
- key_count: 0
  name: Mediaconvert Api Dvbdds Handling Example
  slug: mediaconvert-api-dvbdds-handling-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Bitstream Mode Example
  slug: mediaconvert-api-eac3-atmos-bitstream-mode-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Coding Mode Example
  slug: mediaconvert-api-eac3-atmos-coding-mode-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Dialogue Intelligence Example
  slug: mediaconvert-api-eac3-atmos-dialogue-intelligence-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Downmix Control Example
  slug: mediaconvert-api-eac3-atmos-downmix-control-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Dynamic Range Compression Line Example
  slug: mediaconvert-api-eac3-atmos-dynamic-range-compression-line-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Dynamic Range Compression Rf Example
  slug: mediaconvert-api-eac3-atmos-dynamic-range-compression-rf-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Dynamic Range Control Example
  slug: mediaconvert-api-eac3-atmos-dynamic-range-control-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Metering Mode Example
  slug: mediaconvert-api-eac3-atmos-metering-mode-example
- key_count: 17
  name: Mediaconvert Api Eac3 Atmos Settings Example
  slug: mediaconvert-api-eac3-atmos-settings-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Stereo Downmix Example
  slug: mediaconvert-api-eac3-atmos-stereo-downmix-example
- key_count: 0
  name: Mediaconvert Api Eac3 Atmos Surround Ex Mode Example
  slug: mediaconvert-api-eac3-atmos-surround-ex-mode-example
- key_count: 0
  name: Mediaconvert Api Eac3 Attenuation Control Example
  slug: mediaconvert-api-eac3-attenuation-control-example
- key_count: 0
  name: Mediaconvert Api Eac3 Bitstream Mode Example
  slug: mediaconvert-api-eac3-bitstream-mode-example
- key_count: 0
  name: Mediaconvert Api Eac3 Coding Mode Example
  slug: mediaconvert-api-eac3-coding-mode-example
- key_count: 0
  name: Mediaconvert Api Eac3 Dc Filter Example
  slug: mediaconvert-api-eac3-dc-filter-example
- key_count: 0
  name: Mediaconvert Api Eac3 Dynamic Range Compression Line Example
  slug: mediaconvert-api-eac3-dynamic-range-compression-line-example
- key_count: 0
  name: Mediaconvert Api Eac3 Dynamic Range Compression Rf Example
  slug: mediaconvert-api-eac3-dynamic-range-compression-rf-example
- key_count: 0
  name: Mediaconvert Api Eac3 Lfe Control Example
  slug: mediaconvert-api-eac3-lfe-control-example
- key_count: 0
  name: Mediaconvert Api Eac3 Lfe Filter Example
  slug: mediaconvert-api-eac3-lfe-filter-example
- key_count: 0
  name: Mediaconvert Api Eac3 Metadata Control Example
  slug: mediaconvert-api-eac3-metadata-control-example
- key_count: 0
  name: Mediaconvert Api Eac3 Passthrough Control Example
  slug: mediaconvert-api-eac3-passthrough-control-example
- key_count: 0
  name: Mediaconvert Api Eac3 Phase Control Example
  slug: mediaconvert-api-eac3-phase-control-example
- key_count: 21
  name: Mediaconvert Api Eac3 Settings Example
  slug: mediaconvert-api-eac3-settings-example
- key_count: 0
  name: Mediaconvert Api Eac3 Stereo Downmix Example
  slug: mediaconvert-api-eac3-stereo-downmix-example
- key_count: 0
  name: Mediaconvert Api Eac3 Surround Ex Mode Example
  slug: mediaconvert-api-eac3-surround-ex-mode-example
- key_count: 0
  name: Mediaconvert Api Eac3 Surround Mode Example
  slug: mediaconvert-api-eac3-surround-mode-example
- key_count: 0
  name: Mediaconvert Api Embedded Convert608 To708 Example
  slug: mediaconvert-api-embedded-convert608-to708-example
- key_count: 2
  name: Mediaconvert Api Embedded Destination Settings Example
  slug: mediaconvert-api-embedded-destination-settings-example
- key_count: 4
  name: Mediaconvert Api Embedded Source Settings Example
  slug: mediaconvert-api-embedded-source-settings-example
- key_count: 0
  name: Mediaconvert Api Embedded Terminate Captions Example
  slug: mediaconvert-api-embedded-terminate-captions-example
- key_count: 0
  name: Mediaconvert Api Embedded Timecode Override Example
  slug: mediaconvert-api-embedded-timecode-override-example
- key_count: 1
  name: Mediaconvert Api Endpoint Example
  slug: mediaconvert-api-endpoint-example
- key_count: 1
  name: Mediaconvert Api Esam Manifest Confirm Condition Notification Example
  slug: mediaconvert-api-esam-manifest-confirm-condition-notification-example
- key_count: 3
  name: Mediaconvert Api Esam Settings Example
  slug: mediaconvert-api-esam-settings-example
- key_count: 1
  name: Mediaconvert Api Esam Signal Processing Notification Example
  slug: mediaconvert-api-esam-signal-processing-notification-example
- key_count: 2
  name: Mediaconvert Api Extended Data Services Example
  slug: mediaconvert-api-extended-data-services-example
- key_count: 0
  name: Mediaconvert Api F4V Moov Placement Example
  slug: mediaconvert-api-f4v-moov-placement-example
- key_count: 1
  name: Mediaconvert Api F4V Settings Example
  slug: mediaconvert-api-f4v-settings-example
- key_count: 2
  name: Mediaconvert Api File Group Settings Example
  slug: mediaconvert-api-file-group-settings-example
- key_count: 0
  name: Mediaconvert Api File Source Convert608 To708 Example
  slug: mediaconvert-api-file-source-convert608-to708-example
- key_count: 5
  name: Mediaconvert Api File Source Settings Example
  slug: mediaconvert-api-file-source-settings-example
- key_count: 0
  name: Mediaconvert Api File Source Time Delta Units Example
  slug: mediaconvert-api-file-source-time-delta-units-example
- key_count: 0
  name: Mediaconvert Api Font Script Example
  slug: mediaconvert-api-font-script-example
- key_count: 2
  name: Mediaconvert Api Force Include Rendition Size Example
  slug: mediaconvert-api-force-include-rendition-size-example
- key_count: 4
  name: Mediaconvert Api Frame Capture Settings Example
  slug: mediaconvert-api-frame-capture-settings-example
- key_count: 0
  name: Mediaconvert Api Get Job Request Example
  slug: mediaconvert-api-get-job-request-example
- key_count: 1
  name: Mediaconvert Api Get Job Response Example
  slug: mediaconvert-api-get-job-response-example
- key_count: 0
  name: Mediaconvert Api Get Job Template Request Example
  slug: mediaconvert-api-get-job-template-request-example
- key_count: 1
  name: Mediaconvert Api Get Job Template Response Example
  slug: mediaconvert-api-get-job-template-response-example
- key_count: 0
  name: Mediaconvert Api Get Policy Request Example
  slug: mediaconvert-api-get-policy-request-example
- key_count: 1
  name: Mediaconvert Api Get Policy Response Example
  slug: mediaconvert-api-get-policy-response-example
- key_count: 0
  name: Mediaconvert Api Get Preset Request Example
  slug: mediaconvert-api-get-preset-request-example
- key_count: 1
  name: Mediaconvert Api Get Preset Response Example
  slug: mediaconvert-api-get-preset-response-example
- key_count: 0
  name: Mediaconvert Api Get Queue Request Example
  slug: mediaconvert-api-get-queue-request-example
- key_count: 1
  name: Mediaconvert Api Get Queue Response Example
  slug: mediaconvert-api-get-queue-response-example
- key_count: 0
  name: Mediaconvert Api H264 Adaptive Quantization Example
  slug: mediaconvert-api-h264-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H264 Codec Level Example
  slug: mediaconvert-api-h264-codec-level-example
- key_count: 0
  name: Mediaconvert Api H264 Codec Profile Example
  slug: mediaconvert-api-h264-codec-profile-example
- key_count: 0
  name: Mediaconvert Api H264 Dynamic Sub Gop Example
  slug: mediaconvert-api-h264-dynamic-sub-gop-example
- key_count: 0
  name: Mediaconvert Api H264 Entropy Encoding Example
  slug: mediaconvert-api-h264-entropy-encoding-example
- key_count: 0
  name: Mediaconvert Api H264 Field Encoding Example
  slug: mediaconvert-api-h264-field-encoding-example
- key_count: 0
  name: Mediaconvert Api H264 Flicker Adaptive Quantization Example
  slug: mediaconvert-api-h264-flicker-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H264 Framerate Control Example
  slug: mediaconvert-api-h264-framerate-control-example
- key_count: 0
  name: Mediaconvert Api H264 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-h264-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api H264 Gop B Reference Example
  slug: mediaconvert-api-h264-gop-b-reference-example
- key_count: 0
  name: Mediaconvert Api H264 Gop Size Units Example
  slug: mediaconvert-api-h264-gop-size-units-example
- key_count: 0
  name: Mediaconvert Api H264 Interlace Mode Example
  slug: mediaconvert-api-h264-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api H264 Par Control Example
  slug: mediaconvert-api-h264-par-control-example
- key_count: 0
  name: Mediaconvert Api H264 Quality Tuning Level Example
  slug: mediaconvert-api-h264-quality-tuning-level-example
- key_count: 3
  name: Mediaconvert Api H264 Qvbr Settings Example
  slug: mediaconvert-api-h264-qvbr-settings-example
- key_count: 0
  name: Mediaconvert Api H264 Rate Control Mode Example
  slug: mediaconvert-api-h264-rate-control-mode-example
- key_count: 0
  name: Mediaconvert Api H264 Repeat Pps Example
  slug: mediaconvert-api-h264-repeat-pps-example
- key_count: 0
  name: Mediaconvert Api H264 Scan Type Conversion Mode Example
  slug: mediaconvert-api-h264-scan-type-conversion-mode-example
- key_count: 0
  name: Mediaconvert Api H264 Scene Change Detect Example
  slug: mediaconvert-api-h264-scene-change-detect-example
- key_count: 42
  name: Mediaconvert Api H264 Settings Example
  slug: mediaconvert-api-h264-settings-example
- key_count: 0
  name: Mediaconvert Api H264 Slow Pal Example
  slug: mediaconvert-api-h264-slow-pal-example
- key_count: 0
  name: Mediaconvert Api H264 Spatial Adaptive Quantization Example
  slug: mediaconvert-api-h264-spatial-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H264 Syntax Example
  slug: mediaconvert-api-h264-syntax-example
- key_count: 0
  name: Mediaconvert Api H264 Telecine Example
  slug: mediaconvert-api-h264-telecine-example
- key_count: 0
  name: Mediaconvert Api H264 Temporal Adaptive Quantization Example
  slug: mediaconvert-api-h264-temporal-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H264 Unregistered Sei Timecode Example
  slug: mediaconvert-api-h264-unregistered-sei-timecode-example
- key_count: 0
  name: Mediaconvert Api H265 Adaptive Quantization Example
  slug: mediaconvert-api-h265-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H265 Alternate Transfer Function Sei Example
  slug: mediaconvert-api-h265-alternate-transfer-function-sei-example
- key_count: 0
  name: Mediaconvert Api H265 Codec Level Example
  slug: mediaconvert-api-h265-codec-level-example
- key_count: 0
  name: Mediaconvert Api H265 Codec Profile Example
  slug: mediaconvert-api-h265-codec-profile-example
- key_count: 0
  name: Mediaconvert Api H265 Dynamic Sub Gop Example
  slug: mediaconvert-api-h265-dynamic-sub-gop-example
- key_count: 0
  name: Mediaconvert Api H265 Flicker Adaptive Quantization Example
  slug: mediaconvert-api-h265-flicker-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H265 Framerate Control Example
  slug: mediaconvert-api-h265-framerate-control-example
- key_count: 0
  name: Mediaconvert Api H265 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-h265-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api H265 Gop B Reference Example
  slug: mediaconvert-api-h265-gop-b-reference-example
- key_count: 0
  name: Mediaconvert Api H265 Gop Size Units Example
  slug: mediaconvert-api-h265-gop-size-units-example
- key_count: 0
  name: Mediaconvert Api H265 Interlace Mode Example
  slug: mediaconvert-api-h265-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api H265 Par Control Example
  slug: mediaconvert-api-h265-par-control-example
- key_count: 0
  name: Mediaconvert Api H265 Quality Tuning Level Example
  slug: mediaconvert-api-h265-quality-tuning-level-example
- key_count: 3
  name: Mediaconvert Api H265 Qvbr Settings Example
  slug: mediaconvert-api-h265-qvbr-settings-example
- key_count: 0
  name: Mediaconvert Api H265 Rate Control Mode Example
  slug: mediaconvert-api-h265-rate-control-mode-example
- key_count: 0
  name: Mediaconvert Api H265 Sample Adaptive Offset Filter Mode Example
  slug: mediaconvert-api-h265-sample-adaptive-offset-filter-mode-example
- key_count: 0
  name: Mediaconvert Api H265 Scan Type Conversion Mode Example
  slug: mediaconvert-api-h265-scan-type-conversion-mode-example
- key_count: 0
  name: Mediaconvert Api H265 Scene Change Detect Example
  slug: mediaconvert-api-h265-scene-change-detect-example
- key_count: 41
  name: Mediaconvert Api H265 Settings Example
  slug: mediaconvert-api-h265-settings-example
- key_count: 0
  name: Mediaconvert Api H265 Slow Pal Example
  slug: mediaconvert-api-h265-slow-pal-example
- key_count: 0
  name: Mediaconvert Api H265 Spatial Adaptive Quantization Example
  slug: mediaconvert-api-h265-spatial-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H265 Telecine Example
  slug: mediaconvert-api-h265-telecine-example
- key_count: 0
  name: Mediaconvert Api H265 Temporal Adaptive Quantization Example
  slug: mediaconvert-api-h265-temporal-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api H265 Temporal Ids Example
  slug: mediaconvert-api-h265-temporal-ids-example
- key_count: 0
  name: Mediaconvert Api H265 Tiles Example
  slug: mediaconvert-api-h265-tiles-example
- key_count: 0
  name: Mediaconvert Api H265 Unregistered Sei Timecode Example
  slug: mediaconvert-api-h265-unregistered-sei-timecode-example
- key_count: 0
  name: Mediaconvert Api H265 Write Mp4 Packaging Type Example
  slug: mediaconvert-api-h265-write-mp4-packaging-type-example
- key_count: 0
  name: Mediaconvert Api Hdr To Sdr Tone Mapper Example
  slug: mediaconvert-api-hdr-to-sdr-tone-mapper-example
- key_count: 12
  name: Mediaconvert Api Hdr10 Metadata Example
  slug: mediaconvert-api-hdr10-metadata-example
- key_count: 2
  name: Mediaconvert Api Hdr10 Plus Example
  slug: mediaconvert-api-hdr10-plus-example
- key_count: 0
  name: Mediaconvert Api Hls Ad Markers Example
  slug: mediaconvert-api-hls-ad-markers-example
- key_count: 2
  name: Mediaconvert Api Hls Additional Manifest Example
  slug: mediaconvert-api-hls-additional-manifest-example
- key_count: 0
  name: Mediaconvert Api Hls Audio Only Container Example
  slug: mediaconvert-api-hls-audio-only-container-example
- key_count: 0
  name: Mediaconvert Api Hls Audio Only Header Example
  slug: mediaconvert-api-hls-audio-only-header-example
- key_count: 0
  name: Mediaconvert Api Hls Audio Track Type Example
  slug: mediaconvert-api-hls-audio-track-type-example
- key_count: 4
  name: Mediaconvert Api Hls Caption Language Mapping Example
  slug: mediaconvert-api-hls-caption-language-mapping-example
- key_count: 0
  name: Mediaconvert Api Hls Caption Language Setting Example
  slug: mediaconvert-api-hls-caption-language-setting-example
- key_count: 0
  name: Mediaconvert Api Hls Caption Segment Length Control Example
  slug: mediaconvert-api-hls-caption-segment-length-control-example
- key_count: 0
  name: Mediaconvert Api Hls Client Cache Example
  slug: mediaconvert-api-hls-client-cache-example
- key_count: 0
  name: Mediaconvert Api Hls Codec Specification Example
  slug: mediaconvert-api-hls-codec-specification-example
- key_count: 0
  name: Mediaconvert Api Hls Descriptive Video Service Flag Example
  slug: mediaconvert-api-hls-descriptive-video-service-flag-example
- key_count: 0
  name: Mediaconvert Api Hls Directory Structure Example
  slug: mediaconvert-api-hls-directory-structure-example
- key_count: 7
  name: Mediaconvert Api Hls Encryption Settings Example
  slug: mediaconvert-api-hls-encryption-settings-example
- key_count: 0
  name: Mediaconvert Api Hls Encryption Type Example
  slug: mediaconvert-api-hls-encryption-type-example
- key_count: 31
  name: Mediaconvert Api Hls Group Settings Example
  slug: mediaconvert-api-hls-group-settings-example
- key_count: 0
  name: Mediaconvert Api Hls I Frame Only Manifest Example
  slug: mediaconvert-api-hls-i-frame-only-manifest-example
- key_count: 0
  name: Mediaconvert Api Hls Image Based Trick Play Example
  slug: mediaconvert-api-hls-image-based-trick-play-example
- key_count: 6
  name: Mediaconvert Api Hls Image Based Trick Play Settings Example
  slug: mediaconvert-api-hls-image-based-trick-play-settings-example
- key_count: 0
  name: Mediaconvert Api Hls Initialization Vector In Manifest Example
  slug: mediaconvert-api-hls-initialization-vector-in-manifest-example
- key_count: 0
  name: Mediaconvert Api Hls Interval Cadence Example
  slug: mediaconvert-api-hls-interval-cadence-example
- key_count: 0
  name: Mediaconvert Api Hls Key Provider Type Example
  slug: mediaconvert-api-hls-key-provider-type-example
- key_count: 0
  name: Mediaconvert Api Hls Manifest Compression Example
  slug: mediaconvert-api-hls-manifest-compression-example
- key_count: 0
  name: Mediaconvert Api Hls Manifest Duration Format Example
  slug: mediaconvert-api-hls-manifest-duration-format-example
- key_count: 0
  name: Mediaconvert Api Hls Offline Encrypted Example
  slug: mediaconvert-api-hls-offline-encrypted-example
- key_count: 0
  name: Mediaconvert Api Hls Output Selection Example
  slug: mediaconvert-api-hls-output-selection-example
- key_count: 0
  name: Mediaconvert Api Hls Program Date Time Example
  slug: mediaconvert-api-hls-program-date-time-example
- key_count: 3
  name: Mediaconvert Api Hls Rendition Group Settings Example
  slug: mediaconvert-api-hls-rendition-group-settings-example
- key_count: 0
  name: Mediaconvert Api Hls Segment Control Example
  slug: mediaconvert-api-hls-segment-control-example
- key_count: 0
  name: Mediaconvert Api Hls Segment Length Control Example
  slug: mediaconvert-api-hls-segment-length-control-example
- key_count: 7
  name: Mediaconvert Api Hls Settings Example
  slug: mediaconvert-api-hls-settings-example
- key_count: 0
  name: Mediaconvert Api Hls Stream Inf Resolution Example
  slug: mediaconvert-api-hls-stream-inf-resolution-example
- key_count: 0
  name: Mediaconvert Api Hls Target Duration Compatibility Mode Example
  slug: mediaconvert-api-hls-target-duration-compatibility-mode-example
- key_count: 0
  name: Mediaconvert Api Hls Timed Metadata Id3 Frame Example
  slug: mediaconvert-api-hls-timed-metadata-id3-frame-example
- key_count: 3
  name: Mediaconvert Api Hop Destination Example
  slug: mediaconvert-api-hop-destination-example
- key_count: 2
  name: Mediaconvert Api Id3 Insertion Example
  slug: mediaconvert-api-id3-insertion-example
- key_count: 2
  name: Mediaconvert Api Image Inserter Example
  slug: mediaconvert-api-image-inserter-example
- key_count: 0
  name: Mediaconvert Api Imsc Accessibility Subs Example
  slug: mediaconvert-api-imsc-accessibility-subs-example
- key_count: 2
  name: Mediaconvert Api Imsc Destination Settings Example
  slug: mediaconvert-api-imsc-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Imsc Style Passthrough Example
  slug: mediaconvert-api-imsc-style-passthrough-example
- key_count: 2
  name: Mediaconvert Api Input Clipping Example
  slug: mediaconvert-api-input-clipping-example
- key_count: 0
  name: Mediaconvert Api Input Deblock Filter Example
  slug: mediaconvert-api-input-deblock-filter-example
- key_count: 4
  name: Mediaconvert Api Input Decryption Settings Example
  slug: mediaconvert-api-input-decryption-settings-example
- key_count: 0
  name: Mediaconvert Api Input Denoise Filter Example
  slug: mediaconvert-api-input-denoise-filter-example
- key_count: 22
  name: Mediaconvert Api Input Example
  slug: mediaconvert-api-input-example
- key_count: 0
  name: Mediaconvert Api Input Filter Enable Example
  slug: mediaconvert-api-input-filter-enable-example
- key_count: 0
  name: Mediaconvert Api Input Policy Example
  slug: mediaconvert-api-input-policy-example
- key_count: 0
  name: Mediaconvert Api Input Psi Control Example
  slug: mediaconvert-api-input-psi-control-example
- key_count: 0
  name: Mediaconvert Api Input Rotate Example
  slug: mediaconvert-api-input-rotate-example
- key_count: 0
  name: Mediaconvert Api Input Sample Range Example
  slug: mediaconvert-api-input-sample-range-example
- key_count: 0
  name: Mediaconvert Api Input Scan Type Example
  slug: mediaconvert-api-input-scan-type-example
- key_count: 18
  name: Mediaconvert Api Input Template Example
  slug: mediaconvert-api-input-template-example
- key_count: 0
  name: Mediaconvert Api Input Timecode Source Example
  slug: mediaconvert-api-input-timecode-source-example
- key_count: 1
  name: Mediaconvert Api Input Video Generator Example
  slug: mediaconvert-api-input-video-generator-example
- key_count: 11
  name: Mediaconvert Api Insertable Image Example
  slug: mediaconvert-api-insertable-image-example
- key_count: 27
  name: Mediaconvert Api Job Example
  slug: mediaconvert-api-job-example
- key_count: 2
  name: Mediaconvert Api Job Messages Example
  slug: mediaconvert-api-job-messages-example
- key_count: 0
  name: Mediaconvert Api Job Phase Example
  slug: mediaconvert-api-job-phase-example
- key_count: 12
  name: Mediaconvert Api Job Settings Example
  slug: mediaconvert-api-job-settings-example
- key_count: 0
  name: Mediaconvert Api Job Status Example
  slug: mediaconvert-api-job-status-example
- key_count: 13
  name: Mediaconvert Api Job Template Example
  slug: mediaconvert-api-job-template-example
- key_count: 0
  name: Mediaconvert Api Job Template List By Example
  slug: mediaconvert-api-job-template-list-by-example
- key_count: 12
  name: Mediaconvert Api Job Template Settings Example
  slug: mediaconvert-api-job-template-settings-example
- key_count: 13
  name: Mediaconvert Api Kantar Watermark Settings Example
  slug: mediaconvert-api-kantar-watermark-settings-example
- key_count: 0
  name: Mediaconvert Api Language Code Example
  slug: mediaconvert-api-language-code-example
- key_count: 0
  name: Mediaconvert Api List Job Templates Request Example
  slug: mediaconvert-api-list-job-templates-request-example
- key_count: 2
  name: Mediaconvert Api List Job Templates Response Example
  slug: mediaconvert-api-list-job-templates-response-example
- key_count: 0
  name: Mediaconvert Api List Jobs Request Example
  slug: mediaconvert-api-list-jobs-request-example
- key_count: 2
  name: Mediaconvert Api List Jobs Response Example
  slug: mediaconvert-api-list-jobs-response-example
- key_count: 0
  name: Mediaconvert Api List Presets Request Example
  slug: mediaconvert-api-list-presets-request-example
- key_count: 2
  name: Mediaconvert Api List Presets Response Example
  slug: mediaconvert-api-list-presets-response-example
- key_count: 0
  name: Mediaconvert Api List Queues Request Example
  slug: mediaconvert-api-list-queues-request-example
- key_count: 2
  name: Mediaconvert Api List Queues Response Example
  slug: mediaconvert-api-list-queues-response-example
- key_count: 0
  name: Mediaconvert Api List Tags For Resource Request Example
  slug: mediaconvert-api-list-tags-for-resource-request-example
- key_count: 1
  name: Mediaconvert Api List Tags For Resource Response Example
  slug: mediaconvert-api-list-tags-for-resource-response-example
- key_count: 0
  name: Mediaconvert Api M2Ts Audio Buffer Model Example
  slug: mediaconvert-api-m2ts-audio-buffer-model-example
- key_count: 0
  name: Mediaconvert Api M2Ts Audio Duration Example
  slug: mediaconvert-api-m2ts-audio-duration-example
- key_count: 0
  name: Mediaconvert Api M2Ts Buffer Model Example
  slug: mediaconvert-api-m2ts-buffer-model-example
- key_count: 0
  name: Mediaconvert Api M2Ts Data Pts Control Example
  slug: mediaconvert-api-m2ts-data-pts-control-example
- key_count: 0
  name: Mediaconvert Api M2Ts Ebp Audio Interval Example
  slug: mediaconvert-api-m2ts-ebp-audio-interval-example
- key_count: 0
  name: Mediaconvert Api M2Ts Ebp Placement Example
  slug: mediaconvert-api-m2ts-ebp-placement-example
- key_count: 0
  name: Mediaconvert Api M2Ts Es Rate In Pes Example
  slug: mediaconvert-api-m2ts-es-rate-in-pes-example
- key_count: 0
  name: Mediaconvert Api M2Ts Force Ts Video Ebp Order Example
  slug: mediaconvert-api-m2ts-force-ts-video-ebp-order-example
- key_count: 0
  name: Mediaconvert Api M2Ts Klv Metadata Example
  slug: mediaconvert-api-m2ts-klv-metadata-example
- key_count: 0
  name: Mediaconvert Api M2Ts Nielsen Id3 Example
  slug: mediaconvert-api-m2ts-nielsen-id3-example
- key_count: 0
  name: Mediaconvert Api M2Ts Pcr Control Example
  slug: mediaconvert-api-m2ts-pcr-control-example
- key_count: 0
  name: Mediaconvert Api M2Ts Rate Mode Example
  slug: mediaconvert-api-m2ts-rate-mode-example
- key_count: 1
  name: Mediaconvert Api M2Ts Scte35 Esam Example
  slug: mediaconvert-api-m2ts-scte35-esam-example
- key_count: 0
  name: Mediaconvert Api M2Ts Scte35 Source Example
  slug: mediaconvert-api-m2ts-scte35-source-example
- key_count: 0
  name: Mediaconvert Api M2Ts Segmentation Markers Example
  slug: mediaconvert-api-m2ts-segmentation-markers-example
- key_count: 0
  name: Mediaconvert Api M2Ts Segmentation Style Example
  slug: mediaconvert-api-m2ts-segmentation-style-example
- key_count: 39
  name: Mediaconvert Api M2Ts Settings Example
  slug: mediaconvert-api-m2ts-settings-example
- key_count: 0
  name: Mediaconvert Api M3U8 Audio Duration Example
  slug: mediaconvert-api-m3u8-audio-duration-example
- key_count: 0
  name: Mediaconvert Api M3U8 Data Pts Control Example
  slug: mediaconvert-api-m3u8-data-pts-control-example
- key_count: 0
  name: Mediaconvert Api M3U8 Nielsen Id3 Example
  slug: mediaconvert-api-m3u8-nielsen-id3-example
- key_count: 0
  name: Mediaconvert Api M3U8 Pcr Control Example
  slug: mediaconvert-api-m3u8-pcr-control-example
- key_count: 0
  name: Mediaconvert Api M3U8 Scte35 Source Example
  slug: mediaconvert-api-m3u8-scte35-source-example
- key_count: 19
  name: Mediaconvert Api M3U8 Settings Example
  slug: mediaconvert-api-m3u8-settings-example
- key_count: 2
  name: Mediaconvert Api Min Bottom Rendition Size Example
  slug: mediaconvert-api-min-bottom-rendition-size-example
- key_count: 2
  name: Mediaconvert Api Min Top Rendition Size Example
  slug: mediaconvert-api-min-top-rendition-size-example
- key_count: 6
  name: Mediaconvert Api Motion Image Inserter Example
  slug: mediaconvert-api-motion-image-inserter-example
- key_count: 2
  name: Mediaconvert Api Motion Image Insertion Framerate Example
  slug: mediaconvert-api-motion-image-insertion-framerate-example
- key_count: 0
  name: Mediaconvert Api Motion Image Insertion Mode Example
  slug: mediaconvert-api-motion-image-insertion-mode-example
- key_count: 2
  name: Mediaconvert Api Motion Image Insertion Offset Example
  slug: mediaconvert-api-motion-image-insertion-offset-example
- key_count: 0
  name: Mediaconvert Api Motion Image Playback Example
  slug: mediaconvert-api-motion-image-playback-example
- key_count: 0
  name: Mediaconvert Api Mov Clap Atom Example
  slug: mediaconvert-api-mov-clap-atom-example
- key_count: 0
  name: Mediaconvert Api Mov Cslg Atom Example
  slug: mediaconvert-api-mov-cslg-atom-example
- key_count: 0
  name: Mediaconvert Api Mov Mpeg2 Four Cc Control Example
  slug: mediaconvert-api-mov-mpeg2-four-cc-control-example
- key_count: 0
  name: Mediaconvert Api Mov Padding Control Example
  slug: mediaconvert-api-mov-padding-control-example
- key_count: 0
  name: Mediaconvert Api Mov Reference Example
  slug: mediaconvert-api-mov-reference-example
- key_count: 5
  name: Mediaconvert Api Mov Settings Example
  slug: mediaconvert-api-mov-settings-example
- key_count: 3
  name: Mediaconvert Api Mp2 Settings Example
  slug: mediaconvert-api-mp2-settings-example
- key_count: 0
  name: Mediaconvert Api Mp3 Rate Control Mode Example
  slug: mediaconvert-api-mp3-rate-control-mode-example
- key_count: 5
  name: Mediaconvert Api Mp3 Settings Example
  slug: mediaconvert-api-mp3-settings-example
- key_count: 0
  name: Mediaconvert Api Mp4 Cslg Atom Example
  slug: mediaconvert-api-mp4-cslg-atom-example
- key_count: 0
  name: Mediaconvert Api Mp4 Free Space Box Example
  slug: mediaconvert-api-mp4-free-space-box-example
- key_count: 0
  name: Mediaconvert Api Mp4 Moov Placement Example
  slug: mediaconvert-api-mp4-moov-placement-example
- key_count: 6
  name: Mediaconvert Api Mp4 Settings Example
  slug: mediaconvert-api-mp4-settings-example
- key_count: 0
  name: Mediaconvert Api Mpd Accessibility Caption Hints Example
  slug: mediaconvert-api-mpd-accessibility-caption-hints-example
- key_count: 0
  name: Mediaconvert Api Mpd Audio Duration Example
  slug: mediaconvert-api-mpd-audio-duration-example
- key_count: 0
  name: Mediaconvert Api Mpd Caption Container Type Example
  slug: mediaconvert-api-mpd-caption-container-type-example
- key_count: 0
  name: Mediaconvert Api Mpd Klv Metadata Example
  slug: mediaconvert-api-mpd-klv-metadata-example
- key_count: 0
  name: Mediaconvert Api Mpd Manifest Metadata Signaling Example
  slug: mediaconvert-api-mpd-manifest-metadata-signaling-example
- key_count: 0
  name: Mediaconvert Api Mpd Scte35 Esam Example
  slug: mediaconvert-api-mpd-scte35-esam-example
- key_count: 0
  name: Mediaconvert Api Mpd Scte35 Source Example
  slug: mediaconvert-api-mpd-scte35-source-example
- key_count: 11
  name: Mediaconvert Api Mpd Settings Example
  slug: mediaconvert-api-mpd-settings-example
- key_count: 0
  name: Mediaconvert Api Mpd Timed Metadata Box Version Example
  slug: mediaconvert-api-mpd-timed-metadata-box-version-example
- key_count: 0
  name: Mediaconvert Api Mpd Timed Metadata Example
  slug: mediaconvert-api-mpd-timed-metadata-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Adaptive Quantization Example
  slug: mediaconvert-api-mpeg2-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Codec Level Example
  slug: mediaconvert-api-mpeg2-codec-level-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Codec Profile Example
  slug: mediaconvert-api-mpeg2-codec-profile-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Dynamic Sub Gop Example
  slug: mediaconvert-api-mpeg2-dynamic-sub-gop-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Framerate Control Example
  slug: mediaconvert-api-mpeg2-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-mpeg2-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Gop Size Units Example
  slug: mediaconvert-api-mpeg2-gop-size-units-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Interlace Mode Example
  slug: mediaconvert-api-mpeg2-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Intra Dc Precision Example
  slug: mediaconvert-api-mpeg2-intra-dc-precision-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Par Control Example
  slug: mediaconvert-api-mpeg2-par-control-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Quality Tuning Level Example
  slug: mediaconvert-api-mpeg2-quality-tuning-level-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Rate Control Mode Example
  slug: mediaconvert-api-mpeg2-rate-control-mode-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Scan Type Conversion Mode Example
  slug: mediaconvert-api-mpeg2-scan-type-conversion-mode-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Scene Change Detect Example
  slug: mediaconvert-api-mpeg2-scene-change-detect-example
- key_count: 33
  name: Mediaconvert Api Mpeg2 Settings Example
  slug: mediaconvert-api-mpeg2-settings-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Slow Pal Example
  slug: mediaconvert-api-mpeg2-slow-pal-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Spatial Adaptive Quantization Example
  slug: mediaconvert-api-mpeg2-spatial-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Syntax Example
  slug: mediaconvert-api-mpeg2-syntax-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Telecine Example
  slug: mediaconvert-api-mpeg2-telecine-example
- key_count: 0
  name: Mediaconvert Api Mpeg2 Temporal Adaptive Quantization Example
  slug: mediaconvert-api-mpeg2-temporal-adaptive-quantization-example
- key_count: 2
  name: Mediaconvert Api Ms Smooth Additional Manifest Example
  slug: mediaconvert-api-ms-smooth-additional-manifest-example
- key_count: 0
  name: Mediaconvert Api Ms Smooth Audio Deduplication Example
  slug: mediaconvert-api-ms-smooth-audio-deduplication-example
- key_count: 1
  name: Mediaconvert Api Ms Smooth Encryption Settings Example
  slug: mediaconvert-api-ms-smooth-encryption-settings-example
- key_count: 0
  name: Mediaconvert Api Ms Smooth Fragment Length Control Example
  slug: mediaconvert-api-ms-smooth-fragment-length-control-example
- key_count: 8
  name: Mediaconvert Api Ms Smooth Group Settings Example
  slug: mediaconvert-api-ms-smooth-group-settings-example
- key_count: 0
  name: Mediaconvert Api Ms Smooth Manifest Encoding Example
  slug: mediaconvert-api-ms-smooth-manifest-encoding-example
- key_count: 0
  name: Mediaconvert Api Mxf Afd Signaling Example
  slug: mediaconvert-api-mxf-afd-signaling-example
- key_count: 0
  name: Mediaconvert Api Mxf Profile Example
  slug: mediaconvert-api-mxf-profile-example
- key_count: 3
  name: Mediaconvert Api Mxf Settings Example
  slug: mediaconvert-api-mxf-settings-example
- key_count: 0
  name: Mediaconvert Api Mxf Xavc Duration Mode Example
  slug: mediaconvert-api-mxf-xavc-duration-mode-example
- key_count: 2
  name: Mediaconvert Api Mxf Xavc Profile Settings Example
  slug: mediaconvert-api-mxf-xavc-profile-settings-example
- key_count: 4
  name: Mediaconvert Api Nex Guard File Marker Settings Example
  slug: mediaconvert-api-nex-guard-file-marker-settings-example
- key_count: 0
  name: Mediaconvert Api Nielsen Active Watermark Process Type Example
  slug: mediaconvert-api-nielsen-active-watermark-process-type-example
- key_count: 2
  name: Mediaconvert Api Nielsen Configuration Example
  slug: mediaconvert-api-nielsen-configuration-example
- key_count: 11
  name: Mediaconvert Api Nielsen Non Linear Watermark Settings Example
  slug: mediaconvert-api-nielsen-non-linear-watermark-settings-example
- key_count: 0
  name: Mediaconvert Api Nielsen Source Watermark Status Type Example
  slug: mediaconvert-api-nielsen-source-watermark-status-type-example
- key_count: 0
  name: Mediaconvert Api Nielsen Unique Tic Per Audio Track Type Example
  slug: mediaconvert-api-nielsen-unique-tic-per-audio-track-type-example
- key_count: 0
  name: Mediaconvert Api Noise Filter Post Temporal Sharpening Example
  slug: mediaconvert-api-noise-filter-post-temporal-sharpening-example
- key_count: 0
  name: Mediaconvert Api Noise Filter Post Temporal Sharpening Strength Example
  slug: mediaconvert-api-noise-filter-post-temporal-sharpening-strength-example
- key_count: 4
  name: Mediaconvert Api Noise Reducer Example
  slug: mediaconvert-api-noise-reducer-example
- key_count: 0
  name: Mediaconvert Api Noise Reducer Filter Example
  slug: mediaconvert-api-noise-reducer-filter-example
- key_count: 1
  name: Mediaconvert Api Noise Reducer Filter Settings Example
  slug: mediaconvert-api-noise-reducer-filter-settings-example
- key_count: 3
  name: Mediaconvert Api Noise Reducer Spatial Filter Settings Example
  slug: mediaconvert-api-noise-reducer-spatial-filter-settings-example
- key_count: 5
  name: Mediaconvert Api Noise Reducer Temporal Filter Settings Example
  slug: mediaconvert-api-noise-reducer-temporal-filter-settings-example
- key_count: 3
  name: Mediaconvert Api Opus Settings Example
  slug: mediaconvert-api-opus-settings-example
- key_count: 0
  name: Mediaconvert Api Order Example
  slug: mediaconvert-api-order-example
- key_count: 2
  name: Mediaconvert Api Output Channel Mapping Example
  slug: mediaconvert-api-output-channel-mapping-example
- key_count: 2
  name: Mediaconvert Api Output Detail Example
  slug: mediaconvert-api-output-detail-example
- key_count: 8
  name: Mediaconvert Api Output Example
  slug: mediaconvert-api-output-example
- key_count: 1
  name: Mediaconvert Api Output Group Detail Example
  slug: mediaconvert-api-output-group-detail-example
- key_count: 5
  name: Mediaconvert Api Output Group Example
  slug: mediaconvert-api-output-group-example
- key_count: 6
  name: Mediaconvert Api Output Group Settings Example
  slug: mediaconvert-api-output-group-settings-example
- key_count: 0
  name: Mediaconvert Api Output Group Type Example
  slug: mediaconvert-api-output-group-type-example
- key_count: 0
  name: Mediaconvert Api Output Sdt Example
  slug: mediaconvert-api-output-sdt-example
- key_count: 1
  name: Mediaconvert Api Output Settings Example
  slug: mediaconvert-api-output-settings-example
- key_count: 0
  name: Mediaconvert Api Pad Video Example
  slug: mediaconvert-api-pad-video-example
- key_count: 1
  name: Mediaconvert Api Partner Watermarking Example
  slug: mediaconvert-api-partner-watermarking-example
- key_count: 3
  name: Mediaconvert Api Policy Example
  slug: mediaconvert-api-policy-example
- key_count: 8
  name: Mediaconvert Api Preset Example
  slug: mediaconvert-api-preset-example
- key_count: 0
  name: Mediaconvert Api Preset List By Example
  slug: mediaconvert-api-preset-list-by-example
- key_count: 4
  name: Mediaconvert Api Preset Settings Example
  slug: mediaconvert-api-preset-settings-example
- key_count: 0
  name: Mediaconvert Api Pricing Plan Example
  slug: mediaconvert-api-pricing-plan-example
- key_count: 0
  name: Mediaconvert Api Prores Chroma Sampling Example
  slug: mediaconvert-api-prores-chroma-sampling-example
- key_count: 0
  name: Mediaconvert Api Prores Codec Profile Example
  slug: mediaconvert-api-prores-codec-profile-example
- key_count: 0
  name: Mediaconvert Api Prores Framerate Control Example
  slug: mediaconvert-api-prores-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Prores Framerate Conversion Algorithm Example
  slug: mediaconvert-api-prores-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Prores Interlace Mode Example
  slug: mediaconvert-api-prores-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api Prores Par Control Example
  slug: mediaconvert-api-prores-par-control-example
- key_count: 0
  name: Mediaconvert Api Prores Scan Type Conversion Mode Example
  slug: mediaconvert-api-prores-scan-type-conversion-mode-example
- key_count: 13
  name: Mediaconvert Api Prores Settings Example
  slug: mediaconvert-api-prores-settings-example
- key_count: 0
  name: Mediaconvert Api Prores Slow Pal Example
  slug: mediaconvert-api-prores-slow-pal-example
- key_count: 0
  name: Mediaconvert Api Prores Telecine Example
  slug: mediaconvert-api-prores-telecine-example
- key_count: 1
  name: Mediaconvert Api Put Policy Request Example
  slug: mediaconvert-api-put-policy-request-example
- key_count: 1
  name: Mediaconvert Api Put Policy Response Example
  slug: mediaconvert-api-put-policy-response-example
- key_count: 11
  name: Mediaconvert Api Queue Example
  slug: mediaconvert-api-queue-example
- key_count: 0
  name: Mediaconvert Api Queue List By Example
  slug: mediaconvert-api-queue-list-by-example
- key_count: 0
  name: Mediaconvert Api Queue Status Example
  slug: mediaconvert-api-queue-status-example
- key_count: 3
  name: Mediaconvert Api Queue Transition Example
  slug: mediaconvert-api-queue-transition-example
- key_count: 4
  name: Mediaconvert Api Rectangle Example
  slug: mediaconvert-api-rectangle-example
- key_count: 3
  name: Mediaconvert Api Remix Settings Example
  slug: mediaconvert-api-remix-settings-example
- key_count: 0
  name: Mediaconvert Api Renewal Type Example
  slug: mediaconvert-api-renewal-type-example
- key_count: 0
  name: Mediaconvert Api Required Flag Example
  slug: mediaconvert-api-required-flag-example
- key_count: 6
  name: Mediaconvert Api Reservation Plan Example
  slug: mediaconvert-api-reservation-plan-example
- key_count: 3
  name: Mediaconvert Api Reservation Plan Settings Example
  slug: mediaconvert-api-reservation-plan-settings-example
- key_count: 0
  name: Mediaconvert Api Reservation Plan Status Example
  slug: mediaconvert-api-reservation-plan-status-example
- key_count: 2
  name: Mediaconvert Api Resource Tags Example
  slug: mediaconvert-api-resource-tags-example
- key_count: 0
  name: Mediaconvert Api Respond To Afd Example
  slug: mediaconvert-api-respond-to-afd-example
- key_count: 0
  name: Mediaconvert Api Rule Type Example
  slug: mediaconvert-api-rule-type-example
- key_count: 1
  name: Mediaconvert Api S3 Destination Access Control Example
  slug: mediaconvert-api-s3-destination-access-control-example
- key_count: 2
  name: Mediaconvert Api S3 Destination Settings Example
  slug: mediaconvert-api-s3-destination-settings-example
- key_count: 3
  name: Mediaconvert Api S3 Encryption Settings Example
  slug: mediaconvert-api-s3-encryption-settings-example
- key_count: 0
  name: Mediaconvert Api S3 Object Canned Acl Example
  slug: mediaconvert-api-s3-object-canned-acl-example
- key_count: 0
  name: Mediaconvert Api S3 Server Side Encryption Type Example
  slug: mediaconvert-api-s3-server-side-encryption-type-example
- key_count: 0
  name: Mediaconvert Api Sample Range Conversion Example
  slug: mediaconvert-api-sample-range-conversion-example
- key_count: 0
  name: Mediaconvert Api Scaling Behavior Example
  slug: mediaconvert-api-scaling-behavior-example
- key_count: 0
  name: Mediaconvert Api Scc Destination Framerate Example
  slug: mediaconvert-api-scc-destination-framerate-example
- key_count: 1
  name: Mediaconvert Api Scc Destination Settings Example
  slug: mediaconvert-api-scc-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Simulate Reserved Queue Example
  slug: mediaconvert-api-simulate-reserved-queue-example
- key_count: 5
  name: Mediaconvert Api Speke Key Provider Cmaf Example
  slug: mediaconvert-api-speke-key-provider-cmaf-example
- key_count: 4
  name: Mediaconvert Api Speke Key Provider Example
  slug: mediaconvert-api-speke-key-provider-example
- key_count: 1
  name: Mediaconvert Api Srt Destination Settings Example
  slug: mediaconvert-api-srt-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Srt Style Passthrough Example
  slug: mediaconvert-api-srt-style-passthrough-example
- key_count: 4
  name: Mediaconvert Api Static Key Provider Example
  slug: mediaconvert-api-static-key-provider-example
- key_count: 0
  name: Mediaconvert Api Status Update Interval Example
  slug: mediaconvert-api-status-update-interval-example
- key_count: 2
  name: Mediaconvert Api Tag Resource Request Example
  slug: mediaconvert-api-tag-resource-request-example
- key_count: 0
  name: Mediaconvert Api Tag Resource Response Example
  slug: mediaconvert-api-tag-resource-response-example
- key_count: 2
  name: Mediaconvert Api Teletext Destination Settings Example
  slug: mediaconvert-api-teletext-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Teletext Page Type Example
  slug: mediaconvert-api-teletext-page-type-example
- key_count: 1
  name: Mediaconvert Api Teletext Source Settings Example
  slug: mediaconvert-api-teletext-source-settings-example
- key_count: 3
  name: Mediaconvert Api Timecode Burnin Example
  slug: mediaconvert-api-timecode-burnin-example
- key_count: 0
  name: Mediaconvert Api Timecode Burnin Position Example
  slug: mediaconvert-api-timecode-burnin-position-example
- key_count: 4
  name: Mediaconvert Api Timecode Config Example
  slug: mediaconvert-api-timecode-config-example
- key_count: 0
  name: Mediaconvert Api Timecode Source Example
  slug: mediaconvert-api-timecode-source-example
- key_count: 0
  name: Mediaconvert Api Timed Metadata Example
  slug: mediaconvert-api-timed-metadata-example
- key_count: 1
  name: Mediaconvert Api Timed Metadata Insertion Example
  slug: mediaconvert-api-timed-metadata-insertion-example
- key_count: 3
  name: Mediaconvert Api Timing Example
  slug: mediaconvert-api-timing-example
- key_count: 1
  name: Mediaconvert Api Track Source Settings Example
  slug: mediaconvert-api-track-source-settings-example
- key_count: 1
  name: Mediaconvert Api Ttml Destination Settings Example
  slug: mediaconvert-api-ttml-destination-settings-example
- key_count: 0
  name: Mediaconvert Api Ttml Style Passthrough Example
  slug: mediaconvert-api-ttml-style-passthrough-example
- key_count: 0
  name: Mediaconvert Api Type Example
  slug: mediaconvert-api-type-example
- key_count: 1
  name: Mediaconvert Api Untag Resource Request Example
  slug: mediaconvert-api-untag-resource-request-example
- key_count: 0
  name: Mediaconvert Api Untag Resource Response Example
  slug: mediaconvert-api-untag-resource-response-example
- key_count: 8
  name: Mediaconvert Api Update Job Template Request Example
  slug: mediaconvert-api-update-job-template-request-example
- key_count: 1
  name: Mediaconvert Api Update Job Template Response Example
  slug: mediaconvert-api-update-job-template-response-example
- key_count: 3
  name: Mediaconvert Api Update Preset Request Example
  slug: mediaconvert-api-update-preset-request-example
- key_count: 1
  name: Mediaconvert Api Update Preset Response Example
  slug: mediaconvert-api-update-preset-response-example
- key_count: 3
  name: Mediaconvert Api Update Queue Request Example
  slug: mediaconvert-api-update-queue-request-example
- key_count: 1
  name: Mediaconvert Api Update Queue Response Example
  slug: mediaconvert-api-update-queue-response-example
- key_count: 0
  name: Mediaconvert Api Vc3 Class Example
  slug: mediaconvert-api-vc3-class-example
- key_count: 0
  name: Mediaconvert Api Vc3 Framerate Control Example
  slug: mediaconvert-api-vc3-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Vc3 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-vc3-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Vc3 Interlace Mode Example
  slug: mediaconvert-api-vc3-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api Vc3 Scan Type Conversion Mode Example
  slug: mediaconvert-api-vc3-scan-type-conversion-mode-example
- key_count: 9
  name: Mediaconvert Api Vc3 Settings Example
  slug: mediaconvert-api-vc3-settings-example
- key_count: 0
  name: Mediaconvert Api Vc3 Slow Pal Example
  slug: mediaconvert-api-vc3-slow-pal-example
- key_count: 0
  name: Mediaconvert Api Vc3 Telecine Example
  slug: mediaconvert-api-vc3-telecine-example
- key_count: 0
  name: Mediaconvert Api Vchip Action Example
  slug: mediaconvert-api-vchip-action-example
- key_count: 0
  name: Mediaconvert Api Video Codec Example
  slug: mediaconvert-api-video-codec-example
- key_count: 12
  name: Mediaconvert Api Video Codec Settings Example
  slug: mediaconvert-api-video-codec-settings-example
- key_count: 15
  name: Mediaconvert Api Video Description Example
  slug: mediaconvert-api-video-description-example
- key_count: 2
  name: Mediaconvert Api Video Detail Example
  slug: mediaconvert-api-video-detail-example
- key_count: 8
  name: Mediaconvert Api Video Preprocessor Example
  slug: mediaconvert-api-video-preprocessor-example
- key_count: 10
  name: Mediaconvert Api Video Selector Example
  slug: mediaconvert-api-video-selector-example
- key_count: 0
  name: Mediaconvert Api Video Timecode Insertion Example
  slug: mediaconvert-api-video-timecode-insertion-example
- key_count: 3
  name: Mediaconvert Api Vorbis Settings Example
  slug: mediaconvert-api-vorbis-settings-example
- key_count: 0
  name: Mediaconvert Api Vp8 Framerate Control Example
  slug: mediaconvert-api-vp8-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Vp8 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-vp8-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Vp8 Par Control Example
  slug: mediaconvert-api-vp8-par-control-example
- key_count: 0
  name: Mediaconvert Api Vp8 Quality Tuning Level Example
  slug: mediaconvert-api-vp8-quality-tuning-level-example
- key_count: 0
  name: Mediaconvert Api Vp8 Rate Control Mode Example
  slug: mediaconvert-api-vp8-rate-control-mode-example
- key_count: 13
  name: Mediaconvert Api Vp8 Settings Example
  slug: mediaconvert-api-vp8-settings-example
- key_count: 0
  name: Mediaconvert Api Vp9 Framerate Control Example
  slug: mediaconvert-api-vp9-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Vp9 Framerate Conversion Algorithm Example
  slug: mediaconvert-api-vp9-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Vp9 Par Control Example
  slug: mediaconvert-api-vp9-par-control-example
- key_count: 0
  name: Mediaconvert Api Vp9 Quality Tuning Level Example
  slug: mediaconvert-api-vp9-quality-tuning-level-example
- key_count: 0
  name: Mediaconvert Api Vp9 Rate Control Mode Example
  slug: mediaconvert-api-vp9-rate-control-mode-example
- key_count: 13
  name: Mediaconvert Api Vp9 Settings Example
  slug: mediaconvert-api-vp9-settings-example
- key_count: 2
  name: Mediaconvert Api Warning Group Example
  slug: mediaconvert-api-warning-group-example
- key_count: 0
  name: Mediaconvert Api Watermarking Strength Example
  slug: mediaconvert-api-watermarking-strength-example
- key_count: 0
  name: Mediaconvert Api Wav Format Example
  slug: mediaconvert-api-wav-format-example
- key_count: 4
  name: Mediaconvert Api Wav Settings Example
  slug: mediaconvert-api-wav-settings-example
- key_count: 0
  name: Mediaconvert Api Webvtt Accessibility Subs Example
  slug: mediaconvert-api-webvtt-accessibility-subs-example
- key_count: 2
  name: Mediaconvert Api Webvtt Destination Settings Example
  slug: mediaconvert-api-webvtt-destination-settings-example
- key_count: 3
  name: Mediaconvert Api Webvtt Hls Source Settings Example
  slug: mediaconvert-api-webvtt-hls-source-settings-example
- key_count: 0
  name: Mediaconvert Api Webvtt Style Passthrough Example
  slug: mediaconvert-api-webvtt-style-passthrough-example
- key_count: 0
  name: Mediaconvert Api Xavc Adaptive Quantization Example
  slug: mediaconvert-api-xavc-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Xavc Entropy Encoding Example
  slug: mediaconvert-api-xavc-entropy-encoding-example
- key_count: 0
  name: Mediaconvert Api Xavc Flicker Adaptive Quantization Example
  slug: mediaconvert-api-xavc-flicker-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Xavc Framerate Control Example
  slug: mediaconvert-api-xavc-framerate-control-example
- key_count: 0
  name: Mediaconvert Api Xavc Framerate Conversion Algorithm Example
  slug: mediaconvert-api-xavc-framerate-conversion-algorithm-example
- key_count: 0
  name: Mediaconvert Api Xavc Gop B Reference Example
  slug: mediaconvert-api-xavc-gop-b-reference-example
- key_count: 0
  name: Mediaconvert Api Xavc Hd Intra Cbg Profile Class Example
  slug: mediaconvert-api-xavc-hd-intra-cbg-profile-class-example
- key_count: 1
  name: Mediaconvert Api Xavc Hd Intra Cbg Profile Settings Example
  slug: mediaconvert-api-xavc-hd-intra-cbg-profile-settings-example
- key_count: 0
  name: Mediaconvert Api Xavc Hd Profile Bitrate Class Example
  slug: mediaconvert-api-xavc-hd-profile-bitrate-class-example
- key_count: 0
  name: Mediaconvert Api Xavc Hd Profile Quality Tuning Level Example
  slug: mediaconvert-api-xavc-hd-profile-quality-tuning-level-example
- key_count: 9
  name: Mediaconvert Api Xavc Hd Profile Settings Example
  slug: mediaconvert-api-xavc-hd-profile-settings-example
- key_count: 0
  name: Mediaconvert Api Xavc Hd Profile Telecine Example
  slug: mediaconvert-api-xavc-hd-profile-telecine-example
- key_count: 0
  name: Mediaconvert Api Xavc Interlace Mode Example
  slug: mediaconvert-api-xavc-interlace-mode-example
- key_count: 0
  name: Mediaconvert Api Xavc Profile Example
  slug: mediaconvert-api-xavc-profile-example
- key_count: 16
  name: Mediaconvert Api Xavc Settings Example
  slug: mediaconvert-api-xavc-settings-example
- key_count: 0
  name: Mediaconvert Api Xavc Slow Pal Example
  slug: mediaconvert-api-xavc-slow-pal-example
- key_count: 0
  name: Mediaconvert Api Xavc Spatial Adaptive Quantization Example
  slug: mediaconvert-api-xavc-spatial-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Xavc Temporal Adaptive Quantization Example
  slug: mediaconvert-api-xavc-temporal-adaptive-quantization-example
- key_count: 0
  name: Mediaconvert Api Xavc4K Intra Cbg Profile Class Example
  slug: mediaconvert-api-xavc4k-intra-cbg-profile-class-example
- key_count: 1
  name: Mediaconvert Api Xavc4K Intra Cbg Profile Settings Example
  slug: mediaconvert-api-xavc4k-intra-cbg-profile-settings-example
- key_count: 0
  name: Mediaconvert Api Xavc4K Intra Vbr Profile Class Example
  slug: mediaconvert-api-xavc4k-intra-vbr-profile-class-example
- key_count: 1
  name: Mediaconvert Api Xavc4K Intra Vbr Profile Settings Example
  slug: mediaconvert-api-xavc4k-intra-vbr-profile-settings-example
- key_count: 0
  name: Mediaconvert Api Xavc4K Profile Bitrate Class Example
  slug: mediaconvert-api-xavc4k-profile-bitrate-class-example
- key_count: 0
  name: Mediaconvert Api Xavc4K Profile Codec Profile Example
  slug: mediaconvert-api-xavc4k-profile-codec-profile-example
- key_count: 0
  name: Mediaconvert Api Xavc4K Profile Quality Tuning Level Example
  slug: mediaconvert-api-xavc4k-profile-quality-tuning-level-example
- key_count: 8
  name: Mediaconvert Api Xavc4K Profile Settings Example
  slug: mediaconvert-api-xavc4k-profile-settings-example
features:
- description: Graphic overlays, content protection, multi-language audio, closed captioning, and professional broadcast formats.
  name: Broadcast-Grade Video Processing
- description: Supports AVC, HEVC, AV1, Apple ProRes, MPEG-2, CMAF, HLS, DASH ISO, Smooth Streaming, 4K, 8K, and HDR including Dolby Vision.
  name: Comprehensive Format Support
- description: Automates workload provisioning, scaling, monitoring, and resource optimization without manual server management.
  name: Automated Infrastructure Management
- description: Jobs run on redundant infrastructure across multiple Availability Zones with automatic health monitoring and failover.
  name: Built-in Reliability
- description: Create reusable job templates and output presets to standardize and accelerate video transcoding workflows.
  name: Job Templates and Presets
- description: Organize and prioritize transcoding jobs using on-demand and reserved queues.
  name: Queue Management
finops:
- name: Amazon Mediaconvert Finops
  service_category: API
  slug: amazon-mediaconvert-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-mediaconvert.png
json_schemas:
- name: AacAudioDescriptionBroadcasterMix
  property_count: 0
  slug: mediaconvert-api-aac-audio-description-broadcaster-mix
- name: AacCodecProfile
  property_count: 0
  slug: mediaconvert-api-aac-codec-profile
- name: AacCodingMode
  property_count: 0
  slug: mediaconvert-api-aac-coding-mode
- name: AacRateControlMode
  property_count: 0
  slug: mediaconvert-api-aac-rate-control-mode
- name: AacRawFormat
  property_count: 0
  slug: mediaconvert-api-aac-raw-format
- name: AacSettings
  property_count: 9
  slug: mediaconvert-api-aac-settings
- name: AacSpecification
  property_count: 0
  slug: mediaconvert-api-aac-specification
- name: AacVbrQuality
  property_count: 0
  slug: mediaconvert-api-aac-vbr-quality
- name: Ac3BitstreamMode
  property_count: 0
  slug: mediaconvert-api-ac3-bitstream-mode
- name: Ac3CodingMode
  property_count: 0
  slug: mediaconvert-api-ac3-coding-mode
- name: Ac3DynamicRangeCompressionLine
  property_count: 0
  slug: mediaconvert-api-ac3-dynamic-range-compression-line
- name: Ac3DynamicRangeCompressionProfile
  property_count: 0
  slug: mediaconvert-api-ac3-dynamic-range-compression-profile
- name: Ac3DynamicRangeCompressionRf
  property_count: 0
  slug: mediaconvert-api-ac3-dynamic-range-compression-rf
- name: Ac3LfeFilter
  property_count: 0
  slug: mediaconvert-api-ac3-lfe-filter
- name: Ac3MetadataControl
  property_count: 0
  slug: mediaconvert-api-ac3-metadata-control
- name: Ac3Settings
  property_count: 10
  slug: mediaconvert-api-ac3-settings
- name: AccelerationMode
  property_count: 0
  slug: mediaconvert-api-acceleration-mode
- name: AccelerationSettings
  property_count: 1
  slug: mediaconvert-api-acceleration-settings
- name: AccelerationStatus
  property_count: 0
  slug: mediaconvert-api-acceleration-status
- name: AfdSignaling
  property_count: 0
  slug: mediaconvert-api-afd-signaling
- name: AiffSettings
  property_count: 3
  slug: mediaconvert-api-aiff-settings
- name: AllowedRenditionSize
  property_count: 3
  slug: mediaconvert-api-allowed-rendition-size
- name: AlphaBehavior
  property_count: 0
  slug: mediaconvert-api-alpha-behavior
- name: AncillaryConvert608To708
  property_count: 0
  slug: mediaconvert-api-ancillary-convert608-to708
- name: AncillarySourceSettings
  property_count: 3
  slug: mediaconvert-api-ancillary-source-settings
- name: AncillaryTerminateCaptions
  property_count: 0
  slug: mediaconvert-api-ancillary-terminate-captions
- name: AntiAlias
  property_count: 0
  slug: mediaconvert-api-anti-alias
- name: AssociateCertificateRequest
  property_count: 1
  slug: mediaconvert-api-associate-certificate-request
- name: AssociateCertificateResponse
  property_count: 0
  slug: mediaconvert-api-associate-certificate-response
- name: AudioChannelTag
  property_count: 0
  slug: mediaconvert-api-audio-channel-tag
- name: AudioChannelTaggingSettings
  property_count: 1
  slug: mediaconvert-api-audio-channel-tagging-settings
- name: AudioCodec
  property_count: 0
  slug: mediaconvert-api-audio-codec
- name: AudioCodecSettings
  property_count: 11
  slug: mediaconvert-api-audio-codec-settings
- name: AudioDefaultSelection
  property_count: 0
  slug: mediaconvert-api-audio-default-selection
- name: AudioDescription
  property_count: 11
  slug: mediaconvert-api-audio-description
- name: AudioDurationCorrection
  property_count: 0
  slug: mediaconvert-api-audio-duration-correction
- name: AudioLanguageCodeControl
  property_count: 0
  slug: mediaconvert-api-audio-language-code-control
- name: AudioNormalizationAlgorithmControl
  property_count: 0
  slug: mediaconvert-api-audio-normalization-algorithm-control
- name: AudioNormalizationAlgorithm
  property_count: 0
  slug: mediaconvert-api-audio-normalization-algorithm
- name: AudioNormalizationLoudnessLogging
  property_count: 0
  slug: mediaconvert-api-audio-normalization-loudness-logging
- name: AudioNormalizationPeakCalculation
  property_count: 0
  slug: mediaconvert-api-audio-normalization-peak-calculation
- name: AudioNormalizationSettings
  property_count: 7
  slug: mediaconvert-api-audio-normalization-settings
- name: AudioSelectorGroup
  property_count: 1
  slug: mediaconvert-api-audio-selector-group
- name: AudioSelector
  property_count: 12
  slug: mediaconvert-api-audio-selector
- name: AudioSelectorType
  property_count: 0
  slug: mediaconvert-api-audio-selector-type
- name: AudioTypeControl
  property_count: 0
  slug: mediaconvert-api-audio-type-control
- name: AutomatedAbrRule
  property_count: 5
  slug: mediaconvert-api-automated-abr-rule
- name: AutomatedAbrSettings
  property_count: 4
  slug: mediaconvert-api-automated-abr-settings
- name: AutomatedEncodingSettings
  property_count: 1
  slug: mediaconvert-api-automated-encoding-settings
- name: Av1AdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-av1-adaptive-quantization
- name: Av1BitDepth
  property_count: 0
  slug: mediaconvert-api-av1-bit-depth
- name: Av1FramerateControl
  property_count: 0
  slug: mediaconvert-api-av1-framerate-control
- name: Av1FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-av1-framerate-conversion-algorithm
- name: Av1QvbrSettings
  property_count: 2
  slug: mediaconvert-api-av1-qvbr-settings
- name: Av1RateControlMode
  property_count: 0
  slug: mediaconvert-api-av1-rate-control-mode
- name: Av1Settings
  property_count: 13
  slug: mediaconvert-api-av1-settings
- name: Av1SpatialAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-av1-spatial-adaptive-quantization
- name: AvailBlanking
  property_count: 1
  slug: mediaconvert-api-avail-blanking
- name: AvcIntraClass
  property_count: 0
  slug: mediaconvert-api-avc-intra-class
- name: AvcIntraFramerateControl
  property_count: 0
  slug: mediaconvert-api-avc-intra-framerate-control
- name: AvcIntraFramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-avc-intra-framerate-conversion-algorithm
- name: AvcIntraInterlaceMode
  property_count: 0
  slug: mediaconvert-api-avc-intra-interlace-mode
- name: AvcIntraScanTypeConversionMode
  property_count: 0
  slug: mediaconvert-api-avc-intra-scan-type-conversion-mode
- name: AvcIntraSettings
  property_count: 10
  slug: mediaconvert-api-avc-intra-settings
- name: AvcIntraSlowPal
  property_count: 0
  slug: mediaconvert-api-avc-intra-slow-pal
- name: AvcIntraTelecine
  property_count: 0
  slug: mediaconvert-api-avc-intra-telecine
- name: AvcIntraUhdQualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-avc-intra-uhd-quality-tuning-level
- name: AvcIntraUhdSettings
  property_count: 1
  slug: mediaconvert-api-avc-intra-uhd-settings
- name: BandwidthReductionFilter
  property_count: 2
  slug: mediaconvert-api-bandwidth-reduction-filter
- name: BandwidthReductionFilterSharpening
  property_count: 0
  slug: mediaconvert-api-bandwidth-reduction-filter-sharpening
- name: BandwidthReductionFilterStrength
  property_count: 0
  slug: mediaconvert-api-bandwidth-reduction-filter-strength
- name: BillingTagsSource
  property_count: 0
  slug: mediaconvert-api-billing-tags-source
- name: BurnInSubtitleStylePassthrough
  property_count: 0
  slug: mediaconvert-api-burn-in-subtitle-style-passthrough
- name: BurninDestinationSettings
  property_count: 21
  slug: mediaconvert-api-burnin-destination-settings
- name: BurninSubtitleAlignment
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-alignment
- name: BurninSubtitleApplyFontColor
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-apply-font-color
- name: BurninSubtitleBackgroundColor
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-background-color
- name: BurninSubtitleFallbackFont
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-fallback-font
- name: BurninSubtitleFontColor
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-font-color
- name: BurninSubtitleOutlineColor
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-outline-color
- name: BurninSubtitleShadowColor
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-shadow-color
- name: BurninSubtitleTeletextSpacing
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-teletext-spacing
- name: CancelJobRequest
  property_count: 0
  slug: mediaconvert-api-cancel-job-request
- name: CancelJobResponse
  property_count: 0
  slug: mediaconvert-api-cancel-job-response
- name: CaptionDescriptionPreset
  property_count: 4
  slug: mediaconvert-api-caption-description-preset
- name: CaptionDescription
  property_count: 5
  slug: mediaconvert-api-caption-description
- name: CaptionDestinationSettings
  property_count: 10
  slug: mediaconvert-api-caption-destination-settings
- name: CaptionDestinationType
  property_count: 0
  slug: mediaconvert-api-caption-destination-type
- name: CaptionSelector
  property_count: 3
  slug: mediaconvert-api-caption-selector
- name: CaptionSourceFramerate
  property_count: 2
  slug: mediaconvert-api-caption-source-framerate
- name: CaptionSourceSettings
  property_count: 8
  slug: mediaconvert-api-caption-source-settings
- name: CaptionSourceType
  property_count: 0
  slug: mediaconvert-api-caption-source-type
- name: ChannelMapping
  property_count: 1
  slug: mediaconvert-api-channel-mapping
- name: ClipLimits
  property_count: 4
  slug: mediaconvert-api-clip-limits
- name: CmafAdditionalManifest
  property_count: 2
  slug: mediaconvert-api-cmaf-additional-manifest
- name: CmafClientCache
  property_count: 0
  slug: mediaconvert-api-cmaf-client-cache
- name: CmafCodecSpecification
  property_count: 0
  slug: mediaconvert-api-cmaf-codec-specification
- name: CmafEncryptionSettings
  property_count: 6
  slug: mediaconvert-api-cmaf-encryption-settings
- name: CmafEncryptionType
  property_count: 0
  slug: mediaconvert-api-cmaf-encryption-type
- name: CmafGroupSettings
  property_count: 27
  slug: mediaconvert-api-cmaf-group-settings
- name: CmafImageBasedTrickPlay
  property_count: 0
  slug: mediaconvert-api-cmaf-image-based-trick-play
- name: CmafImageBasedTrickPlaySettings
  property_count: 6
  slug: mediaconvert-api-cmaf-image-based-trick-play-settings
- name: CmafInitializationVectorInManifest
  property_count: 0
  slug: mediaconvert-api-cmaf-initialization-vector-in-manifest
- name: CmafIntervalCadence
  property_count: 0
  slug: mediaconvert-api-cmaf-interval-cadence
- name: CmafKeyProviderType
  property_count: 0
  slug: mediaconvert-api-cmaf-key-provider-type
- name: CmafManifestCompression
  property_count: 0
  slug: mediaconvert-api-cmaf-manifest-compression
- name: CmafManifestDurationFormat
  property_count: 0
  slug: mediaconvert-api-cmaf-manifest-duration-format
- name: CmafMpdManifestBandwidthType
  property_count: 0
  slug: mediaconvert-api-cmaf-mpd-manifest-bandwidth-type
- name: CmafMpdProfile
  property_count: 0
  slug: mediaconvert-api-cmaf-mpd-profile
- name: CmafPtsOffsetHandlingForBFrames
  property_count: 0
  slug: mediaconvert-api-cmaf-pts-offset-handling-for-b-frames
- name: CmafSegmentControl
  property_count: 0
  slug: mediaconvert-api-cmaf-segment-control
- name: CmafSegmentLengthControl
  property_count: 0
  slug: mediaconvert-api-cmaf-segment-length-control
- name: CmafStreamInfResolution
  property_count: 0
  slug: mediaconvert-api-cmaf-stream-inf-resolution
- name: CmafTargetDurationCompatibilityMode
  property_count: 0
  slug: mediaconvert-api-cmaf-target-duration-compatibility-mode
- name: CmafVideoCompositionOffsets
  property_count: 0
  slug: mediaconvert-api-cmaf-video-composition-offsets
- name: CmafWriteDASHManifest
  property_count: 0
  slug: mediaconvert-api-cmaf-write-dash-manifest
- name: CmafWriteHLSManifest
  property_count: 0
  slug: mediaconvert-api-cmaf-write-hls-manifest
- name: CmafWriteSegmentTimelineInRepresentation
  property_count: 0
  slug: mediaconvert-api-cmaf-write-segment-timeline-in-representation
- name: CmfcAudioDuration
  property_count: 0
  slug: mediaconvert-api-cmfc-audio-duration
- name: CmfcAudioTrackType
  property_count: 0
  slug: mediaconvert-api-cmfc-audio-track-type
- name: CmfcDescriptiveVideoServiceFlag
  property_count: 0
  slug: mediaconvert-api-cmfc-descriptive-video-service-flag
- name: CmfcIFrameOnlyManifest
  property_count: 0
  slug: mediaconvert-api-cmfc-i-frame-only-manifest
- name: CmfcKlvMetadata
  property_count: 0
  slug: mediaconvert-api-cmfc-klv-metadata
- name: CmfcManifestMetadataSignaling
  property_count: 0
  slug: mediaconvert-api-cmfc-manifest-metadata-signaling
- name: CmfcScte35Esam
  property_count: 0
  slug: mediaconvert-api-cmfc-scte35-esam
- name: CmfcScte35Source
  property_count: 0
  slug: mediaconvert-api-cmfc-scte35-source
- name: CmfcSettings
  property_count: 14
  slug: mediaconvert-api-cmfc-settings
- name: CmfcTimedMetadataBoxVersion
  property_count: 0
  slug: mediaconvert-api-cmfc-timed-metadata-box-version
- name: CmfcTimedMetadata
  property_count: 0
  slug: mediaconvert-api-cmfc-timed-metadata
- name: ColorCorrector
  property_count: 10
  slug: mediaconvert-api-color-corrector
- name: ColorMetadata
  property_count: 0
  slug: mediaconvert-api-color-metadata
- name: ColorSpaceConversion
  property_count: 0
  slug: mediaconvert-api-color-space-conversion
- name: ColorSpace
  property_count: 0
  slug: mediaconvert-api-color-space
- name: ColorSpaceUsage
  property_count: 0
  slug: mediaconvert-api-color-space-usage
- name: Commitment
  property_count: 0
  slug: mediaconvert-api-commitment
- name: ContainerSettings
  property_count: 9
  slug: mediaconvert-api-container-settings
- name: ContainerType
  property_count: 0
  slug: mediaconvert-api-container-type
- name: CopyProtectionAction
  property_count: 0
  slug: mediaconvert-api-copy-protection-action
- name: CreateJobRequest
  property_count: 13
  slug: mediaconvert-api-create-job-request
- name: CreateJobResponse
  property_count: 1
  slug: mediaconvert-api-create-job-response
- name: CreateJobTemplateRequest
  property_count: 10
  slug: mediaconvert-api-create-job-template-request
- name: CreateJobTemplateResponse
  property_count: 1
  slug: mediaconvert-api-create-job-template-response
- name: CreatePresetRequest
  property_count: 5
  slug: mediaconvert-api-create-preset-request
- name: CreatePresetResponse
  property_count: 1
  slug: mediaconvert-api-create-preset-response
- name: CreateQueueRequest
  property_count: 6
  slug: mediaconvert-api-create-queue-request
- name: CreateQueueResponse
  property_count: 1
  slug: mediaconvert-api-create-queue-response
- name: DashAdditionalManifest
  property_count: 2
  slug: mediaconvert-api-dash-additional-manifest
- name: DashIsoEncryptionSettings
  property_count: 2
  slug: mediaconvert-api-dash-iso-encryption-settings
- name: DashIsoGroupAudioChannelConfigSchemeIdUri
  property_count: 0
  slug: mediaconvert-api-dash-iso-group-audio-channel-config-scheme-id-uri
- name: DashIsoGroupSettings
  property_count: 21
  slug: mediaconvert-api-dash-iso-group-settings
- name: DashIsoHbbtvCompliance
  property_count: 0
  slug: mediaconvert-api-dash-iso-hbbtv-compliance
- name: DashIsoImageBasedTrickPlay
  property_count: 0
  slug: mediaconvert-api-dash-iso-image-based-trick-play
- name: DashIsoImageBasedTrickPlaySettings
  property_count: 6
  slug: mediaconvert-api-dash-iso-image-based-trick-play-settings
- name: DashIsoIntervalCadence
  property_count: 0
  slug: mediaconvert-api-dash-iso-interval-cadence
- name: DashIsoMpdManifestBandwidthType
  property_count: 0
  slug: mediaconvert-api-dash-iso-mpd-manifest-bandwidth-type
- name: DashIsoMpdProfile
  property_count: 0
  slug: mediaconvert-api-dash-iso-mpd-profile
- name: DashIsoPlaybackDeviceCompatibility
  property_count: 0
  slug: mediaconvert-api-dash-iso-playback-device-compatibility
- name: DashIsoPtsOffsetHandlingForBFrames
  property_count: 0
  slug: mediaconvert-api-dash-iso-pts-offset-handling-for-b-frames
- name: DashIsoSegmentControl
  property_count: 0
  slug: mediaconvert-api-dash-iso-segment-control
- name: DashIsoSegmentLengthControl
  property_count: 0
  slug: mediaconvert-api-dash-iso-segment-length-control
- name: DashIsoVideoCompositionOffsets
  property_count: 0
  slug: mediaconvert-api-dash-iso-video-composition-offsets
- name: DashIsoWriteSegmentTimelineInRepresentation
  property_count: 0
  slug: mediaconvert-api-dash-iso-write-segment-timeline-in-representation
- name: DashManifestStyle
  property_count: 0
  slug: mediaconvert-api-dash-manifest-style
- name: DecryptionMode
  property_count: 0
  slug: mediaconvert-api-decryption-mode
- name: DeinterlaceAlgorithm
  property_count: 0
  slug: mediaconvert-api-deinterlace-algorithm
- name: DeinterlacerControl
  property_count: 0
  slug: mediaconvert-api-deinterlacer-control
- name: DeinterlacerMode
  property_count: 0
  slug: mediaconvert-api-deinterlacer-mode
- name: Deinterlacer
  property_count: 3
  slug: mediaconvert-api-deinterlacer
- name: DeleteJobTemplateRequest
  property_count: 0
  slug: mediaconvert-api-delete-job-template-request
- name: DeleteJobTemplateResponse
  property_count: 0
  slug: mediaconvert-api-delete-job-template-response
- name: DeletePolicyRequest
  property_count: 0
  slug: mediaconvert-api-delete-policy-request
- name: DeletePolicyResponse
  property_count: 0
  slug: mediaconvert-api-delete-policy-response
- name: DeletePresetRequest
  property_count: 0
  slug: mediaconvert-api-delete-preset-request
- name: DeletePresetResponse
  property_count: 0
  slug: mediaconvert-api-delete-preset-response
- name: DeleteQueueRequest
  property_count: 0
  slug: mediaconvert-api-delete-queue-request
- name: DeleteQueueResponse
  property_count: 0
  slug: mediaconvert-api-delete-queue-response
- name: DescribeEndpointsMode
  property_count: 0
  slug: mediaconvert-api-describe-endpoints-mode
- name: DescribeEndpointsRequest
  property_count: 3
  slug: mediaconvert-api-describe-endpoints-request
- name: DescribeEndpointsResponse
  property_count: 2
  slug: mediaconvert-api-describe-endpoints-response
- name: DestinationSettings
  property_count: 1
  slug: mediaconvert-api-destination-settings
- name: DisassociateCertificateRequest
  property_count: 0
  slug: mediaconvert-api-disassociate-certificate-request
- name: DisassociateCertificateResponse
  property_count: 0
  slug: mediaconvert-api-disassociate-certificate-response
- name: DolbyVisionLevel6Metadata
  property_count: 2
  slug: mediaconvert-api-dolby-vision-level6-metadata
- name: DolbyVisionLevel6Mode
  property_count: 0
  slug: mediaconvert-api-dolby-vision-level6-mode
- name: DolbyVisionMapping
  property_count: 0
  slug: mediaconvert-api-dolby-vision-mapping
- name: DolbyVisionProfile
  property_count: 0
  slug: mediaconvert-api-dolby-vision-profile
- name: DolbyVision
  property_count: 4
  slug: mediaconvert-api-dolby-vision
- name: DropFrameTimecode
  property_count: 0
  slug: mediaconvert-api-drop-frame-timecode
- name: DvbNitSettings
  property_count: 3
  slug: mediaconvert-api-dvb-nit-settings
- name: DvbSdtSettings
  property_count: 4
  slug: mediaconvert-api-dvb-sdt-settings
- name: DvbSubDestinationSettings
  property_count: 27
  slug: mediaconvert-api-dvb-sub-destination-settings
- name: DvbSubSourceSettings
  property_count: 1
  slug: mediaconvert-api-dvb-sub-source-settings
- name: DvbSubSubtitleFallbackFont
  property_count: 0
  slug: mediaconvert-api-dvb-sub-subtitle-fallback-font
- name: DvbSubtitleAlignment
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-alignment
- name: DvbSubtitleApplyFontColor
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-apply-font-color
- name: DvbSubtitleBackgroundColor
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-background-color
- name: DvbSubtitleFontColor
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-font-color
- name: DvbSubtitleOutlineColor
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-outline-color
- name: DvbSubtitleShadowColor
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-shadow-color
- name: DvbSubtitleStylePassthrough
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-style-passthrough
- name: DvbSubtitleTeletextSpacing
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-teletext-spacing
- name: DvbSubtitlingType
  property_count: 0
  slug: mediaconvert-api-dvb-subtitling-type
- name: DvbTdtSettings
  property_count: 1
  slug: mediaconvert-api-dvb-tdt-settings
- name: DvbddsHandling
  property_count: 0
  slug: mediaconvert-api-dvbdds-handling
- name: Eac3AtmosBitstreamMode
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-bitstream-mode
- name: Eac3AtmosCodingMode
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-coding-mode
- name: Eac3AtmosDialogueIntelligence
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dialogue-intelligence
- name: Eac3AtmosDownmixControl
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-downmix-control
- name: Eac3AtmosDynamicRangeCompressionLine
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dynamic-range-compression-line
- name: Eac3AtmosDynamicRangeCompressionRf
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dynamic-range-compression-rf
- name: Eac3AtmosDynamicRangeControl
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dynamic-range-control
- name: Eac3AtmosMeteringMode
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-metering-mode
- name: Eac3AtmosSettings
  property_count: 17
  slug: mediaconvert-api-eac3-atmos-settings
- name: Eac3AtmosStereoDownmix
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-stereo-downmix
- name: Eac3AtmosSurroundExMode
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-surround-ex-mode
- name: Eac3AttenuationControl
  property_count: 0
  slug: mediaconvert-api-eac3-attenuation-control
- name: Eac3BitstreamMode
  property_count: 0
  slug: mediaconvert-api-eac3-bitstream-mode
- name: Eac3CodingMode
  property_count: 0
  slug: mediaconvert-api-eac3-coding-mode
- name: Eac3DcFilter
  property_count: 0
  slug: mediaconvert-api-eac3-dc-filter
- name: Eac3DynamicRangeCompressionLine
  property_count: 0
  slug: mediaconvert-api-eac3-dynamic-range-compression-line
- name: Eac3DynamicRangeCompressionRf
  property_count: 0
  slug: mediaconvert-api-eac3-dynamic-range-compression-rf
- name: Eac3LfeControl
  property_count: 0
  slug: mediaconvert-api-eac3-lfe-control
- name: Eac3LfeFilter
  property_count: 0
  slug: mediaconvert-api-eac3-lfe-filter
- name: Eac3MetadataControl
  property_count: 0
  slug: mediaconvert-api-eac3-metadata-control
- name: Eac3PassthroughControl
  property_count: 0
  slug: mediaconvert-api-eac3-passthrough-control
- name: Eac3PhaseControl
  property_count: 0
  slug: mediaconvert-api-eac3-phase-control
- name: Eac3Settings
  property_count: 21
  slug: mediaconvert-api-eac3-settings
- name: Eac3StereoDownmix
  property_count: 0
  slug: mediaconvert-api-eac3-stereo-downmix
- name: Eac3SurroundExMode
  property_count: 0
  slug: mediaconvert-api-eac3-surround-ex-mode
- name: Eac3SurroundMode
  property_count: 0
  slug: mediaconvert-api-eac3-surround-mode
- name: EmbeddedConvert608To708
  property_count: 0
  slug: mediaconvert-api-embedded-convert608-to708
- name: EmbeddedDestinationSettings
  property_count: 2
  slug: mediaconvert-api-embedded-destination-settings
- name: EmbeddedSourceSettings
  property_count: 4
  slug: mediaconvert-api-embedded-source-settings
- name: EmbeddedTerminateCaptions
  property_count: 0
  slug: mediaconvert-api-embedded-terminate-captions
- name: EmbeddedTimecodeOverride
  property_count: 0
  slug: mediaconvert-api-embedded-timecode-override
- name: Endpoint
  property_count: 1
  slug: mediaconvert-api-endpoint
- name: EsamManifestConfirmConditionNotification
  property_count: 1
  slug: mediaconvert-api-esam-manifest-confirm-condition-notification
- name: EsamSettings
  property_count: 3
  slug: mediaconvert-api-esam-settings
- name: EsamSignalProcessingNotification
  property_count: 1
  slug: mediaconvert-api-esam-signal-processing-notification
- name: ExtendedDataServices
  property_count: 2
  slug: mediaconvert-api-extended-data-services
- name: F4vMoovPlacement
  property_count: 0
  slug: mediaconvert-api-f4v-moov-placement
- name: F4vSettings
  property_count: 1
  slug: mediaconvert-api-f4v-settings
- name: FileGroupSettings
  property_count: 2
  slug: mediaconvert-api-file-group-settings
- name: FileSourceConvert608To708
  property_count: 0
  slug: mediaconvert-api-file-source-convert608-to708
- name: FileSourceSettings
  property_count: 5
  slug: mediaconvert-api-file-source-settings
- name: FileSourceTimeDeltaUnits
  property_count: 0
  slug: mediaconvert-api-file-source-time-delta-units
- name: FontScript
  property_count: 0
  slug: mediaconvert-api-font-script
- name: ForceIncludeRenditionSize
  property_count: 2
  slug: mediaconvert-api-force-include-rendition-size
- name: FrameCaptureSettings
  property_count: 4
  slug: mediaconvert-api-frame-capture-settings
- name: GetJobRequest
  property_count: 0
  slug: mediaconvert-api-get-job-request
- name: GetJobResponse
  property_count: 1
  slug: mediaconvert-api-get-job-response
- name: GetJobTemplateRequest
  property_count: 0
  slug: mediaconvert-api-get-job-template-request
- name: GetJobTemplateResponse
  property_count: 1
  slug: mediaconvert-api-get-job-template-response
- name: GetPolicyRequest
  property_count: 0
  slug: mediaconvert-api-get-policy-request
- name: GetPolicyResponse
  property_count: 1
  slug: mediaconvert-api-get-policy-response
- name: GetPresetRequest
  property_count: 0
  slug: mediaconvert-api-get-preset-request
- name: GetPresetResponse
  property_count: 1
  slug: mediaconvert-api-get-preset-response
- name: GetQueueRequest
  property_count: 0
  slug: mediaconvert-api-get-queue-request
- name: GetQueueResponse
  property_count: 1
  slug: mediaconvert-api-get-queue-response
- name: H264AdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h264-adaptive-quantization
- name: H264CodecLevel
  property_count: 0
  slug: mediaconvert-api-h264-codec-level
- name: H264CodecProfile
  property_count: 0
  slug: mediaconvert-api-h264-codec-profile
- name: H264DynamicSubGop
  property_count: 0
  slug: mediaconvert-api-h264-dynamic-sub-gop
- name: H264EntropyEncoding
  property_count: 0
  slug: mediaconvert-api-h264-entropy-encoding
- name: H264FieldEncoding
  property_count: 0
  slug: mediaconvert-api-h264-field-encoding
- name: H264FlickerAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h264-flicker-adaptive-quantization
- name: H264FramerateControl
  property_count: 0
  slug: mediaconvert-api-h264-framerate-control
- name: H264FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-h264-framerate-conversion-algorithm
- name: H264GopBReference
  property_count: 0
  slug: mediaconvert-api-h264-gop-b-reference
- name: H264GopSizeUnits
  property_count: 0
  slug: mediaconvert-api-h264-gop-size-units
- name: H264InterlaceMode
  property_count: 0
  slug: mediaconvert-api-h264-interlace-mode
- name: H264ParControl
  property_count: 0
  slug: mediaconvert-api-h264-par-control
- name: H264QualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-h264-quality-tuning-level
- name: H264QvbrSettings
  property_count: 3
  slug: mediaconvert-api-h264-qvbr-settings
- name: H264RateControlMode
  property_count: 0
  slug: mediaconvert-api-h264-rate-control-mode
- name: H264RepeatPps
  property_count: 0
  slug: mediaconvert-api-h264-repeat-pps
- name: H264ScanTypeConversionMode
  property_count: 0
  slug: mediaconvert-api-h264-scan-type-conversion-mode
- name: H264SceneChangeDetect
  property_count: 0
  slug: mediaconvert-api-h264-scene-change-detect
- name: H264Settings
  property_count: 42
  slug: mediaconvert-api-h264-settings
- name: H264SlowPal
  property_count: 0
  slug: mediaconvert-api-h264-slow-pal
- name: H264SpatialAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h264-spatial-adaptive-quantization
- name: H264Syntax
  property_count: 0
  slug: mediaconvert-api-h264-syntax
- name: H264Telecine
  property_count: 0
  slug: mediaconvert-api-h264-telecine
- name: H264TemporalAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h264-temporal-adaptive-quantization
- name: H264UnregisteredSeiTimecode
  property_count: 0
  slug: mediaconvert-api-h264-unregistered-sei-timecode
- name: H265AdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h265-adaptive-quantization
- name: H265AlternateTransferFunctionSei
  property_count: 0
  slug: mediaconvert-api-h265-alternate-transfer-function-sei
- name: H265CodecLevel
  property_count: 0
  slug: mediaconvert-api-h265-codec-level
- name: H265CodecProfile
  property_count: 0
  slug: mediaconvert-api-h265-codec-profile
- name: H265DynamicSubGop
  property_count: 0
  slug: mediaconvert-api-h265-dynamic-sub-gop
- name: H265FlickerAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h265-flicker-adaptive-quantization
- name: H265FramerateControl
  property_count: 0
  slug: mediaconvert-api-h265-framerate-control
- name: H265FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-h265-framerate-conversion-algorithm
- name: H265GopBReference
  property_count: 0
  slug: mediaconvert-api-h265-gop-b-reference
- name: H265GopSizeUnits
  property_count: 0
  slug: mediaconvert-api-h265-gop-size-units
- name: H265InterlaceMode
  property_count: 0
  slug: mediaconvert-api-h265-interlace-mode
- name: H265ParControl
  property_count: 0
  slug: mediaconvert-api-h265-par-control
- name: H265QualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-h265-quality-tuning-level
- name: H265QvbrSettings
  property_count: 3
  slug: mediaconvert-api-h265-qvbr-settings
- name: H265RateControlMode
  property_count: 0
  slug: mediaconvert-api-h265-rate-control-mode
- name: H265SampleAdaptiveOffsetFilterMode
  property_count: 0
  slug: mediaconvert-api-h265-sample-adaptive-offset-filter-mode
- name: H265ScanTypeConversionMode
  property_count: 0
  slug: mediaconvert-api-h265-scan-type-conversion-mode
- name: H265SceneChangeDetect
  property_count: 0
  slug: mediaconvert-api-h265-scene-change-detect
- name: H265Settings
  property_count: 41
  slug: mediaconvert-api-h265-settings
- name: H265SlowPal
  property_count: 0
  slug: mediaconvert-api-h265-slow-pal
- name: H265SpatialAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h265-spatial-adaptive-quantization
- name: H265Telecine
  property_count: 0
  slug: mediaconvert-api-h265-telecine
- name: H265TemporalAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-h265-temporal-adaptive-quantization
- name: H265TemporalIds
  property_count: 0
  slug: mediaconvert-api-h265-temporal-ids
- name: H265Tiles
  property_count: 0
  slug: mediaconvert-api-h265-tiles
- name: H265UnregisteredSeiTimecode
  property_count: 0
  slug: mediaconvert-api-h265-unregistered-sei-timecode
- name: H265WriteMp4PackagingType
  property_count: 0
  slug: mediaconvert-api-h265-write-mp4-packaging-type
- name: HDRToSDRToneMapper
  property_count: 0
  slug: mediaconvert-api-hdr-to-sdr-tone-mapper
- name: Hdr10Metadata
  property_count: 12
  slug: mediaconvert-api-hdr10-metadata
- name: Hdr10Plus
  property_count: 2
  slug: mediaconvert-api-hdr10-plus
- name: HlsAdMarkers
  property_count: 0
  slug: mediaconvert-api-hls-ad-markers
- name: HlsAdditionalManifest
  property_count: 2
  slug: mediaconvert-api-hls-additional-manifest
- name: HlsAudioOnlyContainer
  property_count: 0
  slug: mediaconvert-api-hls-audio-only-container
- name: HlsAudioOnlyHeader
  property_count: 0
  slug: mediaconvert-api-hls-audio-only-header
- name: HlsAudioTrackType
  property_count: 0
  slug: mediaconvert-api-hls-audio-track-type
- name: HlsCaptionLanguageMapping
  property_count: 4
  slug: mediaconvert-api-hls-caption-language-mapping
- name: HlsCaptionLanguageSetting
  property_count: 0
  slug: mediaconvert-api-hls-caption-language-setting
- name: HlsCaptionSegmentLengthControl
  property_count: 0
  slug: mediaconvert-api-hls-caption-segment-length-control
- name: HlsClientCache
  property_count: 0
  slug: mediaconvert-api-hls-client-cache
- name: HlsCodecSpecification
  property_count: 0
  slug: mediaconvert-api-hls-codec-specification
- name: HlsDescriptiveVideoServiceFlag
  property_count: 0
  slug: mediaconvert-api-hls-descriptive-video-service-flag
- name: HlsDirectoryStructure
  property_count: 0
  slug: mediaconvert-api-hls-directory-structure
- name: HlsEncryptionSettings
  property_count: 7
  slug: mediaconvert-api-hls-encryption-settings
- name: HlsEncryptionType
  property_count: 0
  slug: mediaconvert-api-hls-encryption-type
- name: HlsGroupSettings
  property_count: 31
  slug: mediaconvert-api-hls-group-settings
- name: HlsIFrameOnlyManifest
  property_count: 0
  slug: mediaconvert-api-hls-i-frame-only-manifest
- name: HlsImageBasedTrickPlay
  property_count: 0
  slug: mediaconvert-api-hls-image-based-trick-play
- name: HlsImageBasedTrickPlaySettings
  property_count: 6
  slug: mediaconvert-api-hls-image-based-trick-play-settings
- name: HlsInitializationVectorInManifest
  property_count: 0
  slug: mediaconvert-api-hls-initialization-vector-in-manifest
- name: HlsIntervalCadence
  property_count: 0
  slug: mediaconvert-api-hls-interval-cadence
- name: HlsKeyProviderType
  property_count: 0
  slug: mediaconvert-api-hls-key-provider-type
- name: HlsManifestCompression
  property_count: 0
  slug: mediaconvert-api-hls-manifest-compression
- name: HlsManifestDurationFormat
  property_count: 0
  slug: mediaconvert-api-hls-manifest-duration-format
- name: HlsOfflineEncrypted
  property_count: 0
  slug: mediaconvert-api-hls-offline-encrypted
- name: HlsOutputSelection
  property_count: 0
  slug: mediaconvert-api-hls-output-selection
- name: HlsProgramDateTime
  property_count: 0
  slug: mediaconvert-api-hls-program-date-time
- name: HlsRenditionGroupSettings
  property_count: 3
  slug: mediaconvert-api-hls-rendition-group-settings
- name: HlsSegmentControl
  property_count: 0
  slug: mediaconvert-api-hls-segment-control
- name: HlsSegmentLengthControl
  property_count: 0
  slug: mediaconvert-api-hls-segment-length-control
- name: HlsSettings
  property_count: 7
  slug: mediaconvert-api-hls-settings
- name: HlsStreamInfResolution
  property_count: 0
  slug: mediaconvert-api-hls-stream-inf-resolution
- name: HlsTargetDurationCompatibilityMode
  property_count: 0
  slug: mediaconvert-api-hls-target-duration-compatibility-mode
- name: HlsTimedMetadataId3Frame
  property_count: 0
  slug: mediaconvert-api-hls-timed-metadata-id3-frame
- name: HopDestination
  property_count: 3
  slug: mediaconvert-api-hop-destination
- name: Id3Insertion
  property_count: 2
  slug: mediaconvert-api-id3-insertion
- name: ImageInserter
  property_count: 2
  slug: mediaconvert-api-image-inserter
- name: ImscAccessibilitySubs
  property_count: 0
  slug: mediaconvert-api-imsc-accessibility-subs
- name: ImscDestinationSettings
  property_count: 2
  slug: mediaconvert-api-imsc-destination-settings
- name: ImscStylePassthrough
  property_count: 0
  slug: mediaconvert-api-imsc-style-passthrough
- name: InputClipping
  property_count: 2
  slug: mediaconvert-api-input-clipping
- name: InputDeblockFilter
  property_count: 0
  slug: mediaconvert-api-input-deblock-filter
- name: InputDecryptionSettings
  property_count: 4
  slug: mediaconvert-api-input-decryption-settings
- name: InputDenoiseFilter
  property_count: 0
  slug: mediaconvert-api-input-denoise-filter
- name: InputFilterEnable
  property_count: 0
  slug: mediaconvert-api-input-filter-enable
- name: InputPolicy
  property_count: 0
  slug: mediaconvert-api-input-policy
- name: InputPsiControl
  property_count: 0
  slug: mediaconvert-api-input-psi-control
- name: InputRotate
  property_count: 0
  slug: mediaconvert-api-input-rotate
- name: InputSampleRange
  property_count: 0
  slug: mediaconvert-api-input-sample-range
- name: InputScanType
  property_count: 0
  slug: mediaconvert-api-input-scan-type
- name: Input
  property_count: 22
  slug: mediaconvert-api-input
- name: InputTemplate
  property_count: 18
  slug: mediaconvert-api-input-template
- name: InputTimecodeSource
  property_count: 0
  slug: mediaconvert-api-input-timecode-source
- name: InputVideoGenerator
  property_count: 1
  slug: mediaconvert-api-input-video-generator
- name: InsertableImage
  property_count: 11
  slug: mediaconvert-api-insertable-image
- name: JobMessages
  property_count: 2
  slug: mediaconvert-api-job-messages
- name: JobPhase
  property_count: 0
  slug: mediaconvert-api-job-phase
- name: Job
  property_count: 27
  slug: mediaconvert-api-job
- name: JobSettings
  property_count: 12
  slug: mediaconvert-api-job-settings
- name: JobStatus
  property_count: 0
  slug: mediaconvert-api-job-status
- name: JobTemplateListBy
  property_count: 0
  slug: mediaconvert-api-job-template-list-by
- name: JobTemplate
  property_count: 13
  slug: mediaconvert-api-job-template
- name: JobTemplateSettings
  property_count: 12
  slug: mediaconvert-api-job-template-settings
- name: KantarWatermarkSettings
  property_count: 13
  slug: mediaconvert-api-kantar-watermark-settings
- name: LanguageCode
  property_count: 0
  slug: mediaconvert-api-language-code
- name: ListJobTemplatesRequest
  property_count: 0
  slug: mediaconvert-api-list-job-templates-request
- name: ListJobTemplatesResponse
  property_count: 2
  slug: mediaconvert-api-list-job-templates-response
- name: ListJobsRequest
  property_count: 0
  slug: mediaconvert-api-list-jobs-request
- name: ListJobsResponse
  property_count: 2
  slug: mediaconvert-api-list-jobs-response
- name: ListPresetsRequest
  property_count: 0
  slug: mediaconvert-api-list-presets-request
- name: ListPresetsResponse
  property_count: 2
  slug: mediaconvert-api-list-presets-response
- name: ListQueuesRequest
  property_count: 0
  slug: mediaconvert-api-list-queues-request
- name: ListQueuesResponse
  property_count: 2
  slug: mediaconvert-api-list-queues-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: mediaconvert-api-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: mediaconvert-api-list-tags-for-resource-response
- name: M2tsAudioBufferModel
  property_count: 0
  slug: mediaconvert-api-m2ts-audio-buffer-model
- name: M2tsAudioDuration
  property_count: 0
  slug: mediaconvert-api-m2ts-audio-duration
- name: M2tsBufferModel
  property_count: 0
  slug: mediaconvert-api-m2ts-buffer-model
- name: M2tsDataPtsControl
  property_count: 0
  slug: mediaconvert-api-m2ts-data-pts-control
- name: M2tsEbpAudioInterval
  property_count: 0
  slug: mediaconvert-api-m2ts-ebp-audio-interval
- name: M2tsEbpPlacement
  property_count: 0
  slug: mediaconvert-api-m2ts-ebp-placement
- name: M2tsEsRateInPes
  property_count: 0
  slug: mediaconvert-api-m2ts-es-rate-in-pes
- name: M2tsForceTsVideoEbpOrder
  property_count: 0
  slug: mediaconvert-api-m2ts-force-ts-video-ebp-order
- name: M2tsKlvMetadata
  property_count: 0
  slug: mediaconvert-api-m2ts-klv-metadata
- name: M2tsNielsenId3
  property_count: 0
  slug: mediaconvert-api-m2ts-nielsen-id3
- name: M2tsPcrControl
  property_count: 0
  slug: mediaconvert-api-m2ts-pcr-control
- name: M2tsRateMode
  property_count: 0
  slug: mediaconvert-api-m2ts-rate-mode
- name: M2tsScte35Esam
  property_count: 1
  slug: mediaconvert-api-m2ts-scte35-esam
- name: M2tsScte35Source
  property_count: 0
  slug: mediaconvert-api-m2ts-scte35-source
- name: M2tsSegmentationMarkers
  property_count: 0
  slug: mediaconvert-api-m2ts-segmentation-markers
- name: M2tsSegmentationStyle
  property_count: 0
  slug: mediaconvert-api-m2ts-segmentation-style
- name: M2tsSettings
  property_count: 39
  slug: mediaconvert-api-m2ts-settings
- name: M3u8AudioDuration
  property_count: 0
  slug: mediaconvert-api-m3u8-audio-duration
- name: M3u8DataPtsControl
  property_count: 0
  slug: mediaconvert-api-m3u8-data-pts-control
- name: M3u8NielsenId3
  property_count: 0
  slug: mediaconvert-api-m3u8-nielsen-id3
- name: M3u8PcrControl
  property_count: 0
  slug: mediaconvert-api-m3u8-pcr-control
- name: M3u8Scte35Source
  property_count: 0
  slug: mediaconvert-api-m3u8-scte35-source
- name: M3u8Settings
  property_count: 19
  slug: mediaconvert-api-m3u8-settings
- name: MinBottomRenditionSize
  property_count: 2
  slug: mediaconvert-api-min-bottom-rendition-size
- name: MinTopRenditionSize
  property_count: 2
  slug: mediaconvert-api-min-top-rendition-size
- name: MotionImageInserter
  property_count: 6
  slug: mediaconvert-api-motion-image-inserter
- name: MotionImageInsertionFramerate
  property_count: 2
  slug: mediaconvert-api-motion-image-insertion-framerate
- name: MotionImageInsertionMode
  property_count: 0
  slug: mediaconvert-api-motion-image-insertion-mode
- name: MotionImageInsertionOffset
  property_count: 2
  slug: mediaconvert-api-motion-image-insertion-offset
- name: MotionImagePlayback
  property_count: 0
  slug: mediaconvert-api-motion-image-playback
- name: MovClapAtom
  property_count: 0
  slug: mediaconvert-api-mov-clap-atom
- name: MovCslgAtom
  property_count: 0
  slug: mediaconvert-api-mov-cslg-atom
- name: MovMpeg2FourCCControl
  property_count: 0
  slug: mediaconvert-api-mov-mpeg2-four-cc-control
- name: MovPaddingControl
  property_count: 0
  slug: mediaconvert-api-mov-padding-control
- name: MovReference
  property_count: 0
  slug: mediaconvert-api-mov-reference
- name: MovSettings
  property_count: 5
  slug: mediaconvert-api-mov-settings
- name: Mp2Settings
  property_count: 3
  slug: mediaconvert-api-mp2-settings
- name: Mp3RateControlMode
  property_count: 0
  slug: mediaconvert-api-mp3-rate-control-mode
- name: Mp3Settings
  property_count: 5
  slug: mediaconvert-api-mp3-settings
- name: Mp4CslgAtom
  property_count: 0
  slug: mediaconvert-api-mp4-cslg-atom
- name: Mp4FreeSpaceBox
  property_count: 0
  slug: mediaconvert-api-mp4-free-space-box
- name: Mp4MoovPlacement
  property_count: 0
  slug: mediaconvert-api-mp4-moov-placement
- name: Mp4Settings
  property_count: 6
  slug: mediaconvert-api-mp4-settings
- name: MpdAccessibilityCaptionHints
  property_count: 0
  slug: mediaconvert-api-mpd-accessibility-caption-hints
- name: MpdAudioDuration
  property_count: 0
  slug: mediaconvert-api-mpd-audio-duration
- name: MpdCaptionContainerType
  property_count: 0
  slug: mediaconvert-api-mpd-caption-container-type
- name: MpdKlvMetadata
  property_count: 0
  slug: mediaconvert-api-mpd-klv-metadata
- name: MpdManifestMetadataSignaling
  property_count: 0
  slug: mediaconvert-api-mpd-manifest-metadata-signaling
- name: MpdScte35Esam
  property_count: 0
  slug: mediaconvert-api-mpd-scte35-esam
- name: MpdScte35Source
  property_count: 0
  slug: mediaconvert-api-mpd-scte35-source
- name: MpdSettings
  property_count: 11
  slug: mediaconvert-api-mpd-settings
- name: MpdTimedMetadataBoxVersion
  property_count: 0
  slug: mediaconvert-api-mpd-timed-metadata-box-version
- name: MpdTimedMetadata
  property_count: 0
  slug: mediaconvert-api-mpd-timed-metadata
- name: Mpeg2AdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-mpeg2-adaptive-quantization
- name: Mpeg2CodecLevel
  property_count: 0
  slug: mediaconvert-api-mpeg2-codec-level
- name: Mpeg2CodecProfile
  property_count: 0
  slug: mediaconvert-api-mpeg2-codec-profile
- name: Mpeg2DynamicSubGop
  property_count: 0
  slug: mediaconvert-api-mpeg2-dynamic-sub-gop
- name: Mpeg2FramerateControl
  property_count: 0
  slug: mediaconvert-api-mpeg2-framerate-control
- name: Mpeg2FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-mpeg2-framerate-conversion-algorithm
- name: Mpeg2GopSizeUnits
  property_count: 0
  slug: mediaconvert-api-mpeg2-gop-size-units
- name: Mpeg2InterlaceMode
  property_count: 0
  slug: mediaconvert-api-mpeg2-interlace-mode
- name: Mpeg2IntraDcPrecision
  property_count: 0
  slug: mediaconvert-api-mpeg2-intra-dc-precision
- name: Mpeg2ParControl
  property_count: 0
  slug: mediaconvert-api-mpeg2-par-control
- name: Mpeg2QualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-mpeg2-quality-tuning-level
- name: Mpeg2RateControlMode
  property_count: 0
  slug: mediaconvert-api-mpeg2-rate-control-mode
- name: Mpeg2ScanTypeConversionMode
  property_count: 0
  slug: mediaconvert-api-mpeg2-scan-type-conversion-mode
- name: Mpeg2SceneChangeDetect
  property_count: 0
  slug: mediaconvert-api-mpeg2-scene-change-detect
- name: Mpeg2Settings
  property_count: 33
  slug: mediaconvert-api-mpeg2-settings
- name: Mpeg2SlowPal
  property_count: 0
  slug: mediaconvert-api-mpeg2-slow-pal
- name: Mpeg2SpatialAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-mpeg2-spatial-adaptive-quantization
- name: Mpeg2Syntax
  property_count: 0
  slug: mediaconvert-api-mpeg2-syntax
- name: Mpeg2Telecine
  property_count: 0
  slug: mediaconvert-api-mpeg2-telecine
- name: Mpeg2TemporalAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-mpeg2-temporal-adaptive-quantization
- name: MsSmoothAdditionalManifest
  property_count: 2
  slug: mediaconvert-api-ms-smooth-additional-manifest
- name: MsSmoothAudioDeduplication
  property_count: 0
  slug: mediaconvert-api-ms-smooth-audio-deduplication
- name: MsSmoothEncryptionSettings
  property_count: 1
  slug: mediaconvert-api-ms-smooth-encryption-settings
- name: MsSmoothFragmentLengthControl
  property_count: 0
  slug: mediaconvert-api-ms-smooth-fragment-length-control
- name: MsSmoothGroupSettings
  property_count: 8
  slug: mediaconvert-api-ms-smooth-group-settings
- name: MsSmoothManifestEncoding
  property_count: 0
  slug: mediaconvert-api-ms-smooth-manifest-encoding
- name: MxfAfdSignaling
  property_count: 0
  slug: mediaconvert-api-mxf-afd-signaling
- name: MxfProfile
  property_count: 0
  slug: mediaconvert-api-mxf-profile
- name: MxfSettings
  property_count: 3
  slug: mediaconvert-api-mxf-settings
- name: MxfXavcDurationMode
  property_count: 0
  slug: mediaconvert-api-mxf-xavc-duration-mode
- name: MxfXavcProfileSettings
  property_count: 2
  slug: mediaconvert-api-mxf-xavc-profile-settings
- name: NexGuardFileMarkerSettings
  property_count: 4
  slug: mediaconvert-api-nex-guard-file-marker-settings
- name: NielsenActiveWatermarkProcessType
  property_count: 0
  slug: mediaconvert-api-nielsen-active-watermark-process-type
- name: NielsenConfiguration
  property_count: 2
  slug: mediaconvert-api-nielsen-configuration
- name: NielsenNonLinearWatermarkSettings
  property_count: 11
  slug: mediaconvert-api-nielsen-non-linear-watermark-settings
- name: NielsenSourceWatermarkStatusType
  property_count: 0
  slug: mediaconvert-api-nielsen-source-watermark-status-type
- name: NielsenUniqueTicPerAudioTrackType
  property_count: 0
  slug: mediaconvert-api-nielsen-unique-tic-per-audio-track-type
- name: NoiseFilterPostTemporalSharpening
  property_count: 0
  slug: mediaconvert-api-noise-filter-post-temporal-sharpening
- name: NoiseFilterPostTemporalSharpeningStrength
  property_count: 0
  slug: mediaconvert-api-noise-filter-post-temporal-sharpening-strength
- name: NoiseReducerFilter
  property_count: 0
  slug: mediaconvert-api-noise-reducer-filter
- name: NoiseReducerFilterSettings
  property_count: 1
  slug: mediaconvert-api-noise-reducer-filter-settings
- name: NoiseReducer
  property_count: 4
  slug: mediaconvert-api-noise-reducer
- name: NoiseReducerSpatialFilterSettings
  property_count: 3
  slug: mediaconvert-api-noise-reducer-spatial-filter-settings
- name: NoiseReducerTemporalFilterSettings
  property_count: 5
  slug: mediaconvert-api-noise-reducer-temporal-filter-settings
- name: OpusSettings
  property_count: 3
  slug: mediaconvert-api-opus-settings
- name: Order
  property_count: 0
  slug: mediaconvert-api-order
- name: OutputChannelMapping
  property_count: 2
  slug: mediaconvert-api-output-channel-mapping
- name: OutputDetail
  property_count: 2
  slug: mediaconvert-api-output-detail
- name: OutputGroupDetail
  property_count: 1
  slug: mediaconvert-api-output-group-detail
- name: OutputGroup
  property_count: 5
  slug: mediaconvert-api-output-group
- name: OutputGroupSettings
  property_count: 6
  slug: mediaconvert-api-output-group-settings
- name: OutputGroupType
  property_count: 0
  slug: mediaconvert-api-output-group-type
- name: Output
  property_count: 8
  slug: mediaconvert-api-output
- name: OutputSdt
  property_count: 0
  slug: mediaconvert-api-output-sdt
- name: OutputSettings
  property_count: 1
  slug: mediaconvert-api-output-settings
- name: PadVideo
  property_count: 0
  slug: mediaconvert-api-pad-video
- name: PartnerWatermarking
  property_count: 1
  slug: mediaconvert-api-partner-watermarking
- name: Policy
  property_count: 3
  slug: mediaconvert-api-policy
- name: PresetListBy
  property_count: 0
  slug: mediaconvert-api-preset-list-by
- name: Preset
  property_count: 8
  slug: mediaconvert-api-preset
- name: PresetSettings
  property_count: 4
  slug: mediaconvert-api-preset-settings
- name: PricingPlan
  property_count: 0
  slug: mediaconvert-api-pricing-plan
- name: ProresChromaSampling
  property_count: 0
  slug: mediaconvert-api-prores-chroma-sampling
- name: ProresCodecProfile
  property_count: 0
  slug: mediaconvert-api-prores-codec-profile
- name: ProresFramerateControl
  property_count: 0
  slug: mediaconvert-api-prores-framerate-control
- name: ProresFramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-prores-framerate-conversion-algorithm
- name: ProresInterlaceMode
  property_count: 0
  slug: mediaconvert-api-prores-interlace-mode
- name: ProresParControl
  property_count: 0
  slug: mediaconvert-api-prores-par-control
- name: ProresScanTypeConversionMode
  property_count: 0
  slug: mediaconvert-api-prores-scan-type-conversion-mode
- name: ProresSettings
  property_count: 13
  slug: mediaconvert-api-prores-settings
- name: ProresSlowPal
  property_count: 0
  slug: mediaconvert-api-prores-slow-pal
- name: ProresTelecine
  property_count: 0
  slug: mediaconvert-api-prores-telecine
- name: PutPolicyRequest
  property_count: 1
  slug: mediaconvert-api-put-policy-request
- name: PutPolicyResponse
  property_count: 1
  slug: mediaconvert-api-put-policy-response
- name: QueueListBy
  property_count: 0
  slug: mediaconvert-api-queue-list-by
- name: Queue
  property_count: 11
  slug: mediaconvert-api-queue
- name: QueueStatus
  property_count: 0
  slug: mediaconvert-api-queue-status
- name: QueueTransition
  property_count: 3
  slug: mediaconvert-api-queue-transition
- name: Rectangle
  property_count: 4
  slug: mediaconvert-api-rectangle
- name: RemixSettings
  property_count: 3
  slug: mediaconvert-api-remix-settings
- name: RenewalType
  property_count: 0
  slug: mediaconvert-api-renewal-type
- name: RequiredFlag
  property_count: 0
  slug: mediaconvert-api-required-flag
- name: ReservationPlan
  property_count: 6
  slug: mediaconvert-api-reservation-plan
- name: ReservationPlanSettings
  property_count: 3
  slug: mediaconvert-api-reservation-plan-settings
- name: ReservationPlanStatus
  property_count: 0
  slug: mediaconvert-api-reservation-plan-status
- name: ResourceTags
  property_count: 2
  slug: mediaconvert-api-resource-tags
- name: RespondToAfd
  property_count: 0
  slug: mediaconvert-api-respond-to-afd
- name: RuleType
  property_count: 0
  slug: mediaconvert-api-rule-type
- name: S3DestinationAccessControl
  property_count: 1
  slug: mediaconvert-api-s3-destination-access-control
- name: S3DestinationSettings
  property_count: 2
  slug: mediaconvert-api-s3-destination-settings
- name: S3EncryptionSettings
  property_count: 3
  slug: mediaconvert-api-s3-encryption-settings
- name: S3ObjectCannedAcl
  property_count: 0
  slug: mediaconvert-api-s3-object-canned-acl
- name: S3ServerSideEncryptionType
  property_count: 0
  slug: mediaconvert-api-s3-server-side-encryption-type
- name: SampleRangeConversion
  property_count: 0
  slug: mediaconvert-api-sample-range-conversion
- name: ScalingBehavior
  property_count: 0
  slug: mediaconvert-api-scaling-behavior
- name: SccDestinationFramerate
  property_count: 0
  slug: mediaconvert-api-scc-destination-framerate
- name: SccDestinationSettings
  property_count: 1
  slug: mediaconvert-api-scc-destination-settings
- name: SimulateReservedQueue
  property_count: 0
  slug: mediaconvert-api-simulate-reserved-queue
- name: SpekeKeyProviderCmaf
  property_count: 5
  slug: mediaconvert-api-speke-key-provider-cmaf
- name: SpekeKeyProvider
  property_count: 4
  slug: mediaconvert-api-speke-key-provider
- name: SrtDestinationSettings
  property_count: 1
  slug: mediaconvert-api-srt-destination-settings
- name: SrtStylePassthrough
  property_count: 0
  slug: mediaconvert-api-srt-style-passthrough
- name: StaticKeyProvider
  property_count: 4
  slug: mediaconvert-api-static-key-provider
- name: StatusUpdateInterval
  property_count: 0
  slug: mediaconvert-api-status-update-interval
- name: TagResourceRequest
  property_count: 2
  slug: mediaconvert-api-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: mediaconvert-api-tag-resource-response
- name: TeletextDestinationSettings
  property_count: 2
  slug: mediaconvert-api-teletext-destination-settings
- name: TeletextPageType
  property_count: 0
  slug: mediaconvert-api-teletext-page-type
- name: TeletextSourceSettings
  property_count: 1
  slug: mediaconvert-api-teletext-source-settings
- name: TimecodeBurninPosition
  property_count: 0
  slug: mediaconvert-api-timecode-burnin-position
- name: TimecodeBurnin
  property_count: 3
  slug: mediaconvert-api-timecode-burnin
- name: TimecodeConfig
  property_count: 4
  slug: mediaconvert-api-timecode-config
- name: TimecodeSource
  property_count: 0
  slug: mediaconvert-api-timecode-source
- name: TimedMetadataInsertion
  property_count: 1
  slug: mediaconvert-api-timed-metadata-insertion
- name: TimedMetadata
  property_count: 0
  slug: mediaconvert-api-timed-metadata
- name: Timing
  property_count: 3
  slug: mediaconvert-api-timing
- name: TrackSourceSettings
  property_count: 1
  slug: mediaconvert-api-track-source-settings
- name: TtmlDestinationSettings
  property_count: 1
  slug: mediaconvert-api-ttml-destination-settings
- name: TtmlStylePassthrough
  property_count: 0
  slug: mediaconvert-api-ttml-style-passthrough
- name: Type
  property_count: 0
  slug: mediaconvert-api-type
- name: UntagResourceRequest
  property_count: 1
  slug: mediaconvert-api-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: mediaconvert-api-untag-resource-response
- name: UpdateJobTemplateRequest
  property_count: 8
  slug: mediaconvert-api-update-job-template-request
- name: UpdateJobTemplateResponse
  property_count: 1
  slug: mediaconvert-api-update-job-template-response
- name: UpdatePresetRequest
  property_count: 3
  slug: mediaconvert-api-update-preset-request
- name: UpdatePresetResponse
  property_count: 1
  slug: mediaconvert-api-update-preset-response
- name: UpdateQueueRequest
  property_count: 3
  slug: mediaconvert-api-update-queue-request
- name: UpdateQueueResponse
  property_count: 1
  slug: mediaconvert-api-update-queue-response
- name: Vc3Class
  property_count: 0
  slug: mediaconvert-api-vc3-class
- name: Vc3FramerateControl
  property_count: 0
  slug: mediaconvert-api-vc3-framerate-control
- name: Vc3FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-vc3-framerate-conversion-algorithm
- name: Vc3InterlaceMode
  property_count: 0
  slug: mediaconvert-api-vc3-interlace-mode
- name: Vc3ScanTypeConversionMode
  property_count: 0
  slug: mediaconvert-api-vc3-scan-type-conversion-mode
- name: Vc3Settings
  property_count: 9
  slug: mediaconvert-api-vc3-settings
- name: Vc3SlowPal
  property_count: 0
  slug: mediaconvert-api-vc3-slow-pal
- name: Vc3Telecine
  property_count: 0
  slug: mediaconvert-api-vc3-telecine
- name: VchipAction
  property_count: 0
  slug: mediaconvert-api-vchip-action
- name: VideoCodec
  property_count: 0
  slug: mediaconvert-api-video-codec
- name: VideoCodecSettings
  property_count: 12
  slug: mediaconvert-api-video-codec-settings
- name: VideoDescription
  property_count: 15
  slug: mediaconvert-api-video-description
- name: VideoDetail
  property_count: 2
  slug: mediaconvert-api-video-detail
- name: VideoPreprocessor
  property_count: 8
  slug: mediaconvert-api-video-preprocessor
- name: VideoSelector
  property_count: 10
  slug: mediaconvert-api-video-selector
- name: VideoTimecodeInsertion
  property_count: 0
  slug: mediaconvert-api-video-timecode-insertion
- name: VorbisSettings
  property_count: 3
  slug: mediaconvert-api-vorbis-settings
- name: Vp8FramerateControl
  property_count: 0
  slug: mediaconvert-api-vp8-framerate-control
- name: Vp8FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-vp8-framerate-conversion-algorithm
- name: Vp8ParControl
  property_count: 0
  slug: mediaconvert-api-vp8-par-control
- name: Vp8QualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-vp8-quality-tuning-level
- name: Vp8RateControlMode
  property_count: 0
  slug: mediaconvert-api-vp8-rate-control-mode
- name: Vp8Settings
  property_count: 13
  slug: mediaconvert-api-vp8-settings
- name: Vp9FramerateControl
  property_count: 0
  slug: mediaconvert-api-vp9-framerate-control
- name: Vp9FramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-vp9-framerate-conversion-algorithm
- name: Vp9ParControl
  property_count: 0
  slug: mediaconvert-api-vp9-par-control
- name: Vp9QualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-vp9-quality-tuning-level
- name: Vp9RateControlMode
  property_count: 0
  slug: mediaconvert-api-vp9-rate-control-mode
- name: Vp9Settings
  property_count: 13
  slug: mediaconvert-api-vp9-settings
- name: WarningGroup
  property_count: 2
  slug: mediaconvert-api-warning-group
- name: WatermarkingStrength
  property_count: 0
  slug: mediaconvert-api-watermarking-strength
- name: WavFormat
  property_count: 0
  slug: mediaconvert-api-wav-format
- name: WavSettings
  property_count: 4
  slug: mediaconvert-api-wav-settings
- name: WebvttAccessibilitySubs
  property_count: 0
  slug: mediaconvert-api-webvtt-accessibility-subs
- name: WebvttDestinationSettings
  property_count: 2
  slug: mediaconvert-api-webvtt-destination-settings
- name: WebvttHlsSourceSettings
  property_count: 3
  slug: mediaconvert-api-webvtt-hls-source-settings
- name: WebvttStylePassthrough
  property_count: 0
  slug: mediaconvert-api-webvtt-style-passthrough
- name: XavcAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-xavc-adaptive-quantization
- name: XavcEntropyEncoding
  property_count: 0
  slug: mediaconvert-api-xavc-entropy-encoding
- name: XavcFlickerAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-xavc-flicker-adaptive-quantization
- name: XavcFramerateControl
  property_count: 0
  slug: mediaconvert-api-xavc-framerate-control
- name: XavcFramerateConversionAlgorithm
  property_count: 0
  slug: mediaconvert-api-xavc-framerate-conversion-algorithm
- name: XavcGopBReference
  property_count: 0
  slug: mediaconvert-api-xavc-gop-b-reference
- name: XavcHdIntraCbgProfileClass
  property_count: 0
  slug: mediaconvert-api-xavc-hd-intra-cbg-profile-class
- name: XavcHdIntraCbgProfileSettings
  property_count: 1
  slug: mediaconvert-api-xavc-hd-intra-cbg-profile-settings
- name: XavcHdProfileBitrateClass
  property_count: 0
  slug: mediaconvert-api-xavc-hd-profile-bitrate-class
- name: XavcHdProfileQualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-xavc-hd-profile-quality-tuning-level
- name: XavcHdProfileSettings
  property_count: 9
  slug: mediaconvert-api-xavc-hd-profile-settings
- name: XavcHdProfileTelecine
  property_count: 0
  slug: mediaconvert-api-xavc-hd-profile-telecine
- name: XavcInterlaceMode
  property_count: 0
  slug: mediaconvert-api-xavc-interlace-mode
- name: XavcProfile
  property_count: 0
  slug: mediaconvert-api-xavc-profile
- name: XavcSettings
  property_count: 16
  slug: mediaconvert-api-xavc-settings
- name: XavcSlowPal
  property_count: 0
  slug: mediaconvert-api-xavc-slow-pal
- name: XavcSpatialAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-xavc-spatial-adaptive-quantization
- name: XavcTemporalAdaptiveQuantization
  property_count: 0
  slug: mediaconvert-api-xavc-temporal-adaptive-quantization
- name: Xavc4kIntraCbgProfileClass
  property_count: 0
  slug: mediaconvert-api-xavc4k-intra-cbg-profile-class
- name: Xavc4kIntraCbgProfileSettings
  property_count: 1
  slug: mediaconvert-api-xavc4k-intra-cbg-profile-settings
- name: Xavc4kIntraVbrProfileClass
  property_count: 0
  slug: mediaconvert-api-xavc4k-intra-vbr-profile-class
- name: Xavc4kIntraVbrProfileSettings
  property_count: 1
  slug: mediaconvert-api-xavc4k-intra-vbr-profile-settings
- name: Xavc4kProfileBitrateClass
  property_count: 0
  slug: mediaconvert-api-xavc4k-profile-bitrate-class
- name: Xavc4kProfileCodecProfile
  property_count: 0
  slug: mediaconvert-api-xavc4k-profile-codec-profile
- name: Xavc4kProfileQualityTuningLevel
  property_count: 0
  slug: mediaconvert-api-xavc4k-profile-quality-tuning-level
- name: Xavc4kProfileSettings
  property_count: 8
  slug: mediaconvert-api-xavc4k-profile-settings
json_structures:
- name: Mediaconvert Api Aac Audio Description Broadcaster Mix Structure
  property_count: 0
  slug: mediaconvert-api-aac-audio-description-broadcaster-mix-structure
- name: Mediaconvert Api Aac Codec Profile Structure
  property_count: 0
  slug: mediaconvert-api-aac-codec-profile-structure
- name: Mediaconvert Api Aac Coding Mode Structure
  property_count: 0
  slug: mediaconvert-api-aac-coding-mode-structure
- name: Mediaconvert Api Aac Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-aac-rate-control-mode-structure
- name: Mediaconvert Api Aac Raw Format Structure
  property_count: 0
  slug: mediaconvert-api-aac-raw-format-structure
- name: Mediaconvert Api Aac Settings Structure
  property_count: 9
  slug: mediaconvert-api-aac-settings-structure
- name: Mediaconvert Api Aac Specification Structure
  property_count: 0
  slug: mediaconvert-api-aac-specification-structure
- name: Mediaconvert Api Aac Vbr Quality Structure
  property_count: 0
  slug: mediaconvert-api-aac-vbr-quality-structure
- name: Mediaconvert Api Ac3 Bitstream Mode Structure
  property_count: 0
  slug: mediaconvert-api-ac3-bitstream-mode-structure
- name: Mediaconvert Api Ac3 Coding Mode Structure
  property_count: 0
  slug: mediaconvert-api-ac3-coding-mode-structure
- name: Mediaconvert Api Ac3 Dynamic Range Compression Line Structure
  property_count: 0
  slug: mediaconvert-api-ac3-dynamic-range-compression-line-structure
- name: Mediaconvert Api Ac3 Dynamic Range Compression Profile Structure
  property_count: 0
  slug: mediaconvert-api-ac3-dynamic-range-compression-profile-structure
- name: Mediaconvert Api Ac3 Dynamic Range Compression Rf Structure
  property_count: 0
  slug: mediaconvert-api-ac3-dynamic-range-compression-rf-structure
- name: Mediaconvert Api Ac3 Lfe Filter Structure
  property_count: 0
  slug: mediaconvert-api-ac3-lfe-filter-structure
- name: Mediaconvert Api Ac3 Metadata Control Structure
  property_count: 0
  slug: mediaconvert-api-ac3-metadata-control-structure
- name: Mediaconvert Api Ac3 Settings Structure
  property_count: 10
  slug: mediaconvert-api-ac3-settings-structure
- name: Mediaconvert Api Acceleration Mode Structure
  property_count: 0
  slug: mediaconvert-api-acceleration-mode-structure
- name: Mediaconvert Api Acceleration Settings Structure
  property_count: 1
  slug: mediaconvert-api-acceleration-settings-structure
- name: Mediaconvert Api Acceleration Status Structure
  property_count: 0
  slug: mediaconvert-api-acceleration-status-structure
- name: Mediaconvert Api Afd Signaling Structure
  property_count: 0
  slug: mediaconvert-api-afd-signaling-structure
- name: Mediaconvert Api Aiff Settings Structure
  property_count: 3
  slug: mediaconvert-api-aiff-settings-structure
- name: Mediaconvert Api Allowed Rendition Size Structure
  property_count: 3
  slug: mediaconvert-api-allowed-rendition-size-structure
- name: Mediaconvert Api Alpha Behavior Structure
  property_count: 0
  slug: mediaconvert-api-alpha-behavior-structure
- name: Mediaconvert Api Ancillary Convert608 To708 Structure
  property_count: 0
  slug: mediaconvert-api-ancillary-convert608-to708-structure
- name: Mediaconvert Api Ancillary Source Settings Structure
  property_count: 3
  slug: mediaconvert-api-ancillary-source-settings-structure
- name: Mediaconvert Api Ancillary Terminate Captions Structure
  property_count: 0
  slug: mediaconvert-api-ancillary-terminate-captions-structure
- name: Mediaconvert Api Anti Alias Structure
  property_count: 0
  slug: mediaconvert-api-anti-alias-structure
- name: Mediaconvert Api Associate Certificate Request Structure
  property_count: 1
  slug: mediaconvert-api-associate-certificate-request-structure
- name: Mediaconvert Api Associate Certificate Response Structure
  property_count: 0
  slug: mediaconvert-api-associate-certificate-response-structure
- name: Mediaconvert Api Audio Channel Tag Structure
  property_count: 0
  slug: mediaconvert-api-audio-channel-tag-structure
- name: Mediaconvert Api Audio Channel Tagging Settings Structure
  property_count: 1
  slug: mediaconvert-api-audio-channel-tagging-settings-structure
- name: Mediaconvert Api Audio Codec Settings Structure
  property_count: 11
  slug: mediaconvert-api-audio-codec-settings-structure
- name: Mediaconvert Api Audio Codec Structure
  property_count: 0
  slug: mediaconvert-api-audio-codec-structure
- name: Mediaconvert Api Audio Default Selection Structure
  property_count: 0
  slug: mediaconvert-api-audio-default-selection-structure
- name: Mediaconvert Api Audio Description Structure
  property_count: 11
  slug: mediaconvert-api-audio-description-structure
- name: Mediaconvert Api Audio Duration Correction Structure
  property_count: 0
  slug: mediaconvert-api-audio-duration-correction-structure
- name: Mediaconvert Api Audio Language Code Control Structure
  property_count: 0
  slug: mediaconvert-api-audio-language-code-control-structure
- name: Mediaconvert Api Audio Normalization Algorithm Control Structure
  property_count: 0
  slug: mediaconvert-api-audio-normalization-algorithm-control-structure
- name: Mediaconvert Api Audio Normalization Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-audio-normalization-algorithm-structure
- name: Mediaconvert Api Audio Normalization Loudness Logging Structure
  property_count: 0
  slug: mediaconvert-api-audio-normalization-loudness-logging-structure
- name: Mediaconvert Api Audio Normalization Peak Calculation Structure
  property_count: 0
  slug: mediaconvert-api-audio-normalization-peak-calculation-structure
- name: Mediaconvert Api Audio Normalization Settings Structure
  property_count: 7
  slug: mediaconvert-api-audio-normalization-settings-structure
- name: Mediaconvert Api Audio Selector Group Structure
  property_count: 1
  slug: mediaconvert-api-audio-selector-group-structure
- name: Mediaconvert Api Audio Selector Structure
  property_count: 12
  slug: mediaconvert-api-audio-selector-structure
- name: Mediaconvert Api Audio Selector Type Structure
  property_count: 0
  slug: mediaconvert-api-audio-selector-type-structure
- name: Mediaconvert Api Audio Type Control Structure
  property_count: 0
  slug: mediaconvert-api-audio-type-control-structure
- name: Mediaconvert Api Automated Abr Rule Structure
  property_count: 5
  slug: mediaconvert-api-automated-abr-rule-structure
- name: Mediaconvert Api Automated Abr Settings Structure
  property_count: 4
  slug: mediaconvert-api-automated-abr-settings-structure
- name: Mediaconvert Api Automated Encoding Settings Structure
  property_count: 1
  slug: mediaconvert-api-automated-encoding-settings-structure
- name: Mediaconvert Api Av1 Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-av1-adaptive-quantization-structure
- name: Mediaconvert Api Av1 Bit Depth Structure
  property_count: 0
  slug: mediaconvert-api-av1-bit-depth-structure
- name: Mediaconvert Api Av1 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-av1-framerate-control-structure
- name: Mediaconvert Api Av1 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-av1-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Av1 Qvbr Settings Structure
  property_count: 2
  slug: mediaconvert-api-av1-qvbr-settings-structure
- name: Mediaconvert Api Av1 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-av1-rate-control-mode-structure
- name: Mediaconvert Api Av1 Settings Structure
  property_count: 13
  slug: mediaconvert-api-av1-settings-structure
- name: Mediaconvert Api Av1 Spatial Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-av1-spatial-adaptive-quantization-structure
- name: Mediaconvert Api Avail Blanking Structure
  property_count: 1
  slug: mediaconvert-api-avail-blanking-structure
- name: Mediaconvert Api Avc Intra Class Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-class-structure
- name: Mediaconvert Api Avc Intra Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-framerate-control-structure
- name: Mediaconvert Api Avc Intra Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Avc Intra Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-interlace-mode-structure
- name: Mediaconvert Api Avc Intra Scan Type Conversion Mode Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-scan-type-conversion-mode-structure
- name: Mediaconvert Api Avc Intra Settings Structure
  property_count: 10
  slug: mediaconvert-api-avc-intra-settings-structure
- name: Mediaconvert Api Avc Intra Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-slow-pal-structure
- name: Mediaconvert Api Avc Intra Telecine Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-telecine-structure
- name: Mediaconvert Api Avc Intra Uhd Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-avc-intra-uhd-quality-tuning-level-structure
- name: Mediaconvert Api Avc Intra Uhd Settings Structure
  property_count: 1
  slug: mediaconvert-api-avc-intra-uhd-settings-structure
- name: Mediaconvert Api Bandwidth Reduction Filter Sharpening Structure
  property_count: 0
  slug: mediaconvert-api-bandwidth-reduction-filter-sharpening-structure
- name: Mediaconvert Api Bandwidth Reduction Filter Strength Structure
  property_count: 0
  slug: mediaconvert-api-bandwidth-reduction-filter-strength-structure
- name: Mediaconvert Api Bandwidth Reduction Filter Structure
  property_count: 2
  slug: mediaconvert-api-bandwidth-reduction-filter-structure
- name: Mediaconvert Api Billing Tags Source Structure
  property_count: 0
  slug: mediaconvert-api-billing-tags-source-structure
- name: Mediaconvert Api Burn In Subtitle Style Passthrough Structure
  property_count: 0
  slug: mediaconvert-api-burn-in-subtitle-style-passthrough-structure
- name: Mediaconvert Api Burnin Destination Settings Structure
  property_count: 21
  slug: mediaconvert-api-burnin-destination-settings-structure
- name: Mediaconvert Api Burnin Subtitle Alignment Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-alignment-structure
- name: Mediaconvert Api Burnin Subtitle Apply Font Color Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-apply-font-color-structure
- name: Mediaconvert Api Burnin Subtitle Background Color Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-background-color-structure
- name: Mediaconvert Api Burnin Subtitle Fallback Font Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-fallback-font-structure
- name: Mediaconvert Api Burnin Subtitle Font Color Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-font-color-structure
- name: Mediaconvert Api Burnin Subtitle Outline Color Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-outline-color-structure
- name: Mediaconvert Api Burnin Subtitle Shadow Color Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-shadow-color-structure
- name: Mediaconvert Api Burnin Subtitle Teletext Spacing Structure
  property_count: 0
  slug: mediaconvert-api-burnin-subtitle-teletext-spacing-structure
- name: Mediaconvert Api Cancel Job Request Structure
  property_count: 0
  slug: mediaconvert-api-cancel-job-request-structure
- name: Mediaconvert Api Cancel Job Response Structure
  property_count: 0
  slug: mediaconvert-api-cancel-job-response-structure
- name: Mediaconvert Api Caption Description Preset Structure
  property_count: 4
  slug: mediaconvert-api-caption-description-preset-structure
- name: Mediaconvert Api Caption Description Structure
  property_count: 5
  slug: mediaconvert-api-caption-description-structure
- name: Mediaconvert Api Caption Destination Settings Structure
  property_count: 10
  slug: mediaconvert-api-caption-destination-settings-structure
- name: Mediaconvert Api Caption Destination Type Structure
  property_count: 0
  slug: mediaconvert-api-caption-destination-type-structure
- name: Mediaconvert Api Caption Selector Structure
  property_count: 3
  slug: mediaconvert-api-caption-selector-structure
- name: Mediaconvert Api Caption Source Framerate Structure
  property_count: 2
  slug: mediaconvert-api-caption-source-framerate-structure
- name: Mediaconvert Api Caption Source Settings Structure
  property_count: 8
  slug: mediaconvert-api-caption-source-settings-structure
- name: Mediaconvert Api Caption Source Type Structure
  property_count: 0
  slug: mediaconvert-api-caption-source-type-structure
- name: Mediaconvert Api Channel Mapping Structure
  property_count: 1
  slug: mediaconvert-api-channel-mapping-structure
- name: Mediaconvert Api Clip Limits Structure
  property_count: 4
  slug: mediaconvert-api-clip-limits-structure
- name: Mediaconvert Api Cmaf Additional Manifest Structure
  property_count: 2
  slug: mediaconvert-api-cmaf-additional-manifest-structure
- name: Mediaconvert Api Cmaf Client Cache Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-client-cache-structure
- name: Mediaconvert Api Cmaf Codec Specification Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-codec-specification-structure
- name: Mediaconvert Api Cmaf Encryption Settings Structure
  property_count: 6
  slug: mediaconvert-api-cmaf-encryption-settings-structure
- name: Mediaconvert Api Cmaf Encryption Type Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-encryption-type-structure
- name: Mediaconvert Api Cmaf Group Settings Structure
  property_count: 27
  slug: mediaconvert-api-cmaf-group-settings-structure
- name: Mediaconvert Api Cmaf Image Based Trick Play Settings Structure
  property_count: 6
  slug: mediaconvert-api-cmaf-image-based-trick-play-settings-structure
- name: Mediaconvert Api Cmaf Image Based Trick Play Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-image-based-trick-play-structure
- name: Mediaconvert Api Cmaf Initialization Vector In Manifest Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-initialization-vector-in-manifest-structure
- name: Mediaconvert Api Cmaf Interval Cadence Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-interval-cadence-structure
- name: Mediaconvert Api Cmaf Key Provider Type Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-key-provider-type-structure
- name: Mediaconvert Api Cmaf Manifest Compression Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-manifest-compression-structure
- name: Mediaconvert Api Cmaf Manifest Duration Format Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-manifest-duration-format-structure
- name: Mediaconvert Api Cmaf Mpd Manifest Bandwidth Type Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-mpd-manifest-bandwidth-type-structure
- name: Mediaconvert Api Cmaf Mpd Profile Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-mpd-profile-structure
- name: Mediaconvert Api Cmaf Pts Offset Handling For B Frames Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-pts-offset-handling-for-b-frames-structure
- name: Mediaconvert Api Cmaf Segment Control Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-segment-control-structure
- name: Mediaconvert Api Cmaf Segment Length Control Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-segment-length-control-structure
- name: Mediaconvert Api Cmaf Stream Inf Resolution Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-stream-inf-resolution-structure
- name: Mediaconvert Api Cmaf Target Duration Compatibility Mode Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-target-duration-compatibility-mode-structure
- name: Mediaconvert Api Cmaf Video Composition Offsets Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-video-composition-offsets-structure
- name: Mediaconvert Api Cmaf Write Dash Manifest Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-write-dash-manifest-structure
- name: Mediaconvert Api Cmaf Write Hls Manifest Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-write-hls-manifest-structure
- name: Mediaconvert Api Cmaf Write Segment Timeline In Representation Structure
  property_count: 0
  slug: mediaconvert-api-cmaf-write-segment-timeline-in-representation-structure
- name: Mediaconvert Api Cmfc Audio Duration Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-audio-duration-structure
- name: Mediaconvert Api Cmfc Audio Track Type Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-audio-track-type-structure
- name: Mediaconvert Api Cmfc Descriptive Video Service Flag Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-descriptive-video-service-flag-structure
- name: Mediaconvert Api Cmfc I Frame Only Manifest Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-i-frame-only-manifest-structure
- name: Mediaconvert Api Cmfc Klv Metadata Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-klv-metadata-structure
- name: Mediaconvert Api Cmfc Manifest Metadata Signaling Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-manifest-metadata-signaling-structure
- name: Mediaconvert Api Cmfc Scte35 Esam Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-scte35-esam-structure
- name: Mediaconvert Api Cmfc Scte35 Source Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-scte35-source-structure
- name: Mediaconvert Api Cmfc Settings Structure
  property_count: 14
  slug: mediaconvert-api-cmfc-settings-structure
- name: Mediaconvert Api Cmfc Timed Metadata Box Version Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-timed-metadata-box-version-structure
- name: Mediaconvert Api Cmfc Timed Metadata Structure
  property_count: 0
  slug: mediaconvert-api-cmfc-timed-metadata-structure
- name: Mediaconvert Api Color Corrector Structure
  property_count: 10
  slug: mediaconvert-api-color-corrector-structure
- name: Mediaconvert Api Color Metadata Structure
  property_count: 0
  slug: mediaconvert-api-color-metadata-structure
- name: Mediaconvert Api Color Space Conversion Structure
  property_count: 0
  slug: mediaconvert-api-color-space-conversion-structure
- name: Mediaconvert Api Color Space Structure
  property_count: 0
  slug: mediaconvert-api-color-space-structure
- name: Mediaconvert Api Color Space Usage Structure
  property_count: 0
  slug: mediaconvert-api-color-space-usage-structure
- name: Mediaconvert Api Commitment Structure
  property_count: 0
  slug: mediaconvert-api-commitment-structure
- name: Mediaconvert Api Container Settings Structure
  property_count: 9
  slug: mediaconvert-api-container-settings-structure
- name: Mediaconvert Api Container Type Structure
  property_count: 0
  slug: mediaconvert-api-container-type-structure
- name: Mediaconvert Api Copy Protection Action Structure
  property_count: 0
  slug: mediaconvert-api-copy-protection-action-structure
- name: Mediaconvert Api Create Job Request Structure
  property_count: 13
  slug: mediaconvert-api-create-job-request-structure
- name: Mediaconvert Api Create Job Response Structure
  property_count: 1
  slug: mediaconvert-api-create-job-response-structure
- name: Mediaconvert Api Create Job Template Request Structure
  property_count: 10
  slug: mediaconvert-api-create-job-template-request-structure
- name: Mediaconvert Api Create Job Template Response Structure
  property_count: 1
  slug: mediaconvert-api-create-job-template-response-structure
- name: Mediaconvert Api Create Preset Request Structure
  property_count: 5
  slug: mediaconvert-api-create-preset-request-structure
- name: Mediaconvert Api Create Preset Response Structure
  property_count: 1
  slug: mediaconvert-api-create-preset-response-structure
- name: Mediaconvert Api Create Queue Request Structure
  property_count: 6
  slug: mediaconvert-api-create-queue-request-structure
- name: Mediaconvert Api Create Queue Response Structure
  property_count: 1
  slug: mediaconvert-api-create-queue-response-structure
- name: Mediaconvert Api Dash Additional Manifest Structure
  property_count: 2
  slug: mediaconvert-api-dash-additional-manifest-structure
- name: Mediaconvert Api Dash Iso Encryption Settings Structure
  property_count: 2
  slug: mediaconvert-api-dash-iso-encryption-settings-structure
- name: Mediaconvert Api Dash Iso Group Audio Channel Config Scheme Id Uri Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-group-audio-channel-config-scheme-id-uri-structure
- name: Mediaconvert Api Dash Iso Group Settings Structure
  property_count: 21
  slug: mediaconvert-api-dash-iso-group-settings-structure
- name: Mediaconvert Api Dash Iso Hbbtv Compliance Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-hbbtv-compliance-structure
- name: Mediaconvert Api Dash Iso Image Based Trick Play Settings Structure
  property_count: 6
  slug: mediaconvert-api-dash-iso-image-based-trick-play-settings-structure
- name: Mediaconvert Api Dash Iso Image Based Trick Play Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-image-based-trick-play-structure
- name: Mediaconvert Api Dash Iso Interval Cadence Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-interval-cadence-structure
- name: Mediaconvert Api Dash Iso Mpd Manifest Bandwidth Type Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-mpd-manifest-bandwidth-type-structure
- name: Mediaconvert Api Dash Iso Mpd Profile Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-mpd-profile-structure
- name: Mediaconvert Api Dash Iso Playback Device Compatibility Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-playback-device-compatibility-structure
- name: Mediaconvert Api Dash Iso Pts Offset Handling For B Frames Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-pts-offset-handling-for-b-frames-structure
- name: Mediaconvert Api Dash Iso Segment Control Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-segment-control-structure
- name: Mediaconvert Api Dash Iso Segment Length Control Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-segment-length-control-structure
- name: Mediaconvert Api Dash Iso Video Composition Offsets Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-video-composition-offsets-structure
- name: Mediaconvert Api Dash Iso Write Segment Timeline In Representation Structure
  property_count: 0
  slug: mediaconvert-api-dash-iso-write-segment-timeline-in-representation-structure
- name: Mediaconvert Api Dash Manifest Style Structure
  property_count: 0
  slug: mediaconvert-api-dash-manifest-style-structure
- name: Mediaconvert Api Decryption Mode Structure
  property_count: 0
  slug: mediaconvert-api-decryption-mode-structure
- name: Mediaconvert Api Deinterlace Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-deinterlace-algorithm-structure
- name: Mediaconvert Api Deinterlacer Control Structure
  property_count: 0
  slug: mediaconvert-api-deinterlacer-control-structure
- name: Mediaconvert Api Deinterlacer Mode Structure
  property_count: 0
  slug: mediaconvert-api-deinterlacer-mode-structure
- name: Mediaconvert Api Deinterlacer Structure
  property_count: 3
  slug: mediaconvert-api-deinterlacer-structure
- name: Mediaconvert Api Delete Job Template Request Structure
  property_count: 0
  slug: mediaconvert-api-delete-job-template-request-structure
- name: Mediaconvert Api Delete Job Template Response Structure
  property_count: 0
  slug: mediaconvert-api-delete-job-template-response-structure
- name: Mediaconvert Api Delete Policy Request Structure
  property_count: 0
  slug: mediaconvert-api-delete-policy-request-structure
- name: Mediaconvert Api Delete Policy Response Structure
  property_count: 0
  slug: mediaconvert-api-delete-policy-response-structure
- name: Mediaconvert Api Delete Preset Request Structure
  property_count: 0
  slug: mediaconvert-api-delete-preset-request-structure
- name: Mediaconvert Api Delete Preset Response Structure
  property_count: 0
  slug: mediaconvert-api-delete-preset-response-structure
- name: Mediaconvert Api Delete Queue Request Structure
  property_count: 0
  slug: mediaconvert-api-delete-queue-request-structure
- name: Mediaconvert Api Delete Queue Response Structure
  property_count: 0
  slug: mediaconvert-api-delete-queue-response-structure
- name: Mediaconvert Api Describe Endpoints Mode Structure
  property_count: 0
  slug: mediaconvert-api-describe-endpoints-mode-structure
- name: Mediaconvert Api Describe Endpoints Request Structure
  property_count: 3
  slug: mediaconvert-api-describe-endpoints-request-structure
- name: Mediaconvert Api Describe Endpoints Response Structure
  property_count: 2
  slug: mediaconvert-api-describe-endpoints-response-structure
- name: Mediaconvert Api Destination Settings Structure
  property_count: 1
  slug: mediaconvert-api-destination-settings-structure
- name: Mediaconvert Api Disassociate Certificate Request Structure
  property_count: 0
  slug: mediaconvert-api-disassociate-certificate-request-structure
- name: Mediaconvert Api Disassociate Certificate Response Structure
  property_count: 0
  slug: mediaconvert-api-disassociate-certificate-response-structure
- name: Mediaconvert Api Dolby Vision Level6 Metadata Structure
  property_count: 2
  slug: mediaconvert-api-dolby-vision-level6-metadata-structure
- name: Mediaconvert Api Dolby Vision Level6 Mode Structure
  property_count: 0
  slug: mediaconvert-api-dolby-vision-level6-mode-structure
- name: Mediaconvert Api Dolby Vision Mapping Structure
  property_count: 0
  slug: mediaconvert-api-dolby-vision-mapping-structure
- name: Mediaconvert Api Dolby Vision Profile Structure
  property_count: 0
  slug: mediaconvert-api-dolby-vision-profile-structure
- name: Mediaconvert Api Dolby Vision Structure
  property_count: 4
  slug: mediaconvert-api-dolby-vision-structure
- name: Mediaconvert Api Drop Frame Timecode Structure
  property_count: 0
  slug: mediaconvert-api-drop-frame-timecode-structure
- name: Mediaconvert Api Dvb Nit Settings Structure
  property_count: 3
  slug: mediaconvert-api-dvb-nit-settings-structure
- name: Mediaconvert Api Dvb Sdt Settings Structure
  property_count: 4
  slug: mediaconvert-api-dvb-sdt-settings-structure
- name: Mediaconvert Api Dvb Sub Destination Settings Structure
  property_count: 27
  slug: mediaconvert-api-dvb-sub-destination-settings-structure
- name: Mediaconvert Api Dvb Sub Source Settings Structure
  property_count: 1
  slug: mediaconvert-api-dvb-sub-source-settings-structure
- name: Mediaconvert Api Dvb Sub Subtitle Fallback Font Structure
  property_count: 0
  slug: mediaconvert-api-dvb-sub-subtitle-fallback-font-structure
- name: Mediaconvert Api Dvb Subtitle Alignment Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-alignment-structure
- name: Mediaconvert Api Dvb Subtitle Apply Font Color Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-apply-font-color-structure
- name: Mediaconvert Api Dvb Subtitle Background Color Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-background-color-structure
- name: Mediaconvert Api Dvb Subtitle Font Color Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-font-color-structure
- name: Mediaconvert Api Dvb Subtitle Outline Color Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-outline-color-structure
- name: Mediaconvert Api Dvb Subtitle Shadow Color Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-shadow-color-structure
- name: Mediaconvert Api Dvb Subtitle Style Passthrough Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-style-passthrough-structure
- name: Mediaconvert Api Dvb Subtitle Teletext Spacing Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitle-teletext-spacing-structure
- name: Mediaconvert Api Dvb Subtitling Type Structure
  property_count: 0
  slug: mediaconvert-api-dvb-subtitling-type-structure
- name: Mediaconvert Api Dvb Tdt Settings Structure
  property_count: 1
  slug: mediaconvert-api-dvb-tdt-settings-structure
- name: Mediaconvert Api Dvbdds Handling Structure
  property_count: 0
  slug: mediaconvert-api-dvbdds-handling-structure
- name: Mediaconvert Api Eac3 Atmos Bitstream Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-bitstream-mode-structure
- name: Mediaconvert Api Eac3 Atmos Coding Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-coding-mode-structure
- name: Mediaconvert Api Eac3 Atmos Dialogue Intelligence Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dialogue-intelligence-structure
- name: Mediaconvert Api Eac3 Atmos Downmix Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-downmix-control-structure
- name: Mediaconvert Api Eac3 Atmos Dynamic Range Compression Line Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dynamic-range-compression-line-structure
- name: Mediaconvert Api Eac3 Atmos Dynamic Range Compression Rf Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dynamic-range-compression-rf-structure
- name: Mediaconvert Api Eac3 Atmos Dynamic Range Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-dynamic-range-control-structure
- name: Mediaconvert Api Eac3 Atmos Metering Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-metering-mode-structure
- name: Mediaconvert Api Eac3 Atmos Settings Structure
  property_count: 17
  slug: mediaconvert-api-eac3-atmos-settings-structure
- name: Mediaconvert Api Eac3 Atmos Stereo Downmix Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-stereo-downmix-structure
- name: Mediaconvert Api Eac3 Atmos Surround Ex Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-atmos-surround-ex-mode-structure
- name: Mediaconvert Api Eac3 Attenuation Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-attenuation-control-structure
- name: Mediaconvert Api Eac3 Bitstream Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-bitstream-mode-structure
- name: Mediaconvert Api Eac3 Coding Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-coding-mode-structure
- name: Mediaconvert Api Eac3 Dc Filter Structure
  property_count: 0
  slug: mediaconvert-api-eac3-dc-filter-structure
- name: Mediaconvert Api Eac3 Dynamic Range Compression Line Structure
  property_count: 0
  slug: mediaconvert-api-eac3-dynamic-range-compression-line-structure
- name: Mediaconvert Api Eac3 Dynamic Range Compression Rf Structure
  property_count: 0
  slug: mediaconvert-api-eac3-dynamic-range-compression-rf-structure
- name: Mediaconvert Api Eac3 Lfe Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-lfe-control-structure
- name: Mediaconvert Api Eac3 Lfe Filter Structure
  property_count: 0
  slug: mediaconvert-api-eac3-lfe-filter-structure
- name: Mediaconvert Api Eac3 Metadata Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-metadata-control-structure
- name: Mediaconvert Api Eac3 Passthrough Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-passthrough-control-structure
- name: Mediaconvert Api Eac3 Phase Control Structure
  property_count: 0
  slug: mediaconvert-api-eac3-phase-control-structure
- name: Mediaconvert Api Eac3 Settings Structure
  property_count: 21
  slug: mediaconvert-api-eac3-settings-structure
- name: Mediaconvert Api Eac3 Stereo Downmix Structure
  property_count: 0
  slug: mediaconvert-api-eac3-stereo-downmix-structure
- name: Mediaconvert Api Eac3 Surround Ex Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-surround-ex-mode-structure
- name: Mediaconvert Api Eac3 Surround Mode Structure
  property_count: 0
  slug: mediaconvert-api-eac3-surround-mode-structure
- name: Mediaconvert Api Embedded Convert608 To708 Structure
  property_count: 0
  slug: mediaconvert-api-embedded-convert608-to708-structure
- name: Mediaconvert Api Embedded Destination Settings Structure
  property_count: 2
  slug: mediaconvert-api-embedded-destination-settings-structure
- name: Mediaconvert Api Embedded Source Settings Structure
  property_count: 4
  slug: mediaconvert-api-embedded-source-settings-structure
- name: Mediaconvert Api Embedded Terminate Captions Structure
  property_count: 0
  slug: mediaconvert-api-embedded-terminate-captions-structure
- name: Mediaconvert Api Embedded Timecode Override Structure
  property_count: 0
  slug: mediaconvert-api-embedded-timecode-override-structure
- name: Mediaconvert Api Endpoint Structure
  property_count: 1
  slug: mediaconvert-api-endpoint-structure
- name: Mediaconvert Api Esam Manifest Confirm Condition Notification Structure
  property_count: 1
  slug: mediaconvert-api-esam-manifest-confirm-condition-notification-structure
- name: Mediaconvert Api Esam Settings Structure
  property_count: 3
  slug: mediaconvert-api-esam-settings-structure
- name: Mediaconvert Api Esam Signal Processing Notification Structure
  property_count: 1
  slug: mediaconvert-api-esam-signal-processing-notification-structure
- name: Mediaconvert Api Extended Data Services Structure
  property_count: 2
  slug: mediaconvert-api-extended-data-services-structure
- name: Mediaconvert Api F4V Moov Placement Structure
  property_count: 0
  slug: mediaconvert-api-f4v-moov-placement-structure
- name: Mediaconvert Api F4V Settings Structure
  property_count: 1
  slug: mediaconvert-api-f4v-settings-structure
- name: Mediaconvert Api File Group Settings Structure
  property_count: 2
  slug: mediaconvert-api-file-group-settings-structure
- name: Mediaconvert Api File Source Convert608 To708 Structure
  property_count: 0
  slug: mediaconvert-api-file-source-convert608-to708-structure
- name: Mediaconvert Api File Source Settings Structure
  property_count: 5
  slug: mediaconvert-api-file-source-settings-structure
- name: Mediaconvert Api File Source Time Delta Units Structure
  property_count: 0
  slug: mediaconvert-api-file-source-time-delta-units-structure
- name: Mediaconvert Api Font Script Structure
  property_count: 0
  slug: mediaconvert-api-font-script-structure
- name: Mediaconvert Api Force Include Rendition Size Structure
  property_count: 2
  slug: mediaconvert-api-force-include-rendition-size-structure
- name: Mediaconvert Api Frame Capture Settings Structure
  property_count: 4
  slug: mediaconvert-api-frame-capture-settings-structure
- name: Mediaconvert Api Get Job Request Structure
  property_count: 0
  slug: mediaconvert-api-get-job-request-structure
- name: Mediaconvert Api Get Job Response Structure
  property_count: 1
  slug: mediaconvert-api-get-job-response-structure
- name: Mediaconvert Api Get Job Template Request Structure
  property_count: 0
  slug: mediaconvert-api-get-job-template-request-structure
- name: Mediaconvert Api Get Job Template Response Structure
  property_count: 1
  slug: mediaconvert-api-get-job-template-response-structure
- name: Mediaconvert Api Get Policy Request Structure
  property_count: 0
  slug: mediaconvert-api-get-policy-request-structure
- name: Mediaconvert Api Get Policy Response Structure
  property_count: 1
  slug: mediaconvert-api-get-policy-response-structure
- name: Mediaconvert Api Get Preset Request Structure
  property_count: 0
  slug: mediaconvert-api-get-preset-request-structure
- name: Mediaconvert Api Get Preset Response Structure
  property_count: 1
  slug: mediaconvert-api-get-preset-response-structure
- name: Mediaconvert Api Get Queue Request Structure
  property_count: 0
  slug: mediaconvert-api-get-queue-request-structure
- name: Mediaconvert Api Get Queue Response Structure
  property_count: 1
  slug: mediaconvert-api-get-queue-response-structure
- name: Mediaconvert Api H264 Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h264-adaptive-quantization-structure
- name: Mediaconvert Api H264 Codec Level Structure
  property_count: 0
  slug: mediaconvert-api-h264-codec-level-structure
- name: Mediaconvert Api H264 Codec Profile Structure
  property_count: 0
  slug: mediaconvert-api-h264-codec-profile-structure
- name: Mediaconvert Api H264 Dynamic Sub Gop Structure
  property_count: 0
  slug: mediaconvert-api-h264-dynamic-sub-gop-structure
- name: Mediaconvert Api H264 Entropy Encoding Structure
  property_count: 0
  slug: mediaconvert-api-h264-entropy-encoding-structure
- name: Mediaconvert Api H264 Field Encoding Structure
  property_count: 0
  slug: mediaconvert-api-h264-field-encoding-structure
- name: Mediaconvert Api H264 Flicker Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h264-flicker-adaptive-quantization-structure
- name: Mediaconvert Api H264 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-h264-framerate-control-structure
- name: Mediaconvert Api H264 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-h264-framerate-conversion-algorithm-structure
- name: Mediaconvert Api H264 Gop B Reference Structure
  property_count: 0
  slug: mediaconvert-api-h264-gop-b-reference-structure
- name: Mediaconvert Api H264 Gop Size Units Structure
  property_count: 0
  slug: mediaconvert-api-h264-gop-size-units-structure
- name: Mediaconvert Api H264 Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-h264-interlace-mode-structure
- name: Mediaconvert Api H264 Par Control Structure
  property_count: 0
  slug: mediaconvert-api-h264-par-control-structure
- name: Mediaconvert Api H264 Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-h264-quality-tuning-level-structure
- name: Mediaconvert Api H264 Qvbr Settings Structure
  property_count: 3
  slug: mediaconvert-api-h264-qvbr-settings-structure
- name: Mediaconvert Api H264 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-h264-rate-control-mode-structure
- name: Mediaconvert Api H264 Repeat Pps Structure
  property_count: 0
  slug: mediaconvert-api-h264-repeat-pps-structure
- name: Mediaconvert Api H264 Scan Type Conversion Mode Structure
  property_count: 0
  slug: mediaconvert-api-h264-scan-type-conversion-mode-structure
- name: Mediaconvert Api H264 Scene Change Detect Structure
  property_count: 0
  slug: mediaconvert-api-h264-scene-change-detect-structure
- name: Mediaconvert Api H264 Settings Structure
  property_count: 42
  slug: mediaconvert-api-h264-settings-structure
- name: Mediaconvert Api H264 Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-h264-slow-pal-structure
- name: Mediaconvert Api H264 Spatial Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h264-spatial-adaptive-quantization-structure
- name: Mediaconvert Api H264 Syntax Structure
  property_count: 0
  slug: mediaconvert-api-h264-syntax-structure
- name: Mediaconvert Api H264 Telecine Structure
  property_count: 0
  slug: mediaconvert-api-h264-telecine-structure
- name: Mediaconvert Api H264 Temporal Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h264-temporal-adaptive-quantization-structure
- name: Mediaconvert Api H264 Unregistered Sei Timecode Structure
  property_count: 0
  slug: mediaconvert-api-h264-unregistered-sei-timecode-structure
- name: Mediaconvert Api H265 Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h265-adaptive-quantization-structure
- name: Mediaconvert Api H265 Alternate Transfer Function Sei Structure
  property_count: 0
  slug: mediaconvert-api-h265-alternate-transfer-function-sei-structure
- name: Mediaconvert Api H265 Codec Level Structure
  property_count: 0
  slug: mediaconvert-api-h265-codec-level-structure
- name: Mediaconvert Api H265 Codec Profile Structure
  property_count: 0
  slug: mediaconvert-api-h265-codec-profile-structure
- name: Mediaconvert Api H265 Dynamic Sub Gop Structure
  property_count: 0
  slug: mediaconvert-api-h265-dynamic-sub-gop-structure
- name: Mediaconvert Api H265 Flicker Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h265-flicker-adaptive-quantization-structure
- name: Mediaconvert Api H265 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-h265-framerate-control-structure
- name: Mediaconvert Api H265 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-h265-framerate-conversion-algorithm-structure
- name: Mediaconvert Api H265 Gop B Reference Structure
  property_count: 0
  slug: mediaconvert-api-h265-gop-b-reference-structure
- name: Mediaconvert Api H265 Gop Size Units Structure
  property_count: 0
  slug: mediaconvert-api-h265-gop-size-units-structure
- name: Mediaconvert Api H265 Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-h265-interlace-mode-structure
- name: Mediaconvert Api H265 Par Control Structure
  property_count: 0
  slug: mediaconvert-api-h265-par-control-structure
- name: Mediaconvert Api H265 Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-h265-quality-tuning-level-structure
- name: Mediaconvert Api H265 Qvbr Settings Structure
  property_count: 3
  slug: mediaconvert-api-h265-qvbr-settings-structure
- name: Mediaconvert Api H265 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-h265-rate-control-mode-structure
- name: Mediaconvert Api H265 Sample Adaptive Offset Filter Mode Structure
  property_count: 0
  slug: mediaconvert-api-h265-sample-adaptive-offset-filter-mode-structure
- name: Mediaconvert Api H265 Scan Type Conversion Mode Structure
  property_count: 0
  slug: mediaconvert-api-h265-scan-type-conversion-mode-structure
- name: Mediaconvert Api H265 Scene Change Detect Structure
  property_count: 0
  slug: mediaconvert-api-h265-scene-change-detect-structure
- name: Mediaconvert Api H265 Settings Structure
  property_count: 41
  slug: mediaconvert-api-h265-settings-structure
- name: Mediaconvert Api H265 Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-h265-slow-pal-structure
- name: Mediaconvert Api H265 Spatial Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h265-spatial-adaptive-quantization-structure
- name: Mediaconvert Api H265 Telecine Structure
  property_count: 0
  slug: mediaconvert-api-h265-telecine-structure
- name: Mediaconvert Api H265 Temporal Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-h265-temporal-adaptive-quantization-structure
- name: Mediaconvert Api H265 Temporal Ids Structure
  property_count: 0
  slug: mediaconvert-api-h265-temporal-ids-structure
- name: Mediaconvert Api H265 Tiles Structure
  property_count: 0
  slug: mediaconvert-api-h265-tiles-structure
- name: Mediaconvert Api H265 Unregistered Sei Timecode Structure
  property_count: 0
  slug: mediaconvert-api-h265-unregistered-sei-timecode-structure
- name: Mediaconvert Api H265 Write Mp4 Packaging Type Structure
  property_count: 0
  slug: mediaconvert-api-h265-write-mp4-packaging-type-structure
- name: Mediaconvert Api Hdr To Sdr Tone Mapper Structure
  property_count: 0
  slug: mediaconvert-api-hdr-to-sdr-tone-mapper-structure
- name: Mediaconvert Api Hdr10 Metadata Structure
  property_count: 12
  slug: mediaconvert-api-hdr10-metadata-structure
- name: Mediaconvert Api Hdr10 Plus Structure
  property_count: 2
  slug: mediaconvert-api-hdr10-plus-structure
- name: Mediaconvert Api Hls Ad Markers Structure
  property_count: 0
  slug: mediaconvert-api-hls-ad-markers-structure
- name: Mediaconvert Api Hls Additional Manifest Structure
  property_count: 2
  slug: mediaconvert-api-hls-additional-manifest-structure
- name: Mediaconvert Api Hls Audio Only Container Structure
  property_count: 0
  slug: mediaconvert-api-hls-audio-only-container-structure
- name: Mediaconvert Api Hls Audio Only Header Structure
  property_count: 0
  slug: mediaconvert-api-hls-audio-only-header-structure
- name: Mediaconvert Api Hls Audio Track Type Structure
  property_count: 0
  slug: mediaconvert-api-hls-audio-track-type-structure
- name: Mediaconvert Api Hls Caption Language Mapping Structure
  property_count: 4
  slug: mediaconvert-api-hls-caption-language-mapping-structure
- name: Mediaconvert Api Hls Caption Language Setting Structure
  property_count: 0
  slug: mediaconvert-api-hls-caption-language-setting-structure
- name: Mediaconvert Api Hls Caption Segment Length Control Structure
  property_count: 0
  slug: mediaconvert-api-hls-caption-segment-length-control-structure
- name: Mediaconvert Api Hls Client Cache Structure
  property_count: 0
  slug: mediaconvert-api-hls-client-cache-structure
- name: Mediaconvert Api Hls Codec Specification Structure
  property_count: 0
  slug: mediaconvert-api-hls-codec-specification-structure
- name: Mediaconvert Api Hls Descriptive Video Service Flag Structure
  property_count: 0
  slug: mediaconvert-api-hls-descriptive-video-service-flag-structure
- name: Mediaconvert Api Hls Directory Structure Structure
  property_count: 0
  slug: mediaconvert-api-hls-directory-structure-structure
- name: Mediaconvert Api Hls Encryption Settings Structure
  property_count: 7
  slug: mediaconvert-api-hls-encryption-settings-structure
- name: Mediaconvert Api Hls Encryption Type Structure
  property_count: 0
  slug: mediaconvert-api-hls-encryption-type-structure
- name: Mediaconvert Api Hls Group Settings Structure
  property_count: 31
  slug: mediaconvert-api-hls-group-settings-structure
- name: Mediaconvert Api Hls I Frame Only Manifest Structure
  property_count: 0
  slug: mediaconvert-api-hls-i-frame-only-manifest-structure
- name: Mediaconvert Api Hls Image Based Trick Play Settings Structure
  property_count: 6
  slug: mediaconvert-api-hls-image-based-trick-play-settings-structure
- name: Mediaconvert Api Hls Image Based Trick Play Structure
  property_count: 0
  slug: mediaconvert-api-hls-image-based-trick-play-structure
- name: Mediaconvert Api Hls Initialization Vector In Manifest Structure
  property_count: 0
  slug: mediaconvert-api-hls-initialization-vector-in-manifest-structure
- name: Mediaconvert Api Hls Interval Cadence Structure
  property_count: 0
  slug: mediaconvert-api-hls-interval-cadence-structure
- name: Mediaconvert Api Hls Key Provider Type Structure
  property_count: 0
  slug: mediaconvert-api-hls-key-provider-type-structure
- name: Mediaconvert Api Hls Manifest Compression Structure
  property_count: 0
  slug: mediaconvert-api-hls-manifest-compression-structure
- name: Mediaconvert Api Hls Manifest Duration Format Structure
  property_count: 0
  slug: mediaconvert-api-hls-manifest-duration-format-structure
- name: Mediaconvert Api Hls Offline Encrypted Structure
  property_count: 0
  slug: mediaconvert-api-hls-offline-encrypted-structure
- name: Mediaconvert Api Hls Output Selection Structure
  property_count: 0
  slug: mediaconvert-api-hls-output-selection-structure
- name: Mediaconvert Api Hls Program Date Time Structure
  property_count: 0
  slug: mediaconvert-api-hls-program-date-time-structure
- name: Mediaconvert Api Hls Rendition Group Settings Structure
  property_count: 3
  slug: mediaconvert-api-hls-rendition-group-settings-structure
- name: Mediaconvert Api Hls Segment Control Structure
  property_count: 0
  slug: mediaconvert-api-hls-segment-control-structure
- name: Mediaconvert Api Hls Segment Length Control Structure
  property_count: 0
  slug: mediaconvert-api-hls-segment-length-control-structure
- name: Mediaconvert Api Hls Settings Structure
  property_count: 7
  slug: mediaconvert-api-hls-settings-structure
- name: Mediaconvert Api Hls Stream Inf Resolution Structure
  property_count: 0
  slug: mediaconvert-api-hls-stream-inf-resolution-structure
- name: Mediaconvert Api Hls Target Duration Compatibility Mode Structure
  property_count: 0
  slug: mediaconvert-api-hls-target-duration-compatibility-mode-structure
- name: Mediaconvert Api Hls Timed Metadata Id3 Frame Structure
  property_count: 0
  slug: mediaconvert-api-hls-timed-metadata-id3-frame-structure
- name: Mediaconvert Api Hop Destination Structure
  property_count: 3
  slug: mediaconvert-api-hop-destination-structure
- name: Mediaconvert Api Id3 Insertion Structure
  property_count: 2
  slug: mediaconvert-api-id3-insertion-structure
- name: Mediaconvert Api Image Inserter Structure
  property_count: 2
  slug: mediaconvert-api-image-inserter-structure
- name: Mediaconvert Api Imsc Accessibility Subs Structure
  property_count: 0
  slug: mediaconvert-api-imsc-accessibility-subs-structure
- name: Mediaconvert Api Imsc Destination Settings Structure
  property_count: 2
  slug: mediaconvert-api-imsc-destination-settings-structure
- name: Mediaconvert Api Imsc Style Passthrough Structure
  property_count: 0
  slug: mediaconvert-api-imsc-style-passthrough-structure
- name: Mediaconvert Api Input Clipping Structure
  property_count: 2
  slug: mediaconvert-api-input-clipping-structure
- name: Mediaconvert Api Input Deblock Filter Structure
  property_count: 0
  slug: mediaconvert-api-input-deblock-filter-structure
- name: Mediaconvert Api Input Decryption Settings Structure
  property_count: 4
  slug: mediaconvert-api-input-decryption-settings-structure
- name: Mediaconvert Api Input Denoise Filter Structure
  property_count: 0
  slug: mediaconvert-api-input-denoise-filter-structure
- name: Mediaconvert Api Input Filter Enable Structure
  property_count: 0
  slug: mediaconvert-api-input-filter-enable-structure
- name: Mediaconvert Api Input Policy Structure
  property_count: 0
  slug: mediaconvert-api-input-policy-structure
- name: Mediaconvert Api Input Psi Control Structure
  property_count: 0
  slug: mediaconvert-api-input-psi-control-structure
- name: Mediaconvert Api Input Rotate Structure
  property_count: 0
  slug: mediaconvert-api-input-rotate-structure
- name: Mediaconvert Api Input Sample Range Structure
  property_count: 0
  slug: mediaconvert-api-input-sample-range-structure
- name: Mediaconvert Api Input Scan Type Structure
  property_count: 0
  slug: mediaconvert-api-input-scan-type-structure
- name: Mediaconvert Api Input Structure
  property_count: 22
  slug: mediaconvert-api-input-structure
- name: Mediaconvert Api Input Template Structure
  property_count: 18
  slug: mediaconvert-api-input-template-structure
- name: Mediaconvert Api Input Timecode Source Structure
  property_count: 0
  slug: mediaconvert-api-input-timecode-source-structure
- name: Mediaconvert Api Input Video Generator Structure
  property_count: 1
  slug: mediaconvert-api-input-video-generator-structure
- name: Mediaconvert Api Insertable Image Structure
  property_count: 11
  slug: mediaconvert-api-insertable-image-structure
- name: Mediaconvert Api Job Messages Structure
  property_count: 2
  slug: mediaconvert-api-job-messages-structure
- name: Mediaconvert Api Job Phase Structure
  property_count: 0
  slug: mediaconvert-api-job-phase-structure
- name: Mediaconvert Api Job Settings Structure
  property_count: 12
  slug: mediaconvert-api-job-settings-structure
- name: Mediaconvert Api Job Status Structure
  property_count: 0
  slug: mediaconvert-api-job-status-structure
- name: Mediaconvert Api Job Structure
  property_count: 27
  slug: mediaconvert-api-job-structure
- name: Mediaconvert Api Job Template List By Structure
  property_count: 0
  slug: mediaconvert-api-job-template-list-by-structure
- name: Mediaconvert Api Job Template Settings Structure
  property_count: 12
  slug: mediaconvert-api-job-template-settings-structure
- name: Mediaconvert Api Job Template Structure
  property_count: 13
  slug: mediaconvert-api-job-template-structure
- name: Mediaconvert Api Kantar Watermark Settings Structure
  property_count: 13
  slug: mediaconvert-api-kantar-watermark-settings-structure
- name: Mediaconvert Api Language Code Structure
  property_count: 0
  slug: mediaconvert-api-language-code-structure
- name: Mediaconvert Api List Job Templates Request Structure
  property_count: 0
  slug: mediaconvert-api-list-job-templates-request-structure
- name: Mediaconvert Api List Job Templates Response Structure
  property_count: 2
  slug: mediaconvert-api-list-job-templates-response-structure
- name: Mediaconvert Api List Jobs Request Structure
  property_count: 0
  slug: mediaconvert-api-list-jobs-request-structure
- name: Mediaconvert Api List Jobs Response Structure
  property_count: 2
  slug: mediaconvert-api-list-jobs-response-structure
- name: Mediaconvert Api List Presets Request Structure
  property_count: 0
  slug: mediaconvert-api-list-presets-request-structure
- name: Mediaconvert Api List Presets Response Structure
  property_count: 2
  slug: mediaconvert-api-list-presets-response-structure
- name: Mediaconvert Api List Queues Request Structure
  property_count: 0
  slug: mediaconvert-api-list-queues-request-structure
- name: Mediaconvert Api List Queues Response Structure
  property_count: 2
  slug: mediaconvert-api-list-queues-response-structure
- name: Mediaconvert Api List Tags For Resource Request Structure
  property_count: 0
  slug: mediaconvert-api-list-tags-for-resource-request-structure
- name: Mediaconvert Api List Tags For Resource Response Structure
  property_count: 1
  slug: mediaconvert-api-list-tags-for-resource-response-structure
- name: Mediaconvert Api M2Ts Audio Buffer Model Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-audio-buffer-model-structure
- name: Mediaconvert Api M2Ts Audio Duration Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-audio-duration-structure
- name: Mediaconvert Api M2Ts Buffer Model Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-buffer-model-structure
- name: Mediaconvert Api M2Ts Data Pts Control Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-data-pts-control-structure
- name: Mediaconvert Api M2Ts Ebp Audio Interval Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-ebp-audio-interval-structure
- name: Mediaconvert Api M2Ts Ebp Placement Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-ebp-placement-structure
- name: Mediaconvert Api M2Ts Es Rate In Pes Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-es-rate-in-pes-structure
- name: Mediaconvert Api M2Ts Force Ts Video Ebp Order Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-force-ts-video-ebp-order-structure
- name: Mediaconvert Api M2Ts Klv Metadata Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-klv-metadata-structure
- name: Mediaconvert Api M2Ts Nielsen Id3 Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-nielsen-id3-structure
- name: Mediaconvert Api M2Ts Pcr Control Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-pcr-control-structure
- name: Mediaconvert Api M2Ts Rate Mode Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-rate-mode-structure
- name: Mediaconvert Api M2Ts Scte35 Esam Structure
  property_count: 1
  slug: mediaconvert-api-m2ts-scte35-esam-structure
- name: Mediaconvert Api M2Ts Scte35 Source Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-scte35-source-structure
- name: Mediaconvert Api M2Ts Segmentation Markers Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-segmentation-markers-structure
- name: Mediaconvert Api M2Ts Segmentation Style Structure
  property_count: 0
  slug: mediaconvert-api-m2ts-segmentation-style-structure
- name: Mediaconvert Api M2Ts Settings Structure
  property_count: 39
  slug: mediaconvert-api-m2ts-settings-structure
- name: Mediaconvert Api M3U8 Audio Duration Structure
  property_count: 0
  slug: mediaconvert-api-m3u8-audio-duration-structure
- name: Mediaconvert Api M3U8 Data Pts Control Structure
  property_count: 0
  slug: mediaconvert-api-m3u8-data-pts-control-structure
- name: Mediaconvert Api M3U8 Nielsen Id3 Structure
  property_count: 0
  slug: mediaconvert-api-m3u8-nielsen-id3-structure
- name: Mediaconvert Api M3U8 Pcr Control Structure
  property_count: 0
  slug: mediaconvert-api-m3u8-pcr-control-structure
- name: Mediaconvert Api M3U8 Scte35 Source Structure
  property_count: 0
  slug: mediaconvert-api-m3u8-scte35-source-structure
- name: Mediaconvert Api M3U8 Settings Structure
  property_count: 19
  slug: mediaconvert-api-m3u8-settings-structure
- name: Mediaconvert Api Min Bottom Rendition Size Structure
  property_count: 2
  slug: mediaconvert-api-min-bottom-rendition-size-structure
- name: Mediaconvert Api Min Top Rendition Size Structure
  property_count: 2
  slug: mediaconvert-api-min-top-rendition-size-structure
- name: Mediaconvert Api Motion Image Inserter Structure
  property_count: 6
  slug: mediaconvert-api-motion-image-inserter-structure
- name: Mediaconvert Api Motion Image Insertion Framerate Structure
  property_count: 2
  slug: mediaconvert-api-motion-image-insertion-framerate-structure
- name: Mediaconvert Api Motion Image Insertion Mode Structure
  property_count: 0
  slug: mediaconvert-api-motion-image-insertion-mode-structure
- name: Mediaconvert Api Motion Image Insertion Offset Structure
  property_count: 2
  slug: mediaconvert-api-motion-image-insertion-offset-structure
- name: Mediaconvert Api Motion Image Playback Structure
  property_count: 0
  slug: mediaconvert-api-motion-image-playback-structure
- name: Mediaconvert Api Mov Clap Atom Structure
  property_count: 0
  slug: mediaconvert-api-mov-clap-atom-structure
- name: Mediaconvert Api Mov Cslg Atom Structure
  property_count: 0
  slug: mediaconvert-api-mov-cslg-atom-structure
- name: Mediaconvert Api Mov Mpeg2 Four Cc Control Structure
  property_count: 0
  slug: mediaconvert-api-mov-mpeg2-four-cc-control-structure
- name: Mediaconvert Api Mov Padding Control Structure
  property_count: 0
  slug: mediaconvert-api-mov-padding-control-structure
- name: Mediaconvert Api Mov Reference Structure
  property_count: 0
  slug: mediaconvert-api-mov-reference-structure
- name: Mediaconvert Api Mov Settings Structure
  property_count: 5
  slug: mediaconvert-api-mov-settings-structure
- name: Mediaconvert Api Mp2 Settings Structure
  property_count: 3
  slug: mediaconvert-api-mp2-settings-structure
- name: Mediaconvert Api Mp3 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-mp3-rate-control-mode-structure
- name: Mediaconvert Api Mp3 Settings Structure
  property_count: 5
  slug: mediaconvert-api-mp3-settings-structure
- name: Mediaconvert Api Mp4 Cslg Atom Structure
  property_count: 0
  slug: mediaconvert-api-mp4-cslg-atom-structure
- name: Mediaconvert Api Mp4 Free Space Box Structure
  property_count: 0
  slug: mediaconvert-api-mp4-free-space-box-structure
- name: Mediaconvert Api Mp4 Moov Placement Structure
  property_count: 0
  slug: mediaconvert-api-mp4-moov-placement-structure
- name: Mediaconvert Api Mp4 Settings Structure
  property_count: 6
  slug: mediaconvert-api-mp4-settings-structure
- name: Mediaconvert Api Mpd Accessibility Caption Hints Structure
  property_count: 0
  slug: mediaconvert-api-mpd-accessibility-caption-hints-structure
- name: Mediaconvert Api Mpd Audio Duration Structure
  property_count: 0
  slug: mediaconvert-api-mpd-audio-duration-structure
- name: Mediaconvert Api Mpd Caption Container Type Structure
  property_count: 0
  slug: mediaconvert-api-mpd-caption-container-type-structure
- name: Mediaconvert Api Mpd Klv Metadata Structure
  property_count: 0
  slug: mediaconvert-api-mpd-klv-metadata-structure
- name: Mediaconvert Api Mpd Manifest Metadata Signaling Structure
  property_count: 0
  slug: mediaconvert-api-mpd-manifest-metadata-signaling-structure
- name: Mediaconvert Api Mpd Scte35 Esam Structure
  property_count: 0
  slug: mediaconvert-api-mpd-scte35-esam-structure
- name: Mediaconvert Api Mpd Scte35 Source Structure
  property_count: 0
  slug: mediaconvert-api-mpd-scte35-source-structure
- name: Mediaconvert Api Mpd Settings Structure
  property_count: 11
  slug: mediaconvert-api-mpd-settings-structure
- name: Mediaconvert Api Mpd Timed Metadata Box Version Structure
  property_count: 0
  slug: mediaconvert-api-mpd-timed-metadata-box-version-structure
- name: Mediaconvert Api Mpd Timed Metadata Structure
  property_count: 0
  slug: mediaconvert-api-mpd-timed-metadata-structure
- name: Mediaconvert Api Mpeg2 Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-adaptive-quantization-structure
- name: Mediaconvert Api Mpeg2 Codec Level Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-codec-level-structure
- name: Mediaconvert Api Mpeg2 Codec Profile Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-codec-profile-structure
- name: Mediaconvert Api Mpeg2 Dynamic Sub Gop Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-dynamic-sub-gop-structure
- name: Mediaconvert Api Mpeg2 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-framerate-control-structure
- name: Mediaconvert Api Mpeg2 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Mpeg2 Gop Size Units Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-gop-size-units-structure
- name: Mediaconvert Api Mpeg2 Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-interlace-mode-structure
- name: Mediaconvert Api Mpeg2 Intra Dc Precision Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-intra-dc-precision-structure
- name: Mediaconvert Api Mpeg2 Par Control Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-par-control-structure
- name: Mediaconvert Api Mpeg2 Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-quality-tuning-level-structure
- name: Mediaconvert Api Mpeg2 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-rate-control-mode-structure
- name: Mediaconvert Api Mpeg2 Scan Type Conversion Mode Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-scan-type-conversion-mode-structure
- name: Mediaconvert Api Mpeg2 Scene Change Detect Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-scene-change-detect-structure
- name: Mediaconvert Api Mpeg2 Settings Structure
  property_count: 33
  slug: mediaconvert-api-mpeg2-settings-structure
- name: Mediaconvert Api Mpeg2 Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-slow-pal-structure
- name: Mediaconvert Api Mpeg2 Spatial Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-spatial-adaptive-quantization-structure
- name: Mediaconvert Api Mpeg2 Syntax Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-syntax-structure
- name: Mediaconvert Api Mpeg2 Telecine Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-telecine-structure
- name: Mediaconvert Api Mpeg2 Temporal Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-mpeg2-temporal-adaptive-quantization-structure
- name: Mediaconvert Api Ms Smooth Additional Manifest Structure
  property_count: 2
  slug: mediaconvert-api-ms-smooth-additional-manifest-structure
- name: Mediaconvert Api Ms Smooth Audio Deduplication Structure
  property_count: 0
  slug: mediaconvert-api-ms-smooth-audio-deduplication-structure
- name: Mediaconvert Api Ms Smooth Encryption Settings Structure
  property_count: 1
  slug: mediaconvert-api-ms-smooth-encryption-settings-structure
- name: Mediaconvert Api Ms Smooth Fragment Length Control Structure
  property_count: 0
  slug: mediaconvert-api-ms-smooth-fragment-length-control-structure
- name: Mediaconvert Api Ms Smooth Group Settings Structure
  property_count: 8
  slug: mediaconvert-api-ms-smooth-group-settings-structure
- name: Mediaconvert Api Ms Smooth Manifest Encoding Structure
  property_count: 0
  slug: mediaconvert-api-ms-smooth-manifest-encoding-structure
- name: Mediaconvert Api Mxf Afd Signaling Structure
  property_count: 0
  slug: mediaconvert-api-mxf-afd-signaling-structure
- name: Mediaconvert Api Mxf Profile Structure
  property_count: 0
  slug: mediaconvert-api-mxf-profile-structure
- name: Mediaconvert Api Mxf Settings Structure
  property_count: 3
  slug: mediaconvert-api-mxf-settings-structure
- name: Mediaconvert Api Mxf Xavc Duration Mode Structure
  property_count: 0
  slug: mediaconvert-api-mxf-xavc-duration-mode-structure
- name: Mediaconvert Api Mxf Xavc Profile Settings Structure
  property_count: 2
  slug: mediaconvert-api-mxf-xavc-profile-settings-structure
- name: Mediaconvert Api Nex Guard File Marker Settings Structure
  property_count: 4
  slug: mediaconvert-api-nex-guard-file-marker-settings-structure
- name: Mediaconvert Api Nielsen Active Watermark Process Type Structure
  property_count: 0
  slug: mediaconvert-api-nielsen-active-watermark-process-type-structure
- name: Mediaconvert Api Nielsen Configuration Structure
  property_count: 2
  slug: mediaconvert-api-nielsen-configuration-structure
- name: Mediaconvert Api Nielsen Non Linear Watermark Settings Structure
  property_count: 11
  slug: mediaconvert-api-nielsen-non-linear-watermark-settings-structure
- name: Mediaconvert Api Nielsen Source Watermark Status Type Structure
  property_count: 0
  slug: mediaconvert-api-nielsen-source-watermark-status-type-structure
- name: Mediaconvert Api Nielsen Unique Tic Per Audio Track Type Structure
  property_count: 0
  slug: mediaconvert-api-nielsen-unique-tic-per-audio-track-type-structure
- name: Mediaconvert Api Noise Filter Post Temporal Sharpening Strength Structure
  property_count: 0
  slug: mediaconvert-api-noise-filter-post-temporal-sharpening-strength-structure
- name: Mediaconvert Api Noise Filter Post Temporal Sharpening Structure
  property_count: 0
  slug: mediaconvert-api-noise-filter-post-temporal-sharpening-structure
- name: Mediaconvert Api Noise Reducer Filter Settings Structure
  property_count: 1
  slug: mediaconvert-api-noise-reducer-filter-settings-structure
- name: Mediaconvert Api Noise Reducer Filter Structure
  property_count: 0
  slug: mediaconvert-api-noise-reducer-filter-structure
- name: Mediaconvert Api Noise Reducer Spatial Filter Settings Structure
  property_count: 3
  slug: mediaconvert-api-noise-reducer-spatial-filter-settings-structure
- name: Mediaconvert Api Noise Reducer Structure
  property_count: 4
  slug: mediaconvert-api-noise-reducer-structure
- name: Mediaconvert Api Noise Reducer Temporal Filter Settings Structure
  property_count: 5
  slug: mediaconvert-api-noise-reducer-temporal-filter-settings-structure
- name: Mediaconvert Api Opus Settings Structure
  property_count: 3
  slug: mediaconvert-api-opus-settings-structure
- name: Mediaconvert Api Order Structure
  property_count: 0
  slug: mediaconvert-api-order-structure
- name: Mediaconvert Api Output Channel Mapping Structure
  property_count: 2
  slug: mediaconvert-api-output-channel-mapping-structure
- name: Mediaconvert Api Output Detail Structure
  property_count: 2
  slug: mediaconvert-api-output-detail-structure
- name: Mediaconvert Api Output Group Detail Structure
  property_count: 1
  slug: mediaconvert-api-output-group-detail-structure
- name: Mediaconvert Api Output Group Settings Structure
  property_count: 6
  slug: mediaconvert-api-output-group-settings-structure
- name: Mediaconvert Api Output Group Structure
  property_count: 5
  slug: mediaconvert-api-output-group-structure
- name: Mediaconvert Api Output Group Type Structure
  property_count: 0
  slug: mediaconvert-api-output-group-type-structure
- name: Mediaconvert Api Output Sdt Structure
  property_count: 0
  slug: mediaconvert-api-output-sdt-structure
- name: Mediaconvert Api Output Settings Structure
  property_count: 1
  slug: mediaconvert-api-output-settings-structure
- name: Mediaconvert Api Output Structure
  property_count: 8
  slug: mediaconvert-api-output-structure
- name: Mediaconvert Api Pad Video Structure
  property_count: 0
  slug: mediaconvert-api-pad-video-structure
- name: Mediaconvert Api Partner Watermarking Structure
  property_count: 1
  slug: mediaconvert-api-partner-watermarking-structure
- name: Mediaconvert Api Policy Structure
  property_count: 3
  slug: mediaconvert-api-policy-structure
- name: Mediaconvert Api Preset List By Structure
  property_count: 0
  slug: mediaconvert-api-preset-list-by-structure
- name: Mediaconvert Api Preset Settings Structure
  property_count: 4
  slug: mediaconvert-api-preset-settings-structure
- name: Mediaconvert Api Preset Structure
  property_count: 8
  slug: mediaconvert-api-preset-structure
- name: Mediaconvert Api Pricing Plan Structure
  property_count: 0
  slug: mediaconvert-api-pricing-plan-structure
- name: Mediaconvert Api Prores Chroma Sampling Structure
  property_count: 0
  slug: mediaconvert-api-prores-chroma-sampling-structure
- name: Mediaconvert Api Prores Codec Profile Structure
  property_count: 0
  slug: mediaconvert-api-prores-codec-profile-structure
- name: Mediaconvert Api Prores Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-prores-framerate-control-structure
- name: Mediaconvert Api Prores Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-prores-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Prores Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-prores-interlace-mode-structure
- name: Mediaconvert Api Prores Par Control Structure
  property_count: 0
  slug: mediaconvert-api-prores-par-control-structure
- name: Mediaconvert Api Prores Scan Type Conversion Mode Structure
  property_count: 0
  slug: mediaconvert-api-prores-scan-type-conversion-mode-structure
- name: Mediaconvert Api Prores Settings Structure
  property_count: 13
  slug: mediaconvert-api-prores-settings-structure
- name: Mediaconvert Api Prores Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-prores-slow-pal-structure
- name: Mediaconvert Api Prores Telecine Structure
  property_count: 0
  slug: mediaconvert-api-prores-telecine-structure
- name: Mediaconvert Api Put Policy Request Structure
  property_count: 1
  slug: mediaconvert-api-put-policy-request-structure
- name: Mediaconvert Api Put Policy Response Structure
  property_count: 1
  slug: mediaconvert-api-put-policy-response-structure
- name: Mediaconvert Api Queue List By Structure
  property_count: 0
  slug: mediaconvert-api-queue-list-by-structure
- name: Mediaconvert Api Queue Status Structure
  property_count: 0
  slug: mediaconvert-api-queue-status-structure
- name: Mediaconvert Api Queue Structure
  property_count: 11
  slug: mediaconvert-api-queue-structure
- name: Mediaconvert Api Queue Transition Structure
  property_count: 3
  slug: mediaconvert-api-queue-transition-structure
- name: Mediaconvert Api Rectangle Structure
  property_count: 4
  slug: mediaconvert-api-rectangle-structure
- name: Mediaconvert Api Remix Settings Structure
  property_count: 3
  slug: mediaconvert-api-remix-settings-structure
- name: Mediaconvert Api Renewal Type Structure
  property_count: 0
  slug: mediaconvert-api-renewal-type-structure
- name: Mediaconvert Api Required Flag Structure
  property_count: 0
  slug: mediaconvert-api-required-flag-structure
- name: Mediaconvert Api Reservation Plan Settings Structure
  property_count: 3
  slug: mediaconvert-api-reservation-plan-settings-structure
- name: Mediaconvert Api Reservation Plan Status Structure
  property_count: 0
  slug: mediaconvert-api-reservation-plan-status-structure
- name: Mediaconvert Api Reservation Plan Structure
  property_count: 6
  slug: mediaconvert-api-reservation-plan-structure
- name: Mediaconvert Api Resource Tags Structure
  property_count: 2
  slug: mediaconvert-api-resource-tags-structure
- name: Mediaconvert Api Respond To Afd Structure
  property_count: 0
  slug: mediaconvert-api-respond-to-afd-structure
- name: Mediaconvert Api Rule Type Structure
  property_count: 0
  slug: mediaconvert-api-rule-type-structure
- name: Mediaconvert Api S3 Destination Access Control Structure
  property_count: 1
  slug: mediaconvert-api-s3-destination-access-control-structure
- name: Mediaconvert Api S3 Destination Settings Structure
  property_count: 2
  slug: mediaconvert-api-s3-destination-settings-structure
- name: Mediaconvert Api S3 Encryption Settings Structure
  property_count: 3
  slug: mediaconvert-api-s3-encryption-settings-structure
- name: Mediaconvert Api S3 Object Canned Acl Structure
  property_count: 0
  slug: mediaconvert-api-s3-object-canned-acl-structure
- name: Mediaconvert Api S3 Server Side Encryption Type Structure
  property_count: 0
  slug: mediaconvert-api-s3-server-side-encryption-type-structure
- name: Mediaconvert Api Sample Range Conversion Structure
  property_count: 0
  slug: mediaconvert-api-sample-range-conversion-structure
- name: Mediaconvert Api Scaling Behavior Structure
  property_count: 0
  slug: mediaconvert-api-scaling-behavior-structure
- name: Mediaconvert Api Scc Destination Framerate Structure
  property_count: 0
  slug: mediaconvert-api-scc-destination-framerate-structure
- name: Mediaconvert Api Scc Destination Settings Structure
  property_count: 1
  slug: mediaconvert-api-scc-destination-settings-structure
- name: Mediaconvert Api Simulate Reserved Queue Structure
  property_count: 0
  slug: mediaconvert-api-simulate-reserved-queue-structure
- name: Mediaconvert Api Speke Key Provider Cmaf Structure
  property_count: 5
  slug: mediaconvert-api-speke-key-provider-cmaf-structure
- name: Mediaconvert Api Speke Key Provider Structure
  property_count: 4
  slug: mediaconvert-api-speke-key-provider-structure
- name: Mediaconvert Api Srt Destination Settings Structure
  property_count: 1
  slug: mediaconvert-api-srt-destination-settings-structure
- name: Mediaconvert Api Srt Style Passthrough Structure
  property_count: 0
  slug: mediaconvert-api-srt-style-passthrough-structure
- name: Mediaconvert Api Static Key Provider Structure
  property_count: 4
  slug: mediaconvert-api-static-key-provider-structure
- name: Mediaconvert Api Status Update Interval Structure
  property_count: 0
  slug: mediaconvert-api-status-update-interval-structure
- name: Mediaconvert Api Tag Resource Request Structure
  property_count: 2
  slug: mediaconvert-api-tag-resource-request-structure
- name: Mediaconvert Api Tag Resource Response Structure
  property_count: 0
  slug: mediaconvert-api-tag-resource-response-structure
- name: Mediaconvert Api Teletext Destination Settings Structure
  property_count: 2
  slug: mediaconvert-api-teletext-destination-settings-structure
- name: Mediaconvert Api Teletext Page Type Structure
  property_count: 0
  slug: mediaconvert-api-teletext-page-type-structure
- name: Mediaconvert Api Teletext Source Settings Structure
  property_count: 1
  slug: mediaconvert-api-teletext-source-settings-structure
- name: Mediaconvert Api Timecode Burnin Position Structure
  property_count: 0
  slug: mediaconvert-api-timecode-burnin-position-structure
- name: Mediaconvert Api Timecode Burnin Structure
  property_count: 3
  slug: mediaconvert-api-timecode-burnin-structure
- name: Mediaconvert Api Timecode Config Structure
  property_count: 4
  slug: mediaconvert-api-timecode-config-structure
- name: Mediaconvert Api Timecode Source Structure
  property_count: 0
  slug: mediaconvert-api-timecode-source-structure
- name: Mediaconvert Api Timed Metadata Insertion Structure
  property_count: 1
  slug: mediaconvert-api-timed-metadata-insertion-structure
- name: Mediaconvert Api Timed Metadata Structure
  property_count: 0
  slug: mediaconvert-api-timed-metadata-structure
- name: Mediaconvert Api Timing Structure
  property_count: 3
  slug: mediaconvert-api-timing-structure
- name: Mediaconvert Api Track Source Settings Structure
  property_count: 1
  slug: mediaconvert-api-track-source-settings-structure
- name: Mediaconvert Api Ttml Destination Settings Structure
  property_count: 1
  slug: mediaconvert-api-ttml-destination-settings-structure
- name: Mediaconvert Api Ttml Style Passthrough Structure
  property_count: 0
  slug: mediaconvert-api-ttml-style-passthrough-structure
- name: Mediaconvert Api Type Structure
  property_count: 0
  slug: mediaconvert-api-type-structure
- name: Mediaconvert Api Untag Resource Request Structure
  property_count: 1
  slug: mediaconvert-api-untag-resource-request-structure
- name: Mediaconvert Api Untag Resource Response Structure
  property_count: 0
  slug: mediaconvert-api-untag-resource-response-structure
- name: Mediaconvert Api Update Job Template Request Structure
  property_count: 8
  slug: mediaconvert-api-update-job-template-request-structure
- name: Mediaconvert Api Update Job Template Response Structure
  property_count: 1
  slug: mediaconvert-api-update-job-template-response-structure
- name: Mediaconvert Api Update Preset Request Structure
  property_count: 3
  slug: mediaconvert-api-update-preset-request-structure
- name: Mediaconvert Api Update Preset Response Structure
  property_count: 1
  slug: mediaconvert-api-update-preset-response-structure
- name: Mediaconvert Api Update Queue Request Structure
  property_count: 3
  slug: mediaconvert-api-update-queue-request-structure
- name: Mediaconvert Api Update Queue Response Structure
  property_count: 1
  slug: mediaconvert-api-update-queue-response-structure
- name: Mediaconvert Api Vc3 Class Structure
  property_count: 0
  slug: mediaconvert-api-vc3-class-structure
- name: Mediaconvert Api Vc3 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-vc3-framerate-control-structure
- name: Mediaconvert Api Vc3 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-vc3-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Vc3 Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-vc3-interlace-mode-structure
- name: Mediaconvert Api Vc3 Scan Type Conversion Mode Structure
  property_count: 0
  slug: mediaconvert-api-vc3-scan-type-conversion-mode-structure
- name: Mediaconvert Api Vc3 Settings Structure
  property_count: 9
  slug: mediaconvert-api-vc3-settings-structure
- name: Mediaconvert Api Vc3 Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-vc3-slow-pal-structure
- name: Mediaconvert Api Vc3 Telecine Structure
  property_count: 0
  slug: mediaconvert-api-vc3-telecine-structure
- name: Mediaconvert Api Vchip Action Structure
  property_count: 0
  slug: mediaconvert-api-vchip-action-structure
- name: Mediaconvert Api Video Codec Settings Structure
  property_count: 12
  slug: mediaconvert-api-video-codec-settings-structure
- name: Mediaconvert Api Video Codec Structure
  property_count: 0
  slug: mediaconvert-api-video-codec-structure
- name: Mediaconvert Api Video Description Structure
  property_count: 15
  slug: mediaconvert-api-video-description-structure
- name: Mediaconvert Api Video Detail Structure
  property_count: 2
  slug: mediaconvert-api-video-detail-structure
- name: Mediaconvert Api Video Preprocessor Structure
  property_count: 8
  slug: mediaconvert-api-video-preprocessor-structure
- name: Mediaconvert Api Video Selector Structure
  property_count: 10
  slug: mediaconvert-api-video-selector-structure
- name: Mediaconvert Api Video Timecode Insertion Structure
  property_count: 0
  slug: mediaconvert-api-video-timecode-insertion-structure
- name: Mediaconvert Api Vorbis Settings Structure
  property_count: 3
  slug: mediaconvert-api-vorbis-settings-structure
- name: Mediaconvert Api Vp8 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-vp8-framerate-control-structure
- name: Mediaconvert Api Vp8 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-vp8-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Vp8 Par Control Structure
  property_count: 0
  slug: mediaconvert-api-vp8-par-control-structure
- name: Mediaconvert Api Vp8 Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-vp8-quality-tuning-level-structure
- name: Mediaconvert Api Vp8 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-vp8-rate-control-mode-structure
- name: Mediaconvert Api Vp8 Settings Structure
  property_count: 13
  slug: mediaconvert-api-vp8-settings-structure
- name: Mediaconvert Api Vp9 Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-vp9-framerate-control-structure
- name: Mediaconvert Api Vp9 Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-vp9-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Vp9 Par Control Structure
  property_count: 0
  slug: mediaconvert-api-vp9-par-control-structure
- name: Mediaconvert Api Vp9 Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-vp9-quality-tuning-level-structure
- name: Mediaconvert Api Vp9 Rate Control Mode Structure
  property_count: 0
  slug: mediaconvert-api-vp9-rate-control-mode-structure
- name: Mediaconvert Api Vp9 Settings Structure
  property_count: 13
  slug: mediaconvert-api-vp9-settings-structure
- name: Mediaconvert Api Warning Group Structure
  property_count: 2
  slug: mediaconvert-api-warning-group-structure
- name: Mediaconvert Api Watermarking Strength Structure
  property_count: 0
  slug: mediaconvert-api-watermarking-strength-structure
- name: Mediaconvert Api Wav Format Structure
  property_count: 0
  slug: mediaconvert-api-wav-format-structure
- name: Mediaconvert Api Wav Settings Structure
  property_count: 4
  slug: mediaconvert-api-wav-settings-structure
- name: Mediaconvert Api Webvtt Accessibility Subs Structure
  property_count: 0
  slug: mediaconvert-api-webvtt-accessibility-subs-structure
- name: Mediaconvert Api Webvtt Destination Settings Structure
  property_count: 2
  slug: mediaconvert-api-webvtt-destination-settings-structure
- name: Mediaconvert Api Webvtt Hls Source Settings Structure
  property_count: 3
  slug: mediaconvert-api-webvtt-hls-source-settings-structure
- name: Mediaconvert Api Webvtt Style Passthrough Structure
  property_count: 0
  slug: mediaconvert-api-webvtt-style-passthrough-structure
- name: Mediaconvert Api Xavc Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-xavc-adaptive-quantization-structure
- name: Mediaconvert Api Xavc Entropy Encoding Structure
  property_count: 0
  slug: mediaconvert-api-xavc-entropy-encoding-structure
- name: Mediaconvert Api Xavc Flicker Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-xavc-flicker-adaptive-quantization-structure
- name: Mediaconvert Api Xavc Framerate Control Structure
  property_count: 0
  slug: mediaconvert-api-xavc-framerate-control-structure
- name: Mediaconvert Api Xavc Framerate Conversion Algorithm Structure
  property_count: 0
  slug: mediaconvert-api-xavc-framerate-conversion-algorithm-structure
- name: Mediaconvert Api Xavc Gop B Reference Structure
  property_count: 0
  slug: mediaconvert-api-xavc-gop-b-reference-structure
- name: Mediaconvert Api Xavc Hd Intra Cbg Profile Class Structure
  property_count: 0
  slug: mediaconvert-api-xavc-hd-intra-cbg-profile-class-structure
- name: Mediaconvert Api Xavc Hd Intra Cbg Profile Settings Structure
  property_count: 1
  slug: mediaconvert-api-xavc-hd-intra-cbg-profile-settings-structure
- name: Mediaconvert Api Xavc Hd Profile Bitrate Class Structure
  property_count: 0
  slug: mediaconvert-api-xavc-hd-profile-bitrate-class-structure
- name: Mediaconvert Api Xavc Hd Profile Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-xavc-hd-profile-quality-tuning-level-structure
- name: Mediaconvert Api Xavc Hd Profile Settings Structure
  property_count: 9
  slug: mediaconvert-api-xavc-hd-profile-settings-structure
- name: Mediaconvert Api Xavc Hd Profile Telecine Structure
  property_count: 0
  slug: mediaconvert-api-xavc-hd-profile-telecine-structure
- name: Mediaconvert Api Xavc Interlace Mode Structure
  property_count: 0
  slug: mediaconvert-api-xavc-interlace-mode-structure
- name: Mediaconvert Api Xavc Profile Structure
  property_count: 0
  slug: mediaconvert-api-xavc-profile-structure
- name: Mediaconvert Api Xavc Settings Structure
  property_count: 16
  slug: mediaconvert-api-xavc-settings-structure
- name: Mediaconvert Api Xavc Slow Pal Structure
  property_count: 0
  slug: mediaconvert-api-xavc-slow-pal-structure
- name: Mediaconvert Api Xavc Spatial Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-xavc-spatial-adaptive-quantization-structure
- name: Mediaconvert Api Xavc Temporal Adaptive Quantization Structure
  property_count: 0
  slug: mediaconvert-api-xavc-temporal-adaptive-quantization-structure
- name: Mediaconvert Api Xavc4K Intra Cbg Profile Class Structure
  property_count: 0
  slug: mediaconvert-api-xavc4k-intra-cbg-profile-class-structure
- name: Mediaconvert Api Xavc4K Intra Cbg Profile Settings Structure
  property_count: 1
  slug: mediaconvert-api-xavc4k-intra-cbg-profile-settings-structure
- name: Mediaconvert Api Xavc4K Intra Vbr Profile Class Structure
  property_count: 0
  slug: mediaconvert-api-xavc4k-intra-vbr-profile-class-structure
- name: Mediaconvert Api Xavc4K Intra Vbr Profile Settings Structure
  property_count: 1
  slug: mediaconvert-api-xavc4k-intra-vbr-profile-settings-structure
- name: Mediaconvert Api Xavc4K Profile Bitrate Class Structure
  property_count: 0
  slug: mediaconvert-api-xavc4k-profile-bitrate-class-structure
- name: Mediaconvert Api Xavc4K Profile Codec Profile Structure
  property_count: 0
  slug: mediaconvert-api-xavc4k-profile-codec-profile-structure
- name: Mediaconvert Api Xavc4K Profile Quality Tuning Level Structure
  property_count: 0
  slug: mediaconvert-api-xavc4k-profile-quality-tuning-level-structure
- name: Mediaconvert Api Xavc4K Profile Settings Structure
  property_count: 8
  slug: mediaconvert-api-xavc4k-profile-settings-structure
jsonld:
- class_count: 637
  name: Amazon Mediaconvert Mediaconvert Api Context
  property_count: 646
  slug: amazon-mediaconvert-mediaconvert-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MediaConvert
nav: Providers
network: true
overview: 'Amazon MediaConvert publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Endpoints API, Jobs API, and 5 more. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MediaConvert catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MediaConvert''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Mediaconvert Plans Pricing
  plan_count: 3
  slug: amazon-mediaconvert-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Amazon Mediaconvert Rate Limits
  slug: amazon-mediaconvert-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon MediaConvert API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-mediaconvert-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon MediaConvert API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 12
  slug: amazon-mediaconvert-spectral-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 68.7
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-mediaconvert/refs/heads/main/screenshots/amazon-mediaconvert-2026-06-20T171740.png
security:
- kind: authentication
  name: Amazon Mediaconvert Authentication
  slug: amazon-mediaconvert-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Mediaconvert Domain Security
  slug: amazon-mediaconvert-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Mediaconvert Vulnerability Disclosure
  slug: amazon-mediaconvert-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Mediaconvert Trust Center
  slug: amazon-mediaconvert-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-mediaconvert
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Transcode video files for video-on-demand delivery at broadcast quality.
  name: VOD Content Production
- description: Process large content libraries for multiscreen delivery at any scale.
  name: Large Library Transcoding
- description: Create broadcast-format outputs for television and streaming platform distribution.
  name: Broadcast Distribution
- description: Handle variable transcoding workloads with elastic auto-scaling.
  name: Peak Workload Processing
website: https://aws.amazon.com/mediaconvert/
---
