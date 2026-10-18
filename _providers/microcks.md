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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Microcks Agentic Access
  operation_count: 46
  slug: microcks-agentic-access
  summary_line: 46 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to configuration
  name: Microcks Config API
  slug: microcks-config-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to Jobs for discovering mocks and tests
  name: Microcks Job API
  slug: microcks-job-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to metrics
  name: Microcks Metrics API
  slug: microcks-metrics-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to API and Services mocks
  name: Microcks Mock API
  slug: microcks-mock-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: The Resources API from Microcks — 2 operation(s) for resources.
  name: Microcks Resources API
  slug: microcks-resources-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to API and Services tests
  name: Microcks Test API
  slug: microcks-test-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microcks API v1.14 config API
  slug: open-microcks-config-api
- collection_type: open
  name: Microcks API v1.14 config job API
  slug: open-microcks-job-api
- collection_type: open
  name: Microcks API v1.14 config metrics API
  slug: open-microcks-metrics-api
- collection_type: open
  name: Microcks API v1.14 config mock API
  slug: open-microcks-mock-api
- collection_type: open
  name: Microcks API v1.14 config Resources API
  slug: open-microcks-resources-api
- collection_type: open
  name: Microcks API v1.14 config test API
  slug: open-microcks-test-api
- collection_type: open
  name: Microcks API v1.14
  slug: open-microcks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/plans/microcks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microcks-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/rate-limits/microcks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microcks-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/finops/microcks-finops.yml
  title: ''
  type: FinOps
  url: finops/microcks-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/capabilities/microcks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microcks-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.microcks.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/agentic-access/microcks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microcks-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/security/microcks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microcks-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/authentication/microcks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microcks-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/scopes/microcks-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microcks-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microcks
- group: start
  title: ''
  type: Portal
  url: https://microcks.io/
- group: docs
  title: ''
  type: Documentation
  url: https://microcks.io/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microcks
- group: operate
  title: ''
  type: Community
  url: https://microcks.io/community/
- group: company
  title: ''
  type: Blog
  url: https://microcks.io/blog/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microcks/microcks-mcp-server
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/microcks/microcks-spectral-ruleset/blob/b42c0030c31e6fb64e66b6f17ebb8be1b75ceb3d/microcks-rules.yaml
created: '2025-01-08'
description: Microcks is an open source, cloud-native tool for API mocking and testing. It provides a platform for importing API contracts (OpenAPI, AsyncAPI, Postman Collections), generating mock responses, and running test suites. It shortens the feedback loop for API development teams.
finops:
- has_sources: false
  method: generated
  name: Microcks Finops
  primary_unit: ''
  service_category: API
  slug: microcks-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microcks.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microcks
nav: Providers
network: true
overview: 'Microcks publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Config API, Job API, Metrics API, and 3 more. Tagged areas include API Testing, Cloud-Native, DevOps, Mocking, and Open Source.


  The Microcks catalog on APIs.io includes 1 Spectral governance ruleset.


  Microcks'' developer surface includes authentication, developer portal, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Microcks Plans Pricing
  plan_count: 3
  slug: microcks-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Microcks Rate Limits
  slug: microcks-rate-limits
rules:
- authorship: provider
  effective_rule_count: 79
  extends:
  - spectral:oas
  - spectral:asyncapi
  name: Microcks — microcks spectral ruleset rules
  rule_count: 11
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 10
  slug: microcks-microcks-spectral-ruleset-spectral-rules
scopes:
- name: Microcks Scopes
  scope_count: 3
  slug: microcks-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.0
    catalog_earned_first_party: 18.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.0
  facets:
    access_clarity: 7.9
    contract_governance: 54.5
    contract_quality: 46.3
    developer_ergonomics: 35.7
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/screenshots/microcks-2026-06-20T185332.png
security:
- kind: authentication
  name: Microcks Authentication
  slug: microcks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microcks Domain Security
  slug: microcks-domain-security
  summary_line: TLSv1.3
slug: microcks
tags:
- API Testing
- Cloud-Native
- DevOps
- Mocking
- Open Source
website: https://www.microcks.io/
---
