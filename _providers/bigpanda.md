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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bigpanda Agentic Access
  operation_count: 11
  slug: bigpanda-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 27
apis:
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: 'The three agent-facing endpoints: the MCP server, the A2A JSON-RPC endpoint and the agent-card retrieval operation.'
  name: BigPanda Agents API (MCP & A2A)
  slug: bigpanda-agents-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: AI analysis configurations and on-demand AI analysis generation.
  name: BigPanda AI Settings API
  slug: bigpanda-ai-settings-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Alert tags, enrichment items, mapping enrichment schemas and tables — the largest single resource group, and the one that decides what context an incident carries.
  name: BigPanda Alert Tags & Enrichment API
  slug: bigpanda-alert-enrichment-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Alert filters and filter schedules, in current and v1 routes, for suppressing alerts before correlation.
  name: BigPanda Alert Filters API
  slug: bigpanda-alert-filters-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Open Integration Hub ingestion — send raw tool payloads for normalization and processing, with 23 documented tool reference payloads.
  name: BigPanda Alert Ingestion (OIM) API
  slug: bigpanda-alert-ingestion-oim-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Inbound alert ingestion and batch alert resolution — the write path monitoring tools use to push events into BigPanda.
  name: BigPanda Alerts API
  slug: bigpanda-alerts-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Create, read, update and revoke the User API Keys that authenticate every other call.
  name: BigPanda API Keys API
  slug: bigpanda-api-keys-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Search the organization audit log.
  name: BigPanda Audit API
  slug: bigpanda-audit-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Send a natural-language question to Biggy and retrieve the response, synchronously or as an async job.
  name: BigPanda Biggy Query API
  slug: bigpanda-biggy-query-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Request and retrieve AI-powered risk ratings for ServiceNow change requests.
  name: BigPanda Change Risk API
  slug: bigpanda-change-risk-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Ingest deployment and configuration changes and link them to incidents as Root Cause Changes.
  name: BigPanda Changes & Root Cause API
  slug: bigpanda-changes-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The rules that turn alerts into incidents, including their evaluation order.
  name: BigPanda Correlation Patterns API
  slug: bigpanda-correlation-patterns-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Data connectors and their authentication.
  name: BigPanda Data Connectors API
  slug: bigpanda-data-connectors-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Versioned email-parser integration configuration, mirroring the OIM configuration lifecycle.
  name: BigPanda Email Parser Configuration API
  slug: bigpanda-email-parser-configuration-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: BPQL-defined environments and environment groups that scope every incident operation.
  name: BigPanda Environments API
  slug: bigpanda-environments-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Search, read, assign, comment, tag, snooze, merge, split and resolve correlated incidents.
  name: BigPanda Incidents API
  slug: bigpanda-incidents-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Schedule maintenance windows to suppress alerts during planned work, and stop a running window early.
  name: BigPanda Maintenance Plans API
  slug: bigpanda-maintenance-plans-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Add the Biggy transcription bot to a call, then list transcripts, read raw text and generate AI summaries.
  name: BigPanda Meetings & Transcripts API
  slug: bigpanda-meetings-transcripts-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Execute a major-incident workflow from a template, then list, inspect, cancel or resolve the execution.
  name: BigPanda Major Incident Management API
  slug: bigpanda-mim-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Configure Notifications Webhook v2 destinations and discover the dynamic variables a webhook template can interpolate.
  name: BigPanda Notifications & Webhooks API
  slug: bigpanda-notifications-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Versioned Open Integration Hub configuration with list, retrieve, diff and restore — the only versioned object in the BigPanda surface.
  name: BigPanda OIM Configuration API
  slug: bigpanda-oim-configuration-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Troubleshooting logs and multi-context report generation.
  name: BigPanda Reporting API
  slug: bigpanda-reporting-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Roles, role membership and the permission catalog that decides what a User API Key can do.
  name: BigPanda Roles & Permissions API
  slug: bigpanda-roles-permissions-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Machine identities and the API keys attached to them.
  name: BigPanda Service Accounts API
  slug: bigpanda-service-accounts-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: SAML SSO configuration, a SAML debug endpoint, and just-in-time domain and role provisioning.
  name: BigPanda SSO & JIT Provisioning API
  slug: bigpanda-sso-provisioning-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Service and infrastructure topology used to relate alerts across systems.
  name: BigPanda Topology API
  slug: bigpanda-topology-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: User management plus a standards-based SCIM 2.0 provisioning surface for Users and Groups.
  name: BigPanda Users & SCIM API
  slug: bigpanda-users-api
