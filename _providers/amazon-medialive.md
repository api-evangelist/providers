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
- acting_count: 39
  human_in_the_loop: 4
  name: Amazon Medialive Agentic Access
  operation_count: 59
  slug: amazon-medialive-agentic-access
  summary_line: 59 operations · 39 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: The Prod API from Amazon MediaLive — 38 operation(s) for prod.
  name: Amazon MediaLive Prod API
  slug: amazon-medialive-prod-api
artifact_total: 1883
collections:
- collection_type: postman
  name: AWS Elemental MediaLive Prod API
  slug: postman-amazon-medialive-prod-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-medialive/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-medialive-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-medialive-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-medialive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-medialive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-medialive-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/medialive/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/medialive/
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
  url: https://console.aws.amazon.com/medialive/
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
  url: rules/amazon-medialive-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-medialive-vocabulary.yaml
created: '2026-03-16'
description: AWS Elemental MediaLive is a broadcast-grade live video processing service that creates high-quality video streams for delivery to broadcast televisions and internet-connected multiscreen devices.
examples:
- key_count: 0
  name: Medialive Api Aac Coding Mode Example
  slug: medialive-api-aac-coding-mode-example
- key_count: 0
  name: Medialive Api Aac Input Type Example
  slug: medialive-api-aac-input-type-example
- key_count: 0
  name: Medialive Api Aac Profile Example
  slug: medialive-api-aac-profile-example
- key_count: 0
  name: Medialive Api Aac Rate Control Mode Example
  slug: medialive-api-aac-rate-control-mode-example
- key_count: 0
  name: Medialive Api Aac Raw Format Example
  slug: medialive-api-aac-raw-format-example
- key_count: 9
  name: Medialive Api Aac Settings Example
  slug: medialive-api-aac-settings-example
- key_count: 0
  name: Medialive Api Aac Spec Example
  slug: medialive-api-aac-spec-example
- key_count: 0
  name: Medialive Api Aac Vbr Quality Example
  slug: medialive-api-aac-vbr-quality-example
- key_count: 0
  name: Medialive Api Ac3 Bitstream Mode Example
  slug: medialive-api-ac3-bitstream-mode-example
- key_count: 0
  name: Medialive Api Ac3 Coding Mode Example
  slug: medialive-api-ac3-coding-mode-example
- key_count: 0
  name: Medialive Api Ac3 Drc Profile Example
  slug: medialive-api-ac3-drc-profile-example
- key_count: 0
  name: Medialive Api Ac3 Lfe Filter Example
  slug: medialive-api-ac3-lfe-filter-example
- key_count: 0
  name: Medialive Api Ac3 Metadata Control Example
  slug: medialive-api-ac3-metadata-control-example
- key_count: 7
  name: Medialive Api Ac3 Settings Example
  slug: medialive-api-ac3-settings-example
- key_count: 0
  name: Medialive Api Accept Header Example
  slug: medialive-api-accept-header-example
- key_count: 0
  name: Medialive Api Accept Input Device Transfer Request Example
  slug: medialive-api-accept-input-device-transfer-request-example
- key_count: 0
  name: Medialive Api Accept Input Device Transfer Response Example
  slug: medialive-api-accept-input-device-transfer-response-example
- key_count: 0
  name: Medialive Api Accessibility Type Example
  slug: medialive-api-accessibility-type-example
- key_count: 0
  name: Medialive Api Afd Signaling Example
  slug: medialive-api-afd-signaling-example
- key_count: 1
  name: Medialive Api Ancillary Source Settings Example
  slug: medialive-api-ancillary-source-settings-example
- key_count: 1
  name: Medialive Api Archive Cdn Settings Example
  slug: medialive-api-archive-cdn-settings-example
- key_count: 2
  name: Medialive Api Archive Container Settings Example
  slug: medialive-api-archive-container-settings-example
- key_count: 3
  name: Medialive Api Archive Group Settings Example
  slug: medialive-api-archive-group-settings-example
- key_count: 3
  name: Medialive Api Archive Output Settings Example
  slug: medialive-api-archive-output-settings-example
- key_count: 1
  name: Medialive Api Archive S3 Settings Example
  slug: medialive-api-archive-s3-settings-example
- key_count: 0
  name: Medialive Api Arib Destination Settings Example
  slug: medialive-api-arib-destination-settings-example
- key_count: 0
  name: Medialive Api Arib Source Settings Example
  slug: medialive-api-arib-source-settings-example
- key_count: 2
  name: Medialive Api Audio Channel Mapping Example
  slug: medialive-api-audio-channel-mapping-example
- key_count: 7
  name: Medialive Api Audio Codec Settings Example
  slug: medialive-api-audio-codec-settings-example
- key_count: 0
  name: Medialive Api Audio Description Audio Type Control Example
  slug: medialive-api-audio-description-audio-type-control-example
- key_count: 11
  name: Medialive Api Audio Description Example
  slug: medialive-api-audio-description-example
- key_count: 0
  name: Medialive Api Audio Description Language Code Control Example
  slug: medialive-api-audio-description-language-code-control-example
- key_count: 1
  name: Medialive Api Audio Dolby E Decode Example
  slug: medialive-api-audio-dolby-e-decode-example
- key_count: 2
  name: Medialive Api Audio Hls Rendition Selection Example
  slug: medialive-api-audio-hls-rendition-selection-example
- key_count: 2
  name: Medialive Api Audio Language Selection Example
  slug: medialive-api-audio-language-selection-example
- key_count: 0
  name: Medialive Api Audio Language Selection Policy Example
  slug: medialive-api-audio-language-selection-policy-example
- key_count: 0
  name: Medialive Api Audio Normalization Algorithm Control Example
  slug: medialive-api-audio-normalization-algorithm-control-example
- key_count: 0
  name: Medialive Api Audio Normalization Algorithm Example
  slug: medialive-api-audio-normalization-algorithm-example
- key_count: 3
  name: Medialive Api Audio Normalization Settings Example
  slug: medialive-api-audio-normalization-settings-example
- key_count: 0
  name: Medialive Api Audio Only Hls Segment Type Example
  slug: medialive-api-audio-only-hls-segment-type-example
- key_count: 4
  name: Medialive Api Audio Only Hls Settings Example
  slug: medialive-api-audio-only-hls-settings-example
- key_count: 0
  name: Medialive Api Audio Only Hls Track Type Example
  slug: medialive-api-audio-only-hls-track-type-example
- key_count: 1
  name: Medialive Api Audio Pid Selection Example
  slug: medialive-api-audio-pid-selection-example
- key_count: 2
  name: Medialive Api Audio Selector Example
  slug: medialive-api-audio-selector-example
- key_count: 4
  name: Medialive Api Audio Selector Settings Example
  slug: medialive-api-audio-selector-settings-example
- key_count: 2
  name: Medialive Api Audio Silence Failover Settings Example
  slug: medialive-api-audio-silence-failover-settings-example
- key_count: 1
  name: Medialive Api Audio Track Example
  slug: medialive-api-audio-track-example
- key_count: 2
  name: Medialive Api Audio Track Selection Example
  slug: medialive-api-audio-track-selection-example
- key_count: 0
  name: Medialive Api Audio Type Example
  slug: medialive-api-audio-type-example
- key_count: 1
  name: Medialive Api Audio Watermark Settings Example
  slug: medialive-api-audio-watermark-settings-example
- key_count: 0
  name: Medialive Api Authentication Scheme Example
  slug: medialive-api-authentication-scheme-example
- key_count: 4
  name: Medialive Api Automatic Input Failover Settings Example
  slug: medialive-api-automatic-input-failover-settings-example
- key_count: 2
  name: Medialive Api Avail Blanking Example
  slug: medialive-api-avail-blanking-example
- key_count: 0
  name: Medialive Api Avail Blanking State Example
  slug: medialive-api-avail-blanking-state-example
- key_count: 1
  name: Medialive Api Avail Configuration Example
  slug: medialive-api-avail-configuration-example
- key_count: 3
  name: Medialive Api Avail Settings Example
  slug: medialive-api-avail-settings-example
- key_count: 0
  name: Medialive Api Bad Gateway Exception Example
  slug: medialive-api-bad-gateway-exception-example
- key_count: 4
  name: Medialive Api Batch Delete Request Example
  slug: medialive-api-batch-delete-request-example
- key_count: 2
  name: Medialive Api Batch Delete Response Example
  slug: medialive-api-batch-delete-response-example
- key_count: 4
  name: Medialive Api Batch Failed Result Model Example
  slug: medialive-api-batch-failed-result-model-example
- key_count: 1
  name: Medialive Api Batch Schedule Action Create Request Example
  slug: medialive-api-batch-schedule-action-create-request-example
- key_count: 1
  name: Medialive Api Batch Schedule Action Create Result Example
  slug: medialive-api-batch-schedule-action-create-result-example
- key_count: 1
  name: Medialive Api Batch Schedule Action Delete Request Example
  slug: medialive-api-batch-schedule-action-delete-request-example
- key_count: 1
  name: Medialive Api Batch Schedule Action Delete Result Example
  slug: medialive-api-batch-schedule-action-delete-result-example
- key_count: 2
  name: Medialive Api Batch Start Request Example
  slug: medialive-api-batch-start-request-example
- key_count: 2
  name: Medialive Api Batch Start Response Example
  slug: medialive-api-batch-start-response-example
- key_count: 2
  name: Medialive Api Batch Stop Request Example
  slug: medialive-api-batch-stop-request-example
- key_count: 2
  name: Medialive Api Batch Stop Response Example
  slug: medialive-api-batch-stop-response-example
- key_count: 3
  name: Medialive Api Batch Successful Result Model Example
  slug: medialive-api-batch-successful-result-model-example
- key_count: 2
  name: Medialive Api Batch Update Schedule Request Example
  slug: medialive-api-batch-update-schedule-request-example
- key_count: 2
  name: Medialive Api Batch Update Schedule Response Example
  slug: medialive-api-batch-update-schedule-response-example
- key_count: 5
  name: Medialive Api Blackout Slate Example
  slug: medialive-api-blackout-slate-example
- key_count: 0
  name: Medialive Api Blackout Slate Network End Blackout Example
  slug: medialive-api-blackout-slate-network-end-blackout-example
- key_count: 0
  name: Medialive Api Blackout Slate State Example
  slug: medialive-api-blackout-slate-state-example
- key_count: 0
  name: Medialive Api Burn In Alignment Example
  slug: medialive-api-burn-in-alignment-example
- key_count: 0
  name: Medialive Api Burn In Background Color Example
  slug: medialive-api-burn-in-background-color-example
- key_count: 17
  name: Medialive Api Burn In Destination Settings Example
  slug: medialive-api-burn-in-destination-settings-example
- key_count: 0
  name: Medialive Api Burn In Font Color Example
  slug: medialive-api-burn-in-font-color-example
- key_count: 0
  name: Medialive Api Burn In Outline Color Example
  slug: medialive-api-burn-in-outline-color-example
- key_count: 0
  name: Medialive Api Burn In Shadow Color Example
  slug: medialive-api-burn-in-shadow-color-example
- key_count: 0
  name: Medialive Api Burn In Teletext Grid Control Example
  slug: medialive-api-burn-in-teletext-grid-control-example
- key_count: 0
  name: Medialive Api Cancel Input Device Transfer Request Example
  slug: medialive-api-cancel-input-device-transfer-request-example
- key_count: 0
  name: Medialive Api Cancel Input Device Transfer Response Example
  slug: medialive-api-cancel-input-device-transfer-response-example
- key_count: 6
  name: Medialive Api Caption Description Example
  slug: medialive-api-caption-description-example
- key_count: 13
  name: Medialive Api Caption Destination Settings Example
  slug: medialive-api-caption-destination-settings-example
- key_count: 3
  name: Medialive Api Caption Language Mapping Example
  slug: medialive-api-caption-language-mapping-example
- key_count: 4
  name: Medialive Api Caption Rectangle Example
  slug: medialive-api-caption-rectangle-example
- key_count: 3
  name: Medialive Api Caption Selector Example
  slug: medialive-api-caption-selector-example
- key_count: 7
  name: Medialive Api Caption Selector Settings Example
  slug: medialive-api-caption-selector-settings-example
- key_count: 0
  name: Medialive Api Cdi Input Resolution Example
  slug: medialive-api-cdi-input-resolution-example
- key_count: 1
  name: Medialive Api Cdi Input Specification Example
  slug: medialive-api-cdi-input-specification-example
- key_count: 0
  name: Medialive Api Channel Class Example
  slug: medialive-api-channel-class-example
- key_count: 1
  name: Medialive Api Channel Egress Endpoint Example
  slug: medialive-api-channel-egress-endpoint-example
- key_count: 18
  name: Medialive Api Channel Example
  slug: medialive-api-channel-example
- key_count: 0
  name: Medialive Api Channel State Example
  slug: medialive-api-channel-state-example
- key_count: 16
  name: Medialive Api Channel Summary Example
  slug: medialive-api-channel-summary-example
- key_count: 1
  name: Medialive Api Claim Device Request Example
  slug: medialive-api-claim-device-request-example
- key_count: 0
  name: Medialive Api Claim Device Response Example
  slug: medialive-api-claim-device-response-example
- key_count: 0
  name: Medialive Api Color Space Passthrough Settings Example
  slug: medialive-api-color-space-passthrough-settings-example
- key_count: 0
  name: Medialive Api Content Type Example
  slug: medialive-api-content-type-example
- key_count: 14
  name: Medialive Api Create Channel Request Example
  slug: medialive-api-create-channel-request-example
- key_count: 1
  name: Medialive Api Create Channel Response Example
  slug: medialive-api-create-channel-response-example
- key_count: 11
  name: Medialive Api Create Input Request Example
  slug: medialive-api-create-input-request-example
- key_count: 1
  name: Medialive Api Create Input Response Example
  slug: medialive-api-create-input-response-example
- key_count: 2
  name: Medialive Api Create Input Security Group Request Example
  slug: medialive-api-create-input-security-group-request-example
- key_count: 1
  name: Medialive Api Create Input Security Group Response Example
  slug: medialive-api-create-input-security-group-response-example
- key_count: 3
  name: Medialive Api Create Multiplex Program Request Example
  slug: medialive-api-create-multiplex-program-request-example
- key_count: 1
  name: Medialive Api Create Multiplex Program Response Example
  slug: medialive-api-create-multiplex-program-response-example
- key_count: 5
  name: Medialive Api Create Multiplex Request Example
  slug: medialive-api-create-multiplex-request-example
- key_count: 1
  name: Medialive Api Create Multiplex Response Example
  slug: medialive-api-create-multiplex-response-example
- key_count: 2
  name: Medialive Api Create Partner Input Request Example
  slug: medialive-api-create-partner-input-request-example
- key_count: 1
  name: Medialive Api Create Partner Input Response Example
  slug: medialive-api-create-partner-input-response-example
- key_count: 1
  name: Medialive Api Create Tags Request Example
  slug: medialive-api-create-tags-request-example
- key_count: 0
  name: Medialive Api Delete Channel Request Example
  slug: medialive-api-delete-channel-request-example
- key_count: 18
  name: Medialive Api Delete Channel Response Example
  slug: medialive-api-delete-channel-response-example
- key_count: 0
  name: Medialive Api Delete Input Request Example
  slug: medialive-api-delete-input-request-example
- key_count: 0
  name: Medialive Api Delete Input Response Example
  slug: medialive-api-delete-input-response-example
- key_count: 0
  name: Medialive Api Delete Input Security Group Request Example
  slug: medialive-api-delete-input-security-group-request-example
- key_count: 0
  name: Medialive Api Delete Input Security Group Response Example
  slug: medialive-api-delete-input-security-group-response-example
- key_count: 0
  name: Medialive Api Delete Multiplex Program Request Example
  slug: medialive-api-delete-multiplex-program-request-example
- key_count: 5
  name: Medialive Api Delete Multiplex Program Response Example
  slug: medialive-api-delete-multiplex-program-response-example
- key_count: 0
  name: Medialive Api Delete Multiplex Request Example
  slug: medialive-api-delete-multiplex-request-example
- key_count: 10
  name: Medialive Api Delete Multiplex Response Example
  slug: medialive-api-delete-multiplex-response-example
- key_count: 0
  name: Medialive Api Delete Reservation Request Example
  slug: medialive-api-delete-reservation-request-example
- key_count: 19
  name: Medialive Api Delete Reservation Response Example
  slug: medialive-api-delete-reservation-response-example
- key_count: 0
  name: Medialive Api Delete Schedule Request Example
  slug: medialive-api-delete-schedule-request-example
- key_count: 0
  name: Medialive Api Delete Schedule Response Example
  slug: medialive-api-delete-schedule-response-example
- key_count: 0
  name: Medialive Api Delete Tags Request Example
  slug: medialive-api-delete-tags-request-example
- key_count: 0
  name: Medialive Api Describe Channel Request Example
  slug: medialive-api-describe-channel-request-example
- key_count: 18
  name: Medialive Api Describe Channel Response Example
  slug: medialive-api-describe-channel-response-example
- key_count: 0
  name: Medialive Api Describe Input Device Request Example
  slug: medialive-api-describe-input-device-request-example
- key_count: 13
  name: Medialive Api Describe Input Device Response Example
  slug: medialive-api-describe-input-device-response-example
- key_count: 0
  name: Medialive Api Describe Input Device Thumbnail Request Example
  slug: medialive-api-describe-input-device-thumbnail-request-example
- key_count: 1
  name: Medialive Api Describe Input Device Thumbnail Response Example
  slug: medialive-api-describe-input-device-thumbnail-response-example
- key_count: 0
  name: Medialive Api Describe Input Request Example
  slug: medialive-api-describe-input-request-example
- key_count: 16
  name: Medialive Api Describe Input Response Example
  slug: medialive-api-describe-input-response-example
- key_count: 0
  name: Medialive Api Describe Input Security Group Request Example
  slug: medialive-api-describe-input-security-group-request-example
- key_count: 6
  name: Medialive Api Describe Input Security Group Response Example
  slug: medialive-api-describe-input-security-group-response-example
- key_count: 0
  name: Medialive Api Describe Multiplex Program Request Example
  slug: medialive-api-describe-multiplex-program-request-example
- key_count: 5
  name: Medialive Api Describe Multiplex Program Response Example
  slug: medialive-api-describe-multiplex-program-response-example
- key_count: 0
  name: Medialive Api Describe Multiplex Request Example
  slug: medialive-api-describe-multiplex-request-example
- key_count: 10
  name: Medialive Api Describe Multiplex Response Example
  slug: medialive-api-describe-multiplex-response-example
- key_count: 0
  name: Medialive Api Describe Offering Request Example
  slug: medialive-api-describe-offering-request-example
- key_count: 11
  name: Medialive Api Describe Offering Response Example
  slug: medialive-api-describe-offering-response-example
- key_count: 0
  name: Medialive Api Describe Reservation Request Example
  slug: medialive-api-describe-reservation-request-example
- key_count: 19
  name: Medialive Api Describe Reservation Response Example
  slug: medialive-api-describe-reservation-response-example
- key_count: 0
  name: Medialive Api Describe Schedule Request Example
  slug: medialive-api-describe-schedule-request-example
- key_count: 2
  name: Medialive Api Describe Schedule Response Example
  slug: medialive-api-describe-schedule-response-example
- key_count: 0
  name: Medialive Api Device Settings Sync State Example
  slug: medialive-api-device-settings-sync-state-example
- key_count: 0
  name: Medialive Api Device Update Status Example
  slug: medialive-api-device-update-status-example
- key_count: 0
  name: Medialive Api Dolby E Program Selection Example
  slug: medialive-api-dolby-e-program-selection-example
- key_count: 0
  name: Medialive Api Dolby Vision81 Settings Example
  slug: medialive-api-dolby-vision81-settings-example
- key_count: 3
  name: Medialive Api Dvb Nit Settings Example
  slug: medialive-api-dvb-nit-settings-example
- key_count: 0
  name: Medialive Api Dvb Sdt Output Sdt Example
  slug: medialive-api-dvb-sdt-output-sdt-example
- key_count: 4
  name: Medialive Api Dvb Sdt Settings Example
  slug: medialive-api-dvb-sdt-settings-example
- key_count: 0
  name: Medialive Api Dvb Sub Destination Alignment Example
  slug: medialive-api-dvb-sub-destination-alignment-example
- key_count: 0
  name: Medialive Api Dvb Sub Destination Background Color Example
  slug: medialive-api-dvb-sub-destination-background-color-example
- key_count: 0
  name: Medialive Api Dvb Sub Destination Font Color Example
  slug: medialive-api-dvb-sub-destination-font-color-example
- key_count: 0
  name: Medialive Api Dvb Sub Destination Outline Color Example
  slug: medialive-api-dvb-sub-destination-outline-color-example
- key_count: 17
  name: Medialive Api Dvb Sub Destination Settings Example
  slug: medialive-api-dvb-sub-destination-settings-example
- key_count: 0
  name: Medialive Api Dvb Sub Destination Shadow Color Example
  slug: medialive-api-dvb-sub-destination-shadow-color-example
- key_count: 0
  name: Medialive Api Dvb Sub Destination Teletext Grid Control Example
  slug: medialive-api-dvb-sub-destination-teletext-grid-control-example
- key_count: 0
  name: Medialive Api Dvb Sub Ocr Language Example
  slug: medialive-api-dvb-sub-ocr-language-example
- key_count: 2
  name: Medialive Api Dvb Sub Source Settings Example
  slug: medialive-api-dvb-sub-source-settings-example
- key_count: 1
  name: Medialive Api Dvb Tdt Settings Example
  slug: medialive-api-dvb-tdt-settings-example
- key_count: 0
  name: Medialive Api Eac3 Atmos Coding Mode Example
  slug: medialive-api-eac3-atmos-coding-mode-example
- key_count: 0
  name: Medialive Api Eac3 Atmos Drc Line Example
  slug: medialive-api-eac3-atmos-drc-line-example
- key_count: 0
  name: Medialive Api Eac3 Atmos Drc Rf Example
  slug: medialive-api-eac3-atmos-drc-rf-example
- key_count: 7
  name: Medialive Api Eac3 Atmos Settings Example
  slug: medialive-api-eac3-atmos-settings-example
- key_count: 0
  name: Medialive Api Eac3 Attenuation Control Example
  slug: medialive-api-eac3-attenuation-control-example
- key_count: 0
  name: Medialive Api Eac3 Bitstream Mode Example
  slug: medialive-api-eac3-bitstream-mode-example
- key_count: 0
  name: Medialive Api Eac3 Coding Mode Example
  slug: medialive-api-eac3-coding-mode-example
- key_count: 0
  name: Medialive Api Eac3 Dc Filter Example
  slug: medialive-api-eac3-dc-filter-example
- key_count: 0
  name: Medialive Api Eac3 Drc Line Example
  slug: medialive-api-eac3-drc-line-example
- key_count: 0
  name: Medialive Api Eac3 Drc Rf Example
  slug: medialive-api-eac3-drc-rf-example
- key_count: 0
  name: Medialive Api Eac3 Lfe Control Example
  slug: medialive-api-eac3-lfe-control-example
- key_count: 0
  name: Medialive Api Eac3 Lfe Filter Example
  slug: medialive-api-eac3-lfe-filter-example
- key_count: 0
  name: Medialive Api Eac3 Metadata Control Example
  slug: medialive-api-eac3-metadata-control-example
- key_count: 0
  name: Medialive Api Eac3 Passthrough Control Example
  slug: medialive-api-eac3-passthrough-control-example
- key_count: 0
  name: Medialive Api Eac3 Phase Control Example
  slug: medialive-api-eac3-phase-control-example
- key_count: 20
  name: Medialive Api Eac3 Settings Example
  slug: medialive-api-eac3-settings-example
- key_count: 0
  name: Medialive Api Eac3 Stereo Downmix Example
  slug: medialive-api-eac3-stereo-downmix-example
- key_count: 0
  name: Medialive Api Eac3 Surround Ex Mode Example
  slug: medialive-api-eac3-surround-ex-mode-example
- key_count: 0
  name: Medialive Api Eac3 Surround Mode Example
  slug: medialive-api-eac3-surround-mode-example
- key_count: 4
  name: Medialive Api Ebu Tt D Destination Settings Example
  slug: medialive-api-ebu-tt-d-destination-settings-example
- key_count: 0
  name: Medialive Api Ebu Tt D Destination Style Control Example
  slug: medialive-api-ebu-tt-d-destination-style-control-example
- key_count: 0
  name: Medialive Api Ebu Tt D Fill Line Gap Control Example
  slug: medialive-api-ebu-tt-d-fill-line-gap-control-example
- key_count: 0
  name: Medialive Api Embedded Convert608 To708 Example
  slug: medialive-api-embedded-convert608-to708-example
- key_count: 0
  name: Medialive Api Embedded Destination Settings Example
  slug: medialive-api-embedded-destination-settings-example
- key_count: 0
  name: Medialive Api Embedded Plus Scte20 Destination Settings Example
  slug: medialive-api-embedded-plus-scte20-destination-settings-example
- key_count: 0
  name: Medialive Api Embedded Scte20 Detection Example
  slug: medialive-api-embedded-scte20-detection-example
- key_count: 4
  name: Medialive Api Embedded Source Settings Example
  slug: medialive-api-embedded-source-settings-example
- key_count: 12
  name: Medialive Api Encoder Settings Example
  slug: medialive-api-encoder-settings-example
- key_count: 6
  name: Medialive Api Esam Example
  slug: medialive-api-esam-example
- key_count: 1
  name: Medialive Api Failover Condition Example
  slug: medialive-api-failover-condition-example
- key_count: 3
  name: Medialive Api Failover Condition Settings Example
  slug: medialive-api-failover-condition-settings-example
- key_count: 1
  name: Medialive Api Feature Activations Example
  slug: medialive-api-feature-activations-example
- key_count: 0
  name: Medialive Api Feature Activations Input Prepare Schedule Actions Example
  slug: medialive-api-feature-activations-input-prepare-schedule-actions-example
- key_count: 0
  name: Medialive Api Fec Output Include Fec Example
  slug: medialive-api-fec-output-include-fec-example
- key_count: 3
  name: Medialive Api Fec Output Settings Example
  slug: medialive-api-fec-output-settings-example
- key_count: 0
  name: Medialive Api Fixed Afd Example
  slug: medialive-api-fixed-afd-example
- key_count: 1
  name: Medialive Api Fixed Mode Schedule Action Start Settings Example
  slug: medialive-api-fixed-mode-schedule-action-start-settings-example
- key_count: 3
  name: Medialive Api Fmp4 Hls Settings Example
  slug: medialive-api-fmp4-hls-settings-example
- key_count: 0
  name: Medialive Api Fmp4 Nielsen Id3 Behavior Example
  slug: medialive-api-fmp4-nielsen-id3-behavior-example
- key_count: 0
  name: Medialive Api Fmp4 Timed Metadata Behavior Example
  slug: medialive-api-fmp4-timed-metadata-behavior-example
- key_count: 2
  name: Medialive Api Follow Mode Schedule Action Start Settings Example
  slug: medialive-api-follow-mode-schedule-action-start-settings-example
- key_count: 0
  name: Medialive Api Follow Point Example
  slug: medialive-api-follow-point-example
- key_count: 1
  name: Medialive Api Frame Capture Cdn Settings Example
  slug: medialive-api-frame-capture-cdn-settings-example
- key_count: 2
  name: Medialive Api Frame Capture Group Settings Example
  slug: medialive-api-frame-capture-group-settings-example
- key_count: 0
  name: Medialive Api Frame Capture Hls Settings Example
  slug: medialive-api-frame-capture-hls-settings-example
- key_count: 0
  name: Medialive Api Frame Capture Interval Unit Example
  slug: medialive-api-frame-capture-interval-unit-example
- key_count: 1
  name: Medialive Api Frame Capture Output Settings Example
  slug: medialive-api-frame-capture-output-settings-example
- key_count: 1
  name: Medialive Api Frame Capture S3 Settings Example
  slug: medialive-api-frame-capture-s3-settings-example
- key_count: 3
  name: Medialive Api Frame Capture Settings Example
  slug: medialive-api-frame-capture-settings-example
- key_count: 0
  name: Medialive Api Gateway Timeout Exception Example
  slug: medialive-api-gateway-timeout-exception-example
- key_count: 6
  name: Medialive Api Global Configuration Example
  slug: medialive-api-global-configuration-example
- key_count: 0
  name: Medialive Api Global Configuration Input End Action Example
  slug: medialive-api-global-configuration-input-end-action-example
- key_count: 0
  name: Medialive Api Global Configuration Low Framerate Inputs Example
  slug: medialive-api-global-configuration-low-framerate-inputs-example
