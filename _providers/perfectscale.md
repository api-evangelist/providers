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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Perfectscale Agentic Access
  operation_count: 6
  slug: perfectscale-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: Authentication and access tokens
  name: PerfectScale Authentication API
  slug: perfectscale-authentication-api
- description: Automation audit logs
  name: PerfectScale Automation API
  slug: perfectscale-automation-api
- description: Kubernetes cluster operations
  name: PerfectScale Clusters API
  slug: perfectscale-clusters-api
- description: Workload metrics and analysis
  name: PerfectScale Workloads API
  slug: perfectscale-workloads-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PerfectScale Public Authentication API
  slug: open-perfectscale-authentication-api
- collection_type: open
  name: PerfectScale Public Authentication Automation API
  slug: open-perfectscale-automation-api
- collection_type: open
  name: PerfectScale Public Authentication Clusters API
  slug: open-perfectscale-clusters-api
- collection_type: open
  name: PerfectScale Public API
  slug: open-perfectscale-perfectscale
- collection_type: open
  name: PerfectScale Public Authentication Workloads API
  slug: open-perfectscale-workloads-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perfectscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perfectscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/perfectscale-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perfectscale-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perfectscale
- group: company
  title: ''
  type: Website
  url: https://www.perfectscale.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.perfectscale.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.perfectscale.io/llms.txt
created: '2026-03-27'
description: PerfectScale is a Kubernetes cost optimization platform providing autonomous scaling and resource rightsizing.
finops:
- name: Perfectscale Finops
  service_category: API
  slug: perfectscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perfectscale.png
layout: provider
modified: '2026-05-19'
name: PerfectScale
nav: Providers
network: true
overview: 'PerfectScale publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Automation API, Clusters API, and 1 more. Tagged areas include FinOps, Kubernetes, and Cost Optimization.


  PerfectScale''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Perfectscale Plans Pricing
  plan_count: 3
  slug: perfectscale-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Perfectscale Rate Limits
  slug: perfectscale-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 33.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/screenshots/perfectscale-2026-06-20T191600.png
security:
- kind: authentication
  name: Perfectscale Authentication
  slug: perfectscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perfectscale Domain Security
  slug: perfectscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: perfectscale
tags:
- FinOps
- Kubernetes
- Cost Optimization
website: https://www.perfectscale.io/
---
