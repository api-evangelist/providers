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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
api_count: 3
apis:
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing account settings, configurations, and account-level information
  name: ObservePoint Account API
  slug: observepoint-account-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Account-level triggered alerts
  name: ObservePoint Account Triggered Alerts API
  slug: observepoint-account-triggered-alerts-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Alerts related to account usage
  name: ObservePoint Account Usage Alerts API
  slug: observepoint-account-usage-alerts-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Export account usage data
  name: ObservePoint Account Usage Export API
  slug: observepoint-account-usage-export-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Account usage data
  name: ObservePoint Account Usage V2 API
  slug: observepoint-account-usage-v2-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Action Set Action Rules
  name: ObservePoint Action Set Action Rules API
  slug: observepoint-action-set-action-rules-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Action Set Actions
  name: ObservePoint Action Set Actions API
  slug: observepoint-action-set-actions-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Action Sets
  name: ObservePoint Action Sets API
  slug: observepoint-action-sets-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Export alert data
  name: ObservePoint Alert Export API
  slug: observepoint-alert-export-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Alert Summary report endpoints
  name: ObservePoint Alert Summary Report API
  slug: observepoint-alert-summary-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Alert management and configuration
  name: ObservePoint Alerts API
  slug: observepoint-alerts-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing audit actions
  name: ObservePoint Audit Actions API
  slug: observepoint-audit-actions-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing audit request blocking configuration
  name: ObservePoint Audit Blocking Config API
  slug: observepoint-audit-blocking-config-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing audit login actions
  name: ObservePoint Audit Login Actions API
  slug: observepoint-audit-login-actions-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Export audit run data
  name: ObservePoint Audit Run Export API
  slug: observepoint-audit-run-export-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Audit Summary report endpoints
  name: ObservePoint Audit Summary Report API
  slug: observepoint-audit-summary-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing audits including creation, configuration, execution, and retrieving audit results and runs
  name: ObservePoint Audits API
  slug: observepoint-audits-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing audit consent categories
  name: ObservePoint Audits Consent Category API
  slug: observepoint-audits-consent-category-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing audits
  name: ObservePoint Audits Management API
  slug: observepoint-audits-management-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Browser Logs report endpoints
  name: ObservePoint Browser Logs Report API
  slug: observepoint-browser-logs-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Consent Categories
  name: ObservePoint Consent Categories API
  slug: observepoint-consent-categories-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Export consent category data
  name: ObservePoint Consent Category Export API
  slug: observepoint-consent-category-export-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Cookie Inventory report endpoints
  name: ObservePoint Cookie Inventory Report API
  slug: observepoint-cookie-inventory-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Cookie privacy report
  name: ObservePoint Cookie Privacy Report API
  slug: observepoint-cookie-privacy-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing custom HTTP header groups
  name: ObservePoint Custom Headers API
  slug: observepoint-custom-headers-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Data Sources
  name: ObservePoint Data Sources API
  slug: observepoint-data-sources-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: OpAdmin-only APIs for finding email inboxes and messages by search string
  name: ObservePoint Email Finder API
  slug: observepoint-email-finder-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing email inbox configurations and setting
  name: ObservePoint Email Inbox Configuration API
  slug: observepoint-email-inbox-configuration-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Email inbox message alerts
  name: ObservePoint Email Inbox Message Alerts API
  slug: observepoint-email-inbox-message-alerts-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Get Email Inbox message details
  name: ObservePoint Email Inbox Messages API
  slug: observepoint-email-inbox-messages-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for getting email messages and results from email inboxes
  name: ObservePoint Email Inboxes API
  slug: observepoint-email-inboxes-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Access requested exports status/information
  name: ObservePoint Exports API
  slug: observepoint-exports-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: File changes report endpoints
  name: ObservePoint File Changes Report API
  slug: observepoint-file-changes-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing folders including creation, organization, access control, and folder-based resource management
  name: ObservePoint Folders API
  slug: observepoint-folders-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for geo locations
  name: ObservePoint Geo Locations API
  slug: observepoint-geo-locations-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing labels including creation, assignment, and retrieval for organizing audits, journeys, and other resources
  name: ObservePoint Labels API
  slug: observepoint-labels-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Export manual journey run data
  name: ObservePoint Manual Journey Run Export API
  slug: observepoint-manual-journey-run-export-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing manual journeys including real device testing, HAR file ingestion, and journey execution control. These endpoints power Live Connect and HAR Analyzer features in the ObservePoin
  name: ObservePoint Manual Journeys API
  slug: observepoint-manual-journeys-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Find and manage email subscriptions
  name: ObservePoint Notification Center API
  slug: observepoint-notification-center-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Detailed information about specific pages including tags, cookies, request logs, and console logs
  name: ObservePoint Page Details Report API
  slug: observepoint-page-details-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Page Summary report endpoints
  name: ObservePoint Page Summary Report API
  slug: observepoint-page-summary-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Remote File Mappings
  name: ObservePoint Remote File Mappings API
  slug: observepoint-remote-file-mappings-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: The Reports API from ObservePoint — 6 operation(s) for reports.
  name: ObservePoint Reports API
  slug: observepoint-reports-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Request Privacy report endpoints
  name: ObservePoint Request Privacy Report API
  slug: observepoint-request-privacy-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Rule Summary report endpoints
  name: ObservePoint Rule Summary Report API
  slug: observepoint-rule-summary-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing rules including creation, configuration, assignment, and rule-based validation logic
  name: ObservePoint Rules API
  slug: observepoint-rules-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Manage scheduled grid report data exports
  name: ObservePoint Scheduled Exports API
  slug: observepoint-scheduled-exports-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for item schedules and calendars
  name: ObservePoint Schedules API
  slug: observepoint-schedules-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Site Census
  name: ObservePoint Site Censuses API
  slug: observepoint-site-censuses-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing sub-folders including creation, configuration, and sub-folder-based audit and journey management
  name: ObservePoint Sub Folders API
  slug: observepoint-sub-folders-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Tag Duplicates and Multiples report endpoints
  name: ObservePoint Tag Duplicates And Multiples Report API
  slug: observepoint-tag-duplicates-and-multiples-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Tag Health report endpoints
  name: ObservePoint Tag Health Report API
  slug: observepoint-tag-health-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Tag Inventory report endpoints
  name: ObservePoint Tag Inventory Report API
  slug: observepoint-tag-inventory-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Tag privacy report endpoints
  name: ObservePoint Tag Privacy Report API
  slug: observepoint-tag-privacy-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing tags and tag-related operations including tag metadata and configuration
  name: ObservePoint Tags API
  slug: observepoint-tags-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing User Events
  name: ObservePoint User Events API
  slug: observepoint-user-events-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Endpoints for managing users including creation, authentication, permissions, and user account management
  name: ObservePoint Users API
  slug: observepoint-users-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Variable Inventory report endpoints
  name: ObservePoint Variable Inventory Report API
  slug: observepoint-variable-inventory-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Retrieve audit run data including pages, cookies, geo-locations, network requests, JS variables and failures for web audit runs
  name: ObservePoint Web Audits API
  slug: observepoint-web-audits-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing web journey request blocking configuration
  name: ObservePoint Web Journey Blocking Config API
  slug: observepoint-web-journey-blocking-config-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Cookie analysis and reporting for web journeys
  name: ObservePoint Web Journey Cookie Report API
  slug: observepoint-web-journey-cookie-report-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing web journey custom headers
  name: ObservePoint Web Journey Custom Headers API
  slug: observepoint-web-journey-custom-headers-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: Export web journey run data
  name: ObservePoint Web Journey Run Export API
  slug: observepoint-web-journey-run-export-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: The web-journeys-internal API from ObservePoint — 2 operation(s) for web-journeys-internal.
  name: ObservePoint Web Journeys Internal API
  slug: observepoint-web-journeys-internal-api