- key_count: 0
  name: Medialive Api Global Configuration Output Locking Mode Example
  slug: medialive-api-global-configuration-output-locking-mode-example
- key_count: 0
  name: Medialive Api Global Configuration Output Timing Source Example
  slug: medialive-api-global-configuration-output-timing-source-example
- key_count: 0
  name: Medialive Api H264 Adaptive Quantization Example
  slug: medialive-api-h264-adaptive-quantization-example
- key_count: 0
  name: Medialive Api H264 Color Metadata Example
  slug: medialive-api-h264-color-metadata-example
- key_count: 3
  name: Medialive Api H264 Color Space Settings Example
  slug: medialive-api-h264-color-space-settings-example
- key_count: 0
  name: Medialive Api H264 Entropy Encoding Example
  slug: medialive-api-h264-entropy-encoding-example
- key_count: 1
  name: Medialive Api H264 Filter Settings Example
  slug: medialive-api-h264-filter-settings-example
- key_count: 0
  name: Medialive Api H264 Flicker Aq Example
  slug: medialive-api-h264-flicker-aq-example
- key_count: 0
  name: Medialive Api H264 Force Field Pictures Example
  slug: medialive-api-h264-force-field-pictures-example
- key_count: 0
  name: Medialive Api H264 Framerate Control Example
  slug: medialive-api-h264-framerate-control-example
- key_count: 0
  name: Medialive Api H264 Gop B Reference Example
  slug: medialive-api-h264-gop-b-reference-example
- key_count: 0
  name: Medialive Api H264 Gop Size Units Example
  slug: medialive-api-h264-gop-size-units-example
- key_count: 0
  name: Medialive Api H264 Level Example
  slug: medialive-api-h264-level-example
- key_count: 0
  name: Medialive Api H264 Look Ahead Rate Control Example
  slug: medialive-api-h264-look-ahead-rate-control-example
- key_count: 0
  name: Medialive Api H264 Par Control Example
  slug: medialive-api-h264-par-control-example
- key_count: 0
  name: Medialive Api H264 Profile Example
  slug: medialive-api-h264-profile-example
- key_count: 0
  name: Medialive Api H264 Quality Level Example
  slug: medialive-api-h264-quality-level-example
- key_count: 0
  name: Medialive Api H264 Rate Control Mode Example
  slug: medialive-api-h264-rate-control-mode-example
- key_count: 0
  name: Medialive Api H264 Scan Type Example
  slug: medialive-api-h264-scan-type-example
- key_count: 0
  name: Medialive Api H264 Scene Change Detect Example
  slug: medialive-api-h264-scene-change-detect-example
- key_count: 42
  name: Medialive Api H264 Settings Example
  slug: medialive-api-h264-settings-example
- key_count: 0
  name: Medialive Api H264 Spatial Aq Example
  slug: medialive-api-h264-spatial-aq-example
- key_count: 0
  name: Medialive Api H264 Sub Gop Length Example
  slug: medialive-api-h264-sub-gop-length-example
- key_count: 0
  name: Medialive Api H264 Syntax Example
  slug: medialive-api-h264-syntax-example
- key_count: 0
  name: Medialive Api H264 Temporal Aq Example
  slug: medialive-api-h264-temporal-aq-example
- key_count: 0
  name: Medialive Api H264 Timecode Insertion Behavior Example
  slug: medialive-api-h264-timecode-insertion-behavior-example
- key_count: 0
  name: Medialive Api H265 Adaptive Quantization Example
  slug: medialive-api-h265-adaptive-quantization-example
- key_count: 0
  name: Medialive Api H265 Alternative Transfer Function Example
  slug: medialive-api-h265-alternative-transfer-function-example
- key_count: 0
  name: Medialive Api H265 Color Metadata Example
  slug: medialive-api-h265-color-metadata-example
- key_count: 5
  name: Medialive Api H265 Color Space Settings Example
  slug: medialive-api-h265-color-space-settings-example
- key_count: 1
  name: Medialive Api H265 Filter Settings Example
  slug: medialive-api-h265-filter-settings-example
- key_count: 0
  name: Medialive Api H265 Flicker Aq Example
  slug: medialive-api-h265-flicker-aq-example
- key_count: 0
  name: Medialive Api H265 Gop Size Units Example
  slug: medialive-api-h265-gop-size-units-example
- key_count: 0
  name: Medialive Api H265 Level Example
  slug: medialive-api-h265-level-example
- key_count: 0
  name: Medialive Api H265 Look Ahead Rate Control Example
  slug: medialive-api-h265-look-ahead-rate-control-example
- key_count: 0
  name: Medialive Api H265 Profile Example
  slug: medialive-api-h265-profile-example
- key_count: 0
  name: Medialive Api H265 Rate Control Mode Example
  slug: medialive-api-h265-rate-control-mode-example
- key_count: 0
  name: Medialive Api H265 Scan Type Example
  slug: medialive-api-h265-scan-type-example
- key_count: 0
  name: Medialive Api H265 Scene Change Detect Example
  slug: medialive-api-h265-scene-change-detect-example
- key_count: 30
  name: Medialive Api H265 Settings Example
  slug: medialive-api-h265-settings-example
- key_count: 0
  name: Medialive Api H265 Tier Example
  slug: medialive-api-h265-tier-example
- key_count: 0
  name: Medialive Api H265 Timecode Insertion Behavior Example
  slug: medialive-api-h265-timecode-insertion-behavior-example
- key_count: 2
  name: Medialive Api Hdr10 Settings Example
  slug: medialive-api-hdr10-settings-example
- key_count: 0
  name: Medialive Api Hls Ad Markers Example
  slug: medialive-api-hls-ad-markers-example
- key_count: 0
  name: Medialive Api Hls Akamai Http Transfer Mode Example
  slug: medialive-api-hls-akamai-http-transfer-mode-example
- key_count: 7
  name: Medialive Api Hls Akamai Settings Example
  slug: medialive-api-hls-akamai-settings-example
- key_count: 4
  name: Medialive Api Hls Basic Put Settings Example
  slug: medialive-api-hls-basic-put-settings-example
- key_count: 0
  name: Medialive Api Hls Caption Language Setting Example
  slug: medialive-api-hls-caption-language-setting-example
- key_count: 5
  name: Medialive Api Hls Cdn Settings Example
  slug: medialive-api-hls-cdn-settings-example
- key_count: 0
  name: Medialive Api Hls Client Cache Example
  slug: medialive-api-hls-client-cache-example
- key_count: 0
  name: Medialive Api Hls Codec Specification Example
  slug: medialive-api-hls-codec-specification-example
- key_count: 0
  name: Medialive Api Hls Directory Structure Example
  slug: medialive-api-hls-directory-structure-example
- key_count: 0
  name: Medialive Api Hls Discontinuity Tags Example
  slug: medialive-api-hls-discontinuity-tags-example
- key_count: 0
  name: Medialive Api Hls Encryption Type Example
  slug: medialive-api-hls-encryption-type-example
- key_count: 43
  name: Medialive Api Hls Group Settings Example
  slug: medialive-api-hls-group-settings-example
- key_count: 0
  name: Medialive Api Hls H265 Packaging Type Example
  slug: medialive-api-hls-h265-packaging-type-example
- key_count: 2
  name: Medialive Api Hls Id3 Segment Tagging Schedule Action Settings Example
  slug: medialive-api-hls-id3-segment-tagging-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Hls Id3 Segment Tagging State Example
  slug: medialive-api-hls-id3-segment-tagging-state-example
- key_count: 0
  name: Medialive Api Hls Incomplete Segment Behavior Example
  slug: medialive-api-hls-incomplete-segment-behavior-example
- key_count: 5
  name: Medialive Api Hls Input Settings Example
  slug: medialive-api-hls-input-settings-example
- key_count: 0
  name: Medialive Api Hls Iv In Manifest Example
  slug: medialive-api-hls-iv-in-manifest-example
- key_count: 0
  name: Medialive Api Hls Iv Source Example
  slug: medialive-api-hls-iv-source-example
- key_count: 0
  name: Medialive Api Hls Manifest Compression Example
  slug: medialive-api-hls-manifest-compression-example
- key_count: 0
  name: Medialive Api Hls Manifest Duration Format Example
  slug: medialive-api-hls-manifest-duration-format-example
- key_count: 5
  name: Medialive Api Hls Media Store Settings Example
  slug: medialive-api-hls-media-store-settings-example
- key_count: 0
  name: Medialive Api Hls Media Store Storage Class Example
  slug: medialive-api-hls-media-store-storage-class-example
- key_count: 0
  name: Medialive Api Hls Mode Example
  slug: medialive-api-hls-mode-example
- key_count: 0
  name: Medialive Api Hls Output Selection Example
  slug: medialive-api-hls-output-selection-example
- key_count: 4
  name: Medialive Api Hls Output Settings Example
  slug: medialive-api-hls-output-settings-example
- key_count: 0
  name: Medialive Api Hls Program Date Time Clock Example
  slug: medialive-api-hls-program-date-time-clock-example
- key_count: 0
  name: Medialive Api Hls Program Date Time Example
  slug: medialive-api-hls-program-date-time-example
- key_count: 0
  name: Medialive Api Hls Redundant Manifest Example
  slug: medialive-api-hls-redundant-manifest-example
- key_count: 1
  name: Medialive Api Hls S3 Settings Example
  slug: medialive-api-hls-s3-settings-example
- key_count: 0
  name: Medialive Api Hls Scte35 Source Type Example
  slug: medialive-api-hls-scte35-source-type-example
- key_count: 0
  name: Medialive Api Hls Segmentation Mode Example
  slug: medialive-api-hls-segmentation-mode-example
- key_count: 4
  name: Medialive Api Hls Settings Example
  slug: medialive-api-hls-settings-example
- key_count: 0
  name: Medialive Api Hls Stream Inf Resolution Example
  slug: medialive-api-hls-stream-inf-resolution-example
- key_count: 0
  name: Medialive Api Hls Timed Metadata Id3 Frame Example
  slug: medialive-api-hls-timed-metadata-id3-frame-example
- key_count: 1
  name: Medialive Api Hls Timed Metadata Schedule Action Settings Example
  slug: medialive-api-hls-timed-metadata-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Hls Ts File Mode Example
  slug: medialive-api-hls-ts-file-mode-example
- key_count: 0
  name: Medialive Api Hls Webdav Http Transfer Mode Example
  slug: medialive-api-hls-webdav-http-transfer-mode-example
- key_count: 5
  name: Medialive Api Hls Webdav Settings Example
  slug: medialive-api-hls-webdav-settings-example
- key_count: 0
  name: Medialive Api Html Motion Graphics Settings Example
  slug: medialive-api-html-motion-graphics-settings-example
- key_count: 0
  name: Medialive Api I Frame Only Playlist Type Example
  slug: medialive-api-i-frame-only-playlist-type-example
- key_count: 0
  name: Medialive Api Immediate Mode Schedule Action Start Settings Example
  slug: medialive-api-immediate-mode-schedule-action-start-settings-example
- key_count: 4
  name: Medialive Api Input Attachment Example
  slug: medialive-api-input-attachment-example
- key_count: 2
  name: Medialive Api Input Channel Level Example
  slug: medialive-api-input-channel-level-example
- key_count: 0
  name: Medialive Api Input Class Example
  slug: medialive-api-input-class-example
- key_count: 3
  name: Medialive Api Input Clipping Settings Example
  slug: medialive-api-input-clipping-settings-example
- key_count: 0
  name: Medialive Api Input Codec Example
  slug: medialive-api-input-codec-example
- key_count: 0
  name: Medialive Api Input Deblock Filter Example
  slug: medialive-api-input-deblock-filter-example
- key_count: 0
  name: Medialive Api Input Denoise Filter Example
  slug: medialive-api-input-denoise-filter-example
- key_count: 4
  name: Medialive Api Input Destination Example
  slug: medialive-api-input-destination-example
- key_count: 1
  name: Medialive Api Input Destination Request Example
  slug: medialive-api-input-destination-request-example
- key_count: 2
  name: Medialive Api Input Destination Vpc Example
  slug: medialive-api-input-destination-vpc-example
- key_count: 0
  name: Medialive Api Input Device Active Input Example
  slug: medialive-api-input-device-active-input-example
- key_count: 3
  name: Medialive Api Input Device Configurable Settings Example
  slug: medialive-api-input-device-configurable-settings-example
- key_count: 0
  name: Medialive Api Input Device Configured Input Example
  slug: medialive-api-input-device-configured-input-example
- key_count: 0
  name: Medialive Api Input Device Connection State Example
  slug: medialive-api-input-device-connection-state-example
- key_count: 9
  name: Medialive Api Input Device Hd Settings Example
  slug: medialive-api-input-device-hd-settings-example
- key_count: 0
  name: Medialive Api Input Device Ip Scheme Example
  slug: medialive-api-input-device-ip-scheme-example
- key_count: 5
  name: Medialive Api Input Device Network Settings Example
  slug: medialive-api-input-device-network-settings-example
- key_count: 1
  name: Medialive Api Input Device Request Example
  slug: medialive-api-input-device-request-example
- key_count: 0
  name: Medialive Api Input Device Scan Type Example
  slug: medialive-api-input-device-scan-type-example
- key_count: 1
  name: Medialive Api Input Device Settings Example
  slug: medialive-api-input-device-settings-example
- key_count: 0
  name: Medialive Api Input Device State Example
  slug: medialive-api-input-device-state-example
- key_count: 13
  name: Medialive Api Input Device Summary Example
  slug: medialive-api-input-device-summary-example
- key_count: 0
  name: Medialive Api Input Device Thumbnail Example
  slug: medialive-api-input-device-thumbnail-example
- key_count: 0
  name: Medialive Api Input Device Transfer Type Example
  slug: medialive-api-input-device-transfer-type-example
- key_count: 0
  name: Medialive Api Input Device Type Example
  slug: medialive-api-input-device-type-example
- key_count: 9
  name: Medialive Api Input Device Uhd Settings Example
  slug: medialive-api-input-device-uhd-settings-example
- key_count: 16
  name: Medialive Api Input Example
  slug: medialive-api-input-example
- key_count: 0
  name: Medialive Api Input Filter Example
  slug: medialive-api-input-filter-example
- key_count: 3
  name: Medialive Api Input Location Example
  slug: medialive-api-input-location-example
- key_count: 0
  name: Medialive Api Input Loss Action For Hls Out Example
  slug: medialive-api-input-loss-action-for-hls-out-example
- key_count: 0
  name: Medialive Api Input Loss Action For Ms Smooth Out Example
  slug: medialive-api-input-loss-action-for-ms-smooth-out-example
- key_count: 0
  name: Medialive Api Input Loss Action For Rtmp Out Example
  slug: medialive-api-input-loss-action-for-rtmp-out-example
- key_count: 0
  name: Medialive Api Input Loss Action For Udp Out Example
  slug: medialive-api-input-loss-action-for-udp-out-example
- key_count: 5
  name: Medialive Api Input Loss Behavior Example
  slug: medialive-api-input-loss-behavior-example
- key_count: 1
  name: Medialive Api Input Loss Failover Settings Example
  slug: medialive-api-input-loss-failover-settings-example
- key_count: 0
  name: Medialive Api Input Loss Image Type Example
  slug: medialive-api-input-loss-image-type-example
- key_count: 0
  name: Medialive Api Input Maximum Bitrate Example
  slug: medialive-api-input-maximum-bitrate-example
- key_count: 0
  name: Medialive Api Input Preference Example
  slug: medialive-api-input-preference-example
- key_count: 3
  name: Medialive Api Input Prepare Schedule Action Settings Example
  slug: medialive-api-input-prepare-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Input Resolution Example
  slug: medialive-api-input-resolution-example
- key_count: 6
  name: Medialive Api Input Security Group Example
  slug: medialive-api-input-security-group-example
- key_count: 0
  name: Medialive Api Input Security Group State Example
  slug: medialive-api-input-security-group-state-example
- key_count: 11
  name: Medialive Api Input Settings Example
  slug: medialive-api-input-settings-example
- key_count: 0
  name: Medialive Api Input Source End Behavior Example
  slug: medialive-api-input-source-end-behavior-example
- key_count: 3
  name: Medialive Api Input Source Example
  slug: medialive-api-input-source-example
- key_count: 3
  name: Medialive Api Input Source Request Example
  slug: medialive-api-input-source-request-example
- key_count: 0
  name: Medialive Api Input Source Type Example
  slug: medialive-api-input-source-type-example
- key_count: 3
  name: Medialive Api Input Specification Example
  slug: medialive-api-input-specification-example
- key_count: 0
  name: Medialive Api Input State Example
  slug: medialive-api-input-state-example
- key_count: 3
  name: Medialive Api Input Switch Schedule Action Settings Example
  slug: medialive-api-input-switch-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Input Timecode Source Example
  slug: medialive-api-input-timecode-source-example
- key_count: 0
  name: Medialive Api Input Type Example
  slug: medialive-api-input-type-example
- key_count: 2
  name: Medialive Api Input Vpc Request Example
  slug: medialive-api-input-vpc-request-example
- key_count: 1
  name: Medialive Api Input Whitelist Rule Cidr Example
  slug: medialive-api-input-whitelist-rule-cidr-example
- key_count: 1
  name: Medialive Api Input Whitelist Rule Example
  slug: medialive-api-input-whitelist-rule-example
- key_count: 1
  name: Medialive Api Key Provider Settings Example
  slug: medialive-api-key-provider-settings-example
- key_count: 0
  name: Medialive Api Last Frame Clipping Behavior Example
  slug: medialive-api-last-frame-clipping-behavior-example
- key_count: 0
  name: Medialive Api List Channels Request Example
  slug: medialive-api-list-channels-request-example
- key_count: 2
  name: Medialive Api List Channels Response Example
  slug: medialive-api-list-channels-response-example
- key_count: 0
  name: Medialive Api List Input Device Transfers Request Example
  slug: medialive-api-list-input-device-transfers-request-example
- key_count: 2
  name: Medialive Api List Input Device Transfers Response Example
  slug: medialive-api-list-input-device-transfers-response-example
- key_count: 0
  name: Medialive Api List Input Devices Request Example
  slug: medialive-api-list-input-devices-request-example
- key_count: 2
  name: Medialive Api List Input Devices Response Example
  slug: medialive-api-list-input-devices-response-example
- key_count: 0
  name: Medialive Api List Input Security Groups Request Example
  slug: medialive-api-list-input-security-groups-request-example
- key_count: 2
  name: Medialive Api List Input Security Groups Response Example
  slug: medialive-api-list-input-security-groups-response-example
- key_count: 0
  name: Medialive Api List Inputs Request Example
  slug: medialive-api-list-inputs-request-example
- key_count: 2
  name: Medialive Api List Inputs Response Example
  slug: medialive-api-list-inputs-response-example
- key_count: 0
  name: Medialive Api List Multiplex Programs Request Example
  slug: medialive-api-list-multiplex-programs-request-example
- key_count: 2
  name: Medialive Api List Multiplex Programs Response Example
  slug: medialive-api-list-multiplex-programs-response-example
- key_count: 0
  name: Medialive Api List Multiplexes Request Example
  slug: medialive-api-list-multiplexes-request-example
- key_count: 2
  name: Medialive Api List Multiplexes Response Example
  slug: medialive-api-list-multiplexes-response-example
- key_count: 0
  name: Medialive Api List Offerings Request Example
  slug: medialive-api-list-offerings-request-example
- key_count: 2
  name: Medialive Api List Offerings Response Example
  slug: medialive-api-list-offerings-response-example
- key_count: 0
  name: Medialive Api List Reservations Request Example
  slug: medialive-api-list-reservations-request-example
- key_count: 2
  name: Medialive Api List Reservations Response Example
  slug: medialive-api-list-reservations-response-example
- key_count: 0
  name: Medialive Api List Tags For Resource Request Example
  slug: medialive-api-list-tags-for-resource-request-example
- key_count: 1
  name: Medialive Api List Tags For Resource Response Example
  slug: medialive-api-list-tags-for-resource-response-example
- key_count: 0
  name: Medialive Api Log Level Example
  slug: medialive-api-log-level-example
- key_count: 0
  name: Medialive Api M2Ts Absent Input Audio Behavior Example
  slug: medialive-api-m2ts-absent-input-audio-behavior-example
- key_count: 0
  name: Medialive Api M2Ts Arib Captions Pid Control Example
  slug: medialive-api-m2ts-arib-captions-pid-control-example
- key_count: 0
  name: Medialive Api M2Ts Arib Example
  slug: medialive-api-m2ts-arib-example
- key_count: 0
  name: Medialive Api M2Ts Audio Buffer Model Example
  slug: medialive-api-m2ts-audio-buffer-model-example
- key_count: 0
  name: Medialive Api M2Ts Audio Interval Example
  slug: medialive-api-m2ts-audio-interval-example
- key_count: 0
  name: Medialive Api M2Ts Audio Stream Type Example
  slug: medialive-api-m2ts-audio-stream-type-example
- key_count: 0
  name: Medialive Api M2Ts Buffer Model Example
  slug: medialive-api-m2ts-buffer-model-example
- key_count: 0
  name: Medialive Api M2Ts Cc Descriptor Example
  slug: medialive-api-m2ts-cc-descriptor-example
- key_count: 0
  name: Medialive Api M2Ts Ebif Control Example
  slug: medialive-api-m2ts-ebif-control-example
- key_count: 0
  name: Medialive Api M2Ts Ebp Placement Example
  slug: medialive-api-m2ts-ebp-placement-example
- key_count: 0
  name: Medialive Api M2Ts Es Rate In Pes Example
  slug: medialive-api-m2ts-es-rate-in-pes-example
- key_count: 0
  name: Medialive Api M2Ts Klv Example
  slug: medialive-api-m2ts-klv-example
- key_count: 0
  name: Medialive Api M2Ts Nielsen Id3 Behavior Example
  slug: medialive-api-m2ts-nielsen-id3-behavior-example
- key_count: 0
  name: Medialive Api M2Ts Pcr Control Example
  slug: medialive-api-m2ts-pcr-control-example
- key_count: 0
  name: Medialive Api M2Ts Rate Mode Example
  slug: medialive-api-m2ts-rate-mode-example
- key_count: 0
  name: Medialive Api M2Ts Scte35 Control Example
  slug: medialive-api-m2ts-scte35-control-example
- key_count: 0
  name: Medialive Api M2Ts Segmentation Markers Example
  slug: medialive-api-m2ts-segmentation-markers-example
- key_count: 0
  name: Medialive Api M2Ts Segmentation Style Example
  slug: medialive-api-m2ts-segmentation-style-example
- key_count: 48
  name: Medialive Api M2Ts Settings Example
  slug: medialive-api-m2ts-settings-example
- key_count: 0
  name: Medialive Api M2Ts Timed Metadata Behavior Example
  slug: medialive-api-m2ts-timed-metadata-behavior-example
- key_count: 0
  name: Medialive Api M3U8 Nielsen Id3 Behavior Example
  slug: medialive-api-m3u8-nielsen-id3-behavior-example
- key_count: 0
  name: Medialive Api M3U8 Pcr Control Example
  slug: medialive-api-m3u8-pcr-control-example
- key_count: 0
  name: Medialive Api M3U8 Scte35 Behavior Example
  slug: medialive-api-m3u8-scte35-behavior-example
- key_count: 17
  name: Medialive Api M3U8 Settings Example
  slug: medialive-api-m3u8-settings-example
- key_count: 0
  name: Medialive Api M3U8 Timed Metadata Behavior Example
  slug: medialive-api-m3u8-timed-metadata-behavior-example
- key_count: 2
  name: Medialive Api Maintenance Create Settings Example
  slug: medialive-api-maintenance-create-settings-example
- key_count: 0
  name: Medialive Api Maintenance Day Example
  slug: medialive-api-maintenance-day-example
- key_count: 4
  name: Medialive Api Maintenance Status Example
  slug: medialive-api-maintenance-status-example
- key_count: 3
  name: Medialive Api Maintenance Update Settings Example
  slug: medialive-api-maintenance-update-settings-example
- key_count: 0
  name: Medialive Api Max Results Example
  slug: medialive-api-max-results-example
- key_count: 1
  name: Medialive Api Media Connect Flow Example
  slug: medialive-api-media-connect-flow-example
- key_count: 1
  name: Medialive Api Media Connect Flow Request Example
  slug: medialive-api-media-connect-flow-request-example
- key_count: 1
  name: Medialive Api Media Package Group Settings Example
  slug: medialive-api-media-package-group-settings-example
- key_count: 1
  name: Medialive Api Media Package Output Destination Settings Example
  slug: medialive-api-media-package-output-destination-settings-example
- key_count: 0
  name: Medialive Api Media Package Output Settings Example
  slug: medialive-api-media-package-output-settings-example
- key_count: 4
  name: Medialive Api Motion Graphics Activate Schedule Action Settings Example
  slug: medialive-api-motion-graphics-activate-schedule-action-settings-example
- key_count: 2
  name: Medialive Api Motion Graphics Configuration Example
  slug: medialive-api-motion-graphics-configuration-example
- key_count: 0
  name: Medialive Api Motion Graphics Deactivate Schedule Action Settings Example
  slug: medialive-api-motion-graphics-deactivate-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Motion Graphics Insertion Example
  slug: medialive-api-motion-graphics-insertion-example
- key_count: 1
  name: Medialive Api Motion Graphics Settings Example
  slug: medialive-api-motion-graphics-settings-example
- key_count: 0
  name: Medialive Api Mp2 Coding Mode Example
  slug: medialive-api-mp2-coding-mode-example
- key_count: 3
  name: Medialive Api Mp2 Settings Example
  slug: medialive-api-mp2-settings-example
- key_count: 0
  name: Medialive Api Mpeg2 Adaptive Quantization Example
  slug: medialive-api-mpeg2-adaptive-quantization-example
- key_count: 0
  name: Medialive Api Mpeg2 Color Metadata Example
  slug: medialive-api-mpeg2-color-metadata-example
- key_count: 0
  name: Medialive Api Mpeg2 Color Space Example
  slug: medialive-api-mpeg2-color-space-example
- key_count: 0
  name: Medialive Api Mpeg2 Display Ratio Example
  slug: medialive-api-mpeg2-display-ratio-example
- key_count: 1
  name: Medialive Api Mpeg2 Filter Settings Example
  slug: medialive-api-mpeg2-filter-settings-example
- key_count: 0
  name: Medialive Api Mpeg2 Gop Size Units Example
  slug: medialive-api-mpeg2-gop-size-units-example
- key_count: 0
  name: Medialive Api Mpeg2 Scan Type Example
  slug: medialive-api-mpeg2-scan-type-example
- key_count: 17
  name: Medialive Api Mpeg2 Settings Example
  slug: medialive-api-mpeg2-settings-example
- key_count: 0
  name: Medialive Api Mpeg2 Sub Gop Length Example
  slug: medialive-api-mpeg2-sub-gop-length-example
- key_count: 0
  name: Medialive Api Mpeg2 Timecode Insertion Behavior Example
  slug: medialive-api-mpeg2-timecode-insertion-behavior-example
- key_count: 19
  name: Medialive Api Ms Smooth Group Settings Example
  slug: medialive-api-ms-smooth-group-settings-example
- key_count: 0
  name: Medialive Api Ms Smooth H265 Packaging Type Example
  slug: medialive-api-ms-smooth-h265-packaging-type-example
- key_count: 2
  name: Medialive Api Ms Smooth Output Settings Example
  slug: medialive-api-ms-smooth-output-settings-example
- key_count: 10
  name: Medialive Api Multiplex Example
  slug: medialive-api-multiplex-example
- key_count: 0
  name: Medialive Api Multiplex Group Settings Example
  slug: medialive-api-multiplex-group-settings-example
- key_count: 1
  name: Medialive Api Multiplex Media Connect Output Destination Settings Example
  slug: medialive-api-multiplex-media-connect-output-destination-settings-example
- key_count: 1
  name: Medialive Api Multiplex Output Destination Example
  slug: medialive-api-multiplex-output-destination-example
- key_count: 1
  name: Medialive Api Multiplex Output Settings Example
  slug: medialive-api-multiplex-output-settings-example
- key_count: 2
  name: Medialive Api Multiplex Program Channel Destination Settings Example
  slug: medialive-api-multiplex-program-channel-destination-settings-example
- key_count: 5
  name: Medialive Api Multiplex Program Example
  slug: medialive-api-multiplex-program-example
- key_count: 13
  name: Medialive Api Multiplex Program Packet Identifiers Map Example
  slug: medialive-api-multiplex-program-packet-identifiers-map-example
- key_count: 2
  name: Medialive Api Multiplex Program Pipeline Detail Example
  slug: medialive-api-multiplex-program-pipeline-detail-example
