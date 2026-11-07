---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 1
  name: Bandwidth Agentic Access
  operation_count: 62
  slug: bandwidth-agentic-access
  summary_line: 62 operations · 31 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Create, retrieve, and manage phone calls. Supports outbound call creation, call state queries, and in-progress call modifications using BXML or redirect URLs.
  name: Bandwidth Calls API
  slug: bandwidth-calls-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Create and manage multi-party conference calls. Supports adding and removing members, muting, holding, and playing audio to conferences.
  name: Bandwidth Conferences API
  slug: bandwidth-conferences-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Configure notification recipients who receive alerts when 911 calls are made from your endpoints.
  name: Bandwidth Emergency Notification Recipients API
  slug: bandwidth-emergency-notification-recipients-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Manage 911 endpoints that represent end users of your service. Endpoints are identified by Alternate End User IDs (AEUIs) and are associated with locations for emergency routing.
  name: Bandwidth Endpoints API
  slug: bandwidth-endpoints-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Provision and manage physical locations (addresses) for 911 emergency services routing. Locations are validated against the Master Street Address Guide (MSAG) for accuracy.
  name: Bandwidth Locations API
  slug: bandwidth-locations-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Upload, retrieve, and manage media files for use in MMS messages. Supports files up to 3.75 MB with 48-hour retention.
  name: Bandwidth Media API
  slug: bandwidth-media-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Send and retrieve SMS and MMS messages. Supports single and group messaging, delivery receipts, and message history queries.
  name: Bandwidth Messages API
  slug: bandwidth-messages-api
- baseURL: https://voice.bandwidth.com/api/v2
  baseurl_source: declared
  description: Manage call recordings including retrieval of recording metadata, audio files, and transcription of recorded audio content.
  name: Bandwidth Recordings API
  slug: bandwidth-recordings-api
artifact_total: 272
asyncapis:
- description: Bandwidth Messaging API sends webhooks to your application for real-time message delivery notifications and inbound message alerts. Callbacks are sent via HTTP POST to the callback URL configured on t
  name: Bandwidth Messaging Events
  slug: bandwidth-messaging-events-asyncapi
- description: Bandwidth Voice API sends webhooks (BXML callbacks) to your application for real-time call event notifications. These webhooks inform your application of call state changes and request BXML instructio
  name: Bandwidth Voice Events
  slug: bandwidth-voice-events-asyncapi
- description: ''
  name: Bandwidth Webhooks
  slug: bandwidth-webhooks
collections:
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers API
  slug: postman-bandwidth-available-numbers-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Calls API
  slug: postman-bandwidth-calls-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Conferences API
  slug: postman-bandwidth-conferences-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Disconnects API
  slug: postman-bandwidth-disconnects-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Emergency Notification Recipients API
  slug: postman-bandwidth-emergency-notification-recipients-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Endpoints API
  slug: postman-bandwidth-endpoints-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Locations API
  slug: postman-bandwidth-locations-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Media API
  slug: postman-bandwidth-media-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Messages API
  slug: postman-bandwidth-messages-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers MFA API
  slug: postman-bandwidth-mfa-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Number Features API
  slug: postman-bandwidth-number-features-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Orders API
  slug: postman-bandwidth-orders-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Phone Numbers API
  slug: postman-bandwidth-phone-numbers-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Port-Ins API
  slug: postman-bandwidth-port-ins-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Recordings API
  slug: postman-bandwidth-recordings-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers SIP Peers API
  slug: postman-bandwidth-sip-peers-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Sites API
  slug: postman-bandwidth-sites-api
- collection_type: postman
  name: Bandwidth Emergency Calling Available Numbers Toll-Free Verification API
  slug: postman-bandwidth-toll-free-verification-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers API
  slug: open-bandwidth-available-numbers-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Calls API
  slug: open-bandwidth-calls-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Conferences API
  slug: open-bandwidth-conferences-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Disconnects API
  slug: open-bandwidth-disconnects-api
