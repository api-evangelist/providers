---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Indeed Agentic Access
  operation_count: 12
  slug: indeed-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 15
apis:
- description: Search for jobs by keyword, location, and other criteria. Returns job listings with details including title, company, location, and description. This API is deprecated and not available for new integr
  name: Indeed Job Search API
  slug: job-search
- description: Monetize your website by displaying Indeed job listings. Earn revenue through cost-per-click advertising.
  name: Indeed Publisher API
  slug: publisher
- description: Allow job seekers to apply to your jobs directly through Indeed with a streamlined application process. Supports screener questions, EEO compliance for US employers, and disposition data integration.
  name: Indeed Apply API
  slug: apply
- description: A GraphQL API that enables ATS partners to send disposition data for Indeed Apply and non-Indeed Apply jobs to Indeed, tracking application status changes through various stages of the hiring process.
  name: Indeed Disposition Sync API
  slug: disposition-sync
- description: A GraphQL API used to get information about and manage an employer's sponsored job campaigns on Indeed, including campaign creation, budget management, and performance insights.
  name: Indeed Sponsored Jobs API
  slug: sponsored-jobs
- description: Allows partners to list and update job postings on Indeed, including adding metadata to ATS-sourced jobs for improved quality and sponsorship grouping, and subscribing to jobs lifecycle events via web
  name: Indeed Job Update API
  slug: job-update
- description: Stream real-time server-sent events (SSE) to enable front-end applications to update instantly, supporting event filtering, deduplication, and latency tracking.
  name: Indeed Real-time API
  slug: real-time
- description: A GraphQL API for scheduling, updating, retrieving information about, and canceling virtual interview events with job candidates. This API is deprecated.
  name: Indeed Interview API
  slug: interview
- description: A GraphQL API for creating and updating employer entities on Indeed and the Indeed PLUS platform.
  name: Indeed Employer Data API
  slug: employer-data
- description: Tracks candidate events such as job application page visits and completed applications from Indeed to your site. Provides data for reporting, analytics dashboards, and apply-based bidding algorithms.
  name: Indeed Conversion Tracking API
  slug: conversion-tracking
- description: Part of the Candidate Sync APIs, this API allows ATS partners to register employers for Candidate Sync integration.
  name: Indeed Employer Registration API
  slug: employer-registration
- description: Part of the Candidate Sync APIs, this API enables ATS partners to get candidate and application information from Indeed on behalf of employers.
  name: Indeed Retrieve Candidates API
  slug: retrieve-candidates
- description: Operations for retrieving and managing candidate applications. Part of the Candidate Sync APIs, these endpoints enable ATS partners to fetch candidate and application data from Indeed on behalf of reg
  name: Indeed Candidates API
  slug: indeed-candidates-api
- description: Operations for creating and managing employer profiles on Indeed. Employer entities must be created before job postings can be associated with them. Supports global attributes such as employer name an
  name: Indeed Employers API
  slug: indeed-employers-api
- description: Operations for creating, updating, expiring, and retrieving job postings on Indeed. Supports qualifications, working hours, salary, benefits, employer information, and Indeed Apply configuration.
  name: Indeed Jobs API
  slug: indeed-jobs-api
artifact_total: 173
collections:
- collection_type: postman
  name: Indeed Employer Candidates API
  slug: postman-indeed-candidates-api
- collection_type: postman
  name: Indeed Employer Candidates Employers API
  slug: postman-indeed-employers-api
- collection_type: postman
  name: Indeed Employer Candidates Jobs API
  slug: postman-indeed-jobs-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Indeed Employer Candidates API
  slug: open-indeed-candidates-api
- collection_type: open
  name: Indeed Employer API
  slug: open-indeed-employer-api
- collection_type: open
  name: Indeed Employer Candidates Employers API
  slug: open-indeed-employers-api
- collection_type: open
  name: Indeed Employer Candidates Jobs API
  slug: open-indeed-jobs-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/indeed/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/indeed-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indeed-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/indeed-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/indeed-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opensource.indeedeng.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.indeed.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.indeed.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.indeed.com
- group: operate
  title: ''
  type: Support
  url: https://support.indeed.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://engineering.indeedblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indeedeng
