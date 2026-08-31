---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kubecost Agentic Access
  operation_count: 18
  slug: kubecost-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 6
apis:
- description: The Model API from Kubecost — 15 operation(s) for model.
  name: Kubecost Model API
  slug: kubecost-model-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kubecost Allocation API
  slug: open-kubecost-allocation
- collection_type: open
  name: Kubecost Assets API
  slug: open-kubecost-assets
- collection_type: open
  name: Kubecost Budget API
  slug: open-kubecost-budget
- collection_type: open
  name: Kubecost Cloud Cost API
  slug: open-kubecost-cloud-cost
- collection_type: open
  name: Kubecost Forecast API
  slug: open-kubecost-forecast
- collection_type: open
  name: Kubecost Allocation Model API
  slug: open-kubecost-model-api
- collection_type: open
  name: Kubecost Savings API
  slug: open-kubecost-savings
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kubecost-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubecost-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubecost-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubecost
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kubecost
created: '2024-11-13'
description: Kubecost provides real-time cost monitoring and management for Kubernetes environments. Its APIs enable programmatic access to cost allocation data, asset costs, cloud provider spend, budget governance, cost forecasting, and savings recommendations for optimizing Kubernetes and cloud infrastructure spending.
finops:
- name: Kubecost Finops
  service_category: Cloud Cost Management
  slug: kubecost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubecost.png
json_schemas:
- name: Kubecost Allocation
  property_count: 37
  slug: allocation
- name: Kubecost Asset
  property_count: 8
  slug: asset
- name: Kubecost Budget Action
  property_count: 3
  slug: budget-action
- name: Kubecost Budget
  property_count: 10
  slug: budget
- name: Kubecost Cloud Cost
  property_count: 10
  slug: cloud-cost
- name: Kubecost Forecast
  property_count: 3
  slug: forecast
- name: Allocation
  property_count: 37
  slug: kubecost-allocation
- name: Asset
  property_count: 8
  slug: kubecost-asset
- name: Budget
  property_count: 10
  slug: kubecost-budget
- name: BudgetAction
  property_count: 3
  slug: kubecost-budgetaction
- name: BudgetInput
  property_count: 6
  slug: kubecost-budgetinput
- name: ClusterSizingRecommendation
  property_count: 8
  slug: kubecost-clustersizingrecommendation
- name: RequestSizingRecommendation
  property_count: 10
  slug: kubecost-requestsizingrecommendation
- name: Kubecost Savings Recommendation
  property_count: 16
  slug: savings-recommendation
json_structures:
- name: Kubecost Structure
  property_count: 0
  slug: kubecost-structure
jsonld:
- class_count: 0
  name: Kubecost Context
  property_count: 7
  slug: kubecost-context
layout: provider
modified: '2026-05-19'
name: Kubecost
nav: Providers
network: true
overview: 'Kubecost publishes 1 API on the [APIs.io](https://apis.io/) network: Model API. Tagged areas include Cloud Cost, Cost Monitoring, Kubernetes, Optimization, and Spending.


  The Kubecost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Kubecost Plans Pricing
  plan_count: 3
  slug: kubecost-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Kubecost Rate Limits
  slug: kubecost-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kubecost API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kubecost-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 53.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 62.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubecost/refs/heads/main/screenshots/kubecost-2026-06-20T184207.png
security:
- kind: domain-security
  name: Kubecost Domain Security
  slug: kubecost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kubecost
tags:
- Cloud Cost
- Cost Monitoring
- Kubernetes
- Optimization
- Spending
---
