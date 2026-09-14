---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Vivalink Agentic Access
  operation_count: 16
  slug: vivalink-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.vivalink.com
  baseurl_source: declared
  description: VivaLNK wearable biosensors and their assignment to subjects.
  name: VivaLNK Devices API
  slug: vivalink-devices-api
- baseURL: https://api.vivalink.com
  baseurl_source: declared
  description: HL7 FHIR R4 resources for EHR/CTMS interoperability.
  name: VivaLNK FHIR API
  slug: vivalink-fhir-api
- baseURL: https://api.vivalink.com
  baseurl_source: declared
  description: Subjects (patients / study participants) enrolled for monitoring.
  name: VivaLNK Subjects API
  slug: vivalink-subjects-api
- baseURL: https://api.vivalink.com
  baseurl_source: declared
  description: Biometric measurements captured from wearables.
  name: VivaLNK Vital Signs API
  slug: vivalink-vital-signs-api
- baseURL: https://api.vivalink.com
  baseurl_source: declared
  description: Subscriptions for pushed biometric data and alert events.
  name: VivaLNK Webhooks API
  slug: vivalink-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VivaLNK Biometrics Data Platform API (Modeled) Devices API
  slug: open-vivalink-devices-api
- collection_type: open
  name: VivaLNK Biometrics Data Platform API (Modeled) Devices FHIR API
  slug: open-vivalink-fhir-api
- collection_type: open
  name: VivaLNK Biometrics Data Platform API (Modeled) Devices Subjects API
  slug: open-vivalink-subjects-api
- collection_type: open
  name: VivaLNK Biometrics Data Platform API (Modeled) Devices Vital Signs API
  slug: open-vivalink-vital-signs-api
- collection_type: open
  name: VivaLNK Biometrics Data Platform API (Modeled) Devices Webhooks API
  slug: open-vivalink-webhooks-api
- collection_type: open
  name: VivaLNK Biometrics Data Platform API (Modeled)
  slug: open-vivalink
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vivalink-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vivalink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vivalink-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vivalink-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VivaLnk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vivalnk-inc-
- group: company
  title: ''
  type: Website
  url: https://www.vivalink.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.vivalink.com/vivalink-sdk
- group: start
  title: ''
  type: SignUp
  url: https://www.vivalink.com/contact
- group: commercial
  title: ''
  type: Plans
  url: plans/vivalink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vivalink-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vivalink-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.vivalink.com/blog
created: '2026-07-05'
description: VivaLNK (Vivalink) is a connected-health company providing medical-grade wearable biosensors and a Biometrics Data Platform for remote patient monitoring (RPM), hospital-at-home, and decentralized clinical trials. Its wearable sensors capture ECG, heart rate, heart rate variability, respiratory rate, RR interval, body/axillary temperature, SpO2, blood pressure, and three-axis accelerometer data. Mobile edge clients read the sensors over Bluetooth Low Energy (BLE) and deliver data to the cloud over RESTful HTTPS services (Amazon API Gateway plus Amazon Kinesis for near-real-time ingestion). The platform exposes machine-to-machine (M2M) cloud web-service APIs, webhook push, FHIR-based integration, and bulk data-file downloads for EHR, CTMS, and clinical-application integration. The developer surface is delivered through VivaLNK's SDK and Developer Program and is partner-gated; the full API reference is provided under license rather than published openly, so the endpoints described
  here are modeled from VivaLNK's documented platform capabilities.
finops:
- name: Vivalink Finops
  service_category: Connected Health and Remote Patient Monitoring
  slug: vivalink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vivalink.png
layout: provider
modified: '2026-07-05'
name: VivaLNK
nav: Providers
network: true
overview: 'VivaLNK publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Devices API, FHIR API, Subjects API, and 2 more. Tagged areas include Connected Health, Remote Patient Monitoring, RPM, Wearables, and Biosensors.


  VivaLNK''s developer surface includes authentication, documentation, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Vivalink Plans Pricing
  plan_count: 3
  slug: vivalink-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Vivalink Rate Limits
  slug: vivalink-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/vivalink/refs/heads/main/screenshots/vivalink-2026-09-02T170130.png
security:
- kind: authentication
  name: Vivalink Authentication
  slug: vivalink-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vivalink Domain Security
  slug: vivalink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vivalink
tags:
- Connected Health
- Remote Patient Monitoring
- RPM
- Wearables
- Biosensors
- Biometrics
- ECG
- Vital Signs
- Digital Health
- IoT
- Clinical Trials
website: https://www.vivalink.com
---
