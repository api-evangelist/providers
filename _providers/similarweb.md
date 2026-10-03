---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.0
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Similarweb Agentic Access
  operation_count: 27
  slug: similarweb-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 2
apis:
- description: The SimilarWeb Batch API is optimized for large-scale bulk data extraction, supporting jobs of up to one million domains per request. It delivers data asynchronously to cloud storage destinations incl
  name: SimilarWeb Batch API
  slug: similarweb-batch-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Account credits, capabilities, and usage information
  name: SimilarWeb Account API
  phrasing_intents:
  - id: getCredits
    intent: Check remaining data credits
    question: How many data credits do I have left on my Similarweb account?
  - id: checkCapabilities
    intent: Check what my subscription covers for a site
    question: What data does my subscription let me pull for a given website?
  phrasing_ops: 2
  slug: similarweb-account-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Mobile app downloads, active users, sessions, and demographics
  name: SimilarWeb App Intelligence API
  phrasing_intents:
  - id: getAppDownloadsAndroid
    intent: Get download estimates for an Android app
    question: How many downloads does an Android app get on Google Play each month?
  - id: getAppDownloadsIos
    intent: Get download estimates for an iOS app
    question: How many App Store downloads does an iPhone app get?
  phrasing_ops: 2
  slug: similarweb-app-intelligence-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Batch API credit management
  name: SimilarWeb Credits API
  phrasing_intents:
  - id: getBatchCredits
    intent: Check remaining data credits
    question: How many data credits remain on my account?
  phrasing_ops: 1
  slug: similarweb-credits-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Geographic distribution of website traffic
  name: SimilarWeb Geography API
  phrasing_intents:
  - id: getGeographyDesktop
    intent: See a website's desktop traffic by country
    question: Which countries send the most desktop traffic to a website?
  phrasing_ops: 1
  slug: similarweb-geography-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Manage cloud storage integrations (S3, GCS, Snowflake)
  name: SimilarWeb Integrations API
  phrasing_intents:
  - id: createS3Integration
    intent: Connect an Amazon S3 bucket for report delivery
    question: How do I get batch reports delivered straight into my S3 bucket?
  - id: createGcsIntegration
    intent: Connect a Google Cloud Storage bucket
    question: How do I deliver batch reports to a Google Cloud Storage bucket?
  - id: getAllIntegrations
    intent: List configured cloud storage integrations
    question: Which cloud storage destinations are already set up on my account?
  phrasing_ops: 3
  slug: similarweb-integrations-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Keyword analytics including organic and paid keyword data
  name: SimilarWeb Keywords API
  phrasing_intents:
  - id: getWebsiteKeywords
    intent: Get the keywords driving traffic to a website
    question: Which search keywords send the most traffic to a competitor's site?
  phrasing_ops: 1
  slug: similarweb-keywords-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Lead enrichment combining firmographics and web analytics
  name: SimilarWeb Lead Enrichment API
  phrasing_intents:
  - id: getLeadEnrichment
    intent: Enrich a company domain with firmographics and traffic
    question: What's the employee range, revenue and headquarters for a company's domain?
  phrasing_ops: 1
  slug: similarweb-lead-enrichment-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Global, country, and industry rank data
  name: SimilarWeb Rankings API
  phrasing_intents:
  - id: getGlobalRank
    intent: Get a website's global rank
    question: Where does a website rank globally across desktop and mobile?
  - id: getRankTrackingCampaignOverview
    intent: Review a rank tracking campaign's performance
    question: How is my rank tracking campaign's average position trending?
  phrasing_ops: 2
  slug: similarweb-rankings-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Submit, track, and retrieve bulk data report requests
  name: SimilarWeb Reports API
  phrasing_intents:
  - id: requestReport
    intent: Submit a batch data report request
    question: How do I order a bulk data extract delivered to Snowflake or S3?
  - id: getRequestStatus
    intent: Check the status of a batch report
    question: Is my submitted batch report finished yet?
  - id: validateRequest
    intent: Estimate a batch report's credit cost
    question: How many credits will a batch report cost before I submit it?
  - id: getReportHistory
    intent: List past batch report requests
    question: What batch reports have we requested in the past?
  - id: retryRequest
    intent: Retry a failed batch report
    question: How do I rerun a batch report that failed?
  - id: describeTables
    intent: Describe the tables available for batch reports
    question: Which tables can I query in a batch report?
  phrasing_ops: 6
  slug: similarweb-reports-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Similar website discovery
  name: SimilarWeb Similar Sites API
  phrasing_intents:
  - id: getSimilarSites
    intent: Find websites similar to a domain
    question: What websites are most similar to a given domain?
  phrasing_ops: 1
  slug: similarweb-similar-sites-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Website traffic visits, bounce rate, pages per visit, visit duration
  name: SimilarWeb Traffic and Engagement API
  phrasing_intents:
  - id: getVisitsDesktop
    intent: Get a website's desktop visits over time
    question: How many desktop visits does a website get each month?
  - id: getBounceRateDesktop
    intent: Get a website's desktop bounce rate
    question: What's the desktop bounce rate for a website?
  phrasing_ops: 2
  slug: similarweb-traffic-and-engagement-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Marketing channel traffic breakdown including organic, paid, referral, social, and display
  name: SimilarWeb Traffic Sources API
  phrasing_intents:
  - id: getTrafficSourcesOverview
    intent: Break down a site's desktop visits by channel
    question: 'Where does a website''s desktop traffic come from: search, social, direct or referrals?'
  phrasing_ops: 1
  slug: similarweb-traffic-sources-api
