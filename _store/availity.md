---
aid: availity
url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/apis.yml
apis:
  - aid: availity:availity-eligibility-benefits-api
    name: Availity Eligibility & Benefits API
    tags:
      - Benefits
      - EDI
      - Eligibility
      - Healthcare
      - X12 270/271
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/partner/documentation
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
      - url: https://developer.availity.com/blog/2025/3/4/ebvalue-add-api
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-eligibility-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/json-schema/availity-eligibility-schema.json
        type: JSONSchema
    description: The Availity Eligibility & Benefits API supports the ASC X12N 270 and 271 transactions, enabling real-time verification of member coverage, co-pays, deductibles, and benefits information. REST APIs connect provider systems to every major health plan nationwide for eligibility checks.
  - aid: availity:availity-claims-status-api
    name: Availity Claim Status API
    tags:
      - Claims
      - Clearinghouse
      - EDI
      - Healthcare
      - X12 276/277
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/partner/documentation
        type: Documentation
      - url: https://developer.availity.com/blog/2025/3/25/enhanced-claim-status
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-claim-status-openapi.yml
        type: OpenAPI
    description: The Availity Claim Status API enables the standard ASC X12N 276 and 277 transactions, allowing providers to find, create, and manage claim status inquiries against payer systems. REST APIs bridge provider billing systems and payers through the Availity clearinghouse network. Supports both standard 276/277 workflows and enhanced claim status with summary and detail search.
  - aid: availity:availity-claim-attachments-api
    name: Availity Claim Attachments API
    tags:
      - Attachments
      - Claims
      - Clearinghouse
      - EDI
      - Healthcare
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/blog/2025/2/28/claim-attachment-api
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-claim-attachments-openapi.yml
        type: OpenAPI
    description: The Availity Claim Attachments API enables electronic submission of supporting documentation alongside healthcare claims. REST APIs support structured and unstructured attachment types for additional clinical information required by payers during claims adjudication.
  - aid: availity:availity-service-reviews-api
    name: Availity Service Reviews (Prior Authorization) API
    tags:
      - EDI
      - Healthcare
      - Prior Authorization
      - Service Reviews
      - X12 278
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/blog/2025/3/4/service-reviews
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-service-reviews-openapi.yml
        type: OpenAPI
    description: The Availity Service Reviews API enables the ASC X12N 278 transaction for prior authorization and healthcare service review. REST APIs allow providers to find, create, and manage authorization requests and responses with health plan payers through the Availity clearinghouse. Includes IsAuthRequired and Attachments add-on APIs.
  - aid: availity:availity-hipaa-transactions-api
    name: Availity Healthcare HIPAA Transactions API
    tags:
      - Clearinghouse
      - EDI
      - Healthcare
      - HIPAA
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/portal/catalogue-products/healthcare-hipaa-transactions-1
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/portal/catalogue-products/healthcare-hipaa-transactions-1
        type: Documentation
      - url: https://developer.availity.com/blog/2025/3/25/hipaa-transactions
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
    description: 'The Availity Healthcare HIPAA Transactions API provides a unified interface for standard HIPAA EDI transactions. REST APIs enable healthcare providers and vendors to submit and receive X12 EDI transactions across payers including eligibility, claims, remittance, authorizations, and referrals. Quota: 100,000 calls per day, 100 calls per second rate limit.'
  - aid: availity:availity-patient-cost-estimator-api
    name: Availity Patient Cost Estimator API
    tags:
      - Cost Estimation
      - Healthcare
      - Patient Financial Responsibility
      - Price Transparency
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/partner/documentation
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
    description: The Availity Patient Cost Estimator API enables healthcare providers and institutions to estimate service costs before delivery for both institutional and professional services. REST APIs support version 1.0.0 and 2.0.0 and include predetermination requests across all major health plan payers, helping meet price transparency requirements.
  - aid: availity:availity-eb-value-adds-api
    name: Availity Eligibility & Benefits Value-Add APIs
    tags:
      - Care Reminders
      - EDI
      - Eligibility
      - Healthcare
      - Member ID Card
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/blog/2025/3/4/ebvalue-add-api
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
    description: The Availity Eligibility & Benefits Value-Add APIs provide supplementary data during eligibility transactions. The Care Reminders API retrieves real-time care gap information from multiple payers. The Member ID Card API retrieves digital member ID cards in PDF or PNG format during eligibility verification workflows.
  - aid: availity:availity-payer-list-api
    name: Availity Payer List API
    tags:
      - Clearinghouse
      - Healthcare
      - Payer Network
      - Reference Data
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/partner/documentation
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
    description: The Availity Payer List API (v1.0.4) allows healthcare organizations to query available payers and the transactions they support. Returns payer identifiers, names, and supported transaction types including eligibility, claim status, prior authorization, and remittance across the nationwide Availity clearinghouse network.
  - aid: availity:availity-configurations-api
    name: Availity Configurations API
    tags:
      - Configuration
      - Healthcare
      - Payer Requirements
      - Provider Validation
    image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
    humanURL: https://developer.availity.com/
    baseURL: https://api.availity.com
    properties:
      - url: https://developer.availity.com/partner/documentation
        type: Documentation
      - url: https://developer.availity.com/partner/gettingstarted
        type: GettingStarted
    description: The Availity Configurations API (v1.0.0) provides provider details and payer-specific validation requirements. Returns configuration rules for enhanced claim status, prior authorization, and other transaction types so provider systems can validate submissions before sending to payers.
