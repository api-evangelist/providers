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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 26.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 44
  human_in_the_loop: 2
  name: Raygun Agentic Access
  operation_count: 104
  slug: raygun-agentic-access
  summary_line: 104 operations · 44 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: List, retrieve, and regenerate API keys for applications under your Raygun organization. Applications are the root resource — each owns its own error groups, deployments, source maps, sessions, pages,
  name: Raygun Applications API
  slug: raygun-applications-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: Triage error groups and instances — list, get, resolve, activate, ignore, permanently ignore, and comment on grouped errors. Drill into individual error instances with full stack-trace, environment, r
  name: Raygun Errors API
  slug: raygun-errors-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: Record release markers and correlate them with error groups. Supports SCM integration (GitHub, GitLab, Bitbucket, Azure DevOps), commit reprocessing, latest-deploy lookup, and the api-key shortcut var
  name: Raygun Deployments API
  slug: raygun-deployments-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: Upload, list, retrieve, update, and delete JavaScript source maps for symbolicating minified front-end stack traces in Crash Reporting and RUM error data.
  name: Raygun Source Maps API
  slug: raygun-source-maps-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: List and retrieve Real User Monitoring sessions captured for an application. Each session contains page views, custom timings, and the errors a user experienced during that browsing period.
  name: Raygun Sessions API
  slug: raygun-sessions-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: List and retrieve monitored pages for an application — the per-URL aggregation surface for RUM timing, Core Web Vitals, and page-level error rates.
  name: Raygun Pages API
  slug: raygun-pages-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: List and retrieve customer (end-user) records associated with sessions and error instances. Supports both identified and anonymous user records.
  name: Raygun Customers API
  slug: raygun-customers-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: Query time-series and histogram metrics for page performance and error rates with flexible bucket, range, and filter parameters. Powers custom dashboards and external observability exports.
  name: Raygun Metrics API
  slug: raygun-metrics-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: Upload and manage Flutter debug-symbol artifacts so Raygun can symbolicate native crashes from Flutter mobile applications across iOS and Android builds.
  name: Raygun Flutter Symbols API
  slug: raygun-flutter-symbols-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: List and retrieve teams in your Raygun organization. Teams group members and grant shared access to a curated set of applications.
  name: Raygun Teams API
  slug: raygun-teams-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: Send, list, retrieve, and revoke organization-member invitations. Used to programmatically onboard and offboard users from your Raygun account.
  name: Raygun Invitations API
  slug: raygun-invitations-api
- baseURL: https://api.raygun.com/v3
  baseurl_source: spec
  description: List the available Raygun subscription plans so dashboards and automations can inspect entitlement levels and current allotments per product.
  name: Raygun Plans API
  slug: raygun-plans-api
- description: POST /entries ingestion endpoint at api.raygun.com used by all language SDKs and providers to submit crash payloads. X-ApiKey authenticated; 128 KB payload ceiling; 202 on accept, 400/403/413/429 on e
  name: Raygun Crash Reporting Ingestion API
  slug: raygun-crash-reporting-ingestion-api
