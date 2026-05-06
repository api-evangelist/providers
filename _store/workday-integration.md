---
aid: workday-integration
name: Workday Integration
description: Collection of Workday Integration APIs for enterprise resource planning, human capital management, and financial management.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-integration/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - name: Workday Human Capital Management API
    description: API for managing employee data, recruiting, talent management, and workforce planning within Workday's HCM suite. Provides SOAP-based web services for reading and writing HR data including worker records, organizational structures, and staffing transactions.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Employees
      - Human Capital Management
      - Human Resources
      - Talent Management
      - Workforce Planning
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/openapi.json
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
      - type: OpenAPI
        url: openapi/workday-integration-human-capital-management-openapi.yml
    contact:
      - FN: Workday API Support
        email: api-support@workday.com
        url: https://community.workday.com
  - name: Workday Financial Management API
    description: API for financial accounting, expense management, revenue management, and financial reporting. Enables programmatic access to general ledger, accounts payable, accounts receivable, and budgeting functions.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Accounting
      - Expenses
      - Finance
      - Financial Reporting
      - Revenue
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/openapi.json
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
      - type: OpenAPI
        url: openapi/workday-integration-financial-management-openapi.yml
  - name: Workday Payroll API
    description: API for payroll processing, tax management, and compensation. Supports payroll calculations, pay component configurations, tax rate lookups, and payroll detail retrieval across multiple country-specific payroll modules.
    image: https://www.workday.com/content/dam/web/images/icons/payroll-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Benefits
      - Compensation
      - Pay Components
      - Payroll
      - Tax
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll/openapi.json
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
      - type: OpenAPI
        url: openapi/workday-integration-payroll-openapi.yml
  - name: Workday Recruiting API
    description: API for candidate management, job requisitions, and recruiting processes. Provides endpoints for managing interviews, job postings, prospect data including education, experience, resumes, and skills.
    image: https://www.workday.com/content/dam/web/images/icons/recruiting-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Candidates
      - Hiring
      - Jobs
      - Recruiting
      - Talent Acquisition
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/openapi.json
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
      - type: OpenAPI
        url: openapi/workday-integration-recruiting-openapi.yml
  - name: Workday Time Tracking API
    description: API for time entry, attendance, absence management, and scheduling. Supports clock events, time block management, time review events, and validation of worker time records.
    image: https://www.workday.com/content/dam/web/images/icons/time-tracking-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Time_Tracking/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Absence
      - Attendance
      - Clock Events
      - Scheduling
      - Time Tracking
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Time_Tracking/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Time_Tracking/openapi.json
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
      - type: OpenAPI
        url: openapi/workday-integration-time-tracking-openapi.yml
  - name: Workday Integrations API
    description: REST API for building custom integrations with Workday services. Provides endpoints for programmatic access to integration events, launch parameters, and reference data used across Workday modules.
    image: https://www.workday.com/content/dam/web/images/icons/integrations-icon.svg
    humanURL: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/HvgwLhmQNc1eEa0eR93f6w
    baseURL: https://wd2-impl-services1.workday.com/ccx/api
    tags:
      - Automation
      - Custom Integrations
      - Integrations
      - REST API
      - Webhooks
    properties:
      - type: Documentation
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/HvgwLhmQNc1eEa0eR93f6w
      - type: Getting Started
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/_WwNVaErikZF0XOmg3zcJQ
      - type: Rate Limits
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/FIwWY~bJjS7JgZSnPlsJ1A
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
      - type: OpenAPI
        url: openapi/workday-integration-integrations-openapi.yml
  - name: Workday Absence Management API
    description: API for managing employee leave requests, absence types, and time-off balances. Retrieves eligible absence types for employees and supports validation of leave category selections.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Absence_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Absence Management
      - Employee Benefits
      - Leave Requests
      - Time Off
      - Workforce Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Absence_Management/index.html
      - type: OpenAPI
        url: openapi/workday-integration-absence-management-openapi.yml
  - name: Workday Benefits Administration API
    description: API for managing employee benefits enrollment, eligibility, and plan administration. Supports programmatic access to benefits plans, enrollment events, and dependent management.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Benefits_Administration/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Benefits
      - Benefits Administration
      - Employee Benefits
      - Enrollment
      - Health Plans
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Benefits_Administration/index.html
      - type: OpenAPI
        url: openapi/workday-integration-benefits-administration-openapi.yml
  - name: Workday Compensation API
    description: API for managing employee compensation data including salary structures, pay grades, and compensation plans. Provides endpoints for scorecard results and one-time payment requests.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Compensation
      - Compensation Plans
      - Pay Grades
      - Salary
      - Total Rewards
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation/index.html
      - type: OpenAPI
        url: openapi/workday-integration-compensation-openapi.yml
  - name: Workday Compensation Review API
    description: API for managing compensation review processes including merit increases, bonus allocations, and equity grants. Supports compensation review cycle configuration and approval workflows.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation_Review/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Bonus
      - Compensation Review
      - Equity Grants
      - Merit Increases
      - Salary Review
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation_Review/index.html
      - type: OpenAPI
        url: openapi/workday-integration-compensation-review-openapi.yml
  - name: Workday Performance Management API
    description: API for managing employee performance reviews, goals, and feedback. Supports performance review cycles, feedback badge management, and goal tracking across the organization.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Performance_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Employee Development
      - Feedback
      - Goals
      - Performance Management
      - Reviews
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Performance_Management/index.html
      - type: OpenAPI
        url: openapi/workday-integration-performance-management-openapi.yml
  - name: Workday Learning API
    description: API for managing learning and development within the Workday Learning module. Provides access to course catalogs, learning assignments, enrollment data, and training completion records.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Learning/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Course Management
      - Employee Development
      - Learning
      - Learning Management
      - Training
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Learning/index.html
      - type: OpenAPI
        url: openapi/workday-integration-learning-openapi.yml
  - name: Workday Talent API
    description: API for managing talent profiles, succession planning, and career development. Supports mentorship program management and talent pool operations within the organization.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Talent/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Career Development
      - Mentorship
      - Succession Planning
      - Talent Management
      - Talent Pools
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Talent/index.html
      - type: OpenAPI
        url: openapi/workday-integration-talent-openapi.yml
  - name: Workday Staffing API
    description: API for managing staffing transactions including hires, terminations, transfers, and position management. Provides programmatic access to job profiles, positions, and organizational assignments.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Staffing/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Hiring
      - Position Management
      - Staffing
      - Transfers
      - Workforce Planning
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Staffing/index.html
      - type: OpenAPI
        url: openapi/workday-integration-staffing-openapi.yml
  - name: Workday Cash Management API
    description: API for managing cash positions, bank account transactions, and treasury operations. Supports bank statement processing and cash flow management.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Cash_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Banking
      - Cash Management
      - Financial Operations
      - Transactions
      - Treasury
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Cash_Management/index.html
      - type: OpenAPI
        url: openapi/workday-integration-cash-management-openapi.yml
  - name: Workday Revenue Management API
    description: API for revenue recognition, billing, and revenue reporting. Provides programmatic access to revenue schedules, contracts, and billing operations.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Revenue_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Billing
      - Contracts
      - Financial Management
      - Revenue Management
      - Revenue Recognition
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Revenue_Management/index.html
      - type: OpenAPI
        url: openapi/workday-integration-revenue-management-openapi.yml
  - name: Workday Resource Management API
    description: API for managing project resources, resource pools, and resource allocation. Supports workforce capacity planning and resource assignment operations.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Capacity Planning
      - Project Resources
      - Resource Allocation
      - Resource Management
      - Workforce Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/index.html
      - type: OpenAPI
        url: openapi/workday-integration-resource-management-openapi.yml
  - name: Workday Professional Services Automation API
    description: API for managing professional services projects, billing, and resource utilization. Supports project tracking, time and expense management, and services revenue operations.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Professional_Services_Automation/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Billing
      - Professional Services
      - Project Management
      - Resource Utilization
      - Services Automation
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Professional_Services_Automation/index.html
      - type: OpenAPI
        url: openapi/workday-integration-professional-services-automation-openapi.yml
  - name: Workday Workforce Planning API
    description: API for strategic workforce planning, headcount forecasting, and organizational modeling. Enables analysis of workforce supply and demand across the enterprise.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Workforce_Planning/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Headcount Forecasting
      - Organizational Modeling
      - Strategic Planning
      - Workforce Analytics
      - Workforce Planning
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Workforce_Planning/index.html
      - type: OpenAPI
        url: openapi/workday-integration-workforce-planning-openapi.yml
  - name: Workday Identity Management API
    description: API for managing user accounts, authentication, and identity lifecycle within Workday. Supports account provisioning, security group management, and identity governance operations.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Identity_Management/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Authentication
      - Identity Management
      - Provisioning
      - Security
      - User Accounts
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Identity_Management/index.html
      - type: OpenAPI
        url: openapi/workday-integration-identity-management-openapi.yml
  - name: Workday Notification API
    description: API for managing notifications and alerts within Workday. Supports programmatic delivery of system notifications, task reminders, and event alerts to users.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Notification/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Alerts
      - Events
      - Messaging
      - Notifications
      - Task Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Notification/index.html
      - type: OpenAPI
        url: openapi/workday-integration-notification-openapi.yml
  - name: Workday Prism Analytics API
    description: REST API for working with Workday Prism Analytics tables, data change tasks, and datasets. Enables programmatic creation of Prism Analytics tables and datasets and modification of data within them.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Prism_Analytics/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api
    tags:
      - Analytics
      - Business Intelligence
      - Data Management
      - Datasets
      - Prism Analytics
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Prism_Analytics/index.html
      - type: SDKs
        url: https://github.com/Workday/prism-python
      - type: OpenAPI
        url: openapi/workday-integration-prism-analytics-openapi.yml
  - name: Workday Scheduling API
    description: API for managing employee schedules, shift assignments, and scheduling patterns. Supports schedule creation, shift swaps, and coverage planning operations.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Scheduling/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Coverage Planning
      - Employee Scheduling
      - Scheduling
      - Shift Management
      - Workforce Scheduling
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Scheduling/index.html
      - type: OpenAPI
        url: openapi/workday-integration-scheduling-openapi.yml
  - name: Workday Payroll Interface API
    description: API for interfacing with third-party payroll systems. Enables extraction and transmission of payroll data between Workday and external payroll processors.
    image: https://www.workday.com/content/dam/web/images/icons/payroll-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_Interface/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Data Exchange
      - External Systems
      - Payroll Integration
      - Payroll Interface
      - Third Party Payroll
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_Interface/index.html
      - type: OpenAPI
        url: openapi/workday-integration-payroll-interface-openapi.yml
  - name: Workday Dynamic Document Generation API
    description: API for generating dynamic documents such as offer letters, contracts, and compliance forms. Supports template management and automated document creation workflows.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Dynamic_Document_Generation/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Automation
      - Compliance
      - Document Generation
      - Document Management
      - Templates
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Dynamic_Document_Generation/index.html
      - type: OpenAPI
        url: openapi/workday-integration-dynamic-document-generation-openapi.yml
  - name: Workday Connect API
    description: API for managing Workday Connect messaging and communication services. Supports internal messaging, notifications, and collaboration features within the Workday platform.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Workday_Connect/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Collaboration
      - Communication
      - Internal Messaging
      - Messaging
      - Workday Connect
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Workday_Connect/index.html
      - type: OpenAPI
        url: openapi/workday-integration-connect-openapi.yml
  - name: Workday Extensibility API
    description: API for extending Workday functionality through custom objects, calculated fields, and business process extensions. Enables developers to build custom applications and extend the Workday platform.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Workday_Extensibility/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Business Process
      - Custom Objects
      - Customization
      - Extensibility
      - Platform Extension
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Workday_Extensibility/index.html
      - type: OpenAPI
        url: openapi/workday-integration-extensibility-openapi.yml
  - name: Workday External Integrations API
    description: API for managing external system integrations and data exchange with third-party applications. Provides endpoints for configuring and monitoring integration connections.
    image: https://www.workday.com/content/dam/web/images/icons/integrations-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/External_Integrations/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Connectivity
      - Data Exchange
      - External Integrations
      - Integration Management
      - Third Party
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/External_Integrations/index.html
      - type: OpenAPI
        url: openapi/workday-integration-external-integrations-openapi.yml
  - name: Workday Inventory API
    description: API for managing inventory tracking, stock levels, and material movements within the Workday supply chain module. Supports inventory counts and goods receipt operations.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Inventory/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Inventory
      - Materials
      - Stock Management
      - Supply Chain
      - Warehouse
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Inventory/index.html
      - type: OpenAPI
        url: openapi/workday-integration-inventory-openapi.yml
  - name: Workday Settlement Services API
    description: API for managing payment settlement processes and banking transactions. Supports payment processing, settlement runs, and financial reconciliation.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Settlement_Services/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Banking
      - Financial Transactions
      - Payments
      - Reconciliation
      - Settlement
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Settlement_Services/index.html
      - type: OpenAPI
        url: openapi/workday-integration-settlement-services-openapi.yml
  - name: Workday Student Core API
    description: API for managing student records, academic programs, and student lifecycle data within Workday Student. Supports student information systems and academic administration.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Core/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Academic Programs
      - Higher Education
      - Student Information
      - Student Lifecycle
      - Student Records
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Core/index.html
      - type: OpenAPI
        url: openapi/workday-integration-student-core-openapi.yml
  - name: Workday Student Records API
    description: API for managing academic records including transcripts, grades, and course registrations. Supports academic history tracking and degree audit processes.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Records/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Academic History
      - Course Registration
      - Grades
      - Student Records
      - Transcripts
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Records/index.html
      - type: OpenAPI
        url: openapi/workday-integration-student-records-openapi.yml
  - name: Workday Student Finance API
    description: API for managing student financial accounts, tuition billing, and financial aid disbursements. Supports student payment processing and account management.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Finance/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Financial Aid
      - Student Accounts
      - Student Billing
      - Student Finance
      - Tuition
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Finance/index.html
      - type: OpenAPI
        url: openapi/workday-integration-student-finance-openapi.yml
  - name: Workday Student Recruiting API
    description: API for managing student recruitment processes, prospect tracking, and admissions pipeline. Supports recruitment event management and prospect communication.
    image: https://www.workday.com/content/dam/web/images/icons/recruiting-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Recruiting/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Admissions
      - Higher Education
      - Prospect Management
      - Recruitment Events
      - Student Recruiting
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Recruiting/index.html
      - type: OpenAPI
        url: openapi/workday-integration-student-recruiting-openapi.yml
  - name: Workday Admissions API
    description: API for managing the admissions process including applications, evaluations, and admissions decisions. Supports application tracking and enrollment management for educational institutions.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Admissions/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Admissions
      - Applications
      - Enrollment
      - Higher Education
      - Student Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Admissions/index.html
      - type: OpenAPI
        url: openapi/workday-integration-admissions-openapi.yml
  - name: Workday Financial Aid API
    description: API for managing financial aid programs, awards, and disbursements. Supports financial aid packaging, eligibility determination, and award letter generation.
    image: https://www.workday.com/content/dam/web/images/icons/financials-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Aid/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Aid Disbursement
      - Eligibility
      - Financial Aid
      - Higher Education
      - Student Awards
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Aid/index.html
      - type: OpenAPI
        url: openapi/workday-integration-financial-aid-openapi.yml
  - name: Workday Academic Foundation API
    description: API for managing academic foundation data including academic units, programs, and curriculum structures. Provides access to foundational academic configuration data.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Academic_Foundation/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Academic Foundation
      - Academic Programs
      - Academic Units
      - Curriculum
      - Higher Education
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Academic_Foundation/index.html
      - type: OpenAPI
        url: openapi/workday-integration-academic-foundation-openapi.yml
  - name: Workday Academic Advising API
    description: API for managing academic advising activities, student appointments, and advising notes. Supports academic planning and student success tracking.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Academic_Advising/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Academic Advising
      - Academic Planning
      - Advising Notes
      - Higher Education
      - Student Success
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Academic_Advising/index.html
      - type: OpenAPI
        url: openapi/workday-integration-academic-advising-openapi.yml
  - name: Workday Student Transfer Credit API
    description: API for managing transfer credit evaluations, articulation agreements, and credit equivalencies. Supports transfer student onboarding and credit assessment processes.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Transfer_Credit/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Articulation
      - Credit Evaluation
      - Higher Education
      - Student Records
      - Transfer Credit
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Student_Transfer_Credit/index.html
      - type: OpenAPI
        url: openapi/workday-integration-student-transfer-credit-openapi.yml
  - name: Workday Campus Engagement API
    description: API for managing campus engagement activities, student organizations, and campus events. Supports student life management and engagement tracking.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Campus_Engagement/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Campus Engagement
      - Campus Events
      - Higher Education
      - Student Life
      - Student Organizations
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Campus_Engagement/index.html
      - type: OpenAPI
        url: openapi/workday-integration-campus-engagement-openapi.yml
  - name: Workday Tenant Data Translation API
    description: API for managing data translations across Workday tenants. Supports localization, language translations, and multi-language configuration for tenant data.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Tenant_Data_Translation/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Data Translation
      - Internationalization
      - Localization
      - Multi Language
      - Tenant Configuration
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Tenant_Data_Translation/index.html
      - type: OpenAPI
        url: openapi/workday-integration-tenant-data-translation-openapi.yml
  - name: Workday Metadata Translations API
    description: API for managing metadata translations including field labels, enumerations, and system text across supported languages. Supports multi-language metadata management.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Metadata_Translations/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Localization
      - Metadata
      - Multi Language
      - System Configuration
      - Translations
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Metadata_Translations/index.html
      - type: OpenAPI
        url: openapi/workday-integration-metadata-translations-openapi.yml
  - name: Workday Drive API
    description: API for managing Workday Drive file storage and document management. Supports file upload, download, folder management, and document sharing operations.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Drive/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Cloud Storage
      - Document Management
      - File Sharing
      - File Storage
      - Workday Drive
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Drive/index.html
      - type: OpenAPI
        url: openapi/workday-integration-drive-openapi.yml
  - name: Workday Adoption API
    description: API for tracking and managing platform adoption metrics within Workday. Provides insights into feature usage, user engagement, and adoption trends.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Adoption/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Adoption
      - Feature Adoption
      - Platform Metrics
      - Usage Analytics
      - User Engagement
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Adoption/index.html
      - type: OpenAPI
        url: openapi/workday-integration-adoption-openapi.yml
  - name: Workday Moments API
    description: API for managing Workday Moments, which delivers personalized nudges and recommendations to employees. Supports milestone celebrations and key workplace moments.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Moments/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Employee Experience
      - Milestones
      - Moments
      - Nudges
      - Recommendations
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Moments/index.html
      - type: OpenAPI
        url: openapi/workday-integration-moments-openapi.yml
  - name: Workday Org Studio API
    description: API for managing organizational design and modeling through Org Studio. Supports organizational restructuring, role mapping, and org chart management.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Org_Studio/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Org Charts
      - Org Modeling
      - Organizational Design
      - Organizational Management
      - Restructuring
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Org_Studio/index.html
      - type: OpenAPI
        url: openapi/workday-integration-org-studio-openapi.yml
  - name: Workday Flex Team API
    description: API for managing flexible team assignments and cross-functional team structures. Supports dynamic team composition and project-based team management.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Flex_Team/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Cross Functional
      - Dynamic Teams
      - Flex Teams
      - Project Teams
      - Team Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Flex_Team/index.html
      - type: OpenAPI
        url: openapi/workday-integration-flex-team-openapi.yml
  - name: Workday Requests API
    description: API for managing service requests and approval workflows within Workday. Supports request creation, routing, approval chains, and status tracking.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Requests/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Approvals
      - Requests
      - Service Requests
      - Task Management
      - Workflows
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Requests/index.html
      - type: OpenAPI
        url: openapi/workday-integration-requests-openapi.yml
  - name: Workday ACA Partner Integrations API
    description: API for Affordable Care Act partner integrations. Supports ACA compliance reporting, eligibility tracking, and data exchange with ACA reporting partners.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/ACA_Partner_Integrations/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - ACA Compliance
      - Benefits Compliance
      - Healthcare Compliance
      - Partner Integrations
      - Regulatory Reporting
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/ACA_Partner_Integrations/index.html
      - type: OpenAPI
        url: openapi/workday-integration-aca-partner-integrations-openapi.yml
  - name: Workday Benefits Partner Program Integrations API
    description: API for integrating with benefits partner programs and third-party benefits providers. Supports benefits carrier data exchange and enrollment synchronization.
    image: https://www.workday.com/content/dam/web/images/icons/hcm-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Benefits_Partner_Program_Integrations/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Benefits Exchange
      - Benefits Partners
      - Carrier Integration
      - Enrollment Sync
      - Partner Programs
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Benefits_Partner_Program_Integrations/index.html
      - type: OpenAPI
        url: openapi/workday-integration-benefits-partner-program-integrations-openapi.yml
  - name: Workday Payroll AUS API
    description: API for Australian payroll processing including superannuation, PAYG withholding, and Australian tax compliance. Supports country-specific payroll operations for Australia.
    image: https://www.workday.com/content/dam/web/images/icons/payroll-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_AUS/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Australian Tax
      - Country Payroll
      - PAYG
      - Payroll Australia
      - Superannuation
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_AUS/index.html
      - type: OpenAPI
        url: openapi/workday-integration-payroll-aus-openapi.yml
  - name: Workday Payroll CAN API
    description: API for Canadian payroll processing including CPP, EI, and Canadian tax compliance. Supports country-specific payroll operations for Canada.
    image: https://www.workday.com/content/dam/web/images/icons/payroll-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_CAN/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Canadian Tax
      - Country Payroll
      - CPP
      - Employment Insurance
      - Payroll Canada
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_CAN/index.html
      - type: OpenAPI
        url: openapi/workday-integration-payroll-can-openapi.yml
  - name: Workday Payroll FRA API
    description: API for French payroll processing including social contributions and French tax compliance. Supports country-specific payroll operations for France.
    image: https://www.workday.com/content/dam/web/images/icons/payroll-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_FRA/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Country Payroll
      - European Payroll
      - French Tax
      - Payroll France
      - Social Contributions
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_FRA/index.html
      - type: OpenAPI
        url: openapi/workday-integration-payroll-fra-openapi.yml
  - name: Workday Payroll GBR API
    description: API for United Kingdom payroll processing including PAYE, National Insurance, and UK tax compliance. Supports country-specific payroll operations for Great Britain.
    image: https://www.workday.com/content/dam/web/images/icons/payroll-icon.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_GBR/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - British Payroll
      - Country Payroll
      - National Insurance
      - PAYE
      - Payroll UK
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll_GBR/index.html
      - type: OpenAPI
        url: openapi/workday-integration-payroll-gbr-openapi.yml
