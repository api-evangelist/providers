---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The GeniusAPI Suite is Claim Genius''s REST integration layer over its AI vehicle-inspection products. Documented flow: generate a JWT via /api/auth/token using an API ID and secret, upload JPG/PNG/MP4'
  name: Claim Genius GeniusAPI Suite
  slug: geniusapi-suite
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://claimgenius.com/
- group: operate
  title: ''
  type: Support
  url: https://claimgenius.com/contact
- group: company
  title: ''
  type: Blog
  url: https://claimgenius.com/claim-genius-blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claimgenius.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claimgenius.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://claimgenius.com/geniusapi
- group: auth
  title: ''
  type: Authentication
  url: authentication/claim-genius-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/claim-genius-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/claim-genius-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/claim-genius-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/claim-genius-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/claim-genius-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/claim-genius-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/claim-genius-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: The GeniusAPI page names real endpoints (/api/auth/token, /api/file/upload, /api/pipelines/{pipelineName}, /api/pipeline/requests/{requestId}) and advertises an OpenAPI 3.0 spec, but the only route to the reference is "Contact us at contactus@claimgenius.com to request developer access and documentation" — and the developer hub Claim Genius has actually provisioned, claimgenius.readme.io, answers HTTP 401 with a password form (a non-existent ReadMe subdomain returns 404, so the hub is real and deliberately closed).
  evidence:
  - status: 401
    url: https://claimgenius.readme.io/
  - status: 200
    url: https://claimgenius.com/geniusapi
  - status: 404
    url: https://api.claimgenius.com/openapi.json
  - status: 404
    url: https://api.claimgenius.com/swagger.json
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: Claim Genius is an AI vehicle-inspection and automated damage-assessment company serving auto insurance claims, underwriting, dealerships, salvage, lease and rental, fleet and collision repair. Its GeniusINSPECT engine converts vehicle photos and video into structured, decision-ready data — per-part damage classification (scratch, dent, tear, glass, wheel), repair-versus-replace decisions, labor and paint hours, OEM part pricing, repairability status and total-loss probability. The capabilities are packaged as products (GeniusINSPECT for Claims, GeniusINSPECT for Underwriting, GeniusPrepost, GeniusOPS) and exposed to integrators through the GeniusAPI Suite, a JWT-authenticated REST API with asynchronous pipeline processing. The company has operated across the US, EU and Asia since 2018.
image: https://claimgenius.com/assets/logo/CG-AI-logo-trans-512.png
layout: provider
modified: '2026-08-09'
name: Claim Genius
nav: Providers
network: true
overview: 'Claim Genius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Insurance Claims, Insurance Underwriting, Artificial Intelligence, and Computer-Vision.


  Claim Genius'' developer surface includes support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Claim Genius Authentication
  slug: claim-genius-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Claim Genius Domain Security
  slug: claim-genius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: claim-genius
tags:
- Insurance
- Insurance Claims
- Insurance Underwriting
- Artificial Intelligence
- Computer-Vision
- Vehicle Inspection
- Automotive
- Claims Automation
- Damage Assessment
- Insurtech
website: https://claimgenius.com/
---
