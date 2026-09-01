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
- acting_count: 6
  human_in_the_loop: 0
  name: Optscale Agentic Access
  operation_count: 16
  slug: optscale-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- description: User authentication and token management
  name: OptScale Authentication API
  slug: optscale-authentication-api
- description: Cloud account connections (AWS, Azure, GCP, Alibaba, Kubernetes)
  name: OptScale Cloud Accounts API
  slug: optscale-cloud-accounts-api
- description: Organization employees and roles
  name: OptScale Employees API
  slug: optscale-employees-api
- description: Cost reporting and expense breakdowns
  name: OptScale Expenses API
  slug: optscale-expenses-api
- description: Optimization checklist runs and results
  name: OptScale Optimizations API
  slug: optscale-optimizations-api
- description: Organization management
  name: OptScale Organizations API
  slug: optscale-organizations-api
- description: Budget pools and limits
  name: OptScale Pools API
  slug: optscale-pools-api
- description: Cost optimization recommendations
  name: OptScale Recommendations API
  slug: optscale-recommendations-api
- description: Cloud resources and assignment rules
  name: OptScale Resources API
  slug: optscale-resources-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OptScale REST Authentication API
  slug: open-optscale-authentication-api
- collection_type: open
  name: OptScale REST Authentication Cloud Accounts API
  slug: open-optscale-cloud-accounts-api
- collection_type: open
  name: OptScale REST Authentication Employees API
  slug: open-optscale-employees-api
- collection_type: open
  name: OptScale REST Authentication Expenses API
  slug: open-optscale-expenses-api
- collection_type: open
  name: OptScale REST Authentication Optimizations API
  slug: open-optscale-optimizations-api
- collection_type: open
  name: OptScale REST Authentication Organizations API
  slug: open-optscale-organizations-api
- collection_type: open
  name: OptScale REST Authentication Pools API
  slug: open-optscale-pools-api
- collection_type: open
  name: OptScale REST Authentication Recommendations API
  slug: open-optscale-recommendations-api
- collection_type: open
  name: OptScale REST Authentication Resources API
  slug: open-optscale-resources-api
- collection_type: open
  name: OptScale REST API
  slug: open-optscale
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hystax/optscale/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hystax/optscale/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/hystax/optscale/blob/integration/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hystax/optscale/blob/integration/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/hystax/optscale/blob/integration/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/hystax/optscale/blob/integration/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optscale-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hystax.com/optscale/
- group: docs
  title: ''
  type: Documentation
  url: https://hystax.com/documentation/optscale/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hystax
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hystax/optscale
- group: agent
  title: ''
  type: LlmsText
  url: https://my.optscale.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://hystax.com/feed/
created: '2026-03-27'
description: OptScale is an open-source FinOps and cloud cost optimization platform by Hystax supporting AWS, Azure, GCP, Alibaba Cloud, and Kubernetes.
finops:
- name: Optscale Finops
  service_category: API
  slug: optscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optscale.png
layout: provider
modified: '2026-05-19'
name: OptScale
nav: Providers
network: true
overview: 'OptScale publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Cloud Accounts API, Employees API, and 6 more. Tagged areas include FinOps, Cost Optimization, Cloud, Kubernetes, and Open-Source.


  OptScale''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Optscale Plans Pricing
  plan_count: 3
  slug: optscale-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Optscale Rate Limits
  slug: optscale-rate-limits
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optscale/refs/heads/main/screenshots/optscale-2026-06-20T191116.png
security:
- kind: authentication
  name: Optscale Authentication
  slug: optscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Optscale Domain Security
  slug: optscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: optscale
tags:
- FinOps
- Cost Optimization
- Cloud
- Kubernetes
- Open-Source
website: https://hystax.com/optscale/
---
