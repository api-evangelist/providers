---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Workday Recruiting Agentic Access
  operation_count: 47
  slug: workday-recruiting-agentic-access
  summary_line: 47 operations · 23 acting
api_count: 13
apis:
- description: SOAP-based web service providing comprehensive access to Workday Recruiting business services data for integration with talent management and applicant tracking systems. Includes over 120 operations c
  name: Workday Recruiting SOAP Web Services API
  slug: workday-recruiting-soap-web-services-api
- description: To view and maintain Agent Definitions with the Agent System of Record.
  name: Workday Recruiting agentDefinition API
  slug: workday-recruiting-agentdefinition-api
- description: Retrieve and manage pre-hire and applicant records, including high-volume applicant import operations.
  name: Workday Recruiting Applicants API
  slug: workday-recruiting-applicants-api
- description: Submit and retrieve background check results and manage background check packages for candidate screening.
  name: Workday Recruiting Background Checks API
  slug: workday-recruiting-background-checks-api
- description: Create, retrieve, and update candidate profiles including personal information, attachments, photos, and assessment data.
  name: Workday Recruiting Candidates API
  slug: workday-recruiting-candidates-api
- description: Manage recruiting configuration settings including questionnaires, assessment categories, veteran statuses, site brands, and regions.
  name: Workday Recruiting Configuration API
  slug: workday-recruiting-configuration-api
- description: Manage evergreen requisitions used for ongoing hiring needs without a specific number of openings or close date.
  name: Workday Recruiting Evergreen Requisitions API
  slug: workday-recruiting-evergreen-requisitions-api
- description: Schedule interviews, submit interview feedback, manage interview settings, and configure self-schedule calendars.
  name: Workday Recruiting Interviews API
  slug: workday-recruiting-interviews-api
- description: Manage the lifecycle of job applications from submission through disposition, including stage movement and offer initiation.
  name: Workday Recruiting Job Applications API
  slug: workday-recruiting-job-applications-api
- description: Post, update, and unpost jobs to internal and external career sites, and manage job posting site configurations.
  name: Workday Recruiting Job Postings API
  slug: workday-recruiting-job-postings-api
- description: Create, retrieve, edit, close, freeze, and manage job requisitions for open positions within Workday recruiting workflows.
  name: Workday Recruiting Job Requisitions API
  slug: workday-recruiting-job-requisitions-api
- description: Create and manage positions and position restrictions within the position management staffing model.
  name: Workday Recruiting Positions API
  slug: workday-recruiting-positions-api
- description: Manage recruiting agency relationships, agency users, and agency candidate submissions.
  name: Workday Recruiting Recruiting Agencies API
  slug: workday-recruiting-recruiting-agencies-api
arazzos:
- description: Resolve a recruiting agency, submit one of its candidates to a requisition, and confirm the application.
  name: Workday Recruiting Agency Candidate Submission
  slug: workday-recruiting-agency-candidate-submission-workflow
- description: Confirm a target requisition, submit a bulk applicant import, and verify the loaded applicants.
  name: Workday Recruiting Bulk Applicant Import
  slug: workday-recruiting-bulk-applicant-import-workflow
- description: Confirm a requisition, unpost its active posting, then close the requisition.
  name: Workday Recruiting Close a Requisition and Unpost Its Jobs
  slug: workday-recruiting-close-requisition-and-unpost-workflow
- description: Find an open requisition, create the referred candidate, and submit the referral.
  name: Workday Recruiting Employee Referral
  slug: workday-recruiting-employee-referral-workflow
- description: Schedule an interview, capture feedback, and initiate an offer on a positive result.
  name: Workday Recruiting Interview to Offer
  slug: workday-recruiting-interview-to-offer-workflow
- description: Create a candidate, attach a resume, record an assessment, and read the profile back.
  name: Workday Recruiting Onboard a Candidate with Resume and Assessment
  slug: workday-recruiting-onboard-candidate-with-resume-workflow
- description: Create a job requisition, confirm it, then post its job to career sites.
  name: Workday Recruiting Create and Source a Job Requisition
  slug: workday-recruiting-post-and-source-requisition-workflow