artifact_total: 109
asyncapis:
- description: ''
  name: Bigpanda Webhooks
  slug: bigpanda-webhooks
collections:
- collection_type: postman
  name: BigPanda Alerts API
  slug: postman-bigpanda-alerts-api
- collection_type: postman
  name: BigPanda Alerts Audit API
  slug: postman-bigpanda-audit-api
- collection_type: postman
  name: BigPanda Alerts Changes API
  slug: postman-bigpanda-changes-api
- collection_type: postman
  name: BigPanda Alerts Environments API
  slug: postman-bigpanda-environments-api
- collection_type: postman
  name: BigPanda Alerts Incidents API
  slug: postman-bigpanda-incidents-api
- collection_type: postman
  name: BigPanda Alerts Maintenance Plans API
  slug: postman-bigpanda-maintenance-plans-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BigPanda Alerts API
  slug: open-bigpanda-alerts-api
- collection_type: open
  name: BigPanda Alerts Audit API
  slug: open-bigpanda-audit-api
- collection_type: open
  name: BigPanda Alerts Changes API
  slug: open-bigpanda-changes-api
- collection_type: open
  name: BigPanda Alerts Environments API
  slug: open-bigpanda-environments-api
- collection_type: open
  name: BigPanda Alerts Incidents API
  slug: open-bigpanda-incidents-api
- collection_type: open
  name: BigPanda Alerts Maintenance Plans API
  slug: open-bigpanda-maintenance-plans-api
- collection_type: open
  name: BigPanda API
  slug: open-bigpanda
common:
- group: company
  title: ''
  type: Website
  url: https://www.bigpanda.io/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigpanda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bigpanda-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigpanda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigpanda-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigpandaio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigpanda
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bigpanda/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigpanda.io/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/rules/bigpanda-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/vocabulary/bigpanda-vocabulary.yaml
- group: start
  title: ''
  type: Portal
  url: https://api-docs.bigpanda.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.bigpanda.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.bigpanda.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bigpanda.io/docs/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.bigpanda.io/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bigpanda.io/docs/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bigpanda-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bigpanda-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bigpanda-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bigpanda-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bigpanda-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/bigpanda-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bigpanda-problem-types.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bigpanda-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/bigpanda-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bigpanda-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bigpanda-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bigpanda-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bigpanda-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bigpanda-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bigpanda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bigpanda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bigpanda-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bigpanda-api-reference-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://api-docs.bigpanda.io/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bigpanda.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.bigpanda.io/demo/
- group: start
  title: ''
  type: Login
  url: https://login.bigpanda.io/
- group: operate
  title: ''
  type: Support
  url: https://support.bigpanda.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigpanda.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigpanda.io/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://www.bigpanda.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bigpanda.io/feed/
created: '2025-01-08'
description: 'BigPanda is an agentic IT operations (AIOps) platform that ingests alerts from monitoring and observability tools, correlates them into a small number of actionable incidents, links those incidents to the deployment and configuration changes that caused them, and increasingly acts on them through AI agents. Its public API is large and current: 263 operations across 165 paths, published as OpenAPI 3.0.1 on BigPanda''s own API reference, covering alert ingestion and enrichment, correlation patterns, incidents, environments, changes and root cause, maintenance plans, topology, outbound webhooks, SCIM 2.0 user provisioning, SSO, roles and API keys, plus a Biggy assistant surface with a remote Model Context Protocol server and an A2A agent endpoint.'
examples:
- key_count: 6
  name: Bigpanda Alert Request Example
  slug: bigpanda-alert-request-example
