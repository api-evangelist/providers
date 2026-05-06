---
name: Sentry
description: Sentry is an open-source error tracking and performance monitoring platform that helps developers identify, triage, and resolve issues in their applications in real-time.
image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
created: '2024-01-15'
modified: '2026-03-04'
specificationVersion: '0.18'
url: https://sentry.io/apis.json
apis:
  - name: Sentry API
    description: The Sentry API provides programmatic access to Sentry's error tracking, performance monitoring, and organizational data. It allows developers to manage projects, issues, releases, and more.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://sentry.io
    baseURL: https://sentry.io/api/0
    tags:
      - Error Tracking
      - Monitoring
      - Observability
      - Performance
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-api-openapi.yml
      - type: Authentication
        url: https://docs.sentry.io/api/auth/
      - type: Getting Started
        url: https://docs.sentry.io/api/guides/create-auth-token/
      - type: Rate Limits
        url: https://docs.sentry.io/api/ratelimits/
      - type: SDKs
        url: https://docs.sentry.io/platforms/
      - type: PostmanCollection
        url: https://www.postman.com/sentryio/sentry-api-collection/documentation/xtzhckg/sentry-api-collection
      - type: Webhooks
        url: https://docs.sentry.io/organization/integrations/integration-platform/webhooks/
      - type: Pagination
        url: https://docs.sentry.io/api/pagination/
      - type: Permissions
        url: https://docs.sentry.io/api/permissions/
      - type: Reference
        url: https://docs.sentry.io/api/requests/
      - type: JSONSchema
        url: json-schema/sentry-organization-schema.json
      - type: JSONSchema
        url: json-schema/sentry-project-schema.json
      - type: JSONSchema
        url: json-schema/sentry-issue-schema.json
      - type: JSONSchema
        url: json-schema/sentry-event-schema.json
      - type: JSONSchema
        url: json-schema/sentry-team-schema.json
      - type: JSONSchema
        url: json-schema/sentry-release-schema.json
      - type: JSONSchema
        url: json-schema/sentry-alert-rule-schema.json
      - type: JSONSchema
        url: json-schema/sentry-monitor-schema.json
      - type: JSONSchema
        url: json-schema/sentry-replay-schema.json
      - type: JSONLD
        url: json-ld/sentry-context.jsonld
    contact:
      - type: Support
        url: https://sentry.io/support/
      - type: Email
        url: support@sentry.io
      - type: Twitter
        url: https://twitter.com/getsentry
      - type: GitHub
        url: https://github.com/getsentry
  - name: Sentry Events and Issues API
    description: The Events and Issues API provides endpoints for managing error events and issues in Sentry, including listing, retrieving, updating, and bulk-mutating issues and their associated events, tags, and hashes.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/events/
    baseURL: https://sentry.io/api/0
    tags:
      - Debugging
      - Error Tracking
      - Events
      - Issues
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/events/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-events-issues-openapi.yml
  - name: Sentry Organizations API
    description: The Organizations API provides endpoints for managing Sentry organizations, including retrieving and updating organization details, managing members and their roles, listing projects and repositories, and resolving event and short IDs.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/organizations/
    baseURL: https://sentry.io/api/0
    tags:
      - Administration
      - Members
      - Organizations
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/organizations/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-organizations-openapi.yml
  - name: Sentry Projects API
    description: The Projects API provides endpoints for managing Sentry projects, including creating, retrieving, updating, and deleting projects, as well as managing client keys, debug files, service hooks, filters, and user feedback.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/projects/
    baseURL: https://sentry.io/api/0
    tags:
      - Configuration
      - Management
      - Projects
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/projects/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-projects-openapi.yml
  - name: Sentry Teams API
    description: The Teams API provides endpoints for managing teams within Sentry organizations, including creating, retrieving, updating, and deleting teams, managing team members and their roles, and listing projects associated with teams.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/teams/
    baseURL: https://sentry.io/api/0
    tags:
      - Collaboration
      - Members
      - Teams
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/teams/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-teams-openapi.yml
  - name: Sentry Releases API
    description: The Releases API provides endpoints for managing software releases in Sentry, including creating and managing releases, uploading release files, listing commits, managing deployments, and retrieving release health session statistics.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/releases/
    baseURL: https://sentry.io/api/0
    tags:
      - Deployments
      - Releases
      - Version Management
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/releases/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-releases-openapi.yml
  - name: Sentry Alerts API
    description: The Alerts API provides endpoints for managing alert rules in Sentry, including creating, retrieving, updating, and deleting metric alert rules and issue alert rules, as well as managing spike protection notification actions.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/alerts/
    baseURL: https://sentry.io/api/0
    tags:
      - Alerts
      - Monitoring
      - Notifications
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/alerts/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-alerts-openapi.yml
  - name: Sentry Crons API
    description: The Crons API provides endpoints for managing cron job monitors in Sentry, including creating, retrieving, updating, and deleting monitors, managing monitor environments, and retrieving check-in history for tracked scheduled tasks.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/crons/
    baseURL: https://sentry.io/api/0
    tags:
      - Crons
      - Monitoring
      - Scheduled Tasks
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/crons/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-crons-openapi.yml
  - name: Sentry Dashboards API
    description: The Dashboards API provides endpoints for managing custom dashboards in Sentry organizations, including creating, listing, retrieving, editing, and deleting dashboards for visualizing error and performance data.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/dashboards/
    baseURL: https://sentry.io/api/0
    tags:
      - Analytics
      - Dashboards
      - Visualization
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/dashboards/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-dashboards-openapi.yml
  - name: Sentry Discover API
    description: The Discover and Performance API provides endpoints for managing saved queries in Sentry, allowing you to create, list, retrieve, edit, and delete organization-level Discover saved queries for slicing and analyzing error and transaction event data.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/discover/
    baseURL: https://sentry.io/api/0
    tags:
      - Analytics
      - Discover
      - Performance
      - Queries
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/discover/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-discover-openapi.yml
  - name: Sentry Environments API
    description: The Environments API provides endpoints for managing environments in Sentry, including listing project and organization environments, retrieving individual project environment details, and updating project environment settings.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/environments/
    baseURL: https://sentry.io/api/0
    tags:
      - Configuration
      - Environments
      - Management
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/environments/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-environments-openapi.yml
  - name: Sentry Explore API
    description: The Explore API provides endpoints for querying and analyzing event data in Sentry, allowing you to slice and dice events in both table and timeseries formats for flexible data analysis and visualization.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/explore/
    baseURL: https://sentry.io/api/0
    tags:
      - Analytics
      - Events
      - Explore
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/explore/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-explore-openapi.yml
  - name: Sentry Integration Platform API
    description: The Integration Platform API provides endpoints for managing custom integrations in Sentry, including creating and updating external issues, managing integration configurations, listing installations, and retrieving organization-level custom integration details.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/integration/
    baseURL: https://sentry.io/api/0
    tags:
      - Integrations
      - Platform
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/integration/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-integration-platform-openapi.yml
  - name: Sentry Integrations API
    description: The Integrations API provides endpoints for managing third-party integrations within Sentry organizations, including creating and managing data forwarders, handling external user and team records, and controlling integration configurations.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/integrations/
    baseURL: https://sentry.io/api/0
    tags:
      - Configuration
      - Data Forwarding
      - Integrations
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/integrations/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-integrations-openapi.yml
  - name: Sentry Mobile Builds API
    description: The Mobile Builds API provides endpoints for analyzing mobile application artifacts in Sentry, including retrieving install information and size analysis results for mobile build artifacts.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/mobile-builds/
    baseURL: https://sentry.io/api/0
    tags:
      - Artifacts
      - Builds
      - Mobile
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/mobile-builds/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-mobile-builds-openapi.yml
  - name: Sentry Monitors API
    description: The Monitors and Alerts API provides beta endpoints for managing monitors and alerts in Sentry, including creating, retrieving, updating, and deleting monitors and alerts, as well as bulk operations at the organization level.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/monitors/
    baseURL: https://sentry.io/api/0
    tags:
      - Alerts
      - Monitors
      - Uptime
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/monitors/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-monitors-openapi.yml
  - name: Sentry Prevent API
    description: The Prevent API provides endpoints for managing repository integrations and test results in Sentry, including syncing repositories, managing branches, generating upload tokens, and retrieving test result metrics and test suites.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/prevent/
    baseURL: https://sentry.io/api/0
    tags:
      - Quality Assurance
      - Repositories
      - Testing
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/prevent/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-prevent-openapi.yml
  - name: Sentry Replays API
    description: The Replays API provides endpoints for managing session replays in Sentry, including listing, retrieving, and deleting replay instances, accessing recording segments, listing clicked nodes and selectors, and retrieving replay counts for issues or transactions.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/replays/
    baseURL: https://sentry.io/api/0
    tags:
      - Replays
      - Session Recording
      - User Experience
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/replays/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-replays-openapi.yml
  - name: Sentry SCIM API
    description: The SCIM API provides endpoints for federated identity management in Sentry, enabling automated provisioning and deprovisioning of organization members and teams using the System for Cross-Domain Identity Management standard. Requires a Business Plan with SAML2 enabled.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/scim/
    baseURL: https://sentry.io/api/0
    tags:
      - Enterprise
      - Identity Management
      - Provisioning
      - SCIM
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/scim/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-scim-openapi.yml
  - name: Sentry Seer API
    description: The Seer API provides endpoints for AI-powered issue analysis in Sentry, including listing available AI models, starting AI-assisted issue fixes, and retrieving the state of ongoing fix analyses.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/seer/
    baseURL: https://sentry.io/api/0
    tags:
      - AI
      - Automation
      - Issue Analysis
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/seer/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-seer-openapi.yml
  - name: Sentry Users API
    description: The Users API provides endpoints for retrieving user-related information in Sentry, including listing the organizations that the authenticated user belongs to.
    image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
    humanURL: https://docs.sentry.io/api/users/
    baseURL: https://sentry.io/api/0
    tags:
      - Accounts
      - Authentication
      - Users
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/users/
      - type: OpenAPI
        url: https://github.com/getsentry/sentry-api-schema/blob/main/openapi-derefed.json
      - type: OpenAPI
        url: openapi/sentry-users-openapi.yml
