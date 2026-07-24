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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Amazon Mediatailor Agentic Access
  operation_count: 44
  slug: amazon-mediatailor-agentic-access
  summary_line: 44 operations · 28 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The Alerts#resourceArn API from Amazon MediaTailor — 1 operation(s) for alerts#resourcearn.
  name: Amazon MediaTailor Alerts#resourceArn API
  slug: amazon-mediatailor-alerts-resourcearn-api
- description: The Channel API from Amazon MediaTailor — 6 operation(s) for channel.
  name: Amazon MediaTailor Channel API
  slug: amazon-mediatailor-channel-api
- description: The Channels API from Amazon MediaTailor — 1 operation(s) for channels.
  name: Amazon MediaTailor Channels API
  slug: amazon-mediatailor-channels-api
- description: The ConfigureLogs API from Amazon MediaTailor — 2 operation(s) for configurelogs.
  name: Amazon MediaTailor ConfigureLogs API
  slug: amazon-mediatailor-configurelogs-api
- description: The PlaybackConfiguration API from Amazon MediaTailor — 2 operation(s) for playbackconfiguration.
  name: Amazon MediaTailor PlaybackConfiguration API
  slug: amazon-mediatailor-playbackconfiguration-api
- description: The PlaybackConfigurations API from Amazon MediaTailor — 1 operation(s) for playbackconfigurations.
  name: Amazon MediaTailor PlaybackConfigurations API
  slug: amazon-mediatailor-playbackconfigurations-api
- description: The PrefetchSchedule API from Amazon MediaTailor — 2 operation(s) for prefetchschedule.
  name: Amazon MediaTailor PrefetchSchedule API
  slug: amazon-mediatailor-prefetchschedule-api
- description: The SourceLocation API from Amazon MediaTailor — 5 operation(s) for sourcelocation.
  name: Amazon MediaTailor SourceLocation API
  slug: amazon-mediatailor-sourcelocation-api
- description: The SourceLocations API from Amazon MediaTailor — 1 operation(s) for sourcelocations.
  name: Amazon MediaTailor SourceLocations API
  slug: amazon-mediatailor-sourcelocations-api
- description: The Tags API from Amazon MediaTailor — 2 operation(s) for tags.
  name: Amazon MediaTailor Tags API
  slug: amazon-mediatailor-tags-api
artifact_total: 490
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-mediatailor-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-mediatailor-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-mediatailor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-mediatailor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-mediatailor-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/mediatailor/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediatailor/
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
  url: https://console.aws.amazon.com/mediatailor/
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
  url: rules/amazon-mediatailor-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediatailor-vocabulary.yaml
created: '2026-03-16'
description: AWS Elemental MediaTailor is a channel assembly and personalized ad-insertion service that enables you to monetize your video content with server-side targeted advertising while maintaining broadcast-quality.
examples:
- key_count: 2
  name: Mediatailor Api Access Configuration Example
  slug: mediatailor-api-access-configuration-example
- key_count: 0
  name: Mediatailor Api Access Type Example
  slug: mediatailor-api-access-type-example
- key_count: 5
  name: Mediatailor Api Ad Break Example
  slug: mediatailor-api-ad-break-example
- key_count: 1
  name: Mediatailor Api Ad Marker Passthrough Example
  slug: mediatailor-api-ad-marker-passthrough-example
- key_count: 5
  name: Mediatailor Api Alert Example
  slug: mediatailor-api-alert-example
- key_count: 2
  name: Mediatailor Api Avail Matching Criteria Example
  slug: mediatailor-api-avail-matching-criteria-example
- key_count: 2
  name: Mediatailor Api Avail Suppression Example
  slug: mediatailor-api-avail-suppression-example
- key_count: 2
  name: Mediatailor Api Bumper Example
  slug: mediatailor-api-bumper-example
- key_count: 2
  name: Mediatailor Api Cdn Configuration Example
  slug: mediatailor-api-cdn-configuration-example
- key_count: 11
  name: Mediatailor Api Channel Example
  slug: mediatailor-api-channel-example
- key_count: 0
  name: Mediatailor Api Channel State Example
  slug: mediatailor-api-channel-state-example
- key_count: 1
  name: Mediatailor Api Clip Range Example
  slug: mediatailor-api-clip-range-example
- key_count: 0
  name: Mediatailor Api Configuration Aliases Request Example
  slug: mediatailor-api-configuration-aliases-request-example
- key_count: 0
  name: Mediatailor Api Configuration Aliases Response Example
  slug: mediatailor-api-configuration-aliases-response-example
- key_count: 2
  name: Mediatailor Api Configure Logs For Channel Request Example
  slug: mediatailor-api-configure-logs-for-channel-request-example
- key_count: 2
  name: Mediatailor Api Configure Logs For Channel Response Example
  slug: mediatailor-api-configure-logs-for-channel-response-example
- key_count: 2
  name: Mediatailor Api Configure Logs For Playback Configuration Request Example
  slug: mediatailor-api-configure-logs-for-playback-configuration-request-example
- key_count: 2
  name: Mediatailor Api Configure Logs For Playback Configuration Response Example
  slug: mediatailor-api-configure-logs-for-playback-configuration-response-example
- key_count: 5
  name: Mediatailor Api Create Channel Request Example
  slug: mediatailor-api-create-channel-request-example
- key_count: 10
  name: Mediatailor Api Create Channel Response Example
  slug: mediatailor-api-create-channel-response-example
- key_count: 2
  name: Mediatailor Api Create Live Source Request Example
  slug: mediatailor-api-create-live-source-request-example
- key_count: 7
  name: Mediatailor Api Create Live Source Response Example
  slug: mediatailor-api-create-live-source-response-example
- key_count: 3
  name: Mediatailor Api Create Prefetch Schedule Request Example
  slug: mediatailor-api-create-prefetch-schedule-request-example
- key_count: 6
  name: Mediatailor Api Create Prefetch Schedule Response Example
  slug: mediatailor-api-create-prefetch-schedule-response-example
- key_count: 5
  name: Mediatailor Api Create Program Request Example
  slug: mediatailor-api-create-program-request-example
- key_count: 11
  name: Mediatailor Api Create Program Response Example
  slug: mediatailor-api-create-program-response-example
- key_count: 5
  name: Mediatailor Api Create Source Location Request Example
  slug: mediatailor-api-create-source-location-request-example
- key_count: 9
  name: Mediatailor Api Create Source Location Response Example
  slug: mediatailor-api-create-source-location-response-example
- key_count: 2
  name: Mediatailor Api Create Vod Source Request Example
  slug: mediatailor-api-create-vod-source-request-example
- key_count: 7
  name: Mediatailor Api Create Vod Source Response Example
  slug: mediatailor-api-create-vod-source-response-example
- key_count: 3
  name: Mediatailor Api Dash Configuration Example
  slug: mediatailor-api-dash-configuration-example
- key_count: 2
  name: Mediatailor Api Dash Configuration For Put Example
  slug: mediatailor-api-dash-configuration-for-put-example
- key_count: 4
  name: Mediatailor Api Dash Playlist Settings Example
  slug: mediatailor-api-dash-playlist-settings-example
- key_count: 1
  name: Mediatailor Api Default Segment Delivery Configuration Example
  slug: mediatailor-api-default-segment-delivery-configuration-example
- key_count: 0
  name: Mediatailor Api Delete Channel Policy Request Example
  slug: mediatailor-api-delete-channel-policy-request-example
- key_count: 0
  name: Mediatailor Api Delete Channel Policy Response Example
  slug: mediatailor-api-delete-channel-policy-response-example
- key_count: 0
  name: Mediatailor Api Delete Channel Request Example
  slug: mediatailor-api-delete-channel-request-example
- key_count: 0
  name: Mediatailor Api Delete Channel Response Example
  slug: mediatailor-api-delete-channel-response-example
