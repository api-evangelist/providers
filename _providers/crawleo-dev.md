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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Crawleo Dev Agentic Access
  operation_count: 3
  slug: crawleo-dev-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.crawleo.dev
  baseurl_source: declared
  description: The Crawl API from crawleo-dev — 1 operation(s) for crawl.
  name: crawleo-dev Crawl API
  slug: crawleo-dev-crawl-api
- baseURL: https://api.crawleo.dev
  baseurl_source: declared
  description: The Google Maps API from crawleo-dev — 1 operation(s) for google maps.
  name: crawleo-dev Google Maps API
  slug: crawleo-dev-google-maps-api
- baseURL: https://api.crawleo.dev
  baseurl_source: declared
  description: The Search API from crawleo-dev — 1 operation(s) for search.
  name: crawleo-dev Search API
  slug: crawleo-dev-search-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/crawleo-dev/agentic-access/crawleo-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crawleo-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/crawleo-dev/rate-limits/crawleo-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crawleo-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crawleo-dev/plans/crawleo-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crawleo-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crawleo-dev/rules/crawleo-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/crawleo-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/crawleo-dev/json-ld/crawleo-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crawleo-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/crawleo-dev/vocabulary/crawleo-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crawleo-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crawleo-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/crawleo-dev/data-model/crawleo-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crawleo-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/crawleo-dev/authentication/crawleo-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crawleo-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/crawleo-dev/errors/crawleo-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crawleo-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crawleo-dev/conformance/crawleo-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crawleo-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crawleo-dev/llms/crawleo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crawleo-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/crawleo-dev/a2a/crawleo-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/crawleo-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/crawleo-dev/mcp/crawleo-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crawleo-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crawleo-dev/well-known/crawleo-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crawleo-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/crawleo-dev/hosts/crawleo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crawleo-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/crawleo-dev/vendors/crawleo-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crawleo-dev-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.crawleo.dev/playground
- group: company
  title: ''
  type: Newsroom
  url: https://www.crawleo.dev/news
- group: auth
  href: https://artifacts.apis.io/crawleo-dev/security/crawleo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crawleo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crawleo.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.crawleo.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crawleo.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crawleo.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crawleo.dev/login
- group: start
  title: ''
  type: SignUp
  url: https://www.crawleo.dev/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@crawleo.dev
- group: company
  title: ''
  type: Blog
  url: https://www.crawleo.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crawleo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crawleo.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crawleo.dev/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crawleo.dev/policies/privacy
created: '2026-10-30'
description: Crawleo provides a unified Search and Crawl API designed for AI and LLM applications. It aggregates results from Bing, Google Search, Google Maps, and performs web crawling with an anti-bot headful browser. The platform delivers clean Markdown output, supports native Model Context Protocol (MCP), and offers flexible credit‑based pricing. Developers can integrate search, crawling, and data extraction in a single endpoint, simplifying RAG pipelines and AI data workflows.
image: https://www.crawleo.dev/dark-mode-logo.svg
json_schemas:
- name: CrawlResponse
  property_count: 3
  slug: crawleo-dev-crawl-response
- name: GoogleMapsResponse
  property_count: 3
  slug: crawleo-dev-google-maps-response
- name: SearchResponse
  property_count: 4
  slug: crawleo-dev-search-response
jsonld:
- class_count: 4
  name: Crawleo Dev Context
  property_count: 9
  slug: crawleo-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.crawleo.dev.
  name: crawleo-dev MCP Server
  slug: crawleo-dev-mcp-yml
modified: '2026-10-30'
name: crawleo-dev
nav: Providers
network: true
overview: 'crawleo-dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Crawl API, Google Maps API, and Search API. Tagged areas include AI, Search, Crawling, API, and MCP.


  The crawleo-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  crawleo-dev''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, signup flow, support, and 25 more developer resources.'
plans:
- name: Crawleo Dev Plans Pricing
  plan_count: 4
  slug: crawleo-dev-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Crawleo Dev Rate Limits
  slug: crawleo-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: crawleo-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: crawleo-dev-rules
score:
  band: strong
  composite: 64.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 93.3
    catalog_earned_first_party: 0.0
    catalog_gap: 21.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 56.7
    developer_ergonomics: 70.7
    discoverability: 66.7
    operational_transparency: 33.7
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
  name: Crawleo Dev Authentication
  slug: crawleo-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Crawleo Dev Domain Security
  slug: crawleo-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: crawleo
  slug: crawleo-dev-crawleo
slug: crawleo-dev
tags:
- AI
- Search
- Crawling
- API
- MCP
website: https://crawleo.dev/
---
