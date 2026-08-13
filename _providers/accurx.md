---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.7
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accurx-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/accurx-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accurx-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/accurx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accurx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accurx.com/
- group: auth
  title: ''
  type: Security
  url: https://www.accurx.com/security
- group: operate
  title: ''
  type: Support
  url: https://support.accurx.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accurx.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accurx.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accurx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accurx.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accurx.com/terms-and-conditions
- group: operate
  title: ''
  type: Contact
  url: https://www.accurx.com/contact-us
created: '2026-07-24'
description: 'Accurx is a United Kingdom clinical communication and workflow company, founded in 2016 and headquartered in London, whose software is used across NHS primary care, secondary care, and community and mental health services to message patients, run patient triage, batch-message cohorts, book and remind appointments, and (via its Scribe product) draft clinical notes with AI. Accurx integrates around the NHS as an assured IM1 live supplier, using NHS Digital''s interoperability standards for primary care and connecting bi-directionally to the GP clinical-system duopoly (EMIS Health, TPP SystmOne) and Vision, plus NHS national services including the Personal Demographics Service (PDS), NHS Single Sign-On, NHS Login, and the NHS App. Accurx is a consumer and integrator of NHS FHIR and IM1 interfaces rather than a publisher of its own public developer API: as of this review it operates no public developer portal, no self-serve REST/FHIR API, and no downloadable OpenAPI or FHIR CapabilityStatement.
  Third-party and trust integrations are arranged through its partnerships and integration teams under partner agreement.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Accurx
nav: Providers
network: true
overview: 'Accurx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United Kingdom, Clinical Communication, NHS, and National Health System.


  Accurx''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 16.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accurx/refs/heads/main/screenshots/accurx-2026-07-25T181445.png
security:
- kind: domain-security
  name: Accurx Domain Security
  slug: accurx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Accurx Vulnerability Disclosure
  slug: accurx-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: accurx
tags:
- Healthcare
- United Kingdom
- Clinical Communication
- NHS
- National Health System
- Interoperability
- FHIR
- HL7
- Primary Care
- Clinical AI
- Patient Engagement
- Telehealth
website: https://www.accurx.com/
---
