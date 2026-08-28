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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Anthos Agentic Access
  operation_count: 8
  slug: google-anthos-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: The Anthos Multicloud API provides programmatic access to manage Anthos clusters running on other public clouds such as AWS and Azure. Developers can use the API to create, update, and delete attached
  name: Anthos Multicloud API
  slug: anthos-multicloud-api
- description: Operations for managing bare metal on-premises clusters
  name: Google Anthos BareMetalClusters API
  slug: google-anthos-baremetalclusters-api
- description: Operations for managing VMware-based on-premises clusters
  name: Google Anthos VmwareClusters API
  slug: google-anthos-vmwareclusters-api
- description: Operations for managing node pools in VMware clusters
  name: Google Anthos VmwareNodePools API
  slug: google-anthos-vmwarenodepools-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Anthos Google GKE On-Prem API
  slug: open-gke-on-prem-api
- collection_type: open
  name: Google Anthos Google GKE On-Prem BareMetalClusters API
  slug: open-google-anthos-baremetalclusters-api
- collection_type: open
  name: Google Anthos Google GKE On-Prem BareMetalClusters VmwareClusters API
  slug: open-google-anthos-vmwareclusters-api
- collection_type: open
  name: Google Anthos Google GKE On-Prem BareMetalClusters VmwareNodePools API
  slug: open-google-anthos-vmwarenodepools-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-anthos-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-anthos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-anthos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-anthos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-anthos-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/anthos/docs/setup/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/anthos/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-anthos-context.jsonld
created: '2026-03-13'
description: Google Anthos is a managed application platform that extends Google Cloud services and engineering practices to hybrid and multi-cloud environments. Built on Kubernetes, Anthos enables consistent development and operations across on-premises data centers, Google Cloud, and other public clouds like AWS and Azure, with centralized management, policy enforcement, and service mesh capabilities.
finops:
- name: Google Anthos Finops
  service_category: API
  slug: google-anthos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-anthos.png
json_schemas:
- name: Google Anthos On-Prem Cluster
  property_count: 11
  slug: google-anthos-cluster
jsonld:
- class_count: 0
  name: Google Anthos Context
  property_count: 3
  slug: google-anthos-context
layout: provider
modified: '2026-05-19'
name: Google Anthos
nav: Providers
network: true
overview: 'Google Anthos publishes 3 APIs on the [APIs.io](https://apis.io/) network: BareMetalClusters API, VmwareClusters API, and VmwareNodePools API. Tagged areas include Container Platform, Hybrid Cloud, Kubernetes, Multi-Cloud, and On-Premises.


  The Google Anthos catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Anthos'' developer surface includes authentication, getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Google Anthos Plans Pricing
  plan_count: 3
  slug: google-anthos-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Google Anthos Rate Limits
  slug: google-anthos-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Anthos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-anthos-jsonschema-spectral-rules
scopes:
- name: Google Anthos Scopes
  scope_count: 1
  slug: google-anthos-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.3
  delta: 1.9
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-anthos/refs/heads/main/screenshots/google-anthos-2026-06-20T182013.png
security:
- kind: authentication
  name: Google Anthos Authentication
  slug: google-anthos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Anthos Domain Security
  slug: google-anthos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Anthos Vulnerability Disclosure
  slug: google-anthos-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-anthos
tags:
- Container Platform
- Hybrid Cloud
- Kubernetes
- Multi-Cloud
- On-Premises
- Service Mesh
---
