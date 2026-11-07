---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bright Sky Agentic Access
  operation_count: 6
  slug: bright-sky-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- baseURL: https://api.brightsky.dev
  baseurl_source: declared
  description: The Alerts API from Bright Sky — 1 operation(s) for alerts.
  name: Bright Sky Alerts API
  slug: bright-sky-alerts-api
- baseURL: https://api.brightsky.dev
  baseurl_source: declared
  description: The Current Weather API from Bright Sky — 1 operation(s) for current weather.
  name: Bright Sky Current Weather API
  slug: bright-sky-current-weather-api
- baseURL: https://api.brightsky.dev
  baseurl_source: declared
  description: The Internals API from Bright Sky — 2 operation(s) for internals.
  name: Bright Sky Internals API
  slug: bright-sky-internals-api
- baseURL: https://api.brightsky.dev
  baseurl_source: declared
  description: The Radar API from Bright Sky — 1 operation(s) for radar.
  name: Bright Sky Radar API
  slug: bright-sky-radar-api
- baseURL: https://api.brightsky.dev
  baseurl_source: declared
  description: The Weather API from Bright Sky — 1 operation(s) for weather.
  name: Bright Sky Weather API
  slug: bright-sky-weather-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/bright-sky/agentic-access/bright-sky-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bright-sky-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bright-sky/rules/bright-sky-rules.yml
  title: ''
  type: Spectral
  url: rules/bright-sky-rules.yml
- group: design
  href: https://artifacts.apis.io/bright-sky/json-ld/bright-sky-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bright-sky-context.jsonld
- group: design
  href: https://artifacts.apis.io/bright-sky/vocabulary/bright-sky-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bright-sky-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bright-sky/data-model/bright-sky-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bright-sky-data-model.yml
- group: design
  href: https://artifacts.apis.io/bright-sky/errors/bright-sky-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bright-sky-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bright-sky/conformance/bright-sky-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bright-sky-conformance.yml
- group: other
  href: https://artifacts.apis.io/bright-sky/hosts/bright-sky-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bright-sky-hosts.yml
- group: other
  href: https://artifacts.apis.io/bright-sky/vendors/bright-sky-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bright-sky-vendors.yml
- group: build
  href: https://artifacts.apis.io/bright-sky/packages/bright-sky-packages.yml
  title: ''
  type: SDKs
  url: packages/bright-sky-packages.yml
- group: build
  href: https://artifacts.apis.io/bright-sky/packages/bright-sky-packages.yml
  title: ''
  type: Packages
  url: packages/bright-sky-packages.yml
- group: auth
  href: https://artifacts.apis.io/bright-sky/security/bright-sky-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bright-sky-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brightsky.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://brightsky.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.brightsky.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://brightsky.dev/docs/#getting-started
- group: start
  title: ''
  type: Demo
  url: https://brightsky.dev/demo/
created: '2026-10-28'
description: Bright Sky provides a free JSON API delivering German Weather Service (DWD) open weather data. It offers endpoints for historical and forecast weather, including temperature, precipitation, wind, and solar radiation, with demo visualizations like radar and alerts. The service is open, community‑maintained, and supports easy integration via simple HTTP GET requests.
image: https://brightsky.dev/logo.png
jsonld:
- class_count: 16
  name: Bright Sky Context
  property_count: 93
  slug: bright-sky-context
layout: provider
modified: '2026-10-28'
name: Bright Sky
nav: Providers
network: true
overview: 'Bright Sky publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Current Weather API, Internals API, and 2 more. Tagged areas include Company, Weather, Open Data, and JSON.


  The Bright Sky catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bright Sky''s developer surface includes documentation, API reference, getting-started guide, and 14 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Bright Sky API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: bright-sky-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bright-sky/bright-sky-2026-11-03T122612.png
security:
- kind: domain-security
  name: Bright Sky Domain Security
  slug: bright-sky-domain-security
  summary_line: TLSv1.3
slug: bright-sky
tags:
- Company
- Weather
- Open Data
- JSON
website: https://brightsky.dev/
---
