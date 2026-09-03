---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: News Break Agentic Access
  operation_count: 28
  slug: news-break-agentic-access
  summary_line: 28 operations · 20 acting
api_count: 2
apis:
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Account-level spending caps and remaining budget.
  name: News Break Account Billing API
  slug: news-break-account-billing-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Ad accounts under an organization and the users who can access them.
  name: News Break Ad Account API
  slug: news-break-ad-account-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Ads and their creatives, plus creative asset upload.
  name: News Break Ad API
  slug: news-break-ad-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: 'Ad sets: budget, bidding, schedule, platforms and audience targeting.'
  name: News Break Ad Set API
  slug: news-break-ad-set-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: 'Campaigns: the objective-level container for ad sets.'
  name: News Break Campaign API
  slug: news-break-campaign-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Conversion tracking events (pixel and postback).
  name: News Break Event Management API
  slug: news-break-event-management-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Organizations the calling user administers.
  name: News Break Organization API
  slug: news-break-organization-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Synchronous and saved custom performance reports.
  name: News Break Report API
  slug: news-break-report-api
- baseURL: https://business.newsbreak.com/business-api/v1
  baseurl_source: declared
  description: Aggregated monetization performance reporting for MSP organizations and apps.
  name: News Break Reporting API
  slug: news-break-reporting-api
arazzos:
- description: Resolve the caller's organization and ad account, create a campaign, attach a tracking event, create an ad set with budget, bidding and targeting, upload the creative asset to the NewsBreak CDN, and c
  name: Launch a NewsBreak advertising campaign
  slug: news-break-launch-campaign
- description: Pull a last-7-days performance report for an ad account, list its campaigns, and pause a chosen campaign by toggling its status to OFF. Read-only steps are safe to retry; the status toggle is not idem
  name: Report on a NewsBreak ad account and pause underperforming campaigns
  slug: news-break-pause-and-report
artifact_total: 17
collections:
- collection_type: open
  name: NewsBreak Advertising API
  slug: open-news-break-advertising
- collection_type: open
  name: NewsBreak MSP Monetization Reporting API
  slug: open-news-break-monetization-reporting
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/news-break-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/news-break-advertising-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/news-break-monetization-reporting-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/news-break-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/news-break-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.newsbreak.com/
- group: company
  title: ''
  type: About
  url: https://www.newsbreak.com/who-we-are
- group: start
  title: ''
  type: DeveloperPortal
  url: https://advertising-api.newsbreak.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://advertising-api.newsbreak.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://advertising-api.newsbreak.com/hc/en-us/categories/37825505060237-API-Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://advertising-api.newsbreak.com/hc/en-us/articles/43889846961037-API-Integration-Guide
- group: operate
  title: ''
  type: Support
  url: https://help.newsbreak.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.newsbreak.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://business.newsbreak.com/
- group: start
  title: ''
  type: Login
  url: https://business.newsbreak.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.newsbreak.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.newsbreak.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/news-break-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/news-break-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/news-break-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/news-break-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/news-break-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/news-break-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/news-break-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/news-break-conformance.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/news-break-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/news-break-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/news-break-mcp.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/news-break-launch-campaign.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/news-break-pause-and-report.yml
created: '2026-08-01'
description: 'NewsBreak is the leading local news and information platform in the United States, operated by Particle Media, Inc., a Delaware corporation founded in Silicon Valley in 2015 and launched as a mobile app in 2016. Its AI-powered platform serves more than 40 million Americans a month with local news, alerts, crime maps, weather, events and community content, connecting local users, local content creators and local businesses at scale. NewsBreak exposes two developer surfaces. The NewsBreak Advertising API (NewsBreak API for Business) lets technology companies, direct advertisers and agencies programmatically manage the NewsBreak Ads Manager: organizations and ad accounts, ad-account user roles, campaigns, ad sets with budget, bidding, inventory platforms and audience targeting, ads and creative asset upload, account spending caps, conversion tracking events, and multidimensional performance reporting. The NewsBreak MSP Monetization Reporting API serves the supply side, returning
  impressions, revenue, publisher net revenue and eCPM for publishers and monetization partners. NewsBreak also publishes an llms.txt that scopes AI access to its verified local-business content surface.'
image: https://static.newsbreak.com/static/favicon-32x32.png
layout: provider
modified: '2026-08-01'
name: News Break
nav: Providers
network: true
overview: 'News Break publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account Billing API, Ad Account API, Ad API, and 6 more. Tagged areas include Company, Advertising, AdTech, News, and Media.


  News Break''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 9
  name: News Break Rate Limits
  slug: news-break-rate-limits
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 58.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/news-break/refs/heads/main/screenshots/news-break-2026-08-07T185122.png
security:
- kind: authentication
  name: News Break Authentication
  slug: news-break-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: News Break Domain Security
  slug: news-break-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: news-break
tags:
- Company
- Advertising
- AdTech
- News
- Media
- Local News
- Publishing
- Monetization
- Campaign Management
- Reporting
- Analytics
- Content
website: https://www.newsbreak.com/
---
