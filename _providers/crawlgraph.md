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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Hosted remote Model Context Protocol server at https://crawlgraph.com/mcp over Streamable HTTP, plus an open-source local stdio fallback published to npm as crawlgraph-mcp (MIT). Four tools — backlink
  name: CrawlGraph MCP Server
  slug: crawlgraph-mcp-server
- description: CrawlGraph public REST API v1 — backlink lookups, Common Crawl release discovery, async gap analysis, and cross-release change comparison.
  name: CrawlGraph V1 API
  slug: crawlgraph-v1-api
artifact_total: 9
collections:
- collection_type: open
  name: CrawlGraph
  slug: open-crawlgraph-v1
common:
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
  title: ''
  type: OpenAPI
  url: openapi/crawlgraph-v1-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crawlgraph-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crawlgraph-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crawlgraph-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crawlgraph-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/crawlgraph-security.txt
- group: auth
  title: ''
  type: Security
  url: security/crawlgraph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crawlgraph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crawlgraph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crawlgraph-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crawlgraph-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crawlgraph-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crawlgraph-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crawlgraph-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crawlgraph-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crawlgraph-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crawlgraph-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/crawlgraph-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/crawlgraph-v1-overlay.yaml
created: '2026-07-03'
description: 'CrawlGraph is a backlink-intelligence SaaS built on Common Crawl''s open hyperlink graph (121.1M domains / 3.90B domain-level links), positioned as a low-cost alternative to Ahrefs, Moz, Semrush and Majestic. It offers referring-domain lookups with authority scoring, competitor gap analysis, warm outreach-target discovery, and cross-release change comparison. The product ships an unusually complete developer surface for a solo-operator SaaS: a public OpenAPI 3.1 contract, a self-serve free API tier (15 backlink calls a month, no card), a hosted remote MCP server whose tools publish both input and output schemas, an open-source local MCP package on npm, a published llms.txt, and open CC-BY study datasets. It is operated by Search Engine Wizards in Finland and priced as a one-time $99 lifetime licence rather than a subscription.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crawlgraph.png
layout: provider
mcp_servers:
- description: ''
  name: CrawlGraph MCP Server
  slug: crawlgraph-mcp-server
modified: '2026-08-13'
name: CrawlGraph
nav: Providers
network: true
overview: 'CrawlGraph publishes 1 API on the [APIs.io](https://apis.io/) network: V1 API. Tagged areas include SEO, backlink-intelligence, MarTech, Competitive Intelligence, and Web Data.


  CrawlGraph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 25 more developer resources.'
plans:
- name: Crawlgraph Plans Pricing
  plan_count: 3
  slug: crawlgraph-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Crawlgraph Rate Limits
  slug: crawlgraph-rate-limits
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 59.2
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 53.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crawlgraph/refs/heads/main/screenshots/crawlgraph-2026-07-25T210652.png
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
slug: crawlgraph
tags:
- SEO
- backlink-intelligence
- MarTech
- Competitive Intelligence
- Web Data
- Common-Crawl
- link-building
- Developer Tools
- MCP
website: https://crawlgraph.com/docs/api
---
