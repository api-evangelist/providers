---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Finedata Ai Agentic Access
  operation_count: 58
  slug: finedata-ai-agentic-access
  summary_line: 58 operations · 30 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: Create and manage API keys for programmatic access.
  name: finedata-ai API Keys API
  slug: finedata-ai-api-keys-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: Submit long-running scrape jobs and retrieve results later. Supports webhooks and batch processing.
  name: finedata-ai Async Scraping API
  slug: finedata-ai-async-scraping-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: The Google SERP API from finedata-ai — 1 operation(s) for google serp.
  name: finedata-ai Google SERP API
  slug: finedata-ai-google-serp-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: The OAuth API from finedata-ai — 7 operation(s) for oauth.
  name: finedata-ai OAuth API
  slug: finedata-ai-oauth-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: Available subscription plans and pricing.
  name: finedata-ai Plans API
  slug: finedata-ai-plans-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: 'Bring Your Own Proxy — save encrypted proxy lists and reference them by `proxy_profile_id` in scrape requests. **Requirements:** `team_s` plan or higher (or admin `allow_byop` override). **Pricing:** '
  name: finedata-ai Proxy Profiles (BYOP) API
  slug: finedata-ai-proxy-profiles-byop-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: Current user profile and account information.
  name: finedata-ai User API
  slug: finedata-ai-user-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: The User Statistics API from finedata-ai — 1 operation(s) for user statistics.
  name: finedata-ai User Statistics API
  slug: finedata-ai-user-statistics-api
- baseURL: https://api.finedata.ai
  baseurl_source: declared
  description: Core endpoint. Scrape any URL with antibot bypass, JS rendering, and proxy rotation.
  name: finedata-ai Web Scraping API
  slug: finedata-ai-web-scraping-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/finedata-ai/agentic-access/finedata-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/finedata-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/finedata-ai/rate-limits/finedata-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/finedata-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/finedata-ai/rules/finedata-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/finedata-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/finedata-ai/json-ld/finedata-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/finedata-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/finedata-ai/vocabulary/finedata-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/finedata-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/finedata-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/finedata-ai/data-model/finedata-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finedata-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/finedata-ai/changelog/finedata-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/finedata-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://finedata.ai/legal/security/
- group: auth
  href: https://artifacts.apis.io/finedata-ai/authentication/finedata-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finedata-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/finedata-ai/errors/finedata-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finedata-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/finedata-ai/conformance/finedata-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finedata-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/finedata-ai/llms/finedata-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finedata-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/finedata-ai/a2a/finedata-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/finedata-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/finedata-ai/mcp/finedata-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/finedata-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/finedata-ai/mcp/finedata-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/finedata-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/finedata-ai/well-known/finedata-ai-modelcontextprotocol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finedata-ai-modelcontextprotocol-security.txt
- group: agent
  href: https://artifacts.apis.io/finedata-ai/well-known/finedata-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finedata-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/finedata-ai/hosts/finedata-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finedata-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/finedata-ai/vendors/finedata-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finedata-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://finedata.ai/status/
- group: auth
  title: ''
  type: Security
  url: https://finedata.ai/legal/security/
- group: start
  title: ''
  type: Login
  url: https://finedata.ai/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://finedata.ai/changelog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.finedata.ai</code
- group: auth
  href: https://artifacts.apis.io/finedata-ai/security/finedata-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/finedata-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/finedata-ai/security/finedata-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/finedata-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/finedata-ai/security/finedata-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finedata-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finedata.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://finedata.ai/docs/
- group: company
  title: ''
  type: Blog
  url: https://finedata.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://finedata.ai/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://finedata.ai/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finedata.ai/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finedata.ai/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quality-network
- group: start
  title: ''
  type: GettingStarted
  url: https://finedata.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.finedata.ai/openapi.json
created: '2026-10-30'
description: FineData.ai provides an AI‑powered web scraping service that extracts structured data from any website. It offers anti‑bot bypass, full JavaScript rendering, CAPTCHA solving, residential proxies, and batch processing. Users obtain an API key and can POST to endpoints like /api/v1/scrape to retrieve HTML or markdown. The platform supports Model Context Protocol (MCP) for AI agents, token‑based pricing, and detailed documentation. Hosted at api.finedata.ai, it emphasizes privacy, scalability, and developer‑friendly tooling.
image: https://finedata.ai/logo-light.svg
json_schemas:
- name: AsyncJobStatusResponse
  property_count: 21
  slug: finedata-ai-async-job-status-response
- name: AsyncScrapeRequest
  property_count: 34
  slug: finedata-ai-async-scrape-request
- name: BatchJobStatusResponse
  property_count: 8
  slug: finedata-ai-batch-job-status-response
- name: PublicScrapeRequest
  property_count: 34
  slug: finedata-ai-public-scrape-request
- name: PublicScrapeResponse
  property_count: 10
  slug: finedata-ai-public-scrape-response
- name: SerpRequest
  property_count: 7
  slug: finedata-ai-serp-request
jsonld:
- class_count: 25
  name: Finedata Ai Context
  property_count: 129
  slug: finedata-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.finedata.ai requiring OAuth.
  name: finedata-ai MCP Server
  slug: finedata-ai-mcp-yml
modified: '2026-10-30'
name: finedata-ai
nav: Providers
network: true
overview: 'finedata-ai publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Async Scraping API, Google SERP API, and 6 more. Tagged areas include Company, AI, WebScraping, DataExtraction, and MCP.


  The finedata-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  finedata-ai''s developer surface includes changelog, authentication, documentation, engineering blog, support, pricing, getting-started guide, and 31 more developer resources.'
plans:
- name: Finedata Ai Plans Pricing
  plan_count: 0
  slug: finedata-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Finedata Ai Rate Limits
  slug: finedata-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: finedata-ai API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: finedata-ai-rules
scopes:
- name: Finedata Ai Scopes
  scope_count: 0
  slug: finedata-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 79.1
    contract_quality: 57.7
    developer_ergonomics: 63.6
    discoverability: 65.0
    operational_transparency: 75.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Finedata Ai Authentication
  slug: finedata-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Finedata Ai Domain Security
  slug: finedata-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Finedata Ai Vulnerability Disclosure
  slug: finedata-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Finedata Ai Trust Center
  slug: finedata-ai-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: scrape-url
  slug: finedata-ai-scrape-url
slug: finedata-ai
tags:
- Company
- AI
- WebScraping
- DataExtraction
- MCP
- LLM
website: https://finedata.ai/
---