- key_count: 2
  name: Medialive Api Multiplex Program Service Descriptor Example
  slug: medialive-api-multiplex-program-service-descriptor-example
- key_count: 4
  name: Medialive Api Multiplex Program Settings Example
  slug: medialive-api-multiplex-program-settings-example
- key_count: 2
  name: Medialive Api Multiplex Program Summary Example
  slug: medialive-api-multiplex-program-summary-example
- key_count: 4
  name: Medialive Api Multiplex Settings Example
  slug: medialive-api-multiplex-settings-example
- key_count: 1
  name: Medialive Api Multiplex Settings Summary Example
  slug: medialive-api-multiplex-settings-summary-example
- key_count: 0
  name: Medialive Api Multiplex State Example
  slug: medialive-api-multiplex-state-example
- key_count: 3
  name: Medialive Api Multiplex Statmux Video Settings Example
  slug: medialive-api-multiplex-statmux-video-settings-example
- key_count: 9
  name: Medialive Api Multiplex Summary Example
  slug: medialive-api-multiplex-summary-example
- key_count: 2
  name: Medialive Api Multiplex Video Settings Example
  slug: medialive-api-multiplex-video-settings-example
- key_count: 0
  name: Medialive Api Network Input Server Validation Example
  slug: medialive-api-network-input-server-validation-example
- key_count: 2
  name: Medialive Api Network Input Settings Example
  slug: medialive-api-network-input-settings-example
- key_count: 3
  name: Medialive Api Nielsen Cbet Example
  slug: medialive-api-nielsen-cbet-example
- key_count: 2
  name: Medialive Api Nielsen Configuration Example
  slug: medialive-api-nielsen-configuration-example
- key_count: 3
  name: Medialive Api Nielsen Naes Ii Nw Example
  slug: medialive-api-nielsen-naes-ii-nw-example
- key_count: 0
  name: Medialive Api Nielsen Pcm To Id3 Tagging State Example
  slug: medialive-api-nielsen-pcm-to-id3-tagging-state-example
- key_count: 0
  name: Medialive Api Nielsen Watermark Timezones Example
  slug: medialive-api-nielsen-watermark-timezones-example
- key_count: 0
  name: Medialive Api Nielsen Watermarks Cbet Stepaside Example
  slug: medialive-api-nielsen-watermarks-cbet-stepaside-example
- key_count: 0
  name: Medialive Api Nielsen Watermarks Distribution Types Example
  slug: medialive-api-nielsen-watermarks-distribution-types-example
- key_count: 3
  name: Medialive Api Nielsen Watermarks Settings Example
  slug: medialive-api-nielsen-watermarks-settings-example
- key_count: 0
  name: Medialive Api Offering Duration Units Example
  slug: medialive-api-offering-duration-units-example
- key_count: 11
  name: Medialive Api Offering Example
  slug: medialive-api-offering-example
- key_count: 0
  name: Medialive Api Offering Type Example
  slug: medialive-api-offering-type-example
- key_count: 4
  name: Medialive Api Output Destination Example
  slug: medialive-api-output-destination-example
- key_count: 4
  name: Medialive Api Output Destination Settings Example
  slug: medialive-api-output-destination-settings-example
- key_count: 5
  name: Medialive Api Output Example
  slug: medialive-api-output-example
- key_count: 3
  name: Medialive Api Output Group Example
  slug: medialive-api-output-group-example
- key_count: 8
  name: Medialive Api Output Group Settings Example
  slug: medialive-api-output-group-settings-example
- key_count: 1
  name: Medialive Api Output Location Ref Example
  slug: medialive-api-output-location-ref-example
- key_count: 8
  name: Medialive Api Output Settings Example
  slug: medialive-api-output-settings-example
- key_count: 0
  name: Medialive Api Pass Through Settings Example
  slug: medialive-api-pass-through-settings-example
- key_count: 1
  name: Medialive Api Pause State Schedule Action Settings Example
  slug: medialive-api-pause-state-schedule-action-settings-example
- key_count: 5
  name: Medialive Api Pipeline Detail Example
  slug: medialive-api-pipeline-detail-example
- key_count: 0
  name: Medialive Api Pipeline Id Example
  slug: medialive-api-pipeline-id-example
- key_count: 1
  name: Medialive Api Pipeline Pause State Settings Example
  slug: medialive-api-pipeline-pause-state-settings-example
- key_count: 0
  name: Medialive Api Preferred Channel Pipeline Example
  slug: medialive-api-preferred-channel-pipeline-example
- key_count: 6
  name: Medialive Api Purchase Offering Request Example
  slug: medialive-api-purchase-offering-request-example
- key_count: 1
  name: Medialive Api Purchase Offering Response Example
  slug: medialive-api-purchase-offering-response-example
- key_count: 0
  name: Medialive Api Raw Settings Example
  slug: medialive-api-raw-settings-example
- key_count: 0
  name: Medialive Api Reboot Input Device Force Example
  slug: medialive-api-reboot-input-device-force-example
- key_count: 1
  name: Medialive Api Reboot Input Device Request Example
  slug: medialive-api-reboot-input-device-request-example
- key_count: 0
  name: Medialive Api Reboot Input Device Response Example
  slug: medialive-api-reboot-input-device-response-example
- key_count: 0
  name: Medialive Api Rec601 Settings Example
  slug: medialive-api-rec601-settings-example
- key_count: 0
  name: Medialive Api Rec709 Settings Example
  slug: medialive-api-rec709-settings-example
- key_count: 0
  name: Medialive Api Reject Input Device Transfer Request Example
  slug: medialive-api-reject-input-device-transfer-request-example
- key_count: 0
  name: Medialive Api Reject Input Device Transfer Response Example
  slug: medialive-api-reject-input-device-transfer-response-example
- key_count: 3
  name: Medialive Api Remix Settings Example
  slug: medialive-api-remix-settings-example
- key_count: 2
  name: Medialive Api Renewal Settings Example
  slug: medialive-api-renewal-settings-example
- key_count: 0
  name: Medialive Api Reservation Automatic Renewal Example
  slug: medialive-api-reservation-automatic-renewal-example
- key_count: 0
  name: Medialive Api Reservation Codec Example
  slug: medialive-api-reservation-codec-example
- key_count: 19
  name: Medialive Api Reservation Example
  slug: medialive-api-reservation-example
- key_count: 0
  name: Medialive Api Reservation Maximum Bitrate Example
  slug: medialive-api-reservation-maximum-bitrate-example
- key_count: 0
  name: Medialive Api Reservation Maximum Framerate Example
  slug: medialive-api-reservation-maximum-framerate-example
- key_count: 0
  name: Medialive Api Reservation Resolution Example
  slug: medialive-api-reservation-resolution-example
- key_count: 8
  name: Medialive Api Reservation Resource Specification Example
  slug: medialive-api-reservation-resource-specification-example
- key_count: 0
  name: Medialive Api Reservation Resource Type Example
  slug: medialive-api-reservation-resource-type-example
- key_count: 0
  name: Medialive Api Reservation Special Feature Example
  slug: medialive-api-reservation-special-feature-example
- key_count: 0
  name: Medialive Api Reservation State Example
  slug: medialive-api-reservation-state-example
- key_count: 0
  name: Medialive Api Reservation Video Quality Example
  slug: medialive-api-reservation-video-quality-example
- key_count: 0
  name: Medialive Api Rtmp Ad Markers Example
  slug: medialive-api-rtmp-ad-markers-example
- key_count: 0
  name: Medialive Api Rtmp Cache Full Behavior Example
  slug: medialive-api-rtmp-cache-full-behavior-example
- key_count: 0
  name: Medialive Api Rtmp Caption Data Example
  slug: medialive-api-rtmp-caption-data-example
- key_count: 0
  name: Medialive Api Rtmp Caption Info Destination Settings Example
  slug: medialive-api-rtmp-caption-info-destination-settings-example
- key_count: 7
  name: Medialive Api Rtmp Group Settings Example
  slug: medialive-api-rtmp-group-settings-example
- key_count: 0
  name: Medialive Api Rtmp Output Certificate Mode Example
  slug: medialive-api-rtmp-output-certificate-mode-example
- key_count: 4
  name: Medialive Api Rtmp Output Settings Example
  slug: medialive-api-rtmp-output-settings-example
- key_count: 0
  name: Medialive Api S3 Canned Acl Example
  slug: medialive-api-s3-canned-acl-example
- key_count: 3
  name: Medialive Api Schedule Action Example
  slug: medialive-api-schedule-action-example
- key_count: 13
  name: Medialive Api Schedule Action Settings Example
  slug: medialive-api-schedule-action-settings-example
- key_count: 3
  name: Medialive Api Schedule Action Start Settings Example
  slug: medialive-api-schedule-action-start-settings-example
- key_count: 0
  name: Medialive Api Scte20 Convert608 To708 Example
  slug: medialive-api-scte20-convert608-to708-example
- key_count: 0
  name: Medialive Api Scte20 Plus Embedded Destination Settings Example
  slug: medialive-api-scte20-plus-embedded-destination-settings-example
- key_count: 2
  name: Medialive Api Scte20 Source Settings Example
  slug: medialive-api-scte20-source-settings-example
- key_count: 0
  name: Medialive Api Scte27 Destination Settings Example
  slug: medialive-api-scte27-destination-settings-example
- key_count: 0
  name: Medialive Api Scte27 Ocr Language Example
  slug: medialive-api-scte27-ocr-language-example
- key_count: 2
  name: Medialive Api Scte27 Source Settings Example
  slug: medialive-api-scte27-source-settings-example
- key_count: 0
  name: Medialive Api Scte35 Apos No Regional Blackout Behavior Example
  slug: medialive-api-scte35-apos-no-regional-blackout-behavior-example
- key_count: 0
  name: Medialive Api Scte35 Apos Web Delivery Allowed Behavior Example
  slug: medialive-api-scte35-apos-web-delivery-allowed-behavior-example
- key_count: 0
  name: Medialive Api Scte35 Archive Allowed Flag Example
  slug: medialive-api-scte35-archive-allowed-flag-example
- key_count: 4
  name: Medialive Api Scte35 Delivery Restrictions Example
  slug: medialive-api-scte35-delivery-restrictions-example
- key_count: 1
  name: Medialive Api Scte35 Descriptor Example
  slug: medialive-api-scte35-descriptor-example
- key_count: 1
  name: Medialive Api Scte35 Descriptor Settings Example
  slug: medialive-api-scte35-descriptor-settings-example
- key_count: 0
  name: Medialive Api Scte35 Device Restrictions Example
  slug: medialive-api-scte35-device-restrictions-example
- key_count: 0
  name: Medialive Api Scte35 Input Mode Example
  slug: medialive-api-scte35-input-mode-example
- key_count: 2
  name: Medialive Api Scte35 Input Schedule Action Settings Example
  slug: medialive-api-scte35-input-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Scte35 No Regional Blackout Flag Example
  slug: medialive-api-scte35-no-regional-blackout-flag-example
- key_count: 1
  name: Medialive Api Scte35 Return To Network Schedule Action Settings Example
  slug: medialive-api-scte35-return-to-network-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Scte35 Segmentation Cancel Indicator Example
  slug: medialive-api-scte35-segmentation-cancel-indicator-example
- key_count: 11
  name: Medialive Api Scte35 Segmentation Descriptor Example
  slug: medialive-api-scte35-segmentation-descriptor-example
- key_count: 3
  name: Medialive Api Scte35 Splice Insert Example
  slug: medialive-api-scte35-splice-insert-example
- key_count: 0
  name: Medialive Api Scte35 Splice Insert No Regional Blackout Behavior Example
  slug: medialive-api-scte35-splice-insert-no-regional-blackout-behavior-example
- key_count: 2
  name: Medialive Api Scte35 Splice Insert Schedule Action Settings Example
  slug: medialive-api-scte35-splice-insert-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Scte35 Splice Insert Web Delivery Allowed Behavior Example
  slug: medialive-api-scte35-splice-insert-web-delivery-allowed-behavior-example
- key_count: 3
  name: Medialive Api Scte35 Time Signal Apos Example
  slug: medialive-api-scte35-time-signal-apos-example
- key_count: 1
  name: Medialive Api Scte35 Time Signal Schedule Action Settings Example
  slug: medialive-api-scte35-time-signal-schedule-action-settings-example
- key_count: 0
  name: Medialive Api Scte35 Web Delivery Allowed Flag Example
  slug: medialive-api-scte35-web-delivery-allowed-flag-example
- key_count: 0
  name: Medialive Api Smooth Group Audio Only Timecode Control Example
  slug: medialive-api-smooth-group-audio-only-timecode-control-example
- key_count: 0
  name: Medialive Api Smooth Group Certificate Mode Example
  slug: medialive-api-smooth-group-certificate-mode-example
- key_count: 0
  name: Medialive Api Smooth Group Event Id Mode Example
  slug: medialive-api-smooth-group-event-id-mode-example
- key_count: 0
  name: Medialive Api Smooth Group Event Stop Behavior Example
  slug: medialive-api-smooth-group-event-stop-behavior-example
- key_count: 0
  name: Medialive Api Smooth Group Segmentation Mode Example
  slug: medialive-api-smooth-group-segmentation-mode-example
- key_count: 0
  name: Medialive Api Smooth Group Sparse Track Type Example
  slug: medialive-api-smooth-group-sparse-track-type-example
- key_count: 0
  name: Medialive Api Smooth Group Stream Manifest Behavior Example
  slug: medialive-api-smooth-group-stream-manifest-behavior-example
- key_count: 0
  name: Medialive Api Smooth Group Timestamp Offset Mode Example
  slug: medialive-api-smooth-group-timestamp-offset-mode-example
- key_count: 0
  name: Medialive Api Smpte Tt Destination Settings Example
  slug: medialive-api-smpte-tt-destination-settings-example
- key_count: 0
  name: Medialive Api Smpte2038 Data Preference Example
  slug: medialive-api-smpte2038-data-preference-example
- key_count: 2
  name: Medialive Api Standard Hls Settings Example
  slug: medialive-api-standard-hls-settings-example
- key_count: 0
  name: Medialive Api Start Channel Request Example
  slug: medialive-api-start-channel-request-example
- key_count: 18
  name: Medialive Api Start Channel Response Example
  slug: medialive-api-start-channel-response-example
- key_count: 0
  name: Medialive Api Start Input Device Maintenance Window Request Example
  slug: medialive-api-start-input-device-maintenance-window-request-example
- key_count: 0
  name: Medialive Api Start Input Device Maintenance Window Response Example
  slug: medialive-api-start-input-device-maintenance-window-response-example
- key_count: 0
  name: Medialive Api Start Multiplex Request Example
  slug: medialive-api-start-multiplex-request-example
- key_count: 10
  name: Medialive Api Start Multiplex Response Example
  slug: medialive-api-start-multiplex-response-example
- key_count: 1
  name: Medialive Api Start Timecode Example
  slug: medialive-api-start-timecode-example
- key_count: 10
  name: Medialive Api Static Image Activate Schedule Action Settings Example
  slug: medialive-api-static-image-activate-schedule-action-settings-example
- key_count: 2
  name: Medialive Api Static Image Deactivate Schedule Action Settings Example
  slug: medialive-api-static-image-deactivate-schedule-action-settings-example
- key_count: 2
  name: Medialive Api Static Key Settings Example
  slug: medialive-api-static-key-settings-example
- key_count: 0
  name: Medialive Api Stop Channel Request Example
  slug: medialive-api-stop-channel-request-example
- key_count: 18
  name: Medialive Api Stop Channel Response Example
  slug: medialive-api-stop-channel-response-example
- key_count: 0
  name: Medialive Api Stop Multiplex Request Example
  slug: medialive-api-stop-multiplex-request-example
- key_count: 10
  name: Medialive Api Stop Multiplex Response Example
  slug: medialive-api-stop-multiplex-response-example
- key_count: 2
  name: Medialive Api Stop Timecode Example
  slug: medialive-api-stop-timecode-example
- key_count: 0
  name: Medialive Api Tags Example
  slug: medialive-api-tags-example
- key_count: 0
  name: Medialive Api Teletext Destination Settings Example
  slug: medialive-api-teletext-destination-settings-example
- key_count: 2
  name: Medialive Api Teletext Source Settings Example
  slug: medialive-api-teletext-source-settings-example
- key_count: 0
  name: Medialive Api Temporal Filter Post Filter Sharpening Example
  slug: medialive-api-temporal-filter-post-filter-sharpening-example
- key_count: 2
  name: Medialive Api Temporal Filter Settings Example
  slug: medialive-api-temporal-filter-settings-example
- key_count: 0
  name: Medialive Api Temporal Filter Strength Example
  slug: medialive-api-temporal-filter-strength-example
- key_count: 0
  name: Medialive Api Timecode Burnin Font Size Example
  slug: medialive-api-timecode-burnin-font-size-example
- key_count: 0
  name: Medialive Api Timecode Burnin Position Example
  slug: medialive-api-timecode-burnin-position-example
- key_count: 3
  name: Medialive Api Timecode Burnin Settings Example
  slug: medialive-api-timecode-burnin-settings-example
- key_count: 2
  name: Medialive Api Timecode Config Example
  slug: medialive-api-timecode-config-example
- key_count: 0
  name: Medialive Api Timecode Config Source Example
  slug: medialive-api-timecode-config-source-example
- key_count: 3
  name: Medialive Api Transfer Input Device Request Example
  slug: medialive-api-transfer-input-device-request-example
- key_count: 0
  name: Medialive Api Transfer Input Device Response Example
  slug: medialive-api-transfer-input-device-response-example
- key_count: 4
  name: Medialive Api Transferring Input Device Summary Example
  slug: medialive-api-transferring-input-device-summary-example
- key_count: 1
  name: Medialive Api Ttml Destination Settings Example
  slug: medialive-api-ttml-destination-settings-example
- key_count: 0
  name: Medialive Api Ttml Destination Style Control Example
  slug: medialive-api-ttml-destination-style-control-example
- key_count: 1
  name: Medialive Api Udp Container Settings Example
  slug: medialive-api-udp-container-settings-example
- key_count: 3
  name: Medialive Api Udp Group Settings Example
  slug: medialive-api-udp-group-settings-example
- key_count: 4
  name: Medialive Api Udp Output Settings Example
  slug: medialive-api-udp-output-settings-example
- key_count: 0
  name: Medialive Api Udp Timed Metadata Id3 Frame Example
  slug: medialive-api-udp-timed-metadata-id3-frame-example
- key_count: 2
  name: Medialive Api Update Channel Class Request Example
  slug: medialive-api-update-channel-class-request-example
- key_count: 1
  name: Medialive Api Update Channel Class Response Example
  slug: medialive-api-update-channel-class-response-example
- key_count: 9
  name: Medialive Api Update Channel Request Example
  slug: medialive-api-update-channel-request-example
- key_count: 1
  name: Medialive Api Update Channel Response Example
  slug: medialive-api-update-channel-response-example
- key_count: 3
  name: Medialive Api Update Input Device Request Example
  slug: medialive-api-update-input-device-request-example
- key_count: 13
  name: Medialive Api Update Input Device Response Example
  slug: medialive-api-update-input-device-response-example
- key_count: 7
  name: Medialive Api Update Input Request Example
  slug: medialive-api-update-input-request-example
- key_count: 1
  name: Medialive Api Update Input Response Example
  slug: medialive-api-update-input-response-example
- key_count: 2
  name: Medialive Api Update Input Security Group Request Example
  slug: medialive-api-update-input-security-group-request-example
- key_count: 1
  name: Medialive Api Update Input Security Group Response Example
  slug: medialive-api-update-input-security-group-response-example
- key_count: 1
  name: Medialive Api Update Multiplex Program Request Example
  slug: medialive-api-update-multiplex-program-request-example
- key_count: 1
  name: Medialive Api Update Multiplex Program Response Example
  slug: medialive-api-update-multiplex-program-response-example
- key_count: 2
  name: Medialive Api Update Multiplex Request Example
  slug: medialive-api-update-multiplex-request-example
- key_count: 1
  name: Medialive Api Update Multiplex Response Example
  slug: medialive-api-update-multiplex-response-example
- key_count: 2
  name: Medialive Api Update Reservation Request Example
  slug: medialive-api-update-reservation-request-example
- key_count: 1
  name: Medialive Api Update Reservation Response Example
  slug: medialive-api-update-reservation-response-example
- key_count: 2
  name: Medialive Api Video Black Failover Settings Example
  slug: medialive-api-video-black-failover-settings-example
- key_count: 4
  name: Medialive Api Video Codec Settings Example
  slug: medialive-api-video-codec-settings-example
- key_count: 7
  name: Medialive Api Video Description Example
  slug: medialive-api-video-description-example
- key_count: 0
  name: Medialive Api Video Description Respond To Afd Example
  slug: medialive-api-video-description-respond-to-afd-example
- key_count: 0
  name: Medialive Api Video Description Scaling Behavior Example
  slug: medialive-api-video-description-scaling-behavior-example
- key_count: 0
  name: Medialive Api Video Selector Color Space Example
  slug: medialive-api-video-selector-color-space-example
- key_count: 1
  name: Medialive Api Video Selector Color Space Settings Example
  slug: medialive-api-video-selector-color-space-settings-example
- key_count: 0
  name: Medialive Api Video Selector Color Space Usage Example
  slug: medialive-api-video-selector-color-space-usage-example
- key_count: 4
  name: Medialive Api Video Selector Example
  slug: medialive-api-video-selector-example
- key_count: 1
  name: Medialive Api Video Selector Pid Example
  slug: medialive-api-video-selector-pid-example
- key_count: 1
  name: Medialive Api Video Selector Program Id Example
  slug: medialive-api-video-selector-program-id-example
- key_count: 2
  name: Medialive Api Video Selector Settings Example
  slug: medialive-api-video-selector-settings-example
- key_count: 4
  name: Medialive Api Vpc Output Settings Description Example
  slug: medialive-api-vpc-output-settings-description-example
- key_count: 3
  name: Medialive Api Vpc Output Settings Example
  slug: medialive-api-vpc-output-settings-example
- key_count: 0
  name: Medialive Api Wav Coding Mode Example
  slug: medialive-api-wav-coding-mode-example
- key_count: 3
  name: Medialive Api Wav Settings Example
  slug: medialive-api-wav-settings-example
- key_count: 1
  name: Medialive Api Webvtt Destination Settings Example
  slug: medialive-api-webvtt-destination-settings-example
- key_count: 0
  name: Medialive Api Webvtt Destination Style Control Example
  slug: medialive-api-webvtt-destination-style-control-example
features:
- description: Broadcast-grade live video encoding supporting H.264, H.265, and other professional codecs.
  name: Live Video Encoding
- description: Accept live video from RTP, RTMP, HLS pull, MediaConnect, MP4, and other source types.
  name: Multiple Input Types
- description: Pipeline redundancy for high-availability live events with automatic failover.
  name: Redundant Encoding
- description: Insert SCTE-35 markers for downstream ad replacement in live streams.
  name: Dynamic Ad Insertion Markers
- description: Deliver to HLS, DASH, RTMP, archive, UDP, MediaPackage, and other output destinations simultaneously.
  name: Multiple Output Groups
- description: Dynamically switch between input sources during a live event without interruption.
  name: Input Switching
finops:
- name: Amazon Medialive Finops
  service_category: API
  slug: amazon-medialive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-medialive.png
json_schemas:
- name: AacCodingMode
  property_count: 0
  slug: medialive-api-aac-coding-mode
- name: AacInputType
  property_count: 0
  slug: medialive-api-aac-input-type
- name: AacProfile
  property_count: 0
  slug: medialive-api-aac-profile
- name: AacRateControlMode
  property_count: 0
  slug: medialive-api-aac-rate-control-mode
- name: AacRawFormat
  property_count: 0
  slug: medialive-api-aac-raw-format
- name: AacSettings
  property_count: 9
  slug: medialive-api-aac-settings
- name: AacSpec
  property_count: 0
  slug: medialive-api-aac-spec
- name: AacVbrQuality
  property_count: 0
  slug: medialive-api-aac-vbr-quality
- name: Ac3BitstreamMode
  property_count: 0
  slug: medialive-api-ac3-bitstream-mode
- name: Ac3CodingMode
  property_count: 0
  slug: medialive-api-ac3-coding-mode
- name: Ac3DrcProfile
  property_count: 0
  slug: medialive-api-ac3-drc-profile
- name: Ac3LfeFilter
  property_count: 0
  slug: medialive-api-ac3-lfe-filter
- name: Ac3MetadataControl
  property_count: 0
  slug: medialive-api-ac3-metadata-control
- name: Ac3Settings
  property_count: 7
  slug: medialive-api-ac3-settings
- name: AcceptHeader
  property_count: 0
  slug: medialive-api-accept-header
- name: AcceptInputDeviceTransferRequest
  property_count: 0
  slug: medialive-api-accept-input-device-transfer-request
- name: AcceptInputDeviceTransferResponse
  property_count: 0
  slug: medialive-api-accept-input-device-transfer-response
- name: AccessibilityType
  property_count: 0
  slug: medialive-api-accessibility-type
- name: AfdSignaling
  property_count: 0
  slug: medialive-api-afd-signaling
- name: AncillarySourceSettings
  property_count: 1
  slug: medialive-api-ancillary-source-settings
- name: ArchiveCdnSettings
  property_count: 1
  slug: medialive-api-archive-cdn-settings
- name: ArchiveContainerSettings
  property_count: 2
  slug: medialive-api-archive-container-settings
- name: ArchiveGroupSettings
  property_count: 3
  slug: medialive-api-archive-group-settings
- name: ArchiveOutputSettings
  property_count: 3
  slug: medialive-api-archive-output-settings
- name: ArchiveS3Settings
  property_count: 1
  slug: medialive-api-archive-s3-settings
- name: AribDestinationSettings
  property_count: 0
  slug: medialive-api-arib-destination-settings
- name: AribSourceSettings
  property_count: 0
  slug: medialive-api-arib-source-settings
- name: AudioChannelMapping
  property_count: 2
  slug: medialive-api-audio-channel-mapping
- name: AudioCodecSettings
  property_count: 7
  slug: medialive-api-audio-codec-settings
- name: AudioDescriptionAudioTypeControl
  property_count: 0
  slug: medialive-api-audio-description-audio-type-control
- name: AudioDescriptionLanguageCodeControl
  property_count: 0
  slug: medialive-api-audio-description-language-code-control
- name: AudioDescription
  property_count: 11
  slug: medialive-api-audio-description
- name: AudioDolbyEDecode
  property_count: 1
  slug: medialive-api-audio-dolby-e-decode
- name: AudioHlsRenditionSelection
  property_count: 2
  slug: medialive-api-audio-hls-rendition-selection
- name: AudioLanguageSelectionPolicy
  property_count: 0
  slug: medialive-api-audio-language-selection-policy
- name: AudioLanguageSelection
  property_count: 2
  slug: medialive-api-audio-language-selection
- name: AudioNormalizationAlgorithmControl
  property_count: 0
  slug: medialive-api-audio-normalization-algorithm-control
- name: AudioNormalizationAlgorithm
  property_count: 0
  slug: medialive-api-audio-normalization-algorithm
- name: AudioNormalizationSettings
  property_count: 3
  slug: medialive-api-audio-normalization-settings
- name: AudioOnlyHlsSegmentType
  property_count: 0
  slug: medialive-api-audio-only-hls-segment-type
- name: AudioOnlyHlsSettings
  property_count: 4
  slug: medialive-api-audio-only-hls-settings
- name: AudioOnlyHlsTrackType
  property_count: 0
  slug: medialive-api-audio-only-hls-track-type
- name: AudioPidSelection
  property_count: 1
  slug: medialive-api-audio-pid-selection
- name: AudioSelector
  property_count: 2
  slug: medialive-api-audio-selector
- name: AudioSelectorSettings
  property_count: 4
  slug: medialive-api-audio-selector-settings
- name: AudioSilenceFailoverSettings
  property_count: 2
  slug: medialive-api-audio-silence-failover-settings
- name: AudioTrack
  property_count: 1
  slug: medialive-api-audio-track
- name: AudioTrackSelection
  property_count: 2
  slug: medialive-api-audio-track-selection
- name: AudioType
  property_count: 0
  slug: medialive-api-audio-type
- name: AudioWatermarkSettings
  property_count: 1
  slug: medialive-api-audio-watermark-settings
- name: AuthenticationScheme
  property_count: 0
  slug: medialive-api-authentication-scheme
- name: AutomaticInputFailoverSettings
  property_count: 4
  slug: medialive-api-automatic-input-failover-settings
- name: AvailBlanking
  property_count: 2
  slug: medialive-api-avail-blanking
- name: AvailBlankingState
  property_count: 0
  slug: medialive-api-avail-blanking-state
