---
aid: bandwidth
url: https://raw.githubusercontent.com/api-evangelist/bandwidth/refs/heads/main/apis.yml
apis:
- aid: bandwidth:voice-api
  name: Bandwidth Voice API
  tags:
  - Calls
  - Conferences
  - CPaaS
  - Recordings
  - Telephony
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://voice.bandwidth.com/api/v2
  humanURL: https://dev.bandwidth.com/docs/voice/
  properties:
  - url: https://dev.bandwidth.com/docs/voice/
    type: Documentation
  - url: openapi/bandwidth-voice-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/bandwidth-voice-events-asyncapi.yml
    type: AsyncAPI
  description: The Bandwidth Voice API enables developers to programmatically make and receive phone calls, manage call recordings, and create multi-party conferences. It supports advanced call control features including call transfers, bridging, DTMF detection, and text-to-speech. The API uses BXML (Bandwidth XML) verbs for call flow control and provides webhooks for real-time event notifications on call state changes.
- aid: bandwidth:messaging-api
  name: Bandwidth Messaging API
  tags:
  - CPaaS
  - Messaging
  - MMS
  - SMS
  - Text Messaging
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://messaging.bandwidth.com/api/v2
  humanURL: https://dev.bandwidth.com/docs/messaging/
  properties:
  - url: https://dev.bandwidth.com/docs/messaging/
    type: Documentation
  - url: openapi/bandwidth-messaging-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/bandwidth-messaging-events-asyncapi.yml
    type: AsyncAPI
  description: The Bandwidth Messaging API allows developers to send and receive SMS and MMS messages programmatically. It supports both toll-free and local number messaging, group messaging, and application-to-person (A2P) messaging workflows. The API provides delivery receipts via webhooks, message status tracking, and media management for MMS attachments. Bandwidth operates its own tier-1 network, providing direct carrier connectivity for reliable message delivery.
- aid: bandwidth:phone-numbers-api
  name: Bandwidth Phone Numbers API
  tags:
  - Number Management
  - Phone Numbers
  - Porting
  - Telecom
  - Telephone Numbers
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://dashboard.bandwidth.com/api
  humanURL: https://dev.bandwidth.com/docs/numbers/
  properties:
  - url: https://dev.bandwidth.com/docs/numbers/
    type: Documentation
  - url: openapi/bandwidth-phone-numbers-api-openapi.yml
    type: OpenAPI
  description: The Bandwidth Phone Numbers API provides programmatic access to search, order, and manage phone numbers across the United States and Canada. Developers can search for available local, toll-free, and short code numbers, initiate number porting requests, and configure number features such as CNAM, directory listings, and line features. The API also supports managing sites, SIP peers, and number assignments for organizing telephony resources within an account.
- aid: bandwidth:multi-factor-authentication-api
  name: Bandwidth Multi-Factor Authentication API
  tags:
  - Authentication
  - MFA
  - Security
  - Two-Factor Authentication
  - Verification
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://mfa.bandwidth.com/api/v1
  humanURL: https://dev.bandwidth.com/docs/mfa/
  properties:
  - url: https://dev.bandwidth.com/docs/mfa/
    type: Documentation
  - url: openapi/bandwidth-mfa-api-openapi.yml
    type: OpenAPI
  description: The Bandwidth Multi-Factor Authentication API allows developers to generate and verify secure MFA codes delivered via voice calls or SMS messages. It leverages Bandwidth's Voice and Messaging APIs under the hood, handling token generation and management automatically. Developers can customize the code length, expiration time, and delivery message template. The API supports both one-time passcode delivery and verification in a simple two-step workflow.
- aid: bandwidth:emergency-calling-api
  name: Bandwidth Emergency Calling API
  tags:
  - Compliance
  - E911
  - Emergency Services
  - Public Safety
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://dashboard.bandwidth.com/api
  humanURL: https://dev.bandwidth.com/docs/emergency/emergencyCallingApi/
  properties:
  - url: https://dev.bandwidth.com/docs/emergency/emergencyCallingApi/
    type: Documentation
  - url: openapi/bandwidth-emergency-calling-api-openapi.yml
    type: OpenAPI
  description: The Bandwidth Emergency Calling API provides programmatic access to provision and manage 911 endpoints and locations for emergency services routing. It supports Dynamic Location Routing (DLR) for real-time address validation and location updates, ensuring compliance with Kari's Law and RAY BAUM's Act requirements.
- aid: bandwidth:toll-free-verification-api
  name: Bandwidth Toll-Free Verification API
  tags:
  - A2P
  - Messaging Compliance
  - Toll-Free
  - Verification
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://dashboard.bandwidth.com/api
  humanURL: https://dev.bandwidth.com/apis/messaging-apis/toll-free-verification/
  properties:
  - url: https://dev.bandwidth.com/apis/messaging-apis/toll-free-verification/
    type: Documentation
  - url: openapi/bandwidth-toll-free-verification-api-openapi.yml
    type: OpenAPI
  description: The Bandwidth Toll-Free Verification API enables developers to programmatically submit and manage toll-free number verification requests for A2P messaging compliance. It automates the verification submission process, allowing developers to view and update the verification status of their toll-free numbers. This API helps ensure that toll-free messaging traffic complies with carrier requirements and regulations including the Telephone Consumer Protection Act (TCPA).
name: Bandwidth
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A general overview of Bandwidth's Voice Services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

