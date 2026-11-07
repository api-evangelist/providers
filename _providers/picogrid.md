---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The Legion Platform HTTP API (v3, OpenAPI 3.1.0) for controlling and integrating data from unmanned and mission systems: entities and entity locations, feeds (message and file data) and feed definitio'
  name: Legion Platform API
  slug: legion-platform-api
artifact_total: 9
asyncapis:
- description: ''
  name: Picogrid Events Webhooks
  slug: picogrid-events-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/picogrid/security/picogrid-domain-security.yml
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
  href: https://artifacts.apis.io/picogrid/well-known/picogrid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/picogrid-security.txt
- group: agent
  href: https://artifacts.apis.io/picogrid/well-known/picogrid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/picogrid-well-known.yml
- group: auth
  href: https://artifacts.apis.io/picogrid/authentication/picogrid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/picogrid-authentication.yml
- group: auth
  href: https://artifacts.apis.io/picogrid/scopes/picogrid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/picogrid-scopes.yml
- group: auth
  href: https://artifacts.apis.io/picogrid/security/picogrid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/picogrid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://picogrid.com/.well-known/security.txt
- group: design
  href: https://artifacts.apis.io/picogrid/lifecycle/picogrid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/picogrid-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/picogrid/changelog/picogrid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/picogrid-changelog.yml
- group: design
  href: https://artifacts.apis.io/picogrid/errors/picogrid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/picogrid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/picogrid/conventions/picogrid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/picogrid-conventions.yml
- group: design
  href: https://artifacts.apis.io/picogrid/data-model/picogrid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/picogrid-data-model.yml
- group: design
  href: https://artifacts.apis.io/picogrid/asyncapi/picogrid-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/picogrid-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/picogrid/mcp/picogrid-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/picogrid-mcp.yml
- group: design
  href: https://artifacts.apis.io/picogrid/conformance/picogrid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/picogrid-conformance.yml
- group: build
  href: https://artifacts.apis.io/picogrid/packages/picogrid-packages.yml
  title: ''
  type: Packages
  url: packages/picogrid-packages.yml
- group: build
  href: https://artifacts.apis.io/picogrid/packages/picogrid-packages.yml
  title: ''
  type: SDKs
  url: packages/picogrid-packages.yml
- group: agent
  href: https://artifacts.apis.io/picogrid/llms/picogrid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/picogrid-llms.txt
- group: agent
  href: https://artifacts.apis.io/picogrid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Picogrid is an El Segundo, California defense and public-safety technology company whose Legion platform is an API-first systems-integration layer that unifies fragmented sensors, unmanned systems, and mission assets across land, sea, air, and space into a single decision-ready picture. The Legion Platform API (v3, OpenAPI 3.1, OAuth 2.0 via Keycloak) lets operators and AI agents not only observe but command physical systems: registering entities, streaming and searching feed data, dispatching tasking commands over MQTT, managing tracks, video streams and WebRTC, fine-grained authorization, event subscriptions and notifications, and cross-Legion federation. Applications include base security, satellite operations, air defense, SIGINT interoperability, wildfire detection, and human-machine teaming. Backed by Bessemer Venture Partners and Initialized Capital.'
image: https://picogrid.com/
layout: provider
modified: '2026-07-20'
name: Picogrid
nav: Providers
network: true
overview: 'Picogrid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Defense, Public Safety, and Systems Integration.


  The Picogrid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Picogrid''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 24 more developer resources.'
random_paper: 9
scopes:
- name: Picogrid Scopes
  scope_count: 7
  slug: picogrid-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 35.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/picogrid/picogrid-2026-08-17T081219.png
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
skill_count: 3
skills:
- name: Dispatch a tasking command to an entity
  slug: picogrid-dispatch-tasking-command
- name: Ingest and search Legion feed data
  slug: picogrid-ingest-and-search-feeds
- name: Subscribe to Legion events and receive notifications
  slug: picogrid-subscribe-to-events
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
- Authentication
website: https://picogrid.com/
---