- name: AvailConfiguration
  property_count: 1
  slug: medialive-api-avail-configuration
- name: AvailSettings
  property_count: 3
  slug: medialive-api-avail-settings
- name: BadGatewayException
  property_count: 0
  slug: medialive-api-bad-gateway-exception
- name: BatchDeleteRequest
  property_count: 4
  slug: medialive-api-batch-delete-request
- name: BatchDeleteResponse
  property_count: 2
  slug: medialive-api-batch-delete-response
- name: BatchFailedResultModel
  property_count: 4
  slug: medialive-api-batch-failed-result-model
- name: BatchScheduleActionCreateRequest
  property_count: 1
  slug: medialive-api-batch-schedule-action-create-request
- name: BatchScheduleActionCreateResult
  property_count: 1
  slug: medialive-api-batch-schedule-action-create-result
- name: BatchScheduleActionDeleteRequest
  property_count: 1
  slug: medialive-api-batch-schedule-action-delete-request
- name: BatchScheduleActionDeleteResult
  property_count: 1
  slug: medialive-api-batch-schedule-action-delete-result
- name: BatchStartRequest
  property_count: 2
  slug: medialive-api-batch-start-request
- name: BatchStartResponse
  property_count: 2
  slug: medialive-api-batch-start-response
- name: BatchStopRequest
  property_count: 2
  slug: medialive-api-batch-stop-request
- name: BatchStopResponse
  property_count: 2
  slug: medialive-api-batch-stop-response
- name: BatchSuccessfulResultModel
  property_count: 3
  slug: medialive-api-batch-successful-result-model
- name: BatchUpdateScheduleRequest
  property_count: 2
  slug: medialive-api-batch-update-schedule-request
- name: BatchUpdateScheduleResponse
  property_count: 2
  slug: medialive-api-batch-update-schedule-response
- name: BlackoutSlateNetworkEndBlackout
  property_count: 0
  slug: medialive-api-blackout-slate-network-end-blackout
- name: BlackoutSlate
  property_count: 5
  slug: medialive-api-blackout-slate
- name: BlackoutSlateState
  property_count: 0
  slug: medialive-api-blackout-slate-state
- name: BurnInAlignment
  property_count: 0
  slug: medialive-api-burn-in-alignment
- name: BurnInBackgroundColor
  property_count: 0
  slug: medialive-api-burn-in-background-color
- name: BurnInDestinationSettings
  property_count: 17
  slug: medialive-api-burn-in-destination-settings
- name: BurnInFontColor
  property_count: 0
  slug: medialive-api-burn-in-font-color
- name: BurnInOutlineColor
  property_count: 0
  slug: medialive-api-burn-in-outline-color
- name: BurnInShadowColor
  property_count: 0
  slug: medialive-api-burn-in-shadow-color
- name: BurnInTeletextGridControl
  property_count: 0
  slug: medialive-api-burn-in-teletext-grid-control
- name: CancelInputDeviceTransferRequest
  property_count: 0
  slug: medialive-api-cancel-input-device-transfer-request
- name: CancelInputDeviceTransferResponse
  property_count: 0
  slug: medialive-api-cancel-input-device-transfer-response
- name: CaptionDescription
  property_count: 6
  slug: medialive-api-caption-description
- name: CaptionDestinationSettings
  property_count: 13
  slug: medialive-api-caption-destination-settings
- name: CaptionLanguageMapping
  property_count: 3
  slug: medialive-api-caption-language-mapping
- name: CaptionRectangle
  property_count: 4
  slug: medialive-api-caption-rectangle
- name: CaptionSelector
  property_count: 3
  slug: medialive-api-caption-selector
- name: CaptionSelectorSettings
  property_count: 7
  slug: medialive-api-caption-selector-settings
- name: CdiInputResolution
  property_count: 0
  slug: medialive-api-cdi-input-resolution
- name: CdiInputSpecification
  property_count: 1
  slug: medialive-api-cdi-input-specification
- name: ChannelClass
  property_count: 0
  slug: medialive-api-channel-class
- name: ChannelEgressEndpoint
  property_count: 1
  slug: medialive-api-channel-egress-endpoint
- name: Channel
  property_count: 18
  slug: medialive-api-channel
- name: ChannelState
  property_count: 0
  slug: medialive-api-channel-state
- name: ChannelSummary
  property_count: 16
  slug: medialive-api-channel-summary
- name: ClaimDeviceRequest
  property_count: 1
  slug: medialive-api-claim-device-request
- name: ClaimDeviceResponse
  property_count: 0
  slug: medialive-api-claim-device-response
- name: ColorSpacePassthroughSettings
  property_count: 0
  slug: medialive-api-color-space-passthrough-settings
- name: ContentType
  property_count: 0
  slug: medialive-api-content-type
- name: CreateChannelRequest
  property_count: 14
  slug: medialive-api-create-channel-request
- name: CreateChannelResponse
  property_count: 1
  slug: medialive-api-create-channel-response
- name: CreateInputRequest
  property_count: 11
  slug: medialive-api-create-input-request
- name: CreateInputResponse
  property_count: 1
  slug: medialive-api-create-input-response
- name: CreateInputSecurityGroupRequest
  property_count: 2
  slug: medialive-api-create-input-security-group-request
- name: CreateInputSecurityGroupResponse
  property_count: 1
  slug: medialive-api-create-input-security-group-response
- name: CreateMultiplexProgramRequest
  property_count: 3
  slug: medialive-api-create-multiplex-program-request
- name: CreateMultiplexProgramResponse
  property_count: 1
  slug: medialive-api-create-multiplex-program-response
- name: CreateMultiplexRequest
  property_count: 5
  slug: medialive-api-create-multiplex-request
- name: CreateMultiplexResponse
  property_count: 1
  slug: medialive-api-create-multiplex-response
- name: CreatePartnerInputRequest
  property_count: 2
  slug: medialive-api-create-partner-input-request
- name: CreatePartnerInputResponse
  property_count: 1
  slug: medialive-api-create-partner-input-response
- name: CreateTagsRequest
  property_count: 1
  slug: medialive-api-create-tags-request
- name: DeleteChannelRequest
  property_count: 0
  slug: medialive-api-delete-channel-request
- name: DeleteChannelResponse
  property_count: 18
  slug: medialive-api-delete-channel-response
- name: DeleteInputRequest
  property_count: 0
  slug: medialive-api-delete-input-request
- name: DeleteInputResponse
  property_count: 0
  slug: medialive-api-delete-input-response
- name: DeleteInputSecurityGroupRequest
  property_count: 0
  slug: medialive-api-delete-input-security-group-request
- name: DeleteInputSecurityGroupResponse
  property_count: 0
  slug: medialive-api-delete-input-security-group-response
- name: DeleteMultiplexProgramRequest
  property_count: 0
  slug: medialive-api-delete-multiplex-program-request
- name: DeleteMultiplexProgramResponse
  property_count: 5
  slug: medialive-api-delete-multiplex-program-response
- name: DeleteMultiplexRequest
  property_count: 0
  slug: medialive-api-delete-multiplex-request
- name: DeleteMultiplexResponse
  property_count: 10
  slug: medialive-api-delete-multiplex-response
- name: DeleteReservationRequest
  property_count: 0
  slug: medialive-api-delete-reservation-request
- name: DeleteReservationResponse
  property_count: 19
  slug: medialive-api-delete-reservation-response
- name: DeleteScheduleRequest
  property_count: 0
  slug: medialive-api-delete-schedule-request
- name: DeleteScheduleResponse
  property_count: 0
  slug: medialive-api-delete-schedule-response
- name: DeleteTagsRequest
  property_count: 0
  slug: medialive-api-delete-tags-request
- name: DescribeChannelRequest
  property_count: 0
  slug: medialive-api-describe-channel-request
- name: DescribeChannelResponse
  property_count: 18
  slug: medialive-api-describe-channel-response
- name: DescribeInputDeviceRequest
  property_count: 0
  slug: medialive-api-describe-input-device-request
- name: DescribeInputDeviceResponse
  property_count: 13
  slug: medialive-api-describe-input-device-response
- name: DescribeInputDeviceThumbnailRequest
  property_count: 0
  slug: medialive-api-describe-input-device-thumbnail-request
- name: DescribeInputDeviceThumbnailResponse
  property_count: 1
  slug: medialive-api-describe-input-device-thumbnail-response
- name: DescribeInputRequest
  property_count: 0
  slug: medialive-api-describe-input-request
- name: DescribeInputResponse
  property_count: 16
  slug: medialive-api-describe-input-response
- name: DescribeInputSecurityGroupRequest
  property_count: 0
  slug: medialive-api-describe-input-security-group-request
- name: DescribeInputSecurityGroupResponse
  property_count: 6
  slug: medialive-api-describe-input-security-group-response
- name: DescribeMultiplexProgramRequest
  property_count: 0
  slug: medialive-api-describe-multiplex-program-request
- name: DescribeMultiplexProgramResponse
  property_count: 5
  slug: medialive-api-describe-multiplex-program-response
- name: DescribeMultiplexRequest
  property_count: 0
  slug: medialive-api-describe-multiplex-request
- name: DescribeMultiplexResponse
  property_count: 10
  slug: medialive-api-describe-multiplex-response
- name: DescribeOfferingRequest
  property_count: 0
  slug: medialive-api-describe-offering-request
- name: DescribeOfferingResponse
  property_count: 11
  slug: medialive-api-describe-offering-response
- name: DescribeReservationRequest
  property_count: 0
  slug: medialive-api-describe-reservation-request
- name: DescribeReservationResponse
  property_count: 19
  slug: medialive-api-describe-reservation-response
- name: DescribeScheduleRequest
  property_count: 0
  slug: medialive-api-describe-schedule-request
- name: DescribeScheduleResponse
  property_count: 2
  slug: medialive-api-describe-schedule-response
- name: DeviceSettingsSyncState
  property_count: 0
  slug: medialive-api-device-settings-sync-state
- name: DeviceUpdateStatus
  property_count: 0
  slug: medialive-api-device-update-status
- name: DolbyEProgramSelection
  property_count: 0
  slug: medialive-api-dolby-e-program-selection
- name: DolbyVision81Settings
  property_count: 0
  slug: medialive-api-dolby-vision81-settings
- name: DvbNitSettings
  property_count: 3
  slug: medialive-api-dvb-nit-settings
- name: DvbSdtOutputSdt
  property_count: 0
  slug: medialive-api-dvb-sdt-output-sdt
- name: DvbSdtSettings
  property_count: 4
  slug: medialive-api-dvb-sdt-settings
- name: DvbSubDestinationAlignment
  property_count: 0
  slug: medialive-api-dvb-sub-destination-alignment
- name: DvbSubDestinationBackgroundColor
  property_count: 0
  slug: medialive-api-dvb-sub-destination-background-color
- name: DvbSubDestinationFontColor
  property_count: 0
  slug: medialive-api-dvb-sub-destination-font-color
- name: DvbSubDestinationOutlineColor
  property_count: 0
  slug: medialive-api-dvb-sub-destination-outline-color
- name: DvbSubDestinationSettings
  property_count: 17
  slug: medialive-api-dvb-sub-destination-settings
- name: DvbSubDestinationShadowColor
  property_count: 0
  slug: medialive-api-dvb-sub-destination-shadow-color
- name: DvbSubDestinationTeletextGridControl
  property_count: 0
  slug: medialive-api-dvb-sub-destination-teletext-grid-control
- name: DvbSubOcrLanguage
  property_count: 0
  slug: medialive-api-dvb-sub-ocr-language
- name: DvbSubSourceSettings
  property_count: 2
  slug: medialive-api-dvb-sub-source-settings
- name: DvbTdtSettings
  property_count: 1
  slug: medialive-api-dvb-tdt-settings
- name: Eac3AtmosCodingMode
  property_count: 0
  slug: medialive-api-eac3-atmos-coding-mode
- name: Eac3AtmosDrcLine
  property_count: 0
  slug: medialive-api-eac3-atmos-drc-line
- name: Eac3AtmosDrcRf
  property_count: 0
  slug: medialive-api-eac3-atmos-drc-rf
- name: Eac3AtmosSettings
  property_count: 7
  slug: medialive-api-eac3-atmos-settings
- name: Eac3AttenuationControl
  property_count: 0
  slug: medialive-api-eac3-attenuation-control
- name: Eac3BitstreamMode
  property_count: 0
  slug: medialive-api-eac3-bitstream-mode
- name: Eac3CodingMode
  property_count: 0
  slug: medialive-api-eac3-coding-mode
- name: Eac3DcFilter
  property_count: 0
  slug: medialive-api-eac3-dc-filter
- name: Eac3DrcLine
  property_count: 0
  slug: medialive-api-eac3-drc-line
- name: Eac3DrcRf
  property_count: 0
  slug: medialive-api-eac3-drc-rf
- name: Eac3LfeControl
  property_count: 0
  slug: medialive-api-eac3-lfe-control
- name: Eac3LfeFilter
  property_count: 0
  slug: medialive-api-eac3-lfe-filter
- name: Eac3MetadataControl
  property_count: 0
  slug: medialive-api-eac3-metadata-control
- name: Eac3PassthroughControl
  property_count: 0
  slug: medialive-api-eac3-passthrough-control
- name: Eac3PhaseControl
  property_count: 0
  slug: medialive-api-eac3-phase-control
- name: Eac3Settings
  property_count: 20
  slug: medialive-api-eac3-settings
- name: Eac3StereoDownmix
  property_count: 0
  slug: medialive-api-eac3-stereo-downmix
- name: Eac3SurroundExMode
  property_count: 0
  slug: medialive-api-eac3-surround-ex-mode
- name: Eac3SurroundMode
  property_count: 0
  slug: medialive-api-eac3-surround-mode
- name: EbuTtDDestinationSettings
  property_count: 4
  slug: medialive-api-ebu-tt-d-destination-settings
- name: EbuTtDDestinationStyleControl
  property_count: 0
  slug: medialive-api-ebu-tt-d-destination-style-control
- name: EbuTtDFillLineGapControl
  property_count: 0
  slug: medialive-api-ebu-tt-d-fill-line-gap-control
- name: EmbeddedConvert608To708
  property_count: 0
  slug: medialive-api-embedded-convert608-to708
- name: EmbeddedDestinationSettings
  property_count: 0
  slug: medialive-api-embedded-destination-settings
- name: EmbeddedPlusScte20DestinationSettings
  property_count: 0
  slug: medialive-api-embedded-plus-scte20-destination-settings
- name: EmbeddedScte20Detection
  property_count: 0
  slug: medialive-api-embedded-scte20-detection
- name: EmbeddedSourceSettings
  property_count: 4
  slug: medialive-api-embedded-source-settings
- name: EncoderSettings
  property_count: 12
  slug: medialive-api-encoder-settings
- name: Esam
  property_count: 6
  slug: medialive-api-esam
- name: FailoverCondition
  property_count: 1
  slug: medialive-api-failover-condition
- name: FailoverConditionSettings
  property_count: 3
  slug: medialive-api-failover-condition-settings
- name: FeatureActivationsInputPrepareScheduleActions
  property_count: 0
  slug: medialive-api-feature-activations-input-prepare-schedule-actions
- name: FeatureActivations
  property_count: 1
  slug: medialive-api-feature-activations
- name: FecOutputIncludeFec
  property_count: 0
  slug: medialive-api-fec-output-include-fec
- name: FecOutputSettings
  property_count: 3
  slug: medialive-api-fec-output-settings
- name: FixedAfd
  property_count: 0
  slug: medialive-api-fixed-afd
- name: FixedModeScheduleActionStartSettings
  property_count: 1
  slug: medialive-api-fixed-mode-schedule-action-start-settings
- name: Fmp4HlsSettings
  property_count: 3
  slug: medialive-api-fmp4-hls-settings
- name: Fmp4NielsenId3Behavior
  property_count: 0
  slug: medialive-api-fmp4-nielsen-id3-behavior
- name: Fmp4TimedMetadataBehavior
  property_count: 0
  slug: medialive-api-fmp4-timed-metadata-behavior
- name: FollowModeScheduleActionStartSettings
  property_count: 2
  slug: medialive-api-follow-mode-schedule-action-start-settings
- name: FollowPoint
  property_count: 0
  slug: medialive-api-follow-point
- name: FrameCaptureCdnSettings
  property_count: 1
  slug: medialive-api-frame-capture-cdn-settings
- name: FrameCaptureGroupSettings
  property_count: 2
  slug: medialive-api-frame-capture-group-settings
- name: FrameCaptureHlsSettings
  property_count: 0
  slug: medialive-api-frame-capture-hls-settings
- name: FrameCaptureIntervalUnit
  property_count: 0
  slug: medialive-api-frame-capture-interval-unit
- name: FrameCaptureOutputSettings
  property_count: 1
  slug: medialive-api-frame-capture-output-settings
- name: FrameCaptureS3Settings
  property_count: 1
  slug: medialive-api-frame-capture-s3-settings
- name: FrameCaptureSettings
  property_count: 3
  slug: medialive-api-frame-capture-settings
- name: GatewayTimeoutException
  property_count: 0
  slug: medialive-api-gateway-timeout-exception
- name: GlobalConfigurationInputEndAction
  property_count: 0
  slug: medialive-api-global-configuration-input-end-action
- name: GlobalConfigurationLowFramerateInputs
  property_count: 0
  slug: medialive-api-global-configuration-low-framerate-inputs
- name: GlobalConfigurationOutputLockingMode
  property_count: 0
  slug: medialive-api-global-configuration-output-locking-mode
- name: GlobalConfigurationOutputTimingSource
  property_count: 0
  slug: medialive-api-global-configuration-output-timing-source
- name: GlobalConfiguration
  property_count: 6
  slug: medialive-api-global-configuration
- name: H264AdaptiveQuantization
  property_count: 0
  slug: medialive-api-h264-adaptive-quantization
- name: H264ColorMetadata
  property_count: 0
  slug: medialive-api-h264-color-metadata
- name: H264ColorSpaceSettings
  property_count: 3
  slug: medialive-api-h264-color-space-settings
- name: H264EntropyEncoding
  property_count: 0
  slug: medialive-api-h264-entropy-encoding
- name: H264FilterSettings
  property_count: 1
  slug: medialive-api-h264-filter-settings
- name: H264FlickerAq
  property_count: 0
  slug: medialive-api-h264-flicker-aq
- name: H264ForceFieldPictures
  property_count: 0
  slug: medialive-api-h264-force-field-pictures
- name: H264FramerateControl
  property_count: 0
  slug: medialive-api-h264-framerate-control
- name: H264GopBReference
  property_count: 0
  slug: medialive-api-h264-gop-b-reference
- name: H264GopSizeUnits
  property_count: 0
  slug: medialive-api-h264-gop-size-units
- name: H264Level
  property_count: 0
  slug: medialive-api-h264-level
- name: H264LookAheadRateControl
  property_count: 0
  slug: medialive-api-h264-look-ahead-rate-control
- name: H264ParControl
  property_count: 0
  slug: medialive-api-h264-par-control
- name: H264Profile
  property_count: 0
  slug: medialive-api-h264-profile
- name: H264QualityLevel
  property_count: 0
  slug: medialive-api-h264-quality-level
- name: H264RateControlMode
  property_count: 0
  slug: medialive-api-h264-rate-control-mode
- name: H264ScanType
  property_count: 0
  slug: medialive-api-h264-scan-type
- name: H264SceneChangeDetect
  property_count: 0
  slug: medialive-api-h264-scene-change-detect
- name: H264Settings
  property_count: 42
  slug: medialive-api-h264-settings
- name: H264SpatialAq
  property_count: 0
  slug: medialive-api-h264-spatial-aq
- name: H264SubGopLength
  property_count: 0
  slug: medialive-api-h264-sub-gop-length
- name: H264Syntax
  property_count: 0
  slug: medialive-api-h264-syntax
- name: H264TemporalAq
  property_count: 0
  slug: medialive-api-h264-temporal-aq
- name: H264TimecodeInsertionBehavior
  property_count: 0
  slug: medialive-api-h264-timecode-insertion-behavior
- name: H265AdaptiveQuantization
  property_count: 0
  slug: medialive-api-h265-adaptive-quantization
- name: H265AlternativeTransferFunction
  property_count: 0
  slug: medialive-api-h265-alternative-transfer-function
- name: H265ColorMetadata
  property_count: 0
  slug: medialive-api-h265-color-metadata
- name: H265ColorSpaceSettings
  property_count: 5
  slug: medialive-api-h265-color-space-settings
- name: H265FilterSettings
  property_count: 1
  slug: medialive-api-h265-filter-settings
- name: H265FlickerAq
  property_count: 0
  slug: medialive-api-h265-flicker-aq
- name: H265GopSizeUnits
  property_count: 0
  slug: medialive-api-h265-gop-size-units
- name: H265Level
  property_count: 0
  slug: medialive-api-h265-level
- name: H265LookAheadRateControl
  property_count: 0
  slug: medialive-api-h265-look-ahead-rate-control
- name: H265Profile
  property_count: 0
  slug: medialive-api-h265-profile
- name: H265RateControlMode
  property_count: 0
  slug: medialive-api-h265-rate-control-mode
- name: H265ScanType
  property_count: 0
  slug: medialive-api-h265-scan-type
- name: H265SceneChangeDetect
  property_count: 0
  slug: medialive-api-h265-scene-change-detect
- name: H265Settings
  property_count: 30
  slug: medialive-api-h265-settings
- name: H265Tier
  property_count: 0
  slug: medialive-api-h265-tier
- name: H265TimecodeInsertionBehavior
  property_count: 0
  slug: medialive-api-h265-timecode-insertion-behavior
- name: Hdr10Settings
  property_count: 2
  slug: medialive-api-hdr10-settings
- name: HlsAdMarkers
  property_count: 0
  slug: medialive-api-hls-ad-markers
- name: HlsAkamaiHttpTransferMode
  property_count: 0
  slug: medialive-api-hls-akamai-http-transfer-mode
- name: HlsAkamaiSettings
  property_count: 7
  slug: medialive-api-hls-akamai-settings
- name: HlsBasicPutSettings
  property_count: 4
  slug: medialive-api-hls-basic-put-settings
- name: HlsCaptionLanguageSetting
  property_count: 0
  slug: medialive-api-hls-caption-language-setting
- name: HlsCdnSettings
  property_count: 5
  slug: medialive-api-hls-cdn-settings
- name: HlsClientCache
  property_count: 0
  slug: medialive-api-hls-client-cache
- name: HlsCodecSpecification
  property_count: 0
  slug: medialive-api-hls-codec-specification
- name: HlsDirectoryStructure
  property_count: 0
  slug: medialive-api-hls-directory-structure
- name: HlsDiscontinuityTags
  property_count: 0
  slug: medialive-api-hls-discontinuity-tags
- name: HlsEncryptionType
  property_count: 0
  slug: medialive-api-hls-encryption-type
- name: HlsGroupSettings
  property_count: 43
  slug: medialive-api-hls-group-settings
- name: HlsH265PackagingType
  property_count: 0
  slug: medialive-api-hls-h265-packaging-type
- name: HlsId3SegmentTaggingScheduleActionSettings
  property_count: 2
  slug: medialive-api-hls-id3-segment-tagging-schedule-action-settings
- name: HlsId3SegmentTaggingState
  property_count: 0
  slug: medialive-api-hls-id3-segment-tagging-state
- name: HlsIncompleteSegmentBehavior
  property_count: 0
  slug: medialive-api-hls-incomplete-segment-behavior
- name: HlsInputSettings
  property_count: 5
  slug: medialive-api-hls-input-settings
- name: HlsIvInManifest
  property_count: 0
  slug: medialive-api-hls-iv-in-manifest
- name: HlsIvSource
  property_count: 0
  slug: medialive-api-hls-iv-source
- name: HlsManifestCompression
  property_count: 0
  slug: medialive-api-hls-manifest-compression
- name: HlsManifestDurationFormat
  property_count: 0
  slug: medialive-api-hls-manifest-duration-format
- name: HlsMediaStoreSettings
  property_count: 5
  slug: medialive-api-hls-media-store-settings
- name: HlsMediaStoreStorageClass
  property_count: 0
  slug: medialive-api-hls-media-store-storage-class
- name: HlsMode
  property_count: 0
  slug: medialive-api-hls-mode
- name: HlsOutputSelection
  property_count: 0
  slug: medialive-api-hls-output-selection
- name: HlsOutputSettings
  property_count: 4
  slug: medialive-api-hls-output-settings
- name: HlsProgramDateTimeClock
  property_count: 0
  slug: medialive-api-hls-program-date-time-clock
- name: HlsProgramDateTime
  property_count: 0
  slug: medialive-api-hls-program-date-time
- name: HlsRedundantManifest
  property_count: 0
  slug: medialive-api-hls-redundant-manifest
- name: HlsS3Settings
  property_count: 1
  slug: medialive-api-hls-s3-settings
- name: HlsScte35SourceType
  property_count: 0
  slug: medialive-api-hls-scte35-source-type
- name: HlsSegmentationMode
  property_count: 0
  slug: medialive-api-hls-segmentation-mode
- name: HlsSettings
  property_count: 4
  slug: medialive-api-hls-settings
- name: HlsStreamInfResolution
  property_count: 0
  slug: medialive-api-hls-stream-inf-resolution
- name: HlsTimedMetadataId3Frame
  property_count: 0
  slug: medialive-api-hls-timed-metadata-id3-frame
- name: HlsTimedMetadataScheduleActionSettings
  property_count: 1
  slug: medialive-api-hls-timed-metadata-schedule-action-settings
- name: HlsTsFileMode
  property_count: 0
  slug: medialive-api-hls-ts-file-mode
- name: HlsWebdavHttpTransferMode
  property_count: 0
  slug: medialive-api-hls-webdav-http-transfer-mode
- name: HlsWebdavSettings
  property_count: 5
  slug: medialive-api-hls-webdav-settings
- name: HtmlMotionGraphicsSettings
  property_count: 0
  slug: medialive-api-html-motion-graphics-settings
- name: IFrameOnlyPlaylistType
  property_count: 0
  slug: medialive-api-i-frame-only-playlist-type
- name: ImmediateModeScheduleActionStartSettings
  property_count: 0
  slug: medialive-api-immediate-mode-schedule-action-start-settings
- name: InputAttachment
  property_count: 4
  slug: medialive-api-input-attachment
- name: InputChannelLevel
  property_count: 2
  slug: medialive-api-input-channel-level
- name: InputClass
  property_count: 0
  slug: medialive-api-input-class
- name: InputClippingSettings
  property_count: 3
  slug: medialive-api-input-clipping-settings
- name: InputCodec
  property_count: 0
  slug: medialive-api-input-codec
- name: InputDeblockFilter
  property_count: 0
  slug: medialive-api-input-deblock-filter
- name: InputDenoiseFilter
  property_count: 0
  slug: medialive-api-input-denoise-filter
- name: InputDestinationRequest
  property_count: 1
  slug: medialive-api-input-destination-request
- name: InputDestination
  property_count: 4
  slug: medialive-api-input-destination
- name: InputDestinationVpc
  property_count: 2
  slug: medialive-api-input-destination-vpc
- name: InputDeviceActiveInput
  property_count: 0
  slug: medialive-api-input-device-active-input
- name: InputDeviceConfigurableSettings
  property_count: 3
  slug: medialive-api-input-device-configurable-settings
- name: InputDeviceConfiguredInput
  property_count: 0
  slug: medialive-api-input-device-configured-input
- name: InputDeviceConnectionState
  property_count: 0
  slug: medialive-api-input-device-connection-state
- name: InputDeviceHdSettings
  property_count: 9
  slug: medialive-api-input-device-hd-settings
- name: InputDeviceIpScheme
  property_count: 0
  slug: medialive-api-input-device-ip-scheme
- name: InputDeviceNetworkSettings
  property_count: 5
  slug: medialive-api-input-device-network-settings
- name: InputDeviceRequest
  property_count: 1
  slug: medialive-api-input-device-request
- name: InputDeviceScanType
  property_count: 0
  slug: medialive-api-input-device-scan-type
- name: InputDeviceSettings
  property_count: 1
  slug: medialive-api-input-device-settings
- name: InputDeviceState
  property_count: 0
  slug: medialive-api-input-device-state
- name: InputDeviceSummary
  property_count: 13
  slug: medialive-api-input-device-summary
- name: InputDeviceThumbnail
  property_count: 0
  slug: medialive-api-input-device-thumbnail
- name: InputDeviceTransferType
  property_count: 0
  slug: medialive-api-input-device-transfer-type
- name: InputDeviceType
  property_count: 0
  slug: medialive-api-input-device-type
- name: InputDeviceUhdSettings
  property_count: 9
  slug: medialive-api-input-device-uhd-settings
