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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-09-03'
api_count: 30
apis:
- description: Hosted, OAuth-secured Model Context Protocol server that lets AI assistants build campaign drafts, author content, create and count segments, read and analyze flows, browse dashboards, search campaign
  name: MoEngage MCP Server
  slug: moengage-mcp-server
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for importing users and events in bulk.
  name: MoEngage Bulk API
  slug: moengage-bulk-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage and trigger business events.
  name: MoEngage Business Events API
  slug: moengage-business-events-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Download campaign report files.
  name: MoEngage Campaign Reports API
  slug: moengage-campaign-reports-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to fetching and deleting user cards.
  name: MoEngage Cards API
  slug: moengage-cards-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to creating and managing catalog schemas (attributes).
  name: MoEngage Catalog API
  slug: moengage-catalog-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to synchronize cohorts (custom segments) with MoEngage.
  name: MoEngage Cohort Sync API
  slug: moengage-cohort-sync-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Use these operations to programmatically fetch, create, and update reusable content blocks.
  name: MoEngage Content Blocks API
  slug: moengage-content-blocks-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to uploading coupon codes via files and checking/managing file processing status.
  name: MoEngage Coupon Files API
  slug: moengage-coupon-files-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to defining, managing status (active/archive), and modifying coupon list metadata.
  name: MoEngage Coupon Lists API
  slug: moengage-coupon-lists-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Create Campaigns API from MoEngage — 3 operation(s) for create campaigns.
  name: MoEngage Create Campaigns API
  slug: moengage-create-campaigns-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Read custom dashboards and their chart data.
  name: MoEngage Dashboards API
  slug: moengage-dashboards-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for managing user devices.
  name: MoEngage Device API
  slug: moengage-device-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage email templates in MoEngage.
  name: MoEngage Email Templates API
  slug: moengage-email-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for tracking user events.
  name: MoEngage Event API
  slug: moengage-event-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: API endpoints for reporting impressions and clicks.
  name: MoEngage Events API
  slug: moengage-events-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: API endpoints for fetching experiences and metadata.
  name: MoEngage Experiences API
  slug: moengage-experiences-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The File Import API from MoEngage — 3 operation(s) for file import.
  name: MoEngage File Import API
  slug: moengage-file-import-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: If you need to create segments by importing a large number of users, we recommend utilising the File segment API. This API allows you to easily generate a file segment by initiating a call to the file
  name: MoEngage File Segments API
  slug: moengage-file-segments-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: If you need to create a segment based on the events or actions performed by your users on your application or website, the recommended approach is to use the filter segment API. With this API, you can
  name: MoEngage Filter Segments API
  slug: moengage-filter-segments-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Flows API from MoEngage — 4 operation(s) for flows.
  name: MoEngage Flows API
  slug: moengage-flows-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage user data requests for GDPR and CCPA compliance.
  name: MoEngage GDPR API
  slug: moengage-gdpr-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Get Campaign Details API from MoEngage — 6 operation(s) for get campaign details.
  name: MoEngage Get Campaign Details API
  slug: moengage-get-campaign-details-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage In-app templates.
  name: MoEngage In-app Templates API
  slug: moengage-in-app-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to ingesting, updating, and deleting items within a catalog.
  name: MoEngage Items API
  slug: moengage-items-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage broadcast Live Activities for iOS.
  name: MoEngage Live Activities API
  slug: moengage-live-activities-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Archiving and unarchiving through APIs makes it easy to retrieve and reuse segments whenever required for purposes such as A/B testing, maintaining regulatory compliance, and improving system performa
  name: MoEngage Manage Segments API
  slug: moengage-manage-segments-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Retrieve archived message content.
  name: MoEngage Message Archival API
  slug: moengage-message-archival-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Update user email opt-in status and category preferences in MoEngage.
  name: MoEngage Opt-in Management API
  slug: moengage-opt-in-management-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage On-Site Messaging (OSM) templates.
  name: MoEngage OSM Templates API
  slug: moengage-osm-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Personalized Preview API from MoEngage — 1 operation(s) for personalized preview.
  name: MoEngage Personalized Preview API
  slug: moengage-personalized-preview-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Public Offerings API from MoEngage — 3 operation(s) for public offerings.
  name: MoEngage Public Offerings API
  slug: moengage-public-offerings-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to fetching recommendation configurations and results.
  name: MoEngage Recommendations API
  slug: moengage-recommendations-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to generating usage reports for coupon lists.
  name: MoEngage Reports API
  slug: moengage-reports-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Resubscribe users who previously unsubscribed, and optionally update the ESP suppression list.
  name: MoEngage Resubscribe API
  slug: moengage-resubscribe-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage SMS templates.
  name: MoEngage SMS Templates API
  slug: moengage-sms-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Fetch detailed, real-time campaign statistics.
  name: MoEngage Stats API
  slug: moengage-stats-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage user email subscription preferences.
  name: MoEngage Subscription Preferences API
  slug: moengage-subscription-preferences-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Templates API from MoEngage — 2 operation(s) for templates.
  name: MoEngage Templates API
  slug: moengage-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Test Campaigns API from MoEngage — 3 operation(s) for test campaigns.
  name: MoEngage Test Campaigns API
  slug: moengage-test-campaigns-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Endpoints for tracking attribution and installs.
  name: MoEngage Tracking API
  slug: moengage-tracking-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Send transactional alerts using pre-configured templates.
  name: MoEngage Transactional Alerts API
  slug: moengage-transactional-alerts-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to create and send push notification campaigns.
  name: MoEngage Transactional API
  slug: moengage-transactional-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Update Campaigns API from MoEngage — 5 operation(s) for update campaigns.
  name: MoEngage Update Campaigns API
  slug: moengage-update-campaigns-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for creating, updating, retrieving, and managing user profiles.
  name: MoEngage User API
  slug: moengage-user-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Utility endpoints for testing connections.
  name: MoEngage Utilities API
  slug: moengage-utilities-api
