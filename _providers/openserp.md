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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Openserp Agentic Access
  operation_count: 18
  slug: openserp-agentic-access
  summary_line: 18 operations · 4 acting
api_count: 1
apis:
- description: The managed, hosted version of the OpenSERP search API. Bearer-token authenticated, credit-metered pay-as-you-go REST API exposing single-engine web and image search across Google, Bing, Yandex, Baidu
  name: OpenSERP Cloud API
  slug: openserp-cloud
- baseURL: https://api.openserp.org
  baseurl_source: declared
  description: OpenAPI and Swagger UI endpoints
  name: OpenSERP Docs API
  slug: openserp-docs-api
- baseURL: https://api.openserp.org
  baseurl_source: declared
  description: Health and readiness endpoints
  name: OpenSERP Health API
  slug: openserp-health-api
- baseURL: https://api.openserp.org
  baseurl_source: declared
  description: Cross-engine aggregated search endpoints
  name: OpenSERP Mega API
  slug: openserp-mega-api
- baseURL: https://api.openserp.org
  baseurl_source: declared
  description: Dedicated per-engine search endpoints
  name: OpenSERP Search API
  slug: openserp-search-api
- baseURL: https://api.openserp.org
  baseurl_source: declared
  description: Runtime statistics endpoints
  name: OpenSERP Stats API
  slug: openserp-stats-api
artifact_total: 13
asyncapis:
- description: ''
  name: Openserp Monitor Webhooks
  slug: openserp-monitor-webhooks
collections:
- collection_type: open
  name: OpenSERP API
  slug: open-openserp-oss
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/karust/openserp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/karust/openserp/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/karust/openserp/blob/main/docs/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/karust/openserp/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openserp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openserp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openserp.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openserp.org/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://openserp.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://openserp.org/docs/cloud-endpoints/
- group: start
  title: ''
  type: GettingStarted
  url: https://openserp.org/docs/cloud-quickstart/
- group: auth
  title: ''
  type: Authentication
  url: https://openserp.org/docs/cloud-authentication/
- group: design
  title: ''
  type: ErrorCatalog
  url: https://openserp.org/docs/cloud-errors/
- group: commercial
  title: ''
  type: Pricing
  url: https://openserp.org/pricing/
- group: commercial
  title: ''
  type: Plans
  url: https://openserp.org/docs/cloud-pricing/
- group: company
  title: ''
  type: Blog
  url: https://openserp.org/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://openserp.org/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openserpapi
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/karust/openserp
- group: agent
  title: ''
  type: LLMsTxt
  url: https://openserp.org/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: https://openserp.org/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: https://openserp.org/.well-known/mcp.json
- group: start
  title: ''
  type: Login
  url: https://openserp.org/login/
- group: start
  title: ''
  type: SignUp
  url: https://openserp.org/register/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openserp.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openserp.org/privacy/
- group: operate
  title: ''
  type: Support
  url: mailto:support@openserp.org
- group: operate
  title: ''
  type: Community
  url: https://t.me/openserp_cloud
- group: auth
  title: ''
  type: Authentication
  url: authentication/openserp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openserp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openserp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openserp-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openserp-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/openserp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openserp-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/openserp-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/openserp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openserp-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openserp-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openserp-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/openserp-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openserp-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openserp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/openserp-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/openserp-monitor-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/openserp-oss-overlay.yaml
created: '2026-08-10'
description: OpenSERP is an open-source, self-hostable SERP API that returns structured search results from Google, Bing, Yandex, Baidu, DuckDuckGo and Ecosia through one REST interface, alongside OpenSERP Cloud, a managed pay-as-you-go version of the same API adding page extraction, multi-engine megasearch, image search and scheduled rank monitoring. The self-hosted server ships an MIT-licensed Go binary and CLI with a published OpenAPI 3.0.3 contract, a v2 response envelope carrying query echo, metadata, normalized results and pagination, plus cache, proxy-pool and circuit-breaker telemetry endpoints. OpenSERP Cloud adds bearer-token authentication, credit-metered billing, engine health routing, batch URL extraction and Search Monitor webhooks, and the project publishes first-party JavaScript and Python SDKs, an MCP server and an n8n community node.
image: https://openserp.org/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: OpenSERP MCP Server
  slug: openserp-mcp-server
- description: Model Context Protocol server for OpenSERP OSS and OpenSERP Cloud. Exposes live SERP search, multi-engine search, image search, single and batch URL extraction, usage and engine-listing tools.
  name: OpenSERP MCP Server
  slug: openserp-mcp-server-2
modified: '2026-08-10'
name: OpenSERP
nav: Providers
network: true
overview: 'OpenSERP publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Docs API, Health API, Mega API, and 2 more. Tagged areas include Company, Search, SERP, Search API, and Web Scraping.


  The OpenSERP catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenSERP''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, engineering blog, signup flow, and 40 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 51.3
    developer_ergonomics: 78.0
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openserp/refs/heads/main/screenshots/openserp-2026-08-17T081125.png
security:
- kind: authentication
  name: Openserp Authentication
  slug: openserp-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Openserp Domain Security
  slug: openserp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openserp
tags:
- Company
- Search
- SERP
- Search API
- Web Scraping
- Content Extraction
- AI Grounding
- Rank Tracking
- Open-Source
- Developer Tools
website: https://openserp.org
---