- name: InputFilter
  property_count: 0
  slug: medialive-api-input-filter
- name: InputLocation
  property_count: 3
  slug: medialive-api-input-location
- name: InputLossActionForHlsOut
  property_count: 0
  slug: medialive-api-input-loss-action-for-hls-out
- name: InputLossActionForMsSmoothOut
  property_count: 0
  slug: medialive-api-input-loss-action-for-ms-smooth-out
- name: InputLossActionForRtmpOut
  property_count: 0
  slug: medialive-api-input-loss-action-for-rtmp-out
- name: InputLossActionForUdpOut
  property_count: 0
  slug: medialive-api-input-loss-action-for-udp-out
- name: InputLossBehavior
  property_count: 5
  slug: medialive-api-input-loss-behavior
- name: InputLossFailoverSettings
  property_count: 1
  slug: medialive-api-input-loss-failover-settings
- name: InputLossImageType
  property_count: 0
  slug: medialive-api-input-loss-image-type
- name: InputMaximumBitrate
  property_count: 0
  slug: medialive-api-input-maximum-bitrate
- name: InputPreference
  property_count: 0
  slug: medialive-api-input-preference
- name: InputPrepareScheduleActionSettings
  property_count: 3
  slug: medialive-api-input-prepare-schedule-action-settings
- name: InputResolution
  property_count: 0
  slug: medialive-api-input-resolution
- name: Input
  property_count: 16
  slug: medialive-api-input
- name: InputSecurityGroup
  property_count: 6
  slug: medialive-api-input-security-group
- name: InputSecurityGroupState
  property_count: 0
  slug: medialive-api-input-security-group-state
- name: InputSettings
  property_count: 11
  slug: medialive-api-input-settings
- name: InputSourceEndBehavior
  property_count: 0
  slug: medialive-api-input-source-end-behavior
- name: InputSourceRequest
  property_count: 3
  slug: medialive-api-input-source-request
- name: InputSource
  property_count: 3
  slug: medialive-api-input-source
- name: InputSourceType
  property_count: 0
  slug: medialive-api-input-source-type
- name: InputSpecification
  property_count: 3
  slug: medialive-api-input-specification
- name: InputState
  property_count: 0
  slug: medialive-api-input-state
- name: InputSwitchScheduleActionSettings
  property_count: 3
  slug: medialive-api-input-switch-schedule-action-settings
- name: InputTimecodeSource
  property_count: 0
  slug: medialive-api-input-timecode-source
- name: InputType
  property_count: 0
  slug: medialive-api-input-type
- name: InputVpcRequest
  property_count: 2
  slug: medialive-api-input-vpc-request
- name: InputWhitelistRuleCidr
  property_count: 1
  slug: medialive-api-input-whitelist-rule-cidr
- name: InputWhitelistRule
  property_count: 1
  slug: medialive-api-input-whitelist-rule
- name: KeyProviderSettings
  property_count: 1
  slug: medialive-api-key-provider-settings
- name: LastFrameClippingBehavior
  property_count: 0
  slug: medialive-api-last-frame-clipping-behavior
- name: ListChannelsRequest
  property_count: 0
  slug: medialive-api-list-channels-request
- name: ListChannelsResponse
  property_count: 2
  slug: medialive-api-list-channels-response
- name: ListInputDeviceTransfersRequest
  property_count: 0
  slug: medialive-api-list-input-device-transfers-request
- name: ListInputDeviceTransfersResponse
  property_count: 2
  slug: medialive-api-list-input-device-transfers-response
- name: ListInputDevicesRequest
  property_count: 0
  slug: medialive-api-list-input-devices-request
- name: ListInputDevicesResponse
  property_count: 2
  slug: medialive-api-list-input-devices-response
- name: ListInputSecurityGroupsRequest
  property_count: 0
  slug: medialive-api-list-input-security-groups-request
- name: ListInputSecurityGroupsResponse
  property_count: 2
  slug: medialive-api-list-input-security-groups-response
- name: ListInputsRequest
  property_count: 0
  slug: medialive-api-list-inputs-request
- name: ListInputsResponse
  property_count: 2
  slug: medialive-api-list-inputs-response
- name: ListMultiplexProgramsRequest
  property_count: 0
  slug: medialive-api-list-multiplex-programs-request
- name: ListMultiplexProgramsResponse
  property_count: 2
  slug: medialive-api-list-multiplex-programs-response
- name: ListMultiplexesRequest
  property_count: 0
  slug: medialive-api-list-multiplexes-request
- name: ListMultiplexesResponse
  property_count: 2
  slug: medialive-api-list-multiplexes-response
- name: ListOfferingsRequest
  property_count: 0
  slug: medialive-api-list-offerings-request
- name: ListOfferingsResponse
  property_count: 2
  slug: medialive-api-list-offerings-response
- name: ListReservationsRequest
  property_count: 0
  slug: medialive-api-list-reservations-request
- name: ListReservationsResponse
  property_count: 2
  slug: medialive-api-list-reservations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: medialive-api-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: medialive-api-list-tags-for-resource-response
- name: LogLevel
  property_count: 0
  slug: medialive-api-log-level
- name: M2tsAbsentInputAudioBehavior
  property_count: 0
  slug: medialive-api-m2ts-absent-input-audio-behavior
- name: M2tsAribCaptionsPidControl
  property_count: 0
  slug: medialive-api-m2ts-arib-captions-pid-control
- name: M2tsArib
  property_count: 0
  slug: medialive-api-m2ts-arib
- name: M2tsAudioBufferModel
  property_count: 0
  slug: medialive-api-m2ts-audio-buffer-model
- name: M2tsAudioInterval
  property_count: 0
  slug: medialive-api-m2ts-audio-interval
- name: M2tsAudioStreamType
  property_count: 0
  slug: medialive-api-m2ts-audio-stream-type
- name: M2tsBufferModel
  property_count: 0
  slug: medialive-api-m2ts-buffer-model
- name: M2tsCcDescriptor
  property_count: 0
  slug: medialive-api-m2ts-cc-descriptor
- name: M2tsEbifControl
  property_count: 0
  slug: medialive-api-m2ts-ebif-control
- name: M2tsEbpPlacement
  property_count: 0
  slug: medialive-api-m2ts-ebp-placement
- name: M2tsEsRateInPes
  property_count: 0
  slug: medialive-api-m2ts-es-rate-in-pes
- name: M2tsKlv
  property_count: 0
  slug: medialive-api-m2ts-klv
- name: M2tsNielsenId3Behavior
  property_count: 0
  slug: medialive-api-m2ts-nielsen-id3-behavior
- name: M2tsPcrControl
  property_count: 0
  slug: medialive-api-m2ts-pcr-control
- name: M2tsRateMode
  property_count: 0
  slug: medialive-api-m2ts-rate-mode
- name: M2tsScte35Control
  property_count: 0
  slug: medialive-api-m2ts-scte35-control
- name: M2tsSegmentationMarkers
  property_count: 0
  slug: medialive-api-m2ts-segmentation-markers
- name: M2tsSegmentationStyle
  property_count: 0
  slug: medialive-api-m2ts-segmentation-style
- name: M2tsSettings
  property_count: 48
  slug: medialive-api-m2ts-settings
- name: M2tsTimedMetadataBehavior
  property_count: 0
  slug: medialive-api-m2ts-timed-metadata-behavior
- name: M3u8NielsenId3Behavior
  property_count: 0
  slug: medialive-api-m3u8-nielsen-id3-behavior
- name: M3u8PcrControl
  property_count: 0
  slug: medialive-api-m3u8-pcr-control
- name: M3u8Scte35Behavior
  property_count: 0
  slug: medialive-api-m3u8-scte35-behavior
- name: M3u8Settings
  property_count: 17
  slug: medialive-api-m3u8-settings
- name: M3u8TimedMetadataBehavior
  property_count: 0
  slug: medialive-api-m3u8-timed-metadata-behavior
- name: MaintenanceCreateSettings
  property_count: 2
  slug: medialive-api-maintenance-create-settings
- name: MaintenanceDay
  property_count: 0
  slug: medialive-api-maintenance-day
- name: MaintenanceStatus
  property_count: 4
  slug: medialive-api-maintenance-status
- name: MaintenanceUpdateSettings
  property_count: 3
  slug: medialive-api-maintenance-update-settings
- name: MaxResults
  property_count: 0
  slug: medialive-api-max-results
- name: MediaConnectFlowRequest
  property_count: 1
  slug: medialive-api-media-connect-flow-request
- name: MediaConnectFlow
  property_count: 1
  slug: medialive-api-media-connect-flow
- name: MediaPackageGroupSettings
  property_count: 1
  slug: medialive-api-media-package-group-settings
- name: MediaPackageOutputDestinationSettings
  property_count: 1
  slug: medialive-api-media-package-output-destination-settings
- name: MediaPackageOutputSettings
  property_count: 0
  slug: medialive-api-media-package-output-settings
- name: MotionGraphicsActivateScheduleActionSettings
  property_count: 4
  slug: medialive-api-motion-graphics-activate-schedule-action-settings
- name: MotionGraphicsConfiguration
  property_count: 2
  slug: medialive-api-motion-graphics-configuration
- name: MotionGraphicsDeactivateScheduleActionSettings
  property_count: 0
  slug: medialive-api-motion-graphics-deactivate-schedule-action-settings
- name: MotionGraphicsInsertion
  property_count: 0
  slug: medialive-api-motion-graphics-insertion
- name: MotionGraphicsSettings
  property_count: 1
  slug: medialive-api-motion-graphics-settings
- name: Mp2CodingMode
  property_count: 0
  slug: medialive-api-mp2-coding-mode
- name: Mp2Settings
  property_count: 3
  slug: medialive-api-mp2-settings
- name: Mpeg2AdaptiveQuantization
  property_count: 0
  slug: medialive-api-mpeg2-adaptive-quantization
- name: Mpeg2ColorMetadata
  property_count: 0
  slug: medialive-api-mpeg2-color-metadata
- name: Mpeg2ColorSpace
  property_count: 0
  slug: medialive-api-mpeg2-color-space
- name: Mpeg2DisplayRatio
  property_count: 0
  slug: medialive-api-mpeg2-display-ratio
- name: Mpeg2FilterSettings
  property_count: 1
  slug: medialive-api-mpeg2-filter-settings
- name: Mpeg2GopSizeUnits
  property_count: 0
  slug: medialive-api-mpeg2-gop-size-units
- name: Mpeg2ScanType
  property_count: 0
  slug: medialive-api-mpeg2-scan-type
- name: Mpeg2Settings
  property_count: 17
  slug: medialive-api-mpeg2-settings
- name: Mpeg2SubGopLength
  property_count: 0
  slug: medialive-api-mpeg2-sub-gop-length
- name: Mpeg2TimecodeInsertionBehavior
  property_count: 0
  slug: medialive-api-mpeg2-timecode-insertion-behavior
- name: MsSmoothGroupSettings
  property_count: 19
  slug: medialive-api-ms-smooth-group-settings
- name: MsSmoothH265PackagingType
  property_count: 0
  slug: medialive-api-ms-smooth-h265-packaging-type
- name: MsSmoothOutputSettings
  property_count: 2
  slug: medialive-api-ms-smooth-output-settings
- name: MultiplexGroupSettings
  property_count: 0
  slug: medialive-api-multiplex-group-settings
- name: MultiplexMediaConnectOutputDestinationSettings
  property_count: 1
  slug: medialive-api-multiplex-media-connect-output-destination-settings
- name: MultiplexOutputDestination
  property_count: 1
  slug: medialive-api-multiplex-output-destination
- name: MultiplexOutputSettings
  property_count: 1
  slug: medialive-api-multiplex-output-settings
- name: MultiplexProgramChannelDestinationSettings
  property_count: 2
  slug: medialive-api-multiplex-program-channel-destination-settings
- name: MultiplexProgramPacketIdentifiersMap
  property_count: 13
  slug: medialive-api-multiplex-program-packet-identifiers-map
- name: MultiplexProgramPipelineDetail
  property_count: 2
  slug: medialive-api-multiplex-program-pipeline-detail
- name: MultiplexProgram
  property_count: 5
  slug: medialive-api-multiplex-program
- name: MultiplexProgramServiceDescriptor
  property_count: 2
  slug: medialive-api-multiplex-program-service-descriptor
- name: MultiplexProgramSettings
  property_count: 4
  slug: medialive-api-multiplex-program-settings
- name: MultiplexProgramSummary
  property_count: 2
  slug: medialive-api-multiplex-program-summary
- name: Multiplex
  property_count: 10
  slug: medialive-api-multiplex
- name: MultiplexSettings
  property_count: 4
  slug: medialive-api-multiplex-settings
- name: MultiplexSettingsSummary
  property_count: 1
  slug: medialive-api-multiplex-settings-summary
- name: MultiplexState
  property_count: 0
  slug: medialive-api-multiplex-state
- name: MultiplexStatmuxVideoSettings
  property_count: 3
  slug: medialive-api-multiplex-statmux-video-settings
- name: MultiplexSummary
  property_count: 9
  slug: medialive-api-multiplex-summary
- name: MultiplexVideoSettings
  property_count: 2
  slug: medialive-api-multiplex-video-settings
- name: NetworkInputServerValidation
  property_count: 0
  slug: medialive-api-network-input-server-validation
- name: NetworkInputSettings
  property_count: 2
  slug: medialive-api-network-input-settings
- name: NielsenCBET
  property_count: 3
  slug: medialive-api-nielsen-cbet
- name: NielsenConfiguration
  property_count: 2
  slug: medialive-api-nielsen-configuration
- name: NielsenNaesIiNw
  property_count: 3
  slug: medialive-api-nielsen-naes-ii-nw
- name: NielsenPcmToId3TaggingState
  property_count: 0
  slug: medialive-api-nielsen-pcm-to-id3-tagging-state
- name: NielsenWatermarkTimezones
  property_count: 0
  slug: medialive-api-nielsen-watermark-timezones
- name: NielsenWatermarksCbetStepaside
  property_count: 0
  slug: medialive-api-nielsen-watermarks-cbet-stepaside
- name: NielsenWatermarksDistributionTypes
  property_count: 0
  slug: medialive-api-nielsen-watermarks-distribution-types
- name: NielsenWatermarksSettings
  property_count: 3
  slug: medialive-api-nielsen-watermarks-settings
- name: OfferingDurationUnits
  property_count: 0
  slug: medialive-api-offering-duration-units
- name: Offering
  property_count: 11
  slug: medialive-api-offering
- name: OfferingType
  property_count: 0
  slug: medialive-api-offering-type
- name: OutputDestination
  property_count: 4
  slug: medialive-api-output-destination
- name: OutputDestinationSettings
  property_count: 4
  slug: medialive-api-output-destination-settings
- name: OutputGroup
  property_count: 3
  slug: medialive-api-output-group
- name: OutputGroupSettings
  property_count: 8
  slug: medialive-api-output-group-settings
- name: OutputLocationRef
  property_count: 1
  slug: medialive-api-output-location-ref
- name: Output
  property_count: 5
  slug: medialive-api-output
- name: OutputSettings
  property_count: 8
  slug: medialive-api-output-settings
- name: PassThroughSettings
  property_count: 0
  slug: medialive-api-pass-through-settings
- name: PauseStateScheduleActionSettings
  property_count: 1
  slug: medialive-api-pause-state-schedule-action-settings
- name: PipelineDetail
  property_count: 5
  slug: medialive-api-pipeline-detail
- name: PipelineId
  property_count: 0
  slug: medialive-api-pipeline-id
- name: PipelinePauseStateSettings
  property_count: 1
  slug: medialive-api-pipeline-pause-state-settings
- name: PreferredChannelPipeline
  property_count: 0
  slug: medialive-api-preferred-channel-pipeline
- name: PurchaseOfferingRequest
  property_count: 6
  slug: medialive-api-purchase-offering-request
- name: PurchaseOfferingResponse
  property_count: 1
  slug: medialive-api-purchase-offering-response
- name: RawSettings
  property_count: 0
  slug: medialive-api-raw-settings
- name: RebootInputDeviceForce
  property_count: 0
  slug: medialive-api-reboot-input-device-force
- name: RebootInputDeviceRequest
  property_count: 1
  slug: medialive-api-reboot-input-device-request
- name: RebootInputDeviceResponse
  property_count: 0
  slug: medialive-api-reboot-input-device-response
- name: Rec601Settings
  property_count: 0
  slug: medialive-api-rec601-settings
- name: Rec709Settings
  property_count: 0
  slug: medialive-api-rec709-settings
- name: RejectInputDeviceTransferRequest
  property_count: 0
  slug: medialive-api-reject-input-device-transfer-request
- name: RejectInputDeviceTransferResponse
  property_count: 0
  slug: medialive-api-reject-input-device-transfer-response
- name: RemixSettings
  property_count: 3
  slug: medialive-api-remix-settings
- name: RenewalSettings
  property_count: 2
  slug: medialive-api-renewal-settings
- name: ReservationAutomaticRenewal
  property_count: 0
  slug: medialive-api-reservation-automatic-renewal
- name: ReservationCodec
  property_count: 0
  slug: medialive-api-reservation-codec
- name: ReservationMaximumBitrate
  property_count: 0
  slug: medialive-api-reservation-maximum-bitrate
- name: ReservationMaximumFramerate
  property_count: 0
  slug: medialive-api-reservation-maximum-framerate
- name: ReservationResolution
  property_count: 0
  slug: medialive-api-reservation-resolution
- name: ReservationResourceSpecification
  property_count: 8
  slug: medialive-api-reservation-resource-specification
- name: ReservationResourceType
  property_count: 0
  slug: medialive-api-reservation-resource-type
- name: Reservation
  property_count: 19
  slug: medialive-api-reservation
- name: ReservationSpecialFeature
  property_count: 0
  slug: medialive-api-reservation-special-feature
- name: ReservationState
  property_count: 0
  slug: medialive-api-reservation-state
- name: ReservationVideoQuality
  property_count: 0
  slug: medialive-api-reservation-video-quality
- name: RtmpAdMarkers
  property_count: 0
  slug: medialive-api-rtmp-ad-markers
- name: RtmpCacheFullBehavior
  property_count: 0
  slug: medialive-api-rtmp-cache-full-behavior
- name: RtmpCaptionData
  property_count: 0
  slug: medialive-api-rtmp-caption-data
- name: RtmpCaptionInfoDestinationSettings
  property_count: 0
  slug: medialive-api-rtmp-caption-info-destination-settings
- name: RtmpGroupSettings
  property_count: 7
  slug: medialive-api-rtmp-group-settings
- name: RtmpOutputCertificateMode
  property_count: 0
  slug: medialive-api-rtmp-output-certificate-mode
- name: RtmpOutputSettings
  property_count: 4
  slug: medialive-api-rtmp-output-settings
- name: S3CannedAcl
  property_count: 0
  slug: medialive-api-s3-canned-acl
- name: ScheduleAction
  property_count: 3
  slug: medialive-api-schedule-action
- name: ScheduleActionSettings
  property_count: 13
  slug: medialive-api-schedule-action-settings
- name: ScheduleActionStartSettings
  property_count: 3
  slug: medialive-api-schedule-action-start-settings
- name: Scte20Convert608To708
  property_count: 0
  slug: medialive-api-scte20-convert608-to708
- name: Scte20PlusEmbeddedDestinationSettings
  property_count: 0
  slug: medialive-api-scte20-plus-embedded-destination-settings
- name: Scte20SourceSettings
  property_count: 2
  slug: medialive-api-scte20-source-settings
- name: Scte27DestinationSettings
  property_count: 0
  slug: medialive-api-scte27-destination-settings
- name: Scte27OcrLanguage
  property_count: 0
  slug: medialive-api-scte27-ocr-language
- name: Scte27SourceSettings
  property_count: 2
  slug: medialive-api-scte27-source-settings
- name: Scte35AposNoRegionalBlackoutBehavior
  property_count: 0
  slug: medialive-api-scte35-apos-no-regional-blackout-behavior
- name: Scte35AposWebDeliveryAllowedBehavior
  property_count: 0
  slug: medialive-api-scte35-apos-web-delivery-allowed-behavior
- name: Scte35ArchiveAllowedFlag
  property_count: 0
  slug: medialive-api-scte35-archive-allowed-flag
- name: Scte35DeliveryRestrictions
  property_count: 4
  slug: medialive-api-scte35-delivery-restrictions
- name: Scte35Descriptor
  property_count: 1
  slug: medialive-api-scte35-descriptor
- name: Scte35DescriptorSettings
  property_count: 1
  slug: medialive-api-scte35-descriptor-settings
- name: Scte35DeviceRestrictions
  property_count: 0
  slug: medialive-api-scte35-device-restrictions
- name: Scte35InputMode
  property_count: 0
  slug: medialive-api-scte35-input-mode
- name: Scte35InputScheduleActionSettings
  property_count: 2
  slug: medialive-api-scte35-input-schedule-action-settings
- name: Scte35NoRegionalBlackoutFlag
  property_count: 0
  slug: medialive-api-scte35-no-regional-blackout-flag
- name: Scte35ReturnToNetworkScheduleActionSettings
  property_count: 1
  slug: medialive-api-scte35-return-to-network-schedule-action-settings
- name: Scte35SegmentationCancelIndicator
  property_count: 0
  slug: medialive-api-scte35-segmentation-cancel-indicator
- name: Scte35SegmentationDescriptor
  property_count: 11
  slug: medialive-api-scte35-segmentation-descriptor
- name: Scte35SpliceInsertNoRegionalBlackoutBehavior
  property_count: 0
  slug: medialive-api-scte35-splice-insert-no-regional-blackout-behavior
- name: Scte35SpliceInsertScheduleActionSettings
  property_count: 2
  slug: medialive-api-scte35-splice-insert-schedule-action-settings
- name: Scte35SpliceInsert
  property_count: 3
  slug: medialive-api-scte35-splice-insert
- name: Scte35SpliceInsertWebDeliveryAllowedBehavior
  property_count: 0
  slug: medialive-api-scte35-splice-insert-web-delivery-allowed-behavior
- name: Scte35TimeSignalApos
  property_count: 3
  slug: medialive-api-scte35-time-signal-apos
- name: Scte35TimeSignalScheduleActionSettings
  property_count: 1
  slug: medialive-api-scte35-time-signal-schedule-action-settings
- name: Scte35WebDeliveryAllowedFlag
  property_count: 0
  slug: medialive-api-scte35-web-delivery-allowed-flag
- name: SmoothGroupAudioOnlyTimecodeControl
  property_count: 0
  slug: medialive-api-smooth-group-audio-only-timecode-control
- name: SmoothGroupCertificateMode
  property_count: 0
  slug: medialive-api-smooth-group-certificate-mode
- name: SmoothGroupEventIdMode
  property_count: 0
  slug: medialive-api-smooth-group-event-id-mode
- name: SmoothGroupEventStopBehavior
  property_count: 0
  slug: medialive-api-smooth-group-event-stop-behavior
- name: SmoothGroupSegmentationMode
  property_count: 0
  slug: medialive-api-smooth-group-segmentation-mode
- name: SmoothGroupSparseTrackType
  property_count: 0
  slug: medialive-api-smooth-group-sparse-track-type
- name: SmoothGroupStreamManifestBehavior
  property_count: 0
  slug: medialive-api-smooth-group-stream-manifest-behavior
- name: SmoothGroupTimestampOffsetMode
  property_count: 0
  slug: medialive-api-smooth-group-timestamp-offset-mode
- name: SmpteTtDestinationSettings
  property_count: 0
  slug: medialive-api-smpte-tt-destination-settings
- name: Smpte2038DataPreference
  property_count: 0
  slug: medialive-api-smpte2038-data-preference
- name: StandardHlsSettings
  property_count: 2
  slug: medialive-api-standard-hls-settings
- name: StartChannelRequest
  property_count: 0
  slug: medialive-api-start-channel-request
- name: StartChannelResponse
  property_count: 18
  slug: medialive-api-start-channel-response
- name: StartInputDeviceMaintenanceWindowRequest
  property_count: 0
  slug: medialive-api-start-input-device-maintenance-window-request
- name: StartInputDeviceMaintenanceWindowResponse
  property_count: 0
  slug: medialive-api-start-input-device-maintenance-window-response
- name: StartMultiplexRequest
  property_count: 0
  slug: medialive-api-start-multiplex-request
- name: StartMultiplexResponse
  property_count: 10
  slug: medialive-api-start-multiplex-response
- name: StartTimecode
  property_count: 1
  slug: medialive-api-start-timecode
- name: StaticImageActivateScheduleActionSettings
  property_count: 10
  slug: medialive-api-static-image-activate-schedule-action-settings
- name: StaticImageDeactivateScheduleActionSettings
  property_count: 2
  slug: medialive-api-static-image-deactivate-schedule-action-settings
- name: StaticKeySettings
  property_count: 2
  slug: medialive-api-static-key-settings
- name: StopChannelRequest
  property_count: 0
  slug: medialive-api-stop-channel-request
- name: StopChannelResponse
  property_count: 18
  slug: medialive-api-stop-channel-response
- name: StopMultiplexRequest
  property_count: 0
  slug: medialive-api-stop-multiplex-request
- name: StopMultiplexResponse
  property_count: 10
  slug: medialive-api-stop-multiplex-response
- name: StopTimecode
  property_count: 2
  slug: medialive-api-stop-timecode
- name: Tags
  property_count: 0
  slug: medialive-api-tags
- name: TeletextDestinationSettings
  property_count: 0
  slug: medialive-api-teletext-destination-settings
- name: TeletextSourceSettings
  property_count: 2
  slug: medialive-api-teletext-source-settings
- name: TemporalFilterPostFilterSharpening
  property_count: 0
  slug: medialive-api-temporal-filter-post-filter-sharpening
- name: TemporalFilterSettings
  property_count: 2
  slug: medialive-api-temporal-filter-settings
- name: TemporalFilterStrength
  property_count: 0
  slug: medialive-api-temporal-filter-strength
- name: TimecodeBurninFontSize
  property_count: 0
  slug: medialive-api-timecode-burnin-font-size
- name: TimecodeBurninPosition
  property_count: 0
  slug: medialive-api-timecode-burnin-position
- name: TimecodeBurninSettings
  property_count: 3
  slug: medialive-api-timecode-burnin-settings
- name: TimecodeConfig
  property_count: 2
  slug: medialive-api-timecode-config
- name: TimecodeConfigSource
  property_count: 0
  slug: medialive-api-timecode-config-source
- name: TransferInputDeviceRequest
  property_count: 3
  slug: medialive-api-transfer-input-device-request
- name: TransferInputDeviceResponse
  property_count: 0
  slug: medialive-api-transfer-input-device-response
- name: TransferringInputDeviceSummary
  property_count: 4
  slug: medialive-api-transferring-input-device-summary
- name: TtmlDestinationSettings
  property_count: 1
  slug: medialive-api-ttml-destination-settings
- name: TtmlDestinationStyleControl
  property_count: 0
  slug: medialive-api-ttml-destination-style-control
- name: UdpContainerSettings
  property_count: 1
  slug: medialive-api-udp-container-settings
- name: UdpGroupSettings
  property_count: 3
  slug: medialive-api-udp-group-settings
- name: UdpOutputSettings
  property_count: 4
  slug: medialive-api-udp-output-settings
- name: UdpTimedMetadataId3Frame
  property_count: 0
  slug: medialive-api-udp-timed-metadata-id3-frame
- name: UpdateChannelClassRequest
  property_count: 2
  slug: medialive-api-update-channel-class-request
- name: UpdateChannelClassResponse
  property_count: 1
  slug: medialive-api-update-channel-class-response
- name: UpdateChannelRequest
  property_count: 9
  slug: medialive-api-update-channel-request
- name: UpdateChannelResponse
  property_count: 1
  slug: medialive-api-update-channel-response
- name: UpdateInputDeviceRequest
  property_count: 3
  slug: medialive-api-update-input-device-request
- name: UpdateInputDeviceResponse
  property_count: 13
  slug: medialive-api-update-input-device-response
- name: UpdateInputRequest
  property_count: 7
  slug: medialive-api-update-input-request
- name: UpdateInputResponse
  property_count: 1
  slug: medialive-api-update-input-response
- name: UpdateInputSecurityGroupRequest
  property_count: 2
  slug: medialive-api-update-input-security-group-request
- name: UpdateInputSecurityGroupResponse
  property_count: 1
  slug: medialive-api-update-input-security-group-response
- name: UpdateMultiplexProgramRequest
  property_count: 1
  slug: medialive-api-update-multiplex-program-request
- name: UpdateMultiplexProgramResponse
  property_count: 1
  slug: medialive-api-update-multiplex-program-response
- name: UpdateMultiplexRequest
  property_count: 2
  slug: medialive-api-update-multiplex-request
