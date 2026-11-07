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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Zhiyong Dev Agentic Access
  operation_count: 14
  slug: zhiyong-dev-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Agent API from zhiyong-dev — 1 operation(s) for agent.
  name: zhiyong-dev Agent API
  slug: zhiyong-dev-agent-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Agent Discovery.json API from zhiyong-dev — 1 operation(s) for agent discovery.json.
  name: zhiyong-dev Agent Discovery.json API
  slug: zhiyong-dev-agent-discovery-json-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Agent Feedback API from zhiyong-dev — 1 operation(s) for agent feedback.
  name: zhiyong-dev Agent Feedback API
  slug: zhiyong-dev-agent-feedback-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Agent Observation API from zhiyong-dev — 1 operation(s) for agent observation.
  name: zhiyong-dev Agent Observation API
  slug: zhiyong-dev-agent-observation-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Agent Task API from zhiyong-dev — 1 operation(s) for agent task.
  name: zhiyong-dev Agent Task API
  slug: zhiyong-dev-agent-task-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Agent Topic API from zhiyong-dev — 1 operation(s) for agent topic.
  name: zhiyong-dev Agent Topic API
  slug: zhiyong-dev-agent-topic-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Community API from zhiyong-dev — 2 operation(s) for community.
  name: zhiyong-dev Community API
  slug: zhiyong-dev-community-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Entity Feedback API from zhiyong-dev — 1 operation(s) for entity feedback.
  name: zhiyong-dev Entity Feedback API
  slug: zhiyong-dev-entity-feedback-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Health API from zhiyong-dev — 1 operation(s) for health.
  name: zhiyong-dev Health API
  slug: zhiyong-dev-health-api
- baseURL: https://zhiyong.dev
  baseurl_source: declared
  description: The Search API from zhiyong-dev — 1 operation(s) for search.
  name: zhiyong-dev Search API
  slug: zhiyong-dev-search-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/zhiyong-dev/agentic-access/zhiyong-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zhiyong-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/zhiyong-dev/rules/zhiyong-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/zhiyong-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/zhiyong-dev/json-ld/zhiyong-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zhiyong-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/zhiyong-dev/vocabulary/zhiyong-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zhiyong-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/zhiyong-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zhiyong-dev/data-model/zhiyong-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zhiyong-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/zhiyong-dev/errors/zhiyong-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zhiyong-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zhiyong-dev/conformance/zhiyong-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zhiyong-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zhiyong-dev/llms/zhiyong-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zhiyong-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/zhiyong-dev/a2a/zhiyong-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zhiyong-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/zhiyong-dev/mcp/zhiyong-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zhiyong-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/zhiyong-dev/well-known/zhiyong-dev-easyshiftplan-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zhiyong-dev-easyshiftplan-security.txt
- group: agent
  href: https://artifacts.apis.io/zhiyong-dev/well-known/zhiyong-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zhiyong-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/zhiyong-dev/hosts/zhiyong-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zhiyong-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/zhiyong-dev/vendors/zhiyong-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zhiyong-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zhiyong.dev/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zhiyong.dev/privacy.html
- group: auth
  href: https://artifacts.apis.io/zhiyong-dev/security/zhiyong-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zhiyong-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kg.zhiyong.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://zhiyong.dev/openapi.json
  - status: null
    url: https://zhiyong.dev/mcp
  - status: null
    url: https://forecast.zhiyong.dev/openapi.json
  - status: null
    url: https://kg.zhiyong.dev/openapi.json
  - status: null
    url: https://kg.zhiyong.dev/mcp
  - status: 401
    url: https://easyshiftplan.zhiyong.dev/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Zhiyong Dev is a technology-focused company specializing in software development tools and API services. The company provides a suite of developer-oriented platforms, including API documentation, SDK generation, and integration solutions aimed at streamlining application development workflows. Their offerings target both enterprise and individual developers seeking robust, scalable, and well-documented APIs to accelerate product delivery and enhance system interoperability across diverse environments.
image: https://zhiyong.dev/zhiyong-ai-icon.jpg
json_schemas:
- name: AgentFeedbackDiscoveryResponse
  property_count: 8
  slug: zhiyong-dev-agent-feedback-discovery-response
- name: CommunityFeedResponse
  property_count: 8
  slug: zhiyong-dev-community-feed-response
- name: CommunityThreadResponse
  property_count: 13
  slug: zhiyong-dev-community-thread-response
- name: CommunityTopicsResponse
  property_count: 7
  slug: zhiyong-dev-community-topics-response
- name: Health
  property_count: 5
  slug: zhiyong-dev-health
- name: SearchResponse
  property_count: 5
  slug: zhiyong-dev-search-response
jsonld:
- class_count: 14
  name: Zhiyong Dev Context
  property_count: 77
  slug: zhiyong-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at zhiyong.dev.
  name: zhiyong-dev MCP Server
  slug: zhiyong-dev-mcp-yml
modified: '2026-10-29'
name: zhiyong-dev
nav: Providers
network: true
overview: 'zhiyong-dev publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Agent Discovery.json API, Agent Feedback API, and 7 more. Tagged areas include Company, Software, Developer Tools, and Integration.


  The zhiyong-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: zhiyong-dev API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: zhiyong-dev-rules
scopes:
- name: Zhiyong Dev Scopes
  scope_count: 0
  slug: zhiyong-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 57.3
    developer_ergonomics: 1.8
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zhiyong-dev/zhiyong-dev-2026-11-03T150520.png
security:
- kind: authentication
  name: Zhiyong Dev Authentication
  slug: zhiyong-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zhiyong Dev Domain Security
  slug: zhiyong-dev-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: agent-discovery
  slug: zhiyong-dev-agent-discovery
- name: forecast
  slug: zhiyong-dev-forecast
- name: semantic-search
  slug: zhiyong-dev-semantic-search
- name: zhiyong-dev-submit-agent-observation
  slug: zhiyong-dev-submit-agent-observation
slug: zhiyong-dev
tags:
- Company
- Software
- Developer Tools
- Integration
website: https://kg.zhiyong.dev/
---
