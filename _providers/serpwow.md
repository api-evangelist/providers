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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
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
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SerpWow Search API
  slug: open-serpwow-search-api
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
random_paper: 46
rate_limits:
- limit_count: 5
  name: Serpwow Rate Limits
  slug: serpwow-rate-limits
score:
  band: emerging
  composite: 23.6
  delta: -1.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 24.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
