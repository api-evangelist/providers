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
api_count: 6
apis:
- description: Routes electronic prescriptions between prescribers and pharmacies over the NCPDP SCRIPT standard, supporting NewRx, RxRenewal, RxChange, RxTransfer, RxFill, CancelRx, and NewRxRequest transactions, p
  name: Surescripts E-Prescribing
  slug: surescripts-e-prescribing-api
- description: Verifies patient pharmacy benefit eligibility and returns formulary and benefit coverage details so prescribers see coverage and coverage alternatives in workflow. Modeled on X12 270/271 eligibility e
  name: Surescripts Eligibility and Formulary
  slug: surescripts-eligibility-formulary-api
- description: Returns patient-specific, real-time out-of-pocket drug cost, coverage status, and therapeutic alternatives at the point of prescribing. Modeled on the NCPDP Real-Time Prescription Benefit (RTPB) stand
  name: Surescripts Real-Time Prescription Benefit
  slug: surescripts-real-time-prescription-benefit-api
- description: Automates electronic prior authorization (ePA) between prescribers and PBMs/payers using the NCPDP SCRIPT ePA transaction set (PAInitiationRequest, PARequest, PAResponse, and related messages). Delive
  name: Surescripts Electronic Prior Authorization
  slug: surescripts-electronic-prior-authorization-api
- description: Provides secure, HIPAA-compliant clinical message exchange (Direct Secure Messaging) for care coordination between providers, including transitions of care and referrals. Delivered over the Direct pro
  name: Surescripts Clinical Direct Messaging
  slug: surescripts-clinical-direct-messaging-api
- description: 'Locates where a patient has clinical records across the network and enables retrieval of relevant clinical documents to inform care decisions. Delivered to certified participants through the network; '
  name: Surescripts Record Locator and Exchange
  slug: surescripts-record-locator-exchange-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surescripts-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/surescripts
- group: company
  title: ''
  type: Website
  url: https://surescripts.com
- group: docs
  title: ''
  type: Documentation
  url: https://surescripts.com/what-we-do
- group: auth
  title: ''
  type: Certifications
  url: https://surescripts.com/why-surescripts/certifications-and-accreditations
created: '2026-07-04'
description: Surescripts operates the largest health information network in the United States, connecting prescribers, pharmacies, pharmacy benefit managers (PBMs), health plans, and health systems for e-prescribing, medication history, benefit and eligibility verification, electronic prior authorization, and clinical interoperability. Surescripts is a network operator rather than a public API provider - its transaction services run over NCPDP SCRIPT (NewRx, RxRenewal, RxChange, RxTransfer, RxFill, CancelRx), NCPDP Telecommunication, and X12 (270/271 eligibility, 278 prior authorization) standards. There is no self-serve developer portal, no published OpenAPI, and no free API keys; access is gated behind a Surescripts certification process (conformance testing against current NCPDP standards, plus DEA third-party audit for EPCS) or through a certified middleware/EHR partner. The service surfaces below are honestly modeled from Surescripts' published solution descriptions and the underlying
  NCPDP/X12 transaction standards - endpoints are not publicly documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surescripts.png
layout: provider
modified: '2026-07-25'
name: Surescripts
nav: Providers
network: true
overview: 'Surescripts publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, E-Prescribing, Health Information Network, NCPDP SCRIPT, and Medication History.


  Surescripts'' developer surface includes documentation and 4 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 8.1
  delta: -2.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Surescripts Domain Security
  slug: surescripts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: surescripts
tags:
- Healthcare
- E-Prescribing
- Health Information Network
- NCPDP SCRIPT
- Medication History
- Prior Authorization
- Interoperability
- Gated
website: https://surescripts.com
---
