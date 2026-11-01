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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Acuris Geo Com Agentic Access
  operation_count: 23
  slug: acuris-geo-com-agentic-access
  summary_line: 23 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Key check and account-related helpers
  name: acuris-geo-com Account API
  slug: acuris-geo-com-account-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Stripe-hosted self-serve subscription checkout
  name: acuris-geo-com Billing API
  slug: acuris-geo-com-billing-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Client configuration for forms
  name: acuris-geo-com Config API
  slug: acuris-geo-com-config-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Rooftop / reference-database geocoding
  name: acuris-geo-com Geocoding API
  slug: acuris-geo-com-geocoding-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: UK postcode → all addresses (Royal Mail PAF)
  name: acuris-geo-com Postcode lookup API
  slug: acuris-geo-com-postcode-lookup-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Autocomplete-style suggestions
  name: acuris-geo-com Suggest API
  slug: acuris-geo-com-suggest-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Address validation and free-tier transactions
  name: acuris-geo-com Validation API
  slug: acuris-geo-com-validation-api
- baseURL: https://api.acuris-geo.com
  baseurl_source: declared
  description: Stable `/v1/*` mirrors of the core endpoints. Behaviour is identical to the unversioned routes above — same engine, same response schema — but the path is guaranteed not to change, so prefer these for
  name: acuris-geo-com Versioned aliases (v1) API
  slug: acuris-geo-com-versioned-aliases-v1-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/acuris-geo-com/agentic-access/acuris-geo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acuris-geo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/acuris-geo-com/plans/acuris-geo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acuris-geo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/acuris-geo-com/rules/acuris-geo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/acuris-geo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/acuris-geo-com/json-ld/acuris-geo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/acuris-geo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/acuris-geo-com/vocabulary/acuris-geo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acuris-geo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/acuris-geo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/acuris-geo-com/data-model/acuris-geo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acuris-geo-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/acuris-geo-com/authentication/acuris-geo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acuris-geo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/acuris-geo-com/errors/acuris-geo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acuris-geo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/acuris-geo-com/conformance/acuris-geo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acuris-geo-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/acuris-geo-com/mcp/acuris-geo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/acuris-geo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/acuris-geo-com/mcp/acuris-geo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acuris-geo-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/acuris-geo-com/hosts/acuris-geo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acuris-geo-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/acuris-geo-com/packages/acuris-geo-com-packages.yml
  title: ''
  type: SDKs
  url: packages/acuris-geo-com-packages.yml
- group: build
  href: https://artifacts.apis.io/acuris-geo-com/packages/acuris-geo-com-packages.yml
  title: ''
  type: Packages
  url: packages/acuris-geo-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acuris-geo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://api.acuris-geo.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://api.acuris-geo.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://api.acuris-geo.com/console
- group: start
  title: ''
  type: Login
  url: https://api.acuris-geo.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.acuris-geo.com/team/
- group: auth
  href: https://artifacts.apis.io/acuris-geo-com/security/acuris-geo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acuris-geo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acuris-geo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.acuris-geo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.acuris-geo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.acuris-geo.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Acuris-GmbH
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acuris-geo.com/privacy-policy/
created: '2026-10-30'
description: Acuris Geo provides developer APIs for global address validation and geocoding across more than 240 countries, delivering point-coordinate precision, forward and reverse geocoding, UK Royal Mail PAF data (UDPRN/UPRN), and eIDAS 2.0 EUDI Wallet verification. The service offers real-time responses and includes an open-source MCP server for AI assistants such as Claude, Cursor, and Copilot. It serves worldwide customers seeking reliable location data and compliance-ready address services.
image: https://www.acuris-geo.com/wp-content/uploads/2026/05/acuris-mark.png
json_schemas:
- name: DevKeyResponse
  property_count: 14
  slug: acuris-geo-com-dev-key-response
- name: ForwardGeocodeResponse
  property_count: 27
  slug: acuris-geo-com-forward-geocode-response
- name: GeocodeResponse
  property_count: 27
  slug: acuris-geo-com-geocode-response
- name: ReverseResponse
  property_count: 20
  slug: acuris-geo-com-reverse-response
- name: SuggestItem
  property_count: 0
  slug: acuris-geo-com-suggest-item
- name: ValidateResponse
  property_count: 70
  slug: acuris-geo-com-validate-response
jsonld:
- class_count: 28
  name: Acuris Geo Com Context
  property_count: 193
  slug: acuris-geo-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.acuris-geo.com requiring an API key.
  name: acuris-geo-com MCP Server
  slug: acuris-geo-com-mcp-yml
modified: '2026-10-30'
name: acuris-geo-com
nav: Providers
network: true
overview: 'acuris-geo-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Config API, and 5 more. Tagged areas include Company, Geocoding, Address-Validation, Location-Data, and API.


  The acuris-geo-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  acuris-geo-com''s developer surface includes authentication, support, sandbox, API reference, getting-started guide, and 23 more developer resources.'
plans:
- name: Acuris Geo Com Plans Pricing
  plan_count: 1
  slug: acuris-geo-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Acuris Geo Com Rate Limits
  slug: acuris-geo-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: acuris-geo-com API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: acuris-geo-com-rules
scopes:
- name: Acuris Geo Com Scopes
  scope_count: 0
  slug: acuris-geo-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.2
    catalog_earned_first_party: 0.0
    catalog_gap: 32.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.2
    contract_governance: 70.9
    contract_quality: 61.1
    developer_ergonomics: 66.0
    discoverability: 66.7
    operational_transparency: 21.1
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
  name: Acuris Geo Com Authentication
  slug: acuris-geo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Acuris Geo Com Domain Security
  slug: acuris-geo-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: geocode-address
  slug: acuris-geo-com-geocode_address
- name: reverse-geocode
  slug: acuris-geo-com-reverse_geocode
- name: suggest-addresses
  slug: acuris-geo-com-suggest
- name: validate-address
  slug: acuris-geo-com-validate_address
slug: acuris-geo-com
tags:
- Company
- Geocoding
- Address-Validation
- Location-Data
- API
website: https://acuris-geo.com/
---
