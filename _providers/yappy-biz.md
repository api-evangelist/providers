---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Yappy Biz Agentic Access
  operation_count: 15
  slug: yappy-biz-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 1
apis:
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: Many reads, one request, one unit of rate limit.
  name: yappy-biz Batch API
  slug: yappy-biz-batch-api
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: What Yappy and its backends cost.
  name: yappy-biz Commerce API
  slug: yappy-biz-commerce-api
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: Finding your way around the API.
  name: yappy-biz Discovery API
  slug: yappy-biz-discovery-api
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: Documentation pages, FAQ, and search.
  name: yappy-biz Documentation API
  slug: yappy-biz-documentation-api
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: Asynchronous corpus exports.
  name: yappy-biz Exports API
  slug: yappy-biz-exports-api
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: Features, requirements, and machine compatibility.
  name: yappy-biz Product API
  slug: yappy-biz-product-api
- baseURL: https://yappy.biz/api/v1
  baseurl_source: declared
  description: Yappy's macOS release history and current version.
  name: yappy-biz Releases API
  slug: yappy-biz-releases-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/yappy-biz/agentic-access/yappy-biz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yappy-biz-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/yappy-biz/rate-limits/yappy-biz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/yappy-biz-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/rules/yappy-biz-rules.yml
  title: ''
  type: Spectral
  url: rules/yappy-biz-rules.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/json-ld/yappy-biz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yappy-biz-context.jsonld
- group: design
  href: https://artifacts.apis.io/yappy-biz/vocabulary/yappy-biz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yappy-biz-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/yappy-biz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/data-model/yappy-biz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yappy-biz-data-model.yml
- group: operate
  href: https://artifacts.apis.io/yappy-biz/changelog/yappy-biz-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yappy-biz-changelog.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/conventions/yappy-biz-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/yappy-biz-conventions.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/conventions/yappy-biz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yappy-biz-conventions.yml
- group: start
  href: https://artifacts.apis.io/yappy-biz/sandbox/yappy-biz-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/yappy-biz-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://yappy.biz/contact/
- group: auth
  href: https://artifacts.apis.io/yappy-biz/authentication/yappy-biz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yappy-biz-authentication.yml
- group: auth
  href: https://artifacts.apis.io/yappy-biz/scopes/yappy-biz-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/yappy-biz-scopes.yml
- group: operate
  href: https://artifacts.apis.io/yappy-biz/lifecycle/yappy-biz-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/yappy-biz-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/lifecycle/yappy-biz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yappy-biz-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/errors/yappy-biz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yappy-biz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/yappy-biz/conformance/yappy-biz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yappy-biz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/yappy-biz/llms/yappy-biz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yappy-biz-llms.txt
- group: other
  href: https://artifacts.apis.io/yappy-biz/a2a/yappy-biz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/yappy-biz-a2a.yml
- group: build
  href: https://artifacts.apis.io/yappy-biz/mcp/yappy-biz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/yappy-biz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/yappy-biz/mcp/yappy-biz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yappy-biz-mcp.yml
- group: auth
  href: https://artifacts.apis.io/yappy-biz/well-known/yappy-biz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yappy-biz-security.txt
- group: agent
  href: https://artifacts.apis.io/yappy-biz/well-known/yappy-biz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yappy-biz-well-known.yml
- group: other
  href: https://artifacts.apis.io/yappy-biz/hosts/yappy-biz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yappy-biz-hosts.yml
- group: other
  href: https://artifacts.apis.io/yappy-biz/vendors/yappy-biz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yappy-biz-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OperatingSystem-1
- group: start
  title: ''
  type: DeveloperPortal
  url: https://yappy.biz/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://yappy.biz/docs/changelog
- group: start
  title: ''
  type: SignUp
  url: https://yappy.biz/oauth/register
- group: auth
  href: https://artifacts.apis.io/yappy-biz/security/yappy-biz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yappy-biz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yappy-biz/security/yappy-biz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yappy-biz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yappy.biz/
- group: docs
  title: ''
  type: Documentation
  url: https://yappy.biz/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://yappy.biz/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://yappy.biz/auth.md
- group: commercial
  title: ''
  type: Pricing
  url: https://yappy.biz/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yappy.biz/privacy
created: '2026-10-30'
description: Yappy is a voice‑agent application for macOS that lets users dictate text and issue commands by holding modifier keys. It operates entirely on‑device, ensuring speech data never leaves the user’s computer. The service offers a free, read‑only public API exposing factual information about Yappy’s features, usage statistics, and supported commands, hosted at https://yappy.biz/api/v1.
image: https://yappy.biz/og-image.png
json_schemas:
- name: Compatibility
  property_count: 5
  slug: yappy-biz-compatibility
- name: Doc
  property_count: 10
  slug: yappy-biz-doc
- name: Job
  property_count: 10
  slug: yappy-biz-job
- name: Pricing
  property_count: 6
  slug: yappy-biz-pricing
- name: Requirements
  property_count: 7
  slug: yappy-biz-requirements
- name: ServiceIndex
  property_count: 11
  slug: yappy-biz-service-index
jsonld:
- class_count: 23
  name: Yappy Biz Context
  property_count: 79
  slug: yappy-biz-context
layout: provider
mcp_servers:
- description: Remote MCP server at yappy.biz.
  name: yappy-biz MCP Server
  slug: yappy-biz-mcp-yml
modified: '2026-10-30'
name: yappy-biz
nav: Providers
network: true
overview: 'yappy-biz publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Commerce API, Discovery API, and 4 more. Tagged areas include Voice, macOS, Automation, Accessibility, and Productivity.


  The yappy-biz catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  yappy-biz''s developer surface includes changelog, sandbox, authentication, signup flow, documentation, API reference, getting-started guide, and 31 more developer resources.'
plans:
- name: Yappy Biz Plans Pricing
  plan_count: 0
  slug: yappy-biz-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Yappy Biz Rate Limits
  slug: yappy-biz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: yappy-biz API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: yappy-biz-rules
scopes:
- name: Yappy Biz Scopes
  scope_count: 5
  slug: yappy-biz-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 65.8
    developer_ergonomics: 63.6
    discoverability: 65.0
    operational_transparency: 71.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Yappy Biz Authentication
  slug: yappy-biz-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Yappy Biz Domain Security
  slug: yappy-biz-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Yappy Biz Vulnerability Disclosure
  slug: yappy-biz-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: yappy-biz-agent-auth-skill
  slug: yappy-biz-agent-auth-skill
- name: yappy-macos-support
  slug: yappy-biz-macos-support-skill
- name: yappy
  slug: yappy-biz-yappy-skill
slug: yappy-biz
tags:
- Voice
- macOS
- Automation
- Accessibility
- Productivity
website: https://yappy.biz/
---