- name: UpdateMultiplexResponse
  property_count: 1
  slug: medialive-api-update-multiplex-response
- name: UpdateReservationRequest
  property_count: 2
  slug: medialive-api-update-reservation-request
- name: UpdateReservationResponse
  property_count: 1
  slug: medialive-api-update-reservation-response
- name: VideoBlackFailoverSettings
  property_count: 2
  slug: medialive-api-video-black-failover-settings
- name: VideoCodecSettings
  property_count: 4
  slug: medialive-api-video-codec-settings
- name: VideoDescriptionRespondToAfd
  property_count: 0
  slug: medialive-api-video-description-respond-to-afd
- name: VideoDescriptionScalingBehavior
  property_count: 0
  slug: medialive-api-video-description-scaling-behavior
- name: VideoDescription
  property_count: 7
  slug: medialive-api-video-description
- name: VideoSelectorColorSpace
  property_count: 0
  slug: medialive-api-video-selector-color-space
- name: VideoSelectorColorSpaceSettings
  property_count: 1
  slug: medialive-api-video-selector-color-space-settings
- name: VideoSelectorColorSpaceUsage
  property_count: 0
  slug: medialive-api-video-selector-color-space-usage
- name: VideoSelectorPid
  property_count: 1
  slug: medialive-api-video-selector-pid
- name: VideoSelectorProgramId
  property_count: 1
  slug: medialive-api-video-selector-program-id
- name: VideoSelector
  property_count: 4
  slug: medialive-api-video-selector
- name: VideoSelectorSettings
  property_count: 2
  slug: medialive-api-video-selector-settings
- name: VpcOutputSettingsDescription
  property_count: 4
  slug: medialive-api-vpc-output-settings-description
- name: VpcOutputSettings
  property_count: 3
  slug: medialive-api-vpc-output-settings
- name: WavCodingMode
  property_count: 0
  slug: medialive-api-wav-coding-mode
- name: WavSettings
  property_count: 3
  slug: medialive-api-wav-settings
- name: WebvttDestinationSettings
  property_count: 1
  slug: medialive-api-webvtt-destination-settings
- name: WebvttDestinationStyleControl
  property_count: 0
  slug: medialive-api-webvtt-destination-style-control
json_structures:
- name: Medialive Api Aac Coding Mode Structure
  property_count: 0
  slug: medialive-api-aac-coding-mode-structure
- name: Medialive Api Aac Input Type Structure
  property_count: 0
  slug: medialive-api-aac-input-type-structure
- name: Medialive Api Aac Profile Structure
  property_count: 0
  slug: medialive-api-aac-profile-structure
- name: Medialive Api Aac Rate Control Mode Structure
  property_count: 0
  slug: medialive-api-aac-rate-control-mode-structure
- name: Medialive Api Aac Raw Format Structure
  property_count: 0
  slug: medialive-api-aac-raw-format-structure
- name: Medialive Api Aac Settings Structure
  property_count: 9
  slug: medialive-api-aac-settings-structure
- name: Medialive Api Aac Spec Structure
  property_count: 0
  slug: medialive-api-aac-spec-structure
- name: Medialive Api Aac Vbr Quality Structure
  property_count: 0
  slug: medialive-api-aac-vbr-quality-structure
- name: Medialive Api Ac3 Bitstream Mode Structure
  property_count: 0
  slug: medialive-api-ac3-bitstream-mode-structure
- name: Medialive Api Ac3 Coding Mode Structure
  property_count: 0
  slug: medialive-api-ac3-coding-mode-structure
- name: Medialive Api Ac3 Drc Profile Structure
  property_count: 0
  slug: medialive-api-ac3-drc-profile-structure
- name: Medialive Api Ac3 Lfe Filter Structure
  property_count: 0
  slug: medialive-api-ac3-lfe-filter-structure
- name: Medialive Api Ac3 Metadata Control Structure
  property_count: 0
  slug: medialive-api-ac3-metadata-control-structure
- name: Medialive Api Ac3 Settings Structure
  property_count: 7
  slug: medialive-api-ac3-settings-structure
- name: Medialive Api Accept Header Structure
  property_count: 0
  slug: medialive-api-accept-header-structure
- name: Medialive Api Accept Input Device Transfer Request Structure
  property_count: 0
  slug: medialive-api-accept-input-device-transfer-request-structure
- name: Medialive Api Accept Input Device Transfer Response Structure
  property_count: 0
  slug: medialive-api-accept-input-device-transfer-response-structure
- name: Medialive Api Accessibility Type Structure
  property_count: 0
  slug: medialive-api-accessibility-type-structure
- name: Medialive Api Afd Signaling Structure
  property_count: 0
  slug: medialive-api-afd-signaling-structure
- name: Medialive Api Ancillary Source Settings Structure
  property_count: 1
  slug: medialive-api-ancillary-source-settings-structure
- name: Medialive Api Archive Cdn Settings Structure
  property_count: 1
  slug: medialive-api-archive-cdn-settings-structure
- name: Medialive Api Archive Container Settings Structure
  property_count: 2
  slug: medialive-api-archive-container-settings-structure
- name: Medialive Api Archive Group Settings Structure
  property_count: 3
  slug: medialive-api-archive-group-settings-structure
- name: Medialive Api Archive Output Settings Structure
  property_count: 3
  slug: medialive-api-archive-output-settings-structure
- name: Medialive Api Archive S3 Settings Structure
  property_count: 1
  slug: medialive-api-archive-s3-settings-structure
- name: Medialive Api Arib Destination Settings Structure
  property_count: 0
  slug: medialive-api-arib-destination-settings-structure
- name: Medialive Api Arib Source Settings Structure
  property_count: 0
  slug: medialive-api-arib-source-settings-structure
- name: Medialive Api Audio Channel Mapping Structure
  property_count: 2
  slug: medialive-api-audio-channel-mapping-structure
- name: Medialive Api Audio Codec Settings Structure
  property_count: 7
  slug: medialive-api-audio-codec-settings-structure
- name: Medialive Api Audio Description Audio Type Control Structure
  property_count: 0
  slug: medialive-api-audio-description-audio-type-control-structure
- name: Medialive Api Audio Description Language Code Control Structure
  property_count: 0
  slug: medialive-api-audio-description-language-code-control-structure
- name: Medialive Api Audio Description Structure
  property_count: 11
  slug: medialive-api-audio-description-structure
- name: Medialive Api Audio Dolby E Decode Structure
  property_count: 1
  slug: medialive-api-audio-dolby-e-decode-structure
- name: Medialive Api Audio Hls Rendition Selection Structure
  property_count: 2
  slug: medialive-api-audio-hls-rendition-selection-structure
- name: Medialive Api Audio Language Selection Policy Structure
  property_count: 0
  slug: medialive-api-audio-language-selection-policy-structure
- name: Medialive Api Audio Language Selection Structure
  property_count: 2
  slug: medialive-api-audio-language-selection-structure
- name: Medialive Api Audio Normalization Algorithm Control Structure
  property_count: 0
  slug: medialive-api-audio-normalization-algorithm-control-structure
- name: Medialive Api Audio Normalization Algorithm Structure
  property_count: 0
  slug: medialive-api-audio-normalization-algorithm-structure
- name: Medialive Api Audio Normalization Settings Structure
  property_count: 3
  slug: medialive-api-audio-normalization-settings-structure
- name: Medialive Api Audio Only Hls Segment Type Structure
  property_count: 0
  slug: medialive-api-audio-only-hls-segment-type-structure
- name: Medialive Api Audio Only Hls Settings Structure
  property_count: 4
  slug: medialive-api-audio-only-hls-settings-structure
- name: Medialive Api Audio Only Hls Track Type Structure
  property_count: 0
  slug: medialive-api-audio-only-hls-track-type-structure
- name: Medialive Api Audio Pid Selection Structure
  property_count: 1
  slug: medialive-api-audio-pid-selection-structure
- name: Medialive Api Audio Selector Settings Structure
  property_count: 4
  slug: medialive-api-audio-selector-settings-structure
- name: Medialive Api Audio Selector Structure
  property_count: 2
  slug: medialive-api-audio-selector-structure
- name: Medialive Api Audio Silence Failover Settings Structure
  property_count: 2
  slug: medialive-api-audio-silence-failover-settings-structure
- name: Medialive Api Audio Track Selection Structure
  property_count: 2
  slug: medialive-api-audio-track-selection-structure
- name: Medialive Api Audio Track Structure
  property_count: 1
  slug: medialive-api-audio-track-structure
- name: Medialive Api Audio Type Structure
  property_count: 0
  slug: medialive-api-audio-type-structure
- name: Medialive Api Audio Watermark Settings Structure
  property_count: 1
  slug: medialive-api-audio-watermark-settings-structure
- name: Medialive Api Authentication Scheme Structure
  property_count: 0
  slug: medialive-api-authentication-scheme-structure
- name: Medialive Api Automatic Input Failover Settings Structure
  property_count: 4
  slug: medialive-api-automatic-input-failover-settings-structure
- name: Medialive Api Avail Blanking State Structure
  property_count: 0
  slug: medialive-api-avail-blanking-state-structure
- name: Medialive Api Avail Blanking Structure
  property_count: 2
  slug: medialive-api-avail-blanking-structure
- name: Medialive Api Avail Configuration Structure
  property_count: 1
  slug: medialive-api-avail-configuration-structure
- name: Medialive Api Avail Settings Structure
  property_count: 3
  slug: medialive-api-avail-settings-structure
- name: Medialive Api Bad Gateway Exception Structure
  property_count: 0
  slug: medialive-api-bad-gateway-exception-structure
- name: Medialive Api Batch Delete Request Structure
  property_count: 4
  slug: medialive-api-batch-delete-request-structure
- name: Medialive Api Batch Delete Response Structure
  property_count: 2
  slug: medialive-api-batch-delete-response-structure
- name: Medialive Api Batch Failed Result Model Structure
  property_count: 4
  slug: medialive-api-batch-failed-result-model-structure
- name: Medialive Api Batch Schedule Action Create Request Structure
  property_count: 1
  slug: medialive-api-batch-schedule-action-create-request-structure
- name: Medialive Api Batch Schedule Action Create Result Structure
  property_count: 1
  slug: medialive-api-batch-schedule-action-create-result-structure
- name: Medialive Api Batch Schedule Action Delete Request Structure
  property_count: 1
  slug: medialive-api-batch-schedule-action-delete-request-structure
- name: Medialive Api Batch Schedule Action Delete Result Structure
  property_count: 1
  slug: medialive-api-batch-schedule-action-delete-result-structure
- name: Medialive Api Batch Start Request Structure
  property_count: 2
  slug: medialive-api-batch-start-request-structure
- name: Medialive Api Batch Start Response Structure
  property_count: 2
  slug: medialive-api-batch-start-response-structure
- name: Medialive Api Batch Stop Request Structure
  property_count: 2
  slug: medialive-api-batch-stop-request-structure
- name: Medialive Api Batch Stop Response Structure
  property_count: 2
  slug: medialive-api-batch-stop-response-structure
- name: Medialive Api Batch Successful Result Model Structure
  property_count: 3
  slug: medialive-api-batch-successful-result-model-structure
- name: Medialive Api Batch Update Schedule Request Structure
  property_count: 2
  slug: medialive-api-batch-update-schedule-request-structure
- name: Medialive Api Batch Update Schedule Response Structure
  property_count: 2
  slug: medialive-api-batch-update-schedule-response-structure
- name: Medialive Api Blackout Slate Network End Blackout Structure
  property_count: 0
  slug: medialive-api-blackout-slate-network-end-blackout-structure
- name: Medialive Api Blackout Slate State Structure
  property_count: 0
  slug: medialive-api-blackout-slate-state-structure
- name: Medialive Api Blackout Slate Structure
  property_count: 5
  slug: medialive-api-blackout-slate-structure
- name: Medialive Api Burn In Alignment Structure
  property_count: 0
  slug: medialive-api-burn-in-alignment-structure
- name: Medialive Api Burn In Background Color Structure
  property_count: 0
  slug: medialive-api-burn-in-background-color-structure
- name: Medialive Api Burn In Destination Settings Structure
  property_count: 17
  slug: medialive-api-burn-in-destination-settings-structure
- name: Medialive Api Burn In Font Color Structure
  property_count: 0
  slug: medialive-api-burn-in-font-color-structure
- name: Medialive Api Burn In Outline Color Structure
  property_count: 0
  slug: medialive-api-burn-in-outline-color-structure
- name: Medialive Api Burn In Shadow Color Structure
  property_count: 0
  slug: medialive-api-burn-in-shadow-color-structure
- name: Medialive Api Burn In Teletext Grid Control Structure
  property_count: 0
  slug: medialive-api-burn-in-teletext-grid-control-structure
- name: Medialive Api Cancel Input Device Transfer Request Structure
  property_count: 0
  slug: medialive-api-cancel-input-device-transfer-request-structure
- name: Medialive Api Cancel Input Device Transfer Response Structure
  property_count: 0
  slug: medialive-api-cancel-input-device-transfer-response-structure
- name: Medialive Api Caption Description Structure
  property_count: 6
  slug: medialive-api-caption-description-structure
- name: Medialive Api Caption Destination Settings Structure
  property_count: 13
  slug: medialive-api-caption-destination-settings-structure
- name: Medialive Api Caption Language Mapping Structure
  property_count: 3
  slug: medialive-api-caption-language-mapping-structure
- name: Medialive Api Caption Rectangle Structure
  property_count: 4
  slug: medialive-api-caption-rectangle-structure
- name: Medialive Api Caption Selector Settings Structure
  property_count: 7
  slug: medialive-api-caption-selector-settings-structure
- name: Medialive Api Caption Selector Structure
  property_count: 3
  slug: medialive-api-caption-selector-structure
- name: Medialive Api Cdi Input Resolution Structure
  property_count: 0
  slug: medialive-api-cdi-input-resolution-structure
- name: Medialive Api Cdi Input Specification Structure
  property_count: 1
  slug: medialive-api-cdi-input-specification-structure
- name: Medialive Api Channel Class Structure
  property_count: 0
  slug: medialive-api-channel-class-structure
- name: Medialive Api Channel Egress Endpoint Structure
  property_count: 1
  slug: medialive-api-channel-egress-endpoint-structure
- name: Medialive Api Channel State Structure
  property_count: 0
  slug: medialive-api-channel-state-structure
- name: Medialive Api Channel Structure
  property_count: 18
  slug: medialive-api-channel-structure
- name: Medialive Api Channel Summary Structure
  property_count: 16
  slug: medialive-api-channel-summary-structure
- name: Medialive Api Claim Device Request Structure
  property_count: 1
  slug: medialive-api-claim-device-request-structure
- name: Medialive Api Claim Device Response Structure
  property_count: 0
  slug: medialive-api-claim-device-response-structure
- name: Medialive Api Color Space Passthrough Settings Structure
  property_count: 0
  slug: medialive-api-color-space-passthrough-settings-structure
- name: Medialive Api Content Type Structure
  property_count: 0
  slug: medialive-api-content-type-structure
- name: Medialive Api Create Channel Request Structure
  property_count: 14
  slug: medialive-api-create-channel-request-structure
- name: Medialive Api Create Channel Response Structure
  property_count: 1
  slug: medialive-api-create-channel-response-structure
- name: Medialive Api Create Input Request Structure
  property_count: 11
  slug: medialive-api-create-input-request-structure
- name: Medialive Api Create Input Response Structure
  property_count: 1
  slug: medialive-api-create-input-response-structure
- name: Medialive Api Create Input Security Group Request Structure
  property_count: 2
  slug: medialive-api-create-input-security-group-request-structure
- name: Medialive Api Create Input Security Group Response Structure
  property_count: 1
  slug: medialive-api-create-input-security-group-response-structure
- name: Medialive Api Create Multiplex Program Request Structure
  property_count: 3
  slug: medialive-api-create-multiplex-program-request-structure
- name: Medialive Api Create Multiplex Program Response Structure
  property_count: 1
  slug: medialive-api-create-multiplex-program-response-structure
- name: Medialive Api Create Multiplex Request Structure
  property_count: 5
  slug: medialive-api-create-multiplex-request-structure
- name: Medialive Api Create Multiplex Response Structure
  property_count: 1
  slug: medialive-api-create-multiplex-response-structure
- name: Medialive Api Create Partner Input Request Structure
  property_count: 2
  slug: medialive-api-create-partner-input-request-structure
- name: Medialive Api Create Partner Input Response Structure
  property_count: 1
  slug: medialive-api-create-partner-input-response-structure
- name: Medialive Api Create Tags Request Structure
  property_count: 1
  slug: medialive-api-create-tags-request-structure
- name: Medialive Api Delete Channel Request Structure
  property_count: 0
  slug: medialive-api-delete-channel-request-structure
- name: Medialive Api Delete Channel Response Structure
  property_count: 18
  slug: medialive-api-delete-channel-response-structure
- name: Medialive Api Delete Input Request Structure
  property_count: 0
  slug: medialive-api-delete-input-request-structure
- name: Medialive Api Delete Input Response Structure
  property_count: 0
  slug: medialive-api-delete-input-response-structure
- name: Medialive Api Delete Input Security Group Request Structure
  property_count: 0
  slug: medialive-api-delete-input-security-group-request-structure
- name: Medialive Api Delete Input Security Group Response Structure
  property_count: 0
  slug: medialive-api-delete-input-security-group-response-structure
- name: Medialive Api Delete Multiplex Program Request Structure
  property_count: 0
  slug: medialive-api-delete-multiplex-program-request-structure
- name: Medialive Api Delete Multiplex Program Response Structure
  property_count: 5
  slug: medialive-api-delete-multiplex-program-response-structure
- name: Medialive Api Delete Multiplex Request Structure
  property_count: 0
  slug: medialive-api-delete-multiplex-request-structure
- name: Medialive Api Delete Multiplex Response Structure
  property_count: 10
  slug: medialive-api-delete-multiplex-response-structure
- name: Medialive Api Delete Reservation Request Structure
  property_count: 0
  slug: medialive-api-delete-reservation-request-structure
- name: Medialive Api Delete Reservation Response Structure
  property_count: 19
  slug: medialive-api-delete-reservation-response-structure
- name: Medialive Api Delete Schedule Request Structure
  property_count: 0
  slug: medialive-api-delete-schedule-request-structure
- name: Medialive Api Delete Schedule Response Structure
  property_count: 0
  slug: medialive-api-delete-schedule-response-structure
- name: Medialive Api Delete Tags Request Structure
  property_count: 0
  slug: medialive-api-delete-tags-request-structure
- name: Medialive Api Describe Channel Request Structure
  property_count: 0
  slug: medialive-api-describe-channel-request-structure
- name: Medialive Api Describe Channel Response Structure
  property_count: 18
  slug: medialive-api-describe-channel-response-structure
- name: Medialive Api Describe Input Device Request Structure
  property_count: 0
  slug: medialive-api-describe-input-device-request-structure
- name: Medialive Api Describe Input Device Response Structure
  property_count: 13
  slug: medialive-api-describe-input-device-response-structure
- name: Medialive Api Describe Input Device Thumbnail Request Structure
  property_count: 0
  slug: medialive-api-describe-input-device-thumbnail-request-structure
- name: Medialive Api Describe Input Device Thumbnail Response Structure
  property_count: 1
  slug: medialive-api-describe-input-device-thumbnail-response-structure
- name: Medialive Api Describe Input Request Structure
  property_count: 0
  slug: medialive-api-describe-input-request-structure
- name: Medialive Api Describe Input Response Structure
  property_count: 16
  slug: medialive-api-describe-input-response-structure
- name: Medialive Api Describe Input Security Group Request Structure
  property_count: 0
  slug: medialive-api-describe-input-security-group-request-structure
- name: Medialive Api Describe Input Security Group Response Structure
  property_count: 6
  slug: medialive-api-describe-input-security-group-response-structure
- name: Medialive Api Describe Multiplex Program Request Structure
  property_count: 0
  slug: medialive-api-describe-multiplex-program-request-structure
- name: Medialive Api Describe Multiplex Program Response Structure
  property_count: 5
  slug: medialive-api-describe-multiplex-program-response-structure
- name: Medialive Api Describe Multiplex Request Structure
  property_count: 0
  slug: medialive-api-describe-multiplex-request-structure
- name: Medialive Api Describe Multiplex Response Structure
  property_count: 10
  slug: medialive-api-describe-multiplex-response-structure
- name: Medialive Api Describe Offering Request Structure
  property_count: 0
  slug: medialive-api-describe-offering-request-structure
- name: Medialive Api Describe Offering Response Structure
  property_count: 11
  slug: medialive-api-describe-offering-response-structure
- name: Medialive Api Describe Reservation Request Structure
  property_count: 0
  slug: medialive-api-describe-reservation-request-structure
- name: Medialive Api Describe Reservation Response Structure
  property_count: 19
  slug: medialive-api-describe-reservation-response-structure
- name: Medialive Api Describe Schedule Request Structure
  property_count: 0
  slug: medialive-api-describe-schedule-request-structure
- name: Medialive Api Describe Schedule Response Structure
  property_count: 2
  slug: medialive-api-describe-schedule-response-structure
- name: Medialive Api Device Settings Sync State Structure
  property_count: 0
  slug: medialive-api-device-settings-sync-state-structure
- name: Medialive Api Device Update Status Structure
  property_count: 0
  slug: medialive-api-device-update-status-structure
- name: Medialive Api Dolby E Program Selection Structure
  property_count: 0
  slug: medialive-api-dolby-e-program-selection-structure
- name: Medialive Api Dolby Vision81 Settings Structure
  property_count: 0
  slug: medialive-api-dolby-vision81-settings-structure
- name: Medialive Api Dvb Nit Settings Structure
  property_count: 3
  slug: medialive-api-dvb-nit-settings-structure
- name: Medialive Api Dvb Sdt Output Sdt Structure
  property_count: 0
  slug: medialive-api-dvb-sdt-output-sdt-structure
- name: Medialive Api Dvb Sdt Settings Structure
  property_count: 4
  slug: medialive-api-dvb-sdt-settings-structure
- name: Medialive Api Dvb Sub Destination Alignment Structure
  property_count: 0
  slug: medialive-api-dvb-sub-destination-alignment-structure
- name: Medialive Api Dvb Sub Destination Background Color Structure
  property_count: 0
  slug: medialive-api-dvb-sub-destination-background-color-structure
- name: Medialive Api Dvb Sub Destination Font Color Structure
  property_count: 0
  slug: medialive-api-dvb-sub-destination-font-color-structure
- name: Medialive Api Dvb Sub Destination Outline Color Structure
  property_count: 0
  slug: medialive-api-dvb-sub-destination-outline-color-structure
- name: Medialive Api Dvb Sub Destination Settings Structure
  property_count: 17
  slug: medialive-api-dvb-sub-destination-settings-structure
- name: Medialive Api Dvb Sub Destination Shadow Color Structure
  property_count: 0
  slug: medialive-api-dvb-sub-destination-shadow-color-structure
- name: Medialive Api Dvb Sub Destination Teletext Grid Control Structure
  property_count: 0
  slug: medialive-api-dvb-sub-destination-teletext-grid-control-structure
- name: Medialive Api Dvb Sub Ocr Language Structure
  property_count: 0
  slug: medialive-api-dvb-sub-ocr-language-structure
- name: Medialive Api Dvb Sub Source Settings Structure
  property_count: 2
  slug: medialive-api-dvb-sub-source-settings-structure
- name: Medialive Api Dvb Tdt Settings Structure
  property_count: 1
  slug: medialive-api-dvb-tdt-settings-structure
- name: Medialive Api Eac3 Atmos Coding Mode Structure
  property_count: 0
  slug: medialive-api-eac3-atmos-coding-mode-structure
- name: Medialive Api Eac3 Atmos Drc Line Structure
  property_count: 0
  slug: medialive-api-eac3-atmos-drc-line-structure
- name: Medialive Api Eac3 Atmos Drc Rf Structure
  property_count: 0
  slug: medialive-api-eac3-atmos-drc-rf-structure
- name: Medialive Api Eac3 Atmos Settings Structure
  property_count: 7
  slug: medialive-api-eac3-atmos-settings-structure
- name: Medialive Api Eac3 Attenuation Control Structure
  property_count: 0
  slug: medialive-api-eac3-attenuation-control-structure
- name: Medialive Api Eac3 Bitstream Mode Structure
  property_count: 0
  slug: medialive-api-eac3-bitstream-mode-structure
- name: Medialive Api Eac3 Coding Mode Structure
  property_count: 0
  slug: medialive-api-eac3-coding-mode-structure
- name: Medialive Api Eac3 Dc Filter Structure
  property_count: 0
  slug: medialive-api-eac3-dc-filter-structure
- name: Medialive Api Eac3 Drc Line Structure
  property_count: 0
  slug: medialive-api-eac3-drc-line-structure
- name: Medialive Api Eac3 Drc Rf Structure
  property_count: 0
  slug: medialive-api-eac3-drc-rf-structure
- name: Medialive Api Eac3 Lfe Control Structure
  property_count: 0
  slug: medialive-api-eac3-lfe-control-structure
- name: Medialive Api Eac3 Lfe Filter Structure
  property_count: 0
  slug: medialive-api-eac3-lfe-filter-structure
- name: Medialive Api Eac3 Metadata Control Structure
  property_count: 0
  slug: medialive-api-eac3-metadata-control-structure
- name: Medialive Api Eac3 Passthrough Control Structure
  property_count: 0
  slug: medialive-api-eac3-passthrough-control-structure
- name: Medialive Api Eac3 Phase Control Structure
  property_count: 0
  slug: medialive-api-eac3-phase-control-structure
- name: Medialive Api Eac3 Settings Structure
  property_count: 20
  slug: medialive-api-eac3-settings-structure
- name: Medialive Api Eac3 Stereo Downmix Structure
  property_count: 0
  slug: medialive-api-eac3-stereo-downmix-structure
- name: Medialive Api Eac3 Surround Ex Mode Structure
  property_count: 0
  slug: medialive-api-eac3-surround-ex-mode-structure
- name: Medialive Api Eac3 Surround Mode Structure
  property_count: 0
  slug: medialive-api-eac3-surround-mode-structure
- name: Medialive Api Ebu Tt D Destination Settings Structure
  property_count: 4
  slug: medialive-api-ebu-tt-d-destination-settings-structure
- name: Medialive Api Ebu Tt D Destination Style Control Structure
  property_count: 0
  slug: medialive-api-ebu-tt-d-destination-style-control-structure
- name: Medialive Api Ebu Tt D Fill Line Gap Control Structure
  property_count: 0
  slug: medialive-api-ebu-tt-d-fill-line-gap-control-structure
- name: Medialive Api Embedded Convert608 To708 Structure
  property_count: 0
  slug: medialive-api-embedded-convert608-to708-structure
- name: Medialive Api Embedded Destination Settings Structure
  property_count: 0
  slug: medialive-api-embedded-destination-settings-structure
- name: Medialive Api Embedded Plus Scte20 Destination Settings Structure
  property_count: 0
  slug: medialive-api-embedded-plus-scte20-destination-settings-structure
- name: Medialive Api Embedded Scte20 Detection Structure
  property_count: 0
  slug: medialive-api-embedded-scte20-detection-structure
- name: Medialive Api Embedded Source Settings Structure
  property_count: 4
  slug: medialive-api-embedded-source-settings-structure
- name: Medialive Api Encoder Settings Structure
  property_count: 12
  slug: medialive-api-encoder-settings-structure
- name: Medialive Api Esam Structure
  property_count: 6
  slug: medialive-api-esam-structure
- name: Medialive Api Failover Condition Settings Structure
  property_count: 3
  slug: medialive-api-failover-condition-settings-structure
- name: Medialive Api Failover Condition Structure
  property_count: 1
  slug: medialive-api-failover-condition-structure
- name: Medialive Api Feature Activations Input Prepare Schedule Actions Structure
  property_count: 0
  slug: medialive-api-feature-activations-input-prepare-schedule-actions-structure
- name: Medialive Api Feature Activations Structure
  property_count: 1
  slug: medialive-api-feature-activations-structure
- name: Medialive Api Fec Output Include Fec Structure
  property_count: 0
  slug: medialive-api-fec-output-include-fec-structure
- name: Medialive Api Fec Output Settings Structure
  property_count: 3
  slug: medialive-api-fec-output-settings-structure
- name: Medialive Api Fixed Afd Structure
  property_count: 0
  slug: medialive-api-fixed-afd-structure
- name: Medialive Api Fixed Mode Schedule Action Start Settings Structure
  property_count: 1
  slug: medialive-api-fixed-mode-schedule-action-start-settings-structure
