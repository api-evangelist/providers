---
aid: workday
url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/apis.yml
apis:
- name: Workday HCM API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/hcm.yml
  - type: JSONSchema
    url: json-schema/worker.json
  - type: JSONSchema
    url: json-schema/organization.json
  - type: JSONLD
    url: json-ld/context.jsonld
  - type: Authentication
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
  contact:
  - FN: Workday Support
    email: support@workday.com
    url: https://www.workday.com/en-us/customer-service/support.html
- name: Workday Financial Management API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/financialManagement.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Recruiting API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/recruiting.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Time Tracking API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/timeTracking.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Benefits API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/benefits.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Absence Management API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/absenceManagement.yml
  - type: JSONSchema
    url: json-schema/time-off.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Compensation API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/compensation.yml
  - type: JSONSchema
    url: json-schema/compensation.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Payroll API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/payroll.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Person API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/person.yml
  - type: JSONSchema
    url: json-schema/worker.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Performance Management API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/performanceManagement.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Talent Management API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/talent.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Common API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/common.yml
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Staffing API
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
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.yaml
  - type: OpenAPI
    url: openapi/staffing.yml
  - type: JSONSchema
    url: json-schema/position.json
  - type: JSONSchema
    url: json-schema/organization.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Workday Strategic Sourcing API
  description: Strategic Sourcing API for managing sourcing events, awards, contracts, suppliers, spend categories, and procurement workflows. Includes services for attachments, payments, projects, and reports.
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
- name: Workday SOAP Web Services API
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
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- name: Workday Prism Analytics API
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
    url: json-ld/context.jsonld
  - type: Client Libraries
    url: https://github.com/Workday/prism-python
- name: Workday Extend API
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
  - type: Getting Started
    url: https://developer.workday.com/about
- name: Workday Report-as-a-Service API
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
    url: json-ld/context.jsonld
  - type: Client Libraries
    url: https://github.com/Workday/raas-python
- name: Workday Adaptive Planning API
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
  - type: Change Log
    url: https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/understanding-the-adaptive-planning-rest-api/vmo1623708512342.html
- name: Workday WQL API
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
    url: json-ld/context.jsonld
name: Workday
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of Workday REST and SOAP APIs for human capital management, financial management, enterprise planning, analytics, and platform extensibility.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

