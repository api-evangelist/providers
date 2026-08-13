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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Abstract REST API provides programmatic access to design projects, branches, commits, files, collections, and component libraries managed within the Abstract platform. Access is provided via the a
  name: Abstract API
  slug: abstract-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abstract-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goabstract.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.abstract.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/goabstract
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abstract-app
- group: company
  title: ''
  type: Blog
  url: https://www.goabstract.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goabstract.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goabstract.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/goabstract
- group: commercial
  title: ''
  type: Plans
  url: plans/abstract-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abstract-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/abstract-finops.yml
created: '2026-06-13'
description: Abstract is a design version control and collaboration platform that brings git-inspired branching, merging, and change history to design teams. It provides a REST API and JavaScript SDK for managing projects, branches, commits, files, collections, and design component libraries across teams, integrating with Sketch and other design tools.
finops:
- name: Abstract Finops
  service_category: ''
  slug: abstract-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abstract.png
json_schemas:
- name: Abstract API Schemas
  property_count: 0
  slug: abstract-api
jsonld:
- class_count: 19
  name: Abstract Api Context
  property_count: 3
  slug: abstract-api
layout: provider
modified: '2026-06-13'
name: Abstract
nav: Providers
network: true
overview: 'Abstract publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Version Control, Collaboration, Sketch, and Design Systems.


  The Abstract catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Abstract''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Abstract Plans Pricing
  plan_count: 5
  slug: abstract-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Abstract Rate Limits
  slug: abstract-rate-limits
rules:
- name: Abstract API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: abstract-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 34.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abstract/refs/heads/main/screenshots/abstract-2026-06-20T163425.png
security:
- kind: domain-security
  name: Abstract Domain Security
  slug: abstract-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abstract
tags:
- Design
- Version Control
- Collaboration
- Sketch
- Design Systems
website: https://www.goabstract.com
---
