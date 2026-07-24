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
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Instabug Agentic Access
  operation_count: 10
  slug: instabug-agentic-access
  summary_line: 10 operations
api_count: 13
apis:
- description: Enterprise-only REST API for exporting App Health metrics (crash-free sessions, cold/hot app launches, OOMs, ANRs) for ingest into Grafana, Datadog, or internal dashboards. Authentication and endpoint
  name: Luciq App Health Metrics Export API
  slug: export-api
- description: Outbound HTTP POST webhooks deliver Bugs, Crashes, and APM events to a customer-configured callback URL. Requests are signed with HMAC-SHA256 using a per-webhook secret and delivered with the x-ibg-si
  name: Luciq Webhooks
  slug: webhooks
- description: Native iOS SDK distributed via CocoaPods and Swift Package Manager covering bug reporting, crash reporting, APM (app launch, network, screen rendering, screen loading, flows), session replay, in-app s
  name: Luciq iOS SDK (formerly Instabug-iOS)
  slug: ios-sdk
- description: Native Android SDK covering bug reporting, crash reporting (including ANR capture and deobfuscation), APM (app launch, network, screen rendering, screen loading, execution traces, flows, custom spans)
  name: Luciq Android SDK (formerly Instabug-Android)
  slug: android-sdk
- description: React Native plugin wrapping the native iOS and Android Luciq SDKs. Adds Expo integration, CodePush / Over-The-Air update support, plus bug reporting, crash reporting, APM, session replay, surveys, in
  name: Luciq React Native SDK (formerly Instabug-React-Native)
  slug: react-native-sdk
