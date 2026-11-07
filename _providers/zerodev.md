---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
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
  score: 20.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zerodev Agentic Access
  operation_count: 1
  slug: zerodev-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://rpc.zerodev.app/api/v3/{projectId}/chain/{chainId}
  baseurl_source: declared
  description: The JSON-RPC API from ZeroDev — 1 operation(s) for json-rpc.
  name: ZeroDev JSON-RPC API
  slug: zerodev-json-rpc-api
artifact_total: 9
collections:
- collection_type: open
  name: ZeroDev Bundler & Paymaster RPC JSON-RPC API
  slug: open-zerodev-json-rpc-api
- collection_type: open
  name: ZeroDev Bundler & Paymaster RPC
  slug: open-zerodev
common:
- group: company
  title: ''
  type: Blog
  url: https://www.zerodev.app/blog
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/zerodevapp/sdk/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/zerodevapp/sdk/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/zerodev/agentic-access/zerodev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zerodev-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/zerodev/security/zerodev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zerodev-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zerodevapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zerodev
- group: company
  title: ''
  type: Website
  url: https://zerodev.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zerodev.app
- group: commercial
  href: https://artifacts.apis.io/zerodev/plans/zerodev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zerodev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/zerodev/rate-limits/zerodev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zerodev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zerodev/finops/zerodev-finops.yml
  title: ''
  type: FinOps
  url: finops/zerodev-finops.yml
created: '2026-06-20'
description: ZeroDev is account-abstraction / smart-wallet infrastructure for EVM chains. It runs an ERC-4337 (and EIP-7702) bundler RPC and a paymaster RPC, both exposed as JSON-RPC over HTTPS, plus the Kernel smart-account SDK and a meta-aggregator (Smart Routing). Apps sponsor gas, let users pay gas in ERC-20s, and submit UserOperations through a single project-scoped RPC endpoint.
finops:
- has_sources: true
  method: generated
  name: Zerodev Finops
  primary_unit: ''
  service_category: Web3 Infrastructure
  slug: zerodev-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zerodev.png
layout: provider
modified: '2026-10-06'
name: ZeroDev
nav: Providers
network: true
overview: 'ZeroDev publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: JSON-RPC API. Tagged areas include Account Abstraction, Smart Wallets, ERC-4337, EIP-7702, and Paymaster.


  The ZeroDev catalog on APIs.io includes 1 Spectral governance ruleset.


  ZeroDev''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Zerodev Plans Pricing
  plan_count: 4
  slug: zerodev-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Zerodev Rate Limits
  slug: zerodev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: ZeroDev API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: zerodev-rules
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.9
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 0.0
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zerodev/zerodev-2026-06-20T201834.png
security:
- kind: domain-security
  name: Zerodev Domain Security
  slug: zerodev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zerodev
tags:
- Account Abstraction
- Smart Wallets
- ERC-4337
- EIP-7702
- Paymaster
- Bundler
- JSON-RPC
- Web3
website: https://zerodev.app
---
