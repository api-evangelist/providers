---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The ApiKeys API from Voltair — 2 operation(s) for apikeys.
  name: Voltair ApiKeys API
  slug: voltair-apikeys-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Assets API from Voltair — 6 operation(s) for assets.
  name: Voltair Assets API
  slug: voltair-assets-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Clusters API from Voltair — 3 operation(s) for clusters.
  name: Voltair Clusters API
  slug: voltair-clusters-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The ClusterVisits API from Voltair — 2 operation(s) for clustervisits.
  name: Voltair ClusterVisits API
  slug: voltair-clustervisits-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Events API from Voltair — 2 operation(s) for events.
  name: Voltair Events API
  slug: voltair-events-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Identity API from Voltair — 1 operation(s) for identity.
  name: Voltair Identity API
  slug: voltair-identity-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Inspections API from Voltair — 4 operation(s) for inspections.
  name: Voltair Inspections API
  slug: voltair-inspections-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Media API from Voltair — 7 operation(s) for media.
  name: Voltair Media API
  slug: voltair-media-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Missions API from Voltair — 3 operation(s) for missions.
  name: Voltair Missions API
  slug: voltair-missions-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Organization API from Voltair — 1 operation(s) for organization.
  name: Voltair Organization API
  slug: voltair-organization-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Roles API from Voltair — 2 operation(s) for roles.
  name: Voltair Roles API
  slug: voltair-roles-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Sites API from Voltair — 3 operation(s) for sites.
  name: Voltair Sites API
  slug: voltair-sites-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The SiteVisits API from Voltair — 2 operation(s) for sitevisits.
  name: Voltair SiteVisits API
  slug: voltair-sitevisits-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Transactions API from Voltair — 3 operation(s) for transactions.
  name: Voltair Transactions API
  slug: voltair-transactions-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Users API from Voltair — 5 operation(s) for users.
  name: Voltair Users API
  slug: voltair-users-api
- baseURL: https://api.voltairlabs.com
  baseurl_source: declared
  description: The Webhooks API from Voltair — 5 operation(s) for webhooks.
  name: Voltair Webhooks API
  slug: voltair-webhooks-api
artifact_total: 37
asyncapis:
- description: ''
  name: Voltair Webhooks
  slug: voltair-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voltair ApiKeys API
  slug: open-voltair-apikeys-api
- collection_type: open
  name: Voltair ApiKeys Assets API
  slug: open-voltair-assets-api
- collection_type: open
  name: Voltair ApiKeys Clusters API
  slug: open-voltair-clusters-api
- collection_type: open
  name: Voltair ApiKeys ClusterVisits API
  slug: open-voltair-clustervisits-api
- collection_type: open
  name: Voltair ApiKeys Events API
  slug: open-voltair-events-api
- collection_type: open
  name: Voltair ApiKeys Identity API
  slug: open-voltair-identity-api
- collection_type: open
  name: Voltair ApiKeys Inspections API
  slug: open-voltair-inspections-api
- collection_type: open
  name: Voltair ApiKeys Media API
  slug: open-voltair-media-api
- collection_type: open
  name: Voltair ApiKeys Missions API
  slug: open-voltair-missions-api
- collection_type: open
  name: Voltair ApiKeys Organization API
  slug: open-voltair-organization-api
- collection_type: open
  name: Voltair ApiKeys Roles API
  slug: open-voltair-roles-api
- collection_type: open
  name: Voltair ApiKeys Sites API
  slug: open-voltair-sites-api
- collection_type: open
  name: Voltair ApiKeys SiteVisits API
  slug: open-voltair-sitevisits-api
- collection_type: open
  name: Voltair ApiKeys Transactions API
  slug: open-voltair-transactions-api
- collection_type: open
  name: Voltair ApiKeys Users API
  slug: open-voltair-users-api
- collection_type: open
  name: Voltair ApiKeys Webhooks API
  slug: open-voltair-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/voltair-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/voltair-api-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Voltair
nav: Providers
network: true
overview: 'Voltair publishes 16 APIs on the [APIs.io](https://apis.io/) network, including ApiKeys API, Assets API, Clusters API, and 13 more. Tagged areas include Drones, Earth Observation, Infrastructure Inspection, Utilities, and Energy.


  The Voltair catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Voltair''s developer surface includes documentation, API reference, authentication, and 19 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 0
  name: Voltair Rate Limits
  slug: voltair-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 60.8
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 30.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
