---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zerodev Agentic Access
  operation_count: 1
  slug: zerodev-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The JSON-RPC API from ZeroDev — 1 operation(s) for json-rpc.
  name: ZeroDev JSON-RPC API
  slug: zerodev-json-rpc-api
artifact_total: 7
collections:
- collection_type: open
  name: ZeroDev Bundler & Paymaster RPC
  slug: open-zerodev
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/zerodevapp/sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zerodev-agentic-access.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/zerodev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zerodev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zerodev-finops.yml
created: '2026-06-20'
description: ZeroDev is account-abstraction / smart-wallet infrastructure for EVM chains. It runs an ERC-4337 (and EIP-7702) bundler RPC and a paymaster RPC, both exposed as JSON-RPC over HTTPS, plus the Kernel smart-account SDK and a meta-aggregator (Smart Routing). Apps sponsor gas, let users pay gas in ERC-20s, and submit UserOperations through a single project-scoped RPC endpoint.
finops:
- name: Zerodev Finops
  service_category: Web3 Infrastructure
  slug: zerodev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zerodev.png
layout: provider
modified: '2026-06-20'
name: ZeroDev
nav: Providers
network: true
overview: 'ZeroDev publishes 1 API on the [APIs.io](https://apis.io/) network: JSON-RPC API. Tagged areas include Account Abstraction, Smart Wallets, ERC-4337, EIP-7702, and Paymaster.


  ZeroDev''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Zerodev Plans Pricing
  plan_count: 4
  slug: zerodev-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 4
  name: Zerodev Rate Limits
  slug: zerodev-rate-limits
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.4
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
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zerodev/refs/heads/main/screenshots/zerodev-2026-06-20T201834.png
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