artifact_total: 84
asyncapis:
- description: ''
  name: Moengage Webhooks
  slug: moengage-webhooks
collections:
- collection_type: open
  name: MoEngage Analytics Dashboard and Chart API
  slug: open-moengage-analytics
- collection_type: open
  name: MoEngage Business Events API
  slug: open-moengage-business-events
- collection_type: open
  name: MoEngage Campaigns API
  slug: open-moengage-campaign-draft
- collection_type: open
  name: MoEngage Campaigns API
  slug: open-moengage-campaigns
- collection_type: open
  name: MoEngage Cards API
  slug: open-moengage-cards
- collection_type: open
  name: MoEngage Catalog API
  slug: open-moengage-catalog
- collection_type: open
  name: Cohort Sync API
  slug: open-moengage-cohort-audience
- collection_type: open
  name: MoEngage Content Block API
  slug: open-moengage-content-blocks
- collection_type: open
  name: Coupon List API 🏷️
  slug: open-moengage-coupons
- collection_type: open
  name: MoEngage Segments API
  slug: open-moengage-custom-segments
- collection_type: open
  name: MoEngage Email Subscription Management APIs
  slug: open-moengage-email-subscription
- collection_type: open
  name: Email Templates API V1
  slug: open-moengage-email-templates-1
- collection_type: open
  name: Email Templates API V2
  slug: open-moengage-email-templates-2
- collection_type: open
  name: Flows
  slug: open-moengage-flows
- collection_type: open
  name: MoEngage GDPR / CCPA API
  slug: open-moengage-gdpr-ccpa
- collection_type: open
  name: MoEngage In-app Template API
  slug: open-moengage-in-app-templates
- collection_type: open
  name: MoEngage Inform API
  slug: open-moengage-inform
- collection_type: open
  name: MoEngage Broadcast Live Activities API
  slug: open-moengage-live-activities
- collection_type: open
  name: MoEngage Message Archival API
  slug: open-moengage-message-archival
- collection_type: open
  name: Offer Decisioning Public API - v5
  slug: open-moengage-offerings
- collection_type: open
  name: MoEngage On-Site Messaging (OSM) Template API
  slug: open-moengage-osm-templates
- collection_type: open
  name: Personalize APIs
  slug: open-moengage-personalize-experience
- collection_type: open
  name: Push Templates API
  slug: open-moengage-push-templates
- collection_type: open
  name: MoEngage Push API
  slug: open-moengage-push-v2-1
- collection_type: open
  name: MoEngage Push API
  slug: open-moengage-push
- collection_type: open
  name: MoEngage Recommendation API
  slug: open-moengage-recommendations
