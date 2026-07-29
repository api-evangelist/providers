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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Jakarta Persistence specification for object-relational mapping in Java applications, defining annotations, entity managers, queries via JPQL and the Criteria API, and lifecycle callbacks for mana
  name: Jakarta Persistence API
  slug: jpa
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jpa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jakarta.ee/specifications/persistence/
- group: docs
  title: ''
  type: Documentation
  url: https://jakarta.ee/specifications/persistence/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jakartaee/persistence
created: '2025-01-01'
description: Jakarta Persistence (formerly Java Persistence API / JPA) defines a Java specification and binding layer for the management of persistence and object-relational mapping in Java environments. It provides a standardized ORM framework that enables developers to map Java objects to database tables and interact with relational data using Java rather than SQL. Jakarta Persistence 3.2 is the current stable release with Jakarta EE 11, while version 4.0 is under development for Jakarta EE 12.
finops:
- name: Jpa Finops
  service_category: API
  slug: jpa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jpa.png
layout: provider
modified: '2026-04-28'
name: JPA
nav: Providers
network: true
overview: 'JPA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Java, JPA, Jakarta EE, and ORM.


  JPA''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Jpa Plans Pricing
  plan_count: 3
  slug: jpa-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Jpa Rate Limits
  slug: jpa-rate-limits
score:
  band: emerging
  composite: 20.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jpa/refs/heads/main/screenshots/jpa-2026-06-20T183808.png
security:
- kind: domain-security
  name: Jpa Domain Security
  slug: jpa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jpa
tags:
- Database
- Java
- JPA
- Jakarta EE
- ORM
- Persistence
website: https://jakarta.ee/specifications/persistence/
---
