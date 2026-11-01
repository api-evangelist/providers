---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Professional astrology calculation API powered by Swiss Ephemeris. Compute natal charts, synastry, progressions, directions, transits, Human Design, and 80+ other calculation types via a simple REST A
  name: AstroWay Calculation API
  slug: calculation-api
- baseURL: https://api.astroway.info/v1
  baseurl_source: declared
  description: Professional astrology calculation API powered by Swiss Ephemeris. Compute natal charts, synastry, progressions, directions, transits, Human Design, and 80+ other calculation types via a simple REST A
  name: AstroWay Calculation API V1 API
  slug: astroway-calculation-api-v1-api
- baseURL: https://api.astroway.info/v1
  baseurl_source: declared
  description: Professional astrology calculation API powered by Swiss Ephemeris. Compute natal charts, synastry, progressions, directions, transits, Human Design, and 80+ other calculation types via a simple REST A
  name: astroway-info Openapi API
  slug: astroway-info-openapi-api
artifact_total: 14
asyncapis:
- description: ''
  name: Astroway Info Webhooks
  slug: astroway-info-webhooks
common:
- group: design
  href: https://artifacts.apis.io/astroway-info/rules/astroway-info-rules.yml
  title: ''
  type: Spectral
  url: rules/astroway-info-rules.yml
- group: design
  href: https://artifacts.apis.io/astroway-info/json-ld/astroway-info-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/astroway-info-context.jsonld
- group: design
  href: https://artifacts.apis.io/astroway-info/vocabulary/astroway-info-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astroway-info-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/astroway-info/asyncapi/astroway-info-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/astroway-info-webhooks.yml
- group: design
  href: https://artifacts.apis.io/astroway-info/conformance/astroway-info-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astroway-info-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astroway-info/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/astroway-info/data-model/astroway-info-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astroway-info-data-model.yml
- group: design
  href: https://artifacts.apis.io/astroway-info/errors/astroway-info-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astroway-info-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/astroway-info/llms/astroway-info-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astroway-info-llms.txt
- group: build
  href: https://artifacts.apis.io/astroway-info/mcp/astroway-info-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/astroway-info-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/astroway-info/mcp/astroway-info-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/astroway-info-mcp.yml
- group: auth
  href: https://artifacts.apis.io/astroway-info/well-known/astroway-info-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/astroway-info-api-security.txt
- group: agent
  href: https://artifacts.apis.io/astroway-info/well-known/astroway-info-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astroway-info-well-known.yml
- group: other
  href: https://artifacts.apis.io/astroway-info/hosts/astroway-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astroway-info-hosts.yml
- group: other
  href: https://artifacts.apis.io/astroway-info/vendors/astroway-info-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astroway-info-vendors.yml
- group: build
  href: https://artifacts.apis.io/astroway-info/packages/astroway-info-packages.yml
  title: ''
  type: SDKs
  url: packages/astroway-info-packages.yml
- group: build
  href: https://artifacts.apis.io/astroway-info/packages/astroway-info-packages.yml
  title: ''
  type: Packages
  url: packages/astroway-info-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://api.astroway.info/trust/
- group: start
  title: ''
  type: Login
  url: https://app.astroway.info/my/login
- group: commercial
  title: ''
  type: Pricing
  url: https://app.astroway.info/en/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.astroway.info/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astroway
- group: auth
  href: https://artifacts.apis.io/astroway-info/security/astroway-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astroway-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astroway.info/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astroway.info/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astroway.info/politika-konfidentsialnosti/
- group: company
  title: ''
  type: Blog
  url: https://astroway.info/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://astroway.info/developer/
- group: operate
  title: ''
  type: Support
  url: https://astroway.info/support/
created: '2026-10-29'
description: Astro Way is an online astrology portal offering horoscopes, natal charts, and astrological forecasts in multiple languages. The service provides daily, weekly, and monthly horoscopes, personalized birth chart calculations, and a range of astrological content for users seeking guidance. Operated from the astroway.info domain, the platform serves a Ukrainian‑speaking audience and includes multilingual support.
image: https://astroway.info/wp-content/themes/astroway/theme/img/og-default.jpg
json_schemas:
- name: BiWheelRequest
  property_count: 0
  slug: astroway-info-bi-wheel-request
- name: GenerateReport
  property_count: 12
  slug: astroway-info-generate-report
- name: SynastryReport
  property_count: 4
  slug: astroway-info-synastry-report
- name: TriWheel
  property_count: 4
  slug: astroway-info-tri-wheel
- name: WheelWesternRequest
  property_count: 0
  slug: astroway-info-wheel-western-request
- name: WheelWestern
  property_count: 0
  slug: astroway-info-wheel-western
jsonld:
- class_count: 120
  name: Astroway Info Context
  property_count: 194
  slug: astroway-info-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.astroway.info.
  name: astroway-info MCP Server
  slug: astroway-info-mcp-yml
modified: '2026-10-29'
name: astroway-info
nav: Providers
network: true
overview: 'astroway-info publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including AstroWay Calculation API V1 API, Openapi API, and 1 more. Tagged areas include Astrology, Horoscope, NatalChart, Ukrainian, and OnlinePortal.


  The astroway-info catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  astroway-info''s developer surface includes pricing, documentation, engineering blog, support, and 25 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: astroway-info API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: astroway-info-rules
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 70.8
    developer_ergonomics: 58.8
    discoverability: 56.7
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 60
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astroway Info Domain Security
  slug: astroway-info-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astroway-info
tags:
- Astrology
- Horoscope
- NatalChart
- Ukrainian
- OnlinePortal
website: https://astroway.info/
---
