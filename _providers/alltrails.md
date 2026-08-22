---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.1
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alltrails-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alltrails-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alltrails.com
created: '2026-07-17'
description: AllTrails is an outdoor recreation platform for discovering, mapping, and navigating hiking, trail running, mountain biking, and backpacking routes. It offers a searchable database of hundreds of thousands of trails worldwide with maps, elevation profiles, community reviews, photos, and conditions, plus GPS turn-by-turn navigation, offline downloadable maps, and route planning through its AllTrails+ subscription. AllTrails is a consumer mobile and web application; it does not publish a public developer API program, and its web surface is served behind a Cloudflare WAF that blocks automated discovery. This profile was surfaced as a portfolio company of 500 Global and enriched with the verifiable public signals available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alltrails.png
layout: provider
mcp_servers:
- description: ''
  name: alltrails-mcp.yml
  slug: alltrails-mcpyml
modified: '2026-07-17'
name: AllTrails
nav: Providers
network: true
overview: AllTrails is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Outdoor Recreation, Trails, Hiking, and Maps.
random_paper: 2
score:
  band: minimal
  composite: 5.0
  delta: -1.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  provenance:
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alltrails/refs/heads/main/screenshots/alltrails-2026-07-25T195723.png
security:
- kind: domain-security
  name: Alltrails Domain Security
  slug: alltrails-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alltrails
tags:
- Company
- Outdoor Recreation
- Trails
- Hiking
- Maps
- Navigation
- GPS
- Consumer App
website: https://alltrails.com
---
