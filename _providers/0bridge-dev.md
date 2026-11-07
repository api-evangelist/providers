---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 0bridge provides a single MCP endpoint that aggregates AI tool integrations, allowing unified access to services like Claude, ChatGPT, Codex, and Cursor.
  name: 0bridge MCP
  slug: 0bridge-mcp
- description: '0bridge API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 0bridge API
  slug: 0bridge-dev-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/0bridge-dev/rate-limits/0bridge-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/0bridge-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/0bridge-dev/plans/0bridge-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0bridge-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/0bridge-dev/rules/0bridge-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/0bridge-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/0bridge-dev/json-ld/0bridge-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/0bridge-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/0bridge-dev/vocabulary/0bridge-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0bridge-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/0bridge-dev/data-model/0bridge-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/0bridge-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/0bridge-dev/cli/0bridge-dev-cli.yml
  title: ''
  type: CLI
  url: cli/0bridge-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/0bridge-dev/changelog/0bridge-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/0bridge-dev-changelog.yml
- group: start
  href: https://artifacts.apis.io/0bridge-dev/sandbox/0bridge-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/0bridge-dev-sandbox.yml
- group: design
  href: https://artifacts.apis.io/0bridge-dev/conformance/0bridge-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0bridge-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/0bridge-dev/llms/0bridge-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0bridge-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/0bridge-dev/well-known/0bridge-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0bridge-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/0bridge-dev/hosts/0bridge-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0bridge-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/0bridge-dev/vendors/0bridge-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0bridge-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/0bridge-dev/packages/0bridge-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/0bridge-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/0bridge-dev/packages/0bridge-dev-packages.yml
  title: ''
  type: Packages
  url: packages/0bridge-dev-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://0bridge.dev/login?next=/app/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://0bridge.dev/changelog
- group: auth
  href: https://artifacts.apis.io/0bridge-dev/security/0bridge-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0bridge-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0bridge.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://0bridge.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://0bridge.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://0bridge.dev/pricing
- group: auth
  title: ''
  type: Security
  url: https://0bridge.dev/security
- group: operate
  title: ''
  type: Support
  url: https://0bridge.dev/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0bridge.dev/policy/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0bridge.dev/policy/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0bridge
- group: start
  title: ''
  type: SignUp
  url: https://0bridge.dev/login
coverage:
  checked: '2026-10-31'
  detail: Public documentation exists but no machine-readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://0bridge.dev/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 0bridge is one MCP endpoint that gives every AI tool your team uses, from Claude and ChatGPT to Claude Code, Codex and Cursor, the same services, files, instructions and skills. Each person signs in with their own account and keeps their own memory and history. Free for one person.
image: https://0bridge.dev/og.png
json_schemas:
- name: DeleteApiDriveContentResponse
  property_count: 1
  slug: 0bridge-dev-delete-api-drive-content-response
- name: GetApiDriveSpacesResponse
  property_count: 2
  slug: 0bridge-dev-get-api-drive-spaces-response
- name: PostApiTriggersRequest
  property_count: 1
  slug: 0bridge-dev-post-api-triggers-request
- name: PostApiTriggersResponse
  property_count: 3
  slug: 0bridge-dev-post-api-triggers-response
- name: PostApiWebhookHandlerRequest
  property_count: 2
  slug: 0bridge-dev-post-api-webhook-handler-request
- name: PutApiDriveContentRequest
  property_count: 1
  slug: 0bridge-dev-put-api-drive-content-request
jsonld:
- class_count: 9
  name: 0Bridge Dev Context
  property_count: 13
  slug: 0bridge-dev-context
layout: provider
modified: '2026-10-31'
name: 0bridge
nav: Providers
network: true
overview: '0bridge is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, MCP, Integration, Team Collaboration, and Productivity.


  The 0bridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  0bridge''s developer surface includes CLI, changelog, sandbox, documentation, API reference, pricing, support, and 22 more developer resources.'
plans:
- name: 0Bridge Dev Plans Pricing
  plan_count: 4
  slug: 0bridge-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: 0Bridge Dev Rate Limits
  slug: 0bridge-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 0bridge API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: 0bridge-dev-rules
scopes:
- name: 0Bridge Dev Scopes
  scope_count: 0
  slug: 0bridge-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 32.1
    discoverability: 58.0
    operational_transparency: 36.8
  previous_composite: 47.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 0Bridge Dev Authentication
  slug: 0bridge-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 0Bridge Dev Domain Security
  slug: 0bridge-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 0bridge-dev
tags:
- Artificial Intelligence
- MCP
- Integration
- Team Collaboration
- Productivity
website: https://0bridge.dev/
---
