---
aid: workday-recruiting
name: Workday Recruiting
description: APIs for Workday's cloud-based recruiting and talent acquisition solution, providing programmatic access to job requisitions, candidate management, applications, interviews, job postings, and hiring workflows.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-recruiting/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - HCM
  - Human Resources
  - Recruiting
  - SaaS
  - Talent Acquisition
apis:
  - name: Workday Recruiting REST API
    description: RESTful API for managing recruiting operations including job requisitions, candidates, applications, and hiring processes in Workday. Supports OAuth 2.0 authentication and returns data in JSON format for integration with talent management and applicant tracking systems.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/recruiting/
    tags:
      - Applications
      - Candidates
      - Job Requisitions
      - Recruiting
      - Talent Acquisition
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v41.2/Recruiting_OpenAPI.yaml
      - type: OpenAPI
        url: openapi/workday-recruiting-rest-api-openapi.yml
      - type: Authentication
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
      - type: RateLimits
        url: https://community.workday.com/articles/16827
      - type: JSON-LD
        url: json-ld/workday-recruiting-rest-api-context.jsonld
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-applicant-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-applicant-import-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-attachment-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-background-check-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-background-check-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-background-check-package-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-candidate-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-candidate-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-candidate-assessment-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-evergreen-requisition-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-evergreen-requisition-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-interview-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-interview-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-interview-feedback-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-interview-feedback-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-job-application-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-job-posting-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-job-posting-site-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-job-requisition-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-job-requisition-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-offer-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-offer-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-position-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-position-create-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-questionnaire-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-recruiting-agency-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-reference-schema.json
      - type: JSONSchema
        url: json-schema/recruiting-rest-api-veteran-status-schema.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-applicant-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-applicant-import-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-attachment-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-background-check-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-background-check-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-background-check-package-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-candidate-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-candidate-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-candidate-assessment-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-evergreen-requisition-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-evergreen-requisition-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-interview-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-interview-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-interview-feedback-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-interview-feedback-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-job-application-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-job-posting-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-job-posting-site-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-job-requisition-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-job-requisition-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-offer-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-offer-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-position-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-position-create-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-questionnaire-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-recruiting-agency-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-reference-structure.json
      - type: JSONStructure
        url: json-structure/recruiting-rest-api-veteran-status-structure.json
      - type: Example
        url: examples/recruiting-rest-api-applicant-example.json
      - type: Example
        url: examples/recruiting-rest-api-applicant-import-example.json
      - type: Example
        url: examples/recruiting-rest-api-attachment-example.json
      - type: Example
        url: examples/recruiting-rest-api-background-check-example.json
      - type: Example
        url: examples/recruiting-rest-api-background-check-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-background-check-package-example.json
      - type: Example
        url: examples/recruiting-rest-api-candidate-example.json
      - type: Example
        url: examples/recruiting-rest-api-candidate-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-candidate-assessment-example.json
      - type: Example
        url: examples/recruiting-rest-api-evergreen-requisition-example.json
      - type: Example
        url: examples/recruiting-rest-api-evergreen-requisition-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-interview-example.json
      - type: Example
        url: examples/recruiting-rest-api-interview-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-interview-feedback-example.json
      - type: Example
        url: examples/recruiting-rest-api-interview-feedback-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-job-application-example.json
      - type: Example
        url: examples/recruiting-rest-api-job-posting-example.json
      - type: Example
        url: examples/recruiting-rest-api-job-posting-site-example.json
      - type: Example
        url: examples/recruiting-rest-api-job-requisition-example.json
      - type: Example
        url: examples/recruiting-rest-api-job-requisition-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-offer-example.json
      - type: Example
        url: examples/recruiting-rest-api-offer-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-position-example.json
      - type: Example
        url: examples/recruiting-rest-api-position-create-example.json
      - type: Example
        url: examples/recruiting-rest-api-questionnaire-example.json
      - type: Example
        url: examples/recruiting-rest-api-recruiting-agency-example.json
      - type: Example
        url: examples/recruiting-rest-api-reference-example.json
      - type: Example
        url: examples/recruiting-rest-api-veteran-status-example.json
  - name: Workday Recruiting SOAP Web Services API
    description: SOAP-based web service providing comprehensive access to Workday Recruiting business services data for integration with talent management and applicant tracking systems. Includes over 120 operations covering candidate management, job requisitions, evergreen requisitions, job postings, interviews, background checks, recruiting agencies, and self-schedule calendars.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v45.2/Recruiting.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Candidates
      - Job Requisitions
      - Recruiting
      - SOAP API
      - Web Services
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v45.2/Recruiting.html
      - type: APIReference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: WSDL
        url: wsdl/workday-recruiting-soap.wsdl
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v45.2/Recruiting.wsdl
      - type: XSD
        url: xsd/workday-recruiting-soap.xsd
      - type: XSD
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v45.2/Recruiting.xsd
      - type: ChangeLog
        url: https://community.workday.com/api-versions
