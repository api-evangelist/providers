---
aid: trinet-group
url: https://raw.githubusercontent.com/api-evangelist/trinet-group/refs/heads/main/apis.yml
name: TriNet Group
description: TriNet Group is a professional employer organization (PEO) providing small and midsize businesses with full-service human resources solutions including payroll processing, employee benefits administration, risk management, compliance, and HR technology. TriNet serves over 16,000 companies and 340,000 worksite employees across verticals including technology, financial services, life sciences, professional services, and nonprofits.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Benefits
  - Compliance
  - Human Resources
  - Payroll
  - Professional Employer Organization
  - Risk Management
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trinet-group:company-api
    name: TriNet Company API
    tags:
      - Company
      - Departments
      - Human Resources
      - Holidays
      - Workers Compensation
    humanURL: https://apidocs.trinet.com/home
    baseURL: https://api.trinet.com
    properties:
      - type: Documentation
        url: https://apidocs.trinet.com/home
    description: The TriNet Company API provides access to company-level HR data including organizational structure, departments, holiday schedules, workers compensation codes, and company configuration. Used by HR administrators to retrieve organizational metadata and policy information.
  - aid: trinet-group:employees-api
    name: TriNet Employees API
    tags:
      - Employees
      - Human Resources
      - Onboarding
      - Workforce Management
    humanURL: https://apidocs.trinet.com/home
    baseURL: https://api.trinet.com
    properties:
      - type: Documentation
        url: https://apidocs.trinet.com/home
    description: The TriNet Employees API provides full lifecycle employee data management including retrieving all employee details, adding new employees (onboarding), and managing employee records. Supports HR workflows for workforce visibility and headcount reporting.
  - aid: trinet-group:payroll-api
    name: TriNet Payroll API
    tags:
      - Compensation
      - Human Resources
      - Pay
      - Payroll
    humanURL: https://apidocs.trinet.com/home
    baseURL: https://api.trinet.com
    properties:
      - type: Documentation
        url: https://apidocs.trinet.com/home
    description: The TriNet Payroll API provides access to employee payroll and compensation data including pay rates, pay frequency, bonuses, and additional pay components. Enables integration with financial systems and compensation analytics platforms.
  - aid: trinet-group:identity-api
    name: TriNet Identity API
    tags:
      - Authentication
      - Identity
      - Security
    humanURL: https://apidocs.trinet.com/home
    baseURL: https://api.trinet.com
    properties:
      - type: Documentation
        url: https://apidocs.trinet.com/home
    description: The TriNet Identity API provides access to employee identity and sensitive personally identifiable information (PII) such as Social Security Numbers for authorized systems. Access is strictly scoped and requires elevated permissions for compliance with data privacy regulations.
  - aid: trinet-group:manage-employee-api
    name: TriNet Manage Employee API
    tags:
      - Employee Management
      - Human Resources
      - Roles
      - Workforce Management
    humanURL: https://apidocs.trinet.com/home
    baseURL: https://api.trinet.com
    properties:
      - type: Documentation
        url: https://apidocs.trinet.com/home
    description: The TriNet Manage Employee API enables management of employee roles and access permissions within the TriNet platform. Supports HR administrators in assigning, updating, and auditing employee roles for system access control.
common:
  - type: Website
    url: https://www.trinet.com
    name: TriNet
  - type: DeveloperPortal
    url: https://apidocs.trinet.com/home
    name: TriNet API Portal
  - type: Documentation
    url: https://apidocs.trinet.com/home
    name: TriNet API Documentation
  - type: Authentication
    url: https://apidocs.trinet.com/oauth-scopes
    name: TriNet OAuth Scopes
  - type: PartnerProgram
    url: https://www.trinet.com/hr-services/technology-platform/integration-center
    name: TriNet Integration Center
  - type: Integrations
    url: https://www.trinet.com/hr-services/technology-platform/integration-center/api
    name: TriNet API Integrations
  - type: PrivacyPolicy
    url: https://www.trinet.com/privacy-policy
    name: TriNet Privacy Policy
  - name: Features
    type: Features
    data:
      - name: Payroll Processing
      - name: Benefits Administration
      - name: Risk Management
      - name: Compliance Support
      - name: HR Technology Platform
      - name: Employee Onboarding
      - name: Time and Attendance
      - name: Workers Compensation
      - name: Expense Management
      - name: Performance Management
      - name: Learning and Development
      - name: QuickBooks Online Integration
  - name: Integrations
    type: Integrations
    data:
      - name: QuickBooks Online
      - name: Salesforce
      - name: Slack
      - name: Microsoft Teams
      - name: Google Workspace
      - name: Okta
      - name: Finch
      - name: Merge
      - name: Apideck
  - name: UseCases
    type: UseCases
    data:
      - name: Employee Data Sync
      - name: Payroll Integration
      - name: Benefits Enrollment Automation
      - name: HR System Integration
      - name: Compliance Reporting
      - name: Onboarding Automation
      - name: Headcount Reporting
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
