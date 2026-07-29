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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quarkus Agentic Access
  operation_count: 9
  slug: quarkus-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: The Dev UI API from Quarkus — 1 operation(s) for dev ui.
  name: Quarkus Dev UI API
  slug: quarkus-dev-ui-api
- description: The Health API from Quarkus — 4 operation(s) for health.
  name: Quarkus Health API
  slug: quarkus-health-api
- description: The Info API from Quarkus — 1 operation(s) for info.
  name: Quarkus Info API
  slug: quarkus-info-api
- description: The Metrics API from Quarkus — 1 operation(s) for metrics.
  name: Quarkus Metrics API
  slug: quarkus-metrics-api
- description: The OpenAPI API from Quarkus — 2 operation(s) for openapi.
  name: Quarkus OpenAPI API
  slug: quarkus-openapi-api
artifact_total: 18
collections:
- collection_type: open
  name: Quarkus Dev UI & Health/Metrics API
  slug: open-quarkus-dev-ui
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quarkus-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quarkus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quarkus-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quarkusio
- group: company
  title: ''
  type: Website
  url: https://quarkus.io/
- group: docs
  title: ''
  type: Documentation
  url: https://quarkus.io/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://quarkus.io/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quarkusio
- group: company
  title: ''
  type: Blog
  url: https://quarkus.io/blog/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/quarkusio/quarkus-agent-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/quarkusio/quarkus-skills
created: '2026-03-26'
description: Quarkus is a Kubernetes-native Java framework tailored for GraalVM and OpenJDK HotSpot, designed to build cloud-native microservices and serverless applications with fast startup times and low memory footprint.
finops:
- name: Quarkus Finops
  service_category: API
  slug: quarkus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quarkus.png
json_schemas:
- name: Quarkus Application Configuration
  property_count: 1
  slug: quarkus-application-properties
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Quarkus
nav: Providers
network: true
overview: 'Quarkus publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Dev UI API, Health API, Info API, and 2 more. Tagged areas include Cloud Native, Frameworks, GraalVM, Java, and Kubernetes.


  The Quarkus catalog on APIs.io includes 1 Spectral governance ruleset.


  Quarkus'' developer surface includes documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Quarkus Plans Pricing
  plan_count: 3
  slug: quarkus-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Quarkus Rate Limits
  slug: quarkus-rate-limits
rules:
- name: Quarkus API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quarkus-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.5
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.2
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quarkus/refs/heads/main/screenshots/quarkus-2026-06-20T192414.png
security:
- kind: domain-security
  name: Quarkus Domain Security
  slug: quarkus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Quarkus Vulnerability Disclosure
  slug: quarkus-vulnerability-disclosure
  summary_line: disclosure policy published
skill_count: 3
skills:
- name: hello-world
  slug: hello-world
- name: migrate-spring-to-quarkus
  slug: migrate-spring-to-quarkus
- name: quarkus-update
  slug: quarkus-update
slug: quarkus
tags:
- Cloud Native
- Frameworks
- GraalVM
- Java
- Kubernetes
- Microservices
- Serverless
website: https://quarkus.io/
---
