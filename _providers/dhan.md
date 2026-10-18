---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dhan/refs/heads/main/plans/dhan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dhan-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dhan/refs/heads/main/llms/dhan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dhan-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dhan/refs/heads/main/hosts/dhan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dhan-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dhan.co/terms/
- group: operate
  title: ''
  type: Support
  url: https://dhan.co/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dhan.co/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dhan.co/pricing/
- group: company
  title: ''
  type: Blog
  url: https://dhan.co/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dhan/refs/heads/main/security/dhan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dhan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dhan.co
coverage:
  checked: '2026-10-14'
  detail: The API homepage https://api.dhan.co returns a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://api.dhan.co
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Dhan is an online stock trading and investing platform based in India, offering a wide range of products including equities, commodities, mutual funds, ETFs, and US stocks. It provides advanced trading tools such as the DEXT T3 terminal, options and futures platforms, margin trading, and a gold vault service. The platform also supports algorithmic trading via APIs, integrates with TradingView, and offers educational resources through its blog and community.
image: https://stock-logos.dhan.co/share-image/twitter-share.png
layout: provider
modified: '2026-10-14'
name: Dhan
nav: Providers
network: true
overview: 'Dhan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Trading, and Investment.


  Dhan''s developer surface includes support, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Dhan Plans Pricing
  plan_count: 1
  slug: dhan-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 18.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dhan Domain Security
  slug: dhan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dhan
tags:
- Company
- Finance
- Trading
- Investment
website: https://dhan.co
---
