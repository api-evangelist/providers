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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Go Micro is a distributed systems framework for building microservices in Go, providing service discovery, load balancing, message encoding, RPC, and async messaging out of the box.
  name: Go Micro
  slug: go-micro
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/go-micro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://go-micro.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://go-micro.dev/docs/guide
- group: start
  title: ''
  type: GettingStarted
  url: https://go-micro.dev/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/go-micro
- group: company
  title: ''
  type: Blog
  url: https://go-micro.dev/blog/
created: '2026-03-26'
description: Go Micro is a distributed systems framework for building microservices in Go, providing service discovery, load balancing, message encoding, RPC, and async messaging out of the box.
finops:
- name: Go Micro Finops
  service_category: API
  slug: go-micro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/go-micro.png
json_schemas:
- name: Go Micro Service Options
  property_count: 7
  slug: go-micro-options
- name: Go Micro Service Definition
  property_count: 5
  slug: go-micro-service
layout: provider
modified: '2026-04-28'
name: Go Micro
nav: Providers
network: true
overview: 'Go Micro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Distributed Systems, Frameworks, Go, Golang, and Microservices.


  The Go Micro catalog on APIs.io includes 1 Spectral governance ruleset.


  Go Micro''s developer surface includes documentation, getting-started guide, engineering blog, and 3 more developer resources.'
plans:
- name: Go Micro Plans Pricing
  plan_count: 3
  slug: go-micro-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Go Micro Rate Limits
  slug: go-micro-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Go Micro API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: go-micro-jsonschema-spectral-rules
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 13.3
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 14.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/go-micro/refs/heads/main/screenshots/go-micro-2026-06-20T181938.png
security:
- kind: domain-security
  name: Go Micro Domain Security
  slug: go-micro-domain-security
  summary_line: TLSv1.3
slug: go-micro
tags:
- Distributed Systems
- Frameworks
- Go
- Golang
- Microservices
- RPC
- Service Discovery
website: https://go-micro.dev/
---
