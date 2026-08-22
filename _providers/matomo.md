---
access_model:
  confidence: high
  label: Open source · Free On-Premise · Paid Cloud · Public demo instance
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Matomo Agentic Access
  operation_count: 560
  slug: matomo-agentic-access
  summary_line: 560 operations · 2 acting
api_count: 61
apis:
- description: 'The Matomo Live API exposes 6 operations of the Matomo Reporting API (module `Live`). Real-time visitor data: live counters, the most recent visits in full detail, and individual visitor profiles. Eve'
  name: Matomo Live API
  slug: live-api
- description: 'The Matomo Goals API exposes 11 operations of the Matomo Reporting API (module `Goals`). Conversion goal management and goal reporting — create, update and delete goals, and read conversions, revenue '
  name: Matomo Goals API
  slug: goals-api
- description: The Matomo SegmentEditor API exposes 9 operations of the Matomo Reporting API (module `SegmentEditor`). Saved segment management — the reusable filter definitions that can be applied to any Matomo rep
  name: Matomo Segments API
  slug: segments-api
- description: The single /index.php dispatch entrypoint through which every Matomo Reporting API method is invoked, by supplying module=API and method=Module.Action. This entry documents the entrypoint contract its
  name: Matomo Reporting API (index.php entrypoint)
  slug: matomo-index-php-api
- description: The Matomo Tracking API — the server-side ingest entrypoint at /matomo.php that records pageviews, events, goals, ecommerce orders, site searches and content interactions. It is the counterpart to the
  name: Matomo Tracking API (matomo.php entrypoint)
  slug: matomo-matomo-php-api
- description: The Matomo SitesManager API exposes 53 operations of the Matomo Reporting API (module `SitesManager`). Site provisioning and configuration — add, update and delete tracked sites, retrieve JavaScript a
  name: Matomo SitesManager API
  slug: sites-manager-api
- description: The Matomo TagManager API exposes 47 operations of the Matomo Reporting API (module `TagManager`). Matomo Tag Manager — containers, versions, tags, triggers and variables, plus embed codes, preview mo
  name: Matomo TagManager API
  slug: tag-manager-api
- description: The Matomo UsersManager API exposes 32 operations of the Matomo Reporting API (module `UsersManager`). User and permission administration — create, invite, update and delete Matomo users, assign per-s
  name: Matomo UsersManager API
  slug: users-manager-api
- description: The Matomo CrashAnalytics API exposes 31 operations of the Matomo Reporting API (module `CrashAnalytics`). JavaScript crash tracking — crash groups, messages, sources, and which pages and categories c
  name: Matomo CrashAnalytics API
  slug: crash-analytics-api
- description: The Matomo HeatmapSessionRecording API exposes 31 operations of the Matomo Reporting API (module `HeatmapSessionRecording`). Heatmaps and session recordings — configure them, read recorded heatmap dat
  name: Matomo HeatmapSessionRecording API
  slug: heatmap-session-recording-api
- description: The Matomo FormAnalytics API exposes 26 operations of the Matomo Reporting API (module `FormAnalytics`). Form performance analytics — entry and drop-off fields, field timings, corrections and conversi
  name: Matomo FormAnalytics API
  slug: form-analytics-api
- description: 'The Matomo Referrers API exposes 23 operations of the Matomo Reporting API (module `Referrers`). Where traffic came from: referrer type, search engines, keywords, campaigns, websites, social networks '
  name: Matomo Referrers API
  slug: referrers-api
- description: The Matomo Funnels API exposes 19 operations of the Matomo Reporting API (module `Funnels`). Conversion funnel definition and analysis — flow, entries, exits and step-level drop-off. Every operation i
  name: Matomo Funnels API
  slug: funnels-api
- description: The Matomo Actions API exposes 18 operations of the Matomo Reporting API (module `Actions`). Page, entry page, exit page, page title, download, outlink and site-search reporting — what visitors actual
  name: Matomo Actions API
  slug: actions-api
- description: 'The Matomo API API exposes 17 operations of the Matomo Reporting API (module `API`). Matomo core meta-API: version and environment info, the machine-readable report and segment metadata catalogs, proc'
  name: Matomo API API
  slug: api-api
