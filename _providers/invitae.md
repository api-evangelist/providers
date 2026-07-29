---
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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/invitae-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/invitae-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.invitae.com/
- group: start
  title: ''
  type: Portal
  url: https://www.invitae.com/us/providers
- group: company
  title: ''
  type: Blog
  url: https://blog.invitae.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/invitae
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.invitae.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.invitae.com/terms
created: '2026-07-24'
description: 'Invitae (now Labcorp Invitae, following Labcorp''s 2024 acquisition of select Invitae assets) is a United States medical genetics and healthcare-technology company that provides clinical-grade hereditary and somatic genetic testing across oncology, women''s health, cardiology, neurology, pediatrics, and rare disease. It offers providers an online ordering portal, licensed genetic counseling, and the Gia digital assistant, and returns results into clinician workflows. Invitae''s integration posture is enterprise and partner-gated rather than a self-serve public developer API: genetic test orders and results reach the electronic health record through Epic-certified interfaces and Epic Aura (Orders and Results Anywhere Network) and traditional HL7 order/result feeds delivered by a dedicated EHR integration team. As of this review no public developer portal, FHIR CapabilityStatement, SMART-on-FHIR configuration, or downloadable OpenAPI is published; programmatic access is arranged
  through a partnership/integration engagement in its United States home market.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Invitae
nav: Providers
network: true
overview: 'Invitae is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Genomics, Genetic Testing, and Precision Medicine.


  Invitae''s developer surface includes developer portal, engineering blog, and 6 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 13.5
  delta: -2.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/invitae/refs/heads/main/screenshots/invitae-2026-07-25T222754.png
security:
- kind: domain-security
  name: Invitae Domain Security
  slug: invitae-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: invitae
tags:
- Healthcare
- United States
- Genomics
- Genetic Testing
- Precision Medicine
- Life Sciences
- EHR
- Interoperability
- HL7
- Diagnostics
website: https://www.invitae.com/
---
