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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Workable Agentic Access
  operation_count: 82
  slug: workable-agentic-access
  summary_line: 82 operations · 39 acting
api_count: 33
apis:
- description: Create, read, update, and publish job postings. Jobs are the core organizing entity in Workable; pipelines, candidates, members, and activities are scoped to a job shortcode.
  name: Workable Jobs API
  slug: workable-jobs-api
- description: Create candidates from external sources, retrieve candidate profiles, and update profile data, resumes, cover letters, and source attribution.
  name: Workable Candidates API
  slug: workable-candidates-api
- description: Read pipeline stages configured for a job and move candidates between stages (sourced, applied, phone screen, interview, offer, hired).
  name: Workable Stages API
  slug: workable-stages-api
- description: Manage Workable team members, recruiter accounts, and the per-job collaborators (hiring managers, interviewers, reviewers).
  name: Workable Members API
  slug: workable-members-api
- description: Manage external agency recruiters who can submit candidates against Workable jobs.
  name: Workable Recruiters API
  slug: workable-recruiters-api
- description: Read the company's department list used to scope job postings and reporting.
  name: Workable Departments API
  slug: workable-departments-api
- description: Define and read custom attributes attached to candidates, jobs, and requisitions for tenant-specific reporting and automation.
  name: Workable Custom Attributes API
  slug: workable-custom-attributes-api
- description: Read activity-log entries for candidates and jobs (stage moves, comments, evaluations) for audit and integration use cases.
  name: Workable Activities API
  slug: workable-activities-api
- description: Add and read free-form comments and @-mentions on candidate profiles for collaboration with hiring teams.
  name: Workable Comments API
  slug: workable-comments-api
- description: Submit and read interviewer evaluations and scorecards aligned to the job's interview kit.
  name: Workable Evaluations API
  slug: workable-evaluations-api
- description: Generate and track offers including templates, compensation breakdowns, and offer letter PDFs.
  name: Workable Offers API
  slug: workable-offers-api
- description: Trigger and read candidate assessments delivered through Workable's assessment platform (Assessments+).
  name: Workable Assessments API
  slug: workable-assessments-api
- description: List configured disqualification reasons used when rejecting a candidate (not a fit, withdrew, declined offer, hired elsewhere).
  name: Workable Disqualification Reasons API
  slug: workable-disqualification-reasons-api
- description: Manage application form questions per job, including knockout questions and EEO surveys.
  name: Workable Questions API
  slug: workable-questions-api
- description: Read and create scheduled events (phone screens, interviews) for a candidate, integrated with Workable's calendar sync.
  name: Workable Events API
  slug: workable-events-api
- description: Subscribe to Workable events (candidate.created, candidate.moved, candidate.hired, candidate.disqualified, member.created) for downstream automation.
  name: Workable Webhooks API
  slug: workable-webhooks-api
- description: Read-only public endpoint that exposes published jobs for embedding job listings on external careers pages without authentication.
  name: Workable Public Jobs API
  slug: workable-public-jobs-api
- description: The Accounts API from Workable — 6 operation(s) for accounts.
  name: Workable Accounts API
  slug: workable-accounts-api
- description: The Candidates API from Workable — 16 operation(s) for candidates.
  name: Workable Candidates API
  slug: workable-candidates-api
- description: The CustomAttributes API from Workable — 2 operation(s) for customattributes.
  name: Workable CustomAttributes API
  slug: workable-customattributes-api
- description: The Departments API from Workable — 3 operation(s) for departments.
  name: Workable Departments API
  slug: workable-departments-api
- description: The Employees API from Workable — 5 operation(s) for employees.
  name: Workable Employees API
  slug: workable-employees-api
- description: The Events API from Workable — 2 operation(s) for events.
  name: Workable Events API
  slug: workable-events-api
- description: The Jobs API from Workable — 9 operation(s) for jobs.
  name: Workable Jobs API
  slug: workable-jobs-api
- description: The Members API from Workable — 4 operation(s) for members.
  name: Workable Members API
  slug: workable-members-api
- description: The Offers API from Workable — 3 operation(s) for offers.
  name: Workable Offers API
  slug: workable-offers-api
- description: The Recruiters API from Workable — 1 operation(s) for recruiters.
  name: Workable Recruiters API
  slug: workable-recruiters-api
- description: The Requisitions API from Workable — 4 operation(s) for requisitions.
  name: Workable Requisitions API
  slug: workable-requisitions-api
