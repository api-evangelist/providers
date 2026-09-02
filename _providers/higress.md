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
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: Higress is a next-generation cloud-native API gateway that provides intelligent routing, traffic management, authentication, and observability capabilities for microservices architectures.
  name: Higress
  slug: higress
- description: The Higress Console API provides a RESTful management interface for configuring and administering a running Higress gateway instance. It supports management of ingress routes, service sources, TLS cer
  name: Higress Console API
  slug: higress-console-api
- description: Higress AI Gateway extends the core Higress gateway with AI-specific capabilities including LLM proxy routing, multi-provider support for OpenAI-compatible APIs, prompt templating, token-based rate li
  name: Higress AI Gateway
  slug: higress-ai-gateway
- description: The Higress Wasm Plugin API provides a WebAssembly-based extension interface for developing and deploying custom plugins on the Higress gateway. Plugins can be written in Go, Rust, C++, or any languag
  name: Higress Wasm Plugin API
  slug: higress-wasm-plugin-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/higress-group/higress/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/higress-group/higress/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/alibaba/higress/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/higress-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://higress.io/en-us/
- group: docs
  title: ''
  type: Documentation
  url: https://higress.io/en-us/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://higress.io/en-us/docs/user/quickstart
- group: company
  title: ''
  type: Blog
  url: https://higress.io/en-us/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/alibaba/higress/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alibaba
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/alibaba/higress
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/alibaba/higress/issues
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/higress
- group: agent
  title: ''
  type: LlmsText
  url: https://higress.io/llms.txt
created: '2026-03-16'
description: Higress is a cloud-native API gateway built on Istio and Envoy, providing enterprise-grade API gateway capabilities including traffic management, security, observability, and AI plugin support. It is an open-source project under the CNCF ecosystem.
finops:
- name: Higress Finops
  service_category: API
  slug: higress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/higress.png
layout: provider
modified: '2026-04-28'
name: Higress
nav: Providers
network: true
overview: 'Higress publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, Cloud-Native, Istio, and Kubernetes.


  Higress'' developer surface includes documentation, getting-started guide, engineering blog, changelog, and 10 more developer resources.'
plans:
- name: Higress Plans Pricing
  plan_count: 3
  slug: higress-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Higress Rate Limits
  slug: higress-rate-limits
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 22.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/higress/refs/heads/main/screenshots/higress-2026-06-20T182735.png
security:
- kind: domain-security
  name: Higress Domain Security
  slug: higress-domain-security
  summary_line: TLSv1.3
slug: higress
tags:
- API Gateway
- Cloud-Native
- Istio
- Kubernetes
website: https://higress.io/en-us/
---
