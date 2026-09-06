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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HAProxy Data Plane API is a REST API for managing HAProxy configuration dynamically. It allows runtime configuration of frontends, backends, servers, ACLs, and other HAProxy objects without requir
  name: HAProxy Data Plane API
  slug: haproxy-data-plane-api
- description: 'The HAProxy Runtime API (formerly known as the stats socket) is a socket-based interface for dynamically managing HAProxy at runtime. It allows operators to enable or disable servers, adjust weights, '
  name: HAProxy Runtime API
  slug: haproxy-runtime-api
- description: The HAProxy Kubernetes Ingress Controller implements routing rules defined in Kubernetes Ingress resources, dynamically updating HAProxy configuration as pods are added or removed from the cluster. It
  name: HAProxy Kubernetes Ingress Controller
  slug: haproxy-kubernetes-ingress-controller
artifact_total: 8
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/haproxy-authentication.yml
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
- group: design
  title: ''
  type: Conventions
  url: conventions/haproxy-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/haproxy-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/haproxy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/haproxy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/haproxy-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/haproxy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/haproxy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/haproxy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/haproxy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/haproxy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/haproxy-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/haproxy-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/haproxy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/haproxy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/haproxy-finops.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.haproxy.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://my.haproxy.com/portal/cust/login
created: '2026-03-16'
description: HAProxy is a free, very fast and reliable reverse-proxy offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It exposes a Data Plane API for dynamic configuration management and a stats socket for runtime management.
finops:
- name: Haproxy Finops
  service_category: API
  slug: haproxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haproxy.png
layout: provider
modified: '2026-08-28'
name: HAProxy
nav: Providers
network: true
overview: 'HAProxy publishes 1 API on the [APIs.io](https://apis.io/) network: Data Plane API. Tagged areas include High Availability, Load Balancing, Networking, Reverse Proxy, and Proxy.


  HAProxy''s developer surface includes authentication, documentation, engineering blog, support, CLI, changelog, and 26 more developer resources.'
plans:
- name: Haproxy Plans Pricing
  plan_count: 0
  slug: haproxy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Haproxy Rate Limits
  slug: haproxy-rate-limits
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 63.7
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/screenshots/haproxy-2026-06-20T182509.png
security:
- kind: authentication
  name: Haproxy Authentication
  slug: haproxy-authentication
  summary_line: http · 1 scheme
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
- Proxy
- Kubernetes
- Ingress
- Open-Source
- Infrastructure
- Application Delivery
website: https://www.haproxy.org/
---
