---
aid: microsoft-teams
name: Microsoft Teams
description: Microsoft Teams is a collaboration platform that combines workplace chat, meetings, file storage, and application integration. It provides APIs for building custom integrations, managing teams and channels, sending messages, scheduling meetings, and initiating calls through Microsoft Graph.
image: https://learn.microsoft.com/en-us/graph/images/teams-logo.png
url: https://raw.githubusercontent.com/api-evangelist/microsoft-teams/refs/heads/main/apis.yml
humanURL: https://www.microsoft.com/en-us/microsoft-teams
created: '2024'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
tags:
  - Chat
  - Collaboration
  - Communication
  - Microsoft 365
  - Productivity
  - Video Conferencing
apis:
  - name: Microsoft Graph Teams API
    description: Core REST API for accessing Teams data including teams, channels, messages, tabs, apps, members, online meetings, and calls through Microsoft Graph.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Channels
      - Messages
      - Microsoft Graph
      - REST API
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
      - type: OpenAPI
        url: openapi/microsoft-teams-graph-api.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: RateLimits
        url: https://learn.microsoft.com/en-us/graph/throttling
      - type: JSONSchema
        url: json-schema/teams-graph-api-team-schema.json
      - type: JSONSchema
        url: json-schema/teams-graph-api-channel-schema.json
      - type: JSONSchema
        url: json-schema/teams-graph-api-chat-message-schema.json
      - type: JSONSchema
        url: json-schema/teams-graph-api-conversation-member-schema.json
      - type: JSONSchema
        url: json-schema/teams-graph-api-online-meeting-schema.json
      - type: JSONSchema
        url: json-schema/teams-graph-api-call-schema.json
      - type: JSONStructure
        url: json-structure/teams-graph-api-team-structure.json
      - type: JSON-LD
        url: json-ld/microsoft-teams-graph-api-context.jsonld
      - type: Example
        url: examples/teams-graph-api-team-example.json
      - type: Example
        url: examples/teams-graph-api-channel-example.json
      - type: Example
        url: examples/teams-graph-api-chat-message-example.json
  - name: Microsoft Teams Bot Framework API
    description: API for building conversational bots that interact with users in Microsoft Teams through the Bot Framework.
    humanURL: https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots
    baseURL: https://smba.trafficmanager.net/teams/
    tags:
      - Bot Framework
      - Bots
      - Conversational AI
      - Messaging
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/conversations/conversation-basics
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/build-your-first-app/build-bot
      - type: CodeExamples
        url: https://github.com/microsoft/BotBuilder-Samples
        title: Bot Builder Samples
      - type: APIReference
        url: https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference
  - name: Microsoft Teams Webhook and Connector API
    description: APIs for creating incoming webhooks and Office 365 connectors to post messages and notifications to Teams channels.
    humanURL: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors
    baseURL: https://outlook.office.com/webhook/
    tags:
      - Connectors
      - Incoming Webhooks
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook
  - name: Microsoft Teams Real-Time Communication APIs
    description: APIs for building calling and meeting experiences in Teams including VoIP calls, group calls, IVR flows, and online meetings.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/communications-api-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Audio
      - Calling
      - Meetings
      - Real-Time
      - Video
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/communications-api-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/call
common:
  - type: DeveloperPortal
    url: https://developer.microsoft.com/en-us/microsoft-teams
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/microsoftteams/platform/get-started/get-started-overview
  - type: SDK
    url: https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals
    title: Teams Toolkit
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/microsoft-teams-blog/bg-p/MicrosoftTeamsBlog
  - type: Support
    url: https://learn.microsoft.com/en-us/answers/products/office-teams
  - type: GitHubOrganization
    url: https://github.com/OfficeDev/Microsoft-Teams-Samples
  - type: StatusPage
    url: https://status.teams.microsoft.com/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: rules/microsoft-teams-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/team-collaboration.yaml
  - type: Vocabulary
    url: vocabulary/microsoft-teams-vocabulary.yaml
  - type: Features
    data:
      - 'Microsoft Teams: hundreds of services across Collaboration'
      - 'Detailed pricing: see https://www.microsoft.com/en-us/microsoft-teams/compare-microsoft-teams-options'
      - 'Service: Microsoft Graph - Teams API'
      - 'Service: Bot Framework'
      - 'Service: Adaptive Cards'
      - 'Service: Teams Toolkit'
      - 'Service: Teams Meeting API'
      - 'Service: Teams Webhook API'
      - 'Service: Teams Communication Services'
      - 'Service: PSTN Calling'
      - 'Service: Teams Phone'
    sources:
      - https://www.microsoft.com/en-us/microsoft-teams/compare-microsoft-teams-options
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Team Provisioning
        description: Automate creation and configuration of teams for projects.
      - name: Messaging Automation
        description: Send automated notifications and updates to channels.
      - name: Meeting Scheduling
        description: Programmatically create and manage online meetings.
      - name: Customer Service Bots
        description: Build conversational bots for customer support in Teams.
      - name: Workforce Management
        description: Manage shifts and schedules for frontline workers.
  - type: Integrations
    data:
      - name: Microsoft Power Automate
        description: Automate Teams workflows with Power Automate connectors.
      - name: SharePoint
        description: Teams channels with SharePoint document libraries.
      - name: OneDrive
        description: Share and collaborate on files in Teams via OneDrive.
      - name: Azure Bot Service
        description: Build and deploy bots using Azure Bot Service.
      - name: Adaptive Cards
        description: Rich interactive cards for messaging and notifications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
