---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Search Console Agentic Access
  operation_count: 10
  slug: google-search-console-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 5
apis:
- baseURL: https://searchconsole.googleapis.com
  baseurl_source: declared
  description: Query search traffic data for your site. Retrieve impressions, clicks, click-through rate, and average position grouped by dimensions such as query, page, country, device, search type, and date.
  name: Google Search Console Search Analytics API
  slug: google-search-console-search-analytics-api
- baseURL: https://searchconsole.googleapis.com
  baseurl_source: declared
  description: Submit and manage sitemaps and sitemap indexes for your site. List submitted sitemaps, check their processing status, submit new sitemaps, and delete previously submitted sitemaps.
  name: Google Search Console Sitemaps API
  slug: google-search-console-sitemaps-api
- baseURL: https://searchconsole.googleapis.com
  baseurl_source: declared
  description: Manage site-level access and verification. List verified sites, get details about a specific site, add new sites, and remove sites from your Search Console account.
  name: Google Search Console Sites API
  slug: google-search-console-sites-api
- baseURL: https://searchconsole.googleapis.com
  baseurl_source: declared
  description: Inspect individual URLs to retrieve detailed indexing, crawling, and serving information. Check whether a URL is indexed, view crawl details, mobile usability status, and rich results eligibility.
  name: Google Search Console URL Inspection API
  slug: google-search-console-url-inspection-api
- baseURL: https://searchconsole.googleapis.com
  baseurl_source: declared
  description: The urlNotifications API from Google Search Console — 2 operation(s) for urlnotifications.
  name: Google Search Console URL Notifications API
  slug: google-search-console-urlnotifications-api
- baseURL: https://searchconsole.googleapis.com
  baseurl_source: declared
  description: The urlTestingTools API from Google Search Console — 1 operation(s) for urltestingtools.
  name: Google Search Console URL Testing Tools API
  slug: google-search-console-urltestingtools-api
artifact_total: 111
collections:
- collection_type: postman
  name: Google Search Console Search Analytics API
  slug: postman-google-search-console-search-analytics-api
- collection_type: postman
  name: Google Search Console Search Analytics Sitemaps API
  slug: postman-google-search-console-sitemaps-api
- collection_type: postman
  name: Google Search Console Search Analytics Sites API
  slug: postman-google-search-console-sites-api
- collection_type: postman
  name: Google Search Console Search Analytics URL Inspection API
  slug: postman-google-search-console-url-inspection-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Search Console API
  slug: open-google-search-console-api
- collection_type: open
  name: Google Web Search Indexing API
  slug: open-google-search-console-indexing-api
- collection_type: open
  name: Google Search Console Search Analytics API
  slug: open-google-search-console-search-analytics-api
- collection_type: open
  name: Google Search Console Search Analytics Sitemaps API
  slug: open-google-search-console-sitemaps-api
- collection_type: open
  name: Google Search Console Search Analytics Sites API
  slug: open-google-search-console-sites-api
- collection_type: open
  name: Google Search Console Search Analytics URL Inspection API
  slug: open-google-search-console-url-inspection-api
- collection_type: open
  name: Google Search Console URL Testing Tools API
  slug: open-google-search-console-url-testing-tools-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/google-search-console-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-search-console-url-testing-tools-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-search-console-indexing-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/google-search-console-packages.yml
- group: build
  title: First-party client libraries with published versions and release dates
  type: SDKs
  url: packages/google-search-console-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-search-console-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-search-console-security.txt
- group: auth
  title: ''
  type: Security
  url: security/google-search-console-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-search-console-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-search-console-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-search-console-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-search-console-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-search-console-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-search-console-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-search-console-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-search-console-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-search-console-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-search-console-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-search-console-finops.yml
- group: design
  title: JSON Schema Spectral Rules
  type: SpectralRules
  url: rules/google-search-console-jsonschema-spectral-rules.yml
- group: operate
  title: Google Search Status Dashboard
  type: StatusPage
  url: https://status.search.google.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/webmaster-tools
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/webmaster-tools/v1/api_reference_index
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/webmaster-tools/v1/quickstart/quickstart-python
- group: commercial
  title: Usage limits (the API is free; quotas are the constraint)
  type: Pricing
  url: https://developers.google.com/webmaster-tools/limits
