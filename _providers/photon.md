---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Photon Agentic Access
  operation_count: 0
  slug: photon-agentic-access
  summary_line: 0 operations
api_count: 3
apis:
- description: Photon's native GraphQL Clinical API for managing patients, prescriptions, orders, pharmacies, the treatment/medication catalog, drug-drug and drug-allergy interaction screening, webhooks, and organiz
  name: Photon Clinical API
  slug: photon-clinical-api
- description: 'Photon''s GraphQL Patient Benefits API for managing patient benefits and enabling pharmacy benefit checks (coverage options, copay, and formulary) during the prescribing workflow. Served over the same '
  name: Photon Patient Benefits API
  slug: photon-patient-benefits-api
- description: 'Photon''s public website API, covering the onboarding funnel and newsletter signup: create or resume an onboarding session, save path-specific onboarding answers, submit a completed onboarding flow, an'
  name: Photon Website API
  slug: photon-website-api
artifact_total: 12
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/photon-website-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/photon-website-api-overlay.yaml
- group: other
  title: ''
  type: APICatalog
  url: well-known/photon-api-catalog.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/photon-agentic-access.yml
- group: auth
  title: ''
  type: Compliance
  url: security/photon-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/photon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/photon-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@photon.health
- group: start
  title: ''
  type: Login
  url: https://app.photon.health/login
- group: operate
  title: ''
  type: FAQ
  url: https://photonhealth.com/faq
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/photon-docs-llms.txt
created: '2026-07-24'
description: Photon Health is a United States prescription-infrastructure and e-prescribing (eRx) platform that lets digital-health companies embed prescribing, pharmacy selection, prescription routing, and fulfillment tracking into their clinical applications. Rather than an HL7 FHIR interface, Photon exposes a native GraphQL Clinical API - a single POST /graphql endpoint covering patients, prescriptions, orders, pharmacies, the medication/treatment catalog, drug-drug and drug-allergy screening, webhooks, and organization/user administration - plus a Patient Benefits API for pharmacy benefit checks and coverage. It also ships Photon Elements, prebuilt WebComponent UI for prescribing. The API is secured with OAuth2 client-credentials (Auth0) using machine-to-machine and user access tokens and prescription/order scopes; a sandbox runs on neutron.health. Photon serves prescribers and pharmacy-innovation partners including Amazon Pharmacy, Sesame, WeightWatchers, and Found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Photon MCP Server
  slug: photon-mcp-server
modified: '2026-07-24T18:00:00Z'
name: Photon
nav: Providers
network: true
overview: 'Photon publishes 1 API on the [APIs.io](https://apis.io/) network: Website API. Tagged areas include Healthcare, United States, e-Prescribing, Pharmacy, and Prescription Routing.


  The Photon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Photon''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, engineering blog, sandbox, and 35 more developer resources.'
plans:
- name: Photon Plans Pricing
  plan_count: 0
  slug: photon-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Photon Rate Limits
  slug: photon-rate-limits
scopes:
- name: Photon Scopes
  scope_count: 6
  slug: photon-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 59.2
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 60.5
    developer_ergonomics: 53.0
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 59.2
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/photon/refs/heads/main/screenshots/photon-2026-08-17T081212.png
security:
- kind: authentication
  name: Photon Authentication
  slug: photon-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Photon Domain Security
  slug: photon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Photon Trust Center
  slug: photon-trust-center
  summary_line: SOC 2, HIPAA
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
- Authentication
website: https://photonhealth.com/
---
