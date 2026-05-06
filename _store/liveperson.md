---
aid: liveperson
name: LivePerson
description: LivePerson is a leading provider of conversational AI and digital customer engagement technology. Their platform enables enterprises to design, deploy, and manage AI-powered messaging, voice, and agent-assisted conversations across web, mobile, and social channels, with a comprehensive suite of REST APIs covering conversation orchestration, contact center management, reporting, messaging, and security.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Conversational AI
  - Customer Engagement
  - Messaging
  - Contact Center
  - Bots
  - Chat
created: '2025-01-14'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/liveperson/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: liveperson:conversational-cloud-api
    name: LivePerson Conversational Cloud API
    description: Comprehensive set of REST APIs for managing conversations across messaging channels, including agent operations, consumer messaging, conversation history, and engagement events.
    humanURL: https://developers.liveperson.com/getting-started.html
    baseURL: https://api.liveperson.net
    tags:
      - Conversational AI
      - Messaging
      - Contact Center
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/getting-started.html
      - type: GettingStarted
        url: https://developers.liveperson.com/getting-started-with-liveperson-apis.html
      - type: Authentication
        url: https://developers.liveperson.com/login-service-api-overview.html
  - aid: liveperson:intent-manager-api
    name: LivePerson Intent Manager API
    description: Programmatic access to natural language understanding, intent recognition, and conversation classification capabilities of the LivePerson platform.
    humanURL: https://developers.liveperson.com/intent-manager-overview.html
    tags:
      - Conversational AI
      - NLU
      - Intents
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/intent-manager-overview.html
  - aid: liveperson:conversation-builder-api
    name: LivePerson Conversation Builder API
    description: APIs for designing, deploying, and managing chatbots and dialog flows built with LivePerson Conversation Builder.
    humanURL: https://developers.liveperson.com/conversation-builder-overview.html
    tags:
      - Bots
      - Conversational AI
      - Dialog
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/conversation-builder-overview.html
  - aid: liveperson:knowledgeai-api
    name: LivePerson KnowledgeAI API
    description: APIs for managing knowledge bases, articles, and AI-driven knowledge retrieval used by bots and agents in LivePerson conversations.
    humanURL: https://developers.liveperson.com/knowledgeai-api-overview.html
    tags:
      - Knowledge Base
      - AI
      - Search
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/knowledgeai-api-overview.html
  - aid: liveperson:messaging-operations-api
    name: LivePerson Messaging Operations API
    description: Real-time and historical operational metrics for messaging conversations, including queues, agent activity, and SLA performance.
    humanURL: https://developers.liveperson.com/messaging-operations-api-overview.html
    tags:
      - Analytics
      - Reporting
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/messaging-operations-api-overview.html
  - aid: liveperson:data-access-api
    name: LivePerson Data Access API
    description: Bulk historical conversation analytics and data export API for offline analysis of LivePerson messaging activity.
    humanURL: https://developers.liveperson.com/data-access-api-overview.html
    tags:
      - Analytics
      - Data Export
      - Reporting
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/data-access-api-overview.html
  - aid: liveperson:engagement-history-api
    name: LivePerson Engagement History API
    description: API for retrieving historical chat and messaging engagement records, including transcripts, attributes, and survey results.
    humanURL: https://developers.liveperson.com/engagement-history-api-overview.html
    tags:
      - History
      - Engagement
      - Analytics
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/engagement-history-api-overview.html
  - aid: liveperson:login-service-api
    name: LivePerson Login Service API
    description: Authentication API for obtaining bearer tokens for application and user access to the LivePerson Conversational Cloud APIs.
    humanURL: https://developers.liveperson.com/login-service-api-overview.html
    tags:
      - Authentication
      - Security
      - OAuth
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/login-service-api-overview.html
  - aid: liveperson:functions
    name: LivePerson Functions
    description: Serverless platform for building, deploying, and invoking custom functions that extend LivePerson conversational workflows.
    humanURL: https://developers.liveperson.com/liveperson-functions-overview.html
    tags:
      - Serverless
      - Functions
      - Extensibility
    properties:
      - type: Documentation
        url: https://developers.liveperson.com/liveperson-functions-overview.html
common:
  - type: Website
    url: https://www.liveperson.com
  - type: Portal
    url: https://developers.liveperson.com/
  - type: Documentation
    url: https://developers.liveperson.com/getting-started.html
  - type: GettingStarted
    url: https://developers.liveperson.com/getting-started-with-liveperson-apis.html
  - type: Authentication
    url: https://developers.liveperson.com/login-service-api-overview.html
  - type: StatusPage
    url: https://status.liveperson.com/
  - type: Blog
    url: https://www.liveperson.com/resources/blog/
  - type: GitHubOrganization
    url: https://github.com/LivePersonInc
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
