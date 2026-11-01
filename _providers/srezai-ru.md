---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Search API for AI agents providing web search, rendering, and data extraction.
  name: SrezAI API
  slug: srezai-api
- description: 'srezai-ru API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: srezai-ru API
  slug: srezai-ru-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/srezai-ru/rate-limits/srezai-ru-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/srezai-ru-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/srezai-ru/plans/srezai-ru-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/srezai-ru-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/srezai-ru/rules/srezai-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/srezai-ru-rules.yml
- group: design
  href: https://artifacts.apis.io/srezai-ru/json-ld/srezai-ru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/srezai-ru-context.jsonld
- group: design
  href: https://artifacts.apis.io/srezai-ru/vocabulary/srezai-ru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/srezai-ru-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/srezai-ru/data-model/srezai-ru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/srezai-ru-data-model.yml
- group: build
  href: https://artifacts.apis.io/srezai-ru/cli/srezai-ru-cli.yml
  title: ''
  type: CLI
  url: cli/srezai-ru-cli.yml
- group: auth
  href: https://artifacts.apis.io/srezai-ru/authentication/srezai-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/srezai-ru-authentication.yml
- group: design
  href: https://artifacts.apis.io/srezai-ru/conformance/srezai-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/srezai-ru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/srezai-ru/llms/srezai-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/srezai-ru-llms.txt
- group: agent
  href: https://artifacts.apis.io/srezai-ru/mcp/srezai-ru-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/srezai-ru-mcp.yml
- group: agent
  href: https://artifacts.apis.io/srezai-ru/well-known/srezai-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/srezai-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/srezai-ru/hosts/srezai-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/srezai-ru-hosts.yml
- group: build
  href: https://artifacts.apis.io/srezai-ru/packages/srezai-ru-packages.yml
  title: ''
  type: SDKs
  url: packages/srezai-ru-packages.yml
- group: build
  href: https://artifacts.apis.io/srezai-ru/packages/srezai-ru-packages.yml
  title: ''
  type: Packages
  url: packages/srezai-ru-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://srezai.ru/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/srezai-ru/security/srezai-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/srezai-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://srezai.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://srezai.ru/docs
- group: company
  title: ''
  type: Blog
  url: https://srezai.ru/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://srezai.ru/pricing
- group: operate
  title: ''
  type: Support
  url: https://srezai.ru/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://srezai.ru/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://srezai.ru/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/srezai-team
coverage:
  checked: '2026-10-31'
  detail: Documentation is served as a JavaScript shell with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://srezai.ru/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: СрезAI – поисковый API для ИИ‑агентов, предоставляющий живой веб‑поиск по русскоязычному интернету (Рунету), возможность рендеринга страниц браузером и выдачу чистого Markdown или JSON, что упрощает построение RAG‑проектов и цепочек запросов для больших языковых моделей. Сервис поддерживает REST‑API, Model Context Protocol (MCP), CLI‑инструменты и готовые скиллы, а также предлагает функции поиска изображений, извлечения данных по JSON‑схемам, проверки фактов и глубоких исследований. Компания ориентирована на российский рынок, но предоставляет интерфейсы на английском и русском языках.
image: https://srezai.ru/opengraph-image?0f4e312b94d88b9c
json_schemas:
- name: GetApiV1PartnerResponse
  property_count: 3
  slug: srezai-ru-get-api-v1-partner-response
- name: PostApiV1CrawlRequest
  property_count: 4
  slug: srezai-ru-post-api-v1-crawl-request
- name: PostApiV1ExtractRequest
  property_count: 2
  slug: srezai-ru-post-api-v1-extract-request
- name: PostApiV1MapRequest
  property_count: 4
  slug: srezai-ru-post-api-v1-map-request
- name: PostApiV1MediaRequest
  property_count: 4
  slug: srezai-ru-post-api-v1-media-request
- name: PostApiV1TranscriptRequest
  property_count: 3
  slug: srezai-ru-post-api-v1-transcript-request
jsonld:
- class_count: 13
  name: Srezai Ru Context
  property_count: 22
  slug: srezai-ru-context
layout: provider
mcp_servers:
- description: Remote MCP server at srezai.ru.
  name: srezai-ru MCP Server
  slug: srezai-ru-mcp-yml
modified: '2026-10-31'
name: srezai-ru
nav: Providers
network: true
overview: 'srezai-ru is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Search, AI, API, and Russia.


  The srezai-ru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  srezai-ru''s developer surface includes CLI, authentication, getting-started guide, documentation, engineering blog, pricing, support, and 18 more developer resources.'
plans:
- name: Srezai Ru Plans Pricing
  plan_count: 2
  slug: srezai-ru-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Srezai Ru Rate Limits
  slug: srezai-ru-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: srezai-ru API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: srezai-ru-rules
scopes:
- name: Srezai Ru Scopes
  scope_count: 0
  slug: srezai-ru-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 90.7
    catalog_earned_first_party: 0.0
    catalog_gap: 24.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 79.1
    contract_quality: 53.4
    developer_ergonomics: 54.8
    discoverability: 56.7
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Srezai Ru Authentication
  slug: srezai-ru-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Srezai Ru Domain Security
  slug: srezai-ru-domain-security
  summary_line: TLSv1.3 · DMARC
slug: srezai-ru
tags:
- Company
- Search
- AI
- API
- Russia
website: https://srezai.ru/
---
