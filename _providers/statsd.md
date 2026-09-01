---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Statsd Agentic Access
  operation_count: 10
  slug: statsd-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- description: The StatsD wire protocol is a UTF-8, line-oriented, UDP-by-default packet format used to push application metrics from clients to a StatsD daemon. Each line takes the form `bucket:value|type[|@sample_
  name: StatsD Wire Protocol
  slug: statsd-wire-protocol
- description: DogStatsD is the Datadog Agent's StatsD-compatible ingestion protocol. It is a strict superset of the StatsD wire format that adds first-class tag syntax (`|#k:v,k:v`), histogram (`|h`) and distributi
  name: DogStatsD Wire Protocol
  slug: dogstatsd-wire-protocol
- description: Runtime Configuration Inspection
  name: StatsD Configuration API
  slug: statsd-configuration-api
- description: Inspect Or Delete Counters
  name: StatsD Counters API
  slug: statsd-counters-api
- description: Inspect Or Delete Gauges
  name: StatsD Gauges API
  slug: statsd-gauges-api
- description: Health Check Control
  name: StatsD Health API
  slug: statsd-health-api
- description: Inspect Aggregated In-Memory State
  name: StatsD Stats API
  slug: statsd-stats-api
- description: Inspect Or Delete Timers
  name: StatsD Timers API
  slug: statsd-timers-api
artifact_total: 41
asyncapis:
- description: The DogStatsD wire protocol — Datadog's StatsD-compatible ingestion format. A strict superset of vanilla StatsD that adds first-class tag syntax (`|#k:v,k:v`), histogram (`|h`) and distribution (`|d`)
  name: DogStatsD Wire Protocol
  slug: dogstatsd-wire-protocol-asyncapi
- description: 'The StatsD wire protocol: a UTF-8, line-oriented, UDP-by-default text format used by application code to push metrics to a StatsD daemon for in-memory aggregation. Each datagram contains one or more l'
  name: StatsD Wire Protocol
  slug: statsd-wire-protocol-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StatsD Admin Interface
  slug: open-statsd-admin-interface
- collection_type: open
  name: StatsD Admin Interface Configuration API
  slug: open-statsd-configuration-api
- collection_type: open
  name: StatsD Admin Interface Configuration Counters API
  slug: open-statsd-counters-api
- collection_type: open
  name: StatsD Admin Interface Configuration Gauges API
  slug: open-statsd-gauges-api
- collection_type: open
  name: StatsD Admin Interface Configuration Health API
  slug: open-statsd-health-api
- collection_type: open
  name: StatsD Admin Interface Configuration Stats API
  slug: open-statsd-stats-api
- collection_type: open
  name: StatsD Admin Interface Configuration Timers API
  slug: open-statsd-timers-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/statsd/statsd/blob/master/CODE_OF_CONDUCT.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/statsd-agentic-access.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/statsd/statsd
- group: commercial
  title: ''
  type: License
  url: https://github.com/statsd/statsd/blob/master/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/statsd/statsd/blob/master/CHANGELOG.md
- group: docs
  title: ''
  type: ContributorGuide
  url: https://github.com/statsd/statsd/blob/master/CONTRIBUTING.md
- group: other
  title: ''
  type: Wiki
  url: https://github.com/statsd/statsd/wiki
- group: other
  title: ''
  type: ProtocolSpec
  url: https://github.com/b/statsd_spec
- group: start
  title: ''
  type: PackageRegistry
  url: https://www.npmjs.com/package/statsd
- group: operate
  title: ''
  type: Issues
  url: https://github.com/statsd/statsd/issues
- group: build
  title: ''
  type: SDKs
  url: https://github.com/msiebuhr/node-statsd-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jsocol/pystatsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sivy/py-statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WoLpH/python-statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WoLpH/django-statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Shopify/statsd-instrument
- group: build
  title: ''
  type: SDKs
  url: https://github.com/reinh/statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/youdevise/java-statsd-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/flozano/statsd-netty
- group: build
  title: ''
  type: SDKs
  url: https://github.com/smira/go-statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cactus/go-statsd-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quipo/statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/thephpleague/statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/domnikl/statsd-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/justeat/JustEat.StatsD
- group: build
  title: ''
  type: SDKs
  url: https://github.com/peschuster/graphite-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cosimo/perl5-net-statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sanbeg/Etsy-Statsd
- group: build
  title: ''
  type: SDKs
  url: https://metacpan.org/pod/Metrics::Any::Adapter::Statsd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DataDog/datadogpy
- group: other
  title: ''
  type: AlternativeServer
  url: https://docs.datadoghq.com/developers/dogstatsd/
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/statsd
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/stripe/veneur
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/atlassian/gostatsd
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/github/brubeck
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/armon/statsite
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/jbuchbinder/statsd-c
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/wayfair/statsdcc
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/avito-tech/bioyino
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/bitly/statsdaemon
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/vimeo/statsdaemon
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/amir/gographite
- group: other
  title: ''
  type: AlternativeServer
  url: https://github.com/netdata/netdata