- description: Find an application in review for a requisition, inspect it, and move it forward.
  name: Workday Recruiting Screen and Advance a Job Application
  slug: workday-recruiting-screen-and-advance-application-workflow
artifact_total: 171
collections:
- collection_type: postman
  name: Workday Recruiting REST API
  slug: postman-workday-recruiting-rest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Recruiting REST Applicants agentDefinition API
  slug: open-workday-recruiting-agentdefinition-api
- collection_type: open
  name: Workday Recruiting REST Applicants API
  slug: open-workday-recruiting-applicants-api
- collection_type: open
  name: Workday Recruiting REST Applicants Background Checks API
  slug: open-workday-recruiting-background-checks-api
- collection_type: open
  name: Workday Recruiting REST Applicants Candidates API
  slug: open-workday-recruiting-candidates-api
- collection_type: open
  name: Workday Recruiting REST Applicants Configuration API
  slug: open-workday-recruiting-configuration-api
- collection_type: open
  name: Workday Recruiting REST Applicants Evergreen Requisitions API
  slug: open-workday-recruiting-evergreen-requisitions-api
- collection_type: open
  name: Workday Recruiting REST Applicants Interviews API
  slug: open-workday-recruiting-interviews-api
- collection_type: open
  name: Workday Recruiting REST Applicants Job Applications API
  slug: open-workday-recruiting-job-applications-api
- collection_type: open
  name: Workday Recruiting REST Applicants Job Postings API
  slug: open-workday-recruiting-job-postings-api
- collection_type: open
  name: Workday Recruiting REST Applicants Job Requisitions API
  slug: open-workday-recruiting-job-requisitions-api
- collection_type: open
  name: Workday Recruiting REST Applicants Positions API
  slug: open-workday-recruiting-positions-api
- collection_type: open
  name: Workday Recruiting REST Applicants Recruiting Agencies API
  slug: open-workday-recruiting-recruiting-agencies-api
- collection_type: open
  name: Workday Recruiting REST API
  slug: open-workday-recruiting-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-recruiting-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-recruiting-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-recruiting-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-recruiting-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-recruiting-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-recruiting/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-agency-candidate-submission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-bulk-applicant-import-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-close-requisition-and-unpost-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-employee-referral-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-interview-to-offer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-onboard-candidate-with-resume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-post-and-source-requisition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-recruiting-screen-and-advance-application-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://community.workday.com
- group: start
  title: ''
  type: GettingStarted
  url: https://community.workday.com/api-start
- group: docs
  title: ''
  type: Documentation
  url: https://community.workday.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
- group: start
  title: ''
  type: Console
  url: https://developer.workday.com/about
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/application-development.html
- group: operate
  title: ''
  type: StatusPage
  url: https://community.workday.com/trust/status
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/services/support.html
- group: start
  title: ''
  type: Signup
  url: https://resourcecenter.workday.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: operate
  title: ''
  type: RateLimits
  url: https://community.workday.com/articles/16827
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.workday.com/api-versions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: build
  title: Workday Everywhere SDK
  type: Tools
  url: https://www.npmjs.com/package/@workday/everywhere
- group: build
  title: Workday Canvas Kit
  type: Tools
  url: https://github.com/Workday/canvas-kit
- group: build
  title: Workday Extend JavaScript Example
  type: CodeExamples
  url: https://github.com/Workday/extend-js-example
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- group: company
  title: ''
  type: Partners
  url: https://www.workday.com/en-us/company/partners/overview.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-recruiting-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-recruiting-vocabulary.yaml
created: '2024-01-01'
description: APIs for Workday's cloud-based recruiting and talent acquisition solution, providing programmatic access to job requisitions, candidate management, applications, interviews, job postings, and hiring workflows.
examples:
- key_count: 8
  name: Recruiting Rest Api Applicant Example
  slug: recruiting-rest-api-applicant-example
- key_count: 6
  name: Recruiting Rest Api Applicant Import Example
  slug: recruiting-rest-api-applicant-import-example
- key_count: 6
  name: Recruiting Rest Api Attachment Example
  slug: recruiting-rest-api-attachment-example
