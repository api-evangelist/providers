---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Radio Browser Agentic Access
  operation_count: 29
  slug: radio-browser-agentic-access
  summary_line: 29 operations · 1 acting
api_count: 1
apis:
- baseURL: https://de1.api.radio-browser.info
  baseurl_source: declared
  description: Aggregated counts of countries, languages, tags, codecs, and states.
  name: Radio Browser Categories API
  slug: radio-browser-categories-api
- baseURL: https://de1.api.radio-browser.info
  baseurl_source: declared
  description: Click counting, voting, and station submission.
  name: Radio Browser Interactions API
  slug: radio-browser-interactions-api
- baseURL: https://de1.api.radio-browser.info
  baseurl_source: declared
  description: Server stats, mirror discovery, and configuration.
  name: Radio Browser Service API
  slug: radio-browser-service-api
- baseURL: https://de1.api.radio-browser.info
  baseurl_source: declared
  description: Browse, search, and list radio stations.
  name: Radio Browser Stations API
  slug: radio-browser-stations-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Radio Browser Categories API
  slug: open-radio-browser-categories-api
- collection_type: open
  name: Radio Browser Categories Interactions API
  slug: open-radio-browser-interactions-api
- collection_type: open
  name: Radio Browser Categories Service API
  slug: open-radio-browser-service-api
- collection_type: open
  name: Radio Browser Categories Stations API
  slug: open-radio-browser-stations-api
- collection_type: open
  name: Radio Browser API
  slug: open-radio-browser
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/segler-alex/radiobrowser-api-rust/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/segler-alex/radiobrowser-api-rust/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/segler-alex/radiobrowser-api-rust/blob/master/CODE_OF_CONDUCT.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/radio-browser-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radio-browser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.radio-browser.info/
- group: docs
  title: ''
  type: Documentation
  url: https://api.radio-browser.info/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.radio-browser.info/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segler-alex
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/segler-alex/radiobrowser-api-rust
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/radiobrowser/radiobrowser-api-rust
- group: other
  title: ''
  type: HelmCharts
  url: https://gitlab.com/radiobrowser/helm-charts
- group: commercial
  title: ''
  type: License
  url: https://www.gnu.org/licenses/agpl-3.0.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/radio-browser-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/radio-browser-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/radio-browser-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/radio-browser-rate-limits.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ivandotv/radio-browser-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/andreztz/pyradios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sfuhrm/radiobrowser4j
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nepodev/radio-browser
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tomassasovsky/radio-browser-api.dart
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adinan-cenci/radio-browser
- group: build
  title: ''
  type: SDKs
  url: https://hexdocs.pm/radio_browser/
created: '2026-05-28'
description: Radio Browser is a free, community-driven directory of internet radio stations. The project publishes a public REST API exposing the full catalog of stations along with category aggregates (countries, states, languages, tags, codecs), click counting, voting, and station submission. Mirrors are discovered through a round-robin DNS pool (all.api.radio-browser.info) and the canonical server software (radiobrowser-api-rust) is released under AGPL-3.0, so anyone can self-host an additional mirror.
examples:
- key_count: 5
  name: Radio Browser Click Station Example
  slug: radio-browser-click-station-example
- key_count: 10
  name: Radio Browser Get Stats Example
  slug: radio-browser-get-stats-example
- key_count: 2
  name: Radio Browser Vote Station Example
  slug: radio-browser-vote-station-example
features:
- description: Servers discovered via DNS resolution of all.api.radio-browser.info; clients pick a healthy mirror and fall back as needed.
  name: Round-Robin Mirror Pool
- description: JSON, XML, CSV, M3U, PLS, XSPF, and TTL output for nearly every read endpoint.
  name: Multiple Response Formats
- description: List stations by country, country code, state, language, tag, or codec with station counts per facet.
  name: Faceted Browse
- description: Stations are automatically pinged to verify their stream is reachable; results power lastcheckok and broken-station endpoints.
  name: Continuous Stream Health Checks
- description: Anyone can submit a station via POST /json/add; clicks and votes feed station popularity rankings.
  name: Community Curation
- description: The radiobrowser-api-rust server is open source; operators can self-host an additional mirror.
  name: Open Source Server (AGPL-3.0)
- description: Stations carry optional geo_lat/geo_long for map-based discovery.
  name: Geo Coordinates
- description: Each mirror exposes /metrics in Prometheus exposition format for operational observability.
  name: Prometheus Metrics
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radio-browser.png
integrations:
- description: Multiple custom components and the built-in Radio Browser integration use the API for station selection.
  name: Home Assistant
- description: Media player extensions consume the API to populate radio station catalogs.
  name: VLC / Media Players
- description: Operators run radiobrowser-api-rust to add to the all.api.radio-browser.info pool.
  name: Self-Hosted Mirrors
- description: Listed in public-apis/public-apis under the Music category.
  name: Public APIs Directory
json_schemas:
- name: Category
  property_count: 4
  slug: radio-browser-category
- name: Station
  property_count: 37
  slug: radio-browser-station
- name: ServiceStats
  property_count: 10
  slug: radio-browser-stats
json_structures:
- name: Radio Browser Category Structure
  property_count: 4
  slug: radio-browser-category-structure
- name: Radio Browser Station Structure
  property_count: 24
  slug: radio-browser-station-structure
jsonld:
- class_count: 24
  name: Radio Browser Context
  property_count: 3
  slug: radio-browser-context
layout: provider
modified: '2026-05-28'
name: Radio Browser
nav: Providers
network: true
overview: 'Radio Browser publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Interactions API, Service API, and 1 more. Tagged areas include Music, Radio, Streaming, Open-Source, and Open Data.


  The Radio Browser catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Radio Browser''s developer surface includes documentation, API reference, and 23 more developer resources.'
plans:
- name: Radio Browser Plans Pricing
  plan_count: 1
  slug: radio-browser-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Radio Browser Rate Limits
  slug: radio-browser-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Radio Browser API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: radio-browser-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Radio Browser API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: radio-browser-rules
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 30.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 28.8
    contract_quality: 60.9
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 50.0
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radio-browser/refs/heads/main/screenshots/radio-browser-2026-06-20T192514.png
security:
- kind: domain-security
  name: Radio Browser Domain Security
  slug: radio-browser-domain-security
  summary_line: TLSv1.3 · HSTS
slug: radio-browser
solutions:
- description: The free, hosted, AGPL-licensed Radio Browser mirror network — the default for most apps.
  name: Hosted Community API
- description: Run radiobrowser-api-rust on your own infrastructure for guaranteed throughput, isolated data, or private catalogs.
  name: Self-Hosted Mirror
tags:
- Music
- Radio
- Streaming
- Open-Source
- Open Data
- Community
- Public APIs
- AGPL
use_cases:
- description: Power desktop, mobile, and web players that let users browse the directory and play streams.
  name: Internet Radio Player Apps
- description: Back Alexa/Google/Home Assistant skills that play "play jazz radio from France" requests by searching the directory.
  name: Voice Assistant Skills
- description: Embedded firmware (e.g. AirMusic, Hama, internet radio hardware) ships Radio Browser as a station source.
  name: Smart Speaker Integrations
- description: Researchers analyze the catalog to study global radio programming, language distribution, and genre tagging.
  name: Music Discovery Research
- description: Use the /json/checks data to build dashboards showing global radio stream uptime.
  name: Streaming Health Dashboards
- description: Editors use vote/click data to surface trending stations by country, language, or genre.
  name: Editorial Curation
website: https://www.radio-browser.info/
---
