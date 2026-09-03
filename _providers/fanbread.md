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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fanbread-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fanbread.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FanBread
created: '2026-07-17'
description: Fanbread is a defunct venture-backed company originally surfaced as a portfolio company of 500 Global and added to the API Evangelist network as an enrichment lead. Its primary domain fanbread.com no longer resolves to a live site — the HTTPS handshake fails and HTTP returns 410 Gone from a parking host — and no website, developer portal, documentation, API reference, or machine-readable API surface remains anywhere. The company's GitHub organization survives under the login FanBread but is now titled "Wild Sky Media FnB" and points at wildskymedia.com; its seven public repositories are forks and small front-end utilities with no first-party API artifacts and no activity since April 2020. This profile is retained as a historical record and a dead-domain marker, not as an active API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fanbread.png
layout: provider
modified: '2026-07-20'
name: Fanbread
nav: Providers
network: true
overview: Fanbread is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Venture Backed, 500 Global, and Media.
random_paper: 0
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Fanbread Domain Security
  slug: fanbread-domain-security
  summary_line: no transport/DNS hardening detected
slug: fanbread
tags:
- Company
- Defunct
- Venture Backed
- 500 Global
- Media
website: https://fanbread.com
---