- key_count: 5
  name: Recruiting Rest Api Background Check Create Example
  slug: recruiting-rest-api-background-check-create-example
- key_count: 7
  name: Recruiting Rest Api Background Check Example
  slug: recruiting-rest-api-background-check-example
- key_count: 5
  name: Recruiting Rest Api Background Check Package Example
  slug: recruiting-rest-api-background-check-package-example
- key_count: 6
  name: Recruiting Rest Api Candidate Assessment Example
  slug: recruiting-rest-api-candidate-assessment-example
- key_count: 6
  name: Recruiting Rest Api Candidate Create Example
  slug: recruiting-rest-api-candidate-create-example
- key_count: 13
  name: Recruiting Rest Api Candidate Example
  slug: recruiting-rest-api-candidate-example
- key_count: 4
  name: Recruiting Rest Api Evergreen Requisition Create Example
  slug: recruiting-rest-api-evergreen-requisition-create-example
- key_count: 9
  name: Recruiting Rest Api Evergreen Requisition Example
  slug: recruiting-rest-api-evergreen-requisition-example
- key_count: 8
  name: Recruiting Rest Api Interview Create Example
  slug: recruiting-rest-api-interview-create-example
- key_count: 10
  name: Recruiting Rest Api Interview Example
  slug: recruiting-rest-api-interview-example
- key_count: 3
  name: Recruiting Rest Api Interview Feedback Create Example
  slug: recruiting-rest-api-interview-feedback-create-example
- key_count: 6
  name: Recruiting Rest Api Interview Feedback Example
  slug: recruiting-rest-api-interview-feedback-example
- key_count: 9
  name: Recruiting Rest Api Job Application Example
  slug: recruiting-rest-api-job-application-example
- key_count: 13
  name: Recruiting Rest Api Job Posting Example
  slug: recruiting-rest-api-job-posting-example
- key_count: 5
  name: Recruiting Rest Api Job Posting Site Example
  slug: recruiting-rest-api-job-posting-site-example
- key_count: 13
  name: Recruiting Rest Api Job Requisition Create Example
  slug: recruiting-rest-api-job-requisition-create-example
- key_count: 20
  name: Recruiting Rest Api Job Requisition Example
  slug: recruiting-rest-api-job-requisition-example
- key_count: 5
  name: Recruiting Rest Api Offer Create Example
  slug: recruiting-rest-api-offer-create-example
- key_count: 9
  name: Recruiting Rest Api Offer Example
  slug: recruiting-rest-api-offer-example
- key_count: 7
  name: Recruiting Rest Api Position Create Example
  slug: recruiting-rest-api-position-create-example
- key_count: 11
  name: Recruiting Rest Api Position Example
  slug: recruiting-rest-api-position-example
- key_count: 5
  name: Recruiting Rest Api Questionnaire Example
  slug: recruiting-rest-api-questionnaire-example
- key_count: 7
  name: Recruiting Rest Api Recruiting Agency Example
  slug: recruiting-rest-api-recruiting-agency-example
- key_count: 2
  name: Recruiting Rest Api Reference Example
  slug: recruiting-rest-api-reference-example
- key_count: 3
  name: Recruiting Rest Api Veteran Status Example
  slug: recruiting-rest-api-veteran-status-example
features:
- description: Create, edit, close, freeze, and reopen job requisitions for open positions, with full lifecycle and approval workflow support.
  name: Job Requisition Management
- description: Manage ongoing requisitions used for continuous hiring needs without a specific number of openings or close date.
  name: Evergreen Requisitions
- description: Create, retrieve, and update candidate profiles including personal information, attachments, photos, and assessment data.
  name: Candidate Management
- description: Manage applications from submission through disposition, including stage movement, advancement, and offer initiation.
  name: Job Application Lifecycle
- description: Post, update, and unpost jobs to internal and external career sites and manage job posting site brands and configurations.
  name: Job Posting Distribution
- description: Schedule interviews, submit interview feedback, configure interview settings, and manage self-schedule calendars.
  name: Interview Scheduling
- description: Submit and retrieve background check results and manage background check packages for candidate screening.
  name: Background Check Integration