- description: 'The Matomo AbTesting API exposes 17 operations of the Matomo Reporting API (module `AbTesting`). A/B test experiment management and results reporting. Every operation is dispatched through the single '
  name: Matomo AbTesting API
  slug: ab-testing-api
- description: 'The Matomo MediaAnalytics API exposes 14 operations of the Matomo Reporting API (module `MediaAnalytics`). Video and audio engagement analytics: plays, finishes, play time and audience watch curves. E'
  name: Matomo MediaAnalytics API
  slug: media-analytics-api
- description: The Matomo CustomReports API exposes 13 operations of the Matomo Reporting API (module `CustomReports`). Build and read custom report definitions combining arbitrary dimensions and metrics. Every oper
  name: Matomo CustomReports API
  slug: custom-reports-api
- description: The Matomo MobileMessaging API exposes 12 operations of the Matomo Reporting API (module `MobileMessaging`). SMS delivery configuration and phone-number verification for scheduled reports. Every opera
  name: Matomo MobileMessaging API
  slug: mobile-messaging-api
- description: The Matomo SearchEngineKeywordsPerformance API exposes 12 operations of the Matomo Reporting API (module `SearchEngineKeywordsPerformance`). Real search keyword data imported from Google Search Consol
  name: Matomo SearchEngineKeywordsPerformance API
  slug: search-engine-keywords-performance-api
- description: 'The Matomo MarketingCampaignsReporting API exposes 11 operations of the Matomo Reporting API (module `MarketingCampaignsReporting`). Extended campaign reporting across campaign name, keyword, source, '
  name: Matomo MarketingCampaignsReporting API
  slug: marketing-campaigns-reporting-api
- description: The Matomo VisitsSummary API exposes 10 operations of the Matomo Reporting API (module `VisitsSummary`). The core traffic overview — visits, unique visitors, users, actions, bounces and time on site f
  name: Matomo VisitsSummary API
  slug: visits-summary-api
- description: The Matomo Events API exposes 9 operations of the Matomo Reporting API (module `Events`). Custom event reporting by category, action and name, with the full set of secondary-dimension pivots. Every op
  name: Matomo Events API
  slug: events-api
- description: The Matomo LanguagesManager API exposes 9 operations of the Matomo Reporting API (module `LanguagesManager`). Language and translation operations for the Matomo interface. Every operation is dispatche
  name: Matomo LanguagesManager API
  slug: languages-manager-api
- description: The Matomo DevicesDetection API exposes 8 operations of the Matomo Reporting API (module `DevicesDetection`). Device type, brand, model, operating system, browser and browser-engine reporting. Every o
  name: Matomo DevicesDetection API
  slug: devices-detection-api
- description: The Matomo OAuth2 API exposes 8 operations of the Matomo Reporting API (module `OAuth2`). OAuth 2.0 client administration for the instance (superuser only). Every operation is dispatched through the s
  name: Matomo OAuth2 API
  slug: oauth2-api
- description: 'The Matomo UserCountry API exposes 8 operations of the Matomo Reporting API (module `UserCountry`). Geolocation reporting: country, continent, region and city. Every operation is dispatched through th'
  name: Matomo UserCountry API
  slug: user-country-api
- description: The Matomo Annotations API exposes 7 operations of the Matomo Reporting API (module `Annotations`). Dated notes attached to a site so report readers can see what happened on a given day. Every operati
  name: Matomo Annotations API
  slug: annotations-api
- description: The Matomo CustomAlerts API exposes 7 operations of the Matomo Reporting API (module `CustomAlerts`). Threshold alerts on any report metric, with triggered-alert history. Every operation is dispatched
  name: Matomo CustomAlerts API
  slug: custom-alerts-api
- description: The Matomo AdvertisingConversionExport API exposes 6 operations of the Matomo Reporting API (module `AdvertisingConversionExport`). Export conversions back out to advertising platforms. Every operatio
  name: Matomo AdvertisingConversionExport API
  slug: advertising-conversion-export-api