- collection_type: open
  name: MoEngage SMS Template API
  slug: open-moengage-sms-templates
- collection_type: open
  name: MoEngage Campaign Stats and Reports API
  slug: open-moengage-stats-report
- collection_type: open
  name: MoEngage Subscription Categories API
  slug: open-moengage-subscription-categories
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/moengage-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-gdpr-ccpa-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-business-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-cohort-audience-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-campaign-draft-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-stats-report-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-message-archival-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-push-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-push-v2-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-custom-segments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-email-templates-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-email-templates-2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-push-templates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-sms-templates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-in-app-templates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-osm-templates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-content-blocks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-catalog-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-recommendations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-coupons-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-email-subscription-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-subscription-categories-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-flows-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-inform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-cards-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-live-activities-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-personalize-experience-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moengage-offerings-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moengage-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.moengage.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.moengage.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.moengage.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.moengage.com/docs/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.moengage.com/docs/developer-guide/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.moengage.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.moengage.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moengage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moengage.com/plans-and-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.moengage.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://dashboard.moengage.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moengage.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moengage.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/moengage-dev/api-docs/documentation/p593wcu/moengage-data-apis
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moengage.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.moengage.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.moengage.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moengage-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moengage-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/moengage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moengage-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moengage-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moengage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moengage-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moengage-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/moengage-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moengage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moengage-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moengage-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moengage-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moengage-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moengage-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.moengage.com/responsible-disclosure/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moengage-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/moengage-tool-crosswalk.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moengage-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/moengage-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moengage-webhooks.yml
created: '2026-08-01'
description: MoEngage is an insights-led customer engagement and cross-channel marketing automation platform used by consumer brands to unify customer data, segment audiences, and orchestrate personalized messaging across push notifications, email, SMS, WhatsApp, in-app messages, on-site messaging, app inbox cards, and web push. The platform exposes a broad REST API surface across seven regional data centers (DC-01 through DC-06 and DC-101) covering user and event ingestion, bulk import, business events, GDPR/CCPA data requests, campaign creation and lifecycle management, file- and filter-based segments, cohort sync, content blocks and channel templates, product catalogs, recommendations, coupon lists, offer decisioning, subscription and opt-in preferences, transactional alerts (Inform), iOS Live Activities, personalization experiences, campaign statistics, message archival, and custom analytics dashboards. MoEngage also ships native mobile and web SDKs for Android, iOS, Web, React Native,
  Flutter, Unity, Cordova and Capacitor, and operates a hosted, OAuth-secured Model Context Protocol (MCP) server so AI assistants can draft campaigns, manage segments and flows, and analyze performance conversationally.
image: https://www.moengage.com/wp-content/uploads/2023/03/MoEngage-Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: MoEngage MCP Server
  slug: moengage-mcp-server
modified: '2026-08-14'
name: MoEngage
nav: Providers
network: true
overview: 'MoEngage publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Business Events API, Campaign Reports API, and 42 more. Tagged areas include Customer Engagement, Marketing Automation, Customer Data Platform, Push Notifications, and Email.


  The MoEngage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MoEngage''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 64 more developer resources.'
plans:
- name: Moengage Plans Pricing
  plan_count: 4
  slug: moengage-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Moengage Rate Limits
  slug: moengage-rate-limits
scopes:
- name: Moengage Scopes
  scope_count: 5
  slug: moengage-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 71.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 67.0
    developer_ergonomics: 73.2
    discoverability: 63.0
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 71.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
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
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/screenshots/moengage-2026-08-07T184040.png
security:
- kind: authentication
  name: Moengage Authentication
  slug: moengage-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Moengage Domain Security
  slug: moengage-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Moengage Vulnerability Disclosure
  slug: moengage-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Moengage Trust Center
  slug: moengage-trust-center
  summary_line: SOC 2 Type 2, CSA STAR Level 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO 22301:2019, HIPAA, GDPR, CCPA
slug: moengage
tags:
- Customer Engagement
- Marketing Automation
- Customer Data Platform
- Push Notifications
- Email
- SMS
- WhatsApp
- In-App Messaging
- Segmentation
- Personalization
- Campaign Management
- Analytics
- Mobile SDK
- MCP
- MarTech
website: https://www.moengage.com/
---
