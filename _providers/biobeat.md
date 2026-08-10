---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: 'Modeled resource for enrolling and managing monitored patients on the Biobeat patient management platform - create, list, and update patient records, assign devices, and set per-patient alarm limits. '
  name: Biobeat Patients API
  slug: biobeat-patients-api
- description: Modeled resource for provisioning and managing Biobeat wearable devices - the disposable chest-monitor and the reusable wrist-monitor - including registration, assignment to a patient, and status/batt
  name: Biobeat Devices API
  slug: biobeat-devices-api
- description: Modeled resource for retrieving continuous vital-sign readings collected by Biobeat wearables - cuffless blood pressure, pulse rate, respiratory rate, blood oxygen saturation, temperature, stroke volu
  name: Biobeat Vital Signs Measurements API
  slug: biobeat-measurements-api
- description: Modeled resource for the alerts Biobeat raises when a patient's readings cross configured alarm limits or its health-AI flags early deterioration. Covers listing active alerts and per-patient threshol
  name: Biobeat Alerts API
  slug: biobeat-alerts-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biobeat-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://il.linkedin.com/company/biobeat-ltd.
- group: company
  title: ''
  type: Website
  url: https://www.bio-beat.com/
- group: start
  title: ''
  type: Portal
  url: https://remote-monitoring.us.bio-beat.cloud/
- group: commercial
  title: ''
  type: Plans
  url: plans/biobeat-plans-pricing.yml
created: '2026-07-05'
description: Biobeat Technologies is an Israeli med-tech company whose remote patient monitoring (RPM) health-AI platform pairs a disposable short-term chest-monitor and a reusable long-term wrist-monitor - both using a photoplethysmography (PPG) sensor - to continuously track up to 13 vital signs, including FDA-cleared cuffless blood pressure, pulse rate, respiratory rate, blood oxygen saturation, temperature, stroke volume, cardiac output, and one-lead ECG (chest-monitor). Readings stream to Biobeat's HIPAA- and GDPR-compliant, cloud-based patient management platform, where clinicians view real-time data, trends, and configurable alerts. Biobeat offers programmatic data access and EMR/EHR integration as a paid add-on for hospitals, health systems, and research partners; there is no publicly documented self-serve developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/biobeat.png
layout: provider
modified: '2026-07-05'
name: Biobeat
nav: Providers
network: true
overview: 'Biobeat publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Remote Patient Monitoring, RPM, Wearables, Vital Signs, and Cuffless Blood Pressure.


  Biobeat''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: Biobeat Plans Pricing
  plan_count: 2
  slug: biobeat-plans-pricing
random_paper: 30
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biobeat/refs/heads/main/screenshots/biobeat-2026-07-25T203024.png
security:
- kind: domain-security
  name: Biobeat Domain Security
  slug: biobeat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biobeat
tags:
- Remote Patient Monitoring
- RPM
- Wearables
- Vital Signs
- Cuffless Blood Pressure
- Digital Health
- Medical Devices
- PPG
- Partner Gated
website: https://www.bio-beat.com/
---
