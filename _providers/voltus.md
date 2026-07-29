---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 2
  name: Voltus Agentic Access
  operation_count: 10
  slug: voltus-agentic-access
  summary_line: 10 operations · 5 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: Grid dispatch events for enrolled sites — list dispatches, retrieve a single dispatch by ID, and create a test dispatch. Documented operations are GET /dispatches ("Returns a list of dispatches."), PO
  name: Voltus Dispatches API
  slug: voltus-dispatches-api
- description: 'Read the sites (facilities) enrolled with Voltus under the calling account, with their meters. The single documented operation is GET /sites ("Returns a list of your sites."), returning site name, id '
  name: Voltus Sites API
  slug: voltus-sites-api
- description: Submit and retrieve interval energy telemetry for enrolled sites. Documented operations are POST /telemetry, POST /telemetry/controllable-load ("Posts controllable load.") and GET /telemetry/kw ("Retu
  name: Voltus Telemetry API
  slug: voltus-telemetry-api
- description: Register HTTP callbacks so Voltus can push dispatch notifications instead of the partner polling. Documented operations are GET /webhooks ("Returns a list of all webhooks that have been created."), PO
  name: Voltus Webhooks API
  slug: voltus-webhooks-api
- description: Standards-based alternative to the REST dispatch integration. Voltus states it "supports OpenADR2.0a via Simple HTTP (PULL)" and that "Voltus provides a VTN, and our partners run one or more VENs". Pa
  name: Voltus OpenADR 2.0a VTN
  slug: voltus-openadr-vtn
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: 'The core Voltus demand-response loop: resolve your enrolled sites, poll for dispatches, then read the individual dispatch to drive per-site curtailment commitments. Runs end-to-end against the public '
  name: Poll Voltus dispatches and curtail enrolled sites
  slug: voltus-poll-dispatches-and-curtail
- description: 'Move from polling to push: register an HTTPS callback for dispatch.create and dispatch.update, confirm it is listed, then remove it. Delete is permanent.'
  name: Register a Voltus dispatch webhook and verify it
  slug: voltus-register-webhook-and-verify
- description: Submit interval telemetry and controllable load for an enrolled site, then read interval kW back within Voltus's documented limits (10 sites, 90 days, 10,000 points per site).
  name: Report Voltus telemetry and read it back
  slug: voltus-report-and-read-telemetry
artifact_total: 18
asyncapis:
- description: ''
  name: Voltus Webhooks
  slug: voltus-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/voltus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voltus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voltus-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.voltus.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.voltus.co/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.voltus.co/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.voltus.co/docs/openapi/voltus-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.voltus.co/docs/tutorials/first-api-request-get-sites
- group: learn
  title: ''
  type: Tutorials
  url: https://api.voltus.co/docs/tutorials/
- group: start
  title: ''
  type: Sandbox
  url: https://api.voltus.co/docs/concepts/public-credentials
- group: auth
  title: ''
  type: Authentication
  url: https://api.voltus.co/docs/openapi/voltus-api-reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.voltus.co/docs/changelog
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@voltus.co
- group: company
  title: ''
  type: Blog
  url: https://www.voltus.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voltus.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voltus.co/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voltus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voltus-inc./
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/voltus-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/voltus-openapi-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/voltus-examples.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voltus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voltus-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voltus-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/voltus-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voltus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://api.voltus.co/docs/changelog/deprecated-field-drop-by
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/voltus-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voltus-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/voltus-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voltus-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/voltus-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voltus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/voltusdev/voltus-api-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voltusdev
- group: start
  title: ''
  type: Login
  url: https://cashdash.voltus.co/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/voltusinc
created: '2026-07-27'
description: 'Voltus is a United States virtual power plant (VPP) operator and distributed energy resource (DER) technology platform, headquartered in San Francisco, California, that aggregates commercial, industrial, residential and transportation loads and batteries into wholesale electricity markets across all of North America''s organized markets (AESO, CAISO, ERCOT, IESO, ISO-NE, MISO, NYISO, PJM, SPP). It sits in the demand-response and flexibility layer of the energy value chain: it is not a utility and not a metering data holder, so no Green Button, Consumer Data Right or smart-meter data mandate applies to it — mandate regime is honestly none. Its API posture is unusually good for the sector and unusually split. Voltus runs a genuine public developer portal at api.voltus.co/docs (Docusaurus, no login) with concepts, tutorials, an OpenAPI-generated reference and a changelog, plus a fully anonymous sandbox at sandbox.voltus.co that answers real HTTP requests with the documented public
  key "X-Voltus-API-Key: secret" — a developer can call it before signing anything. Production, however, is partner-only: api.voltus.co/2022-04-15 returns 401 Permission denied to the sandbox key, and real access requires a commercial partnership plus a signed Letter of Authorization per site. Site telemetry and dispatch control are exposed to partners over that account-scoped REST API and over OpenADR 2.0a Simple HTTP PULL with mutual TLS; Voltus publishes no open grid or market data of its own, so consumer/site energy data is available under contract while market data is closed. No downloadable OpenAPI or Swagger document is served — /openapi.json, /swagger.json and /openapi3.yaml all 404 — but the portal is built with the Docusaurus OpenAPI plugin, and the real operation objects (parameters, request bodies, response schemas, examples) were recovered verbatim from the published build and assembled into openapi/voltus-openapi.yml: 10 operations across 8 paths.'
examples:
- key_count: 2
  name: Voltus Dispatch Webhook Payload
  slug: voltus-dispatch-webhook-payload
- key_count: 3
  name: Voltus Get Dispatches 200
  slug: voltus-get-dispatches-200
- key_count: 3
  name: Voltus Get Sites 200
  slug: voltus-get-sites-200
- key_count: 3
  name: Voltus Get Webhooks 200
  slug: voltus-get-webhooks-200
image: https://api.voltus.co/img/voltus.png
layout: provider
modified: '2026-07-27'
name: Voltus
nav: Providers
network: true
overview: 'Voltus publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Dispatches API, Sites API, Telemetry API, and 1 more. Tagged areas include Energy, United States, Electricity, Demand Response, and Virtual Power Plant.


  The Voltus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Voltus'' developer surface includes authentication, documentation, API reference, getting-started guide, sandbox, changelog, support, and 32 more developer resources.'
random_paper: 69
rate_limits:
- limit_count: 0
  name: Voltus Rate Limits
  slug: voltus-rate-limits
score:
  band: developing
  composite: 50.0
  delta: 0.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.9
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Voltus Authentication
  slug: voltus-authentication
  summary_line: apiKey/mutualTLS · 2 schemes
- kind: domain-security
  name: Voltus Domain Security
  slug: voltus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voltus
tags:
- Energy
- United States
- Electricity
- Demand Response
- Virtual Power Plant
- DER
- Grid
- Energy Markets
- Flexibility
- Energy Storage
- OpenADR
- Telemetry
website: https://www.voltus.co/
---
