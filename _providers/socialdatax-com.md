---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 332
  human_in_the_loop: 0
  name: Socialdatax Com Agentic Access
  operation_count: 334
  slug: socialdatax-com-agentic-access
  summary_line: 334 operations · 332 acting
api_count: 1
apis:
- baseURL: https://mcp.socialdatax.com
  baseurl_source: declared
  description: The 互动列表 API from socialdatax-com — 167 operation(s) for 互动列表.
  name: socialdatax-com 互动列表 API
  slug: socialdatax-com-default-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/socialdatax-com/agentic-access/socialdatax-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/socialdatax-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/socialdatax-com/rules/socialdatax-com-rules.yml
  title: ''
  type: Spectral
  url: rules/socialdatax-com-rules.yml
- group: design
  href: https://artifacts.apis.io/socialdatax-com/json-ld/socialdatax-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/socialdatax-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/socialdatax-com/vocabulary/socialdatax-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/socialdatax-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/socialdatax-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/socialdatax-com/data-model/socialdatax-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/socialdatax-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/socialdatax-com/errors/socialdatax-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/socialdatax-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/socialdatax-com/conformance/socialdatax-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socialdatax-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socialdatax-com/llms/socialdatax-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialdatax-com-llms.txt
- group: build
  href: https://artifacts.apis.io/socialdatax-com/mcp/socialdatax-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/socialdatax-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/socialdatax-com/mcp/socialdatax-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/socialdatax-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/socialdatax-com/well-known/socialdatax-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/socialdatax-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/socialdatax-com/hosts/socialdatax-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialdatax-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/socialdatax-com/authentication/socialdatax-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socialdatax-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/socialdatax-com/security/socialdatax-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialdatax-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialdatax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://socialdatax.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://socialdatax.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://socialdatax.com/feishu/
- group: operate
  title: ''
  type: Support
  url: https://socialdatax.com/support
- group: company
  title: ''
  type: Blog
  url: https://socialdatax.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://socialdatax.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialdatax.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialdatax.com/privacy
created: '2026-10-29'
description: SocialDataX provides AI and workflow integration services that deliver social media data from platforms such as Xiaohongshu, Douyin, WeChat, Weibo, Bilibili, Kuaishou, Zhihu, Toutiao, Baidu Tieba, Instagram, X (Twitter), TikTok and YouTube. The platform offers content, creator, interaction and comment data through a unified API, supporting AI tools, Feishu plugins, and custom applications. Users obtain an API key, manage usage credits, and can access pricing details on the site. The service is targeted at developers building AI assistants, data analytics, and social listening solutions.
image: https://socialdatax.com/static/logo.png
jsonld:
- class_count: 1
  name: Socialdatax Com Context
  property_count: 7
  slug: socialdatax-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.socialdatax.com.
  name: socialdatax-com MCP Server
  slug: socialdatax-com-mcp-yml
modified: '2026-10-29'
name: socialdatax-com
nav: Providers
network: true
overview: 'socialdatax-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: 互动列表 API. Tagged areas include Company, Social Media, Data Integration, AI, and API.


  The socialdatax-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  socialdatax-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: socialdatax-com API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: socialdatax-com-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 19.7
    contract_quality: 54.8
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Socialdatax Com Authentication
  slug: socialdatax-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Socialdatax Com Domain Security
  slug: socialdatax-com-domain-security
  summary_line: TLSv1.2
skill_count: 1
skills:
- name: search-content
  slug: socialdatax-com-search
slug: socialdatax-com
tags:
- Company
- Social Media
- Data Integration
- AI
- API
website: https://socialdatax.com/
---
