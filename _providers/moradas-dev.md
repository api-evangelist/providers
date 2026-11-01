---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Free API for Portuguese address autocomplete and postal code lookup.
  name: Moradas API
  slug: moradas-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/moradas-dev/rate-limits/moradas-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moradas-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/moradas-dev/rules/moradas-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/moradas-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/moradas-dev/json-ld/moradas-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/moradas-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/moradas-dev/vocabulary/moradas-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/moradas-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/moradas-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/moradas-dev/data-model/moradas-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moradas-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/moradas-dev/changelog/moradas-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moradas-dev-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://moradas.dev/status
- group: design
  href: https://artifacts.apis.io/moradas-dev/lifecycle/moradas-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moradas-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/moradas-dev/errors/moradas-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moradas-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moradas-dev/conformance/moradas-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moradas-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/moradas-dev/llms/moradas-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moradas-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/moradas-dev/mcp/moradas-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moradas-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/moradas-dev/mcp/moradas-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moradas-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/moradas-dev/hosts/moradas-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moradas-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/moradas-dev/vendors/moradas-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moradas-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/moradas-dev/security/moradas-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moradas-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moradas.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://moradas.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://moradas.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://moradas.dev/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://moradas.dev/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moradas.dev/privacy
created: '2026-10-30'
description: Moradas.dev provides a free, public API for Portuguese address autocomplete and postal code lookup. It enables developers to retrieve street suggestions, resolve full addresses with door numbers, and obtain exact 7‑digit CP7 codes without requiring an API key or registration. The service is CORS‑enabled, offers a fair‑use limit of about 50 requests per 10 seconds per IP, and is intended for both client‑side and server‑side integrations. It is hosted at https://moradas.dev and documented with an OpenAPI 3.1 specification.
image: https://moradas.dev/favicon.svg?v=2
jsonld:
- class_count: 18
  name: Moradas Dev Context
  property_count: 42
  slug: moradas-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at moradas.dev.
  name: moradas-dev MCP Server
  slug: moradas-dev-mcp-yml
modified: '2026-10-30'
name: moradas-dev
nav: Providers
network: true
overview: 'moradas-dev publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Address, Portugal, Autocomplete, OpenAPI, and Free.


  The moradas-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  moradas-dev''s developer surface includes changelog, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Moradas Dev Plans Pricing
  plan_count: 0
  slug: moradas-dev-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Moradas Dev Rate Limits
  slug: moradas-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: moradas-dev API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: moradas-dev-rules
scopes:
- name: Moradas Dev Scopes
  scope_count: 0
  slug: moradas-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 75.9
    catalog_earned_first_party: 0.0
    catalog_gap: 39.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 79.1
    contract_quality: 14.7
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 50.5
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
  name: Moradas Dev Authentication
  slug: moradas-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Moradas Dev Domain Security
  slug: moradas-dev-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: postal-code-info
  slug: moradas-dev-postal_code_info
- name: resolve-postal-code
  slug: moradas-dev-resolve_postal_code
- name: suggest-address
  slug: moradas-dev-suggest_address
- name: verify-addresses
  slug: moradas-dev-verify_addresses
slug: moradas-dev
tags:
- Address
- Portugal
- Autocomplete
- OpenAPI
- Free
website: https://moradas.dev/
---
