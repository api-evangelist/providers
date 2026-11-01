---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Managed Cloud Proxy (MCP) API providing integration endpoints for Weather, Google Mail, Fortnox, Stripe etc.
  name: NordicMCP API
  slug: nordicmcp-api
- description: 'nordicmcp-eu API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: nordicmcp-eu API
  slug: nordicmcp-eu-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/nordicmcp-eu/rate-limits/nordicmcp-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nordicmcp-eu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nordicmcp-eu/plans/nordicmcp-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nordicmcp-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nordicmcp-eu/rules/nordicmcp-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/nordicmcp-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/nordicmcp-eu/json-ld/nordicmcp-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nordicmcp-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/nordicmcp-eu/vocabulary/nordicmcp-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nordicmcp-eu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nordicmcp-eu/data-model/nordicmcp-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nordicmcp-eu-data-model.yml
- group: auth
  href: https://artifacts.apis.io/nordicmcp-eu/authentication/nordicmcp-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nordicmcp-eu-authentication.yml
- group: design
  href: https://artifacts.apis.io/nordicmcp-eu/errors/nordicmcp-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nordicmcp-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nordicmcp-eu/conformance/nordicmcp-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nordicmcp-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nordicmcp-eu/mcp/nordicmcp-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nordicmcp-eu-mcp.yml
- group: other
  href: https://artifacts.apis.io/nordicmcp-eu/hosts/nordicmcp-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordicmcp-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/nordicmcp-eu/vendors/nordicmcp-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nordicmcp-eu-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://nordicmcp.eu/status
- group: auth
  title: ''
  type: Security
  url: https://nordicmcp.eu/security
- group: auth
  href: https://artifacts.apis.io/nordicmcp-eu/security/nordicmcp-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordicmcp-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordicmcp.eu/
- group: other
  title: ''
  type: Image
  url: https://nordicmcp.eu/logo.jpeg
- group: docs
  title: ''
  type: Documentation
  url: https://nordicmcp.eu/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nordicmcp.eu/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nordicmcp.eu/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://nordicmcp.eu/docs
- group: start
  title: ''
  type: SignUp
  url: https://nordicmcp.eu/signup
- group: start
  title: ''
  type: Login
  url: https://nordicmcp.eu/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nordicmcp.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nordicmcp.eu/privacy
coverage:
  checked: '2026-10-29'
  detail: The provider's public documentation is HTML-only and does not publish any OpenAPI, AsyncAPI, GraphQL SDL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://nordicmcp.eu/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: NordicMCP provides Managed Cloud Proxy (MCP) endpoints tailored for AI assistants, delivering ready‑made integrations with services such as Weather, Google Mail, Fortnox, and Stripe. Users can quickly obtain unique endpoint URLs that include built‑in authentication, eliminating the need to manage individual API keys. The platform targets AI tools like Claude and Cursor, enabling seamless interaction with real‑world data through simple HTTP calls. NordicMCP aims to simplify AI‑assistant development by offering a centralized, secure gateway to multiple third‑party services.
image: https://nordicmcp.eu/og.png
json_schemas:
- name: PostInvoicesRequest
  property_count: 3
  slug: nordicmcp-eu-post-invoices-request
jsonld:
- class_count: 1
  name: Nordicmcp Eu Context
  property_count: 3
  slug: nordicmcp-eu-context
layout: provider
mcp_servers:
- description: Remote MCP server at nordicmcp.eu.
  name: nordicmcp-eu MCP Server
  slug: nordicmcp-eu-mcp-yml
modified: '2026-10-29'
name: nordicmcp-eu
nav: Providers
network: true
overview: 'nordicmcp-eu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI, Integrations, and Sweden.


  The nordicmcp-eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  nordicmcp-eu''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 20 more developer resources.'
plans:
- name: Nordicmcp Eu Plans Pricing
  plan_count: 3
  slug: nordicmcp-eu-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Nordicmcp Eu Rate Limits
  slug: nordicmcp-eu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: nordicmcp-eu API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: nordicmcp-eu-rules
scopes:
- name: Nordicmcp Eu Scopes
  scope_count: 0
  slug: nordicmcp-eu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 68.2
    catalog_earned_first_party: 20.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 50.0
    discoverability: 56.7
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
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
  name: Nordicmcp Eu Authentication
  slug: nordicmcp-eu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nordicmcp Eu Domain Security
  slug: nordicmcp-eu-domain-security
  summary_line: TLSv1.3
slug: nordicmcp-eu
tags:
- Company
- MCP
- AI
- Integrations
- Sweden
website: https://nordicmcp.eu/
---
