---
aid: automatic-data-processing
name: Automatic Data Processing (ADP)
description: Automatic Data Processing (ADP) is a global provider of cloud-based human capital management (HCM) solutions including payroll processing, benefits administration, talent management, time and attendance, workforce analytics, and tax compliance services. ADP serves over 1 million businesses worldwide and provides a comprehensive developer platform with REST APIs, SDKs, and marketplace integrations for HCM system connectivity.
url: https://raw.githubusercontent.com/api-evangelist/automatic-data-processing/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - HCM
  - Human Capital Management
  - HR
  - Payroll
  - Benefits
  - Workforce Management
  - Tax Compliance
  - Enterprise
apis:
  - aid: automatic-data-processing:payroll-api
    name: ADP Payroll API
    description: The ADP Payroll API provides programmatic access to payroll processing capabilities including earnings, deductions, pay statements, and payroll runs for employees across ADP Workforce Now and ADP Vantage HCM platforms. Supports payroll input, calculation, and retrieval of pay data.
    humanURL: https://developers.adp.com/articles/api/payroll
    baseURL: https://api.adp.com
    tags:
      - Payroll
      - Earnings
      - Deductions
      - Pay Statements
      - Tax
    properties:
      - type: Documentation
        url: https://developers.adp.com/articles/api/payroll
      - type: Portal
        url: https://developers.adp.com
  - aid: automatic-data-processing:worker-api
    name: ADP Worker Demographics API
    description: The ADP Workers API provides access to employee demographic and employment data including personal information, job assignments, pay rates, reporting relationships, and employment status. Supports CRUD operations on worker records across ADP HCM platforms.
    humanURL: https://developers.adp.com/articles/api/workers
    baseURL: https://api.adp.com
    tags:
      - Worker Demographics
      - Employee Data
      - HR
      - Workforce
    properties:
      - type: Documentation
        url: https://developers.adp.com/articles/api/workers
      - type: Portal
        url: https://developers.adp.com
  - aid: automatic-data-processing:time-labor-api
    name: ADP Time and Labor API
    description: The ADP Time and Labor API enables integration with ADP's timekeeping system for time entries, schedules, time off requests, accruals, and labor cost allocation. Supports both ADP Workforce Now and ADP Vantage time management modules.
    humanURL: https://developers.adp.com/articles/api/time-labor-management
    baseURL: https://api.adp.com
    tags:
      - Time and Attendance
      - Scheduling
      - Timekeeping
      - Labor Management
    properties:
      - type: Documentation
        url: https://developers.adp.com/articles/api/time-labor-management
      - type: Portal
        url: https://developers.adp.com
  - aid: automatic-data-processing:benefits-api
    name: ADP Benefits API
    description: The ADP Benefits API provides access to employee benefits enrollment, plan data, coverage elections, and life event processing. Enables HR system integrations with benefits carriers and third-party benefits administration platforms.
    humanURL: https://developers.adp.com/articles/api/benefits
    baseURL: https://api.adp.com
    tags:
      - Benefits
      - Enrollment
      - Healthcare
      - Insurance
    properties:
      - type: Documentation
        url: https://developers.adp.com/articles/api/benefits
      - type: Portal
        url: https://developers.adp.com
  - aid: automatic-data-processing:talent-api
    name: ADP Talent Management API
    description: The ADP Talent Management API provides access to performance reviews, goal management, succession planning, and learning management data within the ADP platform. Enables integration with third-party talent and learning management systems.
    humanURL: https://developers.adp.com/articles/api/talent-management
    baseURL: https://api.adp.com
    tags:
      - Talent Management
      - Performance Reviews
      - Learning
      - Succession Planning
    properties:
      - type: Documentation
        url: https://developers.adp.com/articles/api/talent-management
      - type: Portal
        url: https://developers.adp.com
  - aid: automatic-data-processing:recruiting-api
    name: ADP Recruiting API
    description: The ADP Recruiting API enables integration with ADP's applicant tracking system for job postings, candidate management, offer letters, and new hire onboarding workflows. Connects with third-party ATS platforms and job boards.
    humanURL: https://developers.adp.com/articles/api/recruiting
    baseURL: https://api.adp.com
    tags:
      - Recruiting
      - Applicant Tracking
      - Onboarding
      - HR
    properties:
      - type: Documentation
        url: https://developers.adp.com/articles/api/recruiting
      - type: Portal
        url: https://developers.adp.com
common:
  - type: Portal
    url: https://developers.adp.com
  - type: Website
    url: https://www.adp.com
  - type: Documentation
    url: https://developers.adp.com/articles/api/all
  - type: GettingStarted
    url: https://developers.adp.com/articles/guide/adp-marketplace-app-intro
  - type: Authentication
    url: https://developers.adp.com/articles/guide/auth-process-data-conn-mgr-mngd-oauth2
  - type: SignUp
    url: https://developers.adp.com/articles/guide/registration
  - type: Marketplace
    url: https://apps.adp.com
  - type: GitHubOrganization
    url: https://github.com/adplabs
  - type: Support
    url: https://developers.adp.com/articles/guide/support
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: ADP APIs use OAuth 2.0 with client credentials and authorization code flows for secure access. Mutual TLS (mTLS) is required for production connections.
      - name: Sandbox Environment
        description: ADP provides a developer sandbox environment with synthetic data for testing integrations before production deployment.
      - name: Marketplace Integration
        description: ADP Marketplace allows ISVs to publish and monetize HCM integrations accessible to ADP's one million plus client base through the app store.
      - name: Webhooks and Events
        description: Event-driven notifications for HR data changes including hire events, terminations, payroll completions, and benefits enrollment changes.
      - name: Data Connector
        description: ADP Data Connector provides managed OAuth2 connections and data sync for partner integrations without custom authentication management.
  - type: UseCases
    data:
      - name: Payroll Integration
        description: Connect HRIS, ERP, and time management systems to ADP payroll for automated payroll input and pay statement distribution.
      - name: HR Data Sync
        description: Synchronize employee records between ADP and third-party HRIS, talent management, and workforce planning systems.
      - name: Benefits Carrier Connectivity
        description: Connect benefits carriers and insurance providers with ADP enrollment data for real-time eligibility and coverage updates.
      - name: Onboarding Automation
        description: Automate new hire workflows from ATS to payroll including I-9, direct deposit setup, and benefits enrollment using ADP APIs.
      - name: Workforce Analytics
        description: Pull ADP workforce data into BI platforms for headcount, compensation, turnover, and labor cost analysis.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync ADP HR data with Salesforce for commission calculations, quota management, and employee-customer relationship tracking.
      - name: SAP SuccessFactors
        description: Bidirectional integration between ADP payroll and SAP SuccessFactors for HCM data synchronization across enterprise systems.
      - name: Microsoft 365
        description: Connect ADP employee data with Microsoft Teams, Active Directory, and SharePoint for identity management and org chart synchronization.
      - name: Workday
        description: Integration between ADP payroll services and Workday HCM for organizations running split HCM/payroll configurations.
      - name: QuickBooks
        description: Sync ADP payroll data with QuickBooks for journal entry and labor cost posting in small business accounting workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
