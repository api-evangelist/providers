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
api_count: 2
apis:
- description: Gloo Mesh Enterprise (also called Gloo Platform) is a service mesh management platform built on Istio that provides intra-mesh and multi-cluster routing, access policies, JWT authentication, rate limi
  name: Gloo Mesh Enterprise
  slug: gloo-mesh-enterprise
- description: Gloo Mesh Core extends a single Istio service mesh with insights, operational tooling, and lifecycle management for upstream Istio deployments. It surfaces Istio insights, telemetry, and a curated set
  name: Gloo Mesh Core
  slug: gloo-mesh-core
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gloo-mesh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gloo-mesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solo.io/
- group: start
  title: ''
  type: Portal
  url: https://www.solo.io/products/gloo-mesh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solo.io/gloo-mesh-enterprise/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.solo.io/gloo-mesh-enterprise/latest/getting_started/
- group: company
  title: ''
  type: Blog
  url: https://www.solo.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solo-io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.solo.io/gloo-mesh-enterprise/latest/changelog/
- group: operate
  title: ''
  type: Community
  url: https://slack.solo.io/
- group: operate
  title: ''
  type: Support
  url: https://www.solo.io/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solo.io/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solo.io/legal/privacy-policy/
created: '2026-04-28'
description: Gloo Mesh is an enterprise service mesh management platform from Solo.io built on Istio, providing multi-cluster and multi-mesh traffic management, security policy enforcement, and observability across hybrid cloud environments. It simplifies service mesh operations with a unified control plane and policy management interface, exposing Kubernetes Custom Resource Definitions (CRDs) such as AccessPolicy, JwtPolicy, and RatelimitPolicy as the primary API surface.
finops:
- name: Gloo Mesh Finops
  service_category: API
  slug: gloo-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gloo-mesh.png
layout: provider
modified: '2026-04-28'
name: Gloo Mesh
nav: Providers
network: true
overview: 'Gloo Mesh publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Istio, Kubernetes, Multi-Cluster, Open-Source, and Service Mesh.


  Gloo Mesh''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 7 more developer resources.'
plans:
- name: Gloo Mesh Plans Pricing
  plan_count: 3
  slug: gloo-mesh-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Gloo Mesh Rate Limits
  slug: gloo-mesh-rate-limits
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gloo-mesh/refs/heads/main/screenshots/gloo-mesh-2026-06-20T181924.png
security:
- kind: domain-security
  name: Gloo Mesh Domain Security
  slug: gloo-mesh-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gloo Mesh Vulnerability Disclosure
  slug: gloo-mesh-vulnerability-disclosure
  summary_line: disclosure policy published
slug: gloo-mesh
tags:
- Istio
- Kubernetes
- Multi-Cluster
- Open-Source
- Service Mesh
website: https://www.solo.io/
---
