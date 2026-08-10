---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Smartrecruiters Agentic Access
  operation_count: 19
  slug: smartrecruiters-agentic-access
  summary_line: 19 operations · 7 acting
api_count: 12
apis:
- description: The Application API enables integration of the full candidate application including screening questions, and allows new applications to be submitted through partner systems and career sites.
  name: SmartRecruiters Application API
  slug: application-api
- description: The Assessment API allows customers to order assessment services available through the SmartRecruiters Marketplace and allows partners to interface with the marketplace to provide and manage assessmen
  name: SmartRecruiters Assessment API
  slug: assessment-api
- description: The Interview API provides self-scheduling capabilities and interview template management for streamlining the interview process between recruiters and candidates.
  name: SmartRecruiters Interview API
  slug: interview-api
- description: The Reporting API provides access to custom reports in CSV format, enabling analytics and data export capabilities for HR metrics and recruiting performance.
  name: SmartRecruiters Reporting API
  slug: reporting-api
- description: The Job Board API enables job board partners to integrate SmartRecruiters job postings directly into their platforms with real-time synchronization.
  name: SmartRecruiters Job Board API
  slug: job-board-api
- description: The Applications API from SmartRecruiters — 3 operation(s) for applications.
  name: SmartRecruiters Applications API
  slug: smartrecruiters-applications-api
- description: The Candidates API from SmartRecruiters — 6 operation(s) for candidates.
  name: SmartRecruiters Candidates API
  slug: smartrecruiters-candidates-api
- description: The Documents API from SmartRecruiters — 1 operation(s) for documents.
  name: SmartRecruiters Documents API
  slug: smartrecruiters-documents-api
- description: The Jobs API from SmartRecruiters — 5 operation(s) for jobs.
  name: SmartRecruiters Jobs API
  slug: smartrecruiters-jobs-api
- description: The Messages API from SmartRecruiters — 1 operation(s) for messages.
  name: SmartRecruiters Messages API
  slug: smartrecruiters-messages-api
- description: The Postings API from SmartRecruiters — 2 operation(s) for postings.
  name: SmartRecruiters Postings API
  slug: smartrecruiters-postings-api
- description: The Teams API from SmartRecruiters — 1 operation(s) for teams.
  name: SmartRecruiters Teams API
  slug: smartrecruiters-teams-api
artifact_total: 58
collections:
- collection_type: open
  name: SmartRecruiters Candidate API
  slug: open-smartrecruiters-candidates
- collection_type: open
  name: SmartRecruiters Job API
  slug: open-smartrecruiters-jobs
- collection_type: open
  name: SmartRecruiters Posting API
  slug: open-smartrecruiters-posting
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartrecruiters-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smartrecruiters-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartrecruiters-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartrecruiters-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/smartrecruiters-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartrecruiters
- group: company
  title: ''
  type: Website
  url: https://www.smartrecruiters.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smartrecruiters.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smartrecruiters.com/docs/the-smartrecruiters-platform
- group: auth
  title: ''
  type: Authentication
  url: https://developers.smartrecruiters.com/docs/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartrecruiters
- group: company
  title: ''
  type: Blog
  url: https://www.smartrecruiters.com/blog/
- group: other
  title: ''
  type: Marketplace
  url: https://www.smartrecruiters.com/marketplace/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.smartrecruiters.com/llms.txt
created: '2025-01-07'
description: SmartRecruiters is a talent acquisition platform that provides a comprehensive suite of APIs for recruiting, hiring, and workforce management. The platform enables organizations to manage job postings, candidate applications, assessments, interviews, and offers through a unified REST API ecosystem.
examples:
- key_count: 2
  name: Smartrecruiters List Postings Example
  slug: smartrecruiters-list-postings-example
- key_count: 2
  name: Smartrecruiters Submit Application Example
  slug: smartrecruiters-submit-application-example
finops:
- name: Smartrecruiters Finops
  service_category: Talent Acquisition / ATS
  slug: smartrecruiters-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartrecruiters.png
json_schemas:
- name: Answer
  property_count: 2
  slug: smartrecruiters-answer