- description: The ReviewCycles API from Workable — 2 operation(s) for reviewcycles.
  name: Workable ReviewCycles API
  slug: workable-reviewcycles-api
- description: The Stages API from Workable — 1 operation(s) for stages.
  name: Workable Stages API
  slug: workable-stages-api
- description: The Subscriptions API from Workable — 2 operation(s) for subscriptions.
  name: Workable Subscriptions API
  slug: workable-subscriptions-api
- description: The TimeOff API from Workable — 4 operation(s) for timeoff.
  name: Workable TimeOff API
  slug: workable-timeoff-api
- description: The TimeTracking API from Workable — 3 operation(s) for timetracking.
  name: Workable TimeTracking API
  slug: workable-timetracking-api
artifact_total: 65
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workable Accounts API
  slug: open-workable-accounts-api
- collection_type: open
  name: Workable Accounts Candidates API
  slug: open-workable-candidates-api
- collection_type: open
  name: Workable Accounts CustomAttributes API
  slug: open-workable-customattributes-api
- collection_type: open
  name: Workable Accounts Departments API
  slug: open-workable-departments-api
- collection_type: open
  name: Workable Accounts Employees API
  slug: open-workable-employees-api
- collection_type: open
  name: Workable Accounts Events API
  slug: open-workable-events-api
- collection_type: open
  name: Workable Accounts Jobs API
  slug: open-workable-jobs-api
- collection_type: open
  name: Workable Accounts Members API
  slug: open-workable-members-api
- collection_type: open
  name: Workable Accounts Offers API
  slug: open-workable-offers-api
- collection_type: open
  name: Workable Accounts Recruiters API
  slug: open-workable-recruiters-api
- collection_type: open
  name: Workable Accounts Requisitions API
  slug: open-workable-requisitions-api
- collection_type: open
  name: Workable Accounts Stages API
  slug: open-workable-stages-api
- collection_type: open
  name: Workable Accounts Subscriptions API
  slug: open-workable-subscriptions-api
- collection_type: open
  name: Workable Accounts TimeOff API
  slug: open-workable-timeoff-api
- collection_type: open
  name: Workable Accounts TimeTracking API
  slug: open-workable-timetracking-api
- collection_type: open
  name: Workable API
  slug: open-workable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workable-software
- group: company
  title: ''
  type: Website
  url: https://www.workable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://workable.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://workable.readme.io/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workable.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.workable.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workable.com/
- group: company
  title: ''
  type: Blog
  url: https://resources.workable.com/
- group: operate
  title: ''
  type: Support
  url: https://help.workable.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workable
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workable.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workable.com/terms
- group: commercial
  title: ''
  type: Plans
  url: plans/workable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/workable-finops.yml
created: '2026-05-08'
description: Workable is an end-to-end hiring platform with ATS, AI sourcing, employer branding, video interviewing, assessments, and HR. The Workable REST API (v3) exposes jobs, candidates, stages, members, departments, custom attributes, offers, assessments, and webhooks.
features:
- REST API v3 with bearer-token authentication
- Workable subdomain-scoped base URL (https://{subdomain}.workable.com/spi/v3/)
- Standard plan from $299/month, Premier $599/month, Enterprise $719/month
- 20% annual discount on all paid plans
- Texting+, Video Interviews+, Assessments+ available as Standard add-ons
- Webhooks for candidate, member, and stage events
- AI sourcing and employer-branding integrated alongside ATS
- Public jobs feed for embedding on external careers pages
finops:
- name: Workable Finops
  service_category: HR
  slug: workable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workable.png
layout: provider
modified: '2026-05-08'
name: Workable
nav: Providers
network: true
overview: 'Workable publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Jobs API, Candidates API, Stages API, and 21 more. Tagged areas include HR, ATS, Recruiting, Sourcing, and Video Interviews.


  Workable''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Workable Plans Pricing
  plan_count: 7
  slug: workable-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Workable Rate Limits
  slug: workable-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 51.5
    developer_ergonomics: 31.0
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workable/refs/heads/main/screenshots/workable-2026-06-20T201548.png
security:
- kind: authentication
  name: Workable Authentication
  slug: workable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workable Domain Security
  slug: workable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Workable Trust Center
  slug: workable-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, GDPR
slug: workable
tags:
- HR
- ATS
- Recruiting
- Sourcing
- Video Interviews
- Assessments
- Software-as-a-Service
website: https://www.workable.com/
---