- key_count: 2
  name: Bigpanda Alert Response Example
  slug: bigpanda-alert-response-example
- key_count: 4
  name: Bigpanda Audit Log Entry Example
  slug: bigpanda-audit-log-entry-example
- key_count: 1
  name: Bigpanda Audit Logs Response Example
  slug: bigpanda-audit-logs-response-example
- key_count: 5
  name: Bigpanda Change Request Example
  slug: bigpanda-change-request-example
- key_count: 2
  name: Bigpanda Change Response Example
  slug: bigpanda-change-response-example
- key_count: 4
  name: Bigpanda Environment Example
  slug: bigpanda-environment-example
- key_count: 3
  name: Bigpanda Environment Request Example
  slug: bigpanda-environment-request-example
- key_count: 1
  name: Bigpanda Environments Response Example
  slug: bigpanda-environments-response-example
- key_count: 6
  name: Bigpanda Incident Example
  slug: bigpanda-incident-example
- key_count: 1
  name: Bigpanda Incidents Response Example
  slug: bigpanda-incidents-response-example
- key_count: 5
  name: Bigpanda Maintenance Plan Example
  slug: bigpanda-maintenance-plan-example
- key_count: 4
  name: Bigpanda Maintenance Plan Request Example
  slug: bigpanda-maintenance-plan-request-example
- key_count: 1
  name: Bigpanda Maintenance Plans Response Example
  slug: bigpanda-maintenance-plans-response-example
features:
- description: ML-powered correlation of alerts from 200+ monitoring tools into actionable incidents.
  name: AI Alert Correlation
- description: Triage, acknowledge, and resolve correlated incidents with full audit trail.
  name: Incident Management
- description: Automatically identify root causes by correlating alerts with change events.
  name: Root Cause Analysis
- description: Schedule maintenance windows to suppress expected alerts during planned work.
  name: Maintenance Plans
- description: Ingest deployment and config changes to correlate with alert spikes.
  name: Change Correlation
- description: Define DSL-based environments to group incidents by source, severity, or host.
  name: Environments
- description: Enrich alerts with contextual tags from CMDB and other data sources.
  name: Enrichments
- description: Automate incident response workflows with AI-driven insights and routing.
  name: AIOps Automation
finops:
- name: Bigpanda Finops
  service_category: API
  slug: bigpanda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigpanda.png
json_schemas:
- name: AlertRequest
  property_count: 6
  slug: bigpanda-alert-request
- name: AlertResponse
  property_count: 2
  slug: bigpanda-alert-response
- name: AuditLogEntry
  property_count: 4
  slug: bigpanda-audit-log-entry
- name: AuditLogsResponse
  property_count: 1
  slug: bigpanda-audit-logs-response
- name: ChangeRequest
  property_count: 5
  slug: bigpanda-change-request
- name: ChangeResponse
  property_count: 2
  slug: bigpanda-change-response
- name: EnvironmentRequest
  property_count: 3
  slug: bigpanda-environment-request
- name: Environment
  property_count: 4
  slug: bigpanda-environment
- name: EnvironmentsResponse
  property_count: 1
  slug: bigpanda-environments-response
- name: Incident
  property_count: 6
  slug: bigpanda-incident
- name: IncidentsResponse
  property_count: 1
  slug: bigpanda-incidents-response
- name: MaintenancePlanRequest
  property_count: 4
  slug: bigpanda-maintenance-plan-request
- name: MaintenancePlan
  property_count: 5
  slug: bigpanda-maintenance-plan
- name: MaintenancePlansResponse
  property_count: 1
  slug: bigpanda-maintenance-plans-response
json_structures:
- name: Bigpanda Alert Request Structure
  property_count: 6
  slug: bigpanda-alert-request-structure
- name: Bigpanda Alert Response Structure
  property_count: 2
  slug: bigpanda-alert-response-structure
