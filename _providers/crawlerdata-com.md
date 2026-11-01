---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Crawlerdata Com Agentic Access
  operation_count: 5
  slug: crawlerdata-com-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.crawlerdata.com
  baseurl_source: declared
  description: 'Google Custom Search JSON API parameters and response format: switch by changing the base URL and key'
  name: crawlerdata-com Custom Search-compatible API
  slug: crawlerdata-com-custom-search-compatible-api
- baseURL: https://api.crawlerdata.com
  baseurl_source: declared
  description: Submit and fetch scraping jobs
  name: crawlerdata-com Jobs API
  slug: crawlerdata-com-jobs-api
- baseURL: https://api.crawlerdata.com
  baseurl_source: declared
  description: Open WebUI "External" web search provider
  name: crawlerdata-com Open WebUI API
  slug: crawlerdata-com-open-webui-api
- baseURL: https://api.crawlerdata.com
  baseurl_source: declared
  description: 'SerpApi parameters and response format: switch by changing the base URL'
  name: crawlerdata-com Serp API Compatible API
  slug: crawlerdata-com-serpapi-compatible-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/crawlerdata-com/agentic-access/crawlerdata-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crawlerdata-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/crawlerdata-com/plans/crawlerdata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crawlerdata-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crawlerdata-com/rules/crawlerdata-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crawlerdata-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crawlerdata-com/json-ld/crawlerdata-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crawlerdata-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crawlerdata-com/vocabulary/crawlerdata-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crawlerdata-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crawlerdata-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/crawlerdata-com/data-model/crawlerdata-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crawlerdata-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/crawlerdata-com/authentication/crawlerdata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crawlerdata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/crawlerdata-com/errors/crawlerdata-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crawlerdata-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crawlerdata-com/conformance/crawlerdata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crawlerdata-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crawlerdata-com/llms/crawlerdata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crawlerdata-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/crawlerdata-com/mcp/crawlerdata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crawlerdata-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crawlerdata-com/well-known/crawlerdata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crawlerdata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/crawlerdata-com/hosts/crawlerdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crawlerdata-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.crawlerdata.com/register
- group: docs
  title: ''
  type: APIReference
  url: https://crawlerdata.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrawlerData
- group: auth
  href: https://artifacts.apis.io/crawlerdata-com/security/crawlerdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crawlerdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crawlerdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crawlerdata.com/apis/google-search-api
- group: company
  title: ''
  type: Blog
  url: https://crawlerdata.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://crawlerdata.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crawlerdata.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crawlerdata.com/legal/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.crawlerdata.com/openapi.json
  - status: 401
    url: https://app.crawlerdata.com/api/mcp
  - status: 401
    url: https://api.crawlerdata.com/mcp
  - status: 200
    url: https://crawlerdata.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: CrawlerData provides a Google Search (SERP) API that returns organic search results, AI-generated overviews with sources, news, images, local business listings, and shopping data. The service offers both desktop and mobile result formats, enabling developers to integrate real-time Google search data into applications such as price monitoring, SEO tools, market research, and e‑commerce platforms. With endpoints for Google Shopping, Images, News, Local, and Autocomplete, CrawlerData delivers structured JSON responses that simplify consumption of Google’s search ecosystem.
image: https://crawlerdata.com/logo.png
json_schemas:
- name: GoogleImagesRequest
  property_count: 5
  slug: crawlerdata-com-google-images-request
- name: GoogleLocalRequest
  property_count: 5
  slug: crawlerdata-com-google-local-request
- name: GoogleNewsRequest
  property_count: 5
  slug: crawlerdata-com-google-news-request
- name: GoogleSearchRequest
  property_count: 5
  slug: crawlerdata-com-google-search-request
- name: GoogleShoppingProductRequest
  property_count: 5
  slug: crawlerdata-com-google-shopping-product-request
- name: GoogleShoppingSearchRequest
  property_count: 5
  slug: crawlerdata-com-google-shopping-search-request
jsonld:
- class_count: 12
  name: Crawlerdata Com Context
  property_count: 14
  slug: crawlerdata-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.crawlerdata.com.
  name: crawlerdata-com MCP Server
  slug: crawlerdata-com-mcp-yml
modified: '2026-10-30'
name: crawlerdata-com
nav: Providers
network: true
overview: 'crawlerdata-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Custom Search-compatible API, Jobs API, Open WebUI API, and 1 more. Tagged areas include Search, API, Google, SERP, and Data.


  The crawlerdata-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  crawlerdata-com''s developer surface includes authentication, signup flow, API reference, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Crawlerdata Com Plans Pricing
  plan_count: 4
  slug: crawlerdata-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Crawlerdata Com Rate Limits
  slug: crawlerdata-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: crawlerdata-com API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 1
  slug: crawlerdata-com-rules
scopes:
- name: Crawlerdata Com Scopes
  scope_count: 0
  slug: crawlerdata-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 60.6
    developer_ergonomics: 37.4
    discoverability: 65.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crawlerdata Com Authentication
  slug: crawlerdata-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Crawlerdata Com Domain Security
  slug: crawlerdata-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: submit-job
  slug: crawlerdata-com-submit-job
slug: crawlerdata-com
tags:
- Search
- API
- Google
- SERP
- Data
- E-commerce
- SEO
website: https://crawlerdata.com/
---
