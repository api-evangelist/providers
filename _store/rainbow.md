---
aid: rainbow
name: Rainbow
description: Rainbow is a CPaaS platform from Alcatel-Lucent Enterprise (ALE) that lets developers enrich applications with chat, group chat, voice, video, file sharing, and telephony PBX features through more than 200 APIs, REST interfaces, and multi-language SDKs including Node.js, C#, iOS, and Android.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Communications
  - CPaaS
  - Chat
  - Voice
  - Video
  - Telephony
  - Messaging
  - Collaboration
  - Unified Communications
created: '2025-02-06'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/rainbow/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: rainbow:rainbow-application-api
    name: Rainbow Application Portal API
    description: The Rainbow Application Portal REST API allows developers to manage Rainbow applications, register OAuth clients, and access provisioning and administration functions for the Rainbow platform.
    humanURL: https://developers.openrainbow.com/doc/hub/api
    baseURL: https://openrainbow.com/api/rainbow
    tags:
      - Applications
      - Administration
      - OAuth
      - Provisioning
    properties:
      - type: Documentation
        url: https://developers.openrainbow.com/doc/hub/api
      - type: OpenAPI
        url: openapi/rainbow-application-openapi.yml
  - aid: rainbow:rainbow-messaging-api
    name: Rainbow Messaging API
    description: REST API for sending and receiving messages, managing conversations, and handling chat bubbles (group rooms) within the Rainbow platform.
    humanURL: https://developers.openrainbow.com/
    baseURL: https://openrainbow.com/api/rainbow
    tags:
      - Messaging
      - Chat
      - Conversations
      - Bubbles
    properties:
      - type: Documentation
        url: https://developers.openrainbow.com/doc/hub/api
      - type: OpenAPI
        url: openapi/rainbow-messaging-openapi.yml
  - aid: rainbow:rainbow-contacts-api
    name: Rainbow Contacts API
    description: REST API for searching, listing, and managing contacts in the Rainbow directory, including enterprise contacts and public profiles.
    humanURL: https://developers.openrainbow.com/
    baseURL: https://openrainbow.com/api/rainbow
    tags:
      - Contacts
      - Directory
      - Search
    properties:
      - type: Documentation
        url: https://developers.openrainbow.com/doc/hub/api
      - type: OpenAPI
        url: openapi/rainbow-contacts-openapi.yml
common:
  - type: Website
    url: https://www.openrainbow.com
  - type: Developer
    url: https://developers.openrainbow.com/
  - type: SignUp
    url: https://hub.openrainbow.com/
  - type: GitHub
    url: https://github.com/Rainbow-CPaaS
  - type: SDKNode
    url: https://github.com/Rainbow-CPaaS/Rainbow-Node-SDK
  - type: SDKIOS
    url: https://github.com/Rainbow-CPaaS/Rainbow-iOS-SDK
  - type: SDKCS
    url: https://github.com/Rainbow-CPaaS/Rainbow-CSharp-SDK-Samples
  - type: CLI
    url: https://github.com/Rainbow-CPaaS/Rainbow-CLI-SDK
  - type: SpectralRules
    url: rules/rainbow-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/communications-platform.yaml
  - type: JSONLD
    url: json-ld/rainbow-context.jsonld
  - type: Vocabulary
    url: vocabulary/rainbow-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
