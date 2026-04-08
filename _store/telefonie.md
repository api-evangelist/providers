---
aid: telefonie
url: https://raw.githubusercontent.com/api-evangelist/telefonie/refs/heads/main/apis.yml
apis:
- name: Voice API
  description: Make and receive phone calls programmatically.
  image: https://www.telefonie.example.com/images/voice-api.png
  humanURL: https://www.telefonie.example.com/voice
  baseURL: https://api.telefonie.example.com/v1/voice
  tags:
  - Calls
  - Voice
  - VOIP
  properties:
  - type: Documentation
    url: https://docs.telefonie.example.com/voice
  - type: OpenAPI
    url: https://api.telefonie.example.com/specs/voice-openapi.json
  - type: Swagger
    url: https://api.telefonie.example.com/specs/voice-swagger.json
  contact:
  - type: Support
    url: https://www.telefonie.example.com/support
  - type: Email
    url: mailto:support@telefonie.example.com
- name: SMS API
  description: Send and receive SMS messages.
  image: https://www.telefonie.example.com/images/sms-api.png
  humanURL: https://www.telefonie.example.com/sms
  baseURL: https://api.telefonie.example.com/v1/sms
  tags:
  - Messaging
  - SMS
  - Text
  properties:
  - type: Documentation
    url: https://docs.telefonie.example.com/sms
  - type: OpenAPI
    url: https://api.telefonie.example.com/specs/sms-openapi.json
  - type: Pricing
    url: https://www.telefonie.example.com/pricing/sms
  contact:
  - type: Support
    url: https://www.telefonie.example.com/support
  - type: Email
    url: mailto:support@telefonie.example.com
- name: Number Management API
  description: Purchase, configure, and manage phone numbers.
  image: https://www.telefonie.example.com/images/numbers-api.png
  humanURL: https://www.telefonie.example.com/numbers
  baseURL: https://api.telefonie.example.com/v1/numbers
  tags:
  - DID
  - Number Provisioning
  - Phone Numbers
  properties:
  - type: Documentation
    url: https://docs.telefonie.example.com/numbers
  - type: OpenAPI
    url: https://api.telefonie.example.com/specs/numbers-openapi.json
  contact:
  - type: Support
    url: https://www.telefonie.example.com/support
- name: Call Recording API
  description: Record and retrieve call recordings.
  image: https://www.telefonie.example.com/images/recording-api.png
  humanURL: https://www.telefonie.example.com/recording
  baseURL: https://api.telefonie.example.com/v1/recordings
  tags:
  - Compliance
  - Recording
  - Storage
  properties:
  - type: Documentation
    url: https://docs.telefonie.example.com/recording
  - type: OpenAPI
    url: https://api.telefonie.example.com/specs/recording-openapi.json
  contact:
  - type: Support
    url: https://www.telefonie.example.com/support
name: Telefonie
tags:
- Messaging
- SMS
- Telecommunications
- Telephony
- Voice
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Telecommunications and telephony services API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

