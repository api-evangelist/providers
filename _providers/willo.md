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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Willo Agentic Access
  operation_count: 44
  slug: willo-agentic-access
  summary_line: 44 operations · 25 acting
api_count: 9
apis:
- description: Organisations created under a parent organisation, inheriting its properties but managed independently.
  name: Willo Child Organisations API
  slug: willo-child-organisations-api
- description: Sub-divisions of the account (shown as "Companies" in the UI), each with its own branding.
  name: Willo Departments API
  slug: willo-departments-api
- description: Pre-built interview templates and their categories, used to create interviews quickly.
  name: Willo Interview Templates API
  slug: willo-interview-templates-api
- description: A named set of pre-defined questions a participant answers; typically a "job" in an ATS.
  name: Willo Interviews API
  slug: willo-interviews-api
- description: Invite, reminder, and success email/SMS templates sent to participants.
  name: Willo Message Templates API
  slug: willo-message-templates-api
- description: Candidates invited to an interview - no download, login, or authentication required.
  name: Willo Participants API
  slug: willo-participants-api
- description: Read-only reference data - languages and IDV countries of employment.
  name: Willo Reference API
  slug: willo-reference-api
- description: Authenticated team members (Owner, Admin, Standard) with access to interviews and participants.
  name: Willo Users API
  slug: willo-users-api
- description: Notifications posted to a third-party endpoint on new response, stage change, new comment, or new score.
  name: Willo Webhooks API
  slug: willo-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Willo Integration API V2 Child Organisations API
  slug: open-willo-child-organisations-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Departments API
  slug: open-willo-departments-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Interview Templates API
  slug: open-willo-interview-templates-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Interviews API
  slug: open-willo-interviews-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Message Templates API
  slug: open-willo-message-templates-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Participants API
  slug: open-willo-participants-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Reference API
  slug: open-willo-reference-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Users API
  slug: open-willo-users-api
- collection_type: open
  name: Willo Integration API V2 Child Organisations Webhooks API
  slug: open-willo-webhooks-api
- collection_type: open
  name: Willo Integration API V2
  slug: open-willo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/willo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/willo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/willo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/willo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/willovideo
- group: company
  title: ''
  type: Website
  url: https://www.willo.video/
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/7798010/VUjSEiSn
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.willo.video/
- group: start
  title: ''
  type: SignUp
  url: https://app.willotalent.com/integrations
- group: operate
  title: ''
  type: Support
  url: https://support.willo.video/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.willo.video/
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.willo.video/changelog
- group: commercial
  title: ''
  type: Plans
  url: plans/willo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/willo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/willo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.willo.video/blog
created: '2026-07-10'
description: Willo is an asynchronous ("one-way") video interviewing and screening platform that lets teams invite candidates to record answers to pre-defined questions on any browser or device with no downloads, apps, or login required. The Willo Integration API V2 exposes the platform's UI actions as a public REST API so you can embed video interviewing into a job board, ATS, CRM, or staffing platform - managing Departments (Companies), Interviews (jobs and their questions), Participants (candidates) and their video Responses, Message Templates, Users, Webhooks, and Interview Templates. Authentication is by an integration key (API key) from the Willo Integrations page, sent in the Authorization header over HTTPS.
finops:
- name: Willo Finops
  service_category: HR Tech and Recruitment
  slug: willo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/willo.png
layout: provider
modified: '2026-07-10'
name: Willo
nav: Providers
network: true
overview: 'Willo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Child Organisations API, Departments API, Interview Templates API, and 6 more. Tagged areas include Video Interviewing, Recruitment, HR Tech, ATS, and Screening.


  Willo''s developer surface includes authentication, documentation, signup flow, support, changelog, engineering blog, and 10 more developer resources.'
plans:
- name: Willo Plans Pricing
  plan_count: 4
  slug: willo-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 4
  name: Willo Rate Limits
  slug: willo-rate-limits
score:
  band: developing
  composite: 45.0
  delta: -5.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 61.3
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/willo/refs/heads/main/screenshots/willo-2026-08-17T082930.png
security:
- kind: authentication
  name: Willo Authentication
  slug: willo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Willo Domain Security
  slug: willo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Willo Trust Center
  slug: willo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: willo
tags:
- Video Interviewing
- Recruitment
- HR Tech
- ATS
- Screening
- Async Video
website: https://www.willo.video/
---
