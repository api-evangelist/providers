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
api_count: 3
apis:
- description: REST API for admin-side ATS operations including candidates, offers (job openings), placements, departments, requisitions, tags, evaluations, scheduled interviews, mailbox messages, and reports. All e
  name: Recruitee Company (ATS) API
  slug: company-api
- description: Public, read-only API used by careers sites and embedded job widgets to fetch published offers, departments, and locations for unauthenticated job seekers. Backs the careers.recruitee.com hosted pages
  name: Recruitee Careers Site API
  slug: careers-site-api
- description: Subscribe to ATS events such as candidate created, candidate stage changed, offer published, evaluation created, and interview scheduled to drive event-driven integrations and HRIS synchronization.
  name: Recruitee Webhooks
  slug: webhooks
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/recruitee-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recruitee-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recruitee
- group: company
  title: ''
  type: Website
  url: https://recruitee.com
- group: other
  title: ''
  type: Parent Company
  url: https://tellent.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recruitee.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.recruitee.com/reference/getting-started
- group: operate
  title: ''
  type: Help Center
  url: https://support.recruitee.com
- group: commercial
  title: ''
  type: Pricing
  url: https://recruitee.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.recruitee.com/#/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.recruitee.com
- group: company
  title: ''
  type: Blog
  url: https://recruitee.com/articles
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recruitee
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.recruitee.com/llms.txt
created: '2026-05-11'
description: Recruitee (part of Tellent) is a collaborative applicant tracking system (ATS) and recruiting platform that helps growing companies build hiring pipelines, publish careers sites, manage candidates, schedule interviews, and collaborate on hiring decisions. Its REST API at https://api.recruitee.com exposes endpoints for candidates, offers, placements, departments, tags, evaluations, interviews, mailboxes, and reports, scoped to a company by the path segment /c/{company_id}. Authentication uses a Bearer personal API token generated from Settings, Apps and plugins, Personal API tokens, with permissions inherited from the creator's Hiring role.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recruitee.png
layout: provider
modified: '2026-05-11'
name: Recruitee
nav: Providers
network: true
overview: 'Recruitee publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Recruiting, ATS, Applicant Tracking, HR, and Hiring.


  Recruitee''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.2
  delta: -2.6
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/screenshots/recruitee-2026-06-20T192710.png
security:
- kind: domain-security
  name: Recruitee Domain Security
  slug: recruitee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Recruitee Trust Center
  slug: recruitee-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: recruitee
tags:
- Recruiting
- ATS
- Applicant Tracking
- HR
- Hiring
- Careers Site
- Tellent
website: https://recruitee.com
---
