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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Butlr GraphQL API manages spatial assets and their configuration across the organization hierarchy - sites, buildings, floors, rooms, zones, hives, and sensors - plus asset tags and self-service w
  name: Butlr GraphQL API
  slug: butlr-graphql-api
- description: The Butlr Reporting API is a RESTful, time-series occupancy API for historical space-utilization analysis. A POST query against a windowing/filter body returns aggregated floor, room, and zone occupan
  name: Butlr Reporting API
  slug: butlr-reporting-api
artifact_total: 9
asyncapis:
- description: API Evangelist generated AsyncAPI rendering of Butlr's documented real-time occupancy webhook events. Butlr does not publish an AsyncAPI document; this file is a faithful reconstruction from https://d
  name: Butlr Real-Time Occupancy Webhooks
  slug: butlr-events-asyncapi
- description: ''
  name: Butlr Webhooks
  slug: butlr-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.butlr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.butlr.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.butlr.io
- group: docs
  title: ''
  type: APIReference
  url: https://graphql-docs.butlr.io/graphql/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.butlr.io/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.butlr.io
- group: company
  title: ''
  type: Blog
  url: https://www.butlr.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/butlrtechnologies
- group: start
  title: ''
  type: SignUp
  url: https://app.butlr.io
- group: start
  title: ''
  type: Login
  url: https://app.butlr.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.butlr.io/legal/tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.butlr.io/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/butlr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/butlr-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/butlr-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/butlr-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/butlr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/butlr-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/butlr-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/butlr-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/butlr-events-asyncapi.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/butlr-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/butlr-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/butlr-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/butlr-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/butlr-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/butlr-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/butlr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/butlr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/butlr-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Butlr is an AI platform for privacy-first, heat-based (thermal) occupancy sensing that turns anonymous people-sensing into real-time space-utilization insight for workplaces, senior living, higher education, retail, and smart buildings. Its camera-free thermal sensors capture no personally identifiable information while powering occupancy, traffic, presence-time, and heatmap analytics. Butlr exposes an API-first platform: a GraphQL asset-management API for sites, buildings, floors, rooms, zones, hives, and sensors; a RESTful Reporting API (v3) for historical time-series occupancy; real-time webhooks for detections, traffic, and occupancy events; and an official Model Context Protocol (MCP) server for agent access. The company reports 30,000+ deployed sensors generating a billion data points daily across 100M+ square feet in 22 countries.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/butlr.png
layout: provider
mcp_servers:
- description: ''
  name: Butlr MCP Server
  slug: butlr-mcp-server
modified: '2026-07-18'
name: Butlr
nav: Providers
network: true
overview: 'Butlr publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, Occupancy, People Sensing, and Smart Buildings.


  The Butlr catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Butlr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 7
scopes:
- name: Butlr Scopes
  scope_count: 12
  slug: butlr-scopes
  summary_line: 12 scopes
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 43.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/butlr/refs/heads/main/screenshots/butlr-2026-07-25T204120.png
security:
- kind: authentication
  name: Butlr Authentication
  slug: butlr-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Butlr Domain Security
  slug: butlr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Butlr Vulnerability Disclosure
  slug: butlr-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: butlr
tags:
- Company
- Sensors
- Occupancy
- People Sensing
- Smart Buildings
- Spatial Intelligence
- IoT
- GraphQL
- Webhook
- Real-Estate
website: https://www.butlr.com
---
