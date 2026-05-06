---
aid: vonage
url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/apis.yml
apis:
  - aid: vonage:vonage-sms-api
    name: Vonage SMS API
    tags:
      - Communication
      - Messaging
      - SMS
      - Telecommunications
    humanURL: https://developer.vonage.com/en/api/sms
    baseURL: https://rest.nexmo.com
    description: Send and receive SMS messages globally using Vonage's SMS API. Supports text, binary, and unicode message types with delivery receipts and inbound message webhooks.
    properties:
      - url: https://developer.vonage.com/en/api/sms
        type: Documentation
      - url: https://rest.nexmo.com
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/openapi/vonage-openapi.yml
        type: OpenAPI
  - aid: vonage:vonage-voice-api
    name: Vonage Voice API
    tags:
      - Communication
      - Telecommunications
      - Voice
      - VoIP
    humanURL: https://developer.vonage.com/en/api/voice
    baseURL: https://api.nexmo.com/v1
    description: Create and control outbound and inbound voice calls using Vonage's Voice API. Supports PSTN, SIP, WebSocket, and VBC endpoints with NCCO (Vonage Call Control Object) for call flow management.
    properties:
      - url: https://developer.vonage.com/en/api/voice
        type: Documentation
      - url: https://api.nexmo.com/v1
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/openapi/vonage-openapi.yml
        type: OpenAPI
  - aid: vonage:vonage-messages-api
    name: Vonage Messages API
    tags:
      - Communication
      - Messaging
      - Omnichannel
      - WhatsApp
      - RCS
    humanURL: https://developer.vonage.com/en/api/messages-olympus
    baseURL: https://api.nexmo.com/v1/messages
    description: Multi-channel messaging API supporting SMS, WhatsApp, Facebook Messenger, Viber, MMS, and RCS. Send and receive messages across multiple channels with a unified API interface.
    properties:
      - url: https://developer.vonage.com/en/api/messages-olympus
        type: Documentation
      - url: https://api.nexmo.com/v1/messages
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/openapi/vonage-openapi.yml
        type: OpenAPI
  - aid: vonage:vonage-verify-api
    name: Vonage Verify API
    tags:
      - Authentication
      - Communication
      - Security
      - Two-Factor Authentication
      - Verification
    humanURL: https://developer.vonage.com/en/api/verify
    baseURL: https://api.nexmo.com
    description: Two-factor authentication and phone verification API. Confirm user phone numbers via SMS, TTS, or WhatsApp verification codes to prevent fraud and authenticate users.
    properties:
      - url: https://developer.vonage.com/en/api/verify
        type: Documentation
      - url: https://api.nexmo.com
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/openapi/vonage-openapi.yml
        type: OpenAPI
  - aid: vonage:vonage-numbers-api
    name: Vonage Numbers API
    tags:
      - Communication
      - Number Management
      - Telecommunications
      - Virtual Numbers
    humanURL: https://developer.vonage.com/en/api/numbers
    baseURL: https://rest.nexmo.com
    description: Provision and manage virtual phone numbers globally. Search available numbers, purchase numbers for your account, and configure number behavior including inbound SMS and voice call routing.
    properties:
      - url: https://developer.vonage.com/en/api/numbers
        type: Documentation
      - url: https://rest.nexmo.com
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/openapi/vonage-openapi.yml
        type: OpenAPI
  - aid: vonage:vonage-application-api
    name: Vonage Application API
    tags:
      - API Management
      - Communication
      - Configuration
      - Developer Tools
    humanURL: https://developer.vonage.com/en/api/application.v2
    baseURL: https://api.nexmo.com/v2/applications
    description: Configure Vonage application settings, webhook URLs, and authentication keys. Create and manage applications that group Vonage API capabilities including voice, messages, RTC, meetings, and video features.
    properties:
      - url: https://developer.vonage.com/en/api/application.v2
        type: Documentation
      - url: https://api.nexmo.com/v2/applications
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/vonage/refs/heads/main/openapi/vonage-openapi.yml
        type: OpenAPI
  - aid: vonage:vonage-conversations-api
    name: Vonage Conversations API
    tags:
      - Communication
      - Conversations
      - Messaging
      - Real-Time
    humanURL: https://developer.vonage.com/en/api/conversation
    baseURL: https://api.nexmo.com/v1
    description: Build multi-channel conversation experiences with threading across SMS, voice, and messaging channels. Manage members, events, and legs within conversation contexts.
    properties:
      - url: https://developer.vonage.com/en/api/conversation
        type: Documentation
      - url: https://api.nexmo.com/v1
        type: BaseURL
  - aid: vonage:vonage-reports-api
    name: Vonage Reports API
    tags:
      - Analytics
      - Communication
      - Reporting
    humanURL: https://developer.vonage.com/en/reports/overview
    baseURL: https://api.nexmo.com/v2/reports
    description: Generate historical reports and lookup messages sent through your Vonage account. Access delivery receipts, call records, and usage data.
    properties:
      - url: https://developer.vonage.com/en/reports/overview
        type: Documentation
      - url: https://api.nexmo.com/v2/reports
        type: BaseURL
  - aid: vonage:vonage-video-api
    name: Vonage Video API
    tags:
      - Communication
      - Telecommunications
      - Video
      - WebRTC
    humanURL: https://developer.vonage.com/en/video/overview
    baseURL: https://api.opentok.com
    description: Embed live, interactive video into web, mobile, and desktop applications using WebRTC. Supports sessions, tokens, broadcasting, recording, and SIP interconnect.
    properties:
      - url: https://developer.vonage.com/en/video/overview
        type: Documentation
      - url: https://tokbox.com/developer/
        type: Portal
      - url: https://api.opentok.com
        type: BaseURL
