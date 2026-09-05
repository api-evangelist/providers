---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - '{''url'': ''https://urjanet.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.arcadia.com:443/platform?utm_source=urjanet — a different registrable domain (urjanet.com -> arcadia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Urjanet Agentic Access
  operation_count: 12
  slug: urjanet-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.urjanet.com
  baseurl_source: declared
  description: The Authentication API from Urjanet — 1 operation(s) for authentication.
  name: Urjanet Authentication API
  slug: urjanet-authentication-api
- baseURL: https://api.urjanet.com
  baseurl_source: declared
  description: The Credentials & Connections API from Urjanet — 3 operation(s) for credentials & connections.
  name: Urjanet Credentials & Connections API
  slug: urjanet-credentials-connections-api
- baseURL: https://api.urjanet.com
  baseurl_source: declared
  description: The Meters API from Urjanet — 2 operation(s) for meters.
  name: Urjanet Meters API
  slug: urjanet-meters-api
- baseURL: https://api.urjanet.com
  baseurl_source: declared
  description: The Statements & Bills API from Urjanet — 3 operation(s) for statements & bills.
  name: Urjanet Statements & Bills API
  slug: urjanet-statements-bills-api
- baseURL: https://api.urjanet.com
  baseurl_source: declared
  description: The Users API from Urjanet — 1 operation(s) for users.
  name: Urjanet Users API
  slug: urjanet-users-api
- baseURL: https://api.urjanet.com
  baseurl_source: declared
  description: The Webhooks API from Urjanet — 1 operation(s) for webhooks.
  name: Urjanet Webhooks API
  slug: urjanet-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Urjanet Utility Cloud Authentication API
  slug: open-urjanet-authentication-api
- collection_type: open
  name: Urjanet Utility Cloud Authentication Credentials & Connections API
  slug: open-urjanet-credentials-connections-api
- collection_type: open
  name: Urjanet Utility Cloud Authentication Meters API
  slug: open-urjanet-meters-api
- collection_type: open
  name: Urjanet Utility Cloud Authentication Statements & Bills API
  slug: open-urjanet-statements-bills-api
- collection_type: open
  name: Urjanet Utility Cloud Authentication Users API
  slug: open-urjanet-users-api
- collection_type: open
  name: Urjanet Utility Cloud Authentication Webhooks API
  slug: open-urjanet-webhooks-api
- collection_type: open
  name: Urjanet Utility Cloud API
  slug: open-urjanet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/urjanet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urjanet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urjanet-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urjanet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/urjanet-inc
- group: company
  title: ''
  type: Website
  url: https://urjanet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/v1.0-Utility-Cloud/reference/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/urjanet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/urjanet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/urjanet-finops.yml
created: '2026-06-21'
description: Urjanet (now part of Arcadia) is a utility-data aggregation platform that programmatically collects utility bill, statement, meter, and interval usage data from thousands of electricity, gas, water, waste, and telecom providers worldwide. Following Arcadia's 2022 acquisition, Urjanet's data access powers the Arcadia "Arc" / Utility Cloud platform, exposed through a REST API (base URL https://api.urjanet.com) for connecting utility credentials and retrieving normalized utility data. Pricing is sales-led and not publicly published.
finops:
- name: Urjanet Finops
  service_category: Data and Analytics
  slug: urjanet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urjanet.png
layout: provider
name: Urjanet
nav: Providers
network: true
overview: 'Urjanet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Credentials & Connections API, Meters API, and 3 more. Tagged areas include Utility Data, Energy, Utility Bills, Aggregation, and Meters.


  Urjanet''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Urjanet Plans Pricing
  plan_count: 1
  slug: urjanet-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Urjanet Rate Limits
  slug: urjanet-rate-limits
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urjanet/refs/heads/main/screenshots/urjanet-2026-09-02T165214.png
security:
- kind: authentication
  name: Urjanet Authentication
  slug: urjanet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Urjanet Domain Security
  slug: urjanet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urjanet
tags:
- Utility Data
- Energy
- Utility Bills
- Aggregation
- Meters
- Sustainability
website: https://urjanet.com/
---
