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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/coinverdict-io/conformance/coinverdict-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinverdict-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinverdict-io/llms/coinverdict-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinverdict-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinverdict-io/mcp/coinverdict-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinverdict-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/coinverdict-io/hosts/coinverdict-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinverdict-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinverdict-io/vendors/coinverdict-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinverdict-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinverdict.io/terms
- group: auth
  href: https://artifacts.apis.io/coinverdict-io/security/coinverdict-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinverdict-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinverdict.io/
created: '2026-11-04'
description: CoinVerdict provides AI‑driven research verdicts for cryptocurrency assets. An AI analyst desk evaluates each coin, delivering a concise verdict grounded in a settled record of key opinion leader (KOL) calls. The platform aims to bring transparent, data‑backed insights to investors and enthusiasts in the fast‑moving crypto market.
image: https://coinverdict.io/og/receipts.png?v=2
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.coinverdict.io.
  name: CoinVerdict MCP Server
  slug: coinverdict-io-mcp-yml
modified: '2026-11-04'
name: CoinVerdict
nav: Providers
network: true
overview: CoinVerdict is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Artificial Intelligence, Research, Verdicts, and Analytics.
random_paper: 23
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinverdict Io Domain Security
  slug: coinverdict-io-domain-security
  summary_line: TLSv1.3
slug: coinverdict-io
tags:
- Cryptocurrency
- Artificial Intelligence
- Research
- Verdicts
- Analytics
website: https://coinverdict.io/
---
