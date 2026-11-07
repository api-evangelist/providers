---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 143
  human_in_the_loop: 1
  name: Buildworkpro Com Agentic Access
  operation_count: 221
  slug: buildworkpro-com-agentic-access
  summary_line: 221 operations · 143 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Estimates and proposals, including line items, sublines, distributed costs, templates and sending.
  name: BuildWorkPro Bids API
  slug: buildworkpro-com-bids-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Per-user Dismiss / Snooze of rows on the "Needs you today" morning briefing.
  name: BuildWorkPro Briefing API
  slug: buildworkpro-com-briefing-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Scheduled events derived from project phases, tasks and bid deadlines.
  name: BuildWorkPro Calendar API
  slug: buildworkpro-com-calendar-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Discussion threads attached to records. Visibility follows the record commented on.
  name: BuildWorkPro Comments API
  slug: buildworkpro-com-comments-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Customers, vendors and subcontractors, with their addresses, notes and tags.
  name: BuildWorkPro Contacts API
  slug: buildworkpro-com-contacts-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Daily crew assignments of tenant users to jobs (the dispatch board).
  name: BuildWorkPro Crew Assignments API
  slug: buildworkpro-com-crewassignments-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: File attachments on any entity, with versioning and signed upload/download URLs.
  name: BuildWorkPro Documents API
  slug: buildworkpro-com-documents-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: 'Accounts receivable: invoices, line items, payments, sending and voiding.'
  name: BuildWorkPro Invoices API
  slug: buildworkpro-com-invoices-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Asynchronous work — CSV imports and exports — with progress and result artifacts.
  name: BuildWorkPro Jobs API
  slug: buildworkpro-com-jobs-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Sales pipeline records and their movement through stages.
  name: BuildWorkPro Leads API
  slug: buildworkpro-com-leads-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: In-app notifications for the user who owns the API key.
  name: BuildWorkPro Notifications API
  slug: buildworkpro-com-notifications-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: OAuth 2.1 authorization, token exchange and dynamic client registration.
  name: BuildWorkPro OAuth API
  slug: buildworkpro-com-oauth-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: API audit logs and usage metering for the authenticated organization.
  name: BuildWorkPro Observability API
  slug: buildworkpro-com-observability-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: 'AIA-style payment applications: schedule of values, retainage and approval.'
  name: BuildWorkPro Pay Apps API
  slug: buildworkpro-com-payapps-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: The catalog of materials and labor items bids are built from, including kits.
  name: BuildWorkPro Products API
  slug: buildworkpro-com-products-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: 'Awarded work: phases, tasks, subtasks, dependencies and assigned contacts.'
  name: BuildWorkPro Projects API
  slug: buildworkpro-com-projects-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Reports v2 — the business review and the report catalog (AR aging, billed vs collected, bid performance, pipeline, WIP).
  name: BuildWorkPro Reports API
  slug: buildworkpro-com-reports-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: One ranked search across records, limited to the types and rows the credential may read.
  name: BuildWorkPro Search API
  slug: buildworkpro-com-search-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Organization-level configuration and branding.
  name: BuildWorkPro Settings API
  slug: buildworkpro-com-settings-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: E-signature requests raised against bids and change orders.
  name: BuildWorkPro Signature Requests API
  slug: buildworkpro-com-signaturerequests-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Daily field reports, photos and their review state.
  name: BuildWorkPro Site Logs API
  slug: buildworkpro-com-sitelogs-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Team members within the authenticated organization.
  name: BuildWorkPro Users API
  slug: buildworkpro-com-users-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Outbound webhook endpoints and their delivery history.
  name: BuildWorkPro Webhooks API
  slug: buildworkpro-com-webhooks-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Scope changes against a project, with approval workflow and line items.
  name: BuildWorkPro Change Orders API
  slug: buildworkpro-com-change-orders-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Reusable phase and task structures applied when a bid becomes a project.
  name: BuildWorkPro Project Templates API
  slug: buildworkpro-com-project-templates-api
- baseURL: https://app.buildworkpro.com/api/v1
  baseurl_source: declared
  description: Labor hours logged against projects, with review and cost roll-up.
  name: BuildWorkPro Time Entries API
  slug: buildworkpro-com-time-entries-api
