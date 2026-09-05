---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Neighbor Agentic Access
  operation_count: 2
  slug: neighbor-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://api.neighbor.com
  baseurl_source: declared
  description: The Public API from Neighbor — 2 operation(s) for public.
  name: Neighbor Public API
  slug: neighbor-public-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Neighbor Public API
  slug: open-neighbor-public-api
- collection_type: open
  name: Neighbor API
  slug: open-neighbor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neighbor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neighbor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neighbor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neiybor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neighbor
created: '2025-02-09'
description: The Neighbor API allows trusted hosts to retrieve reports related to their account, including active reservations and payout transfers.
finops:
- name: Neighbor Finops
  service_category: API
  slug: neighbor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neighbor.png
layout: provider
modified: '2026-05-19'
name: Neighbor
nav: Providers
network: true
overview: 'Neighbor publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Storage, Marketplace, and Reporting.


  Neighbor''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Neighbor Plans Pricing
  plan_count: 3
  slug: neighbor-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Neighbor Rate Limits
  slug: neighbor-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neighbor/refs/heads/main/screenshots/neighbor-2026-06-20T190130.png
security:
- kind: authentication
  name: Neighbor Authentication
  slug: neighbor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Neighbor Domain Security
  slug: neighbor-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: neighbor
tags:
- Storage
- Marketplace
- Reporting
---
