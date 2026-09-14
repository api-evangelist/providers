---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greater-good-health-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/greater-good-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/greater-good-health-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://greatergoodhealth.com/
- group: company
  title: ''
  type: About
  url: https://greatergoodhealth.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://greatergoodhealth.com/about-us/news/
- group: operate
  title: ''
  type: Support
  url: https://greatergoodhealth.com/patients/get-care/
- group: operate
  title: ''
  type: FAQ
  url: https://greatergoodhealth.com/patients/resources/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greatergoodhealth.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greatergoodhealth.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://greatergoodhealth.com/talent/join-our-team/job-openings/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greater-good-health/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Greater-Good-Health
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/GreaterGoodHealth/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/greatergoodhealth/
coverage:
  checked: '2026-08-22'
  detail: Greater Good Health is a nurse-practitioner-led senior primary care clinic operator, not a software vendor - its WordPress marketing site has no /developers, /api or docs section at all, and every contract-discovery probe (openapi.json, swagger.json, api-docs, llms.txt) resolves to the same 64,289-byte "Content Not Found" catch-all page.
  evidence:
  - status: 200
    url: https://greatergoodhealth.com/openapi.json
  - status: 200
    url: https://greatergoodhealth.com/developers
  - status: 403
    url: https://greatergoodhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/greatergoodhealth
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Greater Good Health is a Manhattan Beach, California value-based senior healthcare organization founded in 2021 that delivers preventive, whole-person primary care to older adults through a nurse-practitioner-led model. It operates its own senior primary care clinics and an integrated clinical services platform — risk adjustment and annual wellness visits, transitions of care, high-risk and chronic condition management, and behavioral health — delivered on behalf of health plans, medical groups, ACOs and other risk-bearing organizations. Alongside care delivery it runs a nurse practitioner community, the Greater Good Institute education portal, and clinical technology and analytics tooling for its employed NPs. It is a care delivery organization rather than a software vendor: it publishes no public developer program, API, SDK or machine-readable API contract of any kind.'
image: https://greatergoodhealth.com/wp-content/uploads/2023/06/cropped-ggh-logo-270x270.png
layout: provider
modified: '2026-08-22'
name: Greater Good Health
nav: Providers
network: true
overview: 'Greater Good Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Senior Care, and Value-Based Care.


  Greater Good Health''s developer surface includes engineering blog, support, FAQ, YouTube channel, and 11 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/greater-good-health/refs/heads/main/screenshots/greater-good-health-2026-09-02T145627.png
security:
- kind: domain-security
  name: Greater Good Health Domain Security
  slug: greater-good-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: greater-good-health
tags:
- Company
- Healthcare
- Primary Care
- Senior Care
- Value-Based Care
- Medicare
- Nurse Practitioners
- Clinics
- Population Health
- Health Services
website: https://greatergoodhealth.com/
---