- name: Medialive Api Fmp4 Hls Settings Structure
  property_count: 3
  slug: medialive-api-fmp4-hls-settings-structure
- name: Medialive Api Fmp4 Nielsen Id3 Behavior Structure
  property_count: 0
  slug: medialive-api-fmp4-nielsen-id3-behavior-structure
- name: Medialive Api Fmp4 Timed Metadata Behavior Structure
  property_count: 0
  slug: medialive-api-fmp4-timed-metadata-behavior-structure
- name: Medialive Api Follow Mode Schedule Action Start Settings Structure
  property_count: 2
  slug: medialive-api-follow-mode-schedule-action-start-settings-structure
- name: Medialive Api Follow Point Structure
  property_count: 0
  slug: medialive-api-follow-point-structure
- name: Medialive Api Frame Capture Cdn Settings Structure
  property_count: 1
  slug: medialive-api-frame-capture-cdn-settings-structure
- name: Medialive Api Frame Capture Group Settings Structure
  property_count: 2
  slug: medialive-api-frame-capture-group-settings-structure
- name: Medialive Api Frame Capture Hls Settings Structure
  property_count: 0
  slug: medialive-api-frame-capture-hls-settings-structure
- name: Medialive Api Frame Capture Interval Unit Structure
  property_count: 0
  slug: medialive-api-frame-capture-interval-unit-structure
- name: Medialive Api Frame Capture Output Settings Structure
  property_count: 1
  slug: medialive-api-frame-capture-output-settings-structure
- name: Medialive Api Frame Capture S3 Settings Structure
  property_count: 1
  slug: medialive-api-frame-capture-s3-settings-structure
- name: Medialive Api Frame Capture Settings Structure
  property_count: 3
  slug: medialive-api-frame-capture-settings-structure
- name: Medialive Api Gateway Timeout Exception Structure
  property_count: 0
  slug: medialive-api-gateway-timeout-exception-structure
- name: Medialive Api Global Configuration Input End Action Structure
  property_count: 0
  slug: medialive-api-global-configuration-input-end-action-structure
- name: Medialive Api Global Configuration Low Framerate Inputs Structure
  property_count: 0
  slug: medialive-api-global-configuration-low-framerate-inputs-structure
- name: Medialive Api Global Configuration Output Locking Mode Structure
  property_count: 0
  slug: medialive-api-global-configuration-output-locking-mode-structure
- name: Medialive Api Global Configuration Output Timing Source Structure
  property_count: 0
  slug: medialive-api-global-configuration-output-timing-source-structure
- name: Medialive Api Global Configuration Structure
  property_count: 6
  slug: medialive-api-global-configuration-structure
- name: Medialive Api H264 Adaptive Quantization Structure
  property_count: 0
  slug: medialive-api-h264-adaptive-quantization-structure
- name: Medialive Api H264 Color Metadata Structure
  property_count: 0
  slug: medialive-api-h264-color-metadata-structure
- name: Medialive Api H264 Color Space Settings Structure
  property_count: 3
  slug: medialive-api-h264-color-space-settings-structure
- name: Medialive Api H264 Entropy Encoding Structure
  property_count: 0
  slug: medialive-api-h264-entropy-encoding-structure
- name: Medialive Api H264 Filter Settings Structure
  property_count: 1
  slug: medialive-api-h264-filter-settings-structure
- name: Medialive Api H264 Flicker Aq Structure
  property_count: 0
  slug: medialive-api-h264-flicker-aq-structure
- name: Medialive Api H264 Force Field Pictures Structure
  property_count: 0
  slug: medialive-api-h264-force-field-pictures-structure
- name: Medialive Api H264 Framerate Control Structure
  property_count: 0
  slug: medialive-api-h264-framerate-control-structure
- name: Medialive Api H264 Gop B Reference Structure
  property_count: 0
  slug: medialive-api-h264-gop-b-reference-structure
- name: Medialive Api H264 Gop Size Units Structure
  property_count: 0
  slug: medialive-api-h264-gop-size-units-structure
- name: Medialive Api H264 Level Structure
  property_count: 0
  slug: medialive-api-h264-level-structure
- name: Medialive Api H264 Look Ahead Rate Control Structure
  property_count: 0
  slug: medialive-api-h264-look-ahead-rate-control-structure
- name: Medialive Api H264 Par Control Structure
  property_count: 0
  slug: medialive-api-h264-par-control-structure
- name: Medialive Api H264 Profile Structure
  property_count: 0
  slug: medialive-api-h264-profile-structure
- name: Medialive Api H264 Quality Level Structure
  property_count: 0
  slug: medialive-api-h264-quality-level-structure
- name: Medialive Api H264 Rate Control Mode Structure
  property_count: 0
  slug: medialive-api-h264-rate-control-mode-structure
- name: Medialive Api H264 Scan Type Structure
  property_count: 0
  slug: medialive-api-h264-scan-type-structure
- name: Medialive Api H264 Scene Change Detect Structure
  property_count: 0
  slug: medialive-api-h264-scene-change-detect-structure
- name: Medialive Api H264 Settings Structure
  property_count: 42
  slug: medialive-api-h264-settings-structure
- name: Medialive Api H264 Spatial Aq Structure
  property_count: 0
  slug: medialive-api-h264-spatial-aq-structure
- name: Medialive Api H264 Sub Gop Length Structure
  property_count: 0
  slug: medialive-api-h264-sub-gop-length-structure
- name: Medialive Api H264 Syntax Structure
  property_count: 0
  slug: medialive-api-h264-syntax-structure
- name: Medialive Api H264 Temporal Aq Structure
  property_count: 0
  slug: medialive-api-h264-temporal-aq-structure
- name: Medialive Api H264 Timecode Insertion Behavior Structure
  property_count: 0
  slug: medialive-api-h264-timecode-insertion-behavior-structure
- name: Medialive Api H265 Adaptive Quantization Structure
  property_count: 0
  slug: medialive-api-h265-adaptive-quantization-structure
- name: Medialive Api H265 Alternative Transfer Function Structure
  property_count: 0
  slug: medialive-api-h265-alternative-transfer-function-structure
- name: Medialive Api H265 Color Metadata Structure
  property_count: 0
  slug: medialive-api-h265-color-metadata-structure
- name: Medialive Api H265 Color Space Settings Structure
  property_count: 5
  slug: medialive-api-h265-color-space-settings-structure
- name: Medialive Api H265 Filter Settings Structure
  property_count: 1
  slug: medialive-api-h265-filter-settings-structure
- name: Medialive Api H265 Flicker Aq Structure
  property_count: 0
  slug: medialive-api-h265-flicker-aq-structure
- name: Medialive Api H265 Gop Size Units Structure
  property_count: 0
  slug: medialive-api-h265-gop-size-units-structure
- name: Medialive Api H265 Level Structure
  property_count: 0
  slug: medialive-api-h265-level-structure
- name: Medialive Api H265 Look Ahead Rate Control Structure
  property_count: 0
  slug: medialive-api-h265-look-ahead-rate-control-structure
- name: Medialive Api H265 Profile Structure
  property_count: 0
  slug: medialive-api-h265-profile-structure
- name: Medialive Api H265 Rate Control Mode Structure
  property_count: 0
  slug: medialive-api-h265-rate-control-mode-structure
- name: Medialive Api H265 Scan Type Structure
  property_count: 0
  slug: medialive-api-h265-scan-type-structure
- name: Medialive Api H265 Scene Change Detect Structure
  property_count: 0
  slug: medialive-api-h265-scene-change-detect-structure
- name: Medialive Api H265 Settings Structure
  property_count: 30
  slug: medialive-api-h265-settings-structure
- name: Medialive Api H265 Tier Structure
  property_count: 0
  slug: medialive-api-h265-tier-structure
- name: Medialive Api H265 Timecode Insertion Behavior Structure
  property_count: 0
  slug: medialive-api-h265-timecode-insertion-behavior-structure
- name: Medialive Api Hdr10 Settings Structure
  property_count: 2
  slug: medialive-api-hdr10-settings-structure
- name: Medialive Api Hls Ad Markers Structure
  property_count: 0
  slug: medialive-api-hls-ad-markers-structure
- name: Medialive Api Hls Akamai Http Transfer Mode Structure
  property_count: 0
  slug: medialive-api-hls-akamai-http-transfer-mode-structure
- name: Medialive Api Hls Akamai Settings Structure
  property_count: 7
  slug: medialive-api-hls-akamai-settings-structure
- name: Medialive Api Hls Basic Put Settings Structure
  property_count: 4
  slug: medialive-api-hls-basic-put-settings-structure
- name: Medialive Api Hls Caption Language Setting Structure
  property_count: 0
  slug: medialive-api-hls-caption-language-setting-structure
- name: Medialive Api Hls Cdn Settings Structure
  property_count: 5
  slug: medialive-api-hls-cdn-settings-structure
- name: Medialive Api Hls Client Cache Structure
  property_count: 0
  slug: medialive-api-hls-client-cache-structure
- name: Medialive Api Hls Codec Specification Structure
  property_count: 0
  slug: medialive-api-hls-codec-specification-structure
- name: Medialive Api Hls Directory Structure Structure
  property_count: 0
  slug: medialive-api-hls-directory-structure-structure
- name: Medialive Api Hls Discontinuity Tags Structure
  property_count: 0
  slug: medialive-api-hls-discontinuity-tags-structure
- name: Medialive Api Hls Encryption Type Structure
  property_count: 0
  slug: medialive-api-hls-encryption-type-structure
- name: Medialive Api Hls Group Settings Structure
  property_count: 43
  slug: medialive-api-hls-group-settings-structure
- name: Medialive Api Hls H265 Packaging Type Structure
  property_count: 0
  slug: medialive-api-hls-h265-packaging-type-structure
- name: Medialive Api Hls Id3 Segment Tagging Schedule Action Settings Structure
  property_count: 2
  slug: medialive-api-hls-id3-segment-tagging-schedule-action-settings-structure
- name: Medialive Api Hls Id3 Segment Tagging State Structure
  property_count: 0
  slug: medialive-api-hls-id3-segment-tagging-state-structure
- name: Medialive Api Hls Incomplete Segment Behavior Structure
  property_count: 0
  slug: medialive-api-hls-incomplete-segment-behavior-structure
- name: Medialive Api Hls Input Settings Structure
  property_count: 5
  slug: medialive-api-hls-input-settings-structure
- name: Medialive Api Hls Iv In Manifest Structure
  property_count: 0
  slug: medialive-api-hls-iv-in-manifest-structure
- name: Medialive Api Hls Iv Source Structure
  property_count: 0
  slug: medialive-api-hls-iv-source-structure
- name: Medialive Api Hls Manifest Compression Structure
  property_count: 0
  slug: medialive-api-hls-manifest-compression-structure
- name: Medialive Api Hls Manifest Duration Format Structure
  property_count: 0
  slug: medialive-api-hls-manifest-duration-format-structure
- name: Medialive Api Hls Media Store Settings Structure
  property_count: 5
  slug: medialive-api-hls-media-store-settings-structure
- name: Medialive Api Hls Media Store Storage Class Structure
  property_count: 0
  slug: medialive-api-hls-media-store-storage-class-structure
- name: Medialive Api Hls Mode Structure
  property_count: 0
  slug: medialive-api-hls-mode-structure
- name: Medialive Api Hls Output Selection Structure
  property_count: 0
  slug: medialive-api-hls-output-selection-structure
- name: Medialive Api Hls Output Settings Structure
  property_count: 4
  slug: medialive-api-hls-output-settings-structure
- name: Medialive Api Hls Program Date Time Clock Structure
  property_count: 0
  slug: medialive-api-hls-program-date-time-clock-structure
- name: Medialive Api Hls Program Date Time Structure
  property_count: 0
  slug: medialive-api-hls-program-date-time-structure
- name: Medialive Api Hls Redundant Manifest Structure
  property_count: 0
  slug: medialive-api-hls-redundant-manifest-structure
- name: Medialive Api Hls S3 Settings Structure
  property_count: 1
  slug: medialive-api-hls-s3-settings-structure
- name: Medialive Api Hls Scte35 Source Type Structure
  property_count: 0
  slug: medialive-api-hls-scte35-source-type-structure
- name: Medialive Api Hls Segmentation Mode Structure
  property_count: 0
  slug: medialive-api-hls-segmentation-mode-structure
- name: Medialive Api Hls Settings Structure
  property_count: 4
  slug: medialive-api-hls-settings-structure
- name: Medialive Api Hls Stream Inf Resolution Structure
  property_count: 0
  slug: medialive-api-hls-stream-inf-resolution-structure
- name: Medialive Api Hls Timed Metadata Id3 Frame Structure
  property_count: 0
  slug: medialive-api-hls-timed-metadata-id3-frame-structure
- name: Medialive Api Hls Timed Metadata Schedule Action Settings Structure
  property_count: 1
  slug: medialive-api-hls-timed-metadata-schedule-action-settings-structure
- name: Medialive Api Hls Ts File Mode Structure
  property_count: 0
  slug: medialive-api-hls-ts-file-mode-structure
- name: Medialive Api Hls Webdav Http Transfer Mode Structure
  property_count: 0
  slug: medialive-api-hls-webdav-http-transfer-mode-structure
- name: Medialive Api Hls Webdav Settings Structure
  property_count: 5
  slug: medialive-api-hls-webdav-settings-structure
- name: Medialive Api Html Motion Graphics Settings Structure
  property_count: 0
  slug: medialive-api-html-motion-graphics-settings-structure
- name: Medialive Api I Frame Only Playlist Type Structure
  property_count: 0
  slug: medialive-api-i-frame-only-playlist-type-structure
- name: Medialive Api Immediate Mode Schedule Action Start Settings Structure
  property_count: 0
  slug: medialive-api-immediate-mode-schedule-action-start-settings-structure
- name: Medialive Api Input Attachment Structure
  property_count: 4
  slug: medialive-api-input-attachment-structure
- name: Medialive Api Input Channel Level Structure
  property_count: 2
  slug: medialive-api-input-channel-level-structure
- name: Medialive Api Input Class Structure
  property_count: 0
  slug: medialive-api-input-class-structure
- name: Medialive Api Input Clipping Settings Structure
  property_count: 3
  slug: medialive-api-input-clipping-settings-structure
- name: Medialive Api Input Codec Structure
  property_count: 0
  slug: medialive-api-input-codec-structure
- name: Medialive Api Input Deblock Filter Structure
  property_count: 0
  slug: medialive-api-input-deblock-filter-structure
- name: Medialive Api Input Denoise Filter Structure
  property_count: 0
  slug: medialive-api-input-denoise-filter-structure
- name: Medialive Api Input Destination Request Structure
  property_count: 1
  slug: medialive-api-input-destination-request-structure
- name: Medialive Api Input Destination Structure
  property_count: 4
  slug: medialive-api-input-destination-structure
- name: Medialive Api Input Destination Vpc Structure
  property_count: 2
  slug: medialive-api-input-destination-vpc-structure
- name: Medialive Api Input Device Active Input Structure
  property_count: 0
  slug: medialive-api-input-device-active-input-structure
- name: Medialive Api Input Device Configurable Settings Structure
  property_count: 3
  slug: medialive-api-input-device-configurable-settings-structure
- name: Medialive Api Input Device Configured Input Structure
  property_count: 0
  slug: medialive-api-input-device-configured-input-structure
- name: Medialive Api Input Device Connection State Structure
  property_count: 0
  slug: medialive-api-input-device-connection-state-structure
- name: Medialive Api Input Device Hd Settings Structure
  property_count: 9
  slug: medialive-api-input-device-hd-settings-structure
- name: Medialive Api Input Device Ip Scheme Structure
  property_count: 0
  slug: medialive-api-input-device-ip-scheme-structure
- name: Medialive Api Input Device Network Settings Structure
  property_count: 5
  slug: medialive-api-input-device-network-settings-structure
- name: Medialive Api Input Device Request Structure
  property_count: 1
  slug: medialive-api-input-device-request-structure
- name: Medialive Api Input Device Scan Type Structure
  property_count: 0
  slug: medialive-api-input-device-scan-type-structure
- name: Medialive Api Input Device Settings Structure
  property_count: 1
  slug: medialive-api-input-device-settings-structure
- name: Medialive Api Input Device State Structure
  property_count: 0
  slug: medialive-api-input-device-state-structure
- name: Medialive Api Input Device Summary Structure
  property_count: 13
  slug: medialive-api-input-device-summary-structure
- name: Medialive Api Input Device Thumbnail Structure
  property_count: 0
  slug: medialive-api-input-device-thumbnail-structure
- name: Medialive Api Input Device Transfer Type Structure
  property_count: 0
  slug: medialive-api-input-device-transfer-type-structure
- name: Medialive Api Input Device Type Structure
  property_count: 0
  slug: medialive-api-input-device-type-structure
- name: Medialive Api Input Device Uhd Settings Structure
  property_count: 9
  slug: medialive-api-input-device-uhd-settings-structure
- name: Medialive Api Input Filter Structure
  property_count: 0
  slug: medialive-api-input-filter-structure
- name: Medialive Api Input Location Structure
  property_count: 3
  slug: medialive-api-input-location-structure
- name: Medialive Api Input Loss Action For Hls Out Structure
  property_count: 0
  slug: medialive-api-input-loss-action-for-hls-out-structure
- name: Medialive Api Input Loss Action For Ms Smooth Out Structure
  property_count: 0
  slug: medialive-api-input-loss-action-for-ms-smooth-out-structure
- name: Medialive Api Input Loss Action For Rtmp Out Structure
  property_count: 0
  slug: medialive-api-input-loss-action-for-rtmp-out-structure
- name: Medialive Api Input Loss Action For Udp Out Structure
  property_count: 0
  slug: medialive-api-input-loss-action-for-udp-out-structure
- name: Medialive Api Input Loss Behavior Structure
  property_count: 5
  slug: medialive-api-input-loss-behavior-structure
- name: Medialive Api Input Loss Failover Settings Structure
  property_count: 1
  slug: medialive-api-input-loss-failover-settings-structure
- name: Medialive Api Input Loss Image Type Structure
  property_count: 0
  slug: medialive-api-input-loss-image-type-structure
- name: Medialive Api Input Maximum Bitrate Structure
  property_count: 0
  slug: medialive-api-input-maximum-bitrate-structure
- name: Medialive Api Input Preference Structure
  property_count: 0
  slug: medialive-api-input-preference-structure
- name: Medialive Api Input Prepare Schedule Action Settings Structure
  property_count: 3
  slug: medialive-api-input-prepare-schedule-action-settings-structure
- name: Medialive Api Input Resolution Structure
  property_count: 0
  slug: medialive-api-input-resolution-structure
- name: Medialive Api Input Security Group State Structure
  property_count: 0
  slug: medialive-api-input-security-group-state-structure
- name: Medialive Api Input Security Group Structure
  property_count: 6
  slug: medialive-api-input-security-group-structure
- name: Medialive Api Input Settings Structure
  property_count: 11
  slug: medialive-api-input-settings-structure
- name: Medialive Api Input Source End Behavior Structure
  property_count: 0
  slug: medialive-api-input-source-end-behavior-structure
- name: Medialive Api Input Source Request Structure
  property_count: 3
  slug: medialive-api-input-source-request-structure
- name: Medialive Api Input Source Structure
  property_count: 3
  slug: medialive-api-input-source-structure
- name: Medialive Api Input Source Type Structure
  property_count: 0
  slug: medialive-api-input-source-type-structure
- name: Medialive Api Input Specification Structure
  property_count: 3
  slug: medialive-api-input-specification-structure
- name: Medialive Api Input State Structure
  property_count: 0
  slug: medialive-api-input-state-structure
- name: Medialive Api Input Structure
  property_count: 16
  slug: medialive-api-input-structure
- name: Medialive Api Input Switch Schedule Action Settings Structure
  property_count: 3
  slug: medialive-api-input-switch-schedule-action-settings-structure
- name: Medialive Api Input Timecode Source Structure
  property_count: 0
  slug: medialive-api-input-timecode-source-structure
- name: Medialive Api Input Type Structure
  property_count: 0
  slug: medialive-api-input-type-structure
- name: Medialive Api Input Vpc Request Structure
  property_count: 2
  slug: medialive-api-input-vpc-request-structure
- name: Medialive Api Input Whitelist Rule Cidr Structure
  property_count: 1
  slug: medialive-api-input-whitelist-rule-cidr-structure
- name: Medialive Api Input Whitelist Rule Structure
  property_count: 1
  slug: medialive-api-input-whitelist-rule-structure
- name: Medialive Api Key Provider Settings Structure
  property_count: 1
  slug: medialive-api-key-provider-settings-structure
- name: Medialive Api Last Frame Clipping Behavior Structure
  property_count: 0
  slug: medialive-api-last-frame-clipping-behavior-structure
- name: Medialive Api List Channels Request Structure
  property_count: 0
  slug: medialive-api-list-channels-request-structure
- name: Medialive Api List Channels Response Structure
  property_count: 2
  slug: medialive-api-list-channels-response-structure
- name: Medialive Api List Input Device Transfers Request Structure
  property_count: 0
  slug: medialive-api-list-input-device-transfers-request-structure
- name: Medialive Api List Input Device Transfers Response Structure
  property_count: 2
  slug: medialive-api-list-input-device-transfers-response-structure
- name: Medialive Api List Input Devices Request Structure
  property_count: 0
  slug: medialive-api-list-input-devices-request-structure
- name: Medialive Api List Input Devices Response Structure
  property_count: 2
  slug: medialive-api-list-input-devices-response-structure
- name: Medialive Api List Input Security Groups Request Structure
  property_count: 0
  slug: medialive-api-list-input-security-groups-request-structure
- name: Medialive Api List Input Security Groups Response Structure
  property_count: 2
  slug: medialive-api-list-input-security-groups-response-structure
- name: Medialive Api List Inputs Request Structure
  property_count: 0
  slug: medialive-api-list-inputs-request-structure
- name: Medialive Api List Inputs Response Structure
  property_count: 2
  slug: medialive-api-list-inputs-response-structure
- name: Medialive Api List Multiplex Programs Request Structure
  property_count: 0
  slug: medialive-api-list-multiplex-programs-request-structure
- name: Medialive Api List Multiplex Programs Response Structure
  property_count: 2
  slug: medialive-api-list-multiplex-programs-response-structure
- name: Medialive Api List Multiplexes Request Structure
  property_count: 0
  slug: medialive-api-list-multiplexes-request-structure
- name: Medialive Api List Multiplexes Response Structure
  property_count: 2
  slug: medialive-api-list-multiplexes-response-structure
- name: Medialive Api List Offerings Request Structure
  property_count: 0
  slug: medialive-api-list-offerings-request-structure
- name: Medialive Api List Offerings Response Structure
  property_count: 2
  slug: medialive-api-list-offerings-response-structure
- name: Medialive Api List Reservations Request Structure
  property_count: 0
  slug: medialive-api-list-reservations-request-structure
- name: Medialive Api List Reservations Response Structure
  property_count: 2
  slug: medialive-api-list-reservations-response-structure
- name: Medialive Api List Tags For Resource Request Structure
  property_count: 0
  slug: medialive-api-list-tags-for-resource-request-structure
- name: Medialive Api List Tags For Resource Response Structure
  property_count: 1
  slug: medialive-api-list-tags-for-resource-response-structure
- name: Medialive Api Log Level Structure
  property_count: 0
  slug: medialive-api-log-level-structure
- name: Medialive Api M2Ts Absent Input Audio Behavior Structure
  property_count: 0
  slug: medialive-api-m2ts-absent-input-audio-behavior-structure
- name: Medialive Api M2Ts Arib Captions Pid Control Structure
  property_count: 0
  slug: medialive-api-m2ts-arib-captions-pid-control-structure
- name: Medialive Api M2Ts Arib Structure
  property_count: 0
  slug: medialive-api-m2ts-arib-structure
- name: Medialive Api M2Ts Audio Buffer Model Structure
  property_count: 0
  slug: medialive-api-m2ts-audio-buffer-model-structure
- name: Medialive Api M2Ts Audio Interval Structure
  property_count: 0
  slug: medialive-api-m2ts-audio-interval-structure
- name: Medialive Api M2Ts Audio Stream Type Structure
  property_count: 0
  slug: medialive-api-m2ts-audio-stream-type-structure
- name: Medialive Api M2Ts Buffer Model Structure
  property_count: 0
  slug: medialive-api-m2ts-buffer-model-structure
- name: Medialive Api M2Ts Cc Descriptor Structure
  property_count: 0
  slug: medialive-api-m2ts-cc-descriptor-structure
- name: Medialive Api M2Ts Ebif Control Structure
  property_count: 0
  slug: medialive-api-m2ts-ebif-control-structure
- name: Medialive Api M2Ts Ebp Placement Structure
  property_count: 0
  slug: medialive-api-m2ts-ebp-placement-structure
- name: Medialive Api M2Ts Es Rate In Pes Structure
  property_count: 0
  slug: medialive-api-m2ts-es-rate-in-pes-structure
- name: Medialive Api M2Ts Klv Structure
  property_count: 0
  slug: medialive-api-m2ts-klv-structure
- name: Medialive Api M2Ts Nielsen Id3 Behavior Structure
  property_count: 0
  slug: medialive-api-m2ts-nielsen-id3-behavior-structure
- name: Medialive Api M2Ts Pcr Control Structure
  property_count: 0
  slug: medialive-api-m2ts-pcr-control-structure
- name: Medialive Api M2Ts Rate Mode Structure
  property_count: 0
  slug: medialive-api-m2ts-rate-mode-structure
- name: Medialive Api M2Ts Scte35 Control Structure
  property_count: 0
  slug: medialive-api-m2ts-scte35-control-structure
- name: Medialive Api M2Ts Segmentation Markers Structure
  property_count: 0
  slug: medialive-api-m2ts-segmentation-markers-structure
- name: Medialive Api M2Ts Segmentation Style Structure
  property_count: 0
  slug: medialive-api-m2ts-segmentation-style-structure
- name: Medialive Api M2Ts Settings Structure
  property_count: 48
  slug: medialive-api-m2ts-settings-structure
- name: Medialive Api M2Ts Timed Metadata Behavior Structure
  property_count: 0
  slug: medialive-api-m2ts-timed-metadata-behavior-structure
- name: Medialive Api M3U8 Nielsen Id3 Behavior Structure
  property_count: 0
  slug: medialive-api-m3u8-nielsen-id3-behavior-structure
- name: Medialive Api M3U8 Pcr Control Structure
  property_count: 0
  slug: medialive-api-m3u8-pcr-control-structure
- name: Medialive Api M3U8 Scte35 Behavior Structure
  property_count: 0
  slug: medialive-api-m3u8-scte35-behavior-structure
- name: Medialive Api M3U8 Settings Structure
  property_count: 17
  slug: medialive-api-m3u8-settings-structure
- name: Medialive Api M3U8 Timed Metadata Behavior Structure
  property_count: 0
  slug: medialive-api-m3u8-timed-metadata-behavior-structure
- name: Medialive Api Maintenance Create Settings Structure
  property_count: 2
  slug: medialive-api-maintenance-create-settings-structure
- name: Medialive Api Maintenance Day Structure
  property_count: 0
  slug: medialive-api-maintenance-day-structure
- name: Medialive Api Maintenance Status Structure
  property_count: 4
  slug: medialive-api-maintenance-status-structure
- name: Medialive Api Maintenance Update Settings Structure
  property_count: 3
  slug: medialive-api-maintenance-update-settings-structure
- name: Medialive Api Max Results Structure
  property_count: 0
  slug: medialive-api-max-results-structure
- name: Medialive Api Media Connect Flow Request Structure
  property_count: 1
  slug: medialive-api-media-connect-flow-request-structure
- name: Medialive Api Media Connect Flow Structure
  property_count: 1
  slug: medialive-api-media-connect-flow-structure
- name: Medialive Api Media Package Group Settings Structure
  property_count: 1
  slug: medialive-api-media-package-group-settings-structure
- name: Medialive Api Media Package Output Destination Settings Structure
  property_count: 1
  slug: medialive-api-media-package-output-destination-settings-structure
- name: Medialive Api Media Package Output Settings Structure
  property_count: 0
  slug: medialive-api-media-package-output-settings-structure
- name: Medialive Api Motion Graphics Activate Schedule Action Settings Structure
  property_count: 4
  slug: medialive-api-motion-graphics-activate-schedule-action-settings-structure
- name: Medialive Api Motion Graphics Configuration Structure
  property_count: 2
  slug: medialive-api-motion-graphics-configuration-structure
- name: Medialive Api Motion Graphics Deactivate Schedule Action Settings Structure
  property_count: 0
  slug: medialive-api-motion-graphics-deactivate-schedule-action-settings-structure
- name: Medialive Api Motion Graphics Insertion Structure
  property_count: 0
  slug: medialive-api-motion-graphics-insertion-structure
