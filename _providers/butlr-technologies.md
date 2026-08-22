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
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: GraphQL API for efficient asset/resource management — query and mutate organizations, sites, buildings, floors, rooms, zones, hives, sensors, asset tags, and webhooks across the Butlr spatial data-mod
  name: Butlr GraphQL API
  slug: butlr-graphql-api
- description: RESTful Reporting API v3 delivering historical time-series occupancy and traffic data aggregated by floor, room, or zone with windowing, aggregation functions, timezones, and calibrated occupancy.
  name: Butlr Reporting API
  slug: butlr-reporting-api
artifact_total: 6
asyncapis:
- description: ''
  name: Butlr Technologies Webhooks
  slug: butlr-technologies-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://butlr.com
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
- group: auth
  title: ''
  type: Authentication
  url: authentication/butlr-technologies-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.butlr.io
- group: company
  title: ''
  type: Blog
  url: https://www.butlr.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/butlrtechnologies
- group: start
  title: ''
  type: SignUp
  url: https://app.butlr.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.butlr.com/legal/tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.butlr.com/legal/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/butlr-technologies-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/butlr-technologies-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/butlr-technologies-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/butlr-technologies-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/butlr-technologies-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.butlr.io/changelog.md
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/butlr-technologies-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/butlr-technologies-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/butlr-technologies-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/butlr-technologies-domain-security.yml
created: '2026-07-17'
description: Butlr Technologies is a privacy-first people-sensing platform that uses anonymous, heat-based (thermal) occupancy sensors to deliver real-time activity insights for healthier, more efficient physical spaces across workplaces, senior living, retail, and education. Butlr exposes a developer platform behind api.butlr.io consisting of a GraphQL API for asset management (organizations, sites, buildings, floors, rooms, zones, hives, sensors, and tags), a RESTful Reporting API v3 for historical time-series occupancy and traffic, and event-driven webhooks for real-time occupancy, traffic, and PIR motion. Access is authenticated with OAuth 2.0 (Auth0) via password and client-credentials grants, and an official read-only Model Context Protocol (MCP) server connects AI assistants to the platform. Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/butlr-technologies.png
layout: provider
mcp_servers:
- description: ''
  name: butlr-technologies-mcp.yml
  slug: butlr-technologies-mcpyml
modified: '2026-07-18'
name: Butlr Technologies
nav: Providers
network: true
overview: 'Butlr Technologies publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Occupancy Sensing, People Counting, Smart Buildings, and Space Utilization.


  The Butlr Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Butlr Technologies'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 39.2
  delta: -5.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 45.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/butlr-technologies/refs/heads/main/screenshots/butlr-technologies-2026-07-25T204122.png
security:
- kind: authentication
  name: Butlr Technologies Authentication
  slug: butlr-technologies-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Butlr Technologies Domain Security
  slug: butlr-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: butlr-technologies
tags:
- Company
- Occupancy Sensing
- People Counting
- Smart Buildings
- Space Utilization
- IoT
- Thermal Sensors
- Real-Time Data
- GraphQL
- Webhooks
website: https://butlr.com
---
