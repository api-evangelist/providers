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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Unify Agentic Access
  operation_count: 68
  slug: unify-agentic-access
  summary_line: 68 operations · 37 acting
api_count: 4
apis:
- baseURL: https://api.unifyintent.com/analytics/v1
  baseurl_source: declared
  description: Server-side event collection for the Unify Analytics API - identify, page and track events posted from a website or product with a public write key over HTTP Basic. 3 operation(s).
  name: Unify Analytics Events API
  phrasing_intents:
  - id: send_identify_event
    intent: Identify a website visitor
    question: How do I tell Unify who an anonymous website visitor actually is?
  - id: send_page_event
    intent: Record a page view
    question: How do I log that a visitor viewed a page on my site?
  - id: send_track_event
    intent: Track a custom product event
    question: How do I record a custom action like a signup or a button click?
  phrasing_ops: 3
  slug: unify-events-api
- baseURL: https://api.unifygtm.com/sequences/v1
  baseurl_source: declared
  description: List, retrieve, pause, resume and delete Unify outbound sequences and read their ordered steps. 7 operation(s).
  name: Unify Sequences API
  phrasing_intents:
  - id: create_sequence_enrollment_step_query_job
    intent: Start a bulk export of sequence step activity
    question: How do I export email opens and replies for every step each person went through in my sequences?
  - id: list_sequence_enrollment_step_query_jobs
    intent: List enrollment step export jobs
    question: Which per-step sequence activity exports have I started?
  - id: get_sequence_enrollment_step_query_job
    intent: Check the status of an enrollment step export
    question: Is my sequence step activity export finished yet?
  - id: cancel_sequence_enrollment_step_query_job
    intent: Cancel a running enrollment step export
    question: Can I stop a sequence step activity export that is still running?
  - id: get_sequence_enrollment_step_query_job_results
    intent: Download results of an enrollment step export
    question: How do I page through the per-step email engagement rows from a finished export?
  - id: create_sequence_enrollment
    intent: Enroll a person in a sequence
    question: How do I add a prospect to an outreach sequence?
  - id: list_sequence_enrollments
    intent: List sequence enrollments
    question: Who is currently enrolled in a given sequence and how far along are they?
  - id: create_sequence_enrollment_query_job
    intent: Start a bulk export of sequence enrollments
    question: How do I export thousands of sequence enrollments at once?
  phrasing_ops: 23
  slug: unify-sequences-api
- baseURL: https://api.unifygtm.com/tasks/v1
  baseurl_source: declared
  description: Create, read, update, complete, delete, list and bulk-export the outreach tasks - emails, calls, LinkedIn touches and manual action items - assigned to Unify users against a person. 11 operation(s).
  name: Unify Tasks API
  phrasing_intents:
  - id: list_tasks
    intent: List outreach tasks
    question: What outreach tasks are assigned to a particular rep?
  - id: create_task
    intent: Create an outreach task for a person
    question: How do I create a call or LinkedIn task for a prospect?
  - id: create_task_query_job
    intent: Start a bulk export of tasks
    question: How do I export every task in bulk instead of paging the task list?
  - id: list_task_query_jobs
    intent: List task export jobs
    question: Which bulk task export jobs have I started?
  - id: get_task_query_job
    intent: Check the status of a task export job
    question: Has my task export job finished?
  - id: cancel_task_query_job
    intent: Cancel a running task export job
    question: Can I stop a task export that is still in progress?
  - id: get_task_query_job_results
    intent: Download results of a task export job
    question: How do I page through the tasks a finished export returned?
  - id: retrieve_task
    intent: Get a task by its ID
    question: How do I look up the details of one specific task?
  phrasing_ops: 11
  slug: unify-tasks-api
