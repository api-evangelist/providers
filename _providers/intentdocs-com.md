---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Intentdocs Com Agentic Access
  operation_count: 28
  slug: intentdocs-com-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 1
apis:
- baseURL: https://intentdocs.com
  baseurl_source: declared
  description: Authentication and project discovery for CLI tools like intentdocs-cli
  name: intentdocs-com CLI API
  slug: intentdocs-com-cli-api
- baseURL: https://intentdocs.com
  baseurl_source: declared
  description: Model Context Protocol endpoint for AI development tools (Claude Code, Cursor, etc.)
  name: intentdocs-com MCP API
  slug: intentdocs-com-mcp-api
- baseURL: https://intentdocs.com
  baseurl_source: declared
  description: OAuth 2.1 authorization and token endpoints
  name: intentdocs-com OAuth API
  slug: intentdocs-com-oauth-api
- baseURL: https://intentdocs.com
  baseurl_source: declared
  description: Sync API for external tools to read/write story maps, log activities, and report progress
  name: intentdocs-com Sync API
  slug: intentdocs-com-sync-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/intentdocs-com/agentic-access/intentdocs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intentdocs-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/intentdocs-com/rules/intentdocs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/intentdocs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/intentdocs-com/json-ld/intentdocs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intentdocs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/intentdocs-com/vocabulary/intentdocs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intentdocs-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/intentdocs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/intentdocs-com/data-model/intentdocs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intentdocs-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/intentdocs-com/lifecycle/intentdocs-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/intentdocs-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/intentdocs-com/lifecycle/intentdocs-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/intentdocs-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/intentdocs-com/errors/intentdocs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/intentdocs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/intentdocs-com/conformance/intentdocs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intentdocs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/intentdocs-com/well-known/intentdocs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/intentdocs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/intentdocs-com/hosts/intentdocs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intentdocs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/intentdocs-com/vendors/intentdocs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intentdocs-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/intentdocs-com/packages/intentdocs-com-packages.yml
  title: ''
  type: SDKs
  url: packages/intentdocs-com-packages.yml
- group: build
  href: https://artifacts.apis.io/intentdocs-com/packages/intentdocs-com-packages.yml
  title: ''
  type: Packages
  url: packages/intentdocs-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.intentdocs.com/sign-in
- group: auth
  href: https://artifacts.apis.io/intentdocs-com/scopes/intentdocs-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/intentdocs-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/intentdocs-com/authentication/intentdocs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/intentdocs-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/intentdocs-com/security/intentdocs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intentdocs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intentdocs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.intentdocs.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.intentdocs.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.intentdocs.com/connect
- group: operate
  title: ''
  type: Support
  url: https://www.intentdocs.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.intentdocs.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.intentdocs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intentdocs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intentdocs.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intentdocs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.intentdocs.com/api/mcp
  - status: 200
    url: https://intentdocs.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: IntentDocs turns your app idea into a spec your AI coding agent builds exactly to, one story at a time, and shows you proof each piece works. It is a spec‑driven development platform for AI coding agents, letting you generate structured specs from an AI interview, connect Claude Code, Cursor, or any MCP client over MCP, and get an audit trail of what was built versus what was planned. You can start for free and build your first story without a credit card.
image: https://www.intentdocs.com/opengraph-image-1b0us4?eb1d209e5ae11439
json_schemas:
- name: AcceptanceCriterion
  property_count: 9
  slug: intentdocs-com-acceptance-criterion
- name: BuildOrderStory
  property_count: 9
  slug: intentdocs-com-build-order-story
- name: Decision
  property_count: 6
  slug: intentdocs-com-decision
- name: Story
  property_count: 15
  slug: intentdocs-com-story
jsonld:
- class_count: 5
  name: Intentdocs Com Context
  property_count: 28
  slug: intentdocs-com-context
layout: provider
modified: '2026-10-30'
name: intentdocs-com
nav: Providers
network: true
overview: 'intentdocs-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including CLI API, MCP API, OAuth API, and 1 more. Tagged areas include Company, AI, Spec-Driven, Platform, and Automation.


  The intentdocs-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  intentdocs-com''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: intentdocs-com API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 2
  slug: intentdocs-com-rules
scopes:
- name: Intentdocs Com Scopes
  scope_count: 6
  slug: intentdocs-com-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 58.1
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 13.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Intentdocs Com Authentication
  slug: intentdocs-com-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Intentdocs Com Domain Security
  slug: intentdocs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: intentdocs-com-cli-auth
  slug: intentdocs-com-cli-auth
slug: intentdocs-com
tags:
- Company
- AI
- Spec-Driven
- Platform
- Automation
- Low-Code
website: https://intentdocs.com/
---