- description: The Matomo CustomDimensions API exposes 6 operations of the Matomo Reporting API (module `CustomDimensions`). Configure and read custom dimensions in visit or action scope. Every operation is dispatch
  name: Matomo CustomDimensions API
  slug: custom-dimensions-api
- description: The Matomo PrivacyManager API exposes 6 operations of the Matomo Reporting API (module `PrivacyManager`). GDPR operations — find and export or delete a data subject, manage anonymisation and data rete
  name: Matomo PrivacyManager API
  slug: privacy-manager-api
- description: The Matomo ScheduledReports API exposes 6 operations of the Matomo Reporting API (module `ScheduledReports`). Create, update and send scheduled email and SMS reports. Every operation is dispatched thr
  name: Matomo ScheduledReports API
  slug: scheduled-reports-api
- description: The Matomo Dashboard API exposes 5 operations of the Matomo Reporting API (module `Dashboard`). Dashboard layout and widget management. Every operation is dispatched through the single `/index.php?mod
  name: Matomo Dashboard API
  slug: dashboard-api
- description: The Matomo Insights API exposes 5 operations of the Matomo Reporting API (module `Insights`). Automatic movers-and-shakers analysis — which report rows changed most between two periods. Every operatio
  name: Matomo Insights API
  slug: insights-api
- description: The Matomo Transitions API exposes 4 operations of the Matomo Reporting API (module `Transitions`). What visitors did immediately before and after a given page or page title. Every operation is dispat
  name: Matomo Transitions API
  slug: transitions-api
- description: 'The Matomo VisitorInterest API exposes 4 operations of the Matomo Reporting API (module `VisitorInterest`). Visitor engagement: visit duration, pages per visit, visits per visitor and days since last '
  name: Matomo VisitorInterest API
  slug: visitor-interest-api
- description: The Matomo ActivityLog API exposes 3 operations of the Matomo Reporting API (module `ActivityLog`). Audit log of who changed what inside Matomo. Every operation is dispatched through the single `/inde
  name: Matomo ActivityLog API
  slug: activity-log-api
- description: The Matomo ApiReference API exposes 3 operations of the Matomo Reporting API (module `ApiReference`). Reads the OpenAPI 3.1.0 documents Matomo generates for each installed plugin. This is the endpoint
  name: Matomo ApiReference API
  slug: api-reference-api
- description: The Matomo CoreAdminHome API exposes 3 operations of the Matomo Reporting API (module `CoreAdminHome`). Instance administration operations, including tracking-failure inspection and archive invalidati
  name: Matomo CoreAdminHome API
  slug: core-admin-home-api
- description: The Matomo Feedback API exposes 3 operations of the Matomo Reporting API (module `Feedback`). In-product feedback and survey operations. Every operation is dispatched through the single `/index.php?mo
  name: Matomo Feedback API
  slug: feedback-api
- description: The Matomo MultiSites API exposes 3 operations of the Matomo Reporting API (module `MultiSites`). Cross-site rollup — the All Websites dashboard, with metrics for every site the caller can view in one
  name: Matomo MultiSites API
  slug: multi-sites-api
- description: The Matomo RollUpReporting API exposes 3 operations of the Matomo Reporting API (module `RollUpReporting`). Roll-up sites that aggregate the data of several other sites into one. Every operation is di
  name: Matomo RollUpReporting API
  slug: roll-up-reporting-api
- description: The Matomo Tour API exposes 3 operations of the Matomo Reporting API (module `Tour`). Product onboarding tour and challenge progress. Every operation is dispatched through the single `/index.php?modul
  name: Matomo Tour API
  slug: tour-api
- description: The Matomo VisitTime API exposes 3 operations of the Matomo Reporting API (module `VisitTime`). Visits by server time, local time and day of week. Every operation is dispatched through the single `/in
  name: Matomo VisitTime API
  slug: visit-time-api
- description: The Matomo Cohorts API exposes 2 operations of the Matomo Reporting API (module `Cohorts`). Cohort retention analysis. Every operation is dispatched through the single `/index.php?module=API&method=Co
  name: Matomo Cohorts API
  slug: cohorts-api
