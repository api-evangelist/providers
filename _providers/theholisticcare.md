---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Theholisticcare Agentic Access
  operation_count: 15
  slug: theholisticcare-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: A free, public, read‑only REST API exposing structured mindfulness resources such as research citations, glossary, games, audio practices, and blog excerpts.
  name: THC Open Mindfulness Resources API
  slug: thc-open-mindfulness-resources-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Health API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for health.
  name: The Holistic Care — THC Open Mindfulness API Health API
  slug: theholisticcare-health-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Resources API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for resources.
  name: The Holistic Care — THC Open Mindfulness API Resources API
  slug: theholisticcare-resources-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Search API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for search.
  name: The Holistic Care — THC Open Mindfulness API Search API
  slug: theholisticcare-search-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Blog API from The Holistic Care — THC Open Mindfulness API — 2 operation(s) for blog.
  name: The Holistic Care — THC Open Mindfulness API Blog API
  slug: theholisticcare-blog-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Categories API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for categories.
  name: The Holistic Care — THC Open Mindfulness API Categories API
  slug: theholisticcare-categories-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Glossary API from The Holistic Care — THC Open Mindfulness API — 2 operation(s) for glossary.
  name: The Holistic Care — THC Open Mindfulness API Glossary API
  slug: theholisticcare-glossary-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Mindfulness Games API from The Holistic Care — THC Open Mindfulness API — 2 operation(s) for mindfulness games.
  name: The Holistic Care — THC Open Mindfulness API Mindfulness Games API
  slug: theholisticcare-mindfulness-games-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Panchavikas API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for panchavikas.
  name: The Holistic Care — THC Open Mindfulness API Panchavikas API
  slug: theholisticcare-panchavikas-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Practices API from The Holistic Care — THC Open Mindfulness API — 2 operation(s) for practices.
  name: The Holistic Care — THC Open Mindfulness API Practices API
  slug: theholisticcare-practices-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Whitepapers API from The Holistic Care — THC Open Mindfulness API — 2 operation(s) for whitepapers.
  name: The Holistic Care — THC Open Mindfulness API Whitepapers API
  slug: theholisticcare-whitepapers-api
- description: Production remote MCP server (streamable HTTP, serverInfo thc-open-mindfulness "THC Open Mindfulness MCP" 1.0.0) with seven read-only, unauthenticated tools (search_mindfulness_resources, get_mindfuln
  name: THC Open Mindfulness MCP Server
  slug: thc-open-mindfulness-mcp-server
artifact_total: 32
common:
- group: other
  href: https://artifacts.apis.io/theholisticcare/capabilities/theholisticcare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/theholisticcare-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/theholisticcare/security/theholisticcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theholisticcare-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/theholisticcare/mcp/theholisticcare-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/theholisticcare-mcp.yml
- group: agent
  href: https://artifacts.apis.io/theholisticcare/llms/theholisticcare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/theholisticcare-llms.txt
- group: operate
  href: https://artifacts.apis.io/theholisticcare/rate-limits/theholisticcare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theholisticcare-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/theholisticcare/agentic-access/theholisticcare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/theholisticcare-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://api.theholisticcare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.theholisticcare.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.theholisticcare.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.theholisticcare.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theholisticcare.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theholisticcare.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.theholisticcare.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.theholisticcare.com/login
created: '2026-09-28'
description: The THC Open Mindfulness Resources API, provided by The Holistic Care, offers a free, public, read‑only REST API delivering a comprehensive collection of mindfulness resources. It includes research‑backed citations, an extensive glossary, sixteen interactive mindfulness games, one‑hundred eleven guided audio practices, and excerpts from over five hundred twenty‑seven blog posts. The API requires no authentication, API key, or cost, and supports searching and browsing across all resource families via the /v1/resources and /v1/search endpoints, enabling developers to integrate mindfulness content into applications effortlessly.
json_schemas:
- name: BlogPostDetailResponse
  property_count: 2
  slug: theholisticcare-blog-post-detail-response
- name: BlogPostListResponse
  property_count: 3
  slug: theholisticcare-blog-post-list-response
- name: CategoriesResponse
  property_count: 2
  slug: theholisticcare-categories-response
- name: CitationDetailResponse
  property_count: 2
  slug: theholisticcare-citation-detail-response
- name: CitationListResponse
  property_count: 3
  slug: theholisticcare-citation-list-response
- name: GameDetailResponse
  property_count: 2
  slug: theholisticcare-game-detail-response
- name: GameListResponse
  property_count: 3
  slug: theholisticcare-game-list-response
- name: GlossaryDetailResponse
  property_count: 2
  slug: theholisticcare-glossary-detail-response
- name: GlossaryListResponse
  property_count: 3
  slug: theholisticcare-glossary-list-response
- name: HealthResponse
  property_count: 3
  slug: theholisticcare-health-response
- name: PanchaVikasResourceListResponse
  property_count: 2
  slug: theholisticcare-pancha-vikas-resource-list-response
- name: PracticeDetailResponse
  property_count: 2
  slug: theholisticcare-practice-detail-response
- name: PracticeListResponse
  property_count: 3
  slug: theholisticcare-practice-list-response
- name: ResourceListResponse
  property_count: 3
  slug: theholisticcare-resource-list-response
jsonld:
- class_count: 26
  name: Theholisticcare Context
  property_count: 52
  slug: theholisticcare-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.theholisticcare.com.
  name: The Holistic Care — THC Open Mindfulness API MCP Server
  slug: theholisticcare-mcp-yml
modified: '2026-10-05'
name: The Holistic Care — THC Open Mindfulness API
nav: Providers
network: true
overview: 'The Holistic Care — THC Open Mindfulness API publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including THC Open Mindfulness Resources API, Health API, Resources API, and 9 more. Tagged areas include Mindfulness, Education, Health, OpenAPI, and Public APIs.


  The The Holistic Care — THC Open Mindfulness API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Holistic Care — THC Open Mindfulness API''s developer surface includes documentation, engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 1
  name: Theholisticcare Rate Limits
  slug: theholisticcare-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: The Holistic Care — THC Open Mindfulness API API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: theholisticcare-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.5
    catalog_earned_first_party: 8.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 63.2
    developer_ergonomics: 8.3
    discoverability: 63.3
    operational_transparency: 26.3
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 90.9
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/theholisticcare/theholisticcare-2026-10-11T130846.png
security:
- kind: domain-security
  name: Theholisticcare Domain Security
  slug: theholisticcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: theholisticcare
tags:
- Mindfulness
- Education
- Health
- OpenAPI
- Public APIs
- Free
website: https://api.theholisticcare.com/
---
