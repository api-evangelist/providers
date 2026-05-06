---
aid: gong
name: Gong
description: Gong is a revenue intelligence platform that captures and analyzes customer interactions across phone, web conferencing, and email to provide insights for sales teams.
type: Index
position: Consumer
access: 3rd-Party
image: https://www.gong.io/wp-content/uploads/2021/04/gong-logo.svg
tags: []
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/gong/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: gong:gong-calls-api
    name: Gong Calls API
    description: The Gong Calls API provides endpoints to retrieve, add, and manage call data including recordings, transcripts, and media files. It supports filtering calls by date range, retrieving detailed call analytics, and uploading call recordings from external telephony systems.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Calls
      - Conversations
      - Recordings
      - Transcripts
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: Getting Started
        url: https://help.gong.io/docs/how-to-use-the-gong-developers-hub
      - type: PostmanWorkspace
        url: https://www.postman.com/growment/gong-meetup/collection/yuikwaq/gong-api-beginners-guide
      - type: OpenAPI
        url: openapi/gong-calls-openapi.yml
  - aid: gong:gong-users-api
    name: Gong Users API
    description: The Gong Users API allows retrieval of user information, user histories, and filtering of users by various criteria. It provides access to team member profiles and licensing details within the Gong platform.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Profiles
      - Teams
      - Users
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-users-openapi.yml
  - aid: gong:gong-stats-api
    name: Gong Stats API
    description: The Gong Stats API provides access to activity metrics including user interaction statistics, answered scorecards, talk ratios, and aggregated user activity data for performance tracking and analytics.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Analytics
      - Metrics
      - Performance
      - Statistics
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-stats-openapi.yml
  - aid: gong:gong-crm-api
    name: Gong CRM API
    description: The Gong CRM API enables integration with CRM systems by providing endpoints to register integrations, upload CRM objects and schemas, map users and fields, and manage associations between calls and CRM records.
    humanURL: https://help.gong.io/docs/manage-your-crm-api-integration
    baseURL: https://api.gong.io/v2/
    tags:
      - Accounts
      - CRM
      - Deals
      - Integrations
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/manage-your-crm-api-integration
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-crm-openapi.yml
  - aid: gong:gong-engage-api
    name: Gong Engage API
    description: The Gong Engage API lets you manage and customize Engage flows at scale, with endpoints to list available flows and folders, assign or unassign prospects, and override flow content to tailor messaging for specific campaigns or workflows.
    humanURL: https://help.gong.io/docs/gong-engage-api-capabilities
    baseURL: https://api.gong.io/v2/
    tags:
      - Automation
      - Flows
      - Outreach
      - Prospects
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/gong-engage-api-capabilities
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-engage-openapi.yml
  - aid: gong:gong-settings-api
    name: Gong Settings API
    description: The Gong Settings API provides endpoints to retrieve scorecard configurations and list all company workspaces, enabling programmatic access to organizational settings and evaluation frameworks.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Scorecards
      - Settings
      - Workspaces
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-settings-openapi.yml
  - aid: gong:gong-library-api
    name: Gong Library API
    description: The Gong Library API provides access to the library structure and calls stored in specific folders, enabling programmatic browsing and retrieval of curated call content.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Content
      - Folders
      - Library
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-library-openapi.yml
  - aid: gong:gong-permissions-api
    name: Gong Permissions API
    description: The Gong Permissions API manages access controls through permission profiles and user call access assignments, enabling programmatic configuration of who can access specific calls and features.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Access Control
      - Permissions
      - Security
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-permissions-openapi.yml
  - aid: gong:gong-data-privacy-api
    name: Gong Data Privacy API
    description: The Gong Data Privacy API provides data protection capabilities including finding references to email addresses and phone numbers, and purging associated data to support compliance with privacy regulations.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Compliance
      - Data Protection
      - Privacy
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-data-privacy-openapi.yml
  - aid: gong:gong-auditing-api
    name: Gong Auditing API
    description: The Gong Auditing API enables retrieval of audit log data by type and time range, providing visibility into user actions and system events for compliance and security monitoring.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Auditing
      - Compliance
      - Logs
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-auditing-openapi.yml
  - aid: gong:gong-meetings-api
    name: Gong Meetings API
    description: The Gong Meetings API provides endpoints to create, update, and delete Gong meetings, as well as validate meeting integration status for scheduling and managing meeting workflows.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Collaboration
      - Meetings
      - Scheduling
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-meetings-openapi.yml
  - aid: gong:gong-engagement-api
    name: Gong Engagement API
    description: The Gong Engagement API reports customer engagement events including content sharing, content viewing, and custom actions, providing visibility into how prospects interact with shared materials.
    humanURL: https://help.gong.io/docs/what-the-gong-api-provides
    baseURL: https://api.gong.io/v2/
    tags:
      - Content Sharing
      - Engagement
      - Tracking
    properties:
      - type: Documentation
        url: https://help.gong.io/docs/what-the-gong-api-provides
      - type: Reference
        url: https://app.gong.io/settings/api/documentation
      - type: Authentication
        url: https://help.gong.io/docs/receive-access-to-the-api
      - type: OpenAPI
        url: openapi/gong-engagement-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://app.gong.io
  - type: Developer Portal
    url: https://help.gong.io/docs/how-to-use-the-gong-developers-hub
  - type: Documentation
    url: https://help.gong.io/docs/what-the-gong-api-provides
  - type: Reference
    url: https://app.gong.io/settings/api/documentation
  - type: Getting Started
    url: https://help.gong.io/docs/how-to-use-the-gong-developers-hub
  - type: Authentication
    url: https://help.gong.io/docs/receive-access-to-the-api
  - type: OAuth
    url: https://help.gong.io/docs/create-an-app-for-gong
  - type: Sandbox
    url: https://help.gong.io/docs/set-up-a-developer-instance
  - type: Webhooks
    url: https://help.gong.io/docs/create-a-webhook-rule
  - type: Change Log
    url: https://help.gong.io/docs/release-notes
  - type: Blog
    url: https://www.gong.io/blog/
  - type: Engineering Blog
    url: https://medium.com/gong-tech-blog
  - type: Status
    url: https://status.gong.io
  - type: Support
    url: https://help.gong.io
  - type: Community
    url: https://visioneers.gong.io
  - type: Learning Center
    url: https://academy.gong.io
  - type: Integrations
    url: https://integrations.gong.io/all
  - type: Marketplace
    url: https://www.gong.io/collective
  - type: PostmanWorkspace
    url: https://www.postman.com/growment/gong-meetup/collection/yuikwaq/gong-api-beginners-guide
  - type: Sign Up
    url: https://www.gong.io/get-started/
  - type: Developer Sign Up
    url: https://app.gong.io/welcome/developer/sign-up
  - type: Login
    url: https://app.gong.io/login
  - type: Terms of Service
    url: https://www.gong.io/terms-of-service/
  - type: Privacy Policy
    url: https://www.gong.io/privacy-policy/
  - type: Security
    url: https://www.gong.io/security
  - type: Trust
    url: https://trust.gong.io
  - type: Pricing
    url: https://www.gong.io/pricing
  - type: About
    url: https://www.gong.io/about
  - type: Contact
    url: https://www.gong.io/contact-us/
  - type: GitHub Organization
    url: https://github.com/gong-io
  - type: Website
    url: https://www.gong.io
  - type: JSONSchema
    url: json-schema/gong-call-schema.json
  - type: JSONSchema
    url: json-schema/gong-user-schema.json
  - type: JSONSchema
    url: json-schema/gong-flow-schema.json
  - type: JSONSchema
    url: json-schema/gong-scorecard-schema.json
  - type: JSONSchema
    url: json-schema/gong-workspace-schema.json
  - type: JSONSchema
    url: json-schema/gong-meeting-schema.json
  - type: JSONSchema
    url: json-schema/gong-transcript-schema.json
  - type: JSONSchema
    url: json-schema/gong-prospect-schema.json
  - type: JSONLD
    url: json-ld/gong-context.jsonld
---
