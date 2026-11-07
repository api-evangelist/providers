---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 225
  human_in_the_loop: 1
  name: Firehydrant Agentic Access
  operation_count: 411
  slug: firehydrant-agentic-access
  summary_line: 411 operations · 225 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Audits API from FireHydrant — 1 operation(s) for audits.
  name: FireHydrant Audits API
  slug: firehydrant-audits-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Change Events API from FireHydrant — 2 operation(s) for change events.
  name: FireHydrant Change Events API
  slug: firehydrant-change-events-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Changes API from FireHydrant — 1 operation(s) for changes.
  name: FireHydrant Changes API
  slug: firehydrant-changes-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Conversations API from FireHydrant — 1 operation(s) for conversations.
  name: FireHydrant Conversations API
  slug: firehydrant-conversations-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Environments API from FireHydrant — 2 operation(s) for environments.
  name: FireHydrant Environments API
  slug: firehydrant-environments-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Functionalities API from FireHydrant — 1 operation(s) for functionalities.
  name: FireHydrant Functionalities API
  slug: firehydrant-functionalities-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Incidents API from FireHydrant — 5 operation(s) for incidents.
  name: FireHydrant Incidents API
  slug: firehydrant-incidents-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Ping API from FireHydrant — 1 operation(s) for ping.
  name: FireHydrant Ping API
  slug: firehydrant-ping-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Priorities API from FireHydrant — 1 operation(s) for priorities.
  name: FireHydrant Priorities API
  slug: firehydrant-priorities-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Runbooks API from FireHydrant — 2 operation(s) for runbooks.
  name: FireHydrant Runbooks API
  slug: firehydrant-runbooks-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Scheduled Maintenances API from FireHydrant — 1 operation(s) for scheduled maintenances.
  name: FireHydrant Scheduled Maintenances API
  slug: firehydrant-scheduled-maintenances-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Services API from FireHydrant — 2 operation(s) for services.
  name: FireHydrant Services API
  slug: firehydrant-services-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Severities API from FireHydrant — 1 operation(s) for severities.
  name: FireHydrant Severities API
  slug: firehydrant-severities-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Signals API from FireHydrant — 1 operation(s) for signals.
  name: FireHydrant Signals API
  slug: firehydrant-signals-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The Teams API from FireHydrant — 2 operation(s) for teams.
  name: FireHydrant Teams API
  slug: firehydrant-teams-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Account Settings
  name: FireHydrant Account Settings API
  slug: firehydrant-account-settings-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Alerts
  name: FireHydrant Alerts API
  slug: firehydrant-alerts-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Communication
  name: FireHydrant Communication API
  slug: firehydrant-communication-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Incident Settings
  name: FireHydrant Incident Settings API
  slug: firehydrant-incident-settings-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Integrations
  name: FireHydrant Integrations API
  slug: firehydrant-integrations-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: The metrics API from FireHydrant — 1 operation(s) for metrics.
  name: FireHydrant Metrics API
  slug: firehydrant-metrics-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Metrics/Reporting
  name: FireHydrant Metrics/Reporting API
  slug: firehydrant-metrics-reporting-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Retrospectives
  name: FireHydrant Retrospectives API
  slug: firehydrant-retrospectives-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to SCIM
  name: FireHydrant SCIM API
  slug: firehydrant-scim-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Status Pages
  name: FireHydrant Status Pages API
  slug: firehydrant-status-pages-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Tasks
  name: FireHydrant Tasks API
  slug: firehydrant-tasks-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Users
  name: FireHydrant Users API
  slug: firehydrant-users-api
- baseURL: https://api.firehydrant.io/v1
  baseurl_source: declared
  description: Operations related to Webhooks
  name: FireHydrant Webhooks API
  slug: firehydrant-webhooks-api
artifact_total: 60
asyncapis:
- description: ''
  name: Firehydrant Webhooks
  slug: firehydrant-webhooks
collections:
- collection_type: open
  name: FireHydrant REST Audits API
  slug: open-firehydrant-audits-api
