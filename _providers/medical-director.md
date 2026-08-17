---
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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: FHIR-native integration gateway from Telstra Health that provides a single, standardized interface for approved technology partners to exchange data with MedicalDirector Helix cloud general-practice p
  name: Telstra Health Smart API+
  slug: telstra-health-smart-api-plus
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medical-director-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medical-director-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medical-director-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.medicaldirector.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.telstrahealth.com/products/smart-api/
- group: other
  title: ''
  type: Marketplace
  url: https://www.medicaldirector.com/marketplace
- group: operate
  title: ''
  type: StatusPage
  url: https://www.medicaldirector.com/status
- group: company
  title: ''
  type: Blog
  url: https://www.medicaldirector.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.medicaldirector.com/support
- group: auth
  title: ''
  type: Security
  url: https://www.medicaldirector.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medicaldirector.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medicaldirector.com/documents/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.telstrahealth.com/contact/
created: '2026-07-24'
description: 'MedicalDirector is an Australian clinical and practice-management software provider, owned by Telstra Health, that has served general practices, specialists, and day hospitals across Australia for more than 25 years. Its product family includes Helix (a cloud-based combined clinical and practice-management system), Clinical and Pracsoft (on-premise clinical and practice-management software), Bluechip (specialist practice management), and Day Surgery. Alongside Best Practice, MedicalDirector is one half of the dominant Australian GP-software duopoly. Its programmatic surface is delivered through Telstra Health Smart API+, a FHIR-native integration gateway that lets approved technology partners exchange data with MedicalDirector Helix (and, on a case-by-case basis, MedicalDirector Clinical) without bespoke, platform-specific integrations. Smart API+ is a gated, partner-onboarded API: it is publicly announced and described but has no self-serve public developer portal, and no
  FHIR CapabilityStatement or OpenAPI is published anonymously. Access is granted through a partner agreement, and the underlying FHIR version and SMART-on-FHIR auth specifics are not disclosed on public pages.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: MedicalDirector
nav: Providers
network: true
overview: 'MedicalDirector publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Australia, EHR, EMR, and FHIR.


  MedicalDirector''s developer surface includes documentation, engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 134
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 21.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medical-director/refs/heads/main/screenshots/medical-director-2026-08-07T172351.png
security:
- kind: domain-security
  name: Medical Director Domain Security
  slug: medical-director-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medical-director
tags:
- Healthcare
- Australia
- EHR
- EMR
- FHIR
- Interoperability
- Practice Management
- Primary Care
- Clinical Software
- Digital Health
website: https://www.medicaldirector.com/
---