- collection_type: open
  name: Bandwidth Emergency Calling API
  slug: open-bandwidth-emergency-calling-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Emergency Notification Recipients API
  slug: open-bandwidth-emergency-notification-recipients-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Endpoints API
  slug: open-bandwidth-endpoints-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Locations API
  slug: open-bandwidth-locations-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Media API
  slug: open-bandwidth-media-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Messages API
  slug: open-bandwidth-messages-api
- collection_type: open
  name: Bandwidth Messaging API
  slug: open-bandwidth-messaging-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers MFA API
  slug: open-bandwidth-mfa-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Number Features API
  slug: open-bandwidth-number-features-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Orders API
  slug: open-bandwidth-orders-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Phone Numbers API
  slug: open-bandwidth-phone-numbers-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Port-Ins API
  slug: open-bandwidth-port-ins-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Recordings API
  slug: open-bandwidth-recordings-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers SIP Peers API
  slug: open-bandwidth-sip-peers-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Sites API
  slug: open-bandwidth-sites-api
- collection_type: open
  name: Bandwidth Emergency Calling Available Numbers Toll-Free Verification API
  slug: open-bandwidth-toll-free-verification-api
- collection_type: open
  name: Bandwidth Voice API
  slug: open-bandwidth-voice-api
common:
- group: commercial
  href: https://artifacts.apis.io/bandwidth/finops/bandwidth-finops.yml
  title: ''
  type: FinOps
  url: finops/bandwidth-finops.yml
- group: operate
  href: https://artifacts.apis.io/bandwidth/rate-limits/bandwidth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bandwidth-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bandwidth/plans/bandwidth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bandwidth-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/rules/bandwidth-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/bandwidth-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/rules/bandwidth-rules.yml
  title: ''
  type: Spectral
  url: rules/bandwidth-rules.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/rules/bandwidth-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/bandwidth-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/rules/bandwidth-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/bandwidth-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/vocabulary/bandwidth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bandwidth-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bandwidth/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/asyncapi/bandwidth-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bandwidth-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/data-model/bandwidth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bandwidth-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bandwidth.com/security/
- group: design
  href: https://artifacts.apis.io/bandwidth/errors/bandwidth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bandwidth-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/conformance/bandwidth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bandwidth-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bandwidth/llms/bandwidth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bandwidth-llms.txt
- group: auth
  href: https://artifacts.apis.io/bandwidth/well-known/bandwidth-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bandwidth-status-security.txt
- group: auth
  href: https://artifacts.apis.io/bandwidth/well-known/bandwidth-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bandwidth-community-security.txt
- group: agent
  href: https://artifacts.apis.io/bandwidth/well-known/bandwidth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bandwidth-well-known.yml
- group: other
  href: https://artifacts.apis.io/bandwidth/hosts/bandwidth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bandwidth-hosts.yml
- group: other
  href: https://artifacts.apis.io/bandwidth/vendors/bandwidth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bandwidth-vendors.yml
- group: build
  href: https://artifacts.apis.io/bandwidth/packages/bandwidth-packages.yml
  title: ''
  type: SDKs
  url: packages/bandwidth-packages.yml
- group: build
  href: https://artifacts.apis.io/bandwidth/packages/bandwidth-packages.yml
  title: ''
  type: Packages
  url: packages/bandwidth-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.bandwidth.com/glossary/webhook/
- group: auth
  title: ''
  type: Security
  url: https://www.bandwidth.com/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bandwidth.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bandwidth.com/newsroom/
- group: start
  title: ''
  type: Login
  url: https://community.bandwidth.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.bandwidth.com/leadership/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bandwidth.com/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.bandwidth.com/docs/voice/programmable-voice/build-free-trial
- group: other
  href: https://artifacts.apis.io/bandwidth/capabilities/bandwidth-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bandwidth-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bandwidth/overview