- key_count: 0
  name: Mediatailor Api Delete Live Source Request Example
  slug: mediatailor-api-delete-live-source-request-example
- key_count: 0
  name: Mediatailor Api Delete Live Source Response Example
  slug: mediatailor-api-delete-live-source-response-example
- key_count: 0
  name: Mediatailor Api Delete Playback Configuration Request Example
  slug: mediatailor-api-delete-playback-configuration-request-example
- key_count: 0
  name: Mediatailor Api Delete Playback Configuration Response Example
  slug: mediatailor-api-delete-playback-configuration-response-example
- key_count: 0
  name: Mediatailor Api Delete Prefetch Schedule Request Example
  slug: mediatailor-api-delete-prefetch-schedule-request-example
- key_count: 0
  name: Mediatailor Api Delete Prefetch Schedule Response Example
  slug: mediatailor-api-delete-prefetch-schedule-response-example
- key_count: 0
  name: Mediatailor Api Delete Program Request Example
  slug: mediatailor-api-delete-program-request-example
- key_count: 0
  name: Mediatailor Api Delete Program Response Example
  slug: mediatailor-api-delete-program-response-example
- key_count: 0
  name: Mediatailor Api Delete Source Location Request Example
  slug: mediatailor-api-delete-source-location-request-example
- key_count: 0
  name: Mediatailor Api Delete Source Location Response Example
  slug: mediatailor-api-delete-source-location-response-example
- key_count: 0
  name: Mediatailor Api Delete Vod Source Request Example
  slug: mediatailor-api-delete-vod-source-request-example
- key_count: 0
  name: Mediatailor Api Delete Vod Source Response Example
  slug: mediatailor-api-delete-vod-source-response-example
- key_count: 0
  name: Mediatailor Api Describe Channel Request Example
  slug: mediatailor-api-describe-channel-request-example
- key_count: 11
  name: Mediatailor Api Describe Channel Response Example
  slug: mediatailor-api-describe-channel-response-example
- key_count: 0
  name: Mediatailor Api Describe Live Source Request Example
  slug: mediatailor-api-describe-live-source-request-example
- key_count: 7
  name: Mediatailor Api Describe Live Source Response Example
  slug: mediatailor-api-describe-live-source-response-example
- key_count: 0
  name: Mediatailor Api Describe Program Request Example
  slug: mediatailor-api-describe-program-request-example
- key_count: 11
  name: Mediatailor Api Describe Program Response Example
  slug: mediatailor-api-describe-program-response-example
- key_count: 0
  name: Mediatailor Api Describe Source Location Request Example
  slug: mediatailor-api-describe-source-location-request-example
- key_count: 9
  name: Mediatailor Api Describe Source Location Response Example
  slug: mediatailor-api-describe-source-location-response-example
- key_count: 0
  name: Mediatailor Api Describe Vod Source Request Example
  slug: mediatailor-api-describe-vod-source-request-example
- key_count: 7
  name: Mediatailor Api Describe Vod Source Response Example
  slug: mediatailor-api-describe-vod-source-response-example
- key_count: 0
  name: Mediatailor Api Get Channel Policy Request Example
  slug: mediatailor-api-get-channel-policy-request-example
- key_count: 1
  name: Mediatailor Api Get Channel Policy Response Example
  slug: mediatailor-api-get-channel-policy-response-example
- key_count: 0
  name: Mediatailor Api Get Channel Schedule Request Example
  slug: mediatailor-api-get-channel-schedule-request-example
- key_count: 2
  name: Mediatailor Api Get Channel Schedule Response Example
  slug: mediatailor-api-get-channel-schedule-response-example
- key_count: 0
  name: Mediatailor Api Get Playback Configuration Request Example
  slug: mediatailor-api-get-playback-configuration-request-example
- key_count: 19
  name: Mediatailor Api Get Playback Configuration Response Example
  slug: mediatailor-api-get-playback-configuration-response-example
- key_count: 0
  name: Mediatailor Api Get Prefetch Schedule Request Example
  slug: mediatailor-api-get-prefetch-schedule-request-example
- key_count: 6
  name: Mediatailor Api Get Prefetch Schedule Response Example
  slug: mediatailor-api-get-prefetch-schedule-response-example
- key_count: 1
  name: Mediatailor Api Hls Configuration Example
  slug: mediatailor-api-hls-configuration-example
- key_count: 1
  name: Mediatailor Api Hls Playlist Settings Example
  slug: mediatailor-api-hls-playlist-settings-example
- key_count: 1
  name: Mediatailor Api Http Configuration Example
  slug: mediatailor-api-http-configuration-example
- key_count: 3
  name: Mediatailor Api Http Package Configuration Example
  slug: mediatailor-api-http-package-configuration-example
- key_count: 0
  name: Mediatailor Api Http Package Configurations Example
  slug: mediatailor-api-http-package-configurations-example
- key_count: 0
  name: Mediatailor Api Integer Example
  slug: mediatailor-api-integer-example
- key_count: 0
  name: Mediatailor Api List Alerts Request Example
  slug: mediatailor-api-list-alerts-request-example
- key_count: 2
  name: Mediatailor Api List Alerts Response Example
  slug: mediatailor-api-list-alerts-response-example
- key_count: 0
  name: Mediatailor Api List Channels Request Example
  slug: mediatailor-api-list-channels-request-example
- key_count: 2
  name: Mediatailor Api List Channels Response Example
  slug: mediatailor-api-list-channels-response-example
- key_count: 0
  name: Mediatailor Api List Live Sources Request Example
  slug: mediatailor-api-list-live-sources-request-example
- key_count: 2
  name: Mediatailor Api List Live Sources Response Example
  slug: mediatailor-api-list-live-sources-response-example
- key_count: 0
  name: Mediatailor Api List Playback Configurations Request Example
  slug: mediatailor-api-list-playback-configurations-request-example
- key_count: 2
  name: Mediatailor Api List Playback Configurations Response Example
  slug: mediatailor-api-list-playback-configurations-response-example
- key_count: 3
  name: Mediatailor Api List Prefetch Schedules Request Example
  slug: mediatailor-api-list-prefetch-schedules-request-example
- key_count: 2
  name: Mediatailor Api List Prefetch Schedules Response Example
  slug: mediatailor-api-list-prefetch-schedules-response-example
- key_count: 0
  name: Mediatailor Api List Source Locations Request Example
  slug: mediatailor-api-list-source-locations-request-example
- key_count: 2
  name: Mediatailor Api List Source Locations Response Example
  slug: mediatailor-api-list-source-locations-response-example
- key_count: 0
  name: Mediatailor Api List Tags For Resource Request Example
  slug: mediatailor-api-list-tags-for-resource-request-example
- key_count: 1
  name: Mediatailor Api List Tags For Resource Response Example
  slug: mediatailor-api-list-tags-for-resource-response-example
- key_count: 0
  name: Mediatailor Api List Vod Sources Request Example
  slug: mediatailor-api-list-vod-sources-request-example
- key_count: 2
  name: Mediatailor Api List Vod Sources Response Example
  slug: mediatailor-api-list-vod-sources-response-example
- key_count: 2
  name: Mediatailor Api Live Pre Roll Configuration Example
  slug: mediatailor-api-live-pre-roll-configuration-example
- key_count: 7
  name: Mediatailor Api Live Source Example
  slug: mediatailor-api-live-source-example
- key_count: 1
  name: Mediatailor Api Log Configuration Example
  slug: mediatailor-api-log-configuration-example
- key_count: 1
  name: Mediatailor Api Log Configuration For Channel Example
  slug: mediatailor-api-log-configuration-for-channel-example
- key_count: 0
  name: Mediatailor Api Log Type Example
  slug: mediatailor-api-log-type-example
