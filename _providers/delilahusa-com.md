---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Delilah's REST legislative data API (service "delilah-api") serving bills, roll-call votes, legislators, committees, hearings, sessions, statutes and 2026 election data for all 50 states, D.C. and Con
  name: Delilah API
  slug: delilah-api
- description: 'Free, read-only remote MCP server (streamable HTTP, registry name com.delilahusa/legislation) that gives AI clients 43 tools over Delilah''s legislative record — bills, votes, legislators, committees, '
  name: Delilah for Claude (Legislation MCP Server)
  slug: delilah-mcp
artifact_total: 7
common:
- group: build
  href: https://artifacts.apis.io/delilahusa-com/integrations/delilahusa-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/delilahusa-com-integration-edges.yml
- group: operate
  href: https://artifacts.apis.io/delilahusa-com/rate-limits/delilahusa-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delilahusa-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/delilahusa-com/plans/delilahusa-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delilahusa-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/delilahusa-com/conventions/delilahusa-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delilahusa-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/delilahusa-com/authentication/delilahusa-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delilahusa-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/delilahusa-com/llms/delilahusa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delilahusa-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/delilahusa-com/mcp/delilahusa-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delilahusa-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/delilahusa-com/hosts/delilahusa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delilahusa-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/delilahusa-com/vendors/delilahusa-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delilahusa-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/delilahusa-com/packages/delilahusa-com-packages.yml
  title: ''
  type: SDKs
  url: packages/delilahusa-com-packages.yml
- group: build
  href: https://artifacts.apis.io/delilahusa-com/packages/delilahusa-com-packages.yml
  title: ''
  type: Packages
  url: packages/delilahusa-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/delilahusa-com/security/delilahusa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delilahusa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delilahusa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://delilahusa.com/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://delilahusa.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://delilahusa.com/support
- group: start
  title: ''
  type: Login
  url: https://delilahusa.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://delilahusa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://delilahusa.com/privacy
- group: company
  title: ''
  type: About
  url: https://delilahusa.com/our-story
- group: other
  title: ''
  type: Leadership
  url: https://delilahusa.com/team
- group: company
  title: ''
  type: Newsroom
  url: https://delilahusa.com/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/delilah-technology-group/
created: '2026-11-05'
description: Delilah (Delilah Tech, Inc.) is an AI-for-legislation platform that lets people search, track and understand every bill, vote and legislator in all 50 US states, D.C. and Congress, in plain English with links to the official record. It offers a free Citizen App for iPhone and Android, Ask Delilah AI, Delilah Pro (a research and briefing platform for policy teams), an Incentives database of grants and tax credits written into law, and Delilah for Claude, a free, read-only remote MCP connector that answers questions from the legislative record.
image: https://delilahusa.com/icon.png
layout: provider
mcp_servers:
- description: Official free, read-only remote MCP server from Delilah (Delilah Tech, Inc.) over its legislative record. Tool list below is verbatim from a live tools/list call without credentials (shared free tier)
  name: Delilah for Claude (Legislation MCP Server)
  slug: delilah-for-claude-legislation-mcp-server
modified: '2026-11-05'
name: Delilah
nav: Providers
network: true
overview: 'Delilah is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legislation, Government, Civic Technology, and Artificial Intelligence.


  Delilah''s developer surface includes authentication, documentation, pricing, support, and 19 more developer resources.'
plans:
- name: Delilahusa Com Plans Pricing
  plan_count: 1
  slug: delilahusa-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Delilahusa Com Rate Limits
  slug: delilahusa-com-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 68.3
    operational_transparency: 21.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Delilahusa Com Authentication
  slug: delilahusa-com-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Delilahusa Com Domain Security
  slug: delilahusa-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: delilahusa-com
tags:
- Company
- Legislation
- Government
- Civic Technology
- Artificial Intelligence
- Policy
- MCP
- Public Data
website: https://delilahusa.com/
---
