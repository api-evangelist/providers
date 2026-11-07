---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 68.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bergsonne Allgaeu De Agentic Access
  operation_count: 6
  slug: bergsonne-allgaeu-de-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://bergsonne-allgaeu.de/api/booking
  baseurl_source: declared
  description: The Availability API from Hotel Bergsonne Allgäu — 1 operation(s) for availability.
  name: Hotel Bergsonne Allgäu Availability API
  slug: bergsonne-allgaeu-de-availability-api
- baseURL: https://bergsonne-allgaeu.de/api/booking
  baseurl_source: declared
  description: The Bookings API from Hotel Bergsonne Allgäu — 1 operation(s) for bookings.
  name: Hotel Bergsonne Allgäu Bookings API
  slug: bergsonne-allgaeu-de-bookings-api
- baseURL: https://bergsonne-allgaeu.de/api/booking
  baseurl_source: declared
  description: The Fact Sheet API from Hotel Bergsonne Allgäu — 1 operation(s) for fact sheet.
  name: Hotel Bergsonne Allgäu Fact Sheet API
  slug: bergsonne-allgaeu-de-fact-sheet-api
- baseURL: https://bergsonne-allgaeu.de/api/booking
  baseurl_source: declared
  description: The Hotel API from Hotel Bergsonne Allgäu — 1 operation(s) for hotel.
  name: Hotel Bergsonne Allgäu Hotel API
  slug: bergsonne-allgaeu-de-hotel-api
- baseURL: https://bergsonne-allgaeu.de/api/booking
  baseurl_source: declared
  description: The Hotel Bergsonne Allgäu Booking API API from Hotel Bergsonne Allgäu — 1 operation(s) for hotel bergsonne allgäu booking api.
  name: Hotel Bergsonne Allgäu Hotel Bergsonne Allgäu Booking API
  slug: bergsonne-allgaeu-de-hotel-bergsonne-allg-u-booking-api-api
- baseURL: https://bergsonne-allgaeu.de/api/booking
  baseurl_source: declared
  description: The Price Quote API from Hotel Bergsonne Allgäu — 1 operation(s) for price quote.
  name: Hotel Bergsonne Allgäu Price Quote API
  slug: bergsonne-allgaeu-de-price-quote-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/agentic-access/bergsonne-allgaeu-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bergsonne-allgaeu-de-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/rules/bergsonne-allgaeu-de-rules.yml
  title: ''
  type: Spectral
  url: rules/bergsonne-allgaeu-de-rules.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/json-ld/bergsonne-allgaeu-de-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bergsonne-allgaeu-de-context.jsonld
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/vocabulary/bergsonne-allgaeu-de-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bergsonne-allgaeu-de-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/data-model/bergsonne-allgaeu-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bergsonne-allgaeu-de-data-model.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/conventions/bergsonne-allgaeu-de-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bergsonne-allgaeu-de-conventions.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/conventions/bergsonne-allgaeu-de-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bergsonne-allgaeu-de-conventions.yml
- group: start
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/sandbox/bergsonne-allgaeu-de-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bergsonne-allgaeu-de-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/authentication/bergsonne-allgaeu-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bergsonne-allgaeu-de-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/scopes/bergsonne-allgaeu-de-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bergsonne-allgaeu-de-scopes.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/errors/bergsonne-allgaeu-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bergsonne-allgaeu-de-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/conformance/bergsonne-allgaeu-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bergsonne-allgaeu-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/llms/bergsonne-allgaeu-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bergsonne-allgaeu-de-llms.txt
- group: other
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/a2a/bergsonne-allgaeu-de-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bergsonne-allgaeu-de-a2a.yml
- group: build
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/mcp/bergsonne-allgaeu-de-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bergsonne-allgaeu-de-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/mcp/bergsonne-allgaeu-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bergsonne-allgaeu-de-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/well-known/bergsonne-allgaeu-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bergsonne-allgaeu-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/hosts/bergsonne-allgaeu-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bergsonne-allgaeu-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/vendors/bergsonne-allgaeu-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bergsonne-allgaeu-de-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bergsonne-allgaeu-de/security/bergsonne-allgaeu-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bergsonne-allgaeu-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bergsonne-allgaeu.de/
- group: docs
  title: ''
  type: APIReference
  url: https://bergsonne-allgaeu.de/api/openapi
- group: docs
  title: ''
  type: Documentation
  url: https://bergsonne-allgaeu.de/developers
- group: operate
  title: ''
  type: Support
  url: https://bergsonne-allgaeu.de/kontakt
- group: company
  title: ''
  type: Blog
  url: https://bergsonne-allgaeu.de/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bergsonne-allgaeu.de/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bergsonne-allgaeu.de/datenschutz
created: '2026-11-02'
description: Hotel Bergsonne Allgäu is a smart retreat located on the Imberg plateau in Sonthofen, Germany. Offering modern Alpine atmosphere, the hotel provides rooms for workations, solo trips, couples, and pet‑friendly vacations. Guests enjoy direct booking discounts, spacious rooms with wooden details, a lounge, and easy access to the surrounding Alpine landscape. The property emphasizes freedom, tranquility, and a blend of tradition with contemporary comfort.
image: https://bergsonne-allgaeu.de/cdn-cgi/image/format=auto,quality=65,width=1920/images/hero/hero-summer.jpg
jsonld:
- class_count: 1
  name: Bergsonne Allgaeu De Context
  property_count: 5
  slug: bergsonne-allgaeu-de-context
layout: provider
mcp_servers:
- description: Remote MCP server at bergsonne-allgaeu.de.
  name: Hotel Bergsonne Allgäu MCP Server
  slug: bergsonne-allgaeu-de-mcp-yml
modified: '2026-11-02'
name: Hotel Bergsonne Allgäu
nav: Providers
network: true
overview: 'Hotel Bergsonne Allgäu publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Fact Sheet API, and 3 more. Tagged areas include Hotels, Hospitality, Travel, Germany, and Allgäu.


  The Hotel Bergsonne Allgäu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hotel Bergsonne Allgäu''s developer surface includes sandbox, authentication, API reference, documentation, support, engineering blog, and 22 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Hotel Bergsonne Allgäu API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: bergsonne-allgaeu-de-rules
scopes:
- name: Bergsonne Allgaeu De Scopes
  scope_count: 3
  slug: bergsonne-allgaeu-de-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 54.4
    developer_ergonomics: 32.7
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bergsonne Allgaeu De Authentication
  slug: bergsonne-allgaeu-de-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bergsonne Allgaeu De Domain Security
  slug: bergsonne-allgaeu-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: create-booking
  slug: create-booking
- name: get-price-quote
  slug: get-price-quote
- name: hotel-facts
  slug: hotel-facts
- name: search-availability
  slug: search-availability
slug: bergsonne-allgaeu-de
tags:
- Hotels
- Hospitality
- Travel
- Germany
- Allgäu
- Retreat
website: https://bergsonne-allgaeu.de/
---