- description: 'The Matomo Contents API exposes 2 operations of the Matomo Reporting API (module `Contents`). Content impression and interaction reporting for content blocks and pieces. Every operation is dispatched '
  name: Matomo Contents API
  slug: contents-api
- description: The Matomo Marketplace API exposes 2 operations of the Matomo Reporting API (module `Marketplace`). Access to the Matomo plugin marketplace from inside an instance. Every operation is dispatched throu
  name: Matomo Marketplace API
  slug: marketplace-api
- description: The Matomo Overlay API exposes 2 operations of the Matomo Reporting API (module `Overlay`). Page Overlay support operations, which render analytics on top of the live site. Every operation is dispatch
  name: Matomo Overlay API
  slug: overlay-api
- description: The Matomo Resolution API exposes 2 operations of the Matomo Reporting API (module `Resolution`). Screen resolution and configuration reporting. Every operation is dispatched through the single `/inde
  name: Matomo Resolution API
  slug: resolution-api
- description: The Matomo UserLanguage API exposes 2 operations of the Matomo Reporting API (module `UserLanguage`). Visitor browser language reporting. Every operation is dispatched through the single `/index.php?m
  name: Matomo UserLanguage API
  slug: user-language-api
- description: The Matomo Bandwidth API exposes 1 operations of the Matomo Reporting API (module `Bandwidth`). Bandwidth consumption reporting. Every operation is dispatched through the single `/index.php?module=API
  name: Matomo Bandwidth API
  slug: bandwidth-api
- description: The Matomo CustomJsTracker API exposes 1 operations of the Matomo Reporting API (module `CustomJsTracker`). Access to the generated JavaScript tracker file. Every operation is dispatched through the s
  name: Matomo CustomJsTracker API
  slug: custom-js-tracker-api
- description: The Matomo DevicePlugins API exposes 1 operations of the Matomo Reporting API (module `DevicePlugins`). Browser plugin detection reporting. Every operation is dispatched through the single `/index.php
  name: Matomo DevicePlugins API
  slug: device-plugins-api
- description: The Matomo ImageGraph API exposes 1 operations of the Matomo Reporting API (module `ImageGraph`). Static PNG chart rendering of any Matomo report, for embedding in email and PDFs. Every operation is d
  name: Matomo ImageGraph API
  slug: image-graph-api
- description: 'The Matomo Login API exposes 1 operations of the Matomo Reporting API (module `Login`). Authentication-related operations exposed by the login module. Every operation is dispatched through the single '
  name: Matomo Login API
  slug: login-api
- description: 'The Matomo PagePerformance API exposes 1 operations of the Matomo Reporting API (module `PagePerformance`). Page-load timing reporting: network, server, transfer, DOM processing and DOM completion tim'
  name: Matomo PagePerformance API
  slug: page-performance-api
- description: The Matomo SEO API exposes 1 operations of the Matomo Reporting API (module `SEO`). SEO ranking metrics for a URL. Every operation is dispatched through the single `/index.php?module=API&method=SEO.<A
  name: Matomo SEO API
  slug: seo-api
- description: The Matomo TwoFactorAuth API exposes 1 operations of the Matomo Reporting API (module `TwoFactorAuth`). Two-factor authentication operations. Every operation is dispatched through the single `/index.p
  name: Matomo TwoFactorAuth API
  slug: two-factor-auth-api
- description: The Matomo UserId API exposes 1 operations of the Matomo Reporting API (module `UserId`). Reporting by the User ID assigned to a logged-in visitor. Every operation is dispatched through the single `/i
  name: Matomo UserId API
  slug: user-id-api
- description: The Matomo VisitFrequency API exposes 1 operations of the Matomo Reporting API (module `VisitFrequency`). Returning-visitor metrics. Every operation is dispatched through the single `/index.php?module
  name: Matomo VisitFrequency API
  slug: visit-frequency-api
artifact_total: 76
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Matomo Reporting Index.php API
  slug: open-matomo-index-php-api
- collection_type: open
  name: Matomo Reporting Index.php Matomo.php API
  slug: open-matomo-matomo-php-api
- collection_type: open
  name: Matomo Tracking API
  slug: open-matomo-tracking
