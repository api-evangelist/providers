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
api_count: 1
apis:
- description: Agenlify MCP provides a Machine-Readable Control Protocol for interacting with Agenlify's AI agent directory.
  name: Agenlify MCP
  slug: agenlify-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/agenlify-ai/plans/agenlify-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenlify-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agenlify-ai/mcp/agenlify-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenlify-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/agenlify-ai/hosts/agenlify-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenlify-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenlify-ai/vendors/agenlify-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenlify-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenlify.ai/terms/
- group: operate
  title: ''
  type: Support
  url: https://agenlify.ai/categories/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenlify.ai/privacy/
- group: start
  title: ''
  type: Login
  url: https://agenlify.ai/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://agenlify.ai/compare/?agents=intercom-fin,tidio-lyro,gorgias-ai-agent
- group: auth
  href: https://artifacts.apis.io/agenlify-ai/security/agenlify-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenlify-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenlify.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agenlify.ai/developers/mcp/
- group: company
  title: ''
  type: Blog
  url: https://agenlify.ai/blog/
- group: company
  title: ''
  type: About
  url: https://agenlify.ai/about/
coverage:
  checked: '2026-11-01'
  detail: The provider only offers an MCP endpoint requiring POST, with no public OpenAPI or other machine-readable contract.
  evidence:
  - status: 405
    url: https://agenlify.ai/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agenlify is a directory that helps individuals and small teams choose AI agents for specific tasks. It catalogs over 470 AI products across categories like research, building, content creation, data analysis, automation, and customer support. The site provides detailed reviews, pricing, setup limits, and source links, aiming to simplify the selection process for AI tools.
image: https://agenlify.ai/social.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agenlify.ai.
  name: Agenlify MCP Server
  slug: agenlify-ai-mcp-yml
modified: '2026-10-31'
name: Agenlify
nav: Providers
network: true
overview: 'Agenlify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Directory, Tools, Comparison, and Agents.


  Agenlify''s developer surface includes support, getting-started guide, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Agenlify Ai Plans Pricing
  plan_count: 5
  slug: agenlify-ai-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agenlify Ai Domain Security
  slug: agenlify-ai-domain-security
  summary_line: TLSv1.3
slug: agenlify-ai
tags:
- Artificial Intelligence
- Directory
- Tools
- Comparison
- Agents
website: https://agenlify.ai/
---
