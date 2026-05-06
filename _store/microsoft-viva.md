---
aid: microsoft-viva
name: Microsoft Viva
description: Microsoft Viva is an employee experience platform built on Microsoft 365 and Teams. It provides APIs for Viva Connections, Viva Learning, and Viva Insights to integrate employee experience capabilities into custom applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Employee Experience
  - Insights
  - Learning
  - Microsoft
  - Microsoft 365
url: https://raw.githubusercontent.com/api-evangelist/microsoft-viva/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-viva:connections-api
    name: Viva Connections API
    tags:
      - Adaptive Cards
      - Employee Experience
      - Intranet
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/viva/connections/overview-viva-connections
    properties:
      - url: https://learn.microsoft.com/en-us/viva/connections/overview-viva-connections
        type: Documentation
    description: Viva Connections provides a personalized employee experience gateway built on SharePoint. Developers can create custom dashboard cards using Adaptive Card Extensions (ACEs) in the SharePoint Framework, enabling employees to access company resources, tasks, and communications from a unified interface.
  - aid: microsoft-viva:learning-api
    name: Viva Learning API
    tags:
      - Learning
      - Microsoft Graph
      - Training
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/viva-learning-api-overview
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/viva-learning-api-overview
        type: Documentation
    description: The Viva Learning API through Microsoft Graph enables integration of third-party learning content providers with Microsoft Viva Learning. Developers can register learning providers, sync course catalogs, track learning assignments, and report learner activity and completion status.
  - aid: microsoft-viva:insights-api
    name: Viva Insights API
    tags:
      - Analytics
      - Insights
      - Workplace Analytics
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/viva/insights/overview
    properties:
      - url: https://learn.microsoft.com/en-us/viva/insights/overview
        type: Documentation
    description: Viva Insights provides data-driven insights about work patterns and collaboration habits. The API surfaces analytics about meeting time, focus hours, collaboration patterns, and wellbeing metrics to help organizations improve employee productivity and work-life balance.
common:
  - type: Portal
    url: https://www.microsoft365.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-viva
  - type: Documentation
    url: https://learn.microsoft.com/en-us/viva/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