- group: other
  title: ''
  type: X
  url: https://twitter.com/indeedeng
- group: operate
  title: ''
  type: RateLimits
  url: https://opensource.indeedeng.io/api-documentation/docs/rate-limits
- group: auth
  title: ''
  type: Authentication
  url: https://docs.indeed.com/authorization/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.indeed.com/getstarted/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.indeed.com/release-notes/
- group: start
  title: ''
  type: Sandbox
  url: https://docs.indeed.com/getstarted/simulated-graphql-environment
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/indeed-com/
created: '2025-01-01'
description: Indeed is the world's largest job site, connecting millions of job seekers with employers across industries and locations worldwide. Indeed offers a suite of APIs for applicant tracking systems, job boards, and hiring platforms to integrate with its employment ecosystem.
examples:
- key_count: 6
  name: Indeed Createemployer Example
  slug: indeed-createemployer-example
- key_count: 6
  name: Indeed Createjobpostings Example
  slug: indeed-createjobpostings-example
- key_count: 6
  name: Indeed Employer Address Example
  slug: indeed-employer-address-example
- key_count: 3
  name: Indeed Employer Api Error Example
  slug: indeed-employer-api-error-example
- key_count: 2
  name: Indeed Employer Benefit Example
  slug: indeed-employer-benefit-example
- key_count: 13
  name: Indeed Employer Candidate Example
  slug: indeed-employer-candidate-example
- key_count: 2
  name: Indeed Employer Candidate List Example
  slug: indeed-employer-candidate-list-example
- key_count: 3
  name: Indeed Employer Country Specific Attributes Example
  slug: indeed-employer-country-specific-attributes-example
- key_count: 1
  name: Indeed Employer Create Job Posting Input Example
  slug: indeed-employer-create-job-posting-input-example
- key_count: 3
  name: Indeed Employer Create Job Posting Payload Example
  slug: indeed-employer-create-job-posting-payload-example
- key_count: 4
  name: Indeed Employer Disposition Update Example
  slug: indeed-employer-disposition-update-example
- key_count: 4
  name: Indeed Employer Eeo Responses Example
  slug: indeed-employer-eeo-responses-example
- key_count: 3
  name: Indeed Employer Employer Attributes Example
  slug: indeed-employer-employer-attributes-example
- key_count: 5
  name: Indeed Employer Employer Example
  slug: indeed-employer-employer-example
- key_count: 4
  name: Indeed Employer Employer Registration Example
  slug: indeed-employer-employer-registration-example
- key_count: 4
  name: Indeed Employer Indeed Apply Config Example
  slug: indeed-employer-indeed-apply-config-example
- key_count: 6
  name: Indeed Employer Job Location Example
  slug: indeed-employer-job-location-example
- key_count: 13
  name: Indeed Employer Job Posting Example
  slug: indeed-employer-job-posting-example
- key_count: 2
  name: Indeed Employer Job Posting List Example
  slug: indeed-employer-job-posting-list-example
- key_count: 2
  name: Indeed Employer Job Source Example
  slug: indeed-employer-job-source-example
- key_count: 3
  name: Indeed Employer Locale Specific Attributes Example
  slug: indeed-employer-locale-specific-attributes-example
- key_count: 4
  name: Indeed Employer Page Info Example
  slug: indeed-employer-page-info-example
- key_count: 2
  name: Indeed Employer Patch Employer Input Example
  slug: indeed-employer-patch-employer-input-example
- key_count: 2
  name: Indeed Employer Patch Employer Payload Example
  slug: indeed-employer-patch-employer-payload-example
- key_count: 3
  name: Indeed Employer Qualification Example
  slug: indeed-employer-qualification-example
- key_count: 3
  name: Indeed Employer Resume Example
  slug: indeed-employer-resume-example
- key_count: 3
  name: Indeed Employer Resume File Example
  slug: indeed-employer-resume-file-example
- key_count: 4
  name: Indeed Employer Salary Example
  slug: indeed-employer-salary-example
- key_count: 5
  name: Indeed Employer Screener Question Example
  slug: indeed-employer-screener-question-example
- key_count: 3
  name: Indeed Employer Screener Question Response Example
  slug: indeed-employer-screener-question-response-example
