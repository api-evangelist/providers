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
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: Gloo Edge is a feature-rich, Kubernetes-native ingress controller and API gateway built on Envoy Proxy, supporting advanced routing, security policies, and observability for cloud-native workloads. It
  name: Gloo Edge
  slug: gloo-edge
- description: Gloo Gateway is the next-generation API gateway from Solo.io built on Envoy Proxy and implementing the Kubernetes Gateway API specification. It provides advanced traffic management, security, and exte
  name: Gloo Gateway
  slug: gloo-gateway
- description: Gloo Mesh is an enterprise service mesh management platform from Solo.io built on Istio, providing multi-cluster and multi-mesh traffic management, security policy enforcement, and observability acros
  name: Gloo Mesh
  slug: gloo-mesh
- description: Gloo Portal is a developer portal product from Solo.io that enables organizations to expose, document, and manage API products for internal and external consumers. It integrates with Gloo Gateway to p
  name: Gloo Portal
  slug: gloo-portal
artifact_total: 9
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/solo-io/gloo/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gloo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gloo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solo.io/
- group: start
  title: ''
  type: Portal
  url: https://www.solo.io/products/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solo.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.solo.io/gloo-edge/latest/getting_started/
- group: company
  title: ''
  type: Blog
  url: https://www.solo.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solo-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/solo-io/gloo
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/solo-io/gloo/releases
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
created: '2026-03-18'
description: Gloo is a suite of open-source and enterprise API gateway and service mesh products from Solo.io built on Envoy Proxy, offering advanced traffic management, security, observability, and developer portal capabilities for Kubernetes and cloud-native environments.
finops:
- name: Gloo Finops
  service_category: API
  slug: gloo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gloo.png
layout: provider
modified: '2026-04-28'
name: Gloo
nav: Providers
network: true
overview: 'Gloo publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, Envoy, Kubernetes, Open-Source, and Service Mesh.


  Gloo''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 9 more developer resources.'
plans:
- name: Gloo Plans Pricing
  plan_count: 3
  slug: gloo-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Gloo Rate Limits
  slug: gloo-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gloo/refs/heads/main/screenshots/gloo-2026-06-20T181923.png
security:
- kind: domain-security
  name: Gloo Domain Security
  slug: gloo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gloo Vulnerability Disclosure
  slug: gloo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: gloo
tags:
- API Gateway
- Envoy
- Kubernetes
- Open-Source
- Service Mesh
website: https://www.solo.io/
---
