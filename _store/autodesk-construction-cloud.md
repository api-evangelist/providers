---
aid: autodesk-construction-cloud
name: Autodesk Construction Cloud
description: Autodesk Construction Cloud (ACC) is a unified platform connecting workflows, teams, and data across the construction project lifecycle, integrating preconstruction, design collaboration, project management, and field execution tools. ACC provides REST APIs through the Autodesk Platform Services (APS) for programmatic access to project management, issues, RFIs, submittals, cost management, model coordination, and data export capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Construction
  - BIM
  - Project Management
  - AEC
  - CAD
  - Architecture
  - Engineering
  - Field Management
url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: autodesk-construction-cloud:acc-admin-api
    name: Autodesk Construction Cloud Admin API
    description: The Autodesk Construction Cloud Admin API provides programmatic management of ACC accounts, projects, users, and company settings. REST APIs enable automation of project provisioning, user access control, and account-level administration across ACC and BIM 360 deployments.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - ACC
      - Administration
      - BIM
      - Construction
      - Project Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accounts-accountidprojects-GET/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/openapi/acc-admin-openapi.yml
  - aid: autodesk-construction-cloud:acc-issues-api
    name: Autodesk Construction Cloud Issues API
    description: The ACC Issues API enables creation, retrieval, and management of construction issues, observations, and punch list items. REST APIs integrate with field management workflows for quality control, safety reporting, and project closeout in Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM
      - Construction
      - Field Management
      - Issues
      - Quality
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/issues-issues-POST/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/openapi/acc-issues-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/json-schema/acc-issue-schema.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/examples/acc-issue-example.json
  - aid: autodesk-construction-cloud:acc-cost-management-api
    name: Autodesk Construction Cloud Cost Management API
    description: The ACC Cost Management API provides access to budget codes, contract lifecycle management, and expense tracking in Autodesk Construction Cloud. REST APIs enable ERP integration, change order management, and financial reporting across construction project portfolios.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - ACC
      - Budget
      - Construction
      - Contracts
      - Cost Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/cost-actions-POST/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
  - aid: autodesk-construction-cloud:acc-model-coordination-api
    name: Autodesk Construction Cloud Model Coordination API
    description: The ACC Model Coordination API enables access to model sets, clash detection results, and coordination issues in Autodesk Construction Cloud. REST APIs support automated BIM coordination workflows, clash review automation, and model aggregation across design disciplines.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM
      - Clash Detection
      - Construction
      - IFC
      - Model Coordination
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/mc-modelset-service-v3-create-model-set-POST/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
  - aid: autodesk-construction-cloud:acc-rfis-api
    name: Autodesk Construction Cloud RFIs API
    description: The ACC RFIs API enables management of Requests for Information (RFIs) in Autodesk Construction Cloud. REST APIs support RFI creation, tracking, response workflows, and reporting for construction project documentation and decision management.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - ACC
      - Construction
      - Document Management
      - RFI
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-search-POST/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
  - aid: autodesk-construction-cloud:acc-submittals-api
    name: Autodesk Construction Cloud Submittals API
    description: The ACC Submittals API provides programmatic access to submittal workflows in Autodesk Construction Cloud. REST APIs support submittal item creation, review routing, approval tracking, and specification section management for construction project compliance.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - ACC
      - Construction
      - Document Management
      - Submittals
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/submittals-items-GET/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
  - aid: autodesk-construction-cloud:acc-data-connector-api
    name: Autodesk Construction Cloud Data Connector API
    description: The ACC Data Connector API enables bulk extraction of project data from Autodesk Construction Cloud for analytics and reporting. REST APIs support scheduled and on-demand data exports across issues, RFIs, submittals, assets, and other project modules for business intelligence integration.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/
    baseURL: https://developer.api.autodesk.com
    tags:
      - ACC
      - Analytics
      - Construction
      - Data Export
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference/http/data-connector-requests-POST/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
common:
  - type: Website
    url: https://www.autodesk.com
  - type: Portal
    url: https://aps.autodesk.com/
  - type: Documentation
    url: https://aps.autodesk.com/developer/documentation
  - type: GettingStarted
    url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
  - type: Quickstart
    url: https://get-started.aps.autodesk.com/
  - type: TermsOfService
    url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service
  - type: PrivacyPolicy
    url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
  - type: StatusPage
    url: https://health.autodesk.com/
  - type: Support
    url: https://aps.autodesk.com/contact-support
  - type: ChangeLog
    url: https://aps.autodesk.com/topics/platform-updates
  - type: GitHubOrganization
    url: https://github.com/autodesk-platform-services
  - type: AsyncAPI
    url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/asyncapi/acc-webhooks-asyncapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/json-schema/acc-project-schema.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/json-ld/acc-context.jsonld
  - type: Features
    data:
      - name: Project Administration
        description: Programmatic management of ACC accounts, projects, users, and company settings with automation of project provisioning and user access control.
      - name: Issues and Field Management
        description: Creation, tracking, and management of construction issues, observations, punch lists, and quality control items through REST APIs.
      - name: Cost Management
        description: Budget tracking, contract lifecycle management, change order processing, and financial reporting for construction project portfolios.
      - name: Model Coordination
        description: Automated BIM coordination with clash detection, model set management, and coordination issue tracking across design disciplines.
      - name: RFI and Submittal Management
        description: End-to-end management of Requests for Information and submittal review workflows with approval tracking and compliance reporting.
      - name: Data Connector
        description: Bulk extraction of project data for analytics and business intelligence, supporting scheduled and on-demand exports across all ACC modules.
      - name: Webhooks
        description: Event-driven notifications via webhooks for real-time integration with external systems when project data changes in ACC.
  - type: UseCases
    data:
      - name: ERP Integration
        description: Connecting ACC cost management and project data with enterprise ERP systems for unified financial reporting and project accounting.
      - name: BIM Workflow Automation
        description: Automating BIM coordination workflows including clash detection review, model set updates, and coordination issue resolution across teams.
      - name: Construction Project Reporting
        description: Building custom dashboards and reports using the Data Connector API to aggregate project data across issues, RFIs, submittals, and costs.
      - name: Field Management Integration
        description: Integrating ACC issues and punch list management with mobile field apps, IoT sensors, and safety management platforms.
      - name: Document Control Automation
        description: Automating RFI and submittal routing, review reminders, and approval tracking to reduce administrative burden on project document control teams.
  - type: Integrations
    data:
      - name: Autodesk Platform Services
        description: Full integration with the Autodesk Platform Services (APS) ecosystem including Data Management, Model Derivative, and Authentication APIs.
      - name: Procore
        description: Integration possibilities with Procore construction management platform for cross-platform project data synchronization.
      - name: Primavera P6
        description: Schedule data integration with Oracle Primavera P6 for project schedule management and reporting across enterprise construction portfolios.
      - name: SAP
        description: Enterprise ERP integration with SAP for financial data synchronization, purchase order management, and project accounting workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