- key_count: 3
  name: Indeed Employer Working Hours Example
  slug: indeed-employer-working-hours-example
- key_count: 6
  name: Indeed Updatecandidatedisposition Example
  slug: indeed-updatecandidatedisposition-example
features:
- description: Search millions of job listings by keyword, location, salary, and other criteria across industries worldwide.
  name: Job Search and Discovery
- description: Post and syndicate job listings from ATS platforms to Indeed's marketplace with automated synchronization.
  name: Job Posting and Syndication
- description: Retrieve and manage candidate applications, track disposition status, and sync hiring data with ATS systems.
  name: Candidate Management
- description: Create and manage pay-per-click sponsored job campaigns with budget controls and performance analytics.
  name: Sponsored Job Campaigns
- description: Enable one-click job applications directly through Indeed with screener questions and EEO compliance.
  name: Indeed Apply Integration
- description: Track candidate events from Indeed to employer sites for analytics, reporting, and bidding optimization.
  name: Conversion Tracking
- description: Stream server-sent events for instant application updates and job lifecycle notifications.
  name: Real-Time Event Streaming
finops:
- name: Indeed Finops
  service_category: Recruiting + Job Advertising
  slug: indeed-finops
graphqls:
- description: A GraphQL API that enables ATS partners to create, upsert, expire, and get status for job postings on Indeed. Supports qualifications, working hours, salary, benefits, and employer information.
  name: Indeed GraphQL API
  slug: indeed-graphql
image: https://www.indeed.com/images/indeed-logo.png
integrations:
- description: Native ATS integration for job posting synchronization and candidate data exchange with Greenhouse.
  name: Greenhouse
- description: Pre-built integration for posting jobs and retrieving candidate applications through Lever ATS.
  name: Lever
- description: Enterprise integration for syncing job postings and candidate data with Workday Recruiting.
  name: Workday
- description: Integration for job distribution and candidate management through iCIMS talent acquisition platform.
  name: iCIMS
- description: Connector for job posting and candidate synchronization with SAP SuccessFactors Recruiting.
  name: SAP SuccessFactors
- description: Integration for distributing jobs and managing candidates through Oracle Taleo ATS.
  name: Oracle Taleo
json_schemas:
- name: Address
  property_count: 6
  slug: indeed-address
- name: ApiError
  property_count: 3
  slug: indeed-apierror
- name: Benefit
  property_count: 2
  slug: indeed-benefit
- name: Indeed Candidate
  property_count: 19
  slug: indeed-candidate
- name: CandidateList
  property_count: 3
  slug: indeed-candidatelist
- name: CountrySpecificAttributes
  property_count: 4
  slug: indeed-countryspecificattributes
- name: CreateJobPostingInput
  property_count: 1
  slug: indeed-createjobpostinginput
- name: CreateJobPostingPayload
  property_count: 3
  slug: indeed-createjobpostingpayload
- name: DispositionUpdate
  property_count: 4
  slug: indeed-dispositionupdate
- name: EeoResponses
  property_count: 4
  slug: indeed-eeoresponses
- name: Address
  property_count: 6
  slug: indeed-employer-address
- name: ApiError
  property_count: 3
  slug: indeed-employer-api-error
- name: Benefit
  property_count: 2
  slug: indeed-employer-benefit
- name: CandidateList
  property_count: 2
  slug: indeed-employer-candidate-list
- name: Candidate
  property_count: 13
  slug: indeed-employer-candidate
- name: CountrySpecificAttributes
  property_count: 3
  slug: indeed-employer-country-specific-attributes
- name: CreateJobPostingInput
  property_count: 1
  slug: indeed-employer-create-job-posting-input
- name: CreateJobPostingPayload
  property_count: 3
  slug: indeed-employer-create-job-posting-payload
- name: DispositionUpdate
  property_count: 4
  slug: indeed-employer-disposition-update
- name: EeoResponses
  property_count: 4
  slug: indeed-employer-eeo-responses
- name: EmployerAttributes
  property_count: 3
  slug: indeed-employer-employer-attributes
- name: EmployerRegistration
  property_count: 4
  slug: indeed-employer-employer-registration
- name: Employer
  property_count: 5
  slug: indeed-employer-employer
- name: IndeedApplyConfig
  property_count: 4
  slug: indeed-employer-indeed-apply-config