- group: start
  title: ''
  type: SignUp
  url: https://search.google.com/search-console/welcome
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-search-console/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-search-console-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-search-console-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-search-console-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-search-console-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-search-console-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://developers.googleblog.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: auth
  title: OAuth 2.0 Scopes
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2/scopes
- group: build
  title: API Client Libraries
  type: SDKs
  url: https://developers.google.com/api-client-library
- group: company
  title: Google Search Central Blog
  type: Blog
  url: https://developers.google.com/search/updates
- group: operate
  title: Search Console Help
  type: Support
  url: https://support.google.com/webmasters/
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-search-console-spectral-rules.yml
created: '2024-01-01'
description: 'Google Search Console gives site owners programmatic access to how their site appears in Google Search. Three separately versioned Google APIs make up the surface: the Search Console API for search analytics, sitemaps, site management and URL inspection; the URL Testing Tools API for the mobile-friendly test; and the Web Search Indexing API for telling Google that a page was published, updated or removed. All three are free of charge, authenticate with Google OAuth 2.0 against accounts.google.com, are authorized per verified property rather than per Cloud project, and are described by Google Discovery documents rather than a published OpenAPI.'
examples:
- key_count: 2
  name: Google Search Console Detected Items Example
  slug: google-search-console-detected-items-example
- key_count: 3
  name: Google Search Console Dimension Filter Example
  slug: google-search-console-dimension-filter-example
- key_count: 2
  name: Google Search Console Dimension Filter Group Example
  slug: google-search-console-dimension-filter-group-example
- key_count: 1
  name: Google Search Console Error Example
  slug: google-search-console-error-example
- key_count: 11
  name: Google Search Console Index Status Inspection Result Example
  slug: google-search-console-index-status-inspection-result-example
- key_count: 3
  name: Google Search Console Inspect Url Index Request Example
  slug: google-search-console-inspect-url-index-request-example
- key_count: 0
  name: Google Search Console Inspect Url Index Response Example
  slug: google-search-console-inspect-url-index-response-example
- key_count: 2
  name: Google Search Console Item Example
  slug: google-search-console-item-example
- key_count: 2
  name: Google Search Console Mobile Usability Inspection Result Example
  slug: google-search-console-mobile-usability-inspection-result-example
- key_count: 3
  name: Google Search Console Mobile Usability Issue Example
  slug: google-search-console-mobile-usability-issue-example
- key_count: 2
  name: Google Search Console Rich Results Inspection Result Example
  slug: google-search-console-rich-results-inspection-result-example
- key_count: 3
  name: Google Search Console Rich Results Issue Example
  slug: google-search-console-rich-results-issue-example
- key_count: 9
  name: Google Search Console Search Analytics Query Request Example
  slug: google-search-console-search-analytics-query-request-example
- key_count: 2
  name: Google Search Console Search Analytics Query Response Example
  slug: google-search-console-search-analytics-query-response-example
- key_count: 5
  name: Google Search Console Search Analytics Row Example
  slug: google-search-console-search-analytics-row-example
- key_count: 1
  name: Google Search Console Sitemaps List Response Example
  slug: google-search-console-sitemaps-list-response-example
- key_count: 1
  name: Google Search Console Sites List Response Example
  slug: google-search-console-sites-list-response-example
- key_count: 1
  name: Google Search Console Url Inspection Result Example
  slug: google-search-console-url-inspection-result-example
- key_count: 2
  name: Google Search Console Wmx Site Example
  slug: google-search-console-wmx-site-example
- key_count: 3
  name: Google Search Console Wmx Sitemap Content Example
  slug: google-search-console-wmx-sitemap-content-example
- key_count: 9
  name: Google Search Console Wmx Sitemap Example
  slug: google-search-console-wmx-sitemap-example
features:
- description: Analyze search traffic data including impressions, clicks, CTR, and average position by query, page, country, device, and date.
  name: Search Analytics
- description: Submit, monitor, and manage XML sitemaps and sitemap indexes to optimize crawling and indexing.
  name: Sitemap Management
