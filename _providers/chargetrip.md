---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Chargetrip Agentic Access
  operation_count: 1
  slug: chargetrip-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.chargetrip.io/graphql
  baseurl_source: declared
  description: The Graph QL API from Chargetrip — 1 operation(s) for graph ql.
  name: Chargetrip Graph QL API
  slug: chargetrip-graph-ql-api
artifact_total: 13
asyncapis:
- description: AsyncAPI 2.6 description of Chargetrip's **real-time route updates** surface. Unlike the synchronous query/mutation surface (HTTP POST to `https://api.chargetrip.io/graphql`, modeled in `openapi/charg
  name: Chargetrip Route Updates (GraphQL Subscriptions over WebSocket)
  slug: chargetrip-asyncapi
collections:
- collection_type: open
  name: Chargetrip API (HTTP transport) GraphQL API
  slug: open-chargetrip-graphql-api
- collection_type: open
  name: Chargetrip GraphQL API
  slug: open-chargetrip
common:
- group: agent
  href: https://artifacts.apis.io/chargetrip/agentic-access/chargetrip-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chargetrip-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chargetrip/security/chargetrip-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chargetrip-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chargetrip/security/chargetrip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargetrip-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chargetrip/authentication/chargetrip-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chargetrip-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargetrip
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chargetrip
- group: company
  title: ''
  type: Website
  url: https://www.chargetrip.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chargetrip.com
- group: commercial
  href: https://artifacts.apis.io/chargetrip/plans/chargetrip-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chargetrip-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chargetrip/rate-limits/chargetrip-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chargetrip-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chargetrip/finops/chargetrip-finops.yml
  title: ''
  type: FinOps
  url: finops/chargetrip-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/chargetrip
created: '2026-06-21'
description: Chargetrip provides an EV routing GraphQL API used by automakers and e-mobility services. It plans range-aware routes with charging stops, exposes a curated charge station database, an EV vehicle/consumption database, isolines (reachability), and operator data, with real-time route updates delivered over WebSocket subscriptions.
finops:
- has_sources: true
  method: generated
  name: Chargetrip Finops
  primary_unit: ''
  service_category: Maps and Routing
  slug: chargetrip-finops
  template: false
graphqls:
- description: The [Chargetrip](https://www.chargetrip.com) API is a **native GraphQL API** for
  name: Chargetrip GraphQL API
  slug: chargetrip-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargetrip.png
layout: provider
modified: '2026-06-21'
name: Chargetrip
nav: Providers
network: true
overview: 'Chargetrip publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Electric Vehicles, Routing, Charging Stations, GraphQL, and Mobility.


  The Chargetrip catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chargetrip''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Chargetrip Plans Pricing
  plan_count: 3
  slug: chargetrip-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Chargetrip Rate Limits
  slug: chargetrip-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Chargetrip — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: chargetrip-asyncapi-spectral-rules
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 11.4
    contract_quality: 56.5
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chargetrip/chargetrip-2026-07-25T205058.png
security:
- kind: authentication
  name: Chargetrip Authentication
  slug: chargetrip-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Chargetrip Domain Security
  slug: chargetrip-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chargetrip Vulnerability Disclosure
  slug: chargetrip-vulnerability-disclosure
  summary_line: no policy recorded
slug: chargetrip
tags:
- Electric Vehicles
- Routing
- Charging Stations
- GraphQL
- Mobility
- Real-Time
website: https://www.chargetrip.com
---
