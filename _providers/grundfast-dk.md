---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST over Datafordeler — BBR ejendom (BFE-keyed), Matriklen, DAGI, DHM, Stednavne, DAR address resolution, and CVR company lookup; translated kodelister, WGS84 geometry, and a property-keyed batch.
  name: Grundfast API
  slug: grundfast-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/grundfast-dk/rules/grundfast-dk-rules.yml
  title: ''
  type: Spectral
  url: rules/grundfast-dk-rules.yml
- group: design
  href: https://artifacts.apis.io/grundfast-dk/json-ld/grundfast-dk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/grundfast-dk-context.jsonld
- group: design
  href: https://artifacts.apis.io/grundfast-dk/vocabulary/grundfast-dk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/grundfast-dk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/grundfast-dk/conformance/grundfast-dk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grundfast-dk-conformance.yml
- group: operate
  href: https://artifacts.apis.io/grundfast-dk/rate-limits/grundfast-dk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/grundfast-dk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/grundfast-dk/plans/grundfast-dk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/grundfast-dk-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/grundfast-dk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/grundfast-dk/data-model/grundfast-dk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/grundfast-dk-data-model.yml
- group: start
  href: https://artifacts.apis.io/grundfast-dk/sandbox/grundfast-dk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/grundfast-dk-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/grundfast-dk/security/grundfast-dk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/grundfast-dk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/grundfast-dk/authentication/grundfast-dk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grundfast-dk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/grundfast-dk/scopes/grundfast-dk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/grundfast-dk-scopes.yml
- group: design
  href: https://artifacts.apis.io/grundfast-dk/lifecycle/grundfast-dk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/grundfast-dk-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/grundfast-dk/errors/grundfast-dk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grundfast-dk-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/grundfast-dk/llms/grundfast-dk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grundfast-dk-llms.txt
- group: agent
  href: https://artifacts.apis.io/grundfast-dk/mcp/grundfast-dk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/grundfast-dk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/grundfast-dk/well-known/grundfast-dk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/grundfast-dk-security.txt
- group: agent
  href: https://artifacts.apis.io/grundfast-dk/well-known/grundfast-dk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grundfast-dk-well-known.yml
- group: other
  href: https://artifacts.apis.io/grundfast-dk/hosts/grundfast-dk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grundfast-dk-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://grundfast.dk/status
- group: commercial
  title: ''
  type: Pricing
  url: https://grundfast.dk/en/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://grundfast.dk/changelog
- group: auth
  href: https://artifacts.apis.io/grundfast-dk/security/grundfast-dk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/grundfast-dk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/grundfast-dk/security/grundfast-dk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grundfast-dk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grundfast.dk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://grundfast.dk/docs
- group: docs
  title: ''
  type: Documentation
  url: https://grundfast.dk/docs
- group: docs
  title: ''
  type: APIReference
  url: https://grundfast.dk/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://grundfast.dk/?format=md
- group: operate
  title: ''
  type: Support
  url: https://grundfast.dk/kontakt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grundfast
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://grundfast.dk/openapi.json
  - status: null
    url: https://api.grundfast.dk/openapi.json
  - status: 401
    url: https://grundfast.dk/mcp
  - status: 401
    url: https://api.grundfast.dk/mcp
  - status: 200
    url: https://grundfast.dk/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Grundfast provides a drop-in compatibility API that mirrors the legacy services.datafordeler.dk endpoints for Danish property and geodata (BBR, Matrikel, valuation, building lines, CVR, etc.) ensuring continuity after Datafordeler's shutdown on 15 January 2027. It offers a single API key, auto‑pagination, and a free tier, serving cached data when the upstream service is unavailable.
image: https://grundfast.dk/og/home.png?v=5
jsonld:
- class_count: 96
  name: Grundfast Dk Context
  property_count: 224
  slug: grundfast-dk-context
layout: provider
mcp_servers:
- description: Remote MCP server at grundfast.dk.
  name: grundfast-dk MCP Server
  slug: grundfast-dk-mcp-yml
modified: '2026-10-30'
name: grundfast-dk
nav: Providers
network: true
overview: 'grundfast-dk publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Grundfast API. Tagged areas include RealEstate, Geodata, API, Denmark, and Compatibility.


  The grundfast-dk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  grundfast-dk''s developer surface includes sandbox, authentication, pricing, changelog, documentation, API reference, getting-started guide, and 24 more developer resources.'
plans:
- name: Grundfast Dk Plans Pricing
  plan_count: 5
  slug: grundfast-dk-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 9
  name: Grundfast Dk Rate Limits
  slug: grundfast-dk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: grundfast-dk API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 3
  slug: grundfast-dk-rules
scopes:
- name: Grundfast Dk Scopes
  scope_count: 0
  slug: grundfast-dk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 90.3
    catalog_earned_first_party: 0.0
    catalog_gap: 24.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.9
    contract_governance: 79.1
    contract_quality: 38.7
    developer_ergonomics: 68.3
    discoverability: 65.0
    operational_transparency: 75.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Grundfast Dk Authentication
  slug: grundfast-dk-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Grundfast Dk Domain Security
  slug: grundfast-dk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Grundfast Dk Vulnerability Disclosure
  slug: grundfast-dk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: grundfast
  slug: grundfast-SKILL
slug: grundfast-dk
tags:
- RealEstate
- Geodata
- API
- Denmark
- Compatibility
website: https://grundfast.dk/
---
