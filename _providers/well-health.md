---
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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: apps.health is WELL Health's digital health marketplace through which third-party apps and services integrate with WELL's network of EMRs (OSCAR Pro, Profile), which support HL7 FHIR and other interop
  name: apps.health EMR Integration (FHIR)
  slug: apps-health-integration
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/well-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://well.company/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apps.health/for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://apps.health/for-developers
- group: start
  title: ''
  type: GettingStarted
  url: https://apps.health/how-to-get-your-product-on-apps-health/
- group: design
  title: ''
  type: Conformance
  url: conformance/well-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/well-health-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://well.company/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://well.company/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apps.health/terms
- group: operate
  title: ''
  type: Support
  url: https://well.company/contact/
created: '2026-07-24'
description: 'WELL Health Technologies Corp (TSX: WELL, OTCQX: WHTCF) is a Vancouver, Canada-headquartered healthcare technology company that is Canada''s largest outpatient medical clinic owner-operator and a leading multi-disciplinary digital health service provider. It runs two synergistic channels: an omni-channel patient services business operating 115+ multidisciplinary clinics across Canada plus US telehealth and anesthesia operations, and a virtual-services / practitioner-enablement platform serving 44,000+ providers through the OSCAR Pro EMR, billing and revenue-cycle tools, eReferral, digital booking, and ePharma. Its programmatic surface is the apps.health marketplace, through which third-party digital health apps integrate with WELL''s network of EMRs (OSCAR Pro, Profile) using HL7 FHIR and other interoperability standards. As of this review WELL exposes no self-serve public developer portal, sandbox, OpenAPI, or FHIR CapabilityStatement; integration is FHIR-based but gated behind
  a partner/contact process. Home market is Canada, positioned in a province-fragmented healthcare landscape coordinated federally by Canada Health Infoway''s pan-Canadian FHIR (CA Core / CA Baseline) specifications.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: WELL Health Technologies
nav: Providers
network: true
overview: 'WELL Health Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, EMR, EHR, and FHIR.


  WELL Health Technologies'' developer surface includes documentation, getting-started guide, engineering blog, support, and 7 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 20.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Well Health Domain Security
  slug: well-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: well-health
tags:
- Healthcare
- Canada
- EMR
- EHR
- FHIR
- HL7
- Interoperability
- Digital Health
- Telehealth
- ePharma
- Clinics
website: https://well.company/
---
