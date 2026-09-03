---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The ScaleOps Platform API provides programmatic access to Kubernetes cost optimization features including workload resource recommendations, real-time optimization controls, cost monitoring dashboards
  name: ScaleOps Platform API
  slug: scaleops-platform-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scaleops-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scaleops-sh
- group: company
  title: ''
  type: Website
  url: https://scaleops.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scaleops.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/scaleops-sh
- group: company
  title: ''
  type: Blog
  url: https://scaleops.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://scaleops.com/pricing/
- group: commercial
  title: ''
  type: Cost Monitoring
  url: https://scaleops.com/product/kubernetes-cost-monitoring/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/vocabulary/scaleops-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/json-schema/scaleops-workload-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/json-ld/scaleops-context.jsonld
created: '2026-05-02'
description: ScaleOps is an autonomous Kubernetes cost optimization and resource management platform that continuously manages cloud infrastructure resources in real-time based on actual workload behavior. ScaleOps eliminates the need for manual resource configuration by automatically right-sizing CPU, memory, and replica counts for containers and clusters. The platform integrates natively with AWS, GCP, Azure cost management tools and is deployed via a single Helm command. ScaleOps provides real-time, context-aware optimization for production Kubernetes environments without service disruption.
finops:
- name: Scaleops Finops
  service_category: API
  slug: scaleops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scaleops.png
json_schemas:
- name: ScaleOps Workload
  property_count: 10
  slug: scaleops-workload
json_structures:
- name: Scaleops Workload Structure
  property_count: 0
  slug: scaleops-workload-structure
jsonld:
- class_count: 0
  name: Scaleops Context
  property_count: 17
  slug: scaleops-context
layout: provider
modified: '2026-05-02'
name: ScaleOps
nav: Providers
network: true
overview: 'ScaleOps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Azure, Cost Optimization, FinOps, GCP, and Helm.


  The ScaleOps catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ScaleOps'' developer surface includes documentation, GitHub presence, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Scaleops Plans Pricing
  plan_count: 3
  slug: scaleops-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Scaleops Rate Limits
  slug: scaleops-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ScaleOps API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: scaleops-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 13.1
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 21.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/screenshots/scaleops-2026-06-20T193510.png
security:
- kind: domain-security
  name: Scaleops Domain Security
  slug: scaleops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scaleops
tags:
- Azure
- Cost Optimization
- FinOps
- GCP
- Helm
- Kubernetes
- Resource Management
website: https://scaleops.com/
---
