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
  scored_at: '2026-09-05'
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
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
