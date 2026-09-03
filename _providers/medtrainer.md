---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.medtrainer.com
  baseurl_source: declared
  description: Public department lookup endpoints
  name: MedTrainer Departments API
  slug: medtrainer-departments-api
- baseURL: https://api.medtrainer.com
  baseurl_source: declared
  description: Public division lookup and mutation endpoints
  name: MedTrainer Divisions API
  slug: medtrainer-divisions-api
- baseURL: https://api.medtrainer.com
  baseurl_source: declared
  description: Public location lookup and mutation endpoints
  name: MedTrainer Locations API
  slug: medtrainer-locations-api
- baseURL: https://api.medtrainer.com
  baseurl_source: declared
  description: Public position lookup endpoints
  name: MedTrainer Positions API
  slug: medtrainer-positions-api
- baseURL: https://api.medtrainer.com
  baseurl_source: declared
  description: Public practitioner category lookup endpoints
  name: MedTrainer Practitioner Categories API
  slug: medtrainer-practitioner-categories-api
- baseURL: https://api.medtrainer.com
  baseurl_source: declared
  description: Public practitioner lookup, search, and mutation endpoints
  name: MedTrainer Practitioners API
  slug: medtrainer-practitioners-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medtrainer-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://medtrainer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.medtrainer.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.medtrainer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.medtrainer.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.medtrainer.com/docs#section/Getting-started
- group: company
  title: ''
  type: Blog
  url: https://medtrainer.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://medtrainer.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.medtrainer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://medtrainer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://medtrainer.com/demo/
- group: start
  title: ''
  type: Login
  url: https://medtrainer.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medtrainer.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medtrainer.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://medtrainer.com/security/
- group: auth
  title: ''
  type: Compliance
  url: conformance/medtrainer-conformance.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/medtrainer-public-api-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/medtrainer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/medtrainer-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medtrainer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medtrainer-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medtrainer-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medtrainer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medtrainer-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medtrainer-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/medtrainer-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/medtrainer-public-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medtrainer-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/medtrainer-auth-openid-configuration.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medtrainer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/medtrainer-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medtrainer-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medtrainer-domain-security.yml
created: '2026-08-25'
description: 'MedTrainer is a healthcare workforce compliance software company that consolidates learning management, credentialing and provider enrollment, document and policy management, incident reporting, safety plans, contract management and exclusion/sanction monitoring into a single all-in-one platform for medical practices, ambulatory surgery centers, urgent care, behavioral health, dental groups, community health centers and long-term care organizations. The company publishes a MedTrainer Public API at api.medtrainer.com, documented with an OpenAPI 3.1 definition rendered through Redoc, that lets external integrations search and manage the core provider directory — locations, divisions, departments, positions, practitioner categories and practitioners. The API is notable for being FHIR-aligned: resource payloads use HL7 FHIR shapes and the application/fhir+json media type, searches return FHIR Bundle envelopes with FHIR search parameters (_count, _page, _elements), and every error
  is returned as a FHIR OperationOutcome. Access is customer-gated behind an API key generated from the platform Organization settings, and the wider platform authenticates against an Auth0-backed OpenID Connect provider at auth.medtrainer.com.'
image: https://medtrainer.com/wp-content/uploads/2023/04/MedTrainerLogo.svg
layout: provider
mcp_servers:
- description: ''
  name: MedTrainer MCP Server (WordPress MCP Adapter)
  slug: medtrainer-mcp-server-wordpress-mcp-adapter
modified: '2026-08-25'
name: MedTrainer
nav: Providers
network: true
overview: 'MedTrainer publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Departments API, Divisions API, Locations API, and 3 more. Tagged areas include Company, Healthcare, Compliance, Credentialing, and Learning Management.


  MedTrainer''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Medtrainer Plans Pricing
  plan_count: 3
  slug: medtrainer-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Medtrainer Rate Limits
  slug: medtrainer-rate-limits
scopes:
- name: Medtrainer Scopes
  scope_count: 0
  slug: medtrainer-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 60.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medtrainer/refs/heads/main/screenshots/medtrainer-2026-09-02T150458.png
security:
- kind: authentication
  name: Medtrainer Authentication
  slug: medtrainer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Medtrainer Domain Security
  slug: medtrainer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medtrainer Vulnerability Disclosure
  slug: medtrainer-vulnerability-disclosure
  summary_line: disclosure policy published
slug: medtrainer
tags:
- Company
- Healthcare
- Compliance
- Credentialing
- Learning Management
- Provider Directory
- FHIR
- HL7
- Training
- Risk Management
- Software-as-a-Service
website: https://medtrainer.com/
---
