---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pinpoint Agentic Access
  operation_count: 16
  slug: pinpoint-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://{subdomain}.pinpointhq.com/api/v1
  baseurl_source: declared
  description: Candidate (applicant) records.
  name: Pinpoint Applicants API
  slug: pinpoint-applicants-api
- baseURL: https://{subdomain}.pinpointhq.com/api/v1
  baseurl_source: declared
  description: Candidate applications moving through hiring workflows.
  name: Pinpoint Applications API
  slug: pinpoint-applications-api
- baseURL: https://{subdomain}.pinpointhq.com/api/v1
  baseurl_source: declared
  description: Comments on applications.
  name: Pinpoint Comments API
  slug: pinpoint-comments-api
- baseURL: https://{subdomain}.pinpointhq.com/api/v1
  baseurl_source: declared
  description: Job postings and requisitions.
  name: Pinpoint Jobs API
  slug: pinpoint-jobs-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pinpoint Applicants API
  slug: open-pinpoint-applicants-api
- collection_type: open
  name: Pinpoint Applicants Applications API
  slug: open-pinpoint-applications-api
- collection_type: open
  name: Pinpoint Applicants Comments API
  slug: open-pinpoint-comments-api
- collection_type: open
  name: Pinpoint Applicants Jobs API
  slug: open-pinpoint-jobs-api
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
random_paper: 20
rate_limits:
- limit_count: 3
  name: Pinpoint Rate Limits
  slug: pinpoint-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/pinpoint/refs/heads/main/screenshots/pinpoint-2026-09-02T151506.png
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
