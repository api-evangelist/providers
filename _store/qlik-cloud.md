---
aid: qlik-cloud
name: Qlik Cloud
description: Collection of APIs for Qlik Cloud platform, providing data integration, analytics, and visualization capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Cloud
  - Data Integration
  - SaaS
  - Visualization
url: https://raw.githubusercontent.com/api-evangelist/qlik-cloud/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qlik-cloud:qlik-cloud-rest-api
    name: Qlik Cloud REST API
    description: Main REST API for Qlik Cloud providing access to apps, spaces, users, and resources.
    humanURL: https://qlik.dev/apis/rest
    tags:
      - Analytics
      - Data
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest
      - type: Authentication
        url: https://qlik.dev/authenticate
  - aid: qlik-cloud:qlik-engine-json-api
    name: Qlik Engine JSON API
    description: WebSocket-based JSON-RPC API for direct interaction with the Qlik Associative Engine.
    humanURL: https://qlik.dev/apis/json-rpc
    tags:
      - Engine
      - WebSocket
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/json-rpc
      - type: SDK
        url: https://github.com/qlik-oss/enigma.js
  - aid: qlik-cloud:qlik-data-integration
    name: Qlik Data Integration
    description: APIs for data integration, ETL processes, and data pipeline management.
    humanURL: https://qlik.dev/apis/rest/data-integration
    tags:
      - Data Integration
      - ETL
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-integration
  - aid: qlik-cloud:qlik-reload
    name: Qlik Reload
    description: API for managing app reloads and data refresh operations.
    humanURL: https://qlik.dev/apis/rest/reloads
    tags:
      - Reload
      - Automation
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/reloads
  - aid: qlik-cloud:qlik-users-and-groups
    name: Qlik Users and Groups
    description: Manage users, groups, and access control in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/users
    tags:
      - Users
      - IAM
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/users
  - aid: qlik-cloud:qlik-spaces
    name: Qlik Spaces
    description: Manage shared and personal spaces for organizing Qlik content.
    humanURL: https://qlik.dev/apis/rest/spaces
    tags:
      - Spaces
      - Content Management
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/spaces
  - aid: qlik-cloud:qlik-apps
    name: Qlik Apps
    description: Create, manage, and interact with Qlik Sense applications.
    humanURL: https://qlik.dev/apis/rest/apps
    tags:
      - Applications
      - Analytics
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/apps
  - aid: qlik-cloud:qlik-automations
    name: Qlik Automations
    description: Create and manage automated workflows in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/automations
    tags:
      - Automation
      - Workflows
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automations
common:
  - type: GettingStarted
    url: https://qlik.dev/get-started
  - type: Authentication
    url: https://qlik.dev/authenticate
  - type: Portal
    url: https://qlik.dev
  - type: Community
    url: https://community.qlik.com
  - type: GitHubOrganization
    url: https://github.com/qlik-oss
  - type: Status
    url: https://status.qlik.com
  - type: TermsOfService
    url: https://www.qlik.com/us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.qlik.com/us/legal/privacy
  - type: Website
    url: https://www.qlik.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
