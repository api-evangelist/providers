---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Axiom Co Agentic Access
  operation_count: 56
  slug: axiom-co-agentic-access
  summary_line: 56 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Mark deployments, incidents, and events on charts.
  name: Axiom Annotations API
  slug: axiom-co-annotations-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Collections of charts and visualizations.
  name: Axiom Dashboards API
  slug: axiom-co-dashboards-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Manage the datasets that store ingested event data.
  name: Axiom Datasets API
  slug: axiom-co-datasets-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Inspect and annotate dataset fields.
  name: Axiom Fields API
  slug: axiom-co-fields-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Send logs, traces, and events into a dataset.
  name: Axiom Ingest API
  slug: axiom-co-ingest-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: APL-backed alert monitors.
  name: Axiom Monitors API
  slug: axiom-co-monitors-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Notification channels monitors dispatch through.
  name: Axiom Notifiers API
  slug: axiom-co-notifiers-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Organization-level settings.
  name: Axiom Organizations API
  slug: axiom-co-organizations-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Run APL queries across datasets.
  name: Axiom Query API
  slug: axiom-co-query-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Saved, shareable APL queries.
  name: Axiom Starred Queries API
  slug: axiom-co-starred-queries-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Scoped API tokens used to authenticate requests.
  name: Axiom Tokens API
  slug: axiom-co-tokens-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Current user and organization members.
  name: Axiom Users API
  slug: axiom-co-users-api
- baseURL: https://api.axiom.co/v1
  baseurl_source: declared
  description: Derived fields computed from an APL expression at query time.
  name: Axiom Virtual Fields API
  slug: axiom-co-virtual-fields-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Edge API from Axiom — 3 operation(s) for edge.
  name: Axiom Edge API
  slug: axiom-co-edge-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Groups API from Axiom — 2 operation(s) for groups.
  name: Axiom Groups API
  slug: axiom-co-groups-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Mapfields API from Axiom — 1 operation(s) for mapfields.
  name: Axiom Mapfields API
  slug: axiom-co-mapfields-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Roles API from Axiom — 2 operation(s) for roles.
  name: Axiom Roles API
  slug: axiom-co-roles-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Views API from Axiom — 2 operation(s) for views.
  name: Axiom Views API
  slug: axiom-co-views-api
- description: Axiom's hosted remote Model Context Protocol server (HTTP transport) at mcp.axiom.co, OAuth-protected per RFC 9728, for querying datasets with APL from agents.
  name: Axiom MCP Server
  slug: axiom-co-mcp-server
artifact_total: 62
asyncapis:
- description: 'Axiom delivers monitor-triggered alerts to user-configured HTTP endpoints via the Custom Webhook Notifier. A monitor (match, threshold, or anomaly) runs a periodic query over event data, and when its '
  name: Axiom Custom Webhook Notifier
  slug: axiom-co-custom-webhook-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Axiom Annotations API
  slug: open-axiom-co-annotations-api
- collection_type: open
  name: Axiom Annotations Dashboards API
  slug: open-axiom-co-dashboards-api
- collection_type: open
  name: Axiom Annotations Datasets API
  slug: open-axiom-co-datasets-api
- collection_type: open
  name: Axiom Annotations Fields API
  slug: open-axiom-co-fields-api
- collection_type: open
  name: Axiom Annotations Ingest API
  slug: open-axiom-co-ingest-api
- collection_type: open
  name: Axiom Annotations Monitors API
  slug: open-axiom-co-monitors-api
- collection_type: open
  name: Axiom Annotations Notifiers API
  slug: open-axiom-co-notifiers-api
- collection_type: open
  name: Axiom Annotations Organizations API
  slug: open-axiom-co-organizations-api
- collection_type: open
  name: Axiom Annotations Query API
  slug: open-axiom-co-query-api
- collection_type: open
  name: Axiom Annotations Starred Queries API
  slug: open-axiom-co-starred-queries-api
- collection_type: open
  name: Axiom Annotations Tokens API
  slug: open-axiom-co-tokens-api
- collection_type: open
  name: Axiom Annotations Users API
  slug: open-axiom-co-users-api
- collection_type: open
  name: Axiom Annotations Virtual Fields API
  slug: open-axiom-co-virtual-fields-api
