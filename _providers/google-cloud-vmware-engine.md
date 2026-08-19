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
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Vmware Engine Agentic Access
  operation_count: 7
  slug: google-cloud-vmware-engine-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: Manage clusters within private clouds
  name: Google Cloud VMware Engine Clusters API
  slug: google-cloud-vmware-engine-clusters-api
- description: Manage network policies
  name: Google Cloud VMware Engine NetworkPolicies API
  slug: google-cloud-vmware-engine-networkpolicies-api
- description: Manage VMware private clouds
  name: Google Cloud VMware Engine PrivateClouds API
  slug: google-cloud-vmware-engine-privateclouds-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud VMware Engine Clusters API
  slug: open-google-cloud-vmware-engine-clusters-api
- collection_type: open
  name: Google Cloud VMware Engine Clusters NetworkPolicies API
  slug: open-google-cloud-vmware-engine-networkpolicies-api
- collection_type: open
  name: Google Cloud VMware Engine Clusters PrivateClouds API
  slug: open-google-cloud-vmware-engine-privateclouds-api
- collection_type: open
  name: Google Cloud VMware Engine API
  slug: open-vmwareengine
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-vmware-engine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-vmware-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-vmware-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-vmware-engine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-vmware-engine-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/vmware-engine/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/vmware-engine/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vmwareengine-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/vmware-engine-release-notes.xml
created: '2026-03-13'
description: Google Cloud VMware Engine is a fully managed service that lets you run VMware workloads natively on Google Cloud infrastructure. It provides dedicated, single-tenant VMware SDDC environments with vSphere, vSAN, NSX-T, and HCX, enabling seamless migration and management of VMware-based applications in the cloud.
finops:
- name: Google Cloud Vmware Engine Finops
  service_category: API
  slug: google-cloud-vmware-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-vmware-engine.png
json_schemas:
- name: Google Cloud VMware Engine Private Cloud
  property_count: 8
  slug: vmwareengine-privatecloud
jsonld:
- class_count: 8
  name: Vmwareengine Context
  property_count: 3
  slug: vmwareengine-context
layout: provider
modified: '2026-05-19'
name: Google Cloud VMware Engine
nav: Providers
network: true
overview: 'Google Cloud VMware Engine publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, NetworkPolicies API, and PrivateClouds API. Tagged areas include Compute, Google Cloud, Migration, Private Cloud, and Virtualization.


  The Google Cloud VMware Engine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud VMware Engine''s developer surface includes authentication, getting-started guide, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Google Cloud Vmware Engine Plans Pricing
  plan_count: 3
  slug: google-cloud-vmware-engine-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Google Cloud Vmware Engine Rate Limits
  slug: google-cloud-vmware-engine-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud VMware Engine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-vmware-engine-jsonschema-spectral-rules
scopes:
- name: Google Cloud Vmware Engine Scopes
  scope_count: 1
  slug: google-cloud-vmware-engine-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 34.5
  delta: -9.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 65.7
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-vmware-engine/refs/heads/main/screenshots/google-cloud-vmware-engine-2026-06-20T182153.png
security:
- kind: authentication
  name: Google Cloud Vmware Engine Authentication
  slug: google-cloud-vmware-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Vmware Engine Domain Security
  slug: google-cloud-vmware-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Vmware Engine Vulnerability Disclosure
  slug: google-cloud-vmware-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-vmware-engine
tags:
- Compute
- Google Cloud
- Migration
- Private Cloud
- Virtualization
- VMware
---
