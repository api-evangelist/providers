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
api_count: 2
apis:
- description: Unified in-process library API (fetchTicker, fetchOrderBook, createOrder, fetchBalance, etc.) across 100+ exchanges. Not an HTTP service; exchange REST/WebSocket endpoints belong to each exchange.
  name: CCXT Unified API (library)
  slug: ccxt-unified-api
- description: Official MCP server run locally over stdio (npx -y ccxt-mcp); API keys stay on the user machine. Nothing is hosted.
  name: CCXT MCP Server (local stdio)
  slug: ccxt-mcp-server
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/well-known/ccxt-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ccxt-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/well-known/ccxt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ccxt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/hosts/ccxt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ccxt-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/packages/ccxt-packages.yml
  title: ''
  type: SDKs
  url: packages/ccxt-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/packages/ccxt-packages.yml
  title: ''
  type: Packages
  url: packages/ccxt-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.ccxt.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ccxt.com/en/collections/19730829-getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ccxt.com/playground
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/security/ccxt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ccxt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.ccxt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ccxt.com/docs/manual
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ccxt/refs/heads/main/llms/ccxt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ccxt-llms.txt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ccxt/ccxt
- group: commercial
  title: ''
  type: License
  url: https://github.com/ccxt/ccxt/blob/master/LICENSE.txt
- group: build
  title: ''
  type: SDK
  url: https://www.npmjs.com/package/ccxt
- group: build
  title: ''
  type: SDK
  url: https://pypi.org/project/ccxt/
- group: build
  title: ''
  type: CLI
  url: https://docs.ccxt.com/docs/cli
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ccxt.com/docs/changelog
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://docs.ccxt.com
  - status: 200
    url: https://github.com/ccxt/ccxt
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'CCXT is an open-source (MIT) cryptocurrency trading library that wraps the public and private APIs of 100+ crypto exchanges and prediction markets behind one unified API, in JavaScript/TypeScript, Python, PHP, C#, Go, Java and Rust (npm ccxt 4.5.85). It is a client library, not a hosted HTTP API: there is no CCXT server endpoint and no OpenAPI. It also ships a local stdio MCP server (npm ccxt-mcp), a CLI, and AI coding skills.'
image: https://docs.ccxt.com/og/home
layout: provider
modified: '2026-10-13'
name: CCXT
nav: Providers
network: true
overview: 'CCXT is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, Exchange, and Open Source.


  CCXT''s developer surface includes support, getting-started guide, documentation, SDKs, CLI, changelog, and 12 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 64.3
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ccxt Domain Security
  slug: ccxt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ccxt
tags:
- Company
- Cryptocurrency
- Trading
- Exchange
- Open Source
- SDK
- MCP
website: https://docs.ccxt.com
---
