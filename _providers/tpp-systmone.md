---
access_model:
  confidence: high
  label: NHS partner conformance (IM1 / GP Connect / TPP Integration Request)
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - integration-request
  - im1-pairing
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: TPP's local client-integration interface allowing an approved third-party application to interact with a running SystmOne client. Communication is performed with XML documents (validated against publi
  name: SystmOne Client Integration API
  slug: systmone-client-integration-api
- description: TPP's Patient Facing Services API, enabling patient-facing applications to interact with SystmOne for services such as appointment booking, prescription requests, and record access. Distributed as a d
  name: SystmOne Patient Facing Services (PFS) API
  slug: systmone-pfs-api
- description: TPP's Generic HTML API for embedding and launching third-party web content in context within the SystmOne client. Distributed as a downloadable specification package. Access requires TPP's Integration
  name: SystmOne Generic HTML API
  slug: systmone-generic-html-api
- description: TPP's Telephony API for integrating telephony systems with SystmOne, supporting computer-telephony workflows such as inbound-call patient matching. Distributed as a downloadable specification package.
  name: SystmOne Telephony API
  slug: systmone-telephony-api
- description: The NHS England national integration route by which approved third-party applications connect directly to GP clinical systems including TPP SystmOne. IM1 comprises the Transaction API (real-time read/
  name: Interface Mechanism 1 (IM1)
  slug: im1-interface-mechanism-1
- description: GP Connect is NHS England's national FHIR-based interoperability programme. TPP SystmOne clinical records are exposed through GP Connect's FHIR API for authorised record viewing, appointment managemen
  name: GP Connect (FHIR)
  slug: gp-connect
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tpp-systmone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tpp-uk.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tpp-uk.com/resources/integration-request/
- group: docs
  title: ''
  type: Documentation
  url: https://tpp-uk.com/resources/integration-request/
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.nhs.uk/services/digital-services-for-integrated-care/im1-pairing-integration
- group: company
  title: ''
  type: Blog
  url: https://tpp-uk.com/news-insights/
- group: operate
  title: ''
  type: Support
  url: https://tpp-uk.com/contact_us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tpp-uk.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://tpp-uk.com/cyber-essentials-plus/
- group: auth
  title: ''
  type: Compliance
  url: https://tpp-uk.com/iso-27001/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tpp-systmone-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tpp-systmone-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tpp-systmone-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tpp-systmone-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tpp-systmone-llms.txt
created: '2026-07-24'
description: TPP (The Phoenix Partnership) is a UK healthcare software company founded in 1997 and headquartered in Leeds, England. Its flagship clinical system, SystmOne, is one of the two dominant GP electronic health record platforms in England (alongside EMIS Web) and holds more than 61 million patient records shared across the NHS, serving over 300,000 users and 7,800+ organisations spanning general practice, hospitals, urgent care, mental health, community, and social care. TPP does not operate a public self-serve developer portal; integration is a gated, partner-conformance process. Third parties integrate with SystmOne through NHS England's Interface Mechanism 1 (IM1 Transaction, Bulk, and Patient Facing Services APIs) and the national GP Connect FHIR programme, both governed by the Digital Care Services (DCS) framework and a Supplier Conformance Assessment List (SCAL) approved by NHS England. TPP additionally publishes its own downloadable interface specifications - the SystmOne
  Client Integration API (XML over a TCP socket), a Patient Facing Services (PFS) API, a Generic HTML API, and a Telephony API - and a formal Integration Request process. Home market is the United Kingdom, exclusively within the NHS.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: TPP (SystmOne)
nav: Providers
network: true
overview: 'TPP (SystmOne) publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United Kingdom, EHR, EMR, and FHIR.


  TPP (SystmOne)''s developer surface includes documentation, getting-started guide, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 23.1
  delta: -1.2
  facets:
    access_clarity: 9.2
    commercial_clarity: 9.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 44.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 24.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 34.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Tpp Systmone Authentication
  slug: tpp-systmone-authentication
  summary_line: mutualTLS/nhs-jwt/approval-gated-socket · 3 schemes
- kind: domain-security
  name: Tpp Systmone Domain Security
  slug: tpp-systmone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tpp-systmone
tags:
- Healthcare
- United Kingdom
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- GP Connect
- IM1
- National Health System
- Primary Care
- Clinical System
website: https://tpp-uk.com
---
