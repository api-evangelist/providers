---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Woz Api Nl Agentic Access
  operation_count: 14
  slug: woz-api-nl-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 1
apis:
- baseURL: https://woz-api.nl
  baseurl_source: declared
  description: Je creditsaldo uitlezen zonder een credit te verbruiken.
  name: woz-api-nl Account API
  slug: woz-api-nl-account-api
- baseURL: https://woz-api.nl
  baseurl_source: declared
  description: 'Zelfde antwoord, drie manieren om het op te vragen: op adrestekst, of op een van de twee vaste BAG-sleutels.'
  name: woz-api-nl Adressen API
  slug: woz-api-nl-adressen-api
- baseURL: https://woz-api.nl
  baseurl_source: declared
  description: 'Een hele lijst adressen of een Excel in een keer: een gratis proef van 5 adressen, de prijs en een betaallink, en na betaling de rijen en het bestand.'
  name: woz-api-nl Lijst API
  slug: woz-api-nl-lijst-api
- baseURL: https://woz-api.nl
  baseurl_source: declared
  description: 'Starten zonder account: een gratis proefsleutel, het e-mailadres van de gebruiker, en een betaallink voor credits. Voor AI-assistenten en scripts.'
  name: woz-api-nl Proef API
  slug: woz-api-nl-proef-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/woz-api-nl/agentic-access/woz-api-nl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/woz-api-nl-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/woz-api-nl/rules/woz-api-nl-rules.yml
  title: ''
  type: Spectral
  url: rules/woz-api-nl-rules.yml
- group: design
  href: https://artifacts.apis.io/woz-api-nl/json-ld/woz-api-nl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/woz-api-nl-context.jsonld
- group: design
  href: https://artifacts.apis.io/woz-api-nl/vocabulary/woz-api-nl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/woz-api-nl-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/woz-api-nl/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/woz-api-nl/data-model/woz-api-nl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/woz-api-nl-data-model.yml
- group: design
  href: https://artifacts.apis.io/woz-api-nl/errors/woz-api-nl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/woz-api-nl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/woz-api-nl/conformance/woz-api-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/woz-api-nl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/woz-api-nl/llms/woz-api-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/woz-api-nl-llms.txt
- group: agent
  href: https://artifacts.apis.io/woz-api-nl/mcp/woz-api-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/woz-api-nl-mcp.yml
- group: auth
  href: https://artifacts.apis.io/woz-api-nl/well-known/woz-api-nl-opendata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/woz-api-nl-opendata-security.txt
- group: agent
  href: https://artifacts.apis.io/woz-api-nl/well-known/woz-api-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/woz-api-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/woz-api-nl/hosts/woz-api-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/woz-api-nl-hosts.yml
- group: build
  href: https://artifacts.apis.io/woz-api-nl/packages/woz-api-nl-packages.yml
  title: ''
  type: SDKs
  url: packages/woz-api-nl-packages.yml
- group: build
  href: https://artifacts.apis.io/woz-api-nl/packages/woz-api-nl-packages.yml
  title: ''
  type: Packages
  url: packages/woz-api-nl-packages.yml
- group: start
  title: ''
  type: Login
  url: https://woz-api.nl/Identity/Account/Login
- group: auth
  href: https://artifacts.apis.io/woz-api-nl/scopes/woz-api-nl-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/woz-api-nl-scopes.yml
- group: auth
  href: https://artifacts.apis.io/woz-api-nl/authentication/woz-api-nl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/woz-api-nl-authentication.yml
- group: auth
  href: https://artifacts.apis.io/woz-api-nl/security/woz-api-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/woz-api-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://woz-api.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://woz-api.nl/docs
- group: docs
  title: ''
  type: APIReference
  url: https://woz-api.nl/swagger/v1/swagger.json
- group: commercial
  title: ''
  type: Pricing
  url: https://woz-api.nl/woz-api-prijs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://woz-api.nl/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://woz-api.nl/privacy
created: '2026-10-31'
description: WOZ API provides developers access to official WOZ property valuation data for Dutch addresses. It offers endpoints for WOZ values, BAG building information, cadastral parcels, energy labels, and subsidy eligibility. Users can obtain up to 10 free credits and pay per address thereafter. The service supports multiple programming languages with client libraries and detailed documentation.
image: https://woz-api.nl/img/og-wozapi.png
json_schemas:
- name: BetaalLinkAntwoord
  property_count: 6
  slug: woz-api-nl-betaal-link-antwoord
- name: LijstAanvraag
  property_count: 5
  slug: woz-api-nl-lijst-aanvraag
- name: LijstAntwoord
  property_count: 15
  slug: woz-api-nl-lijst-antwoord
- name: LijstKolomKeuze
  property_count: 9
  slug: woz-api-nl-lijst-kolom-keuze
- name: ProefSleutelAntwoord
  property_count: 5
  slug: woz-api-nl-proef-sleutel-antwoord
- name: WozApiResponse
  property_count: 11
  slug: woz-api-nl-woz-api-response
jsonld:
- class_count: 43
  name: Woz Api Nl Context
  property_count: 156
  slug: woz-api-nl-context
layout: provider
mcp_servers:
- description: Remote MCP server at woz-api.nl.
  name: woz-api-nl MCP Server
  slug: woz-api-nl-mcp-yml
modified: '2026-10-31'
name: woz-api-nl
nav: Providers
network: true
overview: 'woz-api-nl publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Adressen API, Lijst API, and 1 more. Tagged areas include Real Estate, Netherlands, Property Valuation, and WOZ.


  The woz-api-nl catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  woz-api-nl''s developer surface includes authentication, documentation, API reference, pricing, and 21 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: woz-api-nl API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: woz-api-nl-rules
scopes:
- name: Woz Api Nl Scopes
  scope_count: 2
  slug: woz-api-nl-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 65.2
    developer_ergonomics: 33.8
    discoverability: 56.7
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Woz Api Nl Authentication
  slug: woz-api-nl-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Woz Api Nl Domain Security
  slug: woz-api-nl-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: woz-api-nl
tags:
- Real Estate
- Netherlands
- Property Valuation
- WOZ
website: https://woz-api.nl/
---
