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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Kubernetes Engine Agentic Access
  operation_count: 7
  slug: google-cloud-kubernetes-engine-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: Manage GKE clusters
  name: Google Cloud Kubernetes Engine Clusters API
  slug: google-cloud-kubernetes-engine-clusters-api
- description: Manage node pools within clusters
  name: Google Cloud Kubernetes Engine NodePools API
  slug: google-cloud-kubernetes-engine-nodepools-api
- description: View long-running operations
  name: Google Cloud Kubernetes Engine Operations API
  slug: google-cloud-kubernetes-engine-operations-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine Clusters API
  slug: postman-google-cloud-kubernetes-engine-clusters-api
- collection_type: postman
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine Clusters NodePools API
  slug: postman-google-cloud-kubernetes-engine-nodepools-api
- collection_type: postman
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine Clusters Operations API
  slug: postman-google-cloud-kubernetes-engine-operations-api
- collection_type: open
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine API
  slug: open-gke
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-kubernetes-engine/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-kubernetes-engine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-kubernetes-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-kubernetes-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-kubernetes-engine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-kubernetes-engine-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/kubernetes-engine
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/kubernetes-engine/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/kubernetes-engine/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/kubernetes-engine/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/kubernetes-engine/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/gke-context.jsonld
created: '2026-03-13'
description: Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling containerized applications using Google infrastructure. GKE runs on Kubernetes, providing automated cluster management, auto-scaling, auto-repair, and integrated logging and monitoring for container workloads.
finops:
- name: Google Cloud Kubernetes Engine Finops
  service_category: API
  slug: google-cloud-kubernetes-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-kubernetes-engine.png
json_schemas:
- name: Google Kubernetes Engine Cluster
  property_count: 14
  slug: gke-cluster
jsonld:
- class_count: 11
  name: Gke Context
  property_count: 3
  slug: gke-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Kubernetes Engine
nav: Providers
network: true
overview: 'Google Cloud Kubernetes Engine publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, NodePools API, and Operations API. Tagged areas include Compute, Containers, GKE, Google Cloud, and Kubernetes.


  The Google Cloud Kubernetes Engine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Kubernetes Engine''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Kubernetes Engine Plans Pricing
  plan_count: 3
  slug: google-cloud-kubernetes-engine-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Google Cloud Kubernetes Engine Rate Limits
  slug: google-cloud-kubernetes-engine-rate-limits
rules:
- name: Google Cloud Kubernetes Engine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-kubernetes-engine-jsonschema-spectral-rules
scopes:
- name: Google Cloud Kubernetes Engine Scopes
  scope_count: 1
  slug: google-cloud-kubernetes-engine-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 63.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.9
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-kubernetes-engine/refs/heads/main/screenshots/google-cloud-kubernetes-engine-2026-06-20T182119.png
security:
- kind: authentication
  name: Google Cloud Kubernetes Engine Authentication
  slug: google-cloud-kubernetes-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Kubernetes Engine Domain Security
  slug: google-cloud-kubernetes-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Kubernetes Engine Vulnerability Disclosure
  slug: google-cloud-kubernetes-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-kubernetes-engine
tags:
- Compute
- Containers
- GKE
- Google Cloud
- Kubernetes
- Orchestration
website: https://cloud.google.com/kubernetes-engine
---
