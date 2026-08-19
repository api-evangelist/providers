---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: High Mobility Agentic Access
  operation_count: 7
  slug: high-mobility-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: OAuth 2.0 token issuance for the High Mobility platform.
  name: High Mobility Authentication API
  slug: high-mobility-authentication-api
- description: Manage fleet vehicle clearance status and onboarding.
  name: High Mobility Fleet Clearance API
  slug: high-mobility-fleet-clearance-api
- description: Retrieve real-time vehicle telemetry organized by capability category.
  name: High Mobility Vehicle Data API
  slug: high-mobility-vehicle-data-api
- description: Check brand and capability eligibility for a vehicle.
  name: High Mobility Vehicle Eligibility API
  slug: high-mobility-vehicle-eligibility-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: High Mobility Vehicle Authentication API
  slug: open-high-mobility-authentication-api
- collection_type: open
  name: High Mobility Vehicle Authentication Fleet Clearance API
  slug: open-high-mobility-fleet-clearance-api
- collection_type: open
  name: High Mobility Vehicle Authentication Vehicle Data API
  slug: open-high-mobility-vehicle-data-api
- collection_type: open
  name: High Mobility Vehicle Authentication Vehicle Eligibility API
  slug: open-high-mobility-vehicle-eligibility-api
- collection_type: open
  name: High Mobility Vehicle API
  slug: open-high-mobility
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/highmobility/open-api-specifications/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/high-mobility-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/high-mobility-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/high-mobility-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/high-mobility-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/high-mobility
- group: start
  title: ''
  type: Portal
  url: https://high-mobility.com/developers/
- group: company
  title: ''
  type: Website
  url: https://high-mobility.com/
- group: docs
  title: ''
  type: Documentation
  url: https://high-mobility.com/learn/documentation/
- group: start
  title: ''
  type: Signup
  url: https://high-mobility.com/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/highmobility
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.high-mobility.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.high-mobility.com/blog
created: '2026-03-16'
description: High Mobility provides a connected car API platform that enables developers to build apps using real-time data from vehicles. The platform provides access to car data such as location, fuel level, door locks, diagnostics, and other vehicle telemetry data.
finops:
- name: High Mobility Finops
  service_category: API
  slug: high-mobility-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/high-mobility.png
layout: provider
modified: '2026-05-19'
name: High Mobility
nav: Providers
network: true
overview: 'High Mobility publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Fleet Clearance API, Vehicle Data API, and 1 more. Tagged areas include Automotive, Connected Cars, IoT, and Vehicle Data.


  High Mobility''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: High Mobility Plans Pricing
  plan_count: 3
  slug: high-mobility-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 5
  name: High Mobility Rate Limits
  slug: high-mobility-rate-limits
scopes:
- name: High Mobility Scopes
  scope_count: 1
  slug: high-mobility-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: thin
  composite: 35.9
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 59.3
    developer_ergonomics: 33.3
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/high-mobility/refs/heads/main/screenshots/high-mobility-2026-06-20T182732.png
security:
- kind: authentication
  name: High Mobility Authentication
  slug: high-mobility-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: High Mobility Domain Security
  slug: high-mobility-domain-security
  summary_line: TLSv1.3 · HSTS
slug: high-mobility
tags:
- Automotive
- Connected Cars
- IoT
- Vehicle Data
website: https://high-mobility.com/
---