- key_count: 0
  name: Mediatailor Api Log Types Example
  slug: mediatailor-api-log-types-example
- key_count: 0
  name: Mediatailor Api Long Example
  slug: mediatailor-api-long-example
- key_count: 1
  name: Mediatailor Api Manifest Processing Rules Example
  slug: mediatailor-api-manifest-processing-rules-example
- key_count: 0
  name: Mediatailor Api Max Results Example
  slug: mediatailor-api-max-results-example
- key_count: 0
  name: Mediatailor Api Message Type Example
  slug: mediatailor-api-message-type-example
- key_count: 0
  name: Mediatailor Api Mode Example
  slug: mediatailor-api-mode-example
- key_count: 0
  name: Mediatailor Api Operator Example
  slug: mediatailor-api-operator-example
- key_count: 0
  name: Mediatailor Api Origin Manifest Type Example
  slug: mediatailor-api-origin-manifest-type-example
- key_count: 19
  name: Mediatailor Api Playback Configuration Example
  slug: mediatailor-api-playback-configuration-example
- key_count: 0
  name: Mediatailor Api Playback Mode Example
  slug: mediatailor-api-playback-mode-example
- key_count: 3
  name: Mediatailor Api Prefetch Consumption Example
  slug: mediatailor-api-prefetch-consumption-example
- key_count: 3
  name: Mediatailor Api Prefetch Retrieval Example
  slug: mediatailor-api-prefetch-retrieval-example
- key_count: 6
  name: Mediatailor Api Prefetch Schedule Example
  slug: mediatailor-api-prefetch-schedule-example
- key_count: 1
  name: Mediatailor Api Put Channel Policy Request Example
  slug: mediatailor-api-put-channel-policy-request-example
- key_count: 0
  name: Mediatailor Api Put Channel Policy Response Example
  slug: mediatailor-api-put-channel-policy-response-example
- key_count: 14
  name: Mediatailor Api Put Playback Configuration Request Example
  slug: mediatailor-api-put-playback-configuration-request-example
- key_count: 19
  name: Mediatailor Api Put Playback Configuration Response Example
  slug: mediatailor-api-put-playback-configuration-response-example
- key_count: 0
  name: Mediatailor Api Relative Position Example
  slug: mediatailor-api-relative-position-example
- key_count: 4
  name: Mediatailor Api Request Output Item Example
  slug: mediatailor-api-request-output-item-example
- key_count: 0
  name: Mediatailor Api Request Outputs Example
  slug: mediatailor-api-request-outputs-example
- key_count: 5
  name: Mediatailor Api Response Output Item Example
  slug: mediatailor-api-response-output-item-example
- key_count: 0
  name: Mediatailor Api Response Outputs Example
  slug: mediatailor-api-response-outputs-example
- key_count: 4
  name: Mediatailor Api Schedule Ad Break Example
  slug: mediatailor-api-schedule-ad-break-example
- key_count: 2
  name: Mediatailor Api Schedule Configuration Example
  slug: mediatailor-api-schedule-configuration-example
- key_count: 10
  name: Mediatailor Api Schedule Entry Example
  slug: mediatailor-api-schedule-entry-example
- key_count: 0
  name: Mediatailor Api Schedule Entry Type Example
  slug: mediatailor-api-schedule-entry-type-example
- key_count: 3
  name: Mediatailor Api Secrets Manager Access Token Configuration Example
  slug: mediatailor-api-secrets-manager-access-token-configuration-example
- key_count: 2
  name: Mediatailor Api Segment Delivery Configuration Example
  slug: mediatailor-api-segment-delivery-configuration-example
- key_count: 8
  name: Mediatailor Api Segmentation Descriptor Example
  slug: mediatailor-api-segmentation-descriptor-example
- key_count: 0
  name: Mediatailor Api Segmentation Descriptor List Example
  slug: mediatailor-api-segmentation-descriptor-list-example
- key_count: 2
  name: Mediatailor Api Slate Source Example
  slug: mediatailor-api-slate-source-example
- key_count: 9
  name: Mediatailor Api Source Location Example
  slug: mediatailor-api-source-location-example
- key_count: 4
  name: Mediatailor Api Splice Insert Message Example
  slug: mediatailor-api-splice-insert-message-example
- key_count: 0
  name: Mediatailor Api Start Channel Request Example
  slug: mediatailor-api-start-channel-request-example
- key_count: 0
  name: Mediatailor Api Start Channel Response Example
  slug: mediatailor-api-start-channel-response-example
- key_count: 0
  name: Mediatailor Api Stop Channel Request Example
  slug: mediatailor-api-stop-channel-request-example
- key_count: 0
  name: Mediatailor Api Stop Channel Response Example
  slug: mediatailor-api-stop-channel-response-example
- key_count: 0
  name: Mediatailor Api String Example
  slug: mediatailor-api-string-example
- key_count: 1
  name: Mediatailor Api Tag Resource Request Example
  slug: mediatailor-api-tag-resource-request-example
- key_count: 0
  name: Mediatailor Api Tier Example
  slug: mediatailor-api-tier-example
- key_count: 1
  name: Mediatailor Api Time Signal Message Example
  slug: mediatailor-api-time-signal-message-example
- key_count: 5
  name: Mediatailor Api Transition Example
  slug: mediatailor-api-transition-example
- key_count: 0
  name: Mediatailor Api Type Example
  slug: mediatailor-api-type-example
- key_count: 0
  name: Mediatailor Api Untag Resource Request Example
  slug: mediatailor-api-untag-resource-request-example
- key_count: 2
  name: Mediatailor Api Update Channel Request Example
  slug: mediatailor-api-update-channel-request-example
- key_count: 10
  name: Mediatailor Api Update Channel Response Example
  slug: mediatailor-api-update-channel-response-example
- key_count: 1
  name: Mediatailor Api Update Live Source Request Example
  slug: mediatailor-api-update-live-source-request-example
- key_count: 7
  name: Mediatailor Api Update Live Source Response Example
  slug: mediatailor-api-update-live-source-response-example
- key_count: 2
  name: Mediatailor Api Update Program Request Example
  slug: mediatailor-api-update-program-request-example
- key_count: 11
  name: Mediatailor Api Update Program Response Example
  slug: mediatailor-api-update-program-response-example
- key_count: 2
  name: Mediatailor Api Update Program Schedule Configuration Example
  slug: mediatailor-api-update-program-schedule-configuration-example
- key_count: 2
  name: Mediatailor Api Update Program Transition Example
  slug: mediatailor-api-update-program-transition-example
- key_count: 4
  name: Mediatailor Api Update Source Location Request Example
  slug: mediatailor-api-update-source-location-request-example
- key_count: 9
  name: Mediatailor Api Update Source Location Response Example
  slug: mediatailor-api-update-source-location-response-example
- key_count: 1
  name: Mediatailor Api Update Vod Source Request Example
  slug: mediatailor-api-update-vod-source-request-example
- key_count: 7
  name: Mediatailor Api Update Vod Source Response Example
  slug: mediatailor-api-update-vod-source-response-example
- key_count: 7
  name: Mediatailor Api Vod Source Example
  slug: mediatailor-api-vod-source-example
features:
- description: Seamless ad replacement at the server side for consistent viewer experience across devices.
  name: Server-Side Ad Insertion
- description: Insert targeted ads based on viewer demographics, geography, and behavioral data.
  name: Personalized Ad Targeting
- description: Create linear channels from VOD assets and live streams with automated ad scheduling.
  name: Channel Assembly
- description: Connect to any VAST/VPAID-compliant ad decision server for programmatic advertising.
  name: Ad Decision Server Integration
- description: Configure ad insertion parameters, slate, and CDN settings per playback session.
  name: Playback Configuration
finops:
- name: Amazon Mediatailor Finops
  service_category: API
  slug: amazon-mediatailor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-mediatailor.png