- description: Manage agency relationships, agency users, and agency candidate submissions tied to job requisitions.
  name: Recruiting Agency Workflows
- description: Bulk applicant import operations to support high-volume hiring and third-party sourcing pipelines.
  name: High-Volume Applicant Import
- description: Create and manage positions and position restrictions within the position management staffing model.
  name: Position Management
- description: Manage recruiting configuration including questionnaires, assessment categories, veteran statuses, site brands, and regions.
  name: Recruiting Configuration
- description: Standards-based OAuth 2.0 authentication for secure programmatic access to recruiting data.
  name: OAuth 2.0 Authentication
- description: Comprehensive SOAP web services with over 120 recruiting operations for deep enterprise integration.
  name: SOAP Web Services
finops:
- name: Workday Recruiting Finops
  service_category: API
  slug: workday-recruiting-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-recruiting.png
integrations:
- description: Native integration with Workday Human Capital Management for seamless transition from candidate to employee.
  name: Workday HCM
- description: Connect with LinkedIn Recruiter and LinkedIn Job Postings for sourcing and posting workflows.
  name: LinkedIn Talent Solutions
- description: Distribute Workday job postings to Indeed and ingest applications back into Workday.
  name: Indeed
- description: Background check integration for criminal, employment, and education verification.
  name: HireRight
- description: Background screening, drug testing, and identity verification integration.
  name: Sterling
- description: Technical assessment integration for engineering and developer hiring pipelines.
  name: HackerRank
- description: Self-schedule interview integration for candidate-driven scheduling.
  name: Calendly
- description: Calendar and meeting integration for interview scheduling and coordination.
  name: Microsoft Outlook and Teams
- description: Calendar and meeting integration for interview scheduling.
  name: Google Workspace
- description: E-signature integration for offer letter and onboarding document workflows.
  name: DocuSign
- description: Pre-built integrations with talent acquisition vendors listed in the Workday Marketplace.
  name: Workday Marketplace Partners
json_schemas:
- name: ApplicantImport
  property_count: 6
  slug: recruiting-rest-api-applicant-import
- name: Applicant
  property_count: 8
  slug: recruiting-rest-api-applicant
- name: Attachment
  property_count: 6
  slug: recruiting-rest-api-attachment
- name: BackgroundCheckCreate
  property_count: 5
  slug: recruiting-rest-api-background-check-create
- name: BackgroundCheckPackage
  property_count: 5
  slug: recruiting-rest-api-background-check-package
- name: BackgroundCheck
  property_count: 7
  slug: recruiting-rest-api-background-check
- name: CandidateAssessment
  property_count: 6
  slug: recruiting-rest-api-candidate-assessment
- name: CandidateCreate
  property_count: 6
  slug: recruiting-rest-api-candidate-create
- name: Candidate
  property_count: 13
  slug: recruiting-rest-api-candidate
- name: EvergreenRequisitionCreate
  property_count: 4
  slug: recruiting-rest-api-evergreen-requisition-create
- name: EvergreenRequisition
  property_count: 9
  slug: recruiting-rest-api-evergreen-requisition
- name: InterviewCreate
  property_count: 8
  slug: recruiting-rest-api-interview-create
- name: InterviewFeedbackCreate
  property_count: 3
  slug: recruiting-rest-api-interview-feedback-create
- name: InterviewFeedback
  property_count: 6
  slug: recruiting-rest-api-interview-feedback
- name: Interview
  property_count: 10
  slug: recruiting-rest-api-interview
- name: JobApplication
  property_count: 9
  slug: recruiting-rest-api-job-application
- name: JobPosting
  property_count: 13
  slug: recruiting-rest-api-job-posting
- name: JobPostingSite
  property_count: 5
  slug: recruiting-rest-api-job-posting-site
- name: JobRequisitionCreate
  property_count: 13
  slug: recruiting-rest-api-job-requisition-create
- name: JobRequisition
  property_count: 20
  slug: recruiting-rest-api-job-requisition
- name: OfferCreate
  property_count: 5
  slug: recruiting-rest-api-offer-create
- name: Offer
  property_count: 9
  slug: recruiting-rest-api-offer
- name: PositionCreate
  property_count: 7
  slug: recruiting-rest-api-position-create
