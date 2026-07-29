---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful API for managing recruitment workflows including jobs, candidates, placements, submissions, interviews, and companies in JobAdder. Authentication uses OAuth 2.0 authorization code flow with be
  name: JobAdder REST API
  slug: rest-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobadder-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jobadder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jobadder-com
- group: company
  title: ''
  type: Website
  url: https://jobadder.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jobadder.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://jobadderapi.zendesk.com/hc/en-us
- group: start
  title: ''
  type: Signup
  url: https://jobadder.com/contact-sales
- group: commercial
  title: ''
  type: Pricing
  url: https://jobadder.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://jobadder.com/blog/feed/
created: '2026-05-11'
description: JobAdder is a cloud-based recruitment and applicant tracking platform used by staffing agencies and in-house talent acquisition teams to manage jobs, candidates, placements, and client relationships. The platform offers a comprehensive REST API that exposes recruitment workflows including job posting, candidate search, application tracking, and analytics. The JobAdder API uses OAuth 2.0 authorization code flow with region-specific base URLs returned in the token response.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jobadder.png
layout: provider
modified: '2026-05-11'
name: JobAdder
nav: Providers
network: true
overview: 'JobAdder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Recruitment, Applicant Tracking System, Staffing, Human Resources, and Talent Acquisition.


  JobAdder''s developer surface includes documentation, support, signup flow, pricing, engineering blog, and 4 more developer resources.'
random_paper: 57
score:
  band: minimal
  composite: 12.7
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jobadder/refs/heads/main/screenshots/jobadder-2026-06-20T183744.png
security:
- kind: domain-security
  name: Jobadder Domain Security
  slug: jobadder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jobadder
tags:
- Recruitment
- Applicant Tracking System
- Staffing
- Human Resources
- Talent Acquisition
- Hiring
website: https://jobadder.com
---