- name: JobLocation
  property_count: 6
  slug: indeed-employer-job-location
- name: JobPostingList
  property_count: 2
  slug: indeed-employer-job-posting-list
- name: JobPosting
  property_count: 13
  slug: indeed-employer-job-posting
- name: JobSource
  property_count: 2
  slug: indeed-employer-job-source
- name: LocaleSpecificAttributes
  property_count: 3
  slug: indeed-employer-locale-specific-attributes
- name: PageInfo
  property_count: 4
  slug: indeed-employer-page-info
- name: PatchEmployerInput
  property_count: 2
  slug: indeed-employer-patch-employer-input
- name: PatchEmployerPayload
  property_count: 2
  slug: indeed-employer-patch-employer-payload
- name: Qualification
  property_count: 3
  slug: indeed-employer-qualification
- name: ResumeFile
  property_count: 3
  slug: indeed-employer-resume-file
- name: Resume
  property_count: 3
  slug: indeed-employer-resume
- name: Salary
  property_count: 4
  slug: indeed-employer-salary
- name: Employer
  property_count: 6
  slug: indeed-employer
- name: ScreenerQuestionResponse
  property_count: 3
  slug: indeed-employer-screener-question-response
- name: ScreenerQuestion
  property_count: 5
  slug: indeed-employer-screener-question
- name: WorkingHours
  property_count: 3
  slug: indeed-employer-working-hours
- name: EmployerAttributes
  property_count: 3
  slug: indeed-employerattributes
- name: EmployerRegistration
  property_count: 4
  slug: indeed-employerregistration
- name: IndeedApplyConfig
  property_count: 4
  slug: indeed-indeedapplyconfig
- name: JobLocation
  property_count: 6
  slug: indeed-joblocation
- name: JobPosting
  property_count: 18
  slug: indeed-jobposting
- name: JobPostingList
  property_count: 3
  slug: indeed-jobpostinglist
- name: JobSource
  property_count: 2
  slug: indeed-jobsource
- name: LocaleSpecificAttributes
  property_count: 3
  slug: indeed-localespecificattributes
- name: PageInfo
  property_count: 4
  slug: indeed-pageinfo
- name: PatchEmployerInput
  property_count: 3
  slug: indeed-patchemployerinput
- name: PatchEmployerPayload
  property_count: 3
  slug: indeed-patchemployerpayload
- name: Qualification
  property_count: 3
  slug: indeed-qualification
- name: Resume
  property_count: 4
  slug: indeed-resume
- name: ResumeFile
  property_count: 3
  slug: indeed-resumefile
- name: Salary
  property_count: 4
  slug: indeed-salary
- name: ScreenerQuestion
  property_count: 5
  slug: indeed-screenerquestion
- name: ScreenerQuestionResponse
  property_count: 3
  slug: indeed-screenerquestionresponse
- name: WorkingHours
  property_count: 3
  slug: indeed-workinghours
json_structures:
- name: Indeed Employer Address Structure
  property_count: 6
  slug: indeed-employer-address-structure
- name: Indeed Employer Api Error Structure
  property_count: 3
  slug: indeed-employer-api-error-structure
- name: Indeed Employer Benefit Structure
  property_count: 2
  slug: indeed-employer-benefit-structure
- name: Indeed Employer Candidate List Structure
  property_count: 2
  slug: indeed-employer-candidate-list-structure
- name: Indeed Employer Candidate Structure
  property_count: 13
  slug: indeed-employer-candidate-structure
- name: Indeed Employer Country Specific Attributes Structure
  property_count: 3
  slug: indeed-employer-country-specific-attributes-structure
- name: Indeed Employer Create Job Posting Input Structure
  property_count: 1
  slug: indeed-employer-create-job-posting-input-structure
- name: Indeed Employer Create Job Posting Payload Structure
  property_count: 3
  slug: indeed-employer-create-job-posting-payload-structure
- name: Indeed Employer Disposition Update Structure
  property_count: 4
  slug: indeed-employer-disposition-update-structure
- name: Indeed Employer Eeo Responses Structure
  property_count: 4
  slug: indeed-employer-eeo-responses-structure