- name: Bigpanda Audit Log Entry Structure
  property_count: 4
  slug: bigpanda-audit-log-entry-structure
- name: Bigpanda Audit Logs Response Structure
  property_count: 1
  slug: bigpanda-audit-logs-response-structure
- name: Bigpanda Change Request Structure
  property_count: 5
  slug: bigpanda-change-request-structure
- name: Bigpanda Change Response Structure
  property_count: 2
  slug: bigpanda-change-response-structure
- name: Bigpanda Environment Request Structure
  property_count: 3
  slug: bigpanda-environment-request-structure
- name: Bigpanda Environment Structure
  property_count: 4
  slug: bigpanda-environment-structure
- name: Bigpanda Environments Response Structure
  property_count: 1
  slug: bigpanda-environments-response-structure
- name: Bigpanda Incident Structure
  property_count: 6
  slug: bigpanda-incident-structure
- name: Bigpanda Incidents Response Structure
  property_count: 1
  slug: bigpanda-incidents-response-structure
- name: Bigpanda Maintenance Plan Request Structure
  property_count: 4
  slug: bigpanda-maintenance-plan-request-structure
- name: Bigpanda Maintenance Plan Structure
  property_count: 5
  slug: bigpanda-maintenance-plan-structure
- name: Bigpanda Maintenance Plans Response Structure
  property_count: 1
  slug: bigpanda-maintenance-plans-response-structure
jsonld:
- class_count: 6
  name: Bigpanda Context
  property_count: 19
  slug: bigpanda-context
layout: provider
mcp_servers:
- description: 'BigPanda ships two distinct remote Model Context Protocol surfaces. The product one is the Biggy action-plan server at https://api.biggy.io/mcp, documented in BigPanda''s own API reference: a single st'
  name: BigPanda MCP Server
  slug: bigpanda-mcp-server
modified: '2026-09-04'
name: BigPanda
nav: Providers
network: true
overview: 'BigPanda publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Agents API (MCP & A2A), AI Settings API, Alert Tags & Enrichment API, and 24 more. Tagged areas include Incidents, Monitoring, Platform, AIOps, and IT Operations.


  The BigPanda catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  BigPanda''s developer surface includes authentication, developer portal, API reference, documentation, getting-started guide, changelog, pricing, and 38 more developer resources.'
plans:
- name: Bigpanda Plans Pricing
  plan_count: 0
  slug: bigpanda-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Bigpanda Rate Limits
  slug: bigpanda-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BigPanda API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bigpanda-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: BigPanda API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 21
  slug: bigpanda-spectral-rules
scopes:
- name: Bigpanda Scopes
  scope_count: 0
  slug: bigpanda-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 75.5
    catalog_earned_first_party: 12.0
    catalog_gap: 39.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.4
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 47.0
    contract_quality: 71.1
    developer_ergonomics: 60.1
    discoverability: 81.5
    governance: 47.0
    operational_transparency: 81.6
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 28
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/screenshots/bigpanda-2026-06-20T173234.png
security:
- kind: authentication
  name: Bigpanda Authentication
  slug: bigpanda-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Bigpanda Domain Security
  slug: bigpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bigpanda Trust Center
  slug: bigpanda-trust-center
  summary_line: SOC 2, ISO 27001
slug: bigpanda
tags:
- Incidents
- Monitoring
- Platform
- AIOps
- IT Operations
- Alerts
- Incident Management
- Observability
- Agents
- MCP
use_cases:
- description: Reduce alert fatigue by correlating thousands of alerts into a handful of incidents.
  name: Alert Noise Reduction
- description: Automatically link deployment changes to alert spikes for faster root cause identification.
  name: Change Impact Analysis
- description: Route correlated incidents to the right on-call team with full context.
  name: On-Call Automation
- description: Suppress alerts during planned maintenance to prevent false incident creation.
  name: Maintenance Scheduling
- description: Automatically create and update tickets in ServiceNow or Jira from correlated incidents.
  name: ITSM Integration
website: https://www.bigpanda.io/
---
