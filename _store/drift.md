---
aid: drift
name: Drift
description: Drift is a cloud-based conversational marketing and sales platform that adds live chat, chatbots, and AI-driven engagement to websites for lead capture, routing, and conversion. Drift was acquired by Salesloft in 2024.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sales
  - Marketing
  - Conversational AI
  - Chatbots
  - Live Chat
url: https://raw.githubusercontent.com/api-evangelist/drift/refs/heads/main/apis.yml
created: '2025-02-09'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: drift:drift
    name: Drift
    description: The Drift API allows developers to build custom integrations with the Drift platform, including managing contacts, conversations, messages, accounts, users, playbooks, teams, and webhooks for chat-driven sales and marketing automation.
    humanURL: https://devdocs.drift.com
    baseURL: https://driftapi.com
    tags:
      - Sales
      - Marketing
      - Conversational AI
      - Chatbots
    properties:
      - type: Documentation
        url: https://devdocs.drift.com
      - type: OpenAPI
        url: openapi/drift-openapi.yml
      - type: Quick Start
        url: https://devdocs.drift.com/docs/quick-start-to-drift-apps
      - type: Authentication
        url: https://devdocs.drift.com/docs/authentication
      - type: Webhooks
        url: https://devdocs.drift.com/docs/webhooks
common:
  - name: Using Drift APIs
    url: https://devdocs.drift.com/docs/using-drift-apis
    type: Documentation
  - name: Using Drift APIs
    url: https://devdocs.drift.com/docs/using-drift-apis
    type: Guide
  - name: FAQs
    url: https://devdocs.drift.com/docs/faqs
    type: FAQ
  - type: Website
    url: https://www.drift.com
  - type: Features
    data:
      - Premium from $2,500/mo ($30K/year)
      - Advanced $4,500-$6,000/month
      - Enterprise $8,000-$15,000+/month
      - 'Additional seats: $50-$100/agent/month'
      - Annual contracts only (no monthly)
      - Drift AI conversational chatbot
      - Live chat with intelligent routing
      - Conversational landing pages (Advanced+)
      - Account-based engagement and routing
      - Conversation Cloud (acquired by Salesloft 2024)
      - Drift Video for personalized video
      - Drift Email Bot for email response automation
      - REST API at driftapi.com
      - Default 600 req/min/app
      - OAuth 2.0 + access tokens
      - Webhooks for messages, contacts, conversations
    sources:
      - https://www.drift.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
