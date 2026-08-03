---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Messagebird Agentic Access
  operation_count: 80
  slug: messagebird-agentic-access
  summary_line: 80 operations · 40 acting
api_count: 19
apis:
- description: Operations for searching available phone numbers for purchase.
  name: messagebird Available Numbers API
  slug: messagebird-available-numbers-api
- description: Operations for retrieving account balance information.
  name: messagebird Balance API
  slug: messagebird-balance-api
- description: Operations for managing call flows that define interactive voice response sequences.
  name: messagebird Call Flows API
  slug: messagebird-call-flows-api
- description: Operations for creating, listing, and managing voice calls.
  name: messagebird Calls API
  slug: messagebird-calls-api
- description: Operations for managing individual contacts.
  name: messagebird Contacts API
  slug: messagebird-contacts-api
- description: Operations for listing and managing conversations across channels.
  name: messagebird Conversations API
  slug: messagebird-conversations-api
- description: Operations for managing contact groups.
  name: messagebird Groups API
  slug: messagebird-groups-api
- description: Operations for creating and viewing HLR network queries.
  name: messagebird HLR API
  slug: messagebird-hlr-api
- description: Operations for viewing and managing call legs. A leg represents a single voice connection within a call.
  name: messagebird Legs API
  slug: messagebird-legs-api
- description: Operations for looking up and validating phone numbers.
  name: messagebird Lookup API
  slug: messagebird-lookup-api
- description: Operations for sending and retrieving messages within conversations.
  name: messagebird Messages API
  slug: messagebird-messages-api
- description: Operations for managing purchased phone numbers.
  name: messagebird Purchased Numbers API
  slug: messagebird-purchased-numbers-api
- description: Operations for managing call recordings.
  name: messagebird Recordings API
  slug: messagebird-recordings-api
- description: Operations for managing message templates on supported platforms.
  name: messagebird Templates API
  slug: messagebird-templates-api
- description: Operations for creating and viewing transcriptions of call recordings.
  name: messagebird Transcriptions API
  slug: messagebird-transcriptions-api
- description: Operations for creating, verifying, and managing verification tokens.
  name: messagebird Verify API
  slug: messagebird-verify-api
- description: Operations for sending and managing text-to-speech voice messages.
  name: messagebird Voice Messages API
  slug: messagebird-voice-messages-api
- description: Operations for managing conversation webhooks that receive real-time event notifications.
  name: messagebird Webhooks API
  slug: messagebird-webhooks-api
- description: Operations for sending and receiving WhatsApp messages through the Conversations API interface.
  name: messagebird WhatsApp Messages API
  slug: messagebird-whatsapp-messages-api
artifact_total: 132
asyncapis:
- description: The MessageBird Conversations webhook system delivers real-time notifications for conversation events across all messaging channels including SMS, WhatsApp, Facebook Messenger, Telegram, and more. Web
  name: MessageBird Conversations Events
  slug: messagebird-conversations-asyncapi
collections:
- collection_type: open
  name: MessageBird Balance API
  slug: open-messagebird-balance
- collection_type: open
  name: MessageBird Contacts API
  slug: open-messagebird-contacts
- collection_type: open
  name: MessageBird Conversations API
  slug: open-messagebird-conversations
- collection_type: open
  name: MessageBird HLR API
  slug: open-messagebird-hlr
- collection_type: open
  name: MessageBird Integrations API
  slug: open-messagebird-integrations
- collection_type: open
  name: MessageBird Lookup API
  slug: open-messagebird-lookup
- collection_type: open
  name: MessageBird Numbers API
  slug: open-messagebird-numbers
- collection_type: open
  name: MessageBird SMS Messaging API
  slug: open-messagebird-sms-messaging
- collection_type: open
  name: MessageBird Verify API
  slug: open-messagebird-verify
- collection_type: open
  name: MessageBird Voice Calling API
  slug: open-messagebird-voice-calling
- collection_type: open
  name: MessageBird Voice Messaging API
  slug: open-messagebird-voice-messaging
- collection_type: open
  name: MessageBird WhatsApp API
  slug: open-messagebird-whatsapp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/messagebird-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/messagebird-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/messagebird-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/messagebird-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/messagebird
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/birdhq
- group: design
  title: ''
  type: JSONLD
  url: json-ld/messagebird-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/messagebird-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/messagebird-conversation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/messagebird-contact-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://bird.com/llms.txt
