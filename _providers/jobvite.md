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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'REST APIs for exchanging candidate, requisition, and application data between Jobvite and external systems in JSON format. Includes the Onboard New Hire API for pushing employee data into the Jobvite '
  name: Jobvite REST API
  slug: rest-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobvite-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Jobvite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jobvite
- group: company
  title: ''
  type: Website
  url: https://www.jobvite.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.jobvite.com
- group: other
  title: ''
  type: Parent Company
  url: https://www.employinc.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jobvite.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.jobvite.com/request-a-demo
- group: operate
  title: ''
  type: Support
  url: https://help.jobvite.com
- group: company
  title: ''
  type: Blog
  url: https://www.jobvite.com/feed/
created: '2026-05-11'
description: Jobvite, part of Employ Inc., is an applicant tracking system (ATS) and recruiting platform that helps enterprises source, hire, and onboard talent. The platform combines candidate relationship management, recruitment marketing, branded career sites, and onboarding workflows. Jobvite provides REST APIs that facilitate real-time data exchange in JSON for candidate records, requisitions, applications, and the Onboard New Hire endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jobvite.png
layout: provider
modified: '2026-05-11'
name: Jobvite
nav: Providers
network: true
overview: 'Jobvite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Applicant Tracking, ATS, Recruiting, Human Resources, and Talent Acquisition.


  Jobvite''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 5 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 15.3
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jobvite/refs/heads/main/screenshots/jobvite-2026-06-20T183746.png
security:
- kind: domain-security
  name: Jobvite Domain Security
  slug: jobvite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jobvite
tags:
- Applicant Tracking
- ATS
- Recruiting
- Human Resources
- Talent Acquisition
- Onboarding
website: https://www.jobvite.com
---
