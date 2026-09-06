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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tikv Agentic Access
  operation_count: 10
  slug: tikv-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: The official Java client for TiKV. Supports raw key-value operations and transactional operations via gRPC. Available on Maven Central.
  name: TiKV Java Client
  slug: tikv-client-java
- description: The official Rust client for TiKV providing raw and transactional key-value access to TiKV clusters.
  name: TiKV Rust Client
  slug: tikv-client-rust
- description: The official Python client for TiKV supporting raw and transactional key-value operations.
  name: TiKV Python Client
  slug: tikv-client-python
- baseURL: http://localhost:20160
  baseurl_source: declared
  description: TiKV node configuration management
  name: TiKV Configuration API
  slug: tikv-configuration-api
- baseURL: http://localhost:20160
  baseurl_source: declared
  description: Debug and diagnostic endpoints
  name: TiKV Debug API
  slug: tikv-debug-api
- baseURL: http://localhost:20160
  baseurl_source: declared
  description: Prometheus metrics endpoint
  name: TiKV Metrics API
  slug: tikv-metrics-api
- baseURL: http://localhost:20160
  baseurl_source: declared
  description: Region management and inspection
  name: TiKV Regions API
  slug: tikv-regions-api
- baseURL: http://localhost:20160
  baseurl_source: declared
  description: Node status and health
  name: TiKV Status API
  slug: tikv-status-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TiKV HTTP Management Configuration API
  slug: open-tikv-configuration-api
- collection_type: open
  name: TiKV HTTP Management Configuration Debug API
  slug: open-tikv-debug-api
- collection_type: open
  name: TiKV HTTP Management API
  slug: open-tikv-http-api
- collection_type: open
  name: TiKV HTTP Management Configuration Metrics API
  slug: open-tikv-metrics-api
- collection_type: open
  name: TiKV HTTP Management Configuration Regions API
  slug: open-tikv-regions-api
- collection_type: open
  name: TiKV HTTP Management Configuration Status API
  slug: open-tikv-status-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tikv/tikv/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tikv/tikv/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/tikv/tikv/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/tikv/tikv/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/tikv/tikv/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tikv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tikv-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pingcap
- group: company
  title: ''
  type: Website
  url: https://tikv.org/
- group: docs
  title: ''
  type: Documentation
  url: https://tikv.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://tikv.org/docs/7.1/concepts/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tikv
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tikv/tikv
- group: other
  title: ''
  type: Governance
  url: https://github.com/tikv/tikv/blob/master/GOVERNANCE.md
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/tikv/
- group: company
  title: ''
  type: Blog
  url: https://tikv.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://tikv.org/community/
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/tikv/tikv/blob/master/ROADMAP.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/tikv/tikv/blob/master/LICENSE
- group: operate
  title: ''
  type: Slack
  url: https://slack.tidb.io/invite?team=tikv-wg
- group: operate
  title: ''
  type: Forums
  url: https://internals.tidb.io/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-go
created: '2025-01-01'
description: TiKV is a CNCF-graduated distributed transactional key-value database built in Rust with Raft consensus. Originally created to complement TiDB, it provides horizontal scalability, strong consistency, and high availability with ACID transaction support. Client APIs are available for Java, Rust, Python, Go, and C++. An HTTP management API provides status, configuration, and monitoring endpoints.
examples:
- key_count: 2
  name: Tikv Getregionbyid Example
  slug: tikv-getRegionById-example
- key_count: 2
  name: Tikv Getstatus Example
  slug: tikv-getStatus-example
finops:
- name: Tikv Finops
  service_category: Database
  slug: tikv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tikv.png
json_schemas:
- name: TiKV Region
  property_count: 10
  slug: tikv-region
json_structures:
- name: Tikv Region Structure
  property_count: 0
  slug: tikv-region-structure
jsonld:
- class_count: 14
  name: Tikv Context
  property_count: 0
  slug: tikv-context
layout: provider
modified: '2026-05-19'
name: TiKV
nav: Providers
network: true
overview: 'TiKV publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Debug API, Metrics API, and 2 more. Tagged areas include ACID, CNCF, Database, Distributed Systems, and Key-Value Store.


  The TiKV catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TiKV''s developer surface includes documentation, getting-started guide, engineering blog, and 22 more developer resources.'
plans:
- name: Tikv Plans Pricing
  plan_count: 1
  slug: tikv-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Tikv Rate Limits
  slug: tikv-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TiKV API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tikv-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: TiKV API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: tikv-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 50.2
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tikv/refs/heads/main/screenshots/tikv-2026-06-20T195351.png
security:
- kind: domain-security
  name: Tikv Domain Security
  slug: tikv-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tikv
tags:
- ACID
- CNCF
- Database
- Distributed Systems
- Key-Value Store
- Open-Source
- Rust
website: https://tikv.org/
---
