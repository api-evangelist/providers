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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klara-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klara-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.modmed.com/what-we-do/patient-engagement/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klara-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.klara.com/
- group: start
  title: ''
  type: Login
  url: https://doctor.klara.com/
- group: operate
  title: ''
  type: Support
  url: https://support.klara.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klara.com/
- group: company
  title: ''
  type: Blog
  url: https://www.modmed.com/resources/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.modmed.com/schedule-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modmed.com/klara-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modmed.com/klara-privacy/
created: '2026-07-24'
description: Klara is a US healthcare patient-engagement and communication platform, now part of Modernizing Medicine (ModMed), that gives medical practices two-way secure messaging, patient texting, appointment reminders and scheduling, intake and forms, telemedicine, and automated workflow tools to reduce phone volume and staff workload. Klara markets integration with 50+ EHR and practice-management systems, but it does not publish its own self-serve public developer API, FHIR CapabilityStatement, or downloadable OpenAPI. Its parent, ModMed, operates a partner-gated developer program at portal.api.modmed.com covering an ONC-certified HL7 FHIR R4 API with SMART-on-FHIR (built for the 21st Century Cures Act, US Core, OAuth2, bulk NDJSON export) plus a proprietary FHIR API for the EMA and gGastro EHR/PM platforms and a Synapsys App Marketplace. That certified API surface belongs to ModMed's EHR products, not to the Klara messaging product itself. Home market is the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Klara
nav: Providers
network: true
overview: 'Klara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Patient Engagement, Patient Communication, and Secure Messaging.


  Klara''s developer surface includes support, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 21.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klara/refs/heads/main/screenshots/klara-2026-07-25T223943.png
security:
- kind: domain-security
  name: Klara Domain Security
  slug: klara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klara
tags:
- Healthcare
- United States
- Patient Engagement
- Patient Communication
- Secure Messaging
- Telehealth
- Scheduling
- EHR Integration
website: https://www.klara.com/
---