- baseURL: https://api.unifyintent.com/analytics/v1
  baseurl_source: declared
  description: The Data API from Unify — 18 operation(s) for data.
  name: Unify Data API
  phrasing_intents:
  - id: create_event_query_job
    intent: Start a bulk export of analytics events
    question: How do I export all my website page, track and identify events from Unify in bulk?
  - id: list_event_query_jobs
    intent: List analytics event export jobs
    question: Which analytics event export jobs have I started recently?
  - id: get_event_query_job
    intent: Check the status of an event export job
    question: Has my analytics event export job finished yet?
  - id: cancel_event_query_job
    intent: Cancel a running event export job
    question: Can I stop an analytics event export that is still running?
  - id: get_event_query_job_results
    intent: Download results of an event export job
    question: How do I page through the rows of a finished analytics event export?
  - id: list_objects
    intent: List the objects in a workspace
    question: What standard and custom objects exist in my Unify workspace?
  - id: create_object
    intent: Create a custom object
    question: How do I add a custom object to store a new kind of record?
  - id: get_object
    intent: Get an object definition
    question: What does the definition of one of my workspace objects look like?
  phrasing_ops: 31
  slug: unify-data-api
artifact_total: 35
asyncapis:
- description: ''
  name: Unify Webhooks
  slug: unify-webhooks
collections:
- collection_type: open
  name: Unify Data Event Query Jobs API
  slug: open-unify-event-query-jobs-api
- collection_type: open
  name: Unify Analytics Events API
  slug: open-unify-events-api
- collection_type: open
  name: Unify Data Object Attribute Options API
  slug: open-unify-object-attribute-options-api
- collection_type: open
  name: Unify Data Object Attributes API
  slug: open-unify-object-attributes-api
- collection_type: open
  name: Unify Data Object Record Query Jobs API
  slug: open-unify-object-record-query-jobs-api
- collection_type: open
  name: Unify Data Object Records API
  slug: open-unify-object-records-api
- collection_type: open
  name: Unify Data Objects API
  slug: open-unify-objects-api
- collection_type: open
  name: Unify Sequences Sequence Enrollment Steps API
  slug: open-unify-sequence-enrollment-steps-api
- collection_type: open
  name: Unify Sequences Sequence Enrollments API
  slug: open-unify-sequence-enrollments-api
- collection_type: open
  name: Unify Sequences API
  slug: open-unify-sequences-api
- collection_type: open
  name: Unify Tasks API
  slug: open-unify-tasks-api
common:
- group: other
  href: https://artifacts.apis.io/unify/overlays/unify-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unify-analytics-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/unify/agentic-access/unify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unify-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/unify/security/unify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/unify-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/unify/security/unify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unify-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/unify/authentication/unify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unify-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unifygtm.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.unifygtm.com/developers/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unifygtm.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unifygtm.com/developers/api/data/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unifygtm.com/getting-started/setup-guide
- group: company
  title: ''
  type: Blog
  url: https://www.unifygtm.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unifygtm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unifygtm.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.unifygtm.com/?screen_hint=signup
- group: start
  title: ''
  type: Login
  url: https://auth.unifygtm.com/u/login/identifier
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unifygtm.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unifygtm.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.unifygtm.com/
- group: operate
  href: https://artifacts.apis.io/unify/changelog/unify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/unify-changelog.yml
- group: agent
  href: https://artifacts.apis.io/unify/llms/unify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unify-llms.txt
- group: agent
  href: https://artifacts.apis.io/unify/mcp/unify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unify-mcp.yml
- group: agent
  href: https://artifacts.apis.io/unify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/unify/packages/unify-packages.yml
  title: ''
  type: Packages
  url: packages/unify-packages.yml
- group: build
  href: https://artifacts.apis.io/unify/packages/unify-packages.yml
  title: ''
  type: SDKs
  url: packages/unify-packages.yml
- group: design
  href: https://artifacts.apis.io/unify/conformance/unify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unify-conformance.yml
- group: design
  href: https://artifacts.apis.io/unify/errors/unify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unify/lifecycle/unify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/unify/conventions/unify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unify-conventions.yml
- group: design
  href: https://artifacts.apis.io/unify/data-model/unify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unify-data-model.yml
- group: design
  href: https://artifacts.apis.io/unify/asyncapi/unify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/unify-webhooks.yml
- group: company
  title: ''
  type: XTwitter
  url: https://twitter.com/unifygtm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unifygtm/
- group: other
  href: https://artifacts.apis.io/unify/a2a/unify-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/unify-a2a.yml
