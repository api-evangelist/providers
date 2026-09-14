---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://patientping.com'', ''status'': 301, ''note'': ''declared website redirects to https://bamboohealth.com/ — a different registrable domain (patientping.com -> bamboohealth.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patientping-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patientping.com
- group: start
  title: ''
  type: Login
  url: https://my.patientping.com/
created: '2026-07-17'
description: PatientPing is a real-time care-coordination network that delivers e-notifications ("Pings") and ADT-based admission, discharge, and transfer alerts across hospitals, post-acute facilities, health plans, pharmacies, and community providers. Its Route solution helps hospitals meet the CMS Interoperability and Patient Access Rule e-notifications Condition of Participation. PatientPing was acquired by Appriss Health in 2021 and rebranded as Bamboo Health; patientping.com now redirects to bamboohealth.com. No public developer portal or API documentation is published — clinical integration is handled privately via HL7/ADT data feeds embedded in provider workflow.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patientping.png
layout: provider
modified: '2026-07-20'
name: PatientPing
nav: Providers
network: true
overview: PatientPing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bio Healthcare, Care Coordination, Health IT, and Interoperability.
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/patientping/refs/heads/main/screenshots/patientping-2026-08-07T191554.png
security:
- kind: domain-security
  name: Patientping Domain Security
  slug: patientping-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: patientping
tags:
- Company
- Bio Healthcare
- Care Coordination
- Health IT
- Interoperability
- Notification
- HL7 ADT
website: https://patientping.com
---
