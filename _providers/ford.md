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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Ford Agentic Access
  operation_count: 18
  slug: ford-agentic-access
  summary_line: 18 operations · 10 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: FordConnect allows to send vehicle commands (e.g., lock, unlock, etc.) and request vehicle information (e.g., fuel range, tire pressure, etc.) to Ford and Lincoln vehicles.
  name: FordConnect
  slug: fordconnect
- description: With this API, authorized external parties can retrieve WLTP values based on a specific vehicle configuration.
  name: Ford WLTP Emissions
  slug: ford-wltp-emissions
- description: The Charging API from Ford — 4 operation(s) for charging.
  name: Ford Charging API
  slug: ford-charging-api
- description: The Commands API from Ford — 7 operation(s) for commands.
  name: Ford Commands API
  slug: ford-commands-api
- description: The Images API from Ford — 2 operation(s) for images.
  name: Ford Images API
  slug: ford-images-api
- description: The OAuth API from Ford — 1 operation(s) for oauth.
  name: Ford OAuth API
  slug: ford-oauth-api
- description: The Status API from Ford — 2 operation(s) for status.
  name: Ford Status API
  slug: ford-status-api
- description: The Vehicles API from Ford — 2 operation(s) for vehicles.
  name: Ford Vehicles API
  slug: ford-vehicles-api
artifact_total: 17
collections:
- collection_type: open
  name: FordConnect API
  slug: open-ford
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ford-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ford-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ford-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ford-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ford
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ford-motor-company
- group: start
  title: ''
  type: Portal
  url: https://developer.ford.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ford.com/help/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ford.com/help/privacy/
- group: company
  title: ''
  type: Website
  url: https://www.ford.com/
created: '2025-02-25'
description: Ford is a multinational automotive company that designs, manufactures, and sells a wide range of vehicles, including cars, trucks, and SUVs.
finops:
- name: Ford Finops
  service_category: Connected Vehicle / Mobility
  slug: ford-finops
graphqls:
- description: This conceptual GraphQL schema covers the Ford Motor Company connected vehicle and developer API surface, based on the Ford Developer Portal (https://developer.ford.com/). It models FordConnect capabi
  name: Ford Motor GraphQL Schema
  slug: ford-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ford.png
layout: provider
modified: '2026-04-28'
name: Ford
nav: Providers
network: true
overview: 'Ford publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Charging API, Commands API, Images API, and 3 more. Tagged areas include Automobiles, Cars, and Vehicles.


  Ford''s developer surface includes authentication, developer portal, and 8 more developer resources.'
plans:
- name: Ford Plans Pricing
  plan_count: 2
  slug: ford-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Ford Rate Limits
  slug: ford-rate-limits
scopes:
- name: Ford Scopes
  scope_count: 1
  slug: ford-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 35.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ford/refs/heads/main/screenshots/ford-2026-06-20T181414.png
security:
- kind: authentication
  name: Ford Authentication
  slug: ford-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ford Domain Security
  slug: ford-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ford
tags:
- Automobiles
- Cars
- Vehicles
website: https://www.ford.com/
---
