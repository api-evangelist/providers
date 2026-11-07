---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://awardcast.ai
  baseurl_source: declared
  description: MCP tool list providing search, fetch, and forecasting utilities for US federal contract data.
  name: AwardCast AI MCP
  slug: awardcast-ai-mcp
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/awardcast-ai/plans/awardcast-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/awardcast-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/awardcast-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/awardcast-ai/llms/awardcast-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awardcast-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/awardcast-ai/mcp/awardcast-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awardcast-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/awardcast-ai/hosts/awardcast-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awardcast-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/awardcast-ai/vendors/awardcast-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/awardcast-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awardcast.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awardcast.ai/legal/privacy
- group: auth
  href: https://artifacts.apis.io/awardcast-ai/security/awardcast-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awardcast-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awardcast.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://awardcast.ai/pricing
created: '2026-11-02'
description: AwardCast AI forecasts the U.S. federal award price range, the competition you should expect, and how agencies have paid before, drawing from millions of real federal awards. The platform helps contractors and agencies make data‑driven bidding decisions.
image: https://awardcast.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at awardcast.ai.
  name: AwardCast AI MCP Server
  slug: awardcast-ai-mcp-yml
modified: '2026-11-02'
name: AwardCast AI
nav: Providers
network: true
overview: 'AwardCast AI is listed with 1 API on the [APIs.io](https://apis.io/) network: MCP. Tagged areas include Artificial Intelligence, Forecasting, Government, Contracts, and Pricing.


  AwardCast AI''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Awardcast Ai Plans Pricing
  plan_count: 5
  slug: awardcast-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Awardcast Ai Rate Limits
  slug: awardcast-ai-rate-limits
scopes:
- name: Awardcast Ai Scopes
  scope_count: 0
  slug: awardcast-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 6.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 27.7
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awardcast Ai Authentication
  slug: awardcast-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Awardcast Ai Domain Security
  slug: awardcast-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: awardcast-ai-search
  slug: awardcast-ai-search
slug: awardcast-ai
tags:
- Artificial Intelligence
- Forecasting
- Government
- Contracts
- Pricing
website: https://awardcast.ai/
---
