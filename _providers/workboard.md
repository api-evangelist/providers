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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 12
  name: Workboard Agentic Access
  operation_count: 68
  slug: workboard-agentic-access
  summary_line: 68 operations · 35 acting · 12 human-in-the-loop
api_count: 2
apis:
- description: SCIM 2.0 provisioning API for organization users — create, read, update (title and manager), and disable. Groups, bulk operations, and filtering are not supported. Authenticated with an admin-requeste
  name: WorkBoard SCIM API
  slug: workboard-scim-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The Activity (Action Items) API from WorkBoard — 2 operation(s) for activity (action items).
  name: WorkBoard Activity (Action Items) API
  slug: workboard-activity-action-items-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: Read and write custom field values on Objectives, Key Results, Work Items, and Users
  name: WorkBoard Custom Attributes API
  slug: workboard-custom-attributes-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The Goal (Objective) API from WorkBoard — 5 operation(s) for goal (objective).
  name: WorkBoard Goal (Objective) API
  slug: workboard-goal-objective-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The Metric (Key Result) API from WorkBoard — 6 operation(s) for metric (key result).
  name: WorkBoard Metric (Key Result) API
  slug: workboard-metric-key-result-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The Tags API from WorkBoard — 4 operation(s) for tags.
  name: WorkBoard Tags API
  slug: workboard-tags-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The Team API from WorkBoard — 4 operation(s) for team.
  name: WorkBoard Team API
  slug: workboard-team-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The User API from WorkBoard — 2 operation(s) for user.
  name: WorkBoard User API
  slug: workboard-user-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The User Goals (User Objectives) API from WorkBoard — 2 operation(s) for user goals (user objectives).
  name: WorkBoard User Goals (User Objectives) API
  slug: workboard-user-goals-user-objectives-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: The Webhook API from WorkBoard — 1 operation(s) for webhook.
  name: WorkBoard Webhook API
  slug: workboard-webhook-api
- baseURL: https://www.myworkboard.com/wb/apis
  baseurl_source: declared
  description: '[WorkBoard''s help center documentation on Workstreams.](https://support.workboard.com/hc/en-us/articles/115005163567-Workstreams#workstreams-0-0)'
  name: WorkBoard Workstream API
  slug: workboard-workstream-api
- baseURL: https://myworkboard.com/wb/apis/scim
  baseurl_source: declared
  description: WorkBoard's help center documentation on Datastreams.
  name: WorkBoard Data Stream API
  slug: workboard-data-stream-api
artifact_total: 34
asyncapis:
- description: ''
  name: Workboard Webhooks
  slug: workboard-webhooks
collections:
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Activity (Action Items) API
  slug: open-workboard-activity-action-items-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) custom-attributes API
  slug: open-workboard-custom-attributes-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Datastream API
  slug: open-workboard-datastream-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Goal (Objective) API
  slug: open-workboard-goal-objective-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Metric (Key Result) API
  slug: open-workboard-metric-key-result-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Tags API
  slug: open-workboard-tags-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Team API
  slug: open-workboard-team-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) User API
  slug: open-workboard-user-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) User Goals (User Objectives) API
  slug: open-workboard-user-goals-user-objectives-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Webhook API
  slug: open-workboard-webhook-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Workstream API
  slug: open-workboard-workstream-api
common:
- group: other
  href: https://artifacts.apis.io/workboard/capabilities/workboard-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/workboard-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/workboard/overlays/workboard-external-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workboard-external-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/workboard/agentic-access/workboard-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workboard-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/workboard/security/workboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workboard-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/workboard/authentication/workboard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workboard-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.workboard.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.myworkboard.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.myworkboard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.workboard.com/developer
- group: operate
  title: ''
  type: Support
  url: https://support.myworkboard.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.workboard.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workboard
- group: start
  title: ''
  type: Login
  url: https://www.myworkboard.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workboard.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workboard.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://workboard.statuspage.io/
- group: design
  href: https://artifacts.apis.io/workboard/lifecycle/workboard-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workboard-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/workboard/changelog/workboard-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/workboard-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://www.myworkboard.com/wb/mcp
- group: agent
  href: https://artifacts.apis.io/workboard/mcp/workboard-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/workboard-mcp.yml
- group: agent
  href: https://artifacts.apis.io/workboard/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/workboard/llms/workboard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workboard-llms.txt
- group: build
  href: https://artifacts.apis.io/workboard/packages/workboard-packages.yml
  title: ''
  type: Packages
  url: packages/workboard-packages.yml
- group: agent
  href: https://artifacts.apis.io/workboard/well-known/workboard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workboard-well-known.yml
- group: design
  href: https://artifacts.apis.io/workboard/conformance/workboard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workboard-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.workboard.com/security
- group: auth
  href: https://artifacts.apis.io/workboard/security/workboard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/workboard-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/workboard/security/workboard-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/workboard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.workboard.com/security
- group: design
  href: https://artifacts.apis.io/workboard/errors/workboard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workboard-problem-types.yml
- group: design
  href: https://artifacts.apis.io/workboard/conventions/workboard-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workboard-conventions.yml
- group: design
  href: https://artifacts.apis.io/workboard/data-model/workboard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workboard-data-model.yml
- group: design
  href: https://artifacts.apis.io/workboard/asyncapi/workboard-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/workboard-webhooks.yml
created: '2026-07-17'
description: WorkBoard (WorkBoardAI) is an AI-native strategy, OKR, and strategic portfolio management platform used by enterprises like Cisco, AstraZeneca, and Mercedes-Benz to connect strategy pillars, outcomes, investments, and OKRs. Its External REST API (v1) exposes users, teams, goals (objectives), metrics (key results), action items, workstreams, and datastreams; the Public API v2 manages custom attributes; a SCIM 2.0 API handles user provisioning; and a published MCP server gives AI agents scoped access to OKRs, KPIs, scorecards, business reviews, and meetings.
image: https://img.cdn.myworkboard.com/wb/images/icons/login_logo.png
layout: provider
mcp_servers:
- description: ''
  name: WorkBoard MCP Server
  slug: workboard-mcp-server
modified: '2026-07-21'
name: WorkBoard
nav: Providers
network: true
overview: 'WorkBoard publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity (Action Items) API, Custom Attributes API, Goal (Objective) API, and 9 more. Tagged areas include OKRs, Strategy Execution, Goals, Key Results, and Enterprise.


  The WorkBoard catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WorkBoard''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 26 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: WorkBoard API Rules
  rule_count: 54
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 9
  slug: workboard-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 61.3
    developer_ergonomics: 42.3
    discoverability: 68.3
    operational_transparency: 52.6
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 90.9
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
screenshot: https://apis.io/screenshots/workboard/workboard-2026-08-17T082939.png
security:
- kind: authentication
  name: Workboard Authentication
  slug: workboard-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Workboard Domain Security
  slug: workboard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workboard Vulnerability Disclosure
  slug: workboard-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Workboard Trust Center
  slug: workboard-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, GDPR
skill_count: 3
skills:
- name: Manage custom attributes in WorkBoard
  slug: workboard-custom-attributes
- name: Update OKR progress in WorkBoard
  slug: workboard-okr-progress-update
- name: Build a team OKR report from WorkBoard
  slug: workboard-team-okr-report
slug: workboard
tags:
- OKRs
- Strategy Execution
- Goals
- Key Results
- Enterprise
- AI Agents
- Performance Management
- Strategic Portfolio Management
website: https://www.workboard.com/developer
---
