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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dropwizard Agentic Access
  operation_count: 7
  slug: dropwizard-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: JVM diagnostic endpoints.
  name: Dropwizard Diagnostics API
  slug: dropwizard-diagnostics-api
- description: Health check and liveness endpoints.
  name: Dropwizard Health API
  slug: dropwizard-health-api
- description: Application metrics endpoints.
  name: Dropwizard Metrics API
  slug: dropwizard-metrics-api
- description: Administrative task execution endpoints.
  name: Dropwizard Tasks API
  slug: dropwizard-tasks-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dropwizard Admin API
  slug: open-dropwizard-admin
- collection_type: open
  name: Dropwizard Admin Diagnostics API
  slug: open-dropwizard-diagnostics-api
- collection_type: open
  name: Dropwizard Admin Diagnostics Health API
  slug: open-dropwizard-health-api
- collection_type: open
  name: Dropwizard Admin Diagnostics Metrics API
  slug: open-dropwizard-metrics-api
- collection_type: open
  name: Dropwizard Admin Diagnostics Tasks API
  slug: open-dropwizard-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dropwizard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dropwizard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dropwizard.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dropwizard.io/en/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dropwizard.io/en/stable/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dropwizard
created: '2026-03-26'
description: Dropwizard is a Java framework for developing ops-friendly, high-performance RESTful web services, pulling together stable, mature libraries from the Java ecosystem into a simple, lightweight package.
finops:
- name: Dropwizard Finops
  service_category: API
  slug: dropwizard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dropwizard.png
json_schemas:
- name: Dropwizard Configuration
  property_count: 4
  slug: dropwizard-config
layout: provider
modified: '2026-05-19'
name: Dropwizard
nav: Providers
network: true
overview: 'Dropwizard publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Diagnostics API, Health API, Metrics API, and 1 more. Tagged areas include API Development, Frameworks, Java, Microservices, and REST.


  The Dropwizard catalog on APIs.io includes 1 Spectral governance ruleset.


  Dropwizard''s developer surface includes documentation, getting-started guide, and 4 more developer resources.'
plans:
- name: Dropwizard Plans Pricing
  plan_count: 3
  slug: dropwizard-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Dropwizard Rate Limits
  slug: dropwizard-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Dropwizard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dropwizard-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.6
  delta: -6.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 48.6
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/dropwizard/refs/heads/main/screenshots/dropwizard-2026-06-20T180247.png
security:
- kind: domain-security
  name: Dropwizard Domain Security
  slug: dropwizard-domain-security
  summary_line: TLSv1.3
slug: dropwizard
tags:
- API Development
- Frameworks
- Java
- Microservices
- REST
- Web Services
website: https://www.dropwizard.io/
---
