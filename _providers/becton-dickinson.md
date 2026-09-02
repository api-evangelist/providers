---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'The BD Incada Connected Care Platform is a scalable, AI-enabled, cloud-based platform launched in October 2025 that unifies BD device data from infusion pumps, patient monitors, and pharmacy robotics '
  name: BD Incada Connected Care Platform
  slug: bd-incada-platform
- description: BD Pyxis is a medication management and dispensing system used in hospitals to control medication access, reduce errors, and streamline pharmacy workflows. Pyxis connects to hospital information syste
  name: BD Pyxis Medication Management System
  slug: pyxis
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/becton-dickinson-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/becton-dickinson-and-company
- group: company
  title: ''
  type: Website
  url: https://www.bd.com/
- group: auth
  title: ''
  type: Security
  url: https://www.bd.com/en-us/company/cybersecurity
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bd.com/en-us/company/legal-notices-and-privacy/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bd.com/en-us/company/legal-notices-and-privacy
created: '2026-03-21'
description: Becton Dickinson (BD) is a global medical technology company that develops, manufactures, and sells medical devices, instrument systems, and reagents. In October 2025, BD launched the BD Incada Connected Care Platform, an AI-enabled, cloud-based platform built on AWS that unifies data from nearly 3 million connected BD devices including infusion pumps, patient monitors, and pharmacy robotics. BD also produces the Pyxis medication management system and integrates with EMRs via HL7 FHIR standards for clinical data exchange.
features:
- description: AI-enabled cloud platform launched in 2025 that unifies data from nearly 3 million BD connected medical devices on AWS infrastructure.
  name: BD Incada Connected Care Platform
- description: Natural language search and AI-powered insights for medication inventory, device utilization, and clinical operational analytics.
  name: AI-Powered Analytics
- description: Healthcare interoperability using HL7 and FHIR standards for EMR integration with Mirth, Cloverleaf, and Rhapsody interface engines.
  name: HL7 FHIR Integration
- description: Pyxis automated dispensing system with connected pharmacy workflow, medication safety, and inventory management.
  name: Medication Management
- description: Connectivity for infusion pumps, vital signs monitors, and pharmacy robotics to hospital information systems.
  name: Device Connectivity
- description: Customizable dashboards and analytics enabling frontline clinical teams to act on device and medication data insights.
  name: Enterprise Analytics
finops:
- name: Becton Dickinson Finops
  service_category: Healthcare / Medical Device Connectivity
  slug: becton-dickinson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/becton-dickinson.png
integrations:
- description: Integration with Epic electronic medical records for medication order and administration workflow connectivity.
  name: Epic EMR
- description: Integration with Cerner/Oracle Health for clinical data exchange and medication management.
  name: Cerner EMR
- description: Open-source HL7 interface engine used with BD systems for healthcare data exchange.
  name: Mirth Connect
- description: Amazon Web Services infrastructure powering the BD Incada Connected Care Platform cloud analytics.
  name: AWS
- description: Healthcare integration engine used with BD systems for interfacing with hospital information systems.
  name: Cloverleaf
layout: provider
modified: '2026-04-19'
name: Becton Dickinson
nav: Providers
network: true
overview: Becton Dickinson publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Devices, Infusion Therapy, Medication Management, and Connected Health.
plans:
- name: Becton Dickinson Plans Pricing
  plan_count: 1
  slug: becton-dickinson-plans-pricing
press:
- date: '2026-05-25'
  title: Press releases
  url: https://news.bd.com/press-releases?l=100&o=100
- date: '2026-05-25'
  title: BD Launches Next Generation Hemodynamic Monitoring ...
  url: https://investors.bd.com/news-events/press-releases/detail/881/bd-launches-next-generation-hemodynamic-monitoring-solution-providing-clinicians-with-ai-driven-clinical-decision-support
- date: '2026-05-25'
  title: New Data Reveals BD's Artificial Intelligence Software Highly ...
  url: https://investors.bd.com/news-events/press-releases/detail/851/new-data-reveals-bds-artificial-intelligence-software-highly-effective-in-detecting-indicators-of-controlled-substance-diversion
- date: '2026-05-25'
  title: Becton Dickinson Unveils Artificial Intelligence Powered ...
  url: https://www.2minutemedicine.com/becton-dickinson-unveils-artificial-intelligence-powered-monitor-for-surgery/
- date: '2026-05-25'
  title: BD Helps Scientists Advance Immunology and Cancer ...
  url: https://www.prnewswire.com/news-releases/bd-helps-scientists-advance-immunology-and-cancer-research-with-ai-powered-insights-and-automation-302668624.html
random_paper: 4
rate_limits:
- limit_count: 2
  name: Becton Dickinson Rate Limits
  slug: becton-dickinson-rate-limits
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/becton-dickinson/refs/heads/main/screenshots/becton-dickinson-2026-06-20T173125.png
security:
- kind: domain-security
  name: Becton Dickinson Domain Security
  slug: becton-dickinson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: becton-dickinson
tags:
- Healthcare
- Medical Devices
- Infusion Therapy
- Medication Management
- Connected Health
- Diagnostics
- Fortune 500
use_cases:
- description: Reduce medication errors by connecting BD dispensing systems with EMR medication orders and administration verification.
  name: Medication Safety
- description: Enable hospital IT to integrate BD device data into clinical workflows using HL7 FHIR standards.
  name: Clinical Data Interoperability
- description: Gain enterprise-wide visibility into medication inventory, dispensing patterns, and waste reduction opportunities.
  name: Pharmacy Analytics
- description: Unify data from infusion pumps, patient monitors, and pharmacy systems to support coordinated clinical care decisions.
  name: Connected Care Workflows
website: https://www.bd.com/
---
