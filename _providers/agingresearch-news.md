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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
  score: 28.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgingResearch.News provides a news aggregation service for aging research papers. The website describes the service but no public machine‑readable API contract was found.
  name: AgingResearch.News API
  slug: agingresearch-news-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/agingresearch-news/plans/agingresearch-news-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agingresearch-news-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agingresearch-news/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/agingresearch-news/llms/agingresearch-news-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agingresearch-news-llms.txt
- group: other
  href: https://artifacts.apis.io/agingresearch-news/a2a/agingresearch-news-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agingresearch-news-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agingresearch-news/mcp/agingresearch-news-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agingresearch-news-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agingresearch-news/well-known/agingresearch-news-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agingresearch-news-well-known.yml
- group: other
  href: https://artifacts.apis.io/agingresearch-news/hosts/agingresearch-news-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agingresearch-news-hosts.yml
- group: other
  href: https://artifacts.apis.io/agingresearch-news/vendors/agingresearch-news-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agingresearch-news-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agingresearch.news/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agingresearch.news/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://agingresearch.news/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://agingresearch.news/news
- group: docs
  title: ''
  type: APIReference
  url: https://agingresearch.news/developers
- group: auth
  href: https://artifacts.apis.io/agingresearch-news/security/agingresearch-news-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agingresearch-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agingresearch.news/
coverage:
  checked: '2026-11-01'
  detail: The site is a Next.js app that renders content via JavaScript, preventing machine‑readable discovery of an API contract.
  evidence:
  - status: 200
    url: https://agingresearch.news
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: 'agingresearch-news is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://agingresearch.news/og/site/home/card.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at agingresearch.news.
  name: AgingResearch.News MCP Server
  slug: agingresearch-news-mcp-yml
modified: '2026-11-01'
name: AgingResearch.News
nav: Providers
network: true
overview: 'AgingResearch.News is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aging, Longevity, Artificial Intelligence, and Research.


  AgingResearch.News'' developer surface includes pricing, API reference, and 13 more developer resources.'
plans:
- name: Agingresearch News Plans Pricing
  plan_count: 3
  slug: agingresearch-news-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 5.4
    discoverability: 49.2
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agingresearch News Domain Security
  slug: agingresearch-news-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-paper
  slug: agingresearch-news-getPaper-skill
slug: agingresearch-news
tags:
- Company
- Aging
- Longevity
- Artificial Intelligence
- Research
- News
website: https://agingresearch.news/
---
