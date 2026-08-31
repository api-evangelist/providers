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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Vpc Agentic Access
  operation_count: 7
  slug: google-cloud-vpc-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- description: Manage firewall rules for VPC networks
  name: Google Cloud VPC Firewalls API
  slug: google-cloud-vpc-firewalls-api
- description: Manage VPC networks
  name: Google Cloud VPC Networks API
  slug: google-cloud-vpc-networks-api
- description: Manage routes for VPC networks
  name: Google Cloud VPC Routes API
  slug: google-cloud-vpc-routes-api
- description: Manage subnetworks within VPC networks
  name: Google Cloud VPC Subnetworks API
  slug: google-cloud-vpc-subnetworks-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud VPC Firewalls API
  slug: open-google-cloud-vpc-firewalls-api
- collection_type: open
  name: Google Cloud VPC Firewalls Networks API
  slug: open-google-cloud-vpc-networks-api
- collection_type: open
  name: Google Cloud VPC Firewalls Routes API
  slug: open-google-cloud-vpc-routes-api
- collection_type: open
  name: Google Cloud VPC Firewalls Subnetworks API
  slug: open-google-cloud-vpc-subnetworks-api
- collection_type: open
  name: Google Cloud VPC API
  slug: open-openapi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-vpc-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-vpc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-vpc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-vpc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-vpc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-vpc-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/vpc/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/vpc/network-pricing
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/vpc-release-notes.xml
created: '2026-03-13'
description: Google Cloud Virtual Private Cloud (VPC) provides networking functionality for Google Cloud resources, enabling you to create and manage virtual networks, subnets, firewall rules, and routes for secure and isolated cloud networking.
finops:
- name: Google Cloud Vpc Finops
  service_category: API
  slug: google-cloud-vpc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-vpc.png
layout: provider
modified: '2026-05-19'
name: Google Cloud VPC
nav: Providers
network: true
overview: 'Google Cloud VPC publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Firewalls API, Networks API, Routes API, and 1 more. Tagged areas include Firewall, Google Cloud, Networking, Virtual Networks, and VPC.


  The Google Cloud VPC catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud VPC''s developer surface includes authentication, getting-started guide, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Google Cloud Vpc Plans Pricing
  plan_count: 3
  slug: google-cloud-vpc-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Google Cloud Vpc Rate Limits
  slug: google-cloud-vpc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud VPC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-vpc-jsonschema-spectral-rules
scopes:
- name: Google Cloud Vpc Scopes
  scope_count: 2
  slug: google-cloud-vpc-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-vpc/refs/heads/main/screenshots/google-cloud-vpc-2026-06-20T182148.png
security:
- kind: authentication
  name: Google Cloud Vpc Authentication
  slug: google-cloud-vpc-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Vpc Domain Security
  slug: google-cloud-vpc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Vpc Vulnerability Disclosure
  slug: google-cloud-vpc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-vpc
tags:
- Firewall
- Google Cloud
- Networking
- Virtual Networks
- VPC
---