- name: Application
  property_count: 8
  slug: smartrecruiters-application
- name: ApplicationResult
  property_count: 4
  slug: smartrecruiters-applicationresult
- name: ApplicationStatus
  property_count: 4
  slug: smartrecruiters-applicationstatus
- name: ApplicationSubmission
  property_count: 8
  slug: smartrecruiters-applicationsubmission
- name: SmartRecruiters Candidate
  property_count: 12
  slug: smartrecruiters-candidate
- name: CandidateCreate
  property_count: 8
  slug: smartrecruiters-candidatecreate
- name: CandidateListResult
  property_count: 4
  slug: smartrecruiters-candidatelistresult
- name: CandidateUpdate
  property_count: 6
  slug: smartrecruiters-candidateupdate
- name: CompanySummary
  property_count: 2
  slug: smartrecruiters-companysummary
- name: Department
  property_count: 2
  slug: smartrecruiters-department
- name: Document
  property_count: 6
  slug: smartrecruiters-document
- name: EmploymentType
  property_count: 2
  slug: smartrecruiters-employmenttype
- name: ExperienceLevel
  property_count: 2
  slug: smartrecruiters-experiencelevel
- name: Function
  property_count: 2
  slug: smartrecruiters-function
- name: Industry
  property_count: 2
  slug: smartrecruiters-industry
- name: SmartRecruiters Job
  property_count: 14
  slug: smartrecruiters-job
- name: JobCreate
  property_count: 9
  slug: smartrecruiters-jobcreate
- name: JobListResult
  property_count: 4
  slug: smartrecruiters-joblistresult
- name: JobUpdate
  property_count: 3
  slug: smartrecruiters-jobupdate
- name: Location
  property_count: 7
  slug: smartrecruiters-location
- name: Message
  property_count: 5
  slug: smartrecruiters-message
- name: Posting
  property_count: 12
  slug: smartrecruiters-posting
- name: PostingDetails
  property_count: 0
  slug: smartrecruiters-postingdetails
- name: PostingListResult
  property_count: 4
  slug: smartrecruiters-postinglistresult
- name: Question
  property_count: 5
  slug: smartrecruiters-question
- name: SourceDetails
  property_count: 3
  slug: smartrecruiters-sourcedetails
- name: TeamMember
  property_count: 4
  slug: smartrecruiters-teammember
json_structures:
- name: Smartrecruiters Job Structure
  property_count: 0
  slug: smartrecruiters-job-structure
- name: Smartrecruiters Structure
  property_count: 0
  slug: smartrecruiters-structure
jsonld:
- class_count: 37
  name: Smartrecruiters Context
  property_count: 0
  slug: smartrecruiters-context
layout: provider
modified: '2026-05-19'
name: SmartRecruiters
nav: Providers
network: true
overview: 'SmartRecruiters publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Candidates API, Documents API, and 4 more. Tagged areas include Human Resources, Recruiting, Talent Acquisition, Applicant Tracking, and HR Technology.


  The SmartRecruiters catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SmartRecruiters'' developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Smartrecruiters Plans Pricing
  plan_count: 4
  slug: smartrecruiters-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Smartrecruiters Rate Limits
  slug: smartrecruiters-rate-limits
rules:
- name: SmartRecruiters API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: smartrecruiters-jsonschema-spectral-rules
- name: SmartRecruiters API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: smartrecruiters-rules
scopes:
- name: Smartrecruiters Scopes
  scope_count: 4
  slug: smartrecruiters-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 69.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartrecruiters/refs/heads/main/screenshots/smartrecruiters-2026-06-20T194047.png
security:
- kind: authentication
  name: Smartrecruiters Authentication
  slug: smartrecruiters-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Smartrecruiters Domain Security
  slug: smartrecruiters-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Smartrecruiters Trust Center
  slug: smartrecruiters-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: smartrecruiters
tags:
- Human Resources
- Recruiting
- Talent Acquisition
- Applicant Tracking
- HR Technology
website: https://www.smartrecruiters.com/
---