- baseURL: https://api.similarweb.com
  baseurl_source: declared
  description: Webhook subscription management for data-ready notifications
  name: SimilarWeb Webhooks API
  phrasing_intents:
  - id: subscribeWebhook
    intent: Subscribe a URL to webhook events
    question: How do I get notified when a report completes or new data is released?
  - id: listWebhookSubscriptions
    intent: List active webhook subscriptions
    question: Which webhook subscriptions are active on my account?
  - id: unsubscribeWebhook
    intent: Remove a webhook subscription
    question: How do I stop receiving webhook notifications for a subscription?
  - id: testWebhook
    intent: Send a test notification to a webhook
    question: How can I check that my webhook endpoint is receiving events?
  phrasing_ops: 4
  slug: similarweb-webhooks-api
artifact_total: 45
asyncapis:
- description: ''
  name: Similarweb Webhooks
  slug: similarweb-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SimilarWeb Batch Account API
  slug: open-similarweb-account-api
- collection_type: open
  name: SimilarWeb Batch Account App Intelligence API
  slug: open-similarweb-app-intelligence-api
- collection_type: open
  name: SimilarWeb Batch Account Credits API
  slug: open-similarweb-credits-api
- collection_type: open
  name: SimilarWeb Batch Account Geography API
  slug: open-similarweb-geography-api
- collection_type: open
  name: SimilarWeb Batch Account Integrations API
  slug: open-similarweb-integrations-api
- collection_type: open
  name: SimilarWeb Batch Account Keywords API
  slug: open-similarweb-keywords-api
- collection_type: open
  name: SimilarWeb Batch Account Lead Enrichment API
  slug: open-similarweb-lead-enrichment-api
- collection_type: open
  name: SimilarWeb Batch Account Rankings API
  slug: open-similarweb-rankings-api
- collection_type: open
  name: SimilarWeb Batch Account Reports API
  slug: open-similarweb-reports-api
- collection_type: open
  name: SimilarWeb Batch Account Similar Sites API
  slug: open-similarweb-similar-sites-api
- collection_type: open
  name: SimilarWeb Batch Account Traffic and Engagement API
  slug: open-similarweb-traffic-and-engagement-api
- collection_type: open
  name: SimilarWeb Batch Account Traffic Sources API
  slug: open-similarweb-traffic-sources-api
- collection_type: open
  name: SimilarWeb Batch Account Webhooks API
  slug: open-similarweb-webhooks-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/agentic-access/similarweb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/similarweb-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/security/similarweb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/similarweb-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/authentication/similarweb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/similarweb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.similarweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.similarweb.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/similarweb
- group: company
  title: ''
  type: Blog
  url: https://www.similarweb.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.similarweb.com/corp/daas/api/
