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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Smart hospital beds, ICU beds, med-surg beds, and patient support systems including Centrella, Progressa, and VersaCare platforms. Integrates with hospital IT systems for fall risk monitoring, pressur
  name: Hill-Rom Smart Beds and Patient Support
  slug: hill-rom-smart-beds
- description: Welch Allyn vital signs monitors, otoscopes, ophthalmoscopes, ECG devices, and diagnostic instruments used across primary care, hospitals, and clinics. Connex Spot and Connex Vital Signs Monitors conn
  name: Welch Allyn Vital Signs and Diagnostic Devices
  slug: welch-allyn-vital-signs
- description: Bardy Diagnostics CAM (Carnation Ambulatory Monitor) patch-based ambulatory cardiac monitoring solution for arrhythmia detection, acquired by Hill-Rom in 2021 prior to Baxter's acquisition of Hill-Rom
  name: Bardy Diagnostics Cardiac Monitoring
  slug: bardy-diagnostics-cardiac
- description: 'Hillrom connected care platforms including Voalte clinical communication, nurse call systems, patient engagement, real-time location services, and clinical workflow tools that integrate with hospital '
  name: Hillrom Connected Care and Clinical Workflow
  slug: hillrom-connected-care
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hill-rom-holdings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hillrom.com
- group: other
  title: ''
  type: Parent
  url: https://www.baxter.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hillrom
created: '2026-05-23'
description: 'Hill-Rom Holdings was a global medical technology company best known for its hospital beds, patient support systems, Welch Allyn vital signs monitors, and Bardy Diagnostics cardiac monitoring devices. Hill-Rom was acquired by Baxter International (NYSE: BAX) in December 2021 for $12.4 billion and now operates as Baxter''s Hillrom and Front Line Care segment, continuing to deliver connected care, smart beds, vital signs monitoring, and clinical workflow solutions to hospitals and health systems worldwide.'
features:
- description: 'Hill-Rom Holdings was acquired by Baxter International (NYSE: BAX) in December 2021 in a $12.4 billion all-cash transaction and now operates as Baxter''s Hillrom and Front Line Care segment.'
  name: Acquired by Baxter International
- description: Connected ICU, med-surg, and birthing beds with integrated patient monitoring, fall prevention, pressure injury prevention, and EMR connectivity.
  name: Smart Hospital Beds
- description: Vital signs monitors, physical exam instruments, ECG devices, and connected diagnostic equipment used across hospitals, clinics, and primary care.
  name: Welch Allyn Diagnostic Portfolio
- description: Bardy Diagnostics CAM patch-based ambulatory cardiac monitoring with cloud analytics for arrhythmia detection.
  name: Cardiac Diagnostics
- description: Voalte clinical communication, nurse call, patient engagement, and clinical workflow platforms integrated with hospital EMR and IT systems.
  name: Connected Care and Workflow
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hill-rom-holdings.png
integrations:
- description: Operates as Baxter's Hillrom and Front Line Care segment following the December 2021 acquisition.
  name: Baxter International (Parent)
- description: Welch Allyn Connex devices, Hillrom smart beds, and Voalte communication platforms integrate with Epic, Cerner, Meditech, and other hospital EMRs.
  name: Hospital EMR Systems
- description: Hillrom and Welch Allyn devices participate in Baxter's broader connected device strategy alongside the DeviceBridge platform.
  name: Baxter DeviceBridge
layout: provider
modified: '2026-05-23'
name: Hill-Rom Holdings
nav: Providers
network: true
overview: Hill-Rom Holdings publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Devices, Hospital Beds, Patient Monitoring, and Vital Signs.
random_paper: 25
score:
  band: minimal
  composite: 6.6
  delta: -2.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hill-rom-holdings/refs/heads/main/screenshots/hill-rom-holdings-2026-06-20T182736.png
security:
- kind: domain-security
  name: Hill Rom Holdings Domain Security
  slug: hill-rom-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hill-rom-holdings
tags:
- Healthcare
- Medical Devices
- Hospital Beds
- Patient Monitoring
- Vital Signs
- Connected Care
- Cardiac Diagnostics
use_cases:
- description: Smart beds for ICU, med-surg, and progressive care environments with integrated monitoring and mobility analytics.
  name: Acute Care Hospital Beds
- description: Automated capture and EMR posting of vital signs from Welch Allyn Connex devices at the bedside.
  name: Vital Signs Documentation
- description: Long-duration patch-based ECG monitoring for arrhythmia diagnosis using the Bardy CAM device.
  name: Ambulatory Cardiac Monitoring
- description: Secure mobile messaging, alarm routing, and care team coordination via Voalte across hospital care settings.
  name: Clinical Communication
website: https://www.hillrom.com
---
