---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Insomnia Agentic Access
  operation_count: 10
  slug: insomnia-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Insomnia is an open-source, cross-platform API development platform by Kong for designing, debugging, and testing HTTP, REST, GraphQL, gRPC, SOAP, WebSockets, SSE, and Socket.IO APIs. It includes an I
  name: Insomnia
  slug: insomnia
- baseURL: https://mock.insomnia.rest
  baseurl_source: spec
  description: View request logs for mock servers.
  name: Insomnia Mock Logs API
  slug: insomnia-mock-logs-api
- baseURL: https://mock.insomnia.rest
  baseurl_source: spec
  description: Manage individual routes within a mock server.
  name: Insomnia Mock Routes API
  slug: insomnia-mock-routes-api
- baseURL: https://mock.insomnia.rest
  baseurl_source: spec
  description: Manage mock server instances.
  name: Insomnia Mock Servers API
  slug: insomnia-mock-servers-api
artifact_total: 22
collections:
- collection_type: open
  name: Insomnia Mock Server Mock Logs API
  slug: open-insomnia-mock-logs-api
- collection_type: open
  name: Insomnia Mock Server Mock Logs Mock Routes API
  slug: open-insomnia-mock-routes-api
- collection_type: open
  name: Insomnia Mock Server API
  slug: open-insomnia-mock-server
- collection_type: open
  name: Insomnia Mock Server Mock Logs Mock Servers API
  slug: open-insomnia-mock-servers-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/insomnia/overview
- group: commercial
  href: https://artifacts.apis.io/insomnia/finops/insomnia-finops.yml
  title: ''
  type: FinOps
  url: finops/insomnia-finops.yml
- group: operate
  href: https://artifacts.apis.io/insomnia/rate-limits/insomnia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/insomnia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/insomnia/plans/insomnia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/insomnia-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/insomnia/rules/insomnia-rules.yml
  title: ''
  type: Spectral
  url: rules/insomnia-rules.yml
- group: design
  href: https://artifacts.apis.io/insomnia/rules/insomnia-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/insomnia-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/insomnia/vocabulary/insomnia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/insomnia-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/insomnia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/insomnia/data-model/insomnia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/insomnia-data-model.yml
- group: build
  href: https://artifacts.apis.io/insomnia/cli/insomnia-cli.yml
  title: ''
  type: CLI
  url: cli/insomnia-cli.yml
- group: operate
  href: https://artifacts.apis.io/insomnia/changelog/insomnia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/insomnia-changelog.yml
- group: design
  href: https://artifacts.apis.io/insomnia/errors/insomnia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/insomnia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/insomnia/conformance/insomnia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/insomnia-conformance.yml
- group: other
  href: https://artifacts.apis.io/insomnia/hosts/insomnia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insomnia-hosts.yml
- group: other
  href: https://artifacts.apis.io/insomnia/vendors/insomnia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insomnia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insomnia.rest/terms
- group: operate
  title: ''
  type: Support
  url: https://insomnia.rest/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insomnia.rest/privacy
- group: start
  title: ''
  type: Login
  url: https://app.insomnia.rest/app/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.konghq.com/insomnia/enterprise-onboarding
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.konghq.com/insomnia/ai-in-insomnia/
- group: other
  href: https://artifacts.apis.io/insomnia/vendor-facets/insomnia-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/insomnia-vendor-facets.yml
- group: agent
  href: https://artifacts.apis.io/insomnia/agentic-access/insomnia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/insomnia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/insomnia/security/insomnia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insomnia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/insomnia/authentication/insomnia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/insomnia-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.insomnia.rest/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Kong/insomnia
- group: build
  title: ''
  type: Plugins
  url: https://insomnia.rest/plugins
- group: operate
  title: ''
  type: ChangeLog
  url: https://insomnia.rest/changelog
- group: company
  title: ''
  type: Blog
  url: https://konghq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://insomnia.rest/pricing
- group: build
  title: ''
  type: CLI
  url: https://docs.insomnia.rest/inso-cli/introduction/
- group: company
  title: ''
  type: Website
  url: https://insomnia.rest/
created: '2025-01-08'
description: Insomnia is an open-source, cross-platform API development platform by Kong for designing, debugging, and testing HTTP, REST, GraphQL, gRPC, SOAP, WebSockets, SSE, and Socket.IO APIs. It includes an Inso CLI for CI/CD integration, cloud-hosted and self-hosted mock servers, OpenAPI spec design tools, and collaborative features with cloud sync, local vault, and Git storage options.
finops:
- has_sources: true
  method: derived
  name: Insomnia Finops
  primary_unit: user / month
  service_category: ''
  slug: insomnia-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insomnia.png
json_schemas:
- name: Insomnia Environment
  property_count: 11
  slug: environment
- name: Insomnia Request
  property_count: 17
  slug: request
- name: Insomnia Workspace
  property_count: 9
  slug: workspace
jsonld:
- class_count: 2
  name: Insomnia Context
  property_count: 5
  slug: insomnia-context
layout: provider
modified: '2026-05-19'
name: Insomnia
nav: Providers
network: true
overview: 'Insomnia publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Mock Logs API, Mock Routes API, Mock Servers API, and 1 more. Tagged areas include API Design, CLI, Clients, Developer Tools, and Mocking.


  The Insomnia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Insomnia''s developer surface includes CLI, changelog, support, getting-started guide, authentication, documentation, engineering blog, and 26 more developer resources.'
plans:
- name: Insomnia Plans Pricing
  plan_count: 3
  slug: insomnia-plans-pricing
- name: Insomnia Price Estimates
  plan_count: 0
  slug: insomnia-price-estimates
random_paper: 22
rate_limits:
- limit_count: 5
  name: Insomnia Rate Limits
  slug: insomnia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Insomnia — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: insomnia-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Insomnia API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: insomnia-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 67.1
    contract_governance: 35.6
    contract_quality: 62.5
    developer_ergonomics: 47.0
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/insomnia/insomnia-2026-06-20T183403.png
security:
- kind: authentication
  name: Insomnia Authentication
  slug: insomnia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Insomnia Domain Security
  slug: insomnia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: insomnia-manage-mock-routes
  slug: insomnia-manage-mock-routes
slug: insomnia
tags:
- API Design
- CLI
- Clients
- Developer Tools
- Mocking
- Platform
- Testing
- OpenAPI
website: https://insomnia.rest/
---
