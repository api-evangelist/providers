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
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: The Veradigm FHIR R4 API provides RESTful access to clinical, demographic, and facility data using the HL7 FHIR R4 standard. It supports 28 FHIR resources including Patient, Condition, Observation, Me
  name: Veradigm FHIR R4 API
  slug: veradigm-fhir-r4-api
- description: The Veradigm Unity API exposes clinical, scheduling, demographic, and practice management functions across Allscripts EHR product lines including Touchworks, Professional EHR, and acute care solutions
  name: Veradigm Unity API
  slug: veradigm-unity-api
- description: 'The Paragon Open API provides FHIR-compliant access to data from the Veradigm Paragon acute care EHR platform. It enables third-party applications to integrate with Paragon to access patient clinical '
  name: Veradigm Paragon Open API
  slug: veradigm-paragon-open-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allscripts-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.veradigm.com/
- group: start
  title: ''
  type: DeveloperPortalLegacy
  url: https://developer.allscripts.com/
- group: other
  title: ''
  type: AppExpo
  url: https://expo.veradigm.com/apps
- group: start
  title: ''
  type: Signup
  url: https://developer.veradigm.com/Content/fhir/content/Developer_Signup/
- group: commercial
  title: ''
  type: Plans
  url: https://developer.veradigm.com/Home/LearnMore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veradigm.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veradigm.com/legal/privacy-notice/
- group: build
  title: ''
  type: MasterClientAgreement
  url: https://veradigm.com/img/legal/Client-Master-Agreement.pdf
- group: auth
  title: ''
  type: SecurityProgram
  url: https://veradigm.com/legal/privacy-and-security-program/
- group: auth
  title: ''
  type: ComplianceONC
  url: https://veradigm.com/legal/onc-reg-compliance/
- group: company
  title: ''
  type: Blog
  url: https://veradigm.com/blog/
- group: learn
  title: ''
  type: APIWorkshop
  url: https://lp.veradigm.com/api-workshop-registration-april
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/allscripts/refs/heads/main/finops/allscripts-finops.yml
created: '2026-06-13'
description: Allscripts, now operating as Veradigm, is a healthcare IT company providing REST and FHIR APIs for EHR data exchange, clinical workflows, patient portal, and practice management integrations. The Veradigm Developer Program (formerly Allscripts Developer Program) offers FHIR R4 APIs covering 28 clinical resources as well as a Unity API for clinical, scheduling, demographic, and practice management functions across Allscripts EHR products.
finops:
- name: Allscripts Finops
  service_category: ''
  slug: allscripts-finops
graphqls:
- description: This conceptual GraphQL schema represents the Allscripts (Veradigm) healthcare EHR APIs, covering the Veradigm FHIR R4 API and the Veradigm Unity API. Allscripts, now operating under the Veradigm bran
  name: Allscripts (Veradigm) GraphQL Schema
  slug: allscripts-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allscripts.png
jsonld:
- class_count: 0
  name: Allscripts Context
  property_count: 19
  slug: allscripts-context
layout: provider
modified: '2026-06-13'
name: Allscripts
nav: Providers
network: true
overview: 'Allscripts publishes 1 API on the [APIs.io](https://apis.io/) network: Veradigm FHIR R4 API. Tagged areas include Healthcare IT, EHR, FHIR, Clinical Data, and Practice Management.


  The Allscripts catalog on APIs.io includes 1 JSON-LD context.


  Allscripts'' developer surface includes signup flow, engineering blog, and 12 more developer resources.'
plans:
- name: Unity Api Plans
  plan_count: 3
  slug: unity-api-plans
- name: Veradigm Fhir Plans
  plan_count: 6
  slug: veradigm-fhir-plans
random_paper: 45
rate_limits:
- limit_count: 0
  name: Unity Api Rate Limits
  slug: unity-api-rate-limits
- limit_count: 0
  name: Veradigm Fhir Rate Limits
  slug: veradigm-fhir-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 2.3
  facets:
    commercial_clarity: 73.7
    contract_quality: 58.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allscripts/refs/heads/main/screenshots/allscripts-2026-06-20T171537.png
security:
- kind: domain-security
  name: Allscripts Domain Security
  slug: allscripts-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: allscripts
tags:
- Healthcare IT
- EHR
- FHIR
- Clinical Data
- Practice Management
- HL7
website: https://developer.veradigm.com/
---
