---
aid: trello
url: https://raw.githubusercontent.com/api-evangelist/trello/refs/heads/main/apis.yml
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
name: Trello
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Trello is a web-based, kanban-style, list-making application that allows users to organize tasks, projects, and workflows using boards, lists, and cards.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

