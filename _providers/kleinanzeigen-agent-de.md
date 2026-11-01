---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kleinanzeigen Agent De Agentic Access
  operation_count: 14
  slug: kleinanzeigen-agent-de-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://api.kleinanzeigen-agent.de/api/v2/kleinanzeigen
  baseurl_source: declared
  description: The Ads API from kleinanzeigen-agent-de — 4 operation(s) for ads.
  name: kleinanzeigen-agent-de Ads API
  slug: kleinanzeigen-agent-de-ads-api
- baseURL: https://api.kleinanzeigen-agent.de/api/v2/kleinanzeigen
  baseurl_source: declared
  description: The Categories API from kleinanzeigen-agent-de — 3 operation(s) for categories.
  name: kleinanzeigen-agent-de Categories API
  slug: kleinanzeigen-agent-de-categories-api
- baseURL: https://api.kleinanzeigen-agent.de/api/v2/kleinanzeigen
  baseurl_source: declared
  description: The History API from kleinanzeigen-agent-de — 1 operation(s) for history.
  name: kleinanzeigen-agent-de History API
  slug: kleinanzeigen-agent-de-history-api
- baseURL: https://api.kleinanzeigen-agent.de/api/v2/kleinanzeigen
  baseurl_source: declared
  description: The Locations API from kleinanzeigen-agent-de — 2 operation(s) for locations.
  name: kleinanzeigen-agent-de Locations API
  slug: kleinanzeigen-agent-de-locations-api
- baseURL: https://api.kleinanzeigen-agent.de/api/v2/kleinanzeigen
  baseurl_source: declared
  description: The Search API from kleinanzeigen-agent-de — 2 operation(s) for search.
  name: kleinanzeigen-agent-de Search API
  slug: kleinanzeigen-agent-de-search-api
- baseURL: https://api.kleinanzeigen-agent.de/api/v2/kleinanzeigen
  baseurl_source: declared
  description: The Sellers API from kleinanzeigen-agent-de — 2 operation(s) for sellers.
  name: kleinanzeigen-agent-de Sellers API
  slug: kleinanzeigen-agent-de-sellers-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/agentic-access/kleinanzeigen-agent-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kleinanzeigen-agent-de-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/rules/kleinanzeigen-agent-de-rules.yml
  title: ''
  type: Spectral
  url: rules/kleinanzeigen-agent-de-rules.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/json-ld/kleinanzeigen-agent-de-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kleinanzeigen-agent-de-context.jsonld
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/vocabulary/kleinanzeigen-agent-de-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kleinanzeigen-agent-de-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/data-model/kleinanzeigen-agent-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kleinanzeigen-agent-de-data-model.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/conventions/kleinanzeigen-agent-de-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kleinanzeigen-agent-de-conventions.yml
- group: auth
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/authentication/kleinanzeigen-agent-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kleinanzeigen-agent-de-authentication.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/errors/kleinanzeigen-agent-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kleinanzeigen-agent-de-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/conformance/kleinanzeigen-agent-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kleinanzeigen-agent-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/llms/kleinanzeigen-agent-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kleinanzeigen-agent-de-llms.txt
- group: other
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/a2a/kleinanzeigen-agent-de-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kleinanzeigen-agent-de-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/mcp/kleinanzeigen-agent-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kleinanzeigen-agent-de-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/well-known/kleinanzeigen-agent-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kleinanzeigen-agent-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/hosts/kleinanzeigen-agent-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kleinanzeigen-agent-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/vendors/kleinanzeigen-agent-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kleinanzeigen-agent-de-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://kleinanzeigen-agent.de/webhooks
- group: start
  title: ''
  type: Sandbox
  url: https://kleinanzeigen-agent.de/app/sandbox
- group: auth
  href: https://artifacts.apis.io/kleinanzeigen-agent-de/security/kleinanzeigen-agent-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kleinanzeigen-agent-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kleinanzeigen-agent.de/
- group: docs
  title: ''
  type: Documentation
  url: https://kleinanzeigen-agent.de/dokumentation
- group: company
  title: ''
  type: Blog
  url: https://kleinanzeigen-agent.de/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kleinanzeigen-agent.de/branchen
- group: start
  title: ''
  type: SignUp
  url: https://kleinanzeigen-agent.de/anmelden
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kleinanzeigen-agent.de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kleinanzeigen-agent.de/datenschutz
- group: operate
  title: ''
  type: Support
  url: https://kleinanzeigen-agent.de/impressum
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://kleinanzeigen-agent.de/openapi.json
  - status: 401
    url: https://api.kleinanzeigen-agent.de/mcp
  - status: 200
    url: https://kleinanzeigen-agent.de/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Kleinanzeigen Agent provides a RESTful API that gives developers real-time access to German classified ads data. The API enables search, detailed ad retrieval, seller information, category and location queries, as well as webhook notifications for new listings. It supports API-Key authentication, offers rate-limited credits, and is used for price comparison, market analysis, and automation without the need for custom scraping. Documentation, quick-start guides, and SDKs are available on the provider’s site.
image: https://kleinanzeigen-agent.de/_next/image?url=%2Flogo.png&w=256&q=75
json_schemas:
- name: SuccessResponse
  property_count: 4
  slug: kleinanzeigen-agent-de-success-response
jsonld:
- class_count: 2
  name: Kleinanzeigen Agent De Context
  property_count: 6
  slug: kleinanzeigen-agent-de-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.kleinanzeigen-agent.de.
  name: kleinanzeigen-agent-de MCP Server
  slug: kleinanzeigen-agent-de-mcp-yml
modified: '2026-10-30'
name: kleinanzeigen-agent-de
nav: Providers
network: true
overview: 'kleinanzeigen-agent-de publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ads API, Categories API, History API, and 3 more. Tagged areas include API, Search, Monitoring, Market-Analysis, and Germany.


  The kleinanzeigen-agent-de catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kleinanzeigen-agent-de''s developer surface includes authentication, sandbox, documentation, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
plans:
- name: Kleinanzeigen Agent De Plans Pricing
  plan_count: 0
  slug: kleinanzeigen-agent-de-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Kleinanzeigen Agent De Rate Limits
  slug: kleinanzeigen-agent-de-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: kleinanzeigen-agent-de API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: kleinanzeigen-agent-de-rules
scopes:
- name: Kleinanzeigen Agent De Scopes
  scope_count: 0
  slug: kleinanzeigen-agent-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.1
    catalog_earned_first_party: 0.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 51.1
    developer_ergonomics: 42.1
    discoverability: 65.0
    operational_transparency: 7.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kleinanzeigen Agent De Authentication
  slug: kleinanzeigen-agent-de-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kleinanzeigen Agent De Domain Security
  slug: kleinanzeigen-agent-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: get-ad-details
  slug: kleinanzeigen-agent-de-get-ad-details
- name: get-seller-ads
  slug: kleinanzeigen-agent-de-get-seller-ads
- name: search-listings
  slug: kleinanzeigen-agent-de-search-listings
slug: kleinanzeigen-agent-de
tags:
- API
- Search
- Monitoring
- Market-Analysis
- Germany
- Kleinanzeigen
website: https://kleinanzeigen-agent.de/
---
