---
aid: workday
specificationVersion: '0.19'
type: Index
name: Workday
description: Collection of Workday REST and SOAP APIs for human capital management, financial management, enterprise planning, analytics, and platform extensibility.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
tags:
  - Cloud Computing
  - Enterprise Software
  - Financial Management
  - HCM
  - SaaS
apis:
  - aid: workday:hcm-api
    name: Workday HCM API
    description: Human Capital Management API for managing workforce data, recruiting, talent management, and payroll. Provides RESTful endpoints for core HR operations.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/
    tags:
      - Human Capital Management
      - Human Resources
      - Payroll
      - Talent Management
      - Workforce
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/hcm.yml
      - type: JSONSchema
        url: json-schema/worker.json
      - type: JSONSchema
        url: json-schema/organization.json
      - type: JSONLD
        url: json-ld/hcm-context.jsonld
      - type: Authentication
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://www.workday.com/en-us/customer-service/support.html
  - aid: workday:financial-management-api
    name: Workday Financial Management API
    description: Financial Management API for accounting, procurement, expenses, and financial reporting. Enables programmatic access to financial data and workflows.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/financialManagement/
    tags:
      - Accounting
      - Expenses
      - Financial Management
      - Procurement
      - Revenue
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/financialManagement.yml
      - type: JSONLD
        url: json-ld/financialManagement-context.jsonld
  - aid: workday:recruiting-api
    name: Workday Recruiting API
    description: Recruiting API for managing job postings, candidates, applications, and hiring workflows. Supports interview feedback and prospect management.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/recruiting/
    tags:
      - Applications
      - Candidates
      - Hiring
      - Job Postings
      - Recruiting
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/recruiting.yml
      - type: JSONLD
        url: json-ld/recruiting-context.jsonld
  - aid: workday:time-tracking-api
    name: Workday Time Tracking API
    description: Time Tracking API for managing employee time entry, timesheets, time clock events, and time validations.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/timeTracking/
    tags:
      - Absence
      - Leave Management
      - Time Tracking
      - Timesheets
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/timeTracking.yml
      - type: JSONLD
        url: json-ld/timeTracking-context.jsonld
  - aid: workday:benefits-api
    name: Workday Benefits API
    description: Benefits API for managing employee benefits, enrollments, and coverage. Provides endpoints for benefits administration workflows.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/benefits/
    tags:
      - Benefits
      - Coverage
      - Enrollments
      - Health Insurance
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/benefits.yml
      - type: JSONLD
        url: json-ld/benefits-context.jsonld
  - aid: workday:absence-management-api
    name: Workday Absence Management API
    description: Absence Management API for managing leave balances, time-off requests, leaves of absence, and eligible absence types for workers.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/absenceManagement/
    tags:
      - Absence Management
      - Leave Balances
      - Leave of Absence
      - Time Off
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/absenceManagement.yml
      - type: JSONSchema
        url: json-schema/time-off.json
      - type: JSONLD
        url: json-ld/absenceManagement-context.jsonld
  - aid: workday:compensation-api
    name: Workday Compensation API
    description: Compensation API for managing employee compensation plans, scorecards, scorecard results, and one-time payment requests.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/compensation/
    tags:
      - Compensation
      - One-Time Payments
      - Pay Plans
      - Scorecards
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/compensation.yml
      - type: JSONSchema
        url: json-schema/compensation.json
      - type: JSONLD
        url: json-ld/compensation-context.jsonld
  - aid: workday:payroll-api
    name: Workday Payroll API
    description: Payroll API for managing pay groups, pay group details, tax rates, payroll inputs, and pay components.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/payroll/
    tags:
      - Pay Components
      - Pay Groups
      - Payroll
      - Tax Rates
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/payroll.yml
      - type: JSONLD
        url: json-ld/payroll-context.jsonld
  - aid: workday:person-api
    name: Workday Person API
    description: Person API for managing worker person data including personal information, contact details, and organizational relationships.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/person/
    tags:
      - Contact Information
      - Employee Data
      - Person
      - Workers
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/person.yml
      - type: JSONSchema
        url: json-schema/worker.json
      - type: JSONLD
        url: json-ld/person-context.jsonld
  - aid: workday:performance-management-api
    name: Workday Performance Management API
    description: Performance Management API for managing performance reviews, feedback badges, goals, and employee performance evaluations.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/performanceManagement/
    tags:
      - Feedback
      - Goals
      - Performance Management
      - Reviews
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/performanceManagement.yml
      - type: JSONLD
        url: json-ld/performanceManagement-context.jsonld
  - aid: workday:talent-management-api
    name: Workday Talent Management API
    description: Talent Management API for managing mentorships, talent profiles, career development, and succession planning.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/talent/
    tags:
      - Career Development
      - Mentorships
      - Succession Planning
      - Talent Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/talent.yml
      - type: JSONLD
        url: json-ld/talent-context.jsonld
  - aid: workday:common-api
    name: Workday Common API
    description: Common API providing shared reference data, lookup values, and utility endpoints used across other Workday REST API services.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/common/
    tags:
      - Common
      - Lookup Values
      - Reference Data
      - Shared Services
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/common.yml
      - type: JSONLD
        url: json-ld/common-context.jsonld
  - aid: workday:staffing-api
    name: Workday Staffing API
    description: Staffing API for managing organizational assignments, job profiles, positions, supervisory organizations, and worker staffing events.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/staffing/
    tags:
      - Job Profiles
      - Organizations
      - Positions
      - Staffing
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/staffing.yml
      - type: JSONSchema
        url: json-schema/position.json
      - type: JSONSchema
        url: json-schema/organization.json
      - type: JSONLD
        url: json-ld/staffing-context.jsonld
  - aid: workday:strategic-sourcing-api
    name: Workday Strategic Sourcing API
    description: Strategic Sourcing API for managing sourcing events, awards, contracts, suppliers, spend categories, and procurement workflows.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://apidocs.workdayspend.com/
    baseURL: https://api.workdayspend.com/services/
    tags:
      - Awards
      - Contracts
      - Procurement
      - Strategic Sourcing
      - Suppliers
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/
      - type: Authentication
        url: https://apidocs.workdayspend.com/services/events/v1.html
  - aid: workday:soap-web-services-api
    name: Workday SOAP Web Services API
    description: Standards-based SOAP API providing programmatic access to Workday business management services with WSDL and XML Schema definitions. Covers 55 service areas including Human Resources, Payroll, Benefits, and Financial Management.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/api
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Enterprise Integration
      - SOAP API
      - Web Services
      - WSDL
    properties:
      - type: Documentation
        url: https://community.workday.com/api
      - type: APIReference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - aid: workday:prism-analytics-api
    name: Workday Prism Analytics API
    description: Prism Analytics REST API for working with Workday Prism Analytics tables, data change tasks, and datasets. Enables programmatic creation and management of analytics data.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/prismAnalytics/
    tags:
      - Analytics
      - Business Intelligence
      - Datasets
      - Prism Analytics
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/prismAnalytics.yml
      - type: JSONLD
        url: json-ld/prismAnalytics-context.jsonld
  - aid: workday:extend-api
    name: Workday Extend API
    description: Workday Extend platform for building custom applications that integrate with Workday. Provides low-code and no-code developer tools for creating business solutions.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/
    tags:
      - App Development
      - Custom Applications
      - Low Code
      - Platform Extensibility
    properties:
      - type: Documentation
        url: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
      - type: GettingStarted
        url: https://developer.workday.com/about
  - aid: workday:raas-api
    name: Workday Report-as-a-Service API
    description: Report-as-a-Service (RaaS) exposes custom reports as RESTful web services, enabling programmatic access to report data. Supports query parameters for filtering and returns data in multiple formats.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/api
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Custom Reports
      - Data Export
      - Report as a Service
      - Reporting
    properties:
      - type: Documentation
        url: https://community.workday.com/api
      - type: OpenAPI
        url: openapi/raas.yml
      - type: JSONLD
        url: json-ld/raas-context.jsonld
  - aid: workday:adaptive-planning-api
    name: Workday Adaptive Planning API
    description: Adaptive Planning REST and XML APIs for managing planning data, accounts, dimensions, and custom reports. Supports integration with enterprise planning and budgeting workflows.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://doc.workday.com/adaptive-planning/en-us/integration/managing-data-integration/api-documentation/understanding-the-adaptive-planning-rest-api/api-methods/brk1623709249507.html
    baseURL: https://api.adaptiveinsights.com/api/
    tags:
      - Adaptive Planning
      - Budgeting
      - Financial Planning
      - Forecasting
    properties:
      - type: Documentation
        url: https://doc.workday.com/adaptive-planning/en-us/integration/managing-data-integration/api-documentation/understanding-the-adaptive-planning-rest-api/api-methods/brk1623709249507.html
      - type: ChangeLog
        url: https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/understanding-the-adaptive-planning-rest-api/vmo1623708512342.html
  - aid: workday:wql-api
    name: Workday WQL API
    description: Workday Query Language (WQL) API enabling SQL-like querying of Workday data through REST endpoints. Provides high-performance data access controlled via OAuth 2.0 tokens.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/wql/
    tags:
      - Analytics
      - Data Access
      - Query Language
      - Reporting
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: openapi/wql.yml
      - type: JSONLD
        url: json-ld/wql-context.jsonld
