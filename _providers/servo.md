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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Programmatic access to Servo web rendering engine APIs, embedding interfaces, and browser component tools.
  name: Servo API
  slug: servo-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servo-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://servo.org/documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/servo
- group: company
  title: ''
  type: Blog
  url: https://servo.org/blog/feed.xml
created: '2026-03-16'
description: Servo is a Linux Foundation Europe project providing an open source, high-performance web rendering engine written in Rust. It aims to be a lightweight, embeddable alternative for web technologies in applications, leveraging Rust's safety guarantees for secure and concurrent web content rendering.
finops:
- name: Servo Finops
  service_category: API
  slug: servo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servo.png
layout: provider
modified: '2026-03-16'
name: Servo
nav: Providers
network: true
overview: 'Servo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Browser, Linux Foundation, Rust, and Web Engine.


  Servo''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Servo Plans Pricing
  plan_count: 3
  slug: servo-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Servo Rate Limits
  slug: servo-rate-limits
score:
  band: minimal
  composite: 10.4
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 10.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/servo/refs/heads/main/screenshots/servo-2026-06-20T193732.png
security:
- kind: domain-security
  name: Servo Domain Security
  slug: servo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: servo
tags:
- Browser
- Linux Foundation
- Rust
- Web Engine
---
