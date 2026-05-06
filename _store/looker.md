---
aid: looker
name: Looker
description: Looker is a business intelligence and data analytics platform that enables organizations to explore, analyze, and share real-time business analytics.
image: https://looker.com/assets/img/images/logos/looker-logo.png
url: https://raw.githubusercontent.com/api-evangelist/looker/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
tags:
  - Analytics
  - BI Platform
  - Business Intelligence
  - Data Analytics
  - Data Visualization
apis:
  - aid: looker:api
    name: Looker API
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
        url: openapi/looker-api-openapi.yml
      - type: Authentication
        url: https://developers.looker.com/api/getting-started#authentication
      - type: SDK
        url: https://developers.looker.com/api/sdks
      - type: Console
        url: https://developers.looker.com/api/explorer/4.0
      - type: RateLimits
        url: https://cloud.google.com/looker/docs/api-rate-limits
      - type: APIReference
        url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest
      - type: GettingStarted
        url: https://docs.cloud.google.com/looker/docs/api-getting-started
      - type: Versioning
        url: https://docs.cloud.google.com/looker/docs/api-versioning
  - aid: looker:lookml
    name: LookML API
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
  - aid: looker:action
    name: Looker Action API
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
      - type: GitHubRepository
        url: https://github.com/looker-open-source/actions
  - aid: looker:embed-sdk
    name: Looker Embed SDK
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
      - type: GitHubRepository
        url: https://github.com/looker-open-source/embed-sdk
      - type: APIReference
        url: https://looker-open-source.github.io/embed-sdk/
  - aid: looker:extension-framework
    name: Looker Extension Framework API
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
      - type: CodeExamples
        url: https://docs.cloud.google.com/looker/docs/extension-framework-react-and-js-code-examples
  - aid: looker:google-cloud-core
    name: Looker (Google Cloud core) API
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
      - type: Console
        url: https://console.cloud.google.com/apis/library/looker.googleapis.com
common:
  - type: DeveloperPortal
    url: https://developers.looker.com/
  - type: GitHubOrganization
    url: https://github.com/looker-open-source
  - type: Support
    url: https://cloud.google.com/looker/docs/support
  - type: StatusPage
    url: https://status.looker.com/
  - type: PrivacyPolicy
    url: https://looker.com/privacy
  - type: TermsOfService
    url: https://looker.com/terms
  - type: SDK
    url: https://docs.cloud.google.com/looker/docs/api-sdk
  - type: ChangeLog
    url: https://github.com/looker-open-source/sdk-codegen/blob/main/CHANGELOG.md
  - type: ReleaseNotes
    url: https://docs.cloud.google.com/looker/docs/release-notes
  - type: Pricing
    url: https://cloud.google.com/looker/pricing
  - type: GettingStarted
    url: https://docs.cloud.google.com/looker/docs/api-getting-started
  - type: Authentication
    url: https://docs.cloud.google.com/looker/docs/api-auth
  - type: Tutorials
    url: https://developers.looker.com/api/tutorials/interactive-api-docs-whats-next/
  - type: JSONSchema
    url: json-schema/looker-dashboard-schema.json
  - type: JSONLD
    url: json-ld/looker-context.jsonld
  - type: NaftikoCapability
    url: capabilities/shared/looker-api.yaml
    title: Looker API Shared Definition
  - type: NaftikoCapability
    url: capabilities/analytics-and-reporting.yaml
    title: Analytics and Reporting Workflow
  - type: Features
    data:
      - name: Self-Service Analytics
        description: Enable business users to explore data, build visualizations, and create dashboards without SQL knowledge using LookML models.
      - name: Data Modeling with LookML
        description: Define reusable data models in LookML that provide a semantic layer between databases and end-user analytics.
      - name: Embedded Analytics
        description: Embed interactive dashboards, reports, and data explorations directly into web applications using SSO and cookieless authentication.
      - name: Scheduled Reports
        description: Schedule and deliver reports and dashboards via email, Slack, S3, or custom action destinations.
      - name: Custom Actions
        description: Build webhook-based actions to send query results to any external destination or trigger workflows.
      - name: API-Driven Administration
        description: Programmatically manage users, roles, dashboards, queries, and platform settings through the Looker API.
  - type: UseCases
    data:
      - name: Executive Dashboards
        description: Build real-time executive dashboards aggregating KPIs from multiple data sources for leadership visibility.
      - name: Customer-Facing Analytics
        description: Embed analytics into SaaS products to provide customers with self-service reporting and data exploration.
      - name: Data Governance Reporting
        description: Monitor data quality, usage patterns, and access controls across the organization through audit reports.
      - name: Marketing Performance Analytics
        description: Analyze campaign performance, attribution, and ROI across marketing channels with unified data models.
      - name: Operational Monitoring
        description: Track operational metrics and KPIs in real time with automated alerting and scheduled report delivery.
  - type: Integrations
    data:
      - name: Google BigQuery
        description: Native optimized connector for querying and analyzing data in Google BigQuery data warehouse.
      - name: Snowflake
        description: High-performance connector for Snowflake cloud data warehouse with push-down query optimization.
      - name: Amazon Redshift
        description: Native connector for querying and visualizing data in Amazon Redshift data warehouse.
      - name: Slack
        description: Deliver scheduled reports and dashboard snapshots to Slack channels with interactive query capabilities.
      - name: Google Sheets
        description: Export query results and dashboard data directly to Google Sheets for collaborative analysis.
      - name: Salesforce
        description: Connect to Salesforce data for CRM analytics and combine with other data sources for unified views.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
