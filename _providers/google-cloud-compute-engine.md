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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Compute Engine Agentic Access
  operation_count: 7
  slug: google-cloud-compute-engine-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 4
apis:
- description: Manage persistent disks
  name: Google Cloud Compute Engine Disks API
  slug: google-cloud-compute-engine-disks-api
- description: Manage firewall rules
  name: Google Cloud Compute Engine Firewalls API
  slug: google-cloud-compute-engine-firewalls-api
- description: Manage virtual machine instances
  name: Google Cloud Compute Engine Instances API
  slug: google-cloud-compute-engine-instances-api
- description: Manage VPC networks
  name: Google Cloud Compute Engine Networks API
  slug: google-cloud-compute-engine-networks-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud Compute Engine Google Compute Engine Disks API
  slug: postman-google-cloud-compute-engine-disks-api
- collection_type: postman
  name: Google Cloud Compute Engine Google Compute Engine Disks Firewalls API
  slug: postman-google-cloud-compute-engine-firewalls-api
- collection_type: postman
  name: Google Cloud Compute Engine Google Compute Engine Disks Instances API
  slug: postman-google-cloud-compute-engine-instances-api
- collection_type: postman
  name: Google Cloud Compute Engine Google Compute Engine Disks Networks API
  slug: postman-google-cloud-compute-engine-networks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Compute Engine Google Compute Engine API
  slug: open-compute
- collection_type: open
  name: Google Cloud Compute Engine Google Compute Engine Disks API
  slug: open-google-cloud-compute-engine-disks-api
- collection_type: open
  name: Google Cloud Compute Engine Google Compute Engine Disks Firewalls API
  slug: open-google-cloud-compute-engine-firewalls-api
- collection_type: open
  name: Google Cloud Compute Engine Google Compute Engine Disks Instances API
  slug: open-google-cloud-compute-engine-instances-api
- collection_type: open
  name: Google Cloud Compute Engine Google Compute Engine Disks Networks API
  slug: open-google-cloud-compute-engine-networks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-compute-engine/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-compute-engine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-compute-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-compute-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-compute-engine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-compute-engine-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/compute
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/compute/docs/quickstart-linux
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/compute/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/compute/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/compute/pricing
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
  url: https://cloud.google.com/compute/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/compute-context.jsonld
created: '2026-03-13'
description: Google Cloud Compute Engine delivers virtual machines running in Google's innovative data centers and worldwide fiber network. Compute Engine VMs boot quickly, come with persistent disk storage, and deliver consistent performance. It offers predefined and custom machine types, preemptible VMs, and sole-tenant nodes for specialized workloads.
finops:
- name: Google Cloud Compute Engine Finops
  service_category: API
  slug: google-cloud-compute-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-compute-engine.png
json_schemas:
- name: Google Compute Engine Instance
  property_count: 10
  slug: compute-instance
jsonld:
- class_count: 11
  name: Compute Context
  property_count: 3
  slug: compute-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Compute Engine
nav: Providers
network: true
overview: 'Google Cloud Compute Engine publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Disks API, Firewalls API, Instances API, and 1 more. Tagged areas include Compute, Google Cloud, IaaS, Infrastructure, and Virtual Machines.


  The Google Cloud Compute Engine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Compute Engine''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Compute Engine Plans Pricing
  plan_count: 3
  slug: google-cloud-compute-engine-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google Cloud Compute Engine Rate Limits
  slug: google-cloud-compute-engine-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Compute Engine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-compute-engine-jsonschema-spectral-rules
scopes:
- name: Google Cloud Compute Engine Scopes
  scope_count: 2
  slug: google-cloud-compute-engine-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 48.4
  delta: -6.3
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 65.7
    developer_ergonomics: 52.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-compute-engine/refs/heads/main/screenshots/google-cloud-compute-engine-2026-06-20T182054.png
security:
- kind: authentication
  name: Google Cloud Compute Engine Authentication
  slug: google-cloud-compute-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Compute Engine Domain Security
  slug: google-cloud-compute-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Compute Engine Vulnerability Disclosure
  slug: google-cloud-compute-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-compute-engine
tags:
- Compute
- Google Cloud
- IaaS
- Infrastructure
- Virtual Machines
website: https://cloud.google.com/compute
---
