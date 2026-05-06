---
aid: bubbles
name: Bubble
url: https://raw.githubusercontent.com/api-evangelist/bubbles/refs/heads/main/apis.yml
description: Bubble is an AI-powered no-code development platform that enables individuals and teams to design and launch scalable web applications without writing code. Bubble provides a visual programming environment for building database-backed applications, marketplaces, SaaS tools, and enterprise applications. The platform includes API connector capabilities for integrating with external services via REST APIs, webhooks, and data APIs to expose app data programmatically.
tags:
  - Applications
  - Low Code
  - No Code
  - Visual Programming
  - Webhooks
  - Web Apps
x-type: company
type: Contract
access: 3rd-Party
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: bubbles:bubble-data-api
    name: Bubble Data API
    description: The Bubble Data API allows external services to read, create, update, and delete data stored in Bubble apps via REST endpoints. The API supports authentication via API keys and exposes app data types as addressable resources for integration with third-party tools and services.
    humanURL: https://manual.bubble.io/core-resources/api/the-bubble-api/the-data-api
    baseURL: https://{app-name}.bubbleapps.io/api/1.1
    tags:
      - Data
      - REST
    properties:
      - type: Documentation
        url: https://manual.bubble.io/core-resources/api/the-bubble-api/the-data-api
      - type: Authentication
        url: https://manual.bubble.io/core-resources/api/the-bubble-api/authentication
  - aid: bubbles:bubble-workflow-api
    name: Bubble Workflow API
    description: The Bubble Workflow API enables external systems to trigger backend workflows in a Bubble app via HTTP requests. Workflows can receive data, execute business logic, and return results, supporting integration scenarios such as webhooks, automation triggers, and server-to-server communication.
    humanURL: https://manual.bubble.io/core-resources/api/the-bubble-api/the-workflow-api
    baseURL: https://{app-name}.bubbleapps.io/api/1.1/wf
    tags:
      - Automation
      - Triggers
      - Webhooks
      - Workflows
    properties:
      - type: Documentation
        url: https://manual.bubble.io/core-resources/api/the-bubble-api/the-workflow-api
common:
  - type: Website
    url: https://bubble.io
  - type: Portal
    url: https://manual.bubble.io/core-resources/api
  - type: Documentation
    url: https://manual.bubble.io
  - type: GettingStarted
    url: https://manual.bubble.io/core-resources/api
  - type: Pricing
    url: https://bubble.io/pricing
  - type: TermsOfService
    url: https://bubble.io/terms
  - type: PrivacyPolicy
    url: https://bubble.io/privacy
  - type: SignUp
    url: https://bubble.io/signup
  - type: Login
    url: https://bubble.io/login
  - type: Forum
    url: https://forum.bubble.io
  - type: Blog
    url: https://bubble.io/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
created: '2024-11-13'
modified: '2026-04-21'
---
