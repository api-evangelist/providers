---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Liberty Agentic Access
  operation_count: 11
  slug: open-liberty-agentic-access
  summary_line: 11 operations
api_count: 3
apis:
- description: Server configuration management via Admin REST Connector.
  name: Open Liberty Configuration API
  slug: open-liberty-configuration-api
- description: MicroProfile Health check endpoints.
  name: Open Liberty Health API
  slug: open-liberty-health-api
- description: MicroProfile Metrics endpoints.
  name: Open Liberty Metrics API
  slug: open-liberty-metrics-api
artifact_total: 12
collections:
- collection_type: open
  name: Open Liberty Admin REST API
  slug: open-open-liberty-admin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-liberty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-liberty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-liberty-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openliberty.io/
- group: docs
  title: ''
  type: Documentation
  url: https://openliberty.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://openliberty.io/start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenLiberty
- group: company
  title: ''
  type: Blog
  url: https://openliberty.io/blog/
created: '2026-03-26'
description: Open Liberty is a lightweight, open source Java application server from IBM for building cloud-native microservices and applications with full support for Jakarta EE and MicroProfile.
finops:
- name: Open Liberty Finops
  service_category: API
  slug: open-liberty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-liberty.png
json_schemas:
- name: Open Liberty Server Configuration
  property_count: 1
  slug: server-config
layout: provider
modified: '2026-05-19'
name: Open Liberty
nav: Providers
network: true
overview: 'Open Liberty publishes 3 APIs on the [APIs.io](https://apis.io/) network: Configuration API, Health API, and Metrics API. Tagged areas include Application Server, Cloud Native, IBM, Jakarta EE, and Java.


  The Open Liberty catalog on APIs.io includes 1 Spectral governance ruleset.


  Open Liberty''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 4 more developer resources.'
plans:
- name: Open Liberty Plans Pricing
  plan_count: 3
  slug: open-liberty-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 5
  name: Open Liberty Rate Limits
  slug: open-liberty-rate-limits
rules:
- name: Open Liberty API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: open-liberty-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 32.6
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-liberty/refs/heads/main/screenshots/open-liberty-2026-06-20T190837.png
security:
- kind: authentication
  name: Open Liberty Authentication
  slug: open-liberty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Open Liberty Domain Security
  slug: open-liberty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-liberty
tags:
- Application Server
- Cloud Native
- IBM
- Jakarta EE
- Java
- MicroProfile
- Microservices
website: https://openliberty.io/
---
