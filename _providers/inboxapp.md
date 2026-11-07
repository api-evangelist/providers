---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Inboxapp provides a shared inbox and CRM platform with a developer API documented on the Mintlify site.
  name: Inboxapp API
  slug: inboxapp-api-2
- baseURL: https://inboxapp.com
  baseurl_source: declared
  description: 'Inboxapp API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Inboxapp API
  slug: inboxapp-api
artifact_total: 14
asyncapis:
- description: ''
  name: Inboxapp Webhooks
  slug: inboxapp-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/inboxapp/plans/inboxapp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inboxapp-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/rules/inboxapp-rules.yml
  title: ''
  type: Spectral
  url: rules/inboxapp-rules.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/json-ld/inboxapp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/inboxapp-context.jsonld
- group: design
  href: https://artifacts.apis.io/inboxapp/vocabulary/inboxapp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inboxapp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/asyncapi/inboxapp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/inboxapp-webhooks.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/data-model/inboxapp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inboxapp-data-model.yml
- group: operate
  href: https://artifacts.apis.io/inboxapp/changelog/inboxapp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/inboxapp-changelog.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/conventions/inboxapp-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/inboxapp-conventions.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/conventions/inboxapp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/inboxapp-conventions.yml
- group: operate
  href: https://artifacts.apis.io/inboxapp/lifecycle/inboxapp-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/inboxapp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/lifecycle/inboxapp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/inboxapp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inboxapp/conformance/inboxapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inboxapp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/inboxapp/llms/inboxapp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inboxapp-llms.txt
- group: other
  href: https://artifacts.apis.io/inboxapp/a2a/inboxapp-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/inboxapp-a2a.yml
- group: agent
  href: https://artifacts.apis.io/inboxapp/mcp/inboxapp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/inboxapp-mcp.yml
- group: auth
  href: https://artifacts.apis.io/inboxapp/well-known/inboxapp-helpcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inboxapp-helpcenter-security.txt
- group: agent
  href: https://artifacts.apis.io/inboxapp/well-known/inboxapp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inboxapp-well-known.yml
- group: other
  href: https://artifacts.apis.io/inboxapp/hosts/inboxapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inboxapp-hosts.yml
- group: other
  href: https://artifacts.apis.io/inboxapp/vendors/inboxapp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inboxapp-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inboxapp.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inboxhq
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inboxapp.com/get-started/set-up
- group: operate
  title: ''
  type: ChangeLog
  url: https://inboxapp.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inboxapp.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/inboxapp/security/inboxapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inboxapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inboxapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inboxapp.com
- group: commercial
  title: ''
  type: Pricing
  url: https://inboxapp.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://inboxapp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://inboxapp.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inboxapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inboxapp.com/privacy
coverage:
  checked: '2026-10-20'
  detail: Documentation is rendered via Mintlify JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.inboxapp.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Inboxapp provides a shared inbox and CRM platform that aggregates messages from X, LinkedIn, email and other channels into a single conversation view. Teams can tag, assign, and follow up on leads, deals and support tickets, ensuring no message is missed. The service includes pricing plans, documentation, a changelog, a blog, and a support center, and it offers a login portal for users. Inboxapp is operated by Inbox Tech Inc., founded in 2026.
image: https://inboxapp.com/og-image.jpg
json_schemas:
- name: GetContactsResponse
  property_count: 2
  slug: inboxapp-get-contacts-response
- name: GetPlatformsResponse
  property_count: 2
  slug: inboxapp-get-platforms-response
- name: GetThreadsResponse
  property_count: 2
  slug: inboxapp-get-threads-response
- name: PostApiV2MessagesRequest
  property_count: 2
  slug: inboxapp-post-api-v2-messages-request
- name: PostMessagesResponse
  property_count: 4
  slug: inboxapp-post-messages-response
- name: PostThreadsMessagesRequest
  property_count: 3
  slug: inboxapp-post-threads-messages-request
jsonld:
- class_count: 12
  name: Inboxapp Context
  property_count: 13
  slug: inboxapp-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.inboxapp.com.
  name: Inboxapp MCP Server
  slug: inboxapp-mcp-yml
modified: '2026-10-20'
name: Inboxapp
nav: Providers
network: true
overview: 'Inboxapp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Messaging, Sales, and Collaboration.


  The Inboxapp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Inboxapp''s developer surface includes changelog, getting-started guide, API reference, documentation, pricing, engineering blog, support, and 25 more developer resources.'
plans:
- name: Inboxapp Plans Pricing
  plan_count: 2
  slug: inboxapp-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Inboxapp API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: inboxapp-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 36.8
    contract_governance: 19.7
    contract_quality: 35.5
    developer_ergonomics: 17.9
    discoverability: 66.7
    operational_transparency: 44.7
  previous_composite: 44.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/inboxapp/inboxapp-2026-11-03T133720.png
security:
- kind: domain-security
  name: Inboxapp Domain Security
  slug: inboxapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inboxapp
tags:
- Company
- CRM
- Messaging
- Sales
- Collaboration
website: https://inboxapp.com
---
