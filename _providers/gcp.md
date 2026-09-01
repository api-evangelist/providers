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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Gcp Agentic Access
  operation_count: 18
  slug: gcp-agentic-access
  summary_line: 18 operations · 9 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Persistent disks
  name: Google Cloud Platform APIs Disks API
  slug: gcp-disks-api
- description: Firewall rules
  name: Google Cloud Platform APIs Firewalls API
  slug: gcp-firewalls-api
- description: VM images
  name: Google Cloud Platform APIs Images API
  slug: gcp-images-api
- description: Virtual machine instances
  name: Google Cloud Platform APIs Instances API
  slug: gcp-instances-api
- description: Machine type catalog
  name: Google Cloud Platform APIs MachineTypes API
  slug: gcp-machinetypes-api
- description: VPC networks
  name: Google Cloud Platform APIs Networks API
  slug: gcp-networks-api
- description: Disk snapshots
  name: Google Cloud Platform APIs Snapshots API
  slug: gcp-snapshots-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Compute Engine Disks API
  slug: open-gcp-disks-api
- collection_type: open
  name: Google Cloud Compute Engine Disks Firewalls API
  slug: open-gcp-firewalls-api
- collection_type: open
  name: Google Cloud Compute Engine Disks Images API
  slug: open-gcp-images-api
- collection_type: open
  name: Google Cloud Compute Engine Disks Instances API
  slug: open-gcp-instances-api
- collection_type: open
  name: Google Cloud Compute Engine Disks MachineTypes API
  slug: open-gcp-machinetypes-api
- collection_type: open
  name: Google Cloud Compute Engine Disks Networks API
  slug: open-gcp-networks-api
- collection_type: open
  name: Google Cloud Compute Engine Disks Snapshots API
  slug: open-gcp-snapshots-api
- collection_type: open
  name: Google Cloud Compute Engine API
  slug: open-gcp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gcp-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gcp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gcp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gcp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gcp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gcp-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/docs
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/sdk
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
created: '2024-01-01'
description: Comprehensive collection of Google Cloud Platform APIs for cloud computing, storage, machine learning, and infrastructure management.
finops:
- name: Gcp Finops
  service_category: API
  slug: gcp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gcp.png
layout: provider
modified: '2026-04-28'
name: Google Cloud Platform APIs
nav: Providers
network: true
overview: 'Google Cloud Platform APIs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Disks API, Firewalls API, Images API, and 4 more. Tagged areas include Cloud Computing, Databases, Infrastructure, Machine-Learning, and Networking.


  Google Cloud Platform APIs'' developer surface includes authentication, developer console, support, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Gcp Plans Pricing
  plan_count: 3
  slug: gcp-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Gcp Rate Limits
  slug: gcp-rate-limits
scopes:
- name: Gcp Scopes
  scope_count: 2
  slug: gcp-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 51.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gcp/refs/heads/main/screenshots/gcp-2026-06-20T181700.png
security:
- kind: authentication
  name: Gcp Authentication
  slug: gcp-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gcp Domain Security
  slug: gcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gcp Vulnerability Disclosure
  slug: gcp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gcp
tags:
- Cloud Computing
- Databases
- Infrastructure
- Machine-Learning
- Networking
- Security
- Serverless
- Storage
---
