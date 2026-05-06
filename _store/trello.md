---
aid: trello
url: https://raw.githubusercontent.com/api-evangelist/trello/refs/heads/main/apis.yml
modified: '2026-05-04'
apis:
  - aid: trello:rest-api
    name: Trello REST API
    tags:
      - Atlassian
      - Boards
      - Cards
      - Collaboration
      - Kanban
      - Project Management
      - Task Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trello.com
    humanURL: https://developer.atlassian.com/cloud/trello/rest/
    properties:
      - url: https://developer.atlassian.com/cloud/trello/rest/
        type: Documentation
      - url: openapi/trello-rest-api-openapi.yml
        type: OpenAPI
    description: The Trello REST API provides programmatic access to Trello boards, lists, cards, members, labels, checklists, and other resources that make up the Trello project management platform. Developers can create, read, update, and delete Trello objects, manage team collaboration workflows, and automate task management processes. The API uses key and token based authentication and returns JSON responses for all endpoints.
  - aid: trello:webhooks-api
    name: Trello Webhooks API
    tags:
      - Events
      - Notifications
      - Real-Time
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trello.com
    humanURL: https://developer.atlassian.com/cloud/trello/guides/rest-api/webhooks/
    properties:
      - url: https://developer.atlassian.com/cloud/trello/guides/rest-api/webhooks/
        type: Documentation
      - url: asyncapi/trello-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The Trello Webhooks API allows developers to receive real-time notifications when changes occur on Trello models such as boards, lists, and cards. Rather than polling the REST API for updates, webhooks push event data to a specified callback URL via HTTP POST requests containing JSON payloads. Webhook requests are signed with HMAC-SHA1 for verification, and webhooks are scoped to the permissions of the token used to create them.
  - aid: trello:power-ups
    name: Trello Power-Ups
    tags:
      - Customization
      - Extensions
      - Integrations
      - Plugins
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.atlassian.com/cloud/trello/power-ups/
    properties:
      - url: https://developer.atlassian.com/cloud/trello/power-ups/
        type: Documentation
    description: Trello Power-Ups are a framework for extending and integrating with the Trello platform. Power-Ups allow developers to add custom functionality to Trello boards, including custom fields, board buttons, card buttons, card badges, and card detail sections. The Power-Up framework provides a client library with utilities and helpers for interacting with the Trello interface, managing authorization, and accessing the REST API from within the Power-Up context.
common:
  - type: JSON-LD
    url: json-ld/trello-context.jsonld
  - type: JSONSchema
    url: json-schema/trello-board-schema.json
  - type: JSONSchema
    url: json-schema/trello-card-schema.json
  - type: JSONSchema
    url: json-schema/trello-webhook-payload-schema.json
  - type: JSONStructure
    url: json-structure/trello-board-structure.json
  - type: JSONStructure
    url: json-structure/trello-card-structure.json
  - type: SpectralRules
    url: rules/trello-spectral-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/project-management.yaml
  - type: Vocabulary
    url: vocabulary/trello-vocabulary.yml
  - type: Features
    data:
      - 'Free: up to 10 boards per workspace, unlimited cards'
      - 'Standard at $5/user/mo: unlimited boards, AI quick capture, custom fields'
      - 'Premium at $10/user/mo: AI, multiple views (Timeline/Calendar/Table)'
      - 'Enterprise at $17.50/user/mo: org-wide permissions, SSO via Atlassian Guard'
      - REST API at api.trello.com/1
      - 'Per API key: 300 req/10s'
      - 'Per token: 100 req/10s'
      - 'Search: 50 req/min'
      - 'Webhook deliveries: 600 events/min'
      - Power-Ups for board extensions
      - Butler automation (rules, buttons, scheduled commands)
      - Card mirroring (Standard+)
      - OAuth 1.0a + API key/token
      - Webhooks for board, list, card, member events
      - Atlassian-owned (Confluence/Jira ecosystem)
      - iOS, Android, desktop apps
    sources:
      - https://trello.com/pricing
    updated: '2026-05-04'
description: Trello is a web-based, kanban-style, list-making application that allows users to organize tasks, projects, and workflows using boards, lists, and cards.
---
