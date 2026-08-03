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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: The Session API from Zamna — 9 operation(s) for session.
  name: Zamna Session API
  slug: zamna-session-api
- description: The Start API from Zamna — 1 operation(s) for start.
  name: Zamna Start API
  slug: zamna-start-api
- description: The Start With Booking Id And Surname API from Zamna — 1 operation(s) for start with booking id and surname.
  name: Zamna Start With Booking Id And Surname API
  slug: zamna-start-with-booking-id-and-surname-api
- description: The Start2 API from Zamna — 1 operation(s) for start2.
  name: Zamna Start2 API
  slug: zamna-start2-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zamna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zamna-authentication.yml
- group: company
  title: ''
  type: Website
  url: http://zamna.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.zamna.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.zamna.com/
- group: docs
  title: ''
  type: APIReference
  url: https://paxcheck-app-dev.staging.zamna.com/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.zamna.com/start/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zamna-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zamna-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zamna-paxcheck-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/zamna-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zamna-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zamna-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zamna-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zamna-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/zamna-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zamna-data-model.yml
created: '2026-07-17'
description: Zamna is a GDPR-compliant digital identity and passenger-data verification platform for the aviation and travel industry, used by airlines, airports, ground handlers and governments to verify passport, visa and health documents before a traveler reaches the airport. Its Ready To Fly (PaxCheck) API stitches passenger sessions, document recognition and consent capture into airline systems, while the Checklist API resolves live travel rules into localized, per-passenger requirements and a pluggable WebView drives the MMB/OLCI flows. Zamna has verified over 60 million travel identities across 179+ countries and integrates with airline PSS/DCS platforms such as Amadeus Altea, Navitaire and Sabre.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zamna.png
layout: provider
mcp_servers:
- description: ''
  name: zamna-mcp.yml
  slug: zamna-mcpyml
modified: '2026-07-21'
name: Zamna
nav: Providers
network: true
overview: 'Zamna publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Session API, Start API, Start With Booking Id And Surname API, and 1 more. Tagged areas include Company, Aviation, Travel, Identity Verification, and Digital Identity.


  Zamna''s developer surface includes authentication, documentation, API reference, getting-started guide, sandbox, and 13 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 46.9
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Zamna Authentication
  slug: zamna-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zamna Domain Security
  slug: zamna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zamna
tags:
- Company
- Aviation
- Travel
- Identity Verification
- Digital Identity
- Passenger Processing
- Airlines
- Border Security
- Document Verification
- KYC
website: http://zamna.com
---
