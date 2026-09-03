---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://docs.surescripts.com/
  - https://docs.surescripts.com/medhistory-populations/guide/integration-and-production
  - https://surescripts.com/who-we-are/contact-us
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-02'
api_count: 8
apis:
- description: 'Publicly documented HL7 FHIR Release 4 API for retrieving medication history panels and near-real-time Prescription Notifications for enrolled patient populations. Panels and notifications are pulled '
  name: Surescripts Medication History for Populations FHIR API
  slug: surescripts-medication-history-populations-fhir-api
- description: Four documented REST endpoints that let a technology vendor locate and download NCPDP Formulary and Benefit lists - GET /formulary/pbms, GET /formulary/listTypes, GET /formulary/lists (paged search by
  name: Surescripts Formulary Download API
  slug: surescripts-formulary-download-api
- description: 'Routes electronic prescriptions between prescribers and pharmacies over the NCPDP SCRIPT standard (version 2023011), supporting NewRx, RxRenewalRequest/Response, RxChangeRequest/Response, RxTransfer, '
  name: Surescripts E-Prescribing
  slug: surescripts-e-prescribing-api
- description: 'Verifies patient pharmacy benefit eligibility and returns formulary and benefit coverage details so prescribers see coverage and coverage alternatives in workflow. Eligibility rides X12 270 request / '
  name: Surescripts Eligibility and Formulary
  slug: surescripts-eligibility-formulary-api
- description: Returns patient-specific, real-time out-of-pocket drug cost, coverage status, and therapeutic alternatives at the point of prescribing, as a synchronous RTPBRequest/RTPBResponse pair. Implements the N
  name: Surescripts Real-Time Prescription Benefit
  slug: surescripts-real-time-prescription-benefit-api
- description: Automates electronic prior authorization (ePA) between prescribers and PBMs/payers using the NCPDP SCRIPT ePA transaction set (PAInitiationRequest, PARequest, PAResponse, and related messages) alongsi
  name: Surescripts Electronic Prior Authorization
  slug: surescripts-electronic-prior-authorization-api
- description: Provides secure, HIPAA-compliant clinical message exchange (Direct Secure Messaging) for care coordination between providers, including transitions of care and referrals. Delivered over the Direct Sta
  name: Surescripts Clinical Direct Messaging
  slug: surescripts-clinical-direct-messaging-api
- description: 'Locates where a patient has clinical records across the network and enables retrieval of relevant clinical documents to inform care decisions. Delivered to certified participants through the network; '
  name: Surescripts Record Locator and Exchange
  slug: surescripts-record-locator-exchange-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://surescripts.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.surescripts.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.surescripts.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.surescripts.com/formulary-download/guide/api-details
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.surescripts.com/connectivity/home
- group: operate
  title: ''
  type: Support
  url: https://surescripts.com/support
- group: company
  title: ''
  type: Blog
  url: https://surescripts.com/insights
- group: start
  title: ''
  type: Login
  url: https://sso.surescripts.net/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://surescripts.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://surescripts.com/privacy-office
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/surescripts
- group: auth
  title: ''
  type: Certifications
  url: https://surescripts.com/why-surescripts/certifications-and-accreditations
- group: auth
  title: ''
  type: Compliance
  url: https://surescripts.com/why-surescripts/certifications-and-accreditations
- group: auth
  title: ''
  type: TrustCenter
  url: security/surescripts-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surescripts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/surescripts-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/surescripts-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/surescripts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/surescripts-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/surescripts-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/surescripts-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/surescripts-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/surescripts-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/surescripts-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/surescripts-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/surescripts-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/surescripts-llms.txt
created: '2026-07-04'
description: Surescripts operates the largest health information network in the United States, connecting prescribers, pharmacies, pharmacy benefit managers (PBMs), health plans, and health systems for e-prescribing, medication history, benefit and eligibility verification, electronic prior authorization, and clinical interoperability. Transaction services run over NCPDP SCRIPT (NewRx, RxRenewal, RxChange, RxTransfer, RxFill, CancelRx), NCPDP Real-Time Prescription Benefit, NCPDP Formulary and Benefit, X12 (270/271 eligibility, 278 prior authorization), the Direct Standard, and - since the Surescripts Developer Portal launched at docs.surescripts.com on 2026-08-06 - two publicly documented HTTP APIs - a Medication History for Populations API implemented in HL7 FHIR R4, and a four-endpoint Formulary Download REST API. Both authenticate the calling organization with a Surescripts-issued client certificate over mutual TLS plus a Participant ID header; Surescripts runs its own Certificate Authority.
  There is still no OpenAPI, no self-serve sign-up, no published pricing and no free API keys - production access requires Surescripts certification (conformance testing against current NCPDP standards, Certification Review Board contract approval, and a DEA third-party audit for EPCS) or integration through a certified middleware/EHR partner.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surescripts.png
layout: provider
modified: '2026-08-15'
name: Surescripts
nav: Providers
network: true
overview: 'Surescripts publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, e-Prescribing, Health Information Network, NCPDP SCRIPT, and Medication History.


  Surescripts'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 20 more developer resources.'
plans:
- name: Surescripts Plans Pricing
  plan_count: 0
  slug: surescripts-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Surescripts Rate Limits
  slug: surescripts-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/surescripts/refs/heads/main/screenshots/surescripts-2026-09-02T161313.png
security:
- kind: authentication
  name: Surescripts Authentication
  slug: surescripts-authentication
  summary_line: mutualTLS/apiKey · 4 schemes
- kind: domain-security
  name: Surescripts Domain Security
  slug: surescripts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Surescripts Trust Center
  slug: surescripts-trust-center
  summary_line: HITRUST r2, SOC 2 Type II, EHNAC, DirectTrust, WebTrust for Certification Authorities, HIPAA
slug: surescripts
tags:
- Healthcare
- e-Prescribing
- Health Information Network
- NCPDP SCRIPT
- Medication History
- Prior Authorization
- Interoperability
- FHIR
- Formulary
- Eligibility
- Real-Time Prescription Benefit
- Mutual TLS
- Gated
website: https://surescripts.com
---
