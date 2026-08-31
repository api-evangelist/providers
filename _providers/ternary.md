---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ternary Agentic Access
  operation_count: 20
  slug: ternary-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- description: Manage and query cloud cost anomalies
  name: Ternary Anomaly Detection API
  slug: ternary-anomaly-detection-api
- description: Manage cloud commitment purchases and optimization
  name: Ternary Commitments API
  slug: ternary-commitments-api
- description: Manage cost allocation rules, cost centers, and labels
  name: Ternary Cost Allocation API
  slug: ternary-cost-allocation-api
- description: Budget forecasting and spend projections
  name: Ternary Forecasting API
  slug: ternary-forecasting-api
- description: Kubernetes cost allocation and pod label management
  name: Ternary Kubernetes API
  slug: ternary-kubernetes-api
- description: Cost reports, dashboards, and analytics
  name: Ternary Reporting API
  slug: ternary-reporting-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ternary Anomaly Detection API
  slug: open-ternary-anomaly-detection-api
- collection_type: open
  name: Ternary Anomaly Detection Commitments API
  slug: open-ternary-commitments-api
- collection_type: open
  name: Ternary Anomaly Detection Cost Allocation API
  slug: open-ternary-cost-allocation-api
- collection_type: open
  name: Ternary Anomaly Detection Forecasting API
  slug: open-ternary-forecasting-api
- collection_type: open
  name: Ternary Anomaly Detection Kubernetes API
  slug: open-ternary-kubernetes-api
- collection_type: open
  name: Ternary Anomaly Detection Reporting API
  slug: open-ternary-reporting-api
- collection_type: open
  name: Ternary API
  slug: open-ternary
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ternary-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ternary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ternary-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ternaryinc
- group: company
  title: ''
  type: Website
  url: https://ternary.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ternary.app/
- group: build
  title: ''
  type: GCP Integration
  url: https://ternary.app/integrations/google-cloud-gcp/
- group: other
  title: ''
  type: Kubernetes
  url: https://ternary.app/integrations/kubernetes/
- group: company
  title: ''
  type: Blog
  url: https://ternary.app/blog/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/openapi/ternary-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/vocabulary/ternary-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ternary.app/llms.txt
created: '2026-03-16'
description: Ternary is a multi-cloud FinOps platform providing cost visibility, anomaly detection, commitment management, forecasting, and Kubernetes cost allocation for cloud environments. Originally built for Google Cloud, Ternary now supports AWS, Azure, and other cloud providers through its Universal Spend Ledger, with a REST API for programmatic access to all platform capabilities.
examples:
- key_count: 4
  name: Ternary Create Budget Example
  slug: ternary-create-budget-example
- key_count: 4
  name: Ternary List Anomalies Example
  slug: ternary-list-anomalies-example
finops:
- name: Ternary Finops
  service_category: API
  slug: ternary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ternary.png
json_schemas:
- name: Ternary Cloud Cost Anomaly
  property_count: 12
  slug: ternary-anomaly
- name: Ternary Cloud Cost Budget
  property_count: 11
  slug: ternary-budget
json_structures:
- name: Ternary Anomaly Structure
  property_count: 0
  slug: ternary-anomaly-structure
jsonld:
- class_count: 5
  name: Ternary Context
  property_count: 25
  slug: ternary-context
layout: provider
modified: '2026-05-19'
name: Ternary
nav: Providers
network: true
overview: 'Ternary publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Anomaly Detection API, Commitments API, Cost Allocation API, and 3 more. Tagged areas include Cloud Cost Management, Cost Optimization, FinOps, Google Cloud, and Kubernetes.


  The Ternary catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ternary''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ternary Plans Pricing
  plan_count: 3
  slug: ternary-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Ternary Rate Limits
  slug: ternary-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ternary API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ternary-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Ternary API Rules
  rule_count: 23
  severity_counts:
    error: 7
    warn: 14
    info: 0
    hint: 0
    false: 2
  slug: ternary-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 67.3
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/screenshots/ternary-2026-06-20T195129.png
security:
- kind: authentication
  name: Ternary Authentication
  slug: ternary-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ternary Domain Security
  slug: ternary-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ternary
tags:
- Cloud Cost Management
- Cost Optimization
- FinOps
- Google Cloud
- Kubernetes
- Multi-Cloud
website: https://ternary.app/
---
