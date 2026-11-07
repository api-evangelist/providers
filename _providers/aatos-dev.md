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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AATOS provides a non‑custodial MCP for Stock Tokens on the Robinhood Chain, offering read‑only actions and paid quoting/execution via on‑chain payments.
  name: AATOS API
  slug: aatos-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aatos-dev/plans/aatos-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aatos-dev-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/aatos-dev/authentication/aatos-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aatos-dev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/aatos-dev/llms/aatos-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aatos-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/aatos-dev/hosts/aatos-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aatos-dev-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aatos-dev/security/aatos-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aatos-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aatos.dev/
- group: company
  title: ''
  type: Blog
  url: https://aatos.dev/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://aatos.dev/api/access/pricing
- group: operate
  title: ''
  type: Support
  url: https://aatos.dev/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tailoredtidings
coverage:
  checked: '2026-10-31'
  detail: No machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract is published despite the API being described in JSON pricing data.
  evidence:
  - status: 200
    url: https://aatos.dev/api/access/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AATOS is a non‑custodial MCP for Stock Tokens on the Robinhood Chain (chain ID 4663). It enables agents to list, price, check liquidity and obtain unsigned plans that users sign on‑chain, charging about 10 bps in ETH. The service is not a brokerage and is unavailable to US persons. It offers free read‑only actions and paid quoting/execution, with detailed FAQs and pricing information.
image: https://aatos.dev/brand/aatos-mark-on-dark.svg
layout: provider
modified: '2026-10-31'
name: AATOS
nav: Providers
network: true
overview: 'AATOS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Tokenization, MCP, Robinhood Chain, and Cryptocurrency.


  AATOS''s developer surface includes authentication, engineering blog, pricing, support, and 6 more developer resources.'
plans:
- name: Aatos Dev Plans Pricing
  plan_count: 3
  slug: aatos-dev-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 18.1
  provenance:
    mcp: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aatos Dev Authentication
  slug: aatos-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aatos Dev Domain Security
  slug: aatos-dev-domain-security
  summary_line: TLSv1.3
slug: aatos-dev
tags:
- Finance
- Tokenization
- MCP
- Robinhood Chain
- Cryptocurrency
website: https://aatos.dev/
---