integrations:
- description: Ingest packaged live streams for ad insertion.
  name: AWS Elemental MediaPackage
- description: Deliver ad-inserted content via CloudFront with low latency.
  name: Amazon CloudFront
- description: Store VOD source content and slate media assets in S3.
  name: Amazon S3
- description: Monitor ad insertion metrics and playback session data.
  name: Amazon CloudWatch
json_schemas:
- name: AccessConfiguration
  property_count: 2
  slug: mediatailor-api-access-configuration
- name: AccessType
  property_count: 0
  slug: mediatailor-api-access-type
- name: AdBreak
  property_count: 5
  slug: mediatailor-api-ad-break
- name: AdMarkerPassthrough
  property_count: 1
  slug: mediatailor-api-ad-marker-passthrough
- name: Alert
  property_count: 5
  slug: mediatailor-api-alert
- name: AvailMatchingCriteria
  property_count: 2
  slug: mediatailor-api-avail-matching-criteria
- name: AvailSuppression
  property_count: 2
  slug: mediatailor-api-avail-suppression
- name: Bumper
  property_count: 2
  slug: mediatailor-api-bumper
- name: CdnConfiguration
  property_count: 2
  slug: mediatailor-api-cdn-configuration
- name: Channel
  property_count: 11
  slug: mediatailor-api-channel
- name: ChannelState
  property_count: 0
  slug: mediatailor-api-channel-state
- name: ClipRange
  property_count: 1
  slug: mediatailor-api-clip-range
- name: ConfigurationAliasesRequest
  property_count: 0
  slug: mediatailor-api-configuration-aliases-request
- name: ConfigurationAliasesResponse
  property_count: 0
  slug: mediatailor-api-configuration-aliases-response
- name: ConfigureLogsForChannelRequest
  property_count: 2
  slug: mediatailor-api-configure-logs-for-channel-request
- name: ConfigureLogsForChannelResponse
  property_count: 2
  slug: mediatailor-api-configure-logs-for-channel-response
- name: ConfigureLogsForPlaybackConfigurationRequest
  property_count: 2
  slug: mediatailor-api-configure-logs-for-playback-configuration-request
- name: ConfigureLogsForPlaybackConfigurationResponse
  property_count: 2
  slug: mediatailor-api-configure-logs-for-playback-configuration-response
- name: CreateChannelRequest
  property_count: 5
  slug: mediatailor-api-create-channel-request
- name: CreateChannelResponse
  property_count: 10
  slug: mediatailor-api-create-channel-response
- name: CreateLiveSourceRequest
  property_count: 2
  slug: mediatailor-api-create-live-source-request
- name: CreateLiveSourceResponse
  property_count: 7
  slug: mediatailor-api-create-live-source-response
- name: CreatePrefetchScheduleRequest
  property_count: 3
  slug: mediatailor-api-create-prefetch-schedule-request
- name: CreatePrefetchScheduleResponse
  property_count: 6
  slug: mediatailor-api-create-prefetch-schedule-response
- name: CreateProgramRequest
  property_count: 5
  slug: mediatailor-api-create-program-request
- name: CreateProgramResponse
  property_count: 11
  slug: mediatailor-api-create-program-response
- name: CreateSourceLocationRequest
  property_count: 5
  slug: mediatailor-api-create-source-location-request
- name: CreateSourceLocationResponse
  property_count: 9
  slug: mediatailor-api-create-source-location-response
- name: CreateVodSourceRequest
  property_count: 2
  slug: mediatailor-api-create-vod-source-request
- name: CreateVodSourceResponse
  property_count: 7
  slug: mediatailor-api-create-vod-source-response
- name: DashConfigurationForPut
  property_count: 2
  slug: mediatailor-api-dash-configuration-for-put
- name: DashConfiguration
  property_count: 3
  slug: mediatailor-api-dash-configuration
- name: DashPlaylistSettings
  property_count: 4
  slug: mediatailor-api-dash-playlist-settings
- name: DefaultSegmentDeliveryConfiguration
  property_count: 1
  slug: mediatailor-api-default-segment-delivery-configuration
- name: DeleteChannelPolicyRequest
  property_count: 0
  slug: mediatailor-api-delete-channel-policy-request
- name: DeleteChannelPolicyResponse
  property_count: 0
  slug: mediatailor-api-delete-channel-policy-response
- name: DeleteChannelRequest
  property_count: 0
  slug: mediatailor-api-delete-channel-request
- name: DeleteChannelResponse
  property_count: 0
  slug: mediatailor-api-delete-channel-response
- name: DeleteLiveSourceRequest
  property_count: 0
  slug: mediatailor-api-delete-live-source-request
- name: DeleteLiveSourceResponse
  property_count: 0
  slug: mediatailor-api-delete-live-source-response
- name: DeletePlaybackConfigurationRequest
  property_count: 0
  slug: mediatailor-api-delete-playback-configuration-request
- name: DeletePlaybackConfigurationResponse
  property_count: 0
  slug: mediatailor-api-delete-playback-configuration-response
- name: DeletePrefetchScheduleRequest
  property_count: 0
  slug: mediatailor-api-delete-prefetch-schedule-request
- name: DeletePrefetchScheduleResponse
  property_count: 0
  slug: mediatailor-api-delete-prefetch-schedule-response
- name: DeleteProgramRequest
  property_count: 0
  slug: mediatailor-api-delete-program-request
- name: DeleteProgramResponse
  property_count: 0
  slug: mediatailor-api-delete-program-response
- name: DeleteSourceLocationRequest
  property_count: 0
  slug: mediatailor-api-delete-source-location-request
- name: DeleteSourceLocationResponse
  property_count: 0
  slug: mediatailor-api-delete-source-location-response
- name: DeleteVodSourceRequest
  property_count: 0
  slug: mediatailor-api-delete-vod-source-request
- name: DeleteVodSourceResponse
  property_count: 0
  slug: mediatailor-api-delete-vod-source-response
- name: DescribeChannelRequest
  property_count: 0
  slug: mediatailor-api-describe-channel-request
- name: DescribeChannelResponse
  property_count: 11
  slug: mediatailor-api-describe-channel-response
- name: DescribeLiveSourceRequest
  property_count: 0
  slug: mediatailor-api-describe-live-source-request
- name: DescribeLiveSourceResponse
  property_count: 7
  slug: mediatailor-api-describe-live-source-response
- name: DescribeProgramRequest
  property_count: 0
  slug: mediatailor-api-describe-program-request
- name: DescribeProgramResponse
  property_count: 11
  slug: mediatailor-api-describe-program-response
- name: DescribeSourceLocationRequest
  property_count: 0
  slug: mediatailor-api-describe-source-location-request
- name: DescribeSourceLocationResponse
  property_count: 9
  slug: mediatailor-api-describe-source-location-response
- name: DescribeVodSourceRequest
  property_count: 0
  slug: mediatailor-api-describe-vod-source-request
- name: DescribeVodSourceResponse
  property_count: 7
  slug: mediatailor-api-describe-vod-source-response
- name: GetChannelPolicyRequest
  property_count: 0
  slug: mediatailor-api-get-channel-policy-request
- name: GetChannelPolicyResponse
  property_count: 1
  slug: mediatailor-api-get-channel-policy-response
- name: GetChannelScheduleRequest
  property_count: 0
  slug: mediatailor-api-get-channel-schedule-request
- name: GetChannelScheduleResponse
  property_count: 2
  slug: mediatailor-api-get-channel-schedule-response
- name: GetPlaybackConfigurationRequest
  property_count: 0
  slug: mediatailor-api-get-playback-configuration-request
- name: GetPlaybackConfigurationResponse
  property_count: 19
  slug: mediatailor-api-get-playback-configuration-response
