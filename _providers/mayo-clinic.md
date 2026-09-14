---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: Review and try the existing APIs in the Mayo Clinic Apigee API catalog portal. Provides programmatic access to healthcare data and clinical services.
  name: Mayo Clinic API
  slug: mayo-clinic-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mayo-clinic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mayo-clinic
- group: start
  title: ''
  type: Portal
  url: https://apiportal.mcc.mayo.edu/
- group: company
  title: ''
  type: Website
  url: https://www.mayoclinic.org/
created: '2025-02-12'
description: Mayo Clinic provides a developer API portal with access to clinical and healthcare APIs hosted on an Apigee API catalog. Developers can review, test, and integrate with available APIs for healthcare data and services.
finops:
- name: Mayo Clinic Finops
  service_category: API
  slug: mayo-clinic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mayo-clinic.png
layout: provider
modified: '2026-04-28'
name: Mayo Clinic
nav: Providers
network: true
overview: 'Mayo Clinic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Data, Healthcare, Hospital, and Medical.


  Mayo Clinic''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: Mayo Clinic Plans Pricing
  plan_count: 3
  slug: mayo-clinic-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Mayo Clinic Rate Limits
  slug: mayo-clinic-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/screenshots/mayo-clinic-2026-06-20T185105.png
security:
- kind: domain-security
  name: Mayo Clinic Domain Security
  slug: mayo-clinic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mayo-clinic
tags:
- Clinical Data
- Healthcare
- Hospital
- Medical
website: https://www.mayoclinic.org/
---
