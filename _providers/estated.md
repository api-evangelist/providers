---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Estated Agentic Access
  operation_count: 1
  slug: estated-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The Property API from Estated — 1 operation(s) for property.
  name: Estated Property API
  slug: estated-property-api
artifact_total: 13
collections:
- collection_type: open
  name: Estated Property Data API
  slug: open-estated-property-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/estated-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estated-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/estated-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://estated.com
- group: other
  title: ''
  type: Developers
  url: https://estated.com/developers/docs/v4
- group: docs
  title: ''
  type: Documentation
  url: https://estated.com/developers/docs/v4/property/overview
- group: docs
  title: ''
  type: Schema
  url: https://estated.com/developers/docs/v4/property/schema
- group: start
  title: ''
  type: Signup
  url: https://estated.com/login
- group: other
  title: ''
  type: ParentCompany
  url: https://www.attomdata.com/
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.attomdata.com/news/company-news/attom-company-announcement-10/
- group: other
  title: ''
  type: ParentCompanyProduct
  url: https://www.attomdata.com/solutions/property-data-api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.attomdata.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.attomdata.com/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://www.attomdata.com/contact-us/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/estated
created: '2026-05-25'
description: Estated is a property-data company that operates a JSON REST API returning detailed U.S. residential and commercial property records — assessor data, parcel geometry, structure characteristics, taxes, assessments, market assessments, valuation (AVM), owner of record, deeds, and parcel boundaries. Lookups can be performed by split address, parsed address components, a single combined address string, or by FIPS county code + assessor parcel number (APN). The current public surface is the Property Data API v4 at `https://apis.estated.com/v4/property`, authenticated with a `token` query parameter. Estated was acquired by ATTOM Data in 2020 and its infrastructure is being migrated to ATTOM; the Estated developer documentation is scheduled to be deprecated during 2026, after which property data access will be served through ATTOM's documentation and endpoints. Existing Estated tokens continue to work through the transition and no integration changes are required during the migration
  window.
examples:
- key_count: 2
  name: Estated Get Property Example
  slug: estated-get-property-example
finops:
- name: Estated Finops
  service_category: ''
  slug: estated-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/estated.png
json_schemas:
- name: Estated Property
  property_count: 11
  slug: estated-property
jsonld:
- class_count: 48
  name: Estated Context
  property_count: 0
  slug: estated-context
layout: provider
modified: '2026-05-25'
name: Estated
nav: Providers
network: true
overview: 'Estated publishes 1 API on the [APIs.io](https://apis.io/) network: Property API. Tagged areas include Property Data, Real Estate, Property Records, Assessor, and Parcels.


  The Estated catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Estated''s developer surface includes authentication, documentation, signup flow, GitHub presence, and 11 more developer resources.'
plans:
- name: Estated Plans Pricing
  plan_count: 3
  slug: estated-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 0
  name: Estated Rate Limits
  slug: estated-rate-limits
rules:
- name: Estated API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: estated-jsonschema-spectral-rules
- name: Estated API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: estated-rules
score:
  band: developing
  composite: 48.6
  delta: -4.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/estated/refs/heads/main/screenshots/estated-2026-06-20T180825.png
security:
- kind: authentication
  name: Estated Authentication
  slug: estated-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Estated Domain Security
  slug: estated-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: estated
tags:
- Property Data
- Real Estate
- Property Records
- Assessor
- Parcels
- APN
- FIPS
- Deeds
- AVM
- Valuation
- Boundaries
- GIS
- Owner Of Record
- Tax Assessment
website: https://estated.com
---
