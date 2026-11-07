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
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.temprhq.io
  baseurl_source: declared
  description: 'temprhq-io API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: temprhq-io API
  slug: temprhq-io-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/temprhq-io/rate-limits/temprhq-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/temprhq-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/temprhq-io/plans/temprhq-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/temprhq-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/temprhq-io/rules/temprhq-io-rules.yml
  title: ''
  type: Spectral
  url: rules/temprhq-io-rules.yml
- group: design
  href: https://artifacts.apis.io/temprhq-io/json-ld/temprhq-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/temprhq-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/temprhq-io/vocabulary/temprhq-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/temprhq-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/temprhq-io/data-model/temprhq-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/temprhq-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/temprhq-io/cli/temprhq-io-cli.yml
  title: ''
  type: CLI
  url: cli/temprhq-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/temprhq-io/changelog/temprhq-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/temprhq-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/temprhq-io/authentication/temprhq-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/temprhq-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/temprhq-io/scopes/temprhq-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/temprhq-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/temprhq-io/errors/temprhq-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/temprhq-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/temprhq-io/conformance/temprhq-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/temprhq-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/temprhq-io/llms/temprhq-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/temprhq-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/temprhq-io/mcp/temprhq-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/temprhq-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/temprhq-io/well-known/temprhq-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/temprhq-io-security.txt
- group: auth
  href: https://artifacts.apis.io/temprhq-io/well-known/temprhq-io-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/temprhq-io-portal-security.txt
- group: auth
  href: https://artifacts.apis.io/temprhq-io/well-known/temprhq-io-open-vsx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/temprhq-io-open-vsx-security.txt
- group: auth
  href: https://artifacts.apis.io/temprhq-io/well-known/temprhq-io-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/temprhq-io-api-security.txt
- group: agent
  href: https://artifacts.apis.io/temprhq-io/well-known/temprhq-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/temprhq-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/temprhq-io/hosts/temprhq-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/temprhq-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/temprhq-io/vendors/temprhq-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/temprhq-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/temprhq-io/packages/temprhq-io-packages.yml
  title: ''
  type: SDKs
  url: packages/temprhq-io-packages.yml
- group: build
  href: https://artifacts.apis.io/temprhq-io/packages/temprhq-io-packages.yml
  title: ''
  type: Packages
  url: packages/temprhq-io-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://temprhq.io/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.temprhq.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://temprhq.io/changelog
- group: auth
  href: https://artifacts.apis.io/temprhq-io/security/temprhq-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/temprhq-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/temprhq-io/security/temprhq-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/temprhq-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://temprhq.io/
- group: docs
  title: ''
  type: Documentation
  url: https://temprhq.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://temprhq.io/docs/quickstart-gateway
- group: commercial
  title: ''
  type: Pricing
  url: https://temprhq.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://temprhq.io/blog
- group: operate
  title: ''
  type: Support
  url: https://temprhq.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://temprhq.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://temprhq.io/privacy
created: '2026-10-30'
description: Tempr provides an AI platform that unifies access to multiple large language model providers through a single API, offering plans, budgeting, guardrails, and logging. Users can run Claude Code, Codex, and other tools via the Tempr Gateway API, manage agents in IDEs, CLI, or web, and secure secrets. The service includes a developer portal, documentation, quickstarts, pricing, and a blog.
image: https://temprhq.io/assets/logo.svg
json_schemas:
- name: PostV1EmbeddingsResponse
  property_count: 4
  slug: temprhq-io-post-v1-embeddings-response
- name: PostV1ManagementAgentConfigRulesResponse
  property_count: 5
  slug: temprhq-io-post-v1-management-agent-config-rules-response
- name: PostV1ManagementAgentConfigSkillsRequest
  property_count: 3
  slug: temprhq-io-post-v1-management-agent-config-skills-request
- name: PostV1ManagementKeysRequest
  property_count: 5
  slug: temprhq-io-post-v1-management-keys-request
- name: PostV1ManagementToolPacksRequest
  property_count: 3
  slug: temprhq-io-post-v1-management-tool-packs-request
- name: PutV1ManagementKeys6F1C2B0EEndUsersCustomer4821LimitsRespons
  property_count: 7
  slug: temprhq-io-put-v1-management-keys6-f1-c2-b0-eend-users-customer4821-limits-respons
jsonld:
- class_count: 18
  name: Temprhq Io Context
  property_count: 33
  slug: temprhq-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at temprhq.io.
  name: temprhq-io MCP Server
  slug: temprhq-io-mcp-yml
modified: '2026-10-30'
name: temprhq-io
nav: Providers
network: true
overview: 'temprhq-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Automation, Developer Tools, and Cloud.


  The temprhq-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  temprhq-io''s developer surface includes CLI, changelog, authentication, documentation, getting-started guide, pricing, engineering blog, and 29 more developer resources.'
plans:
- name: Temprhq Io Plans Pricing
  plan_count: 7
  slug: temprhq-io-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Temprhq Io Rate Limits
  slug: temprhq-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: temprhq-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: temprhq-io-rules
scopes:
- name: Temprhq Io Scopes
  scope_count: 1
  slug: temprhq-io-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 26.4
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 44.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 54.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/temprhq-io/temprhq-io-2026-11-03T144425.png
security:
- kind: authentication
  name: Temprhq Io Authentication
  slug: temprhq-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Temprhq Io Domain Security
  slug: temprhq-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Temprhq Io Vulnerability Disclosure
  slug: temprhq-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: temprhq-io
tags:
- Artificial Intelligence
- Platform
- Automation
- Developer Tools
- Cloud
website: https://temprhq.io/
---
