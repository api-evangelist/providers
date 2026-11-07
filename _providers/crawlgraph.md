---
access_model:
  confidence: high
  label: Free tier · Self-serve signup · $99 lifetime
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Crawlgraph Agentic Access
  operation_count: 6
  slug: crawlgraph-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- description: Hosted remote Model Context Protocol server at https://crawlgraph.com/mcp over Streamable HTTP, plus an open-source local stdio fallback published to npm as crawlgraph-mcp (MIT). Four tools — backlink
  name: CrawlGraph MCP Server
  slug: crawlgraph-mcp-server
- baseURL: https://crawlgraph.com/mcp
  baseurl_source: declared
  description: The Backlinks API from CrawlGraph — 1 operation(s) for backlinks.
  name: CrawlGraph Backlinks API
  slug: crawlgraph-backlinks-api
- baseURL: https://crawlgraph.com/mcp
  baseurl_source: declared
  description: The Changes API from CrawlGraph — 1 operation(s) for changes.
  name: CrawlGraph Changes API
  slug: crawlgraph-changes-api
- baseURL: https://crawlgraph.com/mcp
  baseurl_source: declared
  description: The Free Key API from CrawlGraph — 1 operation(s) for free key.
  name: CrawlGraph Free Key API
  slug: crawlgraph-free-key-api
- baseURL: https://crawlgraph.com/mcp
  baseurl_source: declared
  description: The Gap Analysis API from CrawlGraph — 2 operation(s) for gap analysis.
  name: CrawlGraph Gap Analysis API
  slug: crawlgraph-gap-analysis-api
- baseURL: https://crawlgraph.com/mcp
  baseurl_source: declared
  description: The Releases API from CrawlGraph — 1 operation(s) for releases.
  name: CrawlGraph Releases API
  slug: crawlgraph-releases-api
artifact_total: 21
collections:
- collection_type: open
  name: CrawlGraph
  slug: open-crawlgraph-v1
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://crawlgraph.com/feed.xml
- group: other
  href: https://artifacts.apis.io/crawlgraph/capabilities/crawlgraph-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/crawlgraph-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.crawlgraph.com/
- group: agent
  href: https://artifacts.apis.io/crawlgraph/agentic-access/crawlgraph-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crawlgraph-agentic-access.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/pucilpet/crawlgraph-mcp/blob/master/LICENSE
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crawlgraph.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://crawlgraph.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://crawlgraph.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://crawlgraph.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://crawlgraph.com/blog
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pucilpet/crawlgraph-mcp
- group: start
  title: ''
  type: Login
  url: https://crawlgraph.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crawlgraph.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crawlgraph.com/privacy
- group: docs
  href: https://artifacts.apis.io/crawlgraph/openapi/crawlgraph-v1-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/crawlgraph-v1-api-openapi.yml
- group: agent
  href: https://artifacts.apis.io/crawlgraph/mcp/crawlgraph-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crawlgraph-mcp.yml
- group: build
  href: https://artifacts.apis.io/crawlgraph/mcp/crawlgraph-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/crawlgraph-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/crawlgraph/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/crawlgraph/llms/crawlgraph-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crawlgraph-llms.txt
- group: agent
  href: https://artifacts.apis.io/crawlgraph/well-known/crawlgraph-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crawlgraph-well-known.yml
- group: auth
  href: https://artifacts.apis.io/crawlgraph/well-known/crawlgraph-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crawlgraph-security.txt
- group: auth
  href: https://artifacts.apis.io/crawlgraph/security/crawlgraph-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/crawlgraph-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crawlgraph/security/crawlgraph-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crawlgraph-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crawlgraph/security/crawlgraph-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crawlgraph-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/crawlgraph/authentication/crawlgraph-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crawlgraph-authentication.yml
- group: design
  href: https://artifacts.apis.io/crawlgraph/conventions/crawlgraph-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crawlgraph-conventions.yml
- group: design
  href: https://artifacts.apis.io/crawlgraph/errors/crawlgraph-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crawlgraph-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crawlgraph/data-model/crawlgraph-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crawlgraph-data-model.yml
