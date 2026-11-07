---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Searlo Tech Agentic Access
  operation_count: 59
  slug: searlo-tech-agentic-access
  summary_line: 59 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Balance, usage and capability endpoints. Free — do not consume credits.
  name: searlo-tech Account API
  slug: searlo-tech-account-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Answers and citations from ChatGPT, Microsoft Copilot and Gemini, as their users see them.
  name: searlo-tech AI Answers API
  slug: searlo-tech-ai-answers-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Queue work and collect it later, by polling or webhook.
  name: searlo-tech Async API
  slug: searlo-tech-async-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: 'CURRENTLY UNAVAILABLE (coming soon): these endpoints return 403 FEATURE_NOT_AVAILABLE (not retryable, not charged) until their keyword data source is re-enabled. Domain-level SEO reports — keyword foo'
  name: searlo-tech Domain API
  slug: searlo-tech-domain-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Where a domain ranks for a keyword, from a live SERP read, with stored history.
  name: searlo-tech Rankings API
  slug: searlo-tech-rankings-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Query endpoints. Each successful call deducts credits per the pricing page.
  name: searlo-tech Search API
  slug: searlo-tech-search-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: 'The full Google results page: ads, People Also Ask, related searches, knowledge graph and AI Overview, 3 credits per page. From 2026-11-01, a request whose AI Overview had to be completed by rendering'
  name: searlo-tech SERP API
  slug: searlo-tech-serp-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Email verification and the MCP server descriptor.
  name: searlo-tech Tools API
  slug: searlo-tech-tools-api
- baseURL: https://api.searlo.tech/api/v1
  baseurl_source: declared
  description: Retrieval. Search finds the pages; these read them — scrape one, map a site, crawl it, or extract structured records. A fetched page costs 1 credit; from 2026-11-01, a page that had to be rendered (re
  name: searlo-tech Web Data API
  slug: searlo-tech-web-data-api
artifact_total: 25
common:
- group: docs
  title: ''
  type: APIReference
  url: https://searlo.tech/llms.txt
- group: agent
  href: https://artifacts.apis.io/searlo-tech/agentic-access/searlo-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/searlo-tech-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/searlo-tech/rate-limits/searlo-tech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/searlo-tech-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/searlo-tech/rules/searlo-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/searlo-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/searlo-tech/json-ld/searlo-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/searlo-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/searlo-tech/vocabulary/searlo-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/searlo-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/searlo-tech/data-model/searlo-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/searlo-tech-data-model.yml
- group: auth
  href: https://artifacts.apis.io/searlo-tech/authentication/searlo-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/searlo-tech-authentication.yml
- group: design
  href: https://artifacts.apis.io/searlo-tech/errors/searlo-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/searlo-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/searlo-tech/conformance/searlo-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/searlo-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/searlo-tech/llms/searlo-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/searlo-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/searlo-tech/mcp/searlo-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/searlo-tech-mcp.yml
- group: other
  href: https://artifacts.apis.io/searlo-tech/hosts/searlo-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/searlo-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/searlo-tech/vendors/searlo-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/searlo-tech-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.searlo.tech
- group: auth
  title: ''
  type: Security
  url: https://searlo.tech/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/searlo
- group: operate
  title: ''
  type: ChangeLog
  url: https://searlo.tech/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://searlo.tech/blog/crewai-web-search-tool-setup
- group: auth
  href: https://artifacts.apis.io/searlo-tech/security/searlo-tech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/searlo-tech-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/searlo-tech/security/searlo-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/searlo-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://searlo.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://searlo.tech/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://searlo.tech/pricing
- group: company
  title: ''
  type: Blog
  url: https://searlo.tech/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://searlo.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://searlo.tech/privacy
created: '2026-10-31'
description: Searlo provides a SERP API that delivers live search results in clean JSON format across web, news, images, maps, shopping, and AI-generated answers. The platform offers a single API key and credit pool, with a free tier of 3,000 credits and paid usage starting at $3.99 per 1,000 queries. It includes additional tools such as email verification, rank tracking, and AI assistance, targeting developers, marketers, and businesses needing up‑to‑date search data.
image: https://searlo.tech/og
json_schemas:
- name: AsyncTaskSpec
  property_count: 5
  slug: searlo-tech-async-task-spec
- name: ExtractResponse
  property_count: 8
  slug: searlo-tech-extract-response
- name: PlacesResponse
  property_count: 7
  slug: searlo-tech-places-response
- name: ReviewsResponse
  property_count: 9
  slug: searlo-tech-reviews-response
- name: SerpHtmlResult
  property_count: 12
  slug: searlo-tech-serp-html-result
- name: SerpResult
  property_count: 17
  slug: searlo-tech-serp-result
jsonld:
- class_count: 24
  name: Searlo Tech Context
  property_count: 128
  slug: searlo-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.searlo.tech.
  name: searlo-tech MCP Server
  slug: searlo-tech-mcp-yml
modified: '2026-10-31'
name: searlo-tech
nav: Providers
network: true
overview: 'searlo-tech publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, AI Answers API, Async API, and 6 more. Tagged areas include Search, SERP, Artificial Intelligence, and Data.


  The searlo-tech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  searlo-tech''s developer surface includes API reference, authentication, changelog, getting-started guide, documentation, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Searlo Tech Plans Pricing
  plan_count: 0
  slug: searlo-tech-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 16
  name: Searlo Tech Rate Limits
  slug: searlo-tech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: searlo-tech API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: searlo-tech-rules
scopes:
- name: Searlo Tech Scopes
  scope_count: 0
  slug: searlo-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 62.0
    developer_ergonomics: 27.4
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/searlo-tech/searlo-tech-2026-11-03T142923.png
security:
- kind: authentication
  name: Searlo Tech Authentication
  slug: searlo-tech-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Searlo Tech Domain Security
  slug: searlo-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Searlo Tech Vulnerability Disclosure
  slug: searlo-tech-vulnerability-disclosure
  summary_line: no policy recorded
slug: searlo-tech
tags:
- Search
- SERP
- Artificial Intelligence
- Data
website: https://searlo.tech/
---