- group: agent
  href: https://artifacts.apis.io/bandwidth/agentic-access/bandwidth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bandwidth-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bandwidth/security/bandwidth-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bandwidth-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bandwidth/security/bandwidth-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bandwidth-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bandwidth/security/bandwidth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bandwidth-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bandwidth/authentication/bandwidth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bandwidth-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bandwidth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bandwidth-inc
- group: company
  title: ''
  type: Website
  url: https://www.bandwidth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bandwidth.com/
- group: start
  title: ''
  type: Signup
  url: https://app.bandwidth.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.bandwidth.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bandwidth.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bandwidth.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bandwidth.com/
- group: operate
  title: ''
  type: Support
  url: https://support.bandwidth.com/
- group: design
  href: https://artifacts.apis.io/bandwidth/rules/bandwidth-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/bandwidth-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bandwidth/vocabulary/bandwidth-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/bandwidth-vocabulary.yaml
- group: docs
  href: https://artifacts.apis.io/bandwidth/json-schema/bandwidth-call-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/bandwidth-call-schema.json
- group: docs
  href: https://artifacts.apis.io/bandwidth/json-schema/bandwidth-message-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/bandwidth-message-schema.json
- group: docs
  href: https://artifacts.apis.io/bandwidth/json-schema/bandwidth-phone-number-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/bandwidth-phone-number-schema.json
- group: design
  href: https://artifacts.apis.io/bandwidth/json-ld/bandwidth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bandwidth-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.bandwidth.com/llms.txt
created: '2024-01-01'
description: Bandwidth is a leading cloud-based communications platform providing voice, messaging, emergency calling, phone number management, multi-factor authentication, and toll-free verification APIs. Built on Bandwidth's own Tier 1 network, the platform delivers enterprise-grade reliability for CPaaS applications.
examples:
- key_count: 19
  name: Bandwidth Call Example
  slug: bandwidth-call-example
- key_count: 13
  name: Bandwidth Message Example
  slug: bandwidth-message-example
- key_count: 9
  name: Bandwidth Phone Number Example
  slug: bandwidth-phone-number-example
- key_count: 6
  name: Emergency Calling Endpoint Example
  slug: emergency-calling-endpoint-example
- key_count: 2
  name: Emergency Calling Endpoint List Response Example
  slug: emergency-calling-endpoint-list-response-example
- key_count: 6
  name: Emergency Calling Location Example
  slug: emergency-calling-location-example
- key_count: 2
  name: Emergency Calling Location List Response Example
  slug: emergency-calling-location-list-response-example
- key_count: 4
  name: Emergency Calling Notification Recipient Example
  slug: emergency-calling-notification-recipient-example
- key_count: 1
  name: Emergency Calling Notification Recipient List Response Example
  slug: emergency-calling-notification-recipient-list-response-example
- key_count: 8
  name: Messaging Create Message Request Example
  slug: messaging-create-message-request-example
- key_count: 3
  name: Messaging Error Example
  slug: messaging-error-example
- key_count: 4
  name: Messaging Media Example
  slug: messaging-media-example
- key_count: 12
  name: Messaging Message Example
  slug: messaging-message-example
- key_count: 3
  name: Messaging Message List Example
  slug: messaging-message-list-example
- key_count: 2
  name: Mfa Error Example
  slug: mfa-error-example
- key_count: 7
  name: Mfa Mfa Messaging Request Example
  slug: mfa-mfa-messaging-request-example
- key_count: 1
  name: Mfa Mfa Messaging Response Example
  slug: mfa-mfa-messaging-response-example
- key_count: 4
  name: Mfa Mfa Verify Request Example
  slug: mfa-mfa-verify-request-example
- key_count: 1
  name: Mfa Mfa Verify Response Example
  slug: mfa-mfa-verify-response-example
- key_count: 7
  name: Mfa Mfa Voice Request Example
  slug: mfa-mfa-voice-request-example
- key_count: 1
  name: Mfa Mfa Voice Response Example
  slug: mfa-mfa-voice-response-example
