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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quarkus Agentic Access
  operation_count: 9
  slug: quarkus-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Dev UI API from Quarkus — 1 operation(s) for dev ui.
  name: Quarkus Dev UI API
  slug: quarkus-dev-ui-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Health API from Quarkus — 4 operation(s) for health.
  name: Quarkus Health API
  slug: quarkus-health-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Info API from Quarkus — 1 operation(s) for info.
  name: Quarkus Info API
  slug: quarkus-info-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Metrics API from Quarkus — 1 operation(s) for metrics.
  name: Quarkus Metrics API
  slug: quarkus-metrics-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Open API API from Quarkus — 2 operation(s) for open api.
  name: Quarkus Open API
  slug: quarkus-open-api-api
artifact_total: 23
collections:
- collection_type: open
  name: Quarkus & Health/Metrics Dev UI API
  slug: open-quarkus-dev-ui-api
- collection_type: open
  name: Quarkus Dev UI & Health/Metrics API
  slug: open-quarkus-dev-ui
- collection_type: open
  name: Quarkus & /Metrics Dev UI Health API
  slug: open-quarkus-health-api
- collection_type: open
  name: Quarkus & Health/Metrics Dev UI Info API
  slug: open-quarkus-info-api
- collection_type: open
  name: Quarkus & Health/ Dev UI Metrics API
  slug: open-quarkus-metrics-api
- collection_type: open
  name: Quarkus & Health/Metrics Dev UI OpenAPI API
  slug: open-quarkus-openapi-api
common:
- group: commercial
  href: https://artifacts.apis.io/quarkus/plans/quarkus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quarkus-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/quarkus/rate-limits/quarkus-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quarkus-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/quarkus/finops/quarkus-finops.yml
  title: ''
  type: FinOps
  url: finops/quarkus-finops.yml
- group: agent
  href: https://artifacts.apis.io/quarkus/agentic-access/quarkus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quarkus-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/quarkus/security/quarkus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/quarkus-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/quarkus/security/quarkus-domain-security.yml
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
- has_sources: false
  method: generated
  name: Quarkus Finops
  primary_unit: request
  service_category: API
  slug: quarkus-finops
  template: true
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
overview: 'Quarkus publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dev UI API, Health API, Info API, and 2 more. Tagged areas include Cloud-Native, Framework, GraalVM, Java, and Kubernetes.


  The Quarkus catalog on APIs.io includes 1 Spectral governance ruleset.


  Quarkus'' developer surface includes documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Quarkus Plans Pricing
  plan_count: 3
  slug: quarkus-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Quarkus Rate Limits
  slug: quarkus-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Quarkus — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quarkus-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.7
    catalog_earned_first_party: 0.0
    catalog_gap: 68.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 42.2
    developer_ergonomics: 30.2
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/quarkus/quarkus-2026-06-20T192414.png
security:
- kind: domain-security
  name: Quarkus Domain Security
  slug: quarkus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Quarkus Vulnerability Disclosure
  slug: quarkus-vulnerability-disclosure
  summary_line: no policy recorded
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
- Cloud-Native
- Framework
- GraalVM
- Java
- Kubernetes
- Microservices
- Serverless
website: https://quarkus.io/
---