- description: Inspect individual URLs for indexing status, crawl details, mobile usability, and rich results eligibility.
  name: URL Inspection
- description: Monitor which pages are indexed, identify indexing errors, and track coverage status across your site.
  name: Index Coverage
- description: Test pages for mobile-friendliness and identify mobile usability issues.
  name: Mobile Usability Testing
- description: Validate structured data markup and check rich results eligibility for individual URLs.
  name: Rich Results Validation
- description: Manage site ownership verification and access permissions for Search Console properties.
  name: Site Verification
finops:
- name: Google Search Console Finops
  service_category: SEO / Search Tools
  slug: google-search-console-finops
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Combine Search Console data with Google Analytics for comprehensive website performance analysis.
  name: Google Analytics
- description: Connect search performance data with advertising campaigns to optimize paid and organic strategy together.
  name: Google Ads
- description: Deploy Search Console API integrations on Google Cloud Platform infrastructure.
  name: Google Cloud
- description: Export Search Console data to BigQuery for advanced analytics and cross-platform reporting.
  name: BigQuery
- description: Visualize Search Console metrics in dashboards for stakeholder reporting and trend analysis.
  name: Data Studio / Looker
json_schemas:
- name: DetectedItems
  property_count: 2
  slug: google-search-console-detected-items
- name: DimensionFilterGroup
  property_count: 2
  slug: google-search-console-dimension-filter-group
- name: DimensionFilter
  property_count: 3
  slug: google-search-console-dimension-filter
- name: Error
  property_count: 1
  slug: google-search-console-error
- name: IndexStatusInspectionResult
  property_count: 11
  slug: google-search-console-index-status-inspection-result
- name: InspectUrlIndexRequest
  property_count: 3
  slug: google-search-console-inspect-url-index-request
- name: InspectUrlIndexResponse
  property_count: 0
  slug: google-search-console-inspect-url-index-response
- name: Item
  property_count: 2
  slug: google-search-console-item
- name: MobileUsabilityInspectionResult
  property_count: 2
  slug: google-search-console-mobile-usability-inspection-result
- name: MobileUsabilityIssue
  property_count: 3
  slug: google-search-console-mobile-usability-issue
- name: Google Search Console Search Analytics Query
  property_count: 0
  slug: google-search-console-query
- name: RichResultsInspectionResult
  property_count: 2
  slug: google-search-console-rich-results-inspection-result
- name: RichResultsIssue
  property_count: 3
  slug: google-search-console-rich-results-issue
- name: SearchAnalyticsQueryRequest
  property_count: 9
  slug: google-search-console-search-analytics-query-request
- name: SearchAnalyticsQueryResponse
  property_count: 2
  slug: google-search-console-search-analytics-query-response
- name: SearchAnalyticsRow
  property_count: 5
  slug: google-search-console-search-analytics-row
- name: SitemapsListResponse
  property_count: 1
  slug: google-search-console-sitemaps-list-response
- name: SitesListResponse
  property_count: 1
  slug: google-search-console-sites-list-response
- name: UrlInspectionResult
  property_count: 1
  slug: google-search-console-url-inspection-result
- name: WmxSite
  property_count: 2
  slug: google-search-console-wmx-site
- name: WmxSitemapContent
  property_count: 3
  slug: google-search-console-wmx-sitemap-content
- name: WmxSitemap
  property_count: 9
  slug: google-search-console-wmx-sitemap
json_structures:
- name: Google Search Console Detected Items Structure
  property_count: 2
  slug: google-search-console-detected-items-structure
- name: Google Search Console Dimension Filter Group Structure
  property_count: 2
  slug: google-search-console-dimension-filter-group-structure
- name: Google Search Console Dimension Filter Structure
  property_count: 3
  slug: google-search-console-dimension-filter-structure
- name: Google Search Console Error Structure
  property_count: 1
  slug: google-search-console-error-structure
- name: Google Search Console Index Status Inspection Result Structure
  property_count: 11
  slug: google-search-console-index-status-inspection-result-structure
- name: Google Search Console Inspect Url Index Request Structure
  property_count: 3
  slug: google-search-console-inspect-url-index-request-structure
