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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-09-03'
api_count: 15
apis:
- description: Ahrefs' hosted, remote Model Context Protocol server, which lets AI agents query the Ahrefs API on behalf of a signed-in Ahrefs account. Streamable HTTP transport, OAuth 2.0 with PKCE (scope apiv3-mcp
  name: Ahrefs MCP Server
  slug: mcp
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The AI visibility API from Ahrefs — 3 operation(s) for ai visibility.
  name: Ahrefs AI visibility API
  slug: ahrefs-ai-visibility-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: GSC anonymous queries data
  name: Ahrefs Anonymous queries API
  slug: ahrefs-anonymous-queries-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Backlinks data
  name: Ahrefs Backlinks profile API
  slug: ahrefs-backlinks-profile-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Batch Analysis table
  name: Ahrefs Batch Analysis API
  slug: ahrefs-batch-analysis-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Brand Radar prompts API from Ahrefs — 2 operation(s) for brand radar prompts.
  name: Ahrefs Brand Radar prompts API
  slug: ahrefs-brand-radar-prompts-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Brand radar reports API from Ahrefs — 1 operation(s) for brand radar reports.
  name: Ahrefs Brand radar reports API
  slug: ahrefs-brand-radar-reports-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Channels API from Ahrefs — 2 operation(s) for channels.
  name: Ahrefs Channels API
  slug: ahrefs-channels-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Competitors API from Ahrefs — 2 operation(s) for competitors.
  name: Ahrefs Competitors API
  slug: ahrefs-competitors-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Data from competitors
  name: Ahrefs Competitors Overview API
  slug: ahrefs-competitors-overview-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Crawler API from Ahrefs — 2 operation(s) for crawler.
  name: Ahrefs Crawler API
  slug: ahrefs-crawler-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Domain Rating API from Ahrefs — 2 operation(s) for domain rating.
  name: Ahrefs Domain Rating API
  slug: ahrefs-domain-rating-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Geography API from Ahrefs — 8 operation(s) for geography.
  name: Ahrefs Geography API
  slug: ahrefs-geography-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Keyword ideas reports
  name: Ahrefs Keyword ideas API
  slug: ahrefs-keyword-ideas-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Keyword lists API from Ahrefs — 2 operation(s) for keyword lists.
  name: Ahrefs Keyword lists API
  slug: ahrefs-keyword-lists-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: GSC keywords data
  name: Ahrefs Keywords API
  slug: ahrefs-keywords-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Limits and usage API from Ahrefs — 1 operation(s) for limits and usage.
  name: Ahrefs Limits and usage API
  slug: ahrefs-limits-and-usage-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Locations and languages API from Ahrefs — 1 operation(s) for locations and languages.
  name: Ahrefs Locations and languages API
  slug: ahrefs-locations-and-languages-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The MCP API from Ahrefs — 7 operation(s) for mcp.
  name: Ahrefs MCP API
  slug: ahrefs-mcp-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Organic search data
  name: Ahrefs Organic search API
  slug: ahrefs-organic-search-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Outgoing links data
  name: Ahrefs Outgoing links API
  slug: ahrefs-outgoing-links-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Overview API from Ahrefs — 29 operation(s) for overview.
  name: Ahrefs Overview API
  slug: ahrefs-overview-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Overview history API from Ahrefs — 4 operation(s) for overview history.
  name: Ahrefs Overview history API
  slug: ahrefs-overview-history-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Page content API from Ahrefs — 1 operation(s) for page content.
  name: Ahrefs Page content API
  slug: ahrefs-page-content-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Page explorer API from Ahrefs — 1 operation(s) for page explorer.
  name: Ahrefs Page explorer API
  slug: ahrefs-page-explorer-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: GSC pages data
  name: Ahrefs Pages API
  slug: ahrefs-pages-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: Paid search data
  name: Ahrefs Paid search API
  slug: ahrefs-paid-search-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Posts API from Ahrefs — 5 operation(s) for posts.
  name: Ahrefs Posts API
  slug: ahrefs-posts-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Projects API from Ahrefs — 3 operation(s) for projects.
  name: Ahrefs Projects API
  slug: ahrefs-projects-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: SERP Overview data
  name: Ahrefs SERP Overview API
  slug: ahrefs-serp-overview-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The Traffic Sources API from Ahrefs — 8 operation(s) for traffic sources.
  name: Ahrefs Traffic Sources API
  slug: ahrefs-traffic-sources-api
