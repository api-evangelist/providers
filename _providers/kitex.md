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
api_count: 1
apis:
- description: Kitex is a high-performance, extensible RPC framework for building microservices in Go, developed by ByteDance. It supports Thrift and Protocol Buffers serialization, provides built-in service governa
  name: Kitex
  slug: kitex
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cloudwego/kitex/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cloudwego/kitex/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cloudwego/kitex/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cloudwego/kitex/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cloudwego/kitex/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kitex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudwego.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cloudwego.io/docs/kitex/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cloudwego.io/docs/kitex/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudwego
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudwego/kitex
- group: company
  title: ''
  type: Blog
  url: https://www.cloudwego.io/blog/
created: '2026-03-26'
description: Kitex is a high-performance, extensible RPC framework for building microservices in Go, developed by ByteDance. It supports Thrift and Protocol Buffers serialization, provides built-in service governance features including service discovery, load balancing, circuit breaking, and retry policies, and is optimized for high throughput and low latency.
finops:
- name: Kitex Finops
  service_category: API
  slug: kitex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kitex.png
json_schemas:
- name: Kitex Service Configuration
  property_count: 3
  slug: kitex-configuration
layout: provider
modified: '2026-04-28'
name: Kitex
nav: Providers
network: true
overview: 'Kitex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Frameworks, Go, High Performance, Microservices, and Protocol Buffers.


  The Kitex catalog on APIs.io includes 1 Spectral governance ruleset.


  Kitex''s developer surface includes documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Kitex Plans Pricing
  plan_count: 3
  slug: kitex-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Kitex Rate Limits
  slug: kitex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kitex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kitex-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 24.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kitex/refs/heads/main/screenshots/kitex-2026-06-20T184050.png
security:
- kind: domain-security
  name: Kitex Domain Security
  slug: kitex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kitex
tags:
- Frameworks
- Go
- High Performance
- Microservices
- Protocol Buffers
- RPC
- Thrift
website: https://www.cloudwego.io/
---
