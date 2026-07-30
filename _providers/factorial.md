---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Factorial Agentic Access
  operation_count: 30
  slug: factorial-agentic-access
  summary_line: 30 operations · 18 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Versioned REST API for managing employees, contracts, leaves, attendance shifts, time off, documents, and other HR resources in Factorial. Supports API key (Bearer token) and OAuth 2.0 authentication,
  name: Factorial Developer API
  slug: developer-api
- description: The Resources API from Factorial — 16 operation(s) for resources.
  name: Factorial Resources API
  slug: factorial-resources-api
arazzos:
- description: Confirm an employee, add a payroll supplement for them, and list supplements to confirm.
  name: Factorial Add Payroll Supplement
  slug: factorial-add-payroll-supplement-workflow
- description: Find an existing contract version and update it, otherwise create a new one.
  name: Factorial Amend Contract
  slug: factorial-amend-contract-workflow
- description: Clock an employee in, confirm the open shift, then clock them out.
  name: Factorial Attendance Day
  slug: factorial-attendance-day-workflow
- description: Confirm an employee exists, create a contract version for them, and read it back.
  name: Factorial Create Contract Version
  slug: factorial-create-contract-workflow
- description: Look up an employee by email, then file a time off request for the matched employee.
  name: Factorial Find Employee and File Leave
  slug: factorial-find-employee-file-leave-workflow
- description: Confirm an employee, log a completed attendance shift, and read it back.
  name: Factorial Log Attendance Shift
  slug: factorial-log-attendance-shift-workflow
- description: Confirm an employee, terminate them, and verify the termination was recorded.
  name: Factorial Offboard Employee
  slug: factorial-offboard-employee-workflow
- description: Create an employee, confirm the record, assign teams, and send the Factorial invitation.
  name: Factorial Onboard Employee
  slug: factorial-onboard-employee-workflow
- description: Find an employee's existing leave, reschedule it, and confirm the new dates.
  name: Factorial Reschedule Time Off
  slug: factorial-reschedule-time-off-workflow
- description: Create a time off request and read back its stored status.
  name: Factorial Submit Time Off
  slug: factorial-submit-time-off-workflow
- description: Confirm an employee, update their profile fields, and read the record back.
  name: Factorial Update Employee Profile
  slug: factorial-update-employee-profile-workflow
- description: Confirm an employee, upload a document for them, and confirm it appears in their documents.
  name: Factorial Upload Employee Document
  slug: factorial-upload-employee-document-workflow
artifact_total: 21
collections:
- collection_type: open
  name: Factorial Developer API
  slug: open-factorial
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/factorial-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/factorial-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/factorial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/factorial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/factorial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/factorial-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-add-payroll-supplement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-amend-contract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-attendance-day-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-create-contract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-find-employee-file-leave-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-log-attendance-shift-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-offboard-employee-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-onboard-employee-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-reschedule-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-submit-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-update-employee-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/factorial-upload-employee-document-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/factorialco
- group: company
  title: ''
  type: Website
  url: https://factorialhr.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com
- group: commercial
  title: ''
  type: Pricing
  url: https://factorialhr.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://factorialhr.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.factorialhr.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/factorial-hr
- group: agent
  title: ''
  type: LlmsText
  url: https://factorialhr.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://factorialhr.com/blog/feed
created: '2026-05-11'
description: Factorial is a Spain-headquartered HRIS and human resources platform offering employee management, time tracking, attendance, time off, payroll, performance, recruitment, documents, and expenses for small and mid-sized businesses. The Factorial Developer API provides versioned REST endpoints (dated like 2026-04-01) for integrating with employees, leaves, contracts, attendance shifts, and other HR resources, with API key and OAuth 2.0 authentication and both production and demo environments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/factorial.png
layout: provider
modified: '2026-05-11'
name: Factorial
nav: Providers
network: true
overview: 'Factorial publishes 1 API on the [APIs.io](https://apis.io/) network: Resources API. Tagged areas include Human Resources, HRIS, Employee Management, Time Tracking, and Payroll.


  Factorial''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 21 more developer resources.'
random_paper: 47
scopes:
- name: Factorial Scopes
  scope_count: 2
  slug: factorial-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 29.8
  delta: -1.9
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/factorial/refs/heads/main/screenshots/factorial-2026-06-20T181037.png
security:
- kind: authentication
  name: Factorial Authentication
  slug: factorial-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Factorial Domain Security
  slug: factorial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Factorial Vulnerability Disclosure
  slug: factorial-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Factorial Trust Center
  slug: factorial-trust-center
  summary_line: SOC 2, ISO 27001
slug: factorial
tags:
- Human Resources
- HRIS
- Employee Management
- Time Tracking
- Payroll
- Time Off
- Performance Management
website: https://factorialhr.com
---
