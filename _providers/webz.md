---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-09-24'
api_count: 13
apis:
- description: 'Token-authenticated REST endpoints under https://api.webz.io covering seven products: News, Blogs and Forums (/api/news, /api/blogs, /api/forums plus /seg_api/* segmentation), Reviews (/reviewFilter, '
  name: Webz.io API
  slug: webzio-api
- description: A first-party remote Model Context Protocol server that exposes Webz.io semantic news search to any MCP client. It ships one tool, news_search_by_webz, and every call runs a regular News Search API re
  name: Webz.io News Search MCP Server
  slug: webzio-news-search-mcp-server
- description: Live open-web content split by source type. One base URL, six GET endpoints (`/api/news`, `/api/blogs`, `/api/forums` for posts and `/seg_api/news`, `/seg_api/blogs`, `/seg_api/forums` for aggregate s
  name: Webz.io News, Blogs & Forums API
  slug: webzio-news-blogs-forums-api
- description: Contextual, natural-language news search. Single `POST /api/news/context` endpoint that returns ranked article excerpts matching a free-text query. Backs the hosted News Search MCP server and the Lang
  name: Webz.io News Search API
  slug: webzio-news-search-api
- description: Deep and dark web content for threat intelligence. Search endpoint `/cyberFilter`, segmentation `/cyberSeg`, and helper endpoints `/dark-cache` (cached page snapshots) and `/cyber-image` (collected im
  name: Webz.io Cyber API
  slug: webzio-cyber-api
- description: Search compromised records and look up known breaches. Two GET endpoints, `/breaches` (main search) and `/breachCatalog` (breach lookup by name to UUID), authenticated with an API token as a query par
  name: Webz.io Data Breaches API
  slug: webzio-data-breaches-api
- description: Look up leaked session cookies matched to a domain. Single GET endpoint `/cookies` with token authentication and domain-scoped credit consumption.
  name: Webz.io Leaked Cookies API
  slug: webzio-leaked-cookies-api
- description: Detect leaked machine credentials (API keys, tokens, secrets) tied to a domain. Single GET endpoint `/nhi` with token authentication.
  name: Webz.io Non-Human Identities (NHI) API
  slug: webzio-non-human-identities-nhi-api
- description: REST-delivered curated firehose of enriched open-web posts. Preconfigured per-customer feeds via `/firehose?token=&client_feed=`; paginated with `nextPage`. Successor to the FTP-based Legacy Firehose.
  name: Webz.io Firehose API
  slug: webzio-firehose-api
- description: 'Build and deliver historical datasets in three steps - set query and date range at `/setArchiveQuery`, confirm at `/confirmArchiveQuery`, then poll `/getArchiveOrderStatus` for the ZIP download link. '
  name: Webz.io Archive API
  slug: webzio-archive-api
- description: Customer reviews and ratings collected from across the open web as structured JSON - rating, author, language, and the item being reviewed. Shares the News/Blogs/Forums query language but is a separat
  name: Webz.io Reviews API
  slug: webzio-reviews-api
- description: Analyze a domain's exposure across breach, leaked-cookie, and NHI datasets. Served from `api.lunarcyber.com` (Webz.io's Lunar-branded cyber intelligence surface); single GET endpoint `/domain-exposure
  name: Webz.io Domain Exposure API (DEA)
  slug: webzio-domain-exposure-api-dea
- description: Legacy unified `/filterWebContent` endpoint (GET or POST) that returned any open-web content type in one call. Deprecated in favor of the split News, Blogs & Forums APIs but still documented.
  name: Webz.io Web Content API (deprecated)
  slug: webzio-web-content-api-deprecated
artifact_total: 21
common:
- group: operate
  title: ''
  type: HelpCenter
  url: https://webz.io/help/
- group: company
  title: ''
  type: Website
  url: https://www.webz.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/security/webz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webz-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/well-known/webz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webz-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/mcp/webz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/webz-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/llms/webz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webz-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/packages/webz-packages.yml
  title: ''
  type: Packages
  url: packages/webz-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/packages/webz-packages.yml
  title: ''
  type: SDKs
  url: packages/webz-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/conformance/webz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/webz-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/conformance/webz-conformance.yml
  title: ''
  type: Compliance
  url: conformance/webz-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/errors/webz-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/webz-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/lifecycle/webz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/webz-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/lifecycle/webz-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/webz-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webz.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/scopes/webz-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/webz-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/authentication/webz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/webz-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/security/webz-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/webz-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/conventions/webz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/webz-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/data-model/webz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/webz-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/plans/webz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/webz-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/rate-limits/webz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/webz-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.webz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webz.io/docs/webz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.webz.io/docs/webz/news-blogs-forums-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.webz.io/docs/webz/start-here
- group: operate
  title: ''
  type: Support
  url: https://webz.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://webz.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Webhose
- group: commercial
  title: ''
  type: Pricing
  url: https://webz.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.webz.io/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.webz.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webz.io/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webz.io/privacy/
created: '2026-08-27'
description: Webz.io provides structured web-data feeds and APIs covering the open, deep, and dark web for AI, cybersecurity, and intelligence use cases. Content is collected at scale, normalized, enriched with metadata, and delivered through machine-readable data feeds and token-authenticated REST APIs.
image: https://webz.io/wp-content/uploads/2026/08/Webz.io-og-image.png
layout: provider
mcp_servers:
- description: A first-party remote MCP server that exposes Webz.io semantic news search to any MCP client. It ships exactly one tool, news_search_by_webz, and every call runs a regular News Search API request again
  name: Webz.io News Search MCP
  slug: webzio-news-search-mcp
- description: ''
  name: Webz.io MCP Server
  slug: webzio-mcp-server
modified: '2026-08-27'
name: Webz.io
nav: Providers
network: true
overview: 'Webz.io publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include News Data, Web Data, Web Scraping, Dark Web, and deep-web.


  Webz.io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Webz Plans Pricing
  plan_count: 6
  slug: webz-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Webz Rate Limits
  slug: webz-rate-limits
scopes:
- name: Webz Scopes
  scope_count: 0
  slug: webz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 81.5
    operational_transparency: 57.9
  previous_composite: 50.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/webz/refs/heads/main/screenshots/webz-2026-09-02T170544.png
security:
- kind: authentication
  name: Webz Authentication
  slug: webz-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Webz Domain Security
  slug: webz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Webz Trust Center
  slug: webz-trust-center
  summary_line: SOC 2, ISO 27001
slug: webz
tags:
- News Data
- Web Data
- Web Scraping
- Dark Web
- deep-web
- Cybersecurity
- Threat Intelligence
- Data Breach
- pii-monitoring
- OSINT
- reviews-data
- AI Training Data
- Media Monitoring
website: https://www.webz.io/
---
