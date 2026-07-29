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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ternary Agentic Access
  operation_count: 20
  slug: ternary-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 6
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
artifact_total: 21
collections:
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
random_paper: 3
rate_limits:
- limit_count: 5
  name: Ternary Rate Limits
  slug: ternary-rate-limits
rules:
- name: Ternary API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ternary-jsonschema-spectral-rules
- name: Ternary API Rules
  rule_count: 23
  severity_counts:
    error: 7
    warn: 14
    info: 0
    hint: 0
    false: 2
  slug: ternary-rules
score:
  band: developing
  composite: 48.5
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
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
