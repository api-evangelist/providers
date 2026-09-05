---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Cloudzero Agentic Access
  operation_count: 19
  slug: cloudzero-agentic-access
  summary_line: 19 operations · 14 acting
api_count: 1
apis:
- description: The Billing API exposes cost and dimension data for analysis. Endpoints under /v2/billing return cost rows over a date range with selectable dimensions (account, service, region, custom dimension) and
  name: CloudZero Billing API
  slug: billing
- description: The Insights API stores and surfaces actionable cost insights and recommendations. Endpoints under /v2/insights support listing, creating, updating, and deleting insight records, including assigned ow
  name: CloudZero Insights API
  slug: insights
- description: The Budgets API manages cost-and-usage budgets, alerts, thresholds, and actuals tracking. Endpoints under /v2/budgets list, create, update, and delete budgets and surface current consumption against l
  name: CloudZero Budgets API
  slug: budgets
- description: Allocation Telemetry sends, edits, and deletes allocation telemetry data for splitting cloud cost across custom allocation dimensions. Endpoints under /v1/telemetry/allocation/{stream_name} support su
  name: CloudZero Allocation Telemetry API
  slug: allocation-telemetry
- description: Unit Metric Telemetry ingests business metrics that drive unit-economics calculations (cost per customer, cost per transaction, cost per tenant). Endpoints under /v1/telemetry/{stream_name} support su
  name: CloudZero Unit Metric Telemetry API
  slug: unit-metric-telemetry
- description: AnyCost ingests cost data from any source using the AnyCost Stream Adaptor and Common Bill Format (CBF). Endpoints under /v2/connections/billing/anycost/{connection_id}/billing_drops accept uploads of
  name: CloudZero AnyCost API
  slug: anycost
- baseURL: https://api.cloudzero.com
  baseurl_source: declared
  description: Send, edit, and delete allocation telemetry data for splitting cloud cost data through custom allocation dimensions.
  name: CloudZero Allocation Telemetry API
  slug: cloudzero-allocation-telemetry-api
- baseURL: https://api.cloudzero.com
  baseurl_source: declared
  description: Ingest cost data from any source using the AnyCost Stream Adaptor and Common Bill Format (CBF).
  name: CloudZero AnyCost API
  slug: cloudzero-anycost-api
- baseURL: https://api.cloudzero.com
  baseurl_source: declared
  description: Retrieve cost and dimension data for billing analysis.
  name: CloudZero Billing API
  slug: cloudzero-billing-api
- baseURL: https://api.cloudzero.com
  baseurl_source: declared
  description: Create, read, update, and delete budgets for cost tracking.
  name: CloudZero Budgets API
  slug: cloudzero-budgets-api
- baseURL: https://api.cloudzero.com
  baseurl_source: declared
  description: Create, read, update, and delete cost insights.
  name: CloudZero Insights API
  slug: cloudzero-insights-api
- baseURL: https://api.cloudzero.com
  baseurl_source: declared
  description: Send, edit, and delete unit metric telemetry data related to your system operations.
  name: CloudZero Unit Metric Telemetry API
  slug: cloudzero-unit-metric-telemetry-api
artifact_total: 50
collections:
- collection_type: postman
  name: CloudZero Allocation Telemetry API
  slug: postman-cloudzero-allocation-telemetry-api
- collection_type: postman
  name: CloudZero Allocation Telemetry AnyCost API
  slug: postman-cloudzero-anycost-api
- collection_type: postman
  name: CloudZero Allocation Telemetry Billing API
  slug: postman-cloudzero-billing-api
- collection_type: postman
  name: CloudZero Allocation Telemetry Budgets API
  slug: postman-cloudzero-budgets-api
- collection_type: postman
  name: CloudZero Allocation Telemetry Insights API
  slug: postman-cloudzero-insights-api
- collection_type: postman
  name: CloudZero Allocation Telemetry Unit Metric Telemetry API
  slug: postman-cloudzero-unit-metric-telemetry-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudZero Allocation Telemetry API
  slug: open-cloudzero-allocation-telemetry-api
- collection_type: open
  name: CloudZero Allocation Telemetry AnyCost API
  slug: open-cloudzero-anycost-api
