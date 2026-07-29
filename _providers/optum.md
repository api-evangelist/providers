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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: RESTful, JSON and X12 EDI (270/271, 837, 276/277, 835) healthcare transaction APIs for real-time patient eligibility and coverage verification, professional and institutional claim validation and subm
  name: Optum Medical Network Eligibility and Claims API
  slug: optum-medical-network-eligibility-and-claims-api
- description: 'FHIR R4-based Patient Access and interoperability APIs (Endpoint, Procedure, DocumentReference, ObservationVitalSigns, Immunization, and related resources) supporting CMS interoperability and patient '
  name: Optum Data Access and Interoperability (FHIR) API
  slug: optum-data-access-and-interoperability-fhir-api
- description: Real-time dental data exchange APIs for pre-care estimates, eligibility, claims submission and inquiry, attachments with image intelligence, and ERA, with GraphQL options for select operations.
  name: Optum Real for Dental API
  slug: optum-real-for-dental-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.optum.com/vulnerability.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optum-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optum-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optum-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/optum-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/optum-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optum-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.optum.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.optum.com/apitools/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.optum.com/eligibilityandclaims/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.optum.com/eligibilityandclaims/docs/get-started-with-optum-api
- group: operate
  title: ''
  type: Support
  url: https://community.optum.com/developers/home
- group: start
  title: ''
  type: SignUp
  url: https://marketplace.optum.com/apiservices/api-sandbox-access
- group: start
  title: ''
  type: Sandbox
  url: https://marketplace.optum.com/apiservices/api-sandbox-access
- group: company
  title: ''
  type: Website
  url: https://www.optum.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optum.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optum.com/privacy-policy.html
created: '2026-07-17'
description: Optum, part of UnitedHealth Group, is a health services and technology company that operates one of the largest medical and pharmacy networks in the United States. Its developer platform (developer.optum.com) exposes RESTful, JSON- and X12 EDI-based healthcare APIs for eligibility verification, professional and institutional claims validation and submission, claim status, ERA/remittance reports, prior authorization, attachments, payer directory, dental pre-care and claims, pharmacy solutions, and FHIR-based Data Access and Interoperability (Patient Access) endpoints. APIs are secured with OAuth2 client-credentials bearer tokens over TLS 1.2+, with free sandbox access, interactive "Try It" documentation, and downloadable OpenAPI specifications.
image: https://www.optum.com/content/dam/optum4/images/logos/optum-logo.svg
layout: provider
modified: '2026-07-20'
name: Optum
nav: Providers
network: true
overview: 'Optum publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Insurance, Claims, and Eligibility.


  Optum''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, sandbox, and 13 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 31.8
  delta: -3.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 10.5
  previous_composite: 35.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Optum Authentication
  slug: optum-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Optum Domain Security
  slug: optum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optum Vulnerability Disclosure
  slug: optum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: optum
tags:
- Company
- Healthcare
- Health Insurance
- Claims
- Eligibility
- FHIR
- Interoperability
- Pharmacy
- EDI
- X12
- Payments
- Prior Authorization
website: https://www.optum.com/
---
