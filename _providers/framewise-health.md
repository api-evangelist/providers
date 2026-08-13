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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/framewise-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://framewisehealth.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://framewisehealth.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://framewisehealth.com/terms
- group: operate
  title: ''
  type: Support
  url: mailto:contact@framewisehealth.com
- group: auth
  title: ''
  type: Compliance
  url: https://framewisehealth.com
- group: design
  title: ''
  type: Conformance
  url: conformance/framewise-health-conformance.yml
created: '2026-07-17'
description: Framewise Health is an AI-native patient engagement platform (Y Combinator, Spring 2026) that converts a patient's medical records into personalized, clinically-reviewed educational videos. The platform pulls patient data from electronic health records over any FHIR R4 endpoint, generates discharge and treatment-adherence education tailored to the individual using institutional protocols and drug-information databases, and delivers it by SMS in 75+ languages with no app and no login. It then tracks patient comprehension in real time, giving care teams engagement data to flag which patients need follow-up. Framewise integrates with Epic, Oracle Health (Cerner), Athenahealth, ModMed, eClinicalWorks, and NextGen, and is HIPAA and SOC 2 compliant with an AWS BAA and end-to-end encryption. It targets hospitals, pharmaceutical companies, medical device manufacturers, and private clinics seeking to improve patient outcomes and medication adherence.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/framewise-health.png
layout: provider
modified: '2026-07-19'
name: Framewise Health
nav: Providers
network: true
overview: 'Framewise Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Engagement, Patient Education, and FHIR.


  Framewise Health''s developer surface includes support and 6 more developer resources.'
random_paper: 78
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/framewise-health/refs/heads/main/screenshots/framewise-health-2026-07-25T215113.png
security:
- kind: domain-security
  name: Framewise Health Domain Security
  slug: framewise-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: framewise-health
tags:
- Company
- Healthcare
- Patient Engagement
- Patient Education
- FHIR
- EHR Integration
- Health Literacy
- Artificial Intelligence
- HIPAA
- SOC 2
website: https://framewisehealth.com
---
