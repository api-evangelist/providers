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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Go Kit is a programming toolkit for building microservices in Go, emphasizing domain-driven design, transport-agnostic service definitions, and best practices for distributed systems.
  name: Go Kit
  slug: go-kit
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/go-kit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gokit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://gokit.io/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://gokit.io/examples/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/go-kit
created: '2026-03-26'
description: Go Kit is a programming toolkit for building microservices in Go, emphasizing domain-driven design, transport-agnostic service definitions, and best practices for distributed systems.
finops:
- name: Go Kit Finops
  service_category: API
  slug: go-kit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/go-kit.png
json_schemas:
- name: Go Kit Service Transport Configuration
  property_count: 10
  slug: go-kit-transport-config
layout: provider
modified: '2026-04-28'
name: Go Kit
nav: Providers
network: true
overview: 'Go Kit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Distributed Systems, Domain-Driven Design, Frameworks, Go, and Golang.


  The Go Kit catalog on APIs.io includes 1 Spectral governance ruleset.


  Go Kit''s developer surface includes documentation, getting-started guide, and 3 more developer resources.'
plans:
- name: Go Kit Plans Pricing
  plan_count: 3
  slug: go-kit-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Go Kit Rate Limits
  slug: go-kit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Go Kit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: go-kit-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 17.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/go-kit/refs/heads/main/screenshots/go-kit-2026-06-20T181936.png
security:
- kind: domain-security
  name: Go Kit Domain Security
  slug: go-kit-domain-security
  summary_line: TLSv1.3
slug: go-kit
tags:
- Distributed Systems
- Domain-Driven Design
- Frameworks
- Go
- Golang
- Microservices
website: https://gokit.io/
---
