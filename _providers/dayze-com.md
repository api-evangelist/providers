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
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Days lived, notable people knowledge packs, and MCP life-context tools.
  name: Dayze API
  slug: dayze-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/dayze-com/plans/dayze-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dayze-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dayze-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dayze-com/conformance/dayze-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dayze-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dayze-com/llms/dayze-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dayze-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dayze-com/mcp/dayze-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dayze-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dayze-com/mcp/dayze-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dayze-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dayze-com/well-known/dayze-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dayze-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dayze-com/hosts/dayze-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dayze-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dayze-com/vendors/dayze-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dayze-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dayze.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dayze.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dayze.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dayze.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://dayze.com/news
- group: start
  title: ''
  type: Login
  url: https://dayze.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://dayze.com/docs
- group: company
  title: ''
  type: Blog
  url: https://dayze.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://dayze.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/dayze-com/security/dayze-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dayze-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dayze.com/
created: '2026-11-05'
description: 'dayze-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://dayze.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at dayze.com.
  name: dayze-com MCP Server
  slug: dayze-com-mcp-yml
modified: '2026-11-05'
name: dayze-com
nav: Providers
network: true
overview: 'dayze-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Context, Personal CRM, and Life graph.


  dayze-com''s developer surface includes support, pricing, documentation, engineering blog, getting-started guide, and 15 more developer resources.'
plans:
- name: Dayze Com Plans Pricing
  plan_count: 3
  slug: dayze-com-plans-pricing
random_paper: 17
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dayze Com Domain Security
  slug: dayze-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: notable-search
  slug: dayze-com-notable-search
slug: dayze-com
tags:
- AI Context
- Personal CRM
- Life graph
website: https://dayze.com/
---
