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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The UPMC Health Plan Developer API is the payer-side FHIR API mandated by the ONC 21st Century Cures Act and the CMS Interoperability and Patient Access Final Rule. It allows registered third-party ap
  name: UPMC Health Plan ONC 21st Century Cures Act Developer API
  slug: cures-act-developer-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upmc-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.upmc.com/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UPMC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upmc
- group: company
  title: ''
  type: Website
  url: https://www.upmc.com/
- group: company
  title: ''
  type: Website
  url: https://www.upmchealthplan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.upmchealthplan.com/
created: '2026-05-05'
description: A world-renowned health care provider and insurer headquartered in Pittsburgh, Pennsylvania. One of the largest nonprofit health systems in the United States, operating hospitals, physician practices, and a health insurance division (UPMC Health Plan) serving millions of members. UPMC Health Plan exposes an ONC 21st Century Cures Act Developer API for patient-authorized access to clinical and claims data over HL7 FHIR.
features:
- description: Member-authorized access to clinical (USCDI) and claims data per CMS Interoperability and Patient Access Final Rule
  name: Patient Access FHIR API
- description: Public machine-readable provider directory required by CMS Interoperability rules
  name: Provider Directory API
- description: OAuth 2.0 / SMART-on-FHIR app authorization flow for patient-mediated access
  name: SMART-on-FHIR Authorization
- description: USCDI-aligned FHIR R4 resources for clinical and claims data exchange
  name: HL7 FHIR R4 Data Model
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upmc.png
integrations:
- description: Apps register with UPMC Health Plan as SMART-on-FHIR clients to authenticate members
  name: SMART App Launch
- description: USCDI-aligned clinical resources flow to member-authorized third-party applications
  name: USCDI Clinical Data
layout: provider
modified: '2026-05-16'
name: UPMC
nav: Providers
network: true
overview: 'UPMC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health Insurance, Hospitals, Pennsylvania, and FHIR.


  UPMC''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.4
  delta: -1.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upmc/refs/heads/main/screenshots/upmc-2026-06-20T200522.png
security:
- kind: domain-security
  name: Upmc Domain Security
  slug: upmc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upmc
tags:
- Healthcare
- Health Insurance
- Hospitals
- Pennsylvania
- FHIR
use_cases:
- description: Members move their clinical and claims data into third-party apps for personal use
  name: Patient Data Portability
- description: Authorized clinical applications retrieve member records to improve care coordination across providers
  name: Care Coordination
- description: Consumer-facing personal health record and wellness apps connect to UPMC member data with patient consent
  name: Health Apps and PHRs
- description: Apps and portals discover in-network UPMC Health Plan providers through the public provider directory API
  name: Provider Directory Lookups
website: https://www.upmc.com/
---
