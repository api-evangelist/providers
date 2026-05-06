---
aid: intercom
name: Intercom
description: Intercom is an AI-powered customer service platform that enables businesses to build seamless customized experiences through its Help Desk and Messenger. The Intercom API allows developers to integrate with the Intercom platform using RESTful APIs and SDKs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Customer Service
  - Customer Support
  - Messaging
url: https://raw.githubusercontent.com/api-evangelist/intercom/refs/heads/main/apis.yml
created: '2024-07-02'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: intercom:intercom-api
    name: Intercom API
    description: The Intercom API provides programmatic access to the Intercom customer service platform. Build apps on the complete AI customer service platform and create seamless customized experiences in the Intercom Help Desk and Messenger using APIs and SDKs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.intercom.com/
    baseURL: https://api.intercom.io
    tags:
      - Customer Service
      - Messaging
      - REST
    properties:
      - type: Documentation
        url: https://developers.intercom.com/docs/
      - type: Getting Started
        url: https://developers.intercom.com/docs/get-started/
      - type: Authentication
        url: https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/
      - type: OpenAPI
        url: openapi/intercom-openapi.yml
common:
  - type: Portal
    url: https://developers.intercom.com/
  - type: Website
    url: https://www.intercom.com/
  - type: Documentation
    url: https://developers.intercom.com/docs/
  - type: Support
    url: https://www.intercom.com/help/
  - type: Sign Up
    url: https://app.intercom.com/a/signup/
  - type: Features
    data:
      - Essential at $29/seat/mo with Fin Customer Agent and Messenger
      - Advanced at $85/seat/mo with workflows automation and 20 free Lite seats
      - Expert at $132/seat/mo with SSO, HIPAA, SLAs, multibrand
      - Fin AI Agent standalone at $0.99 per resolved outcome
      - Pro AI add-on at $99/mo (CX Score, Topics, Custom Scorecards)
      - Copilot AI add-on at $29/agent/mo
      - Proactive Support Plus add-on at $99/mo
      - REST API at ~166 req/10s (1000/min) standard, 33/10s search, 16/10s bulk
      - Conversations, Contacts, Companies, Tickets, Articles APIs
      - Webhooks for real-time event delivery
      - Outbound messaging via Posts, Surveys, Tours
      - SMS and WhatsApp campaigns (usage-based)
      - Phone Plus voice support (usage-based)
      - Knowledge base and AI-powered help center
      - OAuth 2.0 and personal access tokens
      - Apps Framework for marketplace and embedded apps
    sources:
      - https://www.intercom.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
