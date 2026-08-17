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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 18
  human_in_the_loop: 3
  name: Vonage Agentic Access
  operation_count: 25
  slug: vonage-agentic-access
  summary_line: 25 operations · 18 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: Build multi-channel conversation experiences with threading across SMS, voice, and messaging channels. Manage members, events, and legs within conversation contexts.
  name: Vonage Conversations API
  slug: vonage-conversations-api
- description: Generate historical reports and lookup messages sent through your Vonage account. Access delivery receipts, call records, and usage data.
  name: Vonage Reports API
  slug: vonage-reports-api
- description: Embed live, interactive video into web, mobile, and desktop applications using WebRTC. Supports sessions, tokens, broadcasting, recording, and SIP interconnect.
  name: Vonage Video API
  slug: vonage-video-api
- description: Configure Vonage application settings and webhooks
  name: Vonage Applications API
  slug: vonage-applications-api
- description: Multi-channel messaging via SMS, WhatsApp, Messenger, Viber, MMS, RCS
  name: Vonage Messages API
  slug: vonage-messages-api
- description: Provision and manage virtual phone numbers
  name: Vonage Numbers API
  slug: vonage-numbers-api
- description: Send and receive SMS messages
  name: Vonage SMS API
  slug: vonage-sms-api
- description: Two-factor authentication and phone verification
  name: Vonage Verify API
  slug: vonage-verify-api
- description: Create and control voice calls
  name: Vonage Voice API
  slug: vonage-voice-api
artifact_total: 75
asyncapis:
- description: 'AsyncAPI 2.6 description of Vonage''s publicly-documented WebSocket surface. The only Vonage product whose realtime protocol is publicly specified frame-by-frame is the Voice API WebSocket endpoint: th'
  name: Vonage Voice WebSocket API
  slug: vonage-asyncapi
collections:
- collection_type: postman
  name: Vonage Communications Applications API
  slug: postman-vonage-applications-api
- collection_type: postman
  name: Vonage Communications Applications Messages API
  slug: postman-vonage-messages-api
- collection_type: postman
  name: Vonage Communications Applications Numbers API
  slug: postman-vonage-numbers-api
- collection_type: postman
  name: Vonage Communications Applications SMS API
  slug: postman-vonage-sms-api
- collection_type: postman
  name: Vonage Communications Applications Verify API
  slug: postman-vonage-verify-api
- collection_type: postman
  name: Vonage Communications Applications Voice API
  slug: postman-vonage-voice-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vonage Communications Applications API
  slug: open-vonage-applications-api
- collection_type: open
  name: Vonage Communications Applications Messages API
  slug: open-vonage-messages-api
- collection_type: open
  name: Vonage Communications Applications Numbers API
  slug: open-vonage-numbers-api
- collection_type: open
  name: Vonage Communications Applications SMS API
  slug: open-vonage-sms-api
- collection_type: open
  name: Vonage Communications Applications Verify API
  slug: open-vonage-verify-api
- collection_type: open
  name: Vonage Communications Applications Voice API
  slug: open-vonage-voice-api
- collection_type: open
  name: Vonage Communications API
  slug: open-vonage
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vonage/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vonage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vonage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vonage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vonage-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vonage
- group: start
  title: ''
  type: Portal
  url: https://developer.vonage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vonage.com/en/documentation
- group: operate
  title: ''
  type: Support
  url: https://api.support.vonage.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vonage
- group: start
  title: ''
  type: Portal
  url: https://www.vonage.com/developer-center/
- group: company
  title: ''
  type: Blog
  url: https://developer.vonage.com/en/blog
- group: operate
  title: ''
  type: Community
  url: https://vonage-community.slack.com/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-php-sdk-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-ruby-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-kotlin-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/Vonage/vonage-cli
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vonage.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vonage.com/legal/unified-communications/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vonage.com/communications-apis/#pricing
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Vonage/vonage-mcp-server-documentation
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.vonage.com/llms.txt
created: '2025-02-08'
description: Vonage (part of Ericsson) provides cloud communications APIs for voice, SMS, messaging, video, and verification. The Vonage API platform enables businesses to embed communication capabilities into applications including voice calls, SMS, multi-channel messaging (WhatsApp, Messenger, Viber, RCS), video conferencing, and two-factor authentication. SDKs are available for Node.js, Python, Java, PHP, Ruby, .NET, Go, and Kotlin.
examples:
- key_count: 4
  name: Vonage Createcall Example
  slug: vonage-createCall-example
