---
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
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Recal Agentic Access
  operation_count: 38
  slug: recal-agentic-access
  summary_line: 38 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: The Organization API from Recal — 3 operation(s) for organization.
  name: Recal Organization API
  slug: recal-organization-api
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: Routes for the Organization Scheduling
  name: Recal Organization Scheduling API
  slug: recal-organization-scheduling-api
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: The Organizations Calendar API from Recal — 1 operation(s) for organizations calendar.
  name: Recal Organizations Calendar API
  slug: recal-organizations-calendar-api
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: Routes for the User Calendar
  name: Recal User Calendar API
  slug: recal-user-calendar-api
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: Routes for the User OAuth
  name: Recal User OAuth API
  slug: recal-user-oauth-api
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: Routes for the User Scheduling
  name: Recal User Scheduling API
  slug: recal-user-scheduling-api
- baseURL: https://api.recal.dev
  baseurl_source: declared
  description: Routes for the Users
  name: Recal Users API
  slug: recal-users-api
artifact_total: 23
asyncapis:
- description: ''
  name: Recal Webhooks
  slug: recal-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/recal/agentic-access/recal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recal-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/recal/rules/recal-rules.yml
  title: ''
  type: Spectral
  url: rules/recal-rules.yml
- group: design
  href: https://artifacts.apis.io/recal/json-ld/recal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/recal-context.jsonld
- group: design
  href: https://artifacts.apis.io/recal/vocabulary/recal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/recal-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/recal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/recal/asyncapi/recal-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/recal-webhooks.yml
- group: design
  href: https://artifacts.apis.io/recal/data-model/recal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/recal-data-model.yml
- group: auth
  href: https://artifacts.apis.io/recal/authentication/recal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recal-authentication.yml
- group: design
  href: https://artifacts.apis.io/recal/errors/recal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/recal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/recal/conformance/recal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recal-conformance.yml
- group: other
  href: https://artifacts.apis.io/recal/overlays/recal-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/recal-openapi-overlay.yml
- group: auth
  href: https://artifacts.apis.io/recal/well-known/recal-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recal-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/recal/well-known/recal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recal-well-known.yml
- group: other
  href: https://artifacts.apis.io/recal/hosts/recal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recal-hosts.yml
- group: other
  href: https://artifacts.apis.io/recal/vendors/recal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recal-vendors.yml
- group: build
  href: https://artifacts.apis.io/recal/packages/recal-packages.yml
  title: ''
  type: SDKs
  url: packages/recal-packages.yml
- group: build
  href: https://artifacts.apis.io/recal/packages/recal-packages.yml
  title: ''
  type: Packages
  url: packages/recal-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recal.dev/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recal.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: http://github.com/recal-dev/
- group: company
  title: ''
  type: Blog
  url: https://recal.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.recal.dev/core/oauth/setup-prompt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recal.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://api.recal.dev/v1/swagger
- group: auth
  href: https://artifacts.apis.io/recal/security/recal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://recal.dev/
created: '2026-10-18'
description: Recal provides a unified Calendar & Scheduling Integration API and SDK that lets developers connect to Google Calendar, Microsoft Outlook, and other calendar services through a single API, eliminating provider‑specific code. The platform offers REST endpoints, SDKs, and a developer dashboard for managing integrations, OAuth flows, and scheduling features.
image: https://framerusercontent.com/images/z5OtQokcjGqQ9XkYSVX3HxjSLg.png
json_schemas:
- name: CreateEvent
  property_count: 10
  slug: recal-create-event
- name: CreateMetaEvent
  property_count: 9
  slug: recal-create-meta-event
- name: Event
  property_count: 10
  slug: recal-event
- name: MetaEvent
  property_count: 8
  slug: recal-meta-event
- name: UpdateEvent
  property_count: 10
  slug: recal-update-event
- name: UpdateMetaEvent
  property_count: 9
  slug: recal-update-meta-event
jsonld:
- class_count: 14
  name: Recal Context
  property_count: 36
  slug: recal-context
layout: provider
modified: '2026-10-18'
name: Recal
nav: Providers
network: true
overview: 'Recal publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Organization API, Organization Scheduling API, Organizations Calendar API, and 4 more. Tagged areas include Calendar API, Scheduling, SDK, Multi-Tenant, and Recruiting.


  The Recal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Recal''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 21 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Recal API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: recal-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 72.4
    developer_ergonomics: 51.8
    discoverability: 66.1
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Recal Authentication
  slug: recal-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Recal Domain Security
  slug: recal-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: recal-create-organization-with-members
  slug: recal-create-organization-with-members
- name: recal-user-calendar-manage-event
  slug: recal-user-calendar-manage-event
- name: recal-user-scheduling
  slug: recal-user-scheduling
- name: recal-verify-and-get-token
  slug: recal-verify-and-get-token
slug: recal
tags:
- Calendar API
- Scheduling
- SDK
- Multi-Tenant
- Recruiting
- Marketplace
- AI Agents
website: https://recal.dev/
---
