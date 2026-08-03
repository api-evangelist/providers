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
    auth_clarity: false
    consent_identity: false
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
  score: 0.0
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: 'Modeled partner-gated surface for submitting laboratory requisitions (test orders) electronically to Antech''s reference lab from a veterinary PIMS. Carries the ordering clinic, patient, and requested '
  name: Antech Lab Orders API
  slug: antech-diagnostics-lab-orders-api
- description: 'Modeled partner-gated surface for delivering completed diagnostic results back to the ordering PIMS, where they land in the patient''s medical record. Results include analyte values, reference ranges, '
  name: Antech Lab Results API
  slug: antech-diagnostics-lab-results-api
- description: Modeled patient and client demographic exchange that accompanies a requisition - species, breed, sex, and owner details are linked from the PIMS so results map back to the correct animal record. Not a
  name: Antech Patients API
  slug: antech-diagnostics-patients-api
- description: Modeled reference surface exposing Antech's test catalog - test codes, panels, and species/breed reference data - so a PIMS can map its inventory items to the correct Antech tests. Modeled from docume
  name: Antech Reference Data & Test Catalog API
  slug: antech-diagnostics-reference-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antech-diagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.antechdiagnostics.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antech-diagnostics
- group: start
  title: ''
  type: Portal
  url: https://online.antechdiagnostics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.antechdiagnostics.com/reference-lab/healthtracks/
- group: operate
  title: ''
  type: Support
  url: https://antechonlinesupport.freshdesk.com/support/solutions
- group: other
  title: ''
  type: Parent
  url: https://www.mars.com/made-by-mars/petcare
created: '2026-07-05'
description: Antech Diagnostics operates North America's largest veterinary reference laboratory network, plus in-house diagnostic instruments, imaging, and the HealthTracks diagnostics platform. Antech is part of Mars Petcare (Mars Veterinary Health), acquired via Mars' 2017 purchase of VCA. Antech's programmatic surface is a partner-gated laboratory integration API - commonly configured in practice information management systems (PIMS) as "Antech V3" - that lets veterinary software submit lab requisitions to Antech and receive results back into the patient's medical record. There is no public, self-serve developer portal or published API reference; access requires an Antech account and a business / integration partner relationship, authenticated with an Account Number, Username, Password, and Clinic ID. The logical APIs below are modeled from documented PIMS integration behavior (Vetspire, Cornerstone, DaySmart Vet, NaVetor, ezyVet, NectarVet), not from an Antech-published specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/antech-diagnostics.png
layout: provider
modified: '2026-07-05'
name: Antech Diagnostics
nav: Providers
network: true
overview: 'Antech Diagnostics publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Veterinary, Diagnostics, Laboratory, Reference Lab, and Lab Results.


  Antech Diagnostics'' developer surface includes developer portal, documentation, support, and 4 more developer resources.'
random_paper: 43
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antech-diagnostics/refs/heads/main/screenshots/antech-diagnostics-2026-07-25T200433.png
security:
- kind: domain-security
  name: Antech Diagnostics Domain Security
  slug: antech-diagnostics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antech-diagnostics
tags:
- Veterinary
- Diagnostics
- Laboratory
- Reference Lab
- Lab Results
- Animal Health
- PIMS Integration
- Mars Petcare
website: https://www.antechdiagnostics.com/
---