- key_count: 6
  name: Phone Numbers Address Example
  slug: phone-numbers-address-example
- key_count: 5
  name: Phone Numbers Available Number Example
  slug: phone-numbers-available-number-example
- key_count: 2
  name: Phone Numbers Available Numbers Response Example
  slug: phone-numbers-available-numbers-response-example
- key_count: 2
  name: Phone Numbers Disconnect Request Example
  slug: phone-numbers-disconnect-request-example
- key_count: 2
  name: Phone Numbers Disconnect Response Example
  slug: phone-numbers-disconnect-response-example
- key_count: 2
  name: Phone Numbers Feature Order Request Example
  slug: phone-numbers-feature-order-request-example
- key_count: 2
  name: Phone Numbers Order List Response Example
  slug: phone-numbers-order-list-response-example
- key_count: 4
  name: Phone Numbers Order Request Example
  slug: phone-numbers-order-request-example
- key_count: 6
  name: Phone Numbers Order Response Example
  slug: phone-numbers-order-response-example
- key_count: 8
  name: Phone Numbers Phone Number Example
  slug: phone-numbers-phone-number-example
- key_count: 2
  name: Phone Numbers Phone Number List Response Example
  slug: phone-numbers-phone-number-list-response-example
- key_count: 2
  name: Phone Numbers Port In List Response Example
  slug: phone-numbers-port-in-list-response-example
- key_count: 7
  name: Phone Numbers Port In Request Example
  slug: phone-numbers-port-in-request-example
- key_count: 4
  name: Phone Numbers Port In Response Example
  slug: phone-numbers-port-in-response-example
- key_count: 4
  name: Phone Numbers Sip Peer Example
  slug: phone-numbers-sip-peer-example
- key_count: 1
  name: Phone Numbers Sip Peer List Response Example
  slug: phone-numbers-sip-peer-list-response-example
- key_count: 4
  name: Phone Numbers Site Example
  slug: phone-numbers-site-example
- key_count: 1
  name: Phone Numbers Site List Response Example
  slug: phone-numbers-site-list-response-example
- key_count: 2
  name: Toll Free Verification Error Example
  slug: toll-free-verification-error-example
- key_count: 8
  name: Toll Free Verification Verification Example
  slug: toll-free-verification-verification-example
- key_count: 2
  name: Toll Free Verification Verification List Response Example
  slug: toll-free-verification-verification-list-response-example
- key_count: 11
  name: Toll Free Verification Verification Request Example
  slug: toll-free-verification-verification-request-example
- key_count: 13
  name: Voice Call Example
  slug: voice-call-example
- key_count: 6
  name: Voice Conference Example
  slug: voice-conference-example
- key_count: 6
  name: Voice Conference Member Example
  slug: voice-conference-member-example
- key_count: 12
  name: Voice Create Call Request Example
  slug: voice-create-call-request-example
- key_count: 3
  name: Voice Error Example
  slug: voice-error-example
- key_count: 12
  name: Voice Recording Example
  slug: voice-recording-example
- key_count: 4
  name: Voice Transcription Example
  slug: voice-transcription-example
- key_count: 3
  name: Voice Transcription Request Example
  slug: voice-transcription-request-example
- key_count: 6
  name: Voice Update Call Request Example
  slug: voice-update-call-request-example
- key_count: 3
  name: Voice Update Conference Member Request Example
  slug: voice-update-conference-member-request-example
- key_count: 4
  name: Voice Update Conference Request Example
  slug: voice-update-conference-request-example
