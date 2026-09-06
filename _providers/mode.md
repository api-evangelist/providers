---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Mode Agentic Access
  operation_count: 94
  slug: mode-agentic-access
  summary_line: 94 operations · 45 acting
api_count: 1
apis:
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Account API from Mode — 1 operation(s) for account.
  name: Mode Account API
  slug: mode-account-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Audit Logs API from Mode — 1 operation(s) for audit logs.
  name: Mode Audit Logs API
  slug: mode-audit-logs-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Data Sources API from Mode — 6 operation(s) for data sources.
  name: Mode Data Sources API
  slug: mode-data-sources-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Datasets API from Mode — 8 operation(s) for datasets.
  name: Mode Datasets API
  slug: mode-datasets-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Definitions API from Mode — 2 operation(s) for definitions.
  name: Mode Definitions API
  slug: mode-definitions-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Groups API from Mode — 4 operation(s) for groups.
  name: Mode Groups API
  slug: mode-groups-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Invites API from Mode — 1 operation(s) for invites.
  name: Mode Invites API
  slug: mode-invites-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Memberships API from Mode — 2 operation(s) for memberships.
  name: Mode Memberships API
  slug: mode-memberships-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Reports API from Mode — 27 operation(s) for reports.
  name: Mode Reports API
  slug: mode-reports-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Spaces API from Mode — 6 operation(s) for spaces.
  name: Mode Spaces API
  slug: mode-spaces-api
- baseURL: https://app.mode.com/api
  baseurl_source: declared
  description: The Verify API from Mode — 1 operation(s) for verify.
  name: Mode Verify API
  slug: mode-verify-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mode Account API
  slug: open-mode-account-api
- collection_type: open
  name: Mode Account Audit Logs API
  slug: open-mode-audit-logs-api
- collection_type: open
  name: Mode Account Data Sources API
  slug: open-mode-data-sources-api
- collection_type: open
  name: Mode Account Datasets API
  slug: open-mode-datasets-api
- collection_type: open
  name: Mode Account Definitions API
  slug: open-mode-definitions-api
- collection_type: open
  name: Mode Account Groups API
  slug: open-mode-groups-api
- collection_type: open
  name: Mode Account Invites API
  slug: open-mode-invites-api
- collection_type: open
  name: Mode Account Memberships API
  slug: open-mode-memberships-api
- collection_type: open
  name: Mode Account Reports API
  slug: open-mode-reports-api
- collection_type: open
  name: Mode Account Spaces API
  slug: open-mode-spaces-api
- collection_type: open
  name: Mode Account Verify API
  slug: open-mode-verify-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/thoughtspot/
- group: other
  title: ''
  type: Overlay
  url: overlays/mode-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mode.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mode.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://mode.com/developer/api-reference/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://mode.com/developer/api-reference/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://mode.com/developer/api-reference/introduction/
- group: operate
  title: ''
  type: Support
  url: https://mode.com/help/
- group: company
  title: ''
  type: Blog
  url: https://mode.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mode
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modeanalytics.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mode.com/compare-plans/
- group: start
  title: ''
  type: Login
  url: https://app.mode.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mode.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mode.com/legal/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mode-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mode-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mode-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mode-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mode-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mode-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mode-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mode-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mode-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mode-domain-security.yml
created: '2026-07-17'
description: Mode is a collaborative business intelligence and analytics platform that unites data and business teams around a single analytical workflow. Built by analysts for analysts, Mode combines ad hoc SQL exploration, Python and R notebooks, interactive dashboards, self-serve reporting, and custom data applications on top of connected data warehouses. Mode was acquired by ThoughtSpot in 2023 and positions itself as the intelligence layer for the modern data stack. Mode exposes a REST API (documented at its Developer Hub) for programmatic management of workspaces, users, collections, data sources, reports, queries, charts, datasets, definitions, exports, report schedules, and subscriptions. The API uses HTTP Basic authentication with workspace or personal API tokens and returns HAL+JSON, and is available to workspaces on a paid Mode Business plan.
image: https://avatars.githubusercontent.com/u/5306870?v=4
layout: provider
modified: '2026-07-20'
name: Mode
nav: Providers
network: true
overview: 'Mode publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Audit Logs API, Data Sources API, and 8 more. Tagged areas include Company, Enterprise, Business Intelligence, Analytics, and Data.


  Mode''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 19 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mode/refs/heads/main/screenshots/mode-2026-08-07T183917.png
security:
- kind: authentication
  name: Mode Authentication
  slug: mode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mode Domain Security
  slug: mode-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mode
tags:
- Company
- Enterprise
- Business Intelligence
- Analytics
- Data
- Reporting
- Dashboards
- SQL
- Data Stack
website: https://mode.com
---