- description: Flutter plugin wrapping the native iOS and Android Luciq SDKs to deliver bug reporting, crash reporting (with crash-free sessions), APM (app launch, network, screen loading, UI hangs, flows, custom sp
  name: Luciq Flutter SDK (formerly Instabug-Flutter)
  slug: flutter-sdk
- description: Kotlin Multiplatform SDK that ships the Luciq mobile observability surface (bug reporting, crash reporting, APM with Ktor network logging, session replay, surveys, in-app replies, feature requests, cu
  name: Luciq Kotlin Multiplatform SDK
  slug: kmp-sdk
- description: Inspect grouped UI freeze (hang) events for a Luciq application, filterable by date, status, app version, device, OS, and current view.
  name: Instabug (Luciq) App Hangs API
  slug: instabug-app-hangs-api
- description: Enumerate the mobile applications accessible to the authenticated account. Applications are the root scoping primitive for every other MCP tool in this surface.
  name: Instabug (Luciq) Applications API
  slug: instabug-applications-api
- description: Read user-reported bugs submitted via the Luciq SDK report flow, filterable by status, priority, and app version, with full detail including logs, user data, and device metadata for reproduction.
  name: Instabug (Luciq) Bugs API
  slug: instabug-bugs-api
- description: Inspect grouped crashes for a Luciq application, including occurrence frequency, affected users, root cause hints, and aggregation patterns by device, OS, app version, view, app status, and experiment
  name: Instabug (Luciq) Crashes API
  slug: instabug-crashes-api
- description: 'Drill down from a crash group into individual occurrence ULIDs and the full per-occurrence context: device, OS, memory, storage, app status, user identity, and log URLs.'
  name: Instabug (Luciq) Occurrences API
  slug: instabug-occurrences-api
- description: Read app store, native-prompt, and custom-prompt reviews captured through the Luciq SDK, with filters for rating, version, country, device, prompt type, and OS.
  name: Instabug (Luciq) Reviews API
  slug: instabug-reviews-api
artifact_total: 66
asyncapis:
- description: Luciq (formerly Instabug) webhooks deliver real-time notifications about bug reports, crash reports, and APM events to a configured callback URL via HTTP POST. The webhook integration is configured pe
  name: Luciq Webhook Events
  slug: instabug-webhooks-asyncapi
collections:
- collection_type: open
  name: Luciq MCP Server
  slug: open-instabug-mcp-server
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instabug-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instabug-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instabug-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instabug-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://luciq.ai
- group: start
  title: ''
  type: Login
  url: https://dashboard.luciq.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.luciq.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.luciq.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://luciq.ai/pricing
- group: other
  title: ''
  type: Platforms
  url: https://luciq.ai/platforms
- group: operate
  title: ''
  type: MigrationHub
  url: https://docs.luciq.ai/getting-started/luciq-migration-hub
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.luciq.ai/changelog/readme
- group: company
  title: ''
  type: Blog
  url: https://luciq.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Instabug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instabug
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Instabug
- group: other
  title: ''
  type: Sitemap
  url: https://docs.luciq.ai/sitemap.md
- group: agent
  title: ''
  type: LLMsFullText
  url: https://docs.luciq.ai/llms-full.txt
- group: auth
  title: ''
  type: SecuritySOC2
  url: https://luciq.ai/pricing
- group: other
  title: ''
  type: SubProcessors
  url: https://docs.luciq.ai/organization-settings/others/sub-processors
- group: auth
  title: ''
  type: GDPR
  url: https://docs.luciq.ai/organization-settings/gdpr
- group: other
  title: ''
  type: AuditNotes
  url: https://docs.luciq.ai/organization-settings/audit-notes
- group: other
  title: ''
  type: SSO
  url: https://docs.luciq.ai/organization-settings/user-management/sso-using-saml
- group: other
  title: ''
  type: SCIM
  url: https://docs.luciq.ai/organization-settings/user-management/scim-provisioning
- group: commercial
  title: ''
  type: Plans
  url: plans/instabug-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instabug-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instabug-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-application-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-crash-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-occurrence-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-bug-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-review-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-app-hang-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instabug-webhook-payload-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/instabug-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/instabug-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/instabug-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/instabug-rules.yml
- group: other
  title: ''
  type: Branding
  url: ''
- group: other
  title: ''
  type: Customers
  url: ''
- group: agent
  title: ''
  type: MCPCapability
  url: ''
- group: build
  title: ''
  type: GitHubOrganizationProfile
  url: ''
- group: commercial
  title: ''
  type: BillingModel
  url: ''
created: '2026-05-23'
description: Instabug — now rebranded as Luciq — is an agentic mobile observability platform covering bug reporting, crash reporting, application performance monitoring, session replay, surveys, feature flags, rollout management, and AI agents (Detect, Resolve, Release). Public agent-facing surface is the Luciq MCP Server at api.luciq.ai/api/mcp; data export, webhooks, and per-platform SDKs (iOS, Android, React Native, Flutter, KMP) round out the API footprint.
examples:
- key_count: 2
  name: Instabug Get Occurrence Details Example
  slug: instabug-get-occurrence-details-example
- key_count: 2
  name: Instabug List Applications Example
  slug: instabug-list-applications-example
- key_count: 2
  name: Instabug List Bugs Example
  slug: instabug-list-bugs-example
- key_count: 2
  name: Instabug List Crashes Example
  slug: instabug-list-crashes-example
- key_count: 2
  name: Instabug List Reviews Example
  slug: instabug-list-reviews-example
- key_count: 2
  name: Instabug Webhook Crash Example
  slug: instabug-webhook-crash-example
features:
- 'Observability pillar: crash detection, UI glitches, session replay, user feedback'
- 'Intelligence pillar: automated prioritization, business-impact scoring, frustration-free sessions'
- 'Resolution pillar: SmartResolve, root cause analysis, AI Debugging Assistant, automated pull requests'
- 'Prevention pillar: real-time alerts, release management, feature flags, PR review by Release Agent'
- 'AI agents: Detect Agent, Resolve Agent, Release Agent'
- 'Agent Skills: luciq-debug, luciq-setup, luciq-migrate'
- Luciq MCP Server with 10 tools across applications, crashes, occurrences, app hangs, bugs, reviews
- SDKs across iOS, Android, React Native, Flutter, KMP (5 platforms)
- 'Legacy SDKs: Cordova, Swift Package Manager standalone'
- 30+ third-party integrations (Jira, Slack, GitHub, PagerDuty, Datadog, Grafana, LaunchDarkly, etc.)
- Webhooks with HMAC-SHA256 signing for Bugs, Crashes, APM events
- 'Pricing model: priced on Daily Active Users (DAU) and Seats, not logs/sessions/traces'
- 'Per DAU entitlement: 180 sessions/month'
- Unlimited apps per account; unlimited integrations
- SOC 2 Type II, SAML SSO, OAuth SSO, SCIM provisioning, RBAC, regional data pinning
- 'Retention: Crash 180d, Bug 365d, APM 8w, Session Replay 4w, Surveys 365d'
- 100 Observer seats included on Enterprise plans
finops:
- name: Instabug Finops
  service_category: Mobile Observability
  slug: instabug-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instabug.png
integrations:
- 'Project Management: Jira, Trello, Asana, ClickUp, Basecamp (v2 & v3), Shortcut, Pivotal Tracker, Teamwork Projects, Manuscript, Microsoft Azure DevOps, Phabricator'
- 'Notifications: Slack, Microsoft Teams'
- 'Incident Management: PagerDuty, Opsgenie'
- 'Customer Service: Zendesk, ServiceNow, Freshdesk, FrontApp'
- 'Source Control: GitHub, GitLab'
- 'SSO: Okta, OneLogin, Google Cloud Identity, SAML, OAuth'
- 'Observability: New Relic, Instana, Grafana, Datadog, Dynatrace'
- 'Feature Flags: LaunchDarkly'
- 'Other: Webhooks, Zapier, GitHub Marketplace, AWS Marketplace, Jira Marketplace'
json_schemas:
- name: Luciq App Hang
  property_count: 10
  slug: instabug-app-hang
- name: Luciq Application
  property_count: 4
  slug: instabug-application
- name: Luciq Bug Report
  property_count: 13
  slug: instabug-bug
- name: Luciq Crash
  property_count: 13
  slug: instabug-crash
- name: Luciq Crash Occurrence
  property_count: 12
  slug: instabug-occurrence
- name: Luciq App Review
  property_count: 10
  slug: instabug-review
- name: Luciq Webhook Payload
  property_count: 0
  slug: instabug-webhook-payload
json_structures:
- name: Instabug Structure
  property_count: 0
  slug: instabug-structure
jsonld:
- class_count: 0
  name: Instabug Context
  property_count: 7
  slug: instabug-context
layout: provider
modified: '2026-05-23'
name: Instabug (Luciq)
nav: Providers
network: true
overview: 'Instabug (Luciq) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Luciq Webhooks, App Hangs API, Applications API, and 4 more. Tagged areas include Agentic AI, APM, Application Performance Monitoring, Bug Reporting, and Crash Reporting.


  The Instabug (Luciq) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Instabug (Luciq)''s developer surface includes authentication, developer portal, documentation, pricing, changelog, engineering blog, and 32 more developer resources.'
plans:
- name: Instabug Plans Pricing
  plan_count: 3
  slug: instabug-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 7
  name: Instabug Rate Limits
  slug: instabug-rate-limits
rules:
- name: Instabug (Luciq) API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: instabug-asyncapi-spectral-rules
- name: Instabug (Luciq) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: instabug-jsonschema-spectral-rules
- name: Instabug (Luciq) API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: instabug-rules
scopes:
- name: Instabug Scopes
  scope_count: 1
  slug: instabug-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 57.6
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 65.9
    developer_ergonomics: 34.8
    discoverability: 67.5
    governance: 65.8
    operational_transparency: 52.6
  previous_composite: 57.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instabug/refs/heads/main/screenshots/instabug-2026-06-20T183406.png
security:
- kind: authentication
  name: Instabug Authentication
  slug: instabug-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Instabug Domain Security
  slug: instabug-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instabug
tags:
- Agentic AI
- APM
- Application Performance Monitoring
- Bug Reporting
- Crash Reporting
- MCP
- Mobile
- Mobile Observability
- Observability
- Session Replay
website: https://luciq.ai
---
