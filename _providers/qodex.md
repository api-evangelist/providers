---
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API testing platform allowing import of OpenAPI specs and automated testing of APIs.
  name: Qodex API
  slug: qodex-api-2
- baseURL: https://agents.qodex.ai
  baseurl_source: declared
  description: 'QodexAI API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: QodexAI API
  slug: qodex-api
artifact_total: 15
asyncapis:
- description: ''
  name: Qodex Webhooks
  slug: qodex-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/qodex/plans/qodex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qodex-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/qodex/rules/qodex-rules.yml
  title: ''
  type: Spectral
  url: rules/qodex-rules.yml
- group: design
  href: https://artifacts.apis.io/qodex/json-ld/qodex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qodex-context.jsonld
- group: design
  href: https://artifacts.apis.io/qodex/vocabulary/qodex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qodex-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/qodex/asyncapi/qodex-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/qodex-webhooks.yml
- group: design
  href: https://artifacts.apis.io/qodex/data-model/qodex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qodex-data-model.yml
- group: operate
  href: https://artifacts.apis.io/qodex/changelog/qodex-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qodex-changelog.yml
- group: auth
  href: https://artifacts.apis.io/qodex/authentication/qodex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qodex-authentication.yml
- group: design
  href: https://artifacts.apis.io/qodex/errors/qodex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qodex-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qodex/conformance/qodex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qodex-conformance.yml
- group: agent
  href: https://artifacts.apis.io/qodex/llms/qodex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qodex-llms.txt
- group: agent
  href: https://artifacts.apis.io/qodex/mcp/qodex-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qodex-mcp.yml
- group: agent
  href: https://artifacts.apis.io/qodex/well-known/qodex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qodex-well-known.yml
- group: other
  href: https://artifacts.apis.io/qodex/hosts/qodex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qodex-hosts.yml
- group: other
  href: https://artifacts.apis.io/qodex/vendors/qodex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qodex-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qodex-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://qodex.ai/docs/changelog
- group: auth
  href: https://artifacts.apis.io/qodex/security/qodex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qodex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qodex.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://qodex.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://qodex.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://qodex.ai/docs/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://qodex.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qodex.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qodex.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://qodex.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://qodex.ai/contact-us
coverage:
  checked: '2026-10-21'
  detail: Documentation provides API testing features but no machine‑readable OpenAPI or other contract is available.
  evidence:
  - status: 200
    url: https://qodex.ai/docs/api-testing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: QodexAI provides continuous testing for AI‑speed engineering, turning test knowledge into durable scenarios that evolve with your product. It integrates with GitHub pull requests, CLI, chat, schedules, and deploy checks, helping teams ensure reliable AI‑driven software delivery.
image: https://qodex.ai/assets/images/logo-header.png
json_schemas:
- name: PostApiOrdersRequest
  property_count: 2
  slug: qodex-post-api-orders-request
- name: PostApiOrdersResponse
  property_count: 2
  slug: qodex-post-api-orders-response
- name: PostApiProjectsMyProjectSlugWebhooksTriggerResponse
  property_count: 4
  slug: qodex-post-api-projects-my-project-slug-webhooks-trigger-response
- name: PostAuthLoginResponse
  property_count: 2
  slug: qodex-post-auth-login-response
- name: PostCheckoutResponse
  property_count: 2
  slug: qodex-post-checkout-response
- name: PostV1PaymentsRequest
  property_count: 3
  slug: qodex-post-v1-payments-request
jsonld:
- class_count: 21
  name: Qodex Context
  property_count: 28
  slug: qodex-context
layout: provider
mcp_servers:
- description: Remote MCP server at qodex.ai.
  name: QodexAI MCP Server
  slug: qodex-mcp-yml
modified: '2026-10-21'
name: QodexAI
nav: Providers
network: true
overview: 'QodexAI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Testing, Continuous Integration, and DevOps.


  The QodexAI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  QodexAI''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Qodex Plans Pricing
  plan_count: 7
  slug: qodex-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: QodexAI API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: qodex-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 32.9
    developer_ergonomics: 47.6
    discoverability: 56.7
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 17
      marker_coverage: 100.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Qodex Authentication
  slug: qodex-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qodex Domain Security
  slug: qodex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qodex
tags:
- Company
- AI
- Testing
- Continuous Integration
- DevOps
website: https://qodex.ai/
---
