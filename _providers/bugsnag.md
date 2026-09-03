---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Bugsnag Agentic Access
  operation_count: 38
  slug: bugsnag-agentic-access
  summary_line: 38 operations · 16 acting
api_count: 5
apis:
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Notify Bugsnag about application builds and deployments. Build notifications are used to track releases, identify regressions, and associate source control information with error data.
  name: bugsnag Builds API
  slug: bugsnag-builds-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Manage collaborators within an organization or project. Collaborators are users who have access to view and manage Bugsnag data.
  name: bugsnag Collaborators API
  slug: bugsnag-collaborators-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Manage comments on errors. Comments allow team members to discuss and annotate specific errors.
  name: bugsnag Comments API
  slug: bugsnag-comments-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access information about the currently authenticated user.
  name: bugsnag CurrentUser API
  slug: bugsnag-currentuser-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access and manage errors within projects. Errors represent groups of similar events that have been detected by Bugsnag.
  name: bugsnag Errors API
  slug: bugsnag-errors-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access event field definitions for projects. Event fields describe the available data dimensions for filtering and searching events.
  name: bugsnag EventFields API
  slug: bugsnag-eventfields-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access individual error events. Events represent individual occurrences of an error within a project.
  name: bugsnag Events API
  slug: bugsnag-events-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Send error and exception notifications to Bugsnag. Each notification can contain one or more events representing individual error occurrences.
  name: bugsnag Notifications API
  slug: bugsnag-notifications-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access and manage organizations. An organization is the top-level entity in Bugsnag that contains projects and collaborators.
  name: bugsnag Organizations API
  slug: bugsnag-organizations-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access pivot data for errors. Pivots allow you to group and analyze error data by various dimensions such as browser, device, or location.
  name: bugsnag Pivots API
  slug: bugsnag-pivots-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access and manage projects within an organization. Projects represent individual applications being monitored by Bugsnag.
  name: bugsnag Projects API
  slug: bugsnag-projects-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access release information for projects. Releases represent deployed versions of your application and their associated error data.
  name: bugsnag Releases API
  slug: bugsnag-releases-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Report session data to Bugsnag for stability score calculations. Sessions represent periods of user activity and are used to compute crash-free session and user percentages.
  name: bugsnag Sessions API
  slug: bugsnag-sessions-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access stability metrics for projects. Stability data provides crash-free session and user percentages across releases.
  name: bugsnag Stability API
  slug: bugsnag-stability-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Send OpenTelemetry trace data to Bugsnag for performance monitoring. Spans represent individual operations and are assembled into traces that visualize request flow and latency.
  name: bugsnag Traces API
  slug: bugsnag-traces-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access trend data for errors and projects. Trends provide time-series data showing how error rates and stability change over time.
  name: bugsnag Trends API
  slug: bugsnag-trends-api
artifact_total: 111
asyncapis:
- description: 'Bugsnag webhooks deliver real-time notifications about error events to a configured callback URL via HTTP POST. The webhook integration sends JSON payloads containing information about the triggering '
  name: Bugsnag Webhook Events
  slug: bugsnag-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bugsnag Build API
  slug: open-bugsnag-build
- collection_type: open
  name: Bugsnag Build Builds API
  slug: open-bugsnag-builds-api
- collection_type: open
  name: Bugsnag Build Builds Collaborators API
  slug: open-bugsnag-collaborators-api
- collection_type: open
  name: Bugsnag Build Builds Comments API
  slug: open-bugsnag-comments-api
- collection_type: open
  name: Bugsnag Build Builds CurrentUser API
  slug: open-bugsnag-currentuser-api
- collection_type: open
  name: Bugsnag Data Access API
  slug: open-bugsnag-data-access
- collection_type: open
  name: Bugsnag Error Reporting API
  slug: open-bugsnag-error-reporting
- collection_type: open
  name: Bugsnag Build Builds Errors API
  slug: open-bugsnag-errors-api
- collection_type: open
  name: Bugsnag Build Builds EventFields API
  slug: open-bugsnag-eventfields-api
- collection_type: open
  name: Bugsnag Build Builds Events API
  slug: open-bugsnag-events-api
- collection_type: open
  name: Bugsnag Build Builds Notifications API
  slug: open-bugsnag-notifications-api
- collection_type: open
  name: Bugsnag Build Builds Organizations API
  slug: open-bugsnag-organizations-api
- collection_type: open
  name: Bugsnag Build Builds Pivots API
  slug: open-bugsnag-pivots-api
- collection_type: open
  name: Bugsnag Build Builds Projects API
  slug: open-bugsnag-projects-api
- collection_type: open
  name: Bugsnag Build Builds Releases API
  slug: open-bugsnag-releases-api
- collection_type: open
  name: Bugsnag Session Tracking API
  slug: open-bugsnag-session-tracking
- collection_type: open
  name: Bugsnag Build Builds Sessions API
  slug: open-bugsnag-sessions-api
- collection_type: open
  name: Bugsnag Build Builds Stability API
  slug: open-bugsnag-stability-api
- collection_type: open
  name: Bugsnag Trace API
  slug: open-bugsnag-trace
- collection_type: open
  name: Bugsnag Build Builds Traces API
  slug: open-bugsnag-traces-api
