---
aid: qliksense
name: Qlik Sense APIs
description: Collection of APIs for Qlik Sense, a business intelligence and visual analytics platform. Qlik provides REST APIs, WebSocket APIs, and developer tools for managing cloud tenants, applications, data connections, users, automations, and AI-powered analytics through the Qlik Cloud platform.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Analytics
  - Business Intelligence
  - Cloud
  - Data Visualization
  - Enterprise
apis:
  - aid: qliksense:engine-api
    name: Qlik Engine API
    description: JSON-RPC WebSocket API for interacting with the Qlik Associative Engine, creating and manipulating apps, and building visualizations.
    humanURL: https://qlik.dev/apis/json-rpc/qix
    baseURL: wss://your-tenant.qlikcloud.com/app/
    tags:
      - Analytics
      - Business Intelligence
      - JSON-RPC
      - WebSocket
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/json-rpc/qix
  - aid: qliksense:apps-api
    name: Qlik Apps API
    description: Manage Qlik Sense applications including creating, updating, publishing, and deleting apps in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/apps
    baseURL: https://your-tenant.qlikcloud.com/api/v1/apps
    tags:
      - Applications
      - Apps
      - Cloud
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/apps
  - aid: qliksense:users-api
    name: Qlik Users API
    description: Manage users, groups, and authentication in Qlik Cloud tenants.
    humanURL: https://qlik.dev/apis/rest/users
    baseURL: https://your-tenant.qlikcloud.com/api/v1/users
    tags:
      - Identity
      - REST
      - Users
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/users
  - aid: qliksense:spaces-api
    name: Qlik Spaces API
    description: Manage shared and managed spaces for collaboration and content organization in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/spaces
    baseURL: https://your-tenant.qlikcloud.com/api/v1/spaces
    tags:
      - Collaboration
      - Organization
      - REST
      - Spaces
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/spaces
  - aid: qliksense:data-connections-api
    name: Qlik Data Connections API
    description: Create and manage data connections to various data sources in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/data-connections
    baseURL: https://your-tenant.qlikcloud.com/api/v1/data-connections
    tags:
      - Connections
      - Data
      - Integration
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-connections
  - aid: qliksense:automations-api
    name: Qlik Automations API
    description: Create and manage no-code automation workflows in Qlik Automate that connect applications together.
    humanURL: https://qlik.dev/apis/rest/automations
    baseURL: https://your-tenant.qlikcloud.com/api/v1/automations
    tags:
      - Automations
      - No-Code
      - REST
      - Workflows
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automations
  - aid: qliksense:reloads-api
    name: Qlik Reload API
    description: Trigger and manage data reload operations for Qlik Sense apps.
    humanURL: https://qlik.dev/apis/rest/reloads
    baseURL: https://your-tenant.qlikcloud.com/api/v1/reloads
    tags:
      - Data
      - ETL
      - Reload
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/reloads
  - aid: qliksense:webhooks-api
    name: Qlik Webhooks API
    description: Create and manage webhooks to provide other applications with real-time information from Qlik Cloud events.
    humanURL: https://qlik.dev/apis/rest/webhooks
    baseURL: https://your-tenant.qlikcloud.com/api/v1/webhooks
    tags:
      - Events
      - Real-Time
      - REST
      - Webhooks
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/webhooks
  - aid: qliksense:reports-api
    name: Qlik Reports API
    description: Generate downloadable report assets from data with configurable templates and output formats.
    humanURL: https://qlik.dev/apis/rest/reports
    baseURL: https://your-tenant.qlikcloud.com/api/v1/reports
    tags:
      - Export
      - Reports
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/reports
  - aid: qliksense:ml-api
    name: Qlik Machine Learning API
    description: Generate profile insights, create and manage ML experiments, deploy models, and run predictions in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/ml
    baseURL: https://your-tenant.qlikcloud.com/api/v1/ml
    tags:
      - AI
      - Machine Learning
      - Predictions
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/ml
  - aid: qliksense:natural-language-api
    name: Qlik Natural Language API
    description: Parse natural language queries with support for language configuration, visualization generation, and conversation context.
    humanURL: https://qlik.dev/apis/rest/questions
    baseURL: https://your-tenant.qlikcloud.com/api/v1/questions
    tags:
      - AI
      - Natural Language
      - NLP
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/questions
  - aid: qliksense:tenants-api
    name: Qlik Tenants API
    description: Configure and manage Qlik Cloud tenants including settings, licenses, and administrative operations.
    humanURL: https://qlik.dev/apis/rest/tenants
    baseURL: https://your-tenant.qlikcloud.com/api/v1/tenants
    tags:
      - Administration
      - Configuration
      - REST
      - Tenants
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/tenants
  - aid: qliksense:audits-api
    name: Qlik Audits API
    description: Access events emitted upon each action taken in a tenant for detailed audit logging and compliance.
    humanURL: https://qlik.dev/apis/rest/audits
    baseURL: https://your-tenant.qlikcloud.com/api/v1/audits
    tags:
      - Audits
      - Compliance
      - Logging
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/audits
common:
  - type: Portal
    url: https://qlik.dev/
  - type: GettingStarted
    url: https://qlik.dev/get-started
  - type: Authentication
    url: https://qlik.dev/authenticate
  - type: Support
    url: https://support.qlik.com/
  - type: TermsOfService
    url: https://www.qlik.com/us/legal/terms-of-service
  - type: PrivacyPolicy
    url: https://www.qlik.com/us/legal/privacy
  - type: ChangeLog
    url: https://qlik.dev/changelog/
  - type: CLI
    url: https://qlik.dev/toolkits/qlik-cli/
  - type: SDK
    url: https://qlik.dev/toolkits/qlik-api/
  - type: GitHubOrganization
    url: https://github.com/qlik-oss
  - type: Tutorials
    url: https://qlik.dev/tutorials/
  - type: StatusPage
    url: https://status.qlik.com/
  - type: Blog
    url: https://qlik.dev/changelog/tag/api/
  - type: Features
    data:
      - name: Associative Engine
        description: Qlik's unique Associative Engine enables dynamic data exploration without predefined queries or drill paths.
      - name: 50+ REST APIs
        description: Comprehensive REST API coverage for all Qlik Cloud resources including apps, data, users, and automation.
      - name: AI-Powered Analytics
        description: AutoML, natural language queries, and AI assistants for data-driven insights.
      - name: No-Code Automation
        description: Build automation workflows connecting Qlik with external applications without coding.
      - name: Real-Time Webhooks
        description: Event-driven architecture with webhooks for real-time notifications on platform events.
      - name: Multi-Cloud Deployment
        description: Deploy Qlik Cloud across AWS, Azure, and GCP regions with global availability.
  - type: UseCases
    data:
      - name: Embedded Analytics
        description: Embed interactive Qlik visualizations and dashboards in custom web applications.
      - name: Data Pipeline Automation
        description: Automate data integration and transformation workflows using APIs and automation connectors.
      - name: Self-Service BI
        description: Enable business users to create and share analytics apps through the platform APIs.
      - name: AI-Powered Insights
        description: Generate predictive analytics and natural language insights using ML and NLP APIs.
      - name: Multi-Tenant Management
        description: Manage multiple Qlik Cloud tenants programmatically for SaaS and enterprise deployments.
  - type: Integrations
    data:
      - name: Snowflake
        description: Direct connectivity for analytics on Snowflake cloud data warehouse.
      - name: Databricks
        description: Integration with Databricks lakehouse for large-scale analytics workloads.
      - name: SAP
        description: Enterprise data connectivity for SAP ERP, BW, and HANA data sources.
      - name: Salesforce
        description: CRM data integration for sales analytics and pipeline management.
      - name: Slack
        description: Collaboration integration for sharing analytics insights and alerts in Slack.
      - name: Microsoft Teams
        description: Embed analytics and receive notifications within Microsoft Teams.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
