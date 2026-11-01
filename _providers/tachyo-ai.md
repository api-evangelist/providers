---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/tachyo-ai/authentication/tachyo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tachyo-ai-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://access.tachyo.ai/status
- group: design
  href: https://artifacts.apis.io/tachyo-ai/lifecycle/tachyo-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tachyo-ai-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/tachyo-ai/hosts/tachyo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tachyo-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tachyo-ai/vendors/tachyo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tachyo-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://tachyo.ai/dapp/login
- group: auth
  href: https://artifacts.apis.io/tachyo-ai/security/tachyo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tachyo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tachyo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tachyo.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tachyo.ai/getting-started/first-session
- group: operate
  title: ''
  type: Support
  url: https://docs.tachyo.ai/under-the-hood/what-we-dont-do
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 0
    url: https://api.tachyo.ai/openapi.json
  - status: 404
    url: https://tachyo.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Tachyo AI provides a smart‑money wallet scoring platform for memecoin traders across multiple blockchains. It grades over 720,000 wallets based on trade performance, offering detailed scores and analytics to help users assess token holders before investing. The service includes tools for token risk assessment, wallet tier classification, and market insights, targeting crypto enthusiasts and professional traders seeking data‑driven decisions.
image: https://tachyo.ai/home/og.png?v=4
layout: provider
modified: '2026-10-29'
name: tachyo-ai
nav: Providers
network: true
overview: 'tachyo-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Analytics, Wallet, and Memecoin.


  tachyo-ai''s developer surface includes authentication, documentation, getting-started guide, support, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tachyo Ai Authentication
  slug: tachyo-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tachyo Ai Domain Security
  slug: tachyo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tachyo-ai
tags:
- Company
- Crypto
- Analytics
- Wallet
- Memecoin
website: https://tachyo.ai/
---
