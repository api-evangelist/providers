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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Helidon Agentic Access
  operation_count: 10
  slug: helidon-agentic-access
  summary_line: 10 operations
api_count: 4
apis:
- description: The Health API from Helidon — 4 operation(s) for health.
  name: Helidon Health API
  slug: helidon-health-api
- description: The Info API from Helidon — 1 operation(s) for info.
  name: Helidon Info API
  slug: helidon-info-api
- description: The Metrics API from Helidon — 4 operation(s) for metrics.
  name: Helidon Metrics API
  slug: helidon-metrics-api
- description: The OpenAPI API from Helidon — 1 operation(s) for openapi.
  name: Helidon OpenAPI API
  slug: helidon-openapi-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Helidon Observe ( & Metrics) Health API
  slug: open-helidon-health-api
- collection_type: open
  name: Helidon Observe ( & Metrics) Health Info API
  slug: open-helidon-info-api
- collection_type: open
  name: Helidon Observe ( & ) Health Metrics API
  slug: open-helidon-metrics-api
- collection_type: open
  name: Helidon Observe (Health & Metrics) API
  slug: open-helidon-observe
- collection_type: open
  name: Helidon Observe ( & Metrics) Health OpenAPI API
  slug: open-helidon-openapi-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helidon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helidon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://helidon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://helidon.io/docs/latest
- group: start
  title: ''
  type: GettingStarted
  url: https://helidon.io/docs/latest/#/about/prerequisites
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helidon-io
- group: company
  title: ''
  type: Blog
  url: https://medium.com/helidon
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/helidon
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/helidon-io/helidon-mcp
created: '2026-03-26'
description: Helidon is a collection of Java libraries from Oracle for writing microservices that run on a fast web core powered by Netty, supporting MicroProfile and reactive programming models.
finops:
- name: Helidon Finops
  service_category: API
  slug: helidon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helidon.png
json_schemas:
- name: Helidon Application Configuration
  property_count: 5
  slug: helidon-application-config
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Helidon
nav: Providers
network: true
overview: 'Helidon publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Health API, Info API, Metrics API, and 1 more. Tagged areas include Cloud Native, Frameworks, Java, MicroProfile, and Microservices.


  The Helidon catalog on APIs.io includes 1 Spectral governance ruleset.


  Helidon''s developer surface includes documentation, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Helidon Plans Pricing
  plan_count: 3
  slug: helidon-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Helidon Rate Limits
  slug: helidon-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Helidon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: helidon-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.9
  delta: -11.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 48.3
    developer_ergonomics: 23.8
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 36.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/helidon/refs/heads/main/screenshots/helidon-2026-06-20T182619.png
security:
- kind: domain-security
  name: Helidon Domain Security
  slug: helidon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: helidon
tags:
- Cloud Native
- Frameworks
- Java
- MicroProfile
- Microservices
- Oracle
- Reactive
website: https://helidon.io/
---
