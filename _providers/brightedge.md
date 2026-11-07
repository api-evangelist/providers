---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 72
  human_in_the_loop: 2
  name: Brightedge Agentic Access
  operation_count: 248
  slug: brightedge-agentic-access
  summary_line: 248 operations · 72 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: BrightEdge's hosted, remote Model Context Protocol server. An MCP client POSTs to https://mcp2.brightedge.com/mcp (or the SSE endpoint https://mcp2-sse.brightedge.com/sse) and, after an OAuth 2.0 auth
  name: BrightEdge MCP Server
  slug: brightedge-mcp-server
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Auth API from BrightEdge — 3 operation(s) for auth.
  name: BrightEdge Auth API
  slug: brightedge-auth-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Authorize API from BrightEdge — 2 operation(s) for authorize.
  name: BrightEdge Authorize API
  slug: brightedge-authorize-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Feedback API from BrightEdge — 4 operation(s) for feedback.
  name: BrightEdge Feedback API
  slug: brightedge-feedback-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Oauth API from BrightEdge — 3 operation(s) for oauth.
  name: BrightEdge OAuth API
  slug: brightedge-oauth-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Ping API from BrightEdge — 1 operation(s) for ping.
  name: BrightEdge Ping API
  slug: brightedge-ping-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Saml API from BrightEdge — 2 operation(s) for saml.
  name: BrightEdge SAML API
  slug: brightedge-saml-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Sso API from BrightEdge — 2 operation(s) for sso.
  name: BrightEdge SSO API
  slug: brightedge-sso-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The Token API from BrightEdge — 2 operation(s) for token.
  name: BrightEdge Token API
  slug: brightedge-token-api
- baseURL: https://api.brightedge.com
  baseurl_source: declared
  description: The .well Known API from BrightEdge — 7 operation(s) for .well known.
  name: BrightEdge .well Known API
  slug: brightedge-well-known-api
artifact_total: 69
collections:
- collection_type: open
  name: BrightEdge Platform accounts API
  slug: open-brightedge-accounts-api
- collection_type: open
  name: BrightEdge Platform accounts ai_catalyst API
  slug: open-brightedge-ai-catalyst-api
- collection_type: open
  name: BrightEdge Platform accounts autopilot API
  slug: open-brightedge-autopilot-api
- collection_type: open
  name: BrightEdge Platform accounts backlinks API
  slug: open-brightedge-backlinks-api
- collection_type: open
  name: BrightEdge Platform accounts be_local API
  slug: open-brightedge-be-local-api
- collection_type: open
  name: BrightEdge Platform accounts budd API
  slug: open-brightedge-budd-api
- collection_type: open
  name: BrightEdge Platform accounts bulk_export API
  slug: open-brightedge-bulk-export-api
- collection_type: open
  name: BrightEdge Platform accounts chrome_extension API
  slug: open-brightedge-chrome-extension-api
- collection_type: open
  name: BrightEdge Platform accounts Chrome Extension Keywords API
  slug: open-brightedge-chrome-extension-keywords-api
- collection_type: open
  name: BrightEdge Platform accounts Chrome Extension Overview API
  slug: open-brightedge-chrome-extension-overview-api
- collection_type: open
  name: BrightEdge Platform accounts chromeextension API
  slug: open-brightedge-chromeextension-api
- collection_type: open
  name: BrightEdge Platform accounts competitors API
  slug: open-brightedge-competitors-api
- collection_type: open
  name: BrightEdge Platform accounts core API
  slug: open-brightedge-core-api
- collection_type: open
  name: BrightEdge Platform accounts datacube_searchengines API
  slug: open-brightedge-datacube-searchengines-api
- collection_type: open
  name: BrightEdge Platform accounts dataset API
  slug: open-brightedge-dataset-api
- collection_type: open
  name: BrightEdge Platform accounts domains API
  slug: open-brightedge-domains-api
- collection_type: open
  name: BrightEdge Platform accounts instant API
  slug: open-brightedge-instant-api
- collection_type: open
  name: BrightEdge Platform accounts keywordgroups API
  slug: open-brightedge-keywordgroups-api
- collection_type: open
  name: BrightEdge Platform accounts keywords API
  slug: open-brightedge-keywords-api
- collection_type: open
  name: BrightEdge Platform accounts Latest5 API
  slug: open-brightedge-latest5-api
- collection_type: open
  name: BrightEdge Platform accounts legacy API
  slug: open-brightedge-legacy-api
- collection_type: open
  name: BrightEdge Platform accounts marketinsights API
  slug: open-brightedge-marketinsights-api
