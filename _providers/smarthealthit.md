---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Smarthealthit Agentic Access
  operation_count: 15
  slug: smarthealthit-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 6
apis:
- description: Specification for issuing and verifying tamper-evident clinical records - vaccination history, lab results, and insurance cards - as signed JWS payloads carried in QR codes or files. Issuers expose th
  name: SMART Health Cards Framework
  slug: smarthealthit-health-cards-framework
- description: FHIR Bulk Data $export operations on the reference Bulk Data server.
  name: SMART Health IT Bulk Data API
  slug: smarthealthit-bulk-data-api
- description: Observations, conditions, medications, encounters, allergies, and immunizations.
  name: SMART Health IT Clinical Records API
  slug: smarthealthit-clinical-records-api
- description: Server capability discovery.
  name: SMART Health IT Conformance API
  slug: smarthealthit-conformance-api
- description: Synthetic patient demographic records.
  name: SMART Health IT Patients API
  slug: smarthealthit-patients-api
- description: OAuth 2.0 authorization endpoints on the SMART App Launcher.
  name: SMART Health IT SMART App Launch API
  slug: smarthealthit-smart-app-launch-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SMART Health IT Sandbox FHIR APIs Bulk Data API
  slug: open-smarthealthit-bulk-data-api
- collection_type: open
  name: SMART Health IT Sandbox FHIR APIs Bulk Data Clinical Records API
  slug: open-smarthealthit-clinical-records-api
- collection_type: open
  name: SMART Health IT Sandbox FHIR APIs Bulk Data Conformance API
  slug: open-smarthealthit-conformance-api
- collection_type: open
  name: SMART Health IT Sandbox FHIR APIs Bulk Data Patients API
  slug: open-smarthealthit-patients-api
- collection_type: open
  name: SMART Health IT Sandbox FHIR APIs Bulk Data SMART App Launch API
  slug: open-smarthealthit-smart-app-launch-api
- collection_type: open
  name: SMART Health IT Sandbox FHIR APIs
  slug: open-smarthealthit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smarthealthit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smarthealthit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smarthealthit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smarthealthit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://smarthealthit.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.smarthealthit.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smart-on-fhir
- group: docs
  title: ''
  type: Specification
  url: https://hl7.org/fhir/smart-app-launch/
- group: commercial
  title: ''
  type: Plans
  url: plans/smarthealthit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smarthealthit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smarthealthit-finops.yml
created: '2026-07-11'
description: SMART Health IT is the open standards and open source project run by the Computational Health Informatics Program at Boston Children's Hospital and Harvard Medical School that defines SMART on FHIR - the OAuth 2.0-based SMART App Launch framework that lets patient-facing and clinician-facing apps plug into any EHR and read clinical records over FHIR. The project publishes the HL7 SMART App Launch and FHIR Bulk Data specifications, the SMART Health Cards and SMART Health Links verifiable clinical data frameworks, open source client libraries, and free public sandboxes - an open FHIR R4 server loaded with synthetic patient records, the SMART App Launcher for simulating EHR and patient portal launches, and a reference Bulk Data server for testing system-level export.
finops:
- name: Smarthealthit Finops
  service_category: Healthcare Interoperability
  slug: smarthealthit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smarthealthit.png
layout: provider
modified: '2026-07-11'
name: SMART Health IT
nav: Providers
network: true
overview: 'SMART Health IT publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bulk Data API, Clinical Records API, Conformance API, and 2 more. Tagged areas include SMART on FHIR, FHIR, Health IT, EHR Integration, and Clinical Data.


  SMART Health IT''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Smarthealthit Plans Pricing
  plan_count: 1
  slug: smarthealthit-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 4
  name: Smarthealthit Rate Limits
  slug: smarthealthit-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 1.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Smarthealthit Authentication
  slug: smarthealthit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Smarthealthit Domain Security
  slug: smarthealthit-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Smarthealthit Vulnerability Disclosure
  slug: smarthealthit-vulnerability-disclosure
  summary_line: disclosure policy published
slug: smarthealthit
tags:
- SMART on FHIR
- FHIR
- Health IT
- EHR Integration
- Clinical Data
- Clinical Records
- Patient Facing
- Open Standards
- Interoperability
website: https://smarthealthit.org
---
