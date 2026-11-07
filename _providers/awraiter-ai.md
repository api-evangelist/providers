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
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 2
  name: Awraiter Ai Agentic Access
  operation_count: 66
  slug: awraiter-ai-agentic-access
  summary_line: 66 operations · 29 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://awraiter.ai
  baseurl_source: declared
  description: Self-description.
  name: AwrAiter Catalog API
  slug: awraiter-ai-catalog-api
- baseURL: https://awraiter.ai
  baseurl_source: declared
  description: Tools that change nothing.
  name: AwrAiter Read API
  slug: awraiter-ai-read-api
- baseURL: https://awraiter.ai
  baseurl_source: declared
  description: Tools that create, change or schedule something.
  name: AwrAiter Write API
  slug: awraiter-ai-write-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/awraiter-ai/agentic-access/awraiter-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/awraiter-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/awraiter-ai/rules/awraiter-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/awraiter-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/awraiter-ai/json-ld/awraiter-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/awraiter-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/awraiter-ai/vocabulary/awraiter-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/awraiter-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/awraiter-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/awraiter-ai/data-model/awraiter-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/awraiter-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/awraiter-ai/errors/awraiter-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/awraiter-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/awraiter-ai/conformance/awraiter-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/awraiter-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/awraiter-ai/llms/awraiter-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awraiter-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/awraiter-ai/mcp/awraiter-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/awraiter-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/awraiter-ai/mcp/awraiter-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awraiter-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/awraiter-ai/well-known/awraiter-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awraiter-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/awraiter-ai/hosts/awraiter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awraiter-ai-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://awraiter.ai/login
- group: auth
  href: https://artifacts.apis.io/awraiter-ai/security/awraiter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awraiter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awraiter.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://awraiter.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://awraiter.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awraiter.ai/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awraiter.ai/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://awraiter.ai/support/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://awraiter.ai/openapi.json
  - status: 401
    url: https://awraiter.ai/mcp
  - status: 200
    url: https://awraiter.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Awraiter AI (AwrAiter) provides a SaaS platform for managing Telegram channels. It offers a unified panel where users can plan weekly content, schedule posts, and view analytics. The service supports multiple channels, AI-powered content generation via ChatGPT and Claude, and team collaboration features. Free tier includes one channel, with paid plans starting at €9 per month for additional channels and advanced analytics.
image: https://awraiter.ai/og-en.png
json_schemas:
- name: ApplyDraftEmojiReplacementsInput
  property_count: 7
  slug: awraiter-ai-apply-draft-emoji-replacements-input
- name: CreatePollInput
  property_count: 5
  slug: awraiter-ai-create-poll-input
- name: CreatePostFromTextInput
  property_count: 10
  slug: awraiter-ai-create-post-from-text-input
- name: CreateReportInput
  property_count: 10
  slug: awraiter-ai-create-report-input
- name: PreviewDraftEmojiReplacementsInput
  property_count: 4
  slug: awraiter-ai-preview-draft-emoji-replacements-input
- name: SetAutopilotPolicyInput
  property_count: 3
  slug: awraiter-ai-set-autopilot-policy-input
jsonld:
- class_count: 91
  name: Awraiter Ai Context
  property_count: 92
  slug: awraiter-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at awraiter.ai.
  name: AwrAiter MCP Server
  slug: awraiter-ai-mcp-yml
modified: '2026-11-02'
name: AwrAiter
nav: Providers
network: true
overview: 'AwrAiter publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Catalog API, Read API, and Write API. Tagged areas include Telegram, Content Planning, Analytics, AI Integration, and Software-as-a-Service.


  The AwrAiter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AwrAiter''s developer surface includes documentation, pricing, support, and 18 more developer resources.'
plans:
- name: Awraiter Ai Plans Pricing
  plan_count: 0
  slug: awraiter-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Awraiter Ai Rate Limits
  slug: awraiter-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: AwrAiter API Rules
  rule_count: 60
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 6
  slug: awraiter-ai-rules
scopes:
- name: Awraiter Ai Scopes
  scope_count: 0
  slug: awraiter-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 63.8
    developer_ergonomics: 13.6
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 41.1
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awraiter Ai Authentication
  slug: awraiter-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Awraiter Ai Domain Security
  slug: awraiter-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: list-tools
  slug: awraiter-ai-list-tools-skill
slug: awraiter-ai
tags:
- Telegram
- Content Planning
- Analytics
- AI Integration
- Software-as-a-Service
website: https://awraiter.ai/
---
