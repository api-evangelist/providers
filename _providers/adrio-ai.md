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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Adrio provides an API for managing ad creative workflows.
  name: Adrio API
  slug: adrio-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/adrio-ai/plans/adrio-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adrio-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adrio-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/adrio-ai/changelog/adrio-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adrio-ai-changelog.yml
- group: agent
  href: https://artifacts.apis.io/adrio-ai/llms/adrio-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adrio-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/adrio-ai/mcp/adrio-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adrio-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adrio-ai/well-known/adrio-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adrio-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adrio-ai/hosts/adrio-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adrio-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adrio-ai/vendors/adrio-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adrio-ai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://adrio.ai/docs/changelog
- group: auth
  href: https://artifacts.apis.io/adrio-ai/security/adrio-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adrio-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adrio.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adrio.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://adrio.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://adrio.ai/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://adrio.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://adrio.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adrio.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adrio.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adrio.ai/legal/privacy
coverage:
  checked: '2026-11-01'
  detail: Public documentation exists but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://adrio.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Adrio is an AI‑powered creative studio that helps performance marketers design, generate, and launch Meta (Facebook and Instagram) ad creatives in seconds. Its Spark agent researches competitor ads, creates static and video assets, and automates testing and budgeting, offering a fast, data‑driven workflow for high‑converting campaigns.
image: https://adrio.ai/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.adrio.ai.
  name: Adrio MCP Server
  slug: adrio-ai-mcp-yml
modified: '2026-10-31'
name: Adrio
nav: Providers
network: true
overview: 'Adrio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, Creative, Meta, and Marketing.


  Adrio''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Adrio Ai Plans Pricing
  plan_count: 4
  slug: adrio-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Adrio Ai Rate Limits
  slug: adrio-ai-rate-limits
scopes:
- name: Adrio Ai Scopes
  scope_count: 0
  slug: adrio-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.5
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 31.1
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adrio Ai Authentication
  slug: adrio-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adrio Ai Domain Security
  slug: adrio-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adrio-ai
tags:
- Artificial Intelligence
- Advertising
- Creative
- Meta
- Marketing
website: https://adrio.ai/
---
