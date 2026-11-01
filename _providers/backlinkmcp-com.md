---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Machine-Readable API providing domain authority scores, backlink graphs, and link analytics.
  name: BacklinkMCP MCP API
  slug: backlinkmcp-mcp-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/backlinkmcp-com/plans/backlinkmcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/backlinkmcp-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/backlinkmcp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/backlinkmcp-com/llms/backlinkmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backlinkmcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/backlinkmcp-com/mcp/backlinkmcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backlinkmcp-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/backlinkmcp-com/well-known/backlinkmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backlinkmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/backlinkmcp-com/hosts/backlinkmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backlinkmcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backlinkmcp-com/vendors/backlinkmcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backlinkmcp-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://backlinkmcp.com/login
- group: auth
  href: https://artifacts.apis.io/backlinkmcp-com/security/backlinkmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backlinkmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backlinkmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://backlinkmcp.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://backlinkmcp.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backlinkmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backlinkmcp.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://backlinkmcp.com/articles
coverage:
  checked: '2026-10-30'
  detail: Provider offers MCP endpoint but no OpenAPI/AsyncAPI/GraphQL spec; docs are markdown without machine-readable contracts.
  evidence:
  - status: 200
    url: https://backlinkmcp.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: BacklinkMCP provides an MCP (Machine-Readable) and REST API that delivers domain authority scores, backlink graphs, and link analytics for AI agents and applications. The service offers real-time backlink data without requiring user sign‑up, enabling developers to integrate SEO intelligence directly into their tools. Features include domain rating, referring domain counts, top linkers, and bulk analysis, all accessible via simple HTTP endpoints. Updated regularly, the API aims to provide high‑trust link signals from authoritative sources while remaining affordable and easy to use.
image: https://backlinkmcp.com/og/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at backlinkmcp.com.
  name: backlinkmcp-com MCP Server
  slug: backlinkmcp-com-mcp-yml
modified: '2026-10-30'
name: backlinkmcp-com
nav: Providers
network: true
overview: 'backlinkmcp-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API, SEO, Backlink Data, Domain Authority, and AI Agents.


  backlinkmcp-com''s developer surface includes documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Backlinkmcp Com Plans Pricing
  plan_count: 2
  slug: backlinkmcp-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.2
    catalog_earned_first_party: 0.0
    catalog_gap: 75.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 56.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Backlinkmcp Com Domain Security
  slug: backlinkmcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: backlinkmcp-com
tags:
- API
- SEO
- Backlink Data
- Domain Authority
- AI Agents
- REST
- MCP
website: https://backlinkmcp.com/
---