features:
- 'SMS 10DLC outbound: $0.004/message'
- 'MMS 10DLC outbound: $0.015/message'
- 'SMS Short Code: $0.008/msg out, MMS Short Code: $0.020'
- 'SMS Toll-free: $0.007/msg out'
- 'Voice US Local: $0.010 outbound, $0.0055 inbound per minute'
- Tier 1 carrier with own network and interconnects
- REST API for Messaging and Voice
- Default 10 messages/sec and 10 calls/sec
- OAuth + API keys
- Webhooks for delivery receipts and inbound events
- BXML for voice IVR scripting
- Verify API for OTP
- Number Management API
- Phone Number Insight (line-type lookup)
- Iris API for porting and management
- Enterprise committed-use volume contracts
finops:
- has_sources: true
  method: derived
  name: Bandwidth Finops
  primary_unit: minute
  service_category: ''
  slug: bandwidth-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bandwidth.png
json_schemas:
- name: Bandwidth Call
  property_count: 19
  slug: bandwidth-call
- name: Conference
  property_count: 6
  slug: bandwidth-conference
- name: CreateCallRequest
  property_count: 12
  slug: bandwidth-create-call-request
- name: CreateMessageRequest
  property_count: 8
  slug: bandwidth-create-message-request
- name: EndpointListResponse
  property_count: 2
  slug: bandwidth-endpoint-list-response
- name: Endpoint
  property_count: 6
  slug: bandwidth-endpoint
- name: LocationListResponse
  property_count: 2
  slug: bandwidth-location-list-response
- name: Location
  property_count: 6
  slug: bandwidth-location
- name: Media
  property_count: 4
  slug: bandwidth-media
- name: MessageList
  property_count: 3
  slug: bandwidth-message-list
- name: Bandwidth Message
  property_count: 13
  slug: bandwidth-message
- name: NotificationRecipientListResponse
  property_count: 1
  slug: bandwidth-notification-recipient-list-response
- name: NotificationRecipient
  property_count: 4
  slug: bandwidth-notification-recipient
- name: Bandwidth Phone Number
  property_count: 9
  slug: bandwidth-phone-number
- name: Recording
  property_count: 12
  slug: bandwidth-recording
- name: TranscriptionRequest
  property_count: 3
  slug: bandwidth-transcription-request
- name: Transcription
  property_count: 4
  slug: bandwidth-transcription
- name: UpdateCallRequest
  property_count: 6
  slug: bandwidth-update-call-request
- name: UpdateConferenceMemberRequest
  property_count: 3
  slug: bandwidth-update-conference-member-request
- name: UpdateConferenceRequest
  property_count: 4
  slug: bandwidth-update-conference-request
- name: EndpointListResponse
  property_count: 2
  slug: emergency-calling-endpoint-list-response
- name: Endpoint
  property_count: 6
  slug: emergency-calling-endpoint
- name: LocationListResponse
  property_count: 2
  slug: emergency-calling-location-list-response
- name: Location
  property_count: 6
  slug: emergency-calling-location
- name: NotificationRecipientListResponse
  property_count: 1
  slug: emergency-calling-notification-recipient-list-response
- name: NotificationRecipient
  property_count: 4
  slug: emergency-calling-notification-recipient
- name: CreateMessageRequest
  property_count: 8
  slug: messaging-create-message-request
- name: Error
  property_count: 3
  slug: messaging-error
- name: Media
  property_count: 4
  slug: messaging-media
- name: MessageList
  property_count: 3
  slug: messaging-message-list
- name: Message
  property_count: 12
  slug: messaging-message
- name: Error
  property_count: 2
  slug: mfa-error
- name: MfaMessagingRequest
  property_count: 7
  slug: mfa-mfa-messaging-request
- name: MfaMessagingResponse
  property_count: 1
  slug: mfa-mfa-messaging-response
- name: MfaVerifyRequest
  property_count: 4
  slug: mfa-mfa-verify-request
- name: MfaVerifyResponse
  property_count: 1
  slug: mfa-mfa-verify-response
- name: MfaVoiceRequest
  property_count: 7
  slug: mfa-mfa-voice-request
- name: MfaVoiceResponse
  property_count: 1
  slug: mfa-mfa-voice-response
- name: Address
  property_count: 6
  slug: phone-numbers-address
