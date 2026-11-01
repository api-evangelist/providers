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
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Topxea Com Agentic Access
  operation_count: 11
  slug: topxea-com-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- baseURL: https://ai.topxea.com
  baseurl_source: declared
  description: 'The Messages API for every text model except Jev, with x-api-key or Authorization: Bearer.'
  name: topxea-com Anthropic Compatible API
  slug: topxea-com-anthropic-compatible-api
- baseURL: https://ai.topxea.com
  baseurl_source: declared
  description: 'Chat Completions, Responses, Images, Video and the model list, with Authorization: Bearer <key>.'
  name: topxea-com Open AI Compatible API
  slug: topxea-com-openai-compatible-api
- baseURL: https://ai.topxea.com
  baseurl_source: declared
  description: No key needed.
  name: topxea-com Public API
  slug: topxea-com-public-api
- baseURL: https://ai.topxea.com
  baseurl_source: declared
  description: 'System One: typed questions about a state, answered with probabilities.'
  name: topxea-com Type Safe API
  slug: topxea-com-typesafe-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/topxea-com/agentic-access/topxea-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/topxea-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/topxea-com/rules/topxea-com-rules.yml
  title: ''
  type: Spectral
  url: rules/topxea-com-rules.yml
- group: design
  href: https://artifacts.apis.io/topxea-com/json-ld/topxea-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/topxea-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/topxea-com/vocabulary/topxea-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/topxea-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/topxea-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/topxea-com/data-model/topxea-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/topxea-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/topxea-com/cli/topxea-com-cli.yml
  title: ''
  type: CLI
  url: cli/topxea-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/topxea-com/changelog/topxea-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/topxea-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/topxea-com/authentication/topxea-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/topxea-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/topxea-com/errors/topxea-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/topxea-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/topxea-com/conformance/topxea-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/topxea-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/topxea-com/llms/topxea-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/topxea-com-llms.txt
- group: other
  href: https://artifacts.apis.io/topxea-com/hosts/topxea-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/topxea-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://topxea.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://ai.topxea.com/docs/kimi-k3-1-pro
- group: start
  title: ''
  type: GettingStarted
  url: https://ai.topxea.com/docs/use-topxai-with-cherry-studio
- group: auth
  href: https://artifacts.apis.io/topxea-com/security/topxea-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/topxea-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://topxea.com/
- group: company
  title: ''
  type: Blog
  url: https://topxea.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://topxea.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://topxea.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UnbelievableT
created: '2026-10-29'
description: TopxAI (topxea.com) offers AI value-chain quotes, company research, and financial data for AI‑related public companies. The platform provides historical market data, financial ratios, cash‑flow metrics, and AI tools that let users compare valuations, explore industry trends, and access subscription‑based research. With coverage of 179 companies across materials, chips, infrastructure, and applications, TopxAI serves analysts, investors, and developers seeking AI market insights.
image: https://wlksiulicosdnerzhkdl.supabase.co/storage/v1/object/public/eastore-assets/og/cover.png
json_schemas:
- name: ChatCompletionRequest
  property_count: 13
  slug: topxea-com-chat-completion-request
- name: MessagesRequest
  property_count: 8
  slug: topxea-com-messages-request
- name: PricingModel
  property_count: 11
  slug: topxea-com-pricing-model
- name: ResponsesRequest
  property_count: 7
  slug: topxea-com-responses-request
- name: SystemOneRequest
  property_count: 4
  slug: topxea-com-system-one-request
- name: VideoRequest
  property_count: 8
  slug: topxea-com-video-request
jsonld:
- class_count: 17
  name: Topxea Com Context
  property_count: 74
  slug: topxea-com-context
layout: provider
modified: '2026-10-29'
name: topxea-com
nav: Providers
network: true
overview: 'topxea-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Anthropic Compatible API, Open AI Compatible API, Public API, and 1 more. Tagged areas include Company, AI, Data, Finance, and Research.


  The topxea-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  topxea-com''s developer surface includes CLI, changelog, authentication, documentation, getting-started guide, engineering blog, and 16 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: topxea-com API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: topxea-com-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 67.6
    developer_ergonomics: 56.4
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
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
  name: Topxea Com Authentication
  slug: topxea-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Topxea Com Domain Security
  slug: topxea-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: chat-completion
  slug: topxea-com-chat-completion
slug: topxea-com
tags:
- Company
- AI
- Data
- Finance
- Research
website: https://topxea.com/
---