- collection_type: open
  name: CloudZero API
  slug: open-cloudzero-api
- collection_type: open
  name: CloudZero Allocation Telemetry Billing API
  slug: open-cloudzero-billing-api
- collection_type: open
  name: CloudZero Allocation Telemetry Budgets API
  slug: open-cloudzero-budgets-api
- collection_type: open
  name: CloudZero Allocation Telemetry Insights API
  slug: open-cloudzero-insights-api
- collection_type: open
  name: CloudZero Allocation Telemetry Unit Metric Telemetry API
  slug: open-cloudzero-unit-metric-telemetry-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cloudzero/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudzero-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudzero-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudzero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudzero-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudzero
- group: company
  title: ''
  type: Website
  url: https://www.cloudzero.com/
- group: start
  title: ''
  type: Portal
  url: https://app.cloudzero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudzero.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudzero.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudzero.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Cloudzero
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudzero.com/terms-of-service/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.cloudzero.com/privacy-policy/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cloudzero.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cloudzero.com/feed
created: '2026-01-02'
description: CloudZero is a cloud cost intelligence and FinOps platform that automates the collection, allocation, and analysis of infrastructure spend to uncover waste and improve unit economics. The CloudZero API V2 is REST-oriented, uses API key authentication, and exposes endpoints for querying billing costs and dimensions, managing insights and budgets, sending unit metric and allocation telemetry, and ingesting cost data from any source via the AnyCost framework.
finops:
- name: Cloudzero Finops
  service_category: FinOps Platform
  slug: cloudzero-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudzero.png
json_schemas:
- name: AllocationTelemetryRecord
  property_count: 4
  slug: cloudzero-allocationtelemetryrecord
- name: CloudZero Billing Drop
  property_count: 1
  slug: cloudzero-billing-drop
- name: BillingDrop
  property_count: 1
  slug: cloudzero-billingdrop
- name: Budget
  property_count: 8
  slug: cloudzero-budget
- name: CloudZero Budget
  property_count: 8
  slug: cloudzero-budget
- name: BudgetInput
  property_count: 5
  slug: cloudzero-budgetinput
- name: CloudZero Cost
  property_count: 2
  slug: cloudzero-cost
- name: Insight
  property_count: 7
  slug: cloudzero-insight
- name: CloudZero Insight
  property_count: 7
  slug: cloudzero-insight
- name: InsightInput
  property_count: 4
  slug: cloudzero-insightinput
- name: MetricTelemetryRecord
  property_count: 4
  slug: cloudzero-metrictelemetryrecord
- name: Pagination
  property_count: 3
  slug: cloudzero-pagination
- name: CloudZero Telemetry Record
  property_count: 5
  slug: cloudzero-telemetry-record
json_structures:
- name: Cloudzero Structure
  property_count: 0
  slug: cloudzero-structure
jsonld:
- class_count: 2
  name: Cloudzero Context
  property_count: 11
  slug: cloudzero-context
layout: provider
modified: '2026-05-19'
name: CloudZero
nav: Providers
network: true
overview: 'CloudZero publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Allocation Telemetry API, AnyCost API, Billing API, and 3 more. Tagged areas include Budgets, Cloud Cost Management, Cost Allocation, Cost Optimization, and FinOps.


  The CloudZero catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CloudZero''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, privacy policy, engineering blog, and 9 more developer resources.'
plans:
- name: Cloudzero Plans Pricing
  plan_count: 1
  slug: cloudzero-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Cloudzero Rate Limits
  slug: cloudzero-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CloudZero API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloudzero-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: CloudZero API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: cloudzero-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.5
    catalog_earned_first_party: 0.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 72.8
    developer_ergonomics: 29.8
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudzero/refs/heads/main/screenshots/cloudzero-2026-06-20T174620.png
security:
- kind: authentication
  name: Cloudzero Authentication
  slug: cloudzero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudzero Domain Security
  slug: cloudzero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudzero Trust Center
  slug: cloudzero-trust-center
  summary_line: SOC 2, GDPR
slug: cloudzero
tags:
- Budgets
- Cloud Cost Management
- Cost Allocation
- Cost Optimization
- FinOps
- Telemetry
- Unit Economics
website: https://www.cloudzero.com/
---