- name: AvailableNumber
  property_count: 5
  slug: phone-numbers-available-number
- name: AvailableNumbersResponse
  property_count: 2
  slug: phone-numbers-available-numbers-response
- name: DisconnectRequest
  property_count: 2
  slug: phone-numbers-disconnect-request
- name: DisconnectResponse
  property_count: 2
  slug: phone-numbers-disconnect-response
- name: FeatureOrderRequest
  property_count: 2
  slug: phone-numbers-feature-order-request
- name: OrderListResponse
  property_count: 2
  slug: phone-numbers-order-list-response
- name: OrderRequest
  property_count: 4
  slug: phone-numbers-order-request
- name: OrderResponse
  property_count: 6
  slug: phone-numbers-order-response
- name: PhoneNumberListResponse
  property_count: 2
  slug: phone-numbers-phone-number-list-response
- name: PhoneNumber
  property_count: 8
  slug: phone-numbers-phone-number
- name: PortInListResponse
  property_count: 2
  slug: phone-numbers-port-in-list-response
- name: PortInRequest
  property_count: 7
  slug: phone-numbers-port-in-request
- name: PortInResponse
  property_count: 4
  slug: phone-numbers-port-in-response
- name: SipPeerListResponse
  property_count: 1
  slug: phone-numbers-sip-peer-list-response
- name: SipPeer
  property_count: 4
  slug: phone-numbers-sip-peer
- name: SiteListResponse
  property_count: 1
  slug: phone-numbers-site-list-response
- name: Site
  property_count: 4
  slug: phone-numbers-site
- name: Error
  property_count: 2
  slug: toll-free-verification-error
- name: VerificationListResponse
  property_count: 2
  slug: toll-free-verification-verification-list-response
- name: VerificationRequest
  property_count: 11
  slug: toll-free-verification-verification-request
- name: Verification
  property_count: 8
  slug: toll-free-verification-verification
- name: Call
  property_count: 13
  slug: voice-call
- name: ConferenceMember
  property_count: 6
  slug: voice-conference-member
- name: Conference
  property_count: 6
  slug: voice-conference
- name: CreateCallRequest
  property_count: 12
  slug: voice-create-call-request
- name: Error
  property_count: 3
  slug: voice-error
- name: Recording
  property_count: 12
  slug: voice-recording
- name: TranscriptionRequest
  property_count: 3
  slug: voice-transcription-request
- name: Transcription
  property_count: 4
  slug: voice-transcription
- name: UpdateCallRequest
  property_count: 6
  slug: voice-update-call-request
- name: UpdateConferenceMemberRequest
  property_count: 3
  slug: voice-update-conference-member-request
- name: UpdateConferenceRequest
  property_count: 4
  slug: voice-update-conference-request
json_structures:
- name: Bandwidth Call Structure
  property_count: 19
  slug: bandwidth-call-structure
- name: Bandwidth Message Structure
  property_count: 13
  slug: bandwidth-message-structure
- name: Bandwidth Phone Number Structure
  property_count: 9
  slug: bandwidth-phone-number-structure
- name: Emergency Calling Endpoint List Response Structure
  property_count: 2
  slug: emergency-calling-endpoint-list-response-structure
- name: Emergency Calling Endpoint Structure
  property_count: 6
  slug: emergency-calling-endpoint-structure
- name: Emergency Calling Location List Response Structure
  property_count: 2
  slug: emergency-calling-location-list-response-structure
- name: Emergency Calling Location Structure
  property_count: 6
  slug: emergency-calling-location-structure
- name: Emergency Calling Notification Recipient List Response Structure
  property_count: 1
  slug: emergency-calling-notification-recipient-list-response-structure
- name: Emergency Calling Notification Recipient Structure
  property_count: 4
  slug: emergency-calling-notification-recipient-structure
- name: Messaging Create Message Request Structure
  property_count: 8
  slug: messaging-create-message-request-structure
- name: Messaging Error Structure
  property_count: 3
  slug: messaging-error-structure
