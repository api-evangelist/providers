---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 26
  human_in_the_loop: 3
  name: Timescaledb Agentic Access
  operation_count: 35
  slug: timescaledb-agentic-access
  summary_line: 35 operations · 26 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: The database itself is accessed via the PostgreSQL wire protocol (port 5432), with TimescaleDB SQL functions for hypertable management, compression, continuous aggregates and hyperfunctions. Not a RES
  name: TimescaleDB PostgreSQL Wire Interface
  slug: postgres-wire
- description: Track analytics events.
  name: TimescaleDB / Tiger Data Analytics API
  slug: timescaledb-analytics-api
- description: Authentication and authorization information.
  name: TimescaleDB / Tiger Data Auth API
  slug: timescaledb-auth-api
- description: The Read Replica Sets API from TimescaleDB / Tiger Data — 6 operation(s) for read replica sets.
  name: TimescaleDB / Tiger Data Read Replica Sets API
  slug: timescaledb-read-replica-sets-api
- description: Manage services, read replicas, and their associated actions.
  name: TimescaleDB / Tiger Data Services API
  slug: timescaledb-services-api
- description: Manage VPCs and their peering connections.
  name: TimescaleDB / Tiger Data VPCs API
  slug: timescaledb-vpcs-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tiger Cloud Analytics API
  slug: open-timescaledb-analytics-api
- collection_type: open
  name: Tiger Cloud Analytics Auth API
  slug: open-timescaledb-auth-api
- collection_type: open
  name: Tiger Cloud Analytics Read Replica Sets API
  slug: open-timescaledb-read-replica-sets-api
- collection_type: open
  name: Tiger Cloud Analytics Services API
  slug: open-timescaledb-services-api
- collection_type: open
  name: Tiger Cloud Analytics VPCs API
  slug: open-timescaledb-vpcs-api
- collection_type: open
  name: Tiger Cloud API
  slug: open-timescaledb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/timescaledb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/timescaledb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/timescaledb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timescaledb-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/timescaledb
- group: company
  title: ''
  type: Website
  url: https://www.tigerdata.com/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.timescale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tigerdata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tigerdata.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/timescale
- group: start
  title: ''
  type: Console
  url: https://console.cloud.timescale.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/timescaledb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/timescaledb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/timescaledb-finops.yml
created: '2026-05-08'
description: TimescaleDB (now part of Tiger Data) is a PostgreSQL-native time-series database featuring hypertables, columnstore (Hypercore), continuous aggregates, retention policies and hyperfunctions. The managed Tiger Cloud platform exposes a public REST API for managing projects, services, VPCs, peering and read replicas, while the database itself is consumed via standard PostgreSQL wire protocol.
finops:
- name: Timescaledb Finops
  service_category: Database (Time-Series)
  slug: timescaledb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/timescaledb.png
json_schemas:
- name: AuthInfo
  property_count: 2
  slug: timescaledb-authinfo
- name: ConnectionPooler
  property_count: 1
  slug: timescaledb-connectionpooler
- name: DeployStatus
  property_count: 0
  slug: timescaledb-deploystatus
- name: Endpoint
  property_count: 2
  slug: timescaledb-endpoint
- name: EnvironmentTag
  property_count: 0
  slug: timescaledb-environmenttag
- name: Error
  property_count: 2
  slug: timescaledb-error
- name: ForkServiceCreate
  property_count: 6
  slug: timescaledb-forkservicecreate
- name: ForkSpec
  property_count: 3
  slug: timescaledb-forkspec
- name: ForkStrategy
  property_count: 0
  slug: timescaledb-forkstrategy
- name: HAReplica
  property_count: 2
  slug: timescaledb-hareplica
- name: Peering
  property_count: 7
  slug: timescaledb-peering
- name: PeeringCreate
  property_count: 3
  slug: timescaledb-peeringcreate
- name: ReadReplicaSet
  property_count: 9
  slug: timescaledb-readreplicaset
- name: ReadReplicaSetCreate
  property_count: 4
  slug: timescaledb-readreplicasetcreate
- name: ResizeInput
  property_count: 2
  slug: timescaledb-resizeinput
- name: Service
  property_count: 16
  slug: timescaledb-service
- name: ServiceCreate
  property_count: 7
  slug: timescaledb-servicecreate
- name: ServiceLogEntry
  property_count: 3
  slug: timescaledb-servicelogentry
- name: ServiceLogs
  property_count: 3
  slug: timescaledb-servicelogs
- name: ServiceType
  property_count: 0
  slug: timescaledb-servicetype
- name: ServiceVPCInput
  property_count: 1
  slug: timescaledb-servicevpcinput
- name: SetEnvironmentInput
  property_count: 1
  slug: timescaledb-setenvironmentinput
- name: SetHAReplicaInput
  property_count: 2
  slug: timescaledb-sethareplicainput
- name: UpdatePasswordInput
  property_count: 1
  slug: timescaledb-updatepasswordinput
- name: VPC
  property_count: 4
  slug: timescaledb-vpc
- name: VPCCreate
  property_count: 3
  slug: timescaledb-vpccreate
- name: VPCRename
  property_count: 1
  slug: timescaledb-vpcrename
json_structures:
- name: Timescaledb Structure
  property_count: 0
  slug: timescaledb-structure
layout: provider
modified: '2026-05-19'
name: TimescaleDB / Tiger Data
nav: Providers
network: true
overview: 'TimescaleDB / Tiger Data publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Read Replica Sets API, and 2 more. Tagged areas include Database, Time-Series, PostgreSQL, Open Source, and Cloud.


  The TimescaleDB / Tiger Data catalog on APIs.io includes 1 Spectral governance ruleset.


  TimescaleDB / Tiger Data''s developer surface includes documentation, pricing, GitHub presence, developer console, and 10 more developer resources.'
plans:
- name: Timescaledb Plans Pricing
  plan_count: 6
  slug: timescaledb-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Timescaledb Rate Limits
  slug: timescaledb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TimescaleDB / Tiger Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: timescaledb-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.9
  delta: -7.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 51.5
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/timescaledb/refs/heads/main/screenshots/timescaledb-2026-06-20T195406.png
security:
- kind: domain-security
  name: Timescaledb Domain Security
  slug: timescaledb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Timescaledb Vulnerability Disclosure
  slug: timescaledb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Timescaledb Trust Center
  slug: timescaledb-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: timescaledb
tags:
- Database
- Time-Series
- PostgreSQL
- Open Source
- Cloud
- Hypertables
- Continuous Aggregates
- Tiger Cloud
website: https://www.tigerdata.com/
---
