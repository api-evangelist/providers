---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Agency Growth platform, documented via MCP endpoint but no machine‑readable contract found.
  name: Agency Growth API
  slug: agency-growth-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/agencygrowth-com/plans/agencygrowth-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agencygrowth-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agencygrowth-com/llms/agencygrowth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agencygrowth-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agencygrowth-com/a2a/agencygrowth-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agencygrowth-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agencygrowth-com/mcp/agencygrowth-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agencygrowth-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agencygrowth-com/hosts/agencygrowth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agencygrowth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agencygrowth-com/vendors/agencygrowth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agencygrowth-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://agencygrowth.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://agencygrowth.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://agencygrowth.com/grok-bot-setup
- group: auth
  href: https://artifacts.apis.io/agencygrowth-com/security/agencygrowth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agencygrowth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agencygrowth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agencygrowth.com/mcp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agencygrowth.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agencygrowth.com/terms
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires POST and returns error, no OpenAPI or other spec discovered.
  evidence:
  - status: 405
    url: https://agencygrowth.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agency Growth provides AI-powered agents that help marketing agencies automate content creation, client outreach, and revenue growth. Their platform offers tools for generating social media posts, videos, and carousels, as well as AI-driven lead generation and client retention solutions. The service includes a customizable Growth Plan, white‑label AI agents, and integrations with popular tools, aiming to boost agency efficiency and scale without hiring additional staff.
image: https://agencygrowth.com/opengraph-image?2496c4313993d7e4
layout: provider
mcp_servers:
- description: Remote MCP server at agencygrowth.com.
  name: Agency Growth MCP Server
  slug: agencygrowth-com-mcp-yml
modified: '2026-10-31'
name: Agency Growth
nav: Providers
network: true
overview: 'Agency Growth is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Artificial Intelligence, Automation, Software-as-a-Service, and Agency.


  Agency Growth''s developer surface includes support, pricing, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Agencygrowth Com Plans Pricing
  plan_count: 5
  slug: agencygrowth-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 23.2
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
  name: Agencygrowth Com Domain Security
  slug: agencygrowth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agencygrowth-com
tags:
- Marketing
- Artificial Intelligence
- Automation
- Software-as-a-Service
- Agency
website: https://agencygrowth.com/
---