- name: Messaging Media Structure
  property_count: 4
  slug: messaging-media-structure
- name: Messaging Message List Structure
  property_count: 3
  slug: messaging-message-list-structure
- name: Messaging Message Structure
  property_count: 12
  slug: messaging-message-structure
- name: Mfa Error Structure
  property_count: 2
  slug: mfa-error-structure
- name: Mfa Mfa Messaging Request Structure
  property_count: 7
  slug: mfa-mfa-messaging-request-structure
- name: Mfa Mfa Messaging Response Structure
  property_count: 1
  slug: mfa-mfa-messaging-response-structure
- name: Mfa Mfa Verify Request Structure
  property_count: 4
  slug: mfa-mfa-verify-request-structure
- name: Mfa Mfa Verify Response Structure
  property_count: 1
  slug: mfa-mfa-verify-response-structure
- name: Mfa Mfa Voice Request Structure
  property_count: 7
  slug: mfa-mfa-voice-request-structure
- name: Mfa Mfa Voice Response Structure
  property_count: 1
  slug: mfa-mfa-voice-response-structure
- name: Phone Numbers Address Structure
  property_count: 6
  slug: phone-numbers-address-structure
- name: Phone Numbers Available Number Structure
  property_count: 5
  slug: phone-numbers-available-number-structure
- name: Phone Numbers Available Numbers Response Structure
  property_count: 2
  slug: phone-numbers-available-numbers-response-structure
- name: Phone Numbers Disconnect Request Structure
  property_count: 2
  slug: phone-numbers-disconnect-request-structure
- name: Phone Numbers Disconnect Response Structure
  property_count: 2
  slug: phone-numbers-disconnect-response-structure
- name: Phone Numbers Feature Order Request Structure
  property_count: 2
  slug: phone-numbers-feature-order-request-structure
- name: Phone Numbers Order List Response Structure
  property_count: 2
  slug: phone-numbers-order-list-response-structure
- name: Phone Numbers Order Request Structure
  property_count: 4
  slug: phone-numbers-order-request-structure
- name: Phone Numbers Order Response Structure
  property_count: 6
  slug: phone-numbers-order-response-structure
- name: Phone Numbers Phone Number List Response Structure
  property_count: 2
  slug: phone-numbers-phone-number-list-response-structure
- name: Phone Numbers Phone Number Structure
  property_count: 8
  slug: phone-numbers-phone-number-structure
- name: Phone Numbers Port In List Response Structure
  property_count: 2
  slug: phone-numbers-port-in-list-response-structure
- name: Phone Numbers Port In Request Structure
  property_count: 7
  slug: phone-numbers-port-in-request-structure
- name: Phone Numbers Port In Response Structure
  property_count: 4
  slug: phone-numbers-port-in-response-structure
- name: Phone Numbers Sip Peer List Response Structure
  property_count: 1
  slug: phone-numbers-sip-peer-list-response-structure
- name: Phone Numbers Sip Peer Structure
  property_count: 4
  slug: phone-numbers-sip-peer-structure
- name: Phone Numbers Site List Response Structure
  property_count: 1
  slug: phone-numbers-site-list-response-structure
- name: Phone Numbers Site Structure
  property_count: 4
  slug: phone-numbers-site-structure
- name: Toll Free Verification Error Structure
  property_count: 2
  slug: toll-free-verification-error-structure
- name: Toll Free Verification Verification List Response Structure
  property_count: 2
  slug: toll-free-verification-verification-list-response-structure
- name: Toll Free Verification Verification Request Structure
  property_count: 11
  slug: toll-free-verification-verification-request-structure
- name: Toll Free Verification Verification Structure
  property_count: 8
  slug: toll-free-verification-verification-structure
- name: Voice Call Structure
  property_count: 13
  slug: voice-call-structure
- name: Voice Conference Member Structure
  property_count: 6
  slug: voice-conference-member-structure
