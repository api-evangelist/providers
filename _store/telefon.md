---
name: Telefon
description: Telefon is a cloud-based programmable communications platform providing voice calling, SMS messaging, number management, and call recording APIs for developers and enterprises. The platform enables applications to make and receive phone calls, send SMS and MMS messages, manage phone number inventories, and record calls for compliance and quality assurance purposes. Telefon supports global coverage across 180+ countries with competitive per-minute and per-message pricing.
image: https://www.telefon.com/logo.png
url: https://www.telefon.com
type: Index
tags:
  - Call Recording
  - Communications
  - CPaaS
  - Global Coverage
  - Messaging
  - Number Provisioning
  - SMS
  - Telephony
  - Voice
  - VoIP
created: '2024-01-15'
modified: '2026-05-03'
specificationVersion: '0.16'
apis:
  - name: Telefon Voice API
    description: Programmable voice API for building call-based applications. Make outbound calls, handle inbound calls with webhooks, build IVR menus, perform call transfer and conferencing, and control calls in real-time. Supports SIP trunking, WebRTC, text-to-speech, speech recognition, and call recording.
    image: https://www.telefon.com/voice-icon.png
    humanURL: https://developers.telefon.com/voice
    baseURL: https://api.telefon.com/v1/voice
    version: v1
    tags:
      - Calls
      - Communications
      - IVR
      - SIP Trunking
      - Telephony
      - TTS
      - Voice
      - WebRTC
    properties:
      - type: Documentation
        url: https://developers.telefon.com/voice
      - type: OpenAPI
        url: openapi/telefon-voice-openapi.yml
      - type: Authentication
        url: https://developers.telefon.com/authentication
      - type: GettingStarted
        url: https://developers.telefon.com/getting-started
      - type: Pricing
        url: https://www.telefon.com/pricing/voice
      - type: RateLimits
        url: https://developers.telefon.com/rate-limits
    contact:
      - type: Email
        url: mailto:api@telefon.com
      - type: Support
        url: https://www.telefon.com/support
  - name: Telefon SMS API
    description: Send and receive SMS and MMS messages globally. Supports A2P (Application-to-Person) messaging, two-way conversational SMS, delivery receipts, inbound webhooks, message queuing for high throughput, and unicode character sets for international languages. Compliant with TCPA (US), GDPR (EU), and other regional regulations.
    image: https://www.telefon.com/sms-icon.png
    humanURL: https://developers.telefon.com/sms
    baseURL: https://api.telefon.com/v1/sms
    version: v1
    tags:
      - A2P Messaging
      - Communications
      - Messaging
      - MMS
      - SMS
      - Two-Way SMS
      - Unicode
    properties:
      - type: Documentation
        url: https://developers.telefon.com/sms
      - type: OpenAPI
        url: openapi/telefon-sms-openapi.yml
      - type: Authentication
        url: https://developers.telefon.com/authentication
      - type: Pricing
        url: https://www.telefon.com/pricing/sms
      - type: Rate Limits
        url: https://developers.telefon.com/rate-limits
    contact:
      - type: Email
        url: mailto:api@telefon.com
  - name: Telefon Number Management API
    description: Search, provision, configure, and manage phone numbers worldwide. Supports local, national, mobile, toll-free, and short code numbers across 70+ countries. Configure voice and SMS routing, manage number pools, and handle number portability requests. Supports regulatory compliance requirements including address verification for regulated number types.
    image: https://www.telefon.com/numbers-icon.png
    humanURL: https://developers.telefon.com/numbers
    baseURL: https://api.telefon.com/v1/numbers
    version: v1
    tags:
      - DID
      - Number Management
      - Number Portability
      - Number Provisioning
      - Phone Numbers
      - Short Codes
      - Toll-Free
    properties:
      - type: Documentation
        url: https://developers.telefon.com/numbers
      - type: OpenAPI
        url: openapi/telefon-numbers-openapi.yml
      - type: Authentication
        url: https://developers.telefon.com/authentication
      - type: Pricing
        url: https://www.telefon.com/pricing/numbers
    contact:
      - type: Email
        url: mailto:api@telefon.com
  - name: Telefon Call Recording API
    description: Record, store, transcribe, and retrieve call recordings. Supports on-demand and automatic recording, dual-channel recording for separate caller/callee audio, AI-powered transcription in 30+ languages, PII redaction, storage management, and compliance archiving with configurable retention policies.
    image: https://www.telefon.com/recording-icon.png
    humanURL: https://developers.telefon.com/recording
    baseURL: https://api.telefon.com/v1/recording
    version: v1
    tags:
      - AI Transcription
      - Audio
      - Call Recording
      - Compliance
      - Dual Channel
      - PII Redaction
      - Storage
      - Transcription
    properties:
      - type: Documentation
        url: https://developers.telefon.com/recording
      - type: OpenAPI
        url: openapi/telefon-recording-openapi.yml
      - type: Authentication
        url: https://developers.telefon.com/authentication
      - type: Privacy Policy
        url: https://www.telefon.com/privacy
      - type: Compliance
        url: https://www.telefon.com/compliance
    contact:
      - type: Email
        url: mailto:api@telefon.com
common:
  - type: Getting Started
    url: https://developers.telefon.com/getting-started
  - type: Authentication
    url: https://developers.telefon.com/authentication
  - type: SDKs
    url: https://www.telefon.com/sdks
  - type: Status Page
    url: https://status.telefon.com
  - type: Terms of Service
    url: https://www.telefon.com/terms
  - type: Privacy Policy
    url: https://www.telefon.com/privacy
  - type: Support
    url: https://www.telefon.com/support
  - type: Blog
    url: https://blog.telefon.com
  - type: Change Log
    url: https://developers.telefon.com/changelog
  - type: Pricing
    url: https://www.telefon.com/pricing
  - type: GitHub
    url: https://github.com/telefon-api
maintainers:
  - name: Telefon API Team
    email: api@telefon.com
---
