---
aid: alteryx
name: Alteryx
description: Alteryx is an analytics automation platform that enables data analysts and scientists to break data barriers, deliver insights, and experience the thrill of getting to the answer faster.
image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
url: https://raw.githubusercontent.com/api-evangelist/alteryx/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Analytics
  - Automation
  - Data Engineering
  - Data Preparation
  - Data Science
  - ETL
  - Machine Learning
  - Predictive Analytics
apis:
  - name: Alteryx Server API
    description: REST API for managing workflows, schedules, and jobs on Alteryx Server. Provides Subscription, User V2, Admin V1, Admin V2, and V3 API endpoints for creating, updating, searching, and deleting users, user groups, schedules, credentials, collections, workflows, and Server connections.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/current/en/server/api-overview.html
    baseURL: https://your-server/webapi
    tags:
      - Automation
      - Jobs
      - Scheduling
      - Server
      - Workflows
    properties:
      - type: Documentation
        url: https://help.alteryx.com/current/en/server/api-overview.html
      - type: APIReference
        url: https://help.alteryx.com/developer-help/server-api-reference
      - type: Authentication
        url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3/server-api-configuration-and-authorization.html
      - type: GettingStarted
        url: https://help.alteryx.com/current/en/developer-help/apis/get-started-with-apis.html
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
  - name: Alteryx Server API V3
    description: The V3 Admin API for Alteryx Server uses OAuth 2 authentication and implements POST, PUT, GET, and DELETE functionality for modifying assets, users, credentials, and connections so admins can automate tasks and integrate Server with their existing API automation tools.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3.html
    baseURL: https://your-server/webapi/v3
    tags:
      - Admin
      - Credentials
      - OAuth2
      - Server
      - Users
      - Workflows
    properties:
      - type: Documentation
        url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3.html
      - type: Authentication
        url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3/server-api-configuration-and-authorization.html
      - type: OpenAPI
        url: openapi/alteryx-server-api-v3.yml
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
  - name: Alteryx Server API V1
    description: The V1 API for Alteryx Server provides endpoints for admins including the Migratable Endpoint for migrating workflows across Server environments and the Auditlog Endpoint for tracking changes to system entities.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v1.html
    baseURL: https://your-server/webapi/v1
    tags:
      - Admin
      - Audit
      - Migration
      - Server
    properties:
      - type: Documentation
        url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v1.html
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
  - name: Alteryx Gallery API
    description: API for interacting with Alteryx Analytics Gallery for workflow sharing and execution.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/developer-help/gallery-api-overview
    baseURL: https://gallery.alteryx.com/api
    tags:
      - Gallery
      - Public API
      - Sharing
      - Workflows
    properties:
      - type: Documentation
        url: https://help.alteryx.com/developer-help/gallery-api-overview
      - type: APIReference
        url: https://help.alteryx.com/developer-help/gallery-api-reference
      - type: Authentication
        url: https://help.alteryx.com/developer-help/gallery-api-authentication
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
  - name: Alteryx Connect API
    description: API for Alteryx Connect data catalog and collaboration platform.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/developer-help/connect-api
    baseURL: https://your-connect-server/api
    tags:
      - Collaboration
      - Data Catalog
      - Governance
      - Metadata
    properties:
      - type: Documentation
        url: https://help.alteryx.com/developer-help/connect-api
      - type: Authentication
        url: https://help.alteryx.com/developer-help/connect-authentication
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
  - name: Alteryx AlteryxEngine API
    description: The AlteryxEngine API allows you to call into the Alteryx Engine to build applications that can programmatically execute Alteryx Designer workflows. Workflows and applications can be executed as a separate child process or in-process.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/current/en/developer-help/apis/alteryxengine-api-overview.html
    baseURL: https://your-server/api
    tags:
      - Designer
      - Engine
      - Execution
      - Workflows
    properties:
      - type: Documentation
        url: https://help.alteryx.com/current/en/developer-help/apis/alteryxengine-api-overview.html
      - type: GettingStarted
        url: https://help.alteryx.com/current/en/developer-help/apis/alteryxengine-api-overview/alteryxengine-api-example.html
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
  - name: Alteryx Designer Cloud API
    description: REST API for Alteryx Designer Cloud (powered by Trifacta) providing data preparation, transformation, and pipeline management capabilities. Enables programmatic access to data preparation workflows and job execution.
    image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
    humanURL: https://help.alteryx.com/dataprep/en/developer/api-reference.html
    baseURL: https://api.trifacta.com
    tags:
      - Cloud
      - Data Preparation
      - Pipelines
      - Transformation
      - Trifacta
    properties:
      - type: Documentation
        url: https://help.alteryx.com/dataprep/en/developer/api-reference.html
      - type: APIReference
        url: https://api.trifacta.com/
      - type: Authentication
        url: https://help.alteryx.com/Dataprep/en/developer/api-reference/manage-api-access-tokens.html
    contact:
      - FN: Alteryx Support
        email: support@alteryx.com
        url: https://community.alteryx.com
