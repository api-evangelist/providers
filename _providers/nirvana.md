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
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Nirvana Agentic Access
  operation_count: 4
  slug: nirvana-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://coverage-api.meetnirvana.com/v1
  baseurl_source: declared
  description: Real-time per-session patient cost estimates.
  name: Nirvana Health Cost Estimation API
  slug: nirvana-cost-estimation-api
- baseURL: https://coverage-api.meetnirvana.com/v1
  baseurl_source: declared
  description: Multi-payer coverage discovery.
  name: Nirvana Health Coverage Scan API
  slug: nirvana-coverage-scan-api
- baseURL: https://coverage-api.meetnirvana.com/v1
  baseurl_source: declared
  description: Active-coverage discovery and eligibility verification.
  name: Nirvana Health Eligibility API
  slug: nirvana-eligibility-api
- baseURL: https://coverage-api.meetnirvana.com/v1
  baseurl_source: declared
  description: Medicaid coverage and eligibility.
  name: Nirvana Health Medicaid API
  slug: nirvana-medicaid-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nirvana Coverage Cost Estimation API
  slug: open-nirvana-cost-estimation-api
- collection_type: open
  name: Nirvana Coverage Cost Estimation Coverage Scan API
  slug: open-nirvana-coverage-scan-api
- collection_type: open
  name: Nirvana Coverage Cost Estimation Eligibility API
  slug: open-nirvana-eligibility-api
- collection_type: open
  name: Nirvana Coverage Cost Estimation Medicaid API
  slug: open-nirvana-medicaid-api
- collection_type: open
  name: Nirvana Coverage API
  slug: open-nirvana
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nirvana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nirvana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nirvana-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.meetnirvana.com/blog
created: '2026-06-21'
description: Nirvana is a real-time insurance eligibility, benefits, and patient cost-estimation platform purpose-built for behavioral and mental health. Its Coverage API normalizes complex payer data into structured JSON, returning eligibility, plan-level benefits, patient cost-share, session limits, and prior authorization details, and can recover active coverage from only basic patient demographics.
finops:
- name: Nirvana Finops
  service_category: Healthcare and Insurance
  slug: nirvana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nirvana.png
layout: provider
modified: '2026-06-21'
name: Nirvana Health
nav: Providers
network: true
overview: 'Nirvana Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cost Estimation API, Coverage Scan API, Eligibility API, and 1 more. Tagged areas include Healthcare, Insurance, Eligibility, Benefits, and Cost Estimation.


  Nirvana Health''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Nirvana Plans Pricing
  plan_count: 1
  slug: nirvana-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Nirvana Rate Limits
  slug: nirvana-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/nirvana/refs/heads/main/screenshots/nirvana-2026-08-07T185339.png
security:
- kind: authentication
  name: Nirvana Authentication
  slug: nirvana-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nirvana Domain Security
  slug: nirvana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nirvana
tags:
- Healthcare
- Insurance
- Eligibility
- Benefits
- Cost Estimation
- Behavioral Health
---
