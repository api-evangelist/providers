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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cardvolume Com Agentic Access
  operation_count: 5
  slug: cardvolume-com-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Read‑only public data API for verified trading‑card sales.
  name: CardVolume API
  slug: cardvolume-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/cardvolume-com/agentic-access/cardvolume-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cardvolume-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cardvolume-com/rules/cardvolume-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cardvolume-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cardvolume-com/errors/cardvolume-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cardvolume-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cardvolume-com/conformance/cardvolume-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardvolume-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cardvolume-com/llms/cardvolume-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardvolume-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cardvolume-com/mcp/cardvolume-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cardvolume-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cardvolume-com/well-known/cardvolume-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardvolume-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cardvolume-com/hosts/cardvolume-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardvolume-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardvolume-com/vendors/cardvolume-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardvolume-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardvolume.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardvolume.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://cardvolume.com/learn/pricing/
- group: docs
  title: ''
  type: APIReference
  url: https://cardvolume.com/developers/
- group: auth
  href: https://artifacts.apis.io/cardvolume-com/security/cardvolume-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardvolume-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardvolume.com/
created: '2026-11-03'
description: CardVolume provides documented sales, graded populations and plain‑language research for trading cards that collectors search for. It tracks every price to a sale, publishes market indexes and record sales for categories such as Pokémon, Magic, Yu‑Gi‑Oh! and sports cards, and shows sources and data timestamps. The service does not display asking prices or averages and marks data as “unknown” when evidence is thin.
layout: provider
mcp_servers:
- description: Remote MCP server at cardvolume.com.
  name: CardVolume MCP Server
  slug: cardvolume-com-mcp-yml
modified: '2026-11-03'
name: CardVolume
nav: Providers
network: true
overview: 'CardVolume is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CardVolume, Trading Cards, Collectibles, and Market Data.


  The CardVolume catalog on APIs.io includes 1 Spectral governance ruleset.


  CardVolume''s developer surface includes pricing, API reference, and 13 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: CardVolume API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: cardvolume-com-rules
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardvolume Com Domain Security
  slug: cardvolume-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardvolume-com
tags:
- CardVolume
- Trading Cards
- Collectibles
- Market Data
website: https://cardvolume.com/
---
