---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Restate Agentic Access
  operation_count: 25
  slug: restate-agentic-access
  summary_line: 25 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Cluster health
  name: Restate Cluster Health API
  slug: restate-cluster-health-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Service Deployment management
  name: Restate Deployment API
  slug: restate-deployment-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Admin API health
  name: Restate Health API
  slug: restate-health-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Invocation management
  name: Restate Invocation API
  slug: restate-invocation-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Service management
  name: Restate Service API
  slug: restate-service-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Service handlers metadata
  name: Restate Service Handler API
  slug: restate-service-handler-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: Subscription management
  name: Restate Subscription API
  slug: restate-subscription-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: API Version
  name: Restate Version API
  slug: restate-version-api
- baseURL: http://localhost:9070
  baseurl_source: declared
  description: The Open API API from Restate — 1 operation(s) for open api.
  name: Restate Open API
  slug: restate-open-api-api
artifact_total: 35
collections:
- collection_type: open
  name: Admin API
  slug: open-restate-admin-api
- collection_type: open
  name: Admin cluster_health API
  slug: open-restate-cluster-health-api
- collection_type: open
  name: Admin cluster_health deployment API
  slug: open-restate-deployment-api
- collection_type: open
  name: Admin cluster_health health API
  slug: open-restate-health-api
- collection_type: open
  name: Admin cluster_health invocation API
  slug: open-restate-invocation-api
- collection_type: open
  name: Admin cluster_health openapi API
  slug: open-restate-openapi-api
- collection_type: open
  name: Admin cluster_health service API
  slug: open-restate-service-api
- collection_type: open
  name: Admin cluster_health service_handler API
  slug: open-restate-service-handler-api
- collection_type: open
  name: Admin cluster_health subscription API
  slug: open-restate-subscription-api
- collection_type: open
  name: Admin cluster_health version API
  slug: open-restate-version-api
common:
- group: commercial
  href: https://artifacts.apis.io/restate/plans/restate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/restate-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/restate/rate-limits/restate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/restate-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/restate/finops/restate-finops.yml
  title: ''
  type: FinOps
  url: finops/restate-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/restatedev/restate/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/restatedev/restate/releases
- group: agent
  href: https://artifacts.apis.io/restate/agentic-access/restate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/restate-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/restate/security/restate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/restate-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/restate/security/restate-domain-security.yml
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
  url: https://artifacts.apis.io/restate/crd/restatecloudenvironments.yaml
- name: restateclusters
  url: https://artifacts.apis.io/restate/crd/restateclusters.yaml
- name: restatedeployments
  url: https://artifacts.apis.io/restate/crd/restatedeployments.yaml
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
- has_sources: false
  method: generated
  name: Restate Finops
  primary_unit: request
  service_category: API
  slug: restate-finops
  template: true
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
overview: 'Restate publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cluster Health API, Deployment API, Health API, and 6 more. Tagged areas include Durable Execution, Workflows, Microservices, Orchestration, and Distributed Systems.


  The Restate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Restate''s developer surface includes documentation, code examples, engineering blog, and 19 more developer resources.'
plans:
- name: Restate Plans Pricing
  plan_count: 3
  slug: restate-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Restate Rate Limits
  slug: restate-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Restate — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restate-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Restate API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 6
  slug: restate-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 27.3
    contract_quality: 56.3
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 26.3
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/restate/restate-2026-06-20T193014.png
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
