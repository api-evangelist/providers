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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kubecost Agentic Access
  operation_count: 18
  slug: kubecost-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 1
apis:
- description: The Model API from Kubecost — 15 operation(s) for model.
  name: Kubecost Model API
  slug: kubecost-model-api
artifact_total: 29
collections:
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
  name: Kubecost Savings API
  slug: open-kubecost-savings
common:
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
random_paper: 48
rate_limits:
- limit_count: 2
  name: Kubecost Rate Limits
  slug: kubecost-rate-limits
rules:
- name: Kubecost API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kubecost-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 0.0
    discoverability: 60.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 40.8
  schema_version: 0.5
  scored_at: '2026-07-23'
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
