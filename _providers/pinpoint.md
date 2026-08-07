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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pinpoint Agentic Access
  operation_count: 16
  slug: pinpoint-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 4
apis:
- description: Candidate (applicant) records.
  name: Pinpoint Applicants API
  slug: pinpoint-applicants-api
- description: Candidate applications moving through hiring workflows.
  name: Pinpoint Applications API
  slug: pinpoint-applications-api
- description: Comments on applications.
  name: Pinpoint Comments API
  slug: pinpoint-comments-api
- description: Job postings and requisitions.
  name: Pinpoint Jobs API
  slug: pinpoint-jobs-api
artifact_total: 11
collections:
- collection_type: open
  name: Pinpoint API
  slug: open-pinpoint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinpoint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinpoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinpoint-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinpoint-hq
- group: company
  title: ''
  type: Website
  url: https://www.pinpointhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pinpointhq.com/docs/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/pinpoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pinpoint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pinpoint-finops.yml
created: '2026-06-21'
description: Pinpoint is an applicant tracking system (ATS) and recruitment platform for in-house talent teams. Its REST API follows the JSON:API specification and is served per-tenant at https://{subdomain}.pinpointhq.com/api/v1, exposing jobs, applications, candidates, comments, files, and webhooks for building recruitment integrations. Not to be confused with AWS Pinpoint (customer engagement) or Pinpoint (signal/data intelligence).
finops:
- name: Pinpoint Finops
  service_category: Recruitment and HR Technology
  slug: pinpoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pinpoint.png
layout: provider
modified: '2026-06-21'
name: Pinpoint
nav: Providers
network: true
overview: 'Pinpoint publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applicants API, Applications API, Comments API, and 1 more. Tagged areas include ATS, Recruitment, Hiring, HR Tech, and JSON:API.


  Pinpoint''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Pinpoint Plans Pricing
  plan_count: 1
  slug: pinpoint-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 3
  name: Pinpoint Rate Limits
  slug: pinpoint-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Pinpoint Authentication
  slug: pinpoint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pinpoint Domain Security
  slug: pinpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinpoint
tags:
- ATS
- Recruitment
- Hiring
- HR Tech
- JSON:API
website: https://www.pinpointhq.com
---