common:
  - type: Portal
    url: https://community.workday.com
  - type: GettingStarted
    url: https://community.workday.com/api-start
  - type: Documentation
    url: https://community.workday.com/api
  - type: Authentication
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
  - type: Console
    url: https://developer.workday.com/about
  - type: Blog
    url: https://blog.workday.com/en-us/application-development.html
  - type: StatusPage
    url: https://community.workday.com/trust/status
  - type: Support
    url: https://www.workday.com/en-us/services/support.html
  - type: SignUp
    url: https://resourcecenter.workday.com/
  - type: TermsOfService
    url: https://www.workday.com/en-us/legal.html
  - type: PrivacyPolicy
    url: https://www.workday.com/en-us/privacy.html
  - type: RateLimits
    url: https://community.workday.com/articles/16827
  - type: ChangeLog
    url: https://community.workday.com/api-versions
  - type: GitHubOrganization
    url: https://github.com/Workday
  - type: Tools
    url: https://www.npmjs.com/package/@workday/everywhere
    title: Workday Everywhere SDK
  - type: Tools
    url: https://github.com/Workday/canvas-kit
    title: Workday Canvas Kit
  - type: CodeExamples
    url: https://github.com/Workday/extend-js-example
    title: Workday Extend JavaScript Example
  - type: Marketplace
    url: https://marketplace.workday.com/en-US/home
  - type: Partners
    url: https://www.workday.com/en-us/company/partners/overview.html
  - type: SpectralRules
    url: rules/workday-recruiting-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/requisition-management.yaml
  - type: NaftikoCapability
    url: capabilities/candidate-pipeline.yaml
  - type: NaftikoCapability
    url: capabilities/interview-and-screening.yaml
  - type: NaftikoCapability
    url: capabilities/recruiting-configuration.yaml
  - type: NaftikoCapability
    url: capabilities/shared/recruiting.yaml
  - type: Vocabulary
    url: vocabulary/workday-recruiting-vocabulary.yaml
  - type: Features
    data:
      - name: Job Requisition Management
        description: Create, edit, close, freeze, and reopen job requisitions for open positions, with full lifecycle and approval workflow support.
      - name: Evergreen Requisitions
        description: Manage ongoing requisitions used for continuous hiring needs without a specific number of openings or close date.
      - name: Candidate Management
        description: Create, retrieve, and update candidate profiles including personal information, attachments, photos, and assessment data.
      - name: Job Application Lifecycle
        description: Manage applications from submission through disposition, including stage movement, advancement, and offer initiation.
      - name: Job Posting Distribution
        description: Post, update, and unpost jobs to internal and external career sites and manage job posting site brands and configurations.
      - name: Interview Scheduling
        description: Schedule interviews, submit interview feedback, configure interview settings, and manage self-schedule calendars.
      - name: Background Check Integration
        description: Submit and retrieve background check results and manage background check packages for candidate screening.
      - name: Recruiting Agency Workflows
        description: Manage agency relationships, agency users, and agency candidate submissions tied to job requisitions.
      - name: High-Volume Applicant Import
        description: Bulk applicant import operations to support high-volume hiring and third-party sourcing pipelines.
      - name: Position Management
        description: Create and manage positions and position restrictions within the position management staffing model.
      - name: Recruiting Configuration
        description: Manage recruiting configuration including questionnaires, assessment categories, veteran statuses, site brands, and regions.
      - name: OAuth 2.0 Authentication
        description: Standards-based OAuth 2.0 authentication for secure programmatic access to recruiting data.
      - name: SOAP Web Services
        description: Comprehensive SOAP web services with over 120 recruiting operations for deep enterprise integration.
  - type: UseCases
    data:
      - name: Applicant Tracking System Integration
        description: Sync requisitions, candidates, and applications between Workday and third-party ATS or CRM platforms.
      - name: Talent Sourcing Automation
        description: Push candidates from sourcing tools and job boards into Workday requisition pipelines.
      - name: Job Board Distribution
        description: Automatically distribute Workday job postings to external job boards and career site networks.
      - name: Background Screening Workflow
        description: Trigger and ingest background check results from screening vendors tied to candidate stages.
      - name: Interview Coordination
        description: Integrate with calendar and scheduling tools to coordinate interviewer availability and candidate self-scheduling.
      - name: Assessment and Skills Testing
        description: Connect Workday Recruiting to assessment platforms for skills, behavioral, and technical evaluations.
      - name: Hiring Analytics and Reporting
        description: Extract recruiting data for reporting in BI tools, data warehouses, and people analytics platforms.
      - name: Onboarding Handoff
        description: Trigger onboarding workflows in HRIS or onboarding platforms upon requisition fill or hire stage.
      - name: Recruiting Agency Submissions
        description: Enable third-party staffing agencies to submit candidates directly into Workday requisitions.
      - name: Compliance and EEO Reporting
        description: Capture self-identification data and applicant flow logs to satisfy EEO, OFCCP, and regional reporting requirements.
      - name: Internal Mobility
        description: Connect internal career site workflows to surface roles to existing employees.
      - name: High-Volume Hiring
        description: Power retail, hospitality, and seasonal hiring with bulk applicant import and rapid-disposition workflows.
  - type: Integrations
    data:
      - name: Workday HCM
        description: Native integration with Workday Human Capital Management for seamless transition from candidate to employee.
      - name: LinkedIn Talent Solutions
        description: Connect with LinkedIn Recruiter and LinkedIn Job Postings for sourcing and posting workflows.
      - name: Indeed
        description: Distribute Workday job postings to Indeed and ingest applications back into Workday.
      - name: HireRight
        description: Background check integration for criminal, employment, and education verification.
      - name: Sterling
        description: Background screening, drug testing, and identity verification integration.
      - name: HackerRank
        description: Technical assessment integration for engineering and developer hiring pipelines.
      - name: Calendly
        description: Self-schedule interview integration for candidate-driven scheduling.
      - name: Microsoft Outlook and Teams
        description: Calendar and meeting integration for interview scheduling and coordination.
      - name: Google Workspace
        description: Calendar and meeting integration for interview scheduling.
      - name: DocuSign
        description: E-signature integration for offer letter and onboarding document workflows.
      - name: Workday Marketplace Partners
        description: Pre-built integrations with talent acquisition vendors listed in the Workday Marketplace.
  - type: Solutions
    data:
      - name: Workday Talent Acquisition
        description: End-to-end recruiting solution from sourcing through hire, unifying recruiting with the broader Workday HCM platform.
      - name: HiredScore AI for Recruiting
        description: AI-driven candidate matching, screening, and recruiter productivity embedded in Workday Recruiting.
      - name: Workday Onboarding
        description: Native onboarding handoff that converts hires into engaged employees inside the Workday HCM system of record.
      - name: Workday Skills Cloud
        description: Skills-driven hiring leveraging the Workday skills ontology across requisitions and candidate profiles.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
