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
    agent_card: flavored
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
  score: 4.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/carbonaa-org/llms/carbonaa-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carbonaa-org-llms.txt
- group: other
  href: https://artifacts.apis.io/carbonaa-org/a2a/carbonaa-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/carbonaa-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/carbonaa-org/mcp/carbonaa-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carbonaa-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/carbonaa-org/hosts/carbonaa-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonaa-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/carbonaa-org/vendors/carbonaa-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbonaa-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/carbonaa-org/security/carbonaa-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonaa-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonaa.org/
- group: docs
  title: ''
  type: Documentation
  url: https://carbonaa.org/Documentation
- group: company
  title: ''
  type: Blog
  url: https://carbonaa.org/Blog
- group: commercial
  title: ''
  type: Pricing
  url: https://carbonaa.org/CBAMPricingPage
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://carbonaa.org/mcp
  - status: 200
    url: https://carbonaa.org/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Carbonaa is a SaaS platform for climate and carbon management, offering carbon footprint assessments, EU CBAM compliance, satellite-powered environmental intelligence, automated carbon offsetting, and AI-driven data infrastructure. It serves enterprises seeking comprehensive sustainability solutions and regulatory reporting.
image: https://qtrypzzcjebvfcihiynt.supabase.co/storage/v1/render/image/public/base44-prod/public/698e01874e509203d1af5b00/b1609daf0_ChatGPTImageFeb13202611_37_09PM.png?width=1200&height=630&resize=contain
layout: provider
mcp_servers:
- description: Remote MCP server at carbonaa.org.
  name: Carbonaa MCP Server
  slug: carbonaa-org-mcp-yml
modified: '2026-11-03'
name: Carbonaa
nav: Providers
network: true
overview: 'Carbonaa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Climate, Carbon Management, Sustainability, and Environmental Data.


  Carbonaa''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbonaa Org Domain Security
  slug: carbonaa-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: carbonaa-org
tags:
- Software-as-a-Service
- Climate
- Carbon Management
- Sustainability
- Environmental Data
website: https://carbonaa.org/
---
