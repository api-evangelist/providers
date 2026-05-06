---
aid: workday-studio
name: Workday Studio
description: Workday Studio is an integrated development environment (IDE) for building custom integrations and applications on the Workday platform. It provides tools for creating web services, custom reports, and integration solutions.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-studio/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Cloud
  - Development
  - Enterprise
  - Finance
  - HR
  - IDE
  - Integration
apis:
  - name: Workday Studio Integration API
    description: API for building and deploying custom integrations using Workday Studio, an Eclipse-based IDE that provides a graphical development environment with drag-and-drop reusable components for creating sophisticated integrations with flow control, data transformation, error handling, and scripting.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanUrl: https://doc.workday.com/
    baseUrl: https://{tenant}.workday.com/ccx/service
    tags:
      - Custom
      - Development
      - Integration
    properties:
      - type: Documentation
        url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/HdIduH8HQGat1qdv1nXNVQ
      - type: OpenAPI
        url: openapi/workday-studio-integration-openapi.yml
      - type: APIReference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Integrations/v17/Integrations.html
      - type: Authentication
        url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/rvVKnUi_v3MwKZ1VqF_1Jw
      - type: GettingStarted
        url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/z~y4T3OBwNz42E1hT8azSA
      - type: SDK
        url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/HdIduH8HQGat1qdv1nXNVQ
  - name: Workday Web Services API
    description: SOAP and REST web services for integrating with Workday applications, providing programmatic access to business management services with WSDL and XML Schema definitions across 55 service areas including Human Resources, Payroll, Benefits, and Financial Management.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanUrl: https://doc.workday.com/
    baseUrl: https://{tenant}.workday.com/ccx/service/{tenant}
    tags:
      - Enterprise
      - REST
      - SOAP
      - Web Services
    properties:
      - type: Documentation
        url: https://doc.workday.com/reader/J1YvL9yFQMumSgoRA4j4bA/root
      - type: OpenAPI
        url: openapi/workday-studio-web-services-openapi.yml
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/
      - type: APIReference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: RateLimits
        url: https://doc.workday.com/reader/J1YvL9yFQMumSgoRA4j4bA/L~jJl~pFV91hFVm2h3UFWQ
  - name: Workday REST API
    description: RESTful API providing modern JSON-based access to Workday data and services. Uses OAuth 2.0 authentication and standard HTTP methods for operations across HCM, financial management, recruiting, payroll, and other Workday domains.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanUrl: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseUrl: https://{tenant}.workday.com/ccx/api
    tags:
      - Data Access
      - JSON
      - OAuth
      - REST
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: APIReference
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: Authentication
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
  - name: Workday Custom Reports API
    description: API for creating and executing custom reports built in Workday Studio. Exposes custom reports as RESTful web services through Report-as-a-Service (RaaS), enabling programmatic access to report data with support for query parameters and multiple output formats.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanUrl: https://doc.workday.com/
    baseUrl: https://{tenant}.workday.com/ccx/service/customreport2/{tenant}
    tags:
      - Analytics
      - Custom
      - Report as a Service
      - Reports
    properties:
      - type: Documentation
        url: https://doc.workday.com/reader/J1YvL9yFQMumSgoRA4j4bA/ziYjYJxh2YKGvz8I5V46bQ
      - type: Tutorial
        url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/kPBEj3_Lz04YDSUvAEKl4w
  - name: Workday Orchestrate API
    description: Low-code integration and automation platform for building event-driven and batch integrations using a visual drag-and-drop builder. Enables developers to create workflows that connect Workday with external systems, automate business processes, and handle real-time data synchronization.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanUrl: https://www.workday.com/en-us/products/platform-product-extensions/integrations.html
    baseUrl: https://{tenant}.workday.com/ccx/api
    tags:
      - Automation
      - Event Driven
      - Low Code
      - Orchestration
      - Workflows
    properties:
      - type: Documentation
        url: https://www.workday.com/en-us/products/platform-product-extensions/integrations.html
