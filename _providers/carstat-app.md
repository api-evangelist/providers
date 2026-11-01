---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Carstat App Agentic Access
  operation_count: 16
  slug: carstat-app-agentic-access
  summary_line: 16 operations
api_count: 2
apis:
- baseURL: https://api.carstat.app
  baseurl_source: declared
  description: Browse and retrieve NHTSA recall campaigns. Use the discovery endpoints (years → makes → models) to navigate available data, then fetch all recall campaigns for a specific vehicle.
  name: carstat-app Recalls API
  slug: carstat-app-recalls-api
- baseURL: https://api.carstat.app
  baseurl_source: declared
  description: Browse and retrieve NHTSA 5-star crash test ratings. Use the discovery endpoints (years → makes → models) to navigate available data, then fetch frontal, side, pole, and rollover ratings for a specifi
  name: carstat-app Safety Ratings API
  slug: carstat-app-safety-ratings-api
- baseURL: https://api.carstat.app
  baseurl_source: declared
  description: Retrieve full 250+ field engineering specifications. Browse years → makes → models → modifications to get a modification_id, then fetch the full spec sheet. Also supports metric-based search.
  name: carstat-app Vehicle Specifications API
  slug: carstat-app-vehicle-specifications-api
- baseURL: https://api.carstat.app
  baseurl_source: declared
  description: Decode a VIN into its manufacturer, model, model year, origin and build plant. It answers for vehicle classes the specification catalog does not cover.
  name: carstat-app VIN Decoding API
  slug: carstat-app-vin-decoding-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/carstat-app/agentic-access/carstat-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carstat-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/carstat-app/plans/carstat-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carstat-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carstat-app/rules/carstat-app-rules.yml
  title: ''
  type: Spectral
  url: rules/carstat-app-rules.yml
- group: design
  href: https://artifacts.apis.io/carstat-app/json-ld/carstat-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carstat-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/carstat-app/vocabulary/carstat-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carstat-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carstat-app/data-model/carstat-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carstat-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/carstat-app/cli/carstat-app-cli.yml
  title: ''
  type: CLI
  url: cli/carstat-app-cli.yml
- group: operate
  href: https://artifacts.apis.io/carstat-app/changelog/carstat-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/carstat-app-changelog.yml
- group: design
  href: https://artifacts.apis.io/carstat-app/errors/carstat-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carstat-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carstat-app/conformance/carstat-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carstat-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carstat-app/llms/carstat-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carstat-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/carstat-app/well-known/carstat-app-cursor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carstat-app-cursor-security.txt
- group: agent
  href: https://artifacts.apis.io/carstat-app/well-known/carstat-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carstat-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/carstat-app/hosts/carstat-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carstat-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/carstat-app/vendors/carstat-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carstat-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carstat.app/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://carstat.app/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carstat.app/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://carstat.app/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.openai.com/api/docs/guides/custom-mcp-server
- group: docs
  title: ''
  type: APIReference
  url: https://carstat.app/api-docs
- group: auth
  href: https://artifacts.apis.io/carstat-app/authentication/carstat-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carstat-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/carstat-app/security/carstat-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carstat-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carstat.app/
created: '2026-10-30'
description: Carstat provides a comprehensive vehicle data API offering specifications, VIN decoding, NHTSA recall information, and safety ratings. The RESTful service and native MCP server enable developers and AI agents to retrieve detailed car make, model, configuration, and safety data across global markets, supporting prepaid credit plans without monthly subscriptions.
image: https://carstat.app/social-preview.png
jsonld:
- class_count: 10
  name: Carstat App Context
  property_count: 67
  slug: carstat-app-context
layout: provider
modified: '2026-10-30'
name: carstat-app
nav: Providers
network: true
overview: 'carstat-app publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Recalls API, Safety Ratings API, Vehicle Specifications API, and 1 more. Tagged areas include Company, Automotive, Data, API, and Vehicle.


  The carstat-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  carstat-app''s developer surface includes CLI, changelog, pricing, getting-started guide, API reference, authentication, and 18 more developer resources.'
plans:
- name: Carstat App Plans Pricing
  plan_count: 2
  slug: carstat-app-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: carstat-app API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: carstat-app-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 75.9
    catalog_earned_first_party: 0.0
    catalog_gap: 39.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 79.1
    contract_quality: 57.5
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 42.1
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
  name: Carstat App Authentication
  slug: carstat-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carstat App Domain Security
  slug: carstat-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carstat-app
tags:
- Company
- Automotive
- Data
- API
- Vehicle
website: https://carstat.app/
---
