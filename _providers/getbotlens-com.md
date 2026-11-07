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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Model Context Protocol (MCP) API providing tools for article search and retrieval.
  name: MCP
  slug: mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/getbotlens-com/plans/getbotlens-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getbotlens-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/getbotlens-com/llms/getbotlens-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getbotlens-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/getbotlens-com/mcp/getbotlens-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getbotlens-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/getbotlens-com/well-known/getbotlens-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getbotlens-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getbotlens-com/hosts/getbotlens-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getbotlens-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getbotlens-com/vendors/getbotlens-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getbotlens-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getbotlens.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://getbotlens.com/get-started/
- group: auth
  href: https://artifacts.apis.io/getbotlens-com/security/getbotlens-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getbotlens-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getbotlens.com/
created: '2026-10-29'
description: BotLens identifies every visitor — human, bot, AI agent, or threat. See what’s polluting your funnel. Expose what’s slipping past your security. Know which AI shopping agents belong and which ones don’t. Insights for your next move. Your Analytics Has a Bot Problem. We Fixed It.
image: https://getbotlens.com/wp-content/uploads/2026/04/Botlens-final-logo-02-e1776169355204.png
layout: provider
mcp_servers:
- description: Remote MCP server at getbotlens.mcp.getbotlens.com.
  name: getbotlens-com MCP Server
  slug: getbotlens-com-mcp-yml
modified: '2026-10-29'
name: getbotlens-com
nav: Providers
network: true
overview: 'getbotlens-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bot Detection, Analytics, Security, Artificial Intelligence, and Web.


  getbotlens-com''s developer surface includes getting-started guide and 9 more developer resources.'
plans:
- name: Getbotlens Com Plans Pricing
  plan_count: 2
  slug: getbotlens-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.3
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getbotlens-com/getbotlens-com-2026-11-03T132650.png
security:
- kind: domain-security
  name: Getbotlens Com Domain Security
  slug: getbotlens-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getbotlens-com
tags:
- Bot Detection
- Analytics
- Security
- Artificial Intelligence
- Web
website: https://getbotlens.com/
---
