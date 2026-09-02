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
- description: Rules, capabilities, vocabulary, and linked-data description covering classic Gang of Four patterns and key API design patterns.
  name: Design Patterns Catalog
  slug: catalog
artifact_total: 6
common:
- group: docs
  title: ''
  type: Reference
  url: https://refactoring.guru/design-patterns
- group: docs
  title: ''
  type: Reference
  url: https://en.wikipedia.org/wiki/Software_design_pattern
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2025-01-01'
description: Reusable solutions to commonly occurring problems in software design, including the Gang of Four catalog (creational, structural, behavioral) and core API design patterns such as HATEOAS, idempotency keys, webhooks, and sagas.
finops:
- name: Design Patterns Finops
  service_category: API
  slug: design-patterns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/design-patterns.png
jsonld:
- class_count: 0
  name: Design Patterns Context
  property_count: 0
  slug: design-patterns
layout: provider
modified: '2026-04-28'
name: Design Patterns
nav: Providers
network: true
overview: 'Design Patterns publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Best Practices, Object-Oriented Programming, Software Architecture, Software Engineering, and API Design.


  The Design Patterns catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Design Patterns Plans Pricing
  plan_count: 3
  slug: design-patterns-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Design Patterns Rate Limits
  slug: design-patterns-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Design Patterns API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: design-patterns-rules
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 15.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 14.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/design-patterns/refs/heads/main/screenshots/design-patterns-2026-06-20T175933.png
slug: design-patterns
tags:
- Best Practices
- Object-Oriented Programming
- Software Architecture
- Software Engineering
- API Design
---
