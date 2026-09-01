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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Digital intake, consent, and clinical questionnaire capture - logic-driven interviews customized per patient and delivered as mobile intake in 20+ languages. Completed intake, consent, and patient-rep
  name: Phreesia Intake & Forms API
  slug: phreesia-intake-forms-api
- description: Bidirectional patient registration and demographic data exchange - verify and update patient identity, contact, and demographic fields and write them back to the EHR/PM system of record. Modeled on HL
  name: Phreesia Registration & Demographics API
  slug: phreesia-registration-demographics-api
- description: Appointment scheduling, reminders, and contactless mobile/kiosk check-in, driving arrival status back into the practice management system. Modeled on HL7v2 SIU and FHIR Appointment/Schedule/Slot flows
  name: Phreesia Scheduling & Appointments API
  slug: phreesia-scheduling-appointments-api
- description: Real-time insurance eligibility and benefits verification at or before check-in, returning coverage, copay, and patient-responsibility estimates. Modeled on X12 270/271 eligibility and FHIR Coverage/C
  name: Phreesia Insurance Eligibility Verification API
  slug: phreesia-eligibility-verification-api
- description: Patient payments, card-on-file, copay collection, and payment plans, with real-time payment posting back to the PM/billing system. Endpoints are modeled from published product capability; Phreesia doe
  name: Phreesia Payments API
  slug: phreesia-payments-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/phreesia-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phreesia-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/phreesia
- group: company
  title: ''
  type: Website
  url: https://www.phreesia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.phreesia.com/products/integrations/
- group: commercial
  title: ''
  type: Plans
  url: https://www.phreesia.com/pricing/
- group: other
  title: ''
  type: Company
  url: https://www.phreesia.com/company/about-us/
created: '2026-07-05'
description: Phreesia is a patient intake, registration, scheduling, payments, and engagement platform for healthcare organizations, powering more than 150 million patient visits annually. It delivers digital check-in, mobile intake and consent forms in 20+ languages, logic-driven patient interviews, real-time insurance eligibility verification, and patient payments, and pushes the resulting data back into the provider's systems of record. Phreesia is not a self-serve public API product - it is an enterprise platform whose integrations are delivered by a dedicated interoperability team using open healthcare standards (HL7v2, FHIR, CCD, CSV) alongside proprietary APIs and data extracts, with bidirectional interfaces into EHR/EMR, PM, HIE, data warehouse, and data lake systems (Epic, athenahealth, eClinicalWorks, NextGen, Oracle Health/Cerner, Veradigm, Meditech, ModMed, and more). There is no publicly documented developer portal, API reference, or self-service key registration as of this
  writing; the API surface below is modeled from Phreesia's published product and integration capabilities, not from public reference documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phreesia.png
layout: provider
modified: '2026-07-05'
name: Phreesia
nav: Providers
network: true
overview: 'Phreesia publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Patient Intake, Patient Registration, Patient Engagement, and Scheduling.


  Phreesia''s developer surface includes documentation and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 1
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Phreesia Domain Security
  slug: phreesia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Phreesia Trust Center
  slug: phreesia-trust-center
  summary_line: SOC 2, PCI DSS
slug: phreesia
tags:
- Healthcare
- Patient Intake
- Patient Registration
- Patient Engagement
- Scheduling
- Payments
- Insurance Eligibility
- HL7
- FHIR
- Interoperability
- EHR Integration
- Partner API
website: https://www.phreesia.com/
---
