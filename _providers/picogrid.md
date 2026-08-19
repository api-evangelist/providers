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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'The Legion Platform HTTP API (v3, OpenAPI 3.1.0) for controlling and integrating data from unmanned and mission systems: entities and entity locations, feeds (message and file data) and feed definitio'
  name: Legion Platform API
  slug: legion-platform-api
artifact_total: 7
asyncapis:
- description: ''
  name: Picogrid Events Webhooks
  slug: picogrid-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/picogrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://picogrid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.picogrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.picogrid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.picogrid.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.picogrid.com/reference/start
- group: operate
  title: ''
  type: StatusPage
  url: https://status.picogrid.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.picogrid.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://picogrid.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/picogrid
- group: operate
  title: ''
  type: Support
  url: mailto:support@picogrid.com
- group: other
  title: ''
  type: Product
  url: https://picogrid.com/legion
- group: company
  title: ''
  type: Partners
  url: https://picogrid.com/partners
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/picogrid-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/picogrid-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/picogrid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/picogrid-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/picogrid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://picogrid.com/.well-known/security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/picogrid-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/picogrid-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/picogrid-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/picogrid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/picogrid-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/picogrid-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/picogrid-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/picogrid-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/picogrid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/picogrid-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/picogrid-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Picogrid is an El Segundo, California defense and public-safety technology company whose Legion platform is an API-first systems-integration layer that unifies fragmented sensors, unmanned systems, and mission assets across land, sea, air, and space into a single decision-ready picture. The Legion Platform API (v3, OpenAPI 3.1, OAuth 2.0 via Keycloak) lets operators and AI agents not only observe but command physical systems: registering entities, streaming and searching feed data, dispatching tasking commands over MQTT, managing tracks, video streams and WebRTC, fine-grained authorization, event subscriptions and notifications, and cross-Legion federation. Applications include base security, satellite operations, air defense, SIGINT interoperability, wildfire detection, and human-machine teaming. Backed by Bessemer Venture Partners and Initialized Capital.'
image: https://picogrid.com/
layout: provider
mcp_servers:
- description: ''
  name: picogrid-mcp.yml
  slug: picogrid-mcpyml
modified: '2026-07-20'
name: Picogrid
nav: Providers
network: true
overview: 'Picogrid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Defense, Public Safety, and Systems Integration.


  The Picogrid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Picogrid''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 24 more developer resources.'
random_paper: 104
scopes:
- name: Picogrid Scopes
  scope_count: 7
  slug: picogrid-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 34.6
  delta: -8.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 47.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 42.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/picogrid/refs/heads/main/screenshots/picogrid-2026-08-17T081219.png
security:
- kind: authentication
  name: Picogrid Authentication
  slug: picogrid-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 1 scheme
- kind: domain-security
  name: Picogrid Domain Security
  slug: picogrid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Picogrid Vulnerability Disclosure
  slug: picogrid-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: picogrid
tags:
- Company
- Data
- Defense
- Public Safety
- Systems Integration
- Sensors
- Unmanned Systems
- Command and Control
- Geospatial
- Situational Awareness
- OAuth
- Video Streaming
website: https://picogrid.com/
---
