---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ledgy Agentic Access
  operation_count: 1
  slug: ledgy-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://app.ledgy.com/graphql
  baseurl_source: declared
  description: The Graph QL API from Ledgy — 1 operation(s) for graph ql.
  name: Ledgy Graph QL API
  slug: ledgy-graph-ql-api
artifact_total: 12
collections:
- collection_type: open
  name: Ledgy GraphQL API
  slug: open-ledgy-graphql-api
- collection_type: open
  name: Ledgy GraphQL API
  slug: open-ledgy
common:
- group: other
  href: https://artifacts.apis.io/ledgy/capabilities/ledgy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ledgy-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ledgy/agentic-access/ledgy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ledgy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ledgy/security/ledgy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ledgy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ledgy/security/ledgy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ledgy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ledgy/authentication/ledgy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ledgy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ledgy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ledgy
- group: company
  title: ''
  type: Website
  url: https://www.ledgy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ledgy.com/
- group: commercial
  href: https://artifacts.apis.io/ledgy/plans/ledgy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ledgy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ledgy/rate-limits/ledgy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ledgy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ledgy/finops/ledgy-finops.yml
  title: ''
  type: FinOps
  url: finops/ledgy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ledgy.com/blog
created: '2026-06-21'
description: Ledgy is a European equity-management platform for cap tables, ESOP/equity plans, stakeholder and investor relations, and financing rounds. The Ledgy GraphQL API exposes a company's cap table, transactions (convertibles, grants, transfers), share classes, financing rounds, ESOP grants, and portfolio data through a single Bearer-authenticated endpoint at https://app.ledgy.com/graphql.
finops:
- has_sources: true
  method: generated
  name: Ledgy Finops
  primary_unit: ''
  service_category: Management and Governance
  slug: ledgy-finops
  template: false
graphqls:
- description: '[Ledgy](https://www.ledgy.com/) is a European equity-management platform for cap tables,'
  name: Ledgy GraphQL API
  slug: ledgy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ledgy.png
layout: provider
modified: '2026-06-21'
name: Ledgy
nav: Providers
network: true
overview: 'Ledgy publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Equity Management, Cap Table, ESOP, Stakeholders, and GraphQL.


  The Ledgy catalog on APIs.io includes 1 Spectral governance ruleset.


  Ledgy''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Ledgy Plans Pricing
  plan_count: 3
  slug: ledgy-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Ledgy Rate Limits
  slug: ledgy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Ledgy API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: ledgy-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 52.7
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ledgy/ledgy-2026-07-25T224817.png
security:
- kind: authentication
  name: Ledgy Authentication
  slug: ledgy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ledgy Domain Security
  slug: ledgy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ledgy Trust Center
  slug: ledgy-trust-center
  summary_line: SOC 2, ISO 27001
slug: ledgy
tags:
- Equity Management
- Cap Table
- ESOP
- Stakeholders
- GraphQL
website: https://www.ledgy.com/
---