- group: other
  title: ''
  type: Backend
  url: https://github.com/statsd/statsd/blob/master/docs/graphite.md
- group: other
  title: ''
  type: Backend
  url: https://github.com/statsd/statsd/blob/master/docs/backend.md
- group: other
  title: ''
  type: Backend
  url: https://github.com/statsd/statsd/blob/master/docs/backend.md
- group: other
  title: ''
  type: Backend
  url: https://github.com/camitz/aws-cloudwatch-statsd-backend
- group: other
  title: ''
  type: Backend
  url: https://github.com/bernd/statsd-influxdb-backend
- group: other
  title: ''
  type: Backend
  url: https://github.com/DataDog/statsd-datadog-backend
- group: other
  title: ''
  type: Backend
  url: https://github.com/emurphy/statsd-opentsdb-backend
- group: other
  title: ''
  type: Backend
  url: https://github.com/jjneely/statsd-stackdriver-backend
- group: other
  title: ''
  type: Backend
  url: https://github.com/markkimsal/statsd-elasticsearch-backend
created: '2024-01-01'
description: StatsD is the network daemon and UDP-based line protocol for application metrics, originally written at Etsy and now maintained at github.com/statsd/statsd. A StatsD client emits short text packets — counters, gauges, timers, histograms, sets, and meters — to a daemon that aggregates them in memory and flushes derived series to a backend such as Graphite, InfluxDB, Datadog, CloudWatch, or any of 30+ third-party sinks. The wire format is the canonical contract; dozens of language clients and several alternative servers (DogStatsD, Telegraf, gostatsd, brubeck, statsite, Veneur, bioyino) speak it with small, well-documented dialect extensions for tags, histograms, events, and service checks.
examples:
- key_count: 3
  name: Dogstatsd Distribution Example
  slug: dogstatsd-distribution-example
- key_count: 3
  name: Dogstatsd Event Example
  slug: dogstatsd-event-example
- key_count: 3
  name: Dogstatsd Service Check Example
  slug: dogstatsd-service-check-example
- key_count: 3
  name: Dogstatsd Tagged Counter Example
  slug: dogstatsd-tagged-counter-example
- key_count: 5
  name: Statsd Admin Stats Example
  slug: statsd-admin-stats-example
- key_count: 3
  name: Statsd Counter Example
  slug: statsd-counter-example
- key_count: 3
  name: Statsd Counter Sampled Example
  slug: statsd-counter-sampled-example
- key_count: 3
  name: Statsd Gauge Delta Example
  slug: statsd-gauge-delta-example
- key_count: 3
  name: Statsd Gauge Example
  slug: statsd-gauge-example
- key_count: 4
  name: Statsd Histogram Example
  slug: statsd-histogram-example
- key_count: 3
  name: Statsd Multi Metric Packet Example
  slug: statsd-multi-metric-packet-example
- key_count: 3
  name: Statsd Set Example
  slug: statsd-set-example
- key_count: 4
  name: Statsd Timer Example
  slug: statsd-timer-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/statsd.png
json_schemas:
- name: DogStatsD Event
  property_count: 9
  slug: dogstatsd-event
- name: DogStatsD Service Check
  property_count: 7
  slug: dogstatsd-service-check
- name: StatsD Metric Instance
  property_count: 10
  slug: statsd-metric-instance
- name: StatsD Metric Line
  property_count: 0
  slug: statsd-metric-line
json_structures:
- name: Statsd Metric Instance Structure
  property_count: 0
  slug: statsd-metric-instance-structure
jsonld:
- class_count: 0
  name: Statsd Context
  property_count: 8
  slug: statsd-context
layout: provider
modified: '2026-05-23'
name: StatsD
nav: Providers
network: true
overview: 'StatsD publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Wire Protocol, DogStatsD Wire Protocol, Configuration API, and 5 more. Tagged areas include Aggregation, Daemon, DogStatsD, Line Protocol, and Metrics.


  The StatsD catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  StatsD''s developer surface includes GitHub presence, changelog, and 50 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: StatsD API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: statsd-admin-interface-rules
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: StatsD API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: statsd-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: StatsD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: statsd-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 69.7
    contract_quality: 63.9
    developer_ergonomics: 26.2
    discoverability: 53.7
    governance: 69.7
    operational_transparency: 5.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/statsd/refs/heads/main/screenshots/statsd-2026-06-20T194527.png
slug: statsd
tags:
- Aggregation
- Daemon
- DogStatsD
- Line Protocol
- Metrics
- Observability
- Open-Source
- StatsD
- TCP
- UDP
- Wire Protocol
---