- key_count: 4
  name: Vonage Requestverification Example
  slug: vonage-requestVerification-example
- key_count: 4
  name: Vonage Sendmessage Example
  slug: vonage-sendMessage-example
- key_count: 4
  name: Vonage Sendsms Example
  slug: vonage-sendSms-example
features:
- 'Pay-As-You-Go: no platform fee, per-message/minute pricing'
- 'US SMS outbound: $0.00809/message'
- 'US SMS inbound: $0.00649/message'
- 'US Voice outbound (local): $0.00798/minute'
- 'US Voice inbound: $0.0085/minute'
- Verify API for OTP across SMS/Voice/WhatsApp channels
- Messages API for SMS, MMS, WhatsApp, Viber, Facebook Messenger
- Voice API with TwiML-style NCCO scripting
- Number Insight for line type / carrier lookup
- Network APIs (CAMARA — SIM Swap, Number Verify, Location)
- Default 30 msg/sec for SMS and Verify
- Vonage Video API (formerly OpenTok)
- Conversation API for chat/voice/video apps
- Webhooks for delivery receipts and inbound events
- JWT and API key/secret auth
- Carrier surcharges add 50-100% over base rates
finops:
- name: Vonage Finops
  service_category: Communications
  slug: vonage-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Vonage Communications API platform (part of Ericsson). Vonage provides cloud communications APIs spanning Voice, SMS, multi-channel Messagin
  name: Vonage GraphQL Schema
  slug: vonage-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vonage.png
json_schemas:
- name: Application
  property_count: 4
  slug: vonage-application
- name: ApplicationList
  property_count: 5
  slug: vonage-applicationlist
- name: ApplicationRequest
  property_count: 2
  slug: vonage-applicationrequest
- name: AvailableNumberList
  property_count: 2
  slug: vonage-availablenumberlist
- name: Vonage Call
  property_count: 12
  slug: vonage-call
- name: CallList
  property_count: 4
  slug: vonage-calllist
- name: CreateCallRequest
  property_count: 6
  slug: vonage-createcallrequest
- name: Vonage Message
  property_count: 13
  slug: vonage-message
- name: MessageRequest
  property_count: 6
  slug: vonage-messagerequest
- name: MessageResponse
  property_count: 1
  slug: vonage-messageresponse
- name: Number
  property_count: 5
  slug: vonage-number
- name: NumberList
  property_count: 2
  slug: vonage-numberlist
- name: SmsResponse
  property_count: 2
  slug: vonage-smsresponse
- name: VerifyCheckResponse
  property_count: 5
  slug: vonage-verifycheckresponse
- name: VerifyResponse
  property_count: 3
  slug: vonage-verifyresponse
- name: VerifySearchResponse
  property_count: 12
  slug: vonage-verifysearchresponse
json_structures:
- name: Vonage Message Structure
  property_count: 0
  slug: vonage-message-structure
- name: Vonage Structure
  property_count: 0
  slug: vonage-structure
jsonld:
- class_count: 0
  name: Vonage Context
  property_count: 19
  slug: vonage-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Vonage
nav: Providers
network: true
overview: 'Vonage publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Messages API, Numbers API, and 3 more. Tagged areas include Communication, Messaging, Telecommunications, Video Conferencing, and Voice.


  The Vonage catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Vonage''s developer surface includes authentication, developer portal, documentation, support, engineering blog, CLI, pricing, and 20 more developer resources.'
plans:
- name: Vonage Plans Pricing
  plan_count: 2
  slug: vonage-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 4
  name: Vonage Rate Limits
  slug: vonage-rate-limits
rules:
- name: Vonage API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: vonage-asyncapi-spectral-rules
- name: Vonage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vonage-jsonschema-spectral-rules
- name: Vonage API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 6
    warn: 4
  slug: vonage-rules
score:
  band: developing
  composite: 54.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 73.9
    developer_ergonomics: 69.6
    discoverability: 81.5
    governance: 47.9
    operational_transparency: 13.2
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/screenshots/vonage-2026-06-20T165933.png
security:
- kind: authentication
  name: Vonage Authentication
  slug: vonage-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Vonage Domain Security
  slug: vonage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vonage Vulnerability Disclosure
  slug: vonage-vulnerability-disclosure
  summary_line: disclosure policy published
slug: vonage
tags:
- Communication
- Messaging
- Telecommunications
- Video Conferencing
- Voice
- SMS
- Verification
website: https://developer.vonage.com/
---
