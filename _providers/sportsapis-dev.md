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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Directory comparing 50+ sports odds and data APIs for developers building betting apps, odds comparison tools, and sports analytics platforms.
  name: Sports Odds API Directory
  slug: sports-odds-api-directory
- baseURL: https://api.rapidoddsapi.com
  baseurl_source: declared
  description: 'SportsAPIs.dev API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: SportsAPIs.dev API
  slug: sportsapis-dev-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/sportsapis-dev/rules/sportsapis-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/sportsapis-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/sportsapis-dev/json-ld/sportsapis-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sportsapis-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/sportsapis-dev/vocabulary/sportsapis-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sportsapis-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sportsapis-dev/data-model/sportsapis-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sportsapis-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sportsapis-dev/authentication/sportsapis-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sportsapis-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/sportsapis-dev/conformance/sportsapis-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sportsapis-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sportsapis-dev/llms/sportsapis-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sportsapis-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/sportsapis-dev/hosts/sportsapis-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sportsapis-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/sportsapis-dev/vendors/sportsapis-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sportsapis-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sportsapis.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sportsapis.dev/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://sportsapis.dev/sports-mcp-servers#sportsapis-mcp
- group: auth
  href: https://artifacts.apis.io/sportsapis-dev/security/sportsapis-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sportsapis-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sportsapis.dev
coverage:
  checked: '2026-10-18'
  detail: The site provides HTML documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://sportsapis.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: SportsAPIs.dev curates a comprehensive directory of over 45 sports odds and sports data APIs, providing detailed reviews, feature comparisons, and integration guidance for developers building betting applications, odds comparison tools, and sports analytics platforms. The site offers free read‑only access to its Multi‑Channel Platform (MCP) registry, allowing users to explore API offerings without authentication.
image: https://sportsapis.dev/assets/images/og/og-index.webp
json_schemas:
- name: GetV1DataFilenameResponse
  property_count: 4
  slug: sportsapis-dev-get-v1-data-filename-response
- name: PostBetbuilderPriceRequest
  property_count: 1
  slug: sportsapis-dev-post-betbuilder-price-request
- name: PostBetbuilderPriceResponse
  property_count: 1
  slug: sportsapis-dev-post-betbuilder-price-response
- name: PostV1SportsSportEventsIdSgpRequest
  property_count: 1
  slug: sportsapis-dev-post-v1-sports-sport-events-id-sgp-request
jsonld:
- class_count: 4
  name: Sportsapis Dev Context
  property_count: 7
  slug: sportsapis-dev-context
layout: provider
modified: '2026-10-17'
name: SportsAPIs.dev
nav: Providers
network: true
overview: 'SportsAPIs.dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Odds, Data, and Gambling.


  The SportsAPIs.dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SportsAPIs.dev''s developer surface includes authentication, getting-started guide, and 12 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: SportsAPIs.dev API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: sportsapis-dev-rules
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 24.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 17
      marker_coverage: 100.0
      total: 17
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sportsapis Dev Authentication
  slug: sportsapis-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sportsapis Dev Domain Security
  slug: sportsapis-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sportsapis-dev
tags:
- Company
- Sports
- Odds
- Data
- Gambling
website: https://sportsapis.dev
---
