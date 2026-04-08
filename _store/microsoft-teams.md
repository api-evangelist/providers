---
aid: microsoft-teams
url: https://raw.githubusercontent.com/api-evangelist/microsoft-teams/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph Teams API
  description: Core API for accessing Teams data including teams, channels, messages, tabs, and apps through Microsoft Graph.
  image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
  humanURL: https://docs.microsoft.com/en-us/graph/teams-concept-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Channels
  - Messages
  - Microsoft Graph
  - REST API
  - Teams
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Rate Limits
    url: https://docs.microsoft.com/en-us/graph/throttling
- name: Microsoft Teams Bot Framework API
  description: API for building conversational bots that interact with users in Microsoft Teams.
  humanURL: https://docs.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots
  baseURL: https://smba.trafficmanager.net/teams/
  tags:
  - Bot Framework
  - Bots
  - Conversational AI
  - Messaging
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/bots/how-to/conversations/conversation-basics
  - type: Quickstart
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/build-your-first-app/build-bot
  - type: Samples
    url: https://github.com/microsoft/BotBuilder-Samples
  - type: Schema
    url: https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference
- name: Microsoft Teams Webhook and Connector API
  description: APIs for creating incoming webhooks and Office 365 connectors to post messages to Teams channels.
  humanURL: https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors
  baseURL: https://outlook.office.com/webhook/
  tags:
  - Connectors
  - Incoming Webhooks
  - Notifications
  - Webhooks
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook
  - type: Message Card Reference
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference
  - type: Adaptive Cards
    url: https://adaptivecards.io/
- name: Microsoft Teams Real-time Communication APIs
  description: APIs for building calling and meeting experiences in Teams using Azure Communication Services.
  humanURL: https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/calls-and-meetings/calls-meetings-bots-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Audio
  - Calling
  - Meetings
  - Real-Time
  - Video
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/communications-api-overview
  - type: Cloud Communications API
    url: https://docs.microsoft.com/en-us/graph/api/resources/call
  - type: Meeting API
    url: https://docs.microsoft.com/en-us/graph/api/resources/onlinemeeting
- name: Microsoft Teams App Manifest API
  description: Schema and APIs for Teams app manifest configuration and deployment.
  humanURL: https://docs.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema
  tags:
  - App Manifest
  - Configuration
  - Deployment
  - Schema
  properties:
  - type: Schema Documentation
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema
  - type: App Submission
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/submission-checklist
  - type: Developer Portal
    url: https://dev.teams.microsoft.com/
name: Microsoft Teams
tags:
- Chat
- Collaboration
- Communication
- Productivity
- Video Conferencing
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/01/Microsoft-Teams-icon.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Teams is a collaboration platform that combines workplace chat, meetings, file storage, and application integration. It provides APIs for building custom integrations and extending Teams functionality.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

