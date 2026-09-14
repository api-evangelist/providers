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
- baseURL: https://api.workwelltech.com
  baseurl_source: declared
  description: Raw punch records across a date range
  name: Workwell Technologies Punch Reports API
  slug: workwell-technologies-punch-reports-api
- baseURL: https://api.workwelltech.com
  baseurl_source: declared
  description: Per-user, per-pay-period timecards
  name: Workwell Technologies Timecards API
  slug: workwell-technologies-timecards-api
- baseURL: https://api.workwelltech.com
  baseurl_source: declared
  description: User records for the uAttend account
  name: Workwell Technologies Users API
  slug: workwell-technologies-users-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WorkWell Technologies API (uAttend) Punch Reports API
  slug: open-workwell-technologies-punch-reports-api
- collection_type: open
  name: WorkWell Technologies API (uAttend) Punch Reports Timecards API
  slug: open-workwell-technologies-timecards-api
- collection_type: open
  name: WorkWell Technologies API (uAttend) Punch Reports Users API
  slug: open-workwell-technologies-users-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/workwell-technologies-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/workwell-technologies-uattend-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://workwelltech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uattend.zendesk.com/hc/en-us/articles/48783008798875-uAttend-API
- group: docs
  title: ''
  type: APIReference
  url: https://uattend.zendesk.com/hc/en-us/articles/48783008798875-uAttend-API
- group: operate
  title: ''
  type: Support
  url: https://uattend.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://uattend.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uattend.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://v2.trackmytime.com/login/login.aspx
created: '2026-07-17'
description: Workwell Technologies, Inc. is a Carlsbad, California workforce management company backed by Battery Ventures, best known for its uAttend cloud-connected time and attendance platform and uPunch punch clocks. uAttend pairs biometric time clocks (fingerprint, facial recognition, RFID, voice control) with cloud software for time tracking, scheduling, overtime alerts, and optional payroll processing for small businesses. The WorkWell Technologies API exposes employee, timecard, and punch data from uAttend accounts over HTTPS with API-key authentication, supporting payroll and HRIS integrations.
image: https://uattend.com/wp-content/uploads/2019/07/uAttendLogo-01.svg
layout: provider
modified: '2026-07-21'
name: Workwell Technologies
nav: Providers
network: true
overview: 'Workwell Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Punch Reports API, Timecards API, and Users API. Tagged areas include Company, Workforce Management, Time Tracking, Attendance, and Payroll.


  Workwell Technologies'' developer surface includes documentation, API reference, support, engineering blog, and 5 more developer resources.'
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/workwell-technologies/refs/heads/main/screenshots/workwell-technologies-2026-09-02T170954.png
slug: workwell-technologies
tags:
- Company
- Workforce Management
- Time Tracking
- Attendance
- Payroll
- Human Resources
- Time Clocks
- Biometrics
- Scheduling
website: https://workwelltech.com/
---
