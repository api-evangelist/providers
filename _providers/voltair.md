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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-23'
api_count: 16
apis:
- description: The ApiKeys API from Voltair — 2 operation(s) for apikeys.
  name: Voltair ApiKeys API
  slug: voltair-apikeys-api
- description: The Assets API from Voltair — 6 operation(s) for assets.
  name: Voltair Assets API
  slug: voltair-assets-api
- description: The Clusters API from Voltair — 3 operation(s) for clusters.
  name: Voltair Clusters API
  slug: voltair-clusters-api
- description: The ClusterVisits API from Voltair — 2 operation(s) for clustervisits.
  name: Voltair ClusterVisits API
  slug: voltair-clustervisits-api
- description: The Events API from Voltair — 2 operation(s) for events.
  name: Voltair Events API
  slug: voltair-events-api
- description: The Identity API from Voltair — 1 operation(s) for identity.
  name: Voltair Identity API
  slug: voltair-identity-api
- description: The Inspections API from Voltair — 4 operation(s) for inspections.
  name: Voltair Inspections API
  slug: voltair-inspections-api
- description: The Media API from Voltair — 7 operation(s) for media.
  name: Voltair Media API
  slug: voltair-media-api
- description: The Missions API from Voltair — 3 operation(s) for missions.
  name: Voltair Missions API
  slug: voltair-missions-api
- description: The Organization API from Voltair — 1 operation(s) for organization.
  name: Voltair Organization API
  slug: voltair-organization-api
- description: The Roles API from Voltair — 2 operation(s) for roles.
  name: Voltair Roles API
  slug: voltair-roles-api
- description: The Sites API from Voltair — 3 operation(s) for sites.
  name: Voltair Sites API
  slug: voltair-sites-api
- description: The SiteVisits API from Voltair — 2 operation(s) for sitevisits.
  name: Voltair SiteVisits API
  slug: voltair-sitevisits-api
- description: The Transactions API from Voltair — 3 operation(s) for transactions.
  name: Voltair Transactions API
  slug: voltair-transactions-api
- description: The Users API from Voltair — 5 operation(s) for users.
  name: Voltair Users API
  slug: voltair-users-api
- description: The Webhooks API from Voltair — 5 operation(s) for webhooks.
  name: Voltair Webhooks API
  slug: voltair-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Voltair Webhooks
  slug: voltair-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voltair-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voltairlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.voltairlabs.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.voltairlabs.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VoltairLabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voltairlabs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/voltair-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voltair-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/voltair-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voltair-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voltair-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/voltair-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voltair-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voltair-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voltair-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voltair-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voltair-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/voltair-plan-inspection-mission.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/voltair-retrieve-inspection-results.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/voltair-manage-webhooks-and-keys.md
created: '2026-07-17'
description: Voltair (Y Combinator W26, San Francisco) is building a globally distributed network of autonomous drones for Earth observation, starting with power utilities. Its long-range, weatherized Faraday-1 aircraft recharge on Lighthouse-1 pads installed at utility substations and capture high-resolution RGB, radiometric thermal, and LiDAR data for asset inspection, LiDAR corridor mapping, post-storm damage assessment, and rapid fault localization. The Voltair API is an organization-scoped infrastructure inspection platform covering sites, assets, defects, clusters, missions, visits, media, inspections, an audit/undo transaction log, API keys, and signed webhooks.
image: https://avatars.githubusercontent.com/u/203074429
layout: provider
mcp_servers:
- description: ''
  name: voltair-mcp.yml
  slug: voltair-mcpyml
modified: '2026-07-21'
name: Voltair
nav: Providers
network: true
overview: 'Voltair publishes 16 APIs on the [APIs.io](https://apis.io/) network, including ApiKeys API, Assets API, Clusters API, and 13 more. Tagged areas include Drones, Earth Observation, Infrastructure Inspection, Utilities, and Energy.


  The Voltair catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Voltair''s developer surface includes documentation, API reference, authentication, and 17 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Voltair Rate Limits
  slug: voltair-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 62.4
    developer_ergonomics: 41.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 35.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Voltair Authentication
  slug: voltair-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Voltair Domain Security
  slug: voltair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voltair
tags:
- Drones
- Earth Observation
- Infrastructure Inspection
- Utilities
- Energy
- Robotics
- LiDAR
- Aerial Imagery
website: https://voltairlabs.com
---
