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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: 'ONC Certified FHIR R4 (v4.0.1) API implementing US Core 6.1.0, SMART App Launch 2.0.0, and Bulk Data Access 1.0.1. Provides read and search access across 47 FHIR resource types (Patient, Observation, '
  name: Practice Fusion FHIR API (Patient Data Sharing)
  slug: practice-fusion-fhir-api-patient-data-sharing
- description: Proprietary bi-directional laboratory integration API connecting practices with 300+ independent, hospital, and health-system labs including Labcorp, Quest Diagnostics, RadNet, SimonMed, and Rayus for
  name: Practice Fusion Labs API
  slug: practice-fusion-labs-api
- description: Proprietary bi-directional imaging integration API for order receipt and study transmission across imaging providers, supporting 100,000+ medical professionals.
  name: Practice Fusion Imaging API
  slug: practice-fusion-imaging-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/practice-fusion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/practice-fusion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/practice-fusion-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/practice-fusion-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/practice-fusion-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.practicefusion.com/onc-certified-ehr/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/practice-fusion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/practice-fusion-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/practice-fusion-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/practice-fusion-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/practice-fusion-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/practice-fusion-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/practice-fusion-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.practicefusion.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.practicefusion.com/fhir/
- group: docs
  title: ''
  type: Documentation
  url: https://www.practicefusion.com/fhir/api-specifications/
- group: docs
  title: ''
  type: APIReference
  url: https://www.practicefusion.com/fhir/api-specifications/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.practicefusion.com/fhir/get-started/
- group: operate
  title: ''
  type: Support
  url: https://partnersupport.practicefusion.com/s/
- group: start
  title: ''
  type: SignUp
  url: https://pfpds.practicefusion.com/s/Registration
- group: company
  title: ''
  type: Blog
  url: https://www.practicefusion.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.practicefusion.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.practicefusion.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.practicefusion.com/pages/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.practicefusion.com/pages/privacy-policy.html
created: '2026-07-17'
description: Practice Fusion is a cloud-based electronic health record (EHR) platform for independent ambulatory medical practices, serving roughly 6.4% of U.S. ambulatory practices with more than 43 million clinical records and around 5 million patient visits per month. Its developer surface centers on an ONC Certified Health IT FHIR R4 (Patient Data Sharing / PDS) API implementing US Core 6.1.0, SMART App Launch 2.0.0, and Bulk Data Access 1.0.1 over SMART-on-FHIR OAuth2, alongside proprietary bi-directional Labs and Imaging APIs and a partner marketplace of 600+ integrated companies.
image: https://www.practicefusion.com/assets/img/practice-fusion-logo.png
layout: provider
mcp_servers:
- description: ''
  name: practice-fusion-mcp.yml
  slug: practice-fusion-mcpyml
modified: '2026-07-20'
name: Practice Fusion
nav: Providers
network: true
overview: 'Practice Fusion publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Electronic Health Records, EHR, and FHIR.


  Practice Fusion''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, engineering blog, and 18 more developer resources.'
random_paper: 79
scopes:
- name: Practice Fusion Scopes
  scope_count: 0
  slug: practice-fusion-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 40.0
    developer_ergonomics: 54.3
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 47.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Practice Fusion Authentication
  slug: practice-fusion-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Practice Fusion Domain Security
  slug: practice-fusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: practice-fusion
tags:
- Company
- Healthcare
- Electronic Health Records
- EHR
- FHIR
- Interoperability
- Medical
- Health IT
- SMART on FHIR
- Clinical Data
website: https://www.practicefusion.com/
---