name: Vonage
tags:
  - Communication
  - Messaging
  - Telecommunications
  - Video Conferencing
  - Voice
  - SMS
  - Verification
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-05-04'
position: Consumer
description: Vonage (part of Ericsson) provides cloud communications APIs for voice, SMS, messaging, video, and verification. The Vonage API platform enables businesses to embed communication capabilities into applications including voice calls, SMS, multi-channel messaging (WhatsApp, Messenger, Viber, RCS), video conferencing, and two-factor authentication. SDKs are available for Node.js, Python, Java, PHP, Ruby, .NET, Go, and Kotlin.
common:
  - url: https://developer.vonage.com/
    name: Vonage API Developer Portal
    type: Portal
    description: Official developer portal for Vonage APIs.
  - url: https://developer.vonage.com/en/documentation
    name: Vonage API Documentation
    type: Documentation
    description: Complete API documentation for all Vonage APIs.
  - url: https://api.support.vonage.com/hc/en-us
    name: Vonage API Support
    type: Support
    description: Vonage developer support center.
  - url: https://github.com/Vonage
    name: Vonage GitHub Organization
    type: GitHubOrganization
    description: Vonage SDKs, code samples, and tools on GitHub.
  - url: https://www.vonage.com/developer-center/
    name: Developer Center
    type: Portal
    description: Vonage developer resources and tools.
  - url: https://developer.vonage.com/en/blog
    name: Vonage Developer Blog
    type: Blog
    description: Developer tutorials and updates.
  - url: https://vonage-community.slack.com/
    name: Vonage Community Slack
    type: Community
    description: Community Slack workspace for Vonage developers.
  - url: https://github.com/Vonage/vonage-node-sdk
    name: Vonage Node.js SDK
    type: SDK
    description: Official Vonage SDK for Node.js.
  - url: https://github.com/Vonage/vonage-python-sdk
    name: Vonage Python SDK
    type: SDK
    description: Official Vonage SDK for Python.
  - url: https://github.com/Vonage/vonage-java-sdk
    name: Vonage Java SDK
    type: SDK
    description: Official Vonage SDK for Java.
  - url: https://github.com/Vonage/vonage-php-sdk-core
    name: Vonage PHP SDK
    type: SDK
    description: Official Vonage SDK for PHP.
  - url: https://github.com/Vonage/vonage-ruby-sdk
    name: Vonage Ruby SDK
    type: SDK
    description: Official Vonage SDK for Ruby.
  - url: https://github.com/Vonage/vonage-dotnet-sdk
    name: Vonage .NET SDK
    type: SDK
    description: Official Vonage SDK for .NET/C#.
  - url: https://github.com/Vonage/vonage-go-sdk
    name: Vonage Go SDK
    type: SDK
    description: Official Vonage SDK for Go.
  - url: https://github.com/Vonage/vonage-kotlin-sdk
    name: Vonage Kotlin SDK
    type: SDK
    description: Official Vonage SDK for Kotlin.
  - url: https://github.com/Vonage/vonage-cli
    name: Vonage CLI
    type: CLI
    description: Command-line interface for managing Vonage resources.
  - url: https://www.vonage.com/legal/
    name: Terms of Service
    type: TermsOfService
    description: Vonage terms of service.
  - url: https://www.vonage.com/legal/unified-communications/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
    description: Vonage privacy policy.
  - url: https://www.vonage.com/communications-apis/#pricing
    name: Pricing
    type: Pricing
    description: Vonage API pricing.
  - type: Features
    data:
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
    sources:
      - https://www.vonage.com/communications-apis/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
