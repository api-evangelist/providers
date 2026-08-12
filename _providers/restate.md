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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Restate Agentic Access
  operation_count: 25
  slug: restate-agentic-access
  summary_line: 25 operations · 12 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Cluster health
  name: Restate cluster_health API
  slug: restate-cluster-health-api
- description: Service Deployment management
  name: Restate deployment API
  slug: restate-deployment-api
- description: Admin API health
  name: Restate health API
  slug: restate-health-api
- description: Invocation management
  name: Restate invocation API
  slug: restate-invocation-api
- description: The openapi API from Restate — 1 operation(s) for openapi.
  name: Restate openapi API
  slug: restate-openapi-api
- description: Service management
  name: Restate service API
  slug: restate-service-api
- description: Service handlers metadata
  name: Restate service_handler API
  slug: restate-service-handler-api
- description: Subscription management
  name: Restate subscription API
  slug: restate-subscription-api
- description: API Version
  name: Restate version API
  slug: restate-version-api
artifact_total: 26
collections:
- collection_type: open
  name: Admin API
  slug: open-restate-admin-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/restate-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/restate-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restate-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/restatedev
- group: company
  title: ''
  type: Website
  url: https://restate.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.restate.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restatedev
- group: build
  title: ''
  type: TypeScript SDK
  url: https://github.com/restatedev/sdk-typescript
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/restatedev/sdk-python
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/restatedev/sdk-java
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/restatedev/sdk-go
- group: build
  title: ''
  type: Rust SDK
  url: https://github.com/restatedev/sdk-rust
- group: build
  title: ''
  type: Examples
  url: https://github.com/restatedev/examples
- group: other
  title: ''
  type: Web UI
  url: https://github.com/restatedev/restate-web-ui
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/skW3AZ6uGd
- group: company
  title: ''
  type: Blog
  url: https://restate.dev/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.restate.dev/llms.txt
crds:
- name: restatecloudenvironments
  url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/crd/restatecloudenvironments.yaml
- name: restateclusters
  url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/crd/restateclusters.yaml
- name: restatedeployments
  url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/crd/restatedeployments.yaml
created: '2026-03-26'
description: Restate is a low-latency durable execution engine for building resilient applications that tolerate all infrastructure faults. It provides durable execution for workflows, event-driven handlers, and stateful orchestration of microservices with exactly-once semantics, automatic retries, and built-in state management.
examples:
- key_count: 2
  name: Restate Create Deployment Example
  slug: restate-create-deployment-example
- key_count: 2
  name: Restate List Deployments Example
  slug: restate-list-deployments-example
- key_count: 2
  name: Restate List Invocations Example
  slug: restate-list-invocations-example
finops:
- name: Restate Finops
  service_category: API
  slug: restate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restate.png
json_schemas:
- name: Deployment
  property_count: 7
  slug: restate-deployment
- name: Invocation
  property_count: 13
  slug: restate-invocation
json_structures:
- name: Restate Deployment Structure
  property_count: 0
  slug: restate-deployment-structure
- name: Restate Invocation Structure
  property_count: 0
  slug: restate-invocation-structure
jsonld:
- class_count: 32
  name: Restate Context
  property_count: 0
  slug: restate-context
layout: provider
modified: '2026-05-19'
name: Restate
nav: Providers
network: true
overview: 'Restate publishes 9 APIs on the [APIs.io](https://apis.io/) network, including cluster_health API, deployment API, health API, and 6 more. Tagged areas include Durable Execution, Workflows, Microservices, Orchestration, and Distributed Systems.


  The Restate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Restate''s developer surface includes documentation, code examples, engineering blog, and 14 more developer resources.'
plans:
- name: Restate Plans Pricing
  plan_count: 3
  slug: restate-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Restate Rate Limits
  slug: restate-rate-limits
rules:
- name: Restate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restate-jsonschema-spectral-rules
- name: Restate API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 6
  slug: restate-rules
score:
  band: thin
  composite: 41.5
  delta: -6.8
  facets:
    commercial_clarity: 23.7
    contract_quality: 59.0
    developer_ergonomics: 30.4
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/screenshots/restate-2026-06-20T193014.png
security:
- kind: domain-security
  name: Restate Domain Security
  slug: restate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Restate Trust Center
  slug: restate-trust-center
  summary_line: SOC 2
slug: restate
tags:
- Durable Execution
- Workflows
- Microservices
- Orchestration
- Distributed Systems
website: https://restate.dev/
---
