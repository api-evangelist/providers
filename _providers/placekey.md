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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Placekey Agentic Access
  operation_count: 2
  slug: placekey-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: The Bulk API from Placekey — 1 operation(s) for bulk.
  name: Placekey Bulk API
  slug: placekey-bulk-api
- description: The Lookup API from Placekey — 1 operation(s) for lookup.
  name: Placekey Lookup API
  slug: placekey-lookup-api
artifact_total: 9
collections:
- collection_type: open
  name: Placekey API
  slug: open-placekey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/placekey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/placekey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/placekey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Placekey
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/placekey
- group: company
  title: ''
  type: Website
  url: https://www.placekey.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.placekey.io
- group: commercial
  title: ''
  type: Plans
  url: plans/placekey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/placekey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/placekey-finops.yml
created: '2026-06-21'
description: Placekey is a free, universal identifier for any physical place, designed to make it easy to join and match address and point-of-interest data across disparate datasets. The Placekey API resolves an address or latitude/longitude into a single Placekey, supporting both single and bulk (up to 100 per batch) lookups for address matching, deduplication, and data enrichment.
finops:
- name: Placekey Finops
  service_category: Location and Mapping
  slug: placekey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/placekey.png
layout: provider
modified: '2026-06-21'
name: Placekey
nav: Providers
network: true
overview: 'Placekey publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bulk API and Lookup API. Tagged areas include Location, Geocoding, Address Matching, Identifiers, and POI.


  Placekey''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Placekey Plans Pricing
  plan_count: 4
  slug: placekey-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 4
  name: Placekey Rate Limits
  slug: placekey-rate-limits
score:
  band: thin
  composite: 41.3
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Placekey Authentication
  slug: placekey-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Placekey Domain Security
  slug: placekey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: placekey
tags:
- Location
- Geocoding
- Address Matching
- Identifiers
- POI
website: https://www.placekey.io
---