- group: other
  title: ''
  type: X
  url: https://x.com/similarweb
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/plans/similarweb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/similarweb-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/rate-limits/similarweb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/similarweb-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/finops/similarweb-finops.yml
  title: ''
  type: FinOps
  url: finops/similarweb-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/well-known/similarweb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/similarweb-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/mcp/similarweb-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/similarweb-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/mcp/similarweb-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/similarweb-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/llms/similarweb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/similarweb-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/packages/similarweb-packages.yml
  title: ''
  type: Packages
  url: packages/similarweb-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/conventions/similarweb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/similarweb-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/errors/similarweb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/similarweb-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/lifecycle/similarweb-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/similarweb-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.similarweb.com/api-v5/guides/rest-api-data-version-migration
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/changelog/similarweb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/similarweb-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/conformance/similarweb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/similarweb-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.similarweb.com/corp/privacy-security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/security/similarweb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/similarweb-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/scopes/similarweb-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/similarweb-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/data-model/similarweb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/similarweb-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/components/similarweb-components.yml
  title: ''
  type: Components
  url: components/similarweb-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/asyncapi/similarweb-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/similarweb-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/overlays/similarweb-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/similarweb-rest-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/overlays/similarweb-batch-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/similarweb-batch-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.similarweb.com/api-v5/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.similarweb.com/api-v5/api-reference/website-analysis-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.similarweb.com/api-v5/getting-started/making-your-first-request
- group: auth
  title: ''
  type: Authentication
  url: https://docs.similarweb.com/api-v5/getting-started/authentication
- group: operate
  title: ''
  type: Support
  url: https://support.similarweb.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://developers.similarweb.com/docs/getting-help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/similarweb
- group: start
  title: ''
  type: SignUp
  url: https://account.similarweb.com/standard-api
- group: start
  title: ''
  type: Login
  url: https://pro.similarweb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.similarweb.com/corp/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.similarweb.com/corp/legal/privacy-policy/
created: '2026-06-13'
description: SimilarWeb is a digital intelligence platform offering a REST API for accessing website traffic estimates, audience demographics, keyword analytics, competitive benchmarking, app intelligence data, and lead generation insights. The API provides real-time and historical data covering traffic sources, search behavior, technographics, e-commerce shopper intelligence, and firmographic company data, enabling developers to integrate market intelligence into applications, dashboards, and data pipelines. The current generation is API V5, launched March 2026, which unified the REST and Batch API keys, added multi-metric requests, and shipped a first-party hosted MCP server at mcp.similarweb.com for AI agents; legacy v1-v4 REST endpoints carry a published sunset date of 2026-10-06.
examples:
- key_count: 2
  name: Similarweb Batch Request Example
  slug: similarweb-batch-request-example
- key_count: 2
  name: Similarweb Geography Example
  slug: similarweb-geography-example
- key_count: 2
  name: Similarweb Visits Desktop Example
  slug: similarweb-visits-desktop-example
finops:
- name: Similarweb Finops
  service_category: ''
  slug: similarweb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/similarweb.png
json_schemas:
- name: SimilarWeb Geography Response
  property_count: 2
  slug: similarweb-geography
- name: SimilarWeb Traffic and Engagement Response
  property_count: 6
  slug: similarweb-traffic-engagement
jsonld:
- class_count: 7
  name: Similarweb Context
  property_count: 49
  slug: similarweb-context
layout: provider
mcp_servers:
- description: Similarweb operates a first-party hosted (remote) MCP server at https://mcp.similarweb.com that exposes its Web, Search and App intelligence datasets as MCP tools. It is not an npm or PyPI package — t
  name: SimilarWeb MCP Server
  slug: similarweb-mcp-server
modified: '2026-08-13'
name: SimilarWeb
nav: Providers
network: true
overview: 'SimilarWeb publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, App Intelligence API, Credits API, and 11 more. Tagged areas include Digital Intelligence, Web Analytics, Traffic Analytics, Competitive Intelligence, and Keyword Analytics.


  The SimilarWeb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SimilarWeb''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Similarweb Plans Pricing
  plan_count: 3
  slug: similarweb-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Similarweb Rate Limits
  slug: similarweb-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SimilarWeb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: similarweb-jsonschema-spectral-rules
scopes:
- name: Similarweb Scopes
  scope_count: 1
  slug: similarweb-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 78.3
    catalog_earned_first_party: 24.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 28.0
    contract_quality: 64.1
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 65.8
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/screenshots/similarweb-2026-06-20T193927.png
security:
- kind: authentication
  name: Similarweb Authentication
  slug: similarweb-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Similarweb Domain Security
  slug: similarweb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Similarweb Trust Center
  slug: similarweb-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: similarweb
tags:
- Digital Intelligence
- Web Analytics
- Traffic Analytics
- Competitive Intelligence
- Keyword Analytics
- Audience Demographics
- App Intelligence
- Market Research
- E-Commerce
- SEO
website: https://www.similarweb.com/
---
