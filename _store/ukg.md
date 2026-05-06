---
aid: ukg
name: UKG
description: UKG (Ultimate Kronos Group) is an enterprise human capital management (HCM) and workforce management platform serving over 80,000 organizations worldwide. The UKG Pro suite includes HCM APIs for employee data, payroll, benefits, and personnel actions, plus WFM APIs for time and labor management, scheduling, accruals, and attendance. The UKG Developer Hub provides REST APIs, webhook subscriptions, and People Fabric APIs for building HR integrations, payroll connectors, and workforce analytics applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Human Capital Management
  - HCM
  - Workforce Management
  - HR
  - Payroll
  - Time and Attendance
  - Benefits
  - Scheduling
url: https://raw.githubusercontent.com/api-evangelist/ukg/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: ukg:ukg-pro-hcm-api
    name: UKG Pro HCM API
    description: The UKG Pro HCM API provides programmatic access to human capital management data including employees, personnel actions, benefits, payroll, performance, and organizational structure. Uses Basic Authentication with service account credentials and tenant-specific API keys. Enables integrations with HR systems, payroll processors, benefits administrators, and workforce analytics platforms.
    humanURL: https://developer.ukg.com/hcm/reference/welcome-to-the-ukg-pro-api
    baseURL: https://service.ultipro.com
    tags:
      - HCM
      - Employees
      - Payroll
      - Benefits
      - Personnel Actions
    properties:
      - type: Documentation
        url: https://developer.ukg.com/hcm/reference/welcome-to-the-ukg-pro-api
      - type: OpenAPI
        url: openapi/ukg-pro-hcm-openapi.yml
      - type: JSONSchema
        url: json-schema/pro-hcm-employee-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-employee-job-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-pay-rate-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-benefits-election-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-department-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-location-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-pay-statement-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-direct-deposit-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-personnel-change-request-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-personnel-change-response-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-employee-list-schema.json
      - type: JSONSchema
        url: json-schema/pro-hcm-employee-id-list-schema.json
      - type: JSONStructure
        url: json-structure/pro-hcm-employee-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-employee-job-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-pay-rate-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-benefits-election-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-department-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-location-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-pay-statement-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-direct-deposit-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-personnel-change-request-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-personnel-change-response-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-employee-list-structure.json
      - type: JSONStructure
        url: json-structure/pro-hcm-employee-id-list-structure.json
      - type: JSONLDContext
        url: json-ld/ukg-pro-hcm-context.jsonld
      - type: Example
        url: examples/pro-hcm-employee-example.json
      - type: Example
        url: examples/pro-hcm-employee-job-example.json
      - type: Example
        url: examples/pro-hcm-pay-rate-example.json
      - type: Example
        url: examples/pro-hcm-benefits-election-example.json
      - type: Example
        url: examples/pro-hcm-department-example.json
      - type: Example
        url: examples/pro-hcm-location-example.json
      - type: Example
        url: examples/pro-hcm-pay-statement-example.json
      - type: Example
        url: examples/pro-hcm-direct-deposit-example.json
      - type: Example
        url: examples/pro-hcm-personnel-change-request-example.json
      - type: Example
        url: examples/pro-hcm-personnel-change-response-example.json
      - type: Example
        url: examples/pro-hcm-employee-list-example.json
      - type: Example
        url: examples/pro-hcm-employee-id-list-example.json
  - aid: ukg:ukg-pro-wfm-api
    name: UKG Pro Workforce Management API
    description: The UKG Pro WFM API provides programmatic access to time and labor management data including punches, shifts, schedules, accruals, and attendance. Supports timekeeping, scheduling, and compliance workflows for hourly and salaried employees. Uses OAuth 2.0 with tenant API keys.
    humanURL: https://developer.ukg.com/wfm/reference/welcome-to-the-ukg-pro-workforce-management-api
    baseURL: https://api.ultipro.com/workforce/v1
    tags:
      - Workforce Management
      - Time and Attendance
      - Scheduling
      - Accruals
      - Timekeeping
    properties:
      - type: Documentation
        url: https://developer.ukg.com/wfm/reference/welcome-to-the-ukg-pro-workforce-management-api
      - type: OpenAPI
        url: openapi/ukg-pro-wfm-openapi.yml
      - type: JSONSchema
        url: json-schema/pro-wfm-wfm-employee-schema.json
      - type: JSONSchema
        url: json-schema/pro-wfm-timecard-schema.json
      - type: JSONSchema
        url: json-schema/pro-wfm-punch-schema.json
      - type: JSONSchema
        url: json-schema/pro-wfm-punch-request-schema.json
      - type: JSONSchema
        url: json-schema/pro-wfm-accrual-balance-schema.json
      - type: JSONSchema
        url: json-schema/pro-wfm-shift-schema.json
      - type: JSONStructure
        url: json-structure/pro-wfm-wfm-employee-structure.json
      - type: JSONStructure
        url: json-structure/pro-wfm-timecard-structure.json
      - type: JSONStructure
        url: json-structure/pro-wfm-punch-structure.json
      - type: JSONStructure
        url: json-structure/pro-wfm-punch-request-structure.json
      - type: JSONStructure
        url: json-structure/pro-wfm-accrual-balance-structure.json
      - type: JSONStructure
        url: json-structure/pro-wfm-shift-structure.json
      - type: JSONLDContext
        url: json-ld/ukg-pro-wfm-context.jsonld
      - type: Example
        url: examples/pro-wfm-wfm-employee-example.json
      - type: Example
        url: examples/pro-wfm-timecard-example.json
      - type: Example
        url: examples/pro-wfm-punch-example.json
      - type: Example
        url: examples/pro-wfm-punch-request-example.json
      - type: Example
        url: examples/pro-wfm-accrual-balance-example.json
      - type: Example
        url: examples/pro-wfm-shift-example.json
  - aid: ukg:ukg-hr-service-delivery-api
    name: UKG HR Service Delivery API
    description: The UKG HR Service Delivery API (formerly People Doc) provides access to employee request management, knowledge portal content, process automation, document storage, and compliance workflows. Enables HR case management integrations and employee self-service applications.
    humanURL: https://doc.people-doc.com/api/?urls.primaryName=Client
    baseURL: https://api.people-doc.com
    tags:
      - HR Service Delivery
      - Case Management
      - Document Management
      - Employee Requests
    properties:
      - type: Documentation
        url: https://doc.people-doc.com/api/?urls.primaryName=Client
      - type: APIReference
        url: https://doc.people-doc.com/client/api/index-v2.html
