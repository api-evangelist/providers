---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Service mesh control plane for Kubernetes that implements the Service Mesh Interface (SMI) specification, providing traffic management, security, and observability for microservices via Envoy sidecar '
  name: Open Service Mesh
  slug: open-service-mesh
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/openservicemesh/osm/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/openservicemesh/osm/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/openservicemesh/osm/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/openservicemesh/osm/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/openservicemesh/osm/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/openservicemesh/osm/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-service-mesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openservicemesh.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openservicemesh.io
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/openservicemesh/osm
created: '2026-04-28'
description: Open Service Mesh (OSM) is a lightweight, extensible, cloud native service mesh built on Envoy and the Service Mesh Interface (SMI) specification. OSM provides traffic shifting, mutual TLS, access control, observability, and automatic sidecar injection for Kubernetes-based microservices. The project is now archived by the CNCF.
finops:
- name: Open Service Mesh Finops
  service_category: API
  slug: open-service-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-service-mesh.png
layout: provider
modified: '2026-04-28'
name: Open Service Mesh
nav: Providers
network: true
overview: 'Open Service Mesh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Envoy, Kubernetes, Microservices, and Service Mesh.


  Open Service Mesh''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Open Service Mesh Plans Pricing
  plan_count: 3
  slug: open-service-mesh-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Open Service Mesh Rate Limits
  slug: open-service-mesh-rate-limits
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 24.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-service-mesh/refs/heads/main/screenshots/open-service-mesh-2026-06-20T190850.png
security:
- kind: domain-security
  name: Open Service Mesh Domain Security
  slug: open-service-mesh-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-service-mesh
tags:
- Cloud-Native
- Envoy
- Kubernetes
- Microservices
- Service Mesh
- SMI
website: https://openservicemesh.io
---
