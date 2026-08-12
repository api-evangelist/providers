---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-08-11'
api_count: 11
apis:
- description: 'Create and update user profiles, track events, manage devices, merge and delete users, run bulk imports and file imports, and submit GDPR/CCPA data subject requests. The primary ingestion surface for '
  name: MoEngage Data API
  slug: moengage-data-api
- description: 'Create, update, search, test, and publish Push and Email campaigns. The V5 draft lifecycle builds a campaign incrementally — create a draft, patch components, validate, test-send, then publish — with '
  name: MoEngage Campaigns API
  slug: moengage-campaigns-api
- description: Send transactional and targeted push notifications to Android, iOS, and Web devices, and create push campaigns targeting all users or a group of users. Served from a dedicated push host.
  name: MoEngage Push API
  slug: moengage-push-api
- description: Create and manage file-based segments (upload, add, remove, replace users) and filter-based segments built from event and attribute conditions, plus archive/unarchive operations and cohort audience sy
  name: MoEngage Segments API
  slug: moengage-segments-api
- description: Create, update, and search reusable content across channels — email templates (V1 and V2), push templates, SMS templates, in-app templates, on-site messaging (OSM) templates, and content blocks such a
  name: MoEngage Content and Templates API
  slug: moengage-content-and-templates-api
- description: Manage product and item catalogs (create, add attributes, ingest, search, update, bulk delete), fetch recommendation metadata and items, and administer coupon lists and coupon files including activati
  name: MoEngage Catalog, Recommendations and Coupons API
  slug: moengage-catalog-recommendations-and-coupons-api
- description: Manage email resubscription in bulk, update opt-in management preferences, and read, create, and update per-category subscription preferences for users across channels.
  name: MoEngage Subscriptions API
  slug: moengage-subscriptions-api
- description: Read-only access to MoEngage Custom Dashboards and the analytics data behind each chart, plus Flows endpoints to list flows, read a flow and a specific flow version, and update flow status.
  name: MoEngage Analytics and Flows API
  slug: moengage-analytics-and-flows-api
- description: 'Unified transactional messaging infrastructure for building and managing transactional alerts across SMS, Email, and Push from a single send endpoint. Publishes a dedicated sandbox host alongside the '
  name: MoEngage Inform API
  slug: moengage-inform-api
- description: 'App Inbox Cards fetch and delete, iOS broadcast Live Activities (start, update, end), Personalize experiences fetch/metadata/event tracking from client SDK hosts, and Offer Decisioning offerings with '
  name: MoEngage Engagement Surfaces API
  slug: moengage-engagement-surfaces-api
- description: Hosted, OAuth-secured Model Context Protocol server that lets AI assistants build campaign drafts, author content, create and count segments, read and analyze flows, browse dashboards, search campaign
  name: MoEngage MCP Server
  slug: moengage-mcp-server
artifact_total: 18
common:
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
created: '2026-08-01'
description: MoEngage is an insights-led customer engagement and cross-channel marketing automation platform used by consumer brands to unify customer data, segment audiences, and orchestrate personalized messaging across push notifications, email, SMS, WhatsApp, in-app messages, on-site messaging, app inbox cards, and web push. The platform exposes a broad REST API surface across seven regional data centers (DC-01 through DC-06 and DC-101) covering user and event ingestion, bulk import, business events, GDPR/CCPA data requests, campaign creation and lifecycle management, file- and filter-based segments, cohort sync, content blocks and channel templates, product catalogs, recommendations, coupon lists, offer decisioning, subscription and opt-in preferences, transactional alerts (Inform), iOS Live Activities, personalization experiences, campaign statistics, message archival, and custom analytics dashboards. MoEngage also ships native mobile and web SDKs for Android, iOS, Web, React Native,
  Flutter, Unity, Cordova and Capacitor, and operates a hosted, OAuth-secured Model Context Protocol (MCP) server so AI assistants can draft campaigns, manage segments and flows, and analyze performance conversationally.
image: https://www.moengage.com/wp-content/uploads/2023/03/MoEngage-Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: moengage-mcp.yml
  slug: moengage-mcpyml
modified: '2026-08-01'
name: MoEngage
nav: Providers
network: true
overview: 'MoEngage publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Data API, Campaigns API, Push API, and 7 more. Tagged areas include customer-engagement, marketing-automation, customer-data-platform, push-notifications, and email.


  MoEngage''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 23
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
  band: strong
  composite: 63.1
  delta: -0.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.9
    developer_ergonomics: 79.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 63.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
- customer-engagement
- marketing-automation
- customer-data-platform
- push-notifications
- email
- sms
- whatsapp
- in-app-messaging
- segmentation
- personalization
- campaign-management
- analytics
- mobile-sdk
- mcp
- martech
website: https://www.moengage.com/
---
