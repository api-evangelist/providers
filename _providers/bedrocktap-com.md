---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://bedrocktap.com
  baseurl_source: declared
  description: Unified MCP API aggregating data from 250+ sources.
  name: BedrockTap API
  slug: bedrocktap-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bedrocktap-com/plans/bedrocktap-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bedrocktap-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bedrocktap-com/llms/bedrocktap-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bedrocktap-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bedrocktap-com/mcp/bedrocktap-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bedrocktap-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/bedrocktap-com/hosts/bedrocktap-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bedrocktap-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bedrocktap-com/vendors/bedrocktap-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bedrocktap-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bedrocktap-com/security/bedrocktap-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bedrocktap-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bedrocktap.com/
- group: docs
  title: ''
  type: APIReference
  url: https://bedrocktap.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://bedrocktap.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bedrocktap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bedrocktap.com/privacy
created: '2026-11-02'
description: BedrockTap provides a unified MCP server aggregating data from over 250 sources, offering agents a single schema and credential set to access diverse marketing and analytics data. It supports free tier access with no credit card, and paid plans for higher usage. The platform includes tools for SEO, social media, market research, and more, all accessible via a consistent API.
image: https://bedrocktap.com/opengraph-image.png?opengraph-image.10d2ypv12qwrr.png
layout: provider
mcp_servers:
- description: Remote MCP server at bedrocktap.com.
  name: BedrockTap MCP Server
  slug: bedrocktap-com-mcp-yml
modified: '2026-11-02'
name: BedrockTap
nav: Providers
network: true
overview: 'BedrockTap is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Data Aggregation, Marketing, and Analytics.


  BedrockTap''s developer surface includes API reference, pricing, and 9 more developer resources.'
plans:
- name: Bedrocktap Com Plans Pricing
  plan_count: 3
  slug: bedrocktap-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 3.6
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bedrocktap Com Domain Security
  slug: bedrocktap-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bedrocktap-com
tags:
- Company
- MCP
- Data Aggregation
- Marketing
- Analytics
website: https://bedrocktap.com/
---
