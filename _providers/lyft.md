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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lyft Agentic Access
  operation_count: 19
  slug: lyft-agentic-access
  summary_line: 19 operations · 6 acting
api_count: 7
apis:
- description: Endpoints for creating, scheduling, tracking, and managing rides on behalf of passengers who may not have a Lyft account.
  name: lyft Concierge Rides API
  slug: lyft-concierge-rides-api
- description: Endpoints for estimating ride costs for concierge bookings.
  name: lyft Cost Estimates API
  slug: lyft-cost-estimates-api
- description: Endpoints for checking the availability and proximity of nearby Lyft drivers.
  name: lyft Drivers API
  slug: lyft-drivers-api
- description: Endpoints for estimating the time for the nearest driver to reach a specified pickup location.
  name: lyft ETA API
  slug: lyft-eta-api
- description: Endpoints for retrieving profile information for the authenticated Lyft user.
  name: lyft Profile API
  slug: lyft-profile-api
- description: Endpoints for retrieving available ride types for concierge bookings.
  name: lyft Ride Types API
  slug: lyft-ride-types-api
- description: Endpoints for requesting, tracking, canceling, and managing Lyft rides on behalf of an authenticated user.
  name: lyft Rides API
  slug: lyft-rides-api
artifact_total: 21
collections:
- collection_type: open
  name: Lyft Concierge API
  slug: open-lyft-concierge
- collection_type: open
  name: Lyft Ride-Sharing API
  slug: open-lyft-ride-sharing
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lyft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lyft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lyft-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lyft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lyft
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lyft-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lyft-ride-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lyft-ride-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lyft-cost-estimate-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.lyft.com/blog
description: Lyft is a transportation network company that develops, markets, and operates a mobile app offering ride-hailing, vehicles for hire, motorized scooters, bicycle-sharing, and food delivery services.
finops:
- name: Lyft Finops
  service_category: API
  slug: lyft-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Lyft ride-sharing platform. It is derived from
  name: Lyft GraphQL Schema
  slug: lyft-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lyft.png
json_schemas:
- name: Lyft Cost Estimate
  property_count: 9
  slug: lyft-cost-estimate
- name: Lyft Ride
  property_count: 16
  slug: lyft-ride
- name: Lyft Ride Type
  property_count: 5
  slug: lyft-ride-type
jsonld:
- class_count: 0
  name: Lyft Context
  property_count: 9
  slug: lyft-context
layout: provider
modified: '2026-05-19'
name: lyft
nav: Providers
network: true
overview: 'lyft publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Concierge Rides API, Cost Estimates API, Drivers API, and 4 more.


  The lyft catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lyft''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Lyft Plans Pricing
  plan_count: 3
  slug: lyft-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 5
  name: Lyft Rate Limits
  slug: lyft-rate-limits
rules:
- name: lyft API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: lyft-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.0
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/screenshots/lyft-2026-06-20T184816.png
security:
- kind: authentication
  name: Lyft Authentication
  slug: lyft-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lyft Domain Security
  slug: lyft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lyft
---
