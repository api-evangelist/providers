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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Wasmer Agentic Access
  operation_count: 2
  slug: wasmer-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The wasmer command-line client (wasmer login, publish, deploy, run, ssh) - a first-class consumer of the Registry GraphQL API that wraps publish and Edge deployment workflows.
  name: Wasmer CLI
  slug: wasmer-cli
- baseURL: https://registry.wasmer.io/graphql
  baseurl_source: declared
  description: The Graph QL API from Wasmer — 1 operation(s) for graph ql.
  name: Wasmer Graph QL API
  slug: wasmer-graph-ql-api
artifact_total: 13
collections:
- collection_type: open
  name: Wasmer Registry GraphQL API
  slug: open-wasmer-graphql-api
- collection_type: open
  name: Wasmer Registry GraphQL API
  slug: open-wasmer
common:
- group: agent
  href: https://artifacts.apis.io/wasmer/agentic-access/wasmer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wasmer-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wasmer/security/wasmer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wasmer-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wasmer/security/wasmer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wasmer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wasmer/authentication/wasmer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wasmer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wasmerio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wasmer
- group: company
  title: ''
  type: Website
  url: https://wasmer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wasmer.io
- group: commercial
  href: https://artifacts.apis.io/wasmer/plans/wasmer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wasmer-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wasmer/rate-limits/wasmer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wasmer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wasmer/finops/wasmer-finops.yml
  title: ''
  type: FinOps
  url: finops/wasmer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.wasmer.io/feed
created: '2026-06-20'
description: Wasmer is a WebAssembly runtime, package registry, and edge platform. The Wasmer Registry stores and distributes WebAssembly packages and namespaces, Wasmer Edge deploys those packages as auto-scaling apps, and the wasmer CLI and wasmer.sh interact with the platform through a single public GraphQL API at registry.wasmer.io/graphql.
finops:
- has_sources: true
  method: generated
  name: Wasmer Finops
  primary_unit: ''
  service_category: Compute and Edge
  slug: wasmer-finops
  template: false
graphqls:
- description: Representative GraphQL schema for the [Wasmer](https://wasmer.io) Registry and Edge
  name: Wasmer Registry GraphQL API
  slug: wasmer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wasmer.png
layout: provider
modified: '2026-06-20'
name: Wasmer
nav: Providers
network: true
overview: 'Wasmer publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Graph QL API, and 1 more. Tagged areas include WebAssembly, Wasm, Registry, Edge, and Runtime.


  The Wasmer catalog on APIs.io includes 1 Spectral governance ruleset.


  Wasmer''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Wasmer Plans Pricing
  plan_count: 3
  slug: wasmer-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Wasmer Rate Limits
  slug: wasmer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Wasmer API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: wasmer-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 21.1
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
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wasmer/wasmer-2026-06-20T201241.png
security:
- kind: authentication
  name: Wasmer Authentication
  slug: wasmer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wasmer Domain Security
  slug: wasmer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wasmer Vulnerability Disclosure
  slug: wasmer-vulnerability-disclosure
  summary_line: no policy recorded
slug: wasmer
tags:
- WebAssembly
- Wasm
- Registry
- Edge
- Runtime
website: https://wasmer.io
---