- name: GetPrefetchScheduleRequest
  property_count: 0
  slug: mediatailor-api-get-prefetch-schedule-request
- name: GetPrefetchScheduleResponse
  property_count: 6
  slug: mediatailor-api-get-prefetch-schedule-response
- name: HlsConfiguration
  property_count: 1
  slug: mediatailor-api-hls-configuration
- name: HlsPlaylistSettings
  property_count: 1
  slug: mediatailor-api-hls-playlist-settings
- name: HttpConfiguration
  property_count: 1
  slug: mediatailor-api-http-configuration
- name: HttpPackageConfiguration
  property_count: 3
  slug: mediatailor-api-http-package-configuration
- name: HttpPackageConfigurations
  property_count: 0
  slug: mediatailor-api-http-package-configurations
- name: Integer
  property_count: 0
  slug: mediatailor-api-integer
- name: ListAlertsRequest
  property_count: 0
  slug: mediatailor-api-list-alerts-request
- name: ListAlertsResponse
  property_count: 2
  slug: mediatailor-api-list-alerts-response
- name: ListChannelsRequest
  property_count: 0
  slug: mediatailor-api-list-channels-request
- name: ListChannelsResponse
  property_count: 2
  slug: mediatailor-api-list-channels-response
- name: ListLiveSourcesRequest
  property_count: 0
  slug: mediatailor-api-list-live-sources-request
- name: ListLiveSourcesResponse
  property_count: 2
  slug: mediatailor-api-list-live-sources-response
- name: ListPlaybackConfigurationsRequest
  property_count: 0
  slug: mediatailor-api-list-playback-configurations-request
- name: ListPlaybackConfigurationsResponse
  property_count: 2
  slug: mediatailor-api-list-playback-configurations-response
- name: ListPrefetchSchedulesRequest
  property_count: 3
  slug: mediatailor-api-list-prefetch-schedules-request
- name: ListPrefetchSchedulesResponse
  property_count: 2
  slug: mediatailor-api-list-prefetch-schedules-response
- name: ListSourceLocationsRequest
  property_count: 0
  slug: mediatailor-api-list-source-locations-request
- name: ListSourceLocationsResponse
  property_count: 2
  slug: mediatailor-api-list-source-locations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: mediatailor-api-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: mediatailor-api-list-tags-for-resource-response
- name: ListVodSourcesRequest
  property_count: 0
  slug: mediatailor-api-list-vod-sources-request
- name: ListVodSourcesResponse
  property_count: 2
  slug: mediatailor-api-list-vod-sources-response
- name: LivePreRollConfiguration
  property_count: 2
  slug: mediatailor-api-live-pre-roll-configuration
- name: LiveSource
  property_count: 7
  slug: mediatailor-api-live-source
- name: LogConfigurationForChannel
  property_count: 1
  slug: mediatailor-api-log-configuration-for-channel
- name: LogConfiguration
  property_count: 1
  slug: mediatailor-api-log-configuration
- name: LogType
  property_count: 0
  slug: mediatailor-api-log-type
- name: LogTypes
  property_count: 0
  slug: mediatailor-api-log-types
- name: Long
  property_count: 0
  slug: mediatailor-api-long
- name: ManifestProcessingRules
  property_count: 1
  slug: mediatailor-api-manifest-processing-rules
- name: MaxResults
  property_count: 0
  slug: mediatailor-api-max-results
- name: MessageType
  property_count: 0
  slug: mediatailor-api-message-type
- name: Mode
  property_count: 0
  slug: mediatailor-api-mode
- name: Operator
  property_count: 0
  slug: mediatailor-api-operator
- name: OriginManifestType
  property_count: 0
  slug: mediatailor-api-origin-manifest-type
- name: PlaybackConfiguration
  property_count: 19
  slug: mediatailor-api-playback-configuration
- name: PlaybackMode
  property_count: 0
  slug: mediatailor-api-playback-mode
- name: PrefetchConsumption
  property_count: 3
  slug: mediatailor-api-prefetch-consumption
- name: PrefetchRetrieval
  property_count: 3
  slug: mediatailor-api-prefetch-retrieval
- name: PrefetchSchedule
  property_count: 6
  slug: mediatailor-api-prefetch-schedule
- name: PutChannelPolicyRequest
  property_count: 1
  slug: mediatailor-api-put-channel-policy-request
- name: PutChannelPolicyResponse
  property_count: 0
  slug: mediatailor-api-put-channel-policy-response
- name: PutPlaybackConfigurationRequest
  property_count: 14
  slug: mediatailor-api-put-playback-configuration-request
- name: PutPlaybackConfigurationResponse
  property_count: 19
  slug: mediatailor-api-put-playback-configuration-response
- name: RelativePosition
  property_count: 0
  slug: mediatailor-api-relative-position
- name: RequestOutputItem
  property_count: 4
  slug: mediatailor-api-request-output-item
- name: RequestOutputs
  property_count: 0
  slug: mediatailor-api-request-outputs
- name: ResponseOutputItem
  property_count: 5
  slug: mediatailor-api-response-output-item
- name: ResponseOutputs
  property_count: 0
  slug: mediatailor-api-response-outputs
- name: ScheduleAdBreak
  property_count: 4
  slug: mediatailor-api-schedule-ad-break
- name: ScheduleConfiguration
  property_count: 2
  slug: mediatailor-api-schedule-configuration
- name: ScheduleEntry
  property_count: 10
  slug: mediatailor-api-schedule-entry
- name: ScheduleEntryType
  property_count: 0
  slug: mediatailor-api-schedule-entry-type
- name: SecretsManagerAccessTokenConfiguration
  property_count: 3
  slug: mediatailor-api-secrets-manager-access-token-configuration
- name: SegmentDeliveryConfiguration
  property_count: 2
  slug: mediatailor-api-segment-delivery-configuration
- name: SegmentationDescriptorList
  property_count: 0
  slug: mediatailor-api-segmentation-descriptor-list
- name: SegmentationDescriptor
  property_count: 8
  slug: mediatailor-api-segmentation-descriptor
- name: SlateSource
  property_count: 2
  slug: mediatailor-api-slate-source
- name: SourceLocation
  property_count: 9
  slug: mediatailor-api-source-location
- name: SpliceInsertMessage
  property_count: 4
  slug: mediatailor-api-splice-insert-message
- name: StartChannelRequest
  property_count: 0
  slug: mediatailor-api-start-channel-request
- name: StartChannelResponse
  property_count: 0
  slug: mediatailor-api-start-channel-response
- name: StopChannelRequest
  property_count: 0
  slug: mediatailor-api-stop-channel-request
- name: StopChannelResponse
  property_count: 0
  slug: mediatailor-api-stop-channel-response
- name: String
  property_count: 0
  slug: mediatailor-api-string
- name: TagResourceRequest
  property_count: 1
  slug: mediatailor-api-tag-resource-request
- name: Tier
  property_count: 0
  slug: mediatailor-api-tier
- name: TimeSignalMessage
  property_count: 1
  slug: mediatailor-api-time-signal-message
- name: Transition
  property_count: 5
  slug: mediatailor-api-transition
- name: Type
  property_count: 0
  slug: mediatailor-api-type
- name: UntagResourceRequest
  property_count: 0
  slug: mediatailor-api-untag-resource-request
- name: UpdateChannelRequest
  property_count: 2
  slug: mediatailor-api-update-channel-request
- name: UpdateChannelResponse
  property_count: 10
  slug: mediatailor-api-update-channel-response
- name: UpdateLiveSourceRequest
  property_count: 1
  slug: mediatailor-api-update-live-source-request
- name: UpdateLiveSourceResponse
  property_count: 7
  slug: mediatailor-api-update-live-source-response
- name: UpdateProgramRequest
  property_count: 2
  slug: mediatailor-api-update-program-request
