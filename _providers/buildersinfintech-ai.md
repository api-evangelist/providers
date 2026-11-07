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
- group: agent
  href: https://artifacts.apis.io/buildersinfintech-ai/llms/buildersinfintech-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildersinfintech-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildersinfintech-ai/mcp/buildersinfintech-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buildersinfintech-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/buildersinfintech-ai/well-known/buildersinfintech-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildersinfintech-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildersinfintech-ai/hosts/buildersinfintech-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildersinfintech-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildersinfintech-ai/vendors/buildersinfintech-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildersinfintech-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildersinfintech.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://buildersinfintech.ai/news
- group: auth
  href: https://artifacts.apis.io/buildersinfintech-ai/security/buildersinfintech-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildersinfintech-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildersinfintech.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://buildersinfintech.ai/mcp
  - status: 200
    url: https://buildersinfintech.ai/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Builders in Fintech is a global fintech news and funding database that aggregates daily news, weekly podcasts, funding rounds, company data, and agent‑ready datasets. It provides a searchable platform for fintech builders, investors, and analysts to discover companies, funding events, and market trends across the industry. The site offers data feeds, MCP connectors, and open‑source resources for integration into AI agents and applications.
image: https://yvhyqhbnhkfoziycwapm.supabase.co/storage/v1/object/public/media/brand/566fe486-8eb5-4945-a57c-2f2365cf72a7.png
layout: provider
mcp_servers:
- description: Remote MCP server at buildersinfintech.ai.
  name: Builders in Fintech MCP Server
  slug: buildersinfintech-ai-mcp-yml
modified: '2026-11-03'
name: Builders in Fintech
nav: Providers
network: true
overview: Builders in Fintech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, News, Funding, Data, and Artificial Intelligence.
random_paper: 17
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.2
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildersinfintech Ai Domain Security
  slug: buildersinfintech-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildersinfintech-ai
tags:
- Fintech
- News
- Funding
- Data
- Artificial Intelligence
website: https://buildersinfintech.ai/
---
