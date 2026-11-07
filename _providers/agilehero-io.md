---
access_model:
  confidence: medium
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Agilehero Io Agentic Access
  operation_count: 40
  slug: agilehero-io-agentic-access
  summary_line: 40 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.agilehero.io
  baseurl_source: declared
  description: The token owner, their workspaces and the workspace members.
  name: AgileHero Account API
  slug: agilehero-io-account-api
- baseURL: https://api.agilehero.io
  baseurl_source: declared
  description: Cards on a project's board, and their labels, assignees, relations, checklists and comments.
  name: AgileHero Cards API
  slug: agilehero-io-cards-api
- baseURL: https://api.agilehero.io
  baseurl_source: declared
  description: OAuth protected-resource metadata.
  name: AgileHero Discovery API
  slug: agilehero-io-discovery-api
- baseURL: https://api.agilehero.io
  baseurl_source: declared
  description: Projects, and the lists, labels and epics of a project.
  name: AgileHero Projects API
  slug: agilehero-io-projects-api
- baseURL: https://api.agilehero.io
  baseurl_source: declared
  description: Outbound webhook endpoints (REST Hooks subscribe, unsubscribe, list and sample). Workspace owners and admins only.
  name: AgileHero Webhooks API
  slug: agilehero-io-webhooks-api
artifact_total: 21
common:
- group: docs
  title: ''
  type: Documentation
  url: https://agilehero.io/docs/mcp/
- group: agent
  href: https://artifacts.apis.io/agilehero-io/agentic-access/agilehero-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agilehero-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agilehero-io/plans/agilehero-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agilehero-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agilehero-io/rules/agilehero-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agilehero-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agilehero-io/json-ld/agilehero-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agilehero-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/agilehero-io/vocabulary/agilehero-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agilehero-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agilehero-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agilehero-io/data-model/agilehero-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agilehero-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agilehero-io/changelog/agilehero-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agilehero-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/agilehero-io/conventions/agilehero-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agilehero-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agilehero-io/authentication/agilehero-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agilehero-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/agilehero-io/errors/agilehero-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agilehero-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agilehero-io/conformance/agilehero-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agilehero-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agilehero-io/llms/agilehero-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agilehero-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/agilehero-io/well-known/agilehero-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agilehero-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/agilehero-io/hosts/agilehero-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agilehero-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/agilehero-io/vendors/agilehero-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agilehero-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://agilehero.io/sign-up/
- group: operate
  title: ''
  type: Roadmap
  url: https://agilehero.io/features/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agilehero.io/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agilehero-io
- group: operate
  title: ''
  type: ChangeLog
  url: https://agilehero.io/changelog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.agilehero.io</code
- group: docs
  title: ''
  type: APIReference
  url: https://agilehero.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/agilehero-io/scopes/agilehero-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agilehero-io-scopes.yml
- group: auth
  href: https://artifacts.apis.io/agilehero-io/security/agilehero-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agilehero-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agilehero.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://agilehero.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agilehero.io/terms/
created: '2026-11-01'
description: AgileHero provides an all‑in‑one agile project management tool for teams and AI agents, featuring kanban boards, backlogs, roadmaps, whiteboards, retrospectives, wikis and metrics. The platform offers a free starter tier with no credit‑card required, and integrates with popular services. It aims to streamline workflow, improve visibility, and support AI‑enhanced planning across the software development lifecycle.
image: https://agilehero.io/og/home.png
json_schemas:
- name: CardCreate
  property_count: 10
  slug: agilehero-io-card-create
- name: Card
  property_count: 15
  slug: agilehero-io-card
- name: CardUpdate
  property_count: 8
  slug: agilehero-io-card-update
- name: Comment
  property_count: 9
  slug: agilehero-io-comment
- name: WebhookEndpoint
  property_count: 10
  slug: agilehero-io-webhook-endpoint
- name: WebhookEvent
  property_count: 9
  slug: agilehero-io-webhook-event
jsonld:
- class_count: 28
  name: Agilehero Io Context
  property_count: 62
  slug: agilehero-io-context
layout: provider
modified: '2026-11-01'
name: AgileHero
nav: Providers
network: true
overview: 'AgileHero publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Cards API, Discovery API, and 2 more. Tagged areas include Company, Project Management, Agile, AI Integration, and Collaboration.


  The AgileHero catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgileHero''s developer surface includes documentation, changelog, authentication, signup flow, API reference, pricing, and 23 more developer resources.'
plans:
- name: Agilehero Io Plans Pricing
  plan_count: 2
  slug: agilehero-io-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AgileHero API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: agilehero-io-rules
scopes:
- name: Agilehero Io Scopes
  scope_count: 2
  slug: agilehero-io-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 59.9
    developer_ergonomics: 26.8
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agilehero Io Authentication
  slug: agilehero-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agilehero Io Domain Security
  slug: agilehero-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: agilehero-io-create-card-with-label-and-assignee
  slug: agilehero-io-create-card-with-label-and-assignee
- name: agilehero-io-manage-project-lists
  slug: agilehero-io-manage-project-lists
- name: agilehero-io-manage-webhook-endpoints
  slug: agilehero-io-manage-webhook-endpoints
slug: agilehero-io
tags:
- Company
- Project Management
- Agile
- AI Integration
- Collaboration
website: https://agilehero.io/
---
