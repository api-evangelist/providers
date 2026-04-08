---
aid: microsoft-viva
url: https://raw.githubusercontent.com/api-evangelist/microsoft-viva/refs/heads/main/apis.yml
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
name: Microsoft Viva
tags:
- Employee Experience
- Insights
- Learning
- Microsoft
- Microsoft 365
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Viva is an employee experience platform built on Microsoft 365 and Teams. It provides APIs for Viva Connections, Viva Learning, and Viva Insights to integrate employee experience capabilities into custom applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

