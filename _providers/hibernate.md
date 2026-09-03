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
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: Core Hibernate ORM framework for object-relational mapping.
  name: Hibernate ORM API
  slug: hibernate-orm-api
- description: Bean Validation reference implementation with additional constraints.
  name: Hibernate Validator API
  slug: hibernate-validator-api
- description: Full-text search for domain model with Apache Lucene and Elasticsearch integration.
  name: Hibernate Search API
  slug: hibernate-search-api
- description: Reactive API for Hibernate ORM with non-blocking database access.
  name: Hibernate Reactive API
  slug: hibernate-reactive-api
artifact_total: 8
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hibernate/hibernate-orm/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hibernate/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/hibernate/hibernate-orm/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hibernate-domain-security.yml
- group: operate
  title: ''
  type: Community
  url: https://hibernate.org/community/
- group: operate
  title: ''
  type: Forums
  url: https://discourse.hibernate.org/
- group: operate
  title: ''
  type: Issue Tracker
  url: https://hibernate.atlassian.net/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Hibernate
- group: other
  title: ''
  type: Zulip Chat
  url: https://hibernate.zulipchat.com/
- group: commercial
  title: ''
  type: License
  url: https://www.gnu.org/licenses/lgpl-2.1.html
- group: docs
  title: ''
  type: Contributing Guide
  url: https://hibernate.org/community/contribute/
created: '2024'
description: Hibernate ORM is a powerful object/relational mapping solution for Java applications, providing a framework for mapping an object-oriented domain model to a relational database.
finops:
- name: Hibernate Finops
  service_category: API
  slug: hibernate-finops
image: https://hibernate.org/images/hibernate-logo.svg
layout: provider
modified: '2026-04-28'
name: Hibernate ORM
nav: Providers
network: true
overview: Hibernate ORM publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Java, JPA, Object-Relational Mapping, and ORM.
plans:
- name: Hibernate Plans Pricing
  plan_count: 3
  slug: hibernate-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Hibernate Rate Limits
  slug: hibernate-rate-limits
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -4.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 24.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hibernate/refs/heads/main/screenshots/hibernate-2026-06-20T182721.png
security:
- kind: domain-security
  name: Hibernate Domain Security
  slug: hibernate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hibernate
tags:
- Database
- Java
- JPA
- Object-Relational Mapping
- ORM
- Persistence
website: https://hibernate.org/
---