- collection_type: open
  name: FireHydrant REST Audits Change Events API
  slug: open-firehydrant-change-events-api
- collection_type: open
  name: FireHydrant REST Audits Changes API
  slug: open-firehydrant-changes-api
- collection_type: open
  name: FireHydrant REST Audits Conversations API
  slug: open-firehydrant-conversations-api
- collection_type: open
  name: FireHydrant REST Audits Environments API
  slug: open-firehydrant-environments-api
- collection_type: open
  name: FireHydrant REST Audits Functionalities API
  slug: open-firehydrant-functionalities-api
- collection_type: open
  name: FireHydrant REST Audits Incidents API
  slug: open-firehydrant-incidents-api
- collection_type: open
  name: FireHydrant REST Audits Ping API
  slug: open-firehydrant-ping-api
- collection_type: open
  name: FireHydrant REST Audits Priorities API
  slug: open-firehydrant-priorities-api
- collection_type: open
  name: FireHydrant REST Audits Runbooks API
  slug: open-firehydrant-runbooks-api
- collection_type: open
  name: FireHydrant REST Audits Scheduled Maintenances API
  slug: open-firehydrant-scheduled-maintenances-api
- collection_type: open
  name: FireHydrant REST Audits Services API
  slug: open-firehydrant-services-api
- collection_type: open
  name: FireHydrant REST Audits Severities API
  slug: open-firehydrant-severities-api
- collection_type: open
  name: FireHydrant REST Audits Signals API
  slug: open-firehydrant-signals-api
- collection_type: open
  name: FireHydrant REST Audits Teams API
  slug: open-firehydrant-teams-api
- collection_type: open
  name: FireHydrant REST API
  slug: open-firehydrant
common:
- group: other
  href: https://artifacts.apis.io/firehydrant/capabilities/firehydrant-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/firehydrant-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/firehydrant/agentic-access/firehydrant-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/firehydrant-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/firehydrant/security/firehydrant-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/firehydrant-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/firehydrant/security/firehydrant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firehydrant-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/firehydrant/authentication/firehydrant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firehydrant-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firehydrant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firehydrant
- group: company
  title: ''
  type: Website
  url: https://firehydrant.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firehydrant.com
- group: company
  title: ''
  type: Blog
  url: https://firehydrant.com/rss.xml
- group: docs
  href: https://artifacts.apis.io/firehydrant/openapi/_original/firehydrant-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/firehydrant-api-openapi.yml
- group: other
  href: https://artifacts.apis.io/firehydrant/overlays/firehydrant-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/firehydrant-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.firehydrant.com/reference/firehydrant-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firehydrant.com/reference/firehydrant-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firehydrant.com/docs/admin-quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.firehydrant.com/docs/contacting-support
- group: commercial
  title: ''
  type: Pricing
  url: https://firehydrant.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.firehydrant.io/registrations/new/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firehydrant.com/legal/ssa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firehydrant.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firehydrant.com/
- group: design
  href: https://artifacts.apis.io/firehydrant/lifecycle/firehydrant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/firehydrant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://firehydrant.com/changelog/
- group: operate
  href: https://artifacts.apis.io/firehydrant/changelog/firehydrant-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/firehydrant-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://firehydrant.com/security/
- group: auth
  href: https://artifacts.apis.io/firehydrant/security/firehydrant-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/firehydrant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://firehydrant.com/security/
- group: design
  href: https://artifacts.apis.io/firehydrant/conformance/firehydrant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firehydrant-conformance.yml
- group: build
  href: https://artifacts.apis.io/firehydrant/packages/firehydrant-packages.yml
  title: ''
  type: Packages
  url: packages/firehydrant-packages.yml
- group: build
  href: https://artifacts.apis.io/firehydrant/packages/firehydrant-packages.yml
  title: ''
  type: SDKs
  url: packages/firehydrant-packages.yml
- group: build
  href: https://artifacts.apis.io/firehydrant/cli/firehydrant-cli.yml
  title: ''
  type: CLI
  url: cli/firehydrant-cli.yml
