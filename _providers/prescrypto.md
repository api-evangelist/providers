---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Prescrypto Agentic Access
  operation_count: 32
  slug: prescrypto-agentic-access
  summary_line: 32 operations · 15 acting
api_count: 8
apis:
- description: Hospital / clinic records.
  name: Prescrypto Hospitals API
  slug: prescrypto-hospitals-api
- description: Geographic locations catalog.
  name: Prescrypto Locations API
  slug: prescrypto-locations-api
- description: Medic (prescriber) accounts managed by an admin/manager token.
  name: Prescrypto Medics API
  slug: prescrypto-medics-api
- description: Medic-to-hospital memberships.
  name: Prescrypto Memberships API
  slug: prescrypto-memberships-api
- description: Patient records.
  name: Prescrypto Patients API
  slug: prescrypto-patients-api
- description: Pharmacy-token operations to search and dispense prescriptions.
  name: Prescrypto Pharmacy API
  slug: prescrypto-pharmacy-api
- description: Electronic prescriptions (eRx).
  name: Prescrypto Prescriptions API
  slug: prescrypto-prescriptions-api
- description: Standard-drug catalog search (separate JWT-authenticated endpoint).
  name: Prescrypto Products API
  slug: prescrypto-products-api
artifact_total: 12
asyncapis:
- description: ''
  name: Prescrypto Webhooks
  slug: prescrypto-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prescrypto-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prescrypto-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prescrypto-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prescrypto-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/prescrypto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prescrypto-packages.yml
- group: design
  title: ''
  type: Components
  url: components/prescrypto-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prescrypto-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/prescrypto-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/prescrypto-create-prescription.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/prescrypto-pharmacy-dispense.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prescrypto-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.prescrypto.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/wilsotobianco/prescrypto-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Prescrypto
- group: operate
  title: ''
  type: Support
  url: https://www.prescrypto.com/contact/
- group: company
  title: ''
  type: Website
  url: https://prescrypto.com
created: '2026-07-17'
description: 'Prescrypto is an electronic-prescription (eRx) platform used across Mexico and LATAM, backed by 500 Global. Its REST Integration API lets EHRs, hospital systems, telemedicine apps and pharmacies manage medics, hospitals, patients and prescriptions; generate legally-valid electronic prescriptions that are verified against Mexico''s NOM-151-SCFI-2016 standard via the RexChain blockchain notary; download prescription PDFs; and let pharmacies search and dispense (burn) prescribed medications. The platform also ships a Deeplink auto-login/auto-fill flow, a standard-drug catalog search of ~25,000 records, webhooks for prescription events, and a prescrypto-elements web-component library for embedding Rx functionality in a host site. Authentication is HTTP Token auth (Authorization: Token <key>).'
image: https://www.prescrypto.com/media/logo.jpg
layout: provider
modified: '2026-07-20'
name: Prescrypto
nav: Providers
network: true
overview: 'Prescrypto publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Hospitals API, Locations API, Medics API, and 5 more. Tagged areas include Company, Healthcare, Electronic Prescriptions, eRx, and Pharmacy.


  The Prescrypto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Prescrypto''s developer surface includes authentication, changelog, documentation, API reference, support, and 12 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 38.8
  delta: -0.4
  facets:
    commercial_clarity: 7.9
    contract_quality: 64.6
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.2
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Prescrypto Authentication
  slug: prescrypto-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Prescrypto Domain Security
  slug: prescrypto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prescrypto
tags:
- Company
- Healthcare
- Electronic Prescriptions
- eRx
- Pharmacy
- Telemedicine
- Medical
- Mexico
- LATAM
website: https://prescrypto.com
---