- collection_type: open
  name: Matomo Reporting API
  slug: open-matomo
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matomo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/matomo-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matomo-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matomo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/matomo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/matomo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matomo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matomo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/matomo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matomo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matomo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matomo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matomo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://matomo.org/security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matomo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.matomo.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/matomo-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/matomo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/matomo-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/matomo-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matomo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matomo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/matomo-finops.yml
- group: auth
  title: ''
  type: Security
  url: https://matomo.org/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/matomo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/matomo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matomo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.matomo.org
- group: docs
  title: ''
  type: Documentation
  url: https://developer.matomo.org
- group: docs
  title: ''
  type: APIReference
  url: https://developer.matomo.org/api-reference/api
- group: docs
  title: ''
  type: APIDocumentation
  url: https://developer.matomo.org/api-reference/reporting-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.matomo.org/guides/getting-started-part-1
- group: operate
  title: ''
  type: Roadmap
  url: https://matomo.org/roadmap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matomo-org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/matomo-org/matomo
- group: company
  title: ''
  type: Website
  url: https://matomo.org
- group: company
  title: ''
  type: Blog
  url: https://matomo.org/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://matomo.org/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://matomo.org/start-free-analytics-trial
- group: start
  title: ''
  type: Login
  url: https://matomo.org/login
- group: operate
  title: ''
  type: Support
  url: https://matomo.org/support
- group: operate
  title: ''
  type: Forums
  url: https://forum.matomo.org
- group: other
  title: ''
  type: Marketplace
  url: https://plugins.matomo.org
- group: other
  title: ''
  type: SelfHosted
  url: https://matomo.org/matomo-on-premise
- group: start
  title: ''
  type: Demo
  url: https://demo.matomo.cloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://matomo.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://matomo.org/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matomo
created: '2026-03-26'
description: 'Matomo is an open source web analytics platform — self-hosted (Matomo On-Premise) or vendor-hosted (Matomo Cloud) — that gives an organisation complete ownership of its analytics data. Formerly Piwik, it is the leading privacy-first alternative to Google Analytics, with GDPR tooling, data residency in Frankfurt for Cloud, and no data sampling. Its API surface is substantial and unusual: 556 documented operations across 59 plugin modules, every one dispatched through a single /index.php RPC entrypoint on the customer''s own deployment rather than a vendor host, plus a separate tracking entrypoint at /matomo.php. Matomo generates its own OpenAPI 3.1.0 documents through a first-party ApiReference plugin, and ships a first-party Model Context Protocol server exposing 19 agent tools over an authenticated HTTP endpoint.'
finops:
- name: Matomo Finops
  service_category: API
  slug: matomo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matomo.png
layout: provider
mcp_servers:
- description: ''
  name: matomo-mcp.yml
  slug: matomo-mcpyml
modified: '2026-08-13'
name: Matomo
nav: Providers
network: true
overview: 'Matomo publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Live API, Goals API, Segments API, and 58 more. Tagged areas include Analytics, Web Analytics, Open Source, Privacy, and Data Ownership.


  Matomo''s developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 43 more developer resources.'
plans:
- name: Matomo Plans Pricing
  plan_count: 7
  slug: matomo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Matomo Rate Limits
  slug: matomo-rate-limits
scopes:
- name: Matomo Scopes
  scope_count: 3
  slug: matomo-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 67.4
  delta: 4.8
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 16.7
    contract_quality: 48.3
    developer_ergonomics: 80.4
    discoverability: 66.7
    governance: 16.7
    operational_transparency: 81.6
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matomo/refs/heads/main/screenshots/matomo-2026-06-20T185037.png
security:
- kind: authentication
  name: Matomo Authentication
  slug: matomo-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Matomo Domain Security
  slug: matomo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Matomo Vulnerability Disclosure
  slug: matomo-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Matomo Trust Center
  slug: matomo-trust-center
  summary_line: ISO 27001, GDPR
slug: matomo
tags:
- Analytics
- Web Analytics
- Open Source
- Privacy
- Data Ownership
- Self-Hosted
- GDPR
- Tag Management
- Conversion Optimization
- Model Context Protocol
website: https://matomo.org
---
