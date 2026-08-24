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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 8
  human_in_the_loop: 3
  name: Apiclarity Agentic Access
  operation_count: 27
  slug: apiclarity-agentic-access
  summary_line: 27 operations · 8 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: Captured API traffic events.
  name: APIClarity API Events API
  slug: apiclarity-api-events-api
- description: Discovered APIs and their reconstructed specifications.
  name: APIClarity API Inventory API
  slug: apiclarity-api-inventory-api
- description: Control-plane endpoints for trace sources and discovered APIs.
  name: APIClarity Control API
  slug: apiclarity-control-api
- description: Enabled features in the deployment.
  name: APIClarity Features API
  slug: apiclarity-features-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIClarity API Events API
  slug: open-apiclarity-api-events-api
- collection_type: open
  name: APIClarity API Events API Inventory API
  slug: open-apiclarity-api-inventory-api
- collection_type: open
  name: APIClarity API Events Control API
  slug: open-apiclarity-control-api
- collection_type: open
  name: APIClarity API Events Features API
  slug: open-apiclarity-features-api
- collection_type: open
  name: APIClarity API
  slug: open-apiclarity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apiclarity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apiclarity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apiclarity-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openclarity.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openclarity
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openclarity/apiclarity
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/openclarity/apiclarity#readme
- group: operate
  title: ''
  type: Issues
  url: https://github.com/openclarity/apiclarity/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/openclarity/apiclarity/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/openclarity/apiclarity/blob/master/LICENSE
- group: operate
  title: ''
  type: Slack
  url: https://outshift.slack.com
created: '2026-03-26'
description: APIClarity is an open source API security and observability tool that analyzes API traffic to reconstruct OpenAPI specifications, detect shadow and zombie APIs, identify API differences and changes, and provide API security alerts. It is part of the OpenClarity project and works with Kubernetes service meshes and API gateways for cloud-native API traffic observability.
features:
- description: Automatically reconstruct OpenAPI specifications from observed live API traffic without code instrumentation.
  name: OpenAPI Spec Reconstruction
- description: Identify undocumented shadow APIs being called in production that are not reflected in official specifications.
  name: Shadow API Detection
- description: Detect deprecated or decommissioned API endpoints still receiving traffic in production.
  name: Zombie API Detection
- description: Compare observed API behavior against documented specifications to identify drifts, changes, and violations.
  name: API Diff Analysis
- description: Generate security findings and alerts based on API traffic analysis and specification violations.
  name: API Security Alerts
- description: Deploy as a sidecar or via Helm charts for integration with Kubernetes service meshes and API gateways.
  name: Kubernetes Integration
- description: Automatically build and maintain an inventory of all APIs discovered in the environment.
  name: API Inventory
finops:
- name: Apiclarity Finops
  service_category: API
  slug: apiclarity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiclarity.png
layout: provider
modified: '2026-04-19'
name: APIClarity
nav: Providers
network: true
overview: 'APIClarity publishes 4 APIs on the [APIs.io](https://apis.io/) network, including API Events API, API Inventory API, Control API, and 1 more. Tagged areas include API Observability, API Security, API Traffic Analysis, Cisco, and Kubernetes.


  APIClarity''s developer surface includes authentication, documentation, release notes, and 8 more developer resources.'
plans:
- name: Apiclarity Plans Pricing
  plan_count: 3
  slug: apiclarity-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Apiclarity Rate Limits
  slug: apiclarity-rate-limits
score:
  band: thin
  composite: 29.0
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 42.8
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/screenshots/apiclarity-2026-06-20T172238.png
security:
- kind: authentication
  name: Apiclarity Authentication
  slug: apiclarity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apiclarity Domain Security
  slug: apiclarity-domain-security
  summary_line: no transport/DNS hardening detected
slug: apiclarity
tags:
- API Observability
- API Security
- API Traffic Analysis
- Cisco
- Kubernetes
- Open-Source
- OpenAPI Reconstruction
- OpenClarity
- Service Mesh
- Shadow APIs
use_cases:
- description: Discover all APIs running in a Kubernetes environment including undocumented and shadow APIs.
  name: API Discovery
- description: Assess API security by detecting shadow APIs, spec violations, and suspicious traffic patterns.
  name: API Security Posture Assessment
- description: Generate OpenAPI specifications from live traffic for APIs that lack formal documentation.
  name: API Specification Generation
- description: Enforce API consistency by detecting deviations between actual API behavior and official specifications.
  name: API Governance
- description: Investigate API security incidents using traffic analysis, API inventory, and spec diff data.
  name: Incident Response
website: https://openclarity.io
---