- name: Position
  property_count: 11
  slug: recruiting-rest-api-position
- name: Questionnaire
  property_count: 5
  slug: recruiting-rest-api-questionnaire
- name: RecruitingAgency
  property_count: 7
  slug: recruiting-rest-api-recruiting-agency
- name: Reference
  property_count: 2
  slug: recruiting-rest-api-reference
- name: VeteranStatus
  property_count: 3
  slug: recruiting-rest-api-veteran-status
json_structures:
- name: Recruiting Rest Api Applicant Import Structure
  property_count: 6
  slug: recruiting-rest-api-applicant-import-structure
- name: Recruiting Rest Api Applicant Structure
  property_count: 8
  slug: recruiting-rest-api-applicant-structure
- name: Recruiting Rest Api Attachment Structure
  property_count: 6
  slug: recruiting-rest-api-attachment-structure
- name: Recruiting Rest Api Background Check Create Structure
  property_count: 5
  slug: recruiting-rest-api-background-check-create-structure
- name: Recruiting Rest Api Background Check Package Structure
  property_count: 5
  slug: recruiting-rest-api-background-check-package-structure
- name: Recruiting Rest Api Background Check Structure
  property_count: 7
  slug: recruiting-rest-api-background-check-structure
- name: Recruiting Rest Api Candidate Assessment Structure
  property_count: 6
  slug: recruiting-rest-api-candidate-assessment-structure
- name: Recruiting Rest Api Candidate Create Structure
  property_count: 6
  slug: recruiting-rest-api-candidate-create-structure
- name: Recruiting Rest Api Candidate Structure
  property_count: 13
  slug: recruiting-rest-api-candidate-structure
- name: Recruiting Rest Api Evergreen Requisition Create Structure
  property_count: 4
  slug: recruiting-rest-api-evergreen-requisition-create-structure
- name: Recruiting Rest Api Evergreen Requisition Structure
  property_count: 9
  slug: recruiting-rest-api-evergreen-requisition-structure
- name: Recruiting Rest Api Interview Create Structure
  property_count: 8
  slug: recruiting-rest-api-interview-create-structure
- name: Recruiting Rest Api Interview Feedback Create Structure
  property_count: 3
  slug: recruiting-rest-api-interview-feedback-create-structure
- name: Recruiting Rest Api Interview Feedback Structure
  property_count: 6
  slug: recruiting-rest-api-interview-feedback-structure
- name: Recruiting Rest Api Interview Structure
  property_count: 10
  slug: recruiting-rest-api-interview-structure
- name: Recruiting Rest Api Job Application Structure
  property_count: 9
  slug: recruiting-rest-api-job-application-structure
- name: Recruiting Rest Api Job Posting Site Structure
  property_count: 5
  slug: recruiting-rest-api-job-posting-site-structure
- name: Recruiting Rest Api Job Posting Structure
  property_count: 13
  slug: recruiting-rest-api-job-posting-structure
- name: Recruiting Rest Api Job Requisition Create Structure
  property_count: 13
  slug: recruiting-rest-api-job-requisition-create-structure
- name: Recruiting Rest Api Job Requisition Structure
  property_count: 20
  slug: recruiting-rest-api-job-requisition-structure
- name: Recruiting Rest Api Offer Create Structure
  property_count: 5
  slug: recruiting-rest-api-offer-create-structure
- name: Recruiting Rest Api Offer Structure
  property_count: 9
  slug: recruiting-rest-api-offer-structure
- name: Recruiting Rest Api Position Create Structure
  property_count: 7
  slug: recruiting-rest-api-position-create-structure
- name: Recruiting Rest Api Position Structure
  property_count: 11
  slug: recruiting-rest-api-position-structure
- name: Recruiting Rest Api Questionnaire Structure
  property_count: 5
  slug: recruiting-rest-api-questionnaire-structure
- name: Recruiting Rest Api Recruiting Agency Structure
  property_count: 7
  slug: recruiting-rest-api-recruiting-agency-structure
- name: Recruiting Rest Api Reference Structure
  property_count: 2
  slug: recruiting-rest-api-reference-structure