- collection_type: open
  name: BrightEdge Platform accounts marketo API
  slug: open-brightedge-marketo-api
- collection_type: open
  name: BrightEdge Platform accounts organizations API
  slug: open-brightedge-organizations-api
- collection_type: open
  name: BrightEdge Platform accounts paa per keyword API
  slug: open-brightedge-paa-per-keyword-api
- collection_type: open
  name: BrightEdge Platform accounts page cache API
  slug: open-brightedge-page-cache-api
- collection_type: open
  name: BrightEdge Platform accounts page crawl API
  slug: open-brightedge-page-crawl-api
- collection_type: open
  name: BrightEdge Platform accounts Pages API
  slug: open-brightedge-pages-api
- collection_type: open
  name: BrightEdge Platform accounts people_also_ask API
  slug: open-brightedge-people-also-ask-api
- collection_type: open
  name: BrightEdge Platform accounts ping API
  slug: open-brightedge-ping-api
- collection_type: open
  name: BrightEdge Platform accounts product_grid API
  slug: open-brightedge-product-grid-api
- collection_type: open
  name: BrightEdge Platform accounts qa API
  slug: open-brightedge-qa-api
- collection_type: open
  name: BrightEdge Platform accounts query API
  slug: open-brightedge-query-api
- collection_type: open
  name: BrightEdge Platform accounts recommendations API
  slug: open-brightedge-recommendations-api
- collection_type: open
  name: BrightEdge Platform accounts searchengines API
  slug: open-brightedge-searchengines-api
- collection_type: open
  name: BrightEdge Platform accounts Serp Features API
  slug: open-brightedge-serp-features-api
- collection_type: open
  name: BrightEdge Platform accounts time API
  slug: open-brightedge-time-api
- collection_type: open
  name: BrightEdge Platform accounts top keywords for a domain API
  slug: open-brightedge-top-keywords-for-a-domain-api
- collection_type: open
  name: BrightEdge Platform accounts top keywords per page API
  slug: open-brightedge-top-keywords-per-page-api
- collection_type: open
  name: BrightEdge Platform accounts top pages API
  slug: open-brightedge-top-pages-api
- collection_type: open
  name: BrightEdge Platform accounts user_settings API
  slug: open-brightedge-user-settings-api
- collection_type: open
  name: BrightEdge Platform accounts users API
  slug: open-brightedge-users-api
- collection_type: open
  name: BrightEdge Platform accounts web_vitals API
  slug: open-brightedge-web-vitals-api
- collection_type: open
  name: BrightEdge Platform accounts webhook API
  slug: open-brightedge-webhook-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.brightedge.com/rss.xml
- group: other
  href: https://artifacts.apis.io/brightedge/capabilities/brightedge-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brightedge-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/brightedge/skills/brightedge-bulk-export.md
  title: ''
  type: AgentSkill
  url: skills/brightedge-bulk-export.md
- group: agent
  href: https://artifacts.apis.io/brightedge/mcp/brightedge-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brightedge-mcp.yml
- group: other
  href: https://artifacts.apis.io/brightedge/overlays/brightedge-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brightedge-platform-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/brightedge/security/brightedge-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/brightedge-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/brightedge/security/brightedge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightedge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.brightedge.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.brightedge.com/portal
- group: docs
  title: ''
  type: Documentation
  url: https://api.brightedge.com/portal
- group: docs
  title: ''
  type: APIReference
  url: https://api.brightedge.com/portal
- group: start
  title: ''
  type: GettingStarted
  url: https://www.brightedge.com/brightedge-mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://www.brightedge.com/brightedge-mcp
- group: start
  title: ''
  type: SignUp
  url: https://www.brightedge.com/secure/login
- group: start
  title: ''
  type: Login
  url: https://www.brightedge.com/secure/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightedge.com/products/product-pricing
- group: operate
  title: ''
  type: Support
  url: https://support.brightedge.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.brightedge.com/
- group: company
  title: ''
  type: Blog
  url: https://www.brightedge.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightedge.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightedge.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightedge-seo
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.brightedge.com/resources/product-releases
- group: auth
  title: ''
  type: Compliance
  url: https://www.brightedge.com/trust
- group: agent
  href: https://artifacts.apis.io/brightedge/llms/brightedge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brightedge-llms.txt
- group: agent
  href: https://artifacts.apis.io/brightedge/llms/brightedge-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brightedge-api-llms.txt
- group: build
  href: https://artifacts.apis.io/brightedge/mcp/brightedge-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/brightedge-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/brightedge/well-known/brightedge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brightedge-well-known.yml
