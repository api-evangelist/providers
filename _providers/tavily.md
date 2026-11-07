---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tavily Agentic Access
  operation_count: 5
  slug: tavily-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: The Tavily Web API offers a unified set of endpoints for AI agents to search the web, extract page content, crawl sites, map sitemaps, and run AI research tasks. Endpoints are REST-based and authentic
  name: Tavily Web API
  slug: web-api
- baseURL: https://api.tavily.com
  baseurl_source: declared
  description: The Crawl API from Tavily — 1 operation(s) for crawl.
  name: Tavily Crawl API
  slug: tavily-crawl-api
- baseURL: https://api.tavily.com
  baseurl_source: declared
  description: The Extract API from Tavily — 1 operation(s) for extract.
  name: Tavily Extract API
  slug: tavily-extract-api
- baseURL: https://api.tavily.com
  baseurl_source: declared
  description: The Map API from Tavily — 1 operation(s) for map.
  name: Tavily Map API
  slug: tavily-map-api
- baseURL: https://api.tavily.com
  baseurl_source: declared
  description: The Research API from Tavily — 1 operation(s) for research.
  name: Tavily Research API
  slug: tavily-research-api
- baseURL: https://api.tavily.com
  baseurl_source: declared
  description: The Search API from Tavily — 1 operation(s) for search.
  name: Tavily Search API
  slug: tavily-search-api
artifact_total: 22
collections:
- collection_type: open
  name: Tavily Web Crawl API
  slug: open-tavily-crawl-api
- collection_type: open
  name: Tavily Web Crawl Extract API
  slug: open-tavily-extract-api
- collection_type: open
  name: Tavily Web Crawl Map API
  slug: open-tavily-map-api
- collection_type: open
  name: Tavily Web Crawl Research API
  slug: open-tavily-research-api
- collection_type: open
  name: Tavily Web Crawl Search API
  slug: open-tavily-search-api
- collection_type: open
  name: Tavily Web API
  slug: open-tavily
common:
- group: commercial
  href: https://artifacts.apis.io/tavily/plans/tavily-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tavily-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tavily/rate-limits/tavily-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tavily-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tavily/finops/tavily-finops.yml
  title: ''
  type: FinOps
  url: finops/tavily-finops.yml
- group: other
  href: https://artifacts.apis.io/tavily/a2a/tavily-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tavily-a2a.yml
- group: agent
  href: https://artifacts.apis.io/tavily/agentic-access/tavily-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tavily-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tavily/security/tavily-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tavily-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tavily/security/tavily-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tavily-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tavily/authentication/tavily-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tavily-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tavily.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tavily.com
- group: company
  title: ''
  type: Blog
  url: https://blog.tavily.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tavily-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tavily.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tavily.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tavily.com/privacy
- group: operate
  title: ''
  type: Community
  url: https://community.tavily.com
- group: other
  title: ''
  type: X
  url: https://x.com/tavilyai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tavily
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@tavilyai
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tavily.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:support@tavily.com
created: '2026-05-23'
description: Tavily is a web access API platform optimized for LLMs and AI agents. It exposes a unified REST surface for real-time web search, page content extraction, site crawling, sitemap mapping, and AI-driven research tasks. The platform emphasizes low-latency search with a 180ms p50 on the search endpoint, a 99.99% uptime SLA, and built-in content validation safeguards. Tavily ships Python and JavaScript SDKs and integrates cleanly with major agent frameworks and LLM providers such as OpenAI, Anthropic, and Groq. Used by more than a million developers, it is trusted by enterprise customers including Databricks, IBM, JetBrains, MongoDB, and AWS.
finops:
- has_sources: true
  method: derived
  name: Tavily Finops
  primary_unit: credit
  service_category: ''
  slug: tavily-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.tavily.com over HTTP.
  name: Tavily MCP Server
  slug: tavily
modified: '2026-05-23'
name: Tavily
nav: Providers
network: true
overview: 'Tavily publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Crawl API, Extract API, Map API, and 3 more. Tagged areas include Search, Web Search, AI Agents, LLM, and Extract.


  The Tavily catalog on APIs.io includes 1 Spectral governance ruleset.


  Tavily''s developer surface includes authentication, documentation, engineering blog, pricing, YouTube channel, support, and 15 more developer resources.'
plans:
- name: Tavily Plans Pricing
  plan_count: 4
  slug: tavily-plans-pricing
- name: Tavily Price Estimates
  plan_count: 0
  slug: tavily-price-estimates
random_paper: 17
rate_limits:
- limit_count: 2
  name: Tavily Rate Limits
  slug: tavily-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Tavily API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: tavily-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.5
    catalog_earned_first_party: 12.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 13.6
    contract_quality: 49.0
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 7.9
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tavily/tavily-2026-06-20T194930.png
security:
- kind: authentication
  name: Tavily Authentication
  slug: tavily-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tavily Domain Security
  slug: tavily-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tavily Trust Center
  slug: tavily-trust-center
  summary_line: trust center published
slug: tavily
tags:
- Search
- Web Search
- AI Agents
- LLM
- Extract
- Crawl
- Sitemap
- Research
- REST
- LangChain
- LlamaIndex
- Real-Time
- A2A
website: https://www.tavily.com
---