- baseURL: https://api.ahrefs.com/v3
  baseurl_source: declared
  description: The User Agents API from Ahrefs — 10 operation(s) for user agents.
  name: Ahrefs User Agents API
  slug: ahrefs-user-agents-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Brand radar.
  name: Ahrefs Brand Radar API
  slug: ahrefs-brand-radar-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Fetch data from GSC Insights reports
  name: Ahrefs GSC Insights API
  slug: ahrefs-gsc-insights-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Fetch data from Keywords Explorer reports
  name: Ahrefs Keywords Explorer API
  slug: ahrefs-keywords-explorer-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Project management.
  name: Ahrefs Management API
  slug: ahrefs-management-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Free endpoints that don't require an Ahrefs subscription, or require a free/public APIv3 key
  name: Ahrefs Public API
  slug: ahrefs-public-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Rank tracker.
  name: Ahrefs Rank Tracker API
  slug: ahrefs-rank-tracker-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Site audit.
  name: Ahrefs Site Audit API
  slug: ahrefs-site-audit-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Fetch data from Site Explorer reports
  name: Ahrefs Site Explorer API
  slug: ahrefs-site-explorer-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Social Media Management.
  name: Ahrefs Social Media API
  slug: ahrefs-social-media-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Subscription information.
  name: Ahrefs Subscription Information API
  slug: ahrefs-subscription-information-api
- baseURL: https://api.ahrefs.com/mcp/mcp
  baseurl_source: declared
  description: Web_analytics.
  name: Ahrefs Web Analytics API
  slug: ahrefs-web-analytics-api
artifact_total: 63
collections:
- collection_type: open
  name: Batch Analysis
  slug: open-ahrefs-batch-analysis
- collection_type: open
  name: Brand Radar
  slug: open-ahrefs-brand-radar
- collection_type: open
  name: GSC Insights
  slug: open-ahrefs-gsc
- collection_type: open
  name: Keywords Explorer
  slug: open-ahrefs-keywords-explorer
- collection_type: open
  name: Management
  slug: open-ahrefs-management
- collection_type: open
  name: Public
  slug: open-ahrefs-public
- collection_type: open
  name: Rank Tracker
  slug: open-ahrefs-rank-tracker
- collection_type: open
  name: SERP Overview
  slug: open-ahrefs-serp-overview
- collection_type: open
  name: Site Audit
  slug: open-ahrefs-site-audit
- collection_type: open
  name: Site Explorer
  slug: open-ahrefs-site-explorer
- collection_type: open
  name: Social Media
  slug: open-ahrefs-social-media
- collection_type: open
  name: Subscription Information
  slug: open-ahrefs-subscription-info
- collection_type: open
  name: Web Analytics
  slug: open-ahrefs-web-analytics
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ahrefs-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ahrefs-api-v3-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://ahrefs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ahrefs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ahrefs.com/docs/api/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ahrefs.com/en/api/reference/site-explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ahrefs.com/docs/api/reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.ahrefs.com/en/
- group: company
  title: ''
  type: Blog
  url: https://ahrefs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ahrefs
- group: commercial
  title: ''
  type: Pricing
  url: https://ahrefs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ahrefs.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ahrefs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ahrefs.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ahrefs-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ahrefs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ahrefs-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ahrefs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ahrefs-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/ahrefs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ahrefs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ahrefs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ahrefs-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ahrefs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ahrefs.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ahrefs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ahrefs-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ahrefs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ahrefs.com/ahrefs-connect/docs/legacy-developers
- group: design
  title: ''
  type: Conventions
  url: conventions/ahrefs-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ahrefs-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/ahrefs-components.yml
created: '2026-08-12'
description: Ahrefs is a Singapore-based SEO and marketing intelligence platform built on its own web crawler and index, offering Site Explorer, Keywords Explorer, Site Audit, Rank Tracker, SERP Overview, Brand Radar, Web Analytics and Social Media Management. The Ahrefs API v3 exposes that data set as a REST API at https://api.ahrefs.com/v3 with 148 operations across 13 tools, documented by a single OpenAPI 3.2.0 specification plus one machine-readable spec per tool. Access is metered in API units with a 50-unit request floor, authenticated with a bearer API key, and additionally reachable through a hosted MCP server and the OAuth-based Ahrefs Connect partner program.
image: https://static.ahrefs.com/assets/img/og/ahrefs.png?v=2
layout: provider
mcp_servers:
- description: ''
  name: Ahrefs MCP Server
  slug: ahrefs-mcp-server
modified: '2026-08-12'
name: Ahrefs
nav: Providers
network: true
overview: 'Ahrefs publishes 42 APIs on the [APIs.io](https://apis.io/) network, including AI visibility API, Anonymous queries API, Backlinks profile API, and 39 more. Tagged areas include Company, SEO, Marketing, Search, and Analytics.


  Ahrefs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Ahrefs Plans Pricing
  plan_count: 6
  slug: ahrefs-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Ahrefs Rate Limits
  slug: ahrefs-rate-limits
scopes:
- name: Ahrefs Scopes
  scope_count: 2
  slug: ahrefs-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 62.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ahrefs/refs/heads/main/screenshots/ahrefs-2026-08-17T080541.png
security:
- kind: authentication
  name: Ahrefs Authentication
  slug: ahrefs-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Ahrefs Domain Security
  slug: ahrefs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ahrefs Trust Center
  slug: ahrefs-trust-center
  summary_line: trust center published
slug: ahrefs
tags:
- Company
- SEO
- Marketing
- Search
- Analytics
- Backlinks
- Keywords
- Web Analytics
- Rank Tracking
- Site Audit
- Brand Monitoring
- Social-Media
website: https://ahrefs.com/
---