- name: Recruiting Rest Api Veteran Status Structure
  property_count: 3
  slug: recruiting-rest-api-veteran-status-structure
jsonld:
- class_count: 31
  name: Workday Recruiting Rest Api Context
  property_count: 99
  slug: workday-recruiting-rest-api-context
layout: provider
modified: '2026-05-19'
name: Workday Recruiting
nav: Providers
network: true
overview: 'Workday Recruiting publishes 12 APIs on the [APIs.io](https://apis.io/) network, including agentDefinition API, Applicants API, Background Checks API, and 9 more. Tagged areas include HCM, Human Resources, Recruiting, Software-as-a-Service, and Talent Acquisition.


  The Workday Recruiting catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Recruiting''s developer surface includes authentication, developer portal, getting-started guide, documentation, developer console, engineering blog, support, and 28 more developer resources.'
plans:
- name: Workday Recruiting Plans Pricing
  plan_count: 3
  slug: workday-recruiting-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Workday Recruiting Rate Limits
  slug: workday-recruiting-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Workday Recruiting API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-recruiting-jsonschema-spectral-rules
- effective_rule_count: 114
  extends:
  - spectral:oas
  name: Workday Recruiting API Rules
  rule_count: 73
  severity_counts:
    error: 25
    hint: 0
    info: 7
    warn: 41
  slug: workday-recruiting-spectral-rules
scopes:
- name: Workday Recruiting Scopes
  scope_count: 2
  slug: workday-recruiting-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 43.8
  delta: 1.5
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 28.8
    contract_quality: 32.5
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 28.9
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-recruiting/refs/heads/main/screenshots/workday-recruiting-2026-06-20T201608.png
security:
- kind: authentication
  name: Workday Recruiting Authentication
  slug: workday-recruiting-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Workday Recruiting Domain Security
  slug: workday-recruiting-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Workday Recruiting Trust Center
  slug: workday-recruiting-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-recruiting
solutions:
- description: End-to-end recruiting solution from sourcing through hire, unifying recruiting with the broader Workday HCM platform.
  name: Workday Talent Acquisition
- description: AI-driven candidate matching, screening, and recruiter productivity embedded in Workday Recruiting.
  name: HiredScore AI for Recruiting
- description: Native onboarding handoff that converts hires into engaged employees inside the Workday HCM system of record.
  name: Workday Onboarding
- description: Skills-driven hiring leveraging the Workday skills ontology across requisitions and candidate profiles.
  name: Workday Skills Cloud
tags:
- HCM
- Human Resources
- Recruiting
- Software-as-a-Service
- Talent Acquisition
use_cases:
- description: Sync requisitions, candidates, and applications between Workday and third-party ATS or CRM platforms.
  name: Applicant Tracking System Integration
- description: Push candidates from sourcing tools and job boards into Workday requisition pipelines.
  name: Talent Sourcing Automation
- description: Automatically distribute Workday job postings to external job boards and career site networks.
  name: Job Board Distribution
- description: Trigger and ingest background check results from screening vendors tied to candidate stages.
  name: Background Screening Workflow
- description: Integrate with calendar and scheduling tools to coordinate interviewer availability and candidate self-scheduling.
  name: Interview Coordination
- description: Connect Workday Recruiting to assessment platforms for skills, behavioral, and technical evaluations.
  name: Assessment and Skills Testing
- description: Extract recruiting data for reporting in BI tools, data warehouses, and people analytics platforms.
  name: Hiring Analytics and Reporting
- description: Trigger onboarding workflows in HRIS or onboarding platforms upon requisition fill or hire stage.
  name: Onboarding Handoff
- description: Enable third-party staffing agencies to submit candidates directly into Workday requisitions.
  name: Recruiting Agency Submissions
- description: Capture self-identification data and applicant flow logs to satisfy EEO, OFCCP, and regional reporting requirements.
  name: Compliance and EEO Reporting
- description: Connect internal career site workflows to surface roles to existing employees.
  name: Internal Mobility
- description: Power retail, hospitality, and seasonal hiring with bulk applicant import and rapid-disposition workflows.
  name: High-Volume Hiring
website: https://community.workday.com
---