common:
  - type: Portal
    url: https://sentry.io/
  - type: Website
    url: https://sentry.io/
  - type: Documentation
    url: https://docs.sentry.io/
  - type: Getting Started
    url: https://docs.sentry.io/product/sentry-basics/
  - type: Authentication
    url: https://docs.sentry.io/api/auth/
  - type: Pricing
    url: https://sentry.io/pricing/
  - type: Blog
    url: https://blog.sentry.io/
  - type: GitHub Organization
    url: https://github.com/getsentry
  - type: Discord
    url: https://discord.gg/sentry
  - type: Sign Up
    url: https://sentry.io/signup/
  - type: Login
    url: https://sentry.io/auth/login/
  - type: Support
    url: https://sentry.zendesk.com/hc/en-us/
  - type: Forum
    url: https://forum.sentry.io/
  - type: Change Log
    url: https://sentry.io/changelog/
  - type: Security
    url: https://sentry.io/security/
  - type: Community
    url: https://sentry.io/community/
  - type: Self-Hosted
    url: https://docs.sentry.io/server/
  - type: Developer Documentation
    url: https://develop.sentry.dev/
  - type: CLI
    url: https://docs.sentry.io/cli/
  - type: SDKs
    url: https://docs.sentry.io/platforms/
  - type: Status
    url: https://status.sentry.io/
  - type: Terms of Service
    url: https://sentry.io/terms/
  - type: Privacy Policy
    url: https://sentry.io/privacy/
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
tags:
  - APM
  - Application Monitoring
  - Bug Tracking
  - Developer Tools
  - Error Tracking
  - Observability
  - Performance Monitoring
  - Real-Time Monitoring
---
