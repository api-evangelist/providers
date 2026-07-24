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
api_count: 1
apis:
- description: Kaiser Permanente provides a patient access FHIR API supporting the CMS Interoperability and Patient Access Final Rule. Authenticated members and their authorized third-party applications can retrieve
  name: Kaiser Permanente Patient Access FHIR API
  slug: kaiser-permanente-fhir
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaiser-permanente-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kaiserpermanente
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kaiser-permanente
- group: company
  title: ''
  type: Website
  url: https://www.kaiserpermanente.org/
- group: start
  title: ''
  type: Portal
  url: https://kp.org/fhir
- group: company
  title: ''
  type: Blog
  url: https://about.kaiserpermanente.org/news
created: '2026-05-05'
description: One of the largest nonprofit health plans in the United States integrating health insurance with healthcare delivery. Serves over 12 million members through its network of hospitals, medical offices, and health plan services. Publishes a patient access FHIR API at kp.org/fhir in compliance with the CMS Interoperability and Patient Access Final Rule.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kaiser-permanente.png
layout: provider
modified: '2026-05-16'
name: Kaiser Permanente
nav: Providers
network: true
overview: 'Kaiser Permanente publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Insurance, Health Insurance, Hospitals, and FHIR.


  Kaiser Permanente''s developer surface includes developer portal, engineering blog, and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 11.2
  delta: 0.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaiser-permanente/refs/heads/main/screenshots/kaiser-permanente-2026-06-20T183902.png
security:
- kind: domain-security
  name: Kaiser Permanente Domain Security
  slug: kaiser-permanente-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kaiser-permanente
tags:
- Healthcare
- Insurance
- Health Insurance
- Hospitals
- FHIR
- Interoperability
website: https://www.kaiserpermanente.org/
---