description: Build powerful apps using the fastest and most reliable cloud communications APIs.
features:
- 'Email: starts $1.50 per 1,000 messages'
- 'SMS: per-country rates with Bundle discounts'
- 'WhatsApp: $0.005/msg + Meta passthrough'
- 'Push: $0.0005/notification'
- 'RCS: $0.005/msg + carrier passthrough'
- 'Voice API: custom pricing'
- REST API at api.bird.com
- Default 50 req/sec/workspace
- OAuth 2.0 + API keys
- Webhooks for delivery, status, inbound events
- 200+ countries supported
- Inbox for omnichannel customer messaging
- Flow Builder for no-code journey orchestration
- Conversations API
- Numbers (rental for phone numbers)
- Verify API for OTP
finops:
- name: Messagebird Finops
  service_category: Omnichannel CPaaS
  slug: messagebird-finops
graphqls:
- description: MessageBird (now Bird) is a communications platform for SMS, WhatsApp, email, voice, and push notifications. The API covers messaging, conversations, contacts, flows, channels, voice calls, and omnich
  name: MessageBird GraphQL API
  slug: messagebird-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/messagebird.png
json_schemas:
- name: AvailableNumber
  property_count: 7
  slug: messagebird-availablenumber
- name: AvailableNumberList
  property_count: 3
  slug: messagebird-availablenumberlist
- name: Balance
  property_count: 3
  slug: messagebird-balance
- name: Call
  property_count: 7
  slug: messagebird-call
- name: CallCreate
  property_count: 4
  slug: messagebird-callcreate
- name: CallFlow
  property_count: 6
  slug: messagebird-callflow
- name: CallFlowCreate
  property_count: 3
  slug: messagebird-callflowcreate
- name: CallFlowList
  property_count: 2
  slug: messagebird-callflowlist
- name: CallFlowResponse
  property_count: 1
  slug: messagebird-callflowresponse
- name: CallFlowStep
  property_count: 3
  slug: messagebird-callflowstep
- name: CallList
  property_count: 2
  slug: messagebird-calllist
- name: CallResponse
  property_count: 1
  slug: messagebird-callresponse
- name: Channel
  property_count: 6
  slug: messagebird-channel
- name: MessageBird Contact
  property_count: 13
  slug: messagebird-contact
- name: ContactCreate
  property_count: 7
  slug: messagebird-contactcreate
- name: ContactList
  property_count: 5
  slug: messagebird-contactlist
- name: ContactUpdate
  property_count: 7
  slug: messagebird-contactupdate
- name: MessageBird Conversation
  property_count: 9
  slug: messagebird-conversation
- name: ConversationList
  property_count: 5
  slug: messagebird-conversationlist
- name: ConversationMessage
  property_count: 12
  slug: messagebird-conversationmessage
- name: ConversationMessageList
  property_count: 5
  slug: messagebird-conversationmessagelist
- name: ConversationMessageSend
  property_count: 4
  slug: messagebird-conversationmessagesend
- name: ConversationStart
  property_count: 5
  slug: messagebird-conversationstart
- name: ConversationUpdate
  property_count: 1
  slug: messagebird-conversationupdate
- name: Group
  property_count: 6
  slug: messagebird-group
- name: GroupCreate
  property_count: 1
  slug: messagebird-groupcreate
- name: GroupList
  property_count: 5
  slug: messagebird-grouplist
- name: Hlr
  property_count: 8
  slug: messagebird-hlr
- name: HlrCreate
  property_count: 2
  slug: messagebird-hlrcreate
- name: HlrLookup
  property_count: 6
  slug: messagebird-hlrlookup
- name: Leg
  property_count: 11
  slug: messagebird-leg
- name: LegList
  property_count: 2
  slug: messagebird-leglist
- name: Lookup
  property_count: 7
  slug: messagebird-lookup
- name: MessageBird SMS Message
  property_count: 16
  slug: messagebird-message
- name: MessageContent
  property_count: 7
  slug: messagebird-messagecontent
