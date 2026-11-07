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
  band: agent-aware
  dimensions:
    agent_card: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adweave-ai/plans/adweave-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adweave-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adweave-ai/llms/adweave-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adweave-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/adweave-ai/mcp/adweave-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adweave-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adweave-ai/well-known/adweave-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adweave-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adweave-ai/hosts/adweave-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adweave-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adweave-ai/vendors/adweave-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adweave-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adweave.ai/tos
- group: start
  title: ''
  type: Login
  url: https://adweave.ai/auth/login
- group: auth
  href: https://artifacts.apis.io/adweave-ai/security/adweave-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adweave-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adweave.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adweave.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.adweave.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adweave.ai/privacy
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found after probing common spec endpoints on api.adweave.ai and adweave.ai.
  evidence:
  - status: 404
    url: https://api.adweave.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AdWeave is an AI-powered media buying platform that connects Meta and TikTok ad accounts, offering campaign diagnosis, buyer personas, optimization recommendations, and a Claude plugin that generates creatives, launches campaigns, and closes the feedback loop—all from within Claude.
image: https://www.adweave.ai/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adweave.ai.
  name: AdWeave MCP Server
  slug: adweave-ai-mcp-yml
modified: '2026-10-31'
name: AdWeave
nav: Providers
network: true
overview: 'AdWeave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, Media Buying, Claude Plugin, and Marketing.


  AdWeave''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Adweave Ai Plans Pricing
  plan_count: 2
  slug: adweave-ai-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adweave Ai Domain Security
  slug: adweave-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adweave-ai
tags:
- Artificial Intelligence
- Advertising
- Media Buying
- Claude Plugin
- Marketing
website: https://adweave.ai/
---
