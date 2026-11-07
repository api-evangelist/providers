---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: 0Si Ai Agentic Access
  operation_count: 22
  slug: 0si-ai-agentic-access
  summary_line: 22 operations · 5 acting
api_count: 1
apis:
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Companies API from 공시.ai — 3 operation(s) for companies.
  name: 공시.ai Companies API
  slug: 0si-ai-companies-api
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Disclosures API from 공시.ai — 5 operation(s) for disclosures.
  name: 공시.ai Disclosures API
  slug: 0si-ai-disclosures-api
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Sec API from 공시.ai — 4 operation(s) for sec.
  name: 공시.ai Sec API
  slug: 0si-ai-sec-api
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Status API from 공시.ai — 1 operation(s) for status.
  name: 공시.ai Status API
  slug: 0si-ai-status-api
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Stream API from 공시.ai — 1 operation(s) for stream.
  name: 공시.ai Stream API
  slug: 0si-ai-stream-api
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Usage API from 공시.ai — 1 operation(s) for usage.
  name: 공시.ai Usage API
  slug: 0si-ai-usage-api
- baseURL: https://app.0si.ai/api/v1
  baseurl_source: declared
  description: The Webhooks API from 공시.ai — 5 operation(s) for webhooks.
  name: 공시.ai Webhooks API
  slug: 0si-ai-webhooks-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/0si-ai/agentic-access/0si-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/0si-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/0si-ai/rate-limits/0si-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/0si-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/0si-ai/plans/0si-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0si-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/0si-ai/rules/0si-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/0si-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/0si-ai/json-ld/0si-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/0si-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/0si-ai/vocabulary/0si-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0si-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/0si-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/0si-ai/data-model/0si-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/0si-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/0si-ai/conventions/0si-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/0si-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/0si-ai/authentication/0si-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/0si-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/0si-ai/errors/0si-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/0si-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/0si-ai/conformance/0si-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0si-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/0si-ai/llms/0si-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0si-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/0si-ai/mcp/0si-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/0si-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/0si-ai/well-known/0si-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0si-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/0si-ai/hosts/0si-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0si-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/0si-ai/vendors/0si-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0si-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/0si-ai/packages/0si-ai-packages.yml
  title: ''
  type: Packages
  url: packages/0si-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://0si.ai/static/sdk/osi_client.py
- group: auth
  href: https://artifacts.apis.io/0si-ai/security/0si-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0si-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0si.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://0si.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://0si.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://0si.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://0si.ai/developers#quickstart
- group: operate
  title: ''
  type: Support
  url: https://0si.ai/support
- group: commercial
  title: ''
  type: Pricing
  url: https://0si.ai/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0si.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0si.ai/privacy
created: '2026-10-31'
description: 공시.ai는 한국 DART·KIND와 미국 SEC EDGAR 공시 원문을 AI로 실시간 분석하는 서비스입니다. AI가 원문을 읽고 숫자, 위험 조건, 정정 내역을 한국어로 정리해 제공하며, 관심 종목 알림과 실적 비교 기능을 포함합니다. 무료 플랜으로 체험 가능하고, Pro 플랜에서는 REST API, 웹훅, SSE 스트리밍을 제공해 개발자들이 데이터에 접근할 수 있습니다. 또한 AI 도구와 MCP 커넥터를 통해 에이전트 연동도 지원합니다.
image: https://app.0si.ai/static/og-logo-v2.png
json_schemas:
- name: DeltaResponse
  property_count: 3
  slug: 0si-ai-delta-response
- name: DisclosureDetail
  property_count: 3
  slug: 0si-ai-disclosure-detail
- name: MarketReactionResponse
  property_count: 3
  slug: 0si-ai-market-reaction-response
- name: RevisionHistoryResponse
  property_count: 3
  slug: 0si-ai-revision-history-response
- name: UsageResponse
  property_count: 3
  slug: 0si-ai-usage-response
- name: WebhookInput
  property_count: 9
  slug: 0si-ai-webhook-input
jsonld:
- class_count: 41
  name: 0Si Ai Context
  property_count: 133
  slug: 0si-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.0si.ai requiring an API key.
  name: 공시.ai MCP Server
  slug: 0si-ai-mcp-yml
modified: '2026-10-31'
name: 공시.ai
nav: Providers
network: true
overview: '공시.ai publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Disclosures API, Sec API, and 4 more. Tagged areas include Artificial Intelligence, Finance, Filings, South Korea, and USA.


  The 공시.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  공시.ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 23 more developer resources.'
plans:
- name: 0Si Ai Plans Pricing
  plan_count: 3
  slug: 0si-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: 0Si Ai Rate Limits
  slug: 0si-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: 공시.ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: 0si-ai-rules
scopes:
- name: 0Si Ai Scopes
  scope_count: 0
  slug: 0si-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 62.5
    developer_ergonomics: 46.9
    discoverability: 65.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
    - north-america
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 0Si Ai Authentication
  slug: 0si-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 0Si Ai Domain Security
  slug: 0si-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-company
  slug: 0si-ai-get-company
slug: 0si-ai
tags:
- Artificial Intelligence
- Finance
- Filings
- South Korea
- USA
website: https://0si.ai/
---