- name: MessageCreate
  property_count: 12
  slug: messagebird-messagecreate
- name: MessageList
  property_count: 6
  slug: messagebird-messagelist
- name: MessageSend
  property_count: 5
  slug: messagebird-messagesend
- name: NumberPurchase
  property_count: 3
  slug: messagebird-numberpurchase
- name: NumberUpdate
  property_count: 1
  slug: messagebird-numberupdate
- name: Pagination
  property_count: 4
  slug: messagebird-pagination
- name: PurchasedNumber
  property_count: 10
  slug: messagebird-purchasednumber
- name: PurchasedNumberList
  property_count: 5
  slug: messagebird-purchasednumberlist
- name: Recipient
  property_count: 3
  slug: messagebird-recipient
- name: Recipients
  property_count: 5
  slug: messagebird-recipients
- name: Recording
  property_count: 7
  slug: messagebird-recording
- name: RecordingList
  property_count: 2
  slug: messagebird-recordinglist
- name: RecordingResponse
  property_count: 1
  slug: messagebird-recordingresponse
- name: Template
  property_count: 8
  slug: messagebird-template
- name: TemplateComponent
  property_count: 4
  slug: messagebird-templatecomponent
- name: TemplateCreate
  property_count: 4
  slug: messagebird-templatecreate
- name: TemplateList
  property_count: 5
  slug: messagebird-templatelist
- name: Transcription
  property_count: 5
  slug: messagebird-transcription
- name: TranscriptionCreate
  property_count: 1
  slug: messagebird-transcriptioncreate
- name: TranscriptionList
  property_count: 2
  slug: messagebird-transcriptionlist
- name: TranscriptionResponse
  property_count: 1
  slug: messagebird-transcriptionresponse
- name: Verify
  property_count: 8
  slug: messagebird-verify
- name: VerifyCreate
  property_count: 10
  slug: messagebird-verifycreate
- name: VoiceMessage
  property_count: 12
  slug: messagebird-voicemessage
- name: VoiceMessageCreate
  property_count: 11
  slug: messagebird-voicemessagecreate
- name: VoiceMessageList
  property_count: 6
  slug: messagebird-voicemessagelist
- name: VoiceWebhook
  property_count: 5
  slug: messagebird-voicewebhook
- name: VoiceWebhookCreate
  property_count: 2
  slug: messagebird-voicewebhookcreate
- name: VoiceWebhookList
  property_count: 2
  slug: messagebird-voicewebhooklist
- name: VoiceWebhookResponse
  property_count: 1
  slug: messagebird-voicewebhookresponse
- name: Webhook
  property_count: 7
  slug: messagebird-webhook
- name: WebhookCreate
  property_count: 3
  slug: messagebird-webhookcreate
- name: WebhookList
  property_count: 5
  slug: messagebird-webhooklist
- name: WhatsAppContent
  property_count: 8
  slug: messagebird-whatsappcontent
- name: WhatsAppMessage
  property_count: 12
  slug: messagebird-whatsappmessage
- name: WhatsAppMessageSend
  property_count: 5
  slug: messagebird-whatsappmessagesend
- name: WhatsAppReply
  property_count: 2
  slug: messagebird-whatsappreply
json_structures:
- name: Messagebird Structure
  property_count: 0
  slug: messagebird-structure
jsonld:
- class_count: 0
  name: Messagebird Context
  property_count: 8
  slug: messagebird-context
layout: provider
modified: '2026-05-19'
name: messagebird
nav: Providers
network: true
overview: 'messagebird publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Available Numbers API, Balance API, Call Flows API, and 16 more.


  The messagebird catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  messagebird''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Messagebird Plans Pricing
  plan_count: 6
  slug: messagebird-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Messagebird Rate Limits
  slug: messagebird-rate-limits
rules:
- name: messagebird API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: messagebird-asyncapi-spectral-rules
- name: messagebird API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: messagebird-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.2
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/messagebird/refs/heads/main/screenshots/messagebird-2026-06-20T185240.png
security:
- kind: authentication
  name: Messagebird Authentication
  slug: messagebird-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Messagebird Domain Security
  slug: messagebird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Messagebird Vulnerability Disclosure
  slug: messagebird-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: messagebird
---
