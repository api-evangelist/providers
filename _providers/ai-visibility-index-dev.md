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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP endpoint providing AI visibility scoring tools for domain visibility, industry summary, and methodology.
  name: AI Visibility Index MCP Server
  slug: ai-visibility-index-dev-mcp-server
- description: 'AI Visibility Index API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AI Visibility Index API
  slug: ai-visibility-index-dev-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/ai-visibility-index-dev/plans/ai-visibility-index-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-visibility-index-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ai-visibility-index-dev/rules/ai-visibility-index-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-visibility-index-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-visibility-index-dev/vocabulary/ai-visibility-index-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-visibility-index-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ai-visibility-index-dev/conformance/ai-visibility-index-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-visibility-index-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-visibility-index-dev/llms/ai-visibility-index-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-visibility-index-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/ai-visibility-index-dev/mcp/ai-visibility-index-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ai-visibility-index-dev-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/ai-visibility-index-dev/hosts/ai-visibility-index-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-visibility-index-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-visibility-index-dev/vendors/ai-visibility-index-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-visibility-index-dev-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://ai-visibility-index.dev/docs/mcp/
- group: auth
  href: https://artifacts.apis.io/ai-visibility-index-dev/security/ai-visibility-index-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-visibility-index-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-visibility-index.dev/
- group: company
  title: ''
  type: Blog
  url: https://ai-visibility-index.dev/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://ai-visibility-index.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-visibility-index.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-visibility-index.dev/privacy/
- group: operate
  title: ''
  type: Support
  url: https://ai-visibility-index.dev/contact/
created: '2026-11-01'
description: ChatGPT・Claude・Gemini・Perplexityで調査したEC104社のAI可視性スコアとランキングを無料公開。対象外ドメインは、4エンジンの新規測定・競合比較・改善提案を含む個別診断を選べます。 公開ランキング対象のEC104社について、ChatGPT・Claude・Gemini・Perplexityの保存済みスコアと順位を確認できます。対象外ドメインは、個別診断で新規測定・競合比較・改善提案まで受け付けています。
image: https://ai-visibility-index.dev/images/ogp-default.png
layout: provider
mcp_servers:
- description: ''
  name: AI Visibility Index MCP endpoint (Streamable HTTP)
  slug: ai-visibility-index-mcp-endpoint-streamable-http
modified: '2026-11-01'
name: AI Visibility Index
nav: Providers
network: true
overview: 'AI Visibility Index is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Visibility, Index, Rankings, and EC104.


  The AI Visibility Index catalog on APIs.io includes 1 Spectral governance ruleset.


  AI Visibility Index''s developer surface includes getting-started guide, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Ai Visibility Index Dev Plans Pricing
  plan_count: 1
  slug: ai-visibility-index-dev-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AI Visibility Index API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ai-visibility-index-dev-rules
scopes:
- name: Ai Visibility Index Dev Scopes
  scope_count: 0
  slug: ai-visibility-index-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 10.4
    developer_ergonomics: 9.5
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 26.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
  name: Ai Visibility Index Dev Authentication
  slug: ai-visibility-index-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ai Visibility Index Dev Domain Security
  slug: ai-visibility-index-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ai-visibility-index-dev
tags:
- Artificial Intelligence
- Visibility
- Index
- Rankings
- EC104
website: https://ai-visibility-index.dev/
---
