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
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Partner-gated developer capability, modeled from PocketHealth's public developer-program description. Lets a RIS/PACS/VNA vendor enroll patients for PocketHealth access natively from within the vendor
  name: PocketHealth Patient Enrollment API
  slug: pockethealth-patient-enrollment-api
- description: Partner-gated developer capability, modeled from PocketHealth's public developer-program description. Captures and manages electronic patient consent for sharing diagnostic imaging and reports, so tha
  name: PocketHealth Electronic Consent API
  slug: pockethealth-consent-api
- description: Partner-gated developer capability, modeled from PocketHealth's public developer-program description. Automates secure background delivery of DICOM imaging studies and associated reports from any DICO
  name: PocketHealth Record Delivery API
  slug: pockethealth-record-delivery-api
- description: 'Partner-gated capability, modeled from PocketHealth''s public Image Exchange product description. Supports provider-to-provider imaging exchange across external hospitals and out-of-province networks, '
  name: PocketHealth Image Exchange API
  slug: pockethealth-image-exchange-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pockethealth-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pockethealth
- group: company
  title: ''
  type: Website
  url: https://www.pockethealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.pockethealth.com/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/pockethealth-plans-pricing.yml
created: '2026-07-05'
description: PocketHealth is a patient-centric medical imaging platform that lets patients access, view, store, and share their diagnostic imaging (DICOM) and reports online, and lets healthcare providers exchange imaging across institutions and networks. PocketHealth also publishes an open, RESTful developer API aimed at RIS/PACS/VNA vendors, letting them embed PocketHealth's patient enrollment, electronic consent, and background record-delivery workflows natively into their own clinical software. The developer API is partner-gated - it is free forever for RIS/PACS vendors, healthcare providers, and physicians, but the full technical reference (base URL, endpoint paths, authentication) is not published on the open web; engaged vendors are assigned a dedicated integration rep who provides testing resources and detailed documentation. As a result the APIs below are modeled from PocketHealth's public developer-program descriptions rather than a public API reference or OpenAPI definition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pockethealth.png
layout: provider
modified: '2026-07-05'
name: PocketHealth
nav: Providers
network: true
overview: 'PocketHealth publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Imaging, Healthcare, DICOM, Image Exchange, and RIS.


  PocketHealth''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Pockethealth Plans Pricing
  plan_count: 5
  slug: pockethealth-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 16.2
  delta: -0.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Pockethealth Domain Security
  slug: pockethealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pockethealth
tags:
- Medical Imaging
- Healthcare
- DICOM
- Image Exchange
- RIS
- PACS
- Interoperability
- Patient Access
- Health IT
website: https://www.pockethealth.com
---
