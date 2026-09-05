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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Google Kubernetes Engine Agentic Access
  operation_count: 23
  slug: google-kubernetes-engine-agentic-access
  summary_line: 23 operations · 18 acting
api_count: 5
apis:
- baseURL: https://container.googleapis.com
  baseurl_source: spec
  description: The Clusters API from Google Kubernetes Engine — 1 operation(s) for clusters.
  name: Google Kubernetes Engine Clusters API
  slug: google-kubernetes-engine-clusters-api
- baseURL: https://container.googleapis.com
  baseurl_source: spec
  description: The Google Kubernetes Engine API API from Google Kubernetes Engine — 15 operation(s) for google kubernetes engine api.
  name: Google Kubernetes Engine Google Kubernetes Engine API API
  slug: google-kubernetes-engine-google-kubernetes-engine-api-api
- baseURL: https://container.googleapis.com
  baseurl_source: spec
  description: The NodePools API from Google Kubernetes Engine — 1 operation(s) for nodepools.
  name: Google Kubernetes Engine NodePools API
  slug: google-kubernetes-engine-nodepools-api
- baseURL: https://container.googleapis.com
  baseurl_source: spec
  description: The Operations API from Google Kubernetes Engine — 1 operation(s) for operations.
  name: Google Kubernetes Engine Operations API
  slug: google-kubernetes-engine-operations-api
- baseURL: https://container.googleapis.com
  baseurl_source: spec
  description: The ServerConfig API from Google Kubernetes Engine — 1 operation(s) for serverconfig.
  name: Google Kubernetes Engine ServerConfig API
  slug: google-kubernetes-engine-serverconfig-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Kubernetes Engine Clusters API
  slug: open-google-kubernetes-engine-clusters-api
- collection_type: open
  name: Google Kubernetes Engine Clusters Google Kubernetes Engine API API
  slug: open-google-kubernetes-engine-google-kubernetes-engine-api-api
- collection_type: open
  name: Google Kubernetes Engine Clusters NodePools API
  slug: open-google-kubernetes-engine-nodepools-api
- collection_type: open
  name: Google Kubernetes Engine Clusters Operations API
  slug: open-google-kubernetes-engine-operations-api
- collection_type: open
  name: Google Kubernetes Engine Clusters ServerConfig API
  slug: open-google-kubernetes-engine-serverconfig-api
- collection_type: open
  name: Google Kubernetes Engine API
  slug: open-google-kubernetes-engine
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-kubernetes-engine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-kubernetes-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-kubernetes-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-kubernetes-engine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-kubernetes-engine-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/kubernetes-engine
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/kubernetes-engine/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/kubernetes-engine/pricing
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/containers-kubernetes
- group: start
  title: ''
  type: Signup
  url: https://console.cloud.google.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
created: '2026-03-26'
description: Google Kubernetes Engine (GKE) is a managed Kubernetes service on Google Cloud that provides a production-ready environment for deploying, managing, and scaling containerized applications. It offers autopilot and standard modes, built-in security, multi-cluster management, and seamless integration with Google Cloud services.
finops:
- name: Google Kubernetes Engine Finops
  service_category: API
  slug: google-kubernetes-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-kubernetes-engine.png
layout: provider
modified: '2026-05-19'
name: Google Kubernetes Engine
nav: Providers
network: true
overview: 'Google Kubernetes Engine publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Google Kubernetes Engine API API, NodePools API, and 2 more. Tagged areas include Cloud-Native, Containers, Google Cloud, Kubernetes, and Managed Service.


  Google Kubernetes Engine''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 7 more developer resources.'
plans:
- name: Google Kubernetes Engine Plans Pricing
  plan_count: 3
  slug: google-kubernetes-engine-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Google Kubernetes Engine Rate Limits
  slug: google-kubernetes-engine-rate-limits
scopes:
- name: Google Kubernetes Engine Scopes
  scope_count: 1
  slug: google-kubernetes-engine-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-kubernetes-engine/refs/heads/main/screenshots/google-kubernetes-engine-2026-06-20T182210.png
security:
- kind: authentication
  name: Google Kubernetes Engine Authentication
  slug: google-kubernetes-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Kubernetes Engine Domain Security
  slug: google-kubernetes-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Kubernetes Engine Vulnerability Disclosure
  slug: google-kubernetes-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-kubernetes-engine
tags:
- Cloud-Native
- Containers
- Google Cloud
- Kubernetes
- Managed Service
- Orchestration
website: https://cloud.google.com/kubernetes-engine
---
