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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: FHIR R4 API enabling patients and authorized applications to access clinical health records from Netsmart provider EHR systems including myAvatar, myEvolv, myUnity, GEHRIMED, and TheraOffice. Implemen
  name: Netsmart CareConnect Provider Patient Access API
  slug: netsmart-careconnect-provider-patient-access-api
- description: FHIR R4 backend service API for system-to-system integration and asynchronous bulk data export from Netsmart provider EHR platforms. Supports population-level data extraction per the HL7 Bulk Data 2.0
  name: Netsmart CareConnect Provider System Access API
  slug: netsmart-careconnect-provider-system-access-api
- description: FHIR R4 API for payer organizations enabling patient-directed access to claims, clinical, and coverage data. Supports 30+ FHIR R4 resources including ExplanationOfBenefit, Coverage, and US Core clinic
  name: Netsmart CareConnect Payer Patient Access API
  slug: netsmart-careconnect-payer-patient-access-api
- description: Publicly accessible FHIR R4 API for discovering healthcare providers, organizations, locations, services, and insurance plans within payer networks. No authentication required. Implements DaVinci PDex
  name: Netsmart CareConnect Payer Provider Directory API
  slug: netsmart-careconnect-payer-provider-directory-api
- description: Public endpoint returning an HL7 FHIR R4 Bundle of Organization and Endpoint resources that describe all available CareConnect service base URLs across Netsmart EHR products. Implements SMART App Laun
  name: Netsmart CareConnect Service Base URLs API
  slug: netsmart-careconnect-service-base-urls-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netsmart-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/netsmart/refs/heads/main/plans/netsmart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/netsmart/refs/heads/main/rate-limits/netsmart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/netsmart/refs/heads/main/finops/netsmart-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://careconnect.netsmartcloud.com/docs/
- group: start
  title: ''
  type: Portal
  url: https://careconnect.netsmartcloud.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://careconnect.netsmartcloud.com/docs/getting-started/registration/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://careconnect.netsmartcloud.com/docs/certified/authorization/index.html
- group: start
  title: ''
  type: Sandbox
  url: https://fhirtest.netsmartcloud.com/developers
- group: start
  title: ''
  type: Portal
  url: https://fhir.netsmartcloud.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oauthtest.netsmartcloud.com/terms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careconnect.netsmartcloud.com/terms-of-service/index.html
- group: learn
  title: ''
  type: Tutorials
  url: https://careconnect.netsmartcloud.com/docs/tutorials/index.html
- group: learn
  title: ''
  type: Tutorials
  url: https://careconnect-dev.netsmartdev.com/docs/tutorials/testing-fhir-patient-access-apis-with-postman/index.html
- group: operate
  title: ''
  type: Contact
  url: https://www.ntst.com/lp/information-sharing
- group: company
  title: ''
  type: Website
  url: https://www.ntst.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ntst.com/blog
created: '2026-06-13'
description: Netsmart is a healthcare IT platform provider serving behavioral health, post-acute care, and human services organizations. Its CareConnect integration platform exposes FHIR R4 REST APIs for EHR data access, care coordination, analytics, and interoperability across care settings. APIs support Patient Access, System Access (bulk data), Provider Directory, and General Purpose FHIR R4/STU3 resources across Netsmart EHR products including myAvatar, myEvolv, myUnity, GEHRIMED, and TheraOffice.
finops:
- name: Netsmart Finops
  service_category: ''
  slug: netsmart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netsmart.png
jsonld:
- class_count: 36
  name: Netsmart Context
  property_count: 19
  slug: netsmart-context
layout: provider
modified: '2026-06-13'
name: Netsmart
nav: Providers
network: true
overview: 'Netsmart publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare IT, EHR, FHIR, Behavioral Health, and Post-Acute Care.


  The Netsmart catalog on APIs.io includes 1 JSON-LD context.


  Netsmart''s developer surface includes documentation, developer portal, getting-started guide, authentication, sandbox, engineering blog, and 11 more developer resources.'
plans:
- name: Netsmart Plans Pricing
  plan_count: 2
  slug: netsmart-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 3
  name: Netsmart Rate Limits
  slug: netsmart-rate-limits
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netsmart/refs/heads/main/screenshots/netsmart-2026-06-20T190207.png
security:
- kind: domain-security
  name: Netsmart Domain Security
  slug: netsmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: netsmart
tags:
- Healthcare IT
- EHR
- FHIR
- Behavioral Health
- Post-Acute Care
- Human Services
- Interoperability
- HL7
- Care Coordination
website: https://www.ntst.com/
---