common:
  - type: Website
    url: https://www.workday.com/
  - type: Portal
    url: https://community.workday.com/
  - type: Console
    url: https://developer.workday.com/about
  - type: Login
    url: https://www.myworkday.com/
  - type: SignUp
    url: https://community.workday.com/
  - type: Documentation
    url: https://doc.workday.com/en-us/guides.html
  - type: GettingStarted
    url: https://community.workday.com/node/97816
  - type: Authentication
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
  - type: APIReference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Support
    url: https://www.workday.com/en-us/customer-experience/support.html
  - type: TermsOfService
    url: https://www.workday.com/en-us/legal.html
  - type: PrivacyPolicy
    url: https://www.workday.com/en-us/privacy.html
  - type: StatusPage
    url: https://status.workday.com/
  - type: Blog
    url: https://blog.workday.com/
  - type: DeveloperBlog
    url: https://workday.github.io/
  - type: Contact
    url: https://www.workday.com/en-us/company/about-workday/contact-us.html
  - type: GitHubOrganization
    url: https://github.com/Workday
  - type: Marketplace
    url: https://marketplace.workday.com/en-US/home
  - type: Training
    url: https://www.workday.com/en-us/services/training-certifications.html
  - type: StudioDownload
    url: https://community.workday.com/studio-download
  - type: SpectralRules
    url: rules/workday-studio-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/workday-studio-vocabulary.yaml
  - type: Features
    data:
      - name: Eclipse-based IDE
        description: Workday Studio is an Eclipse-based development environment with a graphical, drag-and-drop interface for designing custom integrations.
      - name: Reusable Components
        description: Provides a library of reusable integration components for transports, transformations, splitters, and routing logic that accelerate integration development.
      - name: Flow Control and Error Handling
        description: Includes constructs for branching, looping, retries, and structured error handling to build resilient integrations.
      - name: Data Transformation
        description: Supports XSLT, XPath, and scripting for mapping and transforming data between Workday and external systems.
      - name: Custom Report-as-a-Service
        description: Exposes custom Workday reports as RESTful web services through Report-as-a-Service (RaaS) for downstream consumption.
      - name: Workday Web Services
        description: Provides SOAP and REST access to 55+ Workday service areas including HCM, Financial Management, Payroll, and Benefits.
      - name: Modern REST API
        description: Offers OAuth 2.0-secured JSON REST endpoints for accessing Workday data and triggering business actions.
      - name: Orchestrate Low-Code Integrations
        description: Workday Orchestrate enables building event-driven and batch integrations through a visual workflow builder without writing code.
      - name: Tenant-Based Deployment
        description: Integrations are deployed against tenant-specific endpoints with environment isolation between sandbox and production tenants.
  - type: UseCases
    data:
      - name: Custom Integrations
        description: Build bespoke integrations between Workday and external HR, payroll, benefits, and financial systems.
      - name: Payroll and Benefits Connectivity
        description: Connect Workday HCM and Payroll to third-party payroll providers, banks, and benefits carriers for data exchange.
      - name: Employee Data Synchronization
        description: Keep worker records, organizational data, and position information in sync between Workday and downstream systems.
      - name: Custom Reporting
        description: Generate custom reports in Workday Studio and expose them through Report-as-a-Service for use in BI tools and dashboards.
      - name: Business Process Automation
        description: Automate cross-system HR and finance business processes using Workday Orchestrate event-driven workflows.
      - name: ERP and CRM Integration
        description: Integrate Workday Financial Management with downstream ERPs, CRMs, and procurement systems for invoicing and revenue management.
      - name: Identity and Access Provisioning
        description: Synchronize worker lifecycle events from Workday into identity providers and downstream applications for user provisioning.
  - type: Integrations
    data:
      - name: Eclipse IDE
        description: Workday Studio runs as an Eclipse-based plug-in providing the development surface for building integrations.
      - name: Salesforce
        description: Common integration target for syncing customer, opportunity, and worker data between Workday and Salesforce.
      - name: ServiceNow
        description: Connect Workday to ServiceNow for IT service management and HR case management workflows.
      - name: ADP
        description: Integrate Workday HCM with ADP and other third-party payroll providers for payroll data exchange.
      - name: Microsoft 365 and Azure AD
        description: Sync worker data with Microsoft 365 and Azure Active Directory for identity provisioning and collaboration tooling.
      - name: SAP
        description: Bridge Workday financial and HR data with SAP ERP systems for organizations running mixed environments.
      - name: AWS, Azure, and Google Cloud
        description: Use Workday integrations to push and pull data from cloud storage, messaging, and data warehouses.
      - name: Snowflake and Data Warehouses
        description: Stream Workday data into Snowflake, BigQuery, and other warehouses for analytics and reporting.
  - type: Solutions
    data:
      - name: Workday HCM
        description: Cloud-based human capital management covering core HR, talent, learning, recruiting, and workforce planning.
      - name: Workday Financial Management
        description: Cloud financial management for accounting, revenue, expenses, projects, and analytics.
      - name: Workday Payroll
        description: Native payroll for the United States, Canada, United Kingdom, and France integrated with Workday HCM.
      - name: Workday Adaptive Planning
        description: Enterprise planning, budgeting, and forecasting platform that integrates with Workday Financials and HCM.
      - name: Workday Extend
        description: Platform for building custom apps that extend Workday functionality using the same data model and security.
      - name: Workday Orchestrate
        description: Low-code integration and automation platform for building workflows across Workday and external systems.
      - name: Workday Marketplace
        description: Curated catalog of partner-built integrations and apps that extend the Workday platform.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
