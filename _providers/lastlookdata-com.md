---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: unknown
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Financial market data API for AI agents providing treasury yields, mortgage rates, FX rates, energy prices, macro indicators, and company fundamentals.
  name: LastLook Data API
  slug: lastlook-data-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/lastlookdata-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lastlookdata-com/llms/lastlookdata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lastlookdata-com-llms.txt
- group: other
  href: https://artifacts.apis.io/lastlookdata-com/a2a/lastlookdata-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lastlookdata-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/lastlookdata-com/mcp/lastlookdata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lastlookdata-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/lastlookdata-com/hosts/lastlookdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lastlookdata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lastlookdata-com/vendors/lastlookdata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lastlookdata-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://lastlookdata.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/lastlookdata-com/security/lastlookdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lastlookdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lastlookdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lastlookdata.com/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lastlookdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lastlookdata.com/privacy
coverage:
  detail: Provider docs are HTML with no discoverable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://api.lastlookdata.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: LastLook Data provides financial market data APIs tailored for AI agents, offering real-time treasury yields, mortgage rates, foreign exchange, macro indicators, cryptocurrency prices, and company fundamentals. Access is managed via x402 micropayments on Base, eliminating the need for API keys, subscriptions, or minimum usage requirements. The service delivers up-to-date data sourced from FRED and other providers, enabling agents to integrate financial insights directly into their workflows without friction.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/3462a646-aab8-4390-b2df-41261d98705b/id-preview-7caf2c69--5899bcfa-c8a8-4d62-a089-9293a252704d.lovable.app-1778428867741.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lastlookdata.com.
  name: lastlookdata-com MCP Server
  slug: lastlookdata-com-mcp-yml
modified: '2026-10-30'
name: lastlookdata-com
nav: Providers
network: true
overview: 'lastlookdata-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: LastLook Data API. Tagged areas include Company, Finance, Data, Artificial Intelligence, and Market Data.


  lastlookdata-com''s developer surface includes API reference, documentation, and 10 more developer resources.'
random_paper: 15
scopes:
- name: Lastlookdata Com Scopes
  scope_count: 0
  slug: lastlookdata-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 14.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 21.5
  provenance:
    conformance: unknown
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lastlookdata-com/lastlookdata-com-2026-11-03T134649.png
security:
- kind: authentication
  name: Lastlookdata Com Authentication
  slug: lastlookdata-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lastlookdata Com Domain Security
  slug: lastlookdata-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: lastlookdata-com-main
  slug: lastlookdata-com-main
slug: lastlookdata-com
tags:
- Company
- Finance
- Data
- Artificial Intelligence
- Market Data
website: https://lastlookdata.com/
---