- group: operate
  href: https://artifacts.apis.io/crawlgraph/rate-limits/crawlgraph-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crawlgraph-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crawlgraph/plans/crawlgraph-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crawlgraph-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crawlgraph/lifecycle/crawlgraph-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crawlgraph-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/crawlgraph/conformance/crawlgraph-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crawlgraph-conformance.yml
- group: build
  href: https://artifacts.apis.io/crawlgraph/packages/crawlgraph-packages.yml
  title: ''
  type: Packages
  url: packages/crawlgraph-packages.yml
- group: other
  href: https://artifacts.apis.io/crawlgraph/overlays/crawlgraph-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crawlgraph-v1-overlay.yaml
- group: build
  href: https://artifacts.apis.io/crawlgraph/examples/crawlgraph-v1-examples.yml
  title: ''
  type: Examples
  url: examples/crawlgraph-v1-examples.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://crawlgraph.com/#pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pucilpet
- group: operate
  href: https://artifacts.apis.io/crawlgraph/lifecycle/crawlgraph-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/crawlgraph-lifecycle.yml
created: '2026-07-03'
description: 'CrawlGraph is a backlink-intelligence SaaS built on Common Crawl''s open hyperlink graph (121.1M domains / 3.90B domain-level links), positioned as a low-cost alternative to Ahrefs, Moz, Semrush and Majestic. It offers referring-domain lookups with authority scoring, competitor gap analysis, warm outreach-target discovery, and cross-release change comparison. The product ships an unusually complete developer surface for a solo-operator SaaS: a public OpenAPI 3.1 contract, a self-serve free API tier (15 backlink calls a month, no card), a hosted remote MCP server whose tools publish both input and output schemas, an open-source local MCP package on npm, a published llms.txt, and open CC-BY study datasets. It is operated by Search Engine Wizards in Finland and priced as a one-time $99 lifetime licence rather than a subscription.'
finops:
- has_sources: true
  method: derived
  name: Crawlgraph Finops
  primary_unit: account
  service_category: ''
  slug: crawlgraph-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crawlgraph.png
layout: provider
mcp_servers:
- description: Remote MCP server at crawlgraph.com requiring an API key; 4 tools listed.
  name: CrawlGraph MCP Server
  slug: crawlgraph-mcp-yml
modified: '2026-10-06'
name: CrawlGraph
nav: Providers
network: true
overview: 'CrawlGraph publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Backlinks API, Changes API, Free Key API, and 3 more. Tagged areas include SEO, backlink-intelligence, MarTech, Competitive Intelligence, and Web Data.


  The CrawlGraph catalog on APIs.io includes 1 Spectral governance ruleset.


  CrawlGraph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, code examples, pricing, and 31 more developer resources.'
plans:
- name: Crawlgraph Plans Pricing
  plan_count: 4
  slug: crawlgraph-plans-pricing
- name: Crawlgraph Price Estimates
  plan_count: 0
  slug: crawlgraph-price-estimates
random_paper: 11
rate_limits:
- limit_count: 4
  name: Crawlgraph Rate Limits
  slug: crawlgraph-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: CrawlGraph API Rules
  rule_count: 48
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 1
  slug: crawlgraph-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 72.4
    contract_governance: 31.8
    contract_quality: 48.3
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/crawlgraph/crawlgraph-2026-07-25T210652.png
security:
- kind: authentication
  name: Crawlgraph Authentication
  slug: crawlgraph-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crawlgraph Domain Security
  slug: crawlgraph-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Crawlgraph Vulnerability Disclosure
  slug: crawlgraph-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: Compare link observations across Common Crawl releases
  slug: crawlgraph-compare-link-changes-across-releases
- name: Find warm outreach targets over MCP
  slug: crawlgraph-find-warm-outreach-targets
- name: Look up referring domains for a domain
  slug: crawlgraph-look-up-referring-domains
- name: Run a competitor backlink gap analysis
  slug: crawlgraph-run-a-competitor-gap-analysis
slug: crawlgraph
tags:
- SEO
- backlink-intelligence
- MarTech
- Competitive Intelligence
- Web Data
- Common-Crawl
- Link Building
- Developer Tools
- MCP
website: https://www.crawlgraph.com/
---
