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
  name: Slab Agentic Access
  operation_count: 1
  slug: slab-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.slab.com/v1/graphql
  baseurl_source: declared
  description: The Graph QL API from Slab — 1 operation(s) for graph ql.
  name: Slab Graph QL API
  slug: slab-graph-ql-api
artifact_total: 11
collections:
- collection_type: open
  name: Slab GraphQL API
  slug: open-slab-graphql-api
- collection_type: open
  name: Slab GraphQL API
  slug: open-slab
common:
- group: agent
  href: https://artifacts.apis.io/slab/agentic-access/slab-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/slab-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/slab/security/slab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/slab-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/slab/security/slab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slab-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/slab/authentication/slab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/slab-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slab-inc
- group: company
  title: ''
  type: Website
  url: https://slab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.slab.com/en/articles/6545629-developer-tools-api-webhooks
- group: commercial
  href: https://artifacts.apis.io/slab/plans/slab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/slab-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/slab/rate-limits/slab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/slab-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/slab/finops/slab-finops.yml
  title: ''
  type: FinOps
  url: finops/slab-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://slab.com/blog/
created: '2026-06-21'
description: Slab is an internal knowledge base and team wiki for the modern workplace, pairing a clean editor and fast search with dozens of integrations. Slab exposes a single GraphQL API at https://api.slab.com/v1/graphql for programmatic access to posts, topics, users, and organization data, available to Business and Enterprise customers.
finops:
- has_sources: true
  method: generated
  name: Slab Finops
  primary_unit: ''
  service_category: Collaboration and Productivity
  slug: slab-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slab.png
layout: provider
modified: '2026-06-21'
name: Slab
nav: Providers
network: true
overview: 'Slab publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Knowledge Base, Wiki, Documentation, Collaboration, and GraphQL.


  The Slab catalog on APIs.io includes 1 Spectral governance ruleset.


  Slab''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Slab Plans Pricing
  plan_count: 4
  slug: slab-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Slab Rate Limits
  slug: slab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Slab API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: slab-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 52.7
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 18.4
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
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/slab/slab-2026-09-02T155823.png
security:
- kind: authentication
  name: Slab Authentication
  slug: slab-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Slab Domain Security
  slug: slab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Slab Vulnerability Disclosure
  slug: slab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: slab
tags:
- Knowledge Base
- Wiki
- Documentation
- Collaboration
- GraphQL
- Knowledge Management
website: https://slab.com/
---