common:
  - type: GettingStarted
    url: https://community.workday.com/api-start
  - type: Authentication
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
  - type: RateLimits
    url: https://community.workday.com/articles/16827
  - type: StatusPage
    url: https://community.workday.com/trust/status
  - type: TermsOfService
    url: https://www.workday.com/en-us/legal.html
  - type: PrivacyPolicy
    url: https://www.workday.com/en-us/privacy.html
  - type: Documentation
    url: https://community.workday.com/api
  - type: Console
    url: https://developer.workday.com/about
  - type: Blog
    url: https://blog.workday.com/en-us/application-development.html
  - type: GitHubOrganization
    url: https://github.com/workday
  - type: SignUp
    url: https://resourcecenter.workday.com/
  - type: Support
    url: https://www.workday.com/en-us/services/support.html
  - type: Marketplace
    url: https://marketplace.workday.com/en-US/home
  - type: Partners
    url: https://www.workday.com/en-us/company/partners/overview.html
  - type: APIReference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: JSONLD
    url: json-ld/context.jsonld
  - type: SpectralRules
    url: rules/workday-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/workday-vocabulary.yaml
  - type: Features
    url: https://www.workday.com/en-us/products.html
    data:
      - name: Human Capital Management
        description: Comprehensive HCM suite for managing the entire employee lifecycle from hiring to retirement with global compliance.
      - name: Financial Management
        description: Cloud-native financial management with real-time accounting, procurement, expenses, and revenue management.
      - name: Adaptive Planning
        description: Enterprise planning and budgeting with collaborative forecasting, scenario modeling, and rolling forecasts.
      - name: Prism Analytics
        description: Augmented analytics platform combining Workday and third-party data for actionable business intelligence.
      - name: Recruiting
        description: End-to-end recruiting solution with job requisitions, candidate management, and interview scheduling.
      - name: Talent Management
        description: Skills-based talent optimization with performance reviews, succession planning, and career development.
      - name: Payroll
        description: Global payroll processing with automated calculations, tax compliance, and pay slip generation.
      - name: Time and Absence Tracking
        description: Automated time entry, timesheet management, leave balances, and absence request workflows.
      - name: Workday Extend
        description: Low-code platform for building custom applications that integrate natively with the Workday ecosystem.
      - name: Report-as-a-Service
        description: Expose custom Workday reports as RESTful web services for programmatic data access and integration.
  - type: UseCases
    url: https://www.workday.com/en-us/solutions.html
    data:
      - name: Employee Onboarding
        description: Automate new hire onboarding workflows including position assignment, benefits enrollment, and system provisioning.
      - name: Workforce Planning
        description: Model headcount scenarios, track open positions, and align workforce supply with business demand.
      - name: Expense Management
        description: Streamline employee expense reporting with automated policy enforcement, approval workflows, and reimbursement.
      - name: Compliance Reporting
        description: Generate regulatory compliance reports for labor laws, tax requirements, and industry-specific mandates.
      - name: Performance Reviews
        description: Conduct structured performance evaluations with goal tracking, feedback collection, and calibration.
      - name: Payroll Integration
        description: Integrate payroll data with third-party systems for tax filing, benefits administration, and general ledger posting.
  - type: Integrations
    url: https://marketplace.workday.com/en-US/home
    data:
      - name: Salesforce
        description: Sync workforce and customer data between Workday HCM and Salesforce CRM for unified employee and customer insights.
      - name: Microsoft 365
        description: Integrate Workday with Microsoft Teams, Outlook, and Azure AD for single sign-on and productivity workflows.
      - name: ServiceNow
        description: Connect Workday HR processes with ServiceNow ITSM for automated employee service delivery and ticket management.
      - name: Slack
        description: Enable Workday notifications, approvals, and time-off requests directly within Slack channels and DMs.
      - name: ADP
        description: Integrate Workday payroll with ADP for third-party payroll processing and tax filing services.
      - name: SAP
        description: Connect Workday financial management with SAP ERP for cross-system accounting and procurement workflows.
      - name: Greenhouse
        description: Integrate Workday with Greenhouse recruiting for seamless candidate pipeline management and hiring workflows.
      - name: Okta
        description: Connect Workday with Okta for identity management, single sign-on, and automated user provisioning.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