- collection_type: open
  name: Axiom API
  slug: open-axiom-co
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/rules/axiom-co-rules.yml
  title: ''
  type: Spectral
  url: rules/axiom-co-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/json-ld/axiom-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axiom-co-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/vocabulary/axiom-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axiom-co-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/asyncapi/axiom-co-custom-webhook-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/axiom-co-custom-webhook-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/data-model/axiom-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axiom-co-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/errors/axiom-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/axiom-co-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/conformance/axiom-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axiom-co-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/integrations/axiom-co-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/axiom-co-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/capabilities/axiom-co-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/axiom-co-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/agentic-access/axiom-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/axiom-co-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/security/axiom-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiom-co-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/authentication/axiom-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axiom-co-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axiomhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiomhq
- group: company
  title: ''
  type: Website
  url: https://axiom.co/
- group: docs
  title: ''
  type: Documentation
  url: https://axiom.co/docs
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/plans/axiom-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axiom-co-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/rate-limits/axiom-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/axiom-co-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/finops/axiom-co-finops.yml
  title: ''
  type: FinOps
  url: finops/axiom-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://axiom.co/blog/feed.xml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/axiomhq/skills
created: '2026-07-02'
description: Axiom is a log management, event data, and observability platform that ingests, stores, and queries large volumes of logs, traces, and events at low cost. Data is loaded into datasets and queried with the Axiom Processing Language (APL). The REST API (base https://api.axiom.co, US region; https://api.eu.axiom.co for EU) exposes ingest, APL query, datasets, fields, annotations, monitors, notifiers, dashboards, virtual fields, starred queries, API tokens, users, and organizations, with v1 and v2 endpoint families and Bearer token authentication.
finops:
- has_sources: true
  method: generated
  name: Axiom Co Finops
  primary_unit: ''
  service_category: Observability and Log Management
  slug: axiom-co-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axiom-co.png
json_schemas:
- name: Annotation
  property_count: 8
  slug: axiom-co-annotation
- name: AplQueryRequest
  property_count: 3
  slug: axiom-co-apl-query-request
- name: Dashboard
  property_count: 5
  slug: axiom-co-dashboard
- name: DatasetCreateRequest
  property_count: 2
  slug: axiom-co-dataset-create-request
- name: Dataset
  property_count: 5
  slug: axiom-co-dataset
- name: DatasetUpdateRequest
  property_count: 1
  slug: axiom-co-dataset-update-request
- name: Field
  property_count: 5
  slug: axiom-co-field
- name: IngestStatus
  property_count: 6
  slug: axiom-co-ingest-status
- name: Monitor
  property_count: 10
  slug: axiom-co-monitor
- name: Notifier
  property_count: 4
  slug: axiom-co-notifier
- name: Organization
  property_count: 4
  slug: axiom-co-organization
- name: QueryResult
  property_count: 3
  slug: axiom-co-query-result
- name: StarredQuery
  property_count: 5
  slug: axiom-co-starred-query
- name: TokenCreateRequest
  property_count: 5
  slug: axiom-co-token-create-request
- name: TokenCreated
  property_count: 0
  slug: axiom-co-token-created
- name: Token
  property_count: 6
  slug: axiom-co-token
- name: User
  property_count: 4
  slug: axiom-co-user
- name: VirtualField
  property_count: 6
  slug: axiom-co-virtual-field
jsonld:
- class_count: 18
  name: Axiom Co Context
  property_count: 45
  slug: axiom-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.axiom.co over HTTP.
  name: Axiom MCP Server
  slug: axiom
modified: '2026-07-02'
name: Axiom
nav: Providers
network: true
overview: 'Axiom publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Annotations API, Dashboards API, Datasets API, and 16 more. Tagged areas include Observability, Log Management, Event Data, Logs, and Tracing.


  The Axiom catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Axiom''s developer surface includes authentication, documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Axiom Co Plans Pricing
  plan_count: 3
  slug: axiom-co-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Axiom Co Rate Limits
  slug: axiom-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Axiom API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: axiom-co-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 68.0
    catalog_earned_first_party: 0.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 7.9
    contract_governance: 19.7
    contract_quality: 69.3
    developer_ergonomics: 38.6
    discoverability: 68.3
    operational_transparency: 18.4
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/axiom-co/refs/heads/main/screenshots/axiom-co-2026-10-11T181759.png
security:
- kind: authentication
  name: Axiom Co Authentication
  slug: axiom-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Axiom Co Domain Security
  slug: axiom-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axiom-co
tags:
- Observability
- Log Management
- Event Data
- Logs
- Tracing
- Analytics
- APL
website: https://axiom.co/
---
