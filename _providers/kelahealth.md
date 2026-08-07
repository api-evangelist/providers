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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kelahealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kelahealth.com/
- group: other
  title: ''
  type: Product
  url: https://kelahealth.com/product-1
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kelahealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kelahealth.com/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://kelahealth.com/privacy-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/kelahealth-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kelahealth-llms.txt
created: '2026-07-17'
description: kelaHealth is a healthcare AI company that improves surgical outcomes through its Surgical Intelligence Service, an AI-enabled API delivering patient-specific predictive insights at critical decision points across the perioperative process. Models trained on millions of surgical procedures predict individual patient risk across nine major complication categories, identify modifiable factors, and recommend stratified interventions tailored to hospital standards. The service integrates into existing medtech and healthcare software applications using EHR, robotic, and social-determinants-of-health data to help providers improve growth, efficiency, quality, and safety. kelaHealth is HIPAA compliant and backed by Techstars. It does not publish a public developer portal, OpenAPI specification, or SDKs; its API is delivered through partner integrations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kelahealth.png
layout: provider
modified: '2026-07-19'
name: kelaHealth
nav: Providers
network: true
overview: kelaHealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Surgery, Artificial Intelligence, and Predictive Analytics.
random_paper: 26
score:
  band: emerging
  composite: 15.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 15.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kelahealth/refs/heads/main/screenshots/kelahealth-2026-07-25T223601.png
security:
- kind: domain-security
  name: Kelahealth Domain Security
  slug: kelahealth-domain-security
  summary_line: TLSv1.3
slug: kelahealth
tags:
- Company
- Healthcare
- Surgery
- Artificial Intelligence
- Predictive Analytics
- Perioperative
- Machine Learning
- MedTech
- Patient Risk
- HIPAA
website: https://kelahealth.com/
---
