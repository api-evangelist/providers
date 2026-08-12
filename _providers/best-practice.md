---
access_model:
  confidence: high
  label: Partner-gated · Halo Cloud subscription + practice pairing
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Best Practice Agentic Access
  operation_count: 29
  slug: best-practice-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 3
apis:
- description: The integrator-facing Halo Cloud API from Best Practice's Halo Connect platform. Lets approved partners query Bp Premier practice data by four means - Sites (retrieve site metadata and onboarding info
  name: Halo Cloud API for Integrators
  slug: halo-cloud-integrator-api
- description: The desktop-application-facing Halo Cloud API from Halo Connect. Provides a token endpoint plus SQL Passthrough and FHIR query access for locally installed applications integrating with Bp Premier. Op
  name: Halo Cloud API for Desktop Applications
  slug: halo-cloud-desktop-api
- description: The HL7 FHIR API for Best Practice Bp Premier, delivered through Halo Connect. Built to the AU Base 4.1.0 implementation guide, falling back to FHIR R4 (4.0.1) where needed. Resources are served under
  name: FHIR API for Bp Premier
  slug: fhir-api-bp-premier
artifact_total: 8
asyncapis:
- description: ''
  name: Best Practice Webhooks
  slug: best-practice-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/best-practice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/best-practice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/best-practice-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bpsoftware.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.haloconnect.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.haloconnect.io/halo-cloud/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.haloconnect.io/api-reference/integrator-openapi.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.haloconnect.io/halo-cloud/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://haloconnect.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.haloconnect.io/
- group: operate
  title: ''
  type: Support
  url: https://bpsoftware.net/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bpsoftware.net/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bpsoftware.net/privacy-policy/
- group: design
  title: ''
  type: Conventions
  url: conventions/best-practice-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/best-practice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/best-practice-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/best-practice-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/best-practice-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/best-practice-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/best-practice-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/best-practice-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/best-practice-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/best-practice-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/best-practice-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/best-practice-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/best-practice-integrator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/best-practice-desktop-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: Best Practice Software is an Australian clinical and practice-management software company, headquartered in Bundaberg, Queensland, and one half of the Australian GP-software duopoly (alongside MedicalDirector). Its flagship products - Bp Premier (general practice), Bp VIP.net (specialist and allied), and Bp Allied - run in thousands of Australian medical practices. Best Practice's programmatic surface is delivered through Halo Connect (Halo Cloud / Halo Link), a FHIR-based integration platform that lets approved partners query practice data over a modern API instead of the legacy SQL database. The FHIR API for Bp Premier is built to the AU Base 4.1.0 implementation guide, falling back to HL7 FHIR R4 (4.0.1), and exposes resources such as Patient, Appointment, Slot (Find Free Slots) and a Patient $summary document. Halo Cloud also offers SQL Passthrough and Registered Queries for structured practice data. Access is gated - integrators require a Halo Cloud subscription plus per-practice
  pairing and PMS-managed database credentials, authenticated with an Azure API Management subscription key (desktop apps additionally use a bearer JWT and device id). This is not a self-serve public API; it is a partner-onboarded, standards-aligned interoperability layer for the Australian primary-care market.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: best-practice-mcp.yml
  slug: best-practice-mcpyml
modified: '2026-07-24'
name: Best Practice Software
nav: Providers
network: true
overview: 'Best Practice Software publishes 3 APIs on the [APIs.io](https://apis.io/) network: Halo Cloud API for Integrators, Halo Cloud API for Desktop Applications, and FHIR API for Bp Premier. Tagged areas include Healthcare, Australia, EHR, EMR, and FHIR.


  The Best Practice Software catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Best Practice Software''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, sandbox, and 21 more developer resources.'
random_paper: 42
score:
  band: developing
  composite: 48.5
  delta: -2.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 71.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/best-practice/refs/heads/main/screenshots/best-practice-2026-07-25T202754.png
security:
- kind: authentication
  name: Best Practice Authentication
  slug: best-practice-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Best Practice Domain Security
  slug: best-practice-domain-security
  summary_line: TLSv1.3 · DMARC
slug: best-practice
tags:
- Healthcare
- Australia
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- AU Base
- Practice Management
- General Practice
- Appointments
- Scheduling
website: https://bpsoftware.net/
---
