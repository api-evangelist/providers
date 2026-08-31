---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Genability Agentic Access
  operation_count: 33
  slug: genability-agentic-access
  summary_line: 33 operations · 3 acting
api_count: 1
apis:
- description: The GET API from Genability — 1 operation(s) for get.
  name: Genability GET API
  slug: genability-get-api
- description: The Rest API from Genability — 32 operation(s) for rest.
  name: Genability Rest API
  slug: genability-rest-api
artifact_total: 8
collections:
- collection_type: open
  name: signal
  slug: open-genability-signal
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/genability-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genability-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genability-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genability-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/genability-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/genability-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/genability-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genability-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/genability-signal-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/genability-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/genability-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/genability-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcadia.com
- group: design
  title: ''
  type: Conventions
  url: conventions/genability-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/genability-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.arcadia.com/v2022-12-21-Signal/changelog
- group: start
  title: ''
  type: Sandbox
  url: sandbox/genability-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/genability-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/genability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.arcadia.com/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://genability.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arcadia.com/v2022-12-21-Signal/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/welcome-to-signal
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arcadia.com/v2022-12-21-Signal/reference/api-basics
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/quick-start
- group: auth
  title: ''
  type: Authentication
  url: https://docs.arcadia.com/v2022-12-21-Signal/reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/rate-limit-best-practices
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.arcadia.com/v2022-12-21-Signal/llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://dash.genability.com/signup
- group: start
  title: ''
  type: Login
  url: https://dash.genability.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Genability
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Genability/genability-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Genability/genability-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Genability/Genability-PHP-Library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genability
- group: operate
  title: ''
  type: Support
  url: https://www.arcadia.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.arcadia.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform-legal.arcadia.com/#platform-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform-legal.arcadia.com/#arcadia-privacy-policy
created: '2026-07-27'
description: 'Genability is a United States energy-data platform, based in San Francisco and now part of Arcadia, that sells programmatic access to North American electricity tariff data and a bill-calculation engine. Its Signal API — served from api.genability.com and documented as "Arcadia Platform - Signal" — covers electricity utilities, tariffs, territories, seasons, time-of-use definitions, calendars, utility taxes and typical-usage baselines across the USA, Canada and Mexico, plus on-demand and mass cost calculations used for solar savings analysis, storage dispatch, EV charging economics, procurement and bill auditing. Genability sits in the private, commercial layer of the energy value chain: it is not a utility, not a retailer and not a designated data holder under any consumer-energy-data mandate, so no Green Button, ESPI, CDR or other energy data standard is referenced anywhere in its documentation. Its API posture is honestly "self-serve but entirely closed data": a developer
  can sign up at dash.genability.com in minutes, but every endpoint — including the ones pathed /rest/public/ — returns 401 without an appId/appKey, so none of this tariff or market reference data is openly published, and Genability exposes no individual customer''s usage or billing data at all (that consumer-data surface lives in Arcadia''s separate Plug/Arc API).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Genability MCP Server
  slug: genability-mcp-server
modified: '2026-07-27'
name: Genability
nav: Providers
network: true
overview: 'Genability publishes 2 APIs on the [APIs.io](https://apis.io/) network: GET API and Rest API. Tagged areas include Energy, United States, Utilities, Electricity, and Tariffs.


  Genability''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 33 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.9
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 47.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genability/refs/heads/main/screenshots/genability-2026-08-07T165554.png
security:
- kind: authentication
  name: Genability Authentication
  slug: genability-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Genability Domain Security
  slug: genability-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Genability Vulnerability Disclosure
  slug: genability-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: genability
tags:
- Energy
- United States
- Utilities
- Electricity
- Tariffs
- Energy Rates
- Rate Calculation
- Energy Data Platform
- Solar
- Grid
website: https://genability.com/
---
