---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Articles API from NewsWhip — 1 operation(s) for articles.
  name: NewsWhip Articles API
  slug: newswhip-articles-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The ArticlesByHrefs API from NewsWhip — 1 operation(s) for articlesbyhrefs.
  name: NewsWhip ArticlesByHrefs API
  slug: newswhip-articlesbyhrefs-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Content API from NewsWhip — 3 operation(s) for content.
  name: NewsWhip Content API
  slug: newswhip-content-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The FbInfluencers API from NewsWhip — 1 operation(s) for fbinfluencers.
  name: NewsWhip FbInfluencers API
  slug: newswhip-fbinfluencers-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The FbPosts API from NewsWhip — 1 operation(s) for fbposts.
  name: NewsWhip FbPosts API
  slug: newswhip-fbposts-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Influencers API from NewsWhip — 2 operation(s) for influencers.
  name: NewsWhip Influencers API
  slug: newswhip-influencers-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Local API from NewsWhip — 1 operation(s) for local.
  name: NewsWhip Local API
  slug: newswhip-local-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Publisher API from NewsWhip — 1 operation(s) for publisher.
  name: NewsWhip Publisher API
  slug: newswhip-publisher-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Rankings API from NewsWhip — 3 operation(s) for rankings.
  name: NewsWhip Rankings API
  slug: newswhip-rankings-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Region API from NewsWhip — 1 operation(s) for region.
  name: NewsWhip Region API
  slug: newswhip-region-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Search API from NewsWhip — 1 operation(s) for search.
  name: NewsWhip Search API
  slug: newswhip-search-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Social API from NewsWhip — 1 operation(s) for social.
  name: NewsWhip Social API
  slug: newswhip-social-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Statistics API from NewsWhip — 1 operation(s) for statistics.
  name: NewsWhip Statistics API
  slug: newswhip-statistics-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The Stats API from NewsWhip — 1 operation(s) for stats.
  name: NewsWhip Stats API
  slug: newswhip-stats-api
- baseURL: https://api.newswhip.com/v1
  baseurl_source: declared
  description: The TwitterInfluencers API from NewsWhip — 1 operation(s) for twitterinfluencers.
  name: NewsWhip TwitterInfluencers API
  slug: newswhip-twitterinfluencers-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: quick-start-api-formerly-get-api Articles API
  slug: open-newswhip-articles-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles ArticlesByHrefs API
  slug: open-newswhip-articlesbyhrefs-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Content API
  slug: open-newswhip-content-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles FbInfluencers API
  slug: open-newswhip-fbinfluencers-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles FbPosts API
  slug: open-newswhip-fbposts-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Influencers API
  slug: open-newswhip-influencers-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Local API
  slug: open-newswhip-local-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Publisher API
  slug: open-newswhip-publisher-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Rankings API
  slug: open-newswhip-rankings-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Region API
  slug: open-newswhip-region-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Search API
  slug: open-newswhip-search-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Social API
  slug: open-newswhip-social-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Statistics API
  slug: open-newswhip-statistics-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles Stats API
  slug: open-newswhip-stats-api
- collection_type: open
  name: quick-start-api-formerly-get-api Articles TwitterInfluencers API
  slug: open-newswhip-twitterinfluencers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/newswhip-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://newswhip.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.newswhip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.newswhip.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.newswhip.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.newswhip.com/docs/first-steps
- group: company
  title: ''
  type: Blog
  url: https://www.newswhip.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://newswhipsupport.sproutsocial.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NewsWhip
- group: start
  title: ''
  type: SignUp
  url: http://go.newswhip.com/API-Access-Request.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.newswhip.com/newswhip-terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.newswhip.com/newswhip-privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/newswhip-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newswhip-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.newswhip.com/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/newswhip-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newswhip-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/newswhip-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newswhip-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/newswhip-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/newswhip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newswhip-rate-limits.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/newswhip-tool-crosswalk.yml
created: '2026-07-17'
description: NewsWhip is a media intelligence and predictive analytics company whose API gives programmatic access to the world's largest human-engagement database — real-time and predicted social engagement metrics, aggregated statistics, publisher and regional rankings, and top influencers for hundreds of millions of articles and social posts it has tracked across the web, Facebook and Twitter since 2014. Developers query trending and predicted content, look up engagement for specific URLs, and surface the pages and accounts driving a story via a JSON HTTPS API documented on the NewsWhip Developer Hub. Added to the API Evangelist network as a portfolio company of 500 Global and enriched by the API Evangelist pipeline from NewsWhip's public developer surface.
image: https://www.newswhip.com/wp-content/uploads/2022/05/API-on-phone.png
layout: provider
mcp_servers:
- description: ''
  name: NewsWhip MCP Server
  slug: newswhip-mcp-server
modified: '2026-08-13'
name: NewsWhip
nav: Providers
network: true
overview: 'NewsWhip publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Articles API, ArticlesByHrefs API, Content API, and 12 more. Tagged areas include Company, Media Intelligence, Social Media Analytics, News, and Content Analytics.


  NewsWhip''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 17 more developer resources.'
plans:
- name: Newswhip Plans Pricing
  plan_count: 3
  slug: newswhip-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Newswhip Rate Limits
  slug: newswhip-rate-limits
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 43.4
  previous_composite: 45.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newswhip/refs/heads/main/screenshots/newswhip-2026-08-07T185140.png
security:
- kind: authentication
  name: Newswhip Authentication
  slug: newswhip-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Newswhip Domain Security
  slug: newswhip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newswhip
tags:
- Company
- Media Intelligence
- Social Media Analytics
- News
- Content Analytics
- Engagement Data
- Predictive Analytics
- Media Monitoring
website: https://newswhip.com
---