- group: agent
  href: https://artifacts.apis.io/firehydrant/mcp/firehydrant-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/firehydrant-mcp.yml
- group: build
  href: https://artifacts.apis.io/firehydrant/mcp/firehydrant-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/firehydrant-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/firehydrant/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/firehydrant/llms/firehydrant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firehydrant-llms.txt
- group: design
  href: https://artifacts.apis.io/firehydrant/asyncapi/firehydrant-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/firehydrant-webhooks.yml
- group: design
  href: https://artifacts.apis.io/firehydrant/conventions/firehydrant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/firehydrant-conventions.yml
- group: design
  href: https://artifacts.apis.io/firehydrant/errors/firehydrant-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/firehydrant-problem-types.yml
- group: design
  href: https://artifacts.apis.io/firehydrant/data-model/firehydrant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firehydrant-data-model.yml
- group: operate
  href: https://artifacts.apis.io/firehydrant/rate-limits/firehydrant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/firehydrant-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/firehydrant/plans/firehydrant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/firehydrant-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/firehydrant/finops/firehydrant-finops.yml
  title: ''
  type: FinOps
  url: finops/firehydrant-finops.yml
created: '2026-03-27'
description: FireHydrant is an incident management platform, now part of Freshworks, that covers the whole incident lifecycle — declaring and driving incidents from Slack or Microsoft Teams, Signals on-call scheduling and alerting, automated runbooks, a service catalog with environments and functionalities, its own hosted status pages, AI-enriched incident summaries, and retrospectives with analytics. Its REST API at api.firehydrant.io/v1 is a 373-operation, 228-path surface covering incidents, alerts, teams, runbooks, changes, integrations, webhooks and SCIM 2.0 provisioning, authenticated with a single organization API key sent as a Bearer token. FireHydrant also ships an official MCP server, first-party TypeScript and Go SDKs, a Terraform provider, and the fhcli change-event CLI.
finops:
- has_sources: true
  method: derived
  name: Firehydrant Finops
  primary_unit: responder
  service_category: ''
  slug: firehydrant-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firehydrant.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server requiring an API key; 5 tools listed.
  name: FireHydrant
  slug: firehydrant
modified: '2026-09-16'
name: FireHydrant
nav: Providers
network: true
overview: 'FireHydrant publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audits API, Change Events API, Changes API, and 25 more. Tagged areas include AIOps, Incident Management, On-Call, Alerting, and Status Pages.


  The FireHydrant catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  FireHydrant''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 35 more developer resources.'
plans:
- name: Firehydrant Plans Pricing
  plan_count: 3
  slug: firehydrant-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Firehydrant Rate Limits
  slug: firehydrant-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: FireHydrant API Rules
  rule_count: 58
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 16
  slug: firehydrant-rules
score:
  band: exemplar
  composite: 72.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 59.2
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 65.8
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 96.6
      derived: 0
      marker_coverage: 3.4
      total: 29
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/firehydrant/firehydrant-2026-06-20T181235.png
security:
- kind: authentication
  name: Firehydrant Authentication
  slug: firehydrant-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Firehydrant Domain Security
  slug: firehydrant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Firehydrant Vulnerability Disclosure
  slug: firehydrant-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Firehydrant Trust Center
  slug: firehydrant-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
skill_count: 5
skills:
- name: Declare and drive a FireHydrant incident
  slug: firehydrant-declare-and-drive-incident
- name: Record change events from CI into FireHydrant
  slug: firehydrant-record-change-events-from-ci
- name: Work a FireHydrant retrospective to publication
  slug: firehydrant-retrospective-workflow
- name: Provision FireHydrant users and teams over SCIM 2.0
  slug: firehydrant-scim-provisioning
- name: Triage FireHydrant Signals alerts and find who is on call
  slug: firehydrant-triage-alerts-and-oncall
slug: firehydrant
tags:
- AIOps
- Incident Management
- On-Call
- Alerting
- Status Pages
- Runbooks
- Site Reliability Engineering
- Observability
- Retrospectives
- DevOps
website: https://firehydrant.com
---
