---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Openkruise Agentic Access
  operation_count: 17
  slug: openkruise-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- description: OpenKruise provides Kubernetes Custom Resource Definitions (CRDs) for advanced workload management. CloneSet offers efficient rolling updates with partition control, Advanced StatefulSet supports in-p
  name: OpenKruise Workload API
  slug: openkruise-api
- baseURL: https://kubernetes.example.com/apis/apps.kruise.io/v1beta1
  baseurl_source: declared
  description: The Apis API from OpenKruise — 9 operation(s) for apis.
  name: OpenKruise Apis API
  slug: openkruise-apis-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenKruise Workload Apis API
  slug: open-openkruise-apis-api
- collection_type: open
  name: OpenKruise Workload API
  slug: open-openkruise
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/openkruise/kruise/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/openkruise/kruise/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/openkruise/kruise/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/openkruise/kruise/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/openkruise/kruise/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openkruise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openkruise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openkruise-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://openkruise.io/docs/
- group: company
  title: ''
  type: Website
  url: https://openkruise.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openkruise
- group: company
  title: ''
  type: Blog
  url: https://openkruise.io/blog/rss.xml
created: '2026-03-16'
description: OpenKruise is a CNCF incubating project providing advanced workload management and deployment automation for Kubernetes. It extends Kubernetes with enhanced controllers including CloneSet for efficient stateless updates, Advanced StatefulSet with in-place updates, Advanced DaemonSet, SidecarSet for sidecar container management, BroadcastJob for node-level tasks, and ImagePullJob for pre-pulling container images.
finops:
- name: Openkruise Finops
  service_category: API
  slug: openkruise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openkruise.png
layout: provider
modified: '2026-04-28'
name: OpenKruise
nav: Providers
network: true
overview: 'OpenKruise publishes 1 API on the [APIs.io](https://apis.io/) network: Apis API. Tagged areas include Cloud-Native, Controllers, Deployment, Incubating, and Kubernetes.


  OpenKruise''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Openkruise Plans Pricing
  plan_count: 3
  slug: openkruise-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Openkruise Rate Limits
  slug: openkruise-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openkruise/refs/heads/main/screenshots/openkruise-2026-06-20T191009.png
security:
- kind: authentication
  name: Openkruise Authentication
  slug: openkruise-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openkruise Domain Security
  slug: openkruise-domain-security
  summary_line: TLSv1.3
slug: openkruise
tags:
- Cloud-Native
- Controllers
- Deployment
- Incubating
- Kubernetes
- Workload Management
- CRDs
website: https://openkruise.io/
---