- name: Google Search Console Inspect Url Index Response Structure
  property_count: 0
  slug: google-search-console-inspect-url-index-response-structure
- name: Google Search Console Item Structure
  property_count: 2
  slug: google-search-console-item-structure
- name: Google Search Console Mobile Usability Inspection Result Structure
  property_count: 2
  slug: google-search-console-mobile-usability-inspection-result-structure
- name: Google Search Console Mobile Usability Issue Structure
  property_count: 3
  slug: google-search-console-mobile-usability-issue-structure
- name: Google Search Console Rich Results Inspection Result Structure
  property_count: 2
  slug: google-search-console-rich-results-inspection-result-structure
- name: Google Search Console Rich Results Issue Structure
  property_count: 3
  slug: google-search-console-rich-results-issue-structure
- name: Google Search Console Search Analytics Query Request Structure
  property_count: 9
  slug: google-search-console-search-analytics-query-request-structure
- name: Google Search Console Search Analytics Query Response Structure
  property_count: 2
  slug: google-search-console-search-analytics-query-response-structure
- name: Google Search Console Search Analytics Row Structure
  property_count: 5
  slug: google-search-console-search-analytics-row-structure
- name: Google Search Console Sitemaps List Response Structure
  property_count: 1
  slug: google-search-console-sitemaps-list-response-structure
- name: Google Search Console Sites List Response Structure
  property_count: 1
  slug: google-search-console-sites-list-response-structure
- name: Google Search Console Url Inspection Result Structure
  property_count: 1
  slug: google-search-console-url-inspection-result-structure
- name: Google Search Console Wmx Site Structure
  property_count: 2
  slug: google-search-console-wmx-site-structure
- name: Google Search Console Wmx Sitemap Content Structure
  property_count: 3
  slug: google-search-console-wmx-sitemap-content-structure
- name: Google Search Console Wmx Sitemap Structure
  property_count: 9
  slug: google-search-console-wmx-sitemap-structure
jsonld:
- class_count: 0
  name: Google Search Console Context
  property_count: 0
  slug: google-search-console-context
layout: provider
mcp_servers:
- description: ''
  name: Google Search Console MCP Server
  slug: google-search-console-mcp-server
modified: '2026-08-13'
name: Google Search Console
nav: Providers
network: true
overview: 'Google Search Console publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Search Analytics API, Sitemaps API, Sites API, and 3 more. Tagged areas include Analytics, Google, Indexing, Search, and Search Analytics.


  The Google Search Console catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Search Console''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 39 more developer resources.'
plans:
- name: Google Search Console Plans Pricing
  plan_count: 1
  slug: google-search-console-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 11
  name: Google Search Console Rate Limits
  slug: google-search-console-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Search Console API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-search-console-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Search Console API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: google-search-console-spectral-rules
scopes:
- name: Google Search Console Scopes
  scope_count: 3
  slug: google-search-console-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 31
    catalog_gap: 36.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 69.7
    developer_ergonomics: 79.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-search-console/refs/heads/main/screenshots/google-search-console-2026-06-20T182231.png
security:
- kind: authentication
  name: Google Search Console Authentication
  slug: google-search-console-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Search Console Domain Security
  slug: google-search-console-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Search Console Vulnerability Disclosure
  slug: google-search-console-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-search-console
tags:
- Analytics
- Google
- Indexing
- Search
- Search Analytics
- SEO
- Sitemap
- URL Inspection
- Webmaster Tools
use_cases:
- description: Track organic search performance metrics to identify trends, measure optimization impact, and report on search visibility.
  name: SEO Performance Monitoring
- description: Identify and resolve indexing issues, crawl errors, and mobile usability problems affecting search performance.
  name: Technical SEO Auditing
- description: Analyze which queries drive traffic to specific pages and optimize content to improve rankings and click-through rates.
  name: Content Optimization
- description: Programmatically submit sitemaps when content is published or updated to accelerate indexing.
  name: Automated Sitemap Submission
- description: Monitor and manage search performance across multiple websites from a single integration.
  name: Multi-Site Management
website: https://developers.google.com/
---
