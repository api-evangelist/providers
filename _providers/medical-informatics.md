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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medical-informatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sickbay.com/
- group: company
  title: ''
  type: Blog
  url: https://sickbay.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://sickbay.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sickbay.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sickbay.com/terms-of-use/
created: '2026-07-17'
description: Medical Informatics Corp. (MIC) is a Houston, Texas healthcare technology company behind the FDA-cleared Sickbay platform for virtual and remote patient monitoring. Founded in 2010 by Emma Fauss and Craig Rusin, Sickbay archives, aggregates, and transforms otherwise unrecorded high-resolution physiological waveform data across disparate, vendor-neutral biomedical devices to enable anytime, anywhere remote monitoring, TeleICUs, alarm management, workflow automation, and patient-centered predictive analytics and AI across the continuum of care. The company is backed by DCVC, Intel Capital, Catalio Capital, and the Texas Medical Center. Sickbay is a clinical SaaS platform with no public developer API surface; integration is delivered through the vendor as HL7/device connectivity.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medical-informatics.png
layout: provider
modified: '2026-07-20'
name: Medical Informatics
nav: Providers
network: true
overview: 'Medical Informatics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Patient Monitoring, and Clinical Informatics.


  Medical Informatics'' developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medical-informatics/refs/heads/main/screenshots/medical-informatics-2026-08-07T172338.png
security:
- kind: domain-security
  name: Medical Informatics Domain Security
  slug: medical-informatics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medical-informatics
tags:
- Company
- Healthcare
- Medical Devices
- Patient Monitoring
- Clinical Informatics
- Predictive Analytics
- Remote Patient Monitoring
- Digital Health
website: https://sickbay.com/
---
