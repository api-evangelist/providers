---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides market data endpoints as defined in the OpenAPI spec.
  name: FinzData API
  slug: finzdata-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/finzdata-com/plans/finzdata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finzdata-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/finzdata-com/authentication/finzdata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finzdata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/finzdata-com/conformance/finzdata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finzdata-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/finzdata-com/llms/finzdata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finzdata-com-llms.txt
- group: other
  href: https://artifacts.apis.io/finzdata-com/a2a/finzdata-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/finzdata-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/finzdata-com/mcp/finzdata-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/finzdata-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/finzdata-com/mcp/finzdata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/finzdata-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/finzdata-com/well-known/finzdata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finzdata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/finzdata-com/hosts/finzdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finzdata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/finzdata-com/vendors/finzdata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finzdata-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/finzdata-com/packages/finzdata-com-packages.yml
  title: ''
  type: SDKs
  url: packages/finzdata-com-packages.yml
- group: build
  href: https://artifacts.apis.io/finzdata-com/packages/finzdata-com-packages.yml
  title: ''
  type: Packages
  url: packages/finzdata-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finzdata.com/terms
- group: operate
  title: ''
  type: Support
  url: https://finzdata.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://finzdata.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finzdata.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://data.finzdata.com/stock/team
- group: start
  title: ''
  type: GettingStarted
  url: https://finzdata.com/docs?ref=llms
- group: auth
  href: https://artifacts.apis.io/finzdata-com/security/finzdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finzdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finzdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://finzdata.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.finzdata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://finzdata.com/shop
- group: start
  title: ''
  type: SignUp
  url: https://finzdata.com/signin
created: '2026-10-30'
description: FinzData provides comprehensive historical market data APIs covering US stocks, options, futures, crypto, and macroeconomic series. Their platform offers point‑in‑time, survivorship‑bias‑free datasets spanning over 26 years, including delisted securities, with granular intraday bars and extensive fundamentals. Users can access data via REST endpoints or a Python client, with free tier access and paid bundles for deeper coverage.
image: https://finzdata.com/assets/brand/finzdata-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.finzdata.com.
  name: finzdata-com MCP Server
  slug: finzdata-com-mcp-yml
modified: '2026-10-30'
name: finzdata-com
nav: Providers
network: true
overview: 'finzdata-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Market Data, Historical Data, API, and Python.


  finzdata-com''s developer surface includes authentication, support, getting-started guide, documentation, API reference, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Finzdata Com Plans Pricing
  plan_count: 9
  slug: finzdata-com-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 66.7
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Finzdata Com Authentication
  slug: finzdata-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Finzdata Com Domain Security
  slug: finzdata-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finzdata-com
tags:
- Finance
- Market Data
- Historical Data
- API
- Python
website: https://finzdata.com/
---
