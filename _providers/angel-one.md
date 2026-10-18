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
  href: https://raw.githubusercontent.com/api-evangelist/angel-one/refs/heads/main/plans/angel-one-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/angel-one-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/angel-one/refs/heads/main/llms/angel-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/angel-one-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angel-one/refs/heads/main/hosts/angel-one-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angel-one-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angel-one/refs/heads/main/vendors/angel-one-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angel-one-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.angelone.in/help-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.angelone.in/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.angelone.in/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angel-one/refs/heads/main/security/angel-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angel-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.angelone.in
coverage:
  checked: '2026-10-14'
  detail: Access to the OpenAPI spec at https://api.angelone.in/openapi.json requires authentication, returning HTTP 403.
  evidence:
  - status: 403
    url: https://api.angelone.in/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-14'
description: Angel One is India’s leading stock broker offering online trading in stocks, mutual funds, commodities, IPOs, futures & options, and ETFs. It provides a smart SuperApp with tools for seamless investing, market insights, and portfolio management for retail investors across India.
image: https://w3assets.angelone.in/wp-content/uploads/2024/08/Monthly-savings-made-easy-with-sip-with-CTA-png.png
layout: provider
modified: '2026-10-14'
name: Angel One
nav: Providers
network: true
overview: 'Angel One is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Brokerage, Investment, and Stock Trading.


  Angel One''s developer surface includes support and 8 more developer resources.'
plans:
- name: Angel One Plans Pricing
  plan_count: 6
  slug: angel-one-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 14.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angel One Domain Security
  slug: angel-one-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: angel-one
tags:
- Company
- Finance
- Brokerage
- Investment
- Stock Trading
website: https://www.angelone.in
---
