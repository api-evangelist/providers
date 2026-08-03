---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: HL7 FHIR RESTful API for reading and writing patient health records in the PKB personal health record, secured with OAuth 2.0 / SMART on FHIR.
  name: Patients Know Best FHIR API
  slug: patients-know-best-fhir-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.patientsknowbest.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.patientsknowbest.com/space/api
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.patientsknowbest.com/space/MAN
- group: docs
  title: ''
  type: APIReference
  url: https://fhir.patientsknowbest.com/metadata
- group: operate
  title: ''
  type: ChangeLog
  url: https://wiki.patientsknowbest.com/space/REL
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pkbstatus.com/
- group: operate
  title: ''
  type: Support
  url: https://patientsknowbest.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://patientsknowbest.com/privacy-statement/
- group: auth
  title: ''
  type: Authentication
  url: authentication/patientsknowbest-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/patientsknowbest-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/patientsknowbest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/patientsknowbest-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/patientsknowbest-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/patientsknowbest-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/patientsknowbest-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patientsknowbest-domain-security.yml
created: '2026-07-17'
description: Patients Know Best (PKB) operates one of the world's largest personal health record (PHR) platforms, giving over seven million patients a single lifelong medical record they own and control. The platform aggregates data from the NHS App, GP systems, hospitals, wearables and health-tech partners, and lets patients securely share it with clinicians and carers, manage care plans, message professionals and track symptoms. For interoperability PKB publishes a HL7 FHIR API (with a public FHIR Conformance / CapabilityStatement) secured with OAuth 2.0 following the SMART on FHIR pattern, alongside HL7 v2 messaging. Backed by Balderton Capital and added to the API Evangelist network from that VC portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patientsknowbest.png
layout: provider
modified: '2026-07-20'
name: Patients Know Best
nav: Providers
network: true
overview: 'Patients Know Best publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Records, FHIR, and Interoperability.


  Patients Know Best''s developer surface includes documentation, API reference, changelog, support, authentication, sandbox, and 10 more developer resources.'
random_paper: 39
score:
  band: emerging
  composite: 27.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 27.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Patientsknowbest Authentication
  slug: patientsknowbest-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Patientsknowbest Domain Security
  slug: patientsknowbest-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: patientsknowbest
tags:
- Company
- Healthcare
- Health Records
- FHIR
- Interoperability
- Patient Data
- NHS
- HL7
website: https://www.patientsknowbest.com/
---
