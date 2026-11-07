---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Steamgpt Net Agentic Access
  operation_count: 11
  slug: steamgpt-net-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 1
apis:
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Bans API from steamgpt-net — 1 operation(s) for bans.
  name: steamgpt-net Bans API
  slug: steamgpt-net-bans-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Batch API from steamgpt-net — 2 operation(s) for batch.
  name: steamgpt-net Batch API
  slug: steamgpt-net-batch-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Compare API from steamgpt-net — 1 operation(s) for compare.
  name: steamgpt-net Compare API
  slug: steamgpt-net-compare-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Converter API from steamgpt-net — 1 operation(s) for converter.
  name: steamgpt-net Converter API
  slug: steamgpt-net-converter-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Faceit API from steamgpt-net — 1 operation(s) for faceit.
  name: steamgpt-net Faceit API
  slug: steamgpt-net-faceit-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Friends API from steamgpt-net — 1 operation(s) for friends.
  name: steamgpt-net Friends API
  slug: steamgpt-net-friends-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Identity API from steamgpt-net — 1 operation(s) for identity.
  name: steamgpt-net Identity API
  slug: steamgpt-net-identity-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Profile API from steamgpt-net — 1 operation(s) for profile.
  name: steamgpt-net Profile API
  slug: steamgpt-net-profile-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Ready API from steamgpt-net — 1 operation(s) for ready.
  name: steamgpt-net Ready API
  slug: steamgpt-net-ready-api
- baseURL: https://steamgpt.net
  baseurl_source: declared
  description: The Summary API from steamgpt-net — 1 operation(s) for summary.
  name: steamgpt-net Summary API
  slug: steamgpt-net-summary-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/steamgpt-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/steamgpt-net/agentic-access/steamgpt-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/steamgpt-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/steamgpt-net/rules/steamgpt-net-rules.yml
  title: ''
  type: Spectral
  url: rules/steamgpt-net-rules.yml
- group: design
  href: https://artifacts.apis.io/steamgpt-net/json-ld/steamgpt-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/steamgpt-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/steamgpt-net/vocabulary/steamgpt-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/steamgpt-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/steamgpt-net/data-model/steamgpt-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/steamgpt-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/steamgpt-net/security/steamgpt-net-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/steamgpt-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/steamgpt-net/authentication/steamgpt-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/steamgpt-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/steamgpt-net/errors/steamgpt-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/steamgpt-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/steamgpt-net/conformance/steamgpt-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/steamgpt-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/steamgpt-net/llms/steamgpt-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/steamgpt-net-llms.txt
- group: other
  href: https://artifacts.apis.io/steamgpt-net/a2a/steamgpt-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/steamgpt-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/steamgpt-net/mcp/steamgpt-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/steamgpt-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/steamgpt-net/well-known/steamgpt-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/steamgpt-net-security.txt
- group: agent
  href: https://artifacts.apis.io/steamgpt-net/well-known/steamgpt-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/steamgpt-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/steamgpt-net/hosts/steamgpt-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/steamgpt-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/steamgpt-net/vendors/steamgpt-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/steamgpt-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/steamgpt-net/scopes/steamgpt-net-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/steamgpt-net-scopes.yml
- group: auth
  href: https://artifacts.apis.io/steamgpt-net/security/steamgpt-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/steamgpt-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/steamgpt-net/security/steamgpt-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/steamgpt-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://steamgpt.net/
- group: docs
  title: ''
  type: Documentation
  url: https://steamgpt.net/docs.md
- group: docs
  title: ''
  type: APIReference
  url: https://steamgpt.net/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://steamgpt.net/about
- group: operate
  title: ''
  type: Support
  url: https://steamgpt.net/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://steamgpt.net/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://steamgpt.net/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SteamGPTnet
created: '2026-10-31'
description: SteamGPT provides a free, no‑key API that transforms Steam user data into AI‑ready formats. It offers endpoints for SteamID conversion, ban checks, and profile lookups, delivering results as markdown, plain text, JSON, or OpenAPI specifications. Targeted at AI agents, developers, and applications, the service operates without registration, cookies, or tracking, and is independent of Valve Corporation.
image: https://steamgpt.net/img/og-home.png
json_schemas:
- name: Bans
  property_count: 2
  slug: steamgpt-net-bans
- name: Batch
  property_count: 2
  slug: steamgpt-net-batch
- name: Compare
  property_count: 2
  slug: steamgpt-net-compare
- name: Converter
  property_count: 2
  slug: steamgpt-net-converter
- name: Identity
  property_count: 2
  slug: steamgpt-net-identity
- name: Summary
  property_count: 2
  slug: steamgpt-net-summary
jsonld:
- class_count: 17
  name: Steamgpt Net Context
  property_count: 34
  slug: steamgpt-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at steamgpt.net.
  name: steamgpt-net MCP Server
  slug: steamgpt-net-mcp-yml
modified: '2026-10-31'
name: steamgpt-net
nav: Providers
network: true
overview: 'steamgpt-net publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bans API, Batch API, Compare API, and 7 more. Tagged areas include Company, Artificial Intelligence, Gaming, and Steam.


  The steamgpt-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  steamgpt-net''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 23 more developer resources.'
plans:
- name: Steamgpt Net Plans Pricing
  plan_count: 0
  slug: steamgpt-net-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Steamgpt Net Rate Limits
  slug: steamgpt-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: steamgpt-net API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: steamgpt-net-rules
scopes:
- name: Steamgpt Net Scopes
  scope_count: 1
  slug: steamgpt-net-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.8
    developer_ergonomics: 35.0
    discoverability: 56.7
    operational_transparency: 34.2
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/steamgpt-net/steamgpt-net-2026-11-03T143804.png
security:
- kind: authentication
  name: Steamgpt Net Authentication
  slug: steamgpt-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Steamgpt Net Domain Security
  slug: steamgpt-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Steamgpt Net Vulnerability Disclosure
  slug: steamgpt-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: steamgpt-net
tags:
- Company
- Artificial Intelligence
- Gaming
- Steam
website: https://steamgpt.net/
---