- group: auth
  href: https://artifacts.apis.io/brightedge/authentication/brightedge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brightedge-authentication.yml
- group: auth
  href: https://artifacts.apis.io/brightedge/scopes/brightedge-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/brightedge-scopes.yml
- group: design
  href: https://artifacts.apis.io/brightedge/conventions/brightedge-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brightedge-conventions.yml
- group: design
  href: https://artifacts.apis.io/brightedge/errors/brightedge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brightedge-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brightedge/lifecycle/brightedge-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brightedge-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/brightedge/data-model/brightedge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brightedge-data-model.yml
- group: design
  href: https://artifacts.apis.io/brightedge/conformance/brightedge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brightedge-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brightedge/agentic-access/brightedge-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brightedge-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/brightedge/packages/brightedge-packages.yml
  title: ''
  type: Packages
  url: packages/brightedge-packages.yml
- group: commercial
  href: https://artifacts.apis.io/brightedge/plans/brightedge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brightedge-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/brightedge/rate-limits/brightedge-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brightedge-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/brightedge/changelog/brightedge-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brightedge-changelog.yml
- group: agent
  href: https://artifacts.apis.io/brightedge/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/brightedge/skills/brightedge-connect-mcp.md
  title: ''
  type: AgentSkill
  url: skills/brightedge-connect-mcp.md
- group: agent
  href: https://artifacts.apis.io/brightedge/skills/brightedge-pull-keyword-rankings.md
  title: ''
  type: AgentSkill
  url: skills/brightedge-pull-keyword-rankings.md
- group: agent
  href: https://artifacts.apis.io/brightedge/skills/brightedge-query-datacube.md
  title: ''
  type: AgentSkill
  url: skills/brightedge-query-datacube.md
created: '2026-07-17'
description: BrightEdge is an enterprise SEO and content performance platform, founded in 2007 and headquartered in Silicon Valley, used by thousands of brands and a majority of the Fortune 100. Its products include the DataCube keyword and content data repository, ContentIQ site auditing, Autopilot, Copilot, and the DataMind AI engine plus AI Catalyst for generative-search visibility. The BrightEdge Platform API (v5.0) is a REST API published at api.brightedge.com that exposes accounts, keywords, keyword groups, competitors, domains, pages, backlinks, the DataCube dataset, recommendations, People-Also-Ask, SERP features, Core Web Vitals, bulk export, and user/organization management, so teams can integrate BrightEdge search and content intelligence into their own reporting, analytics, and data-warehouse workflows.
finops:
- has_sources: true
  method: derived
  name: Brightedge Finops
  primary_unit: ''
  service_category: ''
  slug: brightedge-finops
  template: true
image: https://www.brightedge.com/themes/custom/brightedge/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp2.brightedge.com over HTTP.
  name: BrightEdge MCP Server
  slug: brightedge
- description: ''
  name: BrightEdge MCP product page
  slug: brightedge-mcp-product-page
modified: '2026-10-06'
name: BrightEdge
nav: Providers
network: true
overview: 'BrightEdge publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Authorize API, Feedback API, and 7 more. Tagged areas include Company, SEO, Search, Content, and Marketing.


  The BrightEdge catalog on APIs.io includes 1 Spectral governance ruleset.


  BrightEdge''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 37 more developer resources.'
plans:
- name: Brightedge Plans Pricing
  plan_count: 0
  slug: brightedge-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Brightedge Rate Limits
  slug: brightedge-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: BrightEdge API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 2
  slug: brightedge-rules
scopes:
- name: Brightedge Scopes
  scope_count: 3
  slug: brightedge-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 37.2
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 24.3
      total: 37
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/brightedge/brightedge-2026-07-25T203837.png
security:
- kind: authentication
  name: Brightedge Authentication
  slug: brightedge-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Brightedge Domain Security
  slug: brightedge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brightedge Trust Center
  slug: brightedge-trust-center
  summary_line: SOC 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO/IEC 42001:2023, GDPR, CCPA, EU-U.S. Data Privacy Framework
skill_count: 4
skills:
- name: Create and retrieve a bulk export job
  slug: brightedge-bulk-export
- name: Connect an agent to the BrightEdge MCP server
  slug: brightedge-connect-mcp
- name: Pull keyword rankings for an account
  slug: brightedge-pull-keyword-rankings
- name: Query the DataCube for top pages and keywords
  slug: brightedge-query-datacube
slug: brightedge
tags:
- Company
- SEO
- Search
- Content
- Marketing
- Analytics
- Keywords
- Enterprise
- AI Search
website: http://www.brightedge.com/
---
