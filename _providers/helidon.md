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
    agent_skills: false
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
  score: 23.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Helidon Agentic Access
  operation_count: 10
  slug: helidon-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Health API from Helidon — 4 operation(s) for health.
  name: Helidon Health API
  slug: helidon-health-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Info API from Helidon — 1 operation(s) for info.
  name: Helidon Info API
  slug: helidon-info-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Metrics API from Helidon — 4 operation(s) for metrics.
  name: Helidon Metrics API
  slug: helidon-metrics-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The Open API API from Helidon — 1 operation(s) for open api.
  name: Helidon Open API
  slug: helidon-open-api-api
artifact_total: 17
collections:
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
- group: commercial
  href: https://artifacts.apis.io/helidon/plans/helidon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/helidon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/helidon/rate-limits/helidon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/helidon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/helidon/finops/helidon-finops.yml
  title: ''
  type: FinOps
  url: finops/helidon-finops.yml
- group: agent
  href: https://artifacts.apis.io/helidon/agentic-access/helidon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/helidon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/helidon/security/helidon-domain-security.yml
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
- has_sources: false
  method: generated
  name: Helidon Finops
  primary_unit: request
  service_category: API
  slug: helidon-finops
  template: true
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
overview: 'Helidon publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Info API, Metrics API, and 1 more. Tagged areas include Cloud-Native, Framework, Java, MicroProfile, and Microservices.


  The Helidon catalog on APIs.io includes 1 Spectral governance ruleset.


  Helidon''s developer surface includes documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Helidon Plans Pricing
  plan_count: 3
  slug: helidon-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Helidon Rate Limits
  slug: helidon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Helidon — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: helidon-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.7
    catalog_earned_first_party: 0.0
    catalog_gap: 73.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 42.2
    developer_ergonomics: 23.8
    discoverability: 48.3
    operational_transparency: 10.5
  previous_composite: 22.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/helidon/helidon-2026-06-20T182619.png
security:
- kind: domain-security
  name: Helidon Domain Security
  slug: helidon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: helidon
tags:
- Cloud-Native
- Framework
- Java
- MicroProfile
- Microservices
- Oracle
- Reactive
website: https://helidon.io/
---
