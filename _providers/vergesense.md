---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Buildings API from VergeSense — 3 operation(s) for buildings.
  name: VergeSense Buildings API
  slug: vergesense-buildings-api
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Hardware API from VergeSense — 2 operation(s) for hardware.
  name: VergeSense Hardware API
  slug: vergesense-hardware-api
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Metrics API from VergeSense — 13 operation(s) for metrics.
  name: VergeSense Metrics API
  slug: vergesense-metrics-api
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Predict API from VergeSense — 3 operation(s) for predict.
  name: VergeSense Predict API
  slug: vergesense-predict-api
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Sensors API from VergeSense — 3 operation(s) for sensors.
  name: VergeSense Sensors API
  slug: vergesense-sensors-api
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Spaces API from VergeSense — 4 operation(s) for spaces.
  name: VergeSense Spaces API
  slug: vergesense-spaces-api
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: The Webhooks API from VergeSense — 6 operation(s) for webhooks.
  name: VergeSense Webhooks API
  slug: vergesense-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Vergesense Webhooks
  slug: vergesense-webhooks
common:
- group: other
  href: https://artifacts.apis.io/vergesense/capabilities/vergesense-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vergesense-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/vergesense/overlays/vergesense-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vergesense-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.vergesense.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vergesense.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://vergesense.readme.io/reference/reference-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://vergesense.readme.io/reference/buildings-1
- group: start
  title: ''
  type: GettingStarted
  url: https://vergesense.readme.io/reference/reference-getting-started
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/6835591/2s9Y5Wx3QL
- group: operate
  title: ''
  type: ChangeLog
  url: https://headwayapp.co/vergesense-changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.vergesense.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://support.vergesense.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://cloud.vergesense.com/
- group: start
  title: ''
  type: Login
  url: https://cloud.vergesense.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vergesense.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vergesense.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vergesense
- group: auth
  href: https://artifacts.apis.io/vergesense/authentication/vergesense-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vergesense-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vergesense/scopes/vergesense-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vergesense-scopes.yml
- group: operate
  href: https://artifacts.apis.io/vergesense/rate-limits/vergesense-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vergesense-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/vergesense/errors/vergesense-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vergesense-problem-types.yml
- group: build
  href: https://artifacts.apis.io/vergesense/examples/vergesense-api-examples.json
  title: ''
  type: Examples
  url: examples/vergesense-api-examples.json
- group: design
  href: https://artifacts.apis.io/vergesense/conventions/vergesense-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vergesense-conventions.yml
- group: design
  href: https://artifacts.apis.io/vergesense/lifecycle/vergesense-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vergesense-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/vergesense/lifecycle/vergesense-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/vergesense-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/vergesense/changelog/vergesense-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vergesense-changelog.yml
- group: design
  href: https://artifacts.apis.io/vergesense/conformance/vergesense-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vergesense-conformance.yml
- group: design
  href: https://artifacts.apis.io/vergesense/data-model/vergesense-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vergesense-data-model.yml
- group: design
  href: https://artifacts.apis.io/vergesense/asyncapi/vergesense-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vergesense-webhooks.yml
- group: build
  href: https://artifacts.apis.io/vergesense/packages/vergesense-packages.yml
  title: ''
  type: Packages
  url: packages/vergesense-packages.yml
- group: commercial
  href: https://artifacts.apis.io/vergesense/plans/vergesense-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vergesense-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/vergesense/llms/vergesense-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vergesense-llms.txt
- group: agent
  href: https://artifacts.apis.io/vergesense/well-known/vergesense-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vergesense-well-known.yml
- group: agent
  href: https://artifacts.apis.io/vergesense/mcp/vergesense-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vergesense-mcp.yml
- group: build
  href: https://artifacts.apis.io/vergesense/mcp/vergesense-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vergesense-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/vergesense/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/vergesense/security/vergesense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vergesense-domain-security.yml
created: '2026-09-02'
description: VergeSense is the occupancy intelligence platform for corporate real estate and workplace teams. It combines first-party AI-powered area, entryway and infinity sensors with a cloud analytics platform (Meridian, including a Large Spatial Model) to measure how buildings, floors, neighborhoods and individual spaces are actually used. The public VergeSense API is a key-authenticated REST surface at api.vergesense.com covering buildings, floors, spaces, space types, detections, threshold crossings, hourly and aggregate occupancy metrics, hardware inventory (sensors and gateways), a Predict API built on the Large Spatial Model, and a fully managed webhook subscription surface that pushes space_report, space_availability and motion_detected events to customer endpoints. Collection responses follow the JSON:API specification, timestamps are ISO 8601, and the API is date-versioned (YYYY-MM-DD) via the vs-version request header. VergeSense also operates an OAuth-protected remote MCP server
  at mcp.vergesense.com for agent access.
examples:
- key_count: 3
  name: Vergesense Api Examples
  slug: vergesense-api-examples
finops:
- has_sources: true
  method: derived
  name: Vergesense Finops
  primary_unit: ''
  service_category: ''
  slug: vergesense-finops
  template: true
image: https://www.vergesense.com/hubfs/assets/logo/vergesense-logo--color.png
layout: provider
mcp_servers:
- description: 'VergeSense operates a first-party remote MCP server on its own dedicated subdomain. It is not a derived candidate: an anonymous JSON-RPC POST of tools/list returns HTTP 401 with an RFC 9728 WWW-Authen'
  name: VergeSense MCP Server
  slug: vergesense-mcp-server
modified: '2026-09-02'
name: VergeSense
nav: Providers
network: true
overview: 'VergeSense publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buildings API, Hardware API, Metrics API, and 4 more. Tagged areas include Occupancy Intelligence, Workplace Analytics, Corporate Real Estate, PropTech, and IoT Sensors.


  The VergeSense catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  VergeSense''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, signup flow, and 29 more developer resources.'
plans:
- name: Vergesense Plans Pricing
  plan_count: 0
  slug: vergesense-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Vergesense Rate Limits
  slug: vergesense-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: VergeSense API Rules
  rule_count: 44
  severity_counts:
    error: 34
    hint: 0
    info: 2
    warn: 8
  slug: vergesense-rules
scopes:
- name: Vergesense Scopes
  scope_count: 0
  slug: vergesense-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 63.2
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 55.3
  previous_composite: 53.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vergesense/vergesense-2026-10-11T132850.png
security:
- kind: authentication
  name: Vergesense Authentication
  slug: vergesense-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Vergesense Domain Security
  slug: vergesense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: vergesense-manage-event-webhook
  slug: vergesense-manage-event-webhook
- name: vergesense-portfolio-utilization-report
  slug: vergesense-portfolio-utilization-report
- name: vergesense-predict-space-demand
  slug: vergesense-predict-space-demand
slug: vergesense
tags:
- Occupancy Intelligence
- Workplace Analytics
- Corporate Real Estate
- PropTech
- IoT Sensors
- Building Data
- Space Utilization
- Facilities Management
- Smart Buildings
- Webhook
- MCP
- JSON:API
website: https://www.vergesense.com/
---
