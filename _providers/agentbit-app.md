---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 80
  human_in_the_loop: 1
  name: Agentbit App Agentic Access
  operation_count: 114
  slug: agentbit-app-agentic-access
  summary_line: 114 operations · 80 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Account info and listing
  name: agentbit-app Google Ads - Account API
  slug: agentbit-app-google-ads-account-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Run account audits
  name: agentbit-app Google Ads - Audit API
  slug: agentbit-app-google-ads-audit-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Run custom GAQL queries
  name: agentbit-app Google Ads - Query API
  slug: agentbit-app-google-ads-query-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Read campaigns, keywords, ads, and performance data
  name: agentbit-app Google Ads - Read API
  slug: agentbit-app-google-ads-read-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Create, update, and manage Google Ads entities
  name: agentbit-app Google Ads - Write API
  slug: agentbit-app-google-ads-write-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Run Meta Ads account audits
  name: agentbit-app Meta Ads - Audit API
  slug: agentbit-app-meta-ads-audit-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Read Meta (Facebook/Instagram) campaigns and insights
  name: agentbit-app Meta Ads - Read API
  slug: agentbit-app-meta-ads-read-api
- baseURL: https://mcp.adwhiz.ai
  baseurl_source: declared
  description: Create and manage Meta Ads campaigns
  name: agentbit-app Meta Ads - Write API
  slug: agentbit-app-meta-ads-write-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/agentbit-app/agentic-access/agentbit-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentbit-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentbit-app/rules/agentbit-app-rules.yml
  title: ''
  type: Spectral
  url: rules/agentbit-app-rules.yml
- group: design
  href: https://artifacts.apis.io/agentbit-app/vocabulary/agentbit-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentbit-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentbit-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentbit-app/errors/agentbit-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentbit-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentbit-app/conformance/agentbit-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentbit-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentbit-app/llms/agentbit-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentbit-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentbit-app/mcp/agentbit-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentbit-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentbit-app/hosts/agentbit-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbit-app-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://agentbit.app/tools/category/security
- group: company
  title: ''
  type: Newsroom
  url: https://agentbit.app/tools/category/media
- group: auth
  href: https://artifacts.apis.io/agentbit-app/authentication/agentbit-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentbit-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentbit-app/security/agentbit-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbit-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbit.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentbit.app/tools
- group: docs
  title: ''
  type: Documentation
  url: https://agentbit.app/start
- group: docs
  title: ''
  type: APIReference
  url: https://agentbit.app/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentbit.app/start
- group: company
  title: ''
  type: Blog
  url: https://agentbit.app/blog
created: '2026-10-30'
description: AgentBIT provides a suite of pay‑per‑call API tools designed for AI agents, offering live web, business, finance, and security data without requiring signup or API keys. Users can invoke tools such as currency conversion, social profile lookup, and HMAC signing, each billed per request at a flat rate of $0.402. The platform hosts an OpenAPI specification and a catalog of available tools.
layout: provider
mcp_servers:
- description: Remote MCP server at agentbit.app.
  name: agentbit-app MCP Server
  slug: agentbit-app-mcp-yml
modified: '2026-10-30'
name: agentbit-app
nav: Providers
network: true
overview: 'agentbit-app publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Google Ads - Account API, Google Ads - Audit API, Google Ads - Query API, and 5 more. Tagged areas include Company, AI, Tools, Pay-per-call, and Data.


  The agentbit-app catalog on APIs.io includes 1 Spectral governance ruleset.


  agentbit-app''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: agentbit-app API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: agentbit-app-rules
scopes:
- name: Agentbit App Scopes
  scope_count: 0
  slug: agentbit-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 70.9
    contract_quality: 48.4
    developer_ergonomics: 58.8
    discoverability: 63.3
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentbit App Authentication
  slug: agentbit-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentbit App Domain Security
  slug: agentbit-app-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: add-ad-schedule
  slug: agentbit-app-add_ad_schedule
slug: agentbit-app
tags:
- Company
- AI
- Tools
- Pay-per-call
- Data
website: https://agentbit.app/
---
