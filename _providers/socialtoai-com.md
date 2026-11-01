---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Socialtoai Com Agentic Access
  operation_count: 10
  slug: socialtoai-com-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Account API from socialtoai-com — 1 operation(s) for account.
  name: socialtoai-com Account API
  slug: socialtoai-com-account-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Call API from socialtoai-com — 1 operation(s) for call.
  name: socialtoai-com Call API
  slug: socialtoai-com-call-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Capabilities API from socialtoai-com — 1 operation(s) for capabilities.
  name: socialtoai-com Capabilities API
  slug: socialtoai-com-capabilities-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Comments API from socialtoai-com — 1 operation(s) for comments.
  name: socialtoai-com Comments API
  slug: socialtoai-com-comments-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Detail API from socialtoai-com — 1 operation(s) for detail.
  name: socialtoai-com Detail API
  slug: socialtoai-com-detail-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Find API from socialtoai-com — 1 operation(s) for find.
  name: socialtoai-com Find API
  slug: socialtoai-com-find-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Search API from socialtoai-com — 1 operation(s) for search.
  name: socialtoai-com Search API
  slug: socialtoai-com-search-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The Trending API from socialtoai-com — 1 operation(s) for trending.
  name: socialtoai-com Trending API
  slug: socialtoai-com-trending-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The User Posts API from socialtoai-com — 1 operation(s) for user posts.
  name: socialtoai-com User Posts API
  slug: socialtoai-com-user-posts-api
- baseURL: https://api.socialtoai.com/v1
  baseurl_source: declared
  description: The User Profile API from socialtoai-com — 1 operation(s) for user profile.
  name: socialtoai-com User Profile API
  slug: socialtoai-com-user-profile-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/socialtoai-com/overlays/socialtoai-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/socialtoai-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/socialtoai-com/agentic-access/socialtoai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/socialtoai-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/socialtoai-com/plans/socialtoai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socialtoai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/rules/socialtoai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/socialtoai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/json-ld/socialtoai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/socialtoai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/socialtoai-com/vocabulary/socialtoai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/socialtoai-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/socialtoai-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/data-model/socialtoai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/socialtoai-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/socialtoai-com/changelog/socialtoai-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/socialtoai-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/conventions/socialtoai-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/socialtoai-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/conventions/socialtoai-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/socialtoai-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/socialtoai-com/authentication/socialtoai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socialtoai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/errors/socialtoai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/socialtoai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/socialtoai-com/conformance/socialtoai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socialtoai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socialtoai-com/llms/socialtoai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialtoai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/socialtoai-com/hosts/socialtoai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialtoai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/socialtoai-com/vendors/socialtoai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/socialtoai-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://socialtoai.com/status/
- group: start
  title: ''
  type: Sandbox
  url: https://socialtoai.com/console/playground/
- group: company
  title: ''
  type: Newsroom
  url: https://socialtoai.com/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://socialtoai.com/changelog/
- group: auth
  href: https://artifacts.apis.io/socialtoai-com/security/socialtoai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialtoai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialtoai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://socialtoai.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://socialtoai.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://socialtoai.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://socialtoai.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://socialtoai.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/socialtoai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialtoai.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialtoai.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://socialtoai.com/console/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://socialtoai.com/openapi.json
  - status: null
    url: https://api.socialtoai.com/openapi.json
  - status: 403
    url: https://api.socialtoai.com/mcp
  - status: 200
    url: https://socialtoai.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: SocialToAI provides a Social Media API and MCP server that enables AI agents to access publicly visible social media content across 18 platforms, including TikTok, Instagram, X (Twitter), Reddit, YouTube, Facebook, LinkedIn, Threads, Telegram, Pinterest, Xiaohongshu (RedNote), Douyin, Weibo, WeChat Articles, Bilibili, Zhihu, Kuaishou, and WeChat Channels. The service offers a unified REST endpoint (https://api.socialtoai.com/v1) and an MCP streaming endpoint (https://mcp.socialtoai.com/mcp) with pay‑per‑call pricing, free failed calls, and a free 100‑credit starter tier. It includes ready‑made tools for brand buzz, comment analysis, account monitoring, creator discovery, bulk link data, and viral finding, all accessible via API keys. The platform emphasizes AI‑ready data, transparent pricing, and no subscription model.
image: https://socialtoai.com/og/home.en.png
json_schemas:
- name: AccountResponse
  property_count: 9
  slug: socialtoai-com-account-response
- name: CapabilitiesResponse
  property_count: 4
  slug: socialtoai-com-capabilities-response
- name: CellsEnvelope
  property_count: 10
  slug: socialtoai-com-cells-envelope
- name: Envelope
  property_count: 21
  slug: socialtoai-com-envelope
- name: FindResponse
  property_count: 6
  slug: socialtoai-com-find-response
jsonld:
- class_count: 13
  name: Socialtoai Com Context
  property_count: 81
  slug: socialtoai-com-context
layout: provider
modified: '2026-10-31'
name: socialtoai-com
nav: Providers
network: true
overview: 'socialtoai-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Call API, Capabilities API, and 7 more. Tagged areas include Company, Social Media, AI, Data API, and MCP.


  The socialtoai-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  socialtoai-com''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, support, and 25 more developer resources.'
plans:
- name: Socialtoai Com Plans Pricing
  plan_count: 5
  slug: socialtoai-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Socialtoai Com Rate Limits
  slug: socialtoai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: socialtoai-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: socialtoai-com-rules
scopes:
- name: Socialtoai Com Scopes
  scope_count: 0
  slug: socialtoai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 60.0
    developer_ergonomics: 58.8
    discoverability: 67.9
    operational_transparency: 36.8
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
  name: Socialtoai Com Authentication
  slug: socialtoai-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Socialtoai Com Domain Security
  slug: socialtoai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-content
  slug: socialtoai-com-search
slug: socialtoai-com
tags:
- Company
- Social Media
- AI
- Data API
- MCP
- Analytics
website: https://socialtoai.com/
---
