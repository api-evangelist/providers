---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cronitor Agentic Access
  operation_count: 24
  slug: cronitor-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 1
apis:
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The Groups API from Cronitor — 3 operation(s) for groups.
  name: Cronitor Groups API
  slug: cronitor-groups-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The Notifications API from Cronitor — 2 operation(s) for notifications.
  name: Cronitor Notifications API
  slug: cronitor-notifications-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The aggregates API from Cronitor — 1 operation(s) for aggregates.
  name: Cronitor Aggregates API
  slug: cronitor-aggregates-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The environments API from Cronitor — 2 operation(s) for environments.
  name: Cronitor Environments API
  slug: cronitor-environments-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The integrations API from Cronitor — 4 operation(s) for integrations.
  name: Cronitor Integrations API
  slug: cronitor-integrations-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The issues API from Cronitor — 3 operation(s) for issues.
  name: Cronitor Issues API
  slug: cronitor-issues-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The keys API from Cronitor — 2 operation(s) for keys.
  name: Cronitor Keys API
  slug: cronitor-keys-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The maintenance_windows API from Cronitor — 2 operation(s) for maintenance_windows.
  name: Cronitor Maintenance Windows API
  slug: cronitor-maintenance-windows-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The metrics API from Cronitor — 1 operation(s) for metrics.
  name: Cronitor Metrics API
  slug: cronitor-metrics-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The monitors API from Cronitor — 5 operation(s) for monitors.
  name: Cronitor Monitors API
  slug: cronitor-monitors-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The search API from Cronitor — 1 operation(s) for search.
  name: Cronitor Search API
  slug: cronitor-search-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The site_errors API from Cronitor — 2 operation(s) for site_errors.
  name: Cronitor Site Errors API
  slug: cronitor-site-errors-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The sites API from Cronitor — 3 operation(s) for sites.
  name: Cronitor Sites API
  slug: cronitor-sites-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The statuspage_components API from Cronitor — 2 operation(s) for statuspage_components.
  name: Cronitor Statuspage Components API
  slug: cronitor-statuspage-components-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: The statuspages API from Cronitor — 2 operation(s) for statuspages.
  name: Cronitor Statuspages API
  slug: cronitor-statuspages-api
- baseURL: https://cronitor.io/api/monitors
  baseurl_source: declared
  description: Send events from jobs and heartbeats. Served from cronitor.link.
  name: Cronitor Telemetry API
  slug: cronitor-telemetry-api
artifact_total: 37
collections:
- collection_type: open
  name: Cronitor Groups and Notifications Cronitor Telemetry API API
  slug: open-cronitor-cronitor-telemetry-api-api
- collection_type: open
  name: Cronitor and Notifications Cronitor Telemetry API Groups API
  slug: open-cronitor-groups-api
- collection_type: open
  name: Cronitor Groups and Notifications Cronitor Telemetry API Monitors API
  slug: open-cronitor-monitors-api
- collection_type: open
  name: Cronitor Groups and Cronitor Telemetry API Notifications API
  slug: open-cronitor-notifications-api
- collection_type: open
  name: Cronitor Groups and Notifications Cronitor Telemetry API P API
  slug: open-cronitor-p-api
- collection_type: open
  name: Cronitor Groups and Notifications Cronitor Telemetry API Search API
  slug: open-cronitor-search-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cronitor/overview
- group: other
  href: https://artifacts.apis.io/cronitor/capabilities/cronitor-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cronitor-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cronitor/agentic-access/cronitor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cronitor-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cronitor/security/cronitor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cronitor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cronitor/authentication/cronitor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cronitor-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cronitor.io
- group: docs
  title: ''
  type: Documentation
  url: https://cronitor.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cronitorio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cronitor
- group: company
  title: ''
  type: Blog
  url: https://cronitor.io/cronicle
- group: commercial
  title: ''
  type: Pricing
  url: https://cronitor.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cronitor.io
- group: other
  title: ''
  type: X
  url: https://x.com/cronitorio
- group: commercial
  href: https://artifacts.apis.io/cronitor/plans/cronitor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cronitor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cronitor/rate-limits/cronitor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cronitor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cronitor/finops/cronitor-finops.yml
  title: ''
  type: FinOps
  url: finops/cronitor-finops.yml
- group: design
  href: https://artifacts.apis.io/cronitor/vocabulary/cronitor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cronitor-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cronitor/json-ld/cronitor-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/cronitor-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cronitor/json-schema/cronitor-monitor-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cronitor-monitor-schema.json
- group: docs
  href: https://artifacts.apis.io/cronitor/json-schema/cronitor-telemetry-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cronitor-telemetry-event-schema.json
- group: docs
  href: https://artifacts.apis.io/cronitor/json-schema/cronitor-notification-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cronitor-notification-list-schema.json
created: '2026-06-12'
description: Cronitor is a cron job and scheduled task monitoring platform that provides developers with instant alerts when jobs fail, run too long, or don't run at all. The platform offers a REST API for creating and managing monitors, recording job telemetry events, and configuring alert policies across teams. Cronitor supports job monitoring, heartbeat monitoring, website uptime checks, and Real User Monitoring (RUM), all accessible via a versioned HTTP API using Basic Auth with scoped API keys. SDKs are available for Python, Node.js, Ruby, PHP, Java, Go, and other languages through the cronitorio GitHub organization.
examples:
- key_count: 3
  name: Cronitor Create Monitor Example
  slug: cronitor-create-monitor-example
- key_count: 3
  name: Cronitor List Monitors Example
  slug: cronitor-list-monitors-example
- key_count: 2
  name: Cronitor Telemetry Event Example
  slug: cronitor-telemetry-event-example
finops:
- has_sources: true
  method: generated
  name: Cronitor Finops
  primary_unit: ''
  service_category: Developer Tools
  slug: cronitor-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cronitor.png
json_schemas:
- name: Cronitor Monitor
  property_count: 26
  slug: cronitor-monitor
- name: Cronitor Notification List
  property_count: 8
  slug: cronitor-notification-list
- name: Cronitor Telemetry Event
  property_count: 7
  slug: cronitor-telemetry-event
jsonld:
- class_count: 6
  name: Cronitor Context
  property_count: 38
  slug: cronitor-context
layout: provider
mcp_servers:
- description: Remote MCP server at cronitor.io over HTTP.
  name: Cronitor MCP Server
  slug: cronitor
modified: '2026-09-16'
name: Cronitor
nav: Providers
network: true
overview: 'Cronitor publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Groups API, Notifications API, Aggregates API, and 13 more. Tagged areas include Monitoring, Cron Jobs, Scheduled Tasks, Alerting, and Uptime.


  The Cronitor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cronitor''s developer surface includes authentication, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Cronitor Plans Pricing
  plan_count: 3
  slug: cronitor-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Cronitor Rate Limits
  slug: cronitor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Cronitor — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cronitor-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.8
    catalog_earned_first_party: 0.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 18.4
    contract_governance: 23.5
    contract_quality: 56.4
    developer_ergonomics: 25.0
    discoverability: 68.3
    operational_transparency: 26.3
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 24
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/cronitor/cronitor-2026-06-20T175236.png
security:
- kind: authentication
  name: Cronitor Authentication
  slug: cronitor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cronitor Domain Security
  slug: cronitor-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cronitor
tags:
- Monitoring
- Cron Jobs
- Scheduled Tasks
- Alerting
- Uptime
- Telemetry
- Status Pages
- Scheduling
website: https://cronitor.io
---
