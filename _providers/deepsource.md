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
  name: Deepsource Agentic Access
  operation_count: 1
  slug: deepsource-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.deepsource.com/graphql
  baseurl_source: declared
  description: The Graph QL API from DeepSource — 1 operation(s) for graph ql.
  name: DeepSource Graph QL API
  slug: deepsource-graph-ql-api
artifact_total: 11
collections:
- collection_type: open
  name: DeepSource GraphQL API
  slug: open-deepsource-graphql-api
- collection_type: open
  name: DeepSource GraphQL API
  slug: open-deepsource
common:
- group: agent
  href: https://artifacts.apis.io/deepsource/agentic-access/deepsource-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deepsource-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/deepsource/security/deepsource-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepsource-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/deepsource/authentication/deepsource-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deepsource-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepsourcecorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepsource
- group: company
  title: ''
  type: Website
  url: https://deepsource.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deepsource.com/docs/developers/api
- group: commercial
  href: https://artifacts.apis.io/deepsource/plans/deepsource-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepsource-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/deepsource/rate-limits/deepsource-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deepsource-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deepsource/finops/deepsource-finops.yml
  title: ''
  type: FinOps
  url: finops/deepsource-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://deepsource.com/blog
created: '2026-06-21'
description: DeepSource is a code-quality and security platform that performs static analysis, SCA, secrets detection, AI code review, and Autofix across repositories. Its developer platform is a GraphQL API at https://api.deepsource.com/graphql/ exposing repositories, analysis runs, issues, checks, analyzers, and quality-gate management, authenticated with a Personal Access Token Bearer credential.
finops:
- has_sources: true
  method: generated
  name: Deepsource Finops
  primary_unit: ''
  service_category: Developer Tools
  slug: deepsource-finops
  template: false
graphqls:
- description: The [DeepSource](https://deepsource.com) developer platform is a single **GraphQL API**
  name: DeepSource GraphQL API
  slug: deepsource-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepsource.png
layout: provider
modified: '2026-06-21'
name: DeepSource
nav: Providers
network: true
overview: 'DeepSource publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Code Quality, Static Analysis, Code Review, Security, and GraphQL.


  The DeepSource catalog on APIs.io includes 1 Spectral governance ruleset.


  DeepSource''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Deepsource Plans Pricing
  plan_count: 3
  slug: deepsource-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Deepsource Rate Limits
  slug: deepsource-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: DeepSource API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: deepsource-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 55.7
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 29.8
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
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/deepsource/deepsource-2026-07-25T211607.png
security:
- kind: authentication
  name: Deepsource Authentication
  slug: deepsource-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepsource Domain Security
  slug: deepsource-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: deepsource
tags:
- Code Quality
- Static Analysis
- Code Review
- Security
- GraphQL
- Developer Tools
website: https://deepsource.com
---
