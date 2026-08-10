---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: 'Extensive collection of 400+ JSON-based RESTful API routes powering third-party and internal applications that integrate with NextGen Enterprise EHR and practice management systems. Supports read and '
  name: NextGen Enterprise API
  slug: nextgen-enterprise-api
- description: FHIR-based Patient Access API for NextGen Enterprise enabling patients to connect to their health records via smartphones or browser-based applications. Supports HL7 FHIR DSTU2 and R4 standards. Authe
  name: NextGen Enterprise Patient Access FHIR API
  slug: nextgen-enterprise-patient-access-fhir-api
- description: FHIR R4-based Patient Access API for NextGen Office (formerly MediTouch) ambulatory practices. Enables patients and authorized apps to access personal health information via the YourHealthFile patient
  name: NextGen Office Patient FHIR API
  slug: nextgen-office-patient-fhir-api
- description: SMART on FHIR App Launch API for NextGen Office enabling vendor applications to obtain USCDIv1 clinical data for a single patient. Compliant with 21st Century Cures Act requirements. Supports HL7 SMAR
  name: NextGen Office SMART App Launch FHIR API
  slug: nextgen-office-smart-app-launch-fhir-api
- description: Bulk FHIR API for NextGen Office enabling authorized vendors to obtain USCDIv1 data for multiple patients in a group using the HL7 FHIR Bulk Data Access specification. Compliant with 21st Century Cure
  name: NextGen Office Bulk FHIR API
  slug: nextgen-office-bulk-fhir-api
- description: 'API for NextGen Mirth Connect, an open-source healthcare integration engine supporting HL7 v2, FHIR, and other healthcare data standards for interoperability between clinical systems. Enables message '
  name: NextGen Mirth Connect Integration Engine API
  slug: nextgen-mirth-connect-integration-engine-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextgen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextgen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nextgen.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev-cd.nextgen.com/api
- group: other
  title: ''
  type: DeveloperProgram
  url: https://www.nextgen.com/developer-program
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nextgen.com/api-on-boarding
- group: other
  title: ''
  type: Marketplace
  url: https://www.nextgen.com/solutions/marketplace
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nextgenhealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextgenhealthcareinc
- group: other
  title: ''
  type: X
  url: https://twitter.com/nextgen
- group: company
  title: ''
  type: Blog
  url: https://www.nextgen.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.nextgen.com/company/newsroom
- group: other
  title: ''
  type: Interoperability
  url: https://www.nextgen.com/solutions/interoperability/api-fhir
- group: commercial
  title: ''
  type: Plans
  url: plans/nextgen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nextgen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nextgen-finops.yml
created: '2026-06-13'
description: NextGen Healthcare is a leading ambulatory care EHR and practice management platform providing REST and FHIR APIs for clinical data, scheduling, patient engagement, and healthcare interoperability. The platform offers Enterprise APIs comprising 400+ JSON-based RESTful routes covering EHR, practice management, and clinical workflows, as well as FHIR R4 Patient Access APIs, SMART on FHIR App Launch APIs, and Bulk FHIR APIs compliant with 21st Century Cures Act requirements. Authentication uses OAuth 2.0 with authorization code and client credentials flows. Products support USCDI v1 data exchange, HL7 FHIR DSTU2 and R4 standards, and Mirth Connect integration engine for HL7-based interoperability.
finops:
- name: Nextgen Finops
  service_category: ''
  slug: nextgen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nextgen.png
jsonld:
- class_count: 22
  name: Nextgen Context
  property_count: 2
  slug: nextgen-context
layout: provider
modified: '2026-06-13'
name: NextGen Healthcare
nav: Providers
network: true
overview: 'NextGen Healthcare publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EHR, FHIR, Healthcare, Ambulatory Care, and Clinical Data.


  The NextGen Healthcare catalog on APIs.io includes 1 JSON-LD context.


  NextGen Healthcare''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Nextgen Plans Pricing
  plan_count: 4
  slug: nextgen-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Nextgen Rate Limits
  slug: nextgen-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextgen/refs/heads/main/screenshots/nextgen-2026-06-20T190302.png
security:
- kind: domain-security
  name: Nextgen Domain Security
  slug: nextgen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nextgen
tags:
- EHR
- FHIR
- Healthcare
- Ambulatory Care
- Clinical Data
- Patient Access
- SMART on FHIR
- Practice Management
- Interoperability
- HL7
- 21st Century Cures
website: https://www.nextgen.com/
---