common:
  - type: Website
    url: https://www.ukg.com
  - type: Documentation
    url: https://developer.ukg.com
  - type: Portal
    url: https://developer.ukg.com
  - type: Blog
    url: https://www.ukg.com/blog
  - type: Pricing
    url: https://www.ukg.com/pricing
  - type: TermsOfService
    url: https://www.ukg.com/legal/terms
  - type: PrivacyPolicy
    url: https://www.ukg.com/legal/privacy-policy
  - type: Support
    url: https://support.ukg.com
  - type: GettingStarted
    url: https://developer.ukg.com/general/docs/getting-started
  - type: Authentication
    url: https://developer.ukg.com/hcm/docs/authentication
  - type: Signup
    url: https://www.ukg.com/contact-us
  - type: SpectralRules
    url: rules/ukg-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/workforce-management.yaml
    title: Workforce Management
  - type: NaftikoCapability
    url: capabilities/hr-administration.yaml
    title: HR Administration
  - type: Vocabulary
    url: vocabulary/ukg-vocabulary.yaml
  - type: Features
    data:
      - name: Human Capital Management
        description: Comprehensive HCM covering employee records, org management, talent, and compliance for enterprise organizations.
      - name: Payroll Processing
        description: Full-service payroll with tax compliance, direct deposit, pay statements, and multi-state support.
      - name: Benefits Administration
        description: Benefits enrollment, plan management, life event processing, and ACA compliance tracking.
      - name: Time and Attendance
        description: Automated timekeeping with punch clocks, mobile entry, approval workflows, and FLSA compliance.
      - name: Workforce Scheduling
        description: AI-powered scheduling with demand forecasting, shift management, and coverage optimization.
      - name: Accrual Management
        description: Configurable vacation, sick, and PTO accrual policies with automated balance tracking.
      - name: HR Service Delivery
        description: Employee case management, knowledge portal, HR document management, and process automation.
      - name: People Fabric
        description: Unified data platform connecting HCM and WFM data across all UKG products via modern APIs.
  - type: UseCases
    data:
      - name: Payroll Integration
        description: Sync employee pay data, deductions, and tax information with third-party payroll processors and ERP systems.
      - name: Benefits Connector
        description: Exchange enrollment data and eligibility with benefits carriers, insurance providers, and benefits administration systems.
      - name: Time and Labor Integration
        description: Import punch data, approved timecards, and schedule information into payroll and workforce analytics platforms.
      - name: HRIS Data Sync
        description: Keep employee demographic, job, and organizational data synchronized between UKG and downstream business systems.
      - name: Analytics and Reporting
        description: Export workforce data to business intelligence tools and data warehouses for advanced analytics and reporting.
      - name: Onboarding Automation
        description: Automate new hire provisioning by triggering downstream system access and equipment setup from UKG hire events.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync employee data between UKG and Salesforce for HR-CRM alignment.
      - name: SAP
        description: Integrate with SAP ERP for GL posting, cost center management, and financial reconciliation.
      - name: Microsoft Azure AD
        description: Single sign-on and user provisioning integration with Microsoft Entra ID.
      - name: Workday
        description: Employee data exchange for organizations using both platforms during migration or hybrid scenarios.
      - name: ADP
        description: Payroll data exchange with ADP for organizations using both HCM and payroll platforms.
      - name: Greenhouse
        description: Applicant tracking system integration for recruiting and onboarding handoff.
  - type: Solutions
    data:
      - name: UKG Pro
        description: Enterprise HCM platform for mid-market and enterprise organizations with full HR, payroll, and talent capabilities.
      - name: UKG Pro WFM
        description: Workforce management platform for hourly and complex workforce scheduling, timekeeping, and compliance.
      - name: UKG Ready
        description: Simplified HCM solution for small and medium businesses with combined HR, payroll, and time management.
      - name: UKG HR Service Delivery
        description: Employee experience platform for HR case management, knowledge delivery, and document compliance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
