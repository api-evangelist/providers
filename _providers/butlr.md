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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The Butlr GraphQL API manages spatial assets and their configuration across the organization hierarchy - sites, buildings, floors, rooms, zones, hives, and sensors - plus asset tags and self-service w
  name: Butlr GraphQL API
  slug: butlr-graphql-api
- description: The Butlr Reporting API is a RESTful, time-series occupancy API for historical space-utilization analysis. A POST query against a windowing/filter body returns aggregated floor, room, and zone occupan
  name: Butlr Reporting API
  slug: butlr-reporting-api
artifact_total: 12
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
  type: Blog
  url: https://www.butlr.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.butlr.com/blog/rss.xml
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
  href: https://artifacts.apis.io/butlr/authentication/butlr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/butlr-authentication.yml
- group: auth
  href: https://artifacts.apis.io/butlr/scopes/butlr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/butlr-scopes.yml
- group: agent
  href: https://artifacts.apis.io/butlr/mcp/butlr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/butlr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/butlr/llms/butlr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/butlr-llms.txt
- group: build
  href: https://artifacts.apis.io/butlr/packages/butlr-packages.yml
  title: ''
  type: Packages
  url: packages/butlr-packages.yml
- group: build
  href: https://artifacts.apis.io/butlr/packages/butlr-packages.yml
  title: ''
  type: SDKs
  url: packages/butlr-packages.yml
- group: agent
  href: https://artifacts.apis.io/butlr/well-known/butlr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/butlr-well-known.yml
- group: design
  href: https://artifacts.apis.io/butlr/asyncapi/butlr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/butlr-webhooks.yml
- group: docs
  href: https://artifacts.apis.io/butlr/asyncapi/butlr-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/butlr-events-asyncapi.yml
- group: operate
  href: https://artifacts.apis.io/butlr/changelog/butlr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/butlr-changelog.yml
- group: design
  href: https://artifacts.apis.io/butlr/lifecycle/butlr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/butlr-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/butlr/lifecycle/butlr-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/butlr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/butlr/conventions/butlr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/butlr-conventions.yml
- group: design
  href: https://artifacts.apis.io/butlr/conformance/butlr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/butlr-conformance.yml
- group: design
  href: https://artifacts.apis.io/butlr/data-model/butlr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/butlr-data-model.yml
- group: auth
  href: https://artifacts.apis.io/butlr/security/butlr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/butlr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/butlr/security/butlr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/butlr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/butlr/security/butlr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/butlr-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/butlr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Butlr is an AI platform for privacy-first, heat-based (thermal) occupancy sensing that turns anonymous people-sensing into real-time space-utilization insight for workplaces, senior living, higher education, retail, and smart buildings. Its camera-free thermal sensors capture no personally identifiable information while powering occupancy, traffic, presence-time, and heatmap analytics. Butlr exposes an API-first platform: a GraphQL asset-management API for sites, buildings, floors, rooms, zones, hives, and sensors; a RESTful Reporting API (v3) for historical time-series occupancy; real-time webhooks for detections, traffic, and occupancy events; and an official Model Context Protocol (MCP) server for agent access. The company reports 30,000+ deployed sensors generating a billion data points daily across 100M+ square feet in 22 countries.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/butlr.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 10 tools listed.
  name: Butlr MCP Server
  slug: butlr
modified: '2026-10-06'
name: Butlr
nav: Providers
network: true
overview: 'Butlr is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, Occupancy, People Sensing, and Smart Buildings.


  The Butlr catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Butlr''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, authentication, and 26 more developer resources.'
random_paper: 1
scopes:
- name: Butlr Scopes
  scope_count: 12
  slug: butlr-scopes
  summary_line: 12 scopes
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 48.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/butlr/butlr-2026-07-25T204120.png
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
skill_count: 3
skills:
- name: Find available space and current busyness
  slug: butlr-find-available-space
- name: Analyze historical occupancy and traffic
  slug: butlr-occupancy-analytics
- name: Check sensor and hardware health
  slug: butlr-sensor-health
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
- Real Estate
website: https://www.butlr.com
---
