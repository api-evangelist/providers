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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Upspring Ai Agentic Access
  operation_count: 15
  slug: upspring-ai-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 1
apis:
- baseURL: https://public-api.upspring.ai
  baseurl_source: declared
  description: The Ads API from upspring-ai — 3 operation(s) for ads.
  name: upspring-ai Ads API
  slug: upspring-ai-ads-api
- baseURL: https://public-api.upspring.ai
  baseurl_source: declared
  description: The Advertisers API from upspring-ai — 6 operation(s) for advertisers.
  name: upspring-ai Advertisers API
  slug: upspring-ai-advertisers-api
- baseURL: https://public-api.upspring.ai
  baseurl_source: declared
  description: The Docs API from upspring-ai — 3 operation(s) for docs.
  name: upspring-ai Docs API
  slug: upspring-ai-docs-api
- baseURL: https://public-api.upspring.ai
  baseurl_source: declared
  description: The Taxonomy API from upspring-ai — 2 operation(s) for taxonomy.
  name: upspring-ai Taxonomy API
  slug: upspring-ai-taxonomy-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/upspring-ai/agentic-access/upspring-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/upspring-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/upspring-ai/rate-limits/upspring-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/upspring-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/upspring-ai/plans/upspring-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/upspring-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/upspring-ai/rules/upspring-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/upspring-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/upspring-ai/json-ld/upspring-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/upspring-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/upspring-ai/vocabulary/upspring-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/upspring-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/upspring-ai/data-model/upspring-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upspring-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/upspring-ai/conventions/upspring-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/upspring-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/upspring-ai/authentication/upspring-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upspring-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/upspring-ai/errors/upspring-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/upspring-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/upspring-ai/conformance/upspring-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upspring-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/upspring-ai/llms/upspring-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upspring-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/upspring-ai/mcp/upspring-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/upspring-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/upspring-ai/well-known/upspring-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upspring-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/upspring-ai/well-known/upspring-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upspring-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/upspring-ai/hosts/upspring-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upspring-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/upspring-ai/vendors/upspring-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upspring-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.upspring.ai/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.upspring.ai/en/collections/16472992-getting-started
- group: auth
  href: https://artifacts.apis.io/upspring-ai/security/upspring-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upspring-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upspring.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://public-api.upspring.ai/v1/docs/ui
- group: start
  title: ''
  type: DeveloperPortal
  url: https://public-api.upspring.ai/v1/docs/ui
- group: company
  title: ''
  type: Blog
  url: https://www.upspring.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.upspring.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upspring.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upspring.ai/terms-of-use
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.upspring.ai/mcp
  - status: 200
    url: https://upspring.ai/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Upspring provides live advertising data via MCP, API, and platform, enabling AI models to reason over ad context with reduced token usage. It offers scale grades for spend, traffic, and sales, turning live ads into reasoning‑ready context. About ten times fewer tokens than raw creative are needed, helping marketers and developers integrate advertising insights into AI applications.
image: https://www.upspring.ai/upspring-logo-dark.png
json_schemas:
- name: AdsListResponse
  property_count: 2
  slug: upspring-ai-ads-list-response
- name: AdvertiserByDomainResponse
  property_count: 1
  slug: upspring-ai-advertiser-by-domain-response
- name: AdvertisersListResponse
  property_count: 2
  slug: upspring-ai-advertisers-list-response
- name: PeersResponse
  property_count: 2
  slug: upspring-ai-peers-response
- name: RequestAdvertiserResponse
  property_count: 1
  slug: upspring-ai-request-advertiser-response
- name: SimilarAdsResponse
  property_count: 1
  slug: upspring-ai-similar-ads-response
jsonld:
- class_count: 26
  name: Upspring Ai Context
  property_count: 52
  slug: upspring-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.upspring.ai.
  name: upspring-ai MCP Server
  slug: upspring-ai-mcp-yml
modified: '2026-10-31'
name: upspring-ai
nav: Providers
network: true
overview: 'upspring-ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ads API, Advertisers API, Docs API, and 1 more. Tagged areas include Advertising, Artificial Intelligence, Data, Marketing, and Platform.


  The upspring-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  upspring-ai''s developer surface includes authentication, support, getting-started guide, documentation, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Upspring Ai Plans Pricing
  plan_count: 4
  slug: upspring-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Upspring Ai Rate Limits
  slug: upspring-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: upspring-ai API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: upspring-ai-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Upspring Ai Authentication
  slug: upspring-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Upspring Ai Domain Security
  slug: upspring-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upspring-ai
tags:
- Advertising
- Artificial Intelligence
- Data
- Marketing
- Platform
website: https://www.upspring.ai/
---
