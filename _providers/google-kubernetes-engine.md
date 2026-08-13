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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Google Kubernetes Engine Agentic Access
  operation_count: 23
  slug: google-kubernetes-engine-agentic-access
  summary_line: 23 operations · 18 acting
api_count: 5
apis:
- description: The Clusters API from Google Kubernetes Engine — 1 operation(s) for clusters.
  name: Google Kubernetes Engine Clusters API
  slug: google-kubernetes-engine-clusters-api
- description: The Google Kubernetes Engine API API from Google Kubernetes Engine — 15 operation(s) for google kubernetes engine api.
  name: Google Kubernetes Engine Google Kubernetes Engine API API
  slug: google-kubernetes-engine-google-kubernetes-engine-api-api
- description: The NodePools API from Google Kubernetes Engine — 1 operation(s) for nodepools.
  name: Google Kubernetes Engine NodePools API
  slug: google-kubernetes-engine-nodepools-api
- description: The Operations API from Google Kubernetes Engine — 1 operation(s) for operations.
  name: Google Kubernetes Engine Operations API
  slug: google-kubernetes-engine-operations-api
- description: The ServerConfig API from Google Kubernetes Engine — 1 operation(s) for serverconfig.
  name: Google Kubernetes Engine ServerConfig API
  slug: google-kubernetes-engine-serverconfig-api
artifact_total: 14
collections:
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
overview: 'Google Kubernetes Engine publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Google Kubernetes Engine API API, NodePools API, and 2 more. Tagged areas include Cloud Native, Containers, Google Cloud, Kubernetes, and Managed Service.


  Google Kubernetes Engine''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 7 more developer resources.'
plans:
- name: Google Kubernetes Engine Plans Pricing
  plan_count: 3
  slug: google-kubernetes-engine-plans-pricing
random_paper: 37
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
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.2
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
- Cloud Native
- Containers
- Google Cloud
- Kubernetes
- Managed Service
- Orchestration
website: https://cloud.google.com/kubernetes-engine
---
