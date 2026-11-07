---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cleartape-ai/plans/cleartape-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cleartape-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cleartape-ai/llms/cleartape-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleartape-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/cleartape-ai/mcp/cleartape-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cleartape-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/cleartape-ai/hosts/cleartape-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleartape-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleartape-ai/vendors/cleartape-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleartape-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cleartape-ai/security/cleartape-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleartape-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleartape.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://cleartape.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleartape.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleartape.ai/privacy
- group: operate
  title: ''
  type: HelpCenter
  url: https://cleartape.ai/help
- group: docs
  title: ''
  type: Documentation
  url: https://cleartape.ai/learn
- group: company
  title: ''
  type: Blog
  url: https://cleartape.ai/academy
coverage:
  checked: '2026-11-04'
  detail: Provider documentation pages exist but no machine-readable API contract was found.
  evidence:
  - status: 200
    url: https://cleartape.ai/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Clear Tape provides a US stock screener that evaluates companies on quality, value, growth and momentum using rule‑based strategies. It offers transparent backtests, live records of picks, and a free tier to start screening stocks without price predictions. The platform emphasizes honest data, verifiable results, and clear documentation for developers.
image: https://cleartape.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.cleartape.ai.
  name: Clear Tape MCP Server
  slug: cleartape-ai-mcp-yml
modified: '2026-11-03'
name: Clear Tape
nav: Providers
network: true
overview: 'Clear Tape is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Stock Screener, Data, Backtesting, and Free Tier.


  Clear Tape''s developer surface includes pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Cleartape Ai Plans Pricing
  plan_count: 3
  slug: cleartape-ai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleartape Ai Domain Security
  slug: cleartape-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cleartape-ai
tags:
- Finance
- Stock Screener
- Data
- Backtesting
- Free Tier
website: https://cleartape.ai/
---
