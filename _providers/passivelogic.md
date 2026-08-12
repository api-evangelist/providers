---
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 92
  human_in_the_loop: 6
  name: Passivelogic Agentic Access
  operation_count: 197
  slug: passivelogic-agentic-access
  summary_line: 197 operations · 92 acting · 6 human-in-the-loop
api_count: 18
apis:
- description: The Quantum API — a GraphQL query surface over the Quantum digital twin graph, letting clients query buildings, floors, zones, surfaces, equipment, components, properties and time-series data from the
  name: Quantum GraphQL API
  slug: quantum-graphql-api
- description: Routes related to user account management.
  name: PassiveLogic Account API
  slug: passivelogic-account-api
- description: The api API from PassiveLogic — 2 operation(s) for api.
  name: PassiveLogic API
  slug: passivelogic-api-api
- description: The app API from PassiveLogic — 20 operation(s) for app.
  name: PassiveLogic App API
  slug: passivelogic-app-api
- description: Routes related to AuthGroup management.
  name: PassiveLogic Auth Groups API
  slug: passivelogic-auth-groups-api
- description: Routes related to user auth
  name: PassiveLogic Authentication API
  slug: passivelogic-authentication-api
- description: Routes related to Binding management.
  name: PassiveLogic Bindings API
  slug: passivelogic-bindings-api
- description: The Default API from PassiveLogic — 1 operation(s) for default.
  name: PassiveLogic Default API
  slug: passivelogic-default-api
- description: Routes related to exporting objects and history
  name: PassiveLogic Export API
  slug: passivelogic-export-api
- description: Routes related to the GraphQL API
  name: PassiveLogic Graph QL API
  slug: passivelogic-graphql-api
- description: Routes related to server health checks
  name: PassiveLogic Health API
  slug: passivelogic-health-api
- description: Routes related to Image management
  name: PassiveLogic Images API
  slug: passivelogic-images-api
- description: Routes related to organization management
  name: PassiveLogic Organization API
  slug: passivelogic-organization-api
- description: Routes related to PassiveLogic devices
  name: PassiveLogic PassiveLogic Device API
  slug: passivelogic-passivelogic-device-api
- description: Routes related to quantum sync
  name: PassiveLogic Quantum Sync API
  slug: passivelogic-quantum-sync-api
- description: Routes related to site objects
  name: PassiveLogic Site API
  slug: passivelogic-site-api
- description: The tunnel API from PassiveLogic — 2 operation(s) for tunnel.
  name: PassiveLogic Tunnel API
  slug: passivelogic-tunnel-api
- description: Routes related to server metadata/utility
  name: PassiveLogic Utility API
  slug: passivelogic-utility-api
artifact_total: 23
asyncapis:
- description: ''
  name: Passivelogic Quantum Events
  slug: passivelogic-quantum-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/passivelogic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passivelogic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://passivelogic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://quantumalliance.org/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://passivelogic.com/app/swagger/
- group: operate
  title: ''
  type: Support
  url: https://support.passivelogic.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://passivelogic.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PassiveLogic
- group: start
  title: ''
  type: SignUp
  url: https://passivelogic.com/app/login/signUp
- group: start
  title: ''
  type: Login
  url: https://passivelogic.com/app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://passivelogic.com/footer/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://passivelogic.com/footer/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.passivelogic.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/passivelogic-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/passivelogic-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/passivelogic-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/passivelogic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/passivelogic-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/passivelogic-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/passivelogic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/passivelogic-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/passivelogic-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/passivelogic-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/passivelogic-quantum-object-types.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/passivelogic-rest-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/passivelogic-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: PassiveLogic builds a physics-based autonomy platform for buildings and industrial systems — the Hive, Hive Mini and Cell edge controllers, the Sense wireless sensor line, and the Autonomy Suite design/operate applications (Blueprint, Creator, Lens, Live, Portfolio, Qortex). Its software core is Quantum, an open physics-based digital twin ontology and data model for autonomous systems, developed with the U.S. Department of Energy and the Quantum Alliance consortium. The Quantum API is exposed as a GraphQL query and subscription surface over the digital twin graph, sat behind a documented HTTP REST API covering authentication, API-key issuance, organizations, auth groups, images, bindings, device registration, CSV property-history export and QuantumSync WebSocket data sync. Authentication is handled by an external Keycloak identity provider (OpenID Connect) with JWT, XSRF-protected session tokens and long-lived PL API keys.
image: https://framerusercontent.com/assets/L5gk3b8Fq6q5IinWJOFtKMlivU.png
layout: provider
modified: '2026-08-04'
name: PassiveLogic
nav: Providers
network: true
overview: 'PassiveLogic publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Account API, App API, and 15 more. Tagged areas include Company, digital-twin, building-automation, hvac, and smart-buildings.


  The PassiveLogic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PassiveLogic''s developer surface includes documentation, API reference, support, engineering blog, signup flow, changelog, sandbox, and 20 more developer resources.'
random_paper: 13
scopes:
- name: Passivelogic Scopes
  scope_count: 13
  slug: passivelogic-scopes
  summary_line: 13 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 46.6
  delta: -0.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.1
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 14.1
    operational_transparency: 36.8
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passivelogic/refs/heads/main/screenshots/passivelogic-2026-08-07T191536.png
security:
- kind: authentication
  name: Passivelogic Authentication
  slug: passivelogic-authentication
  summary_line: apiKey/http/openIdConnect · 5 schemes
- kind: domain-security
  name: Passivelogic Domain Security
  slug: passivelogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: passivelogic
tags:
- Company
- digital-twin
- building-automation
- hvac
- smart-buildings
- autonomous-systems
- graphql
- ontology
- iot
- edge-computing
- physical-ai
- energy
website: https://passivelogic.com/
---