- name: Medialive Api Motion Graphics Settings Structure
  property_count: 1
  slug: medialive-api-motion-graphics-settings-structure
- name: Medialive Api Mp2 Coding Mode Structure
  property_count: 0
  slug: medialive-api-mp2-coding-mode-structure
- name: Medialive Api Mp2 Settings Structure
  property_count: 3
  slug: medialive-api-mp2-settings-structure
- name: Medialive Api Mpeg2 Adaptive Quantization Structure
  property_count: 0
  slug: medialive-api-mpeg2-adaptive-quantization-structure
- name: Medialive Api Mpeg2 Color Metadata Structure
  property_count: 0
  slug: medialive-api-mpeg2-color-metadata-structure
- name: Medialive Api Mpeg2 Color Space Structure
  property_count: 0
  slug: medialive-api-mpeg2-color-space-structure
- name: Medialive Api Mpeg2 Display Ratio Structure
  property_count: 0
  slug: medialive-api-mpeg2-display-ratio-structure
- name: Medialive Api Mpeg2 Filter Settings Structure
  property_count: 1
  slug: medialive-api-mpeg2-filter-settings-structure
- name: Medialive Api Mpeg2 Gop Size Units Structure
  property_count: 0
  slug: medialive-api-mpeg2-gop-size-units-structure
- name: Medialive Api Mpeg2 Scan Type Structure
  property_count: 0
  slug: medialive-api-mpeg2-scan-type-structure
- name: Medialive Api Mpeg2 Settings Structure
  property_count: 17
  slug: medialive-api-mpeg2-settings-structure
- name: Medialive Api Mpeg2 Sub Gop Length Structure
  property_count: 0
  slug: medialive-api-mpeg2-sub-gop-length-structure
- name: Medialive Api Mpeg2 Timecode Insertion Behavior Structure
  property_count: 0
  slug: medialive-api-mpeg2-timecode-insertion-behavior-structure
- name: Medialive Api Ms Smooth Group Settings Structure
  property_count: 19
  slug: medialive-api-ms-smooth-group-settings-structure
- name: Medialive Api Ms Smooth H265 Packaging Type Structure
  property_count: 0
  slug: medialive-api-ms-smooth-h265-packaging-type-structure
- name: Medialive Api Ms Smooth Output Settings Structure
  property_count: 2
  slug: medialive-api-ms-smooth-output-settings-structure
- name: Medialive Api Multiplex Group Settings Structure
  property_count: 0
  slug: medialive-api-multiplex-group-settings-structure
- name: Medialive Api Multiplex Media Connect Output Destination Settings Structure
  property_count: 1
  slug: medialive-api-multiplex-media-connect-output-destination-settings-structure
- name: Medialive Api Multiplex Output Destination Structure
  property_count: 1
  slug: medialive-api-multiplex-output-destination-structure
- name: Medialive Api Multiplex Output Settings Structure
  property_count: 1
  slug: medialive-api-multiplex-output-settings-structure
- name: Medialive Api Multiplex Program Channel Destination Settings Structure
  property_count: 2
  slug: medialive-api-multiplex-program-channel-destination-settings-structure
- name: Medialive Api Multiplex Program Packet Identifiers Map Structure
  property_count: 13
  slug: medialive-api-multiplex-program-packet-identifiers-map-structure
- name: Medialive Api Multiplex Program Pipeline Detail Structure
  property_count: 2
  slug: medialive-api-multiplex-program-pipeline-detail-structure
- name: Medialive Api Multiplex Program Service Descriptor Structure
  property_count: 2
  slug: medialive-api-multiplex-program-service-descriptor-structure
- name: Medialive Api Multiplex Program Settings Structure
  property_count: 4
  slug: medialive-api-multiplex-program-settings-structure
- name: Medialive Api Multiplex Program Structure
  property_count: 5
  slug: medialive-api-multiplex-program-structure
- name: Medialive Api Multiplex Program Summary Structure
  property_count: 2
  slug: medialive-api-multiplex-program-summary-structure
- name: Medialive Api Multiplex Settings Structure
  property_count: 4
  slug: medialive-api-multiplex-settings-structure
- name: Medialive Api Multiplex Settings Summary Structure
  property_count: 1
  slug: medialive-api-multiplex-settings-summary-structure
- name: Medialive Api Multiplex State Structure
  property_count: 0
  slug: medialive-api-multiplex-state-structure
- name: Medialive Api Multiplex Statmux Video Settings Structure
  property_count: 3
  slug: medialive-api-multiplex-statmux-video-settings-structure
- name: Medialive Api Multiplex Structure
  property_count: 10
  slug: medialive-api-multiplex-structure
- name: Medialive Api Multiplex Summary Structure
  property_count: 9
  slug: medialive-api-multiplex-summary-structure
- name: Medialive Api Multiplex Video Settings Structure
  property_count: 2
  slug: medialive-api-multiplex-video-settings-structure
- name: Medialive Api Network Input Server Validation Structure
  property_count: 0
  slug: medialive-api-network-input-server-validation-structure
- name: Medialive Api Network Input Settings Structure
  property_count: 2
  slug: medialive-api-network-input-settings-structure
- name: Medialive Api Nielsen Cbet Structure
  property_count: 3
  slug: medialive-api-nielsen-cbet-structure
- name: Medialive Api Nielsen Configuration Structure
  property_count: 2
  slug: medialive-api-nielsen-configuration-structure
- name: Medialive Api Nielsen Naes Ii Nw Structure
  property_count: 3
  slug: medialive-api-nielsen-naes-ii-nw-structure
- name: Medialive Api Nielsen Pcm To Id3 Tagging State Structure
  property_count: 0
  slug: medialive-api-nielsen-pcm-to-id3-tagging-state-structure
- name: Medialive Api Nielsen Watermark Timezones Structure
  property_count: 0
  slug: medialive-api-nielsen-watermark-timezones-structure
- name: Medialive Api Nielsen Watermarks Cbet Stepaside Structure
  property_count: 0
  slug: medialive-api-nielsen-watermarks-cbet-stepaside-structure
- name: Medialive Api Nielsen Watermarks Distribution Types Structure
  property_count: 0
  slug: medialive-api-nielsen-watermarks-distribution-types-structure
- name: Medialive Api Nielsen Watermarks Settings Structure
  property_count: 3
  slug: medialive-api-nielsen-watermarks-settings-structure
- name: Medialive Api Offering Duration Units Structure
  property_count: 0
  slug: medialive-api-offering-duration-units-structure
- name: Medialive Api Offering Structure
  property_count: 11
  slug: medialive-api-offering-structure
- name: Medialive Api Offering Type Structure
  property_count: 0
  slug: medialive-api-offering-type-structure
- name: Medialive Api Output Destination Settings Structure
  property_count: 4
  slug: medialive-api-output-destination-settings-structure
- name: Medialive Api Output Destination Structure
  property_count: 4
  slug: medialive-api-output-destination-structure
- name: Medialive Api Output Group Settings Structure
  property_count: 8
  slug: medialive-api-output-group-settings-structure
- name: Medialive Api Output Group Structure
  property_count: 3
  slug: medialive-api-output-group-structure
- name: Medialive Api Output Location Ref Structure
  property_count: 1
  slug: medialive-api-output-location-ref-structure
- name: Medialive Api Output Settings Structure
  property_count: 8
  slug: medialive-api-output-settings-structure
- name: Medialive Api Output Structure
  property_count: 5
  slug: medialive-api-output-structure
- name: Medialive Api Pass Through Settings Structure
  property_count: 0
  slug: medialive-api-pass-through-settings-structure
- name: Medialive Api Pause State Schedule Action Settings Structure
  property_count: 1
  slug: medialive-api-pause-state-schedule-action-settings-structure
- name: Medialive Api Pipeline Detail Structure
  property_count: 5
  slug: medialive-api-pipeline-detail-structure
- name: Medialive Api Pipeline Id Structure
  property_count: 0
  slug: medialive-api-pipeline-id-structure
- name: Medialive Api Pipeline Pause State Settings Structure
  property_count: 1
  slug: medialive-api-pipeline-pause-state-settings-structure
- name: Medialive Api Preferred Channel Pipeline Structure
  property_count: 0
  slug: medialive-api-preferred-channel-pipeline-structure
- name: Medialive Api Purchase Offering Request Structure
  property_count: 6
  slug: medialive-api-purchase-offering-request-structure
- name: Medialive Api Purchase Offering Response Structure
  property_count: 1
  slug: medialive-api-purchase-offering-response-structure
- name: Medialive Api Raw Settings Structure
  property_count: 0
  slug: medialive-api-raw-settings-structure
- name: Medialive Api Reboot Input Device Force Structure
  property_count: 0
  slug: medialive-api-reboot-input-device-force-structure
- name: Medialive Api Reboot Input Device Request Structure
  property_count: 1
  slug: medialive-api-reboot-input-device-request-structure
- name: Medialive Api Reboot Input Device Response Structure
  property_count: 0
  slug: medialive-api-reboot-input-device-response-structure
- name: Medialive Api Rec601 Settings Structure
  property_count: 0
  slug: medialive-api-rec601-settings-structure
- name: Medialive Api Rec709 Settings Structure
  property_count: 0
  slug: medialive-api-rec709-settings-structure
- name: Medialive Api Reject Input Device Transfer Request Structure
  property_count: 0
  slug: medialive-api-reject-input-device-transfer-request-structure
- name: Medialive Api Reject Input Device Transfer Response Structure
  property_count: 0
  slug: medialive-api-reject-input-device-transfer-response-structure
- name: Medialive Api Remix Settings Structure
  property_count: 3
  slug: medialive-api-remix-settings-structure
- name: Medialive Api Renewal Settings Structure
  property_count: 2
  slug: medialive-api-renewal-settings-structure
- name: Medialive Api Reservation Automatic Renewal Structure
  property_count: 0
  slug: medialive-api-reservation-automatic-renewal-structure
- name: Medialive Api Reservation Codec Structure
  property_count: 0
  slug: medialive-api-reservation-codec-structure
- name: Medialive Api Reservation Maximum Bitrate Structure
  property_count: 0
  slug: medialive-api-reservation-maximum-bitrate-structure
- name: Medialive Api Reservation Maximum Framerate Structure
  property_count: 0
  slug: medialive-api-reservation-maximum-framerate-structure
- name: Medialive Api Reservation Resolution Structure
  property_count: 0
  slug: medialive-api-reservation-resolution-structure
- name: Medialive Api Reservation Resource Specification Structure
  property_count: 8
  slug: medialive-api-reservation-resource-specification-structure
- name: Medialive Api Reservation Resource Type Structure
  property_count: 0
  slug: medialive-api-reservation-resource-type-structure
- name: Medialive Api Reservation Special Feature Structure
  property_count: 0
  slug: medialive-api-reservation-special-feature-structure
- name: Medialive Api Reservation State Structure
  property_count: 0
  slug: medialive-api-reservation-state-structure
- name: Medialive Api Reservation Structure
  property_count: 19
  slug: medialive-api-reservation-structure
- name: Medialive Api Reservation Video Quality Structure
  property_count: 0
  slug: medialive-api-reservation-video-quality-structure
- name: Medialive Api Rtmp Ad Markers Structure
  property_count: 0
  slug: medialive-api-rtmp-ad-markers-structure
- name: Medialive Api Rtmp Cache Full Behavior Structure
  property_count: 0
  slug: medialive-api-rtmp-cache-full-behavior-structure
- name: Medialive Api Rtmp Caption Data Structure
  property_count: 0
  slug: medialive-api-rtmp-caption-data-structure
- name: Medialive Api Rtmp Caption Info Destination Settings Structure
  property_count: 0
  slug: medialive-api-rtmp-caption-info-destination-settings-structure
- name: Medialive Api Rtmp Group Settings Structure
  property_count: 7
  slug: medialive-api-rtmp-group-settings-structure
- name: Medialive Api Rtmp Output Certificate Mode Structure
  property_count: 0
  slug: medialive-api-rtmp-output-certificate-mode-structure
- name: Medialive Api Rtmp Output Settings Structure
  property_count: 4
  slug: medialive-api-rtmp-output-settings-structure
- name: Medialive Api S3 Canned Acl Structure
  property_count: 0
  slug: medialive-api-s3-canned-acl-structure
- name: Medialive Api Schedule Action Settings Structure
  property_count: 13
  slug: medialive-api-schedule-action-settings-structure
- name: Medialive Api Schedule Action Start Settings Structure
  property_count: 3
  slug: medialive-api-schedule-action-start-settings-structure
- name: Medialive Api Schedule Action Structure
  property_count: 3
  slug: medialive-api-schedule-action-structure
- name: Medialive Api Scte20 Convert608 To708 Structure
  property_count: 0
  slug: medialive-api-scte20-convert608-to708-structure
- name: Medialive Api Scte20 Plus Embedded Destination Settings Structure
  property_count: 0
  slug: medialive-api-scte20-plus-embedded-destination-settings-structure
- name: Medialive Api Scte20 Source Settings Structure
  property_count: 2
  slug: medialive-api-scte20-source-settings-structure
- name: Medialive Api Scte27 Destination Settings Structure
  property_count: 0
  slug: medialive-api-scte27-destination-settings-structure
- name: Medialive Api Scte27 Ocr Language Structure
  property_count: 0
  slug: medialive-api-scte27-ocr-language-structure
- name: Medialive Api Scte27 Source Settings Structure
  property_count: 2
  slug: medialive-api-scte27-source-settings-structure
- name: Medialive Api Scte35 Apos No Regional Blackout Behavior Structure
  property_count: 0
  slug: medialive-api-scte35-apos-no-regional-blackout-behavior-structure
- name: Medialive Api Scte35 Apos Web Delivery Allowed Behavior Structure
  property_count: 0
  slug: medialive-api-scte35-apos-web-delivery-allowed-behavior-structure
- name: Medialive Api Scte35 Archive Allowed Flag Structure
  property_count: 0
  slug: medialive-api-scte35-archive-allowed-flag-structure
- name: Medialive Api Scte35 Delivery Restrictions Structure
  property_count: 4
  slug: medialive-api-scte35-delivery-restrictions-structure
- name: Medialive Api Scte35 Descriptor Settings Structure
  property_count: 1
  slug: medialive-api-scte35-descriptor-settings-structure
- name: Medialive Api Scte35 Descriptor Structure
  property_count: 1
  slug: medialive-api-scte35-descriptor-structure
- name: Medialive Api Scte35 Device Restrictions Structure
  property_count: 0
  slug: medialive-api-scte35-device-restrictions-structure
- name: Medialive Api Scte35 Input Mode Structure
  property_count: 0
  slug: medialive-api-scte35-input-mode-structure
- name: Medialive Api Scte35 Input Schedule Action Settings Structure
  property_count: 2
  slug: medialive-api-scte35-input-schedule-action-settings-structure
- name: Medialive Api Scte35 No Regional Blackout Flag Structure
  property_count: 0
  slug: medialive-api-scte35-no-regional-blackout-flag-structure
- name: Medialive Api Scte35 Return To Network Schedule Action Settings Structure
  property_count: 1
  slug: medialive-api-scte35-return-to-network-schedule-action-settings-structure
- name: Medialive Api Scte35 Segmentation Cancel Indicator Structure
  property_count: 0
  slug: medialive-api-scte35-segmentation-cancel-indicator-structure
- name: Medialive Api Scte35 Segmentation Descriptor Structure
  property_count: 11
  slug: medialive-api-scte35-segmentation-descriptor-structure
- name: Medialive Api Scte35 Splice Insert No Regional Blackout Behavior Structure
  property_count: 0
  slug: medialive-api-scte35-splice-insert-no-regional-blackout-behavior-structure
- name: Medialive Api Scte35 Splice Insert Schedule Action Settings Structure
  property_count: 2
  slug: medialive-api-scte35-splice-insert-schedule-action-settings-structure
- name: Medialive Api Scte35 Splice Insert Structure
  property_count: 3
  slug: medialive-api-scte35-splice-insert-structure
- name: Medialive Api Scte35 Splice Insert Web Delivery Allowed Behavior Structure
  property_count: 0
  slug: medialive-api-scte35-splice-insert-web-delivery-allowed-behavior-structure
- name: Medialive Api Scte35 Time Signal Apos Structure
  property_count: 3
  slug: medialive-api-scte35-time-signal-apos-structure
- name: Medialive Api Scte35 Time Signal Schedule Action Settings Structure
  property_count: 1
  slug: medialive-api-scte35-time-signal-schedule-action-settings-structure
- name: Medialive Api Scte35 Web Delivery Allowed Flag Structure
  property_count: 0
  slug: medialive-api-scte35-web-delivery-allowed-flag-structure
- name: Medialive Api Smooth Group Audio Only Timecode Control Structure
  property_count: 0
  slug: medialive-api-smooth-group-audio-only-timecode-control-structure
- name: Medialive Api Smooth Group Certificate Mode Structure
  property_count: 0
  slug: medialive-api-smooth-group-certificate-mode-structure
- name: Medialive Api Smooth Group Event Id Mode Structure
  property_count: 0
  slug: medialive-api-smooth-group-event-id-mode-structure
- name: Medialive Api Smooth Group Event Stop Behavior Structure
  property_count: 0
  slug: medialive-api-smooth-group-event-stop-behavior-structure
- name: Medialive Api Smooth Group Segmentation Mode Structure
  property_count: 0
  slug: medialive-api-smooth-group-segmentation-mode-structure
- name: Medialive Api Smooth Group Sparse Track Type Structure
  property_count: 0
  slug: medialive-api-smooth-group-sparse-track-type-structure
- name: Medialive Api Smooth Group Stream Manifest Behavior Structure
  property_count: 0
  slug: medialive-api-smooth-group-stream-manifest-behavior-structure
- name: Medialive Api Smooth Group Timestamp Offset Mode Structure
  property_count: 0
  slug: medialive-api-smooth-group-timestamp-offset-mode-structure
- name: Medialive Api Smpte Tt Destination Settings Structure
  property_count: 0
  slug: medialive-api-smpte-tt-destination-settings-structure
- name: Medialive Api Smpte2038 Data Preference Structure
  property_count: 0
  slug: medialive-api-smpte2038-data-preference-structure
- name: Medialive Api Standard Hls Settings Structure
  property_count: 2
  slug: medialive-api-standard-hls-settings-structure
- name: Medialive Api Start Channel Request Structure
  property_count: 0
  slug: medialive-api-start-channel-request-structure
- name: Medialive Api Start Channel Response Structure
  property_count: 18
  slug: medialive-api-start-channel-response-structure
- name: Medialive Api Start Input Device Maintenance Window Request Structure
  property_count: 0
  slug: medialive-api-start-input-device-maintenance-window-request-structure
- name: Medialive Api Start Input Device Maintenance Window Response Structure
  property_count: 0
  slug: medialive-api-start-input-device-maintenance-window-response-structure
- name: Medialive Api Start Multiplex Request Structure
  property_count: 0
  slug: medialive-api-start-multiplex-request-structure
- name: Medialive Api Start Multiplex Response Structure
  property_count: 10
  slug: medialive-api-start-multiplex-response-structure
- name: Medialive Api Start Timecode Structure
  property_count: 1
  slug: medialive-api-start-timecode-structure
- name: Medialive Api Static Image Activate Schedule Action Settings Structure
  property_count: 10
  slug: medialive-api-static-image-activate-schedule-action-settings-structure
- name: Medialive Api Static Image Deactivate Schedule Action Settings Structure
  property_count: 2
  slug: medialive-api-static-image-deactivate-schedule-action-settings-structure
- name: Medialive Api Static Key Settings Structure
  property_count: 2
  slug: medialive-api-static-key-settings-structure
- name: Medialive Api Stop Channel Request Structure
  property_count: 0
  slug: medialive-api-stop-channel-request-structure
- name: Medialive Api Stop Channel Response Structure
  property_count: 18
  slug: medialive-api-stop-channel-response-structure
- name: Medialive Api Stop Multiplex Request Structure
  property_count: 0
  slug: medialive-api-stop-multiplex-request-structure
- name: Medialive Api Stop Multiplex Response Structure
  property_count: 10
  slug: medialive-api-stop-multiplex-response-structure
- name: Medialive Api Stop Timecode Structure
  property_count: 2
  slug: medialive-api-stop-timecode-structure
- name: Medialive Api Tags Structure
  property_count: 0
  slug: medialive-api-tags-structure
- name: Medialive Api Teletext Destination Settings Structure
  property_count: 0
  slug: medialive-api-teletext-destination-settings-structure
- name: Medialive Api Teletext Source Settings Structure
  property_count: 2
  slug: medialive-api-teletext-source-settings-structure
- name: Medialive Api Temporal Filter Post Filter Sharpening Structure
  property_count: 0
  slug: medialive-api-temporal-filter-post-filter-sharpening-structure
- name: Medialive Api Temporal Filter Settings Structure
  property_count: 2
  slug: medialive-api-temporal-filter-settings-structure
- name: Medialive Api Temporal Filter Strength Structure
  property_count: 0
  slug: medialive-api-temporal-filter-strength-structure
- name: Medialive Api Timecode Burnin Font Size Structure
  property_count: 0
  slug: medialive-api-timecode-burnin-font-size-structure
- name: Medialive Api Timecode Burnin Position Structure
  property_count: 0
  slug: medialive-api-timecode-burnin-position-structure
- name: Medialive Api Timecode Burnin Settings Structure
  property_count: 3
  slug: medialive-api-timecode-burnin-settings-structure
- name: Medialive Api Timecode Config Source Structure
  property_count: 0
  slug: medialive-api-timecode-config-source-structure
- name: Medialive Api Timecode Config Structure
  property_count: 2
  slug: medialive-api-timecode-config-structure
- name: Medialive Api Transfer Input Device Request Structure
  property_count: 3
  slug: medialive-api-transfer-input-device-request-structure
- name: Medialive Api Transfer Input Device Response Structure
  property_count: 0
  slug: medialive-api-transfer-input-device-response-structure
- name: Medialive Api Transferring Input Device Summary Structure
  property_count: 4
  slug: medialive-api-transferring-input-device-summary-structure
- name: Medialive Api Ttml Destination Settings Structure
  property_count: 1
  slug: medialive-api-ttml-destination-settings-structure
- name: Medialive Api Ttml Destination Style Control Structure
  property_count: 0
  slug: medialive-api-ttml-destination-style-control-structure
- name: Medialive Api Udp Container Settings Structure
  property_count: 1
  slug: medialive-api-udp-container-settings-structure
- name: Medialive Api Udp Group Settings Structure
  property_count: 3
  slug: medialive-api-udp-group-settings-structure
- name: Medialive Api Udp Output Settings Structure
  property_count: 4
  slug: medialive-api-udp-output-settings-structure
- name: Medialive Api Udp Timed Metadata Id3 Frame Structure
  property_count: 0
  slug: medialive-api-udp-timed-metadata-id3-frame-structure
- name: Medialive Api Update Channel Class Request Structure
  property_count: 2
  slug: medialive-api-update-channel-class-request-structure
- name: Medialive Api Update Channel Class Response Structure
  property_count: 1
  slug: medialive-api-update-channel-class-response-structure
- name: Medialive Api Update Channel Request Structure
  property_count: 9
  slug: medialive-api-update-channel-request-structure
- name: Medialive Api Update Channel Response Structure
  property_count: 1
  slug: medialive-api-update-channel-response-structure
- name: Medialive Api Update Input Device Request Structure
  property_count: 3
  slug: medialive-api-update-input-device-request-structure
- name: Medialive Api Update Input Device Response Structure
  property_count: 13
  slug: medialive-api-update-input-device-response-structure
- name: Medialive Api Update Input Request Structure
  property_count: 7
  slug: medialive-api-update-input-request-structure
- name: Medialive Api Update Input Response Structure
  property_count: 1
  slug: medialive-api-update-input-response-structure
- name: Medialive Api Update Input Security Group Request Structure
  property_count: 2
  slug: medialive-api-update-input-security-group-request-structure
- name: Medialive Api Update Input Security Group Response Structure
  property_count: 1
  slug: medialive-api-update-input-security-group-response-structure
- name: Medialive Api Update Multiplex Program Request Structure
  property_count: 1
  slug: medialive-api-update-multiplex-program-request-structure
- name: Medialive Api Update Multiplex Program Response Structure
  property_count: 1
  slug: medialive-api-update-multiplex-program-response-structure
- name: Medialive Api Update Multiplex Request Structure
  property_count: 2
  slug: medialive-api-update-multiplex-request-structure
- name: Medialive Api Update Multiplex Response Structure
  property_count: 1
  slug: medialive-api-update-multiplex-response-structure
- name: Medialive Api Update Reservation Request Structure
  property_count: 2
  slug: medialive-api-update-reservation-request-structure
- name: Medialive Api Update Reservation Response Structure
  property_count: 1
  slug: medialive-api-update-reservation-response-structure
- name: Medialive Api Video Black Failover Settings Structure
  property_count: 2
  slug: medialive-api-video-black-failover-settings-structure
- name: Medialive Api Video Codec Settings Structure
  property_count: 4
  slug: medialive-api-video-codec-settings-structure
- name: Medialive Api Video Description Respond To Afd Structure
  property_count: 0
  slug: medialive-api-video-description-respond-to-afd-structure
- name: Medialive Api Video Description Scaling Behavior Structure
  property_count: 0
  slug: medialive-api-video-description-scaling-behavior-structure
- name: Medialive Api Video Description Structure
  property_count: 7
  slug: medialive-api-video-description-structure
- name: Medialive Api Video Selector Color Space Settings Structure
  property_count: 1
  slug: medialive-api-video-selector-color-space-settings-structure
- name: Medialive Api Video Selector Color Space Structure
  property_count: 0
  slug: medialive-api-video-selector-color-space-structure
- name: Medialive Api Video Selector Color Space Usage Structure
  property_count: 0
  slug: medialive-api-video-selector-color-space-usage-structure
- name: Medialive Api Video Selector Pid Structure
  property_count: 1
  slug: medialive-api-video-selector-pid-structure
- name: Medialive Api Video Selector Program Id Structure
  property_count: 1
  slug: medialive-api-video-selector-program-id-structure
- name: Medialive Api Video Selector Settings Structure
  property_count: 2
  slug: medialive-api-video-selector-settings-structure
- name: Medialive Api Video Selector Structure
  property_count: 4
  slug: medialive-api-video-selector-structure
- name: Medialive Api Vpc Output Settings Description Structure
  property_count: 4
  slug: medialive-api-vpc-output-settings-description-structure
- name: Medialive Api Vpc Output Settings Structure
  property_count: 3
  slug: medialive-api-vpc-output-settings-structure
- name: Medialive Api Wav Coding Mode Structure
  property_count: 0
  slug: medialive-api-wav-coding-mode-structure
- name: Medialive Api Wav Settings Structure
  property_count: 3
  slug: medialive-api-wav-settings-structure
- name: Medialive Api Webvtt Destination Settings Structure
  property_count: 1
  slug: medialive-api-webvtt-destination-settings-structure
- name: Medialive Api Webvtt Destination Style Control Structure
  property_count: 0
  slug: medialive-api-webvtt-destination-style-control-structure
jsonld:
- class_count: 622
  name: Amazon Medialive Medialive Api Context
  property_count: 675
  slug: amazon-medialive-medialive-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MediaLive
nav: Providers
network: true
overview: 'Amazon MediaLive publishes 1 API on the [APIs.io](https://apis.io/) network: Prod API. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MediaLive catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MediaLive''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Medialive Plans Pricing
  plan_count: 3
  slug: amazon-medialive-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Amazon Medialive Rate Limits
  slug: amazon-medialive-rate-limits
rules:
- name: Amazon MediaLive API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-medialive-jsonschema-spectral-rules
- name: Amazon MediaLive API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 12
  slug: amazon-medialive-spectral-rules
score:
  band: strong
  composite: 60.9
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 72.1
    developer_ergonomics: 45.7
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-medialive/refs/heads/main/screenshots/amazon-medialive-2026-06-20T171741.png
security:
- kind: authentication
  name: Amazon Medialive Authentication
  slug: amazon-medialive-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Medialive Domain Security
  slug: amazon-medialive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Medialive Vulnerability Disclosure
  slug: amazon-medialive-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Medialive Trust Center
  slug: amazon-medialive-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-medialive
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Encode and deliver live TV channels with broadcast-grade quality.
  name: Live Television Broadcast
- description: Handle large-scale live sports events with redundant pipelines.
  name: Live Sports Streaming
- description: Create live news channel workflows with multi-source input switching.
  name: Live News Production
- description: Stream virtual conferences, concerts, and entertainment events.
  name: Virtual Events
website: https://aws.amazon.com/medialive/
---
