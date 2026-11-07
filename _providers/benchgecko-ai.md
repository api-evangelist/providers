---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Benchgecko Ai Agentic Access
  operation_count: 6
  slug: benchgecko-ai-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://benchgecko.ai
  baseurl_source: declared
  description: BenchGecko's own tests (CC BY 4.0)
  name: BenchGecko Gecko Tests API
  slug: benchgecko-ai-gecko-tests-api
- baseURL: https://benchgecko.ai
  baseurl_source: declared
  description: Live model catalog, scores and prices
  name: BenchGecko Models API
  slug: benchgecko-ai-models-api
- baseURL: https://benchgecko.ai
  baseurl_source: declared
  description: Price history and per-provider offers
  name: BenchGecko Pricing API
  slug: benchgecko-ai-pricing-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/benchgecko-ai/agentic-access/benchgecko-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/benchgecko-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/benchgecko-ai/rules/benchgecko-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/benchgecko-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/benchgecko-ai/vocabulary/benchgecko-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/benchgecko-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/benchgecko-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/benchgecko-ai/conformance/benchgecko-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/benchgecko-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/benchgecko-ai/llms/benchgecko-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benchgecko-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/benchgecko-ai/mcp/benchgecko-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/benchgecko-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/benchgecko-ai/mcp/benchgecko-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/benchgecko-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/benchgecko-ai/hosts/benchgecko-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benchgecko-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/benchgecko-ai/vendors/benchgecko-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benchgecko-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/benchgecko-ai/packages/benchgecko-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/benchgecko-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/benchgecko-ai/packages/benchgecko-ai-packages.yml
  title: ''
  type: Packages
  url: packages/benchgecko-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://benchgecko.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://benchgecko.ai/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://benchgecko.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://benchgecko.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://benchgecko.ai/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://benchgecko.ai/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://benchgecko.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://benchgecko.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/benchgecko-ai/security/benchgecko-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benchgecko-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://benchgecko.ai/
- group: company
  title: ''
  type: Blog
  url: https://benchgecko.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benchgecko
created: '2026-11-02'
description: BenchGecko provides an AI economy dashboard that tracks models, agents, pricing, companies, and market trends. It offers the Gecko Pulse, Bubble Index, mindshare metrics, frontier race analysis, and a live feed of new AI models and price changes, updated daily. The platform aims to give fresh intelligence for stakeholders in the artificial intelligence landscape.
image: https://benchgecko.ai/logo-final-combo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at benchgecko.ai.
  name: BenchGecko MCP Server
  slug: benchgecko-ai-mcp-yml
modified: '2026-11-02'
name: BenchGecko
nav: Providers
network: true
overview: 'BenchGecko publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Gecko Tests API, Models API, and Pricing API. Tagged areas include Artificial Intelligence, Economy, Dashboards, Analytics, and Market Intelligence.


  The BenchGecko catalog on APIs.io includes 1 Spectral governance ruleset.


  BenchGecko''s developer surface includes pricing, changelog, API reference, engineering blog, and 20 more developer resources.'
plans:
- name: Benchgecko Ai Plans Pricing
  plan_count: 0
  slug: benchgecko-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Benchgecko Ai Rate Limits
  slug: benchgecko-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: BenchGecko API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: benchgecko-ai-rules
scopes:
- name: Benchgecko Ai Scopes
  scope_count: 0
  slug: benchgecko-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 43.5
    developer_ergonomics: 23.1
    discoverability: 65.8
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Benchgecko Ai Authentication
  slug: benchgecko-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Benchgecko Ai Domain Security
  slug: benchgecko-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: compare-models
  slug: compare-models
- name: model-details
  slug: model-details
- name: model-search
  slug: model-search
slug: benchgecko-ai
tags:
- Artificial Intelligence
- Economy
- Dashboards
- Analytics
- Market Intelligence
website: https://benchgecko.ai/
---
