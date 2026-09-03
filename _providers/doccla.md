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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doccla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doccla.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/doccla-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/doccla-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://www.doccla.com/contact
created: '2026-07-17'
description: Doccla is a UK-founded virtual care platform delivering remote patient monitoring and virtual wards across Europe. It combines pre-configured, Bluetooth-connected medical devices, a patient app, and a clinician dashboard to monitor patients at home, reducing hospital admissions and freeing bed capacity for health systems. The platform integrates bidirectionally with electronic health record (EHR) systems, including Oracle Cerner for the Northwest London Virtual Hospital, and is deployed with NHS trusts and European providers. Doccla holds ISO 27001 and ISO 13485 certifications, UKCA and CE medical-device marks, is GDPR compliant, and is registered with the UK Care Quality Commission (CQC). No public developer API or portal is published at this time; integration is delivered via managed EHR and medical-device connections.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doccla.png
layout: provider
modified: '2026-07-18'
name: Doccla
nav: Providers
network: true
overview: 'Doccla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Remote Patient Monitoring, Virtual Wards, and Digital Health.


  Doccla''s developer surface includes support and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doccla/refs/heads/main/screenshots/doccla-2026-07-25T212159.png
security:
- kind: domain-security
  name: Doccla Domain Security
  slug: doccla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Doccla Trust Center
  slug: doccla-trust-center
  summary_line: ISO 27001, ISO 13485, UKCA, CE, GDPR, CQC registered
slug: doccla
tags:
- Company
- Healthcare
- Remote Patient Monitoring
- Virtual Wards
- Digital Health
- Telehealth
- Medical Devices
- EHR Integration
website: https://www.doccla.com
---
