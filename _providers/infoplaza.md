---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Infoplaza Agentic Access
  operation_count: 1
  slug: infoplaza-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Geo API from Infoplaza — 2 operation(s) for geo.
  name: Infoplaza Geo API
  slug: infoplaza-geo-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Marine API from Infoplaza — 7 operation(s) for marine.
  name: Infoplaza Marine API
  slug: infoplaza-marine-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Observations API from Infoplaza — 5 operation(s) for observations.
  name: Infoplaza Observations API
  slug: infoplaza-observations-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Port API from Infoplaza — 2 operation(s) for port.
  name: Infoplaza Port API
  slug: infoplaza-port-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Storms API from Infoplaza — 1 operation(s) for storms.
  name: Infoplaza Storms API
  slug: infoplaza-storms-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Traffic API from Infoplaza — 2 operation(s) for traffic.
  name: Infoplaza Traffic API
  slug: infoplaza-traffic-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Transit API from Infoplaza — 4 operation(s) for transit.
  name: Infoplaza Transit API
  slug: infoplaza-transit-api
- baseURL: https://api.infoplaza.com
  baseurl_source: declared
  description: The Weather API from Infoplaza — 14 operation(s) for weather.
  name: Infoplaza Weather API
  slug: infoplaza-weather-api
artifact_total: 21
common:
- group: design
  href: https://artifacts.apis.io/infoplaza/vocabulary/infoplaza-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/infoplaza-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/infoplaza/conventions/infoplaza-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infoplaza-conventions.yml
- group: design
  href: https://artifacts.apis.io/infoplaza/lifecycle/infoplaza-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infoplaza-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/infoplaza/mcp/infoplaza-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/infoplaza-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/infoplaza/mcp/infoplaza-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/infoplaza-mcp.yml
- group: agent
  href: https://artifacts.apis.io/infoplaza/agentic-access/infoplaza-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infoplaza-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/infoplaza/rate-limits/infoplaza-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/infoplaza-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/infoplaza/plans/infoplaza-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infoplaza-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/infoplaza/rules/infoplaza-rules.yml
  title: ''
  type: Spectral
  url: rules/infoplaza-rules.yml
- group: agent
  href: https://artifacts.apis.io/infoplaza/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/infoplaza/authentication/infoplaza-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infoplaza-authentication.yml
- group: design
  href: https://artifacts.apis.io/infoplaza/errors/infoplaza-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infoplaza-problem-types.yml
- group: design
  href: https://artifacts.apis.io/infoplaza/conformance/infoplaza-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infoplaza-conformance.yml
- group: other
  href: https://artifacts.apis.io/infoplaza/grpc/PlanService.proto
  title: ''
  type: Protobuf
  url: grpc/PlanService.proto
- group: other
  href: https://artifacts.apis.io/infoplaza/grpc/PlanResult.proto
  title: ''
  type: Protobuf
  url: grpc/PlanResult.proto
- group: other
  href: https://artifacts.apis.io/infoplaza/grpc/PlanRequest.proto
  title: ''
  type: Protobuf
  url: grpc/PlanRequest.proto
- group: other
  href: https://artifacts.apis.io/infoplaza/overlays/infoplaza-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infoplaza-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/infoplaza/hosts/infoplaza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infoplaza-hosts.yml
- group: other
  href: https://artifacts.apis.io/infoplaza/vendors/infoplaza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infoplaza-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.infoplaza.com/en/branch/media
- group: company
  title: ''
  type: Blog
  url: https://www.infoplaza.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infoplaza
- group: auth
  href: https://artifacts.apis.io/infoplaza/security/infoplaza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infoplaza-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.infoplaza.com/contact
- group: company
  title: ''
  type: Website
  url: https://www.infoplaza.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.infoplaza.com
- group: docs
  title: ''
  type: Documentation
  url: https://platform.infoplaza.com/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.infoplaza.com/docs/get-started/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://platform.infoplaza.com/reference/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.infoplaza.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://platform.infoplaza.com/contact
- group: company
  title: ''
  type: About
  url: https://www.infoplaza.com/en/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.infoplaza.com/en/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infoplaza
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infoplaza.com/en/disclaimer-and-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infoplaza.com/hubfs/General%20Terms%20and%20Conditions%20IPG-EN%20V20251104.pdf
created: '2026-10-28'
description: Infoplaza is a Dutch weather and mobility information company, founded in 2009, that provides meteorological services around the clock to businesses in offshore, shipping, energy, construction, rail, road-ice, outdoor-event and media sectors, and runs consumer brands including Weeronline, Verkeerplaza and I'm Planner. Its Infoplaza Dataplatform (in beta) exposes geo, weather, marine and mobility APIs with unified API-key authentication, documented weather and marine models, a Free tier and paid plans, plus OpenAPI, Postman and MCP server integrations.
image: https://www.infoplaza.com/hs-fs/hubfs/AdobeStock_393855636.jpeg?width=1280&name=AdobeStock_393855636.jpeg
layout: provider
mcp_servers:
- description: Hosted remote MCP server documented by Infoplaza. The docs state it exposes every Platform API as a tool and that calls use the same api_key, rate limits and credits as direct REST calls.
  name: Infoplaza Dataplatform MCP Server
  slug: infoplaza-dataplatform-mcp-server
modified: '2026-10-28'
name: Infoplaza
nav: Providers
network: true
overview: 'Infoplaza publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Geo API, Marine API, Observations API, and 5 more. Tagged areas include Company, Weather, Mobility, Forecasting, and EventPlanning.


  The Infoplaza catalog on APIs.io includes 1 Spectral governance ruleset.


  Infoplaza''s developer surface includes authentication, engineering blog, support, documentation, getting-started guide, API reference, pricing, and 29 more developer resources.'
plans:
- name: Infoplaza Plans Pricing
  plan_count: 4
  slug: infoplaza-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Infoplaza Rate Limits
  slug: infoplaza-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Infoplaza API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: infoplaza-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 66.8
    catalog_earned_first_party: 24.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 45.9
    developer_ergonomics: 63.7
    discoverability: 66.7
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Infoplaza Authentication
  slug: infoplaza-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Infoplaza Domain Security
  slug: infoplaza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: place-weather-forecast
  slug: infoplaza-place-weather-forecast
- name: port-information
  slug: infoplaza-port-information
- name: shipping-point-forecast
  slug: infoplaza-shipping-point-forecast
- name: shipping-route-forecast
  slug: infoplaza-shipping-route-forecast
- name: station-observations
  slug: infoplaza-station-observations
- name: transit-departures-near-me
  slug: infoplaza-transit-departures-near-me
slug: infoplaza
tags:
- Company
- Weather
- Mobility
- Forecasting
- EventPlanning
- DataAnalytics
- Weather Data
- Marine
- Meteorology
- Geospatial
website: https://www.infoplaza.com/en
---
