---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: REST API for exchanging patient, prescription, encounter and assistance-program application data between a health system, clinic or pharmacy and the TailorMed platform. Part of TailorMed's DTA (Data T
  name: TailorMed Application Data API
  slug: tailormed-application-data-api
- description: REST API for submitting and reconciling claims data against TailorMed's affordability and assistance workflows. Versioned v1.1. Reference published only on the customer-only TailorMed Implementation H
  name: TailorMed Claims Data API
  slug: tailormed-claims-data-api
- description: TailorMed's HL7 and FHIR integration program for keeping patient, prescription and program data in sync with the EHR, including an Epic MyChart integration. Its own version line, currently v1.5.3, wit
  name: TailorMed HL7 & FHIR Data Exchange
  slug: tailormed-hl7-fhir-data-exchange
- description: OpenID Connect / OAuth 2.0 authorization server for the TailorMed platform, served from TailorMed's own domain (an Okta org authorization server on the custom domain auth.tailormed.com, issuer https:/
  name: TailorMed Platform Identity
  slug: tailormed-platform-identity
artifact_total: 10
asyncapis:
- description: ''
  name: Tailormed Webhooks
  slug: tailormed-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tailormed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tailormed.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.tailormed.co/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.tailormed.co/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://hub.tailormed.co/dta/api-documentation
- group: start
  title: ''
  type: Login
  url: https://hub.tailormed.co/login
- group: company
  title: ''
  type: Blog
  url: https://www.tailormed.com/news-blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tailormed.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tailormed.com/legal/privacy-notice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tailormed---medical-journey-innovations/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tailormed-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tailormed-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tailormed-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tailormed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/tailormed-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tailormed-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tailormed-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tailormed-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tailormed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tailormed-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tailormed-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/tailormed-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tailormed-llms.txt
created: '2026-08-29'
description: TailorMed is a medication success platform that removes access, affordability and adherence barriers across the patient medication journey. Its software connects patients, health systems, clinics, pharmacies and life sciences companies to financial assistance, copay, foundation and free-drug programs, and keeps patient, prescription and program data in sync with the record of care via HL7/FHIR, a REST API, or SFTP file exchange. The product line spans TailorMed Core, Connect, Complete, Amplify and Alliance. TailorMed runs a versioned integration program — an Application Data API, a Claims Data API, a webhook guide and an HL7/FHIR data exchange — documented on a customer-only Implementation Hub; no machine-readable contract is published publicly.
image: https://cdn.prod.website-files.com/698cbb7585b4223e82472527/69e8fb0b9cc55b51bd526799_TailorMed-Share.png
layout: provider
modified: '2026-08-29'
name: TailorMed
nav: Providers
network: true
overview: 'TailorMed publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Medication Access, and Medication Affordability.


  The TailorMed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TailorMed''s developer surface includes documentation, API reference, engineering blog, authentication, changelog, and 18 more developer resources.'
plans:
- name: Tailormed Plans Pricing
  plan_count: 0
  slug: tailormed-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Tailormed Rate Limits
  slug: tailormed-rate-limits
scopes:
- name: Tailormed Scopes
  scope_count: 0
  slug: tailormed-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 46.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitech
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tailormed/refs/heads/main/screenshots/tailormed-2026-09-02T162452.png
security:
- kind: authentication
  name: Tailormed Authentication
  slug: tailormed-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tailormed Domain Security
  slug: tailormed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tailormed
tags:
- Company
- Healthcare
- Health IT
- Medication Access
- Medication Affordability
- Financial Navigation
- Patient Assistance
- Pharmacy
- Oncology
- Revenue Cycle
- HL7
- FHIR
- Life Sciences
website: https://www.tailormed.com
---