- group: agent
  href: https://artifacts.apis.io/unify/well-known/unify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unify-well-known.yml
- group: auth
  href: https://artifacts.apis.io/unify/scopes/unify-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/unify-scopes.yml
- group: build
  href: https://artifacts.apis.io/unify/mcp/unify-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/unify-tool-crosswalk.yml
- group: commercial
  href: https://artifacts.apis.io/unify/plans/unify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/unify/rate-limits/unify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/unify-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/unify/components/unify-components.yml
  title: ''
  type: Components
  url: components/unify-components.yml
- group: other
  href: https://artifacts.apis.io/unify/overlays/unify-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unify-data-overlay.yaml
- group: other
  href: https://artifacts.apis.io/unify/overlays/unify-sequences-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unify-sequences-overlay.yaml
- group: other
  href: https://artifacts.apis.io/unify/overlays/unify-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unify-tasks-overlay.yaml
- group: operate
  title: ''
  type: Support
  url: mailto:support@unifygtm.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.unifygtm.com/changelog
created: '2026-07-17'
description: Unify is a B2B outbound and go-to-market platform that pairs AI agents with reps to find buyers already in market and reach them with the right message, combining 40+ data sources, 1.1B+ contacts and 65M+ companies with intent signals, automated Plays and multi-channel sequences. Founded in 2023 and backed by $52M+ from the OpenAI Startup Fund, Thrive Capital, Battery Ventures and Emergence Capital, Unify publishes four anonymous OpenAPI 3.0 documents covering 68 operations across Data, Sequences, Tasks and Analytics, official Python and TypeScript SDKs, browser intent clients, a hosted OAuth-protected MCP server exposing 71 tools, provider-published agent skills, and an A2A agent card.
finops:
- has_sources: true
  method: derived
  name: Unify Finops
  primary_unit: seat
  service_category: ''
  slug: unify-finops
  template: false
image: https://raw.githubusercontent.com/unifygtm/agent-plugins/main/unify/assets/unify-logo-light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.unifygtm.com.
  name: Unify MCP Server
  slug: unify-mcp-yml
modified: '2026-08-13'
name: Unify
nav: Providers
network: true
overview: 'Unify publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics Events API, Sequences API, Tasks API, and 1 more. Tagged areas include Sales, Marketing, Go-To-Market, Outbound, and Intent Data.


  The Unify catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Unify''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Unify Plans Pricing
  plan_count: 5
  slug: unify-plans-pricing
- name: Unify Price Estimates
  plan_count: 0
  slug: unify-price-estimates
random_paper: 3
rate_limits:
- limit_count: 7
  name: Unify Rate Limits
  slug: unify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Unify API Rules
  rule_count: 68
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 8
  slug: unify-rules
scopes:
- name: Unify Scopes
  scope_count: 14
  slug: unify-scopes
  summary_line: 14 scopes · authorizationCode/deviceCode/clientCredentials/refreshToken/tokenExchange/implicit
score:
  band: exemplar
  composite: 74.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 63.1
    developer_ergonomics: 71.4
    discoverability: 80.0
    operational_transparency: 57.9
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/unify/unify-2026-08-17T080432.png
security:
- kind: authentication
  name: Unify Authentication
  slug: unify-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Unify Domain Security
  slug: unify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unify Trust Center
  slug: unify-trust-center
  summary_line: SOC 2
skill_count: 8
skills:
- name: agent-runs
  slug: unify-agent-runs-skill
- name: crm
  slug: unify-crm-skill
- name: data-tables
  slug: unify-data-tables-skill
- name: discovery
  slug: unify-discovery-skill
- name: Unify
  slug: unify-docs-agent-skill
- name: enrichment
  slug: unify-enrichment-skill
- name: outreach
  slug: unify-outreach-skill
- name: unify
  slug: unify-unify-skill
slug: unify
tags:
- Sales
- Marketing
- Go-To-Market
- Outbound
- Intent Data
- AI Agents
- B2B
- Data Enrichment
- Sequences
- Analytics
- Task
- Bulk API
- MCP
- Agent Skills
- Webhook
- A2A
website: https://www.unifygtm.com
---
