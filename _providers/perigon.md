---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.0
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Perigon Agentic Access
  operation_count: 45
  slug: perigon-agentic-access
  summary_line: 45 operations · 19 acting
api_count: 2
apis:
- description: Hosted remote Model Context Protocol server (Streamable HTTP, with an SSE variant) exposing Perigon news search, analytics and monitor tools to AI clients. Authenticates with a Perigon API key as a be
  name: Perigon MCP Server
  slug: perigon-mcp
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: These endpoints enable semantic search beyond traditional keyword matching, content summarization, and advanced information retrieval across articles
  name: Perigon AI & Advanced Search API
  slug: perigon-ai-advanced-search-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Manage contact points used to deliver monitor notifications. Contact points define where and how monitor events are delivered (e.g. webhooks). Only WEBHOOK contact points can be created and managed vi
  name: Perigon Contact Points API
  slug: perigon-contact-points-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Manage AI Monitors — configurable monitors that continuously scan news content for topics, entities, and events of interest. Monitors run asynchronously and emit structured events and AI-generated sum
  name: Perigon Monitors API
  slug: perigon-monitors-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Endpoints for accessing news articles and stories
  name: Perigon News & Stories API
  slug: perigon-news-stories-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Manage custom source groups for organizing and filtering news sources. Source groups allow grouping domains together for use in search queries and monitors.
  name: Perigon Source Groups API
  slug: perigon-source-groups-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Additional endpoints for metadata and related information
  name: Perigon Supplemental Endpoints API
  slug: perigon-supplemental-endpoints-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: The Utilities API from Perigon — 1 operation(s) for utilities.
  name: Perigon Utilities API
  slug: perigon-utilities-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Manage watchlists of people and companies for use with monitors. Watchlists can contain up to 100 combined entities and are used to track mentions across news content.
  name: Perigon Watchlists API
  slug: perigon-watchlists-api
- baseURL: https://api.perigon.io
  baseurl_source: declared
  description: Endpoints for searching ingested Wikipedia content. Provides keyword and filtered search capabilities along with vector-based semantic search across Wikipedia pages.
  name: Perigon Wikipedia API
  slug: perigon-wikipedia-api
artifact_total: 17
asyncapis:
- description: ''
  name: Perigon Webhooks
  slug: perigon-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/agentic-access/perigon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/perigon-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/rate-limits/perigon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/perigon-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/plans/perigon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/perigon-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/asyncapi/perigon-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/perigon-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/data-model/perigon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/perigon-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/changelog/perigon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/perigon-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/conventions/perigon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/perigon-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/authentication/perigon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/perigon-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://perigon.io/api-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perigon.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/lifecycle/perigon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/perigon-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/errors/perigon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/perigon-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/conformance/perigon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/perigon-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/overlays/perigon-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/perigon-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/llms/perigon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/perigon-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/mcp/perigon-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/perigon-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/mcp/perigon-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/perigon-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/well-known/perigon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/perigon-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/packages/perigon-packages.yml
  title: ''
  type: SDKs
  url: packages/perigon-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/packages/perigon-packages.yml
  title: ''
  type: Packages
  url: packages/perigon-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perigon/refs/heads/main/security/perigon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perigon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://perigon.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://perigon.io/docs/api/intro
- group: docs
  title: ''
  type: Documentation
  url: https://perigon.io/docs/api/intro
- group: docs
  title: ''
  type: APIReference
  url: https://perigon.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://perigon.io/docs/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://perigon.io/contact
- group: operate
  title: ''
  type: FAQ
  url: https://perigon.io/docs/api/faqs
- group: company
  title: ''
  type: Blog
  url: https://perigon.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://perigon.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goperigon
- group: commercial
  title: ''
  type: Pricing
  url: https://perigon.io/products/pricing/apis
- group: start
  title: ''
  type: SignUp
  url: https://perigon.io/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://perigon.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://perigon.io/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goperigon
- group: other
  title: ''
  type: Playground
  url: https://perigon.io/sandbox
created: '2026-09-20'
description: Perigon is a real-time global news data and intelligence platform. It provides structured, enriched news data from 200,000+ sources worldwide through REST APIs — articles, clustered stories, AI search summaries, semantic vector search, sources, companies, people, journalists, topics and Wikipedia — plus Signals, an AI-driven monitoring product with monitors, watchlists, contact points and signed webhooks. Perigon publishes an OpenAPI description, a hosted remote MCP server, official TypeScript, Python and Go SDKs, Agent Skills, and an API versioning and deprecation policy.
image: https://perigon.io/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Perigon MCP Server
  slug: perigon-mcp-server
modified: '2026-09-20'
name: Perigon
nav: Providers
network: true
overview: 'Perigon publishes 9 APIs on the [APIs.io](https://apis.io/) network, including AI & Advanced Search API, Contact Points API, Monitors API, and 6 more. Tagged areas include Company, News, Media Monitoring, Search, and Artificial Intelligence.


  The Perigon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Perigon''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, FAQ, and 31 more developer resources.'
plans:
- name: Perigon Plans Pricing
  plan_count: 4
  slug: perigon-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Perigon Rate Limits
  slug: perigon-rate-limits
score:
  band: exemplar
  composite: 67.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 70.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 84.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Perigon Authentication
  slug: perigon-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Perigon Domain Security
  slug: perigon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: perigon
tags:
- Company
- News
- Media Monitoring
- Search
- Artificial Intelligence
- Data
- MCP
- Webhook
website: https://perigon.io/
---
