---
aid: us-citizenship-and-immigration-services
name: US Citizenship and Immigration Services
description: The US Citizenship and Immigration Services (USCIS) is a government agency responsible for overseeing lawful immigration to the United States. Its primary function is to process and adjudicate applications for various immigration benefits, such as green cards, work permits, and naturalization. USCIS provides a public developer portal (developer.uscis.gov) with APIs for case status lookup and FOIA request submission. The Torch API Program enables qualified software developers to integrate USCIS services into immigration case management applications, providing OAuth 2.0 secured access to case status information and Freedom of Information Act (FOIA) request capabilities.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Immigration
  - Citizenship
  - Case Status
  - FOIA
created: '2024-12-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: us-citizenship-and-immigration-services:uscis-case-status-api
    name: USCIS Case Status API
    description: 'The USCIS Case Status API provides case status information to USCIS customers and their representatives who require regular access to case status information. It accepts a 13-character USCIS receipt number and returns the current case status, form type, submission date, and historical status timeline in English and Spanish. Authentication uses OAuth 2.0 client credentials flow. Rate limits: 5 transactions per second, 1,000 daily requests.'
    humanURL: https://developer.uscis.gov/api/case-status
    baseURL: https://api-int.uscis.gov/case-status
    tags:
      - Federal Government
      - Immigration
      - Case Status
      - USCIS
    properties:
      - type: Documentation
        url: https://developer.uscis.gov/api/case-status
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/openapi/uscis-case-status-api-openapi.yml
      - type: DeveloperPortal
        url: https://developer.uscis.gov/
      - type: Sandbox
        url: https://developer.uscis.gov/get-started/sandbox
      - type: Authentication
        url: https://developer.uscis.gov/article/how-get-access-tokens-client-credentials
    contact:
      - FN: USCIS Developer Support
        url: https://developer.uscis.gov/
  - aid: us-citizenship-and-immigration-services:uscis-foia-request-and-status-api
    name: USCIS FOIA Request and Status API
    description: The USCIS FOIA Request and Status API enables consumers to submit Freedom of Information Act (FOIA) or Privacy Act (PA) requests for Alien File records and check the status of submitted requests using the Request Number returned upon creation. Authentication uses OAuth 2.0 client credentials. Version 1.2.0 is the current production version.
    humanURL: https://developer.uscis.gov/api/foia-request-and-status
    baseURL: https://api-int.uscis.gov/foia
    tags:
      - Federal Government
      - Immigration
      - FOIA
      - Alien File
      - Privacy Act
      - USCIS
    properties:
      - type: Documentation
        url: https://developer.uscis.gov/api/foia-request-and-status
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/openapi/uscis-foia-api-openapi.yml
      - type: DeveloperPortal
        url: https://developer.uscis.gov/
features:
  - name: Case Status Lookup
    description: Retrieve current and historical case status by receipt number
  - name: Bilingual Status Messages
    description: Case status returned in both English and Spanish
  - name: FOIA Request Submission
    description: Submit FOIA and Privacy Act requests for Alien File records via API
  - name: FOIA Status Tracking
    description: Check status of submitted FOIA requests using request number
  - name: OAuth 2.0 Authentication
    description: Secure access via OAuth 2.0 client credentials flow with 30-minute token expiry
  - name: Sandbox Environment
    description: Sandbox environment for testing before production deployment
useCases:
  - name: Immigration Case Management
    description: Integrate case status into immigration law firm case management software
  - name: Client Status Notifications
    description: Automatically notify immigration clients of case status changes
  - name: FOIA Request Automation
    description: Automate FOIA request submission and status tracking for legal practitioners
  - name: Beneficiary Self-Service
    description: Enable beneficiaries to check their own case status through integrated applications
solutions:
  - name: Immigration Software
    description: Enable immigration law firms and accredited representatives to integrate USCIS data into practice management software
  - name: Case Tracking Dashboards
    description: Build dashboards for law firms to monitor multiple client cases simultaneously
integrations:
  - name: myUSCIS
    description: myUSCIS personalized account portal for individual applicants
    url: https://my.uscis.gov
  - name: e-FOIA Portal
    description: USCIS electronic FOIA submission portal
    url: https://www.uscis.gov/records/request-records-through-the-freedom-of-information-act-or-privacy-act
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