- collection_type: open
  name: Bugsnag Build Builds Trends API
  slug: open-bugsnag-trends-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bugsnag-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bugsnag-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bugsnag-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bugsnag-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bugsnag
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bugsnag2
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bugsnag-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/bugsnag-error-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/bugsnag-build-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bugsnag-context.jsonld
description: Bugsnag is an application stability monitoring platform that helps software teams detect, diagnose, and fix errors in web, mobile, and back-end applications.
features:
- 'Free: 7.5K events + 1M spans/mo, 1 user'
- 'Select: 50K-3M events tiers, unlimited users, SAML SSO'
- 'Preferred: 100K-3M events, premium support, dedicated CSM'
- 'Enterprise: custom allowances, on-prem option, named CSM'
- Notify API for event ingest from any platform
- Data API at 60 req/min for issue queries
- 50+ platform SDKs (Node, Ruby, Python, JS, mobile, game engines)
- Stability scores and crash benchmarks
- End-to-end distributed tracing
- Auto error prioritization (Select+)
- Auto error assignment (Preferred+)
- Feature flags & experiments (Preferred+)
- On-prem deployment option (Preferred+)
- Sensitive data filtering
- 30+ integrations (Slack, Jira, GitHub, etc.)
- Source map upload for minified JS/native crashes
finops:
- name: Bugsnag Finops
  service_category: Error Monitoring
  slug: bugsnag-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bugsnag.png
json_schemas:
- name: ApplicationInfo
  property_count: 5
  slug: bugsnag-applicationinfo
- name: Breadcrumb
  property_count: 4
  slug: bugsnag-breadcrumb
- name: BreadcrumbPayload
  property_count: 4
  slug: bugsnag-breadcrumbpayload
- name: Bugsnag Build
  property_count: 9
  slug: bugsnag-build
- name: BuildPayload
  property_count: 9
  slug: bugsnag-buildpayload
- name: BuildResponse
  property_count: 2
  slug: bugsnag-buildresponse
- name: Collaborator
  property_count: 8
  slug: bugsnag-collaborator
- name: CollaboratorInvite
  property_count: 3
  slug: bugsnag-collaboratorinvite
- name: CollaboratorUpdate
  property_count: 2
  slug: bugsnag-collaboratorupdate
- name: Comment
  property_count: 6
  slug: bugsnag-comment
- name: CommentCreate
  property_count: 1
  slug: bugsnag-commentcreate
- name: DeviceInfo
  property_count: 6
  slug: bugsnag-deviceinfo
- name: Bugsnag Error Event
  property_count: 14
  slug: bugsnag-error-event
- name: Error
  property_count: 1
  slug: bugsnag-error
- name: ErrorItem
  property_count: 21
  slug: bugsnag-erroritem
- name: ErrorResponse
  property_count: 1
  slug: bugsnag-errorresponse
- name: ErrorUpdate
  property_count: 3
  slug: bugsnag-errorupdate
- name: Event
  property_count: 17
  slug: bugsnag-event
- name: EventField
  property_count: 3
  slug: bugsnag-eventfield
- name: EventPayload
  property_count: 14
  slug: bugsnag-eventpayload
- name: Exception
  property_count: 3
  slug: bugsnag-exception
- name: ExceptionPayload
  property_count: 4
  slug: bugsnag-exceptionpayload
- name: ExportTraceServiceRequest
  property_count: 1
  slug: bugsnag-exporttraceservicerequest
- name: ExportTraceServiceResponse
  property_count: 1
  slug: bugsnag-exporttraceserviceresponse
- name: KeyValue
  property_count: 2
  slug: bugsnag-keyvalue
- name: NotificationPayload
  property_count: 4
  slug: bugsnag-notificationpayload
- name: Notifier
  property_count: 3
  slug: bugsnag-notifier
- name: Organization
  property_count: 8
  slug: bugsnag-organization
- name: Pivot
  property_count: 4
  slug: bugsnag-pivot
- name: PivotValue
  property_count: 4
  slug: bugsnag-pivotvalue
- name: Project
  property_count: 22
  slug: bugsnag-project
- name: ProjectCreate
  property_count: 2
  slug: bugsnag-projectcreate
- name: ProjectUpdate
  property_count: 5
  slug: bugsnag-projectupdate
- name: Release
  property_count: 14
  slug: bugsnag-release
- name: ResourceSpans
  property_count: 2
  slug: bugsnag-resourcespans
- name: ScopeSpans
  property_count: 2
  slug: bugsnag-scopespans
- name: SessionCount
  property_count: 3
  slug: bugsnag-sessioncount
- name: SessionPayload
  property_count: 4
  slug: bugsnag-sessionpayload
- name: Span
  property_count: 10
  slug: bugsnag-span
- name: StabilityTrend
  property_count: 1
  slug: bugsnag-stabilitytrend
- name: StackFrame
  property_count: 6
  slug: bugsnag-stackframe
- name: StackFramePayload
  property_count: 6
  slug: bugsnag-stackframepayload
- name: ThreadPayload
  property_count: 4
  slug: bugsnag-threadpayload
- name: Trend
  property_count: 1
  slug: bugsnag-trend
- name: User
  property_count: 5
  slug: bugsnag-user
json_structures:
- name: Bugsnag Structure
  property_count: 0
  slug: bugsnag-structure
jsonld:
- class_count: 0
  name: Bugsnag Context
  property_count: 7
  slug: bugsnag-context
layout: provider
modified: '2026-05-19'
name: Bugsnag
nav: Providers
network: true
overview: 'Bugsnag publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Collaborators API, Comments API, and 13 more.


  The Bugsnag catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Bugsnag''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Bugsnag Plans Pricing
  plan_count: 4
  slug: bugsnag-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Bugsnag Rate Limits
  slug: bugsnag-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Bugsnag API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: bugsnag-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Bugsnag API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bugsnag-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 69.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 66.9
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 93.8
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bugsnag/refs/heads/main/screenshots/bugsnag-2026-06-20T173757.png
security:
- kind: authentication
  name: Bugsnag Authentication
  slug: bugsnag-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bugsnag Domain Security
  slug: bugsnag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bugsnag Vulnerability Disclosure
  slug: bugsnag-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bugsnag
---
