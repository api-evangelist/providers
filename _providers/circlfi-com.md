---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/circlfi-com/llms/circlfi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/circlfi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/circlfi-com/hosts/circlfi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circlfi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/circlfi-com/vendors/circlfi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circlfi-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circlfi.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://circlfi.com/blog/
- group: auth
  href: https://artifacts.apis.io/circlfi-com/security/circlfi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circlfi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circlfi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://circlfi.com/methodology/
- group: commercial
  title: ''
  type: Pricing
  url: https://circlfi.com/choose-plan/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found; only an MCP endpoint returned 405.
  evidence:
  - status: 405
    url: https://circlfi.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CirclFi provides an institutional-grade equity valuation engine that evaluates over 5,800 US-listed stocks daily using 13 advanced financial models, including Bayesian DCF, Monte Carlo simulations, and earnings power value. The platform aggregates SEC EDGAR data, macroeconomic indicators, and news sentiment to generate consensus intrinsic values, quality scores, and value‑trap flags, offering both free and paid subscription tiers for individuals and institutions.
image: https://circlfi.com/assets/og-default.png
layout: provider
modified: '2026-11-03'
name: CirclFi
nav: Providers
network: true
overview: 'CirclFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Valuation, Stocks, Equity, and Analytics.


  CirclFi''s developer surface includes engineering blog, documentation, pricing, and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circlfi Com Domain Security
  slug: circlfi-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: circlfi-com
tags:
- Finance
- Valuation
- Stocks
- Equity
- Analytics
website: https://circlfi.com/
---