- name: UpdateProgramResponse
  property_count: 11
  slug: mediatailor-api-update-program-response
- name: UpdateProgramScheduleConfiguration
  property_count: 2
  slug: mediatailor-api-update-program-schedule-configuration
- name: UpdateProgramTransition
  property_count: 2
  slug: mediatailor-api-update-program-transition
- name: UpdateSourceLocationRequest
  property_count: 4
  slug: mediatailor-api-update-source-location-request
- name: UpdateSourceLocationResponse
  property_count: 9
  slug: mediatailor-api-update-source-location-response
- name: UpdateVodSourceRequest
  property_count: 1
  slug: mediatailor-api-update-vod-source-request
- name: UpdateVodSourceResponse
  property_count: 7
  slug: mediatailor-api-update-vod-source-response
- name: VodSource
  property_count: 7
  slug: mediatailor-api-vod-source
json_structures:
- name: Mediatailor Api Access Configuration Structure
  property_count: 2
  slug: mediatailor-api-access-configuration-structure
- name: Mediatailor Api Access Type Structure
  property_count: 0
  slug: mediatailor-api-access-type-structure
- name: Mediatailor Api Ad Break Structure
  property_count: 5
  slug: mediatailor-api-ad-break-structure
- name: Mediatailor Api Ad Marker Passthrough Structure
  property_count: 1
  slug: mediatailor-api-ad-marker-passthrough-structure
- name: Mediatailor Api Alert Structure
  property_count: 5
  slug: mediatailor-api-alert-structure
- name: Mediatailor Api Avail Matching Criteria Structure
  property_count: 2
  slug: mediatailor-api-avail-matching-criteria-structure
- name: Mediatailor Api Avail Suppression Structure
  property_count: 2
  slug: mediatailor-api-avail-suppression-structure
- name: Mediatailor Api Bumper Structure
  property_count: 2
  slug: mediatailor-api-bumper-structure
- name: Mediatailor Api Cdn Configuration Structure
  property_count: 2
  slug: mediatailor-api-cdn-configuration-structure
- name: Mediatailor Api Channel State Structure
  property_count: 0
  slug: mediatailor-api-channel-state-structure
- name: Mediatailor Api Channel Structure
  property_count: 11
  slug: mediatailor-api-channel-structure
- name: Mediatailor Api Clip Range Structure
  property_count: 1
  slug: mediatailor-api-clip-range-structure
- name: Mediatailor Api Configuration Aliases Request Structure
  property_count: 0
  slug: mediatailor-api-configuration-aliases-request-structure
- name: Mediatailor Api Configuration Aliases Response Structure
  property_count: 0
  slug: mediatailor-api-configuration-aliases-response-structure
- name: Mediatailor Api Configure Logs For Channel Request Structure
  property_count: 2
  slug: mediatailor-api-configure-logs-for-channel-request-structure
- name: Mediatailor Api Configure Logs For Channel Response Structure
  property_count: 2
  slug: mediatailor-api-configure-logs-for-channel-response-structure
- name: Mediatailor Api Configure Logs For Playback Configuration Request Structure
  property_count: 2
  slug: mediatailor-api-configure-logs-for-playback-configuration-request-structure
- name: Mediatailor Api Configure Logs For Playback Configuration Response Structure
  property_count: 2
  slug: mediatailor-api-configure-logs-for-playback-configuration-response-structure
- name: Mediatailor Api Create Channel Request Structure
  property_count: 5
  slug: mediatailor-api-create-channel-request-structure
- name: Mediatailor Api Create Channel Response Structure
  property_count: 10
  slug: mediatailor-api-create-channel-response-structure
- name: Mediatailor Api Create Live Source Request Structure
  property_count: 2
  slug: mediatailor-api-create-live-source-request-structure
- name: Mediatailor Api Create Live Source Response Structure
  property_count: 7
  slug: mediatailor-api-create-live-source-response-structure
- name: Mediatailor Api Create Prefetch Schedule Request Structure
  property_count: 3
  slug: mediatailor-api-create-prefetch-schedule-request-structure
- name: Mediatailor Api Create Prefetch Schedule Response Structure
  property_count: 6
  slug: mediatailor-api-create-prefetch-schedule-response-structure
- name: Mediatailor Api Create Program Request Structure
  property_count: 5
  slug: mediatailor-api-create-program-request-structure
- name: Mediatailor Api Create Program Response Structure
  property_count: 11
  slug: mediatailor-api-create-program-response-structure
- name: Mediatailor Api Create Source Location Request Structure
  property_count: 5
  slug: mediatailor-api-create-source-location-request-structure
- name: Mediatailor Api Create Source Location Response Structure
  property_count: 9
  slug: mediatailor-api-create-source-location-response-structure
- name: Mediatailor Api Create Vod Source Request Structure
  property_count: 2
  slug: mediatailor-api-create-vod-source-request-structure
- name: Mediatailor Api Create Vod Source Response Structure
  property_count: 7
  slug: mediatailor-api-create-vod-source-response-structure
- name: Mediatailor Api Dash Configuration For Put Structure
  property_count: 2
  slug: mediatailor-api-dash-configuration-for-put-structure
- name: Mediatailor Api Dash Configuration Structure
  property_count: 3
  slug: mediatailor-api-dash-configuration-structure
- name: Mediatailor Api Dash Playlist Settings Structure
  property_count: 4
  slug: mediatailor-api-dash-playlist-settings-structure
- name: Mediatailor Api Default Segment Delivery Configuration Structure
  property_count: 1
  slug: mediatailor-api-default-segment-delivery-configuration-structure
- name: Mediatailor Api Delete Channel Policy Request Structure
  property_count: 0
  slug: mediatailor-api-delete-channel-policy-request-structure
- name: Mediatailor Api Delete Channel Policy Response Structure
  property_count: 0
  slug: mediatailor-api-delete-channel-policy-response-structure
- name: Mediatailor Api Delete Channel Request Structure
  property_count: 0
  slug: mediatailor-api-delete-channel-request-structure
- name: Mediatailor Api Delete Channel Response Structure
  property_count: 0
  slug: mediatailor-api-delete-channel-response-structure
- name: Mediatailor Api Delete Live Source Request Structure
  property_count: 0
  slug: mediatailor-api-delete-live-source-request-structure
- name: Mediatailor Api Delete Live Source Response Structure
  property_count: 0
  slug: mediatailor-api-delete-live-source-response-structure
- name: Mediatailor Api Delete Playback Configuration Request Structure
  property_count: 0
  slug: mediatailor-api-delete-playback-configuration-request-structure
- name: Mediatailor Api Delete Playback Configuration Response Structure
  property_count: 0
  slug: mediatailor-api-delete-playback-configuration-response-structure
- name: Mediatailor Api Delete Prefetch Schedule Request Structure
  property_count: 0
  slug: mediatailor-api-delete-prefetch-schedule-request-structure
- name: Mediatailor Api Delete Prefetch Schedule Response Structure
  property_count: 0
  slug: mediatailor-api-delete-prefetch-schedule-response-structure
- name: Mediatailor Api Delete Program Request Structure
  property_count: 0
  slug: mediatailor-api-delete-program-request-structure
- name: Mediatailor Api Delete Program Response Structure
  property_count: 0
  slug: mediatailor-api-delete-program-response-structure
- name: Mediatailor Api Delete Source Location Request Structure
  property_count: 0
  slug: mediatailor-api-delete-source-location-request-structure
- name: Mediatailor Api Delete Source Location Response Structure
  property_count: 0
  slug: mediatailor-api-delete-source-location-response-structure
- name: Mediatailor Api Delete Vod Source Request Structure
  property_count: 0
  slug: mediatailor-api-delete-vod-source-request-structure
- name: Mediatailor Api Delete Vod Source Response Structure
  property_count: 0
  slug: mediatailor-api-delete-vod-source-response-structure
