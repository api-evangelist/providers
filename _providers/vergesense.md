---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.vergesense.com
  baseurl_source: declared
  description: REST and webhook API for the VergeSense Cloud occupancy intelligence platform. Read buildings, floors, spaces, space types, neighborhoods, space groups, detections and threshold crossings; pull hourly
  name: VergeSense API
  slug: vergesense-api
artifact_total: 9
asyncapis:
- description: ''
  name: Vergesense Webhooks
  slug: vergesense-webhooks
common:
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
  title: ''
  type: Authentication
  url: authentication/vergesense-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vergesense-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vergesense-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vergesense-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/vergesense-api-examples.json
- group: design
  title: ''
  type: Conventions
  url: conventions/vergesense-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vergesense-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/vergesense-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vergesense-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vergesense-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vergesense-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vergesense-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/vergesense-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vergesense-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vergesense-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vergesense-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vergesense-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vergesense-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
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
image: https://www.vergesense.com/hubfs/assets/logo/vergesense-logo--color.png
layout: provider
mcp_servers:
- description: ''
  name: VergeSense MCP Server
  slug: vergesense-mcp-server
modified: '2026-09-02'
name: VergeSense
nav: Providers
network: true
overview: 'VergeSense publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Occupancy Intelligence, Workplace Analytics, Corporate Real Estate, PropTech, and IoT Sensors.


  The VergeSense catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VergeSense''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, signup flow, and 27 more developer resources.'
plans:
- name: Vergesense Plans Pricing
  plan_count: 0
  slug: vergesense-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Vergesense Rate Limits
  slug: vergesense-rate-limits
scopes:
- name: Vergesense Scopes
  scope_count: 0
  slug: vergesense-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 63.6
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 52.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Vergesense Authentication
  slug: vergesense-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Vergesense Domain Security
  slug: vergesense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
- Webhooks
- MCP
- JSON:API
website: https://www.vergesense.com/
---