- baseURL: https://api.observepoint.com
  baseurl_source: declared
  description: APIs for managing Web Journeys
  name: ObservePoint Web Journeys Management API
  slug: observepoint-web-journeys-management-api
artifact_total: 71
asyncapis:
- description: ''
  name: Observepoint Webhooks
  slug: observepoint-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/observepoint-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/observepoint-v3-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/observepoint-grid-reports-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/observepoint-v2-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/observepoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/observepoint-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.observepoint.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.observepoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.observepoint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.observepoint.com/sections/v3-index
- group: start
  title: ''
  type: GettingStarted
  url: https://help.observepoint.com/en/articles/9106323-getting-started-with-the-observepoint-api
- group: operate
  title: ''
  type: Support
  url: https://help.observepoint.com/
- group: company
  title: ''
  type: Blog
  url: https://www.observepoint.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/observepoint
- group: commercial
  title: ''
  type: Pricing
  url: https://www.observepoint.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.observepoint.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.observepoint.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.observepoint.com/service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.observepoint.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://news.observepoint.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.observepoint.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/observepoint-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/observepoint-site-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/observepoint-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/observepoint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/observepoint-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/observepoint-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/observepoint-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/observepoint-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/observepoint-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/observepoint-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/observepoint-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/observepoint-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/observepoint-data-dictionary-schemas.json
created: '2026-08-26'
description: ObservePoint is a web governance and digital data-quality platform that automatically scans websites, mobile web properties and email links to validate analytics tags, marketing pixels, cookies, consent banners, link integrity and WCAG accessibility. Customers configure Audits (large-scale crawls of a site) and Web Journeys (scripted multi-step user paths), run them on a schedule or on demand, and get back structured reports on tags, variables, cookies, network requests, browser logs, privacy exposure and accessibility issues. Everything in the product is available through a public REST API at api.observepoint.com across two supported versions (v2 and v3) plus a Grid Reporting API that returns any report as rows and columns with filtering, sorting, grouping, pagination and export. API access is included with every ObservePoint subscription at no additional cost, and audits and journeys can push completion webhooks (HMAC-SHA256 signed) into CI/CD pipelines, BI tools and ticketing
  systems.
image: https://www.observepoint.com/wp-content/themes/observepoint/assets/images/op-fallback-img.png
json_schemas:
- name: Data Dictionary API by Observepoint
  property_count: 0
  slug: observepoint-data-dictionary-schemas
layout: provider
modified: '2026-08-26'
name: ObservePoint
nav: Providers
network: true
overview: 'ObservePoint publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Triggered Alerts API, Account Usage Alerts API, and 62 more. Tagged areas include Company, web-governance, Tag Management, analytics-validation, and Privacy Compliance.


  The ObservePoint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ObservePoint''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Observepoint Plans Pricing
  plan_count: 0
  slug: observepoint-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Observepoint Rate Limits
  slug: observepoint-rate-limits
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 68.6
    developer_ergonomics: 58.9
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 49.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 65
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/observepoint/refs/heads/main/screenshots/observepoint-2026-09-02T150820.png
security:
- kind: authentication
  name: Observepoint Authentication
  slug: observepoint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Observepoint Domain Security
  slug: observepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: observepoint
tags:
- Company
- web-governance
- Tag Management
- analytics-validation
- Privacy Compliance
- Consent Management
- Web Accessibility
- Data Quality
- Marketing Technology
- website-auditing
- Digital Analytics
- Webhook
website: https://www.observepoint.com/
---
