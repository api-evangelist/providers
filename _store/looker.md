---
aid: looker
url: https://raw.githubusercontent.com/api-evangelist/looker/refs/heads/main/apis.yml
apis:
- name: Looker API
  description: The Looker API provides programmatic access to Looker functionality including running queries, managing users, creating dashboards, and administering the platform.
  image: https://looker.com/assets/img/images/logos/looker-logo.png
  humanURL: https://developers.looker.com/api/explorer/4.0
  baseURL: https://your-instance.looker.com:19999/api/4.0
  tags:
  - Analytics
  - Dashboards
  - Queries
  - REST API
  properties:
  - type: Documentation
    url: https://developers.looker.com/api/getting-started
  - type: OpenAPI
    url: https://raw.githubusercontent.com/looker-open-source/sdk-codegen/main/spec/Looker.4.0.oas.json
  - type: OpenAPI
    url: openapi/looker-api-openapi.yml
  - type: Authentication
    url: https://developers.looker.com/api/getting-started#authentication
  - type: SDKs
    url: https://developers.looker.com/api/sdks
  - type: API Explorer
    url: https://developers.looker.com/api/explorer/4.0
  - type: Rate Limits
    url: https://cloud.google.com/looker/docs/api-rate-limits
  - type: API Reference
    url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest
  - type: Getting Started
    url: https://docs.cloud.google.com/looker/docs/api-getting-started
  - type: API Overview
    url: https://docs.cloud.google.com/looker/docs/api-overview
  - type: API Versioning
    url: https://docs.cloud.google.com/looker/docs/api-versioning
  - type: API Authentication
    url: https://docs.cloud.google.com/looker/docs/api-auth
  - type: OAuth Authentication
    url: https://docs.cloud.google.com/looker/docs/api-cors
  - type: API Support Policy
    url: https://docs.cloud.google.com/looker/docs/api-sdk-support-policy
- name: LookML API
  description: API for programmatically managing LookML projects, models, and views.
  humanURL: https://developers.looker.com/api/explorer/4.0/methods/Project
  baseURL: https://your-instance.looker.com:19999/api/4.0
  tags:
  - Data Modeling
  - LookML
  - Projects
  properties:
  - type: Documentation
    url: https://developers.looker.com/api/explorer/4.0/methods/Project
  - type: Tutorials
    url: https://developers.looker.com/api/lookml-validation
- name: Looker Action API
  description: The Looker Action API enables developers to define custom actions, or destinations, to which Looker can send query results, dashboard results, or user interactions via a webhook-like API.
  humanURL: https://docs.cloud.google.com/looker/docs/actions-overview
  baseURL: https://your-instance.looker.com:19999/api/4.0
  tags:
  - Actions
  - Data Delivery
  - Integrations
  - Webhooks
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/looker/docs/actions-overview
  - type: Action Hub
    url: https://docs.cloud.google.com/looker/docs/action-hub
  - type: GitHub Repository
    url: https://github.com/looker-open-source/actions
  - type: Action API Specification
    url: https://github.com/looker-open-source/actions/blob/master/docs/action_api.md
  - type: Custom Action Hub Example
    url: https://github.com/looker-open-source/custom-action-hub-example
- name: Looker Embed SDK
  description: The Looker Embed SDK is a JavaScript library for embedding Looker content such as dashboards, Looks, Explores, reports, and extensions into web applications, with support for signed SSO and cookieless authentication.
  humanURL: https://docs.cloud.google.com/looker/docs/embed-sdk-intro
  baseURL: https://your-instance.looker.com:19999/api/4.0
  tags:
  - Dashboards
  - Embedding
  - JavaScript SDK
  - SSO
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/looker/docs/embed-sdk-intro
  - type: GitHub Repository
    url: https://github.com/looker-open-source/embed-sdk
  - type: API Reference
    url: https://looker-open-source.github.io/embed-sdk/
  - type: npm Package
    url: https://www.npmjs.com/package/@looker/embed-sdk
  - type: SSO Embedding
    url: https://cloud.google.com/looker/docs/single-sign-on-embedding
  - type: Embed SSO Examples
    url: https://github.com/looker/looker_embed_sso_examples
- name: Looker Extension Framework API
  description: The Looker Extension Framework provides APIs and SDKs for building custom extensions that run inside the Looker UI, with access to the Looker API, Looker components library, and the Embed SDK.
  humanURL: https://developers.looker.com/extensions/overview/
  baseURL: https://your-instance.looker.com:19999/api/4.0
  tags:
  - Extensions
  - JavaScript
  - React
  - UI Components
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/looker/docs/intro-to-extension-framework
  - type: Extension Framework Overview
    url: https://docs.cloud.google.com/looker/docs/extension-framework
  - type: Code Examples
    url: https://docs.cloud.google.com/looker/docs/extension-framework-react-and-js-code-examples
  - type: GitHub Examples
    url: https://github.com/looker-open-source/extension-examples
  - type: npm Package
    url: https://www.npmjs.com/package/@looker/extension-sdk
- name: Looker (Google Cloud core) API
  description: The Looker (Google Cloud core) REST API provides management capabilities for Looker instances running on Google Cloud, including instance lifecycle management, backups, and operations.
  humanURL: https://cloud.google.com/looker/docs/reference/rest
  baseURL: https://looker.googleapis.com/v1
  tags:
  - Backups
  - Google Cloud
  - Infrastructure
  - Instance Management
  properties:
  - type: Documentation
    url: https://cloud.google.com/looker/docs/reference/rest
  - type: Looker Core Overview
    url: https://docs.cloud.google.com/looker/docs/looker-core-overview
  - type: Looker Core Documentation
    url: https://docs.cloud.google.com/looker/docs/looker-core
  - type: Google Cloud Console
    url: https://console.cloud.google.com/apis/library/looker.googleapis.com
name: Looker
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
type: Contract
image: https://looker.com/assets/img/images/logos/looker-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Looker is a business intelligence and data analytics platform that enables organizations to explore, analyze, and share real-time business analytics.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