- name: Voice Conference Structure
  property_count: 6
  slug: voice-conference-structure
- name: Voice Create Call Request Structure
  property_count: 12
  slug: voice-create-call-request-structure
- name: Voice Error Structure
  property_count: 3
  slug: voice-error-structure
- name: Voice Recording Structure
  property_count: 12
  slug: voice-recording-structure
- name: Voice Transcription Request Structure
  property_count: 3
  slug: voice-transcription-request-structure
- name: Voice Transcription Structure
  property_count: 4
  slug: voice-transcription-structure
- name: Voice Update Call Request Structure
  property_count: 6
  slug: voice-update-call-request-structure
- name: Voice Update Conference Member Request Structure
  property_count: 3
  slug: voice-update-conference-member-request-structure
- name: Voice Update Conference Request Structure
  property_count: 4
  slug: voice-update-conference-request-structure
jsonld:
- class_count: 51
  name: Bandwidth Context
  property_count: 137
  slug: bandwidth-context
layout: provider
modified: '2026-05-19'
name: Bandwidth
nav: Providers
network: true
overview: 'Bandwidth publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calls API, Conferences API, Emergency Notification Recipients API, and 5 more. Tagged areas include Communications, CPaaS, Voice, Messaging, and Telephony.


  The Bandwidth catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 4 Spectral governance rulesets.


  Bandwidth''s developer surface includes pricing, changelog, getting-started guide, authentication, documentation, signup flow, engineering blog, and 47 more developer resources.'
plans:
- name: Bandwidth Plans Pricing
  plan_count: 20
  slug: bandwidth-plans-pricing
- name: Bandwidth Price Estimates
  plan_count: 0
  slug: bandwidth-price-estimates
random_paper: 13
rate_limits:
- limit_count: 3
  name: Bandwidth Rate Limits
  slug: bandwidth-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Bandwidth — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: bandwidth-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Bandwidth — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bandwidth-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Bandwidth API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: bandwidth-rules
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Bandwidth API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 13
  slug: bandwidth-spectral-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 87.0
    catalog_earned_first_party: 12.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 72.4
    developer_ergonomics: 39.9
    discoverability: 80.4
    operational_transparency: 43.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 67.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bandwidth/bandwidth-2026-06-20T172942.png
security:
- kind: authentication
  name: Bandwidth Authentication
  slug: bandwidth-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bandwidth Domain Security
  slug: bandwidth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bandwidth Vulnerability Disclosure
  slug: bandwidth-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Bandwidth Trust Center
  slug: bandwidth-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 5
skills:
- name: bandwidth-create-call
  slug: bandwidth-create-call
- name: bandwidth-manage-conferences
  slug: bandwidth-manage-conferences
- name: bandwidth-manage-e911-endpoint
  slug: bandwidth-manage-e911-endpoint
- name: bandwidth-recordings-download-and-transcribe
  slug: bandwidth-recordings-download-and-transcribe
- name: bandwidth-send-and-list-messages
  slug: bandwidth-send-and-list-messages
slug: bandwidth
tags:
- Communications
- CPaaS
- Voice
- Messaging
- Telephony
- SMS
- MFA
- Telecommunications
use_cases:
- description: Embed outbound calling in web and mobile applications.
  name: Click-to-Call
- description: Build interactive voice response menus with DTMF input and TTS.
  name: IVR Systems
- description: Send application-to-person SMS campaigns at scale.
  name: A2P Messaging
- description: Add SMS or voice-based multi-factor authentication to applications.
  name: 2FA / OTP
- description: Automate phone number procurement and assignment for customers.
  name: Number Provisioning
- description: Meet Kari's Law and RAY BAUM's Act requirements for enterprise voice.
  name: E911 Compliance
- description: Build inbound/outbound contact center applications with recording.
  name: Call Center
- description: Migrate existing phone numbers to Bandwidth programmatically.
  name: Number Porting
website: https://www.bandwidth.com/
---