- name: Indeed Employer Employer Attributes Structure
  property_count: 3
  slug: indeed-employer-employer-attributes-structure
- name: Indeed Employer Employer Registration Structure
  property_count: 4
  slug: indeed-employer-employer-registration-structure
- name: Indeed Employer Employer Structure
  property_count: 5
  slug: indeed-employer-employer-structure
- name: Indeed Employer Indeed Apply Config Structure
  property_count: 4
  slug: indeed-employer-indeed-apply-config-structure
- name: Indeed Employer Job Location Structure
  property_count: 6
  slug: indeed-employer-job-location-structure
- name: Indeed Employer Job Posting List Structure
  property_count: 2
  slug: indeed-employer-job-posting-list-structure
- name: Indeed Employer Job Posting Structure
  property_count: 13
  slug: indeed-employer-job-posting-structure
- name: Indeed Employer Job Source Structure
  property_count: 2
  slug: indeed-employer-job-source-structure
- name: Indeed Employer Locale Specific Attributes Structure
  property_count: 3
  slug: indeed-employer-locale-specific-attributes-structure
- name: Indeed Employer Page Info Structure
  property_count: 4
  slug: indeed-employer-page-info-structure
- name: Indeed Employer Patch Employer Input Structure
  property_count: 2
  slug: indeed-employer-patch-employer-input-structure
- name: Indeed Employer Patch Employer Payload Structure
  property_count: 2
  slug: indeed-employer-patch-employer-payload-structure
- name: Indeed Employer Qualification Structure
  property_count: 3
  slug: indeed-employer-qualification-structure
- name: Indeed Employer Resume File Structure
  property_count: 3
  slug: indeed-employer-resume-file-structure
- name: Indeed Employer Resume Structure
  property_count: 3
  slug: indeed-employer-resume-structure
- name: Indeed Employer Salary Structure
  property_count: 4
  slug: indeed-employer-salary-structure
- name: Indeed Employer Screener Question Response Structure
  property_count: 3
  slug: indeed-employer-screener-question-response-structure
- name: Indeed Employer Screener Question Structure
  property_count: 5
  slug: indeed-employer-screener-question-structure
- name: Indeed Employer Working Hours Structure
  property_count: 3
  slug: indeed-employer-working-hours-structure
- name: Indeed Structure
  property_count: 0
  slug: indeed-structure
jsonld:
- class_count: 0
  name: Indeed Context
  property_count: 14
  slug: indeed-context
- class_count: 0
  name: Indeed Employer Context
  property_count: 0
  slug: indeed-employer-context
layout: provider
modified: '2026-05-19'
name: Indeed
nav: Providers
network: true
overview: 'Indeed publishes 3 APIs on the [APIs.io](https://apis.io/) network: Candidates API, Employers API, and Jobs API. Tagged areas include Careers, Employment, Hiring, Job Search, and Jobs.


  The Indeed catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Indeed''s developer surface includes authentication, support, engineering blog, getting-started guide, release notes, sandbox, and 13 more developer resources.'
plans:
- name: Indeed Plans Pricing
  plan_count: 2
  slug: indeed-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Indeed Rate Limits
  slug: indeed-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Indeed API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: indeed-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Indeed API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: indeed-spectral-rules
scopes:
- name: Indeed Scopes
  scope_count: 3
  slug: indeed-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 42.8
  delta: -12.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 75.5
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/indeed/refs/heads/main/screenshots/indeed-2026-06-20T183344.png
security:
- kind: authentication
  name: Indeed Authentication
  slug: indeed-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Indeed Domain Security
  slug: indeed-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: indeed
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
use_cases:
- description: Automatically distribute job postings from applicant tracking systems to Indeed's marketplace with real-time synchronization.
  name: ATS Job Distribution
- description: Retrieve and manage candidates through the hiring pipeline with disposition tracking and status updates.
  name: Candidate Pipeline Management
- description: Track campaign performance, application conversions, and ROI across sponsored and organic job listings.
  name: Recruitment Marketing Analytics
- description: Create and manage employer profiles on Indeed to attract candidates with company information and branding.
  name: Employer Branding
- description: Scale recruitment operations with automated job posting, candidate retrieval, and application processing.
  name: High-Volume Hiring
website: https://opensource.indeedeng.io/
---