common:
  - type: Portal
    url: https://developer.workday.com/about
  - type: Documentation
    url: https://doc.workday.com/
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Getting Started
    url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/_WwNVaErikZF0XOmg3zcJQ
  - type: Authentication
    url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/yZdGMij6UK~tyr4gJLlewA
  - type: Blog
    url: https://workday.github.io/
  - type: Status
    url: https://community.workday.com/trust/status
  - type: Support
    url: https://www.workday.com/en-us/services/support.html
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal/site-terms.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: GitHub Organization
    url: https://github.com/workday
  - type: Community
    url: https://www.workday.com/en-us/services/community.html
  - type: Website
    url: https://www.workday.com
  - type: Login
    url: https://community.workday.com/user/login
  - type: Sign Up
    url: https://community.workday.com/user/register
  - type: SDKs
    url: https://github.com/Workday/prism-python
  - type: JSON-LD
    url: json-ld/workday-integration-context.jsonld
  - type: JSON Schema (Worker)
    url: json-schema/workday-integration-worker-schema.json
  - type: JSON Schema (Organization)
    url: json-schema/workday-integration-organization-schema.json
  - type: JSON Schema (Position)
    url: json-schema/workday-integration-position-schema.json
  - type: JSON Schema (Job Profile)
    url: json-schema/workday-integration-job-profile-schema.json
  - type: JSON Schema (Compensation)
    url: json-schema/workday-integration-compensation-schema.json
  - type: JSON Schema (Absence)
    url: json-schema/workday-integration-absence-schema.json
  - type: JSON Schema (Payroll)
    url: json-schema/workday-integration-payroll-schema.json
  - type: JSON Schema (Recruiting)
    url: json-schema/workday-integration-recruiting-schema.json
  - type: JSON Schema (Time Block)
    url: json-schema/workday-integration-time-block-schema.json
  - type: JSON Schema (Benefit Plan)
    url: json-schema/workday-integration-benefit-plan-schema.json
  - type: JSON Schema (Integration Event)
    url: json-schema/workday-integration-integration-event-schema.json
  - type: JSON Schema (Student)
    url: json-schema/workday-integration-student-schema.json
  - type: Spectral Rules
    url: rules/workday-integration-rules.yml
  - type: JSON Structure (Worker)
    url: json-structure/workday-integration-worker-structure.json
  - type: JSON Structure (Payroll Result)
    url: json-structure/workday-integration-payroll-result-structure.json
  - type: Vocabulary
    url: vocabulary/workday-integration-vocabulary.yml
  - type: Example (List Workers)
    url: examples/workday-integration-list-workers-example.json
  - type: Example (List Job Requisitions)
    url: examples/workday-integration-list-job-requisitions-example.json
  - type: Example (List Payroll Results)
    url: examples/workday-integration-list-payroll-results-example.json
  - type: Naftiko Capability (Hire-to-Retire)
    url: capabilities/hire-to-retire.yaml
  - type: Naftiko Capability (Talent Management)
    url: capabilities/talent-management.yaml
  - type: Naftiko Capability (Payroll Processing)
    url: capabilities/payroll-processing.yaml
  - type: Naftiko Capability (Financial Operations)
    url: capabilities/financial-operations.yaml
  - type: Naftiko Capability (Workforce Intelligence)
    url: capabilities/workforce-intelligence.yaml
  - type: Naftiko Capability (HCM)
    url: capabilities/shared/human-capital-management.yaml
  - type: Naftiko Capability (Recruiting)
    url: capabilities/shared/recruiting.yaml
  - type: Naftiko Capability (Payroll)
    url: capabilities/shared/payroll.yaml
  - type: Naftiko Capability (Time Tracking)
    url: capabilities/shared/time-tracking.yaml
  - type: Naftiko Capability (Absence Management)
    url: capabilities/shared/absence-management.yaml
  - type: Naftiko Capability (Benefits Administration)
    url: capabilities/shared/benefits-administration.yaml
  - type: Naftiko Capability (Compensation)
    url: capabilities/shared/compensation.yaml
  - type: Naftiko Capability (Performance Management)
    url: capabilities/shared/performance-management.yaml
  - type: Naftiko Capability (Learning)
    url: capabilities/shared/learning.yaml
  - type: Naftiko Capability (Financial Management)
    url: capabilities/shared/financial-management.yaml
  - type: Naftiko Capability (Prism Analytics)
    url: capabilities/shared/prism-analytics.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Enterprise
  - ERP
  - Finance
  - HCM
  - Integration
  - Payroll
---
