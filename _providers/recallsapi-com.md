---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Recallsapi Com Agentic Access
  operation_count: 31
  slug: recallsapi-com-agentic-access
  summary_line: 31 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Account API from recallsapi-com — 1 operation(s) for account.
  name: recallsapi-com Account API
  slug: recallsapi-com-account-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Alerts API from recallsapi-com — 1 operation(s) for alerts.
  name: recallsapi-com Alerts API
  slug: recallsapi-com-alerts-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Billing API from recallsapi-com — 2 operation(s) for billing.
  name: recallsapi-com Billing API
  slug: recallsapi-com-billing-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Catalogs API from recallsapi-com — 7 operation(s) for catalogs.
  name: recallsapi-com Catalogs API
  slug: recallsapi-com-catalogs-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Check API from recallsapi-com — 2 operation(s) for check.
  name: recallsapi-com Check API
  slug: recallsapi-com-check-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Credits API from recallsapi-com — 2 operation(s) for credits.
  name: recallsapi-com Credits API
  slug: recallsapi-com-credits-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Health API from recallsapi-com — 1 operation(s) for health.
  name: recallsapi-com Health API
  slug: recallsapi-com-health-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Keys API from recallsapi-com — 1 operation(s) for keys.
  name: recallsapi-com Keys API
  slug: recallsapi-com-keys-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Mcp API from recallsapi-com — 1 operation(s) for mcp.
  name: recallsapi-com MCP API
  slug: recallsapi-com-mcp-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Recalls API from recallsapi-com — 2 operation(s) for recalls.
  name: recallsapi-com Recalls API
  slug: recallsapi-com-recalls-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Receipts API from recallsapi-com — 2 operation(s) for receipts.
  name: recallsapi-com Receipts API
  slug: recallsapi-com-receipts-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Signals API from recallsapi-com — 2 operation(s) for signals.
  name: recallsapi-com Signals API
  slug: recallsapi-com-signals-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The Vehicles API from recallsapi-com — 2 operation(s) for vehicles.
  name: recallsapi-com Vehicles API
  slug: recallsapi-com-vehicles-api
- baseURL: https://api.recallsapi.com
  baseurl_source: declared
  description: The .well Known API from recallsapi-com — 1 operation(s) for .well known.
  name: recallsapi-com .well Known API
  slug: recallsapi-com-well-known-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/recallsapi-com/agentic-access/recallsapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recallsapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/recallsapi-com/plans/recallsapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/recallsapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/recallsapi-com/rules/recallsapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/recallsapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/recallsapi-com/json-ld/recallsapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/recallsapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/recallsapi-com/vocabulary/recallsapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/recallsapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/recallsapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/recallsapi-com/data-model/recallsapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/recallsapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/recallsapi-com/conventions/recallsapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/recallsapi-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://recallsapi.com/privacy#security
- group: auth
  href: https://artifacts.apis.io/recallsapi-com/authentication/recallsapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recallsapi-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.recallsapi.com/v1/health
- group: design
  href: https://artifacts.apis.io/recallsapi-com/lifecycle/recallsapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/recallsapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/recallsapi-com/errors/recallsapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/recallsapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/recallsapi-com/conformance/recallsapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recallsapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/recallsapi-com/llms/recallsapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recallsapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/recallsapi-com/mcp/recallsapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/recallsapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/recallsapi-com/mcp/recallsapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/recallsapi-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/recallsapi-com/well-known/recallsapi-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recallsapi-com-security.txt
- group: agent
  href: https://artifacts.apis.io/recallsapi-com/well-known/recallsapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recallsapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/recallsapi-com/hosts/recallsapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recallsapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/recallsapi-com/vendors/recallsapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recallsapi-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://recallsapi.com/news
- group: auth
  href: https://artifacts.apis.io/recallsapi-com/security/recallsapi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/recallsapi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/recallsapi-com/security/recallsapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recallsapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://recallsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://recallsapi.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://recallsapi.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://recallsapi.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://recallsapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recallsapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recallsapi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://recallsapi.com/
- group: start
  title: ''
  type: SignUp
  url: https://recallsapi.com/pricing
created: '2026-10-31'
description: recallsapi.com provides a US recalls API and monitoring service for marketplace sellers. It aggregates recall records from nine US agencies—including CPSC, FDA, NHTSA, US Coast Guard, FAA—and offers alerts via email, signed webhooks, and a REST API. The service is sold by PrimeZen LLC and supports integration with Amazon, Walmart, eBay, and Shopify platforms. Developers can obtain an API key instantly, explore quickstart guides, and use the MCP server for bulk monitoring. The platform emphasizes compliance, safety, and easy integration for e‑commerce businesses.
jsonld:
- class_count: 10
  name: Recallsapi Com Context
  property_count: 51
  slug: recallsapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.recallsapi.com requiring an API key.
  name: recallsapi-com MCP Server
  slug: recallsapi-com-mcp-yml
modified: '2026-10-31'
name: recallsapi-com
nav: Providers
network: true
overview: 'recallsapi-com publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Alerts API, Billing API, and 11 more. Tagged areas include Company, API, Recall, E-commerce, and Safety.


  The recallsapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  recallsapi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, signup flow, and 26 more developer resources.'
plans:
- name: Recallsapi Com Plans Pricing
  plan_count: 4
  slug: recallsapi-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Recallsapi Com Rate Limits
  slug: recallsapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: recallsapi-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: recallsapi-com-rules
scopes:
- name: Recallsapi Com Scopes
  scope_count: 0
  slug: recallsapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 77.5
    catalog_earned_first_party: 0.0
    catalog_gap: 37.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 53.6
    developer_ergonomics: 51.7
    discoverability: 63.3
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Recallsapi Com Authentication
  slug: recallsapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Recallsapi Com Domain Security
  slug: recallsapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Recallsapi Com Vulnerability Disclosure
  slug: recallsapi-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: check-product
  slug: recallsapi-com-check-product
- name: check-vehicle
  slug: recallsapi-com-check-vehicle
- name: get-recall
  slug: recallsapi-com-get-recall
- name: search-recalls
  slug: recallsapi-com-search-recalls
slug: recallsapi-com
tags:
- Company
- API
- Recall
- E-commerce
- Safety
- US-Agencies
website: https://recallsapi.com/
---