artifact_total: 47
asyncapis:
- description: ''
  name: Buildworkpro Com Webhooks
  slug: buildworkpro-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/buildworkpro-com/agentic-access/buildworkpro-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buildworkpro-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/buildworkpro-com/rate-limits/buildworkpro-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/buildworkpro-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/buildworkpro-com/plans/buildworkpro-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildworkpro-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/rules/buildworkpro-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buildworkpro-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/json-ld/buildworkpro-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildworkpro-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/vocabulary/buildworkpro-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildworkpro-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/buildworkpro-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/asyncapi/buildworkpro-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/buildworkpro-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/data-model/buildworkpro-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildworkpro-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/buildworkpro-com/changelog/buildworkpro-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/buildworkpro-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/conventions/buildworkpro-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/buildworkpro-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/conventions/buildworkpro-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/buildworkpro-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/buildworkpro-com/authentication/buildworkpro-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildworkpro-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/errors/buildworkpro-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildworkpro-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buildworkpro-com/conformance/buildworkpro-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildworkpro-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buildworkpro-com/llms/buildworkpro-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildworkpro-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/buildworkpro-com/well-known/buildworkpro-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buildworkpro-com-security.txt
- group: agent
  href: https://artifacts.apis.io/buildworkpro-com/well-known/buildworkpro-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildworkpro-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildworkpro-com/hosts/buildworkpro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildworkpro-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildworkpro-com/vendors/buildworkpro-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildworkpro-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://buildworkpro.com/api/webhooks/overview/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildworkpro.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://buildworkpro.com/support/
- group: auth
  title: ''
  type: Security
  url: https://buildworkpro.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildworkpro.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://buildworkpro.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://buildworkpro.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://buildworkpro.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://buildworkpro.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://buildworkpro.com/api/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://buildworkpro.com/api/changelog/
- group: auth
  href: https://artifacts.apis.io/buildworkpro-com/security/buildworkpro-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildworkpro-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buildworkpro-com/security/buildworkpro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildworkpro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildworkpro.com/
created: '2026-11-03'
description: BuildWorkPro provides construction project management software tailored for subcontractors and small businesses. Its platform offers tools for bidding, pay applications, change orders, project tracking, and crew management, all at a flat rate of $79 per month with a 14‑day free trial. The solution aims to streamline field operations, improve financial visibility, and enhance collaboration across construction teams.
image: https://buildworkpro.com/og-image.png
json_schemas:
- name: BidLineItem
  property_count: 14
  slug: buildworkpro-com-bid-line-item
- name: Bid
  property_count: 31
  slug: buildworkpro-com-bid
- name: CreateProject
  property_count: 21
  slug: buildworkpro-com-create-project
- name: PayApp
  property_count: 20
  slug: buildworkpro-com-pay-app
- name: Project
  property_count: 25
  slug: buildworkpro-com-project
- name: UpdateProject
  property_count: 21
  slug: buildworkpro-com-update-project
jsonld:
- class_count: 64
  name: Buildworkpro Com Context
  property_count: 282
  slug: buildworkpro-com-context
layout: provider
modified: '2026-11-03'
name: BuildWorkPro
nav: Providers
network: true
overview: 'BuildWorkPro publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bids API, Briefing API, Calendar API, and 23 more. Tagged areas include Construction, Project Management, Subcontractors, Software-as-a-Service, and Construction Software.


  The BuildWorkPro catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BuildWorkPro''s developer surface includes changelog, authentication, support, pricing, documentation, engineering blog, getting-started guide, and 27 more developer resources.'
plans:
- name: Buildworkpro Com Plans Pricing
  plan_count: 1
  slug: buildworkpro-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Buildworkpro Com Rate Limits
  slug: buildworkpro-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: BuildWorkPro API Rules
  rule_count: 70
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 16
  slug: buildworkpro-com-rules
scopes:
- name: Buildworkpro Com Scopes
  scope_count: 0
  slug: buildworkpro-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 68.8
    developer_ergonomics: 36.3
    discoverability: 66.1
    operational_transparency: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buildworkpro Com Authentication
  slug: buildworkpro-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Buildworkpro Com Domain Security
  slug: buildworkpro-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Buildworkpro Com Vulnerability Disclosure
  slug: buildworkpro-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: buildworkpro-com-create-and-manage-webhook
  slug: buildworkpro-com-create-and-manage-webhook
- name: buildworkpro-com-create-and-send-invoice
  slug: buildworkpro-com-create-and-send-invoice
- name: buildworkpro-com-create-contact
  slug: buildworkpro-com-create-contact
- name: buildworkpro-com-payapps-submit-and-approve
  slug: buildworkpro-com-payapps-submit-and-approve
- name: buildworkpro-com-project-management
  slug: buildworkpro-com-project-management
slug: buildworkpro-com
tags:
- Construction
- Project Management
- Subcontractors
- Software-as-a-Service
- Construction Software
website: https://buildworkpro.com/
---
