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
api_count: 2
apis:
- description: The next generation of JUnit for Java 8 and beyond, providing an expressive API for writing tests and extensions.
  name: JUnit 5 Jupiter
  slug: junit5
- description: The legacy version of JUnit still widely used in Java projects.
  name: JUnit 4 Vintage
  slug: junit4
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/junit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://junit.org/junit5/
- group: docs
  title: ''
  type: Documentation
  url: https://junit.org/junit5/docs/current/user-guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/junit-team
- group: commercial
  title: ''
  type: License
  url: https://github.com/junit-team/junit5/blob/main/LICENSE.md
- group: design
  title: ''
  type: JSONLD
  url: json-ld/junit-context.jsonld
created: '2024-01-01'
description: 'JUnit is a programmer-friendly testing framework for Java and the JVM. JUnit 5 is the next generation of JUnit, composed of three modules: JUnit Platform, JUnit Jupiter, and JUnit Vintage.'
finops:
- name: Junit Finops
  service_category: API
  slug: junit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/junit.png
json_schemas:
- name: JUnit Test Report
  property_count: 1
  slug: junit-report
jsonld:
- class_count: 13
  name: Junit Context
  property_count: 0
  slug: junit-context
layout: provider
modified: '2026-04-28'
name: JUnit
nav: Providers
network: true
overview: 'JUnit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Java, TDD, Test Automation, Testing, and Unit Testing.


  The JUnit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JUnit''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Junit Plans Pricing
  plan_count: 3
  slug: junit-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Junit Rate Limits
  slug: junit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: JUnit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: junit-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 18.7
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 23.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/junit/refs/heads/main/screenshots/junit-2026-06-20T183830.png
security:
- kind: domain-security
  name: Junit Domain Security
  slug: junit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: junit
tags:
- Java
- TDD
- Test Automation
- Testing
- Unit Testing
website: https://junit.org/junit5/
---
