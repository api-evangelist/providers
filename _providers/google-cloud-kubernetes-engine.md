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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Kubernetes Engine Agentic Access
  operation_count: 7
  slug: google-cloud-kubernetes-engine-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://container.googleapis.com
  baseurl_source: declared
  description: Manage GKE clusters
  name: Google Cloud Kubernetes Engine Clusters API
  slug: google-cloud-kubernetes-engine-clusters-api
- baseURL: https://container.googleapis.com
  baseurl_source: declared
  description: Manage node pools within clusters
  name: Google Cloud Kubernetes Engine NodePools API
  slug: google-cloud-kubernetes-engine-nodepools-api
- baseURL: https://container.googleapis.com
  baseurl_source: declared
  description: View long-running operations
  name: Google Cloud Kubernetes Engine Operations API
  slug: google-cloud-kubernetes-engine-operations-api
artifact_total: 22
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine API
  slug: open-gke
- collection_type: open
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine Clusters API
  slug: open-google-cloud-kubernetes-engine-clusters-api
- collection_type: open
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine Clusters NodePools API
  slug: open-google-cloud-kubernetes-engine-nodepools-api
- collection_type: open
  name: Google Cloud Kubernetes Engine Google Kubernetes Engine Clusters Operations API
  slug: open-google-cloud-kubernetes-engine-operations-api
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
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google Cloud Kubernetes Engine Rate Limits
  slug: google-cloud-kubernetes-engine-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Kubernetes Engine API Rules
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
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
