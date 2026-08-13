---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Photon's native GraphQL Clinical API for managing patients, prescriptions, orders, pharmacies, the treatment/medication catalog, drug-drug and drug-allergy interaction screening, webhooks, and organiz
  name: Photon Clinical API
  slug: photon-clinical-api
- description: 'Photon''s GraphQL Patient Benefits API for managing patient benefits and enabling pharmacy benefit checks (coverage options, copay, and formulary) during the prescribing workflow. Served over the same '
  name: Photon Patient Benefits API
  slug: photon-patient-benefits-api
artifact_total: 7
asyncapis:
- description: ''
  name: Photon Order Events Webhooks
  slug: photon-order-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://photonhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.photon.health/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.photon.health/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.photon.health/reference/clinical-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.photon.health/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.photon.health/docs/authentication
- group: start
  title: ''
  type: SignUp
  url: https://photonhealth.com/onboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photon-Health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photonhealth
- group: operate
  title: ''
  type: StatusPage
  url: https://status.photon.health
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.photon.health
- group: company
  title: ''
  type: Blog
  url: https://photonhealth.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://photonhealth.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://photonhealth.com/terms
- group: auth
  title: ''
  type: Authentication
  url: authentication/photon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/photon-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/photon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/photon-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/photon-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/photon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/photon-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/photon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/photon-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/photon-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/photon-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/photon-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/photon-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/photon-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/photon-order-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: Photon Health is a United States prescription-infrastructure and e-prescribing (eRx) platform that lets digital-health companies embed prescribing, pharmacy selection, prescription routing, and fulfillment tracking into their clinical applications. Rather than an HL7 FHIR interface, Photon exposes a native GraphQL Clinical API - a single POST /graphql endpoint covering patients, prescriptions, orders, pharmacies, the medication/treatment catalog, drug-drug and drug-allergy screening, webhooks, and organization/user administration - plus a Patient Benefits API for pharmacy benefit checks and coverage. It also ships Photon Elements, prebuilt WebComponent UI for prescribing. The API is secured with OAuth2 client-credentials (Auth0) using machine-to-machine and user access tokens and prescription/order scopes; a sandbox runs on neutron.health. Photon serves prescribers and pharmacy-innovation partners including Amazon Pharmacy, Sesame, WeightWatchers, and Found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: photon-mcp.yml
  slug: photon-mcpyml
modified: '2026-07-24T18:00:00Z'
name: Photon
nav: Providers
network: true
overview: 'Photon publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, e-Prescribing, Pharmacy, and Prescription Routing.


  The Photon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Photon''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, engineering blog, sandbox, and 24 more developer resources.'
random_paper: 64
scopes:
- name: Photon Scopes
  scope_count: 6
  slug: photon-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 48.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Photon Authentication
  slug: photon-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Photon Domain Security
  slug: photon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: photon
tags:
- Healthcare
- United States
- e-Prescribing
- Pharmacy
- Prescription Routing
- GraphQL
- Clinical API
- Digital Health
- Benefit Check
- OAuth2
website: https://photonhealth.com/
---
