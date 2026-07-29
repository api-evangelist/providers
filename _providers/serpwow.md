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
- acting_count: 0
  human_in_the_loop: 0
  name: Serpwow Agentic Access
  operation_count: 6
  slug: serpwow-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: SerpWow accurately returns all data on the Google Trends page including Related Topics (topics that were searched by other users, when searching for the specified search query) and Related Queries (ot
  name: SerpWow
  slug: serpwow
- description: The Search API from SerpWow — 6 operation(s) for search.
  name: SerpWow Search API
  slug: serpwow-search-api
artifact_total: 9
collections:
- collection_type: open
  name: SerpWow API
  slug: open-serpwow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serpwow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serpwow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serpwow-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serpwow
created: '2025-01-07'
description: SerpWow accurately returns all data on the Google Trends page including Related Topics (topics that were searched by other users, when searching for the specified search query) and Related Queries (other search phrases that were searched by users that have also searched for the specified search query).
finops:
- name: Serpwow Finops
  service_category: API
  slug: serpwow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serpwow.png
layout: provider
modified: '2026-03-16'
name: SerpWow
nav: Providers
network: true
overview: 'SerpWow publishes 1 API on the [APIs.io](https://apis.io/) network: Search API.


  SerpWow''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Serpwow Plans Pricing
  plan_count: 3
  slug: serpwow-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Serpwow Rate Limits
  slug: serpwow-rate-limits
score:
  band: thin
  composite: 32.4
  delta: -1.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serpwow/refs/heads/main/screenshots/serpwow-2026-06-20T193727.png
security:
- kind: authentication
  name: Serpwow Authentication
  slug: serpwow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Serpwow Domain Security
  slug: serpwow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: serpwow
---
