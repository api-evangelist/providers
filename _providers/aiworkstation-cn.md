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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 101
  human_in_the_loop: 9
  name: Aiworkstation Cn Agentic Access
  operation_count: 211
  slug: aiworkstation-cn-agentic-access
  summary_line: 211 operations · 101 acting · 9 human-in-the-loop
api_count: 1
apis:
- description: The AI工作站·会话入口 API from AI Workstation — 141 operation(s) for ai工作站·会话入口.
  name: AI Workstation AI工作站·会话入口 API
  slug: aiworkstation-cn-ai-api
- description: The ai-douyin-account-audit API from AI Workstation — 20 operation(s) for ai-douyin-account-audit.
  name: AI Workstation AI Douyin Account Audit API
  slug: aiworkstation-cn-ai-douyin-account-audit-api
- description: The Ai Growth Guide API from AI Workstation — 1 operation(s) for ai growth guide.
  name: AI Workstation Ai Growth Guide API
  slug: aiworkstation-cn-ai-growth-guide-api
- description: The ai-topic-radar API from AI Workstation — 8 operation(s) for ai-topic-radar.
  name: AI Workstation AI Topic Radar API
  slug: aiworkstation-cn-ai-topic-radar-api
- description: The analytics API from AI Workstation — 2 operation(s) for analytics.
  name: AI Workstation Analytics API
  slug: aiworkstation-cn-analytics-api
- description: The gaokao API from AI Workstation — 12 operation(s) for gaokao.
  name: AI Workstation Gaokao API
  slug: aiworkstation-cn-gaokao-api
- description: The system API from AI Workstation — 1 operation(s) for system.
  name: AI Workstation System API
  slug: aiworkstation-cn-system-api
- description: The tts API from AI Workstation — 1 operation(s) for tts.
  name: AI Workstation Tts API
  slug: aiworkstation-cn-tts-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/aiworkstation-cn/agentic-access/aiworkstation-cn-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aiworkstation-cn-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aiworkstation-cn/rules/aiworkstation-cn-rules.yml
  title: ''
  type: Spectral
  url: rules/aiworkstation-cn-rules.yml
- group: design
  href: https://artifacts.apis.io/aiworkstation-cn/json-ld/aiworkstation-cn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiworkstation-cn-context.jsonld
- group: design
  href: https://artifacts.apis.io/aiworkstation-cn/vocabulary/aiworkstation-cn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiworkstation-cn-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aiworkstation-cn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aiworkstation-cn/data-model/aiworkstation-cn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiworkstation-cn-data-model.yml
- group: design
  href: https://artifacts.apis.io/aiworkstation-cn/errors/aiworkstation-cn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiworkstation-cn-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aiworkstation-cn/conformance/aiworkstation-cn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiworkstation-cn-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiworkstation-cn/llms/aiworkstation-cn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiworkstation-cn-llms.txt
- group: other
  href: https://artifacts.apis.io/aiworkstation-cn/hosts/aiworkstation-cn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiworkstation-cn-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aiworkstation-cn/security/aiworkstation-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiworkstation-cn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiworkstation.cn/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiworkstation.cn/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiworkstation.cn/terms/
- group: commercial
  title: ''
  type: Pricing
  url: https://aiworkstation.cn/pricing/
- group: operate
  title: ''
  type: Support
  url: https://aiworkstation.cn/support/
created: '2026-11-01'
description: AI工作站提供多模型 AI 对话、文件分析、图片理解、导出、长期记忆和 AI 导师工作流。Topic Intelligence 和 AI 工作站公开功能的安装、故障和安全联系方式。正式安装包只从 GitHub Release 下载。报告问题时请提供版本、宿主产品、操作系统、已隐去敏感信息的错误和最小复现步骤。安装和功能问题可使用 GitHub Issues；安全漏洞、隐私或合作问题请发送邮件，不要在公开 Issue 中粘贴凭据或对话正文。
image: https://aiworkstation.cn/favicon.ico
json_schemas:
- name: AIChatActionRequest
  property_count: 14
  slug: aiworkstation-cn-aichat-action-request
- name: AIChatRequest
  property_count: 17
  slug: aiworkstation-cn-aichat-request
- name: AIGeneratedFileRequest
  property_count: 16
  slug: aiworkstation-cn-aigenerated-file-request
- name: AIImageWorkbenchTaskRequest
  property_count: 23
  slug: aiworkstation-cn-aiimage-workbench-task-request
- name: TopicFeedResponse
  property_count: 20
  slug: aiworkstation-cn-topic-feed-response
- name: TopicInsightResponse
  property_count: 21
  slug: aiworkstation-cn-topic-insight-response
jsonld:
- class_count: 88
  name: Aiworkstation Cn Context
  property_count: 325
  slug: aiworkstation-cn-context
layout: provider
modified: '2026-11-01'
name: AI Workstation
nav: Providers
network: true
overview: 'AI Workstation publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI工作站·会话入口 API, AI Douyin Account Audit API, Ai Growth Guide API, and 5 more. Tagged areas include Artificial Intelligence, Workstation, Multi-Model, Conversations, and File Analysis.


  The AI Workstation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Workstation''s developer surface includes pricing, support, and 14 more developer resources.'
plans:
- name: Aiworkstation Cn Plans Pricing
  plan_count: 0
  slug: aiworkstation-cn-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Aiworkstation Cn Rate Limits
  slug: aiworkstation-cn-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AI Workstation API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 1
  slug: aiworkstation-cn-rules
scopes:
- name: Aiworkstation Cn Scopes
  scope_count: 0
  slug: aiworkstation-cn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 13.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiworkstation Cn Authentication
  slug: aiworkstation-cn-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aiworkstation Cn Domain Security
  slug: aiworkstation-cn-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: analytics-hit
  slug: aiworkstation-cn-analytics-hit
- name: growth-guide-overview
  slug: aiworkstation-cn-growth-guide-overview
- name: tts-generate
  slug: aiworkstation-cn-tts-generate
slug: aiworkstation-cn
tags:
- Artificial Intelligence
- Workstation
- Multi-Model
- Conversations
- File Analysis
- Image-Understanding
- Long-Term Memory
- Assistant
website: https://aiworkstation.cn/
---