- name: Mediatailor Api Describe Channel Request Structure
  property_count: 0
  slug: mediatailor-api-describe-channel-request-structure
- name: Mediatailor Api Describe Channel Response Structure
  property_count: 11
  slug: mediatailor-api-describe-channel-response-structure
- name: Mediatailor Api Describe Live Source Request Structure
  property_count: 0
  slug: mediatailor-api-describe-live-source-request-structure
- name: Mediatailor Api Describe Live Source Response Structure
  property_count: 7
  slug: mediatailor-api-describe-live-source-response-structure
- name: Mediatailor Api Describe Program Request Structure
  property_count: 0
  slug: mediatailor-api-describe-program-request-structure
- name: Mediatailor Api Describe Program Response Structure
  property_count: 11
  slug: mediatailor-api-describe-program-response-structure
- name: Mediatailor Api Describe Source Location Request Structure
  property_count: 0
  slug: mediatailor-api-describe-source-location-request-structure
- name: Mediatailor Api Describe Source Location Response Structure
  property_count: 9
  slug: mediatailor-api-describe-source-location-response-structure
- name: Mediatailor Api Describe Vod Source Request Structure
  property_count: 0
  slug: mediatailor-api-describe-vod-source-request-structure
- name: Mediatailor Api Describe Vod Source Response Structure
  property_count: 7
  slug: mediatailor-api-describe-vod-source-response-structure
- name: Mediatailor Api Get Channel Policy Request Structure
  property_count: 0
  slug: mediatailor-api-get-channel-policy-request-structure
- name: Mediatailor Api Get Channel Policy Response Structure
  property_count: 1
  slug: mediatailor-api-get-channel-policy-response-structure
- name: Mediatailor Api Get Channel Schedule Request Structure
  property_count: 0
  slug: mediatailor-api-get-channel-schedule-request-structure
- name: Mediatailor Api Get Channel Schedule Response Structure
  property_count: 2
  slug: mediatailor-api-get-channel-schedule-response-structure
- name: Mediatailor Api Get Playback Configuration Request Structure
  property_count: 0
  slug: mediatailor-api-get-playback-configuration-request-structure
- name: Mediatailor Api Get Playback Configuration Response Structure
  property_count: 19
  slug: mediatailor-api-get-playback-configuration-response-structure
- name: Mediatailor Api Get Prefetch Schedule Request Structure
  property_count: 0
  slug: mediatailor-api-get-prefetch-schedule-request-structure
- name: Mediatailor Api Get Prefetch Schedule Response Structure
  property_count: 6
  slug: mediatailor-api-get-prefetch-schedule-response-structure
- name: Mediatailor Api Hls Configuration Structure
  property_count: 1
  slug: mediatailor-api-hls-configuration-structure
- name: Mediatailor Api Hls Playlist Settings Structure
  property_count: 1
  slug: mediatailor-api-hls-playlist-settings-structure
- name: Mediatailor Api Http Configuration Structure
  property_count: 1
  slug: mediatailor-api-http-configuration-structure
- name: Mediatailor Api Http Package Configuration Structure
  property_count: 3
  slug: mediatailor-api-http-package-configuration-structure
- name: Mediatailor Api Http Package Configurations Structure
  property_count: 0
  slug: mediatailor-api-http-package-configurations-structure
- name: Mediatailor Api Integer Structure
  property_count: 0
  slug: mediatailor-api-integer-structure
- name: Mediatailor Api List Alerts Request Structure
  property_count: 0
  slug: mediatailor-api-list-alerts-request-structure
- name: Mediatailor Api List Alerts Response Structure
  property_count: 2
  slug: mediatailor-api-list-alerts-response-structure
- name: Mediatailor Api List Channels Request Structure
  property_count: 0
  slug: mediatailor-api-list-channels-request-structure
- name: Mediatailor Api List Channels Response Structure
  property_count: 2
  slug: mediatailor-api-list-channels-response-structure
- name: Mediatailor Api List Live Sources Request Structure
  property_count: 0
  slug: mediatailor-api-list-live-sources-request-structure
- name: Mediatailor Api List Live Sources Response Structure
  property_count: 2
  slug: mediatailor-api-list-live-sources-response-structure
- name: Mediatailor Api List Playback Configurations Request Structure
  property_count: 0
  slug: mediatailor-api-list-playback-configurations-request-structure
- name: Mediatailor Api List Playback Configurations Response Structure
  property_count: 2
  slug: mediatailor-api-list-playback-configurations-response-structure
- name: Mediatailor Api List Prefetch Schedules Request Structure
  property_count: 3
  slug: mediatailor-api-list-prefetch-schedules-request-structure
- name: Mediatailor Api List Prefetch Schedules Response Structure
  property_count: 2
  slug: mediatailor-api-list-prefetch-schedules-response-structure
- name: Mediatailor Api List Source Locations Request Structure
  property_count: 0
  slug: mediatailor-api-list-source-locations-request-structure
- name: Mediatailor Api List Source Locations Response Structure
  property_count: 2
  slug: mediatailor-api-list-source-locations-response-structure
- name: Mediatailor Api List Tags For Resource Request Structure
  property_count: 0
  slug: mediatailor-api-list-tags-for-resource-request-structure
- name: Mediatailor Api List Tags For Resource Response Structure
  property_count: 1
  slug: mediatailor-api-list-tags-for-resource-response-structure
- name: Mediatailor Api List Vod Sources Request Structure
  property_count: 0
  slug: mediatailor-api-list-vod-sources-request-structure
- name: Mediatailor Api List Vod Sources Response Structure
  property_count: 2
  slug: mediatailor-api-list-vod-sources-response-structure
- name: Mediatailor Api Live Pre Roll Configuration Structure
  property_count: 2
  slug: mediatailor-api-live-pre-roll-configuration-structure
- name: Mediatailor Api Live Source Structure
  property_count: 7
  slug: mediatailor-api-live-source-structure
- name: Mediatailor Api Log Configuration For Channel Structure
  property_count: 1
  slug: mediatailor-api-log-configuration-for-channel-structure
- name: Mediatailor Api Log Configuration Structure
  property_count: 1
  slug: mediatailor-api-log-configuration-structure
- name: Mediatailor Api Log Type Structure
  property_count: 0
  slug: mediatailor-api-log-type-structure
- name: Mediatailor Api Log Types Structure
  property_count: 0
  slug: mediatailor-api-log-types-structure
- name: Mediatailor Api Long Structure
  property_count: 0
  slug: mediatailor-api-long-structure
- name: Mediatailor Api Manifest Processing Rules Structure
  property_count: 1
  slug: mediatailor-api-manifest-processing-rules-structure
- name: Mediatailor Api Max Results Structure
  property_count: 0
  slug: mediatailor-api-max-results-structure
- name: Mediatailor Api Message Type Structure
  property_count: 0
  slug: mediatailor-api-message-type-structure
- name: Mediatailor Api Mode Structure
  property_count: 0
  slug: mediatailor-api-mode-structure
- name: Mediatailor Api Operator Structure
  property_count: 0
  slug: mediatailor-api-operator-structure
- name: Mediatailor Api Origin Manifest Type Structure
  property_count: 0
  slug: mediatailor-api-origin-manifest-type-structure
- name: Mediatailor Api Playback Configuration Structure
  property_count: 19
  slug: mediatailor-api-playback-configuration-structure
- name: Mediatailor Api Playback Mode Structure
  property_count: 0
  slug: mediatailor-api-playback-mode-structure
- name: Mediatailor Api Prefetch Consumption Structure
  property_count: 3
  slug: mediatailor-api-prefetch-consumption-structure
- name: Mediatailor Api Prefetch Retrieval Structure
  property_count: 3
  slug: mediatailor-api-prefetch-retrieval-structure
