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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opencost Agentic Access
  operation_count: 5
  slug: opencost-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: The Allocation API from OpenCost — 1 operation(s) for allocation.
  name: OpenCost Allocation API
  slug: opencost-allocation-api
- description: The Assets API from OpenCost — 1 operation(s) for assets.
  name: OpenCost Assets API
  slug: opencost-assets-api
- description: The CloudCost API from OpenCost — 1 operation(s) for cloudcost.
  name: OpenCost CloudCost API
  slug: opencost-cloudcost-api
- description: The CustomCost API from OpenCost — 2 operation(s) for customcost.
  name: OpenCost CustomCost API
  slug: opencost-customcost-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenCost Allocation API
  slug: open-opencost-allocation-api
- collection_type: open
  name: OpenCost Allocation Assets API
  slug: open-opencost-assets-api
- collection_type: open
  name: OpenCost Allocation CloudCost API
  slug: open-opencost-cloudcost-api
- collection_type: open
  name: OpenCost Allocation CustomCost API
  slug: open-opencost-customcost-api
- collection_type: open
  name: OpenCost API
  slug: open-opencost
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opencost-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opencost-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/opencost
- group: company
  title: ''
  type: Website
  url: https://opencost.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.opencost.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opencost/opencost
- group: company
  title: ''
  type: Blog
  url: https://opencost.io/blog/rss.xml
created: '2025-01-01'
description: An open source CNCF specification and reference implementation for real-time cost monitoring of Kubernetes infrastructure and cloud spending, enabling teams to measure, allocate, and optimize cloud costs across workloads.
finops:
- name: Opencost Finops
  service_category: API
  slug: opencost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opencost.png
json_schemas:
- name: OpenCost Allocation
  property_count: 13
  slug: opencost-allocation
- name: OpenCost Asset
  property_count: 6
  slug: opencost-asset
- name: OpenCost CloudCost
  property_count: 1
  slug: opencost-cloudcost
jsonld:
- class_count: 0
  name: Opencost Context
  property_count: 3
  slug: opencost-context
layout: provider
modified: '2026-05-19'
name: OpenCost
nav: Providers
network: true
overview: 'OpenCost publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Allocation API, Assets API, CloudCost API, and 1 more. Tagged areas include Cloud Cost Management, CNCF, FinOps, Kubernetes, and Observability.


  The OpenCost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenCost''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Opencost Plans Pricing
  plan_count: 3
  slug: opencost-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Opencost Rate Limits
  slug: opencost-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenCost API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: opencost-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 54.1
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/screenshots/opencost-2026-06-20T190924.png
security:
- kind: domain-security
  name: Opencost Domain Security
  slug: opencost-domain-security
  summary_line: TLSv1.3 · HSTS
slug: opencost
tags:
- Cloud Cost Management
- CNCF
- FinOps
- Kubernetes
- Observability
website: https://opencost.io/
---
