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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Thanos Agentic Access
  operation_count: 31
  slug: thanos-agentic-access
  summary_line: 31 operations · 3 acting
api_count: 6
apis:
- description: Endpoints for querying currently active alerts.
  name: Thanos Alerts API
  slug: thanos-alerts-api
- description: Block metadata inspection and compaction status endpoints.
  name: Thanos Blocks API
  slug: thanos-blocks-api
- description: Liveness and readiness probes for the Compactor.
  name: Thanos Health API
  slug: thanos-health-api
- description: The Metadata API from Thanos — 3 operation(s) for metadata.
  name: Thanos Metadata API
  slug: thanos-metadata-api
- description: Prometheus metrics for monitoring Compactor performance.
  name: Thanos Metrics API
  slug: thanos-metrics-api
- description: The Query API from Thanos — 2 operation(s) for query.
  name: Thanos Query API
  slug: thanos-query-api
- description: Prometheus Remote Write ingestion endpoint.
  name: Thanos Remote Write API
  slug: thanos-remote-write-api
- description: The Rules API from Thanos — 2 operation(s) for rules.
  name: Thanos Rules API
  slug: thanos-rules-api
- description: The Stores API from Thanos — 1 operation(s) for stores.
  name: Thanos Stores API
  slug: thanos-stores-api
- description: The Targets API from Thanos — 1 operation(s) for targets.
  name: Thanos Targets API
  slug: thanos-targets-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thanos Compact Alerts API
  slug: open-thanos-alerts-api
- collection_type: open
  name: Thanos Compact Alerts Blocks API
  slug: open-thanos-blocks-api
- collection_type: open
  name: Thanos Compact API
  slug: open-thanos-compact
- collection_type: open
  name: Thanos Compact Alerts Health API
  slug: open-thanos-health-api
- collection_type: open
  name: Thanos Compact Alerts Metadata API
  slug: open-thanos-metadata-api
- collection_type: open
  name: Thanos Compact Alerts Metrics API
  slug: open-thanos-metrics-api
- collection_type: open
  name: Thanos Compact Alerts Query API
  slug: open-thanos-query-api
- collection_type: open
  name: Thanos Receive API
  slug: open-thanos-receive
- collection_type: open
  name: Thanos Compact Alerts Remote Write API
  slug: open-thanos-remote-write-api
- collection_type: open
  name: Thanos Ruler API
  slug: open-thanos-ruler
- collection_type: open
  name: Thanos Compact Alerts Rules API
  slug: open-thanos-rules-api
- collection_type: open
  name: Thanos Sidecar API
  slug: open-thanos-sidecar
- collection_type: open
  name: Thanos Store Gateway API
  slug: open-thanos-store-gateway
- collection_type: open
  name: Thanos Compact Alerts Stores API
  slug: open-thanos-stores-api
- collection_type: open
  name: Thanos Compact Alerts Targets API
  slug: open-thanos-targets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thanos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thanos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thanos.io/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/thanos-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/query-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/store-info.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/thanos-query-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/thanos-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/thanos-vocabulary.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://thanos.io/tip/thanos/getting-started.md/
- group: docs
  title: ''
  type: Documentation
  url: https://thanos.io/tip/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/thanos-io/thanos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thanos-io
- group: operate
  title: ''
  type: Community
  url: https://thanos.io/tip/contributing/community.md/
- group: other
  title: ''
  type: Troubleshooting
  url: https://thanos.io/tip/operating/troubleshooting.md/
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2025'
description: Open-source, highly available Prometheus setup with long-term storage capabilities that provides a global query view across multiple Prometheus servers.
examples:
- key_count: 2
  name: Thanos Query Get Stores Example
  slug: thanos-query-get-stores-example
- key_count: 2
  name: Thanos Query Instant Query Example
  slug: thanos-query-instant-query-example
- key_count: 2
  name: Thanos Query Range Query Example
  slug: thanos-query-range-query-example
finops:
- name: Thanos Finops
  service_category: Observability
  slug: thanos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thanos.png
json_schemas:
- name: Thanos Query Response
  property_count: 5
  slug: query-response
- name: Thanos Store Info
  property_count: 7
  slug: store-info
- name: ActiveTarget
  property_count: 9
  slug: thanos-activetarget
- name: Alert
  property_count: 5
  slug: thanos-alert
- name: AlertingRule
  property_count: 12
  slug: thanos-alertingrule
- name: AlertsResponse
  property_count: 2
  slug: thanos-alertsresponse
- name: BlockMeta
  property_count: 5
  slug: thanos-blockmeta
- name: BlocksResponse
  property_count: 2
  slug: thanos-blocksresponse
- name: DroppedTarget
  property_count: 1
  slug: thanos-droppedtarget
- name: ErrorResponse
  property_count: 2
  slug: thanos-errorresponse
- name: LabelsResponse
  property_count: 3
  slug: thanos-labelsresponse
- name: LabelValuesResponse
  property_count: 3
  slug: thanos-labelvaluesresponse
- name: MatrixResult
  property_count: 2
  slug: thanos-matrixresult
- name: QueryResponse
  property_count: 3
  slug: thanos-queryresponse
- name: RecordingRule
  property_count: 8
  slug: thanos-recordingrule
- name: RuleGroup
  property_count: 5
  slug: thanos-rulegroup
- name: RulesResponse
  property_count: 2
  slug: thanos-rulesresponse
- name: ScalarResult
  property_count: 0
  slug: thanos-scalarresult
- name: SeriesResponse
  property_count: 3
  slug: thanos-seriesresponse
- name: StoreInfo
  property_count: 7
  slug: thanos-storeinfo
- name: StoresResponse
  property_count: 2
  slug: thanos-storesresponse
- name: TargetsResponse
  property_count: 2
  slug: thanos-targetsresponse
- name: VectorResult
  property_count: 2
  slug: thanos-vectorresult
json_structures:
- name: Thanos Query Structure
  property_count: 0
  slug: thanos-query-structure
- name: Thanos Structure
  property_count: 0
  slug: thanos-structure
jsonld:
- class_count: 0
  name: Thanos Context
  property_count: 10
  slug: thanos-context
layout: provider
modified: '2026-05-19'
name: Thanos
nav: Providers
network: true
overview: 'Thanos publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Blocks API, Health API, and 7 more. Tagged areas include Metrics, Monitoring, Observability, Prometheus, and Time Series Database.


  The Thanos catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Thanos'' developer surface includes getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Thanos Plans Pricing
  plan_count: 1
  slug: thanos-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Thanos Rate Limits
  slug: thanos-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Thanos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: thanos-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Thanos API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: thanos-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 60.0
    developer_ergonomics: 26.2
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thanos/refs/heads/main/screenshots/thanos-2026-06-20T195209.png
security:
- kind: domain-security
  name: Thanos Domain Security
  slug: thanos-domain-security
  summary_line: TLSv1.3 · HSTS
slug: thanos
tags:
- Metrics
- Monitoring
- Observability
- Prometheus
- Time Series Database
website: https://thanos.io/
---