- name: Mediatailor Api Prefetch Schedule Structure
  property_count: 6
  slug: mediatailor-api-prefetch-schedule-structure
- name: Mediatailor Api Put Channel Policy Request Structure
  property_count: 1
  slug: mediatailor-api-put-channel-policy-request-structure
- name: Mediatailor Api Put Channel Policy Response Structure
  property_count: 0
  slug: mediatailor-api-put-channel-policy-response-structure
- name: Mediatailor Api Put Playback Configuration Request Structure
  property_count: 14
  slug: mediatailor-api-put-playback-configuration-request-structure
- name: Mediatailor Api Put Playback Configuration Response Structure
  property_count: 19
  slug: mediatailor-api-put-playback-configuration-response-structure
- name: Mediatailor Api Relative Position Structure
  property_count: 0
  slug: mediatailor-api-relative-position-structure
- name: Mediatailor Api Request Output Item Structure
  property_count: 4
  slug: mediatailor-api-request-output-item-structure
- name: Mediatailor Api Request Outputs Structure
  property_count: 0
  slug: mediatailor-api-request-outputs-structure
- name: Mediatailor Api Response Output Item Structure
  property_count: 5
  slug: mediatailor-api-response-output-item-structure
- name: Mediatailor Api Response Outputs Structure
  property_count: 0
  slug: mediatailor-api-response-outputs-structure
- name: Mediatailor Api Schedule Ad Break Structure
  property_count: 4
  slug: mediatailor-api-schedule-ad-break-structure
- name: Mediatailor Api Schedule Configuration Structure
  property_count: 2
  slug: mediatailor-api-schedule-configuration-structure
- name: Mediatailor Api Schedule Entry Structure
  property_count: 10
  slug: mediatailor-api-schedule-entry-structure
- name: Mediatailor Api Schedule Entry Type Structure
  property_count: 0
  slug: mediatailor-api-schedule-entry-type-structure
- name: Mediatailor Api Secrets Manager Access Token Configuration Structure
  property_count: 3
  slug: mediatailor-api-secrets-manager-access-token-configuration-structure
- name: Mediatailor Api Segment Delivery Configuration Structure
  property_count: 2
  slug: mediatailor-api-segment-delivery-configuration-structure
- name: Mediatailor Api Segmentation Descriptor List Structure
  property_count: 0
  slug: mediatailor-api-segmentation-descriptor-list-structure
- name: Mediatailor Api Segmentation Descriptor Structure
  property_count: 8
  slug: mediatailor-api-segmentation-descriptor-structure
- name: Mediatailor Api Slate Source Structure
  property_count: 2
  slug: mediatailor-api-slate-source-structure
- name: Mediatailor Api Source Location Structure
  property_count: 9
  slug: mediatailor-api-source-location-structure
- name: Mediatailor Api Splice Insert Message Structure
  property_count: 4
  slug: mediatailor-api-splice-insert-message-structure
- name: Mediatailor Api Start Channel Request Structure
  property_count: 0
  slug: mediatailor-api-start-channel-request-structure
- name: Mediatailor Api Start Channel Response Structure
  property_count: 0
  slug: mediatailor-api-start-channel-response-structure
- name: Mediatailor Api Stop Channel Request Structure
  property_count: 0
  slug: mediatailor-api-stop-channel-request-structure
- name: Mediatailor Api Stop Channel Response Structure
  property_count: 0
  slug: mediatailor-api-stop-channel-response-structure
- name: Mediatailor Api String Structure
  property_count: 0
  slug: mediatailor-api-string-structure
- name: Mediatailor Api Tag Resource Request Structure
  property_count: 1
  slug: mediatailor-api-tag-resource-request-structure
- name: Mediatailor Api Tier Structure
  property_count: 0
  slug: mediatailor-api-tier-structure
- name: Mediatailor Api Time Signal Message Structure
  property_count: 1
  slug: mediatailor-api-time-signal-message-structure
- name: Mediatailor Api Transition Structure
  property_count: 5
  slug: mediatailor-api-transition-structure
- name: Mediatailor Api Type Structure
  property_count: 0
  slug: mediatailor-api-type-structure
- name: Mediatailor Api Untag Resource Request Structure
  property_count: 0
  slug: mediatailor-api-untag-resource-request-structure
- name: Mediatailor Api Update Channel Request Structure
  property_count: 2
  slug: mediatailor-api-update-channel-request-structure
- name: Mediatailor Api Update Channel Response Structure
  property_count: 10
  slug: mediatailor-api-update-channel-response-structure
- name: Mediatailor Api Update Live Source Request Structure
  property_count: 1
  slug: mediatailor-api-update-live-source-request-structure
- name: Mediatailor Api Update Live Source Response Structure
  property_count: 7
  slug: mediatailor-api-update-live-source-response-structure
- name: Mediatailor Api Update Program Request Structure
  property_count: 2
  slug: mediatailor-api-update-program-request-structure
- name: Mediatailor Api Update Program Response Structure
  property_count: 11
  slug: mediatailor-api-update-program-response-structure
- name: Mediatailor Api Update Program Schedule Configuration Structure
  property_count: 2
  slug: mediatailor-api-update-program-schedule-configuration-structure
- name: Mediatailor Api Update Program Transition Structure
  property_count: 2
  slug: mediatailor-api-update-program-transition-structure
- name: Mediatailor Api Update Source Location Request Structure
  property_count: 4
  slug: mediatailor-api-update-source-location-request-structure
- name: Mediatailor Api Update Source Location Response Structure
  property_count: 9
  slug: mediatailor-api-update-source-location-response-structure
- name: Mediatailor Api Update Vod Source Request Structure
  property_count: 1
  slug: mediatailor-api-update-vod-source-request-structure
- name: Mediatailor Api Update Vod Source Response Structure
  property_count: 7
  slug: mediatailor-api-update-vod-source-response-structure
- name: Mediatailor Api Vod Source Structure
  property_count: 7
  slug: mediatailor-api-vod-source-structure
jsonld:
- class_count: 154
  name: Amazon Mediatailor Mediatailor Api Context
  property_count: 116
  slug: amazon-mediatailor-mediatailor-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MediaTailor
nav: Providers
network: true
overview: 'Amazon MediaTailor publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts#resourceArn API, Channel API, Channels API, and 7 more. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MediaTailor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MediaTailor''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 11 more developer resources.'
plans:
- name: Amazon Mediatailor Plans Pricing
  plan_count: 3
  slug: amazon-mediatailor-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Amazon Mediatailor Rate Limits
  slug: amazon-mediatailor-rate-limits
rules:
- name: Amazon MediaTailor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-mediatailor-jsonschema-spectral-rules
- name: Amazon MediaTailor API Rules
  rule_count: 25
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 11
  slug: amazon-mediatailor-spectral-rules
score:
  band: strong
  composite: 64.8
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 67.4
    developer_ergonomics: 41.3
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 64.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-mediatailor/refs/heads/main/screenshots/amazon-mediatailor-2026-06-20T171741.png
security:
- kind: authentication
  name: Amazon Mediatailor Authentication
  slug: amazon-mediatailor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Mediatailor Domain Security
  slug: amazon-mediatailor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Mediatailor Vulnerability Disclosure
  slug: amazon-mediatailor-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Mediatailor Trust Center
  slug: amazon-mediatailor-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-mediatailor
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Insert targeted ads into video-on-demand content for revenue generation.
  name: VOD Monetization
- description: Replace live ad markers with personalized ads during live events.
  name: Live Stream Advertising
- description: Build free ad-supported streaming TV channels from VOD libraries.
  name: FAST Channel Creation
- description: Deliver personalized ad experiences to individual viewers at scale.
  name: Addressable Advertising
website: https://aws.amazon.com/mediatailor/
---