common:
  - type: DeveloperPortal
    url: https://help.alteryx.com/current/en/developer-help.html
  - type: GettingStarted
    url: https://help.alteryx.com/current/en/developer-help/apis/get-started-with-apis.html
  - type: SDK
    url: https://help.alteryx.com/current/en/developer-help/platform-sdk.html
  - type: StatusPage
    url: https://status.alteryx.com
  - type: Support
    url: https://community.alteryx.com
  - type: Blog
    url: https://community.alteryx.com/t5/Engine-Works/bg-p/engine-works
  - type: X
    url: https://twitter.com/alteryx
  - type: LinkedIn
    url: https://www.linkedin.com/company/alteryx
  - type: GitHubOrganization
    url: https://github.com/alteryx
  - type: Pricing
    url: https://www.alteryx.com/products/pricing
  - type: TrustCenter
    url: https://www.alteryx.com/trust
  - type: TermsOfService
    url: https://www.alteryx.com/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.alteryx.com/privacy-policy
  - type: Legal
    url: https://www.alteryx.com/legal
  - type: Features
    data:
      - name: Workflow Automation
        description: Visual drag-and-drop workflow builder for automating data preparation, blending, and analytics pipelines.
      - name: Scheduled Execution
        description: Schedule workflows to run at specific times or intervals for automated recurring analytics processes.
      - name: User and Access Management
        description: Fine-grained user management with role-based access control for shared workflow environments.
      - name: Credential Management
        description: Secure storage and sharing of data source credentials across workflows and users.
      - name: Collection Organization
        description: Organize workflows, schedules, and users into collections for logical grouping and permission management.
      - name: Cloud Data Preparation
        description: Browser-based data preparation and transformation through Designer Cloud with AI-assisted suggestions.
  - type: UseCases
    data:
      - name: Automated Reporting Pipelines
        description: Schedule and automate data preparation workflows to generate recurring business reports.
      - name: Data Migration
        description: Migrate workflows and configurations across Server environments using the V1 migration API.
      - name: Server Administration Automation
        description: Automate user provisioning, credential management, and workflow deployment through the V3 admin API.
      - name: Self-Service Analytics
        description: Enable business users to discover and run published workflows through the Gallery API.
      - name: Enterprise Data Catalog
        description: Catalog and discover data assets across the organization using Alteryx Connect APIs.
  - type: Integrations
    data:
      - name: Snowflake
        description: Native connector for reading from and writing to Snowflake data warehouse for cloud analytics.
      - name: Tableau
        description: Publish prepared data directly to Tableau Server for visualization and business intelligence.
      - name: Salesforce
        description: Connect to Salesforce CRM data for analytics, reporting, and automated data synchronization.
      - name: AWS S3
        description: Read and write data to Amazon S3 for cloud-based data lake analytics workflows.
      - name: Microsoft Azure
        description: Integration with Azure data services including SQL Database, Blob Storage, and Synapse Analytics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://www.alteryx.com
---