- description: Outbound webhook surface that POSTs JSON events to a customer-configured HTTPS endpoint when error notifications fire (NewErrorOccurred, ErrorReoccurred for regression detection, and the 1/5/10/30/60-
  name: Raygun Outbound Webhooks
  slug: raygun-webhooks-api
- description: Legacy enterprise-only Real User Monitoring read API at api.raygun.com/api/v1/pulse. Uses a Client ID/Secret-issued X-SessionKey with 15-minute TTL. Default rate limit 50 calls/day/application. Most n
  name: Raygun Pulse RUM API (Legacy)
  slug: raygun-pulse-rum-api
arazzos:
- description: Record a deployment for an application and confirm it was created.
  name: Raygun Create and Verify Deployment
  slug: raygun-create-and-verify-deployment-workflow
- description: List the monitored pages for an application and read one in detail.
  name: Raygun Inspect Application Page
  slug: raygun-inspect-application-page-workflow
- description: Read the latest deployment and drill into an error group it introduced.
  name: Raygun Inspect Latest Deployment Errors
  slug: raygun-inspect-latest-deployment-errors-workflow
- description: Resolve an application and look up a single affected customer by identifier.
  name: Raygun Look Up Affected Customer
  slug: raygun-lookup-customer-workflow
- description: Upload a source map for an application and confirm it is registered.
  name: Raygun Publish and Verify Source Map
  slug: raygun-publish-source-map-workflow
- description: Find an active error group in an application and mark it as resolved.
  name: Raygun Resolve Error Group
  slug: raygun-resolve-error-group-workflow
- description: Inspect an error group and its latest occurrence, then record a triage comment.
  name: Raygun Triage Error Group and Add Comment
  slug: raygun-triage-error-group-comment-workflow
artifact_total: 90
collections:
- collection_type: postman
  name: Raygun Applications API
  slug: postman-raygun-applications-api
- collection_type: postman
  name: Raygun Customers API
  slug: postman-raygun-customers-api
- collection_type: postman
  name: Raygun Deployments API
  slug: postman-raygun-deployments-api
- collection_type: postman
  name: Raygun Errors API
  slug: postman-raygun-errors-api
- collection_type: postman
  name: Raygun Flutter Symbols API
  slug: postman-raygun-flutter-symbols-api
- collection_type: postman
  name: Raygun Invitations API
  slug: postman-raygun-invitations-api
- collection_type: postman
  name: Raygun Metrics API
  slug: postman-raygun-metrics-api
- collection_type: postman
  name: Raygun Pages API
  slug: postman-raygun-pages-api
- collection_type: postman
  name: Raygun Plans API
  slug: postman-raygun-plans-api
- collection_type: postman
  name: Raygun Sessions API
  slug: postman-raygun-sessions-api
- collection_type: postman
  name: Raygun Source Maps API
  slug: postman-raygun-source-maps-api
- collection_type: postman
  name: Raygun Teams API
  slug: postman-raygun-teams-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Raygun applications API
  slug: open-raygun-applications-api
- collection_type: open
  name: Raygun applications customers API
  slug: open-raygun-customers-api
- collection_type: open
  name: Raygun applications deployments API
  slug: open-raygun-deployments-api
- collection_type: open
  name: Raygun applications errors API
  slug: open-raygun-errors-api
- collection_type: open
  name: Raygun applications flutter-symbols API
  slug: open-raygun-flutter-symbols-api
- collection_type: open
  name: Raygun applications invitations API
  slug: open-raygun-invitations-api
- collection_type: open
  name: Raygun applications metrics API
  slug: open-raygun-metrics-api
- collection_type: open
  name: Raygun applications pages API
  slug: open-raygun-pages-api
- collection_type: open
  name: Raygun applications plans API
  slug: open-raygun-plans-api
- collection_type: open
  name: Raygun API
  slug: open-raygun-public-api
- collection_type: open
  name: Raygun applications sessions API
  slug: open-raygun-sessions-api
- collection_type: open
  name: Raygun applications source-maps API
  slug: open-raygun-source-maps-api
- collection_type: open
  name: Raygun applications teams API
  slug: open-raygun-teams-api
- collection_type: open
  name: Raygun Outbound Webhooks
  slug: open-raygun-webhooks-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/raygun-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/raygun-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raygun-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/raygun-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/raygun/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-create-and-verify-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-inspect-application-page-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-inspect-latest-deployment-errors-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-lookup-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-publish-source-map-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-resolve-error-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/raygun-triage-error-group-comment-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://raygun.com
- group: docs
  title: ''
  type: Documentation
  url: https://raygun.com/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://raygun.com/documentation/product-guides/public-api/
- group: docs
  title: ''
  type: Documentation
  url: https://api.raygun.io/v3/swagger/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.raygun.io/v3/raygun-openapi-spec.json
- group: docs
  title: ''
  type: Documentation
  url: https://raygun.com/documentation/product-guides/crash-reporting/api/
- group: docs
  title: ''
  type: Documentation
  url: https://raygun.com/documentation/product-guides/real-user-monitoring/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.raygun.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://raygun.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://raygun.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://raygun.com/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://raygun.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.raygun.com/signup
- group: operate
  title: ''
  type: Support
  url: https://raygun.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://raygun.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://raygun.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://raygun.com/platform/security-and-compliance
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MindscapeHQ
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4net
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4reactnative
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4maui
- group: build
  title: ''
  type: SDKs
  url: https://github.com/MindscapeHQ/raygun4blazor
- group: build
  title: ''
  type: Tools
  url: https://github.com/MindscapeHQ/raygun-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/MindscapeHQ/raygun4node-aws-lambda
- group: build
  title: ''
  type: Plugin
  url: https://github.com/MindscapeHQ/ember-cli-raygun
- group: commercial
  title: ''
  type: Plans
  url: plans/raygun-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/raygun-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/raygun-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/raygun-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/raygun-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Raygun is an application monitoring platform that combines Crash Reporting, Real User Monitoring (RUM), and Application Performance Monitoring (APM) into a single observability product for web, mobile, and server applications. The Raygun Public API (v3) is a documented OpenAPI 3.0 surface at api.raygun.com/v3 covering applications, error groups, error instances, deployments, source maps, sessions, pages, customers, metrics, Flutter symbols, teams, invitations, and plans — authenticated with a Personal Access Token. A separate ingestion endpoint at api.raygun.com/entries accepts crash payloads from a broad fleet of native SDKs (JavaScript, .NET, Node, Python, Ruby, PHP, Android, Flutter, React Native, MAUI, Blazor) plus the Raygun CLI. Pricing is tiered (Basic, Team, Business, Enterprise) per product with on-demand per-event overages, 14-day free trial, and 180-day error retention.
examples:
- key_count: 2
  name: Raygun Crash Report Example
  slug: raygun-crash-report-example
- key_count: 8
  name: Raygun Create Deployment Example
  slug: raygun-create-deployment-example
- key_count: 10
  name: Raygun Error Group Example
  slug: raygun-error-group-example
features:
- Crash Reporting — error detection, deduplication into error groups, full stack-trace and breadcrumb context
- Real User Monitoring (RUM) — Core Web Vitals, sessions, pages, custom timings, customer drill-down
- Application Performance Monitoring (APM) — Apdex, sampling, flamechart diagnostics, trace search
- AI Error Resolution — LLM-powered analysis of stack traces with suggested fixes
- Deployment Tracking — release markers correlated with new/regressed error groups
- Source Maps and Flutter Symbols — symbolication of minified JS and Flutter mobile stack traces
- Spike Protection — runaway-event guardrail to prevent surprise overages
- Inbound Filters — drop unwanted events before they count toward quota (Team plan and above)
- Custom Dashboards and Custom Reports across all three products
- SAML SSO, role-based permissions, and team-scoped application access (Business plan and above)
- On-demand overage pricing — $0.001/error, $0.002/session, $0.002/trace
- 180-day error retention, 60-day session retention (custom for Enterprise)
- Native SDKs for JavaScript, .NET, Node.js, Python, Ruby, PHP, Android, iOS, Flutter, React Native, MAUI, Blazor
- Raygun CLI for deploys and source-map uploads from CI
- Integrations with Slack, GitHub, Bitbucket, GitLab, Azure DevOps, and Jira
- HIPAA, GDPR, CCPA, and PCI compliant
- Public OpenAPI 3.0 specification covering 53 operations across 12 resource tags
- Personal Access Token bearer auth for the v3 API; X-ApiKey for ingestion
finops:
- name: Raygun Finops
  service_category: Observability
  slug: raygun-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raygun.png
integrations:
- Slack
- GitHub
- GitHub Enterprise
- Bitbucket
- Bitbucket Server
- GitLab
- Azure DevOps
- Jira
json_schemas:
- name: Raygun Deployment
  property_count: 10
  slug: raygun-deployment
- name: Raygun Error Group
  property_count: 0
  slug: raygun-error-group
jsonld:
- class_count: 0
  name: Raygun Context
  property_count: 12
  slug: raygun-context
layout: provider
modified: '2026-05-30'
name: Raygun
nav: Providers
network: true
overview: 'Raygun publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Errors API, Deployments API, and 10 more. Tagged areas include Observability, Crash Reporting, Real User Monitoring, Application Performance Monitoring, and Error Tracking.


  The Raygun catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Raygun''s developer surface includes authentication, developer portal, documentation, changelog, engineering blog, getting-started guide, pricing, and 42 more developer resources.'
plans:
- name: Raygun Plans Pricing
  plan_count: 13
  slug: raygun-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Raygun Rate Limits
  slug: raygun-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Raygun API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: raygun-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Raygun API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 8
  slug: raygun-rules
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 28.8
    contract_quality: 71.0
    developer_ergonomics: 66.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raygun/refs/heads/main/screenshots/raygun-2026-06-20T192616.png
security:
- kind: authentication
  name: Raygun Authentication
  slug: raygun-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Raygun Domain Security
  slug: raygun-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Raygun Trust Center
  slug: raygun-trust-center
  summary_line: HIPAA, GDPR
slug: raygun
tags:
- Observability
- Crash Reporting
- Real User Monitoring
- Application Performance Monitoring
- Error Tracking
- Errors
- Monitoring
- DevOps
- Source Maps
- Deployment
website: https://raygun.com
---
