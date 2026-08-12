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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: The HAProxy Data Plane API is a REST API for managing HAProxy configuration dynamically. It allows runtime configuration of frontends, backends, servers, ACLs, and other HAProxy objects without requir
  name: HAProxy Data Plane API
  slug: haproxy-data-plane-api
- description: 'The HAProxy Runtime API (formerly known as the stats socket) is a socket-based interface for dynamically managing HAProxy at runtime. It allows operators to enable or disable servers, adjust weights, '
  name: HAProxy Runtime API
  slug: haproxy-runtime-api
- description: The HAProxy Kubernetes Ingress Controller implements routing rules defined in Kubernetes Ingress resources, dynamically updating HAProxy configuration as pods are added or removed from the cluster. It
  name: HAProxy Kubernetes Ingress Controller
  slug: haproxy-kubernetes-ingress-controller
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/haproxytech/dataplaneapi/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/haproxytech/dataplaneapi/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/haproxytech/dataplaneapi/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haproxy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/haproxy-technologies
- group: company
  title: ''
  type: Website
  url: https://www.haproxy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.haproxy.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/haproxy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/haproxytech
- group: operate
  title: ''
  type: Community
  url: https://discourse.haproxy.org/
- group: company
  title: ''
  type: Blog
  url: https://www.haproxy.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.haproxy.com/support/support-options
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.haproxy.com/legal
created: '2026-03-16'
description: HAProxy is a free, very fast and reliable reverse-proxy offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It exposes a Data Plane API for dynamic configuration management and a stats socket for runtime management.
finops:
- name: Haproxy Finops
  service_category: API
  slug: haproxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haproxy.png
layout: provider
modified: '2026-03-18'
name: HAProxy
nav: Providers
network: true
overview: 'HAProxy publishes 1 API on the [APIs.io](https://apis.io/) network: Data Plane API. Tagged areas include High Availability, Load Balancing, Networking, and Reverse Proxy.


  HAProxy''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Haproxy Plans Pricing
  plan_count: 3
  slug: haproxy-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Haproxy Rate Limits
  slug: haproxy-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: -7.8
  facets:
    commercial_clarity: 26.3
    contract_quality: 32.3
    developer_ergonomics: 15.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/screenshots/haproxy-2026-06-20T182509.png
security:
- kind: domain-security
  name: Haproxy Domain Security
  slug: haproxy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: haproxy
tags:
- High Availability
- Load Balancing
- Networking
- Reverse Proxy
website: https://www.haproxy.org/
---
