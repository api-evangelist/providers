---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Agentic News Ai Agentic Access
  operation_count: 21
  slug: agentic-news-ai-agentic-access
  summary_line: 21 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: Create and manage monitoring agents (watches). Each agent tracks a topic and automatically finds matching stories. Requires auth.
  name: Agentic News Agents API
  slug: agentic-news-ai-agents-api
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: Create, list, and revoke API keys for programmatic access. Keys use ak_ prefix with SHA-256 hashing. Requires JWT auth (web app session).
  name: Agentic News API Keys API
  slug: agentic-news-ai-api-keys-api
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: Your personalized daily news briefing based on your monitoring agents. Returns stories ranked by relevance with AI-generated hooks and briefs. Requires auth.
  name: Agentic News Briefing API
  slug: agentic-news-ai-briefing-api
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: Your story feed with per-agent filtering, sorting by date/score/watch, read state tracking, and pagination. Use `watchId` to get stories for a specific agent. Requires auth.
  name: Agentic News Feed API
  slug: agentic-news-ai-feed-api
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: 'Search recent news by meaning, not just keywords. Works without auth (3 results max) or with auth (up to 20 results). Rate limit: 30 req/min.'
  name: Agentic News Search API
  slug: agentic-news-ai-search-api
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: Full details of news story clusters including all source articles, topics, entities, and AI analysis. Requires auth.
  name: Agentic News Stories API
  slug: agentic-news-ai-stories-api
- baseURL: https://api.agentic-news.ai
  baseurl_source: declared
  description: Top trending news stories ranked by coverage volume. No authentication required.
  name: Agentic News Trending API
  slug: agentic-news-ai-trending-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/agentic-news-ai/agentic-access/agentic-news-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentic-news-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/agentic-news-ai/rate-limits/agentic-news-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentic-news-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentic-news-ai/plans/agentic-news-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentic-news-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentic-news-ai/rules/agentic-news-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agentic-news-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agentic-news-ai/vocabulary/agentic-news-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentic-news-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentic-news-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agentic-news-ai/security/agentic-news-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentic-news-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentic-news-ai/errors/agentic-news-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentic-news-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentic-news-ai/conformance/agentic-news-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentic-news-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentic-news-ai/llms/agentic-news-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentic-news-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentic-news-ai/well-known/agentic-news-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentic-news-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/agentic-news-ai/well-known/agentic-news-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentic-news-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentic-news-ai/hosts/agentic-news-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentic-news-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentic-news-ai/vendors/agentic-news-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentic-news-ai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentic-news.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://api.agentic-news.ai/docs
- group: auth
  href: https://artifacts.apis.io/agentic-news-ai/authentication/agentic-news-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentic-news-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentic-news-ai/security/agentic-news-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentic-news-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentic-news-ai/security/agentic-news-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentic-news-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentic-news.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentic-news.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentic-news.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentic-news.ai/terms
- group: start
  title: ''
  type: SignUp
  url: https://agentic-news.ai/signup
- group: start
  title: ''
  type: Login
  url: https://agentic-news.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://agentic-news.ai/about
created: '2026-11-01'
description: Agentic News provides AI-powered news aggregation, delivering curated daily briefings from thousands of publishers. Their agents scan topics, filter out noise, and present concise summaries, allowing users to stay informed with minimal effort. The service offers a free trial and paid plans for unlimited agents and advanced features.
image: https://agentic-news.ai/opengraph-image?cf413e5df761a16f
layout: provider
modified: '2026-11-01'
name: Agentic News
nav: Providers
network: true
overview: 'Agentic News publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, API Keys API, Briefing API, and 4 more. Tagged areas include Artificial Intelligence, News, Aggregation, DailyBriefings, and AI Agents.


  The Agentic News catalog on APIs.io includes 1 Spectral governance ruleset.


  Agentic News'' developer surface includes changelog, API reference, authentication, pricing, signup flow, getting-started guide, and 20 more developer resources.'
plans:
- name: Agentic News Ai Plans Pricing
  plan_count: 2
  slug: agentic-news-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Agentic News Ai Rate Limits
  slug: agentic-news-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Agentic News API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 2
  slug: agentic-news-ai-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 49.4
    developer_ergonomics: 27.9
    discoverability: 66.1
    operational_transparency: 50.0
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentic News Ai Authentication
  slug: agentic-news-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentic News Ai Domain Security
  slug: agentic-news-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentic News Ai Vulnerability Disclosure
  slug: agentic-news-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: create-agent
  slug: create-agent
- name: get-briefing
  slug: get-briefing
- name: search-news
  slug: search-news
slug: agentic-news-ai
tags:
- Artificial Intelligence
- News
- Aggregation
- DailyBriefings
- AI Agents
website: https://agentic-news.ai/
---
