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
api_count: 1
apis:
- description: REST API for accessing Paycor employees, payroll, benefits, time, and organizational data. Uses OAuth 2.0 authorization code flow with authorization at secure.paycor.com/connect/authorize and tokens i
  name: Paycor Public API v1
  slug: public-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paycor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paycor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paycor
- group: company
  title: ''
  type: Website
  url: https://www.paycor.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.paycor.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paycor.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://developers.paycor.com/register
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.paycor.com/llms.txt
created: '2026-05-11'
description: Paycor is a cloud-based human capital management (HCM) platform that provides payroll, HR, benefits administration, talent management, time and attendance, and workforce analytics for small and mid-sized businesses. The platform serves HR and finance teams with a unified system of record for employees, pay, time, and benefits data. Paycor exposes a Public REST API authenticated via OAuth 2.0 with authorization at secure.paycor.com and resource endpoints at apis.paycor.com (production) and apis-sandbox.paycor.com (sandbox).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paycor.png
layout: provider
modified: '2026-05-11'
name: Paycor
nav: Providers
network: true
overview: 'Paycor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HCM, Payroll, Human Resources, Benefits Administration, and Time and Attendance.


  Paycor''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/paycor/refs/heads/main/screenshots/paycor-2026-06-20T191452.png
security:
- kind: domain-security
  name: Paycor Domain Security
  slug: paycor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paycor
tags:
- HCM
- Payroll
- Human Resources
- Benefits Administration
- Time and Attendance
website: https://www.paycor.com
---
