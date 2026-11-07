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
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Usestring Ai Agentic Access
  operation_count: 47
  slug: usestring-ai-agentic-access
  summary_line: 47 operations · 18 acting
api_count: 3
apis:
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Remote CDP browser over WebSocket and reusable browser profiles (contexts).
  name: usestring-ai Browser API
  slug: usestring-ai-browser-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Starting, watching, steering and finishing a feed build.
  name: usestring-ai Builds API
  slug: usestring-ai-builds-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Browser profiles that persist logins and cookies between sessions.
  name: usestring-ai Contexts API
  slug: usestring-ai-contexts-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: This specification and its rendering. Unauthenticated.
  name: usestring-ai Documentation API
  slug: usestring-ai-documentation-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Published feeds you are subscribed to, and the data they collect.
  name: usestring-ai Feeds API
  slug: usestring-ai-feeds-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Retrieve a single URL.
  name: usestring-ai Fetch API
  slug: usestring-ai-fetch-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Query a search engine for organic results.
  name: usestring-ai Search API
  slug: usestring-ai-search-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: 'Hosted-browser (`/wss`) sessions as API objects: ids, status, replays, live view and files. Every `/wss` connection gets an id, returned in its `x-session-id` upgrade response header.'
  name: usestring-ai Sessions API
  slug: usestring-ai-sessions-api
- baseURL: https://request.usestring.ai/v1
  baseurl_source: declared
  description: Discover the URLs of a whole site as an asynchronous job.
  name: usestring-ai Sitemap API
  slug: usestring-ai-sitemap-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/usestring-ai/agentic-access/usestring-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/usestring-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/usestring-ai/rate-limits/usestring-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/usestring-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/usestring-ai/plans/usestring-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usestring-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usestring-ai/rules/usestring-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/usestring-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/usestring-ai/json-ld/usestring-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usestring-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/usestring-ai/vocabulary/usestring-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usestring-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/usestring-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/usestring-ai/data-model/usestring-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usestring-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://usestring.ai/trust
- group: auth
  href: https://artifacts.apis.io/usestring-ai/authentication/usestring-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usestring-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/usestring-ai/errors/usestring-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usestring-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/usestring-ai/conformance/usestring-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usestring-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usestring-ai/llms/usestring-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usestring-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/usestring-ai/mcp/usestring-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usestring-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/usestring-ai/well-known/usestring-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/usestring-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/usestring-ai/well-known/usestring-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usestring-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/usestring-ai/hosts/usestring-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usestring-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/usestring-ai/vendors/usestring-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usestring-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://usestring.ai/security
- group: auth
  href: https://artifacts.apis.io/usestring-ai/security/usestring-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/usestring-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/usestring-ai/security/usestring-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usestring-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/usestring-ai/security/usestring-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usestring-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usestring.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.usestring.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://portal.usestring.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://portal.usestring.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://usestring.ai/web-access
- group: company
  title: ''
  type: Blog
  url: https://usestring.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://usestring.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usestring.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usestring.ai/privacy
created: '2026-10-31'
description: String is a reliable web scraping API that returns public pages as clean Markdown, raw HTML, or JSON. Users pay only when content is returned. The platform offers a Web Access API, a Composer tool for structured feeds, and managed services for bespoke data sets. It emphasizes high reliability, easy integration, and transparent pricing, catering to developers and businesses needing scalable web data extraction. Not to be confused with String Technology (string.xyz), a separate company that builds fiat payments for Web3 games.
image: https://usestring.ai/brand/string-logo.svg
json_schemas:
- name: BuildList
  property_count: 4
  slug: usestring-ai-build-list
- name: Build
  property_count: 16
  slug: usestring-ai-build
- name: Context
  property_count: 10
  slug: usestring-ai-context
- name: FetchRequest
  property_count: 16
  slug: usestring-ai-fetch-request
- name: Fetch JSON envelope
  property_count: 12
  slug: usestring-ai-fetch-response
- name: GateAnswer
  property_count: 0
  slug: usestring-ai-gate-answer
- name: Sample
  property_count: 6
  slug: usestring-ai-sample
- name: SearchRequest
  property_count: 18
  slug: usestring-ai-search-request
- name: SearchResponse
  property_count: 18
  slug: usestring-ai-search-response
- name: SendMessageRequest
  property_count: 2
  slug: usestring-ai-send-message-request
- name: SitemapJob
  property_count: 9
  slug: usestring-ai-sitemap-job
- name: UpdateBuildRequest
  property_count: 1
  slug: usestring-ai-update-build-request
jsonld:
- class_count: 103
  name: Usestring Ai Context
  property_count: 279
  slug: usestring-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.usestring.ai requiring an API key.
  name: String MCP Server
  slug: usestring-ai-mcp-yml
modified: '2026-10-31'
name: String
nav: Providers
network: true
overview: 'String publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including usestring-ai Browser API, usestring-ai Builds API, usestring-ai Contexts API, and 6 more. Tagged areas include Web Scraping, Data Extraction, Markdown, and JSON.


  The String catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  String''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Usestring Ai Plans Pricing
  plan_count: 6
  slug: usestring-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Usestring Ai Rate Limits
  slug: usestring-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: String API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 6
  slug: usestring-ai-rules
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 84.8
    catalog_earned_first_party: 24.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 38.6
    discoverability: 61.7
    operational_transparency: 36.8
  previous_composite: 61.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usestring Ai Authentication
  slug: usestring-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Usestring Ai Domain Security
  slug: usestring-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Usestring Ai Vulnerability Disclosure
  slug: usestring-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Usestring Ai Trust Center
  slug: usestring-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: fetch
  slug: usestring-ai-fetch-skill
- name: search
  slug: usestring-ai-search-skill
- name: sitemap
  slug: usestring-ai-sitemap-skill
slug: usestring-ai
tags:
- Web Scraping
- Data Extraction
- Markdown
- JSON
website: https://usestring.ai/
---