common:
  - url: https://www.availity.com
    type: Website
  - url: https://developer.availity.com/
    type: Portal
  - url: https://developer.availity.com/partner/documentation
    type: Documentation
  - url: https://developer.availity.com/partner/gettingstarted
    type: GettingStarted
  - url: https://developer.availity.com/blog/2025/3/25/availity-api-guide
    type: Documentation
  - url: https://developer.availity.com/partner/contact-us
    type: Support
  - url: https://www.availity.com/terms-of-use/
    type: TermsOfService
  - url: https://www.availity.com/Privacy-Policy/
    type: PrivacyPolicy
  - url: https://github.com/availity
    type: GitHubOrganization
  - url: https://availity.github.io/sdk-js/
    type: SDK
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-eligibility-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-claim-status-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-claim-attachments-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-service-reviews-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/json-schema/availity-eligibility-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/json-ld/availity-eligibility-context.jsonld
    type: JSONLD
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/json-ld/availity-claim-context.jsonld
    type: JSONLD
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/json-ld/availity-service-context.jsonld
    type: JSONLD
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/rules/availity-spectral-rules.yml
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/vocabulary/availity-vocabulary.yaml
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/capabilities/availity-revenue-cycle-management.yaml
    type: NaftikoCapability
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Client credentials grant flow with 5-minute token expiration and HTTPS/TLS encryption for secure API access.
      - name: Real-Time EDI Transactions
        description: Processing over 8.8 million daily transactions and 11 billion annual healthcare transactions across all major health plans.
      - name: Nationwide Payer Network
        description: Access to every major health plan nationwide and over 1 million providers through the Availity clearinghouse.
      - name: Multi-Format Responses
        description: Returns JSON and XML representations including errors using HTTP response codes. Supports CSV, PDF, PNG, and XLS for specific endpoints.
      - name: Cursor-Based Pagination
        description: Collection resources support offset/limit pagination with limit range of 1-50 items per request with link relations.
      - name: Mock/Sandbox Testing
        description: Demo subscriptions support custom response selection via X-Api-Mock-Scenario-ID and X-Api-Mock-Response headers.
      - name: Rate Limiting
        description: Standard tier provides 100,000 calls per day and 100 calls per second for HIPAA transaction APIs.
      - name: ASC X12 EDI Standards
        description: Full support for HIPAA EDI version 005010 transactions including 270/271, 276/277, 278, and 835 transaction sets.
  - type: UseCases
    data:
      - name: Real-Time Eligibility Verification
        description: Verify patient insurance coverage, co-pays, deductibles, and benefits in real time before scheduling or rendering services.
      - name: Claim Status Tracking
        description: Track submitted claims through adjudication, checking ACKNOWLEDGED, PENDING, PAID, DENIED, and ADJUSTED statuses.
      - name: Prior Authorization Management
        description: Submit and track prior authorization requests using X12 278 transactions to check if authorization is required before service delivery.
      - name: Patient Cost Estimation
        description: Estimate patient out-of-pocket costs before services are rendered to meet price transparency requirements and inform patients.
      - name: Electronic Claim Attachments
        description: Electronically attach clinical documentation to claims and authorizations, reducing manual faxing and accelerating adjudication.
      - name: Care Gap Identification
        description: Retrieve real-time care reminders during eligibility checks to identify preventive care gaps and coordinate outreach.
      - name: Digital Member ID Cards
        description: Retrieve member ID cards digitally during eligibility verification, reducing administrative burden and improving patient experience.
      - name: Multi-Payer Data Consolidation
        description: Connect to all major payers through a single clearinghouse API rather than managing individual payer connections.
  - type: Integrations
    data:
      - name: EHR Systems
        description: Integrates with electronic health record systems to embed eligibility and claims workflows into clinical workflows.
      - name: Practice Management Systems
        description: Connects practice management software to payer networks for revenue cycle management and claims processing.
      - name: Revenue Cycle Management Platforms
        description: Integrates with RCM platforms to automate eligibility verification, claim submission, and payment reconciliation.
      - name: Blue Cross Blue Shield Plans
        description: Direct integration with BCBS plans nationwide for eligibility, claims, and prior authorization transactions.
      - name: Humana
        description: Integration with Humana for care reminders, eligibility verification, and claims processing.
      - name: Molina Healthcare
        description: Integration with Molina Healthcare for eligibility and benefits verification and care reminders.
      - name: Florida Blue
        description: Integration with Florida Blue for care reminders and real-time eligibility verification.
      - name: Healthfirst New York
        description: Integration with Healthfirst New York for eligibility and care gap identification.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-04-19'
description: Availity is a healthcare information network and clearinghouse providing REST APIs for real-time HIPAA EDI transactions. The platform processes over 11 billion annual healthcare transactions connecting providers, health plans, and vendors nationwide. Create your application and subscribe to a plan to make use of Availity APIs for eligibility verification, claims management, prior authorization, and patient cost estimation.
---
