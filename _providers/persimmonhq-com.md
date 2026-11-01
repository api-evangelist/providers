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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Persimmon is a brand‑intelligence MCP from Spann. It exposes deterministic momentum scoring, signal evidence, and competitive context for AI agents to call.
  name: Persimmon MCP API
  slug: persimmon-mcp-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/persimmonhq-com/plans/persimmonhq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/persimmonhq-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/persimmonhq-com/llms/persimmonhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/persimmonhq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/persimmonhq-com/mcp/persimmonhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/persimmonhq-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/persimmonhq-com/hosts/persimmonhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/persimmonhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/persimmonhq-com/vendors/persimmonhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/persimmonhq-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/persimmonhq-com/security/persimmonhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/persimmonhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://persimmonhq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://persimmonhq.com/pricing
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation pages are client‑side rendered JavaScript (Next.js), preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://persimmonhq.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Persimmon provides a brand‑intelligence MCP (Machine‑Consumable Product) for AI agents, delivering deterministic momentum indexes, strategic reads, and evidence‑backed competitive context. Users can query brand signals, receive structured strategic arguments, and access a public MCP registry. The platform offers free early‑access reads and paid tiers for strategists and teams, emphasizing data‑driven, auditable insights without fabricating scores.
image: https://persimmonhq.com/persimmon-hero.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.persimmonhq.com.
  name: persimmonhq-com MCP Server
  slug: persimmonhq-com-mcp-yml
modified: '2026-10-30'
name: persimmonhq-com
nav: Providers
network: true
overview: 'persimmonhq-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Brand-Intelligence, MCP, AI-Agents, Analytics, and Competitive-Intelligence.


  persimmonhq-com''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Persimmonhq Com Plans Pricing
  plan_count: 5
  slug: persimmonhq-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Persimmonhq Com Domain Security
  slug: persimmonhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: persimmonhq-com
tags:
- Brand-Intelligence
- MCP
- AI-Agents
- Analytics
- Competitive-Intelligence
website: https://persimmonhq.com/
---
